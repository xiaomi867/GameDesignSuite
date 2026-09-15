---
name: simulation-design
description: 负责游戏数值与系统的可重复模拟、参数扫描、Monte Carlo、离散事件仿真、Bot/策略代理、长期经济与成长模拟。用于回答“100/1000/10000次会怎样、分布是否稳定、哪个参数最敏感、极端组合会不会失控”，不把模拟结果冒充真实玩家体验。
---

# 游戏数值模拟与仿真

目标不是“多跑几次随机数”，而是建立**可复现、可解释、能验证假设、能定位因果参数**的模拟实验。

优先读取：

- [Simulation Method](references/simulation-method.md)
- [Simulation Source Map](references/simulation-source-map.md)
- [Simulation Spec Template](templates/simulation-spec.md)

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
