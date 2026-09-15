# Canonical Detailed Guidance

> Preserved from the canonical Game Design Suite specialist. The runtime wrapper is intentionally compact; this file retains the detailed domain rules, workflows, guards, anti-patterns, and done criteria.

# 战斗策划

目标是让玩家能理解战斗状态、做出有意义决策，并通过规则与反馈形成可控节奏，而不是只让敌我数值互相消耗。

涉及团队阶段职责、打条/失衡/异常、前后台切换、反击/追加、共享资源、敌人与角色循环关系时，优先读取 [Team Combat Loop & Role Contracts](team-combat-loop-and-role-contracts.md)。

涉及速度、行动顺序、额外行动、共享技能点、能量循环、目标概率、韧性/Break 等问题时，与 `balance-design` 的 HSR-style theorycrafting reference 协作，不照抄外部游戏数值。

## Result-Level Professional Context

每一个独立战斗规则、AI、Target、资源循环、Gauge、Boss 战斗窗口或 Encounter 行为结论前，按 `../game-design/references/professional-context-header.md` 输出一次结果级 Header。

战斗规则本身由 `combat-design` 主责；具体技能机制切换到 `skill-design` 主责；倍率/TTK/覆盖率等强度判断由 `balance-design` 主责；空间和关卡编排由 `level-design` 主责。相邻结果即使专业组合相同，也重复显示 Header。

## Combat Grammar / 战斗语法

先把一次完整战斗行为拆成可验证链路：

`Acquire Target -> Telegraph -> Cast -> Resolve -> Damage/Heal -> Apply State -> Trigger -> Response -> Resource/CD Update`

任何技能、Buff、AI 行为都应该能映射到这条链。

检查：

- Target 在什么时候确定；
- Cast 前后是否允许改目标；
- Damage 与 Buff 谁先结算；
- 触发器读取结算前还是结算后状态；
- 死亡/复活/护盾破裂等边界在哪一步发生；
- 多个同帧/同行动 Trigger 的优先级。

## 战斗模型

明确：

- 战斗开始/结束条件；
- 单位状态；
- 攻击流程；
- Target 规则；
- 命中/暴击/伤害；
- 治疗；
- 控制；
- Buff/Debuff；
- 资源与大招；
- 死亡/复活；
- 波次；
- Boss 阶段；
- AI 决策。

## Team Combat Loop / 团队阶段循环

角色职责必须映射到团队循环，而不是只写“输出/坦克/奶妈”。

建议按项目需要拆：

`Build-up -> Setup -> Window Creation -> Exploit -> Sustain -> Recover/Reset`

检查：

- 谁负责积累 Gauge/状态/资源；
- 谁创造 Burst/Break/失衡窗口；
- 谁在窗口中兑现；
- 谁负责维持血线/护盾/资源；
- 循环结束后如何恢复；
- 一个角色是否在所有阶段都最优。

### Phase Ownership

每个角色至少定义主阶段职责。相同“输出”标签可以因 Phase Ownership 不同形成完全不同玩法。

## Gauge / 第二战斗轴

若有韧性、护甲槽、Stagger、Break、Poise、异常积蓄等 Gauge，必须明确：

- Gauge 上限；
- 每技能贡献；
- 阈值；
- 触发状态；
- Window Duration；
- 恢复/重置；
- Boss/Elite 差异；
- 重复触发是否提高门槛或收益衰减；
- 哪些角色主要负责 Build-up，哪些负责 Exploit。

Gauge 的目的应是增加决策轴，而不是多一条血量。

### Cross-State Interaction

不同 Gauge/状态若存在交互，应优先创造新决策，例如：

- 状态 A + 状态 B 触发额外结果；
- Break 后异常更易积累；
- 受击转反击/资源；
- 队友行动触发追加；

不要只做“同时存在时伤害 +X%”。

## Action Combat Reaction Verbs

动作战斗中，防守阶段也应有玩家动词：

- Dodge；
- Perfect Dodge；
- Dodge Counter；
- Parry/Assist；
- Swap；
- Defensive Assist；
- Interrupt；
- Positioning；
- Invulnerability/Armor Window。

每个敌方关键攻击明确：

- Telegraph；
- 可以怎么响应；
- 成功响应收益；
- 失败后果；
- 是否有多种正确答案。

## Turn-Based Reactive Verbs

回合制也可以通过：

- Counter；
- Follow-up；
- Action Advance/Delay；
- Ultimate 插入；
- Ally-action Trigger；
- Enemy-action Trigger；
- Resource Refund；
- Conditional Extra Turn；

建立回合外决策和构筑。

## Action Economy / 行动经济

对回合制或自动战斗，必须把“行动次数”视为资源。

检查：

- Base Action Frequency；
- 速度/攻击间隔；
- Action Advance / Delay；
- Extra Turn；
- Follow-up / Counter；
- 插队；
- 行动是否消耗共享资源；
- 行动是否刷新/减少 Buff；
- 额外行动是否导致资源循环转负。

单次倍率低不代表角色弱；如果单位时间行动更多、触发队友或生成资源，Effective Power 可能更高。

不要脱离真实战斗窗口讨论速度阈值。

## Shared Resource / 团队共享资源

若队伍共用技能点、怒气、卡牌点数、弹药等资源，按 Rotation 分析：

- 谁生成；
- 谁消耗；
- 谁是 Resource Positive / Neutral / Negative；
- Burst Window 是否需要预存；
- 治疗/解控等紧急行为是否会破坏循环；
- 资源是否经常溢出或见底；
- 加速角色/额外行动是否放大消耗。

团队不能只按每个角色个人强度组合。

## Energy / 大招循环

检查：

- 能量上限；
- 初始能量；
- 普攻/技能/受击/击杀/追击回能；
- 哪些回能受回能效率影响；
- 固定回能与倍率回能；
- 大招后返能；
- 溢出；
- 大招所需行动数；
- Buff 是否覆盖大招窗口。

重点观察“少一点回能会多拖一整轮”的 Breakpoint。

## Target / Aggro

先确认 Target 是：

- 强制锁定；
- 前排/后排规则；
- 优先级；
- 权重随机；
- 全随机；
- Bounce/多段随机。

若采用权重随机，不用“高嘲讽=一定挨打”的语言。应与 `balance-design` 显式计算概率。

Target 价值影响：

- Tank 生存职责；
- 反击；
- 受击回能；
- 后排保护；
- Boss 点名；
- 阵型站位。

## Status Reliability / 状态可靠性

控制、Debuff、异常状态不能只看文本 Base Chance。

应区分：

- Base Chance；
- Attacker Hit；
- General Resist；
- Specific Resist；
- Immunity；
- Boss Rule。

对关键控制技能至少检查普通怪/Elite/Boss 的实际成功率和 Breakpoint。

## Field-Time / Action-Time Competition

队伍中的角色会争抢：

- 前台时间；
- 行动次数；
- 换人窗口；
- 终结技插入时机；
- 共享资源；
- Break/失衡/易伤窗口。

因此不能把每个角色各自的最强连段简单相加。

### Window Realization

记录：

`Real Payoff Time = Window Duration - Entry Cost - Setup Cost - Reposition/Swap Cost`

升级增加的攻击次数/连段如果落在窗口外，只能按实际可兑现部分计入价值。

## 决策与可读性

检查玩家是否能：

- 看懂威胁来源；
- 识别前后排/优先级；
- 理解技能释放结果；
- 预判 Boss 行为；
- 通过构筑或操作响应；
- 看懂共享资源是否即将不足；
- 看懂 Break/控制窗口；
- 知道何时进入 Build-up、何时进入 Payoff。

Telegraph 不应与实际结果冲突。

## Role Contract / 角色职责合同

每个角色至少记录：

| 维度 | 定义 |
|---|---|
| Primary Role | 主职责 |
| Phase Ownership | 负责哪个战斗阶段 |
| Resource Relation | 生成/消费/中性 |
| Field/Action Time | 占用多少操作/行动 |
| Target Shape | 单体/扩散/群体/随机 |
| Trigger | 主触发来源 |
| Window | 主要收益窗口 |
| Team Hook | 为队友创造/消费什么 |
| Failure Case | 什么环境会显著失效 |
| Recovery | 循环断裂后如何恢复 |

职业标签写“Tank/Support/击破/异常”，但上表无法对应时，说明标签没有落实成玩法。

## 遭遇设计

每种敌人/组合要提出不同问题，而不是只加血加攻。检查：

- Threat Priority；
- Target Pressure；
- Timing Window；
- Counterplay；
- Composition Synergy；
- Recovery Window；
- Resource Pressure；
- Attack Frequency；
- Target Density；
- Gauge/Status Interaction；
- 是否检验不同 Build；
- 是否长期系统性封印某类角色。

## Boss

Boss 至少明确：

- 核心考题；
- 阶段；
- 关键招式；
- Telegraph；
- Counterplay；
- Enrage/Pressure；
- 失败原因可读性；
- 是否依赖特定角色才能通过；
- Break/控制抗性；
- 目标选择规则；
- 资源与 Burst Window；
- 是否通过节奏/目标/窗口 Stress 角色，而不是简单免疫体系。

## 与其他 Skill 协作

- 具体技能 -> `skill-design`
- 参数与强度 -> `balance-design`
- 场地空间/Encounter Matrix -> `level-design`
- 配置 -> `config-audit`
- 实际实现 -> `code-verification`

不要通过偷改技能机制解决单纯数值问题。

## 战斗反模式

- **Role by Label**：职业名与实际行为无关；
- **All-phase Carry**：一个角色准备、开窗、爆发、续航全部最优；
- **Single-hit Fallacy**：只看单次倍率不看行动频率；
- **Infinite Action Value**：加速、追击、插队形成失控循环；
- **Resource Blindness**：个人输出很高但团队资源破产；
- **Hidden Target RNG**：目标概率不透明导致 Tank/反击价值不可控；
- **Fake Control**：文本控制很强但 Boss 实际高抗/免疫；
- **Second HP Bar / Gauge as Extra HP**：第二 Gauge 没有新决策；
- **Trigger Starvation**：敌人行为让反击/受击/状态角色长期无法工作；
- **Reaction Monopoly**：敌方攻击只有一种正确防守答案；
- **Permanent Burst**：高收益状态覆盖过高，阶段结构消失；
- **Boss-by-Immunity**：靠全面免疫解决构筑过强，直接杀死体系价值。
