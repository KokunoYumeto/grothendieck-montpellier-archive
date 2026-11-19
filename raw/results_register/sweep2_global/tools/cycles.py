"""Sweep 2: what closes each dependency cycle. For every cycle: its 2-cycles, the edges that point to a later id
(a proof citing a later item), and the rows that name many others (summary rows). Claude Opus 5.5 at effort max."""
import sys, re, csv, collections
sys.path.insert(0, r"C:\Users\user\Documents\results_register\sweep2_global\tools")
import core
from core import BYTAG

OUT = core.OUT
E = list(csv.DictReader(open(OUT / "GRAPH_EDGES.tsv", encoding="utf-8"), delimiter="\t"))
C = list(csv.DictReader(open(OUT / "tools" / "analysis_cycles.tsv", encoding="utf-8"), delimiter="\t"))
uses = collections.defaultdict(dict)
for e in E:
    if e["kind"] == "uses" and e["to"] in BYTAG:
        uses[e["from"]][e["to"]] = e


def key(t):
    i = t.split(":", 1)[1]
    parts = re.findall(r"[A-Za-z]+|\d+", i)
    return [(0, int(p)) if p.isdigit() else (1, p) for p in parts]


out = []
for c in C:
    mem = set(c["members"].split())
    inner = [(a, b) for a in mem for b in uses.get(a, {}) if b in mem]
    two = sorted({tuple(sorted((a, b))) for a, b in inner if a in uses.get(b, {})})
    later = [(a, b) for a, b in inner if key(b) > key(a)]
    outdeg = collections.Counter(a for a, b in inner)
    hubs = [f"{a}({n})" for a, n in outdeg.most_common(3)]
    fields = collections.Counter(uses[a][b]["field"] for a, b in inner)
    hows = collections.Counter(uses[a][b]["how"][:30] for a, b in inner)
    ex = [f"{a}->{b} [{uses[a][b]['field']}: {uses[a][b]['evidence'][:60]}]" for a, b in later[:3]]
    out.append(dict(cycle=c["cycle"], size=c["size"], runs=c["runs"], edges=len(inner), two_cycles=len(two),
                    to_later_id=len(later), hubs=" ".join(hubs), fields=dict(fields), hows=dict(hows),
                    two_cycle_pairs=" ".join(f"{a}<->{b}" for a, b in two[:6]), later_examples=" | ".join(ex),
                    statuses=c["statuses"][:120]))
with open(OUT / "tools" / "cycles_detail.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys()), delimiter="\t", lineterminator="\n")
    w.writeheader()
    w.writerows(out)
for o in out:
    print(o["cycle"], o["size"], o["runs"][:30], "e", o["edges"], "2c", o["two_cycles"], "later", o["to_later_id"],
          "|", o["hubs"][:90], "|", o["fields"], "|", list(o["hows"].items())[:3])
