"""Structural checks only. Does not run TeX or modify the transcription."""
from pathlib import Path
import re
import json

ROOT = Path(__file__).resolve().parent

def check(path):
    text = path.read_text(encoding="utf-8")
    stack, envs, maths, errors = [], [], [], []
    line, i = 1, 0
    while i < len(text):
        c = text[i]
        if c == "%":
            j = text.find("\n", i)
            i = len(text) if j < 0 else j
            continue
        if c == "\n":
            line += 1
        if c == "\\":
            m = re.match(r"\\(begin|end)\{([^}]+)\}", text[i:])
            if m:
                typ, name = m.groups()
                if typ == "begin":
                    envs.append((name, line))
                elif not envs or envs[-1][0] != name:
                    errors.append(f"line {line}: unexpected end of {name}")
                else:
                    envs.pop()
                i += len(m.group())
                continue
            if i + 1 < len(text) and text[i+1] in "[]()":
                t = text[i+1]
                if t in "[(":
                    maths.append((t, line))
                elif not maths or maths[-1][0] != {']':'[', ')':'('}[t]:
                    errors.append(f"line {line}: unmatched math delimiter {t}")
                else:
                    maths.pop()
                i += 2
                continue
            m = re.match(r"\\[A-Za-z]+|\\.", text[i:], re.S)
            if m:
                i += len(m.group())
                continue
        elif c == "{":
            stack.append(line)
        elif c == "}":
            if stack:
                stack.pop()
            else:
                errors.append(f"line {line}: extra closing brace")
        elif c == "$":
            if maths and maths[-1][0] == "$":
                maths.pop()
            else:
                maths.append(("$", line))
        i += 1
    errors.extend(f"line {n}: unclosed brace" for n in stack)
    errors.extend(f"line {n}: unclosed environment {s}" for s, n in envs)
    errors.extend(f"line {n}: unclosed math delimiter {s}" for s, n in maths)
    return errors

if __name__ == "__main__":
    pages = sorted((ROOT / "pages").glob("*.tex"))
    files = pages + [ROOT / "K70-06_transcription.tex", ROOT / "K70-06_standalone.tex"]
    report = {str(p.relative_to(ROOT)): check(p) for p in files}
    body = (ROOT / "K70-06_transcription.tex").read_text()
    assert body == "\n".join(p.read_text().rstrip() for p in pages) + "\n"
    assert re.findall(r"\\scanpage\{(\d+)\}", body) == [str(i) for i in range(83, 97)]
    assert body.startswith("\\cotefile{70}\n\\scanpage{83}")
    assert body.count("\\cotefile{") == 1
    assert "\\includegraphics" not in body
    assert not re.search(r"\\(?:newcommand|renewcommand|def|documentclass)\b", body)
    counts = {name: len(re.findall(r"\\" + name + r"\b", body))
              for name in ("unsure", "illegible", "deleted")}
    result = {"balance_passed": not any(report.values()), "files": report,
              "marks_in_assembled_fragment_only": counts,
              "pages": list(range(83, 97)), "compiled": False}
    (ROOT / "K70-06_validation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["balance_passed"] else 1)
