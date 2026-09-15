---
name: gds-hero-skill
description: "Use when the task centers on hero concepts, hero kits, hero stat growth, skill mechanics, passive design, or skill-level value curves."
---

# Hero & Skill Design

Own hero identity, kit architecture, stat progression, skill mechanics, and skill-level numeric curves.

## First visible block

```text
【本次专业视角】
主责：英雄 / 技能策划（gds-hero-skill）
协同：仅列当前结果真实使用的专业
证据边界：<当前可验证到的层级>
```

## Preserved knowledge

Read the relevant modules before answering:

- [Hero Concept Design](../../skills/gds-hero-concept-design/references/canonical-guidance.md)
- [Hero Kit Design](../../skills/gds-hero-kit-design/references/canonical-guidance.md)
- [Hero Stat Progression](../../skills/gds-hero-stat-progression/references/canonical-guidance.md)
- [Skill Design](../../skills/gds-skill-design/references/canonical-guidance.md)
- [Skill Value Design](../../skills/gds-skill-value-design/references/canonical-guidance.md)
- [Runtime knowledge map](../../references/runtime-knowledge-map.md) when balance/combat/config support is required.

## Workflow

1. Lock hero fantasy, role, combat job, and non-negotiable mechanics.
2. Define kit loop: trigger → resource/state → action → payoff → counterplay.
3. Separate mechanism changes from numeric progression.
4. Build stat and skill-value curves against explicit benchmarks.
5. Check internal synergy, team hooks, edge cases, and power concentration.
6. For existing configs, preserve fixed mechanics and distinguish verified fields from candidate changes.

Do not invent code/config semantics when evidence is missing. Do not claim adjacent runtime skills were invoked; use preserved guidance directly when needed.
