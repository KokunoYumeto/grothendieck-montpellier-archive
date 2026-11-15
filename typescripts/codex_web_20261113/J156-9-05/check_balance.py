#!/usr/bin/env python3
"""Lexical delimiter check only; does not invoke or emulate a TeX compiler."""
from pathlib import Path
import re
import sys


def check(path):
    source = path.read_text(encoding="utf-8")
    braces, displays, envs, dollars, errors = [], [], [], [], []
    pairs = dict(braces=0, displays=0, environments=0)
    i, line = 0, 1
    while i < len(source):
        char = source[i]
        if char == "%":
            end = source.find("\n", i)
            i = len(source) if end < 0 else end
            continue
        if char == "\\":
            word = re.match(r"[A-Za-z]+", source[i + 1:])
            if word:
                command = word.group()
                after = i + 1 + len(command)
                if command in ("begin", "end"):
                    match = re.match(r"\s*\{([^{}]+)\}", source[after:])
                    if not match:
                        errors.append(f"line {line}: malformed {command}")
                    elif command == "begin":
                        envs.append((match.group(1), line))
                    elif not envs or envs[-1][0] != match.group(1):
                        errors.append(f"line {line}: unmatched end {match.group(1)}")
                    else:
                        envs.pop()
                        pairs["environments"] += 1
                i = after
                continue
            if i + 1 < len(source):
                symbol = source[i + 1]
                if symbol == "[":
                    displays.append(line)
                elif symbol == "]":
                    if displays:
                        displays.pop()
                        pairs["displays"] += 1
                    else:
                        errors.append(f"line {line}: unmatched display close")
                if symbol == "\n":
                    line += 1
                i += 2  # Escaped braces, dollars, percent signs and backslashes.
                continue
        elif char == "{":
            braces.append(line)
        elif char == "}":
            if braces:
                braces.pop()
                pairs["braces"] += 1
            else:
                errors.append(f"line {line}: unmatched closing brace")
        elif char == "$":
            dollars.append(line)
        if char == "\n":
            line += 1
        i += 1
    if braces:
        errors.append(f"unclosed braces at lines {braces}")
    if displays:
        errors.append(f"unclosed displays at lines {displays}")
    if envs:
        errors.append(f"unclosed environments: {envs}")
    if len(dollars) % 2:
        errors.append(f"odd number of unescaped dollar signs: {len(dollars)}")
    pairs["dollar_pairs"] = len(dollars) // 2
    return errors, pairs


def main():
    root = Path(__file__).resolve().parent
    paths = [Path(arg) for arg in sys.argv[1:]] or [
        *sorted((root / "pages").glob("*.tex")),
        root / "J156-9-05_transcription.tex",
        root / "J156-9-05_standalone.tex",
        root / "PREAMBLE.tex",
    ]
    failed = False
    print("Lexical balance check: braces, display delimiters, dollar pairs, environments.")
    print("Comments and escaped symbols ignored. No compilation attempted.")
    print("Ordinary parentheses are source content and are not repaired or checked.")
    for path in paths:
        errors, pairs = check(path)
        failed |= bool(errors)
        print(f"{'FAIL' if errors else 'PASS'} {path.name}: {pairs}")
        for error in errors:
            print(f"  {error}")
    print("RESULT: " + ("FAIL" if failed else "PASS"))
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
