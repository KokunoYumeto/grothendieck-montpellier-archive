"""Sweep 2, task 3 (first pass, by script): proved rows resting on open or refuted rows, across runs; cycles.
Claude Opus 5.5 at effort max, 18 Nov 2026. Reads GRAPH_EDGES.tsv; writes tools/analysis_*.tsv."""
import sys, re, csv, collections
sys.path.insert(0, r"C:\Users\user\Documents\results_register\sweep2_global\tools")
import core
from core import ROWS, BYTAG

OUT = core.OUT
E = list(csv.DictReader(open(OUT / "GRAPH_EDGES.tsv", encoding="utf-8"), delimiter="\t"))
uses = collections.defaultdict(set)
rev = collections.defaultdict(set)
for e in E:
    if e["kind"] == "uses" and e["to"] in BYTAG:
        uses[e["from"]].add(e["to"])
        rev[e["to"]].add(e["from"])
ST = {t: r["status"] for t, r in BYTAG.items()}
COND = re.compile(r"\b(if|assum|provided|conditional|reduc|equivalent|iff|suppos|granted|would|whenever|under the hypothes|"
                  r"implies|implication|only if|criterion|exactly when|precisely when|on condition)", re.I)


def run_of(t):
    return t.split(":", 1)[0]


def downstream(t, limit=5000):
    seen, st = set(), [t]
    while st and len(seen) < limit:
        x = st.pop()
        for y in rev.get(x, ()):
            if y not in seen:
                seen.add(y)
                st.append(y)
    return seen


rows = []
for t, ts in uses.items():
    s = ST.get(t)
    if s != "Proved":
        continue
    for u in ts:
        su = ST.get(u)
        if su in ("Open", "Unresolved", "Conditional", "?", "audited", "undecided") or su == "Refuted":
            r = BYTAG[t]
            cond = bool(COND.search(r["statement"][:400]))
            cross = run_of(t) != run_of(u)
            ds = downstream(t)
            rows.append(dict(proved=t, uses=u, uses_status=su, cross_run="yes" if cross else "",
                             proved_statement_conditional="yes" if cond else "",
                             downstream_total=len(ds), downstream_cross_run=sum(1 for d in ds if run_of(d) != run_of(t)),
                             proved_statement=r["statement"][:220], used_statement=BYTAG[u]["statement"][:220]))
rows.sort(key=lambda x: (x["uses_status"] == "Refuted", x["cross_run"] != "yes", -x["downstream_total"]))
cols = list(rows[0].keys())
with open(OUT / "tools" / "analysis_proved_on_unproved.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols, delimiter="\t", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

# cycles (Tarjan, iterative)
index, low, onst, st, sccs = {}, {}, set(), [], []
counter = [0]
nodes = set(uses) | {u for v in uses.values() for u in v}


def strongconnect(v0):
    work = [(v0, iter(sorted(uses.get(v0, ()))))]
    index[v0] = low[v0] = counter[0]; counter[0] += 1
    st.append(v0); onst.add(v0)
    while work:
        v, it = work[-1]
        nxt = next(it, None)
        if nxt is not None:
            if nxt not in index:
                index[nxt] = low[nxt] = counter[0]; counter[0] += 1
                st.append(nxt); onst.add(nxt)
                work.append((nxt, iter(sorted(uses.get(nxt, ())))))
            elif nxt in onst:
                low[v] = min(low[v], index[nxt])
        else:
            work.pop()
            if work:
                low[work[-1][0]] = min(low[work[-1][0]], low[v])
            if low[v] == index[v]:
                comp = []
                while True:
                    x = st.pop(); onst.discard(x); comp.append(x)
                    if x == v:
                        break
                if len(comp) > 1:
                    sccs.append(sorted(comp))


for v in sorted(nodes):
    if v not in index:
        strongconnect(v)
with open(OUT / "tools" / "analysis_cycles.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["cycle", "size", "runs", "members", "statuses"])
    for i, c in enumerate(sorted(sccs, key=len, reverse=True)):
        w.writerow([f"CY{i+1:03d}", len(c), ",".join(sorted({run_of(x) for x in c})), " ".join(c),
                    " ".join(ST.get(x, "?") for x in c)])
cnt = collections.Counter((r["uses_status"], r["cross_run"], r["proved_statement_conditional"]) for r in rows)
print("proved rows using an unproved row:", len(rows), {k: v for k, v in sorted(cnt.items())})
print("cycles:", len(sccs), "sizes:", collections.Counter(len(c) for c in sccs).most_common(10))
print("cross-run, non-conditional, open-type targets:")
for r in rows:
    if r["cross_run"] == "yes" and r["uses_status"] != "Refuted":
        print(" ", r["proved"], "->", r["uses"], r["uses_status"], "| cond" if r["proved_statement_conditional"] else "",
              "| down", r["downstream_total"], "|", r["proved_statement"][:100])
