import sys; sys.path.insert(0, r"C:\Users\user\Documents\results_register\sweep2_global\tools")
import core, random, collections
random.seed(3)
by = collections.defaultdict(list)
for r in core.ROWS:
    if r["his_places"].strip() and r["his_places"].strip().lower() not in ("none", "-", "n/a", "none."):
        by[r["run"]].append(r["his_places"])
for run, xs in sorted(by.items()):
    print("==", run, len(xs), "distinct", len(set(xs)))
    for x in random.sample(sorted(set(xs)), min(4, len(set(xs)))): print("    ", x[:170])
