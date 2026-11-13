#!/usr/bin/env python3
"""Lexical balance checks only; does not invoke a TeX engine."""
from pathlib import Path
import re
import sys


def check(path):
    source = path.read_text(encoding="utf-8")
    braces, environments = [], []
    math = None
    errors = []
    counts = {"brace_pairs": 0, "inline_pairs": 0, "display_pairs": 0,
              "environment_pairs": 0}
    i = 0
    while i < len(source):
        char = source[i]
        if char == "%":
            end = source.find("\n", i)
            i = len(source) if end < 0 else end + 1
            continue
        if char == "\\":
            match = re.match(r"\\(begin|end)\{([^{}]+)\}", source[i:])
            if match:
                action, name = match.groups()
                if action == "begin":
                    environments.append(name)
                elif not environments or environments.pop() != name:
                    errors.append(f"mismatched environment {name} at {i}")
                else:
                    counts["environment_pairs"] += 1
                i += len(match.group())
                continue
            nxt = source[i + 1:i + 2]
            if nxt == "[":
                if math is not None:
                    errors.append(f"nested display at {i}")
                math = "display"
            elif nxt == "]":
                if math != "display":
                    errors.append(f"unmatched display close at {i}")
                math = None
                counts["display_pairs"] += 1
            # Consume a control symbol or the full control word, so escaped
            # braces, dollars and percent signs do not act as delimiters.
            command = re.match(r"\\(?:[A-Za-z]+|[^\n])", source[i:])
            i += len(command.group()) if command else 1
            continue
        if char == "{":
            braces.append(i)
        elif char == "}":
            if not braces:
                errors.append(f"unmatched closing brace at {i}")
            else:
                braces.pop()
                counts["brace_pairs"] += 1
        elif char == "$":
            if math == "display":
                errors.append(f"dollar inside display at {i}")
            elif math == "inline":
                math = None
                counts["inline_pairs"] += 1
            else:
                math = "inline"
        i += 1
    if braces:
        errors.append(f"{len(braces)} unclosed braces")
    if environments:
        errors.append(f"unclosed environments: {environments}")
    if math:
        errors.append(f"unclosed {math} math")
    return errors, counts


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    paths = sorted((root / "pages").glob("*.tex"))
    paths += [root / "C29-05_transcription.tex", root / "C29-05_standalone.tex"]
    failed = False
    for path in paths:
        errors, counts = check(path)
        failed |= bool(errors)
        print(f"{path.relative_to(root)}: {'FAIL' if errors else 'PASS'}; {counts}")
        for error in errors:
            print(f"  {error}")
    print("No TeX compilation attempted. These are lexical delimiter checks only.")
    sys.exit(1 if failed else 0)
