# Pacing, Intensity & Beat Budget

> 用途：把“关卡节奏”从感觉词变成可讨论、可配置、可测试的结构。
> 边界：强度分值不是科学真值，必须由项目自己的 Playtest / Telemetry 校准。

## 1. 节奏不是“越来越难”

Pacing 关注活动、信息、压力和恢复如何按时间排列。

至少区分：

- **Difficulty**：完成任务的技术难度；
- **Gameplay Intensity**：玩家需要集中注意、重新规划、处理威胁的程度；
- **Emotional Intensity**：悬念、赌注、演出、剧情造成的投入；
- **Decision Pressure**：选择影响面、不可逆性和信息量；
- **Cognitive Load**：同时需要理解的新信息量。

这些可以同向，也可以刻意错开。

## 2. Re-plan Frequency

一个实用的关卡强度代理指标是：

`Re-plan Frequency = 单位时间内玩家需要改变计划的次数`

可能来自：

- 新敌人加入；
- 目标改变；
- 场地变化；
- 资源危机；
- 阶段切换；
- Target Priority 变化；
- 新机制触发；
- 高价值决策出现。

它不是唯一强度指标，但比单看敌人战力更接近实际认知压力。

## 3. Beat Roles

每一个关卡 Beat 应有明确职能，不要只是一条内容记录。

常见角色：

- **Teach**：教授；
- **Practice**：练习；
- **Test**：考核；
- **Twist**：变奏；
- **Combat**：压力主体；
- **Choice**：决策峰；
- **Reward**：反馈；
- **Recovery**：恢复；
- **Spectacle**：演出/情绪标记；
- **Exploration**：空间阅读；
- **Setup**：伏笔/目标建立；
- **Payoff**：回收；
- **Closure**：收束。

Beat 没有角色时，优先质疑它是否只是填时长。

## 4. Rest Is Structure

休止符不是“没内容”。它承担：

- 恢复注意力；
- 让上一峰值被感知；
- 读取奖励；
- 重建目标；
- 处理资源；
- 提供情绪落点；
- 为下一次高强度建立对比。

连续高强度会造成适应与麻木。

## 5. 宏观节奏

常见但非强制的一种结构：

`Warm-up -> Familiarization -> Challenge -> Peak -> Closure`

设计时检查：

- 开场是否允许玩家重新进入状态；
- 高低强度是否交替；
- 峰值是否有足够前置；
- 最终内容承担的是“技能考试”还是“情绪收束”；
- 结束是否有回味/奖励/结算空间。

**不要把“最终 Boss 必须最难”当默认规则。** 如果最终战承担情绪高潮，真正的技能考试可以前置；若项目目标就是极限挑战，则可以反过来。

## 6. 遭遇战内部五拍

对较长 Encounter，可参考：

`Introduce Threat -> Conflict -> Escalate -> Midpoint Breath -> Final Challenge`

关键是中点喘息：如果没有对比，最后高潮会失去参照。

## 7. Sequencing Knobs

控制强度不要只改敌人血量。

可调整：

- 敌人类型；
- 同屏数量；
- 生成节奏；
- 与玩家发生接触的时间；
- 生成位置；
- 视线方向；
- 高低差；
- 可玩空间尺寸；
- 环境事件；
- 任务目标；
- 对话/预告；
- 音乐与演出；
- 资源供给；
- 失败恢复距离。

## 8. 三角 / 菱形压力

### Triangle
保持敌人质量接近，逐步增加数量。

适合：

- 建立数量压迫；
- 检查 AoE；
- 测试资源管理。

### Diamond
数量下降、单位质量上升。

适合：

- 精英/Boss 前后；
- 从“处理杂兵”过渡到“读单体机制”；
- 减少视觉噪声但提高单体责任。

它们是编排模型，不是硬规则。

## 9. Decision Budget

一关不只预算战斗时间，也要预算“有意义决策”的次数与压力。

一个决策的压力可以粗略由以下维度组成：

- 影响面；
- 不可逆性；
- 后续持续时间；
- 选项复杂度；
- 信息不确定性；
- 与 Build/队伍的耦合；
- 失败成本。

高压决策之间应有足够消化空间。

## 10. Time Budget

总关卡时间至少拆成：

`T_total = T_combat + T_choice + T_travel + T_spectacle + T_reward + T_recovery + T_loading/transition`

不要只用“战斗时长”估计关卡时长。

尤其注意：

- UI 动画；
- 品质展示；
- 结算；
- 走路；
- 等待；
- 选择停留；
- 战后收尾；

都可能成为实际时长大头。

## 11. Beat Sheet

建议正式关卡至少有：

| Beat | Type | Mechanic | Player Goal | Decision | Risk | Intensity | Duration | Recovery | Expected Learning |
|---|---|---|---|---|---|---:|---:|---|---|

强度值初期可为 `candidate`，测试后再校准。

## 12. 验证指标

优先记录：

- 重规划频率；
- 输入停顿分布；
- 目标切换；
- 路径变化；
- 血量/资源曲线；
- 波次耗时；
- 失败率；
- 重试率；
- 退出点；
- 玩家自评紧张度；
- 实际时长 P50/P90；
- 机制误解率。

## 13. Anti-patterns

- **Monotonic Escalation**：一路升压不回落；
- **No Rest**：没有休止符；
- **Difficulty = Intensity**：把所有高潮都做成高难；
- **Boss = Hardest by Default**：最终战机械地做成全场最难；
- **Beat Filler**：Beat 没有明确功能，只是凑长度；
- **Animation Tax**：仪式/动画占据大量时间但没有新信息；
- **Paper Pacing**：文档曲线漂亮，实际构建完全不同；
- **Fake Precision**：把设计者主观的 7/10 强度当客观数据。
