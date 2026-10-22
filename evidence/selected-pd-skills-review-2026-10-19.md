# Selected PD skills: definition review

- Review date: 2026-10-19.
- Reviewed source: [Yuli-yx/awesome-va-skills](https://github.com/Yuli-yx/awesome-va-skills/tree/8d9f7ee56d088f15a398181590c4512bfc725d6f).
- Source revision: `8d9f7ee56d088f15a398181590c4512bfc725d6f`.
- Inputs inspected: the three complete packages, including definitions,
  references, examples, scripts, license files, source attribution and manifest.
- All three listed packages have MIT notices. The collection contains other
  packages under other licenses; this source record does not relicense them.

## Attribution and package requirements

`aisbench-pd-benchmark` is adapted from
[wangxiaoteng888/vllm-ascend-workspace](https://github.com/wangxiaoteng888/vllm-ascend-workspace/tree/5fba343c1c2b3d896f1273e0ecb9b0581f8128d4/.agents/skills/aisbench-pd-benchmark),
revision `5fba343c1c2b3d896f1273e0ecb9b0581f8128d4`; Git author
`wangxiaoteng`. The source
[MIT license](https://github.com/wangxiaoteng888/vllm-ascend-workspace/blob/5fba343c1c2b3d896f1273e0ecb9b0581f8128d4/LICENSE)
credits Qi Mao and is preserved in the package. Yuli-yx maintains the warmup
load/timing and reporting adaptations. The external application
`rayn-zzz/aisbench_auto_tools_prefix` is a separate dependency, not the author
of the skill. Keep the complete skill and obtain AISBench and that wrapper
separately.

`pd-pure-role-benchmark` is a user-authored workspace workflow maintained by
Yuli-yx, with its MIT notice bundled. Keep the protocol reference, agent
metadata and license, plus the companion AISBench PD skill at the same revision.

The user confirmed ownership of `debugging-vllm-ascend-pd-accuracy` and selected
MIT explicitly. Yuli-yx maintains it. Keep SOP, schemas, instrumentation notes,
examples, scripts, agent metadata and license. Inventory compatibility tools
require Python, PyYAML and Paramiko; use configured remote companions where
available. Original sources and adaptation notes are retained in the source
collection's [ATTRIBUTION.md](https://github.com/Yuli-yx/awesome-va-skills/blob/8d9f7ee56d088f15a398181590c4512bfc725d6f/ATTRIBUTION.md).

## Deduplication and task boundaries

The existing 53 catalogue entries were compared with the selected scope:

- AISBench PD benchmarking operates a different client and dataset wrapper
  from the existing `vllm-ascend-benchmark`, which uses `vllm bench`.
- Pure-role acceptance coordinates role-capacity isolation, SLO-constrained
  points, cache-tier validity and matched end-to-end comparisons. It delegates
  client preparation to the AISBench skill rather than duplicating that code.
- PD accuracy diagnosis follows failing requests across P, D, proxy and KV
  transfer to the first numerical divergence and restores the environment.
  Existing correctness, graph and distributed-debug entries cover adjacent
  validation or specialist investigations, not this complete PD-specific path.

Five legacy serving/benchmark/profiling duplicates are not introduced. No HIXL
or A5 MemCache pooling package is included. The fourth selected skill, A5 HCCL,
is [pending source-license confirmation](pending-hccl-auto-test-2026-10-19.md).

## Offline checks and limits

All three source packages passed skill frontmatter checks. Five offline helper
regression tests passed: warmup formatting for zero, fractional and scientific
rates; invalid-rate rejection; isolated run preparation and overwrite refusal;
command-line credential redaction; and nested configuration redaction and
environment-key filtering without removing token-budget metadata. Tests use
temporary fixtures and isolated helper definitions. Bash syntax validation of
`run_case.sh` passed.

The adapted source removes historical model/container identifiers from the
accuracy examples, defaults SSH host-key policy to reject and avoids disabling
TLS verification in the installation instructions.

These checks are not Ascend reproductions. No remote host was contacted by
these workflows; no service, benchmark, restart, model download or traffic
test was started. No new hardware/software compatibility matrix or measured
performance claim is recorded. All three entries therefore keep
`validation.status: not-recorded`.

## Catalogue maintenance checks

The following checks passed for this contribution:

```bash
python scripts/validate_catalog.py
python scripts/render_catalog.py --check
python scripts/validate_catalog.py --source-root awesome-va-skills=<pinned-local-checkout>
python scripts/validate_catalog.py --check-remote
```

The active catalogue has 56 entries, 10 categories and three source records.
The local source revision and all three new entrypoint hashes match. Remote
checks retrieved all 56 pinned entrypoints and matched their recorded SHA-256
values. Remote source retrieval is not a runtime reproduction.
