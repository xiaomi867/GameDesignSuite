# Game Design Suite Chat Edition — Balance / Formula / Simulation / Telemetry / Meta

> Purpose: project knowledge for ordinary Chat mode. This file is NOT a Skill and does not depend on Skill/Plugin runtime.
> The assistant should use the relevant sections as professional guidance, while distinguishing verified evidence from candidate design.

## Usage

- Use this file when the current decision object belongs to **Balance / Formula / Simulation / Telemetry / Meta**.
- For cross-system work, also consult the smallest necessary supporting knowledge files.
- Do not claim that a Skill was invoked. Say which professional domain or project knowledge was used when useful.
- User-fixed mechanics are constraints, not redesign targets, unless the user explicitly reopens them.


---

# Source Module: gds-balance-design

# Canonical Detailed Guidance

> Preserved from the canonical Game Design Suite specialist. The runtime wrapper is intentionally compact; this file retains the detailed domain rules, workflows, guards, anti-patterns, and done criteria.

# 数值策划与平衡

目标不是“让数字看起来顺”，而是把目标体验转译成可测量行为、数值模型、参数和验证闭环，并让数值长期支持角色定位、成长节奏、经济健康和内容难度。

涉及全局数值骨架、体验锚点、宏观时间线、属性价值锚点、长线与局内数值关系、数值可读性、商业约束或外部数值模板迁移时，优先读取 [Numerical System Architecture](numerical-system-architecture.md)。

跨类型能力比较、极端组合、属性交换率、成长强度或复杂验证时，优先读取 [Power Budget & Validation](power-budget-and-validation.md)。

涉及角色基础属性、速度/行动频率、共享技能资源、能量循环、命中/抵抗、目标权重、装备词条预算或类似回合制 RPG 理论计算时，优先读取 [HSR-Inspired Theorycrafting Patterns](hsr-theorycrafting-patterns.md)。

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


---

# Source Module: gds-formula-verification

# Canonical Detailed Guidance

> Preserved from the canonical Game Design Suite specialist. The runtime wrapper is intentionally compact; this file retains the detailed domain rules, workflows, guards, anti-patterns, and done criteria.

# 游戏公式验证

本 Skill 的职责不是“拍一个看起来合理的公式”，而是把公式变成**可追溯、可复算、可与代码/配置交叉验证、可做边界测试**的生产资产。

涉及公式审计时，优先读取：

- [Formula Audit Method](formula-audit-method.md)
- [HSR Formula Reference](hsr-formula-reference.md)
- [ZZZ Formula Reference](zzz-formula-reference.md)
- [Formula Source Map](formula-source-map.md)

## 强制用户可见输出协议（MUST）

无论用户是否提醒，每一个独立公式结论、公式差异、推导、反例、边界问题或修改建议之前，都先显示：

```text
【本次专业视角】
主责：公式 / 数值验证（formula-verification）
协同：仅列当前结果真实使用的专业
```

常见协同：

- `code-verification`：确认公式在代码里实际怎么写、执行顺序、Clamp、Round、类型转换；
- `config-audit`：确认公式输入字段、配置值、单位和默认值；
- `balance-design`：判断公式产生的强度曲线、收益率和数值区间是否合理；
- `combat-design`：确认公式是否符合战斗规则、窗口、Target、状态机；
- `skill-design`：确认技能公式的 Source/Target/Trigger 与设计意图一致；
- `progression-design`：确认等级、突破、星级等成长公式；
- `economy-design`：确认价格、资源流速、兑换等经济公式。

如果当前结果只是“代码实际上怎么执行”，应切换 `code-verification` 主责；如果只是“这个倍率是否平衡”，切换 `balance-design` 主责；如果只是“字段填错”，切换 `config-audit` 主责。

## 1. 先建立 Formula Identity

任何公式在验证前先锁定身份：

| 字段 | 必填内容 |
|---|---|
| Formula ID | 稳定名称，例如 `PlayerDamage.Physical` |
| Purpose | 这个公式解决什么问题 |
| Scope | PVE/PVP、普通攻击/技能/DoT、客户端/服务器等 |
| Source of Truth | 设计文档、代码、配置、运行时日志 |
| Inputs | 输入变量 |
| Units | 百分比/整数/秒/帧/点数等 |
| Output | 输出意义与单位 |
| Order | 运算顺序 |
| Bounds | Clamp/Min/Max |
| Rounding | floor/ceil/round/truncate |
| Timing | 结算时机 |
| Snapshot | 快照还是动态读取 |
| Owner | 谁维护公式 |

如果连 Formula Identity 都没有锁定，不进入“这个公式合理不合理”的阶段。

## 2. 先还原真实公式，再讨论设计

证据优先级：

`verified-runtime > verified-code > verified-config > confirmed design > supported-inference > candidate`

若用户给了代码：

1. 找输入字段；
2. 找解析；
3. 找中间变量；
4. 找运算顺序；
5. 找 Clamp/Round；
6. 找最终 Consumer；
7. 写成数学表达式；
8. 用测试向量复算。

不得仅根据字段名或历史文档猜公式。

## 3. 公式审计的七层检查

### A. Algebra / 代数正确性

- 括号是否正确；
- 加算/乘算是否放错层；
- 分母是否可能为 0；
- 负数是否允许；
- 百分数是否重复除以 100；
- 是否存在整数除法、溢出、精度损失。

### B. Dimension / 单位一致性

检查：

- 秒 vs 毫秒 vs 帧；
- 百分比 `20` vs `0.2`；
- 伤害点数 vs 倍率；
- 攻速 vs 攻击间隔；
- 角度/距离/格子；
- 等级系数与实际等级。

单位不一致时，先修单位，不进入平衡判断。

### C. Domain / 定义域

对每个输入给出：

- 最小值；
- 最大值；
- 合法范围；
- 空值/0/负值；
- 极端 Buff/叠层后范围。

### D. Monotonicity / 单调性

确认设计上应该“越高越强”的变量是否真的单调。

例如：

- 攻击力增加不应在某区间降低伤害；
- 减伤增加不应产生负承伤；
- 速度增加不应因为取整导致长期反向收益，除非有明确 Breakpoint；
- 防御穿透超过目标防御后如何处理必须明确。

### E. Marginal Value / 边际收益

检查一阶变化：

`ΔOutput / ΔInput`

关注：

- 线性；
- 递增收益；
- 递减收益；
- 阈值跳变；
- 软上限/硬上限；
- 乘区稀释；
- 多乘区是否形成爆炸增长。

### F. Boundary / 极端边界

至少测试相关项：

- 0 攻击 / 0 防御；
- 100% 暴击；
- 暴击率 >100%；
- 抗性 <0 / >100%；
- 减伤 =100% / >100%；
- 攻速极高 / 攻击间隔趋近 0；
- 大量叠层；
- 多 Buff 同层叠加；
- 目标死亡/无敌/复活；
- Gauge 已满/已空；
- 资源溢出；
- 同帧多次触发。

### G. Inversion / 反解

必要时反解公式，例如：

- 想让 TTK=20s，需要多少 DPS？
- 想保证 95% 命中，需要多少 Effect Hit？
- 想在 60s 内多行动 1 次，需要多少速度？
- 想把承伤降到 70%，需要多少防御/减伤？

反解有助于发现公式是否支持策划目标。

## 4. 乘区与顺序必须显式化

任何复杂伤害公式都优先写成乘区链，而不是一句“攻击×倍率”。

推荐抽象：

`Final = Base × Crit × DamageBonus × Defense × Resistance × Vulnerability × Mitigation × State × Special`

项目可以有不同乘区，但必须明确：

- 同乘区内是加算还是乘算；
- 不同乘区之间是否相乘；
- Clamp 在乘区前还是后；
- 取整发生在哪一层；
- 是否对 DoT/Break/反击/追击区别处理；
- Buff 读取快照还是动态属性。

## 5. 概率公式不能只看期望值

有随机时至少同时检查：

- 单次概率；
- EV；
- 方差；
- 连续 N 次失败/成功概率；
- P50/P90/P95；
- 保底/伪随机；
- 多段独立判定 vs 一次总判定；
- 暴击/命中是否每段单独 Roll。

例如多段命中：

`P(at least one success) = 1 - Π(1 - p_i)`

不要用“平均命中率”替代真实分布。

## 6. 行动与时间公式必须同时看离散结果

对于速度、攻击间隔、CD、行动条：

- 连续数学值只是中间结果；
- 最终价值往往由“是否多一次行动/多一次技能/多一次 Boss 窗口”决定。

因此必须报告：

- Continuous Value；
- Discrete Breakpoint；
- Realized Actions / Casts；
- Overcap/Waste。

## 7. Snapshot / Dynamic 是公式的一部分

对于 DoT、异常、Buff、护盾、治疗持续效果，必须确认：

- 施加时快照哪些属性；
- Tick 时重新读取哪些属性；
- 目标侧抗性/易伤何时读取；
- 多个角色共同贡献时如何加权；
- Buff 到期后已生成实例是否变化。

如果代码/资料没有证据，不猜。

## 8. 参考游戏公式只做 Pattern Comparator

崩铁、绝区零等外部公式只能用于：

- 识别常见乘区拆法；
- 学习防御/抗性/命中/行动等建模方式；
- 对照边际收益和 Breakpoint；
- 寻找反例和压力测试场景。

禁止：

- 因为参考游戏这么算，就直接要求本项目照抄；
- 把社区理论计算当官方源码事实；
- 忽略本项目节奏、等级、属性规模和目标体验；
- 用参考游戏当前版本数值反推本项目必然合理区间。

## 9. 与代码交叉验证

当代码可用时，推荐最短链：

`Config/Input -> Data Model -> Parser -> Formula Function -> Clamp/Round -> Runtime Consumer -> Final Result`

输出至少说明：

- 文件/类/方法；
- 公式原文；
- 还原后的数学表达式；
- 示例输入；
- 代码输出；
- 手算输出；
- 是否一致；
- 误差来源。

## 10. Test Vector / 测试向量

每个关键公式至少准备：

1. Normal Case；
2. Zero/Empty Case；
3. Lower Bound；
4. Upper Bound；
5. Breakpoint Case；
6. Extreme Stack Case；
7. Regression Case。

若是概率/随机公式，增加 Monte Carlo 或枚举验证。

## 11. 输出规范

每个公式结论建议使用：

| Formula | 当前公式 | 问题 | 证据 | 影响 | 候选公式 | 状态 | 验证 |
|---|---|---|---|---|---|---|---|

复杂公式附：

- Variable Table；
- Formula Blocks；
- Unit Table；
- Test Vectors；
- Boundary Results；
- Sensitivity / Breakpoint；
- Code Cross-check。

## 12. 证据状态

优先使用：

- `verified-formula-design`：正式设计公式明确；
- `verified-config`：输入/参数由真实配置确认；
- `verified-code`：代码公式和执行顺序已确认；
- `verified-runtime`：实际运行/日志复现；
- `supported-inference`：多项证据支持但未直接验证；
- `candidate`：候选公式；
- `unverified`：缺必要证据；
- `externally-blocked`：当前环境无法继续。

不要因为手算结果“看起来对”就标 `verified-runtime`。

## 13. 典型反模式

- **Formula-by-Intuition**：公式靠经验拍，没有目标和边界；
- **Math Washing**：用复杂公式掩盖错误设计；
- **Hidden Bucket**：文档写加算，代码实际乘算或反之；
- **Percent Unit Bug**：20 与 0.2 混用；
- **Integer Division Bug**：整数除法把比例截断；
- **Order-of-Operations Drift**：文档与代码括号不同；
- **Unbounded Multiplier**：乘区无上限导致极端组合爆炸；
- **Negative Defense Leak**：穿透后负防御未定义；
- **Over-100 Probability**：概率未 Clamp；
- **Snapshot Ambiguity**：持续效果快照规则不明确；
- **Reference Copying**：把参考游戏公式直接复制成本项目；
- **Average-only Validation**：只看均值不看分布和极端值；
- **Spreadsheet = Runtime**：表格算对就声称实现正确。


---

# Source Module: gds-simulation-design

# Canonical Detailed Guidance

> Preserved from the canonical Game Design Suite specialist. The runtime wrapper is intentionally compact; this file retains the detailed domain rules, workflows, guards, anti-patterns, and done criteria.

# 游戏数值模拟与仿真

目标不是“多跑几次随机数”，而是建立**可复现、可解释、能验证假设、能定位因果参数**的模拟实验。

优先读取：

- [Simulation Method](simulation-method.md)
- [Simulation Source Map](simulation-source-map.md)
- [Simulation Spec Template](../templates/simulation-spec.md)

## 强制用户可见输出协议（MUST）

每一个独立模拟结论、分布结论、参数敏感性、稳定性判断或模拟方案前，都先显示：

```text
【本次专业视角】
主责：数值模拟 / 仿真（simulation-design）
协同：仅列当前结果真实使用的专业
```

常见协同：

- `formula-verification`：确认模拟里的公式与乘区；
- `balance-design`：定义 Benchmark、强度目标、候选区间；
- `code-verification`：确认生产代码与模拟模型是否同义；
- `config-audit`：确认输入参数与真实配置；
- `meta-balance`：批量英雄、Build、队伍和内容组合的 Meta 仿真；
- `economy-design` / `progression-design`：长期经济与成长状态演化。

## 1. 先定义 Simulation Question

禁止先写模拟器，再找问题。

至少明确：

- Decision：这次模拟要帮助决定什么；
- Hypothesis：什么变化可能导致什么结果；
- Model Scope：模拟哪些系统，不模拟哪些；
- Inputs：固定参数、随机参数、策略参数；
- Outputs：要观测哪些指标；
- Horizon：一次攻击、一场战斗、一局、一天、30天、一个版本；
- Replications：需要多少重复；
- Seed Policy：随机种子如何管理；
- Stop Rule：什么时候认为样本足够；
- Evidence Boundary：模拟最多证明到哪一层。

## 2. 模型分层

根据问题选择最小充分模型：

### Formula Model
纯公式、无状态或低状态，用于单次伤害、治疗、概率、边际收益。

### Rotation / Timeline Model
按时间或行动序列推进，用于攻速、CD、回能、Buff Uptime、Burst Window。

### Discrete Event Simulation
以事件队列推进，用于技能触发、波次、状态、资源、死亡、复活、Boss 阶段。

### Monte Carlo
当随机事件、目标选择、暴击、掉落、卡牌选择、事件路线等造成分布时使用。

### Agent / Policy Simulation
当玩家选择会改变结果时，必须显式定义策略，而不是假装“随机代理=真实玩家”。

### Meta / Long-Horizon Simulation
用于数周成长、经济、内容消费、阵容生态。应与 `meta-balance` 或经济/成长 Skill 协作。

## 3. Determinism / 可复现性

每次正式模拟必须能复现：

- 固定输入快照；
- 记录随机种子；
- 记录模型版本；
- 记录配置版本；
- 记录策略代理版本；
- 避免依赖系统时间、未记录外部状态；
- 同 seed + 同输入应产生同结果。

若生产战斗本身是确定性帧同步或可注入随机源，模拟器优先复用同等语义，而不是另造一套“相似公式”。

## 4. Ground Truth Contract

模拟器的规则来源优先级：

`verified-runtime > verified-code > verified-config > confirmed design > candidate model`

必须区分：

- Production Logic：真实项目规则；
- Simulation Approximation：为了速度做的近似；
- Agent Assumption：玩家/AI行为假设；
- Scenario Assumption：敌人、Build、时间窗假设。

任何近似都要记录，不得静默偏离生产逻辑。

## 5. 输出必须看分布，不只看均值

随机模拟至少根据问题报告：

- N；
- Mean；
- Median；
- Std / Variance；
- P10 / P25 / P75 / P90 / P95；
- Min / Max（注意异常值）；
- Failure Rate / Death Rate / Clear Rate；
- Confidence Interval（必要时）；
- Tail Risk。

例如 1000 次平均 TTK=20s 不代表体验稳定。如果 P90=42s，长尾可能才是主要问题。

## 6. Replication Count 不是固定神数

100 / 1000 / 10000 只是常见采样规模，不是质量等级。

选择 N 应考虑：

- 方差；
- 需要检测的最小差异；
- 尾部事件概率；
- 计算成本；
- 置信区间宽度；
- 是否需要跨多个场景/策略。

对低概率事件，可用更多样本、重要性采样、解析概率或专门边界测试；不要用有限样本宣称“不可能发生”。

## 7. Parameter Sweep / 参数扫描

不要只跑“当前值”和“候选值”。必要时做：

- One-at-a-time Sweep；
- Grid Sweep；
- Random / Latin Hypercube sampling（复杂参数空间）；
- Local Sensitivity；
- Breakpoint Search；
- Threshold / Boundary Search。

输出：

`Input Change -> Output Delta -> Elasticity / Sensitivity`

重点找：

- 非线性；
- 临界点；
- 参数交互；
- 一点改动引发的大幅跳变；
- 多参数同时上调造成的乘法爆炸。

## 8. Counterfactual / 对照实验

一次只改一个关键变量，除非任务本身就是交互效应。

至少准备：

- Baseline；
- Candidate A/B；
- Negative Control（必要时）；
- Extreme Case；
- Regression Case。

如果多个参数一起变化，不能把最终差异归因给其中一个参数。

## 9. Agent / Player Model Guard

模拟玩家决策时必须定义策略：

- Random；
- Greedy；
- Rule-based；
- Risk-averse；
- Resource-saving；
- Expert-like；
- Search-based / MCTS / RL（必要时）。

至少问：

- 代理知道哪些信息；
- 代理优化什么；
- 是否有人类反应/认知限制；
- 是否能代表新手/熟练/专家；
- 结果对策略假设有多敏感。

**Bot Balance ≠ Human Balance。**

## 10. 战斗模拟指标

根据项目需要输出：

- Total Damage / DPS；
- Burst Damage；
- TTK；
- Damage Taken / TTD；
- Healing / HPS / Overheal；
- Shield Generated / Wasted Shield；
- Buff Uptime；
- Skill Cast Count；
- Action Count；
- Crit / Hit / Miss Distribution；
- Resource Generated / Consumed / Overflow；
- CC Uptime；
- Gauge / Break Count；
- Death / Clear Rate；
- Target Distribution。

## 11. 经济与成长模拟指标

长周期模拟可输出：

- Resource Stock Distribution；
- Daily / Weekly Net Flow；
- Time-to-Upgrade；
- Time-to-Purchase；
- Coverage Days；
- Bottleneck Frequency；
- Dead Currency Rate；
- Progression Milestone P50/P90；
- Player-state cohorts；
- Source/Sink contribution。

但资源“堆积”仍需先过 `economy-design` 的 Resource Role 判断，不能通过模拟自动证明“必须新增 Sink”。

## 12. Simulation vs Runtime

模拟结果不能自动升级为 `verified-runtime`。

若需要确认实现一致：

1. 用同一输入/seed 在模拟和真实 Runtime 跑；
2. 对比关键中间状态与最终结果；
3. 定位差异是公式、事件顺序、随机源、取整还是状态机；
4. 建立 Golden Test / Regression Vector。

## 13. Done Criteria

一次模拟任务至少交付：

- Question/Hypothesis；
- 输入与固定条件；
- 模型类型；
- 随机源与 seed；
- 策略代理；
- 样本量依据；
- 输出指标；
- 分布结果；
- 敏感性/边界；
- 模型限制；
- 下一步 Runtime / Telemetry / Playtest 验证。

## 14. 反模式

- **Mean-only Simulation**：只有平均值；
- **Magic N**：把1000次当万能充分样本；
- **Random Bot = Player**：随机决策代理冒充玩家；
- **Silent Approximation**：模拟规则与真实代码不同却不记录；
- **Unseeded Randomness**：问题无法复现；
- **Parameter Soup**：一次改很多变量，无法归因；
- **Simulation = Playtest**：模拟证明不了“好玩”；
- **No Tail Check**：忽略P90/P95长尾；
- **No Regression Vector**：修一次后无法防回归；
- **Optimize to Simulator**：为了模拟指标好看，把设计过拟合给代理。


---

# Source Module: gds-telemetry-experiment-design

# Canonical Detailed Guidance

> Preserved from the canonical Game Design Suite specialist. The runtime wrapper is intentionally compact; this file retains the detailed domain rules, workflows, guards, anti-patterns, and done criteria.

# 游戏 Telemetry 与实验设计

目标是建立从**设计问题 -> 可观察行为 -> 事件数据 -> 指标 -> 假设检验 -> 决策**的完整证据链。

优先读取：

- [Telemetry & Experiment Method](telemetry-and-experiment-method.md)
- [Telemetry Source Map](telemetry-source-map.md)
- [Experiment Plan Template](../templates/experiment-plan.md)

## 强制用户可见输出协议（MUST）

每一个独立埋点建议、指标解释、数据结论、实验方案或因果判断前，都先显示：

```text
【本次专业视角】
主责：数据分析 / 实验设计（telemetry-experiment-design）
协同：仅列当前结果真实使用的专业
```

常见协同：

- `balance-design`：定义平衡问题和数值假设；
- `meta-balance`：角色/阵容/Build生态指标；
- `simulation-design`：上线前建立预期分布与实验先验；
- `game-production`：把体验目标转成行为信号；
- `economy-design` / `progression-design`：资源、成长、留存指标；
- `code-verification`：确认事件是否真实触发、字段是否可信。

## 1. 从 Decision 开始，不从“多埋点”开始

任何分析先明确：

- Decision：最终要做什么决定；
- Observation：当前看到什么症状；
- Hypothesis：怀疑什么机制导致症状；
- Behavior Signal：玩家会出现什么可观察行为；
- Metric：用什么量化；
- Confounders：哪些因素会混淆；
- Decision Rule：看到什么结果才改/不改。

禁止“能埋的都埋”。事件必须服务于问题或长期通用诊断。

## 2. Event Schema 记录事实，不记录推断

埋点优先记录**发生了什么**，而不是客户端替分析层下结论。

例如优先：

- `skill_selected`
- `damage_resolved`
- `wave_started`
- `wave_completed`
- `resource_changed`

而不是：

- `player_is_confused=true`
- `build_is_bad=true`

每个事件至少明确：

- event_name；
- timestamp / sequence；
- player/session/run id；
- build/version/config version；
- context（mode/stage/wave等）；
- entity ids；
- before/after state（必要时）；
- reason/source；
- experiment/variant id（若参与实验）；
- schema version。

## 3. 粒度原则

记录到**最小仍可解释和重建关键行为**的粒度。

太粗：只能知道“输了”，不知道为什么。

太细：事件量巨大、成本高、分析困难，还可能引入隐私/性能问题。

优先保证：

- 可重建关键漏斗；
- 可定位失败点；
- 可拆角色/技能/Build/关卡；
- 可按版本回放指标定义；
- 不依赖 UI 文案作为稳定 ID。

## 4. Metric Taxonomy

根据任务从以下层级选指标：

### Outcome Metrics
胜率、通关率、留存、转化、时长、死亡率、经济健康度等最终结果。

### Behavior Metrics
Pick Rate、技能使用率、换人、重试、放弃、资源消费、Build形成率。

### Diagnostic Metrics
伤害构成、Buff Uptime、触发率、目标分布、资源溢出、失败原因。

### Guardrail Metrics
崩溃率、退出率、异常时长、付费伤害、某群体体验恶化等“不能变坏”的指标。

一个实验只看 Primary KPI 而没有 Guardrail，容易得到局部最优。

## 5. 分群先于总体均值

至少根据问题考虑：

- 新手 / 熟练 / 高熟练；
- 新角色熟练度；
- 付费/非付费（仅在合法且必要时）；
- 进度阶段；
- 队伍/Build类型；
- 关卡/模式；
- 平台/版本；
- 新老玩家；
- 是否第一次接触机制。

总体 50% 胜率可能掩盖“新手35%、高手65%”。

## 6. Balance Data 不等于只有 Win Rate

角色/Build平衡至少按问题组合：

- Pick Rate；
- Win/Clear Rate；
- Ban/Presence（适用的竞技游戏）；
- Matchup；
- Team/Composition performance；
- Move/Skill usage；
- Damage/Healing/Resource contribution；
- Mastery Curve；
- Player-skill buckets；
- Frustration/qualitative feedback；
- Sample Size / uncertainty。

低样本高胜率不能直接等价为“过强”。

## 7. A/B Test 基本结构

正式实验至少写清：

- Hypothesis；
- Control；
- Treatment；
- Unit of Randomization（玩家/账号/队伍/公会等）；
- Eligibility；
- Traffic Split；
- Primary Metric；
- Guardrails；
- Minimum Detectable Effect；
- Sample Size / Duration；
- Analysis Window；
- Exclusion Rules；
- Stop / Rollback Rule；
- Interaction with concurrent experiments。

## 8. 随机化与 SRM

实验上线后优先检查 Sample Ratio Mismatch（SRM）。

若预期 50/50，但实际样本严重偏离：

- 先查随机分桶；
- 崩溃/日志缺失；
- Eligibility；
- 跨设备/跨账号污染；
- Treatment 导致事件不上报；
- 版本差异。

在 SRM 未解释前，不急着解读 Treatment 的 KPI 提升。

## 9. 统计显著 ≠ 设计显著

同时看：

- Effect Size；
- Confidence Interval；
- p-value / Bayesian interval（团队方法任选其一但要一致）；
- Sample Size；
- Practical Significance；
- Guardrail movement。

超大样本下 0.1% 变化也可能显著，但不一定值得改设计。

## 10. 避免常见因果错误

### Selection Bias
高熟练玩家更爱选某角色，角色高胜率可能部分来自玩家群体。

### Survivorship Bias
只分析完成关卡的人，会忽略中途流失者。

### Simpson's Paradox
总体趋势可能与分群趋势相反。

### Novelty Effect
新内容上线短期使用率高不代表长期健康。

### Learning Curve
新角色刚上线的低胜率可能来自学习成本。

### Regression to Mean
极端指标自然回落不能全部归功于改动。

### Concurrent Change
版本同时改了多个系统时，单一归因困难。

## 11. Mastery Curve / 学习曲线

角色、武器、Build或机制若有学习成本，至少比较：

- first 1-3 uses；
- 5-10 uses；
- 20+ uses（按项目调整）；
- 同一玩家纵向表现；
- 玩家基础Skill分层。

不要看到首周低胜率就立即大幅Buff。

## 12. Telemetry 与模拟互证

上线前：

`formula -> simulation -> expected distribution`

上线后：

`telemetry -> observed distribution`

然后比较：

- Mean/Median；
- Tail；
- Trigger frequency；
- Build distribution；
- Strategy mix；
- Runtime mismatch。

差异可能来自玩家策略，而不一定是公式实现错误。

## 13. 数据质量检查

正式分析前至少检查：

- 缺失率；
- 重复事件；
- 事件顺序；
- 时区/时间戳；
- schema/version混用；
- 非法值；
- bot/test账号；
- 版本污染；
- 采样策略；
- 客户端事件是否可伪造；
- server authority 是否需要。

垃圾输入不会因为图表漂亮就变成证据。

## 14. 隐私与最小化

只收集支持产品决策所需的数据。

- 避免无目的敏感数据；
- 稳定 ID 与个人身份分离；
- 遵守项目适用的隐私、同意、留存和删除政策；
- 不因为“以后可能有用”无限收集。

## 15. Done Criteria

一次 Telemetry / Experiment 任务至少交付：

- Decision / Hypothesis；
- Event/Schema；
- Metric definitions；
- Segments；
- Data quality checks；
- Experiment design（若需要）；
- Analysis method；
- Decision threshold；
- Guardrails；
- Evidence boundary；
- Follow-up。

## 16. 反模式

- **Log Everything**：没有问题导向的埋点堆积；
- **Inference Event**：客户端直接上报“玩家困惑”等推断；
- **Win Rate Monoculture**：只用胜率判断平衡；
- **No Segmentation**：只看总体均值；
- **p-value Worship**：显著就等于值得改；
- **No SRM Check**：分桶坏了还继续解释实验；
- **Metric Fishing**：实验结束后到处找显著指标；
- **Learning Curve Blindness**：忽视角色熟练度；
- **Telemetry = Causality**：观察相关性就下因果结论；
- **Experiment Collision**：并发实验相互污染；
- **No Guardrail**：主KPI提升但其他体验崩坏。


---

# Source Module: gds-meta-balance

# Canonical Detailed Guidance

> Preserved from the canonical Game Design Suite specialist. The runtime wrapper is intentionally compact; this file retains the detailed domain rules, workflows, guards, anti-patterns, and done criteria.

# Meta / 版本级平衡

目标是从“一个对象是否合理”上升到“整个选择生态是否健康”。

优先读取：

- [Meta Balance Framework](meta-balance-framework.md)
- [Meta Balance Source Map](meta-balance-source-map.md)
- [Meta Balance Audit Template](../templates/meta-balance-audit.md)

## 强制用户可见输出协议（MUST）

每一个独立Meta结论、Roster异常、组合风险、版本趋势或系统性平衡建议前，都先显示：

```text
【本次专业视角】
主责：Meta / 版本平衡（meta-balance）
协同：仅列当前结果真实使用的专业
```

常见协同：

- `balance-design`：单体Power Budget与候选改动；
- `simulation-design`：预上线组合矩阵和代理仿真；
- `telemetry-experiment-design`：线上Pick/Win/Usage/Segment证据；
- `skill-design` / `combat-design`：解释角色工具、Counter与战斗阶段；
- `level-design`：检查内容环境是否系统性偏袒某类Build。

## 1. 平衡对象不是只有角色

根据项目建立实际生态单位：

- Hero / Character；
- Skill / Card；
- Item / Equipment；
- Build / Archetype；
- Team / Composition；
- Enemy / Encounter；
- Map / Mode；
- Difficulty tier；
- Player skill/mastery cohort。

Meta问题往往来自对象之间的关系，不是某个对象单独数值错误。

## 2. 建立 Balance Matrix

至少按任务建立一个或多个矩阵：

### Roster Matrix
角色 × 关键指标。

### Matchup Matrix
对象A × 对象B 的相对结果。

### Synergy Matrix
组合后收益是否显著超过个体预期。

### Counter Matrix
是否存在有效反制，以及反制成本。

### Content Coverage Matrix
角色/Build × 关卡/敌人/模式。

### Cohort Matrix
角色/Build × 玩家技能/熟练度。

矩阵的作用是发现“局部合理、整体挤压”。

## 3. 不用一个总胜率统治所有判断

根据游戏类型组合：

- Pick / Usage Rate；
- Win / Clear Rate；
- Ban / Presence（适用时）；
- Matchup；
- Team/Composition win rate；
- Role/Position performance；
- Skill/Move usage；
- Build diversity；
- Experienced-player performance；
- First-use vs mastered performance；
- Sample size / uncertainty；
- Frustration / qualitative feedback。

低Pick高Win可能是小样本、高手专属、反制位或隐藏强势；必须继续分解。

## 4. Player Segment / Skill Band

不同玩家层可以存在不同平衡问题。

至少在需要时分：

- 新手；
- 主流熟练度；
- 高熟练；
- 顶尖/竞技；
- 角色新手 vs 角色专精者。

不要因为高端环境健康，就默认新手环境健康；反之亦然。

## 5. Mastery Curve

角色强度必须区分：

- Entry Power；
- Learning Slope；
- Mastered Power；
- Execution Reliability。

新角色上线早期低胜率可能来自学习曲线。高熟练度角色在总体50%时也可能在专精群体过强。

## 6. Accessibility of Power

同样的理论强度，如果一个角色的强工具更容易、更稳定地兑现，其实战生态压力可能更大。

记录：

- Setup Cost；
- Execution Difficulty；
- Counterplay visibility；
- Reliability；
- Error Punishment；
- Recovery。

平衡不能只看最终上限。

## 7. Synergy / Pair Lock

检查组合：

`Observed Pair Value` vs `Expected Independent Value`

重点识别：

- multiplicative synergy；
- infinite/near-infinite loops；
- resource engine；
- permanent uptime；
- unique state detonator；
- mandatory partner；
- one-composition dominance。

强联动本身不是问题；如果没有合理机会成本或替代组合，才会造成Pair Lock。

## 8. Counter Health

一个健康Counter通常满足：

- 玩家能理解；
- 可在合理时机选择；
- 成本可接受；
- 不要求完全放弃自己的Build；
- 不只是“免疫/封死”；
- 被Counter方仍有恢复或二次决策。

如果只能靠Boss/敌人全面免疫某体系来平衡，优先判为系统性设计风险。

## 9. Diversity Metrics

多样性不是“每个对象Pick完全相等”。

可观察：

- Viable Pool Size；
- Top-N usage concentration；
- Herfindahl-Hirschman Index (HHI) 或其他集中度；
- Archetype share；
- Composition diversity；
- Matchup polarization；
- Number of meaningful alternatives。

角色天然人气不同，不能把Popularity直接当Power。

## 10. Power Creep

每个版本记录：

- Baseline power distribution；
- 新内容相对旧内容的Power Delta；
- Top percentile变化；
- 内容TTK/TTD变化；
- 老内容Clear Rate；
- 新机制覆盖旧机制的比例；
- 是否需要全局抬敌人来追赶玩家。

### Power Creep 信号

- 新角色必须明显更强才能被选；
- 新装备普遍替代旧装备；
- Boss只能靠更高HP/免疫应对；
- 老角色需要连续数值Buff才能生存；
- Build选择越来越集中。

## 11. Systemic vs Local Fix

发现Meta问题后先分类：

### Local
一个角色/技能/物品过强，可局部调参。

### Interaction
两个或多个对象组合失控，需要改交互、资源或条件。

### Environment
当前关卡/敌人/模式系统性偏袒一种策略。

### Systemic
底层公式、装备系统、资源经济、Counter结构或奖励机制导致全局偏斜。

不要用十几个局部Nerf掩盖一个系统性根因。

## 12. Patch Risk / 版本风险

任何改动都检查：

- direct targets；
- indirect beneficiaries；
- indirect victims；
- existing counters；
- item/build ripple；
- low/high skill cohorts；
- old content；
- new player experience；
- future content assumptions。

物品、共享资源、通用机制的改动通常比单角色改动波及更广。

## 13. Pre-Analytics + Live Analytics

上线前：

`formula/balance -> simulation -> predicted matrix`

上线后：

`telemetry -> observed matrix`

比较：

- 预测强度与真实胜率；
- 代理策略与真实Pick；
- 预期Counter与真实Counter；
- 预期Build多样性与真实集中度。

差异本身就是重要设计信息。

## 14. Done Criteria

一次Meta评审至少交付：

- Scope与版本；
- Player cohorts；
- Matrix；
- Sample size / uncertainty；
- Outliers；
- Diversity / concentration；
- Synergy/Counter；
- Power creep；
- Root-cause classification；
- Candidate changes；
- Ripple risk；
- Simulation/Telemetry验证计划。

## 15. 反模式

- **50% Win Rate Worship**：总体50%就宣称平衡；
- **Pick Rate = Power**：把人气等同强度；
- **No Skill Buckets**：忽视玩家水平；
- **No Mastery Curve**：忽视角色学习成本；
- **Pair Lock Blindness**：单体正常但组合必选；
- **Counter by Immunity**：靠完全免疫解决体系过强；
- **Patch Whack-a-Mole**：不断局部修补系统性问题；
- **Power Creep Normalization**：通过全体敌人加血适配新角色膨胀；
- **Small Sample Ranking**：低样本对象硬排名；
- **Environment Blindness**：内容环境偏斜被误判为角色数值问题。
