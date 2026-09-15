---
name: router-chain-child-canary
description: Explicit-only diagnostic child Skill for Game Design Suite runtime chain testing. Do not select this Skill from ordinary user requests; it exists only to be loaded by $router-chain-canary.
---

# Router Chain Child Canary

This is a temporary diagnostic child Skill.

If the current user message is exactly:

`GDS_DIRECT_CHAIN_TEST`

reply only:

`GDS_DIRECT_CHAIN_CHILD_92741`

Do not add any prefix, suffix, explanation, header, punctuation, or other text.

For every other message, do not participate in routing, design, analysis, or answering.
