import csv, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
T = r"C:\Users\user\Documents\results_register\horizontal\sweep3\SA20\INTAKE_RESEARCH_SA20_20261121_full_CHECK_EVENTS.tsv"
rows = list(csv.reader(open(T, encoding="utf-8"), delimiter="\t"))[1:]
def lvl(t):
    t = t.lower()
    if t.startswith("statement read only"): return 0
    if t.startswith("carried as background"): return 1
    if t.startswith("used and rechecked"): return 2
    if t.startswith("refuted"): return 5
    if t.startswith("independent re-proof"): return 4
    if t.startswith("computation"): return 4
    return 3
best = {}; bestt = {}
for r in rows:
    l = lvl(r[3])
    if l >= best.get(r[0], -1): best[r[0]] = l; bestt[r[0]] = r[3]
names = {0: "statement read only", 1: "background", 2: "used and rechecked", 3: "targeted (incl. partial)", 4: "re-proof or computation", 5: "refuted"}
c = collections.Counter(best.values())
print("events:", len(rows), "ids:", len(best))
for k in sorted(c): print(names[k], c[k])
part = [i for i in best if best[i] == 3 and "partial" in bestt[i]]
print("targeted partial:", len(part), sorted(part))
print("statement only:", sorted(i for i in best if best[i] == 0))
print("background:", sorted(i for i in best if best[i] == 1))
print("used:", sorted(i for i in best if best[i] == 2))
print("reproof/computation:", sorted(i for i in best if best[i] == 4))
