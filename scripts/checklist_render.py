#!/usr/bin/env python3
"""
Tiny helper to print the path and title of available checklists.
No assessment logic — just navigation aid.

NOT LEGAL ADVICE.
"""

from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKLISTS = ROOT / "checklists"

DISCLAIMER = "NOT LEGAL ADVICE. Orientation materials only."


def main() -> int:
    parser = argparse.ArgumentParser(description="List AIC policy checklists")
    parser.add_argument(
        "--paths-only", action="store_true", help="Print paths only"
    )
    args = parser.parse_args()

    print(DISCLAIMER)
    if not CHECKLISTS.is_dir():
        print("No checklists directory found.")
        return 1

    files = sorted(CHECKLISTS.glob("*.md"))
    if not files:
        print("No checklist files found.")
        return 1

    for f in files:
        if args.paths_only:
            print(f)
        else:
            # first non-empty line as rough title
            title = f.stem
            try:
                with f.open(encoding="utf-8") as fh:
                    for line in fh:
                        line = line.strip()
                        if line.startswith("#"):
                            title = line.lstrip("#").strip()
                            break
            except OSError:
                pass
            print(f"- {title}")
            print(f"  {f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())