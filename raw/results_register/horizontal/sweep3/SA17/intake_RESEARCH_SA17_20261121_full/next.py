"""Print the next file of plan.tsv with ids still lacking an event, with their line numbers (resume aid)."""
import sys
tsv = "../INTAKE_RESEARCH_SA17_20261121_full_CHECK_EVENTS.tsv"
done = {l.split("\t")[0] for l in open(tsv, encoding="utf-8").read().splitlines()[1:]}
rows = [l.split("\t") for l in open("plan.tsv", encoding="utf-8").read().splitlines()]
pend = [r for r in rows if r[2] not in done]
print("pending", len(pend), "of", len(rows))
files = []
for r in pend:
    if r[0] not in files:
        files.append(r[0])
k = int(sys.argv[1]) if len(sys.argv) > 1 else 1
for f in files[:k]:
    print(f, [(r[1], r[2]) for r in pend if r[0] == f])
