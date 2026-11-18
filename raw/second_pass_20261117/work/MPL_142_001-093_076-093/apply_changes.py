"""(Block 076-093; the spec writes the backslash as U+00A4.) Apply the second-pass corrections to copies of the first-pass page files.

Reads changes_spec.txt (literal blocks, no escapes), checks that every old string
occurs exactly once in its file, writes the corrected files (LF, UTF-8) to the out
folder, then runs sanity checks: control characters, brace balance, unchanged
files byte-identical, and a unified diff for review.
"""
import difflib
import pathlib
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone

BASE = pathlib.Path(r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110")
SRC = BASE / "returns/MPL_142_001-093_unzipped/pages"
OUT = BASE / "second_pass/out/MPL_142_001-093"
SPEC = BASE / "second_pass/work/MPL_142_001-093_076-093/changes_spec.txt"
NAME = "MPL_142_001-093_scan%03d.tex"


def parse(spec_text):
    changes = defaultdict(list)
    state, cur_file, old, new = None, None, [], []
    for line in spec_text.split("\n"):
        if line.startswith("@@FILE "):
            cur_file = int(line.split()[1])
            state = None
        elif line == "@@OLD":
            state, old, new = "old", [], []
        elif line == "@@NEW":
            state = "new"
        elif line == "@@END":
            changes[cur_file].append(("\n".join(old), "\n".join(new)))
            state = None
        elif state == "old":
            old.append(line)
        elif state == "new":
            new.append(line)
    return changes


def brace_balance(t):
    t = re.sub(r"\\[{}]", "", t)
    return t.count("{") - t.count("}")


def main():
    changes = parse(SPEC.read_text(encoding="utf-8").replace(chr(164), chr(92)))
    total = 0
    errors = []
    OUT.mkdir(parents=True, exist_ok=True)
    for n in range(76, 94):
        src = SRC / (NAME % n)
        raw = src.read_bytes()
        assert b"\r" not in raw, src
        text = raw.decode("utf-8")
        orig = text
        for old, new in changes.get(n, []):
            c = text.count(old)
            if c != 1:
                errors.append("scan%03d: old string found %d times: %r" % (n, c, old))
                continue
            text = text.replace(old, new)
            total += 1
        if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", text):
            errors.append("scan%03d: control character" % n)
        if brace_balance(text) != brace_balance(orig):
            errors.append("scan%03d: brace balance changed %d -> %d" % (n, brace_balance(orig), brace_balance(text)))
        (OUT / (NAME % n)).write_bytes(text.encode("utf-8"))
        if text == orig:
            print("scan%03d: unchanged (copied)" % n)
        else:
            print("scan%03d: %d change(s)" % (n, len(changes.get(n, []))))
            for d in difflib.unified_diff(orig.split("\n"), text.split("\n"), lineterm="", n=0):
                if d.startswith(("---", "+++", "@@")):
                    continue
                print("   " + d[:400])
    print("applied:", total, "spec entries:", sum(len(v) for v in changes.values()))
    print("UTC now:", datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"))
    if errors:
        print("ERRORS:")
        for e in errors:
            print("  " + e)
        sys.exit(1)


main()
