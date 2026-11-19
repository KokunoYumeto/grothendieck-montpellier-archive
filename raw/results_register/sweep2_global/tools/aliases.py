import sys; sys.path.insert(0, r"C:\Users\user\Documents\results_register\sweep2_global\tools")
from load import *
rows = load_register()
runs = sorted({r["run"] for r in rows})
pat = re.compile(r"\b([A-Z][A-Z0-9]*(?:_[A-Z0-9]+)*)\b[\s:]*\(?([A-Z]{1,3}\.?\d+(?:\.\d+)*[a-z]?)\b")
c = collections.Counter()
ex = {}
for r in rows:
    blob = " ".join((r["statement"], r["notes"], r["depends_on"], r["where_proved"]))
    for m in pat.finditer(blob):
        w = m.group(1)
        if w in runs: continue
        if len(w) < 2: continue
        c[w] += 1
        ex.setdefault(w, (r["run"], blob[max(0,m.start()-30):m.end()+30]))
for w, n in c.most_common(120):
    print(n, w, "|", ex[w][0], "|", ex[w][1].replace("\n"," ")[:110])
