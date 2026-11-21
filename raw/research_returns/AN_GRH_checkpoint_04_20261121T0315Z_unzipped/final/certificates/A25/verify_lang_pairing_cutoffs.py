#!/usr/bin/env python3
"""Check the finite arithmetic anchors used in the written all-prime proof."""
import json
from pathlib import Path

anchors = [
    {"condition": "primitive", "c": 1, "r": 11, "power_of_2": 15},
    {"condition": "primitive", "c": 81, "r": 17, "power_of_2": 24},
    {"condition": "signed", "c": 1, "r": 29, "power_of_2": 21},
    {"condition": "signed", "c": 81, "r": 41, "power_of_2": 30},
]
for row in anchors:
    row["left"] = row["c"] * row["r"]**4
    row["right"] = 2**row["power_of_2"]
    assert row["left"] < row["right"]
assert 13**4 < 2*11**4
result = {
    "result": "PASS",
    "scope": "Four integer anchor inequalities and the rational growth-ratio bound. The written pairing/dimension argument establishes the mathematical implication.",
    "anchors": anchors,
    "growth_ratio_bound": {"numerator": 13**4, "upper_denominator": 2*11**4},
}
out = Path(__file__).with_name("LANG_PAIRING_CUTOFF_CHECK.json")
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"result": "PASS", "output": str(out)}))
