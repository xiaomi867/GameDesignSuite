# Theorycrafting & Roguelite Regression Evals

这些用例用于防止引入参考游戏方法后，Skill 退化成“照抄数值”或“只会算单次倍率”。

## T1 Single-hit Fallacy

**Prompt**

> A 技能倍率 600%，B 技能倍率 450%，所以 A 一定更强，对吗？

**Expected**

- 不直接判 A 更强；
- 检查行动频率、CD、资源、Target、Buff、追击/反击、Burst Window；
- 必要时比较 `PerActionValue × ActionsPerWindow`；
- 给出缺失信息与 candidate 判断。

## T2 Speed Threshold Must Bind to Content Window

**Prompt**

> 速度 134 是不是一定比 133 强很多？

**Expected**

- 不迷信固定速度阈值；
- 先问/确认战斗时间窗、波次、Boss 阶段、行动公式；
- 只有跨过额外行动或 Rotation Breakpoint 时才判定离散增益；
- 不把其他游戏速度阈值照搬。

## T3 Shared Resource Net Flow

**Prompt**

> 四个角色单体强度都很高，为什么队伍打起来资源总不够？

**Expected**

- 计算 Rotation 级资源生成与消耗；
- 标记 Resource Positive / Neutral / Negative；
- 检查额外行动/加速是否放大消耗；
- 不只看个人 DPS。

## T4 Base Chance Is Not Real Chance

**Prompt**

> 技能写 100% 概率眩晕，所以 Boss 一定会被控吧？

**Expected**

- 区分 Base Chance、命中、通用抗性、专属抗性、免疫；
- 未知公式时不编造；
- 对普通怪/Elite/Boss 分层；
- 不能把文本 100% 等价为运行时必定成功。

## T5 Stat Budget Is Not Combat Value

**Prompt**

> 两个套装都等价 8 个有效词条，所以实战价值一定一样？

**Expected**

- 明确 `Stat Budget ≠ Effective Combat Value`；
- 检查乘区稀释、阈值、覆盖率、Build、条件、角色已有属性；
- 词条等价只作为资源预算基准。

## T6 Reference Game Is Not Project Truth

**Prompt**

> 崩铁某属性每级这么成长，我们项目也直接照这个比例做吧。

**Expected**

- 拒绝直接照抄；
- 提取“平滑成长 + 突破跳变 + 标准化 Benchmark”等方法；
- 重新基于本项目 TTK、内容曲线、装备和经济确定比例；
- 外部值标为 reference，不标 verified-project。

## T7 Build Completion Probability

**Prompt**

> 这个 Roguelite Build 成型后比其他体系强 20%，所以应该削弱 20%。

**Expected**

- 不只看完成态强度；
- 检查核心卡出现概率、平均成型波次、P90 成型、Dead Pick、Boss 前成型率；
- 若成型概率更低，应纳入 Context Discount；
- 不机械等比削弱。

## T8 Same-color Drafting

**Prompt**

> 主体系就是让玩家见到同标签卡全拿，这样最容易理解。

**Expected**

- 指出构筑可能退化为 Same-color Drafting；
- 要求 Seed/Engine/Scaler/Stabilizer/Capstone；
- 保留副体系与通用补强选择；
- 每轮三选一要有机会成本。

## T9 Core-or-Brick

**Prompt**

> 某体系必须拿到一张核心红卡才能运转，没拿到就只能重开。

**Expected**

- 标记 `Core-or-Brick` 高风险；
- 检查替代组件、核心保底、权重、低阶引擎、转型路径；
- 不仅通过“提高红卡强度”解决。

## T10 Energy Source Semantics

**Prompt**

> 回能效率 +20%，所以所有获得能量的来源都提升 20%。

**Expected**

- 不默认所有来源受同一倍率影响；
- 要求确认固定回能/倍率回能/击杀/受击/追击/技能特殊回能；
- 配置/代码未知时标 `unverified`。

## T11 Secondary Gauge Value

**Prompt**

> 这个角色 DPS 比主 C 低，所以削弱韧性伤害补一点 DPS 就行。

**Expected**

- 把 Secondary Gauge Contribution 计入 Power Budget；
- 检查 Break Window、控制、团队增益、Boss 适用性；
- 不只按直接 DPS 平衡功能角色。

## T12 Benchmark Drift

**Prompt**

> A 用毕业装备、B 用普通装备测试后，A 高 15%，说明 A 角色基础强度高 15%。

**Expected**

- 拒绝结论；
- 建立标准化 Benchmark；
- 固定等级、突破、技能、装备预算、敌人、时间窗；
- 必要时准备 Midgame / Endgame / High Investment 多套基准。
