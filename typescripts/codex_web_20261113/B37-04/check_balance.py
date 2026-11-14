#!/usr/bin/env python3
"""Check the delivered LaTeX delimiters without compiling or changing readings."""
from pathlib import Path
import csv
import hashlib
import json
import re
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
SCANS = [69, 70, 71, 72, 74, 85, 86, 87, 88]
TOKEN = re.compile(r"\\begin\{([^{}]+)\}|\\end\{([^{}]+)\}|\\\[|\\\]|\\[A-Za-z@]+|\\.|[{}$]")


def strip_comments(text):
    result = []
    for line in text.splitlines(keepends=True):
        for i, char in enumerate(line):
            if char == "%":
                j = i - 1
                while j >= 0 and line[j] == "\\":
                    j -= 1
                if (i - 1 - j) % 2 == 0:
                    line = line[:i] + "\n"
                    break
        result.append(line)
    return "".join(result)


def check(path):
    text = strip_comments(path.read_text())
    braces, envs, math, errors = [], [], None, []
    for match in TOKEN.finditer(text):
        token = match.group()
        line = text.count("\n", 0, match.start()) + 1
        if match.group(1):
            envs.append((match.group(1), line))
        elif match.group(2):
            name = match.group(2)
            if not envs or envs[-1][0] != name:
                errors.append(f"line {line}: unmatched end {name}")
            else:
                envs.pop()
        elif token == "{":
            braces.append(line)
        elif token == "}":
            if braces:
                braces.pop()
            else:
                errors.append(f"line {line}: unmatched closing brace")
        elif token == r"\[":
            if math is not None:
                errors.append(f"line {line}: display starts inside {math}")
            math = ("display", line)
        elif token == r"\]":
            if math is None or math[0] != "display":
                errors.append(f"line {line}: unmatched display end")
            math = None
        elif token == "$":
            if math is None:
                math = ("inline", line)
            elif math[0] == "inline":
                math = None
            else:
                errors.append(f"line {line}: inline dollar inside display")
    if braces:
        errors.append(f"unclosed braces starting on lines {braces}")
    if envs:
        errors.append(f"unclosed environments {envs}")
    if math:
        errors.append(f"unclosed math delimiter {math}")
    return {
        "file": str(path.relative_to(ROOT)),
        "balanced": not errors,
        "errors": errors,
        "marks": {name: len(re.findall(r"\\" + name + r"\s*\{", text))
                  for name in ("unsure", "illegible", "deleted")},
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def main():
    pages = [ROOT / "pages" / f"B37-04_37_scan{scan:03d}.tex" for scan in SCANS]
    assembled = ROOT / "B37-04_transcription.tex"
    results = [check(path) for path in pages + [assembled, ROOT / "B37-04_standalone.tex"]]
    fragment = assembled.read_text()
    assert fragment == "".join(path.read_text() for path in pages), "assembly differs"
    assert re.findall(r"\\scanpage\{(\d+)\}", fragment) == [str(n) for n in SCANS]
    assert fragment.startswith("\\cotefile{37}\n\\scanpage{69}")
    assert len(re.findall(r"\\cotefile\{", fragment)) == 1
    with (ROOT / "B37-04_inventory.csv").open(newline="") as handle:
        inventory = list(csv.DictReader(handle))
    assert all(row["transcribed"] == "yes" for row in inventory)
    assert set(int(row["scan"]) for row in inventory) == set(SCANS)
    assert all(row["kind"] in {"text", "letter part", "display", "diagram", "drawing",
                              "margin note", "insertion", "deletion", "handwritten"}
               for row in inventory)
    assert all(row["hand"] in {"typed", "Grothendieck", "other hand", "unknown"}
               for row in inventory)
    report = {
        "checked_utc": datetime.now(timezone.utc).isoformat(),
        "compiled": False,
        "scope": "Delimiter balance, exact concatenation/order, inventory completeness flags; not a compilation test.",
        "all_balanced": all(item["balanced"] for item in results),
        "inventory_rows": len(inventory),
        "marks_in_assembled_transcription": results[-2]["marks"],
        "files": results,
    }
    (ROOT / "B37-04_balance_check.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k != "files"}, indent=2))
    for result in results:
        print(result["file"], "PASS" if result["balanced"] else result["errors"])
    raise SystemExit(0 if report["all_balanced"] else 1)


if __name__ == "__main__":
    main()
