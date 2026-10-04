# Risk Self-Assessment Checklist

**Not legal advice. Orientation only. Complete as a human; do not treat any score as a decision.**

## Component / scenario under review

- Name / identifier:
- Date:
- Author:
- Linked repository / commit (if any):
- Intended use context (research / TestNet / internal / other):

## A. Function and autonomy

- [ ] What does the component primarily do?
- [ ] Can it produce an automated effect that matters to a person or system without a human gate?
- [ ] Is `NeedHuman` (or equivalent) a first-class outcome?
- [ ] What is the default when inputs are malformed or policy is unclear? (fail-closed?)

## B. Scope of impact

- [ ] Who is affected if the component errs? (developer only / small group / organization / broader public)
- [ ] Is it positioned as shared or public-facing infrastructure?
- [ ] Are there downstream systems that trust its outputs?

## C. Data and identity

- [ ] Does it process personal data? If yes, what categories?
- [ ] Does it handle credentials or identity bindings (SSI-related)?
- [ ] Are data flows documented?

## D. Transparency and accountability

- [ ] Are decision paths and failure modes documented?
- [ ] Is there a path for audit or external inspection?
- [ ] Is public communication under-claim (no overstated maturity)?

## E. Continuity and governance

- [ ] Is succession / continuity considered?
- [ ] Can rule-power be bought (token or otherwise)? (Intended answer: no.)
- [ ] Are there clear human review points for consequential changes?

## F. Open questions and escalation

- List uncertainties:
- Recommended next step (human review / external counsel / further technical work / document and accept for research-only use):

## Sign-off (human)

- Reviewer:
- Date:
- Statement: “This checklist is orientation only and does not constitute a legal or compliance determination.”