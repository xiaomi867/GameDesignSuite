---
name: itemization-runtime-probe
description: 当用户要求设计 RPG 装备系统，包括装备槽位、品质、基础属性、主属性、副属性、随机词条、强化、套装、掉落、替换或分解规则时使用。仅用于测试装备类 Skill 的自动语义触发；命中后必须只回复 GDS_ITEMIZATION_PROBE_38164，不执行任何其他任务。
---

# Itemization Runtime Probe

这是一个临时诊断 Skill，只用于验证 ChatGPT Marketplace Plugin 是否能够根据正常装备设计语义自动选择并注入内部 Skill 正文。

## 唯一行为

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

除上述装备设计语义测试外，不参与任何设计、分析、路由或回答。
