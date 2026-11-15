#!/usr/bin/env python3
"""Lexical LaTeX balance checks only; does not invoke a TeX compiler."""
from pathlib import Path
import re
import sys


def check(path):
    text = path.read_text(encoding="utf-8")
    braces, displays, envs, dollars, errors = [], [], [], [], []
    i, line = 0, 1
    while i < len(text):
        c = text[i]
        if c == "\n":
            line += 1
        if c == "%":
            end = text.find("\n", i)
            i = len(text) if end < 0 else end
            continue
        if c == "\\":
            env = re.match(r"\\(begin|end)\{([^{}]+)\}", text[i:])
            if env:
                kind, name = env.groups()
                if kind == "begin":
                    envs.append((name, line))
                elif not envs or envs[-1][0] != name:
                    errors.append(f"line {line}: unmatched end of {name}")
                else:
                    envs.pop()
                i += len(env.group())
                continue
            if text[i:i+2] == r"\[":
                displays.append(line)
                i += 2
                continue
            if text[i:i+2] == r"\]":
                if displays:
                    displays.pop()
                else:
                    errors.append(f"line {line}: unmatched display close")
                i += 2
                continue
            # Escaped symbols, including literal braces, $, %, and \\.
            if i + 1 < len(text) and not text[i + 1].isalpha():
                i += 2
                continue
            command = re.match(r"\\[A-Za-z]+", text[i:])
            if command:
                i += len(command.group())
                continue
        if c == "{":
            braces.append(line)
        elif c == "}":
            if braces:
                braces.pop()
            else:
                errors.append(f"line {line}: unmatched closing brace")
        elif c == "$":
            if dollars:
                dollars.pop()
            else:
                dollars.append(line)
        i += 1
    for label, stack in (("brace", braces), ("display", displays),
                         ("environment", envs), ("dollar", dollars)):
        if stack:
            errors.append(f"unclosed {label}: {stack}")
    return errors


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    files = sorted((root / "pages").glob("*.tex"))
    files += [root / "J156-9-08_transcription.tex",
              root / "J156-9-08_standalone.tex"]
    failed = False
    for path in files:
        errors = check(path)
        failed |= bool(errors)
        print(f"{path.relative_to(root)}: {'FAIL' if errors else 'PASS'}")
        for error in errors:
            print("  " + error)
    print("Checks: braces, display delimiters, dollar delimiters, environment stack.")
    print("Ordinary parentheses/brackets are not balanced automatically: source omissions are retained.")
    print("No LaTeX compilation or rendering was performed.")
    sys.exit(1 if failed else 0)
