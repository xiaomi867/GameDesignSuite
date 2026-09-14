---
name: code-verification
description: 只读验证游戏客户端/服务器代码如何读取和执行设计与配置，包括字段解析、默认值、枚举、Target、Buff、状态、存档、网络、结算和上传校验。用于确认“表里这样填到底是否生效”，不负责大规模重构实现。
---

# 游戏实现验证

本 Skill 的核心职责是提供“实现事实”，供设计、数值和配置判断使用。

证据状态遵循 [Evidence Standard](../game-design/references/evidence-standard.md)。代码直接确认用 `verified-code`，真实运行/日志确认用 `verified-runtime`，不要笼统写 `verified`。

## 验证流程

1. 找到配置加载入口；
2. 找到字段模型/数据结构；
3. 找到解析与默认值逻辑；
4. 找到运行时消费点；
5. 找到触发条件；
6. 追踪对象/Target；
7. 检查客户端/服务器谁是权威；
8. 检查空值、0、负值、缺省的语义；
9. 检查异常和上传/校验约束；
10. 用最短执行链说明实际行为。

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

### `verified-runtime`
表示通过实际运行、调试、日志或可复现执行确认代码路径真的发生。

`verified-code` 不能自动升级为 `verified-runtime`。

## 新证据覆盖旧推断

如果真实代码与历史候选/旧文档冲突：

1. 明确指出冲突；
2. 降级或撤销旧结论；
3. 按当前代码重新给证据状态；
4. 不为了保持历史回答一致而忽略新证据。

## 输出

至少说明：

- 文件/类/方法；
- 字段；
- 读取位置；
- 条件；
- 默认值；
- 运行时对象；
- 最终影响；
- Evidence Status；
- 尚未验证部分。

推荐使用最短执行链：

`Config -> Data Model -> Parser -> Condition -> Runtime Consumer -> Target/Object -> Result`

若代码不足，不从命名猜行为。

## 与设计协作

- `config-audit` 负责配置结构事实；
- `skill-design`/`combat-design` 负责设计意图；
- `balance-design` 负责参数合理性；
- 本 Skill 负责“代码实际上做了什么”。

发现实现与设计意图不一致时，先报告差异，不擅自决定改设计还是改代码。
