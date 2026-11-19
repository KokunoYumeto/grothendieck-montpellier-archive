"""Sweep 2: classify the 63 cycles by cause, by script. Claude Opus 5.5 at effort max, 18 Nov 2026.
Writes CYCLES.tsv. Causes: summary row (an open, refuted or summary row lists its contributors, which cite it back);
parent and sub-item; range read by my parser; mutual pair of proved rows (to read)."""
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
ST = {t: r["status"] for t, r in BYTAG.items()}


def sccs(nodes, adj):
    index, low, onst, st, out, cnt = {}, {}, set(), [], [], [0]
    for v0 in sorted(nodes):
        if v0 in index:
            continue
        work = [(v0, iter(sorted(adj.get(v0, ()))))]
        index[v0] = low[v0] = cnt[0]; cnt[0] += 1; st.append(v0); onst.add(v0)
        while work:
            v, it = work[-1]
            n = next(it, None)
            if n is not None:
                if n not in nodes:
                    continue
                if n not in index:
                    index[n] = low[n] = cnt[0]; cnt[0] += 1; st.append(n); onst.add(n)
                    work.append((n, iter(sorted(adj.get(n, ())))))
                elif n in onst:
                    low[v] = min(low[v], index[n])
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
                        out.append(comp)
    return out


def is_summary(t):
    r = BYTAG[t]
    return ST[t] in ("Open", "Unresolved", "Refuted", "Explanatory", "?") or re.search(
        r"\b(remaining|main question|summary|we have not|not determined|undecided|task|audit of)\b", r["statement"][:200], re.I)


rows = []
for c in C:
    mem = set(c["members"].split())
    adj = {a: {b for b in uses.get(a, {}) if b in mem} for a in mem}
    hubs = [t for t in mem if is_summary(t)]
    adj2 = {a: (set() if a in hubs else adj[a]) for a in mem}
    rest = sccs(mem, adj2)
    pairs = sorted({tuple(sorted((a, b))) for a in mem for b in adj[a] if a in adj.get(b, set())})
    parent = [(a, b) for a, b in pairs if b.split(":", 1)[1].startswith(a.split(":", 1)[1] + ".") or a.split(":", 1)[1].startswith(b.split(":", 1)[1] + ".")]
    ranged = [(a, b) for a, b in pairs if re.search(r"[–-]", uses[a][b]["evidence"]) or re.search(r"[–-]", uses[b][a]["evidence"])]
    mutual_proved = [(a, b) for a, b in pairs if ST[a] == ST[b] == "Proved" and (a, b) not in parent]
    if hubs and not rest:
        cause = "summary row(s): " + " ".join(sorted(hubs)[:4]) + (" ..." if len(hubs) > 4 else "")
        closing = f"the out-edges of the {len(hubs)} summary row(s)"
    elif parent and len(mem) == 2:
        cause, closing = "parent and sub-item", f"{parent[0][0]} <-> {parent[0][1]}"
    elif hubs and rest:
        cause = f"summary row(s) {' '.join(sorted(hubs)[:3])}; after removing them {len(rest)} smaller cycle(s) of proved rows remain"
        closing = "; ".join(" ".join(sorted(x)[:4]) for x in rest[:3])
    else:
        cause = "mutual citation among proved rows (to read)"
        closing = " ".join(f"{a}<->{b}" for a, b in mutual_proved[:5])
    rows.append(dict(cycle=c["cycle"], size=c["size"], run=c["runs"], members=c["members"][:600], cause=cause,
                     closing_edges=closing[:400], two_cycles=len(pairs), two_cycles_of_proved_rows=len(mutual_proved),
                     ranged_pairs=len(ranged), statuses=c["statuses"][:200]))
with open(OUT / "CYCLES.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter="\t", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
cc = collections.Counter(r["cause"].split(":")[0].split(";")[0][:40] for r in rows)
print(cc)
for r in rows:
    if r["cause"].startswith("mutual") or "remain" in r["cause"]:
        print(r["cycle"], r["size"], r["run"][:22], "|", r["cause"][:90], "|", r["closing_edges"][:160])
