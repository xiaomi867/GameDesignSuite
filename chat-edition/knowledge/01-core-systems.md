# Game Design Suite Chat Edition — Core / Systems

> Purpose: project knowledge for ordinary Chat mode. This file is NOT a Skill and does not depend on Skill/Plugin runtime.
> The assistant should use the relevant sections as professional guidance, while distinguishing verified evidence from candidate design.

## Usage

- Use this file when the current decision object belongs to **Core / Systems**.
- For cross-system work, also consult the smallest necessary supporting knowledge files.
- Do not claim that a Skill was invoked. Say which professional domain or project knowledge was used when useful.
- User-fixed mechanics are constraints, not redesign targets, unless the user explicitly reopens them.


---

# Source Module: gds-game-design

# Canonical Detailed Guidance

> Preserved from the canonical Game Design Suite specialist. The runtime wrapper is intentionally compact; this file retains the detailed domain rules, workflows, guards, anti-patterns, and done criteria.

# 游戏设计总入口

## 基础原则

1. 用户描述问题，AI 判断专业边界。
2. 使用最小充分 Skill 集，不机械全开。
3. 已有项目先理解现状，不把项目当白纸。
4. 用户明确要求保持不变的机制、范围或规则视为硬约束。
5. 多 Skill 参与时形成统一结论，不机械拼接。
6. 区分 `confirmed / supported-inference / candidate / assumed / unknown / verified-config / verified-code / verified-runtime / verified-data / not-yet-playtested / externally-blocked`。
7. 路由不是最终答案；继续把任务做完。
8. 专业身份来自实际路由，不来自角色扮演。
9. 路由粒度是独立结果块，不是整篇答案。
10. Direct Specialist Entry 也必须执行共享 Header 规则。
11. 用户从不需要重复提醒 Header。
12. 私有项目资料只能用于当前项目分析和抽象方法验证，不得复制到公开通用 Skill、reference 或 eval。
13. 外部商业游戏资料只作为参考事实/模式，不能自动成为当前项目标准。
14. 英雄相关任务不再默认全部塞给 `skill-design`；按设定、Kit、等级属性、技能数值拆责。

## Professional Judgment Guard

用户输入先区分：

- **事实**：真实规则、数据、配置、代码、运行时或已确认约束；
- **症状**：资源很多、治疗卡没人拿、升级没感觉等；
- **偏好/约束**：不改技能机制等；
- **候选方案**：用户或历史方案提出的做法；
- **假设**：尚未被证据验证的解释。

不得把症状直接翻译成方案。

例如：

- 资源后期很多 ≠ 必须新增 Sink；
- 某卡没人拿 ≠ 只要加数值；
- 某角色总体胜率50% ≠ Meta一定健康；
- 模拟1000次均值稳定 ≠ 玩家体验已验证；
- Telemetry相关性 ≠ 因果关系；
- 角色设定“高速” ≠ 只要基础速度高；
- 技能Lv10看起来顺 ≠ Lv1~10整条曲线合理；
- 外部角色Lv10约为Lv1两倍 ≠ 当前项目也应该两倍；
- 三个成熟游戏都这么做 ≠ 当前项目应该照搬。

## Symptom-to-Root-Cause Rule

遇到局部症状至少检查：

1. **Local**：字段、倍率、奖励、单个对象；
2. **System**：Hero Contract、Kit、属性成长、技能数值、战斗、装备、经济、成长、公式或数据链；
3. **Cross-system**：上下游系统、生命周期、内容环境、玩家分层、版本生态。

只有局部根因成立时才做局部补丁。

## Missing Evidence Guard

当任务需要配置、代码、Telemetry、Playtest、地图、文档、外部详情页或其他证据但当前不可访问：

1. 只做一次必要可用性检查；
2. 依赖缺失证据的结论标 `unverified` / `externally-blocked`；
3. 列出最小缺失材料；
4. 继续所有不依赖缺失证据的工作；
5. 不从字段名、旧版本、相似游戏或公开资料补成当前项目事实；
6. 外部详情页、等级滑杆、技能等级表不可访问时，不从记忆补精确值；
7. 用户明确“不猜”时严格停在证据边界。

## 路由

### `game-production`
核心体验、玩法循环、系统规则、产品节奏、教程、奖励框架、制作约束、范围与跨系统设计。

### `design-frameworks`
MDA、Core Loop、Flow、设计张力、Pattern、Depth vs Complexity 等方法论。

### `hero-concept-design`
英雄/角色设定、Core Fantasy、阵营/元素/武器/职业标签、叙事身份、Combat Promise、角色池差异化、设定-玩法一致性。

### `hero-kit-design`
Hero Kit机制架构、技能槽位职责、状态机、资源图、Trigger Graph、循环、Target结构、Field/Action Time、Team Hook与失败恢复。

### `hero-stat-progression`
英雄Lv1~上限的HP/ATK/DEF等基础属性成长、突破/晋阶Delta、成长副属性、固定属性、职业/稀有度模板与阶段Power Curve。

### `skill-value-design`
技能Lv1~上限的伤害/治疗/护盾倍率、Buff/Debuff、概率、持续、资源、CD、层数、Fixed vs Scaled字段、技能等级收益与Extended Level。

### `skill-design`
已有项目中的综合技能设计、诊断和改造，尤其涉及Target、Buff/Debuff、配置映射、升星技能改动或用户明确要求“不要改机制”的任务。若Decision Object足够细，优先让四个Hero专业Skill主责。

### `combat-design`
战斗规则、攻击/受击、Target、状态、AI、资源、战斗节奏、遭遇结构。

### `balance-design`
角色总体倍率、DPS/HPS/EHP、控制覆盖、Power Budget、横向强度、参数区间、敌我Benchmark。

### `formula-verification`
伤害/治疗/护盾/防御/抗性/暴击/命中/攻速/行动/概率等公式还原、单位、乘区、Clamp/Round、定义域、边界与代码交叉验证。

### `simulation-design`
Monte Carlo、离散事件、Rotation/Timeline、参数扫描、策略代理、100/1000/10000次分布、敏感性、长周期状态模拟。

### `telemetry-experiment-design`
埋点、事件Schema、指标、玩家分群、漏斗、A/B测试、SRM、显著性、因果边界与线上验证。

### `meta-balance`
多角色/Build/队伍/内容生态、Matchup/Synergy/Counter矩阵、Pick/Win/Presence、Mastery、Power Creep、版本风险与多样性。

### `itemization-benchmark`
公开商业游戏的装备、武器、遗器、圣遗物、声骸等参考数据抽取、等级/强化曲线、结构归一化、跨游戏 Benchmark、可迁移模式与迁移边界。

### `itemization-design`
当前项目装备/Itemization系统、槽位、品质、基础/主/副词条、词条池与权重、随机Roll、强化、套装、唯一特效、Loot可用率、替换/毕业、分解回收、Best-in-Slot与Build生态。装备任务命中本专业时，必须先 load `itemization-design` directly。

### `economy-design`
资源Role、Sources/Sinks、库存、流速、价值锚、兑换、通胀、产销闭环。

### `progression-design`
账号/角色/装备/技能整体等级、星级、突破、技能树、解锁、成长节奏、追赶、长期上限与成长成本。若只讨论英雄基础属性随等级怎么变，转 `hero-stat-progression`；若只讨论技能等级倍率怎么变，转 `skill-value-design`。

### `level-design`
地图、关卡、布局、导航、空间教学、Encounter、波次、Boss、节奏与Metrics。

### `game-interface-design`
HUD、菜单、信息层级、引导、反馈、输入提示、Accessibility。

### `config-audit`
Excel/配置字段、Row/Key/ID、引用、漏配、重复、Group/Stack/Target一致性。

### `code-verification`
客户端/服务器读取、Parser、默认值、运行时目标、实际生效链路。

### `design-review`
已有方案评审、比较、风险、矛盾、反模式、下一步验证实验。

### `game-design-doc`
GDD、System Spec、Pitch Design Doc等正式文档。

## 常见组合

### 新英雄完整设计
按Decision Object依次使用：

`hero-concept-design -> hero-kit-design -> hero-stat-progression -> skill-value-design -> balance-design`

若涉及真实项目：`+ config-audit + code-verification`

若需要公式：`+ formula-verification`

若需要Rotation/极值：`+ simulation-design`

若判断角色池生态：`+ meta-balance`

### 已有英雄技能审计
先按问题拆：

- 设定与玩法是否一致 -> `hero-concept-design`
- 技能循环/状态/资源 -> `hero-kit-design`
- Lv1~LvMax基础属性 -> `hero-stat-progression`
- 技能Lv1~Max数值 -> `skill-value-design`
- 当前配置/代码 -> `config-audit + code-verification`
- 总体强度 -> `balance-design`

综合配置改造仍可由 `skill-design` 协调，但不能吞掉以上独立结果责任。

### 外部英雄参考 / 全量角色Wiki
当用户要求参考崩铁/原神/鸣潮等角色Wiki：

1. 先用总页建立完整角色Index；
2. 二级详情按角色/形态唯一键遍历；
3. 等级滑杆、技能等级切换必须记录Coverage；
4. 角色身份字段 -> `hero-concept-design`；
5. 技能槽位/循环 -> `hero-kit-design`；
6. 等级属性曲线 -> `hero-stat-progression`；
7. 技能等级参数 -> `skill-value-design`。

外部事实只能标 `reference-data`；详情页失败标 `externally-blocked`，不能静默补值。

### 外部装备对标
`itemization-benchmark + itemization-design`

比较具体属性/特效强度：`+ balance-design`

比较等级/突破/强化曲线：`+ progression-design`

比较毕业概率与随机层：`+ simulation-design`

比较套装/专武生态：`+ meta-balance`

### 装备 / Itemization
本 1.7.4 invocation 测试中：先 load `itemization-design` directly，并由它完成装备设计。不要在 root router 中预先并行调用其他专业；需要交叉验证时，等 `itemization-design` 成功加载后再追加 focused Skill。

### 公式审计
`formula-verification + config-audit + code-verification`

若还要判断强度：`+ balance-design`

### 批量战斗模拟
`simulation-design + formula-verification + balance-design`

若需要真实生产逻辑：`+ code-verification + config-audit`

### 上线后平衡验证
`telemetry-experiment-design + balance-design`

角色池/组合生态：`+ meta-balance`

装备生态：`+ itemization-design`

### 版本 / Roster 平衡
`meta-balance + balance-design + telemetry-experiment-design`

上线前预演：`+ simulation-design`

装备/专武/套装造成的生态问题：`+ itemization-design`

### 奖励与经济
`game-production + economy-design + progression-design + balance-design`

装备掉落/分解/强化材料：`+ itemization-design`

长期库存/成长模拟：`+ simulation-design`

线上验证：`+ telemetry-experiment-design`

### Boss / 关卡
`game-production + combat-design + level-design`

若比较角色适配覆盖：`+ meta-balance`

若装备是核心Encounter应对轴：`+ itemization-design`

### GDD
`game-production + 必要专业 Skill + design-review + game-design-doc`

## 英雄设计证据链

复杂英雄任务优先按需要形成：

`Design Intent -> Hero Concept -> Hero Kit -> Stat Progression -> Skill Values -> Formula -> Config/Code -> Simulation -> Runtime -> Telemetry -> Meta -> Playtest`

各层职责：

- Design Intent：为什么要有这个角色；
- Hero Concept：角色是谁、承诺什么体验；
- Hero Kit：机制怎么兑现；
- Stat Progression：等级成长如何支撑体质和Scaling Source；
- Skill Values：技能等级如何分配数值预算；
- Formula：乘区与数学结构；
- Config/Code：项目实际怎么执行；
- Simulation：Rotation、极端值、敏感性与分布；
- Runtime：真实实现是否一致；
- Telemetry：真实玩家行为；
- Meta：角色池与队伍生态；
- Playtest：理解、反馈、节奏、乐趣。

任何前一层都不能替代后一层证据。

## 装备/数值生产证据链

`Design Intent -> External Benchmark(optional) -> Itemization/Build Rules -> Formula -> Config/Code -> Simulation -> Runtime -> Telemetry -> Meta -> Playtest`

外部商业游戏的 `reference-data` 只能证明参考来源事实，不能自动升级为当前项目 verified。

## Private Project Isolation

用户提供真实项目代码、表、日志可以用于：

- 验证通用 Skill 是否覆盖真实生产问题；
- 提取不含业务细节的方法，例如 deterministic seed、Golden Test、Schema Guard、Runtime parity、Hero Contract、Stat Curve Guard、Skill Curve Guard、Loot funnel；
- 发现通用反模式与缺失能力。

不得写入公开通用 Skill：

- 私有项目名；
- 私有角色/技能/装备/表名；
- 私有ID；
- 私有代码路径；
- 私有真实公式；
- 私有英雄基础属性、技能倍率、装备数值、掉率、经济数据；
- 未公开业务规则。

若需要项目专属适配，应单独保存在用户项目私有 workspace，不污染通用 Skill。

## 已有项目规则

根据任务需要优先检查：

1. 用户确认规则；
2. 设计文档；
3. 配置表；
4. 代码与测试；
5. Runtime / 日志；
6. Telemetry / 实验；
7. 地图与内容；
8. 当前制作和技术约束。

外部参考只能进入“参考层”，不能覆盖以上项目真源。

关键证据缺失时继续完成独立可做部分，并明确未知项。

## 边界

- 不替专业 Skill 完成详细设计。
- 不把模拟、Spreadsheet、Telemetry相关性或理论分析描述成“已验证好玩”。
- 不把外部游戏的角色等级上限、技能等级倍率、属性成长、公式、装备掉率、词条数量、套装倍率或实验结果直接复制成本项目标准。
- 不因为三款成熟游戏都使用某结构，就自动把它标为当前项目最佳实践。
- 不保存无意义中间状态。


---

# Source Module: gds-game-production

# Canonical Detailed Guidance

> Preserved from the canonical Game Design Suite specialist. The runtime wrapper is intentionally compact; this file retains the detailed domain rules, workflows, guards, anti-patterns, and done criteria.

# 游戏玩法与系统策划

把玩家体验目标转化为可执行、可测试、可交付的系统规则。

涉及跨系统绑定、系统参与度、强制依赖或“为了联动而联动”时，优先读取 [System Coupling & Anti-patterns](system-coupling-and-antipatterns.md)。

涉及 Roguelite、三选一、祝福/卡牌池、Build、体系成型、随机权重、保底、主/副体系或局内共鸣时，优先读取 [Roguelite Build Architecture](roguelite-build-architecture.md)。

涉及机制教学、局内节奏、玩法 Beat、决策密度、系统如何交给关卡承载时，优先读取 [Gameplay Structure & Pacing](gameplay-structure-and-pacing.md)。

## Result-Level Professional Context

每一个独立玩法循环、系统规则、跨系统关系、奖励框架、教学或制作范围结论前，按 `../game-design/references/professional-context-header.md` 输出一次结果级 Header。

系统/玩法结构本身由 `game-production` 主责；经济根因转由 `economy-design` 主责；成长结构转由 `progression-design` 主责；具体数值强度转由 `balance-design` 主责；关卡空间与 Encounter 转由 `level-design` 主责。相邻结果即使专业组合相同，也重复显示 Header。

## 先定义设计问题

明确：

- Player Promise / 玩家幻想；
- 重复动作与决策；
- 目标情绪与行为；
- 成功、失败、压力与恢复；
- Session 长度；
- 目标玩家与平台；
- 内容、制作和性能约束；
- 当前问题最小可验证切片。

只有不同答案会显著改变设计时才追问；否则声明假设并继续。

## 症状不等于方案

用户或项目暴露出来的“资源多、选择少、成长没感觉、参与度低、内容消耗快”等首先是症状。

禁止直接做以下跳跃：

- 资源多 -> 新增 Sink；
- 系统参与度低 -> 强制绑定奖励/成长；
- 卡没人选 -> 只加数值；
- 内容不够 -> 只加重复玩法；
- 成长慢 -> 直接提高所有产出。

先判断根因属于：局部参数、系统结构、内容生命周期、上下游耦合、信息/UX、制作约束或玩家目标错配。

## 已有项目优先读取现状

不得默认重做已有项目。根据任务需要检查：

- 当前规则和文档；
- 配置与数据；
- Telemetry / Playtest；
- 内容与地图；
- 必要代码；
- 当前制作边界。

用户要求“不改机制”时，机制属于 Fixed Rule，只能调整允许变化的 Tunables。

## 系统设计模板

对每个系统明确：

1. 玩家输入或决策；
2. 系统状态；
3. 触发与规则；
4. 系统响应；
5. 玩家反馈；
6. 结果与后果；
7. 与其他系统依赖；
8. Fixed Rules；
9. Tunable Parameters；
10. 正常、边界、失败、恢复和 Exploit 路径；
11. 最小原型/模拟；
12. 观察指标和决策规则。

## Gameplay Structure

系统不能只描述“有什么功能”，还必须描述玩家如何在时间中体验它。

优先建立：

`Observe -> Interpret -> Decide -> Act -> Feedback -> Update Plan`

并检查：

- 这一系统新增了什么玩家动词；
- 是深化已有动词，还是只增加数值/UI；
- 机制第一次如何被教会；
- 什么时候进入真正测试；
- 后续如何 Twist/Combine；
- 什么时候允许玩家休息、领奖和重规划；
- Session 内有多少高压力决策；
- 是否出现“菜单时间 > 实际玩法时间”。

### Mechanic Lifecycle

新机制应同时规划内容生命周期：

`Introduce -> Practice -> Test -> Twist -> Combine -> Mastery`

系统策划必须向关卡策划提供首次教学条件、安全网、可调参数、失败恢复、Twist 方向和不允许的组合，而不是把系统做完后让关卡“自己想办法塞进去”。

### Decision Budget

选择不是免费的。每个关键决策都有时间和认知成本。

至少检查：

- 影响范围；
- 不可逆性；
- 信息量；
- 后续持续时间；
- 与 Build/队伍的耦合；
- 是否连续出现高压力选择；
- 是否发生在本就高压的战斗阶段。

“更多三选一”不自动等于“更有 Roguelite 深度”。

### Gameplay Rhythm

玩法元素应承担不同节奏角色：

- Pressure；
- Choice；
- Reward；
- Recovery；
- Setup；
- Payoff；
- Twist；
- Closure。

如果所有系统都在制造选择，玩家会菜单疲劳；如果所有系统都只给奖励，体验会失去张力。

### Intensity != Difficulty

玩法强度可以来自：

- 重新规划；
- 信息压力；
- 时间压力；
- 资源危机；
- 场地/目标变化；
- 不确定性；
- 情绪赌注。

不要把节奏问题全部交给敌人加血加攻。

## System Coupling Legitimacy

跨系统联动必须回答：两个系统为什么要发生关系，这个关系给玩家增加了什么决策或能力。

优先级通常是：

`能力/解锁联动 > 效率联动 > 选择联动 > 内容联动 > 资源转换 > 直接收费绑定`

直接让系统 A 的资源成为系统 B 的强制成本，是最强耦合之一，必须谨慎。

任何跨系统强绑定至少检查：

- 玩家认知是否自然；
- 是否增加真实决策；
- 是否破坏原系统职责；
- 是否制造 Mandatory Tax；
- 是否使玩家被迫玩不喜欢的系统；
- 是否增加新角色/新内容切换成本；
- 是否可以用解锁、效率、制造、可选加速等更自然方式实现。

**跨系统联动 ≠ 跨系统互相收费。**

## 跨系统检查

任何修改都检查：

- 上游输入；
- 下游影响；
- 战斗；
- 成长；
- 经济；
- 任务；
- 活动；
- 商店；
- 关卡；
- 养成；
- 留存；
- UX；
- 教程；
- 商业化（若存在）。

局部系统不能当孤岛，但也不能为了“看起来有联动”强行增加耦合。

## Roguelite 构筑规则

局内 Build 不应退化为“同标签卡越多越好”。至少检查：

- Seed：玩家何时知道本局方向；
- Engine：几张卡后核心循环真正成立；
- Scaler：成型后如何继续成长；
- Stabilizer：生存/资源/容错怎么补；
- Capstone：何时出现质变和完成感；
- 主体系 + 副体系关系；
- Off-build 卡是否仍有合理用途；
- 核心组件在关键波次前的出现概率；
- Dead Pick Rate；
- 成型保底；
- Boss 是否能反向检验构筑。

### 三选一不是静态卡牌比较

每次选择的价值取决于：

- 当前 Build；
- 已有核心卡；
- 当前血量/资源；
- 距离 Boss 的阶段；
- 队伍构成；
- 后续成型概率；
- 当前选项的机会成本。

禁止只按“卡牌品质/裸倍率”排序。

### 构筑阈值

可通过同体系数量阈值、共鸣、成型件提供阶段性回报，但阈值数量必须由本项目一局选择次数推导，不照抄外部参考游戏。

### 动态随机

允许根据局内状态动态调整权重，例如：

- 已选体系；
- 连续未出主体系；
- Build 缺失组件；
- Boss 前生存不足；
- 奶妈存在且队伍低血；
- 已经完成引擎后降低重复低价值组件。

动态权重用于降低“随机系统拒绝玩家构筑”的挫败，不应保证每局完美成型。

### 随机玩法仍需结构保证

随机只意味着具体内容可变，不代表宏观节奏无需设计。

需要定义：

- 连续高压事件上限；
- 关键决策最小间隔；
- Boss 前恢复下限；
- 新机制首次出现的安全环境；
- Build 核心组件的最低可达性；
- P50/P90 Session 时长。

## 玩法策划关注点

### Core Loop
检查 `Act -> Feedback -> Reward -> Repeat` 是否闭合，内层输出是否支撑外层循环。

### Choice Quality
选项必须产生真实取舍。关注 Opportunity Cost、信息充分度和后果可读性。

### Failure & Recovery
失败原因可理解，存在恢复路径，避免形成“失败 -> 更弱 -> 更容易继续失败”的负循环。

### Onboarding
优先通过真实玩法教学。可参考：

`Introduce -> Practice -> Confirm -> Combine -> Apply Under Pressure`

不要一次引入多个新规则，也不要把弹窗当机制教学的默认替代品。

### Content Scope
内容数量必须与团队、周期和复用能力相匹配，不用“很多内容”代替预算。

同一机制能否通过环境、目标、敌人、时间和组合产生变奏，比单纯增加新机制数量更重要。

## 常见系统反模式

- **Forced Coupling**：为了联动而强行绑资源或进度；
- **Progression Hostage**：用一个系统卡住另一个系统核心成长；
- **Patch Stacking**：用新功能覆盖旧结构问题；
- **Mandatory Tax**：没有决策价值的固定消费；
- **Feature-as-Fix**：发现问题第一反应是再加一个系统；
- **Reward Bribery**：系统本身无价值，只靠奖励强迫参与；
- **Hollow Loop**：奖励不能反馈到下一层循环；
- **Complexity Over Depth**：规则增加而决策没有增加；
- **Same-color Drafting**：Roguelite 只剩同体系卡越拿越多；
- **Core-or-Brick**：没抽到单张核心卡整局直接报废；
- **Fake Choice Pool**：大量不属于当前 Build 的死选项；
- **Completed-build Lottery**：只平衡最终成型强度，不管成型概率；
- **Choice Spam**：选择密度高到吞掉实际玩法；
- **Difficulty-only Pacing**：用战力曲线替代节奏设计；
- **Mechanic Dump**：一次性把多个新系统扔给玩家；
- **Random = No Structure**：把“随机”当成“不需要编排”。

## 平台与性能

性能是设计约束。根据目标平台考虑同屏单位、Projectile、Physics、VFX、动画、UI 更新、后台模拟、网络、Streaming、CPU/GPU/内存等。

不凭直觉宣称“低端可运行”；需要 Profiling 或目标设备证据。

## 可执行交付

用户要求落地时，根据任务包含：

- Intent
- Player Outcome
- Rules
- States / Transitions
- Player Verbs
- Mechanic Lifecycle
- Decision Budget
- Rhythm Roles
- Tunables
- Dependencies
- Coupling Rationale
- Level Handoff
- Technical Touchpoints
- Exclusions
- Acceptance Scenarios
- Open Decisions

Roguelite 还应根据需要包含：

- Build Inventory；
- Core/Support/Capstone 标签；
- Pool / Weight；
- Completion Threshold；
- Pity / Guarantee；
- Build Completion Rate；
- Dead Pick 指标；
- Boss Check。

## 验证

- 规则：状态路径 walkthrough / 配置 / 实现检查
- 数值：交给 `balance-design`，再通过模拟/对照/实战数据
- 经济：交给 `economy-design`，同时检查 Resource Role 与 Sink Legitimacy
- 成长：交给 `progression-design`，检查 Cost Semantics 与 Switching Cost
- Roguelite：同时检查构筑成型概率、Dead Pick、Choice Quality、极端 Build、Boss Conversion
- 玩法节奏：与 `level-design` 联合检查 Beat、Decision Budget、休止符、峰值和真实时长
- 可用性：代表性用户测试
- 好玩：Playtest，不可由文档证明
- 性能：Profiling

## 专业分工

优先下沉：

- 关卡 -> `level-design`
- 技能 -> `skill-design`
- 战斗 -> `combat-design`
- 数值 -> `balance-design`
- 经济 -> `economy-design`
- 成长 -> `progression-design`
- UI/UX -> `game-interface-design`
- 配置 -> `config-audit`
- 代码 -> `code-verification`


---

# Source Module: gds-design-frameworks

# Canonical Detailed Guidance

> Preserved from the canonical Game Design Suite specialist. The runtime wrapper is intentionally compact; this file retains the detailed domain rules, workflows, guards, anti-patterns, and done criteria.

# 游戏设计方法论

本 Skill 是知识与分析层，不是总路由，不直接决定生产配置。

## Result-Level Professional Context

每一个独立方法论判断或 Framework Finding 前，按 `../game-design/references/professional-context-header.md` 输出一次结果级 Header。即使连续结果专业组合相同也重复；如果当前结果实际转入关卡、数值、经济、技能等生产决策，则对应专业应成为主责，本 Skill 只作为协同，不要把“方法论”长期占据主责。

## Iconic Mechanic

识别玩家能用一句话概括的机械身份。它应：

- 高频出现；
- 能影响实际决策；
- 与同类有区分；
- 不是纯包装词。

没有明确 Iconic Mechanic 时不强行制造。

## Core Dialectic

识别设计反复表达的核心取舍，例如：

- 风险 vs 收益；
- 即时收益 vs 长期收益；
- 稳定 vs 高波动；
- 集中投入 vs 泛化；
- 信息 vs 行动。

可以在多层系统中重复，但不强求所有系统表达同一矛盾。

## MDA

设计从目标体验反推：

`Aesthetics -> Dynamics -> Mechanics`

分析实现效果时正向追踪：

`Mechanics -> Dynamics -> Aesthetics`

不要把“加一个功能”当体验目标。

## Loop Stack

检查：

- Moment-to-Moment
- Encounter
- Session
- Progression
- Meta

并确认内层输出是否成为外层输入。没有反馈到更大循环的环节可能是 Dead End。

## Flow

挑战应大致跟随玩家技能、信息、资源和系统理解增长。允许 Boss 峰值、恢复段和锯齿曲线，不要求永久平滑。

## Depth vs Complexity

- Complexity：需要学习多少规则。
- Depth：规则产生多少有意义决策。

新增规则前问：它增加决策空间，还是只增加记忆成本？

## 常用 Pattern

### Costed Power
强力收益应存在资源、风险、槽位、条件或机会成本。

### Loadout Budget
用槽位、点数、卡组容量、Cost、Hand Size 等限制同时拥有的能力，形成 Build Identity。

### Honest Telegraph
结果发生前提供可信信息。作用范围、时间窗口和实际结果不应欺骗玩家。

### Horizontal / Vertical / Hybrid Progression
不预设哪一种更优；根据难度、留存、内容消耗与玩家掌控感选择。

### Subtract
当复杂度不能增加有效决策时，优先删、合并或复用。

## Pattern 使用原则

Pattern 是参考，不是定律。使用时说明：

- 解决什么问题；
- 适用前提；
- 代价；
- 失败条件；
- 当前项目证据。

方法论只能帮助形成假设和减少方案空间，不能证明“好玩/平衡/可用”。


---

# Source Module: gds-design-review

# Canonical Detailed Guidance

> Preserved from the canonical Game Design Suite specialist. The runtime wrapper is intentionally compact; this file retains the detailed domain rules, workflows, guards, anti-patterns, and done criteria.

# 游戏设计评审

评审是决策辅助，不是万能清单，也不能替代 Playtest。

## Result-Level Professional Context

每一个独立 Review Finding 前，按 `../game-design/references/professional-context-header.md` 输出一次结果级 Header。`design-review` 只有在当前结果本身是“评审/取舍/优先级判断”时主责；如果 Finding 的核心是在确认配置事实、代码语义、数值强度、经济根因等，应由对应专业主责，`design-review` 作为协同。相邻 Finding 即使专业组合相同也重复显示。

## 1. 定义评审对象与决策

先明确：

- Review Object
- Decision at Stake

若没有明确决策，找最重要的未解决假设。

## 2. Evidence Baseline

整理：

- `confirmed`
- `assumed`
- `unknown`

必要时使用专业 Skill 获取配置、代码、数值等证据。

历史方案、用户建议和 AI 先前结论都不是自动成立的事实，必须接受同样的证据审查。

## 3. Review Modes

### Focused
一个技能、一段规则、一个小系统。

### Comprehensive
完整 GDD、复杂系统、多表/多模块，需要跨域矛盾检查。

### Exploratory
方向未确定：提出 2~3 个候选方向和能区分它们的小实验。

### Comparative
比较 A/B/多方案，必须使用相同证据和标准。

## 4. Root Cause Pass

每个重大问题先区分：

1. **Symptom**：玩家/数据/配置表面发生了什么；
2. **Mechanism**：什么规则导致它；
3. **Root Cause**：问题真正来自局部参数、系统结构、内容生命周期、信息/UX、上下游依赖还是制作约束；
4. **Patch Risk**：当前建议是不是只在症状上打补丁。

如果建议只是“新增 Sink、增加奖励、再加一个功能、强制绑定另一个系统、直接加倍率”，默认进入反模式检查。

## 5. Finding 质量

每个重要 Finding 包含：

- Observation
- Mechanism
- Evidence Status
- Root Cause
- Impact
- Recommendation
- Tradeoff
- Validation

推荐最小改动，不默认新增功能。

## 6. 常见风险与反模式

按相关性选择，不机械全查：

### 选择与玩法
- Dominant Strategy
- False Choice
- No Opportunity Cost
- Hollow Loop
- Complexity Over Depth
- Unclear Telegraph
- Recovery Failure

### 英雄与技能
- Button Zoo
- Passive Soup
- Multiplier-only Design
- Role by Label
- Resource Orphan
- Trigger Lottery / Trigger Starvation
- Pair Lock / Team Tax
- Stat Split Tax
- Overloaded Skill
- Dead Slot / Dead Rank
- Window Spill
- Identity Locked Late
- Problem-Sell-Solution
- Direct Replacement / Roster Power Creep

### 战斗与 Encounter
- All-phase Carry
- Gauge as Extra HP
- Shared Resource Blindness
- Reaction Monopoly
- Permanent Burst
- System Invalidation
- Boss Immunity Soup
- DPS Dummy Level
- Window Theft

### 数值与成长
- Power Creep / Treadmill
- Math-washing
- Average-only Balance
- Progression Hostage
- Tax Ladder
- Switching Punishment

### 经济
- Sink for Sink's Sake
- Mandatory Tax
- Resource Everywhere
- Currency Soup
- Production Inflation Patch
- Late-game Dead Currency
- Reward Bribery

### 系统结构
- Forced Coupling
- Patch Stacking
- Feature-as-Fix
- Hidden Dependency
- Cross-System Conflict
- Content/Production Overreach

### 实现与证据
- Config Exists != Runtime Works
- Code Reads != Path Triggers
- Spreadsheet != Playtest
- Historical Conclusion != Verified Fact

发现这些模式时，优先解释“为什么它会发生”，而不是直接给一个更复杂的新系统。

## 7. Hero/Kit Review

评审英雄或技能时，不只看技能文本和倍率。至少检查：

- Core Loop 是否一句话能说清；
- State Machine 是否明确；
- Resource Graph 是否闭环；
- Generator / Setup / Payoff / Recovery 是否都有意义；
- Phase Ownership；
- Field/Action Time；
- Team Hook 与 Pair Lock 风险；
- Trigger Reliability；
- Failure Case；
- Skill Tree 是否有里程碑，而不是全加数；
- 高阶节点是否只是修基础缺陷；
- 升级的 Paper Value 是否能在真实窗口兑现；
- Encounter 是否允许核心机制发生。

如果角色只能在木桩环境成立，或必须依赖唯一队友/特定 Boss 行为，不能只用高倍率解释为“定位特色”。

## 8. Sink / Cost Legitimacy Review

任何新增资源消耗或成长成本都检查：

- Resource Role 是否匹配；
- Fantasy/System Fit 是否成立；
- 是否产生真实决策；
- 是否只是为了消库存；
- 是否是 Source 过高或生命周期断层；
- 是否把一个系统的人为问题转嫁给另一个系统；
- 是否存在更自然的能力/效率/解锁联动。

不能因为“经济闭环”看起来更完整，就通过不合理 Sink。

## 9. Tradeoff

重要修改说明：

- 改善什么；
- 牺牲什么；
- 影响谁；
- 影响哪些系统；
- 制作成本；
- 新风险。

## 10. Severity

需要排优先级时使用：

- `critical`
- `major`
- `minor`

严重度必须由最终评审统一判断，不能原样继承其他 Skill 的标签。

## 11. 正式报告格式

```markdown
# Design Review: [对象]

## Decision at stake
...

## Evidence baseline
- Confirmed:
- Assumed:
- Unknown:

## Priority findings
### [Severity] [Finding]
- Observation:
- Mechanism:
- Root cause:
- Evidence status:
- Impact:
- Recommendation:
- Tradeoff:
- Validation:

## Next experiment
...
```

## 12. 下一步实验

尽量提出最快减少不确定性的测试，例如：

- Spreadsheet Simulation
- Combat Simulation
- Rotation Test
- Trigger Reliability Test
- Encounter Matrix Test
- Greybox
- Prototype
- Playtest
- Telemetry Check
- A/B
- Config Verification
- Code Path Verification

测试只能支持它能证明的结论。


---

# Source Module: gds-game-design-doc

# Canonical Detailed Guidance

> Preserved from the canonical Game Design Suite specialist. The runtime wrapper is intentionally compact; this file retains the detailed domain rules, workflows, guards, anti-patterns, and done criteria.

# 游戏设计文档

本 Skill 负责整理、组织、关联、表达和维护；专业设计由对应 Skill 完成。

## Result-Level Professional Context

当文档任务中输出一个新的专业设计结论、系统决策、风险 Finding 或正式规则前，按 `../game-design/references/professional-context-header.md` 输出一次结果级 Header。`game-design-doc` 只有在“文档组织/规格化表达本身”是当前 Decision Object 时才主责；具体经济、技能、数值、关卡等内容必须由对应专业主责，本 Skill 作为协同。相邻结果专业相同也重复显示。

## 文档类型

根据用户目标选择：

- Concept GDD
- Production GDD
- System Spec
- Pitch Design Document

不要把一个小系统需求扩成巨型 GDD。

## 证据状态

文档内容区分：

- `confirmed`
- `candidate`
- `TBD`
- `unknown`

不得为了“完整”把候选值写成事实。

## 禁止 Fog Words

“快、爽、丰富、深度高、强反馈”等词如果能量化，应给指标；若还未验证，标 `candidate`，不要制造虚假精度。

## 推荐章节

根据项目成熟度选择：

1. Elevator Pitch
2. Player Promise / Audience
3. Design Pillars（通常 3~5，不强制）
4. Core Loop Stack
5. System Inventory
6. System Interaction Matrix
7. Feature Backlog
8. Acceptance Criteria
9. Progression
10. Economy
11. Monetization（若存在）
12. Content Budget
13. Risk Register
14. Open Questions
15. Change Log

## System Interaction Matrix

重点发现：

- 循环依赖；
- 隐性依赖；
- 单点故障；
- 系统冲突；
- 上下游遗漏。

关系类型可用 `critical/direct/indirect/none`，不强制固定枚举。

## Feature Backlog

可使用：

| Feature | Priority | Status | Value | Cost | Depends On | Acceptance Criteria | Owner |
|---|---|---|---|---|---|---|---|

真实依赖优先于表格排序，不用“必须引用上一行”这种格式规则掩盖循环依赖。

## Acceptance Criteria

数量根据复杂度决定，不机械要求至少 3 条。避免“体验良好/运行正常”这种不可验证描述。

## Content Budget

未知数量写 `TBD`，不为了填表虚构英雄、敌人、关卡、任务数量。

## Risk Register

根据项目覆盖 Design、Balance、Technical、Production、Content、Business、Market、UX、Performance 等相关风险。

## 与专业 Skill 协作

必要时使用：

- game-production
- level-design
- skill-design
- combat-design
- balance-design
- economy-design
- progression-design
- game-interface-design
- design-review
- config-audit
- code-verification

## Quality Gate

交付前检查：

- 未定义术语；
- Fog Words；
- Candidate 被写成事实；
- 系统依赖遗漏；
- 隐性循环；
- 无用途资源；
- Feature 无玩家价值；
- AC 不可验证；
- 内容数量无来源；
- 重大 Open Question 被偷偷补全；
- 冲突规则；
- 过期旧方案。
