import sys; sys.path.insert(0, r"C:\Users\user\Documents\results_register\sweep2_global\tools")
from load import *
rows = load_register()
print(len(rows))
by_run = collections.defaultdict(list)
for r in rows: by_run[r["run"]].append(r)
print("run\tn\tdep_nonempty\tuses_resolved\this_places\tlineage")
for run, rs in sorted(by_run.items()):
    dn = sum(1 for r in rs if r["depends_on"].strip() and r["depends_on"].strip().lower() not in ("none","-","n/a"))
    ur = sum(1 for r in rs if r["uses"].strip())
    hp = sum(1 for r in rs if r["his_places"].strip())
    ln = sum(1 for r in rs if r["lineage"].strip())
    print(f"{run}\t{len(rs)}\t{dn}\t{ur}\t{hp}\t{ln}")
