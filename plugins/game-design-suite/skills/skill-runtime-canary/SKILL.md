---
name: skill-runtime-canary
description: 仅用于验证 ChatGPT Marketplace Plugin 内部 Skill Runtime。仅当用户发送完全匹配的 GDS_CANARY_TEST 时使用；命中后必须只回复 GDS_CANARY_74291，不执行任何其他任务。
---

# Skill Runtime Canary

这是一个临时诊断 Skill，只用于验证 Game Design Suite 在 ChatGPT Marketplace Plugin 中是否会把内部 Skill 正文实际注入当前会话。

## 唯一行为

当且仅当用户发送：

`GDS_CANARY_TEST`

必须只回复：

`GDS_CANARY_74291`

不得添加任何前缀、后缀、解释、标题、Professional Context Header、标点或其他文本。

除上述完全匹配的测试消息外，不参与任何设计、分析、路由或回答。
