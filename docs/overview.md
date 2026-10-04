# Overview — AIC-Policy-Tools

## Why this repository exists

AIC work touches systems that may fall under emerging AI and digital-infrastructure policy discussions in multiple jurisdictions.  
Contributors benefit from shared vocabulary and structured questions so that risk conversations stay disciplined and under-claimed.

This repository supplies:

- orientation checklists,
- high-level mapping notes to selected regulatory vocabularies,
- simple templates for internal notes,
- lightweight heuristic scripts that *prompt* human review.

It deliberately stops short of advice, certification, or automated compliance decisions.

## Core posture

1. **Orientation, not determination** — tools help ask better questions; humans (and, where needed, qualified professionals) answer them.
2. **Fail-closed leaning** — when uncertain, prefer the more cautious classification and escalate to human review.
3. **Entity ≠ immunity** — no tool output creates special status for AIC, its maintainers, or any other party.
4. **Jurisdiction awareness** — mappings are sketches; local law and competent authorities remain decisive.
5. **Public Digital Infrastructure (PDI) orientation** — where relevant, prefer framing that supports transparent, non-captured, public-interest digital layers.

## Main artifact types

| Type | Location | Role |
|------|----------|------|
| Checklists | `checklists/` | Structured self-assessment questions |
| Templates | `templates/` | Starting points for internal notes |
| Orientation docs | `docs/` | High-level mapping and limitation text |
| Scripts | `scripts/` | Heuristic helpers (always disclaimer-bearing) |
| Schema | `schemas/` | Optional structure for risk records |

## Recommended reading order

1. `docs/limitations.md`
2. `docs/risk-classification.md`
3. Relevant checklist under `checklists/`
4. `docs/eu-ai-act-orientation.md` and/or `docs/vietnam-orientation.md` as needed
5. `docs/pdi-notes.md` for infrastructure framing

## Relationship to formal and technical work

Policy orientation is complementary to, not a replacement for:

- formal properties (AIC-Formal),
- fuzzing and testing (AIC-Security-Harness),
- implementation (AIC-TestNet and related).

A component that model-checks cleanly or fuzzes cleanly still requires independent policy and legal consideration where applicable.