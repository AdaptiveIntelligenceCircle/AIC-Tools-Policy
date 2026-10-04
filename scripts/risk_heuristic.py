#!/usr/bin/env python3
"""
AIC-Policy-Tools — risk orientation heuristic (VERY limited).

NOT LEGAL ADVICE. NOT A COMPLIANCE DETERMINATION.
Output is a prompt for human judgment only.

Usage:
  python3 risk_heuristic.py
  python3 risk_heuristic.py --json
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any, Dict, List


DISCLAIMER = (
    "NOT LEGAL ADVICE. Orientation heuristic only. "
    "Results must be reviewed by a human and, where appropriate, "
    "by qualified professionals. No compliance or immunity is implied."
)


def ask_bool(prompt: str) -> bool:
    while True:
        raw = input(f"{prompt} [y/n]: ").strip().lower()
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        print("Please answer y or n.")


def collect() -> Dict[str, Any]:
    print("\n=== AIC Risk Orientation Heuristic ===")
    print(DISCLAIMER)
    print("Answer about the component/scenario under review.\n")

    data: Dict[str, Any] = {}
    data["automated_effect_without_human_gate"] = ask_bool(
        "Can it produce a consequential automated effect without a human gate?"
    )
    data["human_gate_first_class"] = ask_bool(
        "Is NeedHuman (or equivalent) a first-class, non-bypassable outcome?"
    )
    data["fail_closed_default"] = ask_bool(
        "Does it default to Deny / restricted mode when uncertain?"
    )
    data["broad_public_impact"] = ask_bool(
        "Could errors affect a broad public or shared infrastructure?"
    )
    data["processes_personal_data"] = ask_bool(
        "Does it process personal data?"
    )
    data["production_or_operational"] = ask_bool(
        "Is the intended context operational/production (not only research/TestNet)?"
    )
    data["token_rule_power"] = ask_bool(
        "Can tokens or payment change protocol rules?"
    )
    return data


def band(data: Dict[str, Any]) -> str:
    """Very rough, conservative banding for conversation only."""
    if data.get("token_rule_power"):
        return "out_of_current_scope_or_needs_redesign"
    if data.get("production_or_operational") and data.get(
        "automated_effect_without_human_gate"
    ):
        return "elevated_careful"
    if data.get("broad_public_impact") and not data.get("human_gate_first_class"):
        return "elevated_careful"
    if data.get("automated_effect_without_human_gate") and not data.get(
        "fail_closed_default"
    ):
        return "elevated_careful"
    if data.get("processes_personal_data") and data.get("production_or_operational"):
        return "elevated_careful"
    if data.get("human_gate_first_class") and data.get("fail_closed_default"):
        if data.get("broad_public_impact") or data.get("production_or_operational"):
            return "moderate_gated"
        return "low_orientation"
    if data.get("production_or_operational"):
        return "moderate_gated"
    return "low_orientation"


def recommendations(b: str, data: Dict[str, Any]) -> List[str]:
    recs = [
        "Treat this output as a prompt only.",
        "Complete checklists/risk-self-assessment.md.",
        "Keep public language under-claim.",
    ]
    if b in ("elevated_careful", "out_of_current_scope_or_needs_redesign"):
        recs.append("Escalate to human maintainer review before any operational step.")
        recs.append("Consider external qualified advice if real users or real data are involved.")
    if data.get("token_rule_power"):
        recs.append("Token rule-power conflicts with stated AIC principles — redesign discussion needed.")
    if not data.get("fail_closed_default"):
        recs.append("Consider strengthening fail-closed defaults.")
    if not data.get("human_gate_first_class") and data.get(
        "automated_effect_without_human_gate"
    ):
        recs.append("Consider making human gates first-class for consequential paths.")
    return recs


def main() -> int:
    parser = argparse.ArgumentParser(description="AIC risk orientation heuristic")
    parser.add_argument(
        "--json", action="store_true", help="Emit JSON instead of text"
    )
    args = parser.parse_args()

    data = collect()
    b = band(data)
    recs = recommendations(b, data)

    result = {
        "disclaimer": DISCLAIMER,
        "answers": data,
        "orientation_band": b,
        "recommendations": recs,
    }

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("\n--- Result (orientation only) ---")
        print(DISCLAIMER)
        print(f"Orientation band: {b}")
        print("Recommendations:")
        for r in recs:
            print(f"  - {r}")
        print("\nNext: fill templates/risk-classification-note.md if documenting.")

    return 0


if __name__ == "__main__":
    sys.exit(main())














