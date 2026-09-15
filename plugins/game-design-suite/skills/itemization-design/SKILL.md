---
name: itemization-design
description: 负责装备与物品化系统（Itemization）设计、审计和数值结构，包括装备槽位、品质、基础属性、主/副词条、词条池、Roll范围、强化、套装、唯一特效、掉落、替换曲线、毕业周期、分解回收、Build生态与Best-in-Slot风险。用于武器、防具、饰品、遗物、符文、芯片、神器等可装备/可构筑物品；具体战斗价值与倍率协同 balance-design，长期成长协同 progression-design，资源与掉落经济协同 economy-design。
---

# Itemization / 装备与物品化设计

目标不是“给装备加一些属性”，而是建立一套能长期支持角色成长、Build选择、Loot期待、资源循环和版本生态的装备系统。

优先读取：

- [Itemization Architecture](references/itemization-architecture.md)
- [Affix Budget & Roll Model](references/affix-budget-and-roll-model.md)
- [Loot, Replacement & Salvage Economy](references/loot-replacement-and-salvage.md)
- [Itemization Audit Template](templates/itemization-audit.md)

## 强制用户可见输出协议（MUST）

每一个独立装备结构结论、属性预算结论、词条池判断、强化方案、套装/唯一特效判断、掉落/替换结论或Build生态结论前，都必须先显示：

```text
【本次专业视角】
主责：装备 / Itemization 策划（itemization-design）
协同：仅列当前结果真实使用的专业
```

常见协同：

- `balance-design`：属性价值、Power Budget、DPS/EHP/TTK、特殊效果强度；
- `progression-design`：强化、品质、装备等级、突破、长期替换与毕业节奏；
- `economy-design`：掉落、强化成本、分解、回收、商店、重复物价值；
- `simulation-design`：词条分布、毕业时间、掉落概率、Build覆盖和极端组合模拟；
- `meta-balance`：Best-in-Slot集中、角色×装备矩阵、Build垄断、Power Creep；
- `config-audit` / `code-verification`：真实表字段、随机规则、权重、强化/套装实现；
- `skill-design`：装备特效与角色技能循环、触发和Team Hook的关系。

Direct Specialist Entry 仍执行共享 First-Visible-Line / Section Gate / Pre-Send Header Lint。

---

## 1. 先定义 Itemization Job

设计任何装备系统前，先回答它在项目里负责什么：

- **Progression**：提供长期成长与替换；
- **Build Expression**：让玩家形成不同构筑；
- **Loot Excitement**：提供掉落期待和惊喜；
- **Role Support**：强化角色定位；
- **Encounter Adaptation**：针对不同敌人/模式调整；
- **Collection**：收集与完成度；
- **Economy Loop**：制造、强化、分解、交易或资源循环；
- **Seasonal/Live Content**：版本追求和Meta变化。

如果装备只是在已有成长外再叠一层“更多攻击/生命”，但没有新的决策或体验价值，先标记为 `Progression Redundancy` 风险。

---

## 2. Slot Architecture / 槽位架构

每个槽位必须有明确职责，不默认所有槽位都是同一张属性表。

可按项目划分：

- Weapon / Main-hand：输出、技能行为、攻击资源；
- Armor / Body：生存、减伤、抗性；
- Shoes / Boots：速度、移动、行动经济；
- Accessory：功能、暴击、资源、条件强化；
- Relic / Rune / Chip：Build特化、规则修改、套装；
- Class/Character-specific Slot：身份强化，但警惕专属绑定。

至少检查：

- Slot 是否承担不同决策；
- Slot Power Budget 是否合理；
- 是否存在某槽位对总强度贡献过大；
- 某槽位是否只有唯一正确答案；
- 是否出现“所有输出都找同一属性、所有坦克都找同一属性”的伪选择。

---

## 3. Item Power Budget

装备总预算建议拆为：

`Total Item Budget = Base Stat Budget + Affix Budget + Special Effect Budget + Set/Collection Budget - Constraint/Condition Cost`

该式是分析框架，不是跨项目固定公式。

必须明确：

- 每个属性的预算单位；
- 属性价值来自哪个 Benchmark；
- 固定值与百分比是否同价；
- 是否存在边际收益递减/递增；
- 是否跨过攻速、暴击、能量、命中等 Breakpoint；
- 特效是否有 Uptime / Reliability / Applicability 折扣；
- 装备是否同时吃多个乘区形成 Double/Triple Scaling。

**禁止把固定的 `ATK:DEF:HP` 比例直接当装备预算真理。** 属性交换率应来自当前项目公式、Benchmark和模拟。

---

## 4. Base Stat / Main Stat / Substat

先区分三类价值：

### Base Stat
装备天然提供，建立槽位和品质身份。

### Main Stat
玩家最主要的装备选择轴，数量应有限、可读、可比较。

### Substat / Affix
提供Build差异、随机性和追求空间。

检查：

- 主词条是否足以产生真实选择；
- 副词条是否只是“继续堆主词条”；
- 同属性是否允许同时出现在主/副词条；
- 固定值属性是否会在后期完全失效；
- 百分比属性是否在后期无限放大；
- 稀有属性是否真正稀有，还是只是低权重但必选；
- 是否存在明显 Dead Affix。

---

## 5. Affix Pool / 词条池

每个词条池至少定义：

- Eligible Slots；
- Tier；
- Min/Max Roll；
- Weight；
- Mutual Exclusion / Group；
- Required/Forbidden Tags；
- Duplicate Rule；
- Rarity Gate；
- Level/Item Power Gate；
- Roll Count；
- Upgrade Roll Rule。

词条设计需要同时检查：

- **Power**：值不值；
- **Frequency**：出现多频繁；
- **Compatibility**：哪些角色/Build能用；
- **Readability**：玩家能否理解；
- **Search Space**：毕业组合有多难；
- **Dead Roll Rate**：掉落中有多少天然废词条；
- **False Choice**：看似很多词条，实际只有暴击/攻速等少数有效。

词条池越大不自动等于Build越丰富。

---

## 6. Roll Range / 随机Roll

随机词条必须明确：

- 是离散档位还是连续区间；
- 初始Roll数；
- 强化时新增词条还是提升旧词条；
- 是否等概率；
- 是否按词条Tier加权；
- 是否有保底/纠偏/定向；
- 是否允许锁词条/重铸；
- 重铸是否保留品质/强化；
- 玩家能否判断“好Roll”和“坏Roll”。

随机系统不能只看期望值，还要看：

- P50 / P90 / P95毕业时间；
- 极端坏运气；
- Best-in-Slot概率；
- 可用装备概率；
- 目标Build的有效掉落率；
- 重复刷取疲劳。

复杂随机模型交给 `simulation-design`。

---

## 7. Quality / Rarity Ladder

品质差异可以来自：

- Base Budget；
- Affix Count；
- Affix Tier；
- Roll Range；
- Enhancement Cap；
- Unique Effect；
- Set Access；
- Rule Modification。

不要默认每升一个品质就全部维度同时变强，否则容易指数膨胀。

品质梯度至少检查：

- 低品质是否有过渡价值；
- 高品质是否只是纯数值碾压；
- 新品质是否直接让旧品质全部报废；
- 品质与获取难度是否匹配；
- 高品质装备是否因为随机副词条反而经常不如低品质。

---

## 8. Enhancement / 强化曲线

强化系统要同时设计：

- 强化上限；
- 每级增长；
- 关键节点；
- 消耗曲线；
- 成功/失败规则（若存在）；
- 返还/继承；
- 换装损失；
- 强化是否改变词条；
- 强化是否形成 Sunk Cost Trap。

验证：

`Upgrade Power Delta <-> Upgrade Cost Delta <-> Replacement Probability`

常见问题：

- 强化太强 -> 玩家不愿换新装备；
- 强化太弱 -> 强化系统没有意义；
- 继承损失太大 -> 形成换装惩罚；
- 成本随等级暴涨但收益线性 -> 后段成为纯税。

成长节奏交给 `progression-design` 协同。

---

## 9. Set Bonus / 套装

套装价值拆为：

`Set Value = Stat Value + Behavior Change + Synergy Value - Slot Lock Cost - Flexibility Loss`

检查：

- 2件/4件/6件是否形成合理阶梯；
- 套装是否强到压死散件；
- 套装是否只服务单一角色；
- 为凑套装牺牲的高质量单件是否有真实机会成本；
- 套装效果是否与角色循环真正交互；
- 是否产生永久Buff、无限资源、近无限循环；
- 是否因为环境变化导致整套装备失效。

强套装可以存在，但不能自动成为所有角色的唯一答案。

---

## 10. Unique / Legendary Effect

唯一特效、专武、神器等应先定义它改变什么：

- 数值倍率；
- Target；
- Trigger；
- Resource；
- Rotation；
- State；
- Team Hook；
- Encounter Response。

优先奖励“新的决策/循环”，而不是单纯更大的乘区。

### 专属装备 Guard

专武/专属遗物需要检查：

- 没有专武时角色是否完整可玩；
- 专武是否只修复人为缺陷；
- 专武提升是纵向强度还是机制解锁；
- 是否形成 `Mandatory Signature / Equipment Tax`；
- 通用装备是否仍有意义。

---

## 11. Loot Quality / 可用掉落率

掉落设计不能只给“橙装5%”。

至少区分：

- Item Drop Rate；
- Target Slot Rate；
- Target Set Rate；
- Target Main Stat Rate；
- Usable Affix Rate；
- Good Roll Rate；
- Upgrade-compatible Rate；
- Actual Build Upgrade Rate。

概念上：

`Actual Upgrade Chance ≈ Drop × Slot × Set × MainStat × UsableAffix × RollQuality`

各项未必独立，正式计算需按真实规则建模。

如果单层概率都“看起来不低”，乘起来后仍可能导致极端低的实际升级概率。

---

## 12. Replacement Curve / 替换曲线

装备成长必须回答：

- 新装备多久出现一次；
- 多久产生一次真实Upgrade；
- 旧装备平均服役多久；
- 强化投入多久被替换；
- 前期/中期/后期替换速度如何变化；
- 毕业后还有什么追求；
- 版本更新如何避免一键报废整个库存。

可跟踪：

- Time-to-First-Usable；
- Time-to-Upgrade；
- Time-to-Best-in-Slot；
- Replacement Frequency；
- Inventory Obsolescence Rate；
- P50/P90/P95 Graduation Time。

---

## 13. Salvage / Duplicate / Crafting Economy

废装备必须有合理去向，但不要为了制造 Sink 强迫分解。

可设计：

- Sell；
- Salvage；
- Feed / EXP；
- Crafting Material；
- Reforge Currency；
- Set Conversion；
- Target Craft；
- Collection/Archive。

检查：

- 废装是否仍有价值；
- 分解是否产生闭环通胀；
- 重铸成本是否远高于重新刷取；
- 重复高稀有装备是否令人沮丧；
- 定向制作是否摧毁Loot期待；
- 装备库存是否无限堆积。

资源生命周期由 `economy-design` 主责。

---

## 14. Build Ecology / 装备生态

单件装备正常不代表生态健康。

至少根据项目建立：

- Character × Item Matrix；
- Build × Item Matrix；
- Item × Encounter Matrix；
- Slot Competition Matrix；
- Set / Unique Synergy Matrix。

检查：

- Best-in-Slot集中度；
- Top-N装备使用集中；
- 角色是否共享同一套装备答案；
- 专武依赖；
- Build多样性；
- 装备是否制造不可替代Pair Lock；
- 新装备是否产生Power Creep；
- 某词条是否因为底层公式成为无条件第一属性。

生态问题交给 `meta-balance` 协同验证。

---

## 15. Deterministic vs Random Itemization

不同项目不应被迫使用随机词条。

### Deterministic
适合强调规划、明确成长、低重复刷取成本的项目。

### Randomized
适合强调Loot、长线刷取、Build探索的项目，但必须控制坏运气和Dead Roll。

### Hybrid
固定主结构 + 随机副词条 / 可定向重铸，常用于兼顾确定性与追求。

先服务目标体验，再决定随机程度。

---

## 16. Itemization Benchmark

正式比较装备时至少固定：

- 角色/职业/Build；
- 等级/技能/其他成长；
- 槽位；
- 装备等级/品质；
- 强化等级；
- 主/副词条；
- 敌人/关卡；
- 战斗时间窗；
- 资源/触发状态；
- 是否考虑队友和套装；
- 随机模型/Seed（若相关）。

不同装备不能在不同Benchmark下直接横比。

---

## 17. Evidence Boundary

根据证据标记：

- 设计规则明确 -> `confirmed`；
- 表直接确认 -> `verified-config`；
- 代码确认 -> `verified-code`；
- Runtime确认 -> `verified-runtime`；
- Telemetry确认 -> `verified-data`；
- 新装备数值方案 -> `candidate`；
- 模拟 -> Simulation evidence，不自动等于Playtest。

外部游戏的词条数量、掉率、强化曲线、套装倍率只能作为参考，不可直接复制为通用标准。

---

## 18. Done Criteria

一次完整Itemization任务至少按需交付：

- Itemization Job；
- Slot Architecture；
- Quality/Rarity Ladder；
- Base/Main/Substat结构；
- Attribute/Power Budget；
- Affix Pool与Roll规则；
- Enhancement曲线；
- Set/Unique预算；
- Drop/Targeting模型；
- Replacement/Graduation目标；
- Salvage/Duplicate处理；
- Build/Meta风险；
- Simulation/Telemetry/Playtest验证计划；
- Evidence状态。

---

## 19. 反模式

- **Stat Soup**：所有装备都堆同一批属性；
- **Fake Choice**：词条很多，但有效词条只有少数；
- **Dead Affix Pool**：大量掉落天然不可用；
- **Best-in-Slot Lock**：每个角色只有唯一装备答案；
- **Signature Tax**：角色必须专武才能完整；
- **Set Prison**：套装收益压死所有散件；
- **Power Creep Ladder**：新版本只能靠更高Item Power吸引玩家；
- **Upgrade Hostage**：强化沉没成本阻止换装；
- **Loot Lottery Without Floor**：多层随机相乘却没有纠偏；
- **Overrandomized Progression**：成长结果主要由运气而非决策决定；
- **Guaranteed Loot Without Choice**：完全确定性但没有Build选择；
- **Salvage Inflation Loop**：分解与重铸形成自我增殖；
- **Universal Stat Ratio**：跨项目硬套固定属性交换率；
- **Average-only Loot Model**：只看期望掉落，不看P90/P95坏运气。

---

## 20. 跨 Skill 交接

当前结果核心是：

- 装备结构、槽位、词条池、套装、唯一特效、掉落可用率 -> `itemization-design` 主责；
- 某属性/特效到底强多少 -> `balance-design` 主责；
- 强化/品质/装备等级的长期节点 -> `progression-design` 主责；
- 掉落资源、强化材料、分解、商店与通胀 -> `economy-design` 主责；
- 大规模掉落/毕业时间/极端Roll模拟 -> `simulation-design` 主责；
- 多角色装备使用集中、BiS、版本生态 -> `meta-balance` 主责；
- 表字段/权重/随机池是否配置正确 -> `config-audit` 主责；
- 程序如何Roll、继承、重铸、触发 -> `code-verification` 主责。

不要用一个“装备策划”Header覆盖这些不同Decision Object。