# Game Design Suite Chat Edition — Level Design Deep Reference

> Deep reference bundle for Chat Edition. These materials preserve detailed reasoning patterns from the canonical Game Design Suite. External commercial-game values remain benchmark/reference evidence, never current-project truth.


---

## Canonical source: references/mechanic-teaching-and-spatial-language.md

# Mechanic Teaching & Spatial Language

> 用途：把机制教学、空间引导、心理地图、探索回环和机制生命周期统一成可执行的关卡方法。
> 边界：起承转合、Teach-Test-Twist、箱庭、安全网等是设计工具，不是所有关卡都必须套用的模板。

## 1. 先定义本关的“玩法句子”

关卡开始前先回答：

- 玩家这一关主要在做什么？
- 本关新教什么？
- 本关考什么？
- 哪一个机制/空间关系值得被记住？
- 玩家通关后应该比进关前多掌握什么？

如果无法用一句话说清，本关通常存在主题分散或内容堆叠。

## 2. Mechanic Lifecycle

对需要教学和深化的机制，优先按生命周期设计：

`Introduce -> Practice -> Test -> Twist/Combine -> Mastery/Closure`

可映射为：

- **Introduce / 起**：低风险、低认知负荷地第一次接触；
- **Practice / 承前段**：允许重复，帮助建立稳定模型；
- **Test / 承后段**：撤除部分安全网，要求玩家真正做到；
- **Twist / 转**：保持核心机制，改变关系、环境、时间、目标或组合；
- **Mastery / 合**：综合使用，形成完成感或迁移到后续内容。

### Twist 的质量标准

“转”不应只是：

- 数量 +50%；
- 伤害 +20%；
- 场景换皮；
- 同一操作再做一次。

更好的 Twist 通常改变：

- 机制与另一个机制的关系；
- 风险结构；
- 空间方向；
- 时间压力；
- 目标优先级；
- 解法数量；
- 玩家原有假设。

## 3. Safety Net

机制第一次出现时，应控制失败成本，让玩家敢于试。

Safety Net 可以是：

- 掉落不会死亡；
- 敌人伤害很低；
- 有明确退路；
- 失败后立即重试；
- 资源可恢复；
- 目标暂不计时；
- 错误路线仍能回到正确路径。

安全网不是永久降低难度。玩家建立正确模型后，应逐步撤掉，否则“知道”不会转化成“做到”。

## 4. Silent Teaching / 不言之教

教学优先让玩家通过环境自己推出结论，而不是先用文字解释。

设计链：

`Signifier -> Hypothesis -> Low-risk Attempt -> Clear Feedback -> Learned Rule`

检查：

- 线索是否足够明显；
- 玩家错误猜测是否会造成不可接受的惩罚；
- 尝试后反馈是否能明确证明规则；
- 是否存在多个互相矛盾的 Signifier；
- UI 教程是否只是弥补空间设计不清。

## 5. Cognitive Load

一次只引入有限的新概念。

区分：

- 新输入；
- 新规则；
- 新敌人；
- 新空间关系；
- 新 UI；
- 新资源；
- 新目标。

同一 Beat 同时新增多个维度时，要么降低风险，要么拆分教学。

## 6. Spaced Repetition

教学后不要立刻连续考试到玩家疲劳。

可以采用：

`Teach -> short reuse -> other content -> delayed recall -> twist`

延迟复用可以验证玩家是否真正形成记忆，而不是只靠短期工作记忆完成。

## 7. Spatial Language

空间不仅承载玩法，也传递信息。

常用 Signifier：

- 高低差；
- 光照与对比；
- 地标；
- 视线走廊；
- 敌人朝向；
- 奖励摆放；
- 门/桥/管道；
- 运动物体；
- 镜头构图；
- 声音方向。

必须区分“玩家看见了”与“玩家理解了”。

## 8. Mental Map

大型或重复访问空间要帮助玩家建立心理地图。

至少检查：

- Landmark 是否唯一且可辨；
- Junction 是否能区分方向；
- 玩家是否知道自己从哪里来；
- 返回路线是否形成可理解 Loop；
- Shortcut 是否缩短重复路程并制造空间顿悟；
- 房间是否有独特功能/视觉/战斗语义。

复杂空间的目标不是让玩家迷路，而是让玩家“理解复杂”。

## 9. One Key, Multiple Locks

关键能力/道具获得后，最好不仅解决一个单点问题，而是重新解释此前见过的多个障碍。

它可以制造：

- 回头探索价值；
- 能力成长感；
- 空间重读；
- 从被动到主动的翻盘感。

但不要为了回收旧区域强迫无意义跑图。

## 10. Box-garden / Dense Small Space

有限空间也可以提供高密度体验：

- 同一空间多次用途；
- 多高度层；
- 视线前后关系；
- 小范围玩法差异；
- 隐藏支路；
- 环路与捷径；
- 前后状态变化。

“地图大”不是内容丰富的充分条件。

## 11. Anti-patterns

- **Tutorial Popup Dependency**：空间没教会，只靠弹窗补；
- **Mechanic Dump**：一次引入过多新规则；
- **One-and-Done Mechanic**：只出现一次，没有生命周期；
- **Fake Twist**：只涨数值，没有关系变化；
- **Permanent Safety Net**：玩家永远不需要真正掌握；
- **Maze by Sameness**：房间高度同质，靠迷路制造时长；
- **Landmark Noise**：所有东西都抢注意力，等于没有引导；
- **Backtracking Tax**：回头没有新理解，只有重复行走。



---

## Canonical source: references/pacing-intensity-and-beat-budget.md

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



---

## Canonical source: references/wave-random-level-architecture.md

# Wave & Randomized Level Architecture

> 用途：波次制、事件制、Roguelite 随机关卡、战斗/选择/奖励混排时使用。
> 边界：随机结构中，设计者控制的是分布、预算、上下界和保底，不是每次实际顺序。

## 1. 先定义“槽位角色”

不同事件不是可互换的填充物。

可按玩法职责分类：

- **Pressure**：战斗/挑战主体；
- **Decision**：Build、路线、资源选择；
- **Reward**：正反馈、掉落、成长确认；
- **Recovery**：治疗、补给、低压力；
- **Twist**：风险交换、规则变化、意外；
- **Setup**：建立后续目标；
- **Payoff**：兑现此前选择；
- **Closure**：结算/收束。

同类型槽位也要允许内容变奏，但不能忘记它的节奏职责。

## 2. Slot Budget

一个 Stage 先定预算，再填内容：

- 总槽数；
- 战斗槽数；
- 决策槽数；
- 奖励/恢复槽数；
- 精英/Boss 数；
- 关键教学槽；
- 关键 Build 成型槽；
- 总时长；
- 总决策次数。

不要反过来“手里有什么事件就塞多少”。

## 3. Decision Budget

局内成长/三选一不只是奖励，也是时间与认知成本。

正式规划至少记录：

`D_total = D_opening + D_between + D_after_combat + D_special`

并区分高/中/低压力决策。

高压力决策通常具有：

- 新增能力；
- 长期不可逆；
- 影响整队/全局；
- 改变 Build 路线；
- 信息量大。

低压力决策通常是：

- 小幅属性；
- 可替代；
- 单局短期；
- 结果直观。

高压决策过密会让关卡从“战斗”变成“菜单管理”。

## 4. Freeze the Vocabulary Before Optimization

如果玩家先要确定“本局能做什么”，再决定“把什么做得更强”，通常应先让核心能力池稳定，再大量投放强化。

否则早期升级会因后续能力池改变而失去参考价值。

适用于：

- 开局英雄/技能 Draft；
- 路线选择；
- 武器基础形态；
- 主要 Build Seed。

不是所有游戏都要开局一次性冻结，但必须明确能力池何时稳定。

## 5. Randomness as Distribution Design

随机结构下不要写：

> 第 5 波一定发生 X。

除非代码确实保证。

更应该定义：

- 出现概率；
- 最短间隔；
- 最大连续次数；
- 阶段权重；
- 前置条件；
- 保底；
- 上下界；
- 峰值概率；
- Boss 前禁出/必出规则。

设计的是分布，不是假装随机不存在。

## 6. Randomness Must Respect Pacing

随机可以变内容，不应轻易打碎结构。

常见策略：

- **固定宏观槽，随机槽内内容**；
- **固定峰值位置区间，随机具体敌人**；
- **固定恢复下限，随机奖励类型**；
- **Boss 前限制高认知事件**；
- **连续高压事件设置冷却/保底**。

## 7. Positive / Negative Feedback Placement

负反馈若存在，要明确它的玩法意义。

更健康的形式通常是：

- 有价交换；
- 玩家主动承担风险；
- 能被后续 Build 转化；
- 在短时间内存在补偿或应对窗口。

纯粹不可控扣损容易被感知为惩罚。

设计负反馈时检查：

- 可预期性；
- 可选择性；
- 损失规模；
- 后续恢复时间；
- 是否形成连败螺旋。

## 8. Peak Placement

阶段峰值不一定是最终 Boss。

可以将：

- **Mechanical Peak**：最高重规划/技能考试；
- **Emotional Peak**：Boss、剧情、演出、赌注；
- **Reward Peak**：重大掉落/构筑成型；

错开排列。

这样比“最后一波同时最难、最长、最复杂、最华丽”更容易控制疲劳。

## 9. Wave Duration Is Player-facing Duration

一个 Wave 的体验时长不能只读配置里的 Duration。

至少拆：

- 前置等待；
- 演出；
- UI 打开；
- 阅读/选择；
- 战斗；
- 结算；
- 掉落；
- 过渡；
- 动画尾巴。

任何自动动画、品质展示、按钮等待都可能成为隐藏时长税。

## 10. Expansion / Compression

当关卡需要加长或缩短时，优先保持结构职责，而不是等比例删除。

### 加槽

优先增加：

- 练习；
- 变奏；
- 奖励；
- 恢复；
- 次级 Build 支撑。

不要只加更多同强度战斗。

### 减槽

优先删除：

- 重复无新信息的 Beat；
- 纯仪式时长；
- 冗余奖励确认；
- 功能重复的低压决策。

保护：

- 核心教学；
- 关键测试；
- 主要 Twist；
- 峰值；
- 收束。

## 11. Acceptance

随机/波次关卡至少验证：

- P50/P90 总时长；
- 每类槽真实时长；
- 连续高压事件概率；
- 高压决策连续出现概率；
- Boss 前恢复概率；
- 关键 Build 成型概率；
- 退出/失败峰值；
- 峰值位置是否与设计一致；
- 随机是否让某些 Run 进入不可恢复状态。

## 12. Anti-patterns

- **Random Pacing Collapse**：随机把高压事件连续堆叠；
- **Event Soup**：不同事件只有表现不同，没有节奏职责；
- **Menu Roguelite**：决策波过多，实际游玩被菜单切碎；
- **Reward Spam**：奖励频率过高导致反馈失去重量；
- **Unbounded Decision Time**：选择停留无界，关卡时长不可控；
- **Final Everything**：最后一波同时承担所有峰值；
- **Config-duration Illusion**：配置写 1 秒，实际玩家体验 10 秒；
- **Random = Unplanned**：用随机掩盖没有设计分布。



---

## Canonical source: references/emotion-encounter-and-closure.md

# Emotion, Encounter & Closure

> 用途：区分“玩法强度”和“情绪强度”，设计 Boss、精英、奖励、失败与收束。

## 1. 两条曲线，不要混成一条

至少同时看：

- **Gameplay Curve**：操作、重规划、资源压力、失败风险；
- **Emotion Curve**：期待、紧张、挫伤、惊喜、掌控、释放、成就。

一个低操作段也可以是高情绪段；一个高难战也可能情绪很平。

## 2. Emotional Latency

情绪并不总在事件发生瞬间达到峰值。

例如：

- 前一战差点团灭；
- 下一 Beat 给恢复/奖励；
- 玩家真正的“松一口气”发生在恢复确认时。

因此评审时不仅看事件本身，还看事件前后的因果链。

## 3. Negative Beat Needs a Landing

负向 Beat 若只是扣资源/扣血/惩罚，会很廉价。

更健康的负向 Beat 应至少满足一种：

- 玩家主动选择风险；
- 很快获得应对手段；
- 形成后续 Payoff；
- 改变优先级；
- 为翻盘制造空间。

“挫伤 -> 无回应 -> 再挫伤”容易形成失败螺旋。

## 4. Mechanical Peak vs Emotional Peak

不要默认二者必须重合。

### Mechanical Peak

适合承担：

- 技能考试；
- Build 检验；
- 复杂目标；
- 最高重规划频率。

### Emotional Peak

适合承担：

- Boss；
- 演出；
- 剧情回收；
- 重大赌注；
- 胜利确认。

把机械峰值略前置，可以让 Boss 更可读、更有表演空间；但如果产品承诺就是“终极挑战”，则可让二者重合。

## 5. Boss Is a Contract

Boss 不是“大号小怪”。至少明确：

- 本场核心考题；
- 玩家已经学过什么；
- 新东西是否过多；
- 阶段变化；
- Telegraph；
- Counterplay；
- 恢复窗口；
- 空间关系；
- 失败原因可读性；
- 是否存在单一角色/Build 强制门槛；
- 战后释放与奖励。

## 6. Midpoint Breath

长战斗若无中点变化，会把持续压力变成疲劳。

可用：

- 阶段转换；
- 清杂兵窗口；
- Boss 硬直；
- 场地重构；
- 资源补给；
- 演出；
- 短暂目标变化。

中点喘息不是无意义暂停，它让下一段重新具有重量。

## 7. Reward Weight

奖励的情绪价值不等于数值价值。

奖励“有重量”通常来自：

- 前面有真实压力；
- 奖励与刚才的付出因果清晰；
- 表现时长与奖励价值匹配；
- 玩家知道它改变了什么；
- 不是连续刷屏到麻木。

## 8. Closure

关卡结束前要明确是否需要收束：

- 战后低压 Beat；
- 奖励确认；
- 世界状态变化；
- 下一目标建立；
- 短演出；
- 返回基地/地图的过渡。

如果最后一帧仍在最高压力，玩家可能只记得疲劳而不是完成感。

## 9. Emotion Beat Sheet

可记录：

| Beat | Expectation | Tension | Frustration | Agency | Relief | Achievement | Cause | Payoff |
|---|---:|---:|---:|---:|---:|---:|---|---|

这些分数初期只是 candidate，必须通过玩家反馈校准。

## 10. Validation

可采集：

- 自评紧张度；
- 自评挫败度；
- “最记得哪一段”；
- 失败后是否愿意重试；
- Boss 死亡时的资源状态；
- 战后停留/跳过行为；
- 峰值位置与设计预期是否一致。

## 11. Anti-patterns

- **All Peaks Aligned**：最难、最长、最复杂、最华丽全塞在最后；
- **Punishment Without Payoff**：负反馈没有后续意义；
- **Reward Confetti**：奖励过密导致无感；
- **Boss as HP Sponge**：只有血量增加，没有行为问题；
- **No Closure**：赢了立刻切走，没有完成感；
- **Fake Drama**：演出很重，但玩家赌注很低。



---

## Canonical source: references/kit-encounter-contract.md

# Kit-to-Encounter Contract

> 用途：把角色技能、战斗机制和关卡/遭遇设计连接起来，避免角色机制只存在于技能描述里、关卡只靠敌人血攻验证角色。

## 1. Encounter 应验证“角色循环”，不是只验 DPS

把每个核心 Kit 映射到关卡条件：

| Kit 机制 | Encounter 需要提供 |
|---|---|
| 反击/受击触发 | 可读且有频率的敌方攻击 |
| AoE/扩散 | 合理目标密度与站位 |
| 单体爆发 | 高价值单体/优先目标 |
| DoT/持续状态 | 足够存活时间与状态持续空间 |
| 状态引爆 | 可建立并保留状态的目标 |
| 击破/失衡 | 可积累 Gauge 与明确 Break Window |
| 弱点利用 | 弱点配置和可读性 |
| 换人/支援 | 清晰攻击预兆和换人窗口 |
| 低血/护盾循环 | 可控制的伤害压力而非随机秒杀 |
| 资源生成/消费 | 足够的循环时间与阶段变化 |

## 2. 关卡不能长期“系统性封印”某类角色

允许局部克制，但要区分：

- **Soft Counter**：价值下降，需要调整策略；
- **Hard Counter**：核心循环无法工作；
- **Invalidation**：整类角色在大量内容中失去功能。

Hard Counter 适合少量明确挑战，不应成为默认 Encounter 模板。

## 3. Encounter Matrix

设计一组关卡时至少跨这些维度变化：

- Enemy Count；
- Target Density；
- Attack Frequency；
- Burst Frequency；
- Telegraph Clarity；
- Mobility；
- Summons/Adds；
- Weakness/Resistance；
- Break/Stun Length；
- Invulnerability；
- Phase Changes；
- Target Priority；
- Resource Pressure；
- Time Limit。

用矩阵检查是否只有一种角色/Build 在所有格子都占优。

## 4. Build-up 与 Payoff 的空间/时间配合

如果角色需要先积累再爆发，关卡要明确：

- Build-up 能否安全完成；
- 是否有足够目标生成资源；
- 窗口出现前是否有明显提示；
- Window Duration 是否允许至少一次完整 Payoff；
- 窗口结束后是否有 Recovery。

如果玩家每次刚进入强化状态 Boss 就无敌/转场，会让角色机制产生挫败。

## 5. Counter / Reactive 角色检查

反击类角色至少测试：

1. 高频多段敌人；
2. 低频重击 Boss；
3. 召唤物环境；
4. 敌人主要攻击其他目标；
5. 长演出/无敌阶段。

目标不是保证反击角色每关都最强，而是确认不会因 Encounter 行为彻底断循环。

## 6. 状态/异常体系检查

状态型角色测试：

- 普通怪是否死得过快，状态还未成立；
- Boss 是否抗性过高；
- 状态持续是否跨阶段清空；
- 多属性/多状态是否有组合空间；
- 敌方净化/免疫是否可读；
- 状态角色是否只能打 Boss、清杂兵体验很差。

## 7. Burst Window 与动作长度

对有明确爆发窗口的角色，关卡需要记录：

`Available Window - Entry/Setup Time - Required Reposition = Real Payoff Time`

动画、换人、移动、连携、目标转移都占用窗口。

不要只看“失衡持续 8 秒”，而忽略玩家真正可操作时间。

## 8. 关卡教学应覆盖技能关系

角色教学关/试玩关不要逐个介绍按钮，优先教核心关系：

- 什么生成资源；
- 什么消耗资源；
- 什么时候切换角色；
- 什么敌方状态是爆发信号；
- 失败后如何恢复循环。

可以按：

`Isolate -> Confirm -> Combine -> Pressure Test`

安排教学 Encounter。

## 9. Boss 设计：Stress，不是 Nullify

Boss 可以挑战角色弱点，但尽量通过：

- 改变节奏；
- 缩短/延长窗口；
- 改变目标数量；
- 要求转火；
- 要求保留资源；
- 逼迫防守响应；

而不是简单写“免疫此体系”。

如果必须免疫，给：

- 明确 Telegraph；
- 替代解法；
- 合理持续时间；
- 后续奖励窗口。

## 10. Roster Coverage Test

正式关卡组需要记录不同角色/Build 的体验：

| Encounter | Burst | Sustain | Counter | DoT/State | Break/Gauge | AoE | Single Target | Support |
|---|---:|---:|---:|---:|---:|---:|---:|---:|

分值只能用于候选比较，不代表真实 Playtest。

目标不是所有角色同强，而是避免内容长期只奖励单一解法。

## 11. Anti-patterns

- **DPS Dummy Level**：所有关卡只是不同血量木桩；
- **System Invalidation**：大量内容直接免疫一个核心体系；
- **Window Theft**：关卡频繁在玩家爆发开始时强制转场；
- **Counter Starvation**：反击角色遇到低频攻击就无法玩；
- **Trash Too Fragile**：状态/构筑还未建立敌人已死亡；
- **Boss Immunity Soup**：Boss 靠大量免疫制造难度；
- **Tutorial by Button List**：试玩关只教按键，不教循环；
- **One-Roster Check**：关卡测试只用最强标准队。
