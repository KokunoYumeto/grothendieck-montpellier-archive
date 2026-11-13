#!/usr/bin/env python3
"""Check source delimiter balance; this does not compile or validate readings."""
from pathlib import Path
import re
import sys


def without_comments(source):
    lines = []
    for line in source.splitlines(keepends=True):
        for i, char in enumerate(line):
            if char != "%":
                continue
            backslashes = 0
            j = i - 1
            while j >= 0 and line[j] == "\\":
                backslashes += 1
                j -= 1
            if backslashes % 2 == 0:
                line = line[:i] + ("\n" if line.endswith("\n") else "")
                break
        lines.append(line)
    return "".join(lines)


def check(path):
    source = without_comments(path.read_text(encoding="utf-8"))
    braces, environments, errors = [], [], []
    math = None
    for match in re.finditer(r"\\[A-Za-z@]+|\\[^\n]|\$\$|[${}]", source):
        token = match.group()
        line = source.count("\n", 0, match.start()) + 1
        if token == "{":
            braces.append(line)
        elif token == "}":
            if braces:
                braces.pop()
            else:
                errors.append(f"line {line}: unmatched closing brace")
        elif token in (r"\begin", r"\end"):
            name = re.match(r"\s*\{([^{}]+)\}", source[match.end():])
            if not name:
                errors.append(f"line {line}: missing environment name")
                continue
            name = name.group(1)
            if token == r"\begin":
                environments.append((name, line))
            elif not environments or environments[-1][0] != name:
                errors.append(f"line {line}: unmatched end of {name}")
            else:
                environments.pop()
        elif token in ("$", "$$"):
            if math is None:
                math = (token, line)
            elif math[0] == token:
                math = None
            else:
                errors.append(f"line {line}: {token} inside {math[0]} math")
        elif token in (r"\[", r"\("):
            if math is not None:
                errors.append(f"line {line}: nested math opening {token}")
            else:
                math = (token, line)
        elif token in (r"\]", r"\)"):
            opening = {r"\]": r"\[", r"\)": r"\("}[token]
            if math is None or math[0] != opening:
                errors.append(f"line {line}: unmatched {token}")
            else:
                math = None
    errors.extend(f"line {line}: unclosed brace" for line in braces)
    errors.extend(f"line {line}: unclosed {name} environment" for name, line in environments)
    if math is not None:
        errors.append(f"line {math[1]}: unclosed {math[0]} math")
    return errors


def main():
    root = Path(__file__).resolve().parent
    paths = sorted((root / "pages").glob("C29-03_29_scan*.tex"))
    paths += [root / "C29-03_transcription.tex", root / "C29-03_standalone.tex"]
    failed = False
    for path in paths:
        errors = check(path)
        print(f"{'FAIL' if errors else 'PASS'} {path.relative_to(root)}")
        for error in errors:
            print(f"  {error}")
        failed |= bool(errors)
    print("No compilation performed. This check covers literal delimiters and environment nesting only.")
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
