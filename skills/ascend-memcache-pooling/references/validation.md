# Controlled hit-rate and performance validation

Use this procedure when the user asks for a measured target. It supplements [deployment validation](deployment.md#validate-the-selected-route); it does not impose a fixed model, topology, hit rate or latency threshold on every deployment.

## Freeze the comparison

Record model/weights and tokenizer revisions, chat template, raw and internal prompt tokens, output length, block size, full connector flags, APC setting, DP/TP, prefix count, request count, concurrency C, request rate RR, seeds, dataset hashes and warmup boundaries. The same prefix data and suffix-generation rules must drive OFF and ON. Prefix count equal to C is a task-specific constraint when requested, not a universal optimum. A repeat-rate UI value is a data-generation parameter, not measured external token reuse.

Define OFF precisely: disabling history reuse while preserving direct P-to-D transfer is different from disabling only the external store while keeping HBM APC, and different again from comparing DRAM-only to SSD-enabled. Use the user's required baseline. If the task requires APC on for both sides, retain it and measure HBM independently; do not silently disable it to improve an external-hit number.

Prewrite/seed and warmup are separate from formal measurement. Use fresh suffixes with shared block-aligned prefixes and account for routing across all DP engines. Preserve per-request outputs, success/failure counts, engine coverage, counter deltas and native benchmark output. No claims from unfinished or failed rounds.

## Make external reuse observable

HBM may satisfy repeated prefixes before the pool is queried. Estimate the actual KV prefix footprint from model layout, block allocation and observed per-engine capacity; raw text/token length alone is insufficient for hybrid KV. Increase distinct prefix working set, rotate prefixes with fresh suffixes, or use supported routing to another compatible instance before shrinking DRAM. Enlarging the prefix count raises the working set, not the mathematical repeat ratio; re-freeze both sides if that count changes.

If a targeted HBM reset is needed, inspect the installed API, affected instances and pending work first. Apply only within user authorization and outside active measurements. A pool-wide `remove_all()` or `DELETE /all_keys` affects stored keys and is not an HBM-only reset; do not execute it as a monitor feature or silently initialize the disk. Disabling APC may also disable external lookup in a selected implementation, so inspect the connector path before suggesting that shortcut.

Measure the P-side historical HBM hits, external hits and external query coverage independently. In P/D, a D-side external counter can represent newly received remote KV. It is not proof of a historical pool hit. For a requested approximately 90% pool-token reuse target, use external-hit tokens divided by the declared full prompt-query denominator, not successful gets or a conditional external lookup rate. Report combined reuse separately.

## Exercise SSD without inventing a percentage

Size MemCache DRAM from the actual prefix set and preserve allocation headroom. Record per-owner DRAM, owner count, high/low eviction thresholds and additional UBSIO memory. Change DRAM or supported watermarks only within authorized tuning bounds, explaining the current-to-proposed values, release support and resource implications. Use a new configuration/attempt hash.

After a successful write, create enough controlled pressure for the relevant prefixes to leave HBM and MemCache DRAM, then read them through the actual inference path. Distinguish MemCache DRAM, UBSIO L2.5 host cache and physical SSD. Require successful reads and consumed KV, plus physical-read evidence tied to the identified device. SSD occupancy, query/exist successes, flushing and rewarming alone are insufficient. State N/A if the release cannot expose the requested attribution; do not turn an unsupported counter into zero or invent a minimum SSD share.

## Tune latency and throughput together

Declare whether the user means mean, P90 or another quantile and use the same definition for OFF/ON. Report TTFT and TPOT from successful formal request intervals; output length one has no meaningful TPOT. Match warmup, stable-window selection, time units and hardware/transport topology. A missing matching baseline remains missing.

For example, when the task requires TTFT <7s, TPOT <20ms and steady input-TPS ON/OFF >=5, all three must be checked on the matched workload. These example thresholds are user-supplied acceptance criteria, not verified results. If a probe fails, adjust C or a positive RR within a bounded search; freeze the selected setting and rerun both OFF and ON with identical C/RR/prefix count/data/flags. Lowering arrival rate can improve latency while reducing offered load; that alone proves no capacity gain. An invalid steady window is not a steady throughput result. Preserve full-run auxiliary results without relabeling them as stable acceptance.

Stop an attempt on first substantive transport, allocation, correctness or resource-ownership failure. Retain the first error and owned process identities before an authorized retry; do not repair by resetting devices, changing transport/topology, force-initializing storage or terminating another user's process.
