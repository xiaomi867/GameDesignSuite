---
name: skill-runtime-canary
description: 仅用于验证 ChatGPT Marketplace Plugin 内部 Skill Runtime。仅当用户发送完全匹配的 GDS_REFRESH_CANARY_6A91Q 时使用；该测试用于确认 Desktop 是否实际刷新了当前版本中的既有 Skill 正文。
---

# Skill Runtime Canary

这是一个临时诊断 Skill，只用于验证当前安装版本是否真正刷新了既有 Skill 的正文与触发元数据。

## One-Time Refresh Canary — 1.7.8

当且仅当用户发送：

`GDS_REFRESH_CANARY_6A91Q`

必须只回复以下一次性验证值：

`GDS_REFRESH_OK_C4F7D2_58103`

不得添加任何前缀、后缀、解释、标题、Professional Context Header、标点或其他文本。

除上述完全匹配的测试消息外，不参与任何设计、分析、路由或回答。
