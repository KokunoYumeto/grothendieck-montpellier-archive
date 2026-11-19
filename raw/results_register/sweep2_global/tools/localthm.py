import sys, re, csv, collections
sys.path.insert(0, r"C:\Users\user\Documents\results_register\sweep2_global\tools")
import core
ex = core.load_extra()
pat = re.compile(r"OpenAI\s*Local|OpenAILocal|OpenAI2026|p-adic section conjecture|local section theorem|stipulated local|Tool\s*\(1\)|local theorem|OpenAI, \*?The p-adic", re.I)
hits = []
for r in core.ROWS:
    blob = " ".join((r["statement"], r["depends_on"], r["notes"], r["where_proved"]))
    e = ex.get(r["tag"], {})
    ul = next((v for k, v in e.items() if k.startswith("uses_local_theorem")), "")
    m = pat.search(blob)
    uses_yes = ul.strip().lower().startswith("yes")
    d5x = re.search(r"\bD\.5[46]\b", r["depends_on"]) and r["run"] == "LM8_PUSH"
    if m or uses_yes or d5x:
        hits.append((r["tag"], r["status"], (m.group(0) if m else ("uses_local_theorem: " + ul[:60] if uses_yes else "D.54/D.56")), r["statement"][:120]))
c = collections.Counter((t.split(":")[0], s) for t, s, _, _ in hits)
print(len(hits)); print(sorted(c.items()))
with open(core.OUT / "tools" / "local_theorem_rows.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["tag", "status", "trigger", "statement"]); w.writerows(hits)
for h in hits[:12]: print(h)
