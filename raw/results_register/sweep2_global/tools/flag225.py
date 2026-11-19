"""Sweep 2: what each of sweep 0's 225 'dependency names no id of the run' flags resolves to.
Claude Opus 5.5 at effort max, 18 Nov 2026. Writes FLAG225_RESOLUTION.tsv."""
import sys, re, csv, collections
sys.path.insert(0, r"C:\Users\user\Documents\results_register\sweep2_global\tools")
import core

OUT = core.OUT
F = [f for f in csv.DictReader(open(core.RR / "FLAGS.tsv", encoding="utf-8"), delimiter="\t") if f["flag"].startswith("dependency names no id")]
E = collections.defaultdict(list)
for e in csv.DictReader(open(OUT / "GRAPH_EDGES.tsv", encoding="utf-8"), delimiter="\t"):
    if e["field"] == "depends_on":
        E[e["from"]].append(e)
U = collections.defaultdict(list)
for u in csv.DictReader(open(OUT / "UNRESOLVED.tsv", encoding="utf-8"), delimiter="\t"):
    if u["field"] == "depends_on":
        U[u["tag"]].append(u)
rows, cnt = [], collections.Counter()
for f in F:
    tag = f["tag"]
    toks = [t.strip() for t in f["detail"].split(",") if t.strip()]
    edges = E.get(tag, [])
    for tok in toks:
        hit = None
        for e in edges:
            ev = e["evidence"]
            if re.search(r"(?<![A-Za-z0-9.])" + re.escape(tok) + r"(?![0-9])", ev):
                if e["kind"] == "uses" and e["to"].split(":")[0] != tag.split(":")[0]:
                    hit = ("another run's id", e["to"], e["how"]); break
                if e["kind"] == "uses" and "read as" in e["how"]:
                    hit = ("a part of the run's own row", e["to"], e["how"]); break
                if e["kind"] == "cites literature":
                    hit = ("literature locator", e["to"][:120], ""); break
                if e["kind"] == "uses computation":
                    hit = ("computation", e["to"][:120], ""); break
                if e["kind"] == "answers prompt item":
                    hit = ("prompt item", e["to"], ""); break
        own = tag.split(":", 1)[1]
        if not hit and tok.startswith(own + "."):
            hit = ("a part of the row itself (its own sub-item)", tag, "")
        if not hit:
            u = next((u for u in U.get(tag, []) if tok in u["fragment"] or tok in u["evidence"]), None)
            if u:
                hit = ("unresolved: " + u["class"], u["fragment"][:120], u["how"][:80])
            else:
                hit = ("literature locator (section number of a cited work)" if re.fullmatch(r"[IVX]+\.?\d.*|[A-Z]{1,3}\d+(\.\d+)+", tok) else "not matched", "", "")
        cnt[hit[0]] += 1
        rows.append(dict(tag=tag, token=tok, resolves_to=hit[0], target=hit[1], how=hit[2]))
with open(OUT / "FLAG225_RESOLUTION.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter="\t", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print(len(F), "flags,", len(rows), "tokens")
for k, v in cnt.most_common():
    print(f"  {k}\t{v}")
