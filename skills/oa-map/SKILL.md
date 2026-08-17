---
name: oa-map
description: Navigate the OA codebase through its knowledge graph. Trace cross-module dependencies, find impact scope, and understand any module.
compatibility: opencode
---

# OA Map

This skill loads the knowledge graph at `graphify-out/graph.json` (131K nodes, 346K edges) to **map** the OA codebase before touching code. Every `graphify` command below runs against that graph.

Always run Step 1 before any other step to orient.

## Branches

### 1. Overview — the big picture

```powershell
graphify query "这个项目的god nodes是什么"
graphify query "fssc模块包含哪些子模块"
graphify query "km agreement模块涉及哪些类"
```

Read `graphify-out/GRAPH_REPORT.md` only when query does not surface enough context.

### 2. Trace — follow a cross-module dependency

The OA project's strength is also its risk: finance touches budget touches approval touches integration. Trace before you touch.

```powershell
# Find how two things connect
graphify path "FsscPaymentMain" "FsscBudgetData"
graphify path "KmAgreementApply" "FsscPaymentMain"

# Show everything a service depends on
graphify query "FsscPaymentMainServiceImp依赖哪些服务" --budget 3000
graphify explain "FsscPaymentMainServiceImp"
```

Completion criterion: you can name each module between A and B and say what connects them.

### 3. Scope — find change impact

Before modifying a class or config, discover what else touches it:

```powershell
graphify explain "FsscVoucherRuleConfig"
graphify query "哪些地方引用了FsscCommonBudgetService"
```

Completion criterion: all upstream and downstream dependents identified, none guessed.

### 4. Explain — understand one concept

```powershell
graphify explain "FsscPaymentMainServiceImp"
# Returns: source location, degree (connectivity count), all incoming/outgoing edges with EXTRACTED/INFERRED tags
```

Completion criterion: you can describe what the node is, where it lives, and what it connects to.

## Module index

| Module | Package | Description |
|--------|---------|-------------|
| **FSSC** (Finance) | `com.landray.kmss.fssc.*` | Financial shared service center — 18 sub-modules |
| `fssc.payment` | payment/ | Payment execution, approval, tracking |
| `fssc.budget` | budget/ | Budget planning, control, approval |
| `fssc.voucher` | voucher/ | Accounting voucher generation |
| `fssc.expense` | expense/ | Employee expense claims |
| `fssc.fee` | fee/ | Fee collections and payments |
| `fssc.invoice` | invoice/ | Invoice verification and matching |
| `fssc.cashier` | cashier/ | Cash/bank daily operations |
| `fssc.ledger` | ledger/ | General ledger |
| `fssc.ocr` | ocr/ | OCR for invoice recognition |
| `fssc.baiwang` | baiwang/ | Baiwang e-invoice platform |
| `fssc.iqubic` | iqubic/ | iQubic financial platform |
| `fssc.k3cloud` | k3cloud/ | Kingdee K3 Cloud ERP |
| `fssc.cmb` | cmb/ | China Merchants Bank interface |
| **KM** (Knowledge) | `com.landray.kmss.km.*` | Knowledge management — 9 sub-modules |
| `km.agreement` | agreement/ | Contracts, templates, e-sign (largest KM sub-module) |
| `km.archives` | archives/ | Document archiving and retention |
| `km.imeeting` | imeeting/ | Meeting room booking and minutes |
| `km.asset` | asset/ | Fixed asset lifecycle |
| `km.institution` | institution/ | Organizational institution docs |
| **HR** | `com.landray.kmss.hr.*` | HR ratify/approval, staff master data |
| **SZSH** | `com.landray.kmss.szsh.*` | Shenzhen Special Holdings custom business |
| **SYS** (System) | `com.landray.kmss.sys.*` | System admin: attend, auth, org, modeling, xform |
| **TIC** (Integration) | `WebContent/tic/` (front-end) | JDBC/REST/SOAP connector configuration hub |
| **THIRD** | `WebContent/third/` | Feishu, WeChat, DingTalk, PDA, mall, LDAP, etc. |
| **Common** | `com.landray.kmss.common.*` | Base DAO/Model/Service framework, HQL builder, event system |
| **Util** | `com.landray.kmss.util.*` | 80+ cross-cutting utilities |

## Pre-built path patterns

When asked about these common OA scenarios, use the corresponding graphify path:

| Scenario | Query |
|----------|-------|
| 付款影响哪些模块 | `graphify query "FsscPaymentMainServiceImp关联的服务" --budget 3000` |
| 凭证和预算的关系 | `graphify path "FsscVoucher" "FsscBudgetData"` |
| 合同关联付款 | `graphify path "KmAgreementApply" "FsscPaymentMain"` |
| 费用报销到凭证 | `graphify path "FsscExpenseShareMain" "FsscVoucher"` |
| 修改工具类的影响 | `graphify query "哪些类引用了ArrayUtil"` |

## Edge confidence

Every edge is tagged with its provenance:
- `EXTRACTED` — explicit in source code (import, extends, implements)
- `INFERRED` — resolved by name/type matching across files
- `AMBIGUOUS` — multiple possible resolutions

EXTRACTED edges are ground truth. Treat INFERRED edges as strong hints to verify by reading the source.
