"""Build the per-folder working-through prompts (18 Nov 2026): GPT-6 Astra (ChatGPT Pro mode) works through the
mathematics of one range of one folder in its own terms, consuming every node on it (the readings, the notes, the
sweep's objects, the check records), with the scans for the reading wherever the mathematics depends on it.

Two variants of the same range (the user, 18 Nov ~16:2x UTC, through the coordinator: pilot both on the same range,
compare quality and time, then choose or combine):
- A, the companion-coded pass (PROMPT_TEMPLATE.md): the units in the companion's format (headnote, keyed notes, status
  blocks), the sort into the handbook's tag space (ITEMS.tsv) and suggested links from units to tags (LINKS.tsv);
- B, the foundational check (PROMPT_TEMPLATE_B.md): the same nodes and the same reading rule, the mathematics only.
Both: scan checks on the crop ("check scan" / "scan error" / "undecided" rows; the ink decides), claims decided under
the push rule and the dated ledger, every entry given a verdict, our results opened last. The full second visual pass
of the plan's section 3 is kept as PROMPT_TEMPLATE_FULL_READING.md (not built by default).

Ranges (UNITS_PLAN.tsv): every folder with a first reading of at least 90 % of its non-blank scans (outside La Longue
Marche and the Dérivateurs manuscript, which are edited). Where Work's math notes give draft units
(UNITS_DRAFT_20261118.tsv), a range is one Work folder or a slice of one: 8-20 draft units, a larger folder split at a
unit boundary, a smaller one merged with the next folder of the cote. Elsewhere a dynamic programme cuts 8-13 pages:
a cut between two pages costs the note entries that cite pages on both sides of it (within two pages), half of each
object that goes on across it, twice each Work unit "Scans a-b" that spans it, and less where the next page opens with
a heading; a range costs its distance from a load of 10 (a page weighs 0.6, plus 0.4 for each 250 words of its
reading, up to 1.6). A range of fewer than four pages joins its smaller neighbour.

Order: the archive topics the vertical research never touched first, in the archive's order; then the stratified
spaces, Pursuing Stacks, around Pursuing Stacks, around La Longue Marche, the Dérivateurs; within a topic, his
chronological order (the folder's date, the cote, the first scan).

usage: python -I -B build_working_through.py plan
       python -I -B build_working_through.py build WT_22_013-022 [more range ids] [--variant A|B|AB]
       python -I -B build_working_through.py build --cote 22 [--variant ...]   |   build --next N [--variant ...]
Upload folders: units/WTA_<range>/ and units/WTB_<range>/ (flat: PROMPT.md, the zips, README.md);
work files: _work/units/<id>/BUILD.json.
Written by Claude Opus 5.5 at effort max (agent a11a6de3, no sub-agents), 18 Nov 2026."""
import collections
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import wt_common as W  # noqa: E402
import build_object_prompts as O  # noqa: E402  (entries, pages of entries, context rules, assembly of a folder)

HERE = W.HERE
OUT = HERE / "units"
WORK = HERE / "_work" / "units"
TEMPLATES = {"A": HERE / "PROMPT_TEMPLATE.md", "B": HERE / "PROMPT_TEMPLATE_B.md", "F": HERE / "PROMPT_TEMPLATE_FULL_READING.md"}
PLAN = HERE / "UNITS_PLAN.tsv"
DRAFT = W.T / "UNITS_DRAFT_20261118.tsv"
CHECK_REGISTER = W.D / "results_register/CHECK_REGISTER.tsv"
COMPLETE = 0.90
MIN_PAGES, MAX_PAGES, TARGET_LOAD = 8, 13, 10.0
DRAFT_MIN, DRAFT_MAX, DRAFT_MAX_PAGES = 8, 20, 20
TOUCHED_ORDER = ["Espaces stratifiés", "Pursuing stacks", "Autour de Pursuing stacks",
                 "Autour de La \"Longue Marche\"", "Dérivateurs"]
CONCORDANCE_MAX = 80


def archive_topics():
    """the archive's topics in its order, the touched ones last"""
    seen = []
    for c, r in sorted(W.MAN.items(), key=lambda kv: W.cote_key(kv[0])):
        if r["topic"] not in seen:
            seen.append(r["topic"])
    touched = [t for k in TOUCHED_ORDER for t in seen if t.startswith(k)]
    return [t for t in seen if t not in touched] + touched, set(touched)


TOPICS, TOUCHED = archive_topics()


def sa_of_cote():
    """cote -> the sweep topic (SA..) whose run took its packages, else the first that lists it"""
    took, listed = {}, {}
    for t in sorted(W.HIN.glob("SA*")):
        p = t / "TOPIC.md"
        if not p.exists():
            continue
        for line in p.read_text(encoding="utf-8").splitlines():
            m = re.match(r"\|\s*([0-9][0-9-]*)\s*\|", line)
            if m:
                listed.setdefault(m.group(1), t.name)
                if not line.rstrip().endswith("other part |"):
                    took.setdefault(m.group(1), t.name)
    return {**listed, **took}


SA_OF = sa_of_cote()


def items_of(r):
    return [x for x in re.split(r"[,;\s]+", r["item"]) if x]


# ------------------------------------------------------------------------------------------------ the data
def load():
    idx = W.build_index()
    by_page = collections.defaultdict(set)   # (cote, scan) -> entry ids
    erow, epages = {}, {}
    tags, item_tag = W.global_objects()
    for r in W.placements():
        eid = r["entry_id"]
        if eid in erow:
            continue
        e = O.entry(eid, r)
        pg = O.entry_pages(eid, r, e["text"], idx)
        erow[eid] = r
        epages[eid] = pg
        for p in pg:
            by_page[p].add(eid)
    du = collections.defaultdict(list)
    for r in W.csv.DictReader(open(DRAFT, encoding="utf-8"), delimiter="\t"):
        du[r["folder"]].append(dict(unit=r["unit"], scans=sorted(W.scans_in(r["scans"])), title=r["title"],
                                    cote=r["cote"], source=r["source"]))
    checks = W.check_register()
    return dict(idx=idx, blanks=W.blanks(), by_page=by_page, erow=erow, epages=epages, tags=tags, item_tag=item_tag,
                du=du, checks=checks, wranges=work_unit_ranges())


def work_unit_ranges():
    """cote -> [(a, b)]: the 'Scans a-b' units of the Work math notes ("What the pages do")"""
    out = collections.defaultdict(list)
    folders = {r["folder"] for r in W.work_rows()}
    for d in (W.CW / "returns").iterdir():
        if (d / "out" / f"{d.name}_mathnotes.md").exists():
            folders.add(d.name)
    for f in folders:
        p = W.work_math_notes_path(f)
        if p is None or not p.exists():
            continue
        a = W.ASSIGN.get(f) or W.ASSIGN.get(re.sub(r"_\d+$", "", f)) or {}
        cote = a.get("cote")
        if not cote:
            continue
        for b in W.md_blocks(p):
            if b[0] == 2 and b[1].lower().startswith("what the pages do"):
                for x, y in re.findall(r"\*\*[^*\n]*?[Ss]cans?\s+0*(\d{1,3})\s*[–-]\s*0*(\d{1,3})[^*\n]*\*\*", b[3]):
                    x, y = int(x), int(y)
                    if 0 < y - x <= 12:
                        out[cote].append((x, y))
    return out


HEADING = re.compile(r"^(\\uline\{|\\uuline\{|\\textbf|\\section|§|N°|n°|\d+[).]\s|\d+\.\d+|[IVX]+[.)]\s|Chap|Questions|"
                     r"Th[ée]or[èe]me|Prop|Lemme|Appendice|Remarque|Corollaire|D[ée]finition|Exemple|\\margin\{.*\d{2,4}\})")
_INFO = {}


def page_info(cote, D):
    """per scan: blank, reading, words, weight, opens with a heading"""
    if cote in _INFO:
        return _INFO[cote]
    info = {}
    for s in W.scans_of(cote):
        rd = D["idx"].get((cote, s), [])
        f = W.first_reading(rd)
        blank = s in D["blanks"].get(cote, set())
        t = W.page_text(f) if f else ""
        wd = W.words(t) if t else 0
        first = ""
        for line in t.splitlines():
            l = line.strip()
            if not l or l.startswith("%") or l.startswith("\\scanpage") or l.startswith("\\mspage") or l.startswith("\\cotefile"):
                continue
            first = l
            break
        strong = bool(HEADING.match(first))
        weak = (not strong and 2 < len(first) <= 45 and not re.search(r"[.,;:]$", first)
                and bool(re.match(r"[A-ZÀ-Ý0-9]", re.sub(r"^\\[a-z]+\{", "", first))))
        info[s] = dict(blank=blank and not f, reading=f, words=wd,
                       weight=0.0 if (blank and not f) else (1.0 if not f else 0.6 + 0.4 * min(2.5, wd / 250)),
                       heading=1.5 if strong else (1.0 if weak else 0.0), routes=sorted({x["route"] for x in rd}))
    _INFO[cote] = info
    return info


def cut_run(cote, scans, info, D):
    """[(first scan, last scan)] of one run of consecutive scans, by the dynamic programme of the docstring"""
    nb = [s for s in scans if not info[s]["blank"]]
    if len(nb) <= MAX_PAGES:
        return [(scans[0], scans[-1])], {}

    def items_on(ss_):
        out = set()
        for s in ss_:
            for eid in D["by_page"].get((cote, s), ()):
                pg = {x for c, x in D["epages"][eid] if c == cote}
                if len(pg) <= 12:
                    out.update(items_of(D["erow"][eid]))
        return out

    def straddle(i):  # cut between scans[i] and scans[i+1]
        left = set(scans[max(0, i - 1):i + 1])
        right = set(scans[i + 1:i + 3])
        n = 0
        for s in left:
            for eid in D["by_page"].get((cote, s), ()):
                pg = {x for c, x in D["epages"][eid] if c == cote}
                if len(pg) <= 12 and pg & right:
                    n += 1
        cont = len(items_on(left) & items_on(right))
        u = sum(1 for a, b in D["wranges"].get(cote, []) if a <= scans[i] < b)
        return max(0.0, n + 0.5 * cont + 2 * u - info[scans[i + 1]]["heading"])

    bc = [straddle(i) for i in range(len(scans) - 1)] + [0.0]
    INF = float("inf")
    best = [INF] * (len(scans) + 1)
    back = [0] * (len(scans) + 1)
    best[0] = 0.0
    cnt, load_ = [0], [0.0]
    for s in scans:
        cnt.append(cnt[-1] + (0 if info[s]["blank"] else 1))
        load_.append(load_[-1] + info[s]["weight"])
    for j in range(1, len(scans) + 1):
        for i in range(j - 1, -1, -1):
            n = cnt[j] - cnt[i]
            if n > MAX_PAGES:
                break
            if n < MIN_PAGES or best[i] == INF:
                continue
            c = best[i] + 0.5 * (load_[j] - load_[i] - TARGET_LOAD) ** 2 + 3 * bc[j - 1]
            if c < best[j]:
                best[j], back[j] = c, i
    if best[len(scans)] == INF:
        return [(scans[0], scans[-1])], {}
    units, j = [], len(scans)
    while j > 0:
        i = back[j]
        units.append((scans[i], scans[j - 1]))
        j = i
    units.reverse()
    return units, {scans[i]: bc[i] for i in range(len(scans))}


def ranges_of(cote, D):
    """the ranges of a cote (see the docstring): [dict(a, b, basis, folders, units)], the page info, the cut costs"""
    info = page_info(cote, D)
    scans = W.scans_of(cote)
    DU = D["du"]
    lab = []
    for s in scans:
        f = info[s]["reading"]
        if info[s]["blank"] and not f:
            lab.append(None)
        elif f and f["route"] == "work1" and f["id"] in DU:
            lab.append(("draft", f["id"]))
        else:
            lab.append(("cut", ""))
    for i in range(len(lab)):
        if lab[i] is None and i > 0:
            lab[i] = lab[i - 1]
    for i in range(len(lab) - 1, -1, -1):
        if lab[i] is None:
            lab[i] = lab[i + 1] if i + 1 < len(lab) and lab[i + 1] else ("cut", "")
    runs = []
    for s, l in zip(scans, lab):
        if runs and runs[-1][0] == l:
            runs[-1][1].append(s)
        else:
            runs.append([l, [s]])
    out, bc = [], {}
    for (kind, folder), ss in runs:
        if kind == "draft":
            units = [u for u in DU[folder] if u["scans"] and min(u["scans"]) in ss]
            n = len(units)
            if n > DRAFT_MAX:
                k = -(-n // DRAFT_MAX)
                size = -(-n // k)
                chunks = [units[i:i + size] for i in range(0, n, size)]
                starts = [ss[0]] + [min(ch[0]["scans"]) for ch in chunks[1:]]
                for i, ch in enumerate(chunks):
                    a = starts[i]
                    b = (starts[i + 1] - 1) if i + 1 < len(chunks) else ss[-1]
                    out.append(dict(a=a, b=b, basis=f"draft units of {folder}", folders=[folder], units=[u["unit"] for u in ch]))
            else:
                out.append(dict(a=ss[0], b=ss[-1], basis=f"draft units of {folder}", folders=[folder],
                                units=[u["unit"] for u in units]))
        else:
            us, b2 = cut_run(cote, ss, info, D)
            bc.update(b2)
            for a, b in us:
                out.append(dict(a=a, b=b, basis="cut by script", folders=[], units=[]))

    def npages(r):
        return sum(1 for s in scans if r["a"] <= s <= r["b"] and not info[s]["blank"])

    def joined(x, y):
        basis = x["basis"] if x["basis"] == y["basis"] else (
            "draft units of " + ", ".join(x["folders"] + y["folders"]) if x["folders"] and y["folders"] and
            x["basis"].startswith("draft") and y["basis"].startswith("draft") else x["basis"] + " + " + y["basis"])
        return dict(a=x["a"], b=y["b"], basis=basis, folders=x["folders"] + y["folders"], units=x["units"] + y["units"])

    changed = True
    while changed:
        changed = False
        for i in range(len(out) - 1):
            x, y = out[i], out[i + 1]
            if (x["basis"].startswith("draft") and y["basis"].startswith("draft")
                    and min(len(x["units"]), len(y["units"])) < DRAFT_MIN
                    and len(x["units"]) + len(y["units"]) <= DRAFT_MAX and npages(x) + npages(y) <= DRAFT_MAX_PAGES):
                out[i:i + 2] = [joined(x, y)]
                changed = True
                break
        if changed:
            continue
        for i, x in enumerate(out):
            if npages(x) < 4 and len(out) > 1:
                if i == 0:
                    j = 1
                elif i == len(out) - 1:
                    j = i - 1
                else:
                    j = i - 1 if npages(out[i - 1]) <= npages(out[i + 1]) else i + 1
                lo, hi = sorted([i, j])
                out[lo:hi + 1] = [joined(out[lo], out[hi])]
                changed = True
                break
    return out, info, bc


def coverage(cote, D):
    sc = W.scans_of(cote)
    nb = [s for s in sc if s not in D["blanks"].get(cote, set())]
    have = [s for s in nb if W.first_reading(D["idx"].get((cote, s), []))]
    return len(have), len(nb)


UNIT_COLS = ["rank", "unit_id", "cote", "archive_topic", "sweep_topic", "vertical_touched", "year", "folder_title",
             "unit", "scans", "pages", "basis", "draft_units", "blank_scans", "missing_scans", "first_reading",
             "second_readings", "hua_text", "note_entries", "words", "load", "cut_cost_after", "expected_minutes",
             "images_mb_est", "built"]


def expected_minutes(load, entries):
    return int(round(8 + 3.2 * load + 0.4 * min(entries, 60)))


def plan(D=None):
    D = D or load()
    rows = []
    for c, r in W.MAN.items():
        if c.startswith("140-") or c.startswith("157-") or not W.scans_of(c):
            continue
        h, nb = coverage(c, D)
        if nb == 0 or h / nb < COMPLETE:
            continue
        rs, info, bc = ranges_of(c, D)
        for k, x in enumerate(rs, 1):
            a, b = x["a"], x["b"]
            ss = [s for s in W.scans_of(c) if a <= s <= b]
            pages = [s for s in ss if not info[s]["blank"]]
            missing = [s for s in pages if not info[s]["reading"]]
            fr = collections.Counter(info[s]["reading"]["route"] for s in pages if info[s]["reading"])
            sec = collections.Counter(rt for s in pages for rt in info[s]["routes"]
                                      if rt in ("work2", "claude2", "pro_b") or (rt in ("pro", "work1") and info[s]["reading"]
                                                                                 and info[s]["reading"]["route"] != rt))
            ht = sum(1 for s in pages if (W.hua(c).get(s) or ("",))[0] == "text")
            ents = set().union(*[D["by_page"].get((c, s), set()) for s in ss]) if ss else set()
            words = sum(info[s]["words"] for s in pages)
            load_ = sum(info[s]["weight"] for s in ss)
            uid = f"WT_{c}_{a:03d}-{b:03d}"
            rows.append(dict(unit_id=uid, cote=c, archive_topic=r["topic"], sweep_topic=SA_OF.get(c, ""),
                             vertical_touched="yes" if r["topic"] in TOUCHED else "no",
                             year=W.year_of(c) if W.year_of(c) != 9999 else "", folder_title=r["title"][:120],
                             unit=f"{k} of {len(rs)}", scans=f"{a}-{b}", pages=len(pages), basis=x["basis"],
                             draft_units=len(x["units"]), blank_scans=O.compress([s for s in ss if info[s]["blank"]]),
                             missing_scans=O.compress(missing),
                             first_reading="; ".join(f"{k_} {v}" for k_, v in fr.most_common()),
                             second_readings="; ".join(f"{k_} {v}" for k_, v in sec.most_common()), hua_text=ht,
                             note_entries=len(ents), words=words, load=round(load_, 1), cut_cost_after=bc.get(b, 0.0),
                             expected_minutes=expected_minutes(load_, len(ents)),
                             images_mb_est=round(1.6 * len(ss) + 1.4, 1),
                             built=" ".join(f"units/WT{v}_{uid[3:]}" for v in "AB" if (OUT / f"WT{v}_{uid[3:]}").exists()),
                             _key=(TOPICS.index(r["topic"]) if r["topic"] in TOPICS else 99, W.year_of(c), W.cote_key(c), a),
                             _units=x["units"], _folders=x["folders"]))
    rows.sort(key=lambda x: x["_key"])
    for i, x in enumerate(rows, 1):
        x["rank"] = i
    PLAN.write_text(W.tsv(rows, UNIT_COLS), encoding="utf-8", newline="")
    print("ranges:", len(rows), "in", len({x['cote'] for x in rows}), "folders;", sum(x["pages"] for x in rows), "pages;",
          sum(x["expected_minutes"] for x in rows), "expected minutes;",
          sum(1 for x in rows if x["basis"].startswith("draft")), "on draft units;",
          "missing pages to transcribe:", sum(len(W.scans_in(x["missing_scans"])) for x in rows))
    print("pages per range:", sorted(collections.Counter(x["pages"] for x in rows).items()))
    return rows, D


# ------------------------------------------------------------------------------------------------ one package
WITNESS_FINDINGS = {
    "pro": "earlier checks found about 1 to 2.5 errors per 100 words on his dense hand, mostly fluent misreadings, dropped "
           "short conditions or symbols, wrong indices, signs and arrow directions, and missed deletions; only a third of "
           "them carried a doubt mark",
    "work1": "earlier checks found it careful on typed and light pages and about 1.4 to 1.7 errors per 100 words on his "
             "dense hand (control folder CTRL-148), with many doubt marks (about 7 per 100 words); typical slips are a "
             "struck letter given live, an insertion attached to the wrong place, a word ending read from the grammar",
    "work2": "a second reading made blind, without the first pass in view; on the control folder CTRL-148 this reader "
             "made about 1.7 errors per 100 words against the Pro first pass's 3.3; its notes often call his slips what "
             "were misreadings",
    "claude2": "a second pass against the scans; on the two control folders it left about 0.5 errors per 100 words and "
               "removed about three-quarters of the first pass's errors, but left most of Pro's doubt marks undecided",
    "api": "a clean typescript transcribed over the API; check the typed text and every handwritten addition on it",
    "pro_cp": "an unfinished first pass (a checkpoint): treat it as a draft",
}


def witness_label(x):
    d = W.run_date(x["route"], x["id"])
    d = f", {d}" if d else ""
    return {"pro": f"witness O, the first pass by GPT-6 Astra (ChatGPT Pro mode){d}",
            "pro_b": f"witness O2, a second chat of the same Pro first pass{d}",
            "pro_cp": "witness O, a Pro first pass known only from a checkpoint",
            "claude2": "witness K, the second pass of Claude Opus 5.5 at effort max (13-17 Nov 2026)",
            "work1": f"witness C, the first reading by {x['model']}{d}",
            "work2": f"witness W, a second reading by {x['model']}{d}",
            "api": "witness T, the typescript transcription by Claude Opus 5.5 over the API (12-13 Nov 2026)"}[x["route"]]


def first_pass_prompt(pkg):
    for base in (W.T / "packages_done", W.T / "packages"):
        for d in sorted(base.glob(f"*{pkg}")):
            if (d / "PROMPT.md").exists() and re.match(r"^(?:P\d+_)?(?:\d+_)?" + re.escape(pkg) + "$", d.name):
                return d / "PROMPT.md"
    return None


def assemble(uid, u, D):
    """everything a package needs, the same for both variants: dict of zips (name -> members) and the texts"""
    c = u["cote"]
    a, b = [int(x) for x in u["scans"].split("-")]
    idx = D["idx"]
    allsc = W.scans_of(c)
    ss = [s for s in allsc if a <= s <= b]
    info = page_info(c, D)
    pages = [s for s in ss if not info[s]["blank"]]
    missing = [s for s in pages if not info[s]["reading"]]
    before = [s for s in allsc if s < a and not info[s]["blank"]][-1:]
    after = [s for s in allsc if s > b and not info[s]["blank"]][:1]
    Z = {}
    # scans
    groups, nimg = [], 0
    for s in ss:
        im = W.page_images(c, s, pieces=3)
        groups.append([(f"{c}_scan{s:03d}{suf}.jpg", data) for suf, data in im])
        nimg += len(im)
    for s in before + after:
        im = W.page_images(c, s, pieces=0)
        if im:
            groups.append([(f"{c}_scan{s:03d}_neighbour.jpg", im[0][1])])
    Z["scans"] = groups
    # witnesses
    wz, pm, used_hua = [], [], set()
    kinds = collections.OrderedDict()
    for s in ss + before + after:
        rd = idx.get((c, s), [])
        f = W.first_reading(rd)
        row = dict(scan=s, in_range="yes" if s in ss else "neighbour (context only)", blank="yes" if info[s]["blank"] else "",
                   start_from="", readings="", hua=(W.hua(c).get(s) or ("nothing",))[0])
        names = []
        for x in rd:
            if x["route"] == "pro_cp" and any(y["route"] == "pro" for y in rd):
                continue
            sub = "first" if x["route"] in ("pro", "pro_b", "pro_cp", "work1", "api") else "second"
            arc = f"{sub}/{x['id']}/{c}_scan{s:03d}.tex"
            if s in ss:
                wz.append((arc, W.page_text(x).encode("utf-8")))
                kinds.setdefault((x["route"], x["id"]), x)
                names.append(f"{witness_label(x).split(',')[0]} `{arc}`")
            else:
                names.append(f"{x['route']} {x['id']}")
            if x is f:
                row["start_from"] = arc if s in ss else f"{x['route']} {x['id']}"
        row["readings"] = "; ".join(names)
        pm.append(row)
        h = W.hua(c).get(s)
        if h and s in ss:
            used_hua.add(h[1])
    for (route, wid), x in kinds.items():
        sub = "first" if route in ("pro", "pro_b", "pro_cp", "work1", "api") else "second"
        if route in ("pro", "pro_b"):
            ret = W.T / "returns" / f"{wid}{'_chatB' if route == 'pro_b' else ''}_unzipped"
            for suf in ("_doubts.md", "_inventory.csv"):
                p = ret / f"{wid}{suf}"
                if p.exists():
                    wz.append((f"{sub}/{wid}/{p.name}", p.read_bytes()))
            fp = first_pass_prompt(wid)
            if fp:
                wz.append((f"{sub}/{wid}/first_pass_PROMPT.md", fp.read_bytes()))
        elif route in ("work1", "work2"):
            out = W.CW / "returns" / wid / "out"
            for suf in ("_doubts.md", "_audit.md", "_inventory.csv"):
                p = out / f"{wid}{suf}"
                if p.exists():
                    wz.append((f"{sub}/{wid}/{p.name}", p.read_bytes()))
            pp = W.CW / "done" / wid / "PROMPT.md"
            if pp.exists():
                wz.append((f"{sub}/{wid}/PROMPT.md", pp.read_bytes()))
        elif route == "claude2":
            d = W.T / "second_pass" / "out" / wid
            for p in sorted(d.glob("*_changes.md")) + sorted(d.glob("*_notes_checked.md")):
                wz.append((f"{sub}/{wid}/{p.name}", p.read_bytes()))
    seen_arc = {n for n, _ in wz}
    for hb in sorted(used_hua, key=lambda p: p.name):
        for src, arc in W.hua_files(c, [s for s in ss if (W.hua(c).get(s) or (None, None))[1] == hb]):
            if arc not in seen_arc:
                wz.append((arc, src.read_bytes()))
                seen_arc.add(arc)
    if used_hua:
        for rel in W.HUA_COMMON:
            wz.append((f"hua/{rel}", (W.HUA / rel).read_bytes()))
    wz.append(("PREAMBLE.tex", O.PREAMBLE.read_bytes()))
    wz.append(("page_map.tsv", W.tsv(pm, ["scan", "in_range", "blank", "start_from", "readings", "hua"]).encode("utf-8")))
    ht = sum(1 for s in pages if (W.hua(c).get(s) or ("",))[0] == "text")
    wl = []
    for (route, wid), x in kinds.items():
        sub = "first" if route in ("pro", "pro_b", "pro_cp", "work1", "api") else "second"
        n = sum(1 for s in pages if any(y["route"] == route and y["id"] == wid for y in idx.get((c, s), [])))
        extra = {"pro": ", with its doubts table and the prompt it was made with (`first_pass_PROMPT.md`, which defines "
                        "our macros)",
                 "work1": ", with its doubts table, its audit and the task it was given (`PROMPT.md`)",
                 "work2": ", with its doubts table and its audit",
                 "claude2": ", with its changes tables and its checked notes"}.get(route, "")
        wl.append(f"  - `{sub}/{wid}/`: {witness_label(x)}, for {n} of the {len(pages)} pages{extra}; "
                  f"{WITNESS_FINDINGS.get(route, '')}.")
    if used_hua:
        wl.append(f"  - `hua/`: witness H, the transcription of the Commutator project of Michel Hua (github.com/"
                  f"Commutator-IO/grothendieck-project, commit `{W.HUA_COMMIT}`), an AI transcription whose batch headers "
                  "name the Claude model of each pass (Claude Opus 5, Claude Opus 5.5) but no effort setting, in that "
                  "project's own macros (`hua/transcripts/preamble/grothendieck.sty` says what each means: `\\struck` a "
                  "deletion, `\\add` an insertion, `\\marginal` a margin note, `\\uncertain` a doubtful reading, `\\ill` a "
                  f"word they could not read). Their page n is our scan n + 1. H has text for {ht} of these {len(pages)} "
                  "pages. Earlier checks found it at about 1.5 errors per 100 words on light pages and 3 to 8 on dense "
                  "ones: plausible prose in place of the ink, struck text given as live, abbreviations expanded, margins "
                  "left out, drawings described. A witness only, credited; this run writes nothing in their conventions.")
    if not {r for r, _ in kinds if r in ("work2", "claude2")}:
        wl.append("  - No second reading of these pages exists yet: your own reading on the crop is the second witness, "
                  "with witness H where it has the page.")
    wz.insert(0, ("README.md", (f"# The witnesses of {uid}\n\n" + "\n".join(x[2:] for x in wl) +
                                "\n\n`page_map.tsv`: for every scan of the range (and the two neighbours), every reading "
                                "and the one a pass starts from. `PREAMBLE.tex`: our macros. All witnesses are AI readings "
                                "of the same scans; none has been checked against the pages by a person. The scans are "
                                "the authority.\n").encode("utf-8")))
    Z["witnesses"] = wz
    # the nodes: entries, concordance, objects, themes, links, checks, draft units
    ents = sorted(set().union(*[D["by_page"].get((c, s), set()) for s in ss]),
                  key=lambda e: (min((x for cc, x in D["epages"][e] if cc == c), default=0), e))
    tag_of = D["item_tag"]
    md, ni = [f"# The notes on {uid}\n\nEvery note entry that cites a page of this range, in page order, in full as it "
              "stands in its file, with the placement of horizontal sweep 1 (Claude Opus 5.5 at effort max, 18 Nov "
              "2026): the object, its item and the object's tag.\n"], []
    files, tagset, itemset = {}, collections.OrderedDict(), set()
    for eid in ents:
        r = D["erow"][eid]
        e = O.entry(eid, r)
        kind, src = O.source_of(eid)
        its = items_of(r)
        itemset.update(its)
        tg = [tag_of.get(x, "") for x in its]
        for t in tg:
            if t:
                tagset.setdefault(t, []).append(eid)
        who = {"pro": "GPT-6 Astra (ChatGPT Pro mode), notes of the transcription package " + src,
               "work": "GPT-6.2 Astra at reasoning effort max (ChatGPT Work), math notes of the folder " + src,
               "codex": "GPT-6 Astra at reasoning effort max (Codex web), notes of the folder " + src}[kind]
        rel = e["file"].replace("\\", "/").split("Documents/")[-1] if e["file"] else ""
        if e["file"]:
            files[rel] = e["file"]
        md.append(f"\n## {eid}: {e['heading']}\n\n- written by: {who}\n- file: `files/{pathlib.Path(rel).name}`, line {e['line']}\n"
                  f"- pages: {O.cotes_scans_text(D['epages'][eid]) or 'none cited'}\n- kind: {r.get('kind', '')}\n"
                  f"- the sweep's object: {r.get('object', '')} (item {r['item']}, tag {', '.join(t for t in tg if t) or 'none'};"
                  f" basis {r.get('basis', '')}; fidelity {r.get('fidelity', '')}"
                  + (f"; flag: {r['flag']}" if r.get("flag") else "") + ")\n\n" + (e["text"].strip() or "(text not found)") + "\n")
        ni.append(dict(entry_id=eid, written_by=who, file=f"files/{pathlib.Path(rel).name}", line=e["line"],
                       pages=O.cotes_scans_text(D["epages"][eid]), kind=r.get("kind", ""), heading=e["heading"],
                       item=r["item"], tag=", ".join(t for t in tg if t), sweep_object=r.get("object", ""),
                       basis=r.get("basis", ""), fidelity=r.get("fidelity", ""), flag=r.get("flag", "")))
    nz = [("NOTES_ON_THESE_PAGES.md", "".join(md).encode("utf-8")),
          ("NOTES_INDEX.tsv", W.tsv(ni, list(ni[0].keys()) if ni else ["entry_id"]).encode("utf-8"))]
    for rel, full in files.items():
        nz.append((f"files/{pathlib.Path(rel).name}", pathlib.Path(full).read_bytes()))
    conc, cmd = [], [f"# The concordance of {uid}\n\nFor every object (the sweep's tag) that the notes on these pages are "
                     "about, the entries on the same object elsewhere in the archive, nearest first (the same folder, "
                     "then the same topic, then other topics), with their text.\n"]
    own, seen_c = set(ents), set()
    item_entries = collections.defaultdict(list)
    for eid, r in D["erow"].items():
        for it in items_of(r):
            item_entries[it].append(eid)
    for t, es in tagset.items():
        g = D["tags"].get(t)
        if not g:
            continue
        cmd.append(f"\n# {t}: {g['object']}\n\n- its entries on these pages: {', '.join(es)}\n- in the archive: "
                   f"{g['n_entries']} entries; {g['cotes_scans'][:200]}\n")
        others = []
        for it in g["items"].split():
            for eid in item_entries.get(it, []):
                if eid in own or eid in seen_c:
                    continue
                pg = D["epages"][eid]
                near = 0 if any(cc == c for cc, _ in pg) else (1 if pg and SA_OF.get(sorted(pg)[0][0], "") == u["sweep_topic"] else 2)
                others.append((near, eid, D["erow"][eid]))
        others.sort(key=lambda x: (x[0], x[1]))
        for near, eid, r in others:
            if len(conc) >= CONCORDANCE_MAX or eid in seen_c:
                continue
            seen_c.add(eid)
            e = O.entry(eid, r)
            conc.append(dict(tag=t, entry_id=eid, nearness=["same folder", "same topic", "other topic"][near],
                             pages=O.cotes_scans_text(D["epages"][eid]), heading=e["heading"], kind=r.get("kind", "")))
            cmd.append(f"\n## {eid} ({['same folder', 'same topic', 'other topic'][near]}; {O.cotes_scans_text(D['epages'][eid])}): "
                       f"{e['heading']}\n\n{e['text'].strip()}\n")
    nz.append(("CONCORDANCE.tsv", W.tsv(conc, ["tag", "entry_id", "nearness", "pages", "heading", "kind"]).encode("utf-8")))
    nz.append(("CONCORDANCE.md", "".join(cmd).encode("utf-8")))
    orows = [D["tags"][t] for t in tagset if t in D["tags"]]
    if orows:
        nz.append(("OBJECTS.tsv", W.tsv(orows, list(orows[0].keys())).encode("utf-8")))
    themes = {D["tags"][t].get("theme") for t in tagset if t in D["tags"]} - {"", None}
    th = [x for x in W.csv.DictReader(open(W.SWEEP / "GLOBAL/THEMES.tsv", encoding="utf-8"), delimiter="\t") if x["theme"] in themes]
    if th:
        nz.append(("THEMES.tsv", W.tsv(th, list(th[0].keys())).encode("utf-8")))
    lk = [x for x in W.csv.DictReader(open(W.SWEEP / "GLOBAL/LINKS.tsv", encoding="utf-8"), delimiter="\t")
          if x.get("tag") in tagset or x.get("to_tag") in tagset or x.get("item") in itemset]
    if lk:
        nz.append(("LINKS.tsv", W.tsv(lk, list(lk[0].keys())).encode("utf-8")))
    ck = [dict(x, checked=k) for k in list(ents) + sorted(itemset) + list(tagset) for x in D["checks"].get(k, [])]
    nz.append(("CHECKS.tsv", W.tsv(ck, ["checked", "id", "date_utc", "who", "how", "result", "where", "source_file"]).encode("utf-8")))
    drafts = [dict(du, folder=f) for f in u["_folders"] for du in D["du"].get(f, []) if du["unit"] in u["_units"]]
    if drafts:
        nz.append(("DRAFT_UNITS.tsv", W.tsv(drafts, ["unit", "folder", "cote", "scans", "title", "source"]).encode("utf-8")))
    sc = collections.Counter(O.source_of(e)[0] for e in ents)
    nz.insert(0, ("README.md", (f"# The nodes of {uid}\n\n- `NOTES_ON_THESE_PAGES.md`, `NOTES_INDEX.tsv`: the {len(ents)} "
                                f"entries that cite these pages ({sc['pro']} from Pro's notes, {sc['work']} from Work's math "
                                f"notes, {sc['codex']} from Codex's notes); `files/`: the whole files they come from.\n"
                                f"- `CONCORDANCE.tsv`, `CONCORDANCE.md`: {len(conc)} entries on the same objects elsewhere.\n"
                                f"- `OBJECTS.tsv`: the sweep's global rows of these {len(orows)} objects (their tags are the "
                                "handbook's draft tags)" + (f"; `THEMES.tsv`, their themes" if th else "")
                                + (f"; `LINKS.tsv`, the sweep's links among them" if lk else "") + ".\n"
                                f"- `CHECKS.tsv`: {len(ck)} rows of the check register (results_register/CHECK_REGISTER.tsv) "
                                "about these entries, items and objects: who checked what, how, with what result.\n"
                                + (f"- `DRAFT_UNITS.tsv`: the {len(drafts)} draft units of Work's math notes for these pages.\n"
                                   if drafts else "")).encode("utf-8")))
    Z["notes"] = nz
    # context
    cz, clist = [], []
    txt, _ = O.assemble_cote(c, idx)
    cz.append((f"this_folder/cote_{c}.tex", txt.encode("utf-8")))
    clist.append(f"`this_folder/cote_{c}.tex`: the whole folder as transcribed so far, each page in the reading a pass "
                 "starts from, for the argument before and after this range")
    for r in W.csv.DictReader(open(O.RULES, encoding="utf-8"), delimiter="\t"):
        if r["cote"] != c or r.get("use") not in ("folder", "both"):
            continue
        if r["path"].startswith("@cote:"):
            n = r["path"][6:]
            if n in W.MAN:
                t2, _ = O.assemble_cote(n, idx)
                cz.append((r["arcname"], t2.encode("utf-8")))
                clist.append(f"`{r['arcname']}`: {r['description']}")
        else:
            p = W.D / r["path"]
            if p.exists():
                cz.append((r["arcname"], p.read_bytes()))
                clist.append(f"`{r['arcname']}`: {r['description']}")
    sa = u["sweep_topic"]
    if sa and (W.HIN / sa / "TOPIC.md").exists():
        cz.append((f"topics/{sa}_TOPIC.md", (W.HIN / sa / "TOPIC.md").read_bytes()))
        clist.append(f"`topics/{sa}_TOPIC.md`: the catalogue of the topic (its folders, what is transcribed and how)")
    if sa and (W.SWEEP3 / sa).is_dir():
        cz += W.sweep3_members(sa)
        clist.append(W.SWEEP3_LINE.format(t=sa))
    cz.insert(0, ("README.md", (f"# The context of {uid}\n\n" + "".join(f"- {x}\n" for x in clist) +
                                "\nNo earlier range of this topic has been worked through yet; when one has, its tables "
                                "join this context as `earlier_ranges/`.\n").encode("utf-8")))
    Z["context"] = cz
    # results (opened last)
    hit = []
    for r in W.register_rows():
        if W.places_cite(r.get("his_places", ""), c, list(range(a, b + 1))):
            hit.append(dict(tag=r["tag"], run=r["run"], status=r["status"], statement=r["statement"],
                            where_proved=r["where_proved"], his_places=r["his_places"], check_events=r["check_events"],
                            check_types=r["check_types"]))
    Z["results"] = [("README.md", (f"# Our results that cite {uid}\n\nThe statements of our research runs (results_register/"
                                   f"REGISTER.tsv, 18 Nov 2026) whose `his_places` cite cote {c} at these scans or without a "
                                   f"scan: {len(hit)} rows. A status is the run's own claim unless `check_events` records a "
                                   "check. Open this only when the work on the pages is done.\n").encode("utf-8")),
                    ("RESULTS_CITING.tsv", W.tsv(hit[:600], ["tag", "run", "status", "statement", "where_proved",
                                                             "his_places", "check_events", "check_types"]).encode("utf-8"))]
    k, n = u["unit"].split(" of ")
    title = W.MAN[c]["title"]
    fnote = (f"The folder's catalogue title: « {title} » ({W.MAN[c]['date']}). It has {len(allsc)} scans; this run takes "
             f"scans {a}-{b}, range {k} of {n} of the folder" + ("; the other ranges are separate runs." if int(n) > 1 else "."))
    if [s for s in ss if info[s]["blank"]]:
        fnote += f" Scans {O.compress([s for s in ss if info[s]['blank']])} are recorded as blank: check that they are."
    if drafts:
        dnote = (f"Work's math notes divide these pages into {len(drafts)} draft units (`DRAFT_UNITS.tsv` in the notes zip), "
                 "each with its scans and a title.")
        urule = ("Start from the draft units of `DRAFT_UNITS.tsv`: keep each where his writing bears it out, and redraw "
                 "it where his argument runs otherwise (merged, split or moved), saying so in `from_draft`.")
    else:
        dnote = "No draft units exist for these pages."
        urule = "Draw the units from his own divisions."
    nb_ = ""
    if before and after:
        nb_ = (f"The pages just before and after this range (scans {before[0]} and {after[0]}) are attached whole, as "
               "`..._neighbour.jpg`, to follow an argument across the cut: they are worked in their own ranges, and are "
               "read here only to complete such an argument.")
    elif before or after:
        nb_ = (f"The page just {'before' if before else 'after'} this range (scan {(before or after)[0]}) is attached "
               "whole, as `..._neighbour.jpg`, to follow an argument across the cut: it is worked in its own range, and is "
               "read here only to complete such an argument.")
    notes_list = (f"  - `NOTES_ON_THESE_PAGES.md`: every note entry on these pages ({len(ents)}: {sc['pro']} from the notes "
                  f"of the Pro first passes, by GPT-6 Astra (ChatGPT Pro mode), written with a context of our earlier work; "
                  f"{sc['work']} from the math notes of Work's readings, by GPT-6.2 Astra at reasoning effort max (ChatGPT "
                  f"Work), written without context; {sc['codex']} from the notes of Codex web, by GPT-6 Astra at reasoning "
                  "effort max, which list only the steps the pages mark as unverified and the title sheets), in full, in "
                  "page order, each with the object the sweep placed it under and the object's tag; `NOTES_INDEX.tsv`, "
                  "the same as an index; `files/`, the whole files they come from;\n"
                  f"  - `CONCORDANCE.md`, `CONCORDANCE.tsv`: for every object these entries are about, the entries on the "
                  f"same object elsewhere in the archive ({len(conc)}), nearest first, with their text;\n"
                  f"  - `OBJECTS.tsv`: the sweep's rows of these {len(orows)} objects, whose tags are the handbook's draft "
                  "tags" + ("; `THEMES.tsv` and `LINKS.tsv`: their themes and the sweep's links" if th or lk else "") + ";\n"
                  f"  - `CHECKS.tsv`: what was already checked about these entries and objects ({len(ck)} rows of our check "
                  "register: who, how, the result)" + (";\n  - `DRAFT_UNITS.tsv`: the draft units of Work's math notes."
                                                       if drafts else "."))
    rep = {"{COTE}": c, "{RANGE}": f"{a}-{b}", "{COUNT}": str(len(pages)), "{FOLDER_NOTE}": fnote, "{DRAFT_NOTE}": dnote,
           "{UNITS_RULE}": urule, "{ATTACH_NOTE}": "", "{NEIGHBOURS}": nb_, "{WITNESS_LIST}": "\n".join(wl),
           "{NOTES_LIST}": notes_list, "{CONTEXT_LIST}": "It holds: " + "; ".join(clist) + ". Search these files for his "
           "objects and numbers: the passages of his published work that his pages annotate, draft or anticipate are "
           "the first grounds.", "{MISSING}": ("scans " + O.compress(missing)) if missing else "none here: every page of this range has a reading",
           "{FIRST}": f"{a:03d}"}
    meta = dict(cote=c, a=a, b=b, pages=pages, missing=missing, ents=ents, conc=conc, nimg=nimg, hit=hit, clist=clist,
                wl=wl, drafts=drafts, checks=len(ck), title=title)
    return Z, rep, meta


def build(uid, rows, D, variants="AB", cache=None, folders=None):
    u = next((x for x in rows if x["unit_id"] == uid), None)
    if u is None:
        raise SystemExit(f"{uid}: not a range of the plan")
    Z, rep, m = assemble(uid, u, D)
    out = []
    for v in variants:
        S = f"WT{v}_{uid[3:]}"
        folder, work = ((folders or {}).get(v) or OUT / S), WORK / S
        W.PRIVACY.clear()
        folder.mkdir(parents=True, exist_ok=True)
        for p in folder.iterdir():
            p.unlink()
        work.mkdir(parents=True, exist_ok=True)
        scan_names = W.zip_parts(folder, f"{S}_scans", Z["scans"], stored=True)
        names = {k: W.zip_parts(folder, f"{S}_{k}", Z[k]) for k in ("witnesses", "notes", "context", "results")}
        sf = (", ".join(f"`{x}`" for x in scan_names[:-1]) + f" and `{scan_names[-1]}` (unpack them into the same folder)"
              if len(scan_names) > 1 else f"`{scan_names[0]}`")
        t = TEMPLATES[v].read_text(encoding="utf-8").replace("{S}", S).replace("{SCANS_FILES}", sf)
        for k_, val in rep.items():
            t = t.replace(k_, val)
        left = re.findall(r"\{[A-Z_]{3,}\}", t)
        if left:
            raise SystemExit(f"{S}: placeholders left: {left}")
        t = W.lintsafe(t)
        (folder / "PROMPT.md").write_text(t, encoding="utf-8", newline="\n")
        ok, msg = W.lint(folder / "PROMPT.md", "--lint-math")
        sizes = {p.name: round(p.stat().st_size / 1e6, 2) for p in sorted(folder.iterdir())}
        kind = {"A": "A, the companion-coded pass (units, keyed notes, status blocks, handbook items, suggested links)",
                "B": "B, the foundational check (the mathematics, the scan checks and the verdicts; no companion writing)",
                "F": "the full second visual pass of the plan's section 3"}[v]
        readme = (f"# {S}: cote {m['cote']}, scans {m['a']}-{m['b']}, variant {kind} (ChatGPT Pro upload folder)\n\n"
                  f"Upload every file of this folder except this README in a new ChatGPT chat with GPT-6 Astra in Pro mode, "
                  f"`PROMPT.md` as a file, no text typed. Range {u['unit']} of the folder: {len(m['pages'])} pages"
                  + (f" ({len(m['missing'])} with no reading yet, transcribed first: scans {O.compress(m['missing'])})" if m["missing"] else "")
                  + f"; {u['basis']}; {len(m['ents'])} note entries; {m['nimg']} images; expected {u['expected_minutes']} "
                  f"minutes (estimate, until the pilot measures it). Images: "
                  f"{sum(v_ for kk, v_ in sizes.items() if 'scans' in kk):.1f} MB.\n\n"
                  f"Folder: « {m['title']} » ({W.MAN[m['cote']]['date']}).\n\n## Files\n\n"
                  + "\n".join(f"- `{n_}` ({sizes[n_]} MB)" for n_ in sizes if n_ != "README.md") +
                  "\n\n## Witnesses\n\n" + "\n".join(x[2:] for x in m["wl"]) +
                  "\n\n## Context (the subject's own, chosen by rule: CONTEXT_RULES.tsv)\n\n" + "".join(f"- {x}\n" for x in m["clist"]) +
                  f"\n## Nodes\n\n- {len(m['ents'])} entries on these pages; {len(m['conc'])} related entries in the concordance; "
                  f"{m['checks']} check-register rows" + (f"; {len(m['drafts'])} draft units" if m["drafts"] else "") + ".\n\n"
                  f"## Results (opened last by the run)\n\n- {len(m['hit'])} statements of our runs whose `his_places` cite these pages.\n\n"
                  "## Provenance\n\n- **Scans:** Université de Montpellier, fonds Grothendieck (grothendieck.umontpellier.fr); "
                  "cotes and scan numbers are theirs; rendered from the archive PDFs as in the first-pass packages (largest "
                  "image, autocontrast, unsharp mask, JPEG 88), whole and in three overlapping strips.\n"
                  f"- **Built** {W.NOW():%Y-%m-%d %H:%M} UTC by `working_through_20261118/build_working_through.py` (Claude "
                  f"Opus 5.5 at effort max). Lint (--lint-math): {'pass' if ok else 'FAIL'}.\n")
        (folder / "README.md").write_text(readme, encoding="utf-8", newline="\n")
        bj = dict(id=S, variant=v, range=uid, cote=m["cote"], scans=[m["a"], m["b"]], pages=len(m["pages"]),
                  privacy=dict(W.PRIVACY), expected_minutes=u["expected_minutes"], topic=u["sweep_topic"],
                  missing=m["missing"], entries=len(m["ents"]), concordance=len(m["conc"]), checks=m["checks"],
                  draft_units=len(m["drafts"]), images=m["nimg"], sizes_mb=sizes, lint=msg, results_rows=len(m["hit"]),
                  context=m["clist"], ok=ok and all(x < 450 for x in sizes.values()) and len(sizes) <= 20,
                  built=f"{W.NOW():%Y-%m-%d %H:%M:%SZ}")
        (work / "BUILD.json").write_text(json.dumps(bj, indent=1, ensure_ascii=False), encoding="utf-8")
        print(json.dumps({k_: bj[k_] for k_ in ("id", "pages", "missing", "entries", "concordance", "checks", "draft_units",
                                                 "images", "sizes_mb", "lint", "ok")}, ensure_ascii=False))
        out.append(bj)
    return out


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in ("plan", "build"):
        raise SystemExit(__doc__)
    args = sys.argv[2:]
    variants = "AB"
    if "--variant" in args:
        i = args.index("--variant")
        variants = args[i + 1]
        args = args[:i] + args[i + 2:]
    rows, D = plan()
    if sys.argv[1] == "build":
        if args[:1] == ["--cote"]:
            ids = [x["unit_id"] for x in rows if x["cote"] in args[1:]]
        elif args[:1] == ["--next"]:
            ids = [x["unit_id"] for x in rows if not any((OUT / f"WT{v}_{x['unit_id'][3:]}").exists() for v in variants)][:int(args[1])]
        else:
            ids = args
        for i in ids:
            build(i, rows, D, variants)
        plan(D)
