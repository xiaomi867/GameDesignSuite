---
name: itemization-runtime-probe
description: 当用户要求设计 RPG 装备系统，包括装备槽位、品质、基础属性、主属性、副属性、随机词条、强化、套装、掉落、替换或分解规则时使用。仅用于测试装备类 Skill 的自动语义触发；也可被其他诊断 Skill 显式加载以验证 bundled Skill 级联。
---

# Itemization Runtime Probe

这是一个临时诊断 Skill。

## Existing-Skill Chain Child — 1.7.7

如果当前用户消息精确为：

`GDS_CANARY_TEST`

说明本 Skill 正在被已知可命中的 `skill-runtime-canary` 显式加载。此时必须只回复：

`GDS_EXISTING_CANARY_CHILD_28417`

不得添加任何前缀、后缀、解释、标题、Professional Context Header、标点或其他文本。

## 原有装备语义 Probe

当用户提出 RPG 装备系统设计请求，且请求涉及以下一个或多个主题：

- 装备槽位；
- 品质；
- 基础属性；
- 主属性；
- 副属性；
- 随机词条；
- 强化；
- 套装；
- 掉落；
- 替换；
- 分解；

必须只回复：

`GDS_ITEMIZATION_PROBE_38164`

不得添加任何前缀、后缀、解释、标题、Professional Context Header、标点或其他文本。

除上述两类诊断请求外，不参与任何设计、分析、路由或回答。
