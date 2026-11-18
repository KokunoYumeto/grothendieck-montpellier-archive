"""Apply the second-pass corrections of block MPL_148_029-072_148-029-148-043.

Reads the first-pass page files, applies the replacements listed in changes.txt
(each with its expected number of occurrences), and writes every page of the block
(changed or not) to second_pass/out/MPL_148_029-072/ under the same file name.
"""
import io
import os
import sys

BASE = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110"
SRC = os.path.join(BASE, "returns", "MPL_148_029-072_unzipped", "pages")
OUT = os.path.join(BASE, "second_pass", "out", "MPL_148_029-072")
HERE = os.path.dirname(os.path.abspath(__file__))
SCANS = ["%03d" % n for n in range(29, 44)]


def fname(scan):
    return "MPL_148_029-072_148_scan%s.tex" % scan


def parse(path):
    text = io.open(path, encoding="utf-8").read()
    items = []
    for block in text.split("@@@ ")[1:]:
        head, rest = block.split("\n", 1)
        scan, count = head.split()
        body = rest.split("<<<\n", 1)[1].rsplit("\n>>>", 1)[0]
        old, new = body.split("\n===\n")
        items.append((scan, int(count), old, new))
    return items


def main():
    items = parse(os.path.join(HERE, "changes.txt"))
    pages = {}
    for s in SCANS:
        pages[s] = io.open(os.path.join(SRC, fname(s)), encoding="utf-8", newline="").read()
    errors = 0
    for scan, count, old, new in items:
        n = pages[scan].count(old)
        if n != count:
            print("MISMATCH scan %s: expected %d, found %d: %r" % (scan, count, n, old[:90]))
            errors += 1
            continue
        pages[scan] = pages[scan].replace(old, new)
    if errors:
        print("%d mismatches; nothing written" % errors)
        sys.exit(1)
    os.makedirs(OUT, exist_ok=True)
    for s in SCANS:
        io.open(os.path.join(OUT, fname(s)), "w", encoding="utf-8", newline="").write(pages[s])
    print("applied %d replacement blocks; wrote %d page files to %s" % (len(items), len(SCANS), OUT))


if __name__ == "__main__":
    main()
