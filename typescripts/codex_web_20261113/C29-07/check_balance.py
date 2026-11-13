"""Lexical checks only; deliberately does not compile or repair readings."""
from pathlib import Path
import re


def uncomment(text):
    return re.sub(r"(?<!\\)%[^\n]*", "", text)


def check(path):
    text = uncomment(path.read_text(encoding="utf-8"))
    braces = []
    environments = []
    mode = None
    errors = []
    tokens = re.finditer(
        r"\\(?:begin|end)\{[^}]+\}|\\\[|\\\]|\\.|[{}$]", text
    )
    for match in tokens:
        token = match.group()
        line = text.count("\n", 0, match.start()) + 1
        if token == "{":
            braces.append(line)
        elif token == "}":
            if braces:
                braces.pop()
            else:
                errors.append(f"line {line}: unmatched closing brace")
        elif token.startswith(r"\begin{"):
            environments.append((token[7:-1], line))
        elif token.startswith(r"\end{"):
            name = token[5:-1]
            if not environments or environments[-1][0] != name:
                errors.append(f"line {line}: unmatched environment end {name}")
            else:
                environments.pop()
        elif token == r"\[":
            if mode is not None:
                errors.append(f"line {line}: display opens in {mode} mode")
            mode = "display"
        elif token == r"\]":
            if mode != "display":
                errors.append(f"line {line}: unmatched display close")
            mode = None
        elif token == "$":
            if mode == "display":
                errors.append(f"line {line}: dollar inside display")
            mode = None if mode == "inline" else "inline"
    if braces:
        errors.append(f"unclosed braces from lines {braces}")
    if environments:
        errors.append(f"unclosed environments {environments}")
    if mode:
        errors.append(f"unclosed {mode} math")
    return errors


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    paths = sorted((root / "pages").glob("*.tex"))
    paths += [root / "C29-07_transcription.tex", root / "C29-07_standalone.tex"]
    failed = False
    for path in paths:
        errors = check(path)
        failed |= bool(errors)
        print(f"{path.relative_to(root)}: {'FAIL' if errors else 'PASS'}")
        for error in errors:
            print("  " + error)
    raise SystemExit(1 if failed else 0)
