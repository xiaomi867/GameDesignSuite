---
name: config-audit
description: 审查游戏 Excel/CSV/JSON/配置表，包括 Row/Key/ID、字段、引用、缺失、重复、类型、Target、Buff、Group、等级映射、星级映射和跨表一致性。用于回答“具体改哪一行哪一字段”，不凭字段名猜运行时语义。无论用户是否提醒，每个独立正式结果前都必须显示【本次专业视角】并标出主责/协同。
---

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
