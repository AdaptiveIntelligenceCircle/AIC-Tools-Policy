# Risk Classification Orientation

**Not legal advice. Orientation only.**

## Purpose

Provide a shared, under-claim way to talk about the *kind* of risk a component or deployment scenario may present, so that documentation and review stay consistent.

## Suggested dimensions (heuristic)

When classifying, consider at least:

1. **Function** — What does the component do? (evaluation, identity, recovery, coordination, …)
2. **Autonomy** — How much automated effect can it have without a human gate?
3. **Scope of impact** — Single user / small group / organization / broader public infrastructure?
4. **Fail posture** — Does the design default to Deny / restricted mode when uncertain?
5. **Human gate presence** — Is `NeedHuman` (or equivalent) a first-class, non-bypassable outcome?
6. **Data sensitivity** — Does it process personal, biometric, or otherwise sensitive data? (Most AIC reference components aim to minimize this.)
7. **Deployment context** — Research / TestNet / internal tool / public-facing service?

## Illustrative bands (non-binding)

These bands are **conversation aids**, not regulatory categories:

| Band | Rough meaning in AIC orientation language |
|------|-------------------------------------------|
| **Low / orientation** | Documentation, checklists, pure formal models, offline analysis tools |
| **Moderate / gated** | Decision-support components that retain explicit human gates and fail-closed defaults |
| **Elevated / careful** | Components that could influence authorization or recovery in shared infrastructure; require heightened review |
| **Out of current scope** | Anything claiming production critical infrastructure control, real-time safety-critical actuation, or large-scale personal-data processing without separate governance |

AIC’s stated design intent (Ethical Kernel, human gates, fail-closed, pre-Covenant) is meant to keep most reference work in the lower-to-moderate orientation bands.  
That intent is not a guarantee of any external classification.

## Process suggestion

1. Fill the relevant checklist (`checklists/risk-self-assessment.md`).
2. Write a short note using `templates/risk-classification-note.md`.
3. If the heuristic script is used, treat its output as one more input, not a decision.
4. Escalate to human review (and external counsel where appropriate) when impact or autonomy is non-trivial.
5. Record assumptions and limitations explicitly.

## Link to formal properties

Properties such as fail-closed and non-bypassable human gates (see AIC-Formal) are *design intents* that support more cautious risk posture.  
They do not by themselves determine regulatory classification.