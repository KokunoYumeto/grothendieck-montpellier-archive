"""Build the object prompts (18 Nov 2026): one ChatGPT Pro prompt per object of horizontal sweep 1, each writing the
handbook's foundational entry for that object (the coordinator's message of ~15:4x UTC, the user's word: "200 prompts
that take like 30 minutes or an hour ... foundational math, horizontal"; built first, before the per-folder units).

Inputs (read-only): results_register/horizontal/sweep1/GLOBAL/GLOBAL_OBJECTS.tsv (the global tags; each object's items
in every topic), sweep1/SA*/OBJECTS.tsv and PLACEMENT.tsv (every note entry placed under an item), the notes themselves
(horizontal/inputs/SA*/, the Work math notes), the page index of wt_common.py (every reading of every page), the
archive PDFs (images), results_register/REGISTER.tsv (our runs' statements, opened last by the run), and
CONTEXT_RULES.tsv (his published text, by cote).

The plan (OBJECTS_PLAN.tsv):
- eligible objects are his mathematics; the research-run lenses, the documentary and apparatus objects and the lists of
  reading questions are left out with the reason (reading questions go to the per-folder pass);
- an object of more than about 28 entries or 16,000 words of notes is cut into parts, by its topic items and then by
  pages; objects of four entries or fewer and under 2,500 words are bundled with neighbours of the same topic and
  folder (up to four objects, about 12 entries), each still getting its own entry;
- order: the topics the vertical research never touched first (in the archive's order), then the stratified spaces,
  the Pursuing Stacks cluster, the Longue Marche cluster and the Derivateurs; within a topic, his chronological order
  (the folder's date, the cote, the first page).

usage: python -I -B build_object_prompts.py plan
       python -I -B build_object_prompts.py build OBJ_H0D6 [more ids]
       python -I -B build_object_prompts.py build --next N        (the next N eligible prompts of the plan not yet built)
Upload folders: objects/<id>/ (flat: PROMPT.md, the zips, README.md); work files: _work/objects/<id>/BUILD.json.
Written by Claude Opus 5.5 at effort max (agent a11a6de3, no sub-agents), 18 Nov 2026."""
import collections
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import wt_common as W  # noqa: E402

HERE = W.HERE
OUT = HERE / "objects"
WORK = HERE / "_work" / "objects"
TEMPLATE = HERE / "OBJECT_PROMPT_TEMPLATE.md"
PLAN = HERE / "OBJECTS_PLAN.tsv"
RULES = HERE / "CONTEXT_RULES.tsv"
PREAMBLE = W.CW / "tools" / "PREAMBLE.tex"
MAX_SCANS = 12
SPLIT_ENTRIES, SPLIT_WORDS = 40, 12000
PART_ENTRIES, PART_WORDS = 25, 8000
SMALL_ENTRIES, SMALL_WORDS = 5, 3000
MERGE_JACCARD = 0.5
BUNDLE_ENTRIES, BUNDLE_OBJECTS = 12, 4

# the topics no research run touched, in the archive's order; then those the vertical work touched
TOPIC_ORDER = ["SA23", "SA15", "SA05", "SA06", "SA07", "SA12", "SA13", "SA19", "SA18", "SA14", "SA16", "SA22", "SA01",
               "SA02", "SA03", "SA04", "SA20", "SA17", "SA08", "SA09", "SA21",
               "SA10", "SA11", "SA24", "SA25", "SA26", "SA27", "SA28", "SA29", "SA30", "SA31", "SA32"]
TOUCHED = set(TOPIC_ORDER[TOPIC_ORDER.index("SA10"):])

LENS_KIND = re.compile(r"^(lens|research question put to the pages|notes' proposal|comparison \(requested\)|context question|"
                       r"context|meta)\b", re.I)
LENS_NAME = re.compile(r"research-run famil|NEW_RESULTS|RESULTS_STATE|mapped onto cote|requested LM bridge|LM bridge|"
                       r"the notes' proposed|with research-run register|register rows|research families", re.I)
DOC_KIND = re.compile(r"^(documentary|archival|apparatus|source accounting|plan|reading|reading question|reading questions|"
                      r"scope)\b", re.I)
DOC_NAME = re.compile(r"documentary|apparatus|source accounting|as a document|page concordance|reading questions|"
                      r"reading doubts|physical unit|codicolog|page sequences|titles, page|dates, marginal|"
                      r"what the package adds", re.I)
OPEN_KIND = re.compile(r"conjecture|question|self-flag|hope|open", re.I)


# ------------------------------------------------------------------------------------------------ loading
def load():
    tags, item_tag = W.global_objects()
    items = W.sweep_objects()
    by_item = collections.defaultdict(list)
    for r in W.placements():
        for it in [x for x in re.split(r"[,;\s]+", r["item"]) if x]:  # a row may name several items (SA23)
            by_item[it].append(dict(r, item=it))
    idx = W.build_index()
    objs = {}
    for tag, g in tags.items():
        its = g["items"].split()
        ents = {}
        for it in its:
            for r in by_item.get(it, []):
                ents.setdefault(r["entry_id"], r)
        objs[tag] = dict(tag=tag, row=g, items=its, entries=ents)
    return objs, items, idx


_ENTRY_CACHE = {}


def entry(eid, prow):
    if eid not in _ENTRY_CACHE:
        h, t, f, l = W.entry_text(eid, prow.get("topic") or prow["_topic_dir"])
        _ENTRY_CACHE[eid] = dict(heading=h or "", text=t or "", file=f, line=l, words=len((t or "").split()))
    return _ENTRY_CACHE[eid]


def source_of(eid):
    if eid.startswith("work:"):
        return "work", eid[5:].rsplit("#", 1)[0]
    if eid.startswith("codex:"):
        return "codex", eid[6:].rsplit("#", 1)[0]
    return "pro", eid.rsplit("#", 1)[0]


def entry_pages(eid, prow, text, idx):
    """the (cote, scan) pages an entry is about: its index row's scans, and the pages its text cites"""
    cotes = [c for c in re.split(r"[,;\s]+", prow.get("cote") or "") if re.match(r"^\d+(-\d+)?$", c)]
    kind, src = source_of(eid)
    if kind != "pro" and not cotes:
        a = W.ASSIGN.get(src) or W.ASSIGN.get(re.sub(r"_\d+$", "", src)) or {}
        if a.get("cote"):
            cotes = [a["cote"]]
    pages = set()
    for c, s in re.findall(r"(?<![\d.])(\d{1,3}(?:-\d)?)\s*[/:]\s*0*(\d{1,3})(?![\d])", text):
        if c in cotes and (c, int(s)) in idx:
            pages.add((c, int(s)))
    nums = W.scans_in(prow.get("scans") or "")
    for a, b in re.findall(r"[Ss]cans?\s+0*(\d{1,3})(?:\s*[-–]\s*0*(\d{1,3}))?", text):
        a = int(a)
        b = int(b) if b else a
        if 0 <= b - a <= 40:
            nums.update(range(a, b + 1))
    if kind == "codex":
        nums.update(int(x) for x in re.findall(r"\*\*0*(\d{2,3})\*\*", text))
    for s in nums:
        own = [(c, s) for c in cotes if any(x["id"] == src for x in idx.get((c, s), []))]
        cand = own or [(c, s) for c in cotes if (c, s) in idx]
        pages.update(cand)
    if not pages and kind != "pro":
        a = W.ASSIGN.get(src) or W.ASSIGN.get(re.sub(r"_\d+$", "", src)) or {}
        for s in W.scans_in(a.get("scans", "")):
            if (a.get("cote"), s) in idx:
                pages.add((a["cote"], s))
    return pages


def classify(o, items):
    kinds = [items[i]["kind"] for i in o["items"] if i in items]
    name = o["row"]["object"]
    status = o["row"].get("status_on_pages", "")
    if LENS_NAME.search(name) or (kinds and all(LENS_KIND.search(k) for k in kinds)):
        return "no", "the research runs' lens (their families or requested bridges mapped onto his pages), not an object of his"
    if DOC_NAME.search(name) or (kinds and all(DOC_KIND.search(k) for k in kinds)):
        if re.search(r"reading", name + " ".join(kinds), re.I):
            return "no", "reading questions: decided on the scans by the per-folder pass, which receives them in its concordance"
        return "no", "documentary or apparatus (titles, dates, sources, the notes' own bookkeeping): for the companion's apparatus"
    if not o["entries"]:
        return "no", "no entries placed"
    if re.match(r"^not on (the|these) pages", status) and all(source_of(e)[0] == "pro" for e in o["entries"]):
        return "no", "not on his pages: the notes' comparison with other material"
    return "yes", ""


def main_topic(o):
    c = collections.Counter(r.get("topic") or r["_topic_dir"] for r in o["entries"].values())
    return c.most_common(1)[0][0] if c else (o["row"]["topics"].split() or ["SA99"])[0]


def order_key(u):
    t = u["topic"]
    ti = TOPIC_ORDER.index(t) if t in TOPIC_ORDER else 99
    return (ti, u["year"], W.cote_key(u["cote"]), u["first_scan"], u["id"])


def summarize(o, idx, items):
    """per entry: pages, words, kind; per object: totals"""
    rows = []
    for eid, prow in o["entries"].items():
        e = entry(eid, prow)
        pg = entry_pages(eid, prow, e["text"], idx)
        rows.append(dict(eid=eid, prow=prow, pages=pg, words=e["words"], src=source_of(eid)[0],
                         kind=prow.get("kind", ""), item=prow["item"]))
    rows.sort(key=lambda r: (min((W.cote_key(c), s) for c, s in r["pages"]) if r["pages"] else ((9999, 0), 0), r["eid"]))
    return rows


def compress(nums):
    nums = sorted(set(nums))
    out, i = [], 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        out.append(str(nums[i]) if i == j else f"{nums[i]}-{nums[j]}")
        i = j + 1
    return ", ".join(out)


def cotes_scans_text(pages):
    by = collections.defaultdict(list)
    for c, s in pages:
        by[c].append(s)
    return "; ".join(f"{c}: {compress(v)}" for c, v in sorted(by.items(), key=lambda kv: W.cote_key(kv[0])))


NUM_RX = re.compile(r"(?<![A-Za-zà-ÿ])(?:Lemme|Proposition|Prop\.|Th[ée]or[èe]me|Th\.|Corollaire|"
                    r"Cor\.|Remarque|Rem\.|D[ée]finition|D[ée]f\.|Exemple|Scholie)\s*\}?\s*\.?\s*"
                    r"(?:\\u{1,2}line\{\s*)?(\d{1,3})(?:\s*\.\s*(\d{1,3}))?(?!\d)")
SPAN_EXTRA = 40
_NUM = {}


def numbered(cote, idx):
    """scan -> the numbers of the statements that open a line on the page ((major, minor) pairs), from the reading a
    pass starts from"""
    if cote not in _NUM:
        out = {}
        for s in W.scans_of(cote):
            f = W.first_reading(idx.get((cote, s), []))
            if f:
                ns = [(int(a), int(b or 0)) for a, b in NUM_RX.findall(W.page_text(f))]
                if ns:
                    out[s] = ns
        _NUM[cote] = out
    return _NUM[cote]


def sequences(cote, idx):
    """[(first scan, last scan)] of his numbered sequences: pages carrying statement numbers (Lemme 1, Proposition 9,
    Remarque 21, ...), with gaps of at most five pages; a page whose numbers all lie below the sequence's highest is a
    back-reference and is passed over; a page that starts again at 1 or 2 after the sequence reached 4 starts a new one"""
    num = numbered(cote, idx)
    seqs, cur = [], None
    for s in sorted(num):
        lo, hi = min(num[s]), max(num[s])
        if cur and s - cur[1] <= 5:
            if hi >= cur[2]:
                cur[1], cur[2] = s, hi
                continue
            if not (lo[0] <= 2 and hi[0] <= 2 and cur[2][0] >= 4):
                continue
        if cur:
            seqs.append((cur[0], cur[1]))
        cur = [s, s, hi]
    if cur:
        seqs.append((cur[0], cur[1]))
    return [q for q in seqs if q[1] > q[0]]


def object_span(pages, idx):
    """B2 of the verdict on OBJ_H035 (19 Nov 2026): the pages the entries cite, extended over the numbered sequences of
    his statements that hold them, with at most SPAN_EXTRA pages added, nearest to a cited page first"""
    pages = set(pages)
    by = collections.defaultdict(set)
    for c, s in pages:
        by[c].add(s)
    extra = set()
    for c, ss in by.items():
        for a, b in sequences(c, idx):
            if any(a - 1 <= s <= b + 1 for s in ss):
                extra.update((c, x) for x in W.scans_of(c) if a <= x <= b and (c, x) in idx)
    extra -= pages
    if len(extra) > SPAN_EXTRA:
        def dist(cs):
            return min((abs(cs[1] - s) for s in by[cs[0]]), default=999)
        extra = set(sorted(extra, key=lambda cs: (dist(cs), W.cote_key(cs[0]), cs[1]))[:SPAN_EXTRA])
    return pages | extra


def est_minutes(span_pages, open_entries):
    """B1 of the verdict on OBJ_H035, for scheduling only (never in a prompt or its README): 15 minutes plus 5.5 a page
    of the object's span, plus 60 when an entry carries an open question (the tail under the progress check)"""
    return int(round(15 + 5.5 * span_pages + (60 if open_entries else 0)))


def merged_groups(objs, items):
    """the eligible objects, grouped: objects that share at least MERGE_JACCARD of their entries are one prompt"""
    elig = [t for t, o in objs.items() if classify(o, items)[0] == "yes"]
    parent = {t: t for t in elig}

    def find(t):
        while parent[t] != t:
            parent[t] = parent[parent[t]]
            t = parent[t]
        return t
    ents = {t: set(objs[t]["entries"]) for t in elig}
    owner = collections.defaultdict(list)
    for t in elig:
        for e in ents[t]:
            owner[e].append(t)
    for e, ts in owner.items():
        for i in range(len(ts)):
            for j in range(i + 1, len(ts)):
                x, y = ts[i], ts[j]
                if len(ents[x] & ents[y]) / len(ents[x] | ents[y]) >= MERGE_JACCARD:
                    parent[find(x)] = find(y)
    groups = collections.defaultdict(list)
    for t in elig:
        groups[find(t)].append(t)
    return [sorted(g) for g in groups.values()]


def unit_base(ts, o, idx, items):
    rows = summarize(o, idx, items) if o["entries"] else []
    pages = set().union(*[r["pages"] for r in rows]) if rows else set()
    topic = main_topic(o) if o["entries"] else (o["row"]["topics"].split() or ["SA99"])[0]
    main_cote = (collections.Counter(c for r in rows for c, s in r["pages"]).most_common(1)
                 or [((re.findall(r"\d+(?:-\d+)?", o["row"]["cotes_scans"]) or ["9999"])[0], 0)])[0][0]
    first = min((s for c, s in pages if c == main_cote), default=0)
    return dict(tags=list(ts), objects=[o["names"][t] for t in ts], topic=topic, cote=main_cote, first_scan=first,
                year=W.year_of(main_cote) if main_cote in W.MAN else 9999, rows=rows, pages=pages)


def make_units(objs, items, idx):
    units, small = [], collections.defaultdict(list)
    excluded = []
    for tag, o in objs.items():
        ok, why = classify(o, items)
        if ok == "no":
            base = unit_base([tag], dict(o, names={tag: o["row"]["object"]}), idx, items)
            excluded.append(dict(base, id=f"OBJ_{tag}", kind="excluded", reason=why))
    for ts in merged_groups(objs, items):
        if len(ts) == 1:
            o = dict(objs[ts[0]], names={ts[0]: objs[ts[0]]["row"]["object"]})
        else:
            ents = {}
            for t in ts:
                for eid, prow in objs[t]["entries"].items():
                    ents.setdefault(eid, prow)
            o = dict(tag=ts[0], row=objs[ts[0]]["row"], items=[i for t in ts for i in objs[t]["items"]], entries=ents,
                     names={t: objs[t]["row"]["object"] for t in ts})
        base = unit_base(ts, o, idx, items)
        rows, pages, main_cote, first = base["rows"], base["pages"], base["cote"], base["first_scan"]
        tag = "+".join(ts)
        single_kind = "single" if len(ts) == 1 else f"{len(ts)} objects sharing their entries"
        n, words = len(rows), sum(r["words"] for r in rows)
        if n > SPLIT_ENTRIES or words > SPLIT_WORDS:
            # parts: by topic item, then by pages, each up to PART_ENTRIES entries / PART_WORDS words
            chunks, cur, cw = [], [], 0
            by_item = collections.OrderedDict()
            for r in rows:
                by_item.setdefault(r["item"], []).append(r)
            for it, rs in by_item.items():
                for r in rs:
                    if cur and (len(cur) >= PART_ENTRIES or cw + r["words"] > PART_WORDS):
                        chunks.append(cur)
                        cur, cw = [], 0
                    cur.append(r)
                    cw += r["words"]
                if cur and len(cur) >= PART_ENTRIES * 0.6:
                    chunks.append(cur)
                    cur, cw = [], 0
            if cur:
                chunks.append(cur)
            for k, ch in enumerate(chunks, 1):
                pg = set().union(*[r["pages"] for r in ch])
                units.append(dict(base, id=f"OBJ_{tag}-{k}", kind=f"part {k} of {len(chunks)}", rows=ch, pages=pg,
                                  first_scan=min((s for c, s in pg if c == main_cote), default=first) + k * 0.001))
        elif n <= SMALL_ENTRIES and words < SMALL_WORDS:
            small[base["topic"]].append(dict(base, id=f"OBJ_{tag}", kind=single_kind))
        else:
            units.append(dict(base, id=f"OBJ_{tag}", kind=single_kind))
    # bundles of small objects of the same topic and folder, in page order
    for key, us in small.items():
        us.sort(key=order_key)
        cur = []
        for u in us + [None]:
            if u is not None and cur and len(cur) < BUNDLE_OBJECTS and sum(len(x["rows"]) for x in cur) + len(u["rows"]) <= BUNDLE_ENTRIES:
                cur.append(u)
                continue
            if cur:
                if len(cur) == 1:
                    units.append(cur[0])
                else:
                    tags_ = [t for x in cur for t in x["tags"]]
                    units.append(dict(cur[0], id="OBJ_" + "+".join(tags_), kind=f"bundle of {len(tags_)} objects",
                                      tags=tags_, objects=[n for x in cur for n in x["objects"]],
                                      rows=[r for x in cur for r in x["rows"]], pages=set().union(*[x["pages"] for x in cur])))
            cur = [u] if u is not None else []
    units.sort(key=order_key)
    excluded.sort(key=order_key)
    return units, excluded


PLAN_COLS = ["rank", "prompt_id", "kind", "tags", "objects", "topic", "vertical_touched", "cote", "year", "first_scan",
             "cotes_scans", "entries", "pro_entries", "work_entries", "codex_entries", "entry_words", "pages_cited",
             "open_question_entries", "span_pages", "expected_minutes", "status_on_pages", "eligible", "reason", "built"]


def plan():
    objs, items, idx = load()
    units, excluded = make_units(objs, items, idx)
    out = []
    for rank, u in enumerate(units + excluded, 1):
        rows = u["rows"]
        words = sum(r["words"] for r in rows)
        sc = collections.Counter(r["src"] for r in rows)
        built = OUT / u["id"]
        out.append(dict(rank=rank if u["kind"] != "excluded" else "", prompt_id=u["id"], kind=u["kind"],
                        tags=" ".join(u["tags"]), objects=" || ".join(u["objects"]), topic=u["topic"],
                        vertical_touched="yes" if u["topic"] in TOUCHED else "no", cote=u["cote"],
                        year=u["year"] if u["year"] != 9999 else "", first_scan=int(u["first_scan"]),
                        cotes_scans=cotes_scans_text(u["pages"]), entries=len(rows), pro_entries=sc["pro"],
                        work_entries=sc["work"], codex_entries=sc["codex"], entry_words=words, pages_cited=len(u["pages"]),
                        open_question_entries=sum(1 for r in rows if OPEN_KIND.search(r["kind"] or "")),
                        span_pages=len(sp) if (sp := object_span(u["pages"], idx) if u["kind"] != "excluded" else None) is not None else "",
                        expected_minutes=est_minutes(len(sp), sum(1 for r in rows if OPEN_KIND.search(r["kind"] or "")))
                        if sp is not None else "",
                        status_on_pages=" | ".join(objs[t]["row"].get("status_on_pages", "") for t in u["tags"])[:200],
                        eligible="no" if u["kind"] == "excluded" else "yes", reason=u.get("reason", ""),
                        built=str(built.relative_to(HERE)).replace("\\", "/") if built.exists() else ""))
    PLAN.write_text(W.tsv(out, PLAN_COLS), encoding="utf-8", newline="")
    el = [r for r in out if r["eligible"] == "yes"]
    print("plan:", len(out), "rows;", len(el), "prompts;", sum(int(r["entries"]) for r in el), "entries;",
          sum(int(r["expected_minutes"]) for r in el), "expected minutes;", len(out) - len(el), "objects left out")
    print("kinds:", collections.Counter(r["kind"].split(" of ")[0] if r["kind"].startswith(("part", "bundle")) else r["kind"]
                                        for r in out))
    print("left out:", collections.Counter(r["reason"].split(":")[0] for r in out if r["eligible"] == "no"))
    return units, objs, items, idx


# ------------------------------------------------------------------------------------------------ building a package
def context_rules(use="object"):
    """cote -> [(source path, arcname, description)] from CONTEXT_RULES.tsv, the rows for this use (or both)"""
    out = collections.defaultdict(list)
    if RULES.exists():
        for r in W.csv.DictReader(open(RULES, encoding="utf-8"), delimiter="\t"):
            if r["cote"].startswith("#") or r.get("use") not in (use, "both") or r["path"].startswith("@"):
                continue
            out[r["cote"]].append((W.D / r["path"], r["arcname"], r["description"]))
    return out


def topic_title(t):
    p = W.HIN / t / "TOPIC.md"
    if p.exists():
        first = p.read_text(encoding="utf-8").splitlines()[0]
        return first.split(":", 1)[1].strip() if ":" in first else first.strip("# ")
    return t


def short_name(name, n=90):
    name = re.sub(r"\s*\((?:cote|cotes)\s[^)]*\)\s*$", "", name).strip()
    if len(name) <= n:
        return name
    cut = name[:n].rsplit(" ", 1)[0].rstrip(",;:")
    return cut + " ..."


def hua_page_text(cote, scan):
    h = W.hua(cote).get(scan)
    if not h:
        return "", ""
    st, f = h
    s = f.read_text(encoding="utf-8", errors="replace").split("\\begin{document}", 1)[-1]
    ps = re.split(r"(\\page(?:range)?\{\d+\}(?:\{\d+\})?)", s)
    for k in range(1, len(ps), 2):
        a = [int(x) for x in re.findall(r"\d+", ps[k])]
        if a[0] + 1 <= scan <= (a[1] if len(a) > 1 else a[0]) + 1:
            return ps[k] + ps[k + 1].rstrip(), f.name
    return "", f.name


def route_name(x):
    return {"pro": "Pro first pass", "pro_b": "Pro first pass, second chat", "pro_cp": "Pro checkpoint",
            "claude2": "Claude second pass", "work1": "Work/Codex first reading", "work2": "Work second reading",
            "api": "API typescript transcription"}[x["route"]]


def assemble_cote(cote, idx):
    parts_, srcs = [], collections.Counter()
    for s in W.scans_of(cote):
        rd = idx.get((cote, s), [])
        f = W.first_reading(rd)
        if not f:
            parts_.append(f"% scan {s}: no reading on disk\n\\scanpage{{{s}}}\n% (not transcribed)\n")
            continue
        srcs[route_name(f)] += 1
        t = W.page_text(f)
        if "\\scanpage" not in t[:200]:
            t = f"\\scanpage{{{s}}}\n" + t
        parts_.append(f"% scan {s}: {route_name(f)} {f['id']} ({f['model']})\n" + t.rstrip() + "\n")
    head = f"% cote {cote}: {W.MAN[cote]['title']} ({W.MAN[cote]['date']}); the reading of each page as it stands on disk\n\\cotefile{{{cote}}}\n"
    return head + "\n".join(parts_), srcs


def build(uid, units, objs, items, idx, folder=None):
    u = next((x for x in units if x["id"] == uid), None)
    if u is None:
        raise SystemExit(f"{uid}: not an eligible prompt of the plan")
    S = uid
    folder, work = (folder or OUT / S), WORK / S
    W.PRIVACY.clear()
    if folder.exists():
        for p in folder.iterdir():
            p.unlink()
    folder.mkdir(parents=True, exist_ok=True)
    work.mkdir(parents=True, exist_ok=True)
    rows = u["rows"]
    tag_of_item = {i: t for t in u["tags"] for i in objs[t]["items"]}
    # ---- entries
    md = [f"# {S}: the note entries\n",
          f"{len(rows)} entries about " + ("these objects" if len(u["tags"]) > 1 else "this object") +
          ", in page order. Each entry is given in full as it stands in its file. The placement lines are the sweep's "
          "(horizontal sweep 1, Claude Opus 5.5 at effort max, 18 Nov 2026).\n"]
    trows = []
    for r in rows:
        e = entry(r["eid"], r["prow"])
        p = r["prow"]
        kind, src = source_of(r["eid"])
        who = {"pro": "GPT-6 Astra (ChatGPT Pro mode), notes of the transcription package " + src,
               "work": "GPT-6.2 Astra at reasoning effort max (ChatGPT Work), math notes of the folder " + src,
               "codex": "GPT-6 Astra at reasoning effort max (Codex web), notes of the folder " + src}[kind]
        rel = e["file"].replace("\\", "/").split("Documents/")[-1] if e["file"] else ""
        md.append(f"\n## {r['eid']}: {e['heading']}\n\n"
                  f"- object: {tag_of_item.get(r['item'], u['tags'][0])}, item {r['item']} of topic {p.get('topic') or p['_topic_dir']}\n"
                  f"- written by: {who}\n- file: `{rel}`, line {e['line']}\n"
                  f"- pages it is about: {cotes_scans_text(r['pages']) or 'none cited'}\n"
                  f"- kind: {p.get('kind', '')}\n- the sweep's placement: {p.get('object', '')}"
                  + (f"; his term: {p['his_term']}" if p.get("his_term") else "")
                  + f"; basis {p.get('basis', '')}; fidelity {p.get('fidelity', '')}"
                  + (f"; flag: {p['flag']}" if p.get("flag") else "") + "\n\n" + (e["text"].strip() or "(the entry's text was not found in its file)") + "\n")
        trows.append(dict(entry_id=r["eid"], tag=tag_of_item.get(r["item"], u["tags"][0]), item=r["item"],
                          topic=p.get("topic") or p["_topic_dir"], written_by=who, file=rel, line=e["line"],
                          pages=cotes_scans_text(r["pages"]), kind=p.get("kind", ""), words=e["words"],
                          sweep_object=p.get("object", ""), his_term=p.get("his_term", ""), basis=p.get("basis", ""),
                          fidelity=p.get("fidelity", ""), flag=p.get("flag", "")))
    obj_rows = [objs[t]["row"] for t in u["tags"]]
    gcols = list(obj_rows[0].keys())
    item_rows = [dict(items[i], tag=t) for t in u["tags"] for i in objs[t]["items"] if i in items]
    icols = ["tag", "item", "_topic", "object", "kind", "statement", "entries", "cotes_scans", "status_on_pages",
             "cross_topic", "flags"]
    chk = W.check_register()
    keys = [r["eid"] for r in rows] + [i for t in u["tags"] for i in objs[t]["items"]] + list(u["tags"])
    ck = [dict(x, checked=k) for k in dict.fromkeys(keys) for x in chk.get(k, [])]
    ent = [("README.md", ("# The entries of " + S + "\n\n- `ENTRIES.md`: every entry in full.\n- `ENTRIES.tsv`: the index.\n"
                          "- `OBJECT.tsv`: the global row of each object (GLOBAL_OBJECTS.tsv) and its items in the topics "
                          "(OBJECTS.tsv of each topic).\n"
                          f"- `CHECKS.tsv`: {len(ck)} rows of our check register (results_register/CHECK_REGISTER.tsv) "
                          "about these entries, items and objects: who checked what, how, with what result.\n").encode()),
           ("ENTRIES.md", "".join(md).encode("utf-8")),
           ("ENTRIES.tsv", W.tsv(trows, list(trows[0].keys())).encode("utf-8")),
           ("OBJECT.tsv", (W.tsv(obj_rows, gcols) + "\n" + W.tsv(item_rows, icols)).encode("utf-8")),
           ("CHECKS.tsv", W.tsv(ck, ["checked", "id", "date_utc", "who", "how", "result", "where", "source_file"]).encode("utf-8"))]
    ent_names = W.zip_parts(folder, f"{S}_entries", ent)
    # ---- pages
    cite = collections.Counter()
    for r in rows:
        for pg in r["pages"]:
            cite[pg] += 1
    pages = sorted(cite, key=lambda cs: (W.cote_key(cs[0]), cs[1]))
    pm, pas = [], [f"# {S}: the passages the entries cite\n\nFor each page: the reading a pass starts from (the Claude second "
                   "pass where one exists, else the first reading), then the other readings on disk, then the text of "
                   "witness H (the Commutator project of Michel Hua, github.com/Commutator-IO/grothendieck-project, commit "
                   f"`{W.HUA_COMMIT}`, an AI transcription by Claude Opus 5 and Claude Opus 5.5; their page n is our scan "
                   "n + 1; a witness only, in their macros). All are AI readings of the same scans; the scan decides.\n"]
    for c, s in pages:
        rd = idx.get((c, s), [])
        f = W.first_reading(rd)
        pas.append(f"\n## cote {c}, scan {s} (cited by {cite[(c, s)]} entr{'y' if cite[(c, s)] == 1 else 'ies'})\n")
        others = [x for x in rd if x is not f]
        for x in ([f] if f else []) + others:
            if x["route"] == "pro_cp" and f is not None:
                continue
            d = W.run_date(x["route"], x["id"])
            pas.append(f"\n**{route_name(x)}** `{x['id']}` ({x['model']}{', ' + d if d else ''}):\n\n```latex\n"
                       f"{W.page_text(x).strip()}\n```\n")
        ht, hb = hua_page_text(c, s)
        if ht:
            pas.append(f"\n**Witness H** (`{hb}`):\n\n```latex\n{ht.strip()}\n```\n")
        pm.append(dict(cote=c, scan=s, cited_by=cite[(c, s)], first_reading=(f"{route_name(f)} {f['id']}" if f else "none"),
                       first_model=f["model"] if f else "", other_readings="; ".join(f"{route_name(x)} {x['id']} ({x['model']})" for x in others),
                       hua=(W.hua(c).get(s) or ("nothing",))[0], image="", page="cited"))
    # images (B2 of the verdict on OBJ_H035, 19 Nov 2026): every page of the object's span, whole, in page order
    span = sorted(object_span(pages, idx), key=lambda cs: (W.cote_key(cs[0]), cs[1]))
    for c, s in span:
        if (c, s) not in cite:
            rd = idx.get((c, s), [])
            f = W.first_reading(rd)
            pm.append(dict(cote=c, scan=s, cited_by=0, first_reading=(f"{route_name(f)} {f['id']}" if f else "none"),
                           first_model=f["model"] if f else "",
                           other_readings="; ".join(f"{route_name(x)} {x['id']} ({x['model']})" for x in rd if x is not f),
                           hua=(W.hua(c).get(s) or ("nothing",))[0], image="", page="span"))
    pm.sort(key=lambda r: (W.cote_key(r["cote"]), r["scan"]))
    groups, imaged = [], set()
    for c, s in span:
        im = W.page_images(c, s, pieces=0)
        if im:
            groups.append([(f"{c}_scan{s:03d}.jpg", im[0][1])])
            imaged.add((c, s))
            for r in pm:
                if r["cote"] == c and r["scan"] == s:
                    r["image"] = f"{c}_scan{s:03d}.jpg"
    scan_names = W.zip_parts(folder, f"{S}_scans", groups, stored=True) if groups else []
    cotes = sorted({c for c, s in pages}, key=W.cote_key)
    tr, trsrc = [], {}
    for c in cotes:
        txt, srcs = assemble_cote(c, idx)
        tr.append((f"transcriptions/cote_{c}.tex", txt.encode("utf-8")))
        trsrc[c] = srcs
    pz = [("README.md", (f"# The pages of {S}\n\n- `PASSAGES.md`: every page the entries cite, with every reading on disk "
                         "and witness H.\n- `page_map.tsv`: per page of the object's span, whether the entries cite it "
                         "(`cited`) or it belongs to the numbered sequence that holds the cited pages (`span`; its reading is "
                         "in `transcriptions/`), the readings, Hua's state (`text`, `desc` = only a "
                         "description, `nothing`) and the image attached.\n- `transcriptions/cote_<C>.tex`: the whole "
                         "folder, each page in the reading a pass starts from, with a comment naming it.\n- `PREAMBLE.tex`: "
                         "our macros.\n").encode()),
          ("PASSAGES.md", "".join(pas).encode("utf-8")),
          ("page_map.tsv", W.tsv(pm, list(pm[0].keys()) if pm else ["cote"]).encode("utf-8")),
          ("PREAMBLE.tex", PREAMBLE.read_bytes())] + tr
    page_names = W.zip_parts(folder, f"{S}_pages", pz)
    # ---- context
    rules = context_rules()
    topics = sorted({r["prow"].get("topic") or r["prow"]["_topic_dir"] for r in rows}, key=lambda t: TOPIC_ORDER.index(t) if t in TOPIC_ORDER else 99)
    near = []
    lk = list(W.csv.DictReader(open(W.SWEEP / "GLOBAL/LINKS.tsv", encoding="utf-8"), delimiter="\t"))
    linked = {x["to_tag"] for x in lk if x.get("tag") in u["tags"] and x.get("to_tag")} | {x["tag"] for x in lk if x.get("to_tag") in u["tags"]}
    themes = {objs[t]["row"].get("theme") for t in u["tags"]} - {""}
    for t, o in objs.items():
        rel = []
        if t in u["tags"]:
            continue
        if set(o["row"]["topics"].split()) & set(topics):
            rel.append("same topic")
        if t in linked:
            rel.append("linked in the sweep")
        if o["row"].get("theme") and o["row"]["theme"] in themes:
            rel.append("same theme " + o["row"]["theme"])
        if rel:
            # B4 of the verdict on OBJ_H035: the statements, so that a link can carry its evidence
            st = list(dict.fromkeys(items[i]["statement"].strip() for i in o["items"]
                                    if i in items and (items[i].get("statement") or "").strip()))
            near.append(dict(tag=t, relation="; ".join(rel), object=o["row"]["object"], topics=o["row"]["topics"],
                             entries=o["row"]["n_entries"], cotes_scans=o["row"]["cotes_scans"][:200],
                             status_on_pages=o["row"]["status_on_pages"][:120],
                             statements=" || ".join(st)[:1500]))
    cfiles, clist = [], []
    for t in topics:
        p = W.HIN / t / "TOPIC.md"
        if p.exists():
            cfiles.append((f"topics/{t}_TOPIC.md", p.read_bytes()))
    for c in cotes:
        for src, arc, desc in rules.get(c, []):
            if src.exists() and arc not in {a for a, _ in cfiles}:
                cfiles.append((arc, src.read_bytes()))
                clist.append(f"`{arc}`: {desc}")
    cfiles.append(("OBJECTS_NEARBY.tsv", W.tsv(near, ["tag", "relation", "object", "topics", "entries", "cotes_scans",
                                                     "status_on_pages", "statements"]).encode("utf-8")))
    th = [x for x in W.csv.DictReader(open(W.SWEEP / "GLOBAL/THEMES.tsv", encoding="utf-8"), delimiter="\t") if x["theme"] in themes]
    if th:
        cfiles.append(("THEMES.tsv", W.tsv(th, list(th[0].keys())).encode("utf-8")))
    s3_topics = [t for t in dict.fromkeys([u["topic"]] + topics) if (W.SWEEP3 / t).is_dir()]
    s3_lines = []
    for t in s3_topics:
        cfiles += W.sweep3_members(t)
        s3_lines.append(W.SWEEP3_LINE.format(t=t))
    readme_c = (f"# The context of {S}\n\n- `topics/<SA>_TOPIC.md`: the catalogue of each topic the entries come from (cotes, "
                "titles, what is transcribed and by which route).\n- `OBJECTS_NEARBY.tsv`: the other objects of the same "
                "topics, and those the sweep linked to this one or put in the same theme, with their tags and the "
                "sweep's statements of each (`statements`, separated by ` || `): the links of the entry are made to "
                "these tags, with the statement that is their evidence.\n" + ("- `THEMES.tsv`: the sweep's theme rows.\n" if th else "")
                + "".join(f"- {x}\n" for x in clist) + "".join(f"- {x}.\n" for x in s3_lines))
    cfiles.insert(0, ("README.md", readme_c.encode("utf-8")))
    ctx_names = W.zip_parts(folder, f"{S}_context", cfiles)
    # ---- results (opened last)
    reg = W.register_rows()
    hit = []
    for r in reg:
        for c in cotes:
            ss = [s for cc, s in pages if cc == c]
            if W.places_cite(r.get("his_places", ""), c, ss):
                hit.append(dict(tag=r["tag"], run=r["run"], status=r["status"], statement=r["statement"],
                                where_proved=r["where_proved"], his_places=r["his_places"], check_events=r["check_events"],
                                check_types=r["check_types"]))
                break
    hit = hit[:400]
    rz = [("README.md", (f"# Our results that cite the folders of {S}\n\nThe statements of our research runs (results_register/"
                         f"REGISTER.tsv, built 18 Nov 2026 by script from each run's newest results table) whose `his_places` "
                         f"cite these folders and pages: {len(hit)} rows. The status is the run's own claim unless "
                         "`check_events` records a check. Open this only after the entry is written.\n").encode()),
          ("RESULTS_CITING.tsv", W.tsv(hit, ["tag", "run", "status", "statement", "where_proved", "his_places",
                                             "check_events", "check_types"]).encode("utf-8"))]
    res_names = W.zip_parts(folder, f"{S}_results", rz)
    # ---- prompt
    t = TEMPLATE.read_text(encoding="utf-8")
    multi = len(u["tags"]) > 1
    olist = []
    for tg in u["tags"]:
        g = objs[tg]["row"]
        stmts = [items[i]["statement"] for i in objs[tg]["items"] if i in items and items[i].get("statement")]
        tnames = "; ".join(topic_title(x) for x in g["topics"].split())
        olist.append(f"- **{tg}**: {g['object']} (in the archive's topic {tnames})." + (f" The sweep's one-line statement: {stmts[0]}" if stmts else ""))
    by_c = collections.defaultdict(list)
    for c, s in pages:
        by_c[c].append(s)
    fl = "\n".join(f"- cote {c}, « {W.MAN[c]['title']} » ({W.MAN[c]['date']}): scans {compress(v)}" for c, v in
                   sorted(by_c.items(), key=lambda kv: W.cote_key(kv[0])))
    sc = collections.Counter(r["src"] for r in rows)
    scope = (f"The entries cite {len(pages)} pages of {len(by_c)} folder{'s' if len(by_c) > 1 else ''}:\n{fl}\n\n"
             f"There are {len(rows)} entries: " + ", ".join(f"{n} {k}" for k, n in (("from Pro's notes", sc['pro']),
                                                                                   ("from Work's math notes", sc['work']),
                                                                                   ("from Codex's notes", sc['codex'])) if n) + ".")
    if u["kind"].startswith("part"):
        k, n = re.findall(r"\d+", u["kind"])[:2]
        scope += (f" This is part {k} of {n} of the object: its entries are too many for one run, so each part takes a share "
                  "of them, and a script merges the parts. Write the entry for the statements of this part's pages, and "
                  f"give ids that cannot collide with the other parts: `{u['tags'][0]}.{k}.<n>`.")
    if multi and "sharing" in u["kind"]:
        scope += (" The sweep placed many of the same entries under these objects, so one run takes them together. Give "
                  "each its own entry, or one entry for both where the mathematics shows they are one object, and say "
                  "which.")
    elif multi:
        scope += (" These objects are small and belong to the same topic, so one run takes them together; each gets its "
                  "own entry.")
    if len(scan_names) > 1:
        sf = ", ".join(f"`{n}`" for n in scan_names[:-1]) + f" and `{scan_names[-1]}` (unpack them into the same folder)"
    else:
        sf = f"`{scan_names[0]}`" if scan_names else "(no images)"
    left = sum(1 for cs in pages if cs not in imaged)
    rep = {"{S}": S,
           "{TITLE_OBJECTS}": (f"{len(u['tags'])} objects ({', '.join(u['tags'])})" if multi else u["tags"][0] + ", " + short_name(u["objects"][0]) + (f" (part {re.findall(r'[0-9]+', u['kind'])[0]})" if u["kind"].startswith("part") else "")),
           "{OBJECT_LIST}": "\n".join(olist), "{SCOPE}": scope,
           "{THIS_OBJECT}": "these objects" if multi else "this object",
           "{ID_PATTERN}": ("<tag>.<n>, by the object's tag" if multi else (f"{u['tags'][0]}.{re.findall(r'[0-9]+', u['kind'])[0]}.<n>" if u["kind"].startswith("part") else f"{u['tags'][0]}.<n>")),
           "{ATTACH_NOTE}": "", "{SCANS_FILES}": sf, "{N_SCANS}": str(len(groups)),
           "{SCANS_LEFT}": (f"The other {left} cited pages have no image here; their readings are in `PASSAGES.md`. " if left > 0 else ""),
           "{CONTEXT_LIST}": ("It holds the catalogue of the topic, the neighbouring objects with their tags, and "
                              + ("his published text on the subject: " + "; ".join(clist) + "." if clist else
                                 "no text of his published work (none of ours matches these folders; find the passages of EGA, SGA or his papers that these pages draft or anticipate in the literature, and cite them by exact locator).")
                              + "".join(f" It also holds {x}." for x in s3_lines)),
           "{ENTRY_PER_OBJECT}": ", one section per object, each in the eight parts below" if multi else ""}
    for k, v in rep.items():
        t = t.replace(k, v)
    left_ph = re.findall(r"\{[A-Z_]{3,}\}", t)
    if left_ph:
        raise SystemExit(f"{S}: placeholders left: {left_ph}")
    t = W.lintsafe(t)
    (folder / "PROMPT.md").write_text(t, encoding="utf-8", newline="\n")
    ok, msg = W.lint(folder / "PROMPT.md", "--lint-math")
    files = sorted(p.name for p in folder.iterdir())
    sizes = {p.name: round(p.stat().st_size / 1e6, 2) for p in sorted(folder.iterdir())}
    readme = (f"# {S}: the foundational entry for {', '.join(u['tags'])} (ChatGPT Pro upload folder)\n\n"
              f"Upload every file of this folder except this README in a new ChatGPT chat with GPT-6 Astra in Pro mode, "
              f"`PROMPT.md` as a file, no text typed. {len(rows)} entries, {len(pages)} pages cited, a span of "
              f"{len(span)} pages, {len(groups)} images. Kind: {u['kind']}.\n\n## The objects\n\n" + "\n".join(olist) + "\n\n## Files\n\n"
              + "\n".join(f"- `{n}` ({sizes[n]} MB)" for n in files if n != "README.md") +
              "\n\n## Context (the subject's own, chosen by rule)\n\n" + readme_c.split("\n", 2)[2] +
              f"\n## Results (opened last by the run)\n\n- {len(hit)} statements of our runs whose `his_places` cite these folders.\n\n"
              "## Provenance\n\n- **Scans:** Université de Montpellier, fonds Grothendieck (grothendieck.umontpellier.fr); "
              "cotes and scan numbers are theirs. Rendered from the archive PDFs as in the first-pass packages.\n"
              "- **Entries:** the notes of our transcription runs (GPT-6 Astra (ChatGPT Pro mode); GPT-6.2 Astra at "
              "reasoning effort max (ChatGPT Work); GPT-6 Astra at reasoning effort max (Codex web)), placed by horizontal "
              "sweep 1 (Claude Opus 5.5 at effort max, 18 Nov 2026).\n"
              f"- **Witness H:** the Commutator project of Michel Hua, github.com/Commutator-IO/grothendieck-project, commit "
              f"`{W.HUA_COMMIT}`, an AI transcription by Claude Opus 5 and Claude Opus 5.5, read again in part by Claude "
              "Fable 5.2; used as a witness and credited; nothing is sent to that project.\n"
              f"- **Built** {W.NOW():%Y-%m-%d %H:%M} UTC by `working_through_20261118/build_object_prompts.py` (Claude Opus "
              f"5.5 at effort max). Lint (--lint-math): {'pass' if ok else 'FAIL'}.\n")
    (folder / "README.md").write_text(readme, encoding="utf-8", newline="\n")
    bj = dict(id=S, kind=u["kind"], tags=u["tags"], entries=len(rows), pages=len(pages), images=len(groups),
              privacy=dict(W.PRIVACY), span_pages=len(span),
              span=cotes_scans_text(span),
              expected_minutes=est_minutes(len(span), sum(1 for r in rows if OPEN_KIND.search(r["kind"] or ""))),
              topic=u["topic"],
              sizes_mb=sizes, lint=msg, ok=ok and all(v < 450 for v in sizes.values()) and len(files) <= 20,
              results_rows=len(hit), context=clist, built=f"{W.NOW():%Y-%m-%d %H:%M:%SZ}",
              transcription_routes={c: dict(v) for c, v in trsrc.items()})
    (work / "BUILD.json").write_text(json.dumps(bj, indent=1, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({k: bj[k] for k in ("id", "entries", "pages", "images", "sizes_mb", "lint", "ok")}, ensure_ascii=False))
    return bj


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in ("plan", "build"):
        raise SystemExit(__doc__)
    units, objs, items, idx = plan()
    if sys.argv[1] == "build":
        ids = sys.argv[2:]
        if ids[:1] == ["--next"]:
            n = int(ids[1])
            ids = [u["id"] for u in units if not (OUT / u["id"]).exists()][:n]
        for i in ids:
            build(i, units, objs, items, idx)
        plan()
