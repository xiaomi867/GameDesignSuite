# ChatGPT Runtime Rebuild V2

This package is a clean runtime adapter built from the existing Game Design Suite canonical skills.

## Goals

- Preserve all 24 production skill capabilities and detailed guidance.
- Remove temporary canaries/probes from the rebuilt runtime.
- Avoid parent-router dependency for normal specialist work.
- Give every specialist a concise `Use when ...` description.
- Give every specialist a fresh runtime identity (`gds-*`) and `agents/openai.yaml`.
- Keep `SKILL.md` compact and use progressive disclosure through `references/canonical-guidance.md`.
- Keep the original `plugins/game-design-suite/skills` tree as the canonical source for Deep Code and historical compatibility.

## Runtime model

`@Game Design Suite Rebuilt (V2)` -> host selects the narrowest matching `gds-*` specialist -> specialist reads its preserved canonical guidance -> specialist answers directly.

The design does not require `game-design -> $child-skill` chaining. Cross-domain collaboration is reported only when the other specialist content is actually loaded.

## Test order

1. `gds-itemization-design`: normal RPG equipment request.
2. `gds-hero-stat-progression`: Lv1-to-Lv80 stat growth request.
3. `gds-balance-design`: numerical benchmark/tuning request.
4. Broad cross-system request to test `gds-game-design`.
