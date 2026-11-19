"""Horizontal sweep 2, part 1 (agent a28ea31fa17dd65e1, Claude Opus 5.5 at effort max).

python -I -B hsweep2.py peek SAnn [source-substring] [nwords]   opening words of every gap entry
python -I -B hsweep2.py full SAnn entry_id [entry_id ...]       whole text of entries
python -I -B hsweep2.py build SAnn                              sweep-1 tables + placed gap entries -> sweep2/SAnn
Rules per topic: rules_SAnn.py next to this file.
"""
import csv, sys, re, collections, importlib.util
from pathlib import Path

csv.field_size_limit(10 ** 9)
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
DOC = Path(r"C:/Users/user/Documents")
H = DOC / "results_register/horizontal"
S1, S2 = H / "sweep1", H / "sweep2"
TOOLS = S2 / "_tools_a28ea31f"
WHO = "Claude Opus 5.5 at effort max, a28ea31fa17dd65e1, horizontal sweep 2"
CHATB = "MPL_15_195-228+18_002-017_chatB"


def clean(s):
    return re.sub(r"\s+", " ", (s or "").replace("\t", " ")).strip()


def rtsv(p):
    with open(p, encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f, delimiter="\t"))
    return rows[0], rows[1:]


def wtsv(p, head, rows):
    with open(p, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(head)
        for r in rows:
            w.writerow([clean(str(x)) for x in r])


_units = None


def units():
    global _units
    if _units is None:
        h, rows = rtsv(S2 / "inputs/UNITS.tsv")
        _units = [dict(zip(h, r)) for r in rows]
    return _units


def gap(topic):
    h, rows = rtsv(S2 / "inputs" / topic / "GAP_INDEX.tsv")
    g = [dict(zip(h, r)) for r in rows]
    g = [e for e in g if e["cls"] not in ("variant", "pro_chatB")]
    if topic == "SA07":
        lh, lrows = rtsv(S2 / "GLOBAL/LINKED_PLACEMENTS.tsv")
        want = {r[0] for r in lrows if r[0].startswith(CHATB) and ":doubts" not in r[0] and not r[lh.index("item")].strip()}
        g += [u for u in units() if u["entry_id"] in want]
    return g


_files = {}


def body(e):
    sf = e["source_file"]
    if sf not in _files:
        lines = (DOC / sf).read_text(encoding="utf-8", errors="replace").splitlines()
        starts = sorted({int(u["line"]) for u in units() if u["source_file"] == sf})
        _files[sf] = (lines, starts)
    lines, starts = _files[sf]
    a = int(e["line"])
    nxt = [s for s in starts if s > a]
    b = nxt[0] if nxt else len(lines) + 1
    head = lines[a - 1] if a - 1 < len(lines) else ""
    m = re.match(r"(#+)\s", head)
    if m:
        lev = len(m.group(1))
        for i in range(a, b - 1):
            mm = re.match(r"(#+)\s", lines[i])
            if mm and len(mm.group(1)) <= lev:
                b = i + 1
                break
    return "\n".join(lines[a:b - 1]).strip()


def short(eid):
    return eid.replace("grothendieck_archive_transcription_20261110/", "")


def folder(eid):
    m = re.match(r"(?:codex|work):([A-Z]+\d+-\d+(?:_\d)?)", eid)
    return m.group(1) if m else None


def cote_of(e, txt):
    m = re.search(r"[Cc]ote\s*(\d+)", e.get("heading", "") + " " + txt[:300])
    if m:
        return m.group(1)
    f = folder(e["entry_id"])
    if f:
        return re.match(r"[A-Z]+(\d+)", f).group(1)
    m = re.match(r"MPL_(\d+)", e["entry_id"])
    return m.group(1) if m else ""


def kind_of(e, txt):
    hd = e.get("heading", "")
    cls = e.get("cls", "")
    if cls == "codex_sheet_notes":
        return "title sheets, dates and page counts" if re.search(r"[Tt]itle", hd) else "steps the pages mark as unverified"
    if cls == "pro_records":
        return "research lead"
    if cls.startswith("work"):
        return "work note: " + hd.lower()
    m = re.search(r"\*\*(?:Kind|Type)[:*]*\s*\**\s*([^\n*]+)", txt)
    if m:
        return clean(m.group(1)).rstrip(".").lower()
    m = re.search(r"\s[—-]\s+([a-z][a-z /-]+)$", hd)
    if m:
        return m.group(1).strip()
    return "note"


def opening(txt, n):
    t = re.sub(r"\*\*(Source|Scans?|Locator|Cote)[^\n]*", "", txt)
    t = re.sub(r"[#*`>]", "", t)
    return " ".join(clean(t).split()[:n])


def load_rules(topic):
    p = TOOLS / f"rules_{topic}.py"
    spec = importlib.util.spec_from_file_location("rules_" + topic, p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def peek(topic, sub="", n=14):
    last = None
    for e in gap(topic):
        if sub and sub not in e["entry_id"]:
            continue
        src, num = e["entry_id"].rsplit("#", 1)
        if src != last:
            print("@@", src)
            last = src
        t = body(e)
        print(f"#{num}|{e['scans'][:14]}|{e['heading'][:40]}|{opening(t, n)}")


def full(topic, ids):
    g = {e["entry_id"]: e for e in gap(topic)}
    for i in ids:
        e = g[i]
        print(f"=== {i} ({e['heading']})\n{body(e)}\n")


def build(topic):
    R = load_rules(topic)
    ph, prow = rtsv(S1 / topic / "PLACEMENT.tsv")
    oh, orow = rtsv(S1 / topic / "OBJECTS.tsv")
    fh, frow = rtsv(S1 / topic / "FLAGS.tsv")
    ch, crow = rtsv(S1 / topic / "CHECK_EVENTS.tsv")
    objs = {r[0]: dict(zip(oh, r)) for r in orow}
    nums = [int(k.split("-")[1]) for k in objs]
    nxt = max(nums) + 1
    newmap = {}
    for key, obj, stmt in getattr(R, "NEW", []):
        it = f"{topic}-{nxt}"
        nxt += 1
        newmap[key] = it
        objs[it] = dict(item=it, object=obj, kind="", statement=stmt, entries="", cotes_scans="",
                        status_on_pages="not checked", cross_topic="", flags="")
    rid = lambda x: newmap.get(x, x)
    # sweep-1 scan overlap: (cote, scan) -> items
    ov = collections.defaultdict(collections.Counter)
    for r in prow:
        d = dict(zip(ph, r))
        for s in re.split(r"[ ,;]+", d.get("scans", "")):
            if s.strip().isdigit():
                ov[(d["cote"], int(s))][d["item"]] += 1
    out, unplaced = [], []
    FOLDER = getattr(R, "FOLDER", {})
    FORCE = getattr(R, "FORCE", {})
    RULES = [(re.compile(r[0], re.I), r[1], r[2] if len(r) > 2 else "", r[3] if len(r) > 3 else "") for r in getattr(R, "RULES", [])]
    PEEKN = getattr(R, "PEEKN", 14)
    for e in gap(topic):
        eid = e["entry_id"]
        t = body(e)
        hd = e.get("heading", "")
        cote = cote_of(e, t)
        kind = kind_of(e, t)
        if not e.get("scans") and getattr(R, "SCANS", None):
            e["scans"] = R.SCANS(e, t)
        op = opening(t, PEEKN)
        note = "chatB " if eid.startswith(CHATB) else ""
        if eid.startswith(CHATB):
            note = "parallel witness of MPL_15_195-228+18_002-017 (chatB). "
        item = basis = None
        fid, flag = "not assessed", ""
        if eid in FORCE:
            f = FORCE[eid]
            item, basis, fid = rid(f[0]), f[1], f[2]
            note += f[3] if len(f) > 3 else ""
            flag = f[4] if len(f) > 4 else ""
        fo = folder(eid)
        if item is None and fo and e["cls"] == "codex_sheet_notes" and kind.startswith("title"):
            item, basis = rid(R.DOCS), "heading"
        if item is None:
            for rx, it, src, bo in RULES:
                if src and src not in eid:
                    continue
                if rx.search(hd + " " + t):
                    item = rid(it)
                    basis = bo or ("opening-read" if rx.search(hd + " " + op) else "body-keyword")
                    note += f"rule /{rx.pattern[:40]}/. "
                    break
        if item is None and fo and fo in FOLDER:
            item, basis = rid(FOLDER[fo]), "folder-map; opening-read"
        if item is None and not any(eid.startswith(x) for x in getattr(R, "OVERLAP_SKIP", [])):
            cnt = collections.Counter()
            for s in re.split(r"[ ,;/]+", e.get("scans", "")):
                if s.strip().isdigit():
                    cnt.update(ov.get((cote, int(s)), {}))
            if cnt:
                item, basis = cnt.most_common(1)[0][0], "scan-overlap; opening-read"
                note += "same cote and scan as sweep-1 placements. "
        if item is None and getattr(R, "FALLBACK", None):
            fb = R.FALLBACK(e, t)
            if fb:
                if isinstance(fb, tuple):
                    item, basis = rid(fb[0]), fb[1]
                    if len(fb) > 2:
                        note += fb[2]
                else:
                    item, basis = rid(fb), "opening-read; fallback by package/section"
        if item is None:
            unplaced.append(eid)
            continue
        if item not in objs:
            raise SystemExit(f"unknown item {item} for {eid}")
        out.append([eid, topic, cote, e.get("scans", ""), kind, objs[item]["object"][:90], "", item, basis, fid, flag,
                    note + f"words {e.get('words', '')}; opening: {op[:120]}"])
    if unplaced:
        print("UNPLACED", len(unplaced))
        for u in unplaced[:60]:
            print("  ", u)
        if not getattr(R, "ALLOW_UNPLACED", False):
            raise SystemExit(1)
    # objects
    add = collections.defaultdict(list)
    for r in out:
        add[r[7]].append(r)
    for it, rs in add.items():
        o = objs[it]
        ents = o["entries"].split() if o["entries"] else []
        o["entries"] = " ".join(ents + [r[0] for r in rs])
        cs = [x for x in o["cotes_scans"].split("; ") if x]
        cs += sorted({f"{r[2]}:{r[3]}" for r in rs} - set(cs))
        o["cotes_scans"] = "; ".join(cs)
        kt = collections.Counter()
        for part in o["kind"].split("; "):
            if ":" in part:
                k, v = part.rsplit(":", 1)
                if v.isdigit():
                    kt[k] += int(v)
        kt.update(r[4] for r in rs)
        o["kind"] = "; ".join(f"{k}:{v}" for k, v in kt.most_common())
    for it, upd in getattr(R, "OBJ", {}).items():
        it = rid(it)
        for k, v in upd.items():
            if k.endswith("+"):
                kk = k[:-1]
                objs[it][kk] = (objs[it][kk] + "; " if objs[it][kk] else "") + v
            else:
                objs[it][k] = v
    flags_new = [[k, w, x, ev] for k, w, x, ev in getattr(R, "FLAGS", [])]
    checks_new = [list(c) for c in getattr(R, "CHECKS", [])]
    for c in checks_new:
        if len(c) == 5:
            c.insert(2, WHO)
    d = S2 / topic
    wtsv(d / "PLACEMENT.tsv", ph, prow + out)
    keyorder = sorted(objs, key=lambda k: int(k.split("-")[1]))
    wtsv(d / "OBJECTS.tsv", oh, [[objs[k].get(c, "") for c in oh] for k in keyorder])
    wtsv(d / "FLAGS.tsv", fh, frow + flags_new)
    wtsv(d / "CHECK_EVENTS.tsv", ch, crow + checks_new + getattr(R, "CHECKS_IMPORTED", []))
    tn = (S1 / topic / "TOPIC_NOTES.md").read_text(encoding="utf-8").rstrip() + "\n\n"
    bas = collections.Counter(r[8].split(";")[0] for r in out)
    cls = collections.Counter(e["cls"] for e in gap(topic))
    tn += f"## Sweep 2, part 1 (gap entries; {WHO}, 18 Nov 2026)\n\n"
    tn += f"Entries placed: {len(out)} ({', '.join(f'{k} {v}' for k, v in cls.most_common())}).\n"
    tn += f"Basis: {', '.join(f'{k} {v}' for k, v in bas.most_common())}.\n"
    tn += f"New items: {', '.join(f'{newmap[k]} ({objs[newmap[k]]['object'][:60]})' for k, _, _ in getattr(R, 'NEW', [])) or 'none'}.\n"
    tn += f"Flags added: {len(flags_new)}. Check events added: {len(checks_new) + len(getattr(R, 'CHECKS_IMPORTED', []))}.\n\n"
    tn += BASIS_LEGEND + "\n" + getattr(R, "NOTES", "").strip() + "\n"
    (d / "TOPIC_NOTES.md").write_text(tn, encoding="utf-8")
    per = collections.Counter(r[7] for r in out)
    print(topic, "placed", len(out), dict(bas), "new", newmap, "flags", len(flags_new))
    print(" per item:", ", ".join(f"{k}:{v}" for k, v in sorted(per.items(), key=lambda x: int(x[0].split('-')[1]))))


BASIS_LEGEND = """Basis words in PLACEMENT (sweep 2):
- heading: placed from the heading alone (title sheets, dates and page counts go to the documents item);
- opening-read: I read the entry's opening (about the first 14-30 words), and the deciding words are in it;
- body-keyword: placed by a keyword rule that matched further into the entry, which I did not read there;
- folder-map: the entry's folder covers the same pages as a sweep-1 Work folder, placed under that folder's item;
- scan-overlap: the same cote and scan as sweep-1 placements of the topic;
- entry-read: I read the whole entry; passage-read: I read the passage on the scan.
Fidelity is assessed only for entry-read and passage-read rows.
"""

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "peek":
        peek(a[1], a[2] if len(a) > 2 else "", int(a[3]) if len(a) > 3 else 14)
    elif a[0] == "full":
        full(a[1], a[2:])
    elif a[0] == "build":
        build(a[1])
