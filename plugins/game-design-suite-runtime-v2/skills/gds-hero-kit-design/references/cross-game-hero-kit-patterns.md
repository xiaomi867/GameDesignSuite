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
