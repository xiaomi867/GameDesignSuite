# Game Design Suite Chat Edition — Hero & Skill

> Purpose: project knowledge for ordinary Chat mode. This file is NOT a Skill and does not depend on Skill/Plugin runtime.
> The assistant should use the relevant sections as professional guidance, while distinguishing verified evidence from candidate design.

## Usage

- Use this file when the current decision object belongs to **Hero & Skill**.
- For cross-system work, also consult the smallest necessary supporting knowledge files.
- Do not claim that a Skill was invoked. Say which professional domain or project knowledge was used when useful.
- User-fixed mechanics are constraints, not redesign targets, unless the user explicitly reopens them.


---

# Source Module: gds-hero-concept-design

# Canonical Detailed Guidance

> Preserved from the canonical Game Design Suite specialist. The runtime wrapper is intentionally compact; this file retains the detailed domain rules, workflows, guards, anti-patterns, and done criteria.

# Hero Concept Design / 英雄设定设计

目标不是写一段“好看的角色背景”，而是建立一份能约束玩法、技能、成长、配装和队伍关系的 **Hero Contract**。

优先读取：

- [Cross-Game Hero Concept Patterns](cross-game-hero-concept-patterns.md)
- [Hero Concept Spec Template](../templates/hero-concept-spec.md)

## 强制用户可见输出协议（MUST）

每一个独立角色设定、身份定位、角色差异化、设定-玩法一致性或角色池定位结论前，都先显示：

```text
【本次专业视角】
主责：角色设定策划（hero-concept-design）
协同：仅列当前结果真实使用的专业
```

常见协同：

- `hero-kit-design`：把设定承诺翻译成技能循环和状态机；
- `hero-stat-progression`：检查体质/职业定位是否被基础属性与成长支持；
- `skill-value-design`：检查数值表达是否强化设定，而不是反向破坏；
- `skill-design`：已有项目综合技能改造；
- `game-production`：角色池、产品节奏、系统定位；
- `meta-balance`：角色池差异、生态占位与同质化；
- `design-review`：发现设定与实际体验矛盾。

Direct Specialist Entry 仍执行共享 First-Visible-Line / Section Gate / Pre-Send Header Lint。

---

## 1. Hero Contract

新角色或重做角色先写清：

- **Core Fantasy**：玩家“成为谁/操控什么力量”；
- **Narrative Identity**：阵营、身份、经历、性格、价值观；
- **Combat Promise**：战斗中玩家应该最明显感受到什么；
- **Primary Role**：输出、承伤、治疗、支援、控制、资源、混合等；
- **Secondary Role**：允许的副职责；
- **Signature Verb**：角色最有辨识度的动作/行为；
- **Power Source**：力量从哪里来；
- **Risk/Cost**：角色力量的代价或限制；
- **Team Relationship**：角色希望什么队友、给队伍什么；
- **Growth Fantasy**：培养后是“数值变大”还是“玩法逐渐完整”。

至少能用一句话表达：

> 这个角色因为【身份/力量来源】，通过【标志性行为】完成【战斗职责】，其强项与限制分别是【X / Y】。

如果删掉角色名字后，这句话可以套在大量其他角色身上，判定为 `Concept Identity Weak`。

---

## 2. Taxonomy 只是坐标，不是角色本身

元素、属性、武器、命途、职业、阵营、稀有度、体型、标签等用于建立角色池坐标。

必须区分：

- **System Taxonomy**：系统分组，例如元素、武器、职业；
- **Combat Role**：主C、治疗、控制、增益等；
- **Character Fantasy**：角色独有的体验承诺；
- **Narrative Identity**：世界观身份与性格；
- **Marketing Surface**：标题、称号、视觉与宣传卖点。

禁止把“火属性+大剑+主C”当成完整角色设定。

---

## 3. Setting -> Gameplay Translation

把设定拆成可验证的玩法约束：

| 设定信息 | 可转译设计问题 |
|---|---|
| 极速/敏捷 | 是否体现在行动频率、位移、追击或动画节奏 |
| 重装/守护 | 是否体现在承伤、护盾、嘲讽、站位或保护队友 |
| 医疗/治愈 | 是否存在明确治疗/净化/救急身份 |
| 黑客/干扰 | 是否体现在控制、缺陷、资源破坏、规则修改 |
| 赌徒/风险 | 是否存在风险-收益、概率、资源押注或状态博弈 |
| 指挥/领袖 | 是否有团队增益、队友驱动或编队协同 |
| 狂战/失控 | 是否存在血线、状态、代价或不可持续爆发 |

这是 Translation Candidate，不要求所有文学设定机械化，但核心卖点若完全不进入玩法，应明确原因。

---

## 4. Narrative-Combat Consistency

至少检查四层一致性：

1. **Identity Consistency**：身份与战斗职责是否冲突；
2. **Verb Consistency**：角色描述的核心行为是否在技能中反复出现；
3. **Power Consistency**：力量来源是否与技能资源/状态一致；
4. **Growth Consistency**：培养节点是否让角色“更像自己”。

常见失败：

- 设定说“高速猎手”，实战却是低频大招炮台；
- 设定说“守护者”，最高收益却要求主动卖队友；
- 设定说“精密操控”，技能全是自动触发且无决策；
- 设定说“团队领袖”，但没有任何 Team Hook；
- 设定说“危险禁术”，却没有风险、代价或状态变化。

---

## 5. Roster Differentiation / 角色池差异

新角色必须在角色池里回答：

- 与同职业角色相比，新的 Decision 是什么；
- 与同属性/武器角色相比，新的循环是什么；
- 是否只是把旧角色倍率提高；
- 是否存在 Same Job, Different Decision；
- 玩家为什么会想拥有/培养这个角色，即使不是绝对更强；
- 新角色是否侵占多个旧角色的核心身份。

角色差异优先来自：

- 不同资源；
- 不同触发；
- 不同目标结构；
- 不同风险；
- 不同战斗阶段；
- 不同队友关系；
- 不同操作/决策；
- 不同成长展开方式。

不要把 Power Creep 当差异化。

---

## 6. Role Tag Guard

角色页面、UI、运营标签或内部标签必须与实际玩法一致。

例如：

- “主力输出”应有明确主要伤害责任；
- “生存治疗”应能稳定承担生存职责；
- “牵引/控制”应存在可观察且有价值的控制行为；
- “快速协奏/资源辅助”等标签应有真实资源贡献。

标签若只是营销词而无法从 Kit/数值验证，标记 `Role Tag Mismatch`。

---

## 7. Rarity / Power Fantasy

稀有度可以影响：

- 机制完整度；
- 动画/表现复杂度；
- Build上限；
- 团队兼容性；
- 成长节点；
- 数值预算。

但禁止默认：

`更高稀有度 = 所有维度全面更强`

否则会造成低稀有度角色失去存在意义。

---

## 8. Setting Evidence Layers

已有项目审查角色设定时区分：

- `confirmed-design`：用户/正式文档已确认；
- `verified-config`：配置中的阵营、属性、职业、标签；
- `verified-code`：代码实际使用的分类/行为；
- `reference-data`：外部商业游戏公开页面；
- `supported-inference`：从多角色归纳的模式；
- `candidate`：为当前项目提出的新设定。

外部游戏角色设定只能用于参考模式，不能覆盖当前项目设定。

---

## 9. 与其他英雄 Skill 的相互验证

正式角色评审建议形成四向闭环：

```text
hero-concept-design
  ↓ 设定承诺
hero-kit-design
  ↓ 机制兑现
hero-stat-progression
  ↓ 成长与体质支持
skill-value-design
  ↓ 数值表达与等级增量
  ↘ 回看是否仍强化原始角色身份
```

至少检查：

- Concept 说“坦克”，基础成长却是玻璃炮；
- Concept 说“追击核心”，Kit 追击触发极低；
- Kit 依赖防御，Stat Growth 却几乎不给防御成长；
- Skill Value 把辅助技能倍率抬到主C水平，导致角色身份漂移。

---

## 10. Done Criteria

一次角色设定任务至少交付：

- Hero Contract；
- Taxonomy；
- Combat Promise；
- Signature Verb；
- Power Source / Cost；
- Team Relationship；
- Growth Fantasy；
- Roster Differentiation；
- 设定 -> 机制约束；
- 与 Kit / Stat / Skill Value 的一致性风险；
- Evidence Boundary。

## 11. 反模式

- **Tag Soup**：堆很多标签但没有核心身份；
- **Lore-only Hero**：故事很完整但玩法没有映射；
- **Mechanics-first Retcon**：先做技能再强行编设定解释；
- **Role Drift**：成长后角色职责与初始定位完全不同且无设计意图；
- **Power-Creep Identity**：唯一卖点是数值更高；
- **Visual/Gameplay Split**：表现与实际操作体验完全相反；
- **Universal Hero**：输出、生存、控制、辅助全部高水平且无机会成本。


---

# Source Module: gds-hero-kit-design

# Canonical Detailed Guidance

> Preserved from the canonical Game Design Suite specialist. The runtime wrapper is intentionally compact; this file retains the detailed domain rules, workflows, guards, anti-patterns, and done criteria.

# Hero Kit Design / 英雄技能设定

目标不是“给英雄填四个技能”，而是让整个 Kit 形成一个可读、可循环、可验证、与角色设定一致的战斗系统。

优先读取：

- [Cross-Game Hero Kit Patterns](cross-game-hero-kit-patterns.md)
- [Hero Kit Audit Template](../templates/hero-kit-audit.md)

## 强制用户可见输出协议（MUST）

每一个独立 Kit 结构、技能槽位职责、状态机、资源循环、触发链、Team Hook 或机制一致性结论前，都先显示：

```text
【本次专业视角】
主责：英雄技能架构（hero-kit-design）
协同：仅列当前结果真实使用的专业
```

常见协同：

- `hero-concept-design`：确认机制是否兑现角色设定；
- `skill-value-design`：为每个机制节点配置数值成长；
- `hero-stat-progression`：确认 Scaling Source 与基础成长匹配；
- `skill-design`：已有项目综合技能改造、Target/Buff配置语义；
- `combat-design`：战斗规则、行动/资源/Target底层约束；
- `balance-design`：判断完整循环的 Power Budget；
- `simulation-design`：验证Rotation、Uptime、触发频率与极端循环；
- `config-audit` / `code-verification`：确认真实实现。

Direct Specialist Entry 仍执行共享 First-Visible-Line / Section Gate / Pre-Send Header Lint。

---

## 1. 先定义 Hero Loop

新角色先写一句：

> 角色通过【Source/Setup】获得【状态/资源】，用【核心动作】完成【Payoff】，随后进入【Recovery/Reset】，并通过【Team Hook】与队伍发生关系。

至少明确：

- Entry State；
- Generator；
- Setup；
- Converter；
- Consumer；
- Payoff；
- Recovery；
- Loop Time；
- Team Hook；
- Failure Case。

如果技能可以各自独立删除而不影响循环，优先判断 Kit Cohesion 不足。

---

## 2. Slot Responsibility

技能槽位要有职责，不要求每个槽位同等强度。

常见职责：

- Basic / Normal：资源底座、低成本动作、补循环；
- Skill / Active：核心转换、主循环驱动；
- Ultimate / Liberation / Burst：高价值窗口、循环收束或状态转换；
- Talent / Passive / Forte：角色规则核心；
- Technique / Intro / Outro：战斗入口、换人、队伍衔接；
- Ascension Passive / Major Node：补充规则、修复体验或扩展Build；
- Eidolon/Constellation/Sequence：扩展、变体、上限或便利性。

禁止为了“槽位都有东西”而重复同一功能。

---

## 3. State Machine

复杂英雄必须显式状态化：

`Neutral -> Setup -> Primed -> Empowered -> Payoff -> Recovery`

每个状态明确：

- Enter Trigger；
- Exit Trigger；
- Duration / Turn / Action Semantics；
- 可否刷新；
- 可否叠加；
- 技能替换；
- 资源变化；
- Target变化；
- Buff/Debuff变化；
- 死亡、换人、控制、波次切换时的处理。

如果强化状态没有明确退出/恢复，警惕永久Burst。

---

## 4. Resource Graph

角色资源必须画成：

`Source -> Storage -> Threshold -> Spend/Convert -> Payoff -> Reset`

资源包括：

- 能量/怒气；
- 技能点/共享资源；
- 弹药；
- 层数；
- 标记；
- 特殊Gauge；
- 生命/护盾；
- 敌方状态；
- 队友行动；
- 受击次数；
- 击破/异常；
- 换人/协奏资源。

必须检查：

- Source是否足够；
- Storage是否会大量溢出；
- Threshold是否有意义；
- Spend是否有决策；
- 是否存在Source无Sink；
- 是否出现无限正反馈循环；
- 队友是否可以不合理地倍增资源生成。

---

## 5. Trigger Topology

不要只读技能描述，画 Trigger Graph：

`Action A -> State B -> Trigger C -> Attack D -> Gain Resource -> Trigger E`

标记：

- 主动触发；
- 自动触发；
- 每行动/每秒/每回合限制；
- ICD / Interval；
- 触发次数上限；
- 是否能被自身触发链递归；
- 是否能触发队友；
- 是否会重复计数；
- Trigger Reliability。

所有“额外行动/追击/反击/协同攻击/连携”必须检查自触发和循环闭合风险。

---

## 6. Target Architecture

每个动作明确：

- Single / Blast / AoE / Bounce / Random / Front / Back / Lowest/Highest HP；
- Ally / Self / Enemy / Team；
- Target Lock Timing；
- 目标死亡后的重定向；
- 多段攻击目标是否可变化；
- 随机目标是否均匀；
- Boss/单体环境是否改变技能价值。

Target不是纯描述字段，它直接影响Power Budget与体验。

---

## 7. Action / Field-Time Budget

根据游戏类型记录：

- Action Count；
- Field Time；
- Animation Time；
- Swap Time；
- Setup Time；
- Burst Window；
- Recovery Window；
- 共享资源占用；
- 输入复杂度。

纸面倍率必须通过真实行动次数与窗口兑现。

---

## 8. Team Hook

角色至少明确：

- 需要队友提供什么；
- 自己给队友什么；
- 是否依赖特定职业/元素/状态；
- 是否有通用Hook和专属Hook；
- 是否形成Mandatory Partner；
- 是否抢占公共资源；
- 是否改变队友行动节奏。

强协同允许存在，但需要 Opportunity Cost 与替代方案。

---

## 9. Mechanic Density / 机制密度

复杂不等于深度。

统计：

- 独立资源数；
- 独立状态数；
- 条件分支数；
- 需要记忆的阈值；
- 技能替换层数；
- 触发链长度；
- 例外规则数。

如果玩家为了使用一个角色必须同时维护过多互不关联规则，标 `Mechanic Soup`。

优先让多个效果围绕同一资源/状态形成组合，而不是每个技能发明一个新名词。

---

## 10. Upgrade Topology

技能等级、被动、星级/命座/共鸣链的升级先分类型：

- Numerical Upgrade；
- Reliability Upgrade；
- Rotation Upgrade；
- QoL Upgrade；
- Rule Expansion；
- New Team Hook；
- Capstone；
- Mechanic Replacement。

不能让所有成长节点都只是“+X%伤害”。

具体数值交给 `skill-value-design`；长期解锁节奏交给 `progression-design`。

---

## 11. Cross-Validation Matrix

### 与 hero-concept-design
- Core Fantasy 是否有高频动作表达；
- Signature Verb 是否出现在主循环；
- 风险/代价是否真实存在。

### 与 hero-stat-progression
- Scaling Source 与高成长属性是否匹配；
- Tank/Healer是否被迫堆完全无关属性；
- 速度/能量等固定属性是否支持循环。

### 与 skill-value-design
- 核心技能的数值成长是否匹配使用频率；
- Utility参数是否被过度随等级放大；
- 低频终结技是否获得合理Payoff。

### 与 balance-design
- 完整Rotation而非单技能是否在角色预算内；
- Team Hook是否形成隐性Power。

---

## 12. External Reference Boundary

崩铁、原神、鸣潮可用于观察不同 Skill Grammar：

- 回合制：Basic / Skill / Ultimate / Talent / Technique / Trace；
- 实时换人制：Normal / Skill / Burst / Passive / Constellation；
- 动作换人制：Normal / Resonance Skill / Forte / Liberation / Intro/Outro/Sequence等。

这只能证明“存在这些架构选择”，不能规定当前项目必须照搬槽位数量或升级结构。

---

## 13. Done Criteria

一次 Hero Kit 任务至少交付：

- Hero Loop；
- Slot Responsibility；
- State Machine；
- Resource Graph；
- Trigger Graph；
- Target Architecture；
- Action/Field-Time Budget；
- Team Hook；
- Failure/Recovery；
- Upgrade Topology；
- 与 Concept / Stat / Skill Value 的交叉验证；
- 需模拟/代码验证的风险。

## 14. 反模式

- **Button Collection**：技能只是几个独立按钮；
- **Mechanic Soup**：资源/状态很多但互不形成决策；
- **Infinite Trigger Loop**：触发链可自循环；
- **Permanent Burst**：强化状态无可靠结束；
- **Mandatory Partner**：角色只能绑定唯一队友；
- **Slot Redundancy**：多个技能做同一件事；
- **Passive Does Everything**：核心玩法几乎全自动，玩家决策被掏空；
- **Kit/Concept Split**：角色设定与实战循环没有对应关系。


---

# Source Module: gds-hero-stat-progression

# Canonical Detailed Guidance

> Preserved from the canonical Game Design Suite specialist. The runtime wrapper is intentionally compact; this file retains the detailed domain rules, workflows, guards, anti-patterns, and done criteria.

# Hero Stat Progression / 英雄等级属性成长

目标不是把 Lv1 和 LvMax 两个数字插值，而是建立**可解释、可复现、能与技能/内容/成长成本联动**的角色属性曲线。

优先读取：

- [Cross-Game Character Stat Growth Patterns](cross-game-character-stat-growth-patterns.md)
- [Hero Stat Curve Audit Template](../templates/hero-stat-curve-audit.md)

## 强制用户可见输出协议（MUST）

每一个独立等级曲线、突破跳变、基础属性模板、成长副属性、阶段Power Delta或成长异常结论前，都先显示：

```text
【本次专业视角】
主责：英雄成长数值（hero-stat-progression）
协同：仅列当前结果真实使用的专业
```

常见协同：

- `hero-concept-design`：确认体质与角色身份一致；
- `hero-kit-design`：确认技能Scaling Source与资源循环；
- `skill-value-design`：检查角色等级成长与技能等级成长是否重复放大；
- `progression-design`：等级上限、突破节点、成本与解锁；
- `balance-design`：阶段强度、横向Power Budget与敌我Benchmark；
- `formula-verification`：属性进入伤害/防御/治疗公式的真实方式；
- `simulation-design`：全等级参数扫描、Breakpoint与极端成长；
- `config-audit` / `code-verification`：真实表与Runtime读取。

Direct Specialist Entry 仍执行共享 First-Visible-Line / Section Gate / Pre-Send Header Lint。

---

## 1. Stat Taxonomy / 先分属性类型

任何成长表先把属性分类：

### Level-Scaled Base Stats
常见：HP、ATK、DEF。

### Fixed/Mostly-Fixed Combat Stats
常见：基础速度、能量上限、基础暴击率、基础暴伤、嘲讽/仇恨权重等。

### Ascension / Breakthrough Bonus Stat
例如暴击、伤害加成、元素/属性伤害、治疗、效果命中、特殊效率等。

### Node-Based Stats
通过行迹/天赋树/技能树节点获得，而不是角色等级自动增长。

### Derived Stats
由公式计算，例如战力、EHP、DPS、实际行动频率。

禁止把所有属性都塞进同一等级插值公式。

---

## 2. Growth Contract

建立曲线前明确：

- Level Cap；
- Breakthrough / Ascension Levels；
- Lv1 Base；
- LvMax Base；
- 每次突破是否直接加属性；
- 突破后是否重置/改变成长斜率；
- Bonus Stat在哪些阶段增加；
- 稀有度/职业是否共享模板；
- 哪些属性固定；
- 目标内容曲线；
- 玩家每个阶段应感知的Power Delta。

必须检查：

`Power Curve <-> Content Curve <-> Cost Curve <-> Time Curve`

---

## 3. Curve Families

允许的曲线族包括：

### Linear
`V(L)=V1 + k*(L-1)`

适合可读、稳定、易预测的成长。

### Piecewise Linear
不同突破区间使用不同斜率。

### Multiplier Table
`V(L)=BaseTemplate * LevelMultiplier(L) + AscensionDelta(Phase)`

适合多个角色共享统一成长形状但拥有不同基础模板。

### Exponential / Power Curve
仅在设计目的明确且有长期数值空间时使用。必须检查后期膨胀。

### Hybrid
基础属性采用Multiplier，突破使用离散Delta，特殊属性通过节点增加。

不能因为某成熟游戏使用某种曲线，就直接复制其Multiplier表。

---

## 4. Normalized Growth

跨角色/跨游戏比较时不要直接比绝对数。

常用：

`Normalized(L) = V(L) / V(Lmax)`

`GrowthFromBase(L) = V(L) / V(1)`

`MarginalGrowth(L) = V(L) - V(L-1)`

`PhaseDelta = V(after ascension) - V(before ascension)`

`PhaseShare = PhaseDelta / V(Lmax)`

这样可以区分：

- 同样LvMax，谁前期更强；
- 哪个系统把Power放在突破；
- 哪些阶段增长过密或过空；
- 是否存在“十级几乎没感觉，突破瞬间暴涨”。

---

## 5. Roster Stat Envelope

建立角色池的属性包络：

- Min / P25 / Median / P75 / Max；
- 同角色职责内分布；
- 同稀有度内分布；
- 同Scaling Source内分布；
- 不同等级阶段的分布。

例如：

- Tank不一定必须全属性最高，但应在其生存核心指标有可解释优势；
- 高速角色的低ATK是否被行动次数补偿；
- HP/DEF双成长是否形成异常EHP；
- Healer的基础体质是否支持其站场/受击预期。

避免“每个新角色都比旧角色基础属性略高一点”的隐性Power Creep。

---

## 6. Scaling-Source Alignment

角色成长必须和 Kit 的Scaling Source交叉验证。

检查：

- 主要伤害吃ATK，ATK成长是否合理；
- Tank以DEF输出，DEF成长是否同时过度提高生存与输出；
- HP治疗+HP生存是否形成Double Scaling；
- 高速角色是否因速度固定而无法体现设定；
- 能量上限与技能循环是否匹配；
- 暴击/命中等Bonus Stat是否恰好补角色需求，还是强行制造专属答案。

如果一个属性同时提高多个主要输出维度，必须交 `balance-design` 做Effective Power检查。

---

## 7. Ascension / Breakthrough Design

突破节点可以承担：

- 等级上限提升；
- Base Stat jump；
- Bonus Stat；
- Major Passive；
- Skill Level Cap；
- 新机制解锁。

检查：

- 是否有可感知收益；
- 是否一次性给太多Power；
- 是否强迫玩家突破才能让角色“能用”；
- 是否和内容门槛形成硬锁；
- 是否出现等级成长+突破+技能解锁同一节点多重爆发。

建议记录每个节点：

`TotalPowerDelta = BaseStatDelta + BonusStatDelta + UnlockValue + SkillCapValue`

这是分析框架，不要求把不同价值机械相加。

---

## 8. Growth Density / 成长密度

把Lv1~LvMax划分阶段，计算：

- 每10级或每阶段属性增长；
- 突破跳变；
- 技能等级上限变化；
- 被动解锁；
- 装备/系统同步开放。

目标不是每一级收益相同，而是避免：

- Dead Levels；
- Power Cliffs；
- 多系统同点爆炸；
- 前期成长过快导致内容失效；
- 后期成长过慢导致升级无感。

---

## 9. Cross-Validation With Skill Levels

角色等级和技能等级往往同时成长，因此必须检查乘法叠加。

概念式：

`Output(L,S) = BaseStat(L) × SkillMultiplier(S) × OtherMultipliers`

若BaseStat从Lv1到满级提升3倍，Skill倍率又提升2倍，则基础输出可出现约6倍放大，还未计算装备/暴击/增伤。

所以不能分别看：

- “属性曲线很平滑”；
- “技能倍率曲线也很平滑”；

然后默认组合后仍然平滑。

必须做二维检查：

`Character Level × Skill Level`。

---

## 10. Fixed Stat Guard

速度、能量、暴击等属性是否随等级成长必须是明确设计决定。

固定属性的好处：

- 循环稳定；
- Build阈值可控；
- 角色身份清晰。

成长属性的风险：

- Breakpoint随等级漂移；
- 低级体验与高级体验不是同一角色；
- 配装目标不断移动。

不要因为HP/ATK/DEF成长，就默认所有属性都应该成长。

---

## 11. External Benchmark Boundary

公开商业游戏角色页可用于研究：

- 等级上限与突破节点；
- 哪些基础属性随等级变化；
- 哪些属性固定；
- 成长副属性如何在突破中投放；
- 技能等级上限如何被突破约束。

但必须记录 Source Date / Version。外部网站可能滞后于当前版本；例如某站点仍显示旧等级上限时，不得把它写成当前项目的“行业标准”。

---

## 12. Statistical / Formula Checks

至少根据任务检查：

- Monotonicity；
- Integer/decimal rounding；
- Level boundary continuity；
- Ascension pre/post values；
- Min/Max outliers；
- Rank-order stability；
- Growth ratio；
- Marginal gain；
- Power Elasticity；
- Breakpoint crossings。

表格计算只能证明数学结果，不能证明体验良好。

---

## 13. Done Criteria

一次英雄等级数值任务至少交付：

- 属性分类；
- Lv1 / 关键突破 / LvMax快照；
- 成长公式或Multiplier表；
- 突破Delta；
- Bonus Stat投放；
- Roster Envelope；
- Scaling Source Alignment；
- Character Level × Skill Level联合检查；
- 异常/Breakpoint；
- Evidence Boundary；
- 需要Simulation/Runtime/Playtest的下一步。

## 14. 反模式

- **Two-Point Interpolation**：只给Lv1/LvMax，中间无验证；
- **All-Stats Growth**：所有属性一起线性涨；
- **Ascension Power Cliff**：突破节点强度断层；
- **Dead Levels**：长区间升级几乎无感；
- **Double-Scaling Blindness**：属性和技能分别合理，组合后爆炸；
- **Role/Stat Mismatch**：角色职责与基础成长方向相反；
- **Cross-Game Copy**：直接复制外部游戏等级Multiplier；
- **Version Blindness**：引用旧Wiki等级上限却当当前事实。


---

# Source Module: gds-skill-design

# Canonical Detailed Guidance

> Preserved from the canonical Game Design Suite specialist. The runtime wrapper is intentionally compact; this file retains the detailed domain rules, workflows, guards, anti-patterns, and done criteria.

# 技能策划

目标不是“把技能栏填满”，而是让角色拥有清晰的玩法身份、资源循环、触发逻辑、团队职责和可成长空间。

复杂角色、新英雄、角色重做、技能树、升星/命座/影画、队伍协同时按需读取：

- 角色循环、状态机、资源图、Team Hook、Field-Time、Trigger Reliability -> [Hero Kit Architecture](hero-kit-architecture.md)
- 技能等级、技能树、被动节点、升星/里程碑升级 -> [Skill Progression & Upgrade Topology](skill-progression-and-upgrade-topology.md)
- 角色池定位、横向差异、团队槽位和角色生态 -> [Hero Roster Architecture](../game-production/references/hero-roster-architecture.md)

## Result-Level Professional Context

每一个独立英雄/技能机制、Target、触发、状态机、Buff、升级或构筑结论前，按 `../game-design/references/professional-context-header.md` 输出一次结果级 Header。

技能机制本身由 `skill-design` 主责；具体倍率/强度转由 `balance-design` 主责；真实表字段不一致转由 `config-audit` 主责；代码语义转由 `code-verification` 主责；团队底层战斗规则可由 `combat-design` 主责。相邻结果即使专业组合相同，也重复显示 Header。

## 0. 机制保护

先区分：

### Fixed Rules
- 技能类型；
- Target 逻辑；
- 触发条件；
- 状态关系；
- 技能行为；
- 玩家明确要求保留的机制。

### Tunables
- 倍率；
- CD；
- 持续；
- 概率；
- 阈值；
- Buff 数值；
- 消耗；
- 初始资源。

用户说“不改机制”时，不通过改 Target、触发、状态或技能结构绕过约束。

发现配置/实现错误时区分：

- **Fix Bug**：让实际行为回到已确认设计；
- **Change Mechanic**：改变原设计规则。

不要把修错和改机制混为一谈。

## 1. 先写角色循环，再写技能

新角色/重做角色先用一句话描述：

> 角色通过【生成条件/资源】进入【关键状态】，在【收益窗口】中用【核心动作】兑现收益，再通过【恢复/重置】重新进入循环。

再确认：

- Core Fantasy；
- Primary Role；
- Phase Ownership；
- Generator；
- Setup；
- Consumer/Payoff；
- Recovery；
- Team Hook；
- Failure Case。

如果角色只能描述成“普攻伤害、技能伤害、大招伤害、被动加伤”，优先判定为 Kit Identity 不足，而不是继续加倍率。

## 2. Skill Grammar / 技能语法

每个技能尽量拆成：

`Input/Trigger -> Acquire Target -> Cost -> Cast -> Resolve -> Damage/Heal -> Buff/Debuff -> Secondary Trigger -> Resource/CD Update`

这样可以明确：

- Target 何时确定；
- Cost 何时扣；
- Damage 与 Buff 的先后；
- Secondary Effect 是否会重复触发；
- 死亡/击杀/破盾等事件在何时判定；
- Buff 读取施法前还是施法后属性。

每个技能还建议标记职能：

- Generator；
- Setup；
- Converter；
- Consumer；
- Payoff；
- Amplifier；
- Safety；
- Mobility/Position；
- Finisher。

技能槽位多不代表每个槽位都必须承担同等数值价值或使用频率。

## 3. State Machine / 状态机

复杂角色必须显式写状态，而不是把状态藏在描述里。

例如：

`Normal -> Setup -> Empowered -> Payoff -> Recovery`

每个状态明确：

- 进入条件；
- 退出条件；
- Duration；
- 可否刷新/覆盖；
- 技能是否替换；
- 资源规则是否变化；
- Target/Trigger 是否变化；
- 被控制/死亡/换人时如何处理。

强化状态如果没有清晰结束与 Recovery，会很容易退化成“永久 Burst”。

## 4. Resource Graph / 资源图

角色资源至少画成：

`Source -> Storage -> Converter -> Sink -> Reset`

资源可以是：

- 能量/怒气；
- 层数；
- 弹药；
- 标记；
- 生命/护盾；
- 敌方状态；
- 队友行动；
- 受击次数；
- Break/异常状态。

必须检查：

- 生成速度；
- 上限；
- 溢出；
- 消费时机；
- 是否有垃圾资源；
- 是否有 Source 无 Sink 或 Sink 无 Source；
- 玩家是否真的能决定何时消费。

## 5. 技能检查清单

每个技能根据任务检查：

- Skill Definition
- Target / Target Selector
- Trigger
- Scaling Source：ATK / DEF / HP / Fixed / Mixed
- Multiplier
- Damage Type
- Crit
- Resource Cost/Gain
- Buff / Debuff
- Duration
- Stack / Refresh / Exclusive
- Group / Mutual Exclusion
- Cooldown / Interval
- Condition
- Priority
- Level Mapping
- Star Mapping
- Interaction with Passive/Ultimate
- Action Advance / Extra Action / Follow-up / Counter
- Energy / Rage Cycle
- Hit / Resist Reliability
- Secondary Gauge Contribution
- State Transition
- Field/Action Time
- Team Hook
- Payoff Window
- Edge Cases

## 6. Scaling Source / 倍率基准属性

必须明确每段效果到底引用：

- 自身攻击；
- 自身防御；
- 自身生命；
- 目标生命；
- 已损生命；
- 固定值；
- 混合属性。

不要只看到 `DamageCfg` 就假设倍率对象。已有项目需要结合 `config-audit + code-verification` 确认枚举、解析与运行时对象。

### 设计检查

- Scaling Source 是否符合角色职责；
- 是否形成有意义的配装方向；
- 是否让 Tank/Healer 为了输出被迫堆不相关属性；
- Mixed Scaling 是否只是增加复杂度而没有决策价值；
- 同一属性同时无限提高输出、生存、资源时是否形成 Double/Triple Scaling；
- 目标生命倍率是否对 Boss 有上限或特殊规则。

## 7. Skill Rotation / 技能循环

技能不能只单独看倍率，应放进完整 Rotation：

- 普攻频率；
- 技能频率；
- 大招周期；
- 被动触发频率；
- 追击/反击次数；
- Buff 覆盖；
- 资源净流；
- 强化状态时长；
- Setup / Payoff 占用；
- 是否因为速度/额外行动改变循环。

### 角色资源标签

可以根据团队共享资源把角色标记为：

- Resource Positive；
- Resource Neutral；
- Resource Negative；
- Burst Consumer；
- Emergency Consumer。

这会直接影响队伍搭配与角色真实价值。

## 8. Field-Time / Action-Time Budget

团队角色不能只看个人技能表。

检查：

- On-field Time；
- Setup Time；
- Payoff Time；
- Swap/Action Cost；
- 公共资源占用；
- 是否抢队友 Burst Window；
- 动画/连段是否把纸面收益拖出真实窗口。

“多一段攻击”不自动等于整段倍率都能兑现。

## 9. Buff/Debuff Duration Semantics

“持续 2 回合”必须明确是谁的回合：

- 施法者行动；
- 目标行动；
- 全局 Round；
- 固定时间；
- 触发次数。

当游戏存在：

- 加速；
- 行动提前；
- 额外行动；
- 插队；

时，不同 Duration Semantics 会产生完全不同的实际覆盖率。

## 10. Trigger Reliability / 触发可靠性

反击、受击回能、队友行动触发、击杀触发、Break 触发等不能只看“能触发”。

必须检查：

- 事件频率；
- 是否依赖敌方 AI；
- 是否依赖指定队友动作；
- 每回合/CD 限制；
- 单体/群体差异；
- 目标死亡是否吞触发；
- Boss 无敌/长演出是否饿死循环；
- 是否有手动/保底替代触发。

高收益可以对应低可靠性，但这必须是有意识的 Risk/Reward，而不是事故。

## 11. 状态可靠性

Debuff/控制类技能不能只看 Base Chance。

应协作 `balance-design` 检查：

- 普通怪实际命中率；
- Elite；
- Boss；
- Specific Resist；
- Immunity；
- 多段判定；
- 是否存在 100% 文本但实际不稳定的情况。

## 12. Team Hook / 队伍关系

角色与队伍的关系优先通过：

- 创建状态；
- 消费队友状态；
- 放大某类行为；
- 提供行动/资源；
- 保护窗口；
- 改变敌方状态；
- 触发追加/协同行动。

属性/阵营/职业条件可以作为 Soft Synergy，但不要默认做成 Hard Pair Lock。

如果角色没有唯一队友就无法完成基础循环，标记 `Pair Lock / Team Tax` 风险。

## 13. 技能等级、技能树与升星

升星/升级必须回答：

- 影响哪个技能；
- 改哪个维度；
- 单次收益；
- 累积收益；
- 是否改变机制；
- 是否出现关键断层；
- 是否符合品质/稀有度定位；
- 是否跨过 Rotation / Energy / Hit / Stack Breakpoint；
- 是否改善 Reliability / Cycle / Team Hook；
- 是否只是修复基础角色的人为缺陷。

建议把成长分成：

- Skill Rank：稳定纵向数值；
- Major Passive：循环、条件、可靠性；
- Minor Stat：Build 支撑；
- Milestone：关键玩法变化；
- Capstone：突破上限或完成角色身份。

避免每次升星同时提升过多技能，除非项目规则明确如此。

### 节点价值

升级不应该只是把所有倍率同步 +X%。可以区分：

- 稳定数值成长；
- 条件改善；
- 覆盖率改善；
- 资源效率；
- Target Coverage；
- Team Synergy；
- Execution/QoL；
- Build 联动；
- 关键 Breakpoint；
- Mechanic Transformation。

但用户明确要求“不改机制”时，只能在允许的 Tunables 内实现，不通过新增行为制造假“成长”。

## 14. 构筑价值

检查技能是否：

- 支撑角色定位；
- 与队友形成互补；
- 存在主核/副核；
- 有明确适用场景；
- 不形成无条件主导策略；
- 不依赖不可控 RNG 才能成立；
- 不因另一技能的速度/资源行为导致隐藏负协同。

### 负协同检查

例如：

- 控制让反击无法触发；
- 治疗把低血 Build 永久抬出阈值；
- 加速导致 Buff 提前过期；
- 额外行动让共享资源快速转负；
- 秒杀小怪让叠层技能失去目标；
- Target 改变让被动无法稳定触发；
- 长连段溢出敌方失衡/易伤窗口。

## 15. 与数值协作

具体倍率与强度交给 `balance-design`。技能策划负责定义参数影响方向、允许范围和角色行为目标。

对于跨类型能力，应共同检查：

- Action Economy；
- Resource Economy；
- Target Value；
- Buff Uptime；
- Reliability；
- Secondary Gauge；
- Context Discount；
- Window Realization。

## 16. 与战斗/关卡协作

复杂角色必须与 `combat-design + level-design` 检查：

- 角色依赖的敌人行为是否稳定存在；
- Counter/DoT/Break/状态体系有没有内容承载；
- Burst Window 是否被 Boss 转场/无敌频繁偷走；
- 单体/群体内容是否都存在；
- 教学关是否教角色循环，而不是逐个按钮。

## 17. 与配置协作

已有配置项目应与 `config-audit` 检查：

- Skill Key/ID；
- BuffCfg；
- Target；
- GroupKey；
- Damage/Heal 字段；
- Level/Star 映射；
- 缺失行；
- 关联引用。

若需要确认运行时行为，与 `code-verification` 协作。

## 18. 输出要求

用户要求落表时不能只写“加强/削弱”。至少给：

| 表/对象 | Key/ID | 字段 | 当前值 | 改后值 | 影响 | 理由 | 验证 |
|---|---|---|---|---|---|---|---|

新英雄/复杂技能建议补：

- Core Loop；
- State Machine；
- Resource Graph；
- Scaling Source；
- Rotation；
- Field/Action Time；
- Resource Net Flow；
- Buff Uptime；
- Trigger/Hit Reliability；
- Breakpoint；
- Team Hook；
- Failure Case；
- Negative Synergy；
- Config/Code Evidence Status。

当前值未知时标 `unknown`。

## 19. 技能设计反模式

- **Multiplier-only Design**：只调倍率不看循环与资源；
- **Button Zoo**：技能很多但没有共同循环；
- **Passive Soup**：大量规则不改变决策；
- **Resource Orphan**：资源存在但没有有意义的消费；
- **Hidden Scaling**：倍率对象不明确，文本/配置/代码不一致；
- **Duration Ambiguity**：回合持续语义不清；
- **Resource Bankruptcy**：单角色很强但团队资源循环崩溃；
- **Guaranteed-on-Paper CC**：忽略敌方抗性；
- **Trigger Lottery/Starvation**：核心收益依赖不可控触发或敌人不配合；
- **Pair Lock**：必须绑唯一队友；
- **Stat Split Tax**：核心属性互不协同；
- **Window Spill**：升级/连段收益溢出真实窗口；
- **Overloaded Skill**：单技能承担太多职能；
- **Dead Slot/Dead Rank**：技能/技能等级长期没有使用价值；
- **Upgrade Soup**：一次升星同时强化多个维度，无法判断价值来源；
- **Problem-Sell-Solution**：先制造基础缺陷，再用高阶节点修复；
- **Synergy Trap**：表面联动，实际触发条件互相冲突。


---

# Source Module: gds-skill-value-design

# Canonical Detailed Guidance

> Preserved from the canonical Game Design Suite specialist. The runtime wrapper is intentionally compact; this file retains the detailed domain rules, workflows, guards, anti-patterns, and done criteria.

# Skill Value Design / 技能数值设计

目标不是“把Lv1倍率乘到Lv10”，而是让每个技能参数的成长方式与其职责、触发频率、循环位置、资源成本和角色定位一致。

优先读取：

- [Cross-Game Skill Scaling Patterns](cross-game-skill-scaling-patterns.md)
- [Skill Value Audit Template](../templates/skill-value-audit.md)

## 强制用户可见输出协议（MUST）

每一个独立技能倍率、技能等级曲线、Buff数值、概率/持续成长、资源/冷却参数或技能升级价值结论前，都先显示：

```text
【本次专业视角】
主责：技能数值策划（skill-value-design）
协同：仅列当前结果真实使用的专业
```

常见协同：

- `hero-kit-design`：确认技能职责、触发频率、循环位置；
- `hero-stat-progression`：检查角色等级属性与技能等级的联合放大；
- `hero-concept-design`：确认数值重点是否强化角色身份；
- `balance-design`：角色总体Power Budget、横向强度；
- `formula-verification`：倍率对象、乘区、Clamp、Round、Snapshot；
- `simulation-design`：Rotation、触发频率、Crit/Target随机分布；
- `config-audit` / `code-verification`：技能等级映射与真实实现。

Direct Specialist Entry 仍执行共享 First-Visible-Line / Section Gate / Pre-Send Header Lint。

---

## 1. Parameter Taxonomy / 先分参数类型

任何技能等级表先把字段分类。

### Throughput Parameters
- Damage Multiplier；
- Heal Ratio / Flat Heal；
- Shield Ratio / Flat Shield；
- Additional Damage；
- DoT / Tick Value。

### Amplification Parameters
- DMG Bonus；
- Vulnerability；
- Crit / Crit DMG；
- DEF/RES Shred；
- Speed/Action modifier；
- Healing/Shield Bonus。

### Reliability Parameters
- Base Chance；
- Hit Count；
- Target Count；
- Stack Cap；
- Trigger Interval；
- Duration；
- Threshold。

### Economy Parameters
- Energy/Rage Cost；
- Resource Gain；
- Cooldown；
- Charge Count；
- Shared-resource cost/generation。

### Structural Parameters
- Target Rule；
- Trigger Rule；
- State Change；
- Skill Replacement；
- Extra Action；
- Follow-up/Counter unlock。

结构参数通常不是简单等级数值；如果升级改变结构，应转 `hero-kit-design` 评估。

---

## 2. Skill Value Contract

每个可升级技能至少记录：

- Skill Job；
- Scaling Source；
- Base Level；
- Normal Max Level；
- Extended Max（星魂/命座/加级时）；
- Use Frequency；
- Resource Cost；
- Target Count；
- Trigger Reliability；
- Damage/Heal/Shield Type；
- Crit Eligibility；
- Level-Scaled Fields；
- Fixed Fields；
- Upgrade Cost；
- Expected Power Delta per level。

没有这些上下文，不直接评价“200%高不高”。

---

## 3. Scaling Families

技能参数可以使用不同增长族。

### Standard Percentage Curve
`V(s)=V1 * M(s)`

适合常规伤害/治疗百分比。

### Flat Curve
Flat值可使用独立Multiplier，避免与百分比值完全同步。

### Additive Step
`V(s)=V1 + Δ(s)`

适合概率、减伤、资源等需要严格边界的参数。

### Milestone Growth
只在特定技能等级增加关键参数，其他等级增长主倍率。

### Fixed Utility
CD、持续、资源回复、目标数等保持固定，只让主要Throughput成长。

### Diminishing Utility
功能参数前期增长较快、后期趋缓，防止控制/减伤/概率接近系统上限。

禁止“一张统一倍率表套所有字段”。

---

## 4. Level Delta / 每级价值

至少计算：

`AbsoluteDelta(s)=V(s)-V(s-1)`

`RelativeDelta(s)=V(s)/V(s-1)-1`

对于最终战斗输出还可计算：

`RealizedPowerDelta = ΔOutput / BaselineOutput`

目标不是每级完全等价值，而是明确：

- 哪些等级是普通成长；
- 哪些是关键节点；
- Lv9->10为何更贵；
- +2技能等级是否过度提高角色；
- 技能加级是否让某参数突破上限/Breakpoint。

---

## 5. Throughput Scaling

伤害/治疗/护盾倍率不能只看单次值。

至少结合：

`PerUseValue × UseFrequency × TargetFactor × Reliability × Uptime`

多段技能再考虑：

- Hit distribution；
- 是否所有段都能命中；
- 是否可切目标；
- 单体/群体环境；
- 条件段/追加段；
- 动画时间与行动成本。

一个1000%但每30秒一次的技能，不自动比200%每3秒一次强。

---

## 6. Utility Scaling Guard

概率、减伤、控制时长、易伤、穿透、行动提前等参数比伤害倍率更容易出现非线性。

必须检查：

- Cap / Clamp；
- 100%附近的边际变化；
- 与Effect Hit / Resist的组合；
- Duration是否跨过一次额外行动；
- SPD/Action是否跨Breakpoint；
- DEF/RES是否进入异常高收益区；
- Reduction是否接近免伤；
- Stack Cap是否导致组合爆炸。

Utility值不能默认与Damage值使用同一成长倍率。

---

## 7. Fixed vs Scaled Fields

一个技能描述中并非所有数字都应该随等级成长。

常见固定字段：

- CD；
- Energy Cost；
- Target Count；
- Duration；
- Resource Gain；
- Stack Cap；
- Toughness / Gauge Value；
- Trigger Interval。

常见成长字段：

- Damage/Heal/Shield；
- 部分Buff/Debuff；
- 部分Base Chance；
- 部分Action/Delay参数。

但具体项目必须根据循环验证。

如果所有字段一起成长，角色高技能等级可能同时获得 Throughput + Reliability + Economy 三重放大。

---

## 8. Skill Level Cap / Extended Levels

必须区分：

- Normal Max；
- Temporary/Equipment Bonus；
- Star/Eidolon/Constellation +Level；
- System Hard Cap。

检查Extended Level：

- 是否继续按同一曲线；
- 是否只提高部分字段；
- 是否出现超出UI/配置上限；
- +2技能等级的真实Power Delta；
- 是否让星级节点的价值异常集中。

---

## 9. Character Level × Skill Level

技能等级不能脱离角色基础属性。

联合模型：

`Output(L,S) = ScalingStat(L) × SkillValue(S) × Multipliers`

至少采样：

- 低角色等级 + 低技能等级；
- 中段匹配等级；
- 满角色等级 + 常规技能满级；
- 满角色等级 + Extended Skill Level。

检查：

- 是否前期过弱；
- 中期是否突然跃迁；
- 后期是否乘法膨胀；
- 星级/命座加级是否放大过度。

---

## 10. Rotation-Level Budget

技能数值最终必须回到完整Rotation。

统计：

- 每分钟/每循环施放次数；
- 技能占总输出/治疗/护盾比例；
- Buff覆盖；
- 资源净流；
- 低频高爆发 vs 高频稳定；
- 被动/追击的隐性贡献；
- Team Amplification。

建议输出 Contribution Share：

`SkillContribution = SkillExpectedValue / TotalRotationValue`

一个角色如果核心技能只占5%贡献，可能存在Mechanic/Numeric mismatch。

---

## 11. Upgrade Cost Alignment

如果技能升级需要资源，检查：

`Power Delta per Cost`

不是要求所有技能性价比完全一样，而是避免：

- 某技能升级几乎没有收益；
- 某被动一升就远超其他技能；
- Utility技能因数值不增长变成“永远不升级”；
- 最后一级成本暴涨但Power Delta没有对应价值。

长期材料与资源循环由 `progression-design + economy-design` 协同。

---

## 12. External Reference Boundary

外部商业游戏可用于研究：

- Skill Level Cap；
- 不同字段使用不同Scaling Family；
- 基础攻击与核心技能是否使用不同曲线；
- 固定Utility与成长Throughput如何分工；
- 高阶加级如何延伸曲线。

外部倍率只能作为 `reference-data`；不得把“某游戏Lv10约为Lv1的2倍”写成通用标准。

---

## 13. Cross Validation

### hero-concept-design
数值重点是否强化角色身份？

### hero-kit-design
倍率最高的动作是否真的是核心Payoff？触发频率是否匹配？

### hero-stat-progression
技能成长与角色属性成长组合后是否仍可控？

### formula-verification
倍率到底乘哪个属性、在哪个乘区、如何Round/Clamp？

### balance-design
完整角色而非单技能是否落在目标Power Budget？

---

## 14. Done Criteria

一次技能数值任务至少交付：

- Parameter Taxonomy；
- Skill Value Contract；
- Lv1~Max完整曲线；
- 每级Absolute/Relative Delta；
- Fixed vs Scaled字段；
- Extended Level；
- Character Level × Skill Level联合检查；
- Rotation Contribution；
- Utility边界/Breakpoint；
- 升级成本性价比；
- Evidence Boundary；
- Simulation/Runtime验证项。

## 15. 反模式

- **One Curve Fits All**：所有字段同一倍率表；
- **Single-Hit Bias**：只看单次倍率；
- **Utility Runaway**：控制/减伤/概率和伤害一样高速成长；
- **Invisible Upgrade**：技能升级玩家几乎无感；
- **Level Cliff**：某一级突然暴涨但无设计理由；
- **Triple Growth**：Throughput、Reliability、Economy同时随等级增强；
- **Extended-Level Explosion**：加技能等级导致异常放大；
- **Stat×Skill Blindness**：只看技能曲线，不看角色基础属性联合成长；
- **External-Copy Curve**：直接抄成熟游戏技能等级倍率表。


---

# Chat Edition Deepening Layer — Hero / World / Skill / Value

This section extends the preserved specialist modules with a stricter end-to-end character pipeline.

## A. Worldbuilding -> Character Contract

A hero should not begin from “element + weapon + role”. Build the chain:

`World Rule -> Faction/Institution -> Social Role -> Personal Desire -> Internal Contradiction -> Power Source -> Visual Motif -> Combat Grammar -> Team Relationship -> Growth Arc`

For each new hero define:

- **World Rule**: which setting rule makes this character possible;
- **Faction Function**: what job/status they have in the world;
- **Personal Want**: immediate desire the player can understand;
- **Deep Need**: what they actually need to change/accept;
- **Contradiction**: tension that creates personality and dramatic pressure;
- **Relationship Web**: ally/rival/debt/trust/power relations;
- **Power Source**: why this character can perform the combat fantasy;
- **Cost / Limitation**: why the power is not free;
- **Visual Motif**: silhouette, prop, color/material language, animation verb;
- **Combat Grammar**: the repeated verbs/states that embody identity;
- **Growth Arc**: what becomes more complete mechanically and narratively.

A hero is weak if the lore, visuals, kit and numbers can be independently swapped onto another character without contradiction.

## B. Playable Causality

Narrative identity must produce player causality, not only biography.

Ask:

- What does the player repeatedly do that expresses this character’s personality?
- What decision does this hero make differently from others?
- Does the player create the character’s fantasy through action, or merely watch it in text/animation?
- Does the world react to the character’s identity/status?
- Does a growth node represent a meaningful evolution, or only higher numbers?

Use `Lore-only Hero` when story exists but cannot be felt in play.

## C. Roster Slot / Release Contract

Before approving a hero, map four slots:

1. **Narrative Slot** — what relationship/world function is missing;
2. **Gameplay Slot** — what new decision/loop is introduced;
3. **Team Slot** — what compositions gain a new option;
4. **Product Slot** — what audience/fantasy surface this hero serves.

Do not accept a hero whose only differentiator is higher throughput.

Check overlap against existing roster on:
- role;
- resource;
- trigger;
- target pattern;
- damage/heal/shield profile;
- team hook;
- build dependency;
- field time/action share;
- mastery curve;
- narrative function.

## D. Hero Numerical Budget Contract

Do not balance a hero from single-skill percentages.

Build a role envelope:

`Entry Power -> Practical Rotation -> Optimized Rotation -> Team Amplification -> Survival/Utility -> Mastery Ceiling`

At minimum calculate or model:

- Rotation Length;
- Actions / Turn / Field Time;
- Resource Net;
- Core Payoff Frequency;
- Contribution Share by skill;
- Single-target / multi-target conversion;
- Reliability;
- Uptime;
- Team amplification;
- EHP / sustain where relevant;
- failure/recovery loss;
- novice vs ordinary vs optimized realization.

Use the smallest number of synthetic “stat weights” possible. Prefer direct outcome metrics such as DPS/HPS/EHP/TTK, action count, uptime and clear-time delta.

## E. Skill Parameter Contract

For each skill define a parameter table:

| Parameter | Meaning |
|---|---|
| Scaling Source | ATK / HP / DEF / fixed / hybrid / target stat |
| Base Value | level-1 or baseline value |
| Level Curve | Lv1->Max family |
| Frequency | expected uses per rotation/minute |
| Target Factor | single / blast / AoE / bounce / random |
| Reliability | expected hit/trigger realization |
| Duration/Uptime | for persistent effects |
| Cap/ICD | stack/trigger/interval cap |
| Resource Effect | generate/spend/refund |
| Team Effect | personal or amplified team value |
| Breakpoint Risk | action/turn/cap threshold |
| Evidence | config/code/runtime/candidate |

This table is mandatory before claiming a skill value is balanced.

## F. Skill Text / Tooltip Contract

Skill descriptions are part of system correctness.

For an existing project, wording must be derived from verified behavior/config where possible.

Recommended information order:

`Trigger/Action -> Target -> Effect -> Value -> Duration -> Stack/Limit -> Special Rule/Exception`

Example grammar:

> 对【后排敌人】造成【攻击力X%】物理伤害；若目标生命低于【50%】，本次伤害提高【Y%】。每次施放最多触发【1次】。

Rules:

- one mechanic = one stable term;
- one target concept = one stable target phrase;
- do not alternate “后排 / 后方目标 / 最远敌人” unless semantics differ;
- distinguish `全体敌人`, `所有敌人`, `敌方全体` only if the project intentionally defines different meanings;
- state whether chance is base chance, final chance or conditional chance;
- state stack cap, refresh behavior and duration semantics when they affect player decisions;
- state “自身/目标/全队/前排/后排” explicitly; avoid ambiguous pronouns;
- do not expose implementation jargon such as raw Buff keys unless the user asks;
- display values must match the same level/star context shown in UI;
- if a passive is not unlocked, wording/UI should not imply it is active;
- if a skill changes at a breakpoint, describe the changed rule, not only “Lv+1”.

### Description QA

Check every skill text against:

`Subject -> Trigger -> Target -> Effect -> Value -> Duration -> Limit -> Exception -> UI State`

If any runtime-relevant semantic is absent, mark `Tooltip Semantic Gap`.

## G. Upgrade / Star / Sequence Topology

For each star/constellation/eidolon/sequence node classify:

- Numerical;
- Reliability;
- Rotation;
- QoL;
- Rule Expansion;
- Team Hook;
- Capstone;
- Mechanic Replacement.

Then test:

- early node value;
- cumulative value;
- node dependency;
- whether a node repairs a deliberately crippled base kit;
- whether one node creates mandatory ownership;
- whether +skill-level nodes create hidden multiplier cliffs;
- whether the final node changes identity rather than only doubling damage.

## H. Character Reference Extraction

When studying HSR / Genshin / Wuthering Waves / ZZZ, do not copy the character.

Extract:

- role taxonomy;
- resource grammar;
- trigger topology;
- target architecture;
- growth topology;
- text grammar;
- build dependency;
- team dependency;
- roster differentiation;
- narrative-to-gameplay translation.

Record the source as `reference-data` and transfer only the abstract pattern after checking current-project constraints.

## I. Hero Acceptance Matrix

A production-ready hero should pass:

| Layer | Question |
|---|---|
| World | Why does this person exist in this setting? |
| Character | What do they want, fear, value and contradict? |
| Visual | Can the identity be read from silhouette/prop/animation verb? |
| Combat | What is the unique loop/decision? |
| Skill | Do slots form one coherent loop? |
| Numbers | Does practical rotation land in the intended role envelope? |
| Growth | Do levels/stars make the hero more themselves? |
| Team | Are hooks useful without becoming a mandatory pair? |
| Content | Do real encounters allow the loop to function? |
| Text | Can players correctly predict behavior from tooltips? |
| Roster | Is the hero meaningfully distinct without raw power creep? |
| Validation | What is verified and what still needs simulation/playtest/runtime evidence? |
