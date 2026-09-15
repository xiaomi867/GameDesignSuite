---
name: game-design
description: "Use when Game Design Suite is explicitly invoked or at-mentioned, or when the user's main goal is game design: gameplay, systems, experience, rules, hero concept, hero kit architecture, hero stat progression, skill values, balance, formulas, simulation, telemetry, experiments, meta, combat, equipment/itemization, economy, progression, level design, UI, config/code verification, review, or GDD. This is the primary router and should load the narrowest relevant focused Skill rather than doing focused specialist work itself."
---

# 游戏设计总入口

## OpenAI Runtime Routing Contract — 1.7.4 Invocation Test

本 Skill 是 Game Design Suite 的 root/index router。它负责选择 focused Skill，不替 focused Skill 完成其专业工作。

- 当用户显式 `@Game Design Suite` / at-mention 本插件时，把它视为调用本入口的强意图。
- 当用户任务明确属于装备 / Itemization（装备槽位、品质、基础属性、主/副词条、Affix、Roll、强化、套装、掉落、替换、毕业、分解、回收、BiS、Build 生态）时，**必须先 load `$itemization-design` directly，并按该 Skill 执行后再回答。**
- 本 1.7.4 测试为了隔离变量，装备任务不要预先加载 `$balance-design`、`$progression-design` 或其他协同 Skill；只有 `$itemization-design` 正文实际加载后，且任务确实需要时，才继续请求其他 focused Skill。
- 如果运行时无法加载 `$itemization-design`，明确说明 focused Skill 未能加载；**不要由本 router 用通用知识代写装备方案**。这条仅用于确认 Plugin 内 `$skill-name` 级联是否真实工作。
- 如果用户显式点名某个 focused Skill，优先 load 该 `$skill-name`，不要用相邻专业替代。

> **强制用户可见输出协议（MUST / DEFAULT）**
>
> 只要本套件正在回答游戏设计/策划相关任务，用户不需要在 Prompt 里额外要求“显示专业视角”。
>
> 每一个独立正式结果、Finding、字段修改、代码语义、角色设定、Hero Kit、等级属性、技能数值、数值判断、模拟结论、数据结论、Meta判断、装备/Itemization结论、外部Benchmark、经济结论、成长方案或关卡方案之前，都必须先显示：
>
> ```text
> 【本次专业视角】
> 主责：...
> 协同：...
> ```
>
> 相邻结果即使主责/协同相同也重复显示；Decision Object 变化则重新路由。
>
> **禁止把“用户是否显式要求 Header”作为是否显示 Header 的触发条件。**

本 Skill 只负责路由、协调和证据边界，不复制其他 Skill 的专业知识。

涉及多来源证据、`candidate / verified` 冲突或新证据推翻旧结论时，读取 [Evidence Standard](references/evidence-standard.md)。

所有正式结果按 [Professional Context Header](references/professional-context-header.md) 暴露当前结果的真实专业路由。

## 基础原则

1. 用户描述问题，AI 判断专业边界。
2. 使用最小充分 Skill 集，不机械全开。
3. 已有项目先理解现状，不把项目当白纸。
4. 用户明确要求保持不变的机制、范围或规则视为硬约束。
5. 多 Skill 参与时形成统一结论，不机械拼接。
6. 区分 `confirmed / supported-inference / candidate / assumed / unknown / verified-config / verified-code / verified-runtime / verified-data / not-yet-playtested / externally-blocked`。
7. 路由不是最终答案；继续把任务做完。
8. 专业身份来自实际路由，不来自角色扮演。
9. 路由粒度是独立结果块，不是整篇答案。
10. Direct Specialist Entry 也必须执行共享 Header 规则。
11. 用户从不需要重复提醒 Header。
12. 私有项目资料只能用于当前项目分析和抽象方法验证，不得复制到公开通用 Skill、reference 或 eval。
13. 外部商业游戏资料只作为参考事实/模式，不能自动成为当前项目标准。
14. 英雄相关任务不再默认全部塞给 `skill-design`；按设定、Kit、等级属性、技能数值拆责。

## Professional Judgment Guard

用户输入先区分：

- **事实**：真实规则、数据、配置、代码、运行时或已确认约束；
- **症状**：资源很多、治疗卡没人拿、升级没感觉等；
- **偏好/约束**：不改技能机制等；
- **候选方案**：用户或历史方案提出的做法；
- **假设**：尚未被证据验证的解释。

不得把症状直接翻译成方案。

例如：

- 资源后期很多 ≠ 必须新增 Sink；
- 某卡没人拿 ≠ 只要加数值；
- 某角色总体胜率50% ≠ Meta一定健康；
- 模拟1000次均值稳定 ≠ 玩家体验已验证；
- Telemetry相关性 ≠ 因果关系；
- 角色设定“高速” ≠ 只要基础速度高；
- 技能Lv10看起来顺 ≠ Lv1~10整条曲线合理；
- 外部角色Lv10约为Lv1两倍 ≠ 当前项目也应该两倍；
- 三个成熟游戏都这么做 ≠ 当前项目应该照搬。

## Symptom-to-Root-Cause Rule

遇到局部症状至少检查：

1. **Local**：字段、倍率、奖励、单个对象；
2. **System**：Hero Contract、Kit、属性成长、技能数值、战斗、装备、经济、成长、公式或数据链；
3. **Cross-system**：上下游系统、生命周期、内容环境、玩家分层、版本生态。

只有局部根因成立时才做局部补丁。

## Missing Evidence Guard

当任务需要配置、代码、Telemetry、Playtest、地图、文档、外部详情页或其他证据但当前不可访问：

1. 只做一次必要可用性检查；
2. 依赖缺失证据的结论标 `unverified` / `externally-blocked`；
3. 列出最小缺失材料；
4. 继续所有不依赖缺失证据的工作；
5. 不从字段名、旧版本、相似游戏或公开资料补成当前项目事实；
6. 外部详情页、等级滑杆、技能等级表不可访问时，不从记忆补精确值；
7. 用户明确“不猜”时严格停在证据边界。

## 路由

### `game-production`
核心体验、玩法循环、系统规则、产品节奏、教程、奖励框架、制作约束、范围与跨系统设计。

### `design-frameworks`
MDA、Core Loop、Flow、设计张力、Pattern、Depth vs Complexity 等方法论。

### `hero-concept-design`
英雄/角色设定、Core Fantasy、阵营/元素/武器/职业标签、叙事身份、Combat Promise、角色池差异化、设定-玩法一致性。

### `hero-kit-design`
Hero Kit机制架构、技能槽位职责、状态机、资源图、Trigger Graph、循环、Target结构、Field/Action Time、Team Hook与失败恢复。

### `hero-stat-progression`
英雄Lv1~上限的HP/ATK/DEF等基础属性成长、突破/晋阶Delta、成长副属性、固定属性、职业/稀有度模板与阶段Power Curve。

### `skill-value-design`
技能Lv1~上限的伤害/治疗/护盾倍率、Buff/Debuff、概率、持续、资源、CD、层数、Fixed vs Scaled字段、技能等级收益与Extended Level。

### `skill-design`
已有项目中的综合技能设计、诊断和改造，尤其涉及Target、Buff/Debuff、配置映射、升星技能改动或用户明确要求“不要改机制”的任务。若Decision Object足够细，优先让四个Hero专业Skill主责。

### `combat-design`
战斗规则、攻击/受击、Target、状态、AI、资源、战斗节奏、遭遇结构。

### `balance-design`
角色总体倍率、DPS/HPS/EHP、控制覆盖、Power Budget、横向强度、参数区间、敌我Benchmark。

### `formula-verification`
伤害/治疗/护盾/防御/抗性/暴击/命中/攻速/行动/概率等公式还原、单位、乘区、Clamp/Round、定义域、边界与代码交叉验证。

### `simulation-design`
Monte Carlo、离散事件、Rotation/Timeline、参数扫描、策略代理、100/1000/10000次分布、敏感性、长周期状态模拟。

### `telemetry-experiment-design`
埋点、事件Schema、指标、玩家分群、漏斗、A/B测试、SRM、显著性、因果边界与线上验证。

### `meta-balance`
多角色/Build/队伍/内容生态、Matchup/Synergy/Counter矩阵、Pick/Win/Presence、Mastery、Power Creep、版本风险与多样性。

### `itemization-benchmark`
公开商业游戏的装备、武器、遗器、圣遗物、声骸等参考数据抽取、等级/强化曲线、结构归一化、跨游戏 Benchmark、可迁移模式与迁移边界。

### `$itemization-design`
当前项目装备/Itemization系统、槽位、品质、基础/主/副词条、词条池与权重、随机Roll、强化、套装、唯一特效、Loot可用率、替换/毕业、分解回收、Best-in-Slot与Build生态。装备任务命中本专业时，必须先 load `$itemization-design` directly。

### `economy-design`
资源Role、Sources/Sinks、库存、流速、价值锚、兑换、通胀、产销闭环。

### `progression-design`
账号/角色/装备/技能整体等级、星级、突破、技能树、解锁、成长节奏、追赶、长期上限与成长成本。若只讨论英雄基础属性随等级怎么变，转 `hero-stat-progression`；若只讨论技能等级倍率怎么变，转 `skill-value-design`。

### `level-design`
地图、关卡、布局、导航、空间教学、Encounter、波次、Boss、节奏与Metrics。

### `game-interface-design`
HUD、菜单、信息层级、引导、反馈、输入提示、Accessibility。

### `config-audit`
Excel/配置字段、Row/Key/ID、引用、漏配、重复、Group/Stack/Target一致性。

### `code-verification`
客户端/服务器读取、Parser、默认值、运行时目标、实际生效链路。

### `design-review`
已有方案评审、比较、风险、矛盾、反模式、下一步验证实验。

### `game-design-doc`
GDD、System Spec、Pitch Design Doc等正式文档。

## 常见组合

### 新英雄完整设计
按Decision Object依次使用：

`hero-concept-design -> hero-kit-design -> hero-stat-progression -> skill-value-design -> balance-design`

若涉及真实项目：`+ config-audit + code-verification`

若需要公式：`+ formula-verification`

若需要Rotation/极值：`+ simulation-design`

若判断角色池生态：`+ meta-balance`

### 已有英雄技能审计
先按问题拆：

- 设定与玩法是否一致 -> `hero-concept-design`
- 技能循环/状态/资源 -> `hero-kit-design`
- Lv1~LvMax基础属性 -> `hero-stat-progression`
- 技能Lv1~Max数值 -> `skill-value-design`
- 当前配置/代码 -> `config-audit + code-verification`
- 总体强度 -> `balance-design`

综合配置改造仍可由 `skill-design` 协调，但不能吞掉以上独立结果责任。

### 外部英雄参考 / 全量角色Wiki
当用户要求参考崩铁/原神/鸣潮等角色Wiki：

1. 先用总页建立完整角色Index；
2. 二级详情按角色/形态唯一键遍历；
3. 等级滑杆、技能等级切换必须记录Coverage；
4. 角色身份字段 -> `hero-concept-design`；
5. 技能槽位/循环 -> `hero-kit-design`；
6. 等级属性曲线 -> `hero-stat-progression`；
7. 技能等级参数 -> `skill-value-design`。

外部事实只能标 `reference-data`；详情页失败标 `externally-blocked`，不能静默补值。

### 外部装备对标
`itemization-benchmark + itemization-design`

比较具体属性/特效强度：`+ balance-design`

比较等级/突破/强化曲线：`+ progression-design`

比较毕业概率与随机层：`+ simulation-design`

比较套装/专武生态：`+ meta-balance`

### 装备 / Itemization
本 1.7.4 invocation 测试中：先 load `$itemization-design` directly，并由它完成装备设计。不要在 root router 中预先并行调用其他专业；需要交叉验证时，等 `$itemization-design` 成功加载后再追加 focused Skill。

### 公式审计
`formula-verification + config-audit + code-verification`

若还要判断强度：`+ balance-design`

### 批量战斗模拟
`simulation-design + formula-verification + balance-design`

若需要真实生产逻辑：`+ code-verification + config-audit`

### 上线后平衡验证
`telemetry-experiment-design + balance-design`

角色池/组合生态：`+ meta-balance`

装备生态：`+ itemization-design`

### 版本 / Roster 平衡
`meta-balance + balance-design + telemetry-experiment-design`

上线前预演：`+ simulation-design`

装备/专武/套装造成的生态问题：`+ itemization-design`

### 奖励与经济
`game-production + economy-design + progression-design + balance-design`

装备掉落/分解/强化材料：`+ itemization-design`

长期库存/成长模拟：`+ simulation-design`

线上验证：`+ telemetry-experiment-design`

### Boss / 关卡
`game-production + combat-design + level-design`

若比较角色适配覆盖：`+ meta-balance`

若装备是核心Encounter应对轴：`+ itemization-design`

### GDD
`game-production + 必要专业 Skill + design-review + game-design-doc`

## 英雄设计证据链

复杂英雄任务优先按需要形成：

`Design Intent -> Hero Concept -> Hero Kit -> Stat Progression -> Skill Values -> Formula -> Config/Code -> Simulation -> Runtime -> Telemetry -> Meta -> Playtest`

各层职责：

- Design Intent：为什么要有这个角色；
- Hero Concept：角色是谁、承诺什么体验；
- Hero Kit：机制怎么兑现；
- Stat Progression：等级成长如何支撑体质和Scaling Source；
- Skill Values：技能等级如何分配数值预算；
- Formula：乘区与数学结构；
- Config/Code：项目实际怎么执行；
- Simulation：Rotation、极端值、敏感性与分布；
- Runtime：真实实现是否一致；
- Telemetry：真实玩家行为；
- Meta：角色池与队伍生态；
- Playtest：理解、反馈、节奏、乐趣。

任何前一层都不能替代后一层证据。

## 装备/数值生产证据链

`Design Intent -> External Benchmark(optional) -> Itemization/Build Rules -> Formula -> Config/Code -> Simulation -> Runtime -> Telemetry -> Meta -> Playtest`

外部商业游戏的 `reference-data` 只能证明参考来源事实，不能自动升级为当前项目 verified。

## Private Project Isolation

用户提供真实项目代码、表、日志可以用于：

- 验证通用 Skill 是否覆盖真实生产问题；
- 提取不含业务细节的方法，例如 deterministic seed、Golden Test、Schema Guard、Runtime parity、Hero Contract、Stat Curve Guard、Skill Curve Guard、Loot funnel；
- 发现通用反模式与缺失能力。

不得写入公开通用 Skill：

- 私有项目名；
- 私有角色/技能/装备/表名；
- 私有ID；
- 私有代码路径；
- 私有真实公式；
- 私有英雄基础属性、技能倍率、装备数值、掉率、经济数据；
- 未公开业务规则。

若需要项目专属适配，应单独保存在用户项目私有 workspace，不污染通用 Skill。

## 已有项目规则

根据任务需要优先检查：

1. 用户确认规则；
2. 设计文档；
3. 配置表；
4. 代码与测试；
5. Runtime / 日志；
6. Telemetry / 实验；
7. 地图与内容；
8. 当前制作和技术约束。

外部参考只能进入“参考层”，不能覆盖以上项目真源。

关键证据缺失时继续完成独立可做部分，并明确未知项。

## 边界

- 不替专业 Skill 完成详细设计。
- 不把模拟、Spreadsheet、Telemetry相关性或理论分析描述成“已验证好玩”。
- 不把外部游戏的角色等级上限、技能等级倍率、属性成长、公式、装备掉率、词条数量、套装倍率或实验结果直接复制成本项目标准。
- 不因为三款成熟游戏都使用某结构，就自动把它标为当前项目最佳实践。
- 不保存无意义中间状态。