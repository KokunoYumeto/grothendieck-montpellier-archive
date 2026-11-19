"""Sweep 2: cross-run edges with the statuses at both ends; status conflicts; prompt-recorded checks.
Claude Opus 5.5 at effort max, 18 Nov 2026. Writes tools/crossrun_edges.tsv, tools/status_conflicts.tsv,
tools/prompt_checks.tsv."""
import sys, re, csv, collections, json
sys.path.insert(0, r"C:\Users\user\Documents\results_register\sweep2_global\tools")
import core
from core import BYTAG

OUT = core.OUT
E = list(csv.DictReader(open(OUT / "GRAPH_EDGES.tsv", encoding="utf-8"), delimiter="\t"))
ST = {t: r["status"] for t, r in BYTAG.items()}


def run_of(t):
    return t.split(":", 1)[0]


X = []
for e in E:
    a, b = e["from"], e["to"]
    if b in BYTAG and run_of(a) != run_of(b):
        X.append(dict(e, from_status=ST[a], to_status=ST[b], from_line=BYTAG[a]["line"], to_line=BYTAG[b]["line"]))
with open(OUT / "tools" / "crossrun_edges.tsv", "w", encoding="utf-8", newline="") as f:
    cols = ["from", "from_status", "to", "to_status", "kind", "field", "how", "from_line", "to_line", "evidence"]
    w = csv.DictWriter(f, fieldnames=cols, delimiter="\t", lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows(X)
pairs = collections.Counter((run_of(x["from"]), run_of(x["to"])) for x in X)
kinds = collections.Counter(x["kind"] for x in X)
print("cross-run edges:", len(X), dict(kinds))
print("run pairs:", len(pairs))
conf = []
for x in X:
    k, fs, ts = x["kind"], x["from_status"], x["to_status"]
    why = ""
    if k == "refutes" and ts in ("Proved", "Known"):
        why = "a row refutes another run's row that is still marked " + ts
    elif k == "corrects" and ts in ("Proved", "Known"):
        why = "a row corrects another run's row that is still marked " + ts
    elif k in ("restates", "checks") and {fs, ts} == {"Proved", "Refuted"}:
        why = f"{k}: one end Proved, the other Refuted"
    elif k in ("restates",) and fs != ts and "Open" in (fs, ts):
        why = f"restates: {fs} here, {ts} there (lineage: which status is current?)"
    elif k == "uses" and fs == "Proved" and ts in ("Open", "Unresolved", "Refuted"):
        why = f"a proved row uses another run's {ts} row"
    if why:
        conf.append(dict(x, why=why))
with open(OUT / "tools" / "status_conflicts.tsv", "w", encoding="utf-8", newline="") as f:
    cols = ["why", "from", "from_status", "to", "to_status", "kind", "field", "how", "evidence"]
    w = csv.DictWriter(f, fieldnames=cols, delimiter="\t", lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows(conf)
print("conflict candidates:", len(conf), collections.Counter(c["why"].split(" that")[0][:60] for c in conf).most_common())

# prompt-recorded checks: R-rows saying refereed / checked / followed / recomputed, with the tags they name
PR = json.load(open(OUT / "tools" / "prompt_rows.json", encoding="utf-8"))
pc = []
for run, d in PR.items():
    for key, v in d["rows"].items():
        if key.startswith("Lead") or key.startswith("L"):
            continue
        txt = v["text"]
        par = re.match(r"\s*(?:\*\*)?\s*\(((?:[^()]|\([^()]*\))*)\)", txt)
        head = par.group(1) if par else txt[:200]
        m = re.search(r"(refereed[^;.)]*|checked[^;.)]*|followed[^;.)]*|recomputed[^;.)]*|intake[^;.)]*|review[^;.)]*|"
                      r"unrefereed[^;.)]*|unread[^;.)]*|claimed Proved|false as stated[^;.)]*)", head, re.I)
        if m and v["tags"]:
            for tg in v["tags"]:
                pc.append(dict(prompt_run=run, row=key, tag=tg, tag_status=ST.get(tg, "?"), outcome=m.group(1)[:160],
                               prompt=d["prompt"]))
with open(OUT / "tools" / "prompt_checks.tsv", "w", encoding="utf-8", newline="") as f:
    cols = ["tag", "tag_status", "outcome", "prompt_run", "row", "prompt"]
    w = csv.DictWriter(f, fieldnames=cols, delimiter="\t", lineterminator="\n")
    w.writeheader()
    w.writerows(pc)
print("prompt-recorded checks:", len(pc), "on", len({p['tag'] for p in pc}), "statements")
