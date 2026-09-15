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
