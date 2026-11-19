#!/usr/bin/env python3
"""Sweep 3.5, second step: from PROPAGATION_CANDIDATES.tsv (propagate.py) write PROPAGATION.tsv, mark the affected
study and lead entries in place (a dated line; transcriptions are never touched), list the unsent prompts that need an
update, add the S6_06_BLIND intake's links into the S6 line, and write SUMMARY.md and CHECK_EVENTS.tsv.

usage: python -I -B results_register/horizontal/sweep3_5/_tools/finalize.py [--mark]
By Claude Opus 5.5 at effort max (agent a0c4bb37), 19 Nov 2026."""
import collections
import csv
import re
import sys
import time
from pathlib import Path

csv.field_size_limit(2**31 - 1)
HERE = Path(__file__).resolve().parent
OUTD = HERE.parent
HZ = OUTD.parent
D = HZ.parents[1]
MARK = "--mark" in sys.argv
TAG = "[19 Nov 2026, sweep 3.5]"
sys.stdout.reconfigure(encoding="utf-8")


def read_tsv(p):
    with Path(p).open(encoding="utf-8-sig", errors="replace", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))


C = read_tsv(OUTD / "PROPAGATION_CANDIDATES.tsv")
WHAT = {
    ("refuted", "x"): "refutes or forces the refined statement there: the entry rests on, restates or plans work on the settled point",
    ("counterexample", "x"): "a counterexample settles the point there: the entry must take the refined statement",
    ("confirmed", "x"): "settles the point there: the entry names a statement or reading now checked",
    ("reading", "x"): "changes or fixes the reading there: the entry cites the page whose reading was decided",
}


def what(r):
    base = WHAT.get((r["source_effect"], "x"), "bears on the entry")
    if r["target_kind"] == "unsent prompt":
        return "the prompt carries the state before this result; its builder updates it: " + base.split(":")[0]
    if r["target_kind"] == "companion unit":
        return "the unit's status line takes the result: " + base.split(":")[0]
    return base


# ---------------------------------------------------------------- the S6 line: S6_06_BLIND intake -> unsent S6 prompts
S6I = D / "s6_pro_prompts_20261112_work" / "reviews" / "INTAKE_S6_06_BLIND_cp36_20261119.md"
S6ROWS = []
if S6I.is_file():
    s6 = S6I.read_text(encoding="utf-8", errors="replace").split("\n")
    sid_rx = re.compile(r"\b(S6_0\d)[ _:]?([A-Z]\.\d+(?:\.[A-Z0-9]+)*)\b")
    settled = []
    for i, ln in enumerate(s6, start=1):
        low = ln.lower()
        if not re.search(r"refut|false|fails|counterexample|proved|confirmed|holds|corrected", low):
            continue
        for a, b in sid_rx.findall(ln):
            settled.append((f"{a} {b}", i, ln))
    prompts = [p for p in sorted((D / "TO_SEND" / "PRO").glob("**/PROMPT*.md")) if "_SENT" not in p.parts and "S6" in str(p)]
    for p in prompts:
        lines = p.read_text(encoding="utf-8", errors="replace").split("\n")
        for sid, si, sl in settled:
            a, b = sid.split(" ")
            rx = re.compile(re.escape(a) + r"[ _:]?" + re.escape(b) + r"\b")
            for j, ln in enumerate(lines, start=1):
                if rx.search(ln):
                    eff = "refuted" if re.search(r"refut|false|fails|counterexample", sl.lower()) else "confirmed"
                    S6ROWS.append({"source_id": sid, "source_intake": "S6_06_BLIND cp36", "source_effect": eff,
                                   "source_text": re.sub(r"\s+", " ", sl)[:200], "target_kind": "unsent prompt",
                                   "target": p.parent.relative_to(D).as_posix(), "target_topic": "S6",
                                   "target_text": re.sub(r"\s+", " ", ln)[:200], "link": "names the settled statement",
                                   "confidence": "medium", "evidence": f"{p.relative_to(D).as_posix()}:{j}"})
seen = set()
ROWS = []
for r in C + S6ROWS:
    k = (r["source_id"], r["target"], r["evidence"])
    if k in seen:
        continue
    seen.add(k)
    r = dict(r)
    r["what_there"] = what(r)
    r["scope"] = ("prompt" if r["target_kind"] == "unsent prompt" else
                  "other topic" if r["target_topic"] and r["target_topic"] != r["source_intake"] else "same topic")
    ROWS.append(r)
ORDER = {"other topic": 0, "prompt": 1, "same topic": 2}
EFF = {"refuted": 0, "counterexample": 1, "reading": 2, "confirmed": 3}
ROWS.sort(key=lambda r: (ORDER[r["scope"]], EFF.get(r["source_effect"], 9), r["source_intake"], r["source_id"]))
cols = ["n", "source_id", "source_intake", "source_effect", "source_text", "scope", "target_kind", "target", "target_topic",
        "target_text", "what_there", "link", "confidence", "evidence"]
with (OUTD / "PROPAGATION.tsv").open("w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_NONE, escapechar="\\")
    w.writerow(cols)
    for n, r in enumerate(ROWS, start=1):
        r["n"] = n
        w.writerow([str(r.get(c, "")).replace("\t", " ") for c in cols])

# ---------------------------------------------------------------- marks in place (study and lead entries only)
marked, skipped = 0, []
if MARK:
    per = collections.defaultdict(list)
    for r in ROWS:
        if r["target_kind"] in ("study", "lead"):
            fp, _, ln = r["evidence"].rpartition(":")
            per[(fp, int(ln))].append(r)
    byfile = collections.defaultdict(dict)
    for (fp, ln), rs in per.items():
        byfile[fp][ln] = rs
    for fp, marks in byfile.items():
        p = D / fp
        if not p.is_file() or "transcription" in p.name or p.suffix != ".md":
            continue
        if time.time() - p.stat().st_mtime < 180:
            skipped.append(fp)
            continue
        lines = p.read_text(encoding="utf-8", errors="replace").split("\n")
        inserts = collections.defaultdict(list)
        for ln, rs in marks.items():
            at = ln  # after this 1-based line; a table row gets its note after the table
            while at < len(lines) and lines[at - 1].lstrip().startswith("|") and lines[at].lstrip().startswith("|"):
                at += 1
            srcs = "; ".join(f"{r['source_id'][:60]} ({r['source_intake']} intake, {r['source_effect']}; "
                             f"PROPAGATION.tsv n={r['n']})" for r in rs[:3])
            more = f"; and {len(rs) - 3} more" if len(rs) > 3 else ""
            inserts[at].append(f"> {TAG} Bears on line {ln}: {srcs}{more}. See results_register/horizontal/sweep3_5/SUMMARY.md.")
        out = []
        for i, l in enumerate(lines, start=1):
            out.append(l)
            if i in inserts:
                for note in inserts[i]:
                    nxt = lines[i] if i < len(lines) else ""
                    if TAG in nxt and note.split(":")[0] in nxt:
                        continue
                    out.append(note)
                    marked += 1
        p.write_text("\n".join(out), encoding="utf-8")

# ---------------------------------------------------------------- prompts that need an update
PR = collections.defaultdict(list)
for r in ROWS:
    if r["target_kind"] == "unsent prompt":
        PR[r["target"]].append(r)
cnt = collections.Counter(r["scope"] for r in ROWS)
print("rows", len(ROWS), dict(cnt), "S6 rows", len(S6ROWS), "marked", marked, "skipped (recently written)", skipped)
print("prompts needing an update", len(PR))
for k, rs in sorted(PR.items(), key=lambda kv: -len(kv[1]))[:12]:
    print(" ", k[-70:], len(rs), sorted({r["source_id"][:24] for r in rs})[:4])
with (OUTD / "PROMPTS_TO_UPDATE.tsv").open("w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_NONE, escapechar="\\")
    w.writerow(["prompt", "rows", "sources", "what to update", "evidence"])
    for k, rs in sorted(PR.items()):
        w.writerow([k, len(rs), "; ".join(sorted({r["source_id"][:50] for r in rs})),
                    "carry the settled results named in PROPAGATION.tsv (rows " + ", ".join(str(r["n"]) for r in rs[:12]) +
                    (" ..." if len(rs) > 12 else "") + ") in place of the earlier state",
                    "; ".join(r["evidence"] for r in rs[:6])])
