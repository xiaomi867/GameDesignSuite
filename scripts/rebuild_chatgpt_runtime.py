from __future__ import annotations

from pathlib import Path
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE_PLUGIN = ROOT / "plugins" / "game-design-suite"
SOURCE_SKILLS = SOURCE_PLUGIN / "skills"
RUNTIME_PLUGIN = ROOT / "plugins" / "game-design-suite-runtime-v2"
RUNTIME_SKILLS = RUNTIME_PLUGIN / "skills"

SKILLS = {
    "game-design": {
        "display": "Game Design",
        "profession": "系统总策划 / Game Design Lead",
        "description": "Use when Game Design Suite is invoked for broad or cross-system game design, or when no narrower specialty owns the whole request: core loop, system relationships, product framing, constraints, tradeoffs, and cross-domain synthesis.",
        "scope": "跨系统总设计、核心循环、系统关系、约束、取舍、总体方案与多专业结论整合。",
        "workflow": ["界定 Decision Object 与硬约束", "拆分涉及的系统与专业边界", "建立核心循环与系统关系", "识别冲突、依赖和证据缺口", "输出统一方案与验证计划"],
        "prompt": "Use $gds-game-design to design or review this game system end to end and separate facts, assumptions, risks, and validation."
    },
    "game-production": {
        "display": "Game Production",
        "profession": "玩法 / 系统策划",
        "description": "Use when Game Design Suite is invoked for gameplay or system production design: core experience, core loop, rules, feature scope, content cadence, onboarding, rewards framework, production constraints, and cross-system implementation planning.",
        "scope": "玩法循环、系统规则、功能范围、节奏、教程、奖励框架、制作约束与落地方案。",
        "workflow": ["定义体验目标", "建立玩法循环与规则", "拆分功能范围与依赖", "制定内容/节奏/奖励框架", "检查制作成本与落地风险"],
        "prompt": "Use $gds-game-production to turn this gameplay idea into a production-ready system design with scope, rules, risks, and validation."
    },
    "design-frameworks": {
        "display": "Design Frameworks",
        "profession": "游戏设计方法 / 框架",
        "description": "Use when Game Design Suite is invoked for design methodology or analytical frameworks: MDA, core loop, flow, player motivation, design tension, depth versus complexity, pattern analysis, or structured problem decomposition.",
        "scope": "MDA、Core Loop、Flow、玩家动机、设计张力、Depth vs Complexity、Pattern 与问题拆解。",
        "workflow": ["明确要解释的设计问题", "选择合适框架而非堆框架", "映射 Mechanics-Dynamics-Aesthetics 或等价关系", "识别张力与复杂度来源", "形成可验证的设计假设"],
        "prompt": "Use $gds-design-frameworks to analyze this design problem with the smallest useful framework set and turn it into testable hypotheses."
    },
    "balance-design": {
        "display": "Balance Design",
        "profession": "数值策划",
        "description": "Use when Game Design Suite is invoked for numerical game balance: power budgets, DPS/HPS/EHP, rates, probabilities, growth curves, breakpoints, difficulty, reward values, parameter ranges, horizontal comparisons, or tuning targets.",
        "scope": "数值目标、Benchmark、Power Budget、DPS/HPS/EHP、概率、成长曲线、阈值、难度与参数区间。",
        "workflow": ["定义体验目标与 Benchmark", "锁定公式/单位/时间窗", "建立预算或参数模型", "做横向/纵向与极端值检查", "给出 candidate 参数与验证方法"],
        "prompt": "Use $gds-balance-design to define benchmarks, formulas, candidate values, and validation for this balance problem."
    },
    "economy-design": {
        "display": "Economy Design",
        "profession": "经济策划",
        "description": "Use when Game Design Suite is invoked for game economy design: currencies, resource roles, sources and sinks, production, inventory, exchange rates, shops, rewards, inflation, hoarding, scarcity, or long-term resource circulation.",
        "scope": "资源角色、Sources/Sinks、库存、产出、消耗、兑换、商店、奖励、通胀与生命周期。",
        "workflow": ["定义资源角色与价值锚", "列 Sources/Sinks 与流速", "检查库存与生命周期", "验证 Sink 合法性和健康盈余", "建立经济监控与调参指标"],
        "prompt": "Use $gds-economy-design to design or audit this resource economy without adding sinks just to consume surplus."
    },
    "progression-design": {
        "display": "Progression Design",
        "profession": "成长策划",
        "description": "Use when Game Design Suite is invoked for long-term progression: account, hero, equipment or skill levels, stars, ascension, unlocks, progression costs, pacing, catch-up, caps, milestones, or power-growth structure across systems.",
        "scope": "账号/角色/装备/技能的等级、星级、突破、解锁、成长成本、阶段节奏、追赶与长期上限。",
        "workflow": ["定义成长层级与职责", "建立阶段节点与解锁", "分配 Power Delta", "设计成本与替换/追赶节奏", "验证前中后期成长密度"],
        "prompt": "Use $gds-progression-design to build a progression structure with milestones, costs, power deltas, pacing, and catch-up rules."
    },
    "combat-design": {
        "display": "Combat Design",
        "profession": "战斗策划",
        "description": "Use when Game Design Suite is invoked for combat-system design: attacks, targeting, resources, states, AI, action economy, damage cadence, control, positioning, encounter rules, team roles, or battle pacing.",
        "scope": "攻击/受击、Target、资源、状态、AI、行动经济、控制、阵容职责、遭遇规则与战斗节奏。",
        "workflow": ["定义战斗承诺与胜负条件", "建立行动/资源/目标规则", "设计状态与反馈循环", "检查角色职责和反制", "验证节奏、可读性和极端循环"],
        "prompt": "Use $gds-combat-design to design or audit these combat rules, action economy, targeting, states, and encounter interactions."
    },
    "skill-design": {
        "display": "Skill Design",
        "profession": "技能策划",
        "description": "Use when Game Design Suite is invoked for an existing project's skill mechanics or configuration-facing skill design: target rules, buffs, debuffs, triggers, states, cooldowns, resource interactions, star upgrades, or a request to tune skills without changing the core mechanic.",
        "scope": "现有项目技能机制、Target、Buff/Debuff、触发、状态、资源、CD、升星与配置映射。",
        "workflow": ["锁定不可修改机制", "还原技能行为链", "核对 Target/Buff/Trigger/Resource", "拆分机制与数值问题", "给出字段级修改与验证"],
        "prompt": "Use $gds-skill-design to audit or tune this existing skill without changing its fixed core mechanic."
    },
    "hero-concept-design": {
        "display": "Hero Concept Design",
        "profession": "英雄 / 角色设定策划",
        "description": "Use when Game Design Suite is invoked for hero or character identity: core fantasy, narrative identity, faction, element, weapon, role tags, combat promise, roster differentiation, or alignment between character concept and gameplay.",
        "scope": "Core Fantasy、角色身份、阵营/元素/武器/职业标签、Combat Promise 与角色池差异化。",
        "workflow": ["定义 Core Fantasy", "建立角色身份与视觉/叙事标签", "明确 Combat Promise", "检查角色池差异化", "验证设定与玩法是否一致"],
        "prompt": "Use $gds-hero-concept-design to define this hero's fantasy, identity, combat promise, and roster differentiation."
    },
    "hero-kit-design": {
        "display": "Hero Kit Design",
        "profession": "英雄机制 / 技能架构策划",
        "description": "Use when Game Design Suite is invoked for hero kit architecture: skill-slot responsibilities, states, resources, trigger graphs, rotations, target structure, field time, team hooks, failure recovery, or how a character's mechanics form a coherent loop.",
        "scope": "技能槽位职责、状态机、资源图、Trigger Graph、循环、Target、Field/Action Time、Team Hook 与失败恢复。",
        "workflow": ["定义 Kit Contract", "分配技能槽位职责", "建立状态/资源/触发图", "推演循环与失败恢复", "检查队伍接口和机制冗余"],
        "prompt": "Use $gds-hero-kit-design to build or audit this hero's kit loop, states, resources, triggers, targeting, and team hooks."
    },
    "hero-stat-progression": {
        "display": "Hero Stat Progression",
        "profession": "英雄属性成长数值策划",
        "description": "Use when Game Design Suite is invoked for character-level base-stat progression: HP, ATK, DEF or other base stats from Lv1 to cap, ascension deltas, rarity or role templates, growth density, normalized curves, and stage-by-stage power growth.",
        "scope": "Lv1~上限基础属性、突破/晋阶 Delta、稀有度/职业模板、成长曲线、Growth Density 与阶段强度。",
        "workflow": ["定义 Growth Contract", "选择曲线族与端点", "计算归一化/边际成长", "配置突破 Delta", "验证职业横向强度与极端值"],
        "prompt": "Use $gds-hero-stat-progression to design Lv1-to-cap base stats, ascension deltas, growth curves, and validation."
    },
    "skill-value-design": {
        "display": "Skill Value Design",
        "profession": "技能数值策划",
        "description": "Use when Game Design Suite is invoked for skill-level numerical progression: damage, healing, shields, buffs, debuffs, probabilities, durations, cooldowns, resource values, stacks, fixed-versus-scaled fields, and Lv1-to-max skill curves.",
        "scope": "技能Lv1~上限的倍率、治疗/护盾、Buff/Debuff、概率、持续、资源、CD、层数与等级收益。",
        "workflow": ["锁定技能机制与字段", "定义技能等级收益预算", "设计 Lv1~Max 曲线", "检查 Fixed vs Scaled 字段", "验证边际收益与 Extended Level"],
        "prompt": "Use $gds-skill-value-design to design or audit this skill's Lv1-to-max numerical curve without changing its mechanics."
    },
    "formula-verification": {
        "display": "Formula Verification",
        "profession": "公式 / 数值验证",
        "description": "Use when Game Design Suite is invoked to derive or verify formulas: damage, healing, shields, defense, resistance, crit, hit, speed, action value, probability, units, multipliers, clamps, rounding, domains, or config-code formula parity.",
        "scope": "公式还原、单位、乘区、Clamp/Round、定义域、边界、配置/代码一致性与计算验证。",
        "workflow": ["定义变量与单位", "还原运算顺序和乘区", "确认 Clamp/Round/边界", "做样例与极值计算", "与配置/代码/参考模型交叉验证"],
        "prompt": "Use $gds-formula-verification to derive and verify this formula, including units, order of operations, clamps, rounding, and edge cases."
    },
    "simulation-design": {
        "display": "Simulation Design",
        "profession": "数值模拟 / 系统仿真",
        "description": "Use when Game Design Suite is invoked for simulation or quantitative scenario testing: Monte Carlo, discrete-event simulation, rotations, timelines, parameter sweeps, strategy agents, distributions, P50/P90/P95, tail risk, sensitivity, or graduation-time models.",
        "scope": "Monte Carlo、离散事件、Rotation/Timeline、参数扫描、策略代理、分布、尾部风险与敏感性。",
        "workflow": ["定义模拟问题与输出指标", "锁定输入分布/规则/Seed", "建立事件或状态模型", "跑分布与敏感性", "解释限制并区分模拟与 Playtest"],
        "prompt": "Use $gds-simulation-design to define a simulation model, distributions, runs, tail-risk metrics, and sensitivity analysis."
    },
    "telemetry-experiment-design": {
        "display": "Telemetry Experiment Design",
        "profession": "数据 / 实验策划",
        "description": "Use when Game Design Suite is invoked for telemetry or experimentation: event schemas, metrics, funnels, cohorts, segmentation, dashboards, A/B tests, SRM, significance, guardrails, causal boundaries, or live validation of design changes.",
        "scope": "埋点、事件Schema、指标、分群、漏斗、A/B、SRM、显著性、Guardrail、因果边界与线上验证。",
        "workflow": ["定义决策问题与假设", "设计事件/属性 Schema", "定义主指标与 Guardrail", "制定实验与分群", "解释统计与因果边界"],
        "prompt": "Use $gds-telemetry-experiment-design to design the telemetry and experiment needed to validate this game-design change."
    },
    "meta-balance": {
        "display": "Meta Balance",
        "profession": "Meta / 生态数值策划",
        "description": "Use when Game Design Suite is invoked for roster or build ecology: pick/win/presence, mastery, team synergies, counters, pair locks, matchup matrices, Best-in-Slot concentration, diversity, power creep, or version-level meta health.",
        "scope": "角色/Build/队伍生态、Pick/Win/Presence、Synergy/Counter、Pair Lock、BiS集中、Power Creep 与多样性。",
        "workflow": ["定义生态对象与内容环境", "建立角色/队伍/Build矩阵", "识别集中度与Pair Lock", "区分强度、熟练度和适用率", "制定版本风险与验证指标"],
        "prompt": "Use $gds-meta-balance to audit roster, team, and build ecology for dominance, pair locks, diversity, and power creep."
    },
    "itemization-design": {
        "display": "Itemization Design",
        "profession": "装备 / Itemization 策划",
        "description": "Use when Game Design Suite is invoked for equipment or itemization design: slots, rarity, base/main/substats, affix pools, roll ranges, enhancement, sets, unique effects, loot targeting, replacement, graduation, salvage, crafting, Best-in-Slot, or build ecology.",
        "scope": "装备槽位、品质、基础/主/副词条、Affix、Roll、强化、套装、唯一特效、掉落、替换、毕业、分解与Build生态。",
        "workflow": ["定义 Itemization Job 与槽位职责", "建立 Item Power Budget", "设计主副属性与 Affix/Roll", "设计强化/套装/唯一特效", "验证实际升级率、替换、分解与Build生态"],
        "prompt": "Use $gds-itemization-design to design this equipment system from itemization job through loot, replacement, salvage, and build ecology."
    },
    "itemization-benchmark": {
        "display": "Itemization Benchmark",
        "profession": "装备 Benchmark / 竞品研究",
        "description": "Use when Game Design Suite is invoked to benchmark public commercial-game equipment systems: weapons, relics, artifacts, echoes, affix structures, enhancement curves, set effects, acquisition, replacement, normalized comparisons, or transferable itemization patterns.",
        "scope": "公开商业游戏装备结构、强化/等级曲线、词条、套装、获取、替换与跨游戏归一化 Benchmark。",
        "workflow": ["固定公开来源与版本", "建立统一字段 Schema", "抽取等级/强化/词条结构", "归一化比较而非直接抄数值", "标记可迁移模式与迁移边界"],
        "prompt": "Use $gds-itemization-benchmark to benchmark these public itemization systems with normalized fields and explicit transfer limits."
    },
    "level-design": {
        "display": "Level Design",
        "profession": "关卡策划",
        "description": "Use when Game Design Suite is invoked for level or encounter design: maps, layouts, navigation, spatial teaching, waves, encounters, bosses, checkpoints, metrics, pacing, difficulty sequencing, or how space teaches mechanics.",
        "scope": "地图、布局、导航、空间教学、Encounter、波次、Boss、检查点、Metrics 与关卡节奏。",
        "workflow": ["定义关卡目标与玩家知识", "设计空间/路径/遭遇结构", "安排教学与难度递进", "配置波次/Boss/奖励节奏", "验证可读性、节奏与失败反馈"],
        "prompt": "Use $gds-level-design to design or audit this level's layout, encounter pacing, teaching, metrics, and boss structure."
    },
    "game-interface-design": {
        "display": "Game Interface Design",
        "profession": "游戏 UI/UX 策划",
        "description": "Use when Game Design Suite is invoked for game UI/UX: HUD, menus, information hierarchy, interaction flows, onboarding, feedback, input prompts, accessibility, state communication, or interface requirements for game systems.",
        "scope": "HUD、菜单、信息层级、交互流程、引导、反馈、输入提示、Accessibility 与系统状态表达。",
        "workflow": ["定义用户任务与信息优先级", "建立界面流程与状态", "设计反馈和错误恢复", "检查输入与可访问性", "验证信息负荷与操作成本"],
        "prompt": "Use $gds-game-interface-design to design or audit this game UI flow, information hierarchy, feedback, and accessibility."
    },
    "config-audit": {
        "display": "Config Audit",
        "profession": "配置审计",
        "description": "Use when Game Design Suite is invoked to audit game configuration or data tables: Excel/CSV/JSON rows, keys, IDs, fields, references, missing entries, duplicates, types, targets, buffs, groups, stacking, weights, random pools, or schema/value consistency.",
        "scope": "Excel/CSV/JSON配置、Row/Key/ID、字段归属、引用、漏配、重复、类型、Target、Buff、Group/Stack与权重一致性。",
        "workflow": ["先锁定 Schema 与字段归属", "再做 Row/Value Pass", "检查引用与缺失/重复", "验证 Group/Target/Stack/Weight", "输出字段级 current→change→reason"],
        "prompt": "Use $gds-config-audit to audit this configuration by exact table, row/key, field, current value, expected value, and reason."
    },
    "code-verification": {
        "display": "Code Verification",
        "profession": "代码 / 实现验证",
        "description": "Use when Game Design Suite is invoked to verify implementation semantics in client or server code: parsers, enums, defaults, field reads, target selection, buffs, stacking, random logic, upgrade inheritance, runtime execution paths, or config-to-code parity.",
        "scope": "客户端/服务器读取、Parser、Enum、默认值、字段语义、Target、Buff、随机、继承与真实运行链路。",
        "workflow": ["定位真实读取入口", "追踪字段→Parser→运行对象", "核对 Enum/默认值/分支", "验证调用链和生效时机", "区分 verified-code 与 runtime 未验证"],
        "prompt": "Use $gds-code-verification to trace how this config or rule is actually read and executed in code."
    },
    "design-review": {
        "display": "Design Review",
        "profession": "设计评审",
        "description": "Use when Game Design Suite is invoked to review an existing design: compare alternatives, find contradictions, anti-patterns, hidden assumptions, cross-system risks, scope problems, evidence gaps, or define the next validation experiment.",
        "scope": "已有方案评审、比较、矛盾、反模式、隐含假设、跨系统风险、证据缺口与下一步验证。",
        "workflow": ["复述目标与硬约束", "区分事实/症状/方案/假设", "定位 Local/System/Cross-system 根因", "比较候选方案与代价", "给出优先级和验证实验"],
        "prompt": "Use $gds-design-review to review this design, separate evidence from assumptions, identify root causes, and recommend validation."
    },
    "game-design-doc": {
        "display": "Game Design Doc",
        "profession": "策划文档 / System Spec",
        "description": "Use when Game Design Suite is invoked to produce or restructure formal game-design documentation: GDD, system spec, feature spec, design pitch, rules document, implementation-facing requirements, acceptance criteria, or decision logs.",
        "scope": "GDD、System Spec、Feature Spec、Pitch、规则文档、实现需求、验收标准与决策记录。",
        "workflow": ["确认文档受众和用途", "建立章节与术语", "写清规则/状态/边界", "补配置/接口/验收需求", "标记未决问题与验证标准"],
        "prompt": "Use $gds-game-design-doc to turn this design into a production-ready GDD or system specification."
    },
}

DIAGNOSTIC_HEADINGS = ("canary", "invocation test", "runtime routing contract", "runtime probe", "refresh canary")

def strip_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        parts = text.split("\n---\n", 1)
        if len(parts) == 2:
            return parts[1]
    return text

def strip_diagnostic_sections(body: str) -> str:
    out = []
    skip = False
    for line in body.splitlines():
        if line.startswith("## "):
            lower = line.lower()
            if any(token in lower for token in DIAGNOSTIC_HEADINGS):
                skip = True
                continue
            skip = False
        if not skip:
            out.append(line)
    return "\n".join(out).strip() + "\n"

def adjust_reference_links(body: str) -> str:
    body = body.replace("](references/", "](")
    body = body.replace("](templates/", "](../templates/")
    body = body.replace("](scripts/", "](../scripts/")
    body = body.replace("](assets/", "](../assets/")
    for old_name in SKILLS:
        body = body.replace(f"${old_name}", old_name)
    return body

def q(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)

def make_wrapper(old_name: str, meta: dict) -> str:
    runtime_name = f"gds-{old_name}"
    workflow = "\n".join(f"{i+1}. {step}" for i, step in enumerate(meta["workflow"]))
    return f'''---
name: {runtime_name}
description: {q(meta["description"])}
user-invocable: true
disable-model-invocation: false
---

# {meta["display"]}

## Runtime role

This is a self-contained Game Design Suite specialist Skill. It must be useful when loaded directly; it does not depend on a parent router and must not assume another Skill was invoked.

Before substantive work, read [Canonical detailed guidance](references/canonical-guidance.md) and then read any supporting references/templates it points to that are relevant to the task.

## Scope

{meta["scope"]}

## Execution contract

- Answer the user's actual task; do not stop at routing.
- Respect user-fixed rules and project constraints.
- Existing projects: inspect real docs/config/code/data before redesign when those sources are required and available.
- Missing evidence: mark dependent claims `unverified` or `externally-blocked`; do not invent project facts.
- Distinguish facts, symptoms, constraints, assumptions, candidate changes, and verified findings.
- Simulation/spreadsheets/theory are not Playtest evidence.
- Do not claim another specialist Skill executed unless its content was actually loaded.
- Use outside commercial-game data only as reference evidence, never as automatic project truth.

## Professional context

For every independent formal result, put this block immediately before the result:

```text
【本次专业视角】
主责：{meta["profession"]}（{runtime_name}）
协同：仅列当前结果中实际加载并使用的专业；没有则写“无”
证据边界：写明当前最高证据层级与关键缺口
```

Do not require the user to ask for this header.

## Domain workflow

{workflow}

## Evidence states

Use the smallest accurate label needed: `confirmed`, `supported-inference`, `candidate`, `assumed`, `unknown`, `verified-config`, `verified-code`, `verified-runtime`, `verified-data`, `not-yet-playtested`, `externally-blocked`.

## Done criteria

A complete answer should contain the decision, rationale, concrete rules/values/fields when appropriate, risks, and the minimum next validation needed. Use the canonical guidance for domain-specific completion criteria and anti-pattern checks.
'''

def make_openai_yaml(old_name: str, meta: dict) -> str:
    short = meta["scope"]
    if len(short) > 140:
        short = short[:137] + "..."
    return f'''interface:
  display_name: {q(meta["display"])}
  short_description: {q(short)}
  default_prompt: {q(meta["prompt"])}
policy:
  allow_implicit_invocation: true
'''

def clean_runtime_plugin() -> None:
    if RUNTIME_PLUGIN.exists():
        shutil.rmtree(RUNTIME_PLUGIN)
    RUNTIME_SKILLS.mkdir(parents=True, exist_ok=True)

    for old_name, meta in SKILLS.items():
        src = SOURCE_SKILLS / old_name
        if not src.exists():
            raise FileNotFoundError(f"Missing canonical skill: {src}")
        runtime_name = f"gds-{old_name}"
        dst = RUNTIME_SKILLS / runtime_name
        shutil.copytree(src, dst)
        source_text = (src / "SKILL.md").read_text(encoding="utf-8")
        body = adjust_reference_links(strip_diagnostic_sections(strip_frontmatter(source_text)))
        refs = dst / "references"
        refs.mkdir(parents=True, exist_ok=True)
        (refs / "canonical-guidance.md").write_text(
            "# Canonical Detailed Guidance\n\n> Preserved from the canonical Game Design Suite specialist. The runtime wrapper is intentionally compact; this file retains the detailed domain rules, workflows, guards, anti-patterns, and done criteria.\n\n" + body,
            encoding="utf-8",
        )
        (dst / "SKILL.md").write_text(make_wrapper(old_name, meta), encoding="utf-8")
        agents = dst / "agents"
        agents.mkdir(parents=True, exist_ok=True)
        (agents / "openai.yaml").write_text(make_openai_yaml(old_name, meta), encoding="utf-8")

    manifest_dir = RUNTIME_PLUGIN / ".codex-plugin"
    manifest_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "name": "game-design-suite-runtime-v2",
        "version": "2.0.0-preview.1",
        "description": "Clean-room ChatGPT/Codex runtime package for Game Design Suite. Preserves all 24 professional capabilities with compact trigger surfaces, progressive disclosure, and independent specialist invocation.",
        "author": {"name": "xiaomi867", "url": "https://github.com/xiaomi867"},
        "homepage": "https://github.com/xiaomi867/GameDesignSuite",
        "repository": "https://github.com/xiaomi867/GameDesignSuite",
        "license": "MIT",
        "keywords": ["game-design", "systems-design", "balance-design", "itemization", "hero-design", "combat-design", "economy-design", "progression-design"],
        "skills": "./skills/",
        "interface": {
            "displayName": "Game Design Suite Rebuilt (V2)",
            "shortDescription": "24 focused game-design skills rebuilt for reliable runtime selection",
            "longDescription": "A clean runtime rebuild of Game Design Suite. Each professional discipline is independently invocable, uses a concise Use-when trigger, exposes OpenAI skill metadata, and progressively loads preserved canonical guidance rather than relying on parent-to-child routing.",
            "developerName": "xiaomi867",
            "category": "Developer Tools",
            "capabilities": ["Interactive", "Read", "Write"],
            "websiteURL": "https://github.com/xiaomi867/GameDesignSuite",
            "defaultPrompt": [
                "Design a complete RPG equipment system with slots, rarity, stats, affixes, enhancement, sets, loot, replacement, and salvage.",
                "Design a hero from concept through kit, stat progression, and skill value curves.",
                "Audit this balance problem with benchmarks, formulas, simulation, and evidence boundaries.",
                "Review this game system and identify local, system, and cross-system root causes."
            ],
            "brandColor": "#111111",
            "screenshots": []
        }
    }
    (manifest_dir / "plugin.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def update_marketplace() -> None:
    path = ROOT / ".agents" / "plugins" / "marketplace.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["plugins"] = [
        {"name": "game-design-suite", "source": {"source": "local", "path": "./plugins/game-design-suite"}, "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}, "category": "Developer Tools"},
        {"name": "game-design-suite-runtime-v2", "source": {"source": "local", "path": "./plugins/game-design-suite-runtime-v2"}, "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}, "category": "Developer Tools"}
    ]
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def write_architecture_doc() -> None:
    docs = ROOT / "docs"
    docs.mkdir(exist_ok=True)
    (docs / "RUNTIME_REBUILD_V2.md").write_text(
        "# ChatGPT Runtime Rebuild V2\n\n"
        "This package is a clean runtime adapter built from the existing Game Design Suite canonical skills.\n\n"
        "## Goals\n\n"
        "- Preserve all 24 production skill capabilities and detailed guidance.\n"
        "- Remove temporary canaries/probes from the rebuilt runtime.\n"
        "- Avoid parent-router dependency for normal specialist work.\n"
        "- Give every specialist a concise `Use when ...` description.\n"
        "- Give every specialist a fresh runtime identity (`gds-*`) and `agents/openai.yaml`.\n"
        "- Keep `SKILL.md` compact and use progressive disclosure through `references/canonical-guidance.md`.\n"
        "- Keep the original `plugins/game-design-suite/skills` tree as the canonical source for Deep Code and historical compatibility.\n\n"
        "## Runtime model\n\n"
        "`@Game Design Suite Rebuilt (V2)` -> host selects the narrowest matching `gds-*` specialist -> specialist reads its preserved canonical guidance -> specialist answers directly.\n\n"
        "The design does not require `game-design -> $child-skill` chaining. Cross-domain collaboration is reported only when the other specialist content is actually loaded.\n\n"
        "## Test order\n\n"
        "1. `gds-itemization-design`: normal RPG equipment request.\n"
        "2. `gds-hero-stat-progression`: Lv1-to-Lv80 stat growth request.\n"
        "3. `gds-balance-design`: numerical benchmark/tuning request.\n"
        "4. Broad cross-system request to test `gds-game-design`.\n",
        encoding="utf-8"
    )

def main() -> None:
    clean_runtime_plugin()
    update_marketplace()
    write_architecture_doc()
    print(f"Generated {len(SKILLS)} runtime skills at {RUNTIME_PLUGIN.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
