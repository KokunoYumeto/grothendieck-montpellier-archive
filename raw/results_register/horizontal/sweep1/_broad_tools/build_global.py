"""Horizontal sweep 1, broad agent a0c4bb37 (Claude Opus 5.5 at effort max), 18 Nov 2026.
Builds sweep1/GLOBAL from every topic's OBJECTS.tsv and PLACEMENT.tsv:
  GLOBAL_OBJECTS.tsv  one 4-character tag (H + 3 base-36 characters) per global object: the items of every topic that
                      are the same object (strict level);
  THEMES.tsv          themes TH-nn: objects linked across topics (cross_topic links, the deep agents' reported lists,
                      weak name matches, partly shared entries): related, not the same;
  LINKS.tsv           every cross-topic pointer found in cross_topic (item ids, topic ids, cotes), resolved to topics;
  merge_log.tsv, shared_cotes_packages.json, and the INBOX\\<agent>.md lists (between the AUTO markers).
Strict merges never join two items of one topic (the topic agent kept them apart). Tags already given keep their
objects on a rerun. Writes only under sweep1/GLOBAL and sweep1/INBOX. usage: python -I -B build_global.py"""
import csv, re, sys, collections, pathlib, json, datetime

sys.stdout.reconfigure(encoding="utf-8")
csv.field_size_limit(10 ** 9)
H = pathlib.Path(r"C:\Users\user\Documents\results_register\horizontal")
S1 = H / "sweep1"
G = S1 / "GLOBAL"
IN = S1 / "INBOX"
G.mkdir(exist_ok=True)
IN.mkdir(exist_ok=True)
AGENTS = {"a34c04448e8299803": "SA32 SA24 SA25 SA26 SA27 SA17 SA08 SA09",
          "ae4ae3dc17acaa440": "SA28 SA29 SA30 SA31 SA20 SA22",
          "a28ea31fa17dd65e1": "SA16 SA18 SA19 SA14 SA15 SA05 SA06 SA07",
          "a6d42bf6fe2b0d8a8": "SA01 SA02 SA03 SA04 SA10 SA11 SA21",
          "a0c4bb37": "SA12 SA13 SA23"}
AGENT = {t: a for a, ts in AGENTS.items() for t in ts.split()}


def read(p):
    with open(p, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def write(p, rows, fields):
    with open(p, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: re.sub(r"\s+", " ", str(r.get(k, ""))) for k in fields})


# cote -> topic, from the topic tables of the inputs
COTE = {}
for tp in sorted(H.glob("inputs/SA[0-9][0-9]/TOPIC.md")):
    t = tp.parent.name
    for line in tp.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*(\d+(?:-\d+)?)\s*\|", line)
        if m:
            COTE.setdefault(m.group(1), t)
items, places = {}, collections.defaultdict(list)
for d in sorted(S1.glob("SA[0-9][0-9]")):
    if (d / "OBJECTS.tsv").exists():
        for r in read(d / "OBJECTS.tsv"):
            it = (r.get("item") or "").strip()
            if it:
                r["topic"] = d.name
                items[it] = r
    if (d / "PLACEMENT.tsv").exists():
        places[d.name] = read(d / "PLACEMENT.tsv")
done_topics = sorted({r["topic"] for r in items.values()})
missing = sorted(t for t in AGENT if t not in done_topics)
# coverage per topic: NOTES_INDEX rows, Work folders, and Codex/API folder notes that are in neither list
WK = collections.defaultdict(set)
for r in read(H / "inputs" / "WORK_MATHNOTES_BY_TOPIC.tsv"):
    WK[r["topic"]].add(r["folder"])
COV = []
for d in sorted(H.glob("inputs/SA[0-9][0-9]")):
    t = d.name
    ni = read(d / "NOTES_INDEX.tsv") if (d / "NOTES_INDEX.tsv").exists() else []
    key = next((k for k in (ni[0].keys() if ni else []) if k.lower() in ("id", "entry_id", "entry")), None)
    ids = {((r[key] if key else list(r.values())[0]) or "").strip() for r in ni}
    pe = {(r.get("entry_id") or "").strip() for r in places.get(t, [])}
    pk = {e.split("#")[0] for e in pe}
    wf = {e[5:] for e in pk if e.startswith("work:")}
    cx = {e[6:] for e in pk if e.startswith("codex:")}
    cfiles = sorted(p.name[:-len("_notes.md")] for p in (d / "codex").glob("*_notes.md")) if (d / "codex").exists() else []
    conly = cfiles  # the Codex "notes on the sheets"; never the same file as the Work math notes of that folder
    pfiles = sorted(p.name[:-len("_notes.md")] for p in (d / "pro").glob("*_notes.md")) if (d / "pro").exists() else []
    noidx = [p for p in pfiles if p not in {i.split("#")[0] for i in ids}]
    COV.append(dict(topic=t, agent=AGENT.get(t, "?"), index_rows=len(ids), index_unplaced=len(ids - pe),
                    pro_packages=len(pfiles), pro_not_in_index=" ".join(noidx),
                    pro_not_in_index_unplaced=" ".join(p for p in noidx if p not in pk),
                    work_folders=len(WK[t]), work_unplaced=" ".join(sorted(WK[t] - wf)),
                    codex_only_files=len(conly), codex_only_unplaced=" ".join(c for c in conly if c not in cx)))
write(G / "COVERAGE.tsv", COV, list(COV[0].keys()))
GAPS = {c["topic"]: c for c in COV if c["index_unplaced"] or c["work_unplaced"] or c["codex_only_unplaced"]
        or c["pro_not_in_index_unplaced"]}
ENT = re.compile(r"[A-Za-z0-9_:+.\-]+#\d+")
E = {it: set(ENT.findall(r.get("entries") or "")) for it, r in items.items()}
IDRE = re.compile(r"\bSA\d\d-\d+\b")
STOP = set("the of and a an in on for to by with from his her its as at is are be or not no over under via into "
           "de la le les des du et un une sur pour dans par en cote cotes scan scans notes note these pages page "
           "this that their what where which".split())


def toks(s):
    s = re.sub(r"[^a-z0-9à-ÿ₀-₉ ]+", " ", (s or "").lower())
    return {w for w in s.split() if w not in STOP and len(w) > 2}


T = {it: toks(r.get("object")) for it, r in items.items()}


class UF:
    def __init__(self, keys, strict):
        self.p = {k: k for k in keys}
        self.top = {k: {items[k]["topic"]} for k in keys}
        self.strict = strict
        self.log = []

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b, why):
        if a not in self.p or b not in self.p:
            return False
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.strict and self.top[ra] & self.top[rb]:
            self.log.append((a, b, "refused (a topic on both sides): " + why))
            return False
        self.p[ra] = rb
        self.top[rb] |= self.top[ra]
        self.log.append((a, b, why))
        return True


# pointers named in cross_topic: item ids, topic ids, cotes (cote 93, 148/030-033)
LINKS = []
for it, r in items.items():
    x = r.get("cross_topic") or ""
    for m in IDRE.findall(x):
        if m != it:
            LINKS.append((it, m.split("-")[0], m, "item id"))
    for m in re.findall(r"\bSA\d\d\b(?!-)", x):
        if m != r["topic"]:
            LINKS.append((it, m, "", "topic id"))
    for m in re.findall(r"\bcotes?\s+(\d+(?:-\d+)?)|\b(\d{2,3}(?:-\d+)?)/\d{2,3}\b", x):
        c = m[0] or m[1]
        t = COTE.get(c)
        if t and t != r["topic"]:
            LINKS.append((it, t, "", "cote " + c))
LINKS = sorted(set(LINKS))
# strict level
S = UF(items, True)
eq = []
for it, r in items.items():
    blob = " ".join(r.get(k) or "" for k in ("object", "statement", "cross_topic"))
    for m in re.findall(r"=\s*(SA\d\d-\d+)", blob) + re.findall(r"(SA\d\d-\d+)\s*\((?:same|identical)", blob):
        if m != it:
            eq.append((it, m))
# "= H???" names a tag of an earlier build: the same object as that tag's items; any other H??? mention is a link
P = G / "GLOBAL_OBJECTS.tsv"
old = {}
if P.exists():
    for r in read(P):
        for it in (r.get("items") or "").split():
            old[it] = r["tag"]
old_items = collections.defaultdict(list)
for it, tg in old.items():
    old_items[tg].append(it)
# a tag retired by a merge points to the tag its object kept (TAG_ALIASES.tsv), so citations of it still resolve
AL = G / "TAG_ALIASES.tsv"
alias_of = {r["retired"]: r["current"] for r in read(AL)} if AL.exists() else {}


def resolve(tg):
    seen = set()
    while tg in alias_of and tg not in seen:
        seen.add(tg)
        tg = alias_of[tg]
    return tg


tag_links = []
for it, r in items.items():
    blob = " ".join(r.get(k) or "" for k in ("object", "statement", "cross_topic"))
    for tg in re.findall(r"=\s*(H[0-9A-Z]{3})\b", blob):
        eq += [(it, b) for b in old_items.get(resolve(tg), []) if b != it]
    for tg in re.findall(r"(?<![=\w])\s*\b(H[0-9A-Z]{3})\b", r.get("cross_topic") or ""):
        tag_links += [(it, b) for b in old_items.get(resolve(tg), []) if b != it]
for a, b in eq:
    S.union(a, b, "stated equal (= or 'same') in " + a)
fam = collections.defaultdict(list)
for it, r in items.items():
    m = re.match(r"research-run family (\S+)", r.get("object") or "")
    if m:
        fam[m.group(1)].append(it)
for f, its in fam.items():
    for b in its[1:]:
        S.union(its[0], b, "the same research-run family " + f)
pairs = []
its = sorted(items)
for i, a in enumerate(its):
    for b in its[i + 1:]:
        if items[a]["topic"] == items[b]["topic"]:
            continue
        sh = len(E[a] & E[b])
        j = len(T[a] & T[b]) / len(T[a] | T[b]) if T[a] and T[b] else 0
        if sh:
            pairs.append(("entries", sh / min(len(E[a]), len(E[b])), sh, j, a, b))
        elif j >= 0.34:
            pairs.append(("name", j, len(T[a] & T[b]), j, a, b))
weak = []
for kind, score, n, j, a, b in sorted(pairs, key=lambda p: (p[0] != "entries", -p[1], -p[2])):
    if kind == "entries" and score >= 0.5:
        S.union(a, b, f"shared entries {n} (overlap {score:.2f})")
    elif kind == "name" and score >= 0.6 and n >= 3:
        S.union(a, b, f"name match {score:.2f}")
    else:
        weak.append((a, b, f"{kind} {score:.2f}" + (f" ({n} shared)" if kind == "entries" else "")))
# theme level
TH = UF(items, False)
for it in items:
    TH.union(it, S.find(it), "same object")
REPORTED = [["SA15-3", "SA18-8", "SA19-6", "SA14-2"], ["SA05-1", "SA18-15"], ["SA05-8", "SA06-2", "SA07-3", "SA18-12"],
            ["SA18-5", "SA19-3", "SA14-1"]]
for grp in REPORTED:
    for b in grp[1:]:
        TH.union(grp[0], b, "reported crossing by a28ea31fa17dd65e1")
for a, t, b, how in LINKS:
    if b:
        TH.union(a, b, "cross_topic of " + a)
for a, b in tag_links:
    TH.union(a, b, "tag named in cross_topic of " + a)
for a, b, why in weak:
    if why.startswith("entries") or (items[b]["topic"] in (items[a].get("cross_topic") or "")
                                     or items[a]["topic"] in (items[b].get("cross_topic") or "")):
        TH.union(a, b, "weak " + why)
# tags, stable across reruns (old, read above); the hand-kept CONCEPTS.tsv tags are reserved
B36 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def b36(n):
    s = ""
    for _ in range(3):
        s, n = B36[n % 36] + s, n // 36
    return "H" + s


groups = collections.defaultdict(list)
for it in items:
    groups[S.find(it)].append(it)
tgroups = collections.defaultdict(set)
for it in items:
    tgroups[TH.find(it)].add(it)
theme_id, k = {}, 0
for root, g in sorted(tgroups.items(), key=lambda kv: (-len({items[i]["topic"] for i in kv[1]}), -len(kv[1]), min(kv[1]))):
    if len({items[i]["topic"] for i in g}) > 1:
        k += 1
        theme_id[root] = f"TH-{k:02d}"
used, nxt, out, tag_of = set(old.values()), 1, [], {}
if (G / "CONCEPTS.tsv").exists():
    used |= {r["tag"] for r in read(G / "CONCEPTS.tsv")}
used |= set(alias_of)
assigned, new_alias = set(), []
for g in sorted(groups.values(), key=lambda g: (-len({items[i]["topic"] for i in g}), min(g))):
    prev = sorted({resolve(old[i]) for i in g if i in old} - assigned)
    if prev:
        tag = prev[0]  # the earliest tag stays; the others become its aliases
        for o in prev[1:]:
            alias_of[o] = tag
            new_alias.append((o, tag))
    else:
        while b36(nxt) in used:
            nxt += 1
        tag = b36(nxt)
        used.add(tag)
    assigned.add(tag)
    rs = [items[i] for i in sorted(g)]
    topics = sorted({r["topic"] for r in rs})
    linked = sorted({t for (a, t, b, how) in LINKS if a in g} - set(topics))
    for i in g:
        tag_of[i] = tag
    obj = max((r.get("object") or "" for r in rs), key=lambda s: (len(toks(s)), -len(s)))
    ents = set().union(*(E[i] for i in g))
    out.append(dict(
        tag=tag, object=obj[:220], kind="; ".join(sorted({(r.get("kind") or "").strip()[:40] for r in rs})),
        items=" ".join(sorted(g)), topics=" ".join(topics), n_topics=len(topics),
        theme=theme_id.get(TH.find(g[0]), ""), linked_topics=" ".join(linked),
        deep_agents=" ".join(sorted({AGENT.get(t, "?") for t in topics})), n_entries=len(ents),
        cotes_scans="; ".join(sorted({(r.get("cotes_scans") or "").strip()[:80] for r in rs}))[:300],
        status_on_pages="; ".join(sorted({(r.get("status_on_pages") or "not checked").strip()[:70] for r in rs}))[:300],
        flags="; ".join(sorted({(r.get("flags") or "").strip()[:90] for r in rs if (r.get("flags") or "").strip()}))[:300],
        merged_by="; ".join(sorted({w for (a, b, w) in S.log if a in g and b in g and not w.startswith("refused")}))[:300]
        or "single item"))
out.sort(key=lambda r: (-r["n_topics"], r["theme"] == "", r["theme"], r["tag"]))
assert len({o["tag"] for o in out}) == len(out), "a tag is given twice"
write(AL, [dict(retired=k, current=resolve(v)) for k, v in sorted(alias_of.items())], ["retired", "current"])
F = ["tag", "object", "kind", "items", "topics", "n_topics", "theme", "linked_topics", "deep_agents", "n_entries",
     "cotes_scans", "status_on_pages", "flags", "merged_by"]
write(P, out, F)
themes = []
for root, tid in theme_id.items():
    g = tgroups[root]
    tags = sorted({tag_of[i] for i in g})
    big = max(g, key=lambda i: (len(E[i]), i))
    themes.append(dict(theme=tid, name_from_largest_item=(items[big].get("object") or "")[:160], tags=" ".join(tags),
                       n_objects=len(tags), items=" ".join(sorted(g)),
                       topics=" ".join(sorted({items[i]["topic"] for i in g})),
                       deep_agents=" ".join(sorted({AGENT[items[i]["topic"]] for i in g})),
                       linked_by="; ".join(sorted({w for (a, b, w) in TH.log if a in g and w != "same object"}))[:300]))
themes.sort(key=lambda r: r["theme"])
write(G / "THEMES.tsv", themes, list(themes[0].keys()))
write(G / "LINKS.tsv", [dict(item=a, item_topic=items[a]["topic"], to_topic=t, to_item=b, found_as=how,
                             to_topic_done="yes" if t in done_topics else "no output yet",
                             tag=tag_of[a], to_tag=tag_of.get(b, "")) for a, t, b, how in LINKS],
      ["item", "item_topic", "to_topic", "to_item", "found_as", "to_topic_done", "tag", "to_tag"])
write(G / "merge_log.tsv", [dict(level="strict", a=a, b=b, why=w) for a, b, w in S.log] +
      [dict(level="theme", a=a, b=b, why=w) for a, b, w in TH.log if w != "same object"], ["level", "a", "b", "why"])
cote_topics, pkg_topics = collections.defaultdict(set), collections.defaultdict(set)
for t, rs in places.items():
    for r in rs:
        c = (r.get("cote") or "").strip()
        if c:
            cote_topics[c].add(t)
        e = (r.get("entry_id") or "").split("#")[0]
        if e:
            pkg_topics[e].add(t)
shared = {"cotes": {c: sorted(ts) for c, ts in sorted(cote_topics.items()) if len(ts) > 1},
          "packages": {p: sorted(ts) for p, ts in sorted(pkg_topics.items()) if len(ts) > 1}}
(G / "shared_cotes_packages.json").write_text(json.dumps(shared, ensure_ascii=False, indent=1), encoding="utf-8")
# inboxes: what other agents' items say about each agent's topics (between AUTO markers; text outside is kept)
now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
for ag, ts in AGENTS.items():
    if ag == "a0c4bb37":
        continue
    mine = set(ts.split())
    L = [f"<!-- AUTO from _broad_tools/build_global.py, {now} -->",
         f"## Cross-topic entries for {ag} (topics {ts}), built {now}", "",
         "Tags: GLOBAL\\GLOBAL_OBJECTS.tsv gives every item a tag H??? (same object across topics) and a theme TH-nn "
         "(related objects). Name the tag in cross_topic (\"= H00x\") when an item of yours is that object.", ""]
    shared_obj = [o for o in out if set(o["topics"].split()) & mine and len({AGENT[t] for t in o["topics"].split()}) > 1]
    L.append(f"### Same object in your topics and another agent's ({len(shared_obj)})")
    for o in shared_obj:
        L.append(f"- {o['tag']}: {o['object'][:120]} | items {o['items']} | merged by: {o['merged_by'][:100]}")
    L.append("")
    inc = [(a, t, b, how) for (a, t, b, how) in LINKS if t in mine and AGENT[items[a]["topic"]] != ag]
    L.append(f"### Other agents' items that point to your topics ({len(inc)})")
    for a, t, b, how in inc:
        r = items[a]
        L.append(f"- {a} ({r['topic']}, {tag_of[a]}) -> {t}{' ' + b if b else ''} [{how}]: {(r.get('object') or '')[:110]}"
                 f" | its cross_topic: {(r.get('cross_topic') or '')[:140]}")
    g_ = [GAPS[t] for t in sorted(mine) if t in GAPS]
    L += ["", f"### Notes of your topics without a PLACEMENT row ({len(g_)} topics; see GLOBAL\\COVERAGE.tsv)"]
    for c in g_:
        L.append(f"- {c['topic']}: NOTES_INDEX rows unplaced {c['index_unplaced']}; Pro packages missing from "
                 f"NOTES_INDEX and unplaced: {c['pro_not_in_index_unplaced'] or 'none'}; Work folders unplaced: "
                 f"{c['work_unplaced'] or 'none'}; Codex/API folder notes on the sheets (inputs\\{c['topic']}\\codex"
                 f"\\<folder>_notes.md, not the Work math notes) unplaced: {c['codex_only_unplaced'] or 'none'}")
    L += ["", "<!-- /AUTO -->"]
    p = IN / f"{ag}.md"
    keep = ""
    if p.exists():
        txt = p.read_text(encoding="utf-8")
        keep = re.sub(r"<!-- AUTO.*?<!-- /AUTO -->\n?", "", txt, flags=re.S)
    p.write_text((keep.rstrip() + "\n\n" if keep.strip() else "") + "\n".join(L) + "\n", encoding="utf-8")
multi = [o for o in out if o["n_topics"] > 1]
# the generated part of CROSS_TOPIC.md (between AUTO markers; the hand-written text outside them is kept)
cnt = collections.Counter()
basis, fid, fk, ce_by = collections.Counter(), collections.Counter(), collections.Counter(), {}
for d in sorted(S1.glob("SA[0-9][0-9]")):
    P_ = places.get(d.name, [])
    cnt["rows"] += len(P_)
    cnt["work"] += sum(1 for r in P_ if (r.get("entry_id") or "").startswith("work:"))
    for r in P_:
        b = (r.get("basis") or "").strip()
        basis[b] += 1
        if b == "passage-read":
            fid[(r.get("fidelity") or "").strip()] += 1
    if (d / "FLAGS.tsv").exists():
        for r in read(d / "FLAGS.tsv"):
            fk[re.sub(r"derivateurs", "dérivateurs", (r.get("kind") or "").strip().lower())] += 1
    if (d / "CHECK_EVENTS.tsv").exists():
        C_ = read(d / "CHECK_EVENTS.tsv")
        ce_by[d.name] = (len(C_), sum(1 for r in C_ if "second pass" in (r.get("how") or "")))
A = [f"<!-- AUTO from _broad_tools/build_global.py, {now} -->", f"## The numbers, {now}", "",
     f"- Topics with OBJECTS.tsv: {len(done_topics)} of 32; without: {' '.join(missing) or 'none'}"
     f" (with a PLACEMENT.tsv but no OBJECTS.tsv yet: {' '.join(t for t in missing if t in places) or 'none'}).",
     f"- Placement rows: {cnt['rows']} (Work and Codex-web units: {cnt['work']}). Basis: "
     + ", ".join(f"{k} {v}" for k, v in basis.most_common()) + ". Fidelity of the passage-read rows: "
     + ", ".join(f"{k} {v}" for k, v in fid.most_common()) + ".",
     f"- Items: {len(items)}; global objects: {len(out)}, of which {len(multi)} in more than one topic; themes: {len(themes)}.",
     f"- Pointers in cross_topic: {len(LINKS)}, of which {sum(1 for l in LINKS if l[1] in missing)} into topics without OBJECTS.tsv.",
     "- Flags: " + ", ".join(f"{k} {v}" for k, v in fk.most_common()) + ".",
     "- Check events (all / imported from the second pass): " + ", ".join(f"{t} {a}/{b}" for t, (a, b) in ce_by.items() if a) + ".",
     "", "### Objects in more than one topic", "", "| tag | theme | topics | object | merged by |", "|---|---|---|---|---|"]
for o in multi:
    A.append(f"| {o['tag']} | {o['theme']} | {o['topics']} | {o['object'][:110]} | {o['merged_by'][:70]} |")
A += ["", "### Themes (related objects across topics)", "", "| theme | objects | topics | largest item |", "|---|---:|---|---|"]
for t in themes:
    A.append(f"| {t['theme']} | {t['n_objects']} | {t['topics']} | {t['name_from_largest_item'][:100]} |")
A += ["", "### Packages placed in more than one topic", ""]
A += [f"- {p}: {' '.join(ts)}" for p, ts in shared["packages"].items()]
A += ["", "### Pointers into topics without OBJECTS.tsv", ""]
A += [f"- {a} ({items[a]['topic']}, {tag_of[a]}) -> {t} [{how}]: {(items[a].get('object') or '')[:100]}"
      for a, t, b, how in LINKS if t in missing]
A += ["", "### Notes without a PLACEMENT row (GLOBAL\\COVERAGE.tsv)", ""]
A += [f"- {c['topic']} ({c['agent']}): NOTES_INDEX rows {c['index_unplaced']}; Pro packages missing from NOTES_INDEX "
      f"and unplaced: {c['pro_not_in_index_unplaced'] or 'none'}; Work folders: {c['work_unplaced'] or 'none'}; "
      f"Codex/API folder notes: {c['codex_only_unplaced'] or 'none'}" for c in GAPS.values()] or ["- none"]
A += ["", "<!-- /AUTO -->"]
cp = G / "CROSS_TOPIC.md"
keep = re.sub(r"<!-- AUTO.*?<!-- /AUTO -->\n?", "", cp.read_text(encoding="utf-8"), flags=re.S) if cp.exists() else ""
cp.write_text((keep.rstrip() + "\n\n" if keep.strip() else "") + "\n".join(A) + "\n", encoding="utf-8")
print(now, "| topics", len(done_topics), "missing", " ".join(missing), "| items", len(items), "| objects", len(out),
      "multi-topic", len(multi), "| themes", len(themes), "| links", len(LINKS),
      "to unfinished", sum(1 for l in LINKS if l[1] in missing), "| refused strict", sum(1 for l in S.log if l[2].startswith("refused")))
print("shared cotes", len(shared["cotes"]), "shared packages", len(shared["packages"]))
for o in multi:
    print(o["tag"], o["theme"] or "-", o["topics"], "|", o["object"][:70], "|", o["merged_by"][:50])
for t in themes:
    print(t["theme"], t["n_objects"], t["topics"], "|", t["name_from_largest_item"][:70])
