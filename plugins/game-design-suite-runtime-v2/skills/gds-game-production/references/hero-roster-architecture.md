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