---
name: hero-concept-design
description: 负责英雄/角色的设定、身份、幻想、阵营/属性/武器/职业标签、叙事定位与玩法承诺，把人物设定转译成可验证的战斗与成长约束。用于新英雄立项、角色设定评审、设定与技能一致性检查、角色池差异化；不负责具体技能机制与倍率，分别协同 hero-kit-design 与 skill-value-design。
---

# Hero Concept Design / 英雄设定设计

目标不是写一段“好看的角色背景”，而是建立一份能约束玩法、技能、成长、配装和队伍关系的 **Hero Contract**。

优先读取：

- [Cross-Game Hero Concept Patterns](references/cross-game-hero-concept-patterns.md)
- [Hero Concept Spec Template](templates/hero-concept-spec.md)

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
