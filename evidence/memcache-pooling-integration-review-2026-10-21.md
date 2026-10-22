# MemCache pooling integration review: 2026-10-21

This review extends zouyida2052's original contribution at
`f5108884c387175025eecf2e58021828f802a204` with Yuli-yx's pooling guidance and
standard-library multi-DP monitor. The integrated definition is pinned by the
`ascend-pooling-workflows` source in `catalog/sources.yaml`.

## Definition and provenance

- Retain the original A3 SDMA standalone/zero-DRAM-client route, A5 UB/UBoE
  recipes, SSD ownership/memory guidance, documentation conflicts and official
  repository pins. Those pins are inherited review evidence; this integration
  does not claim a new inspection of every upstream Wiki document.
- Add a scoped Host RoCE supplement, independent P/D versus pool data-plane
  choices, physical mapping, supported layerwise boundaries and complete
  read-only monitoring commands.
- Separate token reuse, conditional external lookup, successful get operations
  and SSD-medium counts. Preserve N/A for missing core metrics; window resets,
  changed series and failed DP endpoints invalidate an aggregate.
- Document HBM working-set control, actual SSD readback, matched OFF/ON load and
  bounded C/RR tuning. Example user SLOs remain examples, not generic guarantees.
- Preserve CC0 attribution for the original guide and MIT notices for Yuli-yx's
  additions. No vendor scripts/kernel binaries, populated host inventories or
  captured runtime data are included.

## Checks and limitations

Offline checks run on Windows with Python 3.12: 17 monitor tests, including
read-only local HTTP/CLI collection, plus skill frontmatter, package links,
Python syntax, catalogue schema/source hashes and bilingual rendering checks.
CI runs the monitor suite on Python 3.11. Test fixtures use localhost and do not
invoke NPU code or modify a remote service.

This is a definition and offline-tool review. No A3/A5 route, SSD readback,
P/D correctness, latency, throughput or proposed SLO was executed for this
revision. `validation.status` remains `not-recorded`. Remote source reachability
checks verify definition bytes, not runtime compatibility.
