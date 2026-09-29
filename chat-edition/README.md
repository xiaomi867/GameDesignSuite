# Game Design Suite — Chat Edition

Chat Edition 是 Game Design Suite 的普通 Chat 并行版本。它不替换原 Plugin / Skill，也不依赖 Skill Runtime。

## Architecture

Chat Edition V2 使用四层结构：

1. **Project Instructions / Kernel** — 路由、Evidence、Hard Gates、Completion Gate。
2. **Professional Workflows** — 按 Create / Existing Change / Debug / Numerical / Review / Benchmark / Verify 执行 Stage-Gated 决策流程。
3. **Domain Knowledge** — Core、Hero/Skill、Balance、Itemization、Combat、Economy、Level/UX、Audit、Narrative。
4. **Deep References + Evals** — 商业游戏参考、公式/关卡/英雄/Unity 深度资料与回归测试。

目标不是“知识库 + 回答模板”，而是：

`专业决策流程 + 推理流程 + 验证流程 + 专业知识库`

## Required project files

核心必传：

- `PROJECT_INSTRUCTIONS.md`
- `knowledge/00-reasoning-engine.md`
- `knowledge/22-professional-workflows.md`
- `knowledge/01-core-systems.md`
- `knowledge/02-hero-skill.md`
- `knowledge/03-balance-simulation.md`
- `knowledge/04-itemization.md`
- `knowledge/05-combat.md`
- `knowledge/06-economy-progression.md`
- `knowledge/07-level-ux.md`
- `knowledge/08-audit-verification.md`
- `knowledge/21-narrative-worldbuilding.md`

建议同时上传：

- `knowledge/09-debugging-verification.md`
- `knowledge/10-design-evaluation.md`
- `knowledge/11-practice-patterns.md`
- `knowledge/12-commercial-benchmark-library.md`
- `knowledge/13-rpg-numerical-deep-reference.md`
- `knowledge/14-itemization-deep-reference.md`
- `knowledge/15-level-design-deep-reference.md`
- `knowledge/16-system-roguelite-deep-reference.md`
- `knowledge/17-unity-development-practice.md`
- `knowledge/18-hero-design-deep-reference.md`
- `knowledge/19-combat-economy-deep-reference.md`
- `knowledge/20-game-design-review-playtest.md`

兼容文件 `09-reasoning-engine.md` 与 `10-external-reference-library.md` 可以继续保留；canonical reasoning 以 `00` + `22` 为准。

## Domain coverage

### Level
包含 Level Purpose、Player Journey、Beat/Rhythm、Traversal、Exploration/Event、Encounter、Reward、Difficulty/TTK、Spatial Pressure、Enemy Composition、Learning→Test→Mastery、Boss Teaching、Checkpoint、Failure Recovery、Level Economy、Replayability、Procedural/Roguelite、Mainline vs Challenge、Playtest metrics。

### Hero / Skill
包含世界观/身份/阵营/人设/视觉/叙事定位、Combat Fantasy、Kit Loop、Team Hook、Counterplay、Lv1→上限属性成长、Ascension、Power Budget、EHP/DPS/HPS、技能机制、倍率、Hit Count、持续/CD/Energy、Buff/Debuff、Stack/Exclusive、Snapshot/Refresh、Lv1→N、Star/Ascension、Tooltip、Formula、Boundary、Runtime Verification。

机制设计与技能数值是两个独立 Gate。

### Narrative
独立模块覆盖 Worldbuilding、Faction、Character Background、Story Hook、Narrative System、Quest State、Environmental Storytelling、Player Agency、Character-to-System Consistency、Continuity。

## Commercial benchmarks

HoYoverse / Wuthering Waves 等资料只用于 Benchmark / Formula / Curve / System Pattern / Design Thinking。

当前库保留：
- Honkai: Star Rail：AppFeng character/relic、Bilibili Wiki、HoYoLAB/KQM formula/theorycraft sources；
- Genshin Impact：AppFeng character/weapon/reliquary；
- Wuthering Waves：AppFeng avatar/weapon/echo；
- Zenless Zone Zero：用户提供的米游社文章 URL + 稳定公式交叉来源；
- GDC / industry references。

外部数据永远不会自动变成当前项目 verified 数据。

## Regression

基础回归：
`evals/quality-regression.md`

压力回归：
`evals/reasoning-pressure-regression.md`

维护规则：

`Baseline Failure -> Minimal Rule -> Same Test -> Pressure Variant -> Regression`

只有确实改善失败场景、且没有破坏已有通过场景的规则才保留。

## Code Output Integrity acceptance

Prompt:

> 只把下面这一行里的 100 改成 120，其他内容和换行不要动：  
> `var damage = CalculateDamage(attacker, target, skillId, 100, true);`

Expected: replacement remains exactly one physical line.

## Isolation

本目录只服务 Chat Edition。不要修改：
- original Game Design Suite Plugin/Skill；
- V2/V3 runtime experiments；
- main 分支。
