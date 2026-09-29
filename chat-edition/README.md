# Game Design Suite — Chat Edition

This is a parallel, ordinary-Chat version of Game Design Suite. It does **not** modify or replace the existing Plugin/Skill implementations.

## Why this exists

The Chat Edition avoids dependency on ChatGPT Skill/Plugin runtime. It is intended to run inside a normal ChatGPT Project using:
- Project Instructions
- project knowledge files
- ordinary chat conversations

## Files

- `PROJECT_INSTRUCTIONS.md` — paste into the ChatGPT Project's instructions.
- `knowledge/01-core-systems.md`
- `knowledge/02-hero-skill.md`
- `knowledge/03-balance-simulation.md`
- `knowledge/04-itemization.md`
- `knowledge/05-combat.md`
- `knowledge/06-economy-progression.md`
- `knowledge/07-level-ux.md`
- `knowledge/08-audit-verification.md`

The eight knowledge files preserve the professional material from the existing Game Design Suite specialist modules while collapsing runtime routing into project-level instructions.

## Setup in ChatGPT

1. Create a new Project named **Game Design Suite Chat Edition**.
2. Copy the contents of `PROJECT_INSTRUCTIONS.md` into Project Instructions.
3. Upload the eight files under `knowledge/` to the Project.
4. Start a **new chat inside that Project**.
5. Ask normal questions. Do not @mention a Skill or Plugin.

## First acceptance test

Ask:

> 给我设计一套 RPG 装备系统，包含装备槽位、品质、基础属性、主副属性、随机词条、强化、套装、掉落、替换和分解规则。先不要参考我的任何已有项目，也不要使用网页搜索。

Expected first visible block:

```text
【本次专业视角】
主责：装备 / Itemization 策划
协同：...
证据边界：...
```

The answer should follow the full itemization workflow rather than a generic RPG list.

## Isolation

This branch is intentionally separate from:
- the original Game Design Suite plugin;
- V2/V3 runtime experiments;
- diagnostic Canary/Router tests.

Nothing here is required by the existing plugin, and changes here do not affect it.
