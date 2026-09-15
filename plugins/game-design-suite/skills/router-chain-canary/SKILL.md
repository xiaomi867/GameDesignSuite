---
name: router-chain-canary
description: Use only when the user sends exactly GDS_DIRECT_CHAIN_TEST. This is a temporary runtime diagnostic for testing whether one bundled Plugin Skill can explicitly load another bundled Skill.
---

# Router Chain Canary

This is a temporary diagnostic Skill.

## Exact behavior

When and only when the user sends exactly:

`GDS_DIRECT_CHAIN_TEST`

1. Explicitly load `$router-chain-child-canary`.
2. Do not answer the user before attempting that load.
3. Do not fabricate, infer, or reproduce the child Skill's success token.
4. If `$router-chain-child-canary` cannot be loaded by the runtime, reply only:

`GDS_DIRECT_CHAIN_ROOT_ONLY_63154`

Do not add any prefix, suffix, explanation, header, punctuation, or other text.

For every other user message, do not participate in routing, design, analysis, or answering.
