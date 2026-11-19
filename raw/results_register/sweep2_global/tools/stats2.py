import sys; sys.path.insert(0, r"C:\Users\user\Documents\results_register\sweep2_global\tools")
from load import *
rows = load_register()
ids = collections.defaultdict(set)
for r in rows: ids[r["run"]].add(r["id"])
by_run = collections.defaultdict(list)
for r in rows: by_run[r["run"]].append(r)
for run, rs in sorted(by_run.items()):
    samp = []
    for r in rs:
        d = r["depends_on"].strip()
        if not d or d.lower() in ("none","-","n/a"): continue
        toks = [t.strip(" .()[]{}") for t in re.split(r"[,;/]|\band\b|\s+", d)]
        toks = [t for t in toks if t]
        unres = [t for t in toks if t not in ids[run]]
        if unres:
            samp.append(d[:160])
    print(f"=== {run}: {len(samp)} rows with unresolved tokens; ids sample: {sorted(ids[run])[:6]}")
    for s in samp[:4]: print("   ", s)
