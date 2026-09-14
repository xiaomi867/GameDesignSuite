# Game Design Suite Multi-Agent Architecture

Game Design Suite 的专业知识只维护一份。不同宿主只负责“发现/加载”适配，不复制专业规则。

## Canonical Source of Truth

唯一专业真源：

```text
plugins/game-design-suite/skills/<skill-name>/SKILL.md
```

`references/`、`templates/`、`evals/` 等也以 `plugins/game-design-suite/` 下的版本为准。

任何平台适配文件都不得成为第二套专业知识库。

## Host adapters

### ChatGPT / Codex Plugin Marketplace

直接由插件 manifest 暴露：

```text
.agents/plugins/marketplace.json
plugins/game-design-suite/.codex-plugin/plugin.json
plugins/game-design-suite/skills/*
```

### DeepSeek Deep Code

Deep Code 会从项目目录发现：

```text
.deepcode/skills/<name>/SKILL.md
```

本仓库中的 `.deepcode/skills/*/SKILL.md` 是轻量 discovery adapter。每个 adapter 只包含：

- `name`
- `description`
- canonical `SKILL.md` 路径

执行时必须继续读取 canonical Skill，不能只依据 adapter 回答。

启动方式：

```bash
git clone https://github.com/xiaomi867/GameDesignSuite.git
cd GameDesignSuite
deepcode
```

进入 Deep Code 后按 `/` 查看 Skills，或直接输入 `/game-design`、`/balance-design`、`/skill-design` 等。

### AGENTS.md-aware hosts

支持 `AGENTS.md` 的宿主应从仓库根目录 `AGENTS.md` 进入，并直接读取 canonical Skill。

如果宿主自身已有 Skill discovery 目录，可以为该宿主增加类似 `.deepcode/skills/` 的薄适配层；不要复制 canonical 专业正文。

## Routing contract

自然语言任务默认：

1. 读取 `game-design`；
2. 选择最小充分专业 Skill 集；
3. 完整读取所选 canonical `SKILL.md`；
4. 只读取会改变当前判断的 references；
5. 对已有项目优先读取真实文件、配置、数据和必要代码；
6. 缺证据时执行 Missing Evidence Guard；
7. 输出实际成果，而不是只报 Skill 名称。

## One-source maintenance rule

修改专业能力时：

**只改**：

```text
plugins/game-design-suite/skills/
plugins/game-design-suite/evals/
```

不要人工把同一套专业正文同时维护在 `.deepcode/`、根目录 `skills/` 或其他 host 目录。

当 canonical Skill 的 `name` / `description` 改变，运行：

```bash
python scripts/sync_agent_skills.py
```

检查适配层：

```bash
python scripts/sync_agent_skills.py --check
```

## Evidence parity

不同模型允许给出不同候选方案，但必须遵守同一证据标准：

- `verified-config`
- `verified-code`
- `verified-runtime`
- `verified-data`
- `candidate`
- `supported-inference`
- `unverified`
- `not-yet-playtested`
- `externally-blocked`

不得因为更换模型而降低证据标准。

## Model portability boundary

Skill 可以跨模型复用，但最终质量仍受以下因素影响：

- 模型推理能力；
- 上下文长度；
- 文件/代码工具；
- Web/搜索能力；
- Spreadsheet/Simulation 能力；
- 宿主是否真正读取 canonical references。

因此“同一 Skill”意味着流程和专业约束一致，不意味着所有模型会得到完全相同的设计判断。
