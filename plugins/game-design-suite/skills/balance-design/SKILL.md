---
name: balance-design
description: 负责游戏数值策划与平衡，包括属性、技能倍率、DPS/HPS、控制覆盖率、成长曲线、敌我强度、掉落/价格参数、难度曲线和横向强度比较。用于提出候选数值、建立公式、模拟和验证，不把理论计算冒充真实 Playtest。
---

# 数值策划与平衡

目标不是“让数字看起来顺”，而是让数值稳定支持目标体验、角色定位、成长节奏和系统经济。

跨类型能力比较、极端组合、成长强度或复杂验证时，优先读取 [Power Budget & Validation](references/power-budget-and-validation.md)。

涉及角色基础属性、速度/行动频率、共享技能资源、能量循环、命中/抵抗、目标权重、装备词条预算或类似回合制 RPG 理论计算时，优先读取 [HSR-Inspired Theorycrafting Patterns](references/hsr-theorycrafting-patterns.md)。

## Result-Level Professional Context

每一个独立数值判断、强度结论、候选值、Benchmark 结论或极端验证结果前，按 `../game-design/references/professional-context-header.md` 输出一次结果级 Header。

只有当前结果核心是“强度/倍率/曲线/概率/Power Delta 是否合理”时，`balance-design` 才主责。若当前结果只是发现配置字段不一致，应由 `config-audit` 主责；若只是解释代码枚举/运行时语义，应由 `code-verification` 主责；若是成长成本结构或经济根因，应分别由 `progression-design` / `economy-design` 主责。

相邻结果即使专业组合相同，也重复显示 Header。

## 0. 数值合法性先于数值精度

一个方案数学上能闭环，不代表设计上合理。

在调参数前先确认：

- 这个参数/成本/奖励为什么存在；
- 是否符合系统职责与玩家认知；
- 是否只是为了补库存、补参与度、补留存而强行制造；
- 是否把结构问题伪装成数值问题。

如果资源 Sink、成长成本、跨系统绑定本身不合理，禁止通过调倍率、价格、消耗量把它“平衡到可用”。应退回 `economy-design / progression-design / game-production` 先验证设计合法性。

## 1. 先确定体验目标与 Benchmark

在选具体数字前明确：

- 角色/系统定位；
- 目标强度；
- Benchmark；
- 期望 TTK / HPS / 生存时长 / 控制覆盖；
- 玩家阶段；
- 内容难度；
- 允许的波动与风险；
- 哪些机制不可修改；
- 当前参数所属系统是否合理。

Benchmark 必须可重复。根据任务固定：

- 等级/突破/星级；
- 技能等级；
- 装备品质与词条预算；
- 队友；
- 敌人等级、防御、抗性；
- 战斗时间窗；
- 单体/群体/Elite/Boss 场景。

不要拿不同练度、不同敌人、不同战斗时长的结果直接横比。

## 2. 建立模型，并拆乘区

根据任务建立必要公式，例如：

- 单次伤害；
- 期望 DPS；
- HPS；
- EHP；
- Burst Window；
- Crit EV；
- Buff Uptime；
- CC Coverage；
- Resource per Minute / Rotation；
- Cost/Benefit；
- Break-even；
- Growth per Level/Star；
- Enemy-to-Player Power Ratio。

复杂伤害不要只写成“攻击 × 倍率”。优先拆成：

`Final = Base × Crit × DamageBonus × Defense × Resistance × Vulnerability × Mitigation × State`

具体项目可以少于或多于这些乘区，但必须明确：

- 加算还是乘算；
- 所属层；
- 上下限；
- 生效对象；
- 覆盖率；
- 与其他 Buff 是否同乘区稀释。

所有变量写明单位、来源、是否可调和证据状态。

## 3. Power Budget 与 Context Discount

比较不同类型收益时，不只看面板值。

必要时把总价值拆为：

- Raw Power：基础输出/治疗/生存；
- Effective Power：考虑命中、覆盖率、Target、TTK 后的实际价值；
- Situational Power：只在特定敌人/血线/阶段生效的价值；
- Synergy Power：依赖 Build、队友、触发链的附加价值。

条件越苛刻、覆盖率越低、场景越窄，应给予相应折价（Context Discount）。

伤害、治疗、防御、控制和功能卡不能用单一“+X%”直接等价。

## 4. Action Economy、资源循环与能量循环

对回合制、自动战斗、技能循环类游戏，单次技能强度不足以代表角色强度。

至少检查：

- 单位时间/周期行动次数；
- 额外行动/追击/反击；
- 行动提前/延后；
- 技能 CD；
- 攻击间隔/速度；
- 共享资源净流量；
- 怒气/能量大招循环；
- 行动是否触发队友收益。

可以使用：

`PerActionValue × ActionsPerWindow`

以及：

`NetSharedResource = Generated - Consumed`

来判断角色在 Rotation 中是 Resource Positive / Neutral / Negative。

能量类机制要区分固定回能、受倍率影响回能、击杀/受击/追击回能与溢出。不要默认所有回能都吃同一个“回能效率”。

## 5. Stat Budget、Breakpoint 与阈值收益

装备、被动、套装和 Buff 可转换成统一的“有效词条/预算单位”做初步横比，但：

`Stat Budget ≠ Effective Combat Value`

因为实际价值受：

- 乘区稀释；
- 速度阈值；
- 命中阈值；
- 能量循环阈值；
- 暴击方差；
- 角色已有属性；
- 技能适用范围；
- 套装条件与覆盖率；

影响。

速度、行动频率、命中和回能尤其要做 Breakpoint Analysis。只有跨过“多一次行动/稳定命中/提前一轮大招”等离散阈值时，边际价值才可能显著跃升。

不要脱离真实战斗窗口追求固定阈值。

## 6. 先定区间，再定点值

步骤：

1. 选 Benchmark；
2. 给合理区间；
3. 说明参数上调/下调的行为影响；
4. 选择 Candidate；
5. 横向比较；
6. 极端场景压力测试；
7. 再决定是否收敛。

不要因为配置表能填某个数，就认为该数合理。

## 7. 横向平衡

比较同阶段对象时至少考虑：

- 输出；
- 生存；
- 控制；
- 治疗/辅助；
- 目标选择价值；
- 条件触发难度；
- 资源成本；
- 技能循环；
- Build Synergy；
- 对不同敌型/关卡的适用面；
- 机会成本；
- 隐性收益（例如缩短 TTK 带来的生存收益）；
- 行动经济；
- 共享资源净贡献；
- 状态命中可靠性。

不要只比较面板攻击力。

## 8. 成长曲线

检查：

- Lv1 基准；
- 分段成长；
- 突破/星级节点；
- 单次收益；
- 累积收益；
- 低级与高级内容匹配；
- 上限；
- 资源成本；
- 是否产生阶段性断层；
- Power Curve / Cost Curve / Content Curve 是否同步。

推荐把“平滑等级成长”与“突破节点跳变”分开建模，并允许速度、能量上限、攻击间隔等维度按项目需要保持固定，而不是所有属性一起涨。

区分线性、指数、分段、软上限等曲线，说明使用原因。

## 9. 概率、命中与目标权重

有概率时同时检查：

- EV；
- 方差；
- P50/P90 等分布（必要时）；
- 极端连败/连胜；
- 保底；
- 玩家感知公平性。

Debuff/控制应计算实际可靠性，而不是只看 Base Chance。可抽象为：

`RealChance = BaseChance × HitFactor × ResistFactor × SpecificResistFactor`

Target 若采用权重随机，应显式计算：

`P(target i) = Weight_i / Σ Weight`

不要把“更容易被打”当成绝对锁定。

平均值正确不代表体验公平。

## 10. Secondary Gauge / 第二战斗轴

如果游戏存在韧性、护甲槽、Break、Stagger、Poise 等第二 Gauge，必须纳入 Power Budget。

检查：

- Gauge Max；
- 每技能 Gauge Damage；
- Break Trigger；
- Break Reward；
- Recovery；
- Boss Resistance；
- 角色对该 Gauge 的贡献；
- 是否出现只打 HP 或只打 Gauge 的主导策略。

功能角色若主要贡献第二 Gauge，不能只按直接 DPS 评估。

## 11. 极端组合与回归检查

正式改数值时至少考虑相关极端情况：

- 最高暴击/攻速；
- 最低 CD；
- 多 Buff 乘算；
- 无限/高层叠加；
- 重复触发；
- 高 Uptime；
- 极低/极高血线阈值；
- Boss 免控/减益抗性；
- 多角色联动；
- 额外行动导致共享资源转负；
- 行动提前导致 Buff 窗口错位；
- 旧内容与新内容的强度回归。

若一个改动只在平均场景合理、极端组合失控，不能标记为已平衡。

## 12. 经济参数协作

涉及资源产销、价格、货币价值时与 `economy-design` 协作。

数值策划不能因为“库存太多”就主动创造消耗；先检查 Resource Role、Sink Legitimacy、Source 是否过高和生命周期是否断层。

## 13. 技能数值协作

涉及技能时与 `skill-design` 配合。机制不可修改时，只调整 Tunables，例如：

- 倍率；
- CD；
- 持续；
- 概率；
- 阈值；
- Buff 数值；
- 消耗；
- 初始资源。

## 14. 输出规范

正式参数建议至少包含：

| 对象 | 指标/字段 | 当前值 | 候选值 | 基准 | 数值理由 | 设计合法性 | 风险 | 验证 |
|---|---|---:|---:|---|---|---|---|---|

复杂战斗建议附加：

- Damage Block Breakdown；
- Rotation；
- Resource Net Flow；
- Action Count；
- Breakpoint；
- Buff Uptime；
- Hit Reliability；
- Extreme Case。

若当前值未知，不编造，标 `unknown`。

## 15. 验证等级

### 理论验证
公式、表格、Simulation，可证明内部一致性和候选区间。

### Controlled Test
固定变量对照，可帮助判断因果。

### Runtime Data
实际构建、日志或 Telemetry，可验证真实表现。

### Playtest
才能支持“体验/好玩/挫败/节奏”等结论。

结论必须标记 `candidate / verified / not-yet-playtested`，若有具体证据层则优先使用 `verified-config / verified-code / verified-runtime / verified-data`。

## 16. 反模式

- **Math-washing**：用漂亮公式掩盖不合理机制；
- **Balance-by-Tax**：通过增加成本解决结构问题；
- **Average-only Balance**：只看均值不看方差和极端组合；
- **Single-axis Balance**：只用 DPS/面板值比较跨类型能力；
- **Single-hit Fallacy**：只比较单次倍率，不看行动次数/循环；
- **Threshold Blindness**：把速度、命中、回能当连续线性收益；
- **Stat-budget = Power**：把词条预算直接当实战价值；
- **Spreadsheet = Playtest**：把模拟结果当体验证据；
- **Local Optimum**：局部数值合理但破坏经济、成长或内容节奏。
