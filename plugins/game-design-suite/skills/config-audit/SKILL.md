---
name: config-audit
description: 审查游戏 Excel/CSV/JSON/配置表，包括 Row/Key/ID、字段、引用、缺失、重复、类型、Target、Buff、Group、等级映射、星级映射和跨表一致性。用于回答“具体改哪一行哪一字段”，不凭字段名猜运行时语义。
---

# 配置表审查

目标是把问题落到可执行的字段级修改，而不是泛泛描述“配置有问题”。

证据状态遵循 [Evidence Standard](../game-design/references/evidence-standard.md)。配置文件直接确认的事实优先标记 `verified-config`，不要笼统写 `verified`。

## 基本流程

1. 确认涉及哪些表；
2. 找到主 Key/ID；
3. 追踪跨表引用；
4. 检查字段类型、默认值、空值和合法范围；
5. 检查缺失行、重复 Key、断链；
6. 检查等级/星级/品质映射；
7. 检查 Target、Buff、Group、Stack、Duration 等关联；
8. 若字段语义依赖实现，交给 `code-verification`；
9. 输出字段级修改与验证方法。

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
- 文案描述与实际字段不一致。

## 配置事实的边界

### `verified-config`
真实当前配置文件直接支持，例如：

- 某 Key 存在；
- 某字段当前值为 X；
- 某引用指向 Y；
- Lv2~Lv5 缺行或不一致。

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
