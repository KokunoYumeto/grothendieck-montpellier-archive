"""Sweep 2, part 2 (broad agent a0c4bb37, Claude Opus 5.5 at effort max, 18 Nov 2026).
1. The interlinking of section 5 of the handbook sketch, by script, as candidates on shared pages (cote and scan):
   sweep2/GLOBAL/INTERLINKS/ITEM_UNITS.tsv     item -> the companion units on the same pages (UNITS_DRAFT_20261118.tsv)
   sweep2/GLOBAL/INTERLINKS/ITEM_REGISTER.tsv  item -> the research-run statements on the same pages (HIS_PLACES.tsv)
   sweep2/GLOBAL/INTERLINKS/ITEM_DEPENDS.tsv   item -> item, where a statement on A's pages uses one on B's (EDGES.tsv)
   sweep2/GLOBAL/INTERLINKS/HIS_CLAIMS.tsv     each claim of his -> the statements on its pages, with their status
2. results_register/horizontal/WHAT_IS_WHERE.md: the map in the sketch's outline (Part, chapter = topic, object).
Reads sweep2 and the register; writes only those files. Rerun after every check-in.
usage: python -I -B build_what_is_where.py"""
import csv, re, sys, collections, pathlib, datetime

sys.stdout.reconfigure(encoding="utf-8")
csv.field_size_limit(10 ** 9)
D = pathlib.Path(r"C:\Users\user\Documents")
H = D / "results_register" / "horizontal"
S2 = H / "sweep2"
G = S2 / "GLOBAL"
IL = G / "INTERLINKS"
IL.mkdir(exist_ok=True)


def read(p):
    with open(p, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def write(p, rows, fields):
    with open(p, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: re.sub(r"\s+", " ", str(r.get(k, ""))) for k in fields})


def scans_of(cote_field, scans_field):
    """(cote, scan) pairs of a row: 'c/s' pairs as written, bare numbers with the row's first cote; ranges a-b"""
    c0 = re.split(r"[,;+ ]+", (cote_field or "").strip())[0] if (cote_field or "").strip() else ""
    out = set()
    s = scans_field or ""
    for c, a in re.findall(r"(\d{1,3}(?:-\d)?)/(\d{1,3})", s):
        out.add((c, int(a)))
    s = re.sub(r"\d{1,3}(?:-\d)?/\d{1,3}", " ", s)
    for a, b in re.findall(r"(\d{1,3})\s*[-–]\s*(\d{1,3})", s):
        a, b = int(a), int(b)
        if c0 and 0 <= b - a <= 80:
            out |= {(c0, x) for x in range(a, b + 1)}
    s = re.sub(r"\d{1,3}\s*[-–]\s*\d{1,3}", " ", s)
    for a in re.findall(r"\d{1,3}", s):
        if c0:
            out.add((c0, int(a)))
    return out


# --- the map
OBJ = read(G / "GLOBAL_OBJECTS.tsv")
ITEMS, PLACE = {}, collections.defaultdict(list)
for d in sorted(S2.glob("SA[0-9][0-9]")):
    for r in read(d / "OBJECTS.tsv"):
        r["topic"] = d.name
        ITEMS[r["item"].strip()] = r
    for r in read(d / "PLACEMENT.tsv"):
        PLACE[(r.get("item") or "").strip()].append(r)
UN = {u["entry_id"]: u for u in read(S2 / "inputs" / "UNITS.tsv")}
ALIAS = {r["alias"]: r["canonical"] for r in read(G / "ID_ALIASES.tsv")}
for r in read(G / "STALE_PLACEMENTS.tsv"):
    if r.get("settled_to"):
        ALIAS[r["entry_id"]] = r["settled_to"]


def canon(e):
    seen = set()
    while e in ALIAS and e not in seen:
        seen.add(e)
        e = ALIAS[e]
    return e


ISCANS = {it: set().union(*(scans_of(r.get("cote"), r.get("scans")) for r in rows)) if rows else set()
          for it, rows in PLACE.items()}
# --- interlinks on shared pages
UNITS_C = read(D / "grothendieck_archive_transcription_20261110" / "UNITS_DRAFT_20261118.tsv")
by_page_u = collections.defaultdict(set)
for u in UNITS_C:
    for p in scans_of(u["cote"], u["scans"]):
        by_page_u[p].add(u["unit"])
MIS = [r["tag_prefix"] for r in read(G / "MISPLACED_REGISTER_PLACES.tsv")] if (G / "MISPLACED_REGISTER_PLACES.tsv").exists() else []
HP = [r for r in read(D / "results_register" / "sweep2_global" / "HIS_PLACES.tsv") if not any(r["tag"].startswith(m) for m in MIS)]
by_page_r = collections.defaultdict(set)
for r in HP:
    for p in scans_of(r["cote"], r["scans"]):
        by_page_r[p].add(r["tag"])
REG = {r["tag"]: r for r in read(D / "results_register" / "REGISTER.tsv")}
EDGES = [r for r in read(D / "results_register" / "EDGES.tsv") if r["kind"] in ("uses", "depends_on", "cites", "applies")]
iu, ir = [], []
I2U, I2R = collections.defaultdict(collections.Counter), collections.defaultdict(collections.Counter)
for it, ps in ISCANS.items():
    if it not in ITEMS:
        continue
    for p in ps:
        for u in by_page_u.get(p, ()):
            I2U[it][u] += 1
        for t in by_page_r.get(p, ()):
            I2R[it][t] += 1
    for u, n in I2U[it].most_common():
        iu.append(dict(item=it, topic=ITEMS[it]["topic"], unit=u, shared_pages=n))
    for t, n in I2R[it].most_common():
        g = REG.get(t, {})
        ir.append(dict(item=it, topic=ITEMS[it]["topic"], statement=t, status=g.get("status", ""), shared_pages=n,
                       text=(g.get("statement") or "")[:240]))
write(IL / "ITEM_UNITS.tsv", iu, ["item", "topic", "unit", "shared_pages"])
write(IL / "ITEM_REGISTER.tsv", ir, ["item", "topic", "statement", "status", "shared_pages", "text"])
R2I = collections.defaultdict(set)
for it, c in I2R.items():
    for t in c:
        R2I[t].add(it)
dep = collections.Counter()
for e in EDGES:
    for a in R2I.get(e["from"], ()):
        for b in R2I.get(e["to"], ()):
            if a != b:
                dep[(a, b)] += 1
write(IL / "ITEM_DEPENDS.tsv", [dict(item=a, uses=b, via_edges=n) for (a, b), n in dep.most_common()], ["item", "uses", "via_edges"])
CLAIM = re.compile(r"claim|stated|asserted|without proof|conjectur|question|open|unproved", re.I)
hc = []
for it, r in ITEMS.items():
    if CLAIM.search((r.get("kind") or "") + " " + (r.get("status_on_pages") or "")):
        for t, n in I2R.get(it, collections.Counter()).most_common(12):
            g = REG.get(t, {})
            if g.get("status") in ("Proved", "Refuted", "Known", "Open"):
                hc.append(dict(item=it, topic=r["topic"], his_status=(r.get("status_on_pages") or "")[:80], statement=t,
                               status=g.get("status"), shared_pages=n, text=(g.get("statement") or "")[:200]))
write(IL / "HIS_CLAIMS.tsv", hc, ["item", "topic", "his_status", "statement", "status", "shared_pages", "text"])
# --- outline
TITLE = {}
for tp in sorted(H.glob("inputs/SA[0-9][0-9]/TOPIC.md")):
    TITLE[tp.parent.name] = re.sub(r"^#\s*SA\d\d:\s*", "", tp.read_text(encoding="utf-8").splitlines()[0]).strip()
PARTS = [("0", "Conventions and the foundations we use", []),
         ("I", "The Galois theory of the tower", ["SA28", "SA29", "SA30", "SA31", "SA20"]),
         ("II", "Homotopy", ["SA24", "SA25", "SA26", "SA27", "SA32"]),
         ("III", "Cohomology and motives", ["SA05", "SA06", "SA07", "SA15", "SA08", "SA09", "SA14", "SA19", "SA18", "SA16",
                                            "SA17", "SA12", "SA13", "SA23"]),
         ("IV", "Shapes and stratifications", ["SA10", "SA11", "SA21", "SA01", "SA02", "SA03", "SA04"]),
         ("V", "Around his teaching", ["SA22"])]
NONMATH = re.compile(r"documentar|archiv|apparatus|reused|source accounting|title sheet|dates|provenance|biograph|"
                     r"administr|catalog|cover|inventory|record|letter only|^lens|link to the research", re.I)
NONMATH_OBJ = re.compile(r"^(documentary|package apparatus|the reused|reused|title sheets?|covers?|dates|catalogue|"
                         r"provenance|the folder's titles|apparatus)", re.I)
HOMES = {r["item"]: r["home_topic"] for r in read(G / "ITEM_HOMES.tsv")} if (G / "ITEM_HOMES.tsv").exists() else {}
LINKS = read(G / "LINKS.tsv")
REL = collections.defaultdict(set)
for l in LINKS:
    if l.get("to_item"):
        REL[l["item"]].add(l["to_item"])
        REL[l["to_item"]].add(l["item"])
TAG_OF = {}
for o in OBJ:
    for it in o["items"].split():
        TAG_OF[it] = o["tag"]
DEPS = collections.defaultdict(collections.Counter)
DEPD = collections.defaultdict(collections.Counter)
for (a, b), n in dep.items():
    if a in TAG_OF and b in TAG_OF and TAG_OF[a] != TAG_OF[b]:
        DEPS[TAG_OF[a]][TAG_OF[b]] += n
        DEPD[TAG_OF[b]][TAG_OF[a]] += n


# the deep agents' own dependency readings (sweep2/SA<nn>/DEPENDS.tsv, part 2), in their several formats
AGU, AGD = collections.defaultdict(set), collections.defaultdict(set)
n_agdep, n_corr = collections.Counter(), collections.Counter()
for f in sorted(S2.glob("SA[0-9][0-9]/DEPENDS.tsv")):
    for r in read(f):
        it = (r.get("item") or "").strip()
        rel = (r.get("relation") or "").strip().lower()
        other = next(((r.get(k) or "").strip() for k in ("other_item", "other", "uses_item") if (r.get(k) or "").strip()), "")
        if not rel:
            if (r.get("uses") or "").strip():
                rel, other = "uses", r["uses"].strip()
            elif (r.get("used_by") or "").strip():
                rel, other = "used by", r["used_by"].strip()
        for o in re.findall(r"SA\d\d-[0-9A-Z]+", other):
            if it in TAG_OF and o in TAG_OF and TAG_OF[it] != TAG_OF[o]:
                if rel == "uses":
                    AGU[TAG_OF[it]].add(TAG_OF[o]); AGD[TAG_OF[o]].add(TAG_OF[it]); n_agdep[f.parent.name] += 1
                elif rel == "used by":
                    AGU[TAG_OF[o]].add(TAG_OF[it]); AGD[TAG_OF[it]].add(TAG_OF[o]); n_agdep[f.parent.name] += 1
for f in sorted(S2.glob("SA[0-9][0-9]/CORRECTIONS.tsv")):
    n_corr[f.parent.name] = len(read(f))


def where(items):
    src = collections.Counter()
    for it in items:
        for r in PLACE.get(it, []):
            e = canon((r.get("entry_id") or "").strip())
            s = e.split("#")[0]
            src[s] += 1
    out = []
    for s, n in src.most_common(5):
        f = next((UN[e]["source_file"] for e in UN if e.startswith(s + "#")), "") if s else ""
        out.append(f"{s} ({n})" + (f": `{f}`" if f else ""))
    if len(src) > 5:
        out.append(f"and {len(src) - 5} more sources")
    return out


def short(s, n=160):
    s = re.sub(r"\s+", " ", s or "").strip()
    return s if len(s) <= n else s[:n - 1] + "…"


home_of = {}
for o in OBJ:
    its = o["items"].split()
    tops = [HOMES.get(i, ITEMS[i]["topic"]) for i in its if i in ITEMS]
    home_of[o["tag"]] = collections.Counter(tops).most_common(1)[0][0] if tops else ""


def is_nonmath(o):
    its = [ITEMS[i] for i in o["items"].split() if i in ITEMS]
    return bool(its) and all(NONMATH.search(r.get("kind") or "") or NONMATH_OBJ.search(r.get("object") or "") for r in its)


def is_lens(o):
    return all("lens" in (ITEMS[i].get("kind") or "").lower() for i in o["items"].split() if i in ITEMS)


now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
STRANDS = read(G / "MERGES.tsv")
L = [f"# What is where: the Montpellier notes in the handbook's outline",
     "",
     f"Built {now} by `results_register/horizontal/sweep2/_tools/build_what_is_where.py`, written by the broad agent a0c4bb37 (Claude Opus 5.5 at effort max), from the sweep-2 tables. Do not edit this file by hand: rerun the script.",
     "",
     "**How to use it.** Search this file for a word: an object, a cote (\"cote 93\"), a package (\"MPL_29_095-140\"), a folder (\"K157-3-23\") or a tag. Each object gives:",
     "- its global tag (`H???`) and name;",
     "- its items, with their topics;",
     "- where it is: cotes and scans, then the Pro packages and Work or Codex folders with the number of entries and the notes file. The transcription `.tex` lies next to the notes file, with `\\scanpage{N}` at each scan;",
     "- its status on his pages and its flags;",
     "- its links: related objects (cross_topic), the objects it uses and is used by (through the research-run statements on its pages, `EDGES.tsv`), the research-run statements on its pages, and the companion units on its pages.",
     "",
     "Part, chapter and order follow section 4 of `grothendieck_archive_montpellier/HANDBOOK_SKETCH_20261118.md`. Chapters are topics. An object sits in the chapter of the topic that holds most of its items (or its home topic, `GLOBAL/ITEM_HOMES.tsv`); the other topics point to it.",
     "",
     "The links \"uses\", \"used by\", \"statements on these pages\" and \"units\" are candidates found by shared pages, not readings. Their tables are in `sweep2/GLOBAL/INTERLINKS/`.",
     ""]
n_obj = len(OBJ)
nm = [o for o in OBJ if is_nonmath(o) and not is_lens(o)]
ln = [o for o in OBJ if is_lens(o)]
L += [f"**Counts:** {n_obj} objects from {len(ITEMS)} items in 32 topics, of which:",
      f"- {sum(1 for o in OBJ if int(o['n_topics']) > 1)} lie in more than one topic;",
      f"- {len(nm)} are non-mathematical (Appendix A);",
      f"- {len(ln)} are links to the research runs (Appendix B).",
      "",
      f"**Interlinks** (candidates on shared pages):",
      f"- {len(iu)} item-unit links, from {len(UNITS_C)} companion units;",
      f"- {len(ir)} item-statement links, from {len(HP)} places of research-run statements;",
      f"- {len(dep)} item-to-item uses;",
      f"- {len(hc)} links from claims of his to proved, refuted, known or open statements on the same pages.",
      "",
      "## Reports of sweep 2 (each with its places, readings decided on the scans, and corrections)", ""]
for rp in sorted((S2 / "REPORTS").glob("*.md")):
    first = next((ln.lstrip("# ").strip() for ln in rp.read_text(encoding="utf-8").splitlines() if ln.startswith("#")), rp.stem)
    L.append(f"- [{rp.name}](sweep2/REPORTS/{rp.name}): {short(first, 150)}")
L += ["",
      "## How the outline should change (what the map shows)",
      "- **Part 0 has no topic.** Its pointers come from the items' literature fields, which sweep 3 fills.",
      "- **SA01-SA04 (the catalogue section \"Géométrie et topologie combinatoire\", cotes 69-102 and 154) mix two parts.**",
      "  - The combinatorial objects stay in Part IV: regular polyhedra over rings, pseudolines, the natural-map schemes, immersions, the Euler-characteristic axioms.",
      "  - Their algebraic geometry belongs in Part III:",
      "    - the crystals, Barsotti-Tate groups and connections of cote 93 (strand TH-C93, joined to TH-CRYS);",
      "    - good reduction on cote 100 (H0 tag shared with SA15-19);",
      "    - Greenberg-Néron on cote 91;",
      "    - quadratic algebras and extensions on cotes 83-84.",
      "  - These objects are listed in their chapters and named again under Part III, \"From other parts\".",
      "- **SA20 (Autour d'Esquisse) mixes Part I and Part IV.**",
      "  - Its tame-topology objects (cotes 120-121, the \"remords\", tubulure and ombre) belong with SA10, SA11 and SA21 in Part IV.",
      "  - Its plane trees (152), polyhedral chapter (119), analysers (153) and tannakian duality (155) stay with the Esquisse. The last two go with the λ-structures of Part III.",
      "- **SA09's cote 138 (\"Cartes. Étude arithmétique\") is dessins and the Galois action:** Part I. Its catalogue date of 1976-77 is not reliable, since the folder holds documents of 1978 and 1980.",
      "- **SA08-SA09 (the de Rham complex) also hold the SGA 7 IX typescript** (Néron models, the monodromy pairing). That belongs with SGA (SA12) and with abelian varieties (SA18).",
      "- **The research-run mappings** (16 \"lens\" items in SA24-SA27) are links, not his objects: Appendix B.",
      "- **Part III is the largest part** (14 topics). It reads best in four groups:",
      "  - motives and crystals: SA05-07, SA15;",
      "  - de Rham and descent: SA08-09, SA17;",
      "  - Picard, Jacobians, abelian varieties and elliptic curves: SA14, SA19, SA18, SA16;",
      "  - SGA and EGA: SA12, SA13, SA23.",
      "",
      "## Strands (joined by hand) and the largest themes",
      ""]
for m in STRANDS:
    tags = sorted({TAG_OF[i] for i in m["items"].split() if i in TAG_OF})
    L.append(f"- **{m['name']}** ({m['kind']}): {', '.join(tags)}")
    L.append(f"  - items: {m['items']}")
    L.append(f"  - {short(m['settled_as'], 300)}")
TH = sorted(read(G / "THEMES.tsv"), key=lambda r: -int(r["n_objects"]))[:12]
for t in TH:
    L.append(f"- theme {t['theme']} ({t['n_objects']} objects; {t['topics']}): {short(t['name_from_largest_item'], 110)}; tags {t['tags']}")
L.append("")
placed_obj = set()
for pid, pname, tops in PARTS:
    L += [f"## Part {pid}. {pname}", ""]
    if not tops:
        L += ["No topic yet. These are the foundations the items rely on (EGA, SGA, Stacks, Kerodon, the literature), by locator, filled from the items' literature fields in sweep 3.", ""]
    for t in tops:
        tn = S2 / t / "TOPIC_NOTES.md"
        cotes = collections.Counter()
        for it, r in ITEMS.items():
            if r["topic"] == t:
                for (c, s) in ISCANS.get(it, ()):
                    cotes[c] += 1
        L += [f"### {t}. {TITLE.get(t, '')}",
              "",
              f"Topic notes: [sweep2/{t}/TOPIC_NOTES.md](sweep2/{t}/TOPIC_NOTES.md)"
              + (f"; the topic agent's own map, items in mathematical order: [sweep2/{t}/WHAT_IS_WHERE.md](sweep2/{t}/WHAT_IS_WHERE.md)" if (S2 / t / "WHAT_IS_WHERE.md").exists() else "")
              + (f"; corrections ({n_corr[t]}): [sweep2/{t}/CORRECTIONS.tsv](sweep2/{t}/CORRECTIONS.tsv)" if n_corr[t] else "")
              + f". Main cotes: {', '.join(c for c, _ in cotes.most_common(10))}.",
              ""]
        here = [o for o in OBJ if home_of[o["tag"]] == t and not is_nonmath(o) and not is_lens(o)]
        here.sort(key=lambda o: [int(x) if x.isdigit() else 999 for x in re.findall(r"\d+|[A-Z]", min(o["items"].split()))])
        for o in here:
            placed_obj.add(o["tag"])
            its = o["items"].split()
            L.append(f"#### {o['tag']} · {short(o['object'], 140)}")
            L.append(f"- **Items:** " + ", ".join(f"{i} ({ITEMS[i]['topic']})" for i in its if i in ITEMS)
                     + (f"; theme {o['theme']}" if o.get("theme") else "") + (f"; strand {o['strand']}" if o.get("strand") else ""))
            L.append(f"- **Where:** {short(o['cotes_scans'], 200)}")
            for wline in where(its):
                L.append(f"  - {wline}")
            L.append(f"- **Status on the pages:** {short(o['status_on_pages'], 200)}" + (f". **Flags:** {short(o['flags'], 200)}" if o.get("flags") else ""))
            rel = sorted({TAG_OF[x] for i in its for x in REL.get(i, ()) if x in TAG_OF and TAG_OF[x] != o["tag"]})
            uses = [f"{k} ({n})" for k, n in DEPS[o["tag"]].most_common(5)]
            used = [f"{k} ({n})" for k, n in DEPD[o["tag"]].most_common(5)]
            st = collections.Counter()
            for i in its:
                for tg in I2R.get(i, ()):
                    st[REG.get(tg, {}).get("status", "?")] += 1
            un = sorted({u for i in its for u in I2U.get(i, ())})
            links = []
            if rel:
                links.append("related " + ", ".join(rel[:8]) + (" …" if len(rel) > 8 else ""))
            if AGU.get(o["tag"]):
                links.append("uses (the topic agents' reading) " + ", ".join(sorted(AGU[o["tag"]])[:8]))
            if AGD.get(o["tag"]):
                links.append("used by (the topic agents' reading) " + ", ".join(sorted(AGD[o["tag"]])[:8]))
            if uses:
                links.append("uses (through research-run statements on its pages) " + ", ".join(uses))
            if used:
                links.append("used by (through research-run statements) " + ", ".join(used))
            if st:
                links.append("research-run statements on these pages: " + ", ".join(f"{k} {v}" for k, v in st.most_common()))
            if un:
                links.append(f"companion units: {', '.join(un[:6])}" + (f" and {len(un) - 6} more" if len(un) > 6 else ""))
            if links:
                L.append("- **Links:** " + "; ".join(links))
            L.append("")
        others = [o for o in OBJ if t in o["topics"].split() and home_of[o["tag"]] != t and not is_nonmath(o) and not is_lens(o)]
        if others:
            L.append("**Also in this topic, placed in another chapter:** " + "; ".join(f"{o['tag']} ({home_of[o['tag']]}: {short(o['object'], 60)})" for o in others))
            L.append("")
    if pid == "III":
        fo = [o for o in OBJ if o.get("strand") and ("TH-C93" in o["strand"] or "TH-CRYS" in o["strand"]) and home_of[o["tag"]] in ("SA01", "SA02", "SA03", "SA04")]
        if fo:
            L += ["### From other parts: the algebraic geometry of SA01-SA04", ""]
            L += [f"- {o['tag']} · {short(o['object'], 120)} (in {home_of[o['tag']]}; strand {o['strand']})" for o in fo]
            L.append("")
L += ["## Appendix A. Non-mathematical material and its places", "",
      "This covers package apparatus, documentary sheets, covers, dates, reused typescripts, letters as documents, and biography.", ""]
for t in sorted({home_of[o["tag"]] for o in nm}):
    L.append(f"### {t}")
    for o in [o for o in nm if home_of[o["tag"]] == t]:
        L.append(f"- {o['tag']} · {short(o['object'], 150)} (items {o['items']}; {short(o['cotes_scans'], 100)})")
    L.append("")
L += ["## Appendix B. Links to the research runs (lens items)", ""]
L += [f"- {o['tag']} · {short(o['object'], 140)} (items {o['items']})" for o in ln] or ["- none"]
L.append("")
(H / "WHAT_IS_WHERE.md").write_text("\n".join(L) + "\n", encoding="utf-8")
print(now, "| objects", n_obj, "placed in chapters", len(placed_obj), "non-math", len(nm), "lens", len(ln),
      "| item-unit", len(iu), "item-statement", len(ir), "item uses", len(dep), "his claims", len(hc),
      "| lines", len(L))
