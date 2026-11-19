"""Horizontal sweep 2, part 1: refresh the inputs (broad agent a0c4bb37, Claude Opus 5.5 at effort max, 18 Nov 2026).
Splits every notes file of the archive into entries under ONE id rule (sweep2/GLOBAL/ID_RULE.md), compares them with the
sweep-1 placements, and writes:
  sweep2/inputs/UNITS.tsv              every entry, placed or not, with its class, topic, file and line
  sweep2/inputs/GAP_INDEX.tsv          the entries sweep 1 did not place (duplicate texts folded into one entry)
  sweep2/inputs/SA<nn>/GAP_INDEX.tsv   the same, per topic
  sweep2/GLOBAL/ID_ALIASES.tsv         label ids (#R001, #3:N046) and exact duplicates -> the canonical id
  sweep2/GLOBAL/STALE_PLACEMENTS.tsv   sweep-1 placements whose entry no longer exists, with the current entry
  sweep2/GLOBAL/LINKED_ROWS.tsv        second chats (chatB) and folder variants (_2, CTRL-*) -> the entry they witness
Reads only; writes only under sweep2. usage: python -I -B refresh_inputs.py"""
import csv, re, sys, json, hashlib, collections, pathlib, difflib

sys.stdout.reconfigure(encoding="utf-8")
csv.field_size_limit(10 ** 9)
D = pathlib.Path(r"C:\Users\user\Documents")
H = D / "results_register" / "horizontal"
S1, S2 = H / "sweep1", H / "sweep2"
T = D / "grothendieck_archive_transcription_20261110"
PRO, CW = T / "returns", T / "codex_web_20261113"
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
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: re.sub(r"\s+", " ", str(r.get(k, ""))) for k in fields})


# cote -> topic (the topic tables of the sweep-1 inputs)
COTE = {}
for tp in sorted(H.glob("inputs/SA[0-9][0-9]/TOPIC.md")):
    for line in tp.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*(\d+(?:-\d+)?)\s*\|", line)
        if m:
            COTE.setdefault(m.group(1), tp.parent.name)


def topic_of_cote(c):
    return COTE.get(c) or COTE.get(c.split("-")[0]) or ""


# where sweep 1 put each package and folder
PKG_TOPICS = collections.defaultdict(set)
for ni in H.glob("inputs/SA[0-9][0-9]/NOTES_INDEX.tsv"):
    for r in read(ni):
        PKG_TOPICS[r["package"]].add(ni.parent.name)
for p in H.glob("inputs/SA[0-9][0-9]/pro/*_notes.md"):
    PKG_TOPICS[p.name[:-len("_notes.md")]].add(p.parent.parent.name)
FOLDER_TOPIC = {}
for r in read(H / "inputs" / "WORK_MATHNOTES_BY_TOPIC.tsv"):
    FOLDER_TOPIC[r["folder"]] = r["topic"]
for p in H.glob("inputs/SA[0-9][0-9]/codex/*_notes.md"):
    FOLDER_TOPIC.setdefault(p.name[:-len("_notes.md")], p.parent.parent.name)
ASSIGN = {r["folder"]: r["cote"] for r in read(CW / "ASSIGNMENTS.tsv")}


def pkg_cotes(pkg):
    return [part.split("_")[0] for part in pkg[4:].split("+")]


def topic_of_pkg(pkg):
    ts = PKG_TOPICS.get(pkg, set())
    first = topic_of_cote(pkg_cotes(pkg)[0])
    return first if first in ts or not ts else sorted(ts)[0]


def folder_cote(f):
    base = re.sub(r"_\d+$", "", f)
    if base in ASSIGN:
        return ASSIGN[base]
    m = re.match(r"^[A-Z]+(\d+(?:-\d+)?)-\d+$", base)
    return m.group(1) if m else ""


def topic_of_folder(f):
    base = re.sub(r"_\d+$", "", f)
    return FOLDER_TOPIC.get(f) or FOLDER_TOPIC.get(base) or topic_of_cote(folder_cote(f))


HEAD = re.compile(r"^(#{1,4})\s+(.*)$")


def units(path, deepest):
    """Entries of a markdown file: sections at the entry level. Pro notes: the deepest of ###, ##, # occurring at
    least twice (stage A's ###). Work and Codex notes: the shallowest level occurring at least twice."""
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return []
    lev = collections.Counter()
    fence = False
    for ln in lines:
        if ln.strip().startswith("```"):
            fence = not fence
        m = None if fence else HEAD.match(ln)
        if m:
            lev[len(m.group(1))] += 1
    cand = [L for L in (1, 2, 3) if lev[L] >= 2]
    if not cand:
        return [(1, "", "\n".join(lines))] if "".join(lines).strip() else []
    L = max(cand) if deepest else min(cand)
    out, cur, start, head = [], [], None, None
    fence = False
    for i, ln in enumerate(lines, 1):
        if ln.strip().startswith("```"):
            fence = not fence
        m = None if fence else HEAD.match(ln)
        if m and len(m.group(1)) == L:
            if head is not None:
                out.append((start, head, "\n".join(cur)))
            start, head, cur = i, m.group(2).strip(), [ln]
        elif head is not None:
            if m and len(m.group(1)) < L:  # a higher heading closes the entry
                out.append((start, head, "\n".join(cur)))
                head, cur = None, []
            else:
                cur.append(ln)
    if head is not None:
        out.append((start, head, "\n".join(cur)))
    return out


SCAN = re.compile(r"\b(\d{1,3}(?:-\d)?)/(\d{2,3})\b|\b[Ss]cans?\s+(\d{1,3})")


def scans_of(text):
    s = []
    for a, b, c in SCAN.findall(text[:600]):
        s.append(f"{a}/{b}" if a else c)
    return ",".join(dict.fromkeys(s))[:120]


def label_of(head):
    m = re.match(r"^\**\s*([A-Z]{1,3}\d{2,4}(?:\.\d+)?)\b", head)
    return m.group(1) if m else ""


U = []


FULL = re.compile(r"[Ss]cans?\s+(\d{2,3})(?:\s*[–-]\s*(\d{2,3}))?|^\|\s*(\d{2,3})\s*\|", re.M)


def scans_full(text, cote):
    """every scan a doubts entry names (scan N, scans N-M, a table row starting with N), as cote/scan"""
    out = []
    for a, b, c in FULL.findall(text):
        for x in (a, b, c):
            if x:
                out.append(f"{cote}/{int(x):03d}")
    return ",".join(dict.fromkeys(out))[:3000]


def add(entry_src, cls, topic, path, deepest, linked_to="", note="", cote=""):
    for n, (line, head, text) in enumerate(units(path, deepest), 1):
        norm = re.sub(r"\s+", " ", text).strip()
        U.append(dict(entry_id=f"{entry_src}#{n}", cls=cls, topic=topic, agent=AGENT.get(topic, "?"),
                      source_file=str(path.relative_to(D)).replace("\\", "/"), line=line, heading=head[:160],
                      label=label_of(head), words=len(text.split()),
                      scans=scans_full(text, cote) if (entry_src.endswith(":doubts") and cote) else scans_of(head + " " + text),
                      sha=hashlib.sha256(norm.encode("utf-8")).hexdigest()[:16],
                      linked_to=linked_to and f"{linked_to}#{n}", note=note))


# Pro packages: per (package, chatB) the final, else the newest checkpoint (as stage A and the dataset do)
vers = collections.defaultdict(list)
for d in PRO.iterdir():
    m = re.match(r"^(MPL_.+?)(?:_checkpoint_(\d+))?(_chatB)?_unzipped$", d.name)
    if m and d.is_dir():
        vers[(m.group(1), bool(m.group(3)))].append((0 if m.group(2) is None else 1, -int(m.group(2) or 0), d))
for (pkg, chatb), vs in sorted(vers.items()):
    final = sorted(vs)[0]
    d, kind = final[2], ("final" if final[0] == 0 else f"checkpoint {-final[1]}")
    src = pkg + ("_chatB" if chatb else "")
    top = topic_of_pkg(pkg)
    files = [p for p in d.rglob("*.md") if len(p.relative_to(d).parts) <= 2 and "_from_earlier_checkpoints" not in p.parts]
    for p in sorted(files):
        nm = p.name
        if nm == f"{pkg}_notes.md":
            cls = "pro_chatB" if chatb else ("pro_notes" if kind == "final" else "pro_checkpoint_only")
            add(src, cls, top, p, True, linked_to=pkg if chatb else "", note=kind)
        elif nm == f"{pkg}_doubts.md":
            add(src + ":doubts", "pro_chatB" if chatb else "pro_doubts", top, p, True,
                linked_to=(pkg + ":doubts") if chatb else "", note=kind, cote=pkg_cotes(pkg)[0])
        elif nm.endswith("_pointers.md") or nm.startswith("research_leads"):
            add(f"{src}:records:{p.stem}", "pro_records", top, p, True, note=kind)
# Work and Codex-web folders: returns/<folder>/out and returns_control/<folder>/out
for root, ctrl in ((CW / "returns", False), (CW / "returns_control", True)):
    if not root.exists():
        continue
    for d in sorted(root.iterdir()):
        out = d / "out"
        if not out.is_dir():
            continue
        f = d.name
        base = re.sub(r"_\d+$", "", f)
        variant = (f != base) or ctrl
        mc = re.match(r"^CTRL-?(\d+(?:-\d+)?)", f)
        top = topic_of_cote(mc.group(1)) if (ctrl and mc) else topic_of_folder(f)
        for suffix, pre, cls in (("_mathnotes.md", "work:", "work_mathnotes"), ("_notes.md", "codex:", "codex_sheet_notes"),
                                 ("_doubts.md", "codex:", "codex_doubts")):
            p = out / f"{f}{suffix}"
            if not p.exists():  # a variant folder keeps the base name inside (returns/K43-02_2/out/K43-02_mathnotes.md)
                p = out / f"{base}{suffix}"
            if p.exists():
                src = pre + f + (":doubts" if cls == "codex_doubts" else "")
                lk = ""
                if variant and not ctrl:
                    lk = pre + base + (":doubts" if cls == "codex_doubts" else "")
                add(src, "variant" if variant else cls, top, p, False, linked_to=lk, note=("control" if ctrl else cls),
                    cote=(mc.group(1) if (ctrl and mc) else folder_cote(f)))
# sweep-1 placements
placed = collections.defaultdict(set)
for pf in S1.glob("SA[0-9][0-9]/PLACEMENT.tsv"):
    for r in read(pf):
        e = (r.get("entry_id") or "").strip()
        if e:
            placed[e].add(pf.parent.name)
ids = {u["entry_id"]: u for u in U}
# aliases: label forms (#R001, #N141.1) and sub-entries (#3:N046) of the same source
alias = {}
by_label = {}
for u in U:
    if u["label"]:
        by_label[(u["entry_id"].split("#")[0], u["label"])] = u["entry_id"]
for e in placed:
    if e in ids or "#" not in e:
        continue
    src, rest = e.split("#", 1)
    m = re.match(r"^(\d+):(.+)$", rest)
    if m and f"{src}#{m.group(1)}" in ids:
        alias[e] = (f"{src}#{m.group(1)}", "sub-entry of")
    elif (src, rest) in by_label:
        alias[e] = (by_label[(src, rest)], "label of")
# a variant folder placed in sweep 1 (K34-02_2, K154-01_3, ...) that is now filed under its base name: same unit n
for e in placed:
    if e in ids or e in alias or "#" not in e:
        continue
    src, n = e.split("#", 1)
    m = re.match(r"^((?:work|codex):[^:#]+?)_\d+(:doubts)?$", src)
    if m and f"{m.group(1)}{m.group(2) or ''}#{n}" in ids:
        alias[e] = (f"{m.group(1)}{m.group(2) or ''}#{n}", "variant folder now filed under its base name")
# exact duplicate texts across different files: one entry, the others aliases (a placed id is preferred as canonical)
by_sha = collections.defaultdict(list)
for u in U:
    if u["words"] >= 20:
        by_sha[u["sha"]].append(u)
dup_of = {}
for sha, us in by_sha.items():
    if len({u["source_file"] for u in us}) > 1:
        us = sorted(us, key=lambda u: (u["entry_id"] not in placed, u["cls"] == "variant", u["entry_id"]))
        for u in us[1:]:
            dup_of[u["entry_id"]] = us[0]["entry_id"]
for a, c in dup_of.items():
    alias[a] = (c, "exact duplicate of")
placed_res = set(placed) | {alias[e][0] for e in placed if e in alias}
# stale placements: placed ids that resolve to no current entry
stale = []
for e, tps in sorted(placed.items()):
    if e in ids or e in alias:
        continue
    src = e.split("#")[0]
    cands = [u for u in U if u["entry_id"].split("#")[0] == src]
    if not cands and src.startswith(("work:", "codex:")):  # placed under the other prefix of the same folder
        other = ("codex:" if src.startswith("work:") else "work:") + src.split(":", 1)[1]
        cands = [u for u in U if u["entry_id"].split("#")[0] == other]
    row = next((r for r in read(S1 / sorted(tps)[0] / "PLACEMENT.tsv") if r["entry_id"] == e), {})
    obj = (row.get("object") or "") + " " + (row.get("his_term") or "")
    best = max(cands, key=lambda u: difflib.SequenceMatcher(None, obj.lower(), u["heading"].lower()).ratio(), default=None)
    stale.append(dict(entry_id=e, topics=" ".join(sorted(tps)), object=obj.strip()[:120],
                      current_entries=len(cands), proposed=(best or {}).get("entry_id", ""),
                      proposed_heading=(best or {}).get("heading", "")[:120],
                      why="the file has fewer units now" if cands else "the source file is gone or renamed"))
for u in U:
    u["placed_sweep1"] = ("yes" if u["entry_id"] in placed else "via alias" if u["entry_id"] in placed_res else
                          "duplicate of " + dup_of[u["entry_id"]] if u["entry_id"] in dup_of else "no")
F = ["entry_id", "cls", "topic", "agent", "source_file", "line", "heading", "label", "words", "scans", "sha",
     "linked_to", "note", "placed_sweep1"]
write(S2 / "inputs" / "UNITS.tsv", U, F)
DOUBT = ("pro_doubts", "codex_doubts")
is_doubt = lambda u: u["cls"] in DOUBT or u["entry_id"].split("#")[0].endswith(":doubts")
write(S2 / "inputs" / "DOUBTS_INDEX.tsv", [u for u in U if is_doubt(u)], F)
gaps = [u for u in U if u["placed_sweep1"] == "no" and not is_doubt(u)]
write(S2 / "inputs" / "GAP_INDEX.tsv", gaps, F)
for t in sorted({u["topic"] for u in gaps}):
    write(S2 / "inputs" / (t or "NO_TOPIC") / "GAP_INDEX.tsv", [u for u in gaps if u["topic"] == t], F)
write(S2 / "GLOBAL" / "ID_ALIASES.tsv", [dict(alias=a, canonical=c, relation=w) for a, (c, w) in sorted(alias.items())],
      ["alias", "canonical", "relation"])
write(S2 / "GLOBAL" / "STALE_PLACEMENTS.tsv", stale, list(stale[0].keys()) if stale else ["entry_id"])
write(S2 / "GLOBAL" / "LINKED_ROWS.tsv", [dict(entry_id=u["entry_id"], cls=u["cls"], note=u["note"], witnesses=u["linked_to"],
                                               witness_exists="yes" if u["linked_to"] in ids else "no",
                                               same_text="yes" if u["linked_to"] in ids and ids[u["linked_to"]]["sha"] == u["sha"] else "no",
                                               topic=u["topic"], placed_sweep1=u["placed_sweep1"])
                                          for u in U if u["cls"] in ("variant", "pro_chatB") or u["note"] == "control"],
      ["entry_id", "cls", "note", "witnesses", "witness_exists", "same_text", "topic", "placed_sweep1"])
# summary
c = collections.Counter((u["cls"], u["placed_sweep1"] == "no") for u in U)
w = collections.Counter()
for u in gaps:
    w[u["cls"]] += u["words"]
print("units", len(U), "| placed ids in sweep 1", len(placed), "resolved", len(placed_res & set(ids)), "| aliases", len(alias),
      "(dups", len(dup_of), ") | stale", len(stale))
for cls in sorted({u["cls"] for u in U}):
    print(f"  {cls}: units {c[(cls, False)] + c[(cls, True)]}, gaps {c[(cls, True)]}, gap words {w[cls]}")
ga = collections.Counter(u["agent"] for u in gaps)
gw = collections.Counter()
for u in gaps:
    gw[u["agent"]] += u["words"]
print("gaps by agent:", {a: (ga[a], gw[a]) for a in ga}, "| no topic:", sum(1 for u in gaps if not u["topic"]))
