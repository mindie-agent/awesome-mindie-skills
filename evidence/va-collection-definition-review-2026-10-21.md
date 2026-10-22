# VA collection source review: 2026-10-21

This extends the selected PD workflow contribution with distinct, license-resolved
entries from Yuli-yx's complete collection. Existing catalogue IDs and their
sources are preserved. MemCache pooling is submitted separately; this change
does not depend on the pooling feature branch.

The package payload is pinned at
`Yuli-yx/awesome-va-skills@7d3aa5f3b55049a2f917b4ca682c1e9963033c18`.
The collection now uses this catalogue's schema and bilingual rendering while
retaining the old workspace support layout. See its
[attribution](https://github.com/Yuli-yx/awesome-va-skills/blob/7d3aa5f3b55049a2f917b4ca682c1e9963033c18/ATTRIBUTION.md)
and complete package hash manifest for original sources, licenses and local
adaptations. A collection snapshot does not assert byte identity with current
vLLM-Ascend, CANN HIXL or MindIE runtime releases.

## Reviewed scope

The review maps entrypoint task/description, workflow role, execution conditions,
complete package dependencies and license/source attribution into the catalogue.
Workspace-derived packages retain Qi Mao's MIT notice and local contributor
attribution. vLLM Ascend packages retain Apache-2.0; HIXL companions retain CANN
Open Software License v2.0. These are collected/adapted packages, not a claim that
Yuli-yx authored every upstream workflow.

| Entry | Definition SHA-256 |
| --- | --- |
| `aisbench-accuracy` | `e25235228d1840f838c86ab1f6c36eabea8899208462c7137708cf82898fc224` |
| `ascend-memory-profiling` | `b0f7896bedaf9c2efe9337bc4e4f9abd78c9b40c834b87673015d0bf3c05472a` |
| `ascend-profiling-collection` | `7bb6c9d78cc03f7bafac07e06b6011c0c8ca51da0fc00c21cc072e88f0908ca3` |
| `driver-peermem-check` | `b0dd43de7922775c26d7b060f8e32fc803987874e964a0643395d4b38e98e8e4` |
| `hixl-pr-review` | `0fcd9cf33c248ebede257a5c78d7dadb0d0c10ff52cf2c340e66a5413500b395` |
| `hixl-srs-doc-generator` | `eb0afc9f3c328a7c9fce196bb1842882ef38011dfbd03ae2eff2e371deaeaf78` |
| `hixl-troubleshoot` | `5cbc9148120946961dcd85df0edf64ece8a07c9bd7ec68e39e003887e7ee32c0` |
| `hixl-ut-generator` | `6f20964bd37dd9743af59c89f774ca75785b2d348bc78be6ca3774bd91cefb4f` |
| `machine-management` | `52afb57d3926f6f9176b185c297eaa4e6ec5b44df72ea6ded0431391869a939e` |
| `main2main` | `cafb766a60fb297ca0daeccc89a91c9989dfafe6adc0734c81d1fdfaee33f974` |
| `modelscope` | `b4b5377a496ddf2a95eb758f7563967d024226c58a4598b4e874beb071f74bcb` |
| `remote-code-parity` | `315aad9e08078f040c46563f1f8207c9c8517b8337c5eb19c54c8ceaaeae1aed` |
| `remote-toolbox` | `508452de949b2c2ed44fbe19db6d5b4ea762af0b1eedcdd84e3fff6da9389618` |
| `repo-init` | `42572c8325ba759d89999fb70b8727488c66c7f1bb82a33ab5d90ccfac3e9001` |
| `session-management` | `7fe21ceb5b0c302b20091b0cb71a3c1a827d814a93a7828e8bc2146f1ac7cef4` |
| `vllm-ascend-build` | `ee67763b7f6a17348976d43c1765bf12d0559adf7b837a0b251d26b8a01f53d5` |
| `vllm-ascend-model-adapter` | `0ef9f14f2e7d1fe6c6967644158504542248965d1870b1a473fb74173ad1b119` |
| `vllm-ascend-release-note-writer` | `082382b855ebfa6f59201b3e3d3672aebe04e8b1d9a67bb16d1da687edb8050f` |
| `vllm-ascend-release` | `54d237d19339fb2cdb298d2edc02995a4007b2c572a53332ef3d72f6c7867062` |

## Exclusions and validation

The original three PD entries retain their previously reviewed `8d9f7ee` source;
this is intentional, not a partial source-pin update. Separate source identifiers
describe the newly inspected snapshot and its license groups. No existing skill
ID is replaced simply because a similarly named workflow exists in the collection.

`hccl-auto-test`, `compile-mooncake`, `pd-dfx-workbench` and `vllm-ascend-debug`
remain excluded pending license/provenance resolution. In particular, the HCCL
personal skill is still credited to WZN-JJB; see the existing pending record.
Local vendor/kernel attachments and Leaf-Spine drafts are not imported.

Checks cover catalogue schema, local links, source-byte hashes, generated
bilingual README content and rejection of invalid duplicate keys, categories
and stale rendering. This is source/catalogue review only: no remote NPU,
network, build, profiling, benchmark or inference execution was performed.
All added entries remain `validation.status: not-recorded`.
