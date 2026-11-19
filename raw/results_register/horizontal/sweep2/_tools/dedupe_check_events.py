"""Sweep 2: the sweep2/SA<nn>/CHECK_EVENTS.tsv files began as copies of sweep 1's. build_check_register.py merges every
CHECK_EVENTS*.tsv under results_register without removing duplicates, so the rows copied from sweep 1 come out of the
sweep-2 files and only sweep 2's own events stay (broad agent a0c4bb37, Claude Opus 5.5 at effort max, 18 Nov 2026).
usage: python -I -B dedupe_check_events.py SA01 SA02 ...   (only topics whose agents have finished)"""
import sys, pathlib, csv, io, re

H = pathlib.Path(r"C:\Users\user\Documents\results_register\horizontal")
tot = 0
for t in sys.argv[1:]:
    f1, f2 = H / "sweep1" / t / "CHECK_EVENTS.tsv", H / "sweep2" / t / "CHECK_EVENTS.tsv"
    if not f2.exists():
        continue
    lines = f2.read_text(encoding="utf-8").splitlines()
    norm = lambda ln: tuple(re.sub(r"\s+", " ", x).strip() for x in next(csv.reader(io.StringIO(ln), delimiter="	")))
    old = {norm(ln) for ln in f1.read_text(encoding="utf-8").splitlines()[1:] if ln.strip()} if f1.exists() else set()
    keep, seen = [lines[0]], set()
    for ln in lines[1:]:  # drop rows copied from sweep 1, and rows written twice in sweep 2
        if ln.strip() and norm(ln) not in old and norm(ln) not in seen:
            keep.append(ln)
            seen.add(norm(ln))
    removed = len(lines) - len(keep)
    tot += removed
    f2.write_text("\n".join(keep) + "\n", encoding="utf-8")
    print(t, "removed", removed, "kept", len(keep) - 1)
print("removed in all", tot)
