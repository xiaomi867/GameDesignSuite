# Hero / Skill / Combat Regression Evals

这些用例用于防止英雄与技能设计退化成“堆技能 + 拍倍率 + 职业标签”。

## H1 Kit Before Buttons

**Prompt**

> 设计一个新输出英雄，普攻、技能、大招、两个被动都给我。

**Expected**

- 先给 Core Loop / Identity，而不是直接填技能栏；
- 明确 Generator / Setup / Payoff / Recovery；
- 再映射到技能；
- 若所有技能互不关联，判定 Kit Identity 不足。

**Fail**

- 普攻 100%，技能 200%，大招 500%，被动加暴击/加伤。

## H2 Role by Behavior, Not Label

**Prompt**

> 这是一个坦克，因为我把职业标签写成 Tank。

**Expected**

- 检查 Target、受击价值、护盾/减伤、团队保护、资源、Phase Ownership；
- 职业标签不能替代行为证据。

## H3 Reactive Trigger Reliability

**Prompt**

> 角色所有伤害都来自受击反击，伤害很高，所以肯定很强。

**Expected**

- 检查敌人攻击频率、嘲讽/Target、Boss 演出、单体/群体、触发上限；
- 计算/估计 Trigger Reliability；
- 要求保底或主动替代方案的必要性由证据决定。

## H4 State Transformation Must Have a Cycle

**Prompt**

> 大招后进入强化状态，强化状态所有技能都更强。

**Expected**

- 检查进入成本、状态时长、退出、Recovery、资源规则、技能替换；
- 检查强化状态覆盖率是否高到变成永久 Burst；
- 检查“资源满但窗口不对”的情况。

## H5 Resource Graph

**Prompt**

> 角色有一个 10 层特殊资源，你帮我平衡一下。

**Expected**

- 先问/定义 Source -> Storage -> Converter -> Sink -> Reset；
- 不直接定 10 层每层 +X%；
- 检查上限、溢出、消费时机与玩家决策。

## H6 Team Hook vs Pair Lock

**Prompt**

> 为了体现配队，我想让角色没有同阵营队友时核心技能不生效。

**Expected**

- 区分 Soft Synergy / Strong Gate / Hard Pair Lock；
- 检查是否形成 Team Tax；
- 优先讨论额外增强而不是让基础循环残缺。

## H7 Upgrade Must Fit Window

**Prompt**

> 一星让爆发期多攻击 3 次，所以提升就是这 3 次攻击的完整倍率。

**Expected**

- 检查 Burst/Break/Stun Window；
- 计算动作、动画、Setup 占用；
- 只按可兑现部分估计 Realized Value；
- 不把 Paper Value 直接当实战提升。

## H8 Skill Tree Is Not Linear Tree Cosplay

**Prompt**

> 技能树每个节点都加 5% 攻击，这样最清晰吧？

**Expected**

- 区分 Skill Rank / Major Passive / Minor Stat / Milestone / Capstone；
- 指出全加攻击会失去玩法里程碑；
- 但不强迫每个节点都增加新机制。

## H9 Identity Must Not Be Locked Late

**Prompt**

> 角色到 6 星后才获得核心循环，0~5 星主要是基础攻击。

**Expected**

- 标记 Identity Locked Late / Problem-Sell-Solution 风险；
- 核心身份应早期可见，高阶节点负责深化与拓展。

## H10 Team Combat Loop

**Prompt**

> 队伍有输出、坦克、治疗三个职业，所以职责已经完整。

**Expected**

- 继续定义 Phase Ownership、资源关系、行动/前台占用、Team Hook、Failure Case；
- 不用职业名称代替团队循环。

## H11 Gauge Is Not Extra HP

**Prompt**

> 我给敌人加一个 1000 点失衡条，打空后眩晕 2 秒，这就能让战斗更深。

**Expected**

- 检查谁负责积累、窗口如何兑现、重复触发、Boss 差异、队伍职责；
- 若只是额外需要打空的条，标记 Second HP Bar 风险。

## H12 Cross-State Interaction

**Prompt**

> 两种状态一起存在时伤害 +20%，这样就算体系联动吧？

**Expected**

- 检查是否产生新的操作/配队/时机决策；
- 优先考虑状态引爆、转换、窗口、资源等交互；
- 单纯加伤可以成立但不自动等于深度联动。

## H13 Encounter Must Allow Kit to Happen

**Prompt**

> 反击角色在 Boss 关很弱，因为 Boss 每 20 秒只攻击一次，怎么把角色伤害加高？

**Expected**

- 先判断是数值问题还是 Encounter Contract 问题；
- 检查 Attack Frequency、Target、Trigger Reliability；
- 不默认用倍率补偿所有内容行为问题。

## H14 Boss Stress, Not Nullify

**Prompt**

> 这个体系太强，所以新 Boss 直接免疫异常、控制、反击触发。

**Expected**

- 标记 System Invalidation / Boss Immunity Soup；
- 优先用节奏、窗口、目标、转火、资源和有限免疫制造 Stress；
- 如果必须免疫，要求明确 Telegraph、替代解法、有限持续和回报窗口。

## H15 Field-Time Opportunity Cost

**Prompt**

> 四个角色都按各自最高 DPS 循环算，队伍总 DPS 就是相加。

**Expected**

- 拒绝直接相加；
- 检查 Field/Action Time、共享资源、换人、Burst Window 竞争；
- 输出团队级 Rotation。

## H16 New Hero Must Add a Decision

**Prompt**

> 新英雄和旧英雄机制一样，但伤害高 20%，这样玩家会想抽吧？

**Expected**

- 标记 Direct Replacement / Power Creep 风险；
- 优先检查新 Trigger、资源、Target、Phase、Team Hook 或风险收益关系；
- 商业目标不能自动豁免长期角色生态风险。