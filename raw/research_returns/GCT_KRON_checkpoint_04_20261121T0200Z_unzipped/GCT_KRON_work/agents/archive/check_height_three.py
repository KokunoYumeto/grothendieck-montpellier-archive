#!/usr/bin/env python3
"""Exact cross-checks for A-026; the all-h theorem is proved in the TeX file."""
from datetime import datetime, timezone
from pathlib import Path
import importlib.util
import json

BASE = Path(__file__).resolve().parent
WORK = BASE.parents[1]
spec = importlib.util.spec_from_file_location(
    "gct_height_three_characters", WORK/"computations/independent_characters.py")
characters = importlib.util.module_from_spec(spec)
spec.loader.exec_module(characters)


def positive_count(h):
    return sum(1 for c in range(h//4+1)
               for b in range((h-4*c)//3+1)
               if (h-4*c-3*b) % 2 == 0)


def closed(h):
    return ((h*h+12*h+48)//48 if h % 2 == 0
            else (h*h+6*h+21)//48)


def main():
    character_checks = []
    for h in range(7):
        rectangle = (h, h, h) if h else ()
        actual = characters.kronecker(rectangle, rectangle, rectangle)
        count = positive_count(h)
        assert actual == count == closed(h)
        character_checks.append({"h": h, "rectangle": rectangle,
                                 "character_value": actual, "positive_count": count})
    arithmetic_checks = []
    for h in range(241):
        count = positive_count(h)
        assert count == closed(h)
        arithmetic_checks.append({"h": h, "value": count})
    result = {
        "finding": "A-026", "run": "GCT_KRON_20261120",
        "model": "GPT-6 Astra Pro", "effort": "not exposed",
        "date_utc": datetime.now(timezone.utc).isoformat(),
        "source": "Domokos-Drensky arXiv1101.3178v1 Section2 Theorem1 and Remark2(ii), printedp6; degrees p4-p5",
        "method": "Exact Murnaghan-Nakayama engine in computations/independent_characters.py, compared independently with nonnegative solution count and closed expression",
        "character_checks": character_checks,
        "arithmetic_checks": arithmetic_checks,
        "scope": "Finite computations check conventions; the proof for every h is the cited polynomial invariant ring plus Schur-Weyl and the written residue calculation",
        "status": "PASS",
    }
    out = BASE/"HEIGHT_THREE_CERTIFICATE.json"
    tmp = out.with_suffix(".tmp")
    tmp.write_text(json.dumps(result, indent=2)+"\n")
    tmp.replace(out)
    print("PASS seven exact character checks through S18 and241 positive-count/closed-form checks")


if __name__ == "__main__":
    main()
