#!/usr/bin/env python3
"""Static delimiter checks only; never invokes a TeX compiler."""
from pathlib import Path
import re


def without_comments(text):
    lines = []
    for line in text.splitlines():
        for i, char in enumerate(line):
            if char == "%":
                preceding = len(line[:i]) - len(line[:i].rstrip("\\"))
                if preceding % 2 == 0:
                    line = line[:i]
                    break
        lines.append(line)
    return "\n".join(lines)


def check(path):
    text = without_comments(path.read_text())
    errors, braces, displays, envs = [], [], [], []
    dollars = 0
    display_pairs = 0
    environment_pairs = 0
    i = 0
    while i < len(text):
        char = text[i]
        line = text.count("\n", 0, i) + 1
        if char == "\\":
            token = re.match(r"\\(begin|end)\{([^}]+)\}", text[i:])
            if token:
                direction, name = token.groups()
                if direction == "begin":
                    envs.append((name, line))
                elif not envs or envs[-1][0] != name:
                    errors.append(f"line {line}: unmatched end {name}")
                else:
                    envs.pop()
                    environment_pairs += 1
            if text[i:i + 2] == "\\[":
                displays.append(line)
                i += 2
                continue
            if text[i:i + 2] == "\\]":
                if not displays:
                    errors.append(f"line {line}: unmatched display close")
                else:
                    displays.pop()
                    display_pairs += 1
                i += 2
                continue
            if i + 1 < len(text) and not text[i + 1].isalpha():
                i += 2
                continue
        elif char == "{":
            braces.append(line)
        elif char == "}":
            if braces:
                braces.pop()
            else:
                errors.append(f"line {line}: unmatched closing brace")
        elif char == "$":
            dollars += 1
        i += 1
    if braces:
        errors.append(f"unclosed braces from lines {braces}")
    if displays:
        errors.append(f"unclosed displays from lines {displays}")
    if envs:
        errors.append(f"unclosed environments {envs}")
    if dollars % 2:
        errors.append("odd number of unescaped dollar signs")
    detail = (f"{dollars // 2} dollar pairs; {display_pairs} display pairs; "
              f"{environment_pairs} environment pairs")
    return errors, detail


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    files = sorted((root / "pages").glob("*.tex"))
    files += [root / "J156-7-10_transcription.tex",
              root / "J156-7-10_standalone.tex", root / "PREAMBLE.tex"]
    failed = False
    for path in files:
        errors, detail = check(path)
        failed |= bool(errors)
        status = "; ".join(errors) if errors else "PASS"
        print(f"{path.relative_to(root)}: {status}; {detail}")
    print("Static balance only. No compilation or rendering was attempted.")
    raise SystemExit(1 if failed else 0)
