import sys; sys.path.insert(0, r"C:\Users\user\Documents\results_register\sweep2_global\tools")
from load import *
rows = load_register()
seen = {}
for r in rows:
    if r["run"] not in seen: seen[r["run"]] = (r["results"], r["ret"])
for run, (res, ret) in sorted(seen.items()):
    if run < "S6_06": continue
    p = DOC / res
    if not p.exists():
        print(run, "MISSING", res); 
        # look for the folder
        q = DOC / ret
        print("   ret exists:", q.exists())
        continue
    with open(p, encoding="utf-8-sig", newline="") as f:
        hdr = next(csv.reader(f))
    print(run, "|", ret)
    print("    cols:", hdr)
