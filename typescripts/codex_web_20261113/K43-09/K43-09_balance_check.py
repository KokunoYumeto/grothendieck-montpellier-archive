"""Static delimiter checks only; this does not invoke a TeX engine."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent

def check(path):
    s = path.read_text(encoding="utf-8")
    braces, displays, environments = [], [], []
    dollars, errors = [], []
    i = 0
    while i < len(s):
        c = s[i]
        line = s.count("\n", 0, i) + 1
        if c == "%":
            end = s.find("\n", i)
            i = len(s) if end < 0 else end + 1
            continue
        if c == "\\":
            m = re.match(r"\\(begin|end)\{([^}]+)\}", s[i:])
            if m:
                action, name = m.groups()
                if action == "begin":
                    environments.append((name, line))
                elif not environments or environments[-1][0] != name:
                    errors.append(f"line {line}: unmatched end of {name}")
                else:
                    environments.pop()
                i += len(m.group())
                continue
            if i + 1 < len(s) and s[i + 1] in "[]()":
                token = s[i:i + 2]
                if token in (r"\[", r"\("):
                    displays.append((token, line))
                else:
                    expected = r"\[" if token == r"\]" else r"\("
                    if not displays or displays[-1][0] != expected:
                        errors.append(f"line {line}: unmatched {token}")
                    else:
                        displays.pop()
                i += 2
                continue
            m = re.match(r"\\[A-Za-z]+|\\.", s[i:], re.S)
            i += len(m.group()) if m else 1
            continue
        if c == "{":
            braces.append(line)
        elif c == "}":
            if not braces:
                errors.append(f"line {line}: unmatched closing brace")
            else:
                braces.pop()
        elif c == "$":
            dollars.append(line)
        i += 1
    if braces:
        errors.append(f"unclosed braces opened on lines {braces}")
    if displays:
        errors.append(f"unclosed math delimiters {displays}")
    if environments:
        errors.append(f"unclosed environments {environments}")
    if len(dollars) % 2:
        errors.append(f"odd number of unescaped dollars ({len(dollars)})")
    return {"file": str(path.relative_to(ROOT)), "passed": not errors,
            "dollar_pairs": len(dollars) // 2, "errors": errors}

if __name__ == "__main__":
    files = sorted((ROOT / "pages").glob("*.tex"))
    files += [ROOT / "K43-09_transcription.tex", ROOT / "K43-09_standalone.tex"]
    results = [check(p) for p in files]
    report = {"method": "Static brace, display/inline delimiter, dollar-pair and environment balance; no compilation.",
              "all_passed": all(r["passed"] for r in results), "results": results}
    (ROOT / "K43-09_balance_report.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["all_passed"] else 1)
