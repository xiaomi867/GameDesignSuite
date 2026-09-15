---
name: gds-audit-verification
description: "Use when the task centers on auditing real configs or code, tracing fields/references, verifying implementation semantics, or separating verified facts from candidates."
---

# Audit & Verification

Own config auditing, code verification, field attribution, reference tracing, implementation semantics, and evidence-state discipline.

## First visible block

```text
【本次专业视角】
主责：配置审计 / 代码验证（gds-audit-verification）
协同：仅列当前结果真实使用的专业
证据边界：<verified-config / verified-code / verified-runtime / candidate / unknown>
```

## Preserved knowledge

- [Config Audit](../../skills/gds-config-audit/references/canonical-guidance.md)
- [Code Verification](../../skills/gds-code-verification/references/canonical-guidance.md)
- [Runtime knowledge map](../../references/runtime-knowledge-map.md) for domain-specific interpretation after implementation facts are locked.

## Workflow

1. Lock field attribution first: table/sheet, row key/ID, field name, raw value, and cell/location when available.
2. Trace references and schema semantics before interpreting numeric values.
3. Separate verified config, verified code, verified runtime, supported inference, candidate, and unknown.
4. If upstream attribution changes, retract dependent conclusions and re-evaluate downstream claims.
5. Output concrete changes as `field → current → proposed → reason` only when the evidence supports a change.
6. When code/config is missing, list the minimum missing evidence and stop at the evidence boundary instead of guessing.

Configuration discrepancies belong here even when the field contains numbers; balance conclusions should follow only after implementation semantics are verified.
