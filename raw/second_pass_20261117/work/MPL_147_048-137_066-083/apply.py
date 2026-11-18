"""Apply the second-pass replacements for MPL_147_048-137 scans 066-083 and write the corrected files once."""
import os
import re
import sys

ROOT = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110"
SRC = ROOT + "/returns/MPL_147_048-137_unzipped/pages"
DST = ROOT + "/second_pass/out/MPL_147_048-137"


def braces(t):
    t = re.sub(r"\\[{}]", "", t)
    return t.count("{"), t.count("}")


def main():
    spec = open(sys.argv[1], encoding="utf-8").read()
    blocks = re.findall(r"@@@ (\d{3})\n<<<\n(.*?)\n===\n(.*?)\n>>>", spec, re.S)
    by_scan = {}
    for scan, old, new in blocks:
        by_scan.setdefault(scan, []).append((old, new))
    out = {}
    total = 0
    for n in range(66, 84):
        s = "%03d" % n
        fn = "MPL_147_048-137_scan%s.tex" % s
        with open(os.path.join(SRC, fn), encoding="utf-8", newline="") as f:
            txt = f.read()
        nl = "\r\n" if "\r\n" in txt else "\n"
        before = braces(txt)
        for old, new in by_scan.get(s, []):
            old = old.replace("\n", nl)
            new = new.replace("\n", nl)
            c = txt.count(old)
            if c != 1:
                raise SystemExit("scan %s: %d matches for %r" % (s, c, old))
            txt = txt.replace(old, new)
            total += 1
        after = braces(txt)
        if after[0] != after[1]:
            raise SystemExit("scan %s: unbalanced braces %r (before %r)" % (s, after, before))
        out[fn] = (txt, len(by_scan.get(s, [])))
    os.makedirs(DST, exist_ok=True)
    for fn, (txt, k) in out.items():
        p = os.path.join(DST, fn)
        if os.path.exists(p):
            raise SystemExit("refusing to overwrite " + p)
    for fn, (txt, k) in out.items():
        with open(os.path.join(DST, fn), "w", encoding="utf-8", newline="") as f:
            f.write(txt)
        print(fn, "changes:", k)
    print("blocks parsed:", len(blocks), "applied:", total)


if __name__ == "__main__":
    main()
