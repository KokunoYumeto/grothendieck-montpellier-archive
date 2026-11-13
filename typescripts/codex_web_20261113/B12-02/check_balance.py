#!/usr/bin/env python3
"""Static source checks only. This script does not invoke TeX."""
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parent
ORDER = [102, 117, 121, 123, 126, 128, 130, 132, 134, 136, 138]


def escaped(text, i):
    n = 0
    while i and text[i - 1] == "\\":
        n += 1
        i -= 1
    return n % 2 == 1


def uncomment(text):
    return "\n".join(
        line[:next((i for i, c in enumerate(line)
                   if c == "%" and not escaped(line, i)), len(line))]
        for line in text.splitlines()
    )


def check(path):
    text = uncomment(path.read_text(encoding="utf-8"))
    braces = []
    math = None
    inline_pairs = displays = 0
    errors = []
    i = 0
    while i < len(text):
        c = text[i]
        line = text.count("\n", 0, i) + 1
        if c in "{}" and not escaped(text, i):
            if c == "{":
                braces.append(line)
            elif braces:
                braces.pop()
            else:
                errors.append(f"unmatched closing brace, line {line}")
        if c == "$" and not escaped(text, i):
            if math is None:
                math = ("inline", line)
            elif math[0] == "inline":
                math = None
                inline_pairs += 1
            else:
                errors.append(f"dollar inside display, line {line}")
        if c == "\\" and not escaped(text, i) and i + 1 < len(text):
            if text[i + 1] == "[":
                if math is not None:
                    errors.append(f"nested display opening, line {line}")
                math = ("display", line)
                i += 1
            elif text[i + 1] == "]":
                if math is None or math[0] != "display":
                    errors.append(f"unmatched display closing, line {line}")
                else:
                    displays += 1
                math = None
                i += 1
        i += 1
    if braces:
        errors.append(f"unclosed braces starting on lines {braces}")
    if math is not None:
        errors.append(f"unclosed {math[0]} math starting on line {math[1]}")
    env_stack = []
    env_count = 0
    for m in re.finditer(r"(?<!\\)\\(begin|end)\{([^{}]+)\}", text):
        action, env = m.groups()
        if action == "begin":
            env_stack.append(env)
            env_count += 1
        elif not env_stack or env_stack[-1] != env:
            errors.append(f"mismatched environment end {env}")
        else:
            env_stack.pop()
    if env_stack:
        errors.append(f"unclosed environments {env_stack}")
    status = "PASS" if not errors else "FAIL"
    message = (f"{path.relative_to(ROOT)}: {status}; braces balanced; "
               f"inline math pairs={inline_pairs}; displays={displays}; "
               f"environment pairs={env_count}")
    return errors, message


def main():
    pages = [ROOT / "pages" / f"B12-02_12_scan{n}.tex" for n in ORDER]
    fragment = ROOT / "B12-02_transcription.tex"
    files = pages + [fragment, ROOT / "B12-02_standalone.tex"]
    report = ["STATIC BALANCE CHECK — no compilation", ""]
    all_errors = []
    for path in files:
        errors, message = check(path)
        report.append(message)
        report.extend(errors)
        all_errors.extend(errors)
    assembled = fragment.read_text()
    expected = "\n\n".join(p.read_text().rstrip() for p in pages) + "\n"
    assert assembled == expected, "assembled fragment differs from page files"
    assert assembled.startswith("\\cotefile{12}\n\\scanpage{102}")
    assert assembled.count("\\cotefile{") == 1
    assert [int(x) for x in re.findall(r"\\scanpage\{(\d+)\}", assembled)] == ORDER
    assert not re.search(r"\\(?:newcommand|renewcommand|def)\b", assembled)
    with (ROOT / "B12-02_inventory.csv").open(newline="") as f:
        reader = csv.DictReader(f)
        assert reader.fieldnames == ["cote", "scan", "sheet_kind", "hand", "element",
                                    "kind", "position", "first_words_or_objects", "transcribed"]
        rows = list(reader)
    assert all(r["transcribed"] == "yes" for r in rows)
    assert {int(r["scan"]) for r in rows} == set(ORDER)
    assert len({r["element"] for r in rows}) == len(rows)
    report += ["", "Assembly/order/single cote marker: PASS",
               f"Inventory: PASS; {len(rows)} unique elements; all transcribed=yes",
               "No new notation macros in the transcription: PASS", ""]
    for macro in ("unsure", "illegible", "deleted"):
        count = len(re.findall(r"\\" + macro + r"\s*\{", assembled))
        report.append(f"\\{macro} marks in the assembled transcription: {count}")
    report.append("\nOverall result: " + ("FAIL" if all_errors else "PASS"))
    result = "\n".join(report) + "\n"
    (ROOT / "B12-02_balance.txt").write_text(result)
    print(result)
    return bool(all_errors)


if __name__ == "__main__":
    raise SystemExit(main())
