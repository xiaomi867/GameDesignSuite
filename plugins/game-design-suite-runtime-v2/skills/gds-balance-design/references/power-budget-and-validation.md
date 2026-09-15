# Power Budget & Validation

## 目的

用于跨类型能力比较、成长曲线、技能强度、属性价值锚点和极端组合验证。

## Power Budget

不要把不同类型价值直接用面板百分比等价。必要时拆成：

- Raw Power：直接伤害、治疗、防御；
- Effective Power：考虑命中、目标选择、覆盖率、TTK 后的实际价值；
- Situational Power：只在特定血线、敌型、阶段生效；
- Synergy Power：依赖队友、Build、触发链；
- Cost：资源、CD、条件、风险、机会成本。

可用概念式：

`Effective Value = Raw Value × Uptime × Applicability × Reliability × Context Factor - Cost`

该式用于组织思路，不应伪装成通用精确公式。

## Attribute Value Anchor / 属性价值锚点

可以建立属性之间的预算语言，但禁止把固定比值当成跨项目真理。

例如：

`ATK : DEF : HP = 1 : 1 : 10`

最多只能是某个项目、某个阶段、某套公式和某个 Benchmark 下的 `example-heuristic`，不能自动升级成通用标准。

推荐做法：

1. 固定 Benchmark；
2. 对单一属性做小幅扰动；
3. 测量目标指标的边际变化；
4. 在低/中/高阶段和不同敌型重复；
5. 得到 Exchange Rate 区间，而不是永久常数。

例如：

`Marginal DPS = ΔDPS / ΔATK`

`Marginal EHP = ΔEHP / ΔDEF`

`Marginal Survival = ΔEnemyActionsSurvived / ΔHP`

具体使用 DPS、EHP、TTK、TTD、Clear Rate 还是其他指标，应由体验目标决定。

必须区分：

`Stat Budget != Effective Combat Value`

预算只是生产近似，实战价值仍受乘区、阈值、上限、覆盖率、Build 饱和度、队伍与 Encounter 影响。

## Context Discount

条件越苛刻，折价越大。常见折价来源：

- 低触发率；
- 低覆盖率；
- 目标限制；
- 需要前置 Build；
- 需要队友；
- Boss 免疫；
- 血线条件；
- 延迟生效；
- 高风险站位。

## 隐性收益

伤害可能额外带来：

- 缩短 TTK；
- 减少敌方行动次数；
- 更容易通过 DPS Check；
- 提前触发击杀收益；
- 降低治疗/防御压力。

防御/治疗/控制也可能有对应隐性收益。跨类型比较必须纳入。

## Breakpoint 与非线性

属性价值不一定连续线性。特别检查：

- 速度是否多一次实际行动；
- 回能是否提前一轮大招；
- 命中是否跨过可靠性门槛；
- 防御/抗性是否受公式软上限影响；
- 暴击是否受上限与方差影响；
- 资源是否从净正转为净负。

不能只用局部导数或面板百分比替代离散结果。

## 极端组合

至少根据相关性检查：

- 最高攻速；
- 最高暴击；
- 最低 CD；
- 多 Buff 乘算；
- 叠层上限；
- 重复触发；
- 100% Uptime；
- 多角色联动；
- Boss 免控/抗性；
- 新旧内容强度回归。

## 验证层级

- Formula/Spreadsheet：内部一致性；
- Simulation：分布、敏感性和极端值；
- Controlled Runtime：实现是否符合预期；
- Telemetry：真实群体表现；
- Playtest：体验、挫败、节奏、理解。

低层证据不能替代高层结论。

## 常见错误

- 用 DPS 一轴比较所有能力；
- 把平均值当体验；
- 把模拟当 Playtest；
- 用数值把不合理机制“洗平衡”；
- 只验证平均 Build，不测极端组合；
- 局部平衡破坏经济/成长/内容节奏；
- 把外部游戏属性比值当作本项目 Value Anchor；
- 把词条预算直接当成实战强度。
