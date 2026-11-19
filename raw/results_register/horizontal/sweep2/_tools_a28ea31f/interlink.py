"""Sweep 2 part 2 (agent a28ea31fa17dd65e1, Claude Opus 5.5 at effort max): interlinking tables and WHAT_IS_WHERE.

python -I -B interlink.py SAnn   -> sweep2/SAnn/DEPENDS.tsv, CLAIM_LINKS.tsv, UNIT_LINKS.tsv, CORRECTIONS.tsv, WHAT_IS_WHERE.md
Curated data per topic: links_SAnn.py (ORDER, STATUS, DEPENDS, ITEMLINKS, ENTRYLINKS, CORRECTIONS, INTRO).
"""
import csv, re, sys, collections, importlib.util
from pathlib import Path

csv.field_size_limit(10 ** 9)
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
DOC = Path(r"C:/Users/user/Documents")
H = DOC / "results_register/horizontal"
S2 = H / "sweep2"
TOOLS = S2 / "_tools_a28ea31f"
WHO = "Claude Opus 5.5 at effort max, a28ea31fa17dd65e1, sweep 2 part 2"
CLAIMRX = re.compile(r"unproved claim|conjecture|self-flagged|withdrawn|steps the pages mark|his claim|^question|explicit question", re.I)


def clean(s):
    return re.sub(r"\s+", " ", (s or "").replace("\t", " ")).strip()


def rtsv(p):
    with open(p, encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f, delimiter="\t"))
    return rows[0], [dict(zip(rows[0], r)) for r in rows[1:]]


def wtsv(p, head, rows):
    with open(p, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(head)
        for r in rows:
            w.writerow([clean(str(x)) for x in r])


def ints(s):
    out = set()
    for m in re.finditer(r"(\d+)\s*[-–]\s*(\d+)|(\d+)", s or ""):
        if m.group(1):
            a, b = int(m.group(1)), int(m.group(2))
            if 0 <= b - a <= 400:
                out.update(range(a, b + 1))
        else:
            out.add(int(m.group(3)))
    return out


def ranges(nums):
    nums = sorted(nums)
    out, i = [], 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        out.append(str(nums[i]) if i == j else f"{nums[i]}-{nums[j]}")
        i = j + 1
    return ", ".join(out)


def load(topic):
    p = TOOLS / f"links_{topic}.py"
    spec = importlib.util.spec_from_file_location("links_" + topic, p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main(topic):
    L = load(topic)
    _, place = rtsv(S2 / topic / "PLACEMENT.tsv")
    _, objs = rtsv(S2 / topic / "OBJECTS.tsv")
    _, flags = rtsv(S2 / topic / "FLAGS.tsv")
    _, units = rtsv(S2 / "inputs/UNITS.tsv")
    srcfile = {u["entry_id"]: u["source_file"] for u in units}
    _, ud = rtsv(DOC / "grothendieck_archive_transcription_20261110/UNITS_DRAFT_20261118.tsv")
    obj = {o["item"]: o for o in objs}
    order = [i for i in L.ORDER if i in obj] + [i for i in obj if i not in L.ORDER]
    by_item = collections.defaultdict(list)
    for r in place:
        by_item[r["item"]].append(r)
    # where: cotes and scans per item
    where = {}
    for it, rs in by_item.items():
        cs = collections.defaultdict(set)
        srcs = collections.Counter()
        for r in rs:
            cotes = [c for c in re.split(r"[ ,]+", r["cote"]) if c.isdigit()]
            sc = ints(r["scans"].replace("/", ","))
            for c in cotes or ["?"]:
                cs[c] |= sc
            srcs[r["entry_id"].rsplit("#", 1)[0]] += 1
        where[it] = (cs, srcs)
    # DEPENDS
    dep_rows = [[a, "uses", b, basis, ev, note] for a, b, basis, ev, note in L.DEPENDS]
    wtsv(S2 / topic / "DEPENDS.tsv", ["item", "relation", "uses_item", "basis", "evidence", "note"], dep_rows)
    uses = collections.defaultdict(list)
    usedby = collections.defaultdict(list)
    for a, b, basis, ev, note in L.DEPENDS:
        uses[a].append((b, basis))
        usedby[b].append((a, basis))
    # CLAIM_LINKS
    cl_rows = []
    nclaims = collections.Counter()
    for r in place:
        if not CLAIMRX.search(r["kind"] or ""):
            continue
        it = r["item"]
        nclaims[it] += 1
        place_s = f"cote {r['cote']}, scans {r['scans']}".strip()
        if r["entry_id"] in L.ENTRYLINKS:
            for lk, tgt, basis, note in L.ENTRYLINKS[r["entry_id"]]:
                cl_rows.append([r["entry_id"], place_s, r["kind"], it, lk, tgt, basis, note])
            continue
        links = L.ITEMLINKS.get(it, [])
        if not links:
            cl_rows.append([r["entry_id"], place_s, r["kind"], it, "no link found",
                            "none in the register or among the topic's items", "item-level search",
                            L.STATUS.get(it, ("", ""))[1]])
        for lk, tgt, basis, note in links:
            cl_rows.append([r["entry_id"], place_s, r["kind"], it, lk, tgt, "item-level: " + basis, note])
    wtsv(S2 / topic / "CLAIM_LINKS.tsv", ["claim_entry", "his_place", "kind", "item", "link", "target", "basis", "note"], cl_rows)
    # UNIT_LINKS
    ul_rows = []
    folders_of = collections.defaultdict(collections.Counter)
    for r in place:
        m = re.match(r"(?:work|codex):([A-Z]+\d+-\d+(?:_\d)?)", r["entry_id"])
        if m:
            folders_of[m.group(1)][r["item"]] += 1
    folder_item = {f: c.most_common(1)[0][0] for f, c in folders_of.items()}
    seen = set()
    for u in ud:
        f = u["folder"]
        if f in folder_item:
            it = folder_item[f]
            ul_rows.append([it, u["unit"], u["folder"], u["cote"], u["scans"], u["title"], "same folder"])
            seen.add((it, u["unit"]))
    for it in order:
        cs, _ = where.get(it, ({}, {}))
        for u in ud:
            c = u["cote"]
            if c in cs and cs[c] and (it, u["unit"]) not in seen:
                us = ints(u["scans"])
                if us and us & cs[c]:
                    ul_rows.append([it, u["unit"], u["folder"], c, u["scans"], u["title"], "scan overlap"])
                    seen.add((it, u["unit"]))
    wtsv(S2 / topic / "UNIT_LINKS.tsv", ["item", "unit", "folder", "cote", "scans", "title", "basis"], ul_rows)
    nunits = collections.Counter(r[0] for r in ul_rows)
    # CORRECTIONS
    wtsv(S2 / topic / "CORRECTIONS.tsv", ["where", "what", "correction", "basis", "by"],
         [list(c) + [WHO] if len(c) == 4 else list(c) for c in L.CORRECTIONS])
    # flags per item
    ent_item = {r["entry_id"]: r["item"] for r in place}
    fl = collections.defaultdict(list)
    for f in flags:
        hit = set()
        for eid, it in ent_item.items():
            if eid and eid in f["where"]:
                hit.add(it)
        for it in re.findall(rf"\b{topic}-\d+\b", f["where"] + " " + f["what"]):
            hit.add(it)
        for it in hit:
            fl[it].append(f)
    # WHAT_IS_WHERE.md
    o = [f"# {topic}: what is where", "", f"{WHO}, 18 Nov 2026. Built from this folder's PLACEMENT, OBJECTS, FLAGS,",
         "DEPENDS, CLAIM_LINKS and UNIT_LINKS (sweep 1 and sweep 2). Items are in mathematical order.", "",
         "How to read the links: 'Uses' and 'Used by' come from DEPENDS.tsv, with the basis in brackets (his page: the page",
         "refers to or builds on it; our note: a note links them; proof: the mathematics requires it). Claim links are",
         "item-level unless a row says 'decided on the scan': 'known' means the item's subject is established in the cited",
         "literature, not that each of his claims was checked one by one. Companion units come from",
         "UNITS_DRAFT_20261118.tsv, which does not yet cover every folder.", ""]
    o += [L.INTRO.strip(), ""]
    o += ["| # | Item | Entries | Status |", "|---|---|---:|---|"]
    for k, it in enumerate(order, 1):
        o.append(f"| {k} | {it}: {obj[it]['object'][:80]} | {len(by_item.get(it, []))} | {L.STATUS.get(it, ('', ''))[0]} |")
    o.append("")
    for it in order:
        cs, srcs = where.get(it, ({}, collections.Counter()))
        st = L.STATUS.get(it, ("", ""))
        o.append(f"## {it}: {obj[it]['object']}")
        o.append("")
        o.append(f"- **Status:** {st[0]}. {st[1]}".rstrip())
        wl = "; ".join(f"cote {c}, scans {ranges(s)}" if s else f"cote {c}" for c, s in sorted(cs.items(), key=lambda x: (not x[0].isdigit(), int(x[0]) if x[0].isdigit() else 0)))
        o.append(f"- **Where (his pages):** {wl or 'not localized'}.")
        files = collections.Counter()
        for src, n in srcs.items():
            sid = next((r["entry_id"] for r in by_item[it] if r["entry_id"].startswith(src + "#")), None)
            files[(src, srcfile.get(sid, ""))] += n
        o.append("- **Where (our notes):** " + "; ".join(f"{src} ({n})" + (f" in `{fp}`" if fp else "") for (src, fp), n in files.most_common(8))
                 + (f"; and {len(files) - 8} more sources" if len(files) > 8 else "") + ".")
        if obj[it].get("cross_topic"):
            o.append(f"- **Across topics:** {obj[it]['cross_topic']}.")
        u = ", ".join(f"{b} ({ba})" for b, ba in uses.get(it, []))
        ub = ", ".join(f"{a} ({ba})" for a, ba in usedby.get(it, []))
        o.append(f"- **Uses:** {u or 'nothing recorded'}. **Used by:** {ub or 'nothing recorded'}.")
        links = L.ITEMLINKS.get(it, [])
        o.append(f"- **His claims:** {nclaims.get(it, 0)} entries" + (": " + "; ".join(f"{lk} {tgt}" for lk, tgt, _, _ in links) if links else ": no proof or refutation found in the register or the topic") + ".")
        if fl.get(it):
            o.append(f"- **Flags ({len(fl[it])}):** " + " | ".join(clean(f['kind'] + ': ' + f['what'])[:170] for f in fl[it][:3]) + (" | ..." if len(fl[it]) > 3 else ""))
        if nunits.get(it):
            titles = [r[5] for r in ul_rows if r[0] == it][:3]
            o.append(f"- **Companion units ({nunits[it]}):** " + "; ".join(t[:60] for t in titles) + (" ..." if nunits[it] > 3 else ""))
        o.append("")
    if getattr(L, "OUTRO", ""):
        o += [L.OUTRO.strip(), ""]
    (S2 / topic / "WHAT_IS_WHERE.md").write_text("\n".join(o), encoding="utf-8")
    print(topic, "depends", len(dep_rows), "claims", len(cl_rows), "claim-entries", sum(nclaims.values()), "units", len(ul_rows), "corrections", len(L.CORRECTIONS))


if __name__ == "__main__":
    main(sys.argv[1])
