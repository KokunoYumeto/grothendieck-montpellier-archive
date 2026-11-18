"""Check the corrected pages of block MPL_148_029-072_148-029-148-043: brace balance and changed-line counts."""
import io
import difflib

BASE = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110"
SRC = BASE + "/returns/MPL_148_029-072_unzipped/pages/"
OUT = BASE + "/second_pass/out/MPL_148_029-072/"

for n in range(29, 44):
    f = "MPL_148_029-072_148_scan%03d.tex" % n
    a = io.open(SRC + f, encoding="utf-8").read()
    b = io.open(OUT + f, encoding="utf-8").read()
    depth = 0
    neg = False
    i = 0
    while i < len(b):
        c = b[i]
        if c == "\\":
            i += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth < 0:
                neg = True
        i += 1
    changed = sum(1 for d in difflib.ndiff(a.splitlines(), b.splitlines()) if d.startswith("+ "))
    print("scan %03d: changed lines %d, brace depth %d%s" % (n, changed, depth, " NEGATIVE" if neg else ""))
