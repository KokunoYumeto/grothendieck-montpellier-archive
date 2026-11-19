import sys; sys.path.insert(0, r"C:\Users\user\Documents\results_register\sweep2_global\tools")
from load import *
ex = load_extra()
print(len(ex))
cols = collections.Counter()
for t, d in ex.items():
    for k, v in d.items():
        if v.strip(): cols[(t.split(":")[0], k)] += 1
for (run, k), n in sorted(cols.items()): print(run, "|", k, "|", n)
for t in ["ANABELIAN_A1_SUCCESSOR:A.5","S6_02_PUSH:B.4.2","DELTA_ON_GT:A.24","GT_TOWER_CHECK:A.8","LM4_SUCCESSOR:A.12","SECTIONS_OVER_Q:A.24"]:
    print(t, {k:v[:150] for k,v in ex.get(t,{}).items()})
