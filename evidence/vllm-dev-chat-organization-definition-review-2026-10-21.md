# vLLM development chat organization: definition review

- Review date: 2026-10-21.
- Method: inspect the pinned public skill definition, repository README, and MIT license.
- Source project: [Henry-Avery/ascend-agent-skills](https://github.com/Henry-Avery/ascend-agent-skills).
- Source revision: `0d34abd7e3b2e599d8bc5d2bbded76d732fa1e4a`.
- Definition: [`skills/vllm-dev-chat-organization/SKILL.md`](https://github.com/Henry-Avery/ascend-agent-skills/blob/0d34abd7e3b2e599d8bc5d2bbded76d732fa1e4a/skills/vllm-dev-chat-organization/SKILL.md).
- Definition SHA-256: `84a5d5e5772381afad858af0d1e02bb8e8d5e39856d453d446a2165ecd385394`.
- Declared upstream license: MIT.

The task is to make vLLM development chats findable by actual work purpose, PR, model, component, or topology. The definition covers a requested chat scope, title selection, readback after a rename, project or sidebar moves only when requested, and archival only for authorized chats. It preserves user-chosen titles and leaves chats unarchived when the user only asks for manual archive preparation. It does not claim to intercept manual UI actions, run model workloads, or infer validation from a title.

The `delivery` category reflects development handoff and traceability; this is a host-side chat-management task, not an NPU execution skill. Its applicability depends on the host exposing suitable list, read, rename, and archive tools. The definition passed the Codex skill creator's `quick_validate.py`, and a GitHub Contents API readback of the pinned definition matched the recorded SHA-256. No host chat-management run or vLLM device execution is recorded here, so `validation.status` remains `not-recorded`.
