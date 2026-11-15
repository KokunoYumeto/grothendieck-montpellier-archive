#!/usr/bin/env python3
"""Lexical LaTeX balance checks only. This script never compiles TeX."""
from pathlib import Path
import json
import re


def check(path):
    source = path.read_text(encoding="utf-8")
    errors, braces, displays, environments = [], [], [], []
    dollar = None
    i, line = 0, 1
    while i < len(source):
        c = source[i]
        if c == "\n":
            line += 1
            i += 1
            continue
        if c == "%":
            end = source.find("\n", i)
            i = len(source) if end < 0 else end
            continue
        if c == "\\":
            env = re.match(r"\\(begin|end)\{([^{}]+)\}", source[i:])
            if env:
                action, name = env.groups()
                if action == "begin":
                    environments.append((name, line))
                elif not environments or environments[-1][0] != name:
                    errors.append(f"line {line}: unmatched end {name}")
                else:
                    environments.pop()
                i += env.end()
                continue
            nxt = source[i + 1:i + 2]
            if nxt == "[":
                if displays or dollar is not None:
                    errors.append(f"line {line}: display opens in math")
                displays.append(line)
            elif nxt == "]":
                if not displays:
                    errors.append(f"line {line}: unmatched display close")
                else:
                    displays.pop()
            if nxt and (not nxt.isalpha()):
                i += 2
            else:
                command = re.match(r"\\[A-Za-z]+", source[i:])
                i += command.end() if command else 1
            continue
        if c == "{":
            braces.append(line)
        elif c == "}":
            if not braces:
                errors.append(f"line {line}: unmatched closing brace")
            else:
                braces.pop()
        elif c == "$":
            if displays:
                errors.append(f"line {line}: dollar inside display")
            dollar = line if dollar is None else None
        i += 1
    errors += [f"line {n}: unclosed brace" for n in braces]
    errors += [f"line {n}: unclosed display" for n in displays]
    errors += [f"line {n}: unclosed environment {e}" for e, n in environments]
    if dollar is not None:
        errors.append(f"line {dollar}: unpaired dollar")
    return {"file": str(path.relative_to(Path(__file__).parent)),
            "balanced": not errors, "errors": errors}


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    paths = sorted((root / "pages").glob("*.tex"))
    paths += [root / "J156-8-14_transcription.tex", root / "J156-8-14_standalone.tex"]
    results = [check(p) for p in paths]
    report = {"method": "Lexical checks; no TeX engine invoked",
              "checks": ["braces", "display delimiters", "inline dollars", "environment nesting"],
              "passed": all(r["balanced"] for r in results), "files": results}
    (root / "J156-8-14_balance.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["passed"] else 1)
