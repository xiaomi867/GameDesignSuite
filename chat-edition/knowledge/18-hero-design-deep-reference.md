# Game Design Suite Chat Edition — Hero Design Deep Reference

> Deep reference bundle for hero concept, kit architecture, skill progression, roster ecology and cross-game design patterns. External commercial-game structures are benchmark evidence, not current-project rules.


---

## Canonical source: references/cross-game-hero-concept-patterns.md

# Cross-Game Hero Concept Patterns

本参考用于从公开商业游戏角色页提炼“角色信息如何组织、如何与玩法标签建立联系”的模式。它是 Benchmark，不是模板抄写。

## Source Boundary

首批公开来源：

- 崩坏：星穹铁道角色总页：`https://sr.appfeng.com/character`
- 原神角色总页：`https://ys.appfeng.com/character`
- 鸣潮角色总页：`https://mc.appfeng.com/avatar`

详情页为动态更新页面，任何精确角色值都应记录 Source Date / Version。若滑杆或二级详情当前不可读取，标 `externally-blocked`，不要从记忆补值。

## HSR Pattern

公开角色页通常同时暴露：

- 阵营；
- 命途；
- 属性；
- 稀有度；
- 介绍/故事/语音；
- 基础属性；
- 技能树；
- 星魂；
- 配装/队伍推荐。

可迁移模式：

- “命途 + 属性 + 阵营”提供系统坐标，但角色身份仍依赖技能循环和故事；
- 技能树中的 Stat Bonus / Bonus Ability 可承担“培养后更像自己”的成长表达；
- 语音、故事、称号和战斗行为能共同建立 Character Fantasy。

不可直接迁移：命途数量、属性种类、星魂结构、角色数值。

## Genshin Pattern

公开角色页通常同时暴露：

- 元素；
- 武器；
- 所属/地区；
- 性别/体型；
- 生日、命座、称号；
- 角色介绍；
- 基础属性与成长副属性；
- 普攻/战技/爆发/被动；
- 命之座；
- 故事/语音。

可迁移模式：

- Element + Weapon 是清晰的系统入口；
- Title / Region / Constellation / Story 强化世界观身份；
- Ascension Passive 与 Bonus Stat 可以让成长节点承担身份强化；
- 同一元素/武器内仍需靠角色循环、场上时间、反应关系和资源形成差异。

不可直接迁移：元素反应、武器类别数量、命座强度、90/100级上限等具体规则。

## Wuthering Waves Pattern

公开角色页通常同时暴露：

- 属性；
- 武器；
- 稀有度；
- 出生/所属/性别；
- 明确战斗标签，例如主力输出、重击伤害、牵引、生存治疗等；
- 共鸣能力设定；
- 战斗技巧摘要；
- 基础属性；
- 常态攻击、共鸣技能、共鸣回路、共鸣解放、变奏等技能节点；
- 共鸣链；
- 检验鉴定、故事、语音。

可迁移模式：

- 角色页直接把 Narrative Identity 与 Combat Tags 并列，有利于检查“设定-玩法”一致性；
- 战斗技巧摘要先解释循环，再展开技能详情，是较好的 Hero Contract 表达方式；
- 资源名、剑式/状态、共鸣能力等能把角色设定直接连接到玩法语法。

不可直接迁移：Cost、共鸣链、技能槽位结构、属性体系与具体倍率。

## Cross-Game Shared Pattern

三个项目都说明：

1. 角色身份不是只有数值；
2. 系统分类标签负责“找到角色”，独特循环负责“记住角色”；
3. 故事/称号/阵营与战斗能力最好形成同一主题；
4. 长线节点（行迹/命座/共鸣链/被动）常被用来进一步强化角色身份；
5. 角色详情页同时服务于叙事、战斗理解和成长预期。

这是 `supported-inference`，不是行业强制标准。

## Benchmark Questions

审当前项目时可问：

- 玩家看角色卡第一屏，能否在10秒内说出“这个人是谁、做什么、有什么独特点”？
- 系统标签和实际技能循环是否一致？
- 同职业/同阵营/同属性角色有没有 Same Job, Different Decision？
- 培养节点是否强化角色身份，还是只增加通用数值？
- 故事中的核心能力是否至少在一个高频玩法动作中被玩家感知？



---

## Canonical source: references/cross-game-hero-kit-patterns.md

# Cross-Game Hero Kit Patterns

本参考从崩坏：星穹铁道、原神、鸣潮公开角色页归纳不同战斗类型的 Hero Kit 架构。它用于扩展设计空间，不用于复制技能槽位或数值。

## HSR / 回合制角色 Kit

公开角色页常见：

- Basic ATK；
- Skill；
- Ultimate；
- Talent；
- Technique；
- Trace Stat Bonus / Bonus Ability；
- Eidolon。

结构特点：

- 每次行动的 Opportunity Cost 很高，Skill Point / Energy / Turn Economy 是核心；
- 额外行动、追击、反击、行动提前等机制会直接改变行动经济；
- Talent 常用于定义角色核心规则；
- Trace 用于补充被动规则与成长属性；
- Eidolon 常改变循环、可靠性或上限。

参考例：飞霄公开页面显示 Basic/Skill/Ultimate/Talent/Technique 体系，并以特殊资源代替传统能量终结技；砂金则以护盾、防御和受击/追击关系形成不同循环。

## Genshin / 实时换人 Kit

公开角色页常见：

- Normal Attack；
- Elemental Skill；
- Elemental Burst；
- Ascension Passives；
- Utility Passive；
- Constellations。

结构特点：

- Field Time、Swap、Energy Recharge、Elemental Reaction 是重要约束；
- 普攻并非所有角色都承担同等价值；
- Skill/Burst 常形成能量循环和爆发窗口；
- 被动与命座可能改变元素附着、状态、资源或输出窗口；
- 同一技能可能存在点按/长按、状态切换、召唤物等分支。

## Wuthering Waves / 动作换人 Kit

公开角色页常见：

- Normal Attack / 常态攻击；
- Resonance Skill / 共鸣技能；
- Forte Circuit / 共鸣回路；
- Resonance Liberation / 共鸣解放；
- Intro Skill / 变奏；
- Outro Skill / 延奏（页面结构依版本/角色）；
- Inherent Skills / 属性节点；
- Resonance Chain。

结构特点：

- Forte Circuit 常承担角色核心资源和状态机；
- Concerto / Resonance Energy 等多个公共/个人资源共同限制循环；
- Dodge Counter、Heavy Attack、Aerial、Intro/Outro等动作分类能成为 Build Hook；
- 角色页面常直接给“战斗技巧”摘要，先解释循环，再展开技能。

公开的秧秧·玄翎详情能观察到：消耗资源施放常态攻击、资源耗尽后切换剑式、获取另一资源、达到阈值后解锁重击，属于典型 `Source -> State Swap -> Secondary Resource -> Payoff` 循环。

## Shared Patterns

跨三个项目可以观察到：

1. **核心机制通常不平均分布在所有技能槽位**；往往有一个 Talent/Forte/Skill 承担规则核心。
2. **资源与行动经济决定真实强度**；技能倍率不是孤立的。
3. **被动成长节点常用于补可靠性或扩展规则**，而不只是加伤。
4. **高辨识度角色通常有一个可复述的循环**，不是技能列表。
5. **命座/星魂/共鸣链经常改变循环上限，但若修复基础缺陷，会形成付费/成长绑架风险**。

以上为 `supported-inference`。

## Cross-Game Audit Questions

- 核心机制放在哪个槽位，为什么？
- 角色最常按的动作是否正是其核心幻想？
- 资源生产与消费是否形成循环？
- 低频技能是否有足够Payoff？
- 被动是否只是自动加伤，还是改变玩法？
- 高阶成长是扩展还是修复基础残缺？
- 同类角色的不同点来自决策还是倍率？



---

## Canonical source: references/hero-kit-architecture.md

# Hero Kit Architecture

> 用途：把成熟角色制 RPG / 动作游戏中的角色机制拆成可复用的技能策划方法。
>
> 边界：参考《崩坏：星穹铁道》《绝区零》的公开角色、技能树与战斗机制，只学习结构和设计方法，不复制具体角色、倍率、节点数量或付费结构。

## 1. 先设计角色循环，不先填六个技能

角色不是“普攻 + 技能 + 大招 + 两个被动”的集合。先用一句话定义角色循环：

> 角色通过【生成条件/资源】进入【关键状态】，在【窗口】中用【核心动作】兑现收益，再通过【恢复/重置】重新进入循环。

至少回答：

- 核心动词是什么；
- 哪个技能是循环入口；
- 哪个技能是资源生成器；
- 哪个技能是转换器；
- 哪个技能是消费者/兑现点；
- 哪个技能负责稳定性与容错；
- 循环失败时角色还能做什么。

如果删除技能名称后无法描述循环，说明 Kit Identity 不够清楚。

## 2. 八层 Kit 模型

### Identity
角色给玩家的首要承诺，例如反击、防御转输出、异常引爆、状态变身、速切爆发、护盾循环。

### Verb Loop
玩家重复做的行为，不是技能列表。

### State Machine
明确角色状态及转换，例如：

`Normal -> Setup -> Empowered -> Spend/Payoff -> Recovery`

每个状态说明进入条件、退出条件、持续、可被打断/覆盖/刷新规则。

### Resource Graph
把资源画成：

`Source -> Storage -> Converter -> Sink -> Reset`

资源可以是能量、层数、弹药、标记、生命、护盾、敌方状态、队友行动等。

### Trigger Map
每个被动必须明确事件源：

- 自身行动；
- 队友行动；
- 敌人行动；
- 受击；
- 击破/击杀；
- 状态施加/移除；
- 换人/支援；
- 进入某阶段。

### Target Pattern
单体、扩散、群体、随机、多段、前后排、受击者、攻击者、最低血量等必须服务角色职责。

### Team Hook
角色如何与队伍发生关系：

- 创建状态；
- 消费队友状态；
- 放大某类行为；
- 提供行动/资源；
- 保护窗口；
- 改变敌方状态；
- 触发追加/协同动作。

### Payoff Window
角色收益在什么时间被兑现：持续、爆发、敌方失衡期、Boss 破绽、低血线、反击窗口、队友大招窗口等。

## 3. Skill Grammar：每个技能要有职能

可以把技能按功能标记为：

- **Generator**：生成资源/层数/能量；
- **Setup**：建立状态、标记、姿态或条件；
- **Converter**：把 A 资源转成 B 资源/状态；
- **Consumer**：消费资源；
- **Payoff**：兑现主要收益；
- **Amplifier**：放大已有循环；
- **Safety**：容错、生存、抗打断、回复；
- **Mobility/Position**：改变站位或接敌关系；
- **Finisher**：终结、重置或收束循环。

一个技能可以承担多个职能，但如果每个技能都什么都做，角色会失去决策边界。

## 4. 输入槽位不等于价值槽位

动作游戏可存在普攻、闪避、支援、特殊技、连携、终结技、核心技等多个输入/触发槽位；回合制也可存在普攻、战技、终结技、天赋、秘技、额外能力。

不要要求所有槽位数值价值相等。

应根据角色职责决定：

- 哪些是主循环技能；
- 哪些是低频应急；
- 哪些是进入/退出场手段；
- 哪些只提供触发或状态；
- 哪些技能等级优先级自然较低。

“技能存在”不代表“玩家应该同等升级/频繁使用”。

## 5. Field-Time Budget / 行动占用

团队角色设计必须预算角色占用的时间/行动资源。

记录：

- On-field Time；
- Setup Time；
- Payoff Time；
- Swap/Action Cost；
- Team Resource Cost；
- Cooldown/Recovery；
- 是否抢占队友爆发窗口。

一个角色个人 DPS 很高，但占用过多行动、换人、战技点或公共资源，团队价值可能反而下降。

## 6. Phase Ownership

成熟角色通常拥有明确的战斗阶段职责，而不是笼统的“输出/辅助”。

例如：

- Build-up：积累失衡、异常、能量、标记；
- Setup：施加状态、护盾、减益；
- Window Creation：制造弱点、失衡、破绽；
- Window Exploitation：在窗口中爆发；
- Sustain：维持血线/护盾/资源；
- Conversion：把敌方状态、队友行动、受击转化成收益。

同一“输出”角色可以因为 Phase Ownership 不同而有完全不同的玩法。

## 7. 角色机制模式（抽象）

### State Transformation
普通状态通过技能/能量进入强化状态，强化状态更换动作、速度、资源规则或攻击模板。

设计检查：强化状态是否有明确开始/结束、是否有准备成本、是否会出现“资源满了但窗口不对”的尴尬。

### Reactive Counter
敌人行动/受击成为角色资源或攻击触发器。

设计检查：

- 敌人不攻击该角色时是否直接报废；
- Boss 低频行动是否让循环断裂；
- 是否有可靠的吸引攻击/保底触发；
- 反击是否与防御价值绑定。

### State Detonator
角色不一定自己创造全部伤害，而是提前结算/引爆队友或敌方已有状态。

设计价值：让角色成为“体系引擎”而不是泛用伤害 Buff。

检查：没有对应队友/状态时是否完全失能，还是保留最低独立能力。

### Defense-to-Offense Alignment
防御/生命/护盾等主要生存属性同时进入输出或资源循环。

设计价值：减少属性分裂，让 Tank/Support 的成长更统一。

风险：若一个属性同时无限提高生存和输出，Power Budget 可能双重获益，需要 `balance-design` 检查。

### Ammunition / Stack Conversion
多个技能生成同一资源，核心动作消费资源进入高收益模式。

设计检查：

- 资源上限；
- 溢出；
- 生成渠道是否有优先级；
- 玩家是否能主动决定何时消费；
- 高收益动作是否有明显反馈。

## 8. Team Hook 应创造新关系，而不是团队税

可以用阵营/属性/职业/状态作为额外能力触发条件，鼓励配队。

但要区分：

- **Soft Synergy**：满足条件会更强/更顺；
- **Hard Dependency**：不满足条件角色核心循环无法工作。

默认优先 Soft Synergy。

如果一个角色必须与唯一角色绑定才能完成基础循环，标记 `Team Tax / Pair Lock` 风险。

## 9. Trigger Reliability

任何依赖触发的角色都应计算“触发可靠性”。

至少检查：

- 触发事件频率；
- 是否依赖敌方 AI；
- 是否依赖队友具体动作；
- 是否有 CD/每回合次数；
- 是否会因目标死亡丢触发；
- Boss/单体/群体环境差异；
- 是否存在保底或手动替代触发。

高收益可以建立在低可靠性上，但两者必须是有意识的交换。

## 10. 升级不只提高倍率

一个完整角色成长可以拆为：

- Skill Rank：稳定纵向数值；
- Major Passive：改变循环/条件/可靠性；
- Minor Stat：补面板和 Build；
- Milestone Upgrade：关键节点改变技能交互；
- Premium/High-tier Node：扩展上限、释放限制或提供新团队关系。

升级价值分类：

- Vertical Power；
- Reliability；
- Rotation/Cycle；
- Resource Economy；
- Target Coverage；
- Survivability；
- Team Synergy；
- QoL/Execution Ease；
- Mechanic Transformation。

不要所有升级都写成“伤害 +X%”。

## 11. Window Realization

升级的纸面价值必须在真实战斗窗口中兑现。

例如“多打 3 次攻击”如果把动作拖出敌方失衡/易伤窗口，实际提升会显著低于静态倍率。

检查：

`Realized Upgrade Value = Paper Value × Window Coverage × Trigger Reliability × Execution Rate`

该式是设计代理模型，不是通用伤害公式。

## 12. Anti-patterns

- **Button Zoo**：技能很多但没有共同循环；
- **Passive Soup**：被动大量叠规则却不改变决策；
- **Resource Orphan**：有资源但没有有意义的消费时机；
- **Trigger Lottery**：核心输出依赖不可控随机触发；
- **Role by Label**：写着 Tank/Support，但技能行为没有对应职责；
- **Pair Lock**：必须绑唯一队友；
- **Stat Split Tax**：一个角色被迫堆多个互不协同的核心属性；
- **Window Spill**：升级增加动作数量，却溢出真正收益窗口；
- **Overloaded Skill**：单个技能同时承担生成、控制、输出、生存、团队 Buff，挤压其他技能价值；
- **Dead Slot**：技能长期没有使用理由。

## 13. Source Notes

可复用结构参考于公开资料中的：

- 《绝区零》代理人技能槽位、核心技/额外能力、队伍条件；
- 《绝区零》失衡、异常与紊乱形成的阶段循环；
- 《崩坏：星穹铁道》角色技能树、行迹、额外能力、星魂；
- 代表性角色中的状态变身、反击、状态引爆、防御转收益、资源生成/消费等结构。

任何具体项目仍以自身规则、配置、代码和 Playtest 为准。


---

## Canonical source: references/skill-progression-and-upgrade-topology.md

# Skill Progression & Upgrade Topology

> 用途：设计技能等级、技能树、被动节点、升星/突破/高阶节点时使用。
>
> 目标：让成长既有稳定纵向收益，也有关键节点的玩法变化，而不是把所有成长都压成倍率上涨。

## 1. 先区分成长层级

推荐把技能成长拆成不同职责：

- **Skill Rank**：稳定纵向成长，主要改变倍率、护盾、治疗、概率、持续等；
- **Major Passive**：解锁机制、补可靠性、改变资源循环；
- **Minor Stat Node**：提供较小的基础属性或 Build 支撑；
- **Milestone Node**：在关键等级/突破/星级改变角色循环；
- **Capstone Node**：提高上限、释放限制或完成 Build Identity。

如果所有节点都只提供同一类型数值，技能树只是“分叉外观的线性升级”。

## 2. Upgrade Topology 要服务角色循环

技能树不是先画图再填效果。先把角色循环拆成：

`Entry -> Setup -> Engine -> Payoff -> Recovery`

再决定节点应该强化哪一段。

例如：

- 前期节点让循环能启动；
- 中期节点补资源与可靠性；
- 后期节点强化兑现或拓展队伍关系；
- 最高节点可以改变规则，但不应修复角色基础缺陷。

## 3. 数值节点与机制节点分工

### 数值节点
适合频繁成长：

- Skill Multiplier；
- Shield/Heal Value；
- Buff Value；
- Base Chance；
- Duration；
- Resource Gain。

### 机制节点
适合关键里程碑：

- 新触发条件；
- 新资源来源；
- 新消费方式；
- Target Pattern 变化；
- 状态转换；
- 新 Team Hook；
- 限制解除；
- 失败保底；
- 额外行动/追加攻击规则。

机制节点数量应受认知复杂度控制，不是越多越高级。

## 4. Level Rank 不是等比增长的义务

技能等级曲线需要说明：

- Lv1 基准；
- 中段增长；
- Max 增长；
- 是否有前高后低/前低后高；
- 是否存在概率/阈值 Breakpoint；
- 升级后是否改变 Rotation。

如果倍率成长是线性的，但真实收益因 Crit、资源、窗口或触发率发生非线性变化，应以真实循环评估。

## 5. Unlock Gate

技能/被动解锁等级应同时检查：

- 玩家是否已经理解前置机制；
- 解锁后是否有内容可以验证；
- 是否一次引入过多新规则；
- 是否把角色基础功能锁得太晚；
- 是否与资源投入同步；
- 是否造成“抽到角色但前期不好用”。

核心身份应尽早可见；成长节点负责深化，不应把完整角色拆到后期才成立。

## 6. Upgrade Value Classes

每个关键升级标记主价值类型：

| 类型 | 例子 | 主要验证 |
|---|---|---|
| Vertical | 倍率/护盾提高 | Power Delta |
| Reliability | 提高触发率/保底 | Trigger Rate |
| Cycle | 减少 CD/加速回能 | Rotation |
| Economy | 降低资源成本 | Team Resource |
| Coverage | 单体变扩散/更多目标 | Encounter Mix |
| Survival | 减伤/回复/抗打断 | Failure Rate |
| Team | 新协同/共享状态 | Team Value |
| Execution | 减少操作负担 | Error Rate |
| Transformation | 改变技能/状态规则 | New Loop |

不要把不同类型升级只换算成同一个“伤害百分比”后就结束。

## 7. Milestone Cohesion

一个里程碑最好强化同一主题。

例如“反击角色”的节点可以依次解决：

1. 反击成立；
2. 反击更可靠；
3. 反击转化资源；
4. 反击在特定场景扩展；
5. 最终节点突破触发限制。

而不是：

`+攻击 -> +生命 -> +暴击 -> 随机控制 -> 再+攻击`

后者会让成长没有叙事和玩法方向。

## 8. 关键升级不能只修基础缺陷

危险信号：

- 没有某星/某节点就完全无法循环；
- 基础角色资源严重短缺，高阶节点只是把缺口补回来；
- 核心 Trigger 在基础版几乎不可控，高阶才可靠；
- 高阶节点只是移除人为制造的操作痛点。

这类设计容易形成 `Problem-Sell-Solution`，除非项目商业目标明确且体验代价被接受，否则默认标风险。

## 9. Window Fit

升级增加：

- 攻击次数；
- 状态持续；
- 额外行动；
- Burst Length；

都必须检查是否真的落在收益窗口里。

例如敌人失衡只有 6 秒，多出来的连段需要 4 秒，但原本角色已经占满 5 秒，则新增动作的纸面倍率不能全部计入升级价值。

## 10. Upgrade Interaction Audit

检查关键节点之间：

- 是否乘算失控；
- 是否重复解决同一个问题；
- 是否存在前置节点无价值、只为后置铺路；
- 是否让某些技能完全退出循环；
- 是否让资源上限失去意义；
- 是否改变 Target/Trigger 后破坏旧配置；
- 是否与装备/队友形成极端组合。

## 11. 输出建议

正式技能成长至少给：

| 节点 | 解锁条件 | 影响技能 | 类型 | 当前规则 | 新规则/数值 | 循环作用 | 风险 | 验证 |
|---|---|---|---|---|---|---|---|---|

## 12. Anti-patterns

- **Linear Tree Cosplay**：看似技能树，实际全是线性加数；
- **Identity Locked Late**：角色核心身份太晚才解锁；
- **Problem-Sell-Solution**：先制造缺陷，再用高阶节点修掉；
- **Upgrade Soup**：节点主题混乱；
- **Window Spill**：纸面收益无法在实际窗口兑现；
- **Rank Inflation**：等级很多，但每级无感；
- **Dead Rank**：升级某技能却几乎不在实战使用；
- **Mechanic Overload**：每个里程碑都加新规则，导致认知爆炸。


---

## Canonical source: references/hero-roster-architecture.md

# Hero Roster Architecture

> 用途：设计角色池、英雄定位、队伍生态和新角色扩展时使用。
>
> 边界：参考角色制 RPG/动作游戏的公开设计模式，只抽象角色生态和团队关系，不复制具体角色或商业化配置。

## 1. 角色池不是职业表

角色池至少同时覆盖：

- Role：输出/生存/控制/辅助；
- Phase Ownership：准备、打条、开窗、爆发、续航；
- Resource Relation：生成/消费/中性；
- Trigger：主动、受击、敌方行动、队友行动、状态；
- Target Shape：单体、扩散、群体；
- Team Hook：创造/消费什么团队条件；
- Field/Action Time：占用前台或行动资源；
- Failure Case：在哪类内容显著降值。

两个角色即使都是“输出”，只要上面维度不同，就可以形成不同决策。

## 2. Same Job, Different Decision

扩充角色池时优先问：

> 新角色让玩家做了什么以前不同的决策？

而不是：

> 新角色是不是比旧角色伤害高 15%？

可通过：

- 不同资源循环；
- 不同爆发窗口；
- 反击 vs 主动；
- 单体 vs 多目标；
- 状态引爆 vs 自身输出；
- 生命换资源 vs 时间换资源；
- 前台持续站场 vs 速切；
- 敌方行动驱动 vs 队友行动驱动；

实现横向差异。

## 3. Roster Archetype Ecology

可把角色生态拆成：

- **Carry**：主要兑现输出；
- **Engine**：启动/维持体系；
- **Enabler**：创造条件；
- **Converter**：把状态/资源转为收益；
- **Amplifier**：放大已有循环；
- **Anchor**：生存/稳定；
- **Bridge**：连接两个体系；
- **Flex**：低依赖、补位。

角色不必唯一归类，但要知道它对队伍结构承担什么作用。

## 4. Synergy Gate 分级

队伍条件可以分：

- **Natural Synergy**：机制自然互补；
- **Soft Gate**：满足属性/阵营/状态后额外增强；
- **Strong Gate**：不满足条件损失明显；
- **Hard Pair Lock**：核心循环依赖唯一角色。

新角色默认避免 Hard Pair Lock。

如果采用强绑定，需要明确：

- 玩家为什么接受；
- 是否有替代队友；
- 旧角色是否被排除；
- 抽取/养成成本是否放大；
- 内容是否会反向强迫该组合。

## 5. Team Slot Economy

每个队伍槽位都是机会成本。

角色价值不只看个人收益，还要看：

`Net Team Value = Personal Contribution + Enabled Team Value - Slot Opportunity Cost - Resource/Field Cost`

该式是设计模型，不是统一战斗公式。

一个辅助如果只给数值但占据一个完整槽位，需要证明它对团队循环的提升足够大。

## 6. Self-Contained vs Ecosystem Character

### Self-Contained
自身能完成 Setup -> Payoff，队友主要增强效率。

优点：泛用、容易理解。

风险：如果数值也顶级，会挤压体系角色。

### Ecosystem
需要队友提供状态、攻击类型或触发事件，自身负责引爆/转换/放大。

优点：形成配队深度。

风险：抽卡/养成依赖、Pair Lock、环境适应性差。

角色池应有两者，不要全部走一个极端。

## 7. Roster Power Creep Control

新角色扩展优先增加：

- 新触发方式；
- 新 Team Hook；
- 新 Target Shape；
- 新资源转换；
- 新战斗阶段职责；
- 新风险/收益关系；

而不是单纯抬高：

- 基础倍率；
- 全覆盖 Buff；
- 无条件减抗；
- 永久行动优势。

当新角色“旧角色所有优点 + 更高数值 + 无旧缺点”，即进入 Direct Replacement 风险。

## 8. Stat Identity

角色主要属性应与职责尽量对齐。

例如：

- 防御角色以防御驱动护盾，同时部分输出也读取防御；
- 生命型角色以生命承担风险并转换资源；
- 异常/状态角色围绕状态效率构筑。

目的是形成 Build Identity，不是让每个角色只堆单一属性。

警惕：一个属性同时把输出、生存、资源全部无上限放大，会造成 Double/Triple Scaling。

## 9. Roster Coverage Matrix

正式扩充角色池前维护矩阵：

| Hero | Primary Role | Phase | Resource | Trigger | Target | Team Hook | Field Time | Dependency | Failure Case |
|---|---|---|---|---|---|---|---|---|---|

新增角色应回答它填补了哪个空白，或为什么有必要与现有格子重叠。

## 10. Hero Fantasy 与 Mechanic Resonance

技能循环最好能表达角色幻想。

例如“赌徒”可以围绕风险、筹码、波动；“反击剑士”围绕承受/等待/反制；“变身机甲”围绕蓄能、启动、强化时间窗。

不是要求所有技能文字都剧情化，而是：

> 把机制去掉美术名字后，玩家行为仍然应该与角色气质一致。

## 11. Onboarding 与 Complexity Budget

角色复杂度预算至少考虑：

- 新资源数量；
- 新状态数量；
- 新 UI 图标；
- 触发条件；
- 例外规则；
- 队伍要求；
- 操作顺序；
- 敌方状态依赖。

高稀有度不等于必须更复杂。

新手角色可以通过低规则量 + 高反馈建立理解，后续角色再增加组合复杂度。

## 12. Anti-patterns

- **Direct Replacement**：新角色覆盖旧角色全部功能且更强；
- **Role Compression**：一个角色承担过多队伍职责；
- **Pair Lock**：角色只能绑定唯一队友；
- **Synergy Tax**：不满足阵营/属性条件就像残缺角色；
- **Generic Buffer Flood**：大量角色只是不同数值的全队增伤；
- **Stat Identity Collapse**：所有输出最终都只堆同一套属性；
- **Roster Without Counterplay**：角色池很丰富，但关卡从不改变各角色价值；
- **Complexity Inflation**：新角色只能靠增加更多名词显得新。
