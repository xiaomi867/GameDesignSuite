---
name: balance-design
description: 负责游戏数值策划与平衡，包括属性、技能倍率、DPS/HPS、控制覆盖率、成长曲线、敌我强度、掉落/价格参数、难度曲线和横向强度比较。用于提出候选数值、建立公式、模拟和验证，不把理论计算冒充真实 Playtest。
---

# 数值策划与平衡

目标不是“让数字看起来顺”，而是把目标体验转译成可测量行为、数值模型、参数和验证闭环，并让数值长期支持角色定位、成长节奏、经济健康和内容难度。

涉及全局数值骨架、体验锚点、宏观时间线、属性价值锚点、长线与局内数值关系、数值可读性、商业约束或外部数值模板迁移时，优先读取 [Numerical System Architecture](references/numerical-system-architecture.md)。

跨类型能力比较、极端组合、属性交换率、成长强度或复杂验证时，优先读取 [Power Budget & Validation](references/power-budget-and-validation.md)。

涉及角色基础属性、速度/行动频率、共享技能资源、能量循环、命中/抵抗、目标权重、装备词条预算或类似回合制 RPG 理论计算时，优先读取 [HSR-Inspired Theorycrafting Patterns](references/hsr-theorycrafting-patterns.md)。

## Result-Level Professional Context

每一个独立数值判断、强度结论、候选值、Benchmark 结论或极端验证结果前，按 `../game-design/references/professional-context-header.md` 输出一次结果级 Header。

只有当前结果核心是“强度/倍率/曲线/概率/Power Delta 是否合理”时，`balance-design` 才主责。

如果当前结果只是：

- 字段值、漏配、引用错位 -> `config-audit` 主责；
- 代码枚举、Parser、运行时执行 -> `code-verification` 主责；
- 公式数学结构、Clamp、Round、单位 -> `formula-verification` 主责；
- 大规模重复试验、分布、敏感性 -> `simulation-design` 主责；
- 线上指标、埋点、A/B -> `telemetry-experiment-design` 主责；
- 角色池、组合生态、版本强度 -> `meta-balance` 主责；
- 成长成本结构 -> `progression-design` 主责；
- 资源生命周期/产销根因 -> `economy-design` 主责。

相邻结果即使专业组合相同，也重复显示 Header。

---

## 0. 数值合法性先于数值精度

一个方案数学上能闭环，不代表设计上合理。

在调参数前先确认：

- 这个参数/成本/奖励为什么存在；
- 它服务什么玩家体验；
- 它是否符合系统职责与玩家认知；
- 是否只是为了补库存、补参与度、补留存或补营收而强行制造；
- 是否把结构问题伪装成数值问题。

如果资源 Sink、成长成本、跨系统绑定或机制本身不合理，禁止通过调倍率、价格、消耗量把它“平衡到可用”。应退回 `economy-design / progression-design / game-production / design-review` 先验证设计合法性。

---

## 1. 先做 Experience Anchor，再做参数

标准顺序：

`Experience Target -> Observable Behavior -> Metric -> Numerical Model -> Parameters -> Validation`

禁止：

`先拍参数 -> 再找理由解释参数`

### 体验目标示例

- Boss 在目标 Build 下通常存活 20~30 秒；
- 防御升级应让玩家多承受约一次关键攻击；
- 一次突破应有明显 Power Delta，但不直接跳过下一内容层；
- 某周常资源应形成一次真实选择，而不是固定税；
- 速度提升只有在真实窗口增加行动/施法时才产生完整价值。

### 指标要接近体验

根据任务选择：

- TTK / TTD；
- DPS / HPS / EHP；
- Actions-to-Kill；
- Enemy Actions Survived；
- Buff Uptime；
- Control Coverage；
- Time-to-Upgrade；
- Resource Coverage Days；
- Clear Rate；
- Realized Casts / Actions；
- Build/Choice Diversity。

不要用一个方便计算但与体验脱节的指标替代真正目标。

---

## 2. 建立 Numerical Architecture，而不是孤立调点

全局数值问题先区分至少四层：

1. **Macro Pacing / Timeline**：Session、章节、天/周、赛季、账号时间线；
2. **Economy**：Source、Sink、Stock、Conversion、Price、Scarcity；
3. **Progression**：等级、突破、星级、装备、技能、能力解锁；
4. **Combat / Moment-to-Moment**：伤害、治疗、防御、速度、控制、资源、Gauge。

这是跨类型分析框架，不是强制功能列表。

不要因为传统资料写“社会/经济/养成/战斗”，就要求所有项目必须有“社会模块”。不同品类按实际系统映射。

至少检查：

`Power Curve <-> Cost Curve <-> Content Curve <-> Time Curve`

局部数值修复不能破坏其他层。

---

## 3. Benchmark Contract

任何比较必须建立可复现 Benchmark。

根据任务固定：

- 等级/突破/星级；
- 技能等级；
- 装备品质与词条预算；
- 队友/阵容；
- 敌人等级、防御、抗性；
- 敌人攻击频率/行为；
- 战斗时间窗；
- 单体/群体/Elite/Boss；
- 初始资源；
- 随机模型/Seed（若相关）。

不同练度、不同敌人、不同战斗时长的结果不能直接横比。

当结论依赖 Benchmark 时，输出中必须说明 Benchmark 或注明缺失。

---

## 4. 建立模型，并拆乘区

根据任务建立必要模型，例如：

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

所有变量写明：

- 单位；
- 来源；
- 是否可调；
- 定义域；
- 证据状态。

公式本身复杂或需要还原代码时，交给 `formula-verification + code-verification`。

---

## 5. Power Budget 与 Context Discount

比较不同类型收益时，不只看面板值。

必要时拆为：

- Raw Power：基础输出/治疗/生存；
- Effective Power：考虑命中、覆盖率、Target、TTK 后的实际价值；
- Situational Power：只在特定敌人/血线/阶段生效；
- Synergy Power：依赖 Build、队友、触发链；
- Cost：资源、CD、条件、风险、机会成本。

概念式：

`Effective Value = Raw Value × Uptime × Applicability × Reliability × Context Factor - Cost`

该式是分析框架，不是通用精确公式。

条件越苛刻、覆盖率越低、场景越窄，应做 Context Discount。

伤害、治疗、防御、控制和功能卡不能用单一“+X%”直接等价。

---

## 6. Attribute Value Anchor / 属性交换率

可以建立属性预算语言，但禁止使用固定跨项目比例作为真理。

例如：

`ATK : DEF : HP = 1 : 1 : 10`

默认只能是 `example-heuristic`，除非当前项目通过自己的公式、Benchmark 和验证正式确认。

### 推荐推导

1. 固定 Benchmark；
2. 单独扰动一个属性；
3. 计算目标指标变化；
4. 在不同阶段/敌型重复；
5. 得到 Exchange Rate 区间；
6. 再用于装备、成长、Buff 的初步预算。

可用：

`Marginal DPS = ΔDPS / ΔATK`

`Marginal EHP = ΔEHP / ΔDEF`

`Marginal Survival = ΔEnemyActionsSurvived / ΔHP`

必须始终记住：

`Stat Budget != Effective Combat Value`

实际价值仍会被乘区、阈值、上限、覆盖率、Build 饱和、队伍和 Encounter 改变。

---

## 7. Action Economy、资源循环与能量循环

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

可使用：

`PerActionValue × ActionsPerWindow`

以及：

`NetSharedResource = Generated - Consumed`

判断角色在 Rotation 中是 Resource Positive / Neutral / Negative。

能量类机制要区分固定回能、受倍率影响回能、击杀/受击/追击回能与溢出。不要默认所有回能都吃同一个“回能效率”。

---

## 8. Stat Budget、Breakpoint 与阈值收益

装备、被动、套装和 Buff 可以转换成统一预算单位做初步横比，但不能把预算直接等同实战。

实际价值受：

- 乘区稀释；
- 速度阈值；
- 命中阈值；
- 能量循环阈值；
- 暴击方差；
- 角色已有属性；
- 技能适用范围；
- 套装条件与覆盖率；
- 上限/软上限。

速度、行动频率、命中和回能尤其要做 Breakpoint Analysis。

只有跨过“多一次行动/稳定命中/提前一轮大招”等离散阈值时，边际价值才可能显著跃升。

不要脱离真实战斗窗口追求固定阈值。

---

## 9. 成长曲线

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
- Power Curve / Cost Curve / Content Curve / Time Curve 是否同步。

推荐把：

- 平滑等级成长；
- 突破节点跳变；
- 能力解锁；
- 固定/半固定维度；

分开建模。

速度、能量上限、攻击间隔等不必因为“是属性”就强制随等级增长。

区分线性、指数、分段、软上限等曲线，并说明为什么使用。

成长结构问题由 `progression-design` 主责；具体 Power Delta 可由 `balance-design` 主责。

---

## 10. 概率、命中与随机奖励

有概率时不能只看平均值。

至少根据任务检查：

- Base Probability；
- Effective Probability；
- EV；
- 方差；
- P50/P90/P95；
- 连续失败/成功概率；
- Hard Pity / Soft Pity；
- Reset / Guarantee；
- 多段独立判定 vs 一次判定；
- 玩家感知公平性。

Debuff/控制应计算实际可靠性，可抽象为：

`RealChance = BaseChance × HitFactor × ResistFactor × SpecificResistFactor`

Target 若采用权重随机：

`P(target i) = Weight_i / Σ Weight`

不要把“更容易被打”当成绝对锁定。

随机奖励不能只用单抽显示概率判断。保底会改变分布，也可能改变长期有效获得率。

禁止把“100~200抽”“1%~80%”之类外部经验直接写成本项目硬规则；应结合价格、免费流入、最坏成本、重复价值、池周期和体验目标重新建模。

复杂随机分布、Monte Carlo 或置信区间交给 `simulation-design`。

---

## 11. Numerical Readability / 数值可读性

玩家对数字的感知与 UI 表达是数值设计的一部分，但禁止设定跨项目固定“可感知数字区间”。

检查：

- 数量级是否符合品类与幻想；
- 玩家是否能感知升级差异；
- 小数精度是否有意义；
- 是否需要 K/M/B/万/亿等缩写；
- 百分比是否比原始数更清楚；
- 是否出现无意义大数膨胀；
- UI 是否能突出关键 Delta / Breakpoint。

涉及玩家感知阈值时，将外部心理学/社区经验标记为假设，并通过实际 UI/Playtest 或 Telemetry 验证。

---

## 12. Secondary Gauge / 第二战斗轴

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

---

## 13. 横向平衡与生态边界

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
- 不同敌型/关卡适用面；
- 机会成本；
- 隐性收益；
- 行动经济；
- 共享资源净贡献；
- 状态命中可靠性。

不要只比较面板攻击力。

当问题扩大到：

- 角色池整体；
- 队伍/组合；
- Pair Lock；
- Counter Matrix；
- Power Creep；
- 版本 Meta；

切换 `meta-balance` 主责，`balance-design` 提供局部数值模型。

---

## 14. 先定区间，再定点值

步骤：

1. 明确 Experience Target；
2. 建 Benchmark；
3. 给合理区间；
4. 说明参数上调/下调的行为影响；
5. 选择 Candidate；
6. 横向比较；
7. 极端场景压力测试；
8. 必要时 Simulation；
9. 再决定是否收敛。

不要因为配置表能填某个数，就认为该数合理。

---

## 15. 极端组合与回归检查

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

需要批量试验、参数扫描、Monte Carlo 时使用 `simulation-design`。

---

## 16. 商业目标与外部模板的边界

商业目标可以是约束，但不能自动成为唯一数值目标。

采用：

`Experience Target + Business Constraint + Economy Sustainability + Fairness Boundary + Production Reality`

禁止仅为了收入目标：

- 制造没有系统语义的强制消耗；
- 把成长卡点变成 Mandatory Tax；
- 破坏已有 Build 只为推动替换；
- 用短期收入掩盖长期经济崩坏。

“成功项目模板”可以迁移方法和结构，但不能默认迁移具体参数。

统一规则：

`Template Structure can transfer. Template Values require project re-validation.`

外部游戏的：

- 成长率；
- 属性比值；
- 防御公式常数；
- 保底次数；
- 商店价格；
- Win Rate 阈值；
- 速度阈值；

都默认为参考样本，不是本项目标准。

---

## 17. 经济与技能协作

### 经济参数

涉及资源产销、价格、货币价值时与 `economy-design` 协作。

数值策划不能因为“库存太多”就主动创造消耗；先检查 Resource Role、Sink Legitimacy、Source 是否过高和生命周期是否断层。

### 技能数值

涉及技能时与 `skill-design` 配合。机制不可修改时，只调整 Tunables，例如：

- 倍率；
- CD；
- 持续；
- 概率；
- 阈值；
- Buff 数值；
- 消耗；
- 初始资源。

技能机制、Target、状态机由 `skill-design` 主责；代码生效由 `code-verification` 主责。

---

## 18. 外部数值模拟器 / Numerical Tooling

对于复杂项目，建议维护独立于客户端表现层的数值模型或模拟器，用于：

- 读取/镜像必要配置；
- 展示公式中间乘区；
- 固定 Benchmark；
- 参数扫描；
- 100/1000/10000+ 次重复试验；
- 分布与尾部风险；
- Sensitivity；
- Breakpoint；
- Regression。

推荐链路：

`Config/Input -> Normalized Variables -> Formula Buckets -> Timeline/Event Model -> Random Model -> Metrics -> Regression`

但外部模拟器不能取代 Runtime Source of Truth。

有代码/运行时证据时，应做：

`Simulator <-> Formula <-> Code <-> Runtime`

一致性校验。

---

## 19. 输出规范

### 单一参数/对象

正式建议至少包含：

| 对象 | 指标/字段 | 当前值 | 候选值 | Benchmark | 数值理由 | 设计合法性 | 风险 | 验证 |
|---|---|---:|---:|---|---|---|---|---|

### 复杂战斗

建议附：

- Damage Block Breakdown；
- Rotation；
- Resource Net Flow；
- Action Count；
- Breakpoint；
- Buff Uptime；
- Hit Reliability；
- Extreme Case。

### 全项目数值骨架

根据任务选择输出：

- Experience Targets；
- Numerical Architecture Map；
- Benchmark Contracts；
- Attribute Value Anchor；
- Combat Formula Map；
- Progression Curves；
- Economy Flow；
- Content Difficulty Curve；
- Probability Distribution Model；
- Simulator Plan；
- Validation Matrix。

不要为了“完整”默认生成所有文档。

若当前值未知，不编造，标 `unknown`。

---

## 20. 验证等级

### Theory / Formula / Spreadsheet

证明内部一致性、候选区间、理论边界。

### Simulation

证明模型下的分布、敏感性、尾部和极端结果。

### Controlled Runtime

确认实现是否符合设计/公式。

### Telemetry / Experiment

验证真实玩家行为、真实结果和版本影响。

### Playtest

才能支持“好玩、挫败、节奏、理解、可读性”等体验性结论。

复杂数值任务优先形成证据链：

`Design Intent -> Formula -> Config/Code -> Simulation -> Runtime -> Telemetry -> Meta -> Playtest`

低层证据不能冒充高层证据。

结论优先标：

- `candidate`
- `verified-config`
- `verified-code`
- `verified-runtime`
- `verified-data`
- `not-yet-playtested`

不要使用笼统 `verified` 混淆证据层级。

---

## 21. 反模式

- **Math-washing**：用漂亮公式掩盖不合理机制；
- **Parameter-first Design**：先拍数字，再补理由；
- **Balance-by-Tax**：通过增加成本解决结构问题；
- **Average-only Balance**：只看均值不看方差和极端组合；
- **Single-axis Balance**：只用 DPS/面板值比较跨类型能力；
- **Single-hit Fallacy**：只比较单次倍率，不看行动次数/循环；
- **Threshold Blindness**：把速度、命中、回能当连续线性收益；
- **Stat-budget = Power**：把词条预算直接当实战价值；
- **Universal Ratio Fallacy**：把某项目 ATK/DEF/HP 比值当通用真理；
- **Perception Hardcode**：把某数字区间/百分比阈值当跨游戏认知法则；
- **Pity-by-Rule-of-Thumb**：凭“行业常见100~200抽”直接定保底；
- **Successful Template Copying**：复制成功项目具体数值而不重新推导；
- **Revenue-first Override**：用营收目标覆盖体验、经济健康和公平边界；
- **Cross-scale Leakage**：用局内倍率修复长线经济问题，或反过来；
- **Spreadsheet = Playtest**：把模拟/表格结果当体验证据；
- **Local Optimum**：局部数值合理但破坏经济、成长、Meta 或内容节奏。
