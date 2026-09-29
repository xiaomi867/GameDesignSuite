# Game Design Suite Chat Edition — Audit & Verification

> Purpose: project knowledge for ordinary Chat mode. This file is NOT a Skill and does not depend on Skill/Plugin runtime.
> Use it for configuration auditing, schema/field attribution, implementation verification, code/config consistency, and evidence-bound conclusions.

## Usage
- Never infer a field's meaning from a raw value alone.
- Lock Table/Sheet + RowKey/ID + FieldName + RawValue before making configuration conclusions.
- Separate config truth, code semantics, runtime behavior, and candidate fixes.
- Prefer the smallest evidence set that can prove or disprove the claim.
- Do not claim a Skill was invoked.


---

# Source Module: gds-config-audit

# Canonical Detailed Guidance

> Preserved from the canonical Game Design Suite specialist. The runtime wrapper is intentionally compact; this file retains the detailed domain rules, workflows, guards, anti-patterns, and done criteria.

# 配置表审查

> **强制用户可见输出协议（MUST）**
>
> 无论用户有没有写“显示专业视角”，本 Skill **在输出任何独立配置结果、字段异常、引用断链、修改建议或结论之前，都必须先显示一次 `【本次专业视角】`**。
>
> 不得等用户提醒后才显示；不得因为上一结果已经显示过就省略；不得把多个不同 Decision Object 共用一个 Header。
>
> 默认格式：
>
> ```text
> 【本次专业视角】
> 主责：配置审计（config-audit）
> 协同：仅列当前结果真实使用的专业
> ```
>
> 如果下一结果转为代码语义、数值影响、技能设计等，应重新路由并在该结果前显示新的 Header。

目标是把问题落到可执行的字段级修改，而不是泛泛描述“配置有问题”。

证据状态遵循 [Evidence Standard](../game-design/references/evidence-standard.md)。配置文件直接确认的事实优先标记 `verified-config`，不要笼统写 `verified`。

## Per-Result Professional Context Header

每一个独立配置结果、字段异常、引用断链或修改建议之前，都必须按 [Professional Context Header](../game-design/references/professional-context-header.md) 输出一次结果级 Header。

即使连续两个结果主责相同，也重复显示，不因上一段已经写过而省略。

配置事实类结果默认：

```text
【本次专业视角】
主责：配置审计（config-audit）
```

如果当前结果同时需要源码解释字段运行时语义，可写：

```text
【本次专业视角】
主责：配置审计（config-audit）
协同：代码 / 实现验证（code-verification）
证据边界：字段事实可到 verified-config；运行时语义按源码证据决定
```

**发现 `_lv` 系列字段不一致、字段值异常、漏配、错引，本身仍是配置审计主责。** 不因为该差异可能影响强度就改成 `balance-design` 主责。

只有后续结果开始回答“这个差异造成多少强度/覆盖率变化、候选值应该是多少”时，才切换到 `balance-design` 主责并单独形成下一结果块。

若当前结果只是代码枚举/Parser/Runtime Consumer 的语义结论，则应切换为 `code-verification` 主责，`config-audit` 协同。

## 基本流程

1. 确认涉及哪些表；
2. 找到主 Key/ID；
3. **先锁定表头与列映射，再读取字段值**；
4. 追踪跨表引用；
5. 检查字段类型、默认值、空值和合法范围；
6. 检查缺失行、重复 Key、断链；
7. 检查等级/星级/品质映射；
8. 检查 Target、Buff、Group、Stack、Duration 等关联；
9. 若字段语义依赖实现，交给 `code-verification`；
10. 输出字段级修改与验证方法。

## Field Attribution Guard

这是配置审计的硬约束。**先证明“值属于哪个字段”，再讨论这个值是什么意思。**

### 1. Schema Pass / 表头锁定

读取数据前先确认：

- Sheet/表名；
- 真正的 Header Row；
- 每个关键字段的准确列名；
- 是否存在多行表头、合并单元格、隐藏列、重复列名、空列名、别名或导出后列位移；
- 主 Key/ID 位于哪一列。

如果表头不清楚，先标记 `unverified-config`，不得根据视觉位置或历史印象猜列。

### 2. Value Pass / 值读取

每个关键字段事实都应绑定至少以下四元组：

`(Table/Sheet, RowKey/ID, FieldName, RawValue)`

工具能提供单元格地址时，优先扩展成：

`(Table/Sheet, RowKey/ID, FieldName, CellAddress, RawValue)`

例如：

```text
P10BattleBuff.xlsx | BUF_bear_taunt | CoverCheckType | 2
```

不能只写“这里是 2”，更不能因为附近另一个字段也出现 2，就把它归属到错误字段。

### 3. 禁止字段串位

禁止以下行为：

- 把 `CoverCheckType = 2` 写成 `UniqueId = 2`；
- 把 A 列的值分布当成 B 列的值分布；
- 从截图中的视觉邻近关系推断列归属；
- 因为上一轮讨论过某字段，就默认本轮看到的数字仍属于该字段；
- 把行号、枚举值、ID、等级或数量相互混淆；
- 在未锁定字段名时先解释数字含义。

**数字本身没有字段语义。字段身份必须先于数值解释。**

### 4. Critical Field Two-Pass Check

对会直接导致修改建议的关键字段，至少做两次独立检查：

1. 第一次确认 Header -> Column -> RowKey -> RawValue；
2. 第二次在输出结论前重新确认同一 RowKey 的准确 FieldName 与 RawValue。

以下字段默认视为关键字段：

- UniqueId / GroupKey / CoverCheckType / CoverType / CountCoverType / TimeCoverType；
- Target / TargetSelector；
- DamageCfg / DamageCfgSec / HealCfg；
- BuffCfg / AttachToKey；
- 等级/星级映射；
- 任何用户明确指出“你看错字段”的字段。

### 5. Distribution / 批量统计保护

统计某字段分布时，必须明确：

- 统计的是哪个 `FieldName`；
- 有效行范围；
- 空值是否计入；
- 是否过滤注释行/模板行/废弃行；
- 每个分组值是否来自该字段本身。

例如：

```text
Field = UniqueId
空 = 85
bleed = 3
...
```

只有在逐行读取 `UniqueId` 列后才能成立。不得从 `CoverCheckType` 的 1/2/3 分布反推 `UniqueId`。

### 6. 用户纠错后的处理

如果用户指出“你看错列/看错字段”：

1. 立即撤销受该字段归属影响的结论；
2. 回到 Schema Pass 重新确认列；
3. 重新读取对应 RowKey + Field；
4. 明确哪些旧结论被撤回、哪些仍独立成立；
5. 不用新的解释去维护旧答案。

用户纠错不是“风格意见”，而是触发一次字段归属重新验证。

## Code Output Integrity Guard / 代码输出完整性

当用户要求修改、补丁、替换或生成代码时，输出必须可直接复制，并保持原有代码的物理行结构。

- 原本是一行的代码，默认仍保持一行；除非语法必须换行、用户明确要求格式化，或原代码本来就是多行。
- 不把单行方法调用、赋值、条件、日志、字符串、插值字符串、属性声明、配置字符串、Lambda 或链式调用擅自拆成多行。
- UI 的视觉自动换行不是代码换行；不要为了页面宽度主动插入真实换行。
- 用户说“这一行”“替换这一行”“行内代码”“不要拆行”时，视为硬约束。
- 修改已有文件时，未修改行尽量逐字保持；不顺手全文件格式化、改缩进、换括号风格或重排空行。
- 只改一处时优先输出最小替换块；不要无必要重写整个方法或类。
- 保留原有命名、花括号风格、缩进、空行和局部排版。
- 不拆分 GM 指令、路径、资源 Key、Buff/Target 配置串或其他必须保持连续的字符串。
- 输出前检查：是否把原本一行拆成多行、是否引入无关格式变化、是否遗漏括号/引号/分号、是否可直接复制。

对于单行替换，原代码和替换后的代码都必须各自保持一个物理代码行。若无法保证完整文件不被重新格式化，优先给局部最小补丁并明确修改位置。

## Missing Evidence Guard

如果本次任务依赖的真实配置表当前不可访问：

- 只检查一次当前会话/可访问项目资料；
- 不反复搜索不存在的文件；
- 不从旧版本、字段名、截图片段或相似项目补全当前值；
- 依赖真实表才能确认的项标 `unverified-config`；
- 列出最小所需表名、Key/ID 或行范围；
- 继续输出结构性检查清单、候选风险和后续验证步骤。

## 必查错误

- Key/ID 不存在；
- 引用指向错误对象；
- 同组配置不完整；
- Lv1 有、Lv2~LvN 漏；
- 升星映射错位；
- Target 与 Buff 对象冲突；
- Damage/Heal Source 错；
- GroupKey/Stack/Exclusive 冲突；
- 默认值与空值语义错误；
- 类型/枚举不合法；
- 客户端和服务器表版本不一致；
- 文案描述与实际字段不一致；
- **字段串位、列错读、统计列与解释列不一致**。

## 配置事实的边界

### `verified-config`
真实当前配置文件直接支持，例如：

- 某 Key 存在；
- 某字段当前值为 X；
- 某引用指向 Y；
- Lv2~Lv5 缺行或不一致。

`verified-config` 必须建立在字段归属已锁定的前提上。字段名不确定时不能使用该状态。

### `needs-code-verification`
配置结构可以确认，但运行时语义依赖代码，例如：

- 枚举数字含义；
- 空值/0 的默认行为；
- TargetSelector 的真实解析；
- GroupKey 是否互斥/叠加；
- Buff 最终挂载对象；
- 客户端显示与服务器结算差异。

配置存在不等于代码读取，字段名字像 `DamageCfg` 也不代表一定按直觉工作。

## 输出规范

每一项修改尽量给：

| 表 | Row/Key/ID | 字段 | 当前值 | 改后值 | 关联项 | 问题 | Evidence | 理由 | 验证 |
|---|---|---|---|---|---|---|---|---|---|

涉及高风险字段时，在正文或附表中保留最小证据定位：

`Table/Sheet + RowKey/ID + FieldName + RawValue`

新增行要明确：

- 新 Key；
- 基于哪行复制；
- 哪些字段必须改；
- 哪些字段保持；
- 引用它的上游/下游。

## 批量校验

批量英雄/技能/等级表时应检查模式一致性，而不是只抽样看一两行。

必要时建立配置依赖链：

`Hero -> HeroStarSkill -> SkillParameter -> Buff/Target/Trigger/Missile -> Runtime`

并给每个节点标记：

- present；
- referenced；
- verified-config；
- needs-code-verification；
- broken。


---

# Source Module: gds-code-verification

# Canonical Detailed Guidance

> Preserved from the canonical Game Design Suite specialist. The runtime wrapper is intentionally compact; this file retains the detailed domain rules, workflows, guards, anti-patterns, and done criteria.

# 游戏实现验证

> **强制用户可见输出协议（MUST）**
>
> 无论用户有没有写“显示专业视角”，本 Skill **在输出任何独立代码语义、执行链、运行时对象、实现差异或验证结论之前，都必须先显示一次 `【本次专业视角】`**。
>
> 不得等用户提醒后才显示；不得因为上一结果已经显示过就省略；如果结果从代码语义切换到配置事实或数值影响，必须重新路由并显示新的 Header。

本 Skill 的核心职责是提供“实现事实”，供设计、数值和配置判断使用。

证据状态遵循 [Evidence Standard](../game-design/references/evidence-standard.md)。代码直接确认用 `verified-code`，真实运行/日志确认用 `verified-runtime`，不要笼统写 `verified`。

## Per-Result Professional Context Header

每一个独立代码语义结论、执行链结论、运行时对象结论或实现差异结论前，都按 [Professional Context Header](../game-design/references/professional-context-header.md) 输出一次结果级 Header。

默认代码语义结果：

```text
【本次专业视角】
主责：代码 / 实现验证（code-verification）
协同：配置审计（config-audit）
```

如果当前结果只是在报告真实配置字段不一致，应让 `config-audit` 主责；如果下一结果开始评估强度影响，才切换为 `balance-design` 主责。

即使连续两个结果专业组合相同，也重复显示 Header。

## Field Identity Lock

代码解释某个配置值之前，必须先确认**这个值属于哪个配置字段**。

代码语义验证的输入应尽量是：

`(Table/Sheet, RowKey/ID, FieldName, RawValue)`

例如：

```text
P10BattleBuff.xlsx | BUF_bear_taunt | CoverCheckType | 2
```

然后代码侧才去验证：

```text
CoverCheckType 的 2 在当前代码中代表什么？
```

禁止把：

```text
CoverCheckType = 2
```

误绑定成：

```text
UniqueId = 2
```

即使两个字段都可能出现数字 `2`，也属于不同问题。

如果配置字段身份尚未由真实表确认：

- 不解释该数字的运行时语义；
- 标记 `unverified-config-link`；
- 先回到 `config-audit` 锁定 FieldName；
- 不得用代码中某个恰好值为 2 的枚举来反证表字段。

**先锁字段，再查枚举；先锁对象，再追代码。**

## 验证流程

1. 确认上游配置字段身份与 RowKey/ID；
2. 找到配置加载入口；
3. 找到字段模型/数据结构；
4. 找到解析与默认值逻辑；
5. 找到运行时消费点；
6. 找到触发条件；
7. 追踪对象/Target；
8. 检查客户端/服务器谁是权威；
9. 检查空值、0、负值、缺省的语义；
10. 检查异常和上传/校验约束；
11. 用最短执行链说明实际行为。

## Missing Evidence Guard

如果本次任务需要代码，但当前没有对应源码/程序集/运行环境：

- 只检查一次可访问资料；
- 不从类名、字段名、旧版本或历史回答猜当前行为；
- 标记 `unverified-code` 或 `externally-blocked`；
- 列出最小需要的文件/类/模块；
- 继续完成不依赖代码的配置事实、风险点和验证计划；
- 不因为缺代码中止整个任务。

## 必须区分

### 配置存在
不等于代码读取。

### 字段归属正确
不等于运行时语义已确认。

### 代码读取
不等于逻辑路径一定触发。

### 路径触发
不等于最终对象正确。

### 客户端显示
不等于服务器实际结算。

### `verified-code`
表示源码已经明确支持某个语义，例如：

- 枚举 2 = SelfDef；
- 某字段由特定 Parser 读取；
- TargetSelector 最终映射到某对象；
- 某条件决定 Buff 是否挂载。

但 `verified-code` 必须绑定到明确的字段身份。例如“枚举 2 = X”只有在确认当前配置字段使用的正是该枚举后，才能用于解释配置。

### `verified-runtime`
表示通过实际运行、调试、日志或可复现执行确认代码路径真的发生。

`verified-code` 不能自动升级为 `verified-runtime`。

## 新证据覆盖旧推断

如果真实代码与历史候选/旧文档冲突：

1. 明确指出冲突；
2. 降级或撤销旧结论；
3. 按当前代码重新给证据状态；
4. 不为了保持历史回答一致而忽略新证据。

如果用户指出上游字段读错：

1. 立即撤销所有依赖该字段身份的代码解释；
2. 不保留“虽然字段错了，但代码结论大概还对”的说法；
3. 重新从 `Table/RowKey/Field/RawValue` 建立链路。

## 输出

至少说明：

- 上游表/RowKey/Field/RawValue；
- 文件/类/方法；
- 读取位置；
- 条件；
- 默认值；
- 运行时对象；
- 最终影响；
- Evidence Status；
- 尚未验证部分。

推荐使用最短执行链：

`Config Field -> Data Model -> Parser -> Condition -> Runtime Consumer -> Target/Object -> Result`

若配置字段身份或代码不足，不从命名猜行为。

## 与设计协作

- `config-audit` 负责配置结构事实和字段身份；
- `skill-design`/`combat-design` 负责设计意图；
- `balance-design` 负责参数合理性；
- 本 Skill 负责“代码实际上做了什么”。

发现实现与设计意图不一致时，先报告差异，不擅自决定改设计还是改代码。
