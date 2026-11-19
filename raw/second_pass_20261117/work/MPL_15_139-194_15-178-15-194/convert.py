"""Convert a Work (K15-06/K15-07) page to this package's conventions, with exact reading changes.
Usage: python -I -B convert.py <work_page.tex> <out.tex> [<old> <new> <count>]...  (count = expected occurrences)"""
import sys, re
sys.stdout.reconfigure(encoding="utf-8")
src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding="utf-8").read()
reps = sys.argv[3:]
for i in range(0, len(reps), 3):
    old, new, cnt = reps[i], reps[i + 1], int(reps[i + 2])
    c = t.count(old)
    assert c == cnt, (old, c, cnt)
    t = t.replace(old, new)
m = re.search(r"% archive sheet number: (\d+)", t)
sheet = m.group(1) if m else None
t = re.sub(r"(?m)^%[^\n]*\n", "", t)
t = t.replace(r"\cotefile{15}", "")
for L in "ZQRCF":
    t = t.replace(r"\mathbb{" + L + "}", r"\mathbf " + L)
t = t.replace(r"\mathrm{G}_m", "G_m")
t = t.rstrip("\n") + "\n"
if sheet:
    t += r"\margin{" + sheet + "}\n"
open(dst, "w", encoding="utf-8", newline="\n").write(t)
print("ok", dst, "sheet", sheet)
