# -*- coding: utf-8 -*-
"""Read-only MemCache/vLLM Prometheus monitor; Python standard library only.

Single endpoint, repeated --vllm endpoints, or --vllm-host/--vllm-ports ranges.
--loop prints cumulative snapshots; --window prints one interval then exits.
See ../references/monitoring.md for denominator and SSD evidence boundaries.
"""
import argparse
import math
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.request import ProxyHandler, build_opener

DEFAULT_POOL_HOST = "127.0.0.1"
DEFAULT_POOL_PORT = 7000
DEFAULT_VLLM_HOST = "127.0.0.1"
DEFAULT_VLLM_PORT = 8000

SAMPLE_RE = re.compile(r'^(?P<name>[a-zA-Z_:][a-zA-Z0-9_:]*)(\{(?P<labels>[^}]*)\})?\s+(?P<value>[^\s]+)')

W = 104  # 报表总宽

COUNTER_KEYS = [
    "q_req", "q_hit", "q_nf", "exist_req", "exist_ok", "exist_nf",
    "get_req", "get_ok", "get_nf", "get_hits_dram", "get_hits_ssd",
    "rewarm", "rewarm_fail", "rewarm_bytes",
    "flush_blobs", "flush_bytes", "evict", "alloc", "alloc_fail",
    "ext_q", "ext_h", "loc_q", "loc_h",
]


# ---------------------------------------------------------------- 基础工具
def disp_width(s):
    w = 0
    for ch in s:
        w += 2 if ('\u4e00' <= ch <= '\u9fff' or '\u3000' <= ch <= '\u303f' or ch in '◆▣→±') else 1
    return w


def pad(s, width, align="left"):
    gap = width - disp_width(s)
    if gap <= 0:
        return s
    return " " * gap + s if align == "right" else s + " " * gap


def fmt_num(v):
    return "{:,}".format(int(round(v)))


def fmt_bytes(v):
    v = float(v)
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:
        if v < 1024 or unit == 'PB':
            return "%.2f%s" % (v, unit)
        v /= 1024.0


def pct(a, b):
    return 100.0 * a / b if b else 0.0


def bar(p, width=20):
    filled = int(round(p / 100.0 * width))
    return "[" + "#" * filled + "." * (width - filled) + "]"


def eng_name(lab):
    m = re.search(r'engine="([^"]+)"', lab)
    return m.group(1) if m else lab


def detect_scene(s):
    """根据计数器数据自动识别命中路径(无入参, 纯数据判断):
       layerwise 只走 query; 非 layerwise 走 exist+get; 两者兼有时以规模大者为主"""
    q, g = s["q_req"], s["get_req"]
    if q == 0 and g == 0:
        if s["exist_req"] > 0:
            return "仅 exist 探测，尚无 query/get"
        return "无请求"
    if q > 0 and g == 0:
        return "layerwise(query)"
    if g > 0 and q == 0:
        return "非layerwise(exist+get)"
    return "layerwise为主(query)" if q >= g else "非layerwise为主(get)"


def med_view(s):
    """Only explicit get-by-medium counters identify read media."""
    if s["get_req"] > 0 and s.get("medium_available", False):
        return "get", s["get_ok"]
    return "未提供介质读计数", 0


def rate_text(hits, queries, available=True):
    return "%.2f%%" % pct(hits, queries) if available and queries > 0 else "N/A"


def medium_rate(s, medium):
    _, denominator = med_view(s)
    return rate_text(s[medium + "_hit"], denominator, s.get("medium_available", False))


# ---------------------------------------------------------------- 采集
def parse_metrics(text):
    out = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        m = SAMPLE_RE.match(line)
        if not m:
            continue
        try:
            val = float(m.group('value'))
        except ValueError:
            continue
        if not math.isfinite(val) or (m.group('name').endswith('_total') and val < 0):
            raise ValueError('Invalid metric sample: %s' % m.group('name'))
        out[(m.group('name'), m.group('labels') or '')] = val
    return out


def fetch(url, timeout=None):
    timeout = timeout if timeout is not None else urls_arg.get("timeout", 15)
    # Metrics usually live on private networks; do not route through shell proxies.
    with build_opener(ProxyHandler({})).open(url, timeout=timeout) as response:
        return parse_metrics(response.read().decode("utf-8"))


def series(samples, name):
    return {lab: v for (n, lab), v in samples.items() if n == name}


def total_of(samples, name):
    return sum(series(samples, name).values())


def parse_ports(value):
    """Ordered, unique ports, e.g. 8000-8007 or 8000,8002."""
    ports = []
    try:
        for part in value.split(","):
            bounds = part.strip().split("-")
            if len(bounds) not in (1, 2):
                raise ValueError()
            low, high = int(bounds[0]), int(bounds[-1])
            if not 1 <= low <= high <= 65535 or high - low > 255:
                raise ValueError()
            for port in range(low, high + 1):
                if port not in ports:
                    ports.append(port)
        if not ports or len(ports) > 256:
            raise ValueError()
    except ValueError:
        raise argparse.ArgumentTypeError("端口须为 1..65535，最多256个，例如 8000-8007")
    return ports


def merge_vllm(sources):
    """Reject overlapping engine sets: never double-count shared exporters."""
    merged, owners = {}, {}
    for url, samples in sources:
        selected = {k: v for k, v in samples.items() if k[0].startswith("vllm:")}
        if not selected:
            raise ValueError("%s 未返回 vLLM 指标，本轮不输出汇总" % url)
        engines = {m.group(1) for (_, lab) in selected
                   for m in [re.search(r'engine="([^"]+)"', lab)] if m}
        if len(sources) > 1 and not engines:
            raise ValueError("%s 缺少 engine 标签，无法安全汇总" % url)
        for engine in engines:
            if engine in owners:
                raise ValueError("engine %s 同时来自 %s 和 %s；拒绝重复计算"
                                 % (engine, owners[engine], url))
            owners[engine] = url
        for (name, lab), value in selected.items():
            # Retain source identity for unlabeled series and per-engine detail.
            tag = 'scrape_endpoint="%s"' % url
            merged[(name, lab + ("," if lab else "") + tag)] = value
    return merged


def snapshot():
    endpoints = urls_arg["vllm_urls"]
    results, errors = {}, []
    with ThreadPoolExecutor(max_workers=min(16, len(endpoints) + 1)) as executor:
        jobs = {executor.submit(fetch, url): (kind, url)
                for kind, url in [("pool", urls_arg["pool"])] +
                [("vllm", url) for url in endpoints]}
        for job in as_completed(jobs):
            kind, url = jobs[job]
            try:
                results[(kind, url)] = job.result()
            except Exception as exc:
                errors.append("%s %s: %s" % (kind, url, exc))
    if errors:
        raise RuntimeError("采集不完整，本轮不输出汇总；" + "; ".join(errors))
    pool = results[("pool", urls_arg["pool"])]
    if not any(name.startswith("memcache_") for name, _ in pool):
        raise RuntimeError("池端点未返回 memcache 指标（可能为空响应），本轮不输出汇总")
    vllm = merge_vllm([(url, results[("vllm", url)]) for url in endpoints])
    return {"ts": time.time(), "mc": pool, "vllm": vllm}


urls_arg = {}  # 运行期由 main() 填充


def build_stats(snap):
    """提取关注指标(累计值)"""
    mc, vllm = snap["mc"], snap["vllm"]

    def m(name):
        return total_of(mc, name)

    def v(name):
        return total_of(vllm, name)

    caps = series(mc, 'memcache_total_capacity_bytes')
    allocs = series(mc, 'memcache_allocated_bytes')

    s = {"ts": snap["ts"]}
    s["q_req"] = m('memcache_query_requests_total')
    s["q_hit"] = m('memcache_query_hit_keys_total')
    s["q_nf"] = m('memcache_query_not_found_total')
    s["exist_req"] = m('memcache_exist_key_requests_total')
    s["exist_ok"] = m('memcache_exist_key_successes_total')
    s["exist_nf"] = m('memcache_exist_key_not_found_total')
    s["get_req"] = m('memcache_get_requests_total')
    s["get_ok"] = m('memcache_get_successes_total')
    s["get_nf"] = m('memcache_get_not_found_total')
    s["rewarm"] = m('memcache_rewarm_total')
    s["rewarm_fail"] = m('memcache_rewarm_failed_total')
    s["rewarm_bytes"] = m('memcache_rewarm_bytes_total')
    s["rewarm_cur"] = m('memcache_rewarm_bytes_current')
    s["flush_blobs"] = m('memcache_flush_blobs_total')
    s["flush_bytes"] = m('memcache_flush_bytes_total')
    s["evict"] = m('memcache_evict_operations_total')
    s["alloc"] = m('memcache_alloc_requests_total')
    s["alloc_fail"] = m('memcache_alloc_failures_total')
    s["stored_keys"] = m('memcache_stored_keys')
    s["get_hits_dram"] = m('memcache_get_hits_dram_total')
    s["get_hits_ssd"] = m('memcache_get_hits_ssd_total')
    s["dram_cap"] = caps.get('medium="dram"', 0)
    s["dram_alloc"] = allocs.get('medium="dram"', 0)
    s["ssd_cap"] = caps.get('medium="ssd"', 0)
    s["ssd_alloc"] = allocs.get('medium="ssd"', 0)

    s["medium_available"] = all(series(mc, name) for name in (
        "memcache_get_hits_dram_total", "memcache_get_hits_ssd_total"))
    s["ssd_hit"] = s["get_hits_ssd"]
    s["dram_hit"] = s["get_hits_dram"]

    s["ext_q"] = v('vllm:external_prefix_cache_queries_total')
    s["ext_h"] = v('vllm:external_prefix_cache_hits_total')
    s["loc_q"] = v('vllm:prefix_cache_queries_total')
    s["loc_h"] = v('vllm:prefix_cache_hits_total')
    s["ext_q_by_eng"] = series(vllm, 'vllm:external_prefix_cache_queries_total')
    s["ext_h_by_eng"] = series(vllm, 'vllm:external_prefix_cache_hits_total')
    s["kv_usage"] = series(vllm, 'vllm:kv_cache_usage_perc')
    required = ("vllm:prefix_cache_queries_total", "vllm:prefix_cache_hits_total",
                "vllm:external_prefix_cache_queries_total", "vllm:external_prefix_cache_hits_total")
    query_labels = set(s["ext_q_by_eng"])
    s["token_available"] = bool(query_labels) and all(
        set(series(vllm, name)) == query_labels for name in required)
    # Validate raw counter series before aggregation: one restarted rank can be
    # hidden by another rank's increasing counters.
    s["raw_counters"] = {
        (source, name, labels): value
        for source, samples in (("pool", mc), ("vllm", vllm))
        for (name, labels), value in samples.items() if name.endswith("_total")
    }
    return s


def diff_stats(s0, s1):
    before, after = s0["raw_counters"], s1["raw_counters"]
    if before.keys() != after.keys():
        raise ValueError("窗口内计数器集合发生变化，本窗口无效；重新打点")
    if any(after[key] < before[key] for key in before):
        raise ValueError("窗口内计数器回退（可能重启/reset），本窗口无效；重新打点")
    d = {"ts": s1["ts"], "win": s1["ts"] - s0["ts"], "reset": []}
    for k in COUNTER_KEYS:
        d0, d1 = s0.get(k, 0), s1.get(k, 0)
        delta = d1 - d0
        if delta < 0:
            delta = 0
            d["reset"].append(k)
        d[k] = delta
    d["ssd_hit"] = d["get_hits_ssd"]
    d["dram_hit"] = d["get_hits_dram"]
    d["medium_available"] = s0["medium_available"] and s1["medium_available"]
    d["token_available"] = s0["token_available"] and s1["token_available"]
    d["dram_cap"] = s1["dram_cap"]
    d["dram_alloc"] = s1["dram_alloc"]
    d["ssd_cap"] = s1["ssd_cap"]
    d["ssd_alloc"] = s1["ssd_alloc"]
    d["stored_keys"] = s1["stored_keys"]
    d["rewarm_cur"] = s1["rewarm_cur"]
    d["kv_usage"] = s1["kv_usage"]
    d["ext_q_by_eng"] = {lab: max(s1["ext_q_by_eng"].get(lab, 0) - s0["ext_q_by_eng"].get(lab, 0), 0)
                         for lab in s1["ext_q_by_eng"]}
    d["ext_h_by_eng"] = {lab: max(s1["ext_h_by_eng"].get(lab, 0) - s0["ext_h_by_eng"].get(lab, 0), 0)
                         for lab in s1["ext_h_by_eng"]}
    return d


# ---------------------------------------------------------------- 报表
def print_vllm_summary(s):
    available = s["token_available"]
    rows = [
        ("HBM命中/全部查询", s["loc_h"], s["loc_q"]),
        ("池命中/全部查询", s["ext_h"], s["loc_q"]),
        ("总前缀复用/全部查询", s["loc_h"] + s["ext_h"], s["loc_q"]),
        ("池命中/外部查询", s["ext_h"], s["ext_q"]),
    ]
    for label, hits, queries in rows:
        print("  " + pad(label, 26) + pad(rate_text(hits, queries, available), 12, "right")
              + "   %s / %s (tokens)" % (fmt_num(hits), fmt_num(queries)))
    if not available:
        print("  [!] 缺少完整、同标签的四项前缀计数器，token命中率不可用；缺失项不作真0")
    print("  [分 engine 池命中/外部查询]")
    for lab in sorted(s["ext_q_by_eng"]):
        queries = s["ext_q_by_eng"][lab]
        hits = s["ext_h_by_eng"].get(lab, 0)
        print("    engine %s  %s  查询 %s  命中 %s"
              % (eng_name(lab), rate_text(hits, queries, lab in s["ext_h_by_eng"]),
                 fmt_num(queries), fmt_num(hits)))


def print_overview(s):
    print("")
    print("  ▣ 总览 (token复用与读取介质分别统计)")
    print("  " + "─" * (W - 4))
    print_vllm_summary(s)
    print("  " + pad("DRAM占成功get读取", 26) + pad(medium_rate(s, "dram"), 12, "right"))
    print("  " + pad("SSD占成功get读取", 26) + pad(medium_rate(s, "ssd"), 12, "right"))
    if not s["medium_available"] or s["get_req"] == 0:
        print("  读取介质比例 N/A；query/exist/rewarm 不能替代SSD成功读取计数")


def print_window_report(d):
    win = d["win"] or 1
    print("")
    print("═" * W)
    print("  ❖ Prefix Cache 池化系统 · 窗口增量统计    窗口: %s → %s  (%.0fs)"
          % (time.strftime("%H:%M:%S", time.localtime(d["ts"] - win)),
             time.strftime("%H:%M:%S", time.localtime(d["ts"])), win))
    print("═" * W)
    if d["reset"]:
        print("  [!] 计数器回退(可能重启), 已按0处理: %s" % ", ".join(d["reset"]))

    # ---- 总览 ----
    print_overview(d)
    if (d["q_req"] + d["exist_req"] + d["get_req"] + d["ext_q"] + d["loc_q"]) == 0:
        print("  [!] 窗口内无任何新请求(各计数器零增量), 当前系统空闲; 上方累计大数均为历史值")

    # ---- 池化系统 详细 ----
    print("")
    print("  ▣ 来源一: MemCache 池化系统   (%s)" % urls_arg["pool"])
    print("  " + "─" * (W - 4))
    scene = detect_scene(d)
    med_name, med_denom = med_view(d)
    ex_rate = pct(d["exist_ok"], d["exist_req"])
    get_rate = pct(d["get_ok"], d["get_req"])
    q_rate = pct(d["q_hit"], d["q_req"])
    print("  " + pad("命中场景", 26) + pad(scene, 20, "right"))
    print("  " + pad("query 命中率", 26) + pad("%.2f%%" % q_rate, 12, "right")
          + "   命中 %s / 查询 %s / 未命中 %s" % (fmt_num(d["q_hit"]), fmt_num(d["q_req"]), fmt_num(d["q_nf"])))
    print("  " + pad("exist 探测存活率", 26) + pad("%.2f%%" % ex_rate, 12, "right")
          + "   命中 %s / 探测 %s / 未找到 %s" % (fmt_num(d["exist_ok"]), fmt_num(d["exist_req"]), fmt_num(d["exist_nf"])))
    print("  " + pad("get 读取成功率", 26) + pad("%.2f%%" % get_rate, 12, "right")
          + "   命中 %s / 读取 %s" % (fmt_num(d["get_ok"]), fmt_num(d["get_req"])))
    print("  " + pad("DRAM占成功读取(%s)" % med_name, 26) + pad(medium_rate(d, "dram"), 12, "right")
          + "   命中 %s" % fmt_num(d["dram_hit"]))
    print("  " + pad("SSD占成功读取(%s)" % med_name, 26) + pad(medium_rate(d, "ssd"), 12, "right")
          + "   命中 %s   回暖 %s" % (fmt_num(d["ssd_hit"]), fmt_bytes(d["rewarm_bytes"])))
    print("  " + pad("alloc 请求/失败", 26) + pad("%s / %s" % (fmt_num(d["alloc"]), fmt_num(d["alloc_fail"])), 12, "right"))
    print("  " + pad("flush 次数/流量", 26) + pad("%s / %s" % (fmt_num(d["flush_blobs"]), fmt_bytes(d["flush_bytes"])), 12, "right"))
    print("  " + pad("淘汰次数", 26) + pad(fmt_num(d["evict"]), 12, "right"))
    print("  " + pad("存储对象数(快照)", 26) + pad(fmt_num(d["stored_keys"]), 12, "right"))
    print("  " + pad("DRAM 容量占用", 26) + pad("%.1f%%" % pct(d["dram_alloc"], d["dram_cap"]), 12, "right")
          + "   %s / %s" % (fmt_bytes(d["dram_alloc"]), fmt_bytes(d["dram_cap"])))
    print("  " + pad("SSD 容量占用", 26) + pad("%.1f%%" % pct(d["ssd_alloc"], d["ssd_cap"]), 12, "right")
          + "   %s / %s" % (fmt_bytes(d["ssd_alloc"]), fmt_bytes(d["ssd_cap"])))
    print("  " + pad("回暖进行中", 26) + pad(fmt_bytes(d["rewarm_cur"]), 12, "right"))

    # ---- vllm 详细 ----
    print("")
    print("  ▣ 来源二: vLLM 推理引擎      (%s)" % urls_arg["vllm"])
    print("  " + "─" * (W - 4))
    print_vllm_summary(d)
    print("  [KV Cache 使用率快照]")
    for lab, v in sorted(d["kv_usage"].items()):
        print("    engine %s  %5.1f%%  %s" % (eng_name(lab), v * 100, bar(v * 100, 24)))
    print("═" * W)


def print_instant_report(s1):
    print("═" * W)
    print("  ❖ Prefix Cache 池化系统 · 瞬时累计报表    时间: %s"
          % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(s1["ts"])))
    print("═" * W)

    # ---- 总览 ----
    print_overview(s1)

    # ---- 池化系统 详细 ----
    print("")
    print("  ▣ 来源一: MemCache 池化系统   (%s)" % urls_arg["pool"])
    print("  " + "─" * (W - 4))
    scene = detect_scene(s1)
    med_name, med_denom = med_view(s1)
    ex_rate = pct(s1["exist_ok"], s1["exist_req"])
    get_rate = pct(s1["get_ok"], s1["get_req"])
    q_rate = pct(s1["q_hit"], s1["q_req"])
    print("  " + pad("命中场景", 26) + pad(scene, 20, "right"))
    print("  " + pad("query 命中率", 26) + pad("%.2f%%" % q_rate, 12, "right")
          + "   命中 %s / 查询 %s / 未命中 %s" % (fmt_num(s1["q_hit"]), fmt_num(s1["q_req"]), fmt_num(s1["q_nf"])))
    print("  " + pad("exist 探测存活率", 26) + pad("%.2f%%" % ex_rate, 12, "right")
          + "   命中 %s / 探测 %s / 未找到 %s" % (fmt_num(s1["exist_ok"]), fmt_num(s1["exist_req"]), fmt_num(s1["exist_nf"])))
    print("  " + pad("get 读取成功率", 26) + pad("%.2f%%" % get_rate, 12, "right")
          + "   命中 %s / 读取 %s" % (fmt_num(s1["get_ok"]), fmt_num(s1["get_req"])))
    print("  " + pad("DRAM占成功读取(%s)" % med_name, 26) + pad(medium_rate(s1, "dram"), 12, "right")
          + "   命中 %s" % fmt_num(s1["dram_hit"]))
    print("  " + pad("SSD占成功读取(%s)" % med_name, 26) + pad(medium_rate(s1, "ssd"), 12, "right")
          + "   命中 %s  回暖累计 %s" % (fmt_num(s1["ssd_hit"]), fmt_bytes(s1["rewarm_bytes"])))
    print("  " + pad("alloc 请求/失败", 26) + pad("%s / %s" % (fmt_num(s1["alloc"]), fmt_num(s1["alloc_fail"])), 12, "right"))
    print("  " + pad("flush 次数/流量", 26) + pad("%s / %s" % (fmt_num(s1["flush_blobs"]), fmt_bytes(s1["flush_bytes"])), 12, "right"))
    print("  " + pad("淘汰次数", 26) + pad(fmt_num(s1["evict"]), 12, "right"))
    print("  " + pad("存储对象数", 26) + pad(fmt_num(s1["stored_keys"]), 12, "right"))
    print("  " + pad("DRAM 容量占用", 26) + pad("%.1f%%" % pct(s1["dram_alloc"], s1["dram_cap"]), 12, "right")
          + "   %s / %s" % (fmt_bytes(s1["dram_alloc"]), fmt_bytes(s1["dram_cap"])))
    print("  " + pad("SSD 容量占用", 26) + pad("%.1f%%" % pct(s1["ssd_alloc"], s1["ssd_cap"]), 12, "right")
          + "   %s / %s" % (fmt_bytes(s1["ssd_alloc"]), fmt_bytes(s1["ssd_cap"])))
    print("  " + pad("回暖进行中", 26) + pad(fmt_bytes(s1["rewarm_cur"]), 12, "right"))

    # ---- vllm 详细 ----
    print("")
    print("  ▣ 来源二: vLLM 推理引擎      (%s)" % urls_arg["vllm"])
    print("  " + "─" * (W - 4))
    print_vllm_summary(s1)
    print("═" * W)


# ---------------------------------------------------------------- 预留: mooncake
def build_stats_mooncake(snap):
    """mooncake 池化系统指标提取 (预留, 待 mooncake metric 接入后对齐指标名)"""
    # mooncake 的 metrics 暴露形如:
    #   mooncake_store_get_hits_total / mooncake_store_put_... 等
    # 接入时在此解析并返回与 build_stats 同构的 dict 即可复用报表
    raise NotImplementedError("mooncake 指标尚未接入")


def run_window_once(window_s):
    """窗口模式: 开始打点 -> 等待窗口 -> 结束打点 -> 输出增量报表 -> 退出"""
    print("窗口模式: 打点开始(%s), 等待 %gs 后结束打点并输出统计..."
          % (time.strftime("%H:%M:%S"), window_s))
    prev = build_stats(snapshot())
    time.sleep(window_s)
    cur = build_stats(snapshot())
    print_window_report(diff_stats(prev, cur))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--window', type=int, default=0, help='窗口秒数(如60), 打点一次后退出')
    ap.add_argument('--loop', type=int, default=0, help='瞬时报表刷新间隔秒数')
    ap.add_argument('--pool', default=None, help='MemCache指标地址 host:port')
    ap.add_argument('--vllm', action='append', default=None,
                    help='vLLM 地址 host:port；可重复传入多个不同DP端点')
    ap.add_argument('--pool-host', default=None, help='池化系统主机(与--pool二选一)')
    ap.add_argument('--pool-port', type=int, default=None, help='池化系统端口')
    ap.add_argument('--vllm-host', default=None, help='vLLM 主机')
    ap.add_argument('--vllm-port', type=int, default=None, help='vLLM端口')
    ap.add_argument('--vllm-ports', type=parse_ports, help='同主机多个DP端口，例如8000-8007')
    ap.add_argument('--timeout', type=float, default=15, help='单个HTTP请求超时秒数')
    args = ap.parse_args()
    if args.window and args.loop:
        ap.error('--window 与 --loop 请选择一种模式')
    if args.timeout <= 0 or args.loop < 0 or args.window < 0:
        ap.error('timeout 必须大于0，loop/window 不得为负')
    if args.vllm_ports and (args.vllm or args.vllm_port):
        ap.error('--vllm-ports 不能与 --vllm 或 --vllm-port 同用')
    if args.pool and (args.pool_host is not None or args.pool_port is not None):
        ap.error('--pool 不能与 --pool-host 或 --pool-port 同用')
    if args.vllm and (args.vllm_host is not None or args.vllm_port is not None):
        ap.error('--vllm 不能与 --vllm-host 或 --vllm-port 同用')

    pool_host = DEFAULT_POOL_HOST if args.pool_host is None else args.pool_host
    pool_port = DEFAULT_POOL_PORT if args.pool_port is None else args.pool_port
    vllm_host = DEFAULT_VLLM_HOST if args.vllm_host is None else args.vllm_host
    vllm_port = DEFAULT_VLLM_PORT if args.vllm_port is None else args.vllm_port
    if args.pool:
        if ':' in args.pool:
            h, p = args.pool.rsplit(':', 1)
            try:
                pool_host, pool_port = h, int(p)
            except ValueError:
                ap.error('MemCache端口必须为整数')
        else:
            pool_host, pool_port = args.pool, DEFAULT_POOL_PORT
    for host, port in ((pool_host, pool_port), (vllm_host, vllm_port)):
        if (not host or any(c in host for c in ('/', '"', '\\', '@', ' ', '\n'))
                or not 1 <= port <= 65535):
            ap.error('地址须为有效 host[:port]，端口范围 1..65535')
    if args.vllm:
        endpoints = []
        for address in args.vllm:
            if '://' in address or '/' in address or '"' in address:
                ap.error('--vllm 格式为 host:port，不带协议或路径')
            if ':' in address:
                h, p = address.rsplit(':', 1)
                try:
                    port = int(p)
                except ValueError:
                    ap.error('vLLM端口必须为整数')
            else:
                h, port = address, DEFAULT_VLLM_PORT
            if not h or not 1 <= port <= 65535:
                ap.error('vLLM地址或端口无效')
            endpoints.append("http://%s:%s/metrics" % (h, port))
    else:
        endpoints = ["http://%s:%s/metrics" % (vllm_host, port)
                     for port in (args.vllm_ports or [vllm_port])]
    if len(set(endpoints)) != len(endpoints):
        ap.error('vLLM端点重复')
    urls_arg["pool"] = "http://%s:%s/metrics" % (pool_host, pool_port)
    urls_arg["vllm_urls"] = endpoints
    urls_arg["vllm"] = ", ".join(endpoints)
    urls_arg["timeout"] = args.timeout

    try:
        if args.window > 0:
            run_window_once(args.window)
        elif args.loop > 0:
            while True:
                try:
                    print_instant_report(build_stats(snapshot()))
                except Exception as e:
                    print("[!] 采集失败: %s: %s" % (type(e).__name__, e))
                time.sleep(args.loop)
        else:
            print_instant_report(build_stats(snapshot()))
    except KeyboardInterrupt:
        print("\n已停止")
    except Exception as exc:
        print("[!] 采集失败: %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
