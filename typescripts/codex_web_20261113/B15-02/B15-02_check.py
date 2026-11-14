"""Static delimiter checks only; never invokes a TeX engine."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent

def uncomment(text):
    return re.sub(r"(?<!\\)%[^\n]*", "", text)

def check(path):
    text = uncomment(path.read_text(encoding="utf-8"))
    errors, braces, envs, math = [], [], [], None
    token = re.compile(r"\\begin\{([^}]+)\}|\\end\{([^}]+)\}|\\\[|\\\]|\\\(|\\\)|\\[A-Za-z]+|\\.|\$\$|\$|[{}]", re.S)
    for m in token.finditer(text):
        t = m.group()
        line = text.count("\n", 0, m.start()) + 1
        if m.group(1):
            envs.append((m.group(1), line))
        elif m.group(2):
            if not envs or envs[-1][0] != m.group(2):
                errors.append(f"line {line}: unmatched environment end {m.group(2)}")
            else:
                envs.pop()
        elif t == "{":
            braces.append(line)
        elif t == "}":
            if braces:
                braces.pop()
            else:
                errors.append(f"line {line}: unmatched closing brace")
        elif t in (r"\[", r"\("):
            if math is not None:
                errors.append(f"line {line}: nested math delimiter {t}")
            math = (t, line)
        elif t in (r"\]", r"\)"):
            expected = r"\[" if t == r"\]" else r"\("
            if math is None or math[0] != expected:
                errors.append(f"line {line}: unmatched math closer {t}")
            math = None
        elif t in ("$", "$$"):
            if math is None:
                math = (t, line)
            elif math[0] == t:
                math = None
            else:
                errors.append(f"line {line}: mismatched dollar delimiter {t}")
    if braces:
        errors.append(f"unclosed braces at lines {braces}")
    if envs:
        errors.append(f"unclosed environments {envs}")
    if math:
        errors.append(f"unclosed math delimiter {math}")
    return errors

if __name__ == "__main__":
    files = sorted((ROOT / "pages").glob("*.tex"))
    files += [ROOT / "B15-02_transcription.tex", ROOT / "B15-02_standalone.tex"]
    failures = 0
    for path in files:
        errors = check(path)
        failures += bool(errors)
        print(f"{path.relative_to(ROOT)}: " + ("PASS" if not errors else "FAIL: " + "; ".join(errors)))
    print("No compilation performed. Ordinary source parentheses are not repaired by this checker.")
    sys.exit(bool(failures))
