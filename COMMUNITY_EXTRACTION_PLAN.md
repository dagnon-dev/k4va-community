# Community Extraction Plan

This plan records the audit before extraction. Community was implemented independently where commercial coupling or ownership risk existed.

| Module / original path | Classification | Reason | Dependencies | Publication risk | Action |
| --- | --- | --- | --- | --- | --- |
| `backend/app/parser/` | NEEDS_REVIEW | Parser behavior is reusable in concept, but its imports and validation surface are coupled to the commercial backend. | Commercial helpers | Medium | Reimplemented minimal local parser. |
| `backend/app/core/analyzer.py` | KEEP_PRIVATE | Orchestrates commercial membership, reports, packs and storage. | Commercial models and report store | High | Not copied. |
| `backend/app/rules/community/` | NEEDS_REVIEW | Community rules coexist with premium catalogs. | Commercial rule base and registries | Medium | Replaced with explicit generic catalog. |
| `backend/app/rules/banking/` | KEEP_PRIVATE | Banking and regulatory implementation is outside Community scope. | Commercial knowledge and catalogs | High | Not copied. |
| `backend/app/rules/enterprise/`, `fintech/`, `marketplace/` | KEEP_PRIVATE | Premium or organization-specific capabilities. | Commercial entitlement and marketplace code | High | Not copied. |
| `backend/app/auth/`, `billing/`, `subscriptions/`, `marketplace/` | KEEP_PRIVATE | SaaS authentication, payment and account infrastructure. | Supabase, Stripe, database | High | Not copied. |
| `frontend/` | KEEP_PRIVATE | Commercial SaaS UI, routes, branding assets and account flows. | React, Supabase, Stripe | High | Not copied. |
| `backend/tests/fixtures/` and `backend/samples/` | NEEDS_REVIEW | Includes public, corporate-looking and banking examples. | None | Medium to high | Not copied; new synthetic examples created. |
| Commercial `.env`, databases, logs and deployment files | SECRETS_OR_SENSITIVE | May contain credentials, customer or production information. | Environment and infrastructure | Critical | Not copied. |

## Safe-to-open-source result

Only newly authored local parser, deterministic rule engine, generic rules, scorer, reporters, CLI, synthetic examples and tests are included.
