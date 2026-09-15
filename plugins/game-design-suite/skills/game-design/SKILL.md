---
name: game-design
description: 游戏设计通用入口。用户提出玩法、系统、体验、规则、平衡、公式、模拟、Telemetry、A/B实验、Meta生态、技能、战斗、装备/Itemization、外部装备Benchmark、经济、成长、关卡、UI、配置、实现验证、评审或 GDD 等游戏设计问题时使用。负责自动选择并协调最小充分的专业 Skill，不要求用户预先判断专业边界。无论用户是否提醒，每个独立正式结果前都必须显示【本次专业视角】并标出主责/协同。
---

# 游戏设计总入口

> **强制用户可见输出协议（MUST / DEFAULT）**
>
> 只要本套件正在回答游戏设计/策划相关任务，用户不需要在 Prompt 里额外要求“显示专业视角”。
>
> 每一个独立正式结果、Finding、字段修改、代码语义、数值判断、模拟结论、数据结论、Meta判断、装备/Itemization结论、外部装备Benchmark结论、经济结论、成长方案、技能判断或关卡方案之前，都必须先显示：
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
- 装备词条很多 ≠ Build一定丰富；
- 橙装掉率高 ≠ 实际Upgrade Rate高；
- 三个成熟游戏都这么做 ≠ 当前项目应该照搬。

## Symptom-to-Root-Cause Rule

遇到局部症状至少检查：

1. **Local**：字段、倍率、奖励、单个对象；
2. **System**：战斗、装备、经济、成长、内容、公式或数据链本身；
3. **Cross-system**：上下游系统、生命周期、内容环境、玩家分层、版本生态。

只有局部根因成立时才做局部补丁。

## Missing Evidence Guard

当任务需要配置、代码、Telemetry、Playtest、地图、文档、外部详情页或其他证据但当前不可访问：

1. 只做一次必要可用性检查；
2. 依赖缺失证据的结论标 `unverified` / `externally-blocked`；
3. 列出最小缺失材料；
4. 继续所有不依赖缺失证据的工作；
5. 不从字段名、旧版本、相似游戏或公开资料补成当前项目事实；
6. 外部详情页不可访问时，不从记忆补精确等级/强化值；
7. 用户明确“不猜”时严格停在证据边界。

## 路由

### `game-production`
核心体验、玩法循环、系统规则、产品节奏、教程、奖励框架、制作约束、范围与跨系统设计。

### `design-frameworks`
MDA、Core Loop、Flow、设计张力、Pattern、Depth vs Complexity 等方法论。

### `combat-design`
战斗规则、攻击/受击、Target、状态、AI、资源、战斗节奏、遭遇结构。

### `skill-design`
英雄/角色技能机制、Target、Buff/Debuff、触发、状态机、升级与构筑关系。

### `balance-design`
倍率、属性、DPS/HPS/EHP、控制覆盖、Power Budget、成长强度、参数区间、横向强度。

### `formula-verification`
伤害/治疗/护盾/防御/抗性/暴击/命中/攻速/行动/概率等公式还原、单位、乘区、Clamp/Round、定义域、边界与代码交叉验证。

### `simulation-design`
Monte Carlo、离散事件、Rotation/Timeline、参数扫描、策略代理、100/1000/10000次分布、敏感性、长周期状态模拟。

### `telemetry-experiment-design`
埋点、事件Schema、指标、玩家分群、漏斗、A/B测试、SRM、显著性、因果边界与线上验证。

### `meta-balance`
多角色/Build/队伍/内容生态、Matchup/Synergy/Counter矩阵、Pick/Win/Presence、Mastery、Power Creep、版本风险与多样性。

### `itemization-benchmark`
公开商业游戏的装备、武器、遗器、圣遗物、声骸等参考数据抽取、等级/强化曲线、结构归一化、跨游戏 Benchmark、可迁移模式与迁移边界。首批参考覆盖崩坏：星穹铁道、原神、鸣潮。只负责外部参考，不替代当前项目最终设计。

### `itemization-design`
当前项目装备/Itemization系统、槽位、品质、基础/主/副词条、词条池与权重、随机Roll、强化、套装、唯一特效、Loot可用率、替换/毕业、分解回收、Best-in-Slot与Build生态。

### `economy-design`
资源Role、Sources/Sinks、库存、流速、价值锚、兑换、通胀、产销闭环。

### `progression-design`
等级、星级、突破、技能树、解锁、成长节奏、追赶、长期上限。

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

### 英雄技能
`skill-design + balance-design`

已有表：`+ config-audit`

需确认实现：`+ code-verification`

复杂公式：`+ formula-verification`

定稿：`+ design-review`

### 外部装备对标
`itemization-benchmark + itemization-design`

比较具体属性/特效强度：`+ balance-design`

比较等级/突破/强化曲线：`+ progression-design`

比较毕业概率与随机层：`+ simulation-design`

比较套装/专武生态：`+ meta-balance`

外部来源精确值缺失时执行 `externally-blocked`，不从记忆补值。

### 装备 / Itemization
`itemization-design + balance-design + progression-design`

涉及外部商业游戏参考：`+ itemization-benchmark`

涉及掉落、强化材料、分解、商店：`+ economy-design`

复杂随机词条/毕业时间：`+ simulation-design`

多角色BiS、Build集中、版本生态：`+ meta-balance`

已有表/代码：`+ config-audit + code-verification`

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

## 数值生产证据链

复杂数值任务优先按需要形成：

`Design Intent -> External Benchmark(optional) -> Itemization/Build Rules -> Formula -> Config/Code -> Simulation -> Runtime -> Telemetry -> Meta -> Playtest`

其中：

- External Benchmark：只在用户需要外部游戏参考/对标时出现；
- Itemization/Build Rules：只在装备/物品化相关任务出现；
- Design Intent：为什么存在；
- Formula：数学结构是否正确；
- Config/Code：项目实际怎么执行；
- Simulation：预期分布、极端值、敏感性；
- Runtime：真实实现是否一致；
- Telemetry：真实玩家行为与结果；
- Meta：整个选择生态是否健康；
- Playtest：体验、可读性、挫败、乐趣。

外部商业游戏的 `verified-data` 只能证明参考来源事实，不能自动升级为当前项目 verified。

低层证据不能冒充高层结论。

## Private Project Isolation

用户提供真实项目代码、表、日志可以用于：

- 验证通用 Skill 是否覆盖真实生产问题；
- 提取不含业务细节的方法，例如 deterministic seed、Golden Test、Schema Guard、Runtime parity、Loot funnel、Dead-affix guard；
- 发现通用反模式与缺失能力。

不得写入公开通用 Skill：

- 私有项目名；
- 私有角色/技能/装备/表名；
- 私有ID；
- 私有代码路径；
- 私有真实公式；
- 私有装备数值、掉率、经济数据；
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
- 不把外部游戏的阈值、公式、装备掉率、词条数量、套装倍率、强化曲线或精炼/谐振参数直接复制成本项目标准。
- 不因为三款成熟游戏都使用某结构，就自动把它标为当前项目最佳实践。
- 不保存无意义中间状态。
