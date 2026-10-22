import argparse
import contextlib
import importlib.util
import io
import os
from pathlib import Path
import subprocess
import sys
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "cache_metrics.py"
spec = importlib.util.spec_from_file_location("cache_metrics", SCRIPT)
cm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cm)

POOL = "memcache_get_requests_total 10\nmemcache_get_successes_total 10\n"


def sample(engine, queries, hits, local_queries=None, local_hits=0):
    local_queries = queries if local_queries is None else local_queries
    return cm.parse_metrics(
        f'vllm:external_prefix_cache_queries_total{{engine="{engine}"}} {queries}\n'
        f'vllm:external_prefix_cache_hits_total{{engine="{engine}"}} {hits}\n'
        f'vllm:prefix_cache_queries_total{{engine="{engine}"}} {local_queries}\n'
        f'vllm:prefix_cache_hits_total{{engine="{engine}"}} {local_hits}\n'
    )


def stats(sources, pool=POOL, timestamp=1):
    return cm.build_stats({"ts": timestamp, "mc": cm.parse_metrics(pool),
                           "vllm": cm.merge_vllm(sources)})


class MetricsTests(unittest.TestCase):
    def setUp(self):
        self.saved_urls = cm.urls_arg.copy()

    def tearDown(self):
        cm.urls_arg.clear()
        cm.urls_arg.update(self.saved_urls)

    def test_nonfinite_and_negative_counters_rejected(self):
        for value in ('NaN', '+Inf', '-Inf', '-1'):
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, 'Invalid metric'):
                    cm.parse_metrics('vllm:prefix_cache_queries_total ' + value)

    def test_invalid_endpoint_options_fail_before_fetch(self):
        cases = [
            ['--pool', 'localhost:no'], ['--pool-port', '0'],
            ['--pool', 'localhost:7000', '--pool-port', '7000'],
            ['--vllm-port', '65536'],
            ['--vllm', 'localhost:8000', '--vllm-host', 'localhost'],
            ['--pool-host', 'http://localhost'],
        ]
        for flags in cases:
            with self.subTest(flags=flags), patch.object(sys, 'argv', [str(SCRIPT), *flags]), \
                    patch.object(cm, 'snapshot') as collect, \
                    contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit) as error:
                    cm.main()
                self.assertEqual(error.exception.code, 2)
                collect.assert_not_called()

    def test_weighted_total_and_engine_detail(self):
        s = stats([("a", sample(0, 100, 90)), ("b", sample(1, 900, 90))])
        self.assertEqual(cm.pct(s["ext_h"], s["ext_q"]), 18)
        self.assertEqual(len(s["ext_q_by_eng"]), 2)
        self.assertTrue(s["token_available"])

    def test_shared_exporter_rejected(self):
        with self.assertRaisesRegex(ValueError, "重复"):
            cm.merge_vllm([("a", sample(0, 100, 90)), ("b", sample(0, 100, 90))])

    def test_failed_endpoint_does_not_become_zero(self):
        cm.urls_arg.update(pool="pool", vllm_urls=["a", "b"])

        def fake(url):
            if url == "b":
                raise TimeoutError("offline")
            return cm.parse_metrics(POOL) if url == "pool" else sample(0, 100, 90)

        with patch.object(cm, "fetch", side_effect=fake):
            with self.assertRaisesRegex(RuntimeError, "b"):
                cm.snapshot()

    def test_empty_pool_is_not_zero(self):
        cm.urls_arg.update(pool="pool", vllm_urls=["a"])
        with patch.object(cm, "fetch", side_effect=lambda u: {} if u == "pool" else sample(0, 1, 0)):
            with self.assertRaisesRegex(RuntimeError, "memcache"):
                cm.snapshot()

    def test_port_ranges_and_single_endpoint(self):
        self.assertEqual(cm.parse_ports("8000-8007"), list(range(8000, 8008)))
        self.assertEqual(cm.parse_ports("8000,8002-8003,8000"), [8000, 8002, 8003])
        for invalid in ["8007-8000", "0", "65536", "a", "1-300"]:
            with self.assertRaises(argparse.ArgumentTypeError):
                cm.parse_ports(invalid)
        self.assertEqual(stats([("a", sample(0, 100, 90))])["ext_h"], 90)

    def test_distinct_denominators_and_successful_gets(self):
        s = stats([("a", sample(0, 800, 700, local_queries=1000, local_hits=200))])
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            cm.print_overview(s)
        lines = output.getvalue().splitlines()
        for label, expected in [("HBM命中/全部查询", "20.00%"),
                                ("池命中/全部查询", "70.00%"),
                                ("总前缀复用/全部查询", "90.00%"),
                                ("池命中/外部查询", "87.50%")]:
            self.assertIn(expected, next(line for line in lines if label in line))
        self.assertEqual(s["get_ok"], s["get_req"])

    def test_missing_token_metrics_are_unavailable(self):
        samples = sample(0, 800, 700)
        del samples[("vllm:prefix_cache_hits_total", 'engine="0"')]
        s = stats([("a", samples)])
        self.assertFalse(s["token_available"])
        self.assertEqual(cm.rate_text(0, 0), "N/A")

    def test_exist_only_is_not_no_requests(self):
        s = stats([("a", sample(0, 0, 0))], pool="memcache_exist_key_requests_total 5\n")
        self.assertIn("仅 exist", cm.detect_scene(s))

    def test_rewarm_is_not_ssd_read_count(self):
        s = stats([("a", sample(0, 10, 9))], pool=(
            "memcache_query_requests_total 100\nmemcache_query_hit_keys_total 90\n"
            "memcache_rewarm_total 10\nmemcache_rewarm_failed_total 1\n"))
        self.assertEqual(cm.medium_rate(s, "ssd"), "N/A")
        self.assertEqual(s["ssd_hit"], 0)
        s = stats([("a", sample(0, 10, 9))], pool=POOL + (
            "memcache_get_hits_dram_total 6\nmemcache_get_hits_ssd_total 4\n"))
        self.assertEqual(cm.medium_rate(s, "ssd"), "40.00%")

    def test_one_rank_reset_is_not_masked_by_another(self):
        before = stats([("a", sample(0, 100, 50)), ("b", sample(1, 100, 50))])
        after = stats([("a", sample(0, 0, 0)), ("b", sample(1, 300, 150))], timestamp=2)
        with self.assertRaisesRegex(ValueError, "回退"):
            cm.diff_stats(before, after)

    def test_changed_series_invalidates_window(self):
        before = stats([("a", sample(0, 100, 50))])
        after = stats([("a", sample(1, 200, 100))], timestamp=2)
        with self.assertRaisesRegex(ValueError, "集合"):
            cm.diff_stats(before, after)

    def test_window_uses_deltas_not_history(self):
        before = stats([("a", sample(0, 100, 50))])
        after = stats([("a", sample(0, 300, 230))], timestamp=11)
        d = cm.diff_stats(before, after)
        self.assertEqual(cm.pct(d["ext_h"], d["ext_q"]), 90)
        self.assertEqual(d["win"], 10)

    def test_loop_stops_on_keyboard_interrupt(self):
        snap = {"ts": 1, "mc": cm.parse_metrics(POOL), "vllm": sample(0, 100, 90)}
        with patch.object(sys, "argv", [str(SCRIPT), "--loop", "1"]), \
                patch.object(cm, "snapshot", return_value=snap), \
                patch.object(cm.time, "sleep", side_effect=KeyboardInterrupt), \
                contextlib.redirect_stdout(io.StringIO()) as output:
            self.assertEqual(cm.main(), 0)
        self.assertIn("已停止", output.getvalue())


class HttpTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.paths = []

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                cls.paths.append(self.path)
                if self.path.startswith("/bad/"):
                    self.send_error(503)
                    return
                if self.path == "/pool/metrics":
                    body = POOL
                else:
                    engine = 0 if self.path.startswith("/a/") else 1
                    body = "\n".join(
                        '%s{%s} %s' % (name, labels, value)
                        for (name, labels), value in sample(engine, 100, 90).items())
                    if self.path == "/metrics":
                        body = POOL + body
                self.send_response(200)
                self.end_headers()
                self.wfile.write(body.encode())

            def log_message(self, *_args):
                pass

        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def test_read_only_http_snapshot_and_failure(self):
        base = "http://127.0.0.1:%d" % self.server.server_port
        with patch.dict(cm.urls_arg, {"pool": base + "/pool/metrics",
                                     "vllm_urls": [base + "/a/metrics", base + "/b/metrics"]}):
            s = cm.build_stats(cm.snapshot())
            self.assertEqual(s["ext_h"], 180)
            self.assertEqual(s["ext_q"], 200)
            cm.urls_arg["vllm_urls"] = [base + "/bad/metrics"]
            with self.assertRaisesRegex(RuntimeError, "503"):
                cm.snapshot()
        self.assertTrue(all(path.endswith("/metrics") for path in self.paths))

    def test_cli_snapshot_and_window(self):
        endpoint = "127.0.0.1:%d" % self.server.server_port
        for flags, expected in [([], "90.00%"), (["--window", "1"], "零增量")]:
            with self.subTest(flags=flags):
                p = subprocess.run([sys.executable, str(SCRIPT), "--pool", endpoint,
                                    "--vllm", endpoint, "--timeout", "2", *flags],
                                   env=dict(os.environ, PYTHONIOENCODING="utf-8"),
                                   capture_output=True, text=True, encoding="utf-8", timeout=8)
                self.assertEqual(p.returncode, 0, p.stderr)
                self.assertIn(expected, p.stdout)


if __name__ == "__main__":
    unittest.main()
