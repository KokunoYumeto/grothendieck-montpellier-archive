#!/usr/bin/env python3
"""Lexical balance check only; does not invoke a TeX compiler."""
from pathlib import Path
import re
import sys


def check(path):
    source = path.read_text(encoding="utf-8")
    source = re.sub(r"(?<!\\)%[^\n]*", "", source)
    braces, displays, environments, dollars, errors = [], [], [], [], []
    tokens = re.finditer(r"\\(?:begin|end)\{[^{}]+\}|\\\[|\\\]|\\.|[{}$]", source)
    for match in tokens:
        token = match.group()
        line = source.count("\n", 0, match.start()) + 1
        if token.startswith("\\begin{"):
            environments.append((token[7:-1], line))
        elif token.startswith("\\end{"):
            name = token[5:-1]
            if not environments or environments[-1][0] != name:
                errors.append(f"L{line}: unmatched end {name}")
            else:
                environments.pop()
        elif token == "{":
            braces.append(line)
        elif token == "}":
            if braces:
                braces.pop()
            else:
                errors.append(f"L{line}: unmatched closing brace")
        elif token == "\\[":
            if displays:
                errors.append(f"L{line}: nested display opener")
            displays.append(line)
        elif token == "\\]":
            if displays:
                displays.pop()
            else:
                errors.append(f"L{line}: unmatched display closer")
        elif token == "$":
            if dollars:
                dollars.pop()
            else:
                dollars.append(line)
    errors.extend(f"L{line}: unclosed brace" for line in braces)
    errors.extend(f"L{line}: unclosed display" for line in displays)
    errors.extend(f"L{line}: unpaired dollar" for line in dollars)
    errors.extend(f"L{line}: unclosed environment {name}" for name, line in environments)
    return errors


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    paths = sorted((root / "pages").glob("*.tex"))
    paths += [root / "J156-8-06_transcription.tex", root / "J156-8-06_standalone.tex"]
    failed = False
    for path in paths:
        errors = check(path)
        print(f"{path.relative_to(root)}: {'FAIL' if errors else 'PASS'}")
        for error in errors:
            print("  " + error)
        failed |= bool(errors)
    print("Checks: braces, display delimiters, dollar pairs, environment nesting. No compilation.")
    sys.exit(int(failed))
