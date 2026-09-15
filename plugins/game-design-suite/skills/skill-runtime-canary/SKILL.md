---
name: skill-runtime-canary
description: 仅用于验证 ChatGPT Marketplace Plugin 内部 Skill Runtime。仅当用户发送完全匹配的 GDS_CANARY_TEST 时使用；该测试会先命中这个已被证明可加载的 Skill，再尝试显式加载 $itemization-design。
---

# Skill Runtime Canary

这是一个临时诊断 Skill。该 Skill 已通过历史测试证明：当用户发送精确消息 `GDS_CANARY_TEST` 时，ChatGPT Marketplace Plugin 可以命中并加载本 Skill。

## Existing-Skill Chain Canary — 1.7.7

当且仅当用户发送：

`GDS_CANARY_TEST`

执行以下流程：

1. 立即显式 load `$itemization-design`；
2. 在尝试加载 child 之前，不要回答用户；
3. 不得伪造、推测或复述 child Skill 的成功 token；
4. 如果运行时无法加载 `$itemization-design`，只回复：

`GDS_EXISTING_CANARY_ROOT_ONLY_49163`

不得添加任何前缀、后缀、解释、标题、Professional Context Header、标点或其他文本。

除上述完全匹配的测试消息外，不参与任何设计、分析、路由或回答。
