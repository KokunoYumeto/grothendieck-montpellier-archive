"""Horizontal sweep 1: parse a topic's note entries (Pro notes per package, Work math-notes units) and, with a per-topic
cluster file, write PLACEMENT.tsv, OBJECTS.tsv, FLAGS.tsv and CHECK_EVENTS.tsv for that topic.
Written by Claude Opus 5.5 at effort max (agent a28ea31fa17dd65e1), horizontal sweep 1, 18 Nov 2026.
usage: python -I -B hsweep.py list SA16        -> prints a compact listing of the entries (for reading)
       python -I -B hsweep.py build SA16       -> writes the four TSVs from clusters_SA16.py (in this tools folder)
Inputs are read only: results_register/horizontal/inputs/SA<nn>/ and the Work math-notes files listed in
WORK_MATHNOTES_BY_TOPIC.tsv. Outputs: results_register/horizontal/sweep1/SA<nn>/."""
import csv, re, sys, json, pathlib, collections, importlib.util
csv.field_size_limit(10 ** 9)
sys.stdout.reconfigure(encoding="utf-8")
DOC = pathlib.Path(r"C:\Users\user\Documents")
INP = DOC / "results_register" / "horizontal" / "inputs"
OUTROOT = DOC / "results_register" / "horizontal" / "sweep1"
TOOLS = pathlib.Path(__file__).resolve().parent
WHO = "Claude Opus 5.5 at effort max, a28ea31fa17dd65e1, horizontal sweep 1"


def clean(s):
    return re.sub(r"\s+", " ", (s or "").replace("\t", " ")).strip()


def parse_pro(path):
    """Entries in order: dict(heading, section, line, source, kind, manuscript, body)."""
    out, sec, cur = [], "", None
    lines = path.read_text(encoding="utf-8").splitlines()
    for i, ln in enumerate(lines, 1):
        if ln.startswith("### "):
            if cur:
                out.append(cur)
            cur = dict(heading=clean(ln[4:]), section=sec, line=i, source="", kind="", manuscript="", body=[])
        elif ln.startswith("## "):
            if cur:
                out.append(cur)
                cur = None
            sec = clean(ln[3:])
        elif cur is not None:
            m = re.match(r"\*\*(Source|Kind|Manuscript|Context comparison|Results register|Search record)[^*]*:\*\*\s*(.*)", ln)
            if m:
                k = m.group(1).lower()
                if k in ("source", "kind", "manuscript"):
                    cur[k] = clean(m.group(2))
                continue
            if ln.strip():
                cur["body"].append(ln.strip())
    if cur:
        out.append(cur)
    for e in out:
        e["body"] = clean(" ".join(e["body"]))
    return out


def parse_work(path):
    """Units = '## ' sections, in order: dict(title, line, bolds, text)."""
    out, cur = [], None
    lines = path.read_text(encoding="utf-8").splitlines()
    pre = "## " if any(l.startswith("## ") for l in lines) else "# "
    for i, ln in enumerate(lines, 1):
        if ln.startswith(pre):
            if cur:
                out.append(cur)
            cur = dict(title=clean(ln[len(pre):]), line=i, text=[])
        elif cur is not None and ln.strip():
            cur["text"].append(ln.strip())
    if cur:
        out.append(cur)
    for u in out:
        t = " ".join(u["text"])
        u["bolds"] = [clean(b).strip(" .:") for b in re.findall(r"\*\*(.+?)\*\*", t)]
        u["text"] = clean(t)
    return out


def load(topic):
    tdir = INP / topic
    idx = list(csv.DictReader(open(tdir / "NOTES_INDEX.tsv", encoding="utf-8"), delimiter="\t"))
    pkgs = collections.OrderedDict()
    for r in idx:
        pkgs.setdefault(r["package"], []).append(r)
    entries = []
    for pkg, rs in pkgs.items():
        f = tdir / "pro" / f"{pkg}_notes.md"
        parsed = parse_pro(f) if f.exists() else []
        for r in rs:
            n = int(r["entry_id"].split("#")[1])
            e = parsed[n - 1] if 0 < n <= len(parsed) else None
            ok = bool(e) and clean(e["heading"]) == clean(r["heading"])
            if e and not ok:  # find by heading
                e2 = next((x for x in parsed if clean(x["heading"]) == clean(r["heading"])), None)
                e, ok = (e2, True) if e2 else (e, False)
            srcsc = ""
            if e and e["source"]:
                m = re.search(r"[Ss]cans?(?:\(s\))?\s*([0-9][0-9–\-, and]*)", e["source"])
                if m:
                    srcsc = ",".join(str(int(x)) for x in re.findall(r"\d+", m.group(1)))
            entries.append(dict(id=r["entry_id"], src="pro", package=pkg, cote=r["cotes"], heading=clean(r["heading"]), src_scans=srcsc,
                                kind=clean(r["kind"]).rstrip("."), scans=clean(r["scans_cited"]),
                                section=e["section"] if e else "", line=e["line"] if e else 0,
                                manuscript=e["manuscript"] if e else "", body=e["body"] if e else "",
                                file=str(f.relative_to(DOC)), matched=ok))
    wm = [r for r in csv.DictReader(open(INP / "WORK_MATHNOTES_BY_TOPIC.tsv", encoding="utf-8"), delimiter="\t") if r["topic"] == topic]
    for r in wm:
        p = DOC / r["path"]
        if not p.exists():
            print("missing work file:", r["folder"], r["path"], file=sys.stderr)
            continue
        for n, u in enumerate(parse_work(p), 1):
            scans = ",".join(sorted(set(re.findall(r"\b(\d{3})\b", u["text"])))[:12])
            entries.append(dict(id=f"work:{r['folder']}#{n}", src="work", package=r["folder"], cote=r["cote"],
                                heading=u["title"], kind="work unit: " + u["title"], scans=scans, section=u["title"],
                                line=u["line"], manuscript="", body=u["text"], bolds=u["bolds"], file=r["path"], matched=True))
    return entries


def listing(topic):
    es = load(topic)
    print(f"{topic}: {len(es)} entries ({sum(e['src']=='pro' for e in es)} pro, {sum(e['src']=='work' for e in es)} work units); "
          f"unmatched headings: {sum(not e['matched'] for e in es)}")
    lastsec = None
    for e in es:
        if e["src"] == "pro":
            if (e["package"], e["section"]) != lastsec:
                print(f"## {e['package']} | {e['section'][:90]}")
                lastsec = (e["package"], e["section"])
            k = {"reading question": "RQ", "unproved claim": "UC", "unpursued implication": "UI", "own idea": "OI",
                 "self-flagged": "SF", "withdrawn in the same text": "WD", "conjecture": "CJ", "": "-"}.get(e["kind"].lower(), e["kind"][:14])
            man = (" | " + e["manuscript"][:60]) if e["manuscript"] else ""
            print(f"{e['id'].split('#')[1]}|{k}|{e['scans'][:11]}|{e['heading'][:86]}{man}")
        else:
            b = "; ".join(e["bolds"])[:230]
            print(f"W {e['id']} | {e['heading'][:40]} | {b}")


def build(topic):
    spec = importlib.util.spec_from_file_location("cl", TOOLS / f"clusters_{topic}.py")
    cl = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cl)
    es = load(topic)
    out = OUTROOT / topic
    out.mkdir(parents=True, exist_ok=True)
    CL = [(k, obj, re.compile(rx, re.I)) for k, obj, rx in cl.CLUSTERS]
    items, fallback = collections.OrderedDict(), {}
    for k, obj, _ in CL:
        items[k] = dict(object=obj, entries=[], kinds=collections.Counter(), cotes=set())
    for k, obj in getattr(cl, "EXTRA_OBJECTS", {}).items():
        items.setdefault(k, dict(object=obj, entries=[], kinds=collections.Counter(), cotes=set()))
    nxt = max([int(k.split("-")[1]) for k in items] + [0]) + 1
    reads = getattr(cl, "READ", {})      # entry_id -> (basis, fidelity, object or '', note)
    forced = getattr(cl, "FORCE", {})    # entry_id -> item key
    rows = []
    mism = []
    for e in es:
        blob = " ".join([e["heading"], e["manuscript"], " ".join(e.get("bolds", []))])
        key = forced.get(e["id"])
        if key is None:
            for rxs, k2 in getattr(cl, "BODY_RULES", []):
                if re.search(rxs, e["body"][:60]):
                    key = k2
                    break
        if key is None:
            for k, obj, rx in CL:
                if rx.search(blob):
                    key = k
                    break
        if key is None:
            for (pk, sp), k2 in getattr(cl, "SECTION_MAP", {}).items():
                if e["package"] == pk and e["section"].startswith(sp):
                    key = k2
                    break
        if key is None:
            fk = (e["package"], e["section"]) if e["src"] == "pro" else (e["package"], "work:" + e["heading"])
            if fk not in fallback:
                fallback[fk] = f"{topic}-{nxt}"
                nxt += 1
                items[fallback[fk]] = dict(object=(e["section"] if e["src"] == "pro" else f"{e['heading']} ({e['package']})").split(". ", 1)[-1][:120],
                                           entries=[], kinds=collections.Counter(), cotes=set())
            key = fallback[fk]
        it = items[key]
        it["entries"].append(e["id"])
        it["kinds"][e["kind"] or "-"] += 1
        it["cotes"].add(f"{e['cote']}:{e['scans'][:20]}")
        basis, fid, obj, note = reads.get(e["id"], (getattr(cl, "DEFAULT_BASIS", "index-row") if e["src"] == "pro" else "entry-read", "not checked", "", ""))
        if e["src"] == "pro" and basis == "index-row" and not e["heading"]:
            basis = "entry-read"
        sc = e.get("src_scans") or e["scans"]
        if e.get("src_scans") and e["scans"] and set(e["src_scans"].split(",")) != set(e["scans"].split(",")):
            mism.append(e["id"])
        rows.append([e["id"], topic, e["cote"], sc, e["kind"] or "-", obj or it["object"], e["manuscript"][:160],
                     key, basis, fid, "", (note + " | " if note else "") + e["heading"][:160]])
    flags = list(getattr(cl, "FLAGS", []))
    lm = getattr(cl, "LMLENS", None)
    if lm:
        rx = re.compile(lm)
        for e in es:
            if e["src"] == "pro" and rx.search(e["heading"] + " " + e["manuscript"]):
                flags.append(("the LM/Dérivateurs lens", e["id"], "the note reads the page through a research-run or LM planning question: " + e["heading"][:120], "heading (index row)"))
    fl_by_entry = collections.defaultdict(list)
    for f in flags:
        for w in re.findall(r"[A-Za-z0-9_+\-]+#\d+|work:[A-Za-z0-9_\-]+#\d+", f[1]):
            fl_by_entry[w].append(f[0])
    for r in rows:
        r[10] = "; ".join(sorted(set(fl_by_entry.get(r[0], []))))
    with open(out / "PLACEMENT.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["entry_id", "topic", "cote", "scans", "kind", "object", "his_term", "item", "basis", "fidelity", "flag", "note"])
        w.writerows(rows)
    stm = getattr(cl, "STATEMENTS", {})
    with open(out / "OBJECTS.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["item", "object", "kind", "statement", "entries", "cotes_scans", "status_on_pages", "cross_topic", "flags"])
        for k, it in items.items():
            if not it["entries"]:
                continue
            s = stm.get(k, ("", "not checked", ""))
            iflags = sorted({f for e in it["entries"] for f in fl_by_entry.get(e, [])})
            w.writerow([k, it["object"], "; ".join(f"{a}:{b}" for a, b in it["kinds"].most_common(4)), s[0],
                        " ".join(it["entries"]), "; ".join(sorted(it["cotes"]))[:400], s[1], s[2], "; ".join(iflags)])
    with open(out / "FLAGS.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["kind", "where", "what", "evidence"])
        w.writerows(flags)
    with open(out / "CHECK_EVENTS.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["id", "date_utc", "who", "how", "result", "where"])
        for c in getattr(cl, "CHECKS", []):
            w.writerow([c[0], c[1], WHO, c[2], c[3], c[4]])
    used = sum(1 for it in items.values() if it["entries"])
    bc = collections.Counter(r[8] for r in rows)
    fc = collections.Counter(r[9] for r in rows if r[8] == "passage-read")
    print(f"{topic}: {len(rows)} rows ({sum(e['src']=='pro' for e in es)} pro entries, {sum(e['src']=='work' for e in es)} work units); "
          f"{used} items ({sum(1 for k in items if k in dict((c[0], 1) for c in CL) and items[k]['entries'])} named clusters); "
          f"basis {dict(bc)}; fidelity {dict(fc)}; flags {len(flags)} {dict(collections.Counter(f[0] for f in flags))}; checks {len(getattr(cl, 'CHECKS', []))}; index scans differ from the note's Source scans: {len(mism)}")
    (out / "_index_scan_mismatch.txt").write_text(chr(10).join(mism), encoding="utf-8")
    big = sorted(((len(it["entries"]), k, it["object"]) for k, it in items.items() if it["entries"]), reverse=True)[:12]
    for n, k, o in big:
        print(f"   {k} {n} {o[:80]}")


if __name__ == "__main__":
    {"list": listing, "build": build}[sys.argv[1]](sys.argv[2])
