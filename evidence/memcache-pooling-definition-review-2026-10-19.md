# MemCache pooling definition review - 2026-10-19

Source: zouyida2052/awesome-mindie-skills at cc87235a79fc2145afecfbd03b59fc772ee41724, skills/ascend-memcache-pooling/SKILL.md. Original skill under CC0-1.0; upstream reference material retains its own licensing. The implementation is included in this contribution; the catalogue URL points to the immutable published fork commit so installation does not depend on an unmerged upstream path.

Scope: A3 HCCS/SDMA standalone ownership and A5 UB/UBoE fused ownership, each with HBM+DRAM or HBM+DRAM+SSD. Pooling is distinct from optional PD transfer. Model layout, driver, firmware and package compatibility remain deployment inputs.

Reviewed all three skill/reference files against the official Git snapshots and file hashes in the [source ledger](../skills/ascend-memcache-pooling/references/sources.md). Checked A3 init ordering and consumer capacity, A5 transport distinction, additional UBSIO memory, disk-owner count, force-initialization boundaries and scratch-key documentation conflicts. Runtime scripts are generated for the chosen environment; no hard-coded private endpoints or credentials are included.

Behavioral desk checks (not hardware reproductions):

- A3 two-tier, one owner/node and eight inference processes: owner starts before model loading, clients contribute 0GB, no SSD allocation.
- A3 three-tier with an existing disk: one owner implies device_count=1; scratch must remain enabled; conflicting spellings are resolved against the installed UBSIO parser; no automatic force initialization.
- A5 UB/UBoE, four owners/node: device_urma and device_uboe remain distinct; per-owner memory is multiplied by actual owners and UBSIO buffering budgeted separately.
- Unknown A5 Pod UBoE support: request platform evidence instead of claiming the Server example certifies that Pod.
- L2.5 retains writes: external hits and disk capacity are insufficient to claim SSD readback.
- Historical package versus new Wiki: do not inject unsupported options or replace the framework's working PD connector.

Validation performed: skill frontmatter/scaffold validation, catalogue schema/local-link validation, and generated bilingual catalogue drift checks. The pinned source hash is checked against the published Git object. No service was started, disk initialized or package installed on NPU hosts. Hardware reproduction status remains not-recorded; no historical performance result is attributed to this new skill revision.
