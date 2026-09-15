# Numerical Production Regressions

用于验证 Simulation / Telemetry / Meta Balance 三个专业能力不会退化成“多跑几次”“多埋点”“看胜率”。所有案例必须保持项目无关。

## Case 1 — 1000次不是自动充分

Prompt：

> 我跑1000次战斗平均DPS是1200，所以这个Build已经稳定了吗？

Expected：

- `simulation-design` 主责；
- 要求同时看方差、P90/P95、失败率/死亡率等与问题相关的分布；
- 说明样本量要由方差、最小有意义差异和尾部概率决定；
- 不得把1000视为通用充分样本。

## Case 2 — Seed 可复现

Prompt：

> 同一配置每次模拟结果都不一样，怎么排查？

Expected：

- 检查随机源、seed、配置/模型版本、系统时间和共享状态；
- 要求同输入+同seed可复现；
- 不得只建议“再多跑几次”。

## Case 3 — Random Bot 不代表玩家

Prompt：

> 随机AI下两个角色胜率都是50%，能证明平衡吗？

Expected：

- 否；
- 要检查代理策略、信息、熟练度、玩家目标；
- 建议多策略/多persona或真实数据验证；
- 模拟不冒充Playtest。

## Case 4 — 平均值掩盖长尾

Data：A方案平均TTK=20s、P90=45s；B方案平均TTK=21s、P90=27s。

Expected：

- 不只因A均值低就判A更好；
- 结合目标体验讨论尾部风险；
- `simulation-design + balance-design`。

## Case 5 — Telemetry 记录事实而非推断

Prompt：

> 我想埋一个 player_is_confused=true，玩家停顿5秒就上报。

Expected：

- 拒绝把“困惑”作为原始事实；
- 记录停顿、界面、上下文、重试/退出等可观察行为；
- 困惑作为后续推断或Playtest验证。

## Case 6 — 只看胜率 Fail

Prompt：

> 角色A总胜率50%，所以不用调了吧？

Expected：

- 继续检查Pick/Usage、Skill/Mastery buckets、Matchup、Composition、样本量、工具使用率和体验反馈；
- 不能仅凭50%宣布健康。

## Case 7 — 学习曲线

Data：新角色首3局胜率42%，20局以上玩家胜率55%。

Expected：

- 标记明显Mastery Curve；
- 不直接用42%做大幅Buff；
- 检查高熟练上限、学习成本和分群样本。

## Case 8 — SRM

Prompt：

> A/B计划50/50，最终A有60%、B有40%，B留存高2%，能发布B吗？

Expected：

- 先检查Sample Ratio Mismatch；
- 在随机化/日志/eligibility问题未解释前，不直接接受2%提升；
- 检查effect size、CI、guardrail。

## Case 9 — 显著不等于值得改

Data：p=0.01，但提升只有0.05%，且实现成本很高。

Expected：

- 区分Statistical Significance与Practical Significance；
- 结合成本和Guardrail做决策。

## Case 10 — Pair Lock

Data：角色A、B单独都正常，但A+B组合使用率和通关率远高于其他组合。

Expected：

- `meta-balance` 主责；
- 检查Synergy Matrix、资源循环、唯一交互、机会成本；
- 不必然同时Nerf两个角色的基础倍率。

## Case 11 — Content Environment Bias

Data：某远程角色在当前Boss胜率异常高，但其他内容正常。

Expected：

- 检查Content Coverage Matrix与Boss机制；
- 区分角色过强和环境偏袒；
- 不直接全局Nerf。

## Case 12 — Power Creep

Prompt：

> 新角色上线后都比旧角色强10%，旧角色再逐个Buff就行吗？

Expected：

- 标记Power Creep风险；
- 检查历史基准、内容TTK、旧内容膨胀、敌人随之加血等系统后果；
- 不把持续全体抬数值当健康版本治理。

## Case 13 — Simulation vs Runtime

Prompt：

> 模拟器和真实战斗同seed结果不同。

Expected：

- 对比公式、事件顺序、RNG stream、Clamp/Round、快照、状态机；
- 建立Golden Scenario；
- 模拟结果不能标`verified-runtime`。

## Case 14 — Public reference is not project truth

Prompt：

> Riot把53%当警戒线，我们所有项目也统一53%吧。

Expected：

- 拒绝直接复制阈值；
- 说明阈值取决于类型、样本、技能分层、目标多样性；
- 外部案例只做method comparator。

## Case 15 — Private project fixture isolation

Setup：用户上传某项目私有代码/配置帮助完善Skill。

Expected：

- 可以抽象出通用方法，例如seed、Golden Test、公式/Runtime分层、事件schema；
- 不把私有项目名称、表结构、公式、ID、文件路径或业务数据写入公开通用Skill；
- 通用Skill保持跨项目可复用。
