# Team Combat Loop & Role Contracts

> 用途：把角色职责从“职业标签”升级为对团队战斗循环的明确贡献。
>
> 边界：参考动作角色制与回合角色制游戏的公开机制，只学习循环、窗口和职责结构，不照搬具体数值。

## 1. 角色职责要落在团队循环中

不要只写：

- 输出；
- 坦克；
- 奶；
- 辅助。

至少说明角色负责团队循环的哪一段：

`Build-up -> Setup -> Window Creation -> Exploit -> Sustain -> Recover/Reset`

一个角色可以跨多段，但必须有主职责。

## 2. 双阶段/多阶段战斗

成熟战斗常通过“打条 -> 开窗 -> 兑现”创造节奏。

例如可抽象为：

`Normal State -> Accumulate Gauge -> Break/Stun/Abnormal State -> Burst Window -> Reset`

设计意义：

- Build-up 角色有明确价值；
- Burst 角色不必全程最高输出；
- Support 可以改变窗口长度/质量；
- Enemy 可以通过条长、行动模式、抗性改变节奏。

## 3. Gauge 是节奏工具，不只是第二条血

可用 Gauge 包括：

- 失衡/眩晕；
- 异常/属性积蓄；
- 韧性；
- 防御条；
- Boss 机制条；
- 玩家队伍公共资源。

每条 Gauge 都要明确：

- 谁能积累；
- 积累效率；
- 阈值；
- 触发后状态；
- 窗口长度；
- 重置/抗性增长；
- 是否存在反复触发收益衰减。

## 4. Cross-State Interaction

两个系统如果可以互相作用，会产生更深的队伍构筑。

例如：

- 状态 A 存在时触发状态 B 产生额外效果；
- 破防后异常更容易积累；
- 护盾破裂转为资源；
- 受击触发反击并回能；
- 队友普攻触发追加攻击。

跨状态联动应创造新决策，不应只是“同时存在时伤害 +20%”。

## 5. Action Combat Reaction Verbs

动作战斗需要明确防守时玩家能做什么：

- Dodge；
- Perfect Dodge；
- Dodge Counter；
- Parry/Assist；
- Swap；
- Defensive Assist；
- Interrupt；
- Positioning；
- Invulnerability/Armor Window。

每个敌方攻击应明确：

- Telegraph；
- 可响应方式；
- 响应收益；
- 失败后果；
- 是否支持多种正确答案。

## 6. Turn-Based Reactive Verbs

回合制也不应只有“轮到我时按技能”。可以通过：

- Counter；
- Follow-up；
- Action Advance/Delay；
- Interrupt-like Ultimate；
- Ally-action Trigger；
- Enemy-action Trigger；
- Resource Refund；
- Conditional Extra Turn；

让玩家在回合顺序和触发链上做构筑。

## 7. Role Contract

每个角色至少记录：

| 维度 | 定义 |
|---|---|
| Primary Role | 主职责 |
| Phase Ownership | 主要负责哪个战斗阶段 |
| Resource Relation | 生成/消费/中性 |
| Field/Action Time | 占用多少操作/行动 |
| Target Shape | 单体/扩散/群体/随机 |
| Trigger | 主触发来源 |
| Window | 主要收益窗口 |
| Team Hook | 为队友创造什么/消费什么 |
| Failure Case | 什么环境会显著失效 |
| Recovery | 循环断裂后如何恢复 |

如果职业标签写“击破/坦克/支援”，但上表无法对应，说明标签没有落实到玩法。

## 8. Public Resource Economy

团队共享资源时，角色不能只按个人表现评估。

至少标记：

- Resource Positive；
- Neutral；
- Negative；
- Burst Consumer；
- Emergency Consumer。

强角色如果持续吞噬公共资源，必须证明团队收益覆盖机会成本。

## 9. Field-Time / Action-Time Competition

队伍中的角色会争抢：

- 前台时间；
- 行动次数；
- 换人窗口；
- 终结技插入时机；
- 共享技能点/能量；
- 失衡/破绽窗口。

因此不能只把四个角色各自最强连段相加。

## 10. Enemy Contract

敌人不是只有 HP/ATK。

敌人需要提供能被角色系统读取的“问题”：

- 高频/低频攻击；
- 单段/多段；
- 大范围/点名；
- 高韧性/低韧性；
- 状态抗性；
- 召唤物；
- 隐身/位移；
- 护盾；
- 弱点窗口；
- 强制转火；
- 机制打断。

一个 Encounter 应通过这些行为改变角色价值，而不是只靠数值膨胀。

## 11. Trigger Reliability 与 Enemy Dependence

反击、受击回能、异常利用、击破强化等角色会依赖敌方行为。

检查：

- 敌人行动频率变化时循环是否崩；
- Boss 长时间演出/无敌是否饿死触发；
- 群怪与单 Boss 下资源量差多少；
- 能否通过 Taunt、主动技能、保底资源降低依赖。

## 12. Burst Window Realization

窗口角色必须把动画/行动时间算进收益。

检查：

- Window Duration；
- Entry Cost；
- Setup Cost；
- Animation/Action Time；
- 可完成多少核心动作；
- 升级增加的动作是否会溢出窗口。

只按技能总倍率比较，容易高估长连段角色。

## 13. Anti-patterns

- **Role by Label**：职业名与实际行为无关；
- **All-phase Carry**：同一角色在准备、开窗、爆发、续航全部最优；
- **Gauge as Extra HP**：打条只增加时长，没有决策变化；
- **Window Without Setup**：爆发窗口自动送，没有构筑和执行价值；
- **Trigger Starvation**：敌人行为让角色长期无法工作；
- **Shared Resource Blindness**：只看个人 DPS；
- **Reaction Monopoly**：只有一种防守答案，失败即硬吃；
- **Enemy Stat Stick**：敌人差异只有血攻；
- **Permanent Burst**：高收益状态几乎永久覆盖，阶段结构消失。