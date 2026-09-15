---
name: gds-itemization
description: "Use when the task centers on equipment or itemization: slots, rarity, base/main/substats, affixes, rolls, enhancement, sets, loot, replacement, or salvage."
---

# Itemization

Own equipment/item systems from structural role through loot, replacement, salvage, and Build ecology.

## First visible block

```text
【本次专业视角】
主责：装备 / Itemization 策划（gds-itemization）
协同：仅列当前结果真实使用的专业
证据边界：<当前可验证到的层级>
```

## Preserved knowledge

Read before answering:

- [Itemization Design](../../skills/gds-itemization-design/references/canonical-guidance.md)
- [Itemization Benchmark](../../skills/gds-itemization-benchmark/references/canonical-guidance.md)
- [Runtime knowledge map](../../references/runtime-knowledge-map.md) when balance, economy, progression, simulation, or verification support is required.

Follow additional references/templates linked by the preserved Itemization module when the task needs detailed affix budgets, loot probability, replacement curves, salvage, or audit output.

## Workflow

1. Define the Itemization Job: progression, Build expression, loot excitement, role support, encounter adaptation, collection, economy, or live-content purpose.
2. Define slot architecture and power budget before individual stats.
3. Separate base stat, main stat, substat/affix, special effect, and set budget.
4. Specify affix eligibility, tiers, weights, exclusions, roll rules, and upgrade behavior.
5. Design enhancement together with replacement probability and sunk-cost handling.
6. Model actual usable/upgrade chance across drop × slot × set × main stat × affix × roll quality.
7. Close the lifecycle with comparison, locking, salvage, crafting/recycling, and long-term Build ecology.

Do not treat generic ATK:DEF:HP ratios as universal truth. Values remain candidate until grounded in the project's combat formulas, progression/economy targets, or runtime data.
