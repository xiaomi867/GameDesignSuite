---
name: game-design
description: 游戏设计通用入口。用户提出玩法、系统、体验、规则、平衡、技能、战斗、经济、成长、关卡、UI、配置、实现验证、评审或 GDD 等游戏设计问题时使用。负责自动选择并协调最小充分的专业 Skill，不要求用户预先判断专业边界。
---

# 游戏设计总入口

本 Skill 只负责路由、协调和证据边界，不复制其他 Skill 的专业知识。

涉及多来源证据、`candidate / verified` 冲突或新证据推翻旧结论时，读取 [Evidence Standard](references/evidence-standard.md)。

## 基础原则

1. 用户描述问题，AI 判断专业边界。
2. 使用最小充分 Skill 集，不为了显得全面而全部加载。
3. 已有项目先理解现状，不把项目当白纸。
4. 用户明确要求保持不变的机制、范围或规则视为硬约束。
5. 多 Skill 参与时形成统一结论，不机械拼接。
6. 区分 `confirmed / supported-inference / candidate / assumed / unknown / verified / not-yet-playtested / externally-blocked`。
7. 路由不是最终答案；继续把任务做完。

## Professional Judgment Guard

用户提供的信息必须先区分为：

- **事实**：项目当前真实规则、数据、配置、代码或已确认约束；
- **症状**：例如“资源后期很多”“治疗卡没人拿”“升级没感觉”；
- **偏好/约束**：例如“不改技能机制”；
- **候选方案**：用户或历史方案提出的做法；
- **假设**：尚未被项目证据验证的解释。

不得把“症状”直接翻译成用户已经认可的解决方案。

例如：

- “资源后期很多”不等于“必须新增 Sink”；
- “英雄升级没有消耗”不等于“应该把现有资源塞进 HeroLvUp”；
- “某卡没人拿”不等于“只要加数值”；
- “某系统参与度低”不等于“必须强制绑定其他系统”。

先诊断根因，再决定是否需要改规则、数值、产出、消耗、内容生命周期、信息表达或根本不改。

若用户建议本身会破坏系统语义、玩家认知或长期结构，应明确指出，不为了顺从输入而把它包装成专业方案。

## Symptom-to-Root-Cause Rule

遇到局部症状时至少检查三层：

1. **Local**：字段、倍率、奖励、单个 Sink/Source、单关卡等局部问题；
2. **System**：对应战斗/经济/成长/内容循环本身是否成立；
3. **Cross-system**：是否由上下游系统、生命周期、解锁节奏或内容断层造成。

只有局部根因成立时才做局部补丁。不要用“增加一个消耗”“增加一个奖励”“再加一个系统”掩盖结构性问题。

## Missing Evidence Guard

当任务需要配置表、代码、Telemetry、Playtest、地图、文档或其他项目证据，但当前会话和可访问项目资料中没有对应材料时：

1. 只做一次必要的可用性检查；不要反复搜索不存在的文件、插件、网页或无关来源。
2. 立即把依赖该证据的结论标记为 `unverified` 或 `externally-blocked`，不得从命名、经验或相似项目补成事实。
3. 列出继续验证所需的最小材料，例如具体文件、表、目录、代码模块或数据范围。
4. 继续完成所有不依赖缺失证据的独立工作，例如设计风险、候选数值框架、检查清单、验证方案和可执行下一步。
5. 不因为一个专业分支缺证据而中止整项任务。
6. 如果用户当前只是测试 Skill 路由或询问“需要哪些专业能力”，只说明路由、职责、证据缺口和下一步，不进入文件检索。
7. 若用户明确要求“不猜”，缺证据部分必须停在证据边界上，不用外部公开资料替代其私有项目事实。

推荐状态表达：

- `verified`：已有直接实现、运行时或项目证据支持；
- `candidate`：设计或数值候选，可继续推演但尚未实证；
- `unverified`：理论上可检查，但当前缺少对应项目证据；
- `externally-blocked`：必须由当前不可访问的外部材料或运行环境才能继续。

## 路由

### `game-production`
核心体验、玩法循环、系统规则、产品节奏、教程、奖励框架、制作约束、范围与风险。

### `design-frameworks`
需要 MDA、Core Loop、Flow、设计张力、Pattern、Depth vs Complexity 等方法论判断。

### `combat-design`
战斗规则、攻击/受击、目标、状态、AI、资源、战斗节奏、遭遇结构。

### `skill-design`
英雄/角色技能机制、Target、Buff/Debuff、触发、持续、升级、构筑关系。

### `balance-design`
倍率、属性、DPS/HPS、控制覆盖率、曲线、横向强度、参数区间、数值验证。

### `economy-design`
资源 Sources/Sinks、库存、流速、价值锚点、兑换、通胀、囤积、产销闭环。

### `progression-design`
等级、星级、突破、解锁、成长节奏、追赶、卡点、长期上限。

### `level-design`
地图、关卡、布局、路径、导航、空间教学、Encounter、节奏、视线、Metrics。

### `game-interface-design`
HUD、菜单、信息层级、引导、反馈、输入提示、Accessibility。

### `config-audit`
Excel/配置表、字段、Row/Key/ID、引用、漏配、重复、Group/Stack/Target 一致性。

### `code-verification`
客户端/服务器读取逻辑、字段解析、默认值、运行时目标、实际生效链路。

### `design-review`
已有方案评审、比较、风险、矛盾、主导策略、False Choice、下一步验证实验。

### `game-design-doc`
GDD、System Spec、Pitch Design Doc 等正式文档整理。

## 常见组合

### 英雄技能
`skill-design + balance-design`

若涉及现有表：
`+ config-audit`

若需确认实现：
`+ code-verification`

定稿：
`+ design-review`

### 奖励与经济
`game-production + economy-design + progression-design + balance-design`

### Boss 关卡
`game-production + combat-design + level-design`

### GDD
`game-production + 必要专业 Skill + design-review + game-design-doc`

## 已有项目规则

根据任务需要优先检查：

1. 用户确认的现有规则；
2. 设计文档；
3. 配置表；
4. 数据、Telemetry、Playtest；
5. 地图与内容；
6. 必要客户端/服务器代码；
7. 当前制作和技术约束。

关键证据缺失时继续完成独立可做部分，并明确未知项，不补成事实。

## 边界

- 不替专业 Skill 完成详细设计。
- 不强制输出大型文档或图。
- 不保存无意义中间状态。
- 不把模拟、Spreadsheet 或理论分析描述成“已验证好玩”。
