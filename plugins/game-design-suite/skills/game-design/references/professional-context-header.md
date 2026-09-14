# Professional Context Header

> **NON-OPTIONAL USER-VISIBLE OUTPUT CONTRACT**
>
> 只要 Game Design Suite 正在回答游戏设计/策划相关任务，**无论用户有没有提醒、有没有写“显示专业视角”、有没有指定 Skill，每一个独立正式结果前都必须显示 `【本次专业视角】`。**
>
> 这不是可选格式、不是测试专用格式、不是用户需要重复写在 Prompt 里的要求。它是 Game Design Suite 的默认输出协议。
>
> **禁止等待用户写“每一个独立结果前都显示……”后才执行。** 如果用户没有提 Header，也照常显示。

用于让用户在每个正式结果前看见 Game Design Suite **这一结果实际采用的专业路由**，而不是只看到一个泛化的“资深策划”身份声明。

## 目的

Header 是可观察的路由结果，不是角色扮演。

它回答四件事：

1. **Primary Discipline / 主责专业**：谁对当前这个结果的核心判断负责；
2. **Supporting Disciplines / 协同专业**：哪些专业为当前结果提供必要证据或子判断；
3. **Critical Constraint / 关键约束**：哪些 Fixed Rules 会改变当前结果；
4. **Evidence Boundary / 证据边界**：当前结果最多验证到哪一层。

Header 不能替代真正的 Skill 执行，也不能因为写了一个职业名称就声称对应 Skill 已被使用。

## 核心变化：按结果路由，而不是只按整轮路由

**不要只在答案开头显示一次 Header。**

每一个独立的正式结果、结论、Finding、修改建议、设计方案块之前，都必须先输出一次 Professional Context Header。

即使相邻两个结果使用完全相同的专业组合，也重复显示；这样用户可以逐项判断每个结论是谁负责的。

如果下一个结果的决策对象变化，必须重新判断主责/协同，并显示新的 Header。

### 用户无需提醒

以下两种 Prompt 必须产生相同的 Header 行为：

```text
检查钢熊 P10BattleBuff.xlsx 的 CoverCheckType，并结合代码判断影响。
```

和：

```text
检查钢熊 P10BattleBuff.xlsx 的 CoverCheckType，并结合代码判断影响。
要求：每一个独立结果前都显示【本次专业视角】……
```

第二段只是重复规则，不得成为 Header 是否出现的触发条件。

### Result Unit / 什么算一个“结果”

以下通常视为独立结果：

- 一个配置错误或一组同根因配置错误；
- 一个代码语义结论；
- 一个数值平衡判断；
- 一个经济根因与处理方向；
- 一个成长节点方案；
- 一个英雄/技能机制判断；
- 一个关卡/Encounter 方案；
- 一个 Design Review Finding；
- 一组需要用户实际执行的字段修改。

不要给每一句话都加 Header；但只要开始了一个新的核心判断对象，就先显示 Header。

## 强制输出顺序

正式用户可见结果必须遵守：

`Header -> Result -> Evidence/Reasoning -> Recommendation/Validation`

不允许：

`长篇分析 -> Result -> 最后补 Header`

也不允许先输出多个结果，再在答案末尾总结“本次用了哪些 Skill”。

第一条正式结果出现前必须已经有 Header。

## Router Entry 与 Direct Specialist Entry

### Router Entry

如果本轮先进入 `game-design`，Router 先判断第一个结果的主责/协同，再输出该结果的 Header。

### Direct Specialist Entry

宿主可能直接加载 `config-audit`、`balance-design`、`skill-design` 等专业 Skill，而没有先执行 `game-design`。

这种情况下：

- 当前专业 Skill 仍必须在自己的第一个结果前输出 Header；
- **不得以“Router 没有被调用”为理由省略 Header**；
- 只列当前结果**真实已读取/使用**的 Skill；
- 后续如果加载其他 Skill，下一结果根据实际路由重新显示；
- 不得因为没有 Router 就省略 Header。

因此，**Header 不依赖 Router 必须先被调用，也不依赖用户显式要求。**

## 推荐格式

复杂生产结果统一优先使用：

```text
【本次专业视角】
主责：配置审计（config-audit）
协同：代码 / 实现验证（code-verification）
证据边界：配置事实可到 verified-config；运行时语义需源码才能到 verified-code
```

简单结果可压缩为：

```text
【本次专业视角】主责：关卡策划（level-design）｜协同：战斗策划（combat-design）
```

如果不存在协同专业，可以只显示主责。

如果关键约束或证据边界会改变结论，则加入对应行；否则不要为了凑格式强行写。

## Skill -> 专业称谓

| Skill | 用户可见专业称谓 |
|---|---|
| `game-production` | 玩法 / 系统策划 |
| `design-frameworks` | 游戏设计方法 / 框架 |
| `combat-design` | 战斗策划 |
| `skill-design` | 技能 / 英雄策划 |
| `balance-design` | 数值策划 |
| `economy-design` | 经济策划 |
| `progression-design` | 成长策划 |
| `level-design` | 关卡策划 |
| `game-interface-design` | 游戏 UI / UX 策划 |
| `config-audit` | 配置审计 |
| `code-verification` | 代码 / 实现验证 |
| `design-review` | 设计评审 |
| `game-design-doc` | 策划文档 / System Spec |

`game-design` 是总入口与路由器，通常不作为主责职业显示；只有用户明确询问路由机制时才可显示“游戏设计总控 / 路由”。

## 决定主责：按当前结果的 Decision Object

主责不是由用户口中的职业称呼决定，也不是由整个问题最开始的主题永久决定，而是由**当前结果正在做什么决策**决定。

### 配置事实

以下主责通常是 `config-audit`：

- 某字段当前值是什么；
- `_lv1 ~ _lv5` 是否一致；
- 哪个 Key 漏配；
- 哪个引用断链；
- `CoverCheckType` 的基础行是 3、升级行是 2。

即使这个配置错误最终会影响强度，**发现字段不一致本身仍然是配置审计结果，不应标成数值策划主责。**

### 代码语义

以下主责通常是 `code-verification`：

- `CoverCheckType = 2` 在当前代码中代表什么；
- 某字段是否真正被 Parser 读取；
- 运行时最终挂到哪个对象。

配置审计可以作为协同，提供 `Table + Key + Field + RawValue`。

### 数值强度

只有进入这些问题时，`balance-design` 才应成为主责或强协同：

- `CoverCheckType` 的差异会造成多少覆盖率/强度变化；
- 某倍率是否过强/过弱；
- 两个方案的 DPS/EHP/TTK 哪个更合理；
- 某星级节点的 Power Delta 是否合理。

### 经济与成长

- “资源后期很多的根因和处理” -> `economy-design` 主责；
- “英雄升级成本结构怎么设计” -> `progression-design` 主责，`economy-design + balance-design` 协同；
- 不能因为其中有数字就让 `balance-design` 自动主责。

### 英雄/技能

- 技能机制、状态机、Target、触发、Team Hook -> `skill-design` 主责；
- 具体倍率合理性 -> `balance-design` 主责或协同；
- 表字段是否填对 -> `config-audit` 主责；
- 代码是否按设计执行 -> `code-verification` 主责。

### Boss / 关卡

- 空间、Beat、Encounter、波次、路线 -> `level-design` 主责；
- 底层战斗规则、AI、战斗窗口 -> `combat-design` 主责；
- 强度曲线 -> `balance-design` 协同或单独结果主责。

## 混合结果必须拆分

如果一个段落同时包含：

1. “配置里发现不一致”；
2. “代码说明这个枚举是什么意思”；
3. “因此强度需要调整多少”；

不要用一个大 Header 笼统覆盖三件事。应拆成三个结果块，各自显示对应主责/协同。

例如：

```text
【本次专业视角】
主责：配置审计（config-audit）
协同：代码 / 实现验证（code-verification）

结果 1：BUF_bear_def_pct 基础行 CoverCheckType=3，lv2~lv5=2，存在配置不一致。
```

然后：

```text
【本次专业视角】
主责：代码 / 实现验证（code-verification）
协同：配置审计（config-audit）

结果 2：当前代码中 CoverCheckType=2 的运行时语义是……
```

再然后才可能是：

```text
【本次专业视角】
主责：数值策划（balance-design）
协同：技能 / 英雄策划（skill-design） / 配置审计（config-audit）

结果 3：该差异对覆盖率/强度的影响为……
```

## 关键约束

只显示会改变当前结果的硬约束，例如：

- 技能机制不可修改；
- 服务器功能不可改；
- 只能使用现有 TaskType；
- 必须基于已有配置；
- 目标平台性能预算固定。

不要把普通背景信息全部塞进 Header。

## 证据边界

只有当前结果依赖证据时才显示。优先使用具体状态：

- `verified-config`
- `verified-code`
- `verified-runtime`
- `verified-data`
- `candidate`
- `unverified`
- `not-yet-playtested`
- `externally-blocked`

例如：

```text
证据边界：当前只有真实 Excel，可验证到 verified-config；字段运行时语义仍为 unverified-code
```

## 禁止事项

- 不得要求用户每次在 Prompt 里提醒 Header；
- 不得把“用户有没有写 Header 要求”作为是否显示的条件；
- 不得只在整篇答案最前面输出一次 Header，然后后续所有结果共用；
- 不得为了减少重复而省略某个独立结果前的 Header；
- 不得为了显得专业而列出没有实际读取/使用的 Skill；
- 不得把 14 个 Skill 全列出来；
- 不得只写“我是资深数值策划”而不暴露实际路由；
- 不得因为用户指定某职业就跳过真正应主责的专业；
- 不得把“发现配置不一致”错误归给 `balance-design`；
- 不得把 `candidate` 写成 `verified`；
- 不得因为直接进入专业 Skill 就省略 Header。

## 质量标准

一个好的 Header 应让用户在读取**每一个结果**之前都能判断：

- 这个结果由哪个专业主责；
- 哪些专业只是提供协同证据；
- 当前是否违反“不改机制”等硬约束；
- 当前结论到底是配置事实、代码事实、数值判断、设计候选还是运行时证据。
