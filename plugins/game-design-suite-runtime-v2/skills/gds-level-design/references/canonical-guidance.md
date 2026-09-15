# Canonical Detailed Guidance

> Preserved from the canonical Game Design Suite specialist. The runtime wrapper is intentionally compact; this file retains the detailed domain rules, workflows, guards, anti-patterns, and done criteria.

# 关卡设计

目标不是“把内容排进地图”，而是把玩家的学习、决策、行动、压力、恢复和情绪组织成可测试的体验。

根据任务按需读取：

- 机制教学、空间引导、心理地图 -> [Mechanic Teaching & Spatial Language](mechanic-teaching-and-spatial-language.md)
- 节奏、强度、Beat、时长预算 -> [Pacing, Intensity & Beat Budget](pacing-intensity-and-beat-budget.md)
- 波次、随机事件、Roguelite 结构 -> [Wave & Randomized Level Architecture](wave-random-level-architecture.md)
- Boss、机械峰值、情绪峰值、收束 -> [Emotion, Encounter & Closure](emotion-encounter-and-closure.md)
- 角色技能、队伍体系如何被 Encounter 验证 -> [Kit-to-Encounter Contract](kit-encounter-contract.md)

## Result-Level Professional Context

每一个独立 Layout、路径、导航、Encounter、波次、节奏、Boss 或机制教学结论前，按 `../game-design/references/professional-context-header.md` 输出一次结果级 Header。

空间和关卡编排本身由 `level-design` 主责；底层战斗规则由 `combat-design` 主责；具体强度曲线由 `balance-design` 主责；系统玩法结构由 `game-production` 主责；界面引导问题可由 `game-interface-design` 主责。相邻结果即使专业组合相同，也重复显示 Header。

## 1. 先定义关卡问题

明确：

- Level Type：线性 / Hub / Arena / Wave / Roguelite / Puzzle / Open World / Hybrid；
- Player Goal；
- 本关主要动词；
- 本关教什么；
- 本关考什么；
- 玩家已有能力；
- 新引入能力；
- 目标时长；
- 难度位置；
- 玩法强度峰值；
- 情绪峰值；
- 失败与恢复；
- 制作预算；
- 性能约束；
- 当前实现/配置硬约束。

只有不同答案会造成完全不同空间方案时才追问；否则声明假设继续。

## 2. 先定义“玩法句子”，再画地图

正式做 Layout 前先用一句话描述：

> 玩家通过【核心动词/机制】，在【空间/敌人/时间约束】下解决【主要问题】，并在关卡结束前完成【学习/掌握/构筑/情绪目标】。

如果一句话里出现多个互不相关的新机制，优先检查是否内容过载。

## 3. Mechanic Lifecycle

新机制不要只“出现”，要有生命周期。

常用结构：

`Introduce -> Practice -> Test -> Twist/Combine -> Mastery/Closure`

设计时明确每次出现改变了什么：

- 第一次：低风险理解；
- 第二次：练习/撤除部分安全网；
- 第三次：真正测试；
- 后续：组合、反转、时间压力、空间变化或多解；
- 收尾：综合验收或迁移到后续内容。

### Safety Net

首次教学优先控制失败成本，让玩家敢试。玩家形成正确模型后再逐步撤除。

不要用永久安全网代替难度设计，也不要第一次见机制就要求完美执行。

## 4. Silent Teaching / Spatial Signifiers

机制如果能通过空间教会，就不要第一反应写教程弹窗。

检查：

- 玩家首先会看哪里；
- 哪个 Signifier 暗示行动；
- 错误猜测是否会被过度惩罚；
- 尝试后反馈是否明确；
- 奖励、敌人、光照、镜头、地标是否在传达同一个方向；
- UI 是否在弥补空间本身不可读。

## 5. 空间指标 Metrics

根据项目建立必要 Metrics：

- 移动速度；
- 跳跃/冲刺距离；
- 攻击距离；
- 技能范围；
- 视野；
- 转角；
- 门宽；
- 通道宽度；
- 房间尺度；
- 高低差；
- 敌人出生距离；
- 与玩家接触时间；
- Checkpoint 间隔；
- 失败重跑距离。

不靠“感觉差不多”。Metrics 是设计边界，不等于关卡本身。

## 6. Layout 与 Mental Map

检查：

- 主路径；
- 支路；
- 回环；
- 捷径；
- 地标；
- Junction 可辨识度；
- 导航；
- 视线；
- 高低差；
- 安全区/压力区；
- 探索奖励；
- 返回成本；
- 房间是否有独特功能/视觉语义；
- 玩家能否建立心理地图。

复杂空间的目标是“让玩家理解复杂”，不是靠同质房间让玩家迷路。

## 7. Pacing：强度不等于难度

至少区分：

- Gameplay Intensity；
- Difficulty；
- Decision Pressure；
- Cognitive Load；
- Emotional Intensity。

高强度可以来自重新规划、目标改变、场地变化、资源危机和信息压力，不只来自敌人血量。

### 休止符

低强度 Beat 承担恢复、奖励、规划和对比。连续高强度会造成麻木。

常见宏观结构可参考：

`Warm-up -> Familiarization -> Challenge -> Peak -> Closure`

但不要机械套模板。

## 8. Beat Sheet 与 Decision Budget

正式关卡建议按 Beat 编排，而不是只按地图长度。

每个 Beat 至少明确：

- Type；
- Player Goal；
- Mechanic；
- Decision；
- Risk；
- Intensity；
- Duration；
- Recovery；
- Expected Learning / Payoff。

一关还要预算“高压决策”的数量。不可逆、影响全局、改变 Build 的选择不能连续轰炸玩家。

## 9. Encounter

空间必须服务战斗考题。与 `combat-design` 协作确认：

- 敌人类型；
- 同屏数量；
- 生成时机；
- 生成位置；
- 与玩家接触时间；
- 视线；
- 距离；
- 掩体；
- 退路；
- 高低差；
- 资源；
- Threat Priority；
- Counterplay；
- Recovery Window。

不要只通过加血加攻制造 Encounter 差异。

较长战斗可检查：

`Introduce Threat -> Conflict -> Escalate -> Midpoint Breath -> Final Challenge`

中点喘息用于重建节奏，不等于无意义暂停。

### Kit-to-Encounter Contract

已有角色制项目还必须检查“关卡是否真的允许角色机制发生”。

典型映射：

- 反击/受击角色 -> 敌人需要有可读且足够频率的攻击；
- AoE/扩散 -> 需要合理目标密度；
- 单体爆发 -> 需要高价值单体/优先目标；
- DoT/状态引爆 -> 目标需要存活足够久且状态不会频繁无条件清空；
- Break/失衡 -> 需要 Gauge 与明确 Payoff Window；
- 换人/支援 -> 需要清晰 Telegraph 和响应窗口；
- 低血/护盾循环 -> 需要可控压力而不是随机秒杀。

允许局部 Soft Counter，但避免大量关卡长期 Hard Invalidate 一整类角色。

### Encounter Matrix

一组关卡至少跨以下维度变化：

- Enemy Count；
- Target Density；
- Attack Frequency；
- Telegraph；
- Mobility；
- Weakness/Resistance；
- Break/Stun Length；
- Invulnerability；
- Adds；
- Phase Change；
- Resource Pressure；
- Time Limit。

用矩阵检查是否只有一种队伍/角色在所有环境都最优。

## 10. Boss

Boss 至少明确：

- 核心考题；
- 已教授能力；
- 阶段；
- Telegraph；
- Counterplay；
- 空间需求；
- 优势战术点；
- Enrage/Pressure；
- 恢复窗口；
- 失败原因可读性；
- 是否形成角色/Build 强制门槛；
- 战后释放与奖励。

**最终 Boss 不自动等于全场最难。**

先决定它承担：

- Mechanical Peak；
- Emotional Peak；
- Narrative Payoff；
- Ultimate Skill Check；

再决定难度和时长。多个峰值可以重合，也可以错开。

### Stress，不是 Nullify

Boss 优先通过：

- 改节奏；
- 改窗口；
- 改目标数量；
- 强制转火；
- 资源保留；
- 防守响应；

来测试角色，而不是简单“免疫该体系”。

若必须免疫，提供明确 Telegraph、替代解法、有限持续和后续奖励窗口。

## 11. 波次 / Roguelite / 随机事件关卡

随机结构下，关卡设计从“固定顺序”转为“分布设计”。

至少明确：

- Slot Budget；
- Fight / Decision / Reward / Recovery 等槽位职责；
- 总决策预算；
- 高压决策最小间隔；
- 连续高压事件上限；
- Boss 前恢复下限；
- 关键机制/Build 的保底；
- 随机内容与固定宏观结构的边界；
- P50/P90 总时长。

随机不是“不编排”。

## 12. Time Budget

玩家实际体验时长至少拆成：

`Combat + Choice + Travel + Spectacle + Reward + Recovery + Transition`

UI 动画、品质展示、等待、结算和选择停留都要算。

配置里的 `Duration` 不能直接当玩家体感时长；若实现细节影响时长，与 `code-verification` 协作。

## 13. 情绪曲线

同时画玩法曲线与情绪曲线。

检查：

- 紧张；
- 挫伤；
- 掌控；
- 惊喜；
- 释放；
- 成就；
- 期待。

负向 Beat 要有落点：玩家能选择风险、获得应对或在合理时间内得到 Payoff。

## 14. 实现约束优先

已有项目做关卡时必须先确认真实实现：

- 关卡表如何排序；
- 事件/怪物/波次如何引用；
- 随机发生在哪一层；
- 哪些字段是死字段；
- 哪些波次会自动插入；
- 末波/IsEnd/MonsterGroup 等硬约束；
- UI/动画是否增加隐藏时长。

不要设计一个运行时根本无法表达的关卡。

配置事实交给 `config-audit`，实现语义交给 `code-verification`。

## 15. 可执行交付

根据需求输出：

- Intent / Player Outcome；
- Level Type；
- Mechanic Lifecycle；
- Metrics；
- Layout / Route；
- Beat Sheet；
- Intensity Curve；
- Emotion Curve；
- Encounter Plan；
- Encounter Matrix；
- Kit Coverage；
- Decision Budget；
- Time Budget；
- Random Distribution Rules；
- Checkpoint / Recovery；
- Technical Constraints；
- Content Budget；
- Acceptance Criteria；
- Playtest Plan。

## 16. Playtest / Validation

优先记录：

- 玩家路线；
- 迷路点；
- 死亡点；
- 停滞；
- 输入停顿；
- 目标切换；
- 重规划频率；
- 资源耗尽；
- 机制误解；
- 是否看见引导；
- 预期路径 vs 实际路径；
- 每 Beat 实际时长；
- 失败/退出分布；
- 自评紧张/挫败/成就；
- P50/P90 总时长；
- 不同角色/Build 的循环完成率与失效原因。

文档、白盒、强度图或未游玩地图不能证明“好玩/节奏已验证”。

## 17. 关卡反模式

- Mechanic Dump；
- Tutorial Popup Dependency；
- One-and-Done Mechanic；
- Fake Twist；
- Monotonic Escalation；
- No Rest；
- Boss = Hardest by Default；
- Maze by Sameness；
- Backtracking Tax；
- Event Soup；
- Random Pacing Collapse；
- Animation Tax；
- Beat Filler；
- Paper Pacing；
- Fake Precision；
- **DPS Dummy Level**：所有关卡只换血量；
- **System Invalidation**：大量内容直接封印某体系；
- **Window Theft**：玩家刚进入爆发就强制转场；
- **Counter Starvation**：反击角色因敌人低频行动无法玩；
- **Trash Too Fragile**：状态/构筑尚未成立，目标已死亡；
- **Boss Immunity Soup**：靠堆免疫制造难度；
- **Tutorial by Button List**：角色试玩只教按钮不教循环；
- **One-Roster Check**：只用最强标准队验证关卡。

发现这些问题时，优先修结构，不用更多敌人、更多事件、更多数值把问题盖住。
