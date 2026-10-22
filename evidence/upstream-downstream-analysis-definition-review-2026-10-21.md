# Upstream and downstream analysis definition review

- Review date: 2026-10-21.
- Source: [SOMEONEUNSEEN/awesome-mindie-skills](https://github.com/SOMEONEUNSEEN/awesome-mindie-skills).
- Pinned revision: `614d7c22c05f147d96e09044aa1b8e62cc9ec89e`.
- Skill directory: [skills/analyze-upstream-downstream](https://github.com/SOMEONEUNSEEN/awesome-mindie-skills/tree/614d7c22c05f147d96e09044aa1b8e62cc9ec89e/skills/analyze-upstream-downstream).
- Definition SHA-256: `fc3be275595f7d36e419d6f4ac8e15b0a5d256895262f47fd9205e6f9caa86ab`.
- Maintainer: SOMEONEUNSEEN. License: CC0-1.0 under the source repository's [license](https://github.com/SOMEONEUNSEEN/awesome-mindie-skills/blob/614d7c22c05f147d96e09044aa1b8e62cc9ec89e/LICENSE).

## Provenance and inspected scope

The contribution adapts the maintainer's local `analyze-upstream-downstream` skill into English for this repository. The complete three-file layout is retained: [SKILL.md](../skills/analyze-upstream-downstream/SKILL.md), [references/report-template.md](../skills/analyze-upstream-downstream/references/report-template.md), and [agents/openai.yaml](../skills/analyze-upstream-downstream/agents/openai.yaml). All three files were inspected. The catalogue points to the published fork's immutable source commit so installation does not depend on an unmerged upstream path, following the packaging precedent in [PR #2](https://github.com/mindie-agent/awesome-mindie-skills/pull/2).

The workflow compares framework modules with downstream plugins, forks, or platform adaptations. For Ascend inference engineering, a concrete application is assessing which vLLM behavior remains inherited by vLLM Ascend and which overridden paths require manual synchronization. The skill itself is framework-neutral and contains no task-specific source excerpts or private environment identifiers.

The `delivery` category reflects its primary output: an evidence-based migration and validation plan. This complements `vllm-ascend-change-validation`, which selects validation for a proposed diff; this workflow first establishes whether a change is needed by tracing upstream/downstream implementation boundaries. `execution: host` describes source and history inspection using accessible checkouts, Git, and text search. Target-hardware checks may be proposed but are not required to produce the analysis.

Inspection confirmed that the instructions preserve separate baselines for local source, dependency pins, and loaded runtime packages; inspect captured imports, patches, registries, and configuration branches; distinguish inherited behavior from manual synchronization; and separate static evidence from reference, runtime, end-to-end, and performance checks. The report template preserves unresolved hypotheses and unrun checks. Implementation and publication remain subject to the user's task scope. No third-party implementation is bundled.

## Installation and example

Fetch the pinned source and keep the entire skill directory, including `references/` and `agents/`:

```bash
git clone https://github.com/SOMEONEUNSEEN/awesome-mindie-skills.git upstream-downstream-skills
git -C upstream-downstream-skills checkout --detach 614d7c22c05f147d96e09044aa1b8e62cc9ec89e
```

Point a skill-capable assistant to `upstream-downstream-skills/skills/analyze-upstream-downstream/SKILL.md`, or copy that whole directory to its configured skill location. There are no additional Python packages or NPU dependencies for the skill itself. Repository-specific dependencies are relevant only if the requested analysis extends into execution.

Example request:

> Read `upstream-downstream-skills/skills/analyze-upstream-downstream/SKILL.md`. Compare the specified module in `/path/to/upstream` and `/path/to/downstream` at their current snapshots. Trace actual bindings and optional branches, identify inherited and manually synchronized behavior before listing gaps, and return sanitized evidence plus the smallest migration and validation plan. Do not implement changes.

## Validation boundary

The skill frontmatter check passed. Packaging checks confirmed the same three-file layout as the local input, valid relative reference links, valid UI metadata, and absence of local machine identifiers in the published Markdown. These checks verify packaging and instructions, not the quality of an executed analysis.

No real module comparison, framework test, target-device execution, end-to-end run, or performance benchmark was performed with this published revision. Execution validation remains `not-recorded`, with no reproduction cases or hardware compatibility claims. Catalogue and remote hash check results are reported separately in the PR.
