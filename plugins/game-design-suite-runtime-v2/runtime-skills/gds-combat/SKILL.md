---
name: gds-combat
description: "Use when the task centers on combat rules, targeting, resources, states, AI, timing, encounter combat logic, or battle-system behavior."
---

# Combat Design

Own battle-system behavior and combat decision structure.

## First visible block

```text
【本次专业视角】
主责：战斗策划（gds-combat）
协同：仅列当前结果真实使用的专业
证据边界：<当前可验证到的层级>
```

## Preserved knowledge

- [Combat Design](../../skills/gds-combat-design/references/canonical-guidance.md)
- [Runtime knowledge map](../../references/runtime-knowledge-map.md) for hero/skill, balance, level, or verification support.

## Workflow

1. Define combat goals, player decisions, pacing, and loss/failure conditions.
2. Specify targeting, resources, state machines, timing/action economy, reactions, control, AI, and team interactions.
3. Separate systemic rules from hero-specific mechanics and encounter-specific exceptions.
4. Validate readability, counterplay, degenerate loops, infinite-resource/action cases, target ambiguity, and failure recovery.
5. When real config/code exists, verify implementation semantics before proposing numeric or behavioral changes.

Do not invent runtime behavior from field names alone. For cross-domain tasks, read preserved adjacent guidance directly rather than relying on runtime skill chaining.
