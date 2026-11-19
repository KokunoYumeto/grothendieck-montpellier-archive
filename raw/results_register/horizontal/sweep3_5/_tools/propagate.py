#!/usr/bin/env python3
"""Sweep 3.5: propagate the settled results of the six research intakes of 19 Nov 2026 (SA05, SA08, SA09, SA10, SA17,
SA21) and of the OBJ_H035 pilot verdict to every other place they bear on, through the sweep-2/3 link tables (DEPENDS,
ITEM_DEPENDS, GLOBAL_OBJECTS, CLAIM_LINKS, UNIT_LINKS), the topic studies, hunches and research packages, and the
unsent prompts in TO_SEND/PRO.

Writes sweep3_5/PROPAGATION_CANDIDATES.tsv (every link found, with its evidence). The reviewed PROPAGATION.tsv,
SUMMARY.md and CHECK_EVENTS.tsv are written from it after review.

usage: python -I -B results_register/horizontal/sweep3_5/_tools/propagate.py
By Claude Opus 5.5 at effort max (agent a0c4bb37), 19 Nov 2026."""
import collections
import csv
import re
import sys
from pathlib import Path

csv.field_size_limit(2**31 - 1)
HERE = Path(__file__).resolve().parent
OUTD = HERE.parent
HZ = OUTD.parent
D = HZ.parents[1]
S2, S3 = HZ / "sweep2", HZ / "sweep3"
G = D / "grothendieck_archive_transcription_20261110"
TOPICS = [f"SA{i:02d}" for i in range(1, 33)]


def read_tsv(p):
    p = Path(p)
    if not p.is_file():
        return []
    with p.open(encoding="utf-8-sig", errors="replace", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))


def rel(p):
    try:
        return Path(p).resolve().relative_to(D).as_posix()
    except Exception:
        return str(p)


def short(s, n=220):
    return re.sub(r"\s+", " ", s or "").strip()[:n]


# known cotes (to keep locator matching honest)
COTES = set()
for t in TOPICS:
    for r in read_tsv(S2 / t / "PLACEMENT.tsv"):
        c = (r.get("cote") or "").strip()
        if re.fullmatch(r"\d{1,3}(?:-\d{1,2})?", c):
            COTES.add(re.sub(r"^0+", "", c))
ITEM = re.compile(r"\bSA\d\d-(?:Q?\d+)[a-z]?\b")
TAG = re.compile(r"\bH0[0-9A-Z]{2}\b")
LOC1 = re.compile(r"\b(\d{1,3}(?:-\d{1,2})?)\s*,?\s*scans?\s+(\d{1,3})(?:\s*(?:-|–|and)\s*(\d{1,3}))?")
LOC2 = re.compile(r"(?<![\w.:/\[])(\d{1,3}(?:-\d{1,2})?)[:/]0*(\d{1,3})(?:[-–]0*(\d{1,3}))?(?![\w:/])")


def locs(s):
    out = set()
    for rx in (LOC1, LOC2):
        for m in rx.finditer(s or ""):
            c, a, z = m.groups()
            if rx is LOC2 and len(c.split("-")[0]) < 2 and len(m.group(0).split(":")[-1].split("/")[-1].split("-")[0]) < 2:
                continue
            c = re.sub(r"^0+", "", c)
            if c not in COTES and c.split("-")[0] not in COTES:
                continue
            a = int(a)
            z = int(z) if z else a
            if a <= z <= 400 and z - a <= 12:
                out |= {(c, x) for x in range(a, z + 1)}
    return out


def keys(s):
    return set(ITEM.findall(s or "")), set(TAG.findall(s or "")), locs(s)


# ---------------------------------------------------------------- sources: the settled results
SOURCES = []
INTAKES = {}
for t in ("SA05", "SA08", "SA09", "SA10", "SA17", "SA21"):
    cands = sorted((S3 / t).glob(f"INTAKE_RESEARCH_{t}_*CHECK_EVENTS.tsv"), key=lambda p: p.stat().st_mtime)
    if cands:
        INTAKES[t] = cands[-1]
PILOT = G / "working_through_20261118" / "PILOT_VERDICT_OBJ_H035_20261119_CHECK_EVENTS.tsv"
GO = read_tsv(S2 / "GLOBAL" / "GLOBAL_OBJECTS.tsv")
TAG_TOPICS = {(r.get("tag") or "").strip(): sorted(set(re.findall(r"SA\d\d", r.get("topics") or ""))) for r in GO}
TAG_ITEMS = {(r.get("tag") or "").strip(): set(ITEM.findall(r.get("items") or "")) for r in GO}
ITEM_TAG = {}
for tg, its in TAG_ITEMS.items():
    for it in its:
        ITEM_TAG.setdefault(it, tg)


def col(row, *names):
    for n in names:
        for k in row:
            if k and k.strip().lower() == n:
                return row.get(k) or ""
    return ""


def effect_of(typ, outcome):
    t, o = (typ or "").lower(), (outcome or "").lower()
    if "refut" in t or o.startswith("refuted") or "refuted" in o[:40]:
        return "refuted"
    if "against the" in t or "reading" in t or "ink" in o[:60]:
        return "reading"
    if "background" in t:
        return "background"
    if "counterexample" in o[:200] or " fails" in o[:200] or "false" in o[:120]:
        return "counterexample"
    return "confirmed"


for t, p in list(INTAKES.items()) + [("H035", PILOT)]:
    for r in read_tsv(p):
        sid = col(r, "id", "statement_id")
        typ = col(r, "how", "type")
        out = col(r, "result", "outcome")
        where = col(r, "where", "file")
        if not sid or sid.lower() in ("id", "statement_id"):
            continue
        eff = effect_of(typ, out)
        if eff == "background":
            continue
        blob = " ".join([sid, out, where])
        it, tg, lc = keys(blob)
        src_topics = [t] if t != "H035" else TAG_TOPICS.get("H035", [])
        SOURCES.append({"id": sid, "intake": t, "topics": src_topics, "type": typ, "effect": eff, "outcome": out,
                        "where": where, "items": it, "tags": tg | ({ITEM_TAG[x] for x in it if x in ITEM_TAG}),
                        "locs": lc, "file": rel(p)})

# the intakes' own sections on what is settled: each bullet or table row that names an item or a place
SECT = re.compile(r"main (?:question|answers)|item by item|his text|ours|settled|new results|corrections that bear", re.I)
for t in INTAKES:
    mdp = sorted((S3 / t).glob(f"INTAKE_RESEARCH_{t}_*.md"), key=lambda p: p.stat().st_mtime)
    if not mdp:
        continue
    cur = None
    for i, ln in enumerate(mdp[-1].read_text(encoding="utf-8", errors="replace").split("\n"), start=1):
        if ln.startswith("## "):
            cur = ln if SECT.search(ln) else None
            continue
        if not cur or not ln.strip():
            continue
        it, tg, lc = keys(ln)
        if not (it or lc):
            continue
        low = ln.lower()
        if re.search(r"\bfalse\b|fails|refut|counterexample|not exact|wrong", low):
            eff = "refuted"
        elif re.search(r"misread|reads |the ink|ink |reading", low):
            eff = "reading"
        elif re.search(r"proved|holds|true|confirmed|settled|correct", low):
            eff = "confirmed"
        else:
            continue
        SOURCES.append({"id": f"{t} intake {cur[3:40].strip()} l.{i}", "intake": t, "topics": [t], "type": cur[3:].strip(),
                        "effect": eff, "outcome": ln, "where": f"{rel(mdp[-1])}:{i}",
                        "items": it, "tags": tg | ({ITEM_TAG[x] for x in it if x in ITEM_TAG}), "locs": lc,
                        "file": rel(mdp[-1])})

# ---------------------------------------------------------------- targets
ROWS = []


def add(src, kind, target, ttopic, ttext, link, conf, evidence):
    ROWS.append({"source_id": src["id"], "source_intake": src["intake"], "source_effect": src["effect"],
                 "source_text": short(src["outcome"], 200), "target_kind": kind, "target": target,
                 "target_topic": ttopic, "target_text": short(ttext, 200), "link": link, "confidence": conf,
                 "evidence": evidence})


DEP_ROWS = []
for sd in (S2, S3):
    for t in TOPICS:
        for i, r in enumerate(read_tsv(sd / t / "DEPENDS.tsv"), start=2):
            DEP_ROWS.append((sd.name, t, i, r))
ITEM_DEP = read_tsv(S2 / "GLOBAL" / "INTERLINKS" / "ITEM_DEPENDS.tsv")
CLAIMS = [(t, i, r) for t in TOPICS for i, r in enumerate(read_tsv(S2 / t / "CLAIM_LINKS.tsv"), start=2)]
ULINKS = [(t, i, r) for t in TOPICS for i, r in enumerate(read_tsv(S2 / t / "UNIT_LINKS.tsv"), start=2)]
TEXTS = []
for t in TOPICS:
    for nm in ("STUDY.md", "HUNCHES.md", "RESEARCH_PACKAGES.md"):
        p = S3 / t / nm
        if p.is_file():
            TEXTS.append(("study" if nm == "STUDY.md" else "lead", t, p))
PROMPTS = []
for p in sorted((D / "TO_SEND" / "PRO").glob("**/PROMPT*.md")):
    if "_SENT" not in p.parts:
        PROMPTS.append(p)
TEXT_LINES = {}
for kind, t, p in TEXTS:
    TEXT_LINES[p] = p.read_text(encoding="utf-8", errors="replace").split("\n")
PROMPT_LINES = {p: p.read_text(encoding="utf-8", errors="replace").split("\n") for p in PROMPTS}
LINE_KEYS = {}
for p, lines in list(TEXT_LINES.items()) + list(PROMPT_LINES.items()):
    LINE_KEYS[p] = [keys(ln) for ln in lines]

for s in SOURCES:
    its, tgs, lcs = s["items"], s["tags"], s["locs"]
    own = set(s["topics"])
    for sdn, t, i, r in DEP_ROWS:
        used = (r.get("uses_item") or r.get("other") or "")
        if its & set(ITEM.findall(used)):
            add(s, "dependent item", (r.get("item") or "").strip(), t, f"{r.get('relation','')} {used}: {r.get('note','')}",
                "DEPENDS (uses the settled item)", "high", f"results_register/horizontal/{sdn}/{t}/DEPENDS.tsv:{i}")
    for r in ITEM_DEP:
        if its & set(ITEM.findall(r.get("uses") or "")):
            it = (r.get("item") or "").strip()
            add(s, "dependent item", it, it[:4], f"uses {r.get('uses','')} via {r.get('via_edges','')}",
                "ITEM_DEPENDS", "high", "results_register/horizontal/sweep2/GLOBAL/INTERLINKS/ITEM_DEPENDS.tsv")
    for tg in tgs:
        for it in sorted(TAG_ITEMS.get(tg, set()) - its):
            if it[:4] not in own:
                add(s, "same object, other topic", it, it[:4], f"object {tg}", f"GLOBAL_OBJECTS {tg}", "medium",
                    "results_register/horizontal/sweep2/GLOBAL/GLOBAL_OBJECTS.tsv")
    for t, i, r in CLAIMS:
        hit_item = its & set(ITEM.findall(r.get("item") or ""))
        hit_loc = lcs & locs(r.get("his_place") or "")
        if hit_item or hit_loc:
            add(s, "claim link", f"{r.get('claim_entry','')} -> {r.get('target','')}", t,
                f"{r.get('kind','')} {r.get('link','')}: {r.get('note','')}", "CLAIM_LINKS " + ("item" if hit_item else "place"),
                "high" if hit_item else "medium", f"results_register/horizontal/sweep2/{t}/CLAIM_LINKS.tsv:{i}")
    for t, i, r in ULINKS:
        if its & set(ITEM.findall(r.get("item") or "")):
            add(s, "companion unit", f"{r.get('unit','')} ({r.get('folder','')})", t, r.get("title", ""), "UNIT_LINKS",
                "medium", f"results_register/horizontal/sweep2/{t}/UNIT_LINKS.tsv:{i}")
    for kind, t, p in TEXTS:
        for i, (a, b, c) in enumerate(LINE_KEYS[p], start=1):
            hit = (its & a) or (lcs & c)
            if hit and not (t in own and not (lcs & c)):
                add(s, kind, f"{t} {p.name}", t, TEXT_LINES[p][i - 1], "names the settled " + ("item" if its & a else "place"),
                    "medium", f"{rel(p)}:{i}")
    for p in PROMPTS:
        for i, (a, b, c) in enumerate(LINE_KEYS[p], start=1):
            if (its & a) or (lcs & c):
                add(s, "unsent prompt", rel(p.parent), "", PROMPT_LINES[p][i - 1],
                    "names the settled " + ("item" if its & a else "place"), "medium", f"{rel(p)}:{i}")

seen, out = set(), []
for r in ROWS:
    k = (r["source_id"], r["target_kind"], r["target"], r["evidence"])
    if k not in seen:
        seen.add(k)
        out.append(r)
OUTD.mkdir(parents=True, exist_ok=True)
cols = ["n", "source_id", "source_intake", "source_effect", "source_text", "target_kind", "target", "target_topic",
        "target_text", "link", "confidence", "evidence"]
with (OUTD / "PROPAGATION_CANDIDATES.tsv").open("w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_NONE, escapechar="\\")
    w.writerow(cols)
    for n, r in enumerate(out, start=1):
        w.writerow([n] + [str(r[c]).replace("\t", " ") for c in cols[1:]])
sys.stdout.reconfigure(encoding="utf-8")
print("sources", len(SOURCES), collections.Counter(s["effect"] for s in SOURCES))
print("sources with keys", sum(1 for s in SOURCES if s["items"] or s["locs"] or s["tags"]))
print("candidates", len(out), collections.Counter(r["target_kind"] for r in out))
print("by intake", collections.Counter(r["source_intake"] for r in out))
