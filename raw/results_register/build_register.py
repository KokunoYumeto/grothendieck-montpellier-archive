"""Sweep 0: the register of all our results, by script (18 Nov 2026).

The user, 18 Nov 2026 (P6848): "Stack ... all the math that we have, notes, etc., passes over it, checking, organizing ...
internal consistency checks, like making a sort of like the tags, see what depends on what. Basically, just like go
organize." The structure it feeds: grothendieck_archive_montpellier/HANDBOOK_SKETCH_20261118.md (sweep 0).

Reads (never writes) each research run's newest results table (found by field_experts/build_check_ledger.find_returns:
the run's final, else its highest checkpoint), the CHECK_EVENTS.tsv files of that return, and field_experts/
check_ledger.jsonl (which documents name which statement ids). Writes, in results_register/:
- REGISTER.tsv: one row per statement: draft tag RUN:ID, run, line, id, status, statement, where proved, the ids it
  uses, his places, check events by type, check documents by kind, lineage (other runs' ids it names), the return.
- EDGES.tsv: uses edges (within a run and across runs) and lineage edges.
- FLAGS.tsv: what a script can see is wrong or thin: a proved item that uses a refuted one; a dependency that names no
  known id; the same statement with two statuses in two runs; a proved item with no check event and no check document.
- SUMMARY.md: counts per line and run, and the flags by kind.
No model is used. Written and run by the main session (Claude Opus 5.5 Max).
usage: python -I -B results_register/build_register.py"""
import collections
import csv
import hashlib
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
csv.field_size_limit(10 ** 9)
DOC = pathlib.Path(r"C:\Users\user\Documents")
OUT = DOC / "results_register"
sys.path.insert(0, str(DOC / "field_experts"))
import build_check_ledger as B  # noqa: E402

STATUS_KEYS = ("Proved", "Refuted", "Known", "Open", "Conditional", "Unresolved")


def norm_status(s):
    s = (s or "").strip()
    if not s:
        return "?"
    w = s.split()[0].strip(".,;:()")
    syn = {"false": "Refuted", "undecided": "Open", "verified": "Proved", "computed": "Proved"}
    if w.lower() in syn:
        return syn[w.lower()]
    return next((k for k in STATUS_KEYS if w.lower().startswith(k.lower())), w[:20])


def norm_text(s):
    s = re.sub(r"\\[a-zA-Z]+\*?", " ", s or "")
    s = re.sub(r"[^0-9a-zA-Z]+", " ", s).lower()
    return re.sub(r"\s+", " ", s).strip()


def one_line(s, n=None):
    s = re.sub(r"\s+", " ", (s or "").replace("\t", " ")).strip()
    return s if n is None else s[:n]


# 1. the newest results table of each run
rets = B.find_returns()
best = {}
for r in rets:
    if not r["results"]:
        continue
    rank = (1 if r["kind"] == "final" else 0, r["num"] or 0, r["stamp"])
    if r["run"] not in best or rank > best[r["run"]][0]:
        best[r["run"]] = (rank, r)
runs = sorted(best)
run_alt = {}  # names a run goes by in other runs' text
for run in runs:
    run_alt[run] = run
    base = re.sub(r"_(SUCCESSOR|PUSH|FINAL)$", "", run)
    run_alt.setdefault(base, run)

items = {}  # tag -> row
order = []
for run in runs:
    _, r = best[run]
    path = DOC / r["results"]
    with open(path, encoding="utf-8-sig", newline="") as fh:
        rd = csv.DictReader(fh)
        cols = rd.fieldnames or []
        man_col = next((c for c in cols if c.startswith("manuscript")), None)
        for row in rd:
            rid = (row.get("id") or "").strip()
            if not rid:
                continue
            tag = f"{run}:{rid}"
            if tag in items:
                tag = f"{tag}#{sum(1 for t in items if t.startswith(tag))+1}"
            items[tag] = dict(
                tag=tag, run=run, line=r["programme"], id=rid, status=norm_status(row.get("status")),
                status_raw=one_line(row.get("status"), 120), statement=one_line(row.get("statement")),
                where_proved=one_line(row.get("where_proved"), 300), depends_on=one_line(row.get("depends_on"), 500),
                his_places=one_line(row.get(man_col), 300) if man_col else "", notes=one_line(row.get("notes"), 400),
                ret=r["folder"], ret_kind=r["kind"], ret_num=r["num"] or "", stamp=r["stamp"], results=r["results"])
            order.append(tag)

ids_by_run = collections.defaultdict(set)
for t, it in items.items():
    ids_by_run[it["run"]].add(it["id"])

# 2. uses and lineage
edges = []
ID_TOKEN = re.compile(r"[A-Za-z]{0,4}\d*[A-Za-z]?\.?\d+(?:\.\d+)*[a-z]?|[A-Z]{1,4}\d+(?:\.\d+)*")
run_names = sorted(run_alt, key=len, reverse=True)
CROSS = re.compile(r"\b(" + "|".join(re.escape(n) for n in run_names) + r")\b[\s:]*\(?([A-Za-z]{0,4}\d*[A-Za-z]?\.?\d+(?:\.\d+)*[a-z]?)")
dangling = collections.defaultdict(list)
for t, it in items.items():
    uses, lin = [], []
    for tok in re.split(r"[,;/]|\band\b|\s+", it["depends_on"]):
        tok = tok.strip(" .()[]{}")
        if not tok or tok.lower() in ("none", "-", "n/a", "na", "nothing"):
            continue
        if tok in ids_by_run[it["run"]] and tok != it["id"]:
            uses.append(f"{it['run']}:{tok}")
        elif re.fullmatch(r"[A-Z]{1,3}\d*\.\d+(?:\.\d+)*", tok) and tok not in ids_by_run[it["run"]]:
            dangling[t].append(tok)
    blob = " ".join((it["statement"], it["notes"], it["depends_on"], it["where_proved"]))
    for m in CROSS.finditer(blob):
        other = run_alt.get(m.group(1))
        oid = m.group(2)
        if other and other != it["run"] and oid in ids_by_run[other]:
            lin.append(f"{other}:{oid}")
    it["uses"] = sorted(set(uses))
    it["lineage"] = sorted(set(lin))
    for u in it["uses"]:
        edges.append((t, "uses", u))
    for l in it["lineage"]:
        edges.append((t, "names", l))

# 3. check events of each run's newest return
ev = collections.defaultdict(collections.Counter)
for run in runs:
    _, r = best[run]
    folder = DOC / r["folder"]
    files = []
    for depth in range(0, 4):
        files += list(folder.glob("/".join(["*"] * depth + ["CHECK_EVENTS*.tsv"])))
    for f in files:
        try:
            with open(f, encoding="utf-8-sig", newline="") as fh:
                rd = csv.reader(fh, delimiter="\t")
                head = next(rd, [])
                hl = [h.strip().lower() for h in head]
                i_id = next((i for i, h in enumerate(hl) if "statement" in h or h == "id"), 0)
                i_ty = next((i for i, h in enumerate(hl) if h.startswith("type")), None)
                for row in rd:
                    if len(row) <= i_id:
                        continue
                    sid = row[i_id].strip()
                    ty = row[i_ty].strip()[:40] if i_ty is not None and len(row) > i_ty else "?"
                    ev[f"{run}:{sid}"][ty or "?"] += 1
        except (OSError, StopIteration):
            pass
# 4. check documents (intakes, experts, referees, notes) naming the statement
docs = collections.defaultdict(collections.Counter)
for line in open(DOC / "field_experts" / "check_ledger.jsonl", encoding="utf-8"):
    d = json.loads(line)
    run = run_alt.get(d.get("run", ""), d.get("run", ""))
    for sid in d.get("statements", []):
        docs[f"{run}:{sid}"][d.get("kind", "?")] += 1

# 5. flags
flags = []
for t, it in items.items():
    e = ev.get(t, collections.Counter())
    dk = docs.get(t, collections.Counter())
    it["check_events"] = sum(e.values())
    it["check_types"] = "; ".join(f"{k}:{v}" for k, v in e.most_common())
    it["check_docs"] = sum(dk.values())
    it["check_doc_kinds"] = "; ".join(f"{k}:{v}" for k, v in dk.most_common())
    if it["status"] == "Proved":
        bad = [u for u in it["uses"] if items.get(u, {}).get("status") == "Refuted"]
        if bad:
            flags.append(("proved item cites a refuted row (check it uses the refutation, not the claim)", t, ", ".join(bad)))
        if it["check_events"] == 0 and it["check_docs"] == 0:
            flags.append(("proved; no check recorded in our files (check events exist only since 17 Nov)", t, ""))
    if dangling.get(t):
        flags.append(("dependency names no id of the run", t, ", ".join(dangling[t][:8])))
groups = collections.defaultdict(list)
for t, it in items.items():
    k = norm_text(it["statement"])
    if len(k) >= 60:
        groups[hashlib.sha1(k.encode()).hexdigest()[:10]].append(t)
for g, ts in groups.items():
    rr = {items[t]["run"] for t in ts}
    ss = {items[t]["status"] for t in ts}
    for t in ts:
        items[t]["same_statement"] = g if len(ts) > 1 else ""
    if len(rr) > 1 and len(ss) > 1:
        flags.append(("same statement, different statuses in different runs", ts[0],
                      "; ".join(f"{x} {items[x]['status']}" for x in ts)))

# 6. write
OUT.mkdir(exist_ok=True)
cols = ["tag", "run", "line", "id", "status", "status_raw", "statement", "where_proved", "depends_on", "uses", "lineage",
        "his_places", "check_events", "check_types", "check_docs", "check_doc_kinds", "same_statement", "notes", "ret",
        "ret_kind", "ret_num", "stamp", "results"]
with open(OUT / "REGISTER.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(cols)
    for t in order:
        it = items[t]
        w.writerow([", ".join(it[c]) if isinstance(it.get(c), list) else it.get(c, "") for c in cols])
with open(OUT / "EDGES.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["from", "kind", "to"])
    w.writerows(edges)
with open(OUT / "FLAGS.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["flag", "tag", "detail"])
    w.writerows(flags)

by_line = collections.defaultdict(collections.Counter)
by_run = collections.defaultdict(collections.Counter)
for it in items.values():
    by_line[it["line"]][it["status"]] += 1
    by_run[it["run"]][it["status"]] += 1
fl = collections.Counter(f[0] for f in flags)
lines = ["# The register of our results: sweep 0 (by script)", "",
         f"{len(items)} statements from {len(runs)} runs (each run's newest results table); {len(edges)} edges; "
         f"{len(flags)} flags. Built by `results_register/build_register.py`; no model was used. Draft tags are RUN:ID.", "",
         "## By line", "", "| Line | Statements | By status |", "|---|---|---|"]
for ln, c in sorted(by_line.items()):
    lines.append(f"| {ln} | {sum(c.values())} | " + ", ".join(f"{k} {v}" for k, v in c.most_common()) + " |")
lines += ["", "## Flags", "", "| Flag | Count |", "|---|---|"]
lines += [f"| {k} | {v} |" for k, v in fl.most_common()]
lines += ["", "## By run (newest return)", "", "| Run | Line | Return | Statements | By status | Check events | Named in check documents |",
          "|---|---|---|---|---|---|---|"]
for run in runs:
    _, r = best[run]
    its = [it for it in items.values() if it["run"] == run]
    lines.append(f"| {run} | {r['programme']} | {r['kind']} {r['num'] or ''} ({r['stamp']}) | {len(its)} | "
                 + ", ".join(f"{k} {v}" for k, v in by_run[run].most_common()) + f" | "
                 f"{sum(it['check_events'] for it in its)} | {sum(1 for it in its if it['check_docs'])} |")
(OUT / "SUMMARY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"{len(items)} statements, {len(runs)} runs, {len(edges)} edges, flags: {dict(fl)}")
