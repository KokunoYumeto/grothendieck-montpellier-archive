import sys, re, csv
sys.path.insert(0, r"C:/Users/user/Documents/results_register/horizontal/sweep2/_tools_a28ea31f")
import hsweep2 as H
pkg, lo, hi = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
cap = int(sys.argv[4]) if len(sys.argv) > 4 else 10**6
h, rows = H.rtsv(H.S2 / "SA15/PLACEMENT.tsv")
item = {r[0]: r[7].split("-")[1] for r in rows}
for e in H.gap("SA15"):
    if not e["entry_id"].startswith(pkg):
        continue
    n = int(e["entry_id"].rsplit("#", 1)[1])
    if not lo <= n <= hi:
        continue
    t = H.body(e)
    t = re.sub(r"\*\*Kind:\s*([^*]*)\*\*", lambda m: "[" + m.group(1).strip().rstrip(".") + "]", t)
    t = re.sub(r"Location/topic:|Manuscript anchor:|Post-freeze comparison:", "|", t)
    t = re.sub(r"[#*`>]", "", t)
    m = re.search(r"Cote (\d+), scans? (\d+)", e["heading"])
    cs = f"{m.group(1)}:{int(m.group(2))}" if m else e["heading"][:12]
    w = H.clean(t).split()
    print(f"{n}|{cs}|{item.get(e['entry_id'],'?')}| {' '.join(w[:cap])}{' …' if len(w) > cap else ''}")
