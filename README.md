# AIC-Policy-Tools

**Orientation tools, checklists, and lightweight scripts for risk classification and regulatory mapping relevant to Adaptive Intelligence Circle work.**

Status: **pre-Covenant**, experimental, under-claim.  
This repository provides **orientation aids only**. It is **not** legal advice, not a compliance certification, not a substitute for qualified counsel, and not a claim that any AIC component meets or fails any regulatory requirement.

## Purpose

- Help contributors and maintainers think systematically about risk classification.
- Provide high-level mapping sketches to selected regulatory vocabularies (EU AI Act orientation, Vietnam-related orientation notes).
- Offer reusable checklist and template structures for internal documentation.
- Keep all language consistent with AIC principles: under-claim, entity ≠ immunity, Third Path, fail-closed, no token rule-power.

## Explicit non-goals

| This repository does | This repository does **not** |
|----------------------|------------------------------|
| Offer orientation checklists and simple heuristic scripts | Provide legal advice or formal opinions |
| Map concepts at a high level to selected frameworks | Certify compliance with any law or regulation |
| Support internal documentation discipline | Replace review by qualified professionals |
| Stay aligned with Public Digital Infrastructure (PDI) orientation | Claim any special regulatory status for AIC or its maintainers |

## Layout

```
AIC-Policy-Tools/
├── README.md
├── LICENSE
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── SECURITY.md
├── docs/
│   ├── overview.md
│   ├── risk-classification.md
│   ├── eu-ai-act-orientation.md
│   ├── vietnam-orientation.md
│   ├── pdi-notes.md
│   └── limitations.md
├── checklists/
│   ├── risk-self-assessment.md
│   ├── eu-ai-act-high-level.md
│   ├── vietnam-risk-orientation.md
│   └── pdi-self-assessment.md
├── templates/
│   ├── risk-classification-note.md
│   ├── disclosure-note.md
│   └── change-impact-note.md
├── scripts/
│   ├── risk_heuristic.py
│   └── checklist_render.py
├── schemas/
│   └── risk_record.schema.json
├── data/                     # optional sample records (non-sensitive)
└── examples/
```

## Quick start

1. Read `docs/overview.md` and `docs/limitations.md` first.
2. Use checklists under `checklists/` for structured self-reflection.
3. Copy templates under `templates/` when writing internal notes.
4. Optionally run the heuristic script (see `scripts/`) — treat output as a prompt for human judgment, never as a decision.

## Relationship to other AIC repositories

- **AIC-Legal** — authoritative place for formal policy and legal-oriented documents; this repo supplies supporting tools and orientation only.
- **AIC-Formal / AIC-Security-Harness** — technical properties and testing; policy tools remain separate and non-binding.
- **AIC-TransparencyDashboard** — public accountability surface; policy orientation notes may later inform what is disclosed, but no automatic link is assumed.
- **AIC-Beginners / MyVision** — philosophical and onboarding context.

## Principles observed

- **Under-claim**: every artifact carries explicit limits.
- **Entity ≠ immunity**: tools and notes do not create special status for any organization or person.
- **No token rule-power**: no economic or token-based governance appears.
- **Fail-closed posture in spirit**: when uncertain, prefer more restrictive classification and human review.
- **Pre-Covenant**: nothing here advances a mainnet or Covenant declaration.
- **Not legal advice**: repeated in documentation and scripts.

## License

GPL-3.0-or-later for scripts and structure (see LICENSE).  
Documentation and checklists may additionally be treated under CC-BY-4.0 where marked.

## Maintenance note

During periods of reduced maintainer availability the repository remains public.  
Contributions that preserve under-claim language and the “not legal advice” boundary are welcome.
