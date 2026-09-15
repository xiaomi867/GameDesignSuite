---
name: telemetry-experiment-design
description: 负责游戏埋点、指标体系、玩家分群、漏斗、留存/行为分析、A/B测试、实验设计、统计显著性、样本偏差与线上验证。用于把“感觉有问题”转成可测量假设，并判断数值/系统改动在线上是否真的有效，不把相关性误写成因果。
---

# 游戏 Telemetry 与实验设计

目标是建立从**设计问题 -> 可观察行为 -> 事件数据 -> 指标 -> 假设检验 -> 决策**的完整证据链。

优先读取：

- [Telemetry & Experiment Method](references/telemetry-and-experiment-method.md)
- [Telemetry Source Map](references/telemetry-source-map.md)
- [Experiment Plan Template](templates/experiment-plan.md)

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
