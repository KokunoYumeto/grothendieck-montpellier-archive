#!/usr/bin/env python3
"""Static checks only. Does not invoke TeX, OCR, or external programs."""
from pathlib import Path
import collections
import csv
import hashlib
import re

ROOT = Path(__file__).resolve().parent
PAGES = [ROOT / "pages" / f"B10-01_10_scan{s:03d}.tex" for s in range(33, 42)]

def without_comments(text):
    out = []
    i = 0
    while i < len(text):
        if text[i] == "\\" and i + 1 < len(text):
            out.extend(text[i:i+2])
            i += 2
        elif text[i] == "%":
            i = text.find("\n", i)
            if i < 0:
                break
            out.append("\n")
            i += 1
        else:
            out.append(text[i])
            i += 1
    return "".join(out)

def check(path):
    text = without_comments(path.read_text())
    braces, envs = [], []
    math_mode = None
    i = 0
    while i < len(text):
        c = text[i]
        if c == "\\":
            match = re.match(r"\\(begin|end)\{([^{}]+)\}", text[i:])
            if match:
                action, name = match.groups()
                if action == "begin":
                    envs.append(name)
                else:
                    assert envs and envs.pop() == name, (path.name, "environment mismatch", name)
                i += len(match.group())
                continue
            if i + 1 < len(text):
                symbol = text[i + 1]
                if symbol in "[(":
                    assert math_mode is None, (path.name, "nested math delimiter", i)
                    math_mode = symbol
                elif symbol in "])":
                    assert math_mode == {"]": "[", ")": "("}[symbol], (path.name, "math delimiter mismatch", i)
                    math_mode = None
                # This also skips escaped $, braces and the two backslashes of \\.
                i += 2
                continue
        elif c == "{":
            braces.append(i)
        elif c == "}":
            assert braces, (path.name, "extra closing brace", i)
            braces.pop()
        elif c == "$":
            assert math_mode in (None, "$"), (path.name, "dollar inside another math delimiter", i)
            math_mode = None if math_mode == "$" else "$"
        i += 1
    assert not braces, (path.name, "unclosed braces", braces)
    assert not envs, (path.name, "unclosed environments", envs)
    assert math_mode is None, (path.name, "unclosed math delimiter", math_mode)
    print(f"PASS {path.relative_to(ROOT)}: braces, dollars, display/inline delimiters, environments")

for page in PAGES:
    check(page)
for name in ("B10-01_transcription.tex", "B10-01_standalone.tex"):
    check(ROOT / name)

assembled = (ROOT / "B10-01_transcription.tex").read_bytes()
assert assembled == b"".join(page.read_bytes() for page in PAGES), "Assembly differs from ordered page bytes"
text = assembled.decode()
assert text.startswith("\\cotefile{10}\n\\scanpage{33}"), "Unexpected fragment start"
assert text.count("\\cotefile{") == 1
assert re.findall(r"\\scanpage\{(\d+)\}", text) == [str(s) for s in range(33, 42)]
assert "\\documentclass" not in text and "\\newcommand" not in text and "\\mathbf" not in text
with (ROOT / "B10-01_inventory.csv").open(newline="") as handle:
    reader = csv.DictReader(handle)
    assert reader.fieldnames == ["cote","scan","sheet_kind","hand","element","kind","position","first_words_or_objects","transcribed"]
    rows = list(reader)
assert all(row["transcribed"] == "yes" for row in rows)
assert set(row["scan"] for row in rows) == set(str(s) for s in range(33,42))
assert all(row["cote"] == "10" and row["sheet_kind"] == "text" for row in rows)
print("PASS exact ordered assembly, page markers, allowed fragment structure, complete inventory")
print("Inventory rows:", len(rows))
print("Marks in assembled transcription only:")
for macro in ("unsure", "illegible", "deleted"):
    print(f"  \\{macro}: {len(re.findall(chr(92)+chr(92)+macro+r'\{', text))}")
print("Compilation: not attempted.")
