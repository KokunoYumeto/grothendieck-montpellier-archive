"""Sweep 2, part 1, items 2, 9 and 11 (broad agent a0c4bb37, Claude Opus 5.5 at effort max, 18 Nov 2026):
  GLOBAL/STALE_PLACEMENTS.tsv   + settled_to: the current entry each stale sweep-1 placement now names
  GLOBAL/DOUBLE_PLACEMENTS.tsv  every entry placed in more than one topic: the owner topic keeps it, the others link
  GLOBAL/DOUBLE_OBJECTS.tsv     the sweep-1 objects in more than one topic: shared entries, owner, and whether the
                                agents' statements and statuses agree (a script comparison; a difference is a flag)
  GLOBAL/LINKED_PLACEMENTS.tsv  the chatB witnesses and the variant folders, one row each, linked to the item of the
                                entry they witness (variants by entry number, chatB by shared scans)
Reads sweep1 and sweep2/inputs; writes only sweep2/GLOBAL. usage: python -I -B settle.py"""
import csv, re, sys, collections, pathlib, difflib

sys.stdout.reconfigure(encoding="utf-8")
csv.field_size_limit(10 ** 9)
H = pathlib.Path(r"C:\Users\user\Documents\results_register\horizontal")
S1, S2 = H / "sweep1", H / "sweep2"
G2 = S2 / "GLOBAL"


def read(p):
    with open(p, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def write(p, rows, fields):
    with open(p, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: re.sub(r"\s+", " ", str(r.get(k, ""))) for k in fields})


U = {u["entry_id"]: u for u in read(S2 / "inputs" / "UNITS.tsv")}
P1 = {}  # topic -> placement rows of sweep 1
for pf in sorted(S1.glob("SA[0-9][0-9]/PLACEMENT.tsv")):
    P1[pf.parent.name] = read(pf)
O1 = {}
for of in sorted(S1.glob("SA[0-9][0-9]/OBJECTS.tsv")):
    for r in read(of):
        r["topic"] = of.parent.name
        O1[r["item"].strip()] = r
# 9. stale placements: the checked mapping (read 18 Nov 20:2x UTC: the file headings and the placements' objects)
CHECKED = {"MPL_137_002-044#SQ1": ("MPL_137_002-044#112", "'Standing question 1' is entry 112 of the final"),
           "MPL_137_002-044#SQ2": ("MPL_137_002-044#113", "'Standing question 2' is entry 113 of the final"),
           "work:H66-01#1": ("codex:H66-01#1", "H66-01 has notes on the sheets, no math notes: the prefix was work: by mistake"),
           "work:H66-01#2": ("codex:H66-01#2", "as for #1"),
           "work:K32-02#7": ("work:K32-02#6", "sweep 1 counted the '### Reading questions' subsection of entry 6 as entry 7"),
           "work:K123-02#7": ("work:K123-02#6", "sweep 1 counted the '### Reading questions' subsection of entry 6 as entry 7")}
stale = read(G2 / "STALE_PLACEMENTS.tsv")
for s in stale:
    s["settled_to"], s["settled_why"] = CHECKED.get(s["entry_id"], (s.get("proposed", ""), "proposed by heading similarity; not checked"))
write(G2 / "STALE_PLACEMENTS.tsv", stale, list(stale[0].keys()))
alias = {r["alias"]: r["canonical"] for r in read(G2 / "ID_ALIASES.tsv")}
alias.update({s["entry_id"]: s["settled_to"] for s in stale if s["settled_to"]})


def canon(e):
    seen = set()
    while e in alias and e not in seen:
        seen.add(e)
        e = alias[e]
    return e


# 2. double placements: an entry placed in more than one topic
where = collections.defaultdict(list)
for t, rows in P1.items():
    for r in rows:
        e = canon((r.get("entry_id") or "").strip())
        if e:
            where[e].append((t, (r.get("item") or "").strip()))
COTE_TOPIC = {}
for tp in sorted(H.glob("inputs/SA[0-9][0-9]/TOPIC.md")):
    for line in tp.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*(\d+(?:-\d+)?)\s*\|", line)
        if m:
            COTE_TOPIC.setdefault(m.group(1), tp.parent.name)


def owner_of(e, topics):
    u = U.get(e)
    if u and u["topic"] in topics:
        return u["topic"], "the topic that holds the entry's file in the refreshed inputs"
    src = e.split("#")[0]
    m = re.match(r"^(?:codex:|work:)?[A-Z]*?(\d+(?:-\d+)?)-\d+", src) or re.match(r"^MPL_(\d+(?:-\d+)?)", src)
    t = COTE_TOPIC.get(m.group(1)) if m else None
    if t in topics:
        return t, "the topic of the entry's first cote"
    return sorted(topics)[0], "first of the placing topics (no cote rule applies)"


def toks(s):
    return {w for w in re.sub(r"[^a-z0-9à-ÿ ]+", " ", (s or "").lower()).split() if len(w) > 3}


dbl = []
for e, tl in sorted(where.items()):
    topics = sorted({t for t, _ in tl})
    if len(topics) < 2:
        continue
    own, why = owner_of(e, topics)
    items = sorted({i for _, i in tl})
    oi = next((i for t, i in tl if t == own), "")
    dbl.append(dict(entry_id=e, topics=" ".join(topics), owner_topic=own, owner_item=oi,
                    other_items=" ".join(i for t, i in sorted(set(tl)) if t != own), why_owner=why,
                    decision=f"kept in {own} ({oi}); the other topics' rows become links to it"))
write(G2 / "DOUBLE_PLACEMENTS.tsv", dbl, ["entry_id", "topics", "owner_topic", "owner_item", "other_items", "why_owner", "decision"])
# the sweep-1 objects in more than one topic
go = [r for r in read(S1 / "GLOBAL" / "GLOBAL_OBJECTS.tsv") if int(r["n_topics"]) > 1]
dbl_by_item = collections.defaultdict(int)
for d in dbl:
    for i in [d["owner_item"]] + d["other_items"].split():
        dbl_by_item[i] += 1
dob = []
for r in go:
    its = r["items"].split()
    st = {i: (O1.get(i, {}).get("status_on_pages") or "").strip().lower() for i in its}
    sm = [O1.get(i, {}).get("statement") or O1.get(i, {}).get("object") or "" for i in its]
    pair = [(a, b) for k, a in enumerate(sm) for b in sm[k + 1:]]
    jac = min((len(toks(a) & toks(b)) / max(1, len(toks(a) | toks(b))) for a, b in pair), default=1)
    fl = {i: bool((O1.get(i, {}).get("flags") or "").strip()) for i in its}
    status_agree = len({re.sub(r"[;,(].*", "", s).strip() for s in st.values()}) <= 1
    dob.append(dict(tag=r["tag"], object=r["object"][:120], items=r["items"], topics=r["topics"], merged_by=r["merged_by"][:80],
                    shared_entries=sum(dbl_by_item[i] for i in its) // 2 if len(its) == 2 else sum(dbl_by_item[i] for i in its),
                    status_agree="yes" if status_agree else "no: " + " | ".join(f"{i}: {s[:50]}" for i, s in st.items()),
                    statement_overlap=f"{jac:.2f}",
                    flags_in=" ".join(i for i, f in fl.items() if f) or "none",
                    settle=("one placement per shared entry (DOUBLE_PLACEMENTS.tsv); the items stay one object"
                            if any(dbl_by_item[i] for i in its) else "no shared entry: the same object placed from different entries; keep both")))
write(G2 / "DOUBLE_OBJECTS.tsv", dob, list(dob[0].keys()))
# 11. linked rows: chatB witnesses and variant folders
placed_item = {}
for t, rows in P1.items():
    for r in rows:
        placed_item.setdefault(canon(r["entry_id"].strip()), (t, (r.get("item") or "").strip(), r.get("object", ""), r.get("scans", "")))
scan_items = collections.defaultdict(collections.Counter)  # (package, scan) -> items
for e, (t, it, ob, sc) in placed_item.items():
    pkg = e.split("#")[0]
    for s in re.findall(r"\d{1,3}", sc or ""):
        scan_items[(pkg, int(s))][it] += 1
main_units = collections.defaultdict(list)
for e, u in U.items():
    main_units[e.split("#")[0]].append(u)
linked = []
for e, u in U.items():
    if u["cls"] not in ("pro_chatB", "variant") or u["placed_sweep1"] != "no":
        continue
    base = u["linked_to"]
    row = dict(entry_id=e, topic=u["topic"], scans=u["scans"], kind="parallel witness" if u["cls"] == "pro_chatB" else "variant folder",
               witness_of=base, item="", object="", basis="index-row (linked by script)", fidelity="not checked", how="")
    if base and canon(base) in placed_item:
        t, it, ob, sc = placed_item[canon(base)]
        row.update(item=it, object=ob[:150], how="same entry number in the base folder" if u["cls"] == "variant" else "same entry number")
    if u["cls"] == "pro_chatB":
        src = e.split("#")[0].replace("_chatB", "")
        mains = [m for m in main_units.get(src, []) if canon(m["entry_id"]) in placed_item]
        best, score, how = None, 0.0, ""
        us = set(filter(None, (u["scans"] or "").split(",")))
        for m in mains:
            sc = difflib.SequenceMatcher(None, u["heading"].lower(), m["heading"].lower()).ratio()
            if u["label"] and u["label"] == m["label"]:
                sc += 1
            if us and us & set(filter(None, (m["scans"] or "").split(","))):
                sc += 0.3
            if sc > score:
                best, score = m, sc
        row["witness_of"] = src
        if best is not None and score >= 0.6:
            t, it, ob, scn = placed_item[canon(best["entry_id"])]
            row.update(item=it, object=ob[:150], witness_of=best["entry_id"],
                       how=f"the main chat's entry with the closest heading, label or scans (score {score:.2f})")
        else:
            row.update(item="", object="", how="no matching entry in the main chat: to be placed on reading")
    if not row["item"]:
        row["how"] = row["how"] or "the witnessed entry is itself unplaced: placed with it"
    linked.append(row)
write(G2 / "LINKED_PLACEMENTS.tsv", linked, ["entry_id", "topic", "scans", "kind", "witness_of", "item", "object", "basis", "fidelity", "how"])
print("stale", len(stale), "| double-placed entries", len(dbl), "| multi-topic objects", len(dob),
      "status disagree", sum(1 for d in dob if d["status_agree"] != "yes"),
      "| linked rows", len(linked), "with item", sum(1 for l in linked if l["item"]),
      collections.Counter(l["how"] for l in linked).most_common(5))
