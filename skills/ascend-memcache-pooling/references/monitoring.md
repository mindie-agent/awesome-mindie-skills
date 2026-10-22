# Read-only multi-DP cache monitoring

Run [cache_metrics.py](../scripts/cache_metrics.py) with Python 3.10+; it uses only the standard library. The terminal report is in Chinese. Select the actual MemCache metrics endpoint from the effective config and the actual vLLM API metrics endpoints from launch commands. A proxy port or DP RPC port is not automatically a metrics endpoint. Defaults are localhost examples, not discovered service addresses.

## Commands

From the complete skill directory, for eight independent DP API servers on ports 8000 through 8007:

```bash
python3 scripts/cache_metrics.py --pool <POOL_HOST>:<METRICS_PORT> \
  --vllm-host <INFERENCE_HOST> --vllm-ports 8000-8007 --loop 5
```

`--loop 5` refreshes cumulative snapshots every five seconds. Ctrl+C exits. It does not reset counters. For one 60-second interval, collecting before and after then exiting:

```bash
python3 scripts/cache_metrics.py --pool <POOL_HOST>:<METRICS_PORT> \
  --vllm-host <INFERENCE_HOST> --vllm-ports 8000-8007 --window 60
```

Use repeated `--vllm HOST:PORT` for a selected multi-host endpoint list, or one `--vllm HOST:PORT` for a single exporter that already contains all engines. Comma-separated port lists/ranges are supported. `--timeout 5` bounds each HTTP GET. Loop and window modes are mutually exclusive. The legacy single-port host/port options remain supported.

Verify exporter scope first. Overlapping `engine` IDs across endpoints are rejected to avoid counting one shared multiprocess exporter repeatedly. Independent services with overlapping local engine IDs must be monitored separately; this script does not guess global rank identity. Do not combine P and D token counters into one reuse rate: D external hits may mean received P-to-D KV rather than historical prefix reuse.

## Denominators

All ratios use summed counters, not an average of engine percentages:

| Report | Formula and meaning |
| --- | --- |
| HBM / all queries | `prefix_cache_hits_total / prefix_cache_queries_total` |
| Pool / all queries | `external_prefix_cache_hits_total / prefix_cache_queries_total` |
| Combined reuse / all queries | `(HBM hits + external hits) / prefix_cache_queries_total`; only meaningful for non-overlapping hit semantics |
| Pool / external queries | `external_prefix_cache_hits_total / external_prefix_cache_queries_total`; conditional rate |
| DRAM or SSD / successful gets | explicit `memcache_get_hits_dram_total` or `memcache_get_hits_ssd_total` divided by successful gets; object/read operations, not tokens |

The four required vLLM token counters must have matching label sets. Missing series and zero denominators produce N/A. An endpoint failure or empty exporter invalidates the aggregate instead of being treated as zero. Interval mode rejects changed counter sets or any individual series decrease; another engine's increase cannot mask a reset. Scrapes are concurrent but not atomic, so align interpretation with the workload's actual request boundaries.

Example: total queries 1000, HBM hits 200, external queries 800 and external hits 700 give 20% HBM, 70% pool/all, 90% combined and 87.5% pool/external. A 100% successful-get rate does not change these token ratios. `exist` is key-presence probing; an exist-only path is reported separately from no activity. Confirm the target release's counter units, retries and prompt accounting before comparing to client token counts.

## SSD and performance boundaries

SSD capacity, key count, flush, eviction and rewarm are separate diagnostic values, not SSD-read hits. The script uses explicit get-medium counters only; absent counters or a path bypassing get produce N/A for medium shares. It never estimates SSD hits from rewarm bytes. Other optional operation/capacity fields currently use zero placeholders when absent; those detail values do not establish that an operation did not happen or capacity is zero.

SSD acceptance additionally needs successful version-specific read completion/bytes and device physical-read evidence tied to the controlled request window. For loops, identify the backing file and physical device and account for host page cache and unrelated I/O. Kernel-bypass I/O may require another supported observability source. The script does not collect TTFT/TPOT or certify any SLO.

## Offline regression

```bash
python3 -m unittest discover -s tests -p 'test_cache_metrics.py' -v
python3 scripts/cache_metrics.py --help
```

Tests cover weighted aggregation, exporter overlap, missing series/HTTP failures, reset/label changes, interval deltas, read-only local HTTP collection and CLI behavior. They require no NPU and do not validate remote hardware or SSD performance.
