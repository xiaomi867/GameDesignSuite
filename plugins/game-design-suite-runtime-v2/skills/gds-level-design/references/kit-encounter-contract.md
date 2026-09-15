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