---
name: combat-design
description: 负责战斗系统与遭遇规则，包括攻击、受击、目标选择、资源、状态、AI、战斗节奏、敌我职责、Boss/小怪战斗行为和战斗可读性。具体技能机制交给 skill-design，具体参数交给 balance-design。
---

# 战斗策划

目标是让玩家能理解战斗状态、做出有意义决策，并通过规则与反馈形成可控节奏。

涉及速度、行动顺序、额外行动、共享技能点、能量循环、目标概率、韧性/Break 等问题时，与 `balance-design` 的 HSR-style theorycrafting reference 协作，不照抄外部游戏数值。

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

### 原则

单次技能倍率低，不代表角色弱；如果其单位时间行动次数更多、能触发队友或生成资源，Effective Power 可能更高。

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

## Secondary Gauge / 第二战斗轴

若有韧性、护甲槽、Stagger、Break、Poise 等 Gauge，必须明确：

- Gauge 上限；
- 每技能削减值；
- Break 条件；
- Break 奖励；
- 恢复时间；
- Boss 抗性；
- 控制/爆发窗口；
- Build 联动。

这类系统的目的应是增加战斗决策轴，而不是多一条需要清空的血条。

同时检查：

- 只打 HP 是否永远最优；
- 只打 Gauge 是否形成万能解；
- 功能角色的 Gauge 贡献是否被正确计入价值。

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

## 决策与可读性

检查玩家是否能：

- 看懂威胁来源；
- 识别前后排/优先级；
- 理解技能释放结果；
- 预判 Boss 行为；
- 通过构筑或操作响应；
- 看懂共享资源是否即将不足；
- 看懂 Break/控制窗口。

Telegraph 不应与实际结果冲突。

## 角色职责

区分：

- Carry / Burst / Sustained DPS
- Tank
- Healer
- Control
- Support
- Hybrid

职责可以混合，但应明确主要价值、资源成本和代价。

角色职责评估至少考虑：

- Personal Output；
- Team Amplification；
- Survival；
- Action Economy；
- Resource Economy；
- Target Value；
- Gauge Contribution；
- Reliability。

## 遭遇设计

每种敌人/组合要提出不同问题，而不是只加血加攻。检查：

- Threat Priority；
- Target Pressure；
- Timing Window；
- Counterplay；
- Composition Synergy；
- Recovery Window；
- Resource Pressure；
- 是否检验不同 Build；
- 是否只针对某一角色。

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
- 资源与 Burst Window。

## 与其他 Skill 协作

- 具体技能 -> `skill-design`
- 参数与强度 -> `balance-design`
- 场地空间 -> `level-design`
- 配置 -> `config-audit`
- 实际实现 -> `code-verification`

不要通过偷改技能机制解决单纯数值问题。

## 战斗反模式

- **Single-hit Fallacy**：只看单次倍率不看行动频率；
- **Infinite Action Value**：加速、追击、插队形成失控循环；
- **Resource Blindness**：个人输出很高但团队资源破产；
- **Hidden Target RNG**：目标概率不透明导致 Tank/反击价值不可控；
- **Fake Control**：文本控制很强但 Boss 实际高抗/免疫；
- **Second HP Bar**：第二 Gauge 没有新决策，只是额外血量；
- **Boss-by-Immunity**：靠全面免疫解决构筑过强，直接杀死体系价值。
