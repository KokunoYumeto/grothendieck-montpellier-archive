"""Candidate fleet lemmas for every item of the intake pile: tf-idf cosine similarity between each item (statement and
why-interesting) and each fleet lemma (title, plain and formal statement), plus explicit fleet ids named in the item.
Writes PILE_CANDIDATES.tsv (one row per item and candidate) beside this script and prints the score distribution.
Candidate retrieval only: every link is judged by reading both statements.
usage: python -I -B pile_candidates.py [TOPK=6]
Written 24 Nov 2026 by Claude Opus 5.5 at effort max (session 672ae3a0)."""
import collections, csv, json, math, pathlib, re, sys

sys.stdout.reconfigure(encoding="utf-8")
csv.field_size_limit(10 ** 7)
HERE = pathlib.Path(__file__).resolve().parent
PILE = pathlib.Path("<local>/Documents/reports_20261124/INTAKE_PILE_20261124")
TOPK = int(sys.argv[1]) if len(sys.argv) > 1 else 6
IDRX = re.compile(r"\bL-(?:gct|meta|clb|pcx|lib|alg)-\d{3,4}\b")
STOP = set("""the and for with that this from are has have its into all any each one two three not but which where when
then than there their they them these those such some every only also over under more most less least other same both
between within without upon via can may must will would should could does done being been were was is be of in on at to by
an as or if so no yes it we our us a let let's given show shows hence thus since because about after before up down out
new case cases holds hold true false proof proved prove theorem lemma proposition corollary statement result results
number numbers set sets map maps fixed exact exactly least most first second form forms part parts""".split())


def toks(s):
    s = s.lower()
    s = re.sub(r"[_\\{}$^()\[\],.;:'\"`|=<>+*/~!?-]", " ", s)
    return [t for t in s.split() if len(t) > 2 and t not in STOP and not t.isdigit()]


fleet = json.loads((HERE / "RESULTS.json").read_text(encoding="utf-8"))["lemmas"]
fdocs = [toks(" ".join(str(r.get(k) or "") for k in ("title", "plain_statement", "formal_statement"))) for r in fleet]
items = []
for f in sorted(PILE.glob("*_ITEMS.tsv")):
    cl = f.name[:-len("_ITEMS.tsv")]
    with open(f, encoding="utf-8", errors="replace", newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            items.append((cl, row))
idocs = [toks((r.get("statement") or "") + " " + (r.get("why_interesting") or "")) for _, r in items]

N = len(fdocs) + len(idocs)
df = collections.Counter()
for d in fdocs + idocs:
    df.update(set(d))
idf = {t: math.log(N / (1 + c)) for t, c in df.items()}


def vec(d):
    c = collections.Counter(d)
    v = {t: (1 + math.log(n)) * idf[t] for t, n in c.items()}
    norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
    return {t: x / norm for t, x in v.items()}


fv = [vec(d) for d in fdocs]
inv = collections.defaultdict(list)
for j, v in enumerate(fv):
    for t, x in v.items():
        inv[t].append((j, x))

out = HERE / "PILE_CANDIDATES.tsv"
best = collections.defaultdict(list)
with open(out, "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["cluster", "run", "item_id", "rank", "score", "fleet_id", "fleet_status", "fleet_title", "named_in_item",
                "item_statement"])
    for (cl, row), d in zip(items, idocs):
        iv = vec(d)
        sc = collections.Counter()
        for t, x in iv.items():
            for j, y in inv.get(t, ()):
                sc[j] += x * y
        named = set(IDRX.findall((row.get("statement") or "") + " " + (row.get("why_interesting") or "") + " " +
                                 (row.get("locator") or "")))
        top = sc.most_common(TOPK)
        ids_top = {fleet[j]["id"] for j, _ in top}
        for k, (j, s) in enumerate(top, 1):
            r = fleet[j]
            w.writerow([cl, row.get("run"), row.get("item_id"), k, f"{s:.3f}", r["id"], r.get("status"), r.get("title"),
                        "yes" if r["id"] in named else "", " ".join((row.get("statement") or "").split())[:400]])
        for lid in sorted(named - ids_top):
            r = next((x for x in fleet if x["id"] == lid), {})
            w.writerow([cl, row.get("run"), row.get("item_id"), "named", "", lid, r.get("status"), r.get("title"), "yes",
                        " ".join((row.get("statement") or "").split())[:400]])
        best[cl].append(top[0][1] if top else 0.0)
print(f"items {len(items)} | fleet lemmas {len(fleet)} | written {out.name}")
for cl, v in sorted(best.items()):
    v = sorted(v, reverse=True)
    print(f"{cl:16s} n={len(v):3d}  top-score max {v[0]:.2f}  >=0.30: {sum(x >= 0.30 for x in v):3d}  >=0.20: "
          f"{sum(x >= 0.20 for x in v):3d}  >=0.15: {sum(x >= 0.15 for x in v):3d}")
