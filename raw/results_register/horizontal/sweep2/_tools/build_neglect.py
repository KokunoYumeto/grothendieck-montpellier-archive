"""The neglect table for sweep 3's order (broad agent a0c4bb37, Claude Opus 5.5 at effort max, 18 Nov 2026).
Per topic: transcribed pages (distinct cote/scan pairs carrying a \\scanpage in the topic's transcriptions), items, claims of
his, flags, research-register statements on the topic's pages (by status and run; misplaced places left out), companion
units on its pages. Ranked from least to most researched by statements per 100 transcribed pages.
Writes sweep2/GLOBAL/NEGLECT.tsv and NEGLECT.md. usage: python -I -B build_neglect.py"""
import csv, re, sys, collections, pathlib, datetime

sys.stdout.reconfigure(encoding="utf-8")
csv.field_size_limit(10 ** 9)
D = pathlib.Path(r"C:\Users\user\Documents")
H = D / "results_register" / "horizontal"
S2 = H / "sweep2"
G = S2 / "GLOBAL"


def read(p):
    with open(p, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


UN = read(S2 / "inputs" / "UNITS.tsv")
OWN = read(G / "OWNER_OVERRIDES.tsv")
TITLE = {tp.parent.name: re.sub(r"^#\s*SA\d\d:\s*", "", tp.read_text(encoding="utf-8").splitlines()[0]).strip()
         for tp in H.glob("inputs/SA[0-9][0-9]/TOPIC.md")}


def topic(u):
    src = u["entry_id"].split("#")[0]
    src = src.split(":")[1] if src.startswith(("work:", "codex:")) else src
    for o in OWN:
        if re.match(re.escape(o["source_prefix"]) + r"(?:[_#:]|$)", src):
            return o["topic"]
    return u["topic"]


def first_cote(src):
    m = re.match(r"^MPL_(\d+(?:-\d+)?)", src) or re.match(r"^(?:work:|codex:)?[A-Z]+(\d+(?:-\d+)?)-\d+", src) \
        or re.match(r"^(?:work:|codex:)?CTRL-?(\d+)", src)
    return m.group(1) if m else "?"


# transcribed pages: the transcription next to each notes file
pages = collections.defaultdict(set)
seen_tex = set()
for u in UN:
    nf = D / u["source_file"]
    src = u["entry_id"].split("#")[0].split(":records")[0].replace(":doubts", "")
    tex = None
    for cand in (nf.parent / (nf.name.replace("_mathnotes.md", "_transcription.tex").replace("_notes.md", "_transcription.tex")
                              .replace("_doubts.md", "_transcription.tex")),):
        if cand.exists():
            tex = cand
    if tex is None:
        tx = sorted(nf.parent.glob("*_transcription.tex"))
        tex = tx[0] if tx else None
    if tex is None or (tex, topic(u)) in seen_tex:
        continue
    seen_tex.add((tex, topic(u)))
    c = first_cote(re.sub(r"^(work|codex):", "", src))
    for m in re.finditer(r"\\scanpage\{(\d+)\}", tex.read_text(encoding="utf-8", errors="replace")):
        pages[topic(u)].add((c, int(m.group(1))))
items, claims, flags = collections.Counter(), collections.Counter(), collections.Counter()
CLAIM = re.compile(r"his claim|claim|conjectur|stated without|asserted|announced", re.I)
for d in sorted(S2.glob("SA[0-9][0-9]")):
    for r in read(d / "OBJECTS.tsv"):
        items[d.name] += 1
        if CLAIM.search((r.get("kind") or "") + " " + (r.get("status_on_pages") or "")):
            claims[d.name] += 1
    flags[d.name] = len(read(d / "FLAGS.tsv")) if (d / "FLAGS.tsv").exists() else 0
IR = read(G / "INTERLINKS" / "ITEM_REGISTER.tsv")
st = collections.defaultdict(dict)
runs = collections.defaultdict(collections.Counter)
items_linked = collections.defaultdict(set)
for r in IR:
    st[r["topic"]][r["statement"]] = r["status"]
    items_linked[r["topic"]].add(r["item"])
for t, d in st.items():
    for tag in d:
        runs[t][tag.split(":")[0]] += 1
# statements placed on a topic's cotes without an item on those exact scans, and Les Dérivateurs places (given in the
# manuscript's pages, with no scan concordance yet) at topic level
COTE = {}
for tp in sorted(H.glob("inputs/SA[0-9][0-9]/TOPIC.md")):
    for line in tp.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*(\d+(?:-\d+)?)\s*\|", line)
        if m:
            COTE.setdefault(m.group(1), tp.parent.name)
MIS = [r["tag_prefix"] for r in read(G / "MISPLACED_REGISTER_PLACES.tsv")] if (G / "MISPLACED_REGISTER_PLACES.tsv").exists() else []
REGST = {r["tag"]: r["status"] for r in read(D / "results_register" / "REGISTER.tsv")}
topic_level = collections.defaultdict(set)
lm_only = set()
for r in read(D / "results_register" / "sweep2_global" / "HIS_PLACES.tsv"):
    if any(r["tag"].startswith(m) for m in MIS):
        continue
    t = None
    if r["work"] == "Montpellier archive":
        t = COTE.get(r["cote"]) or COTE.get(r["cote"].split("-")[0])
    elif r["work"] == "Les Dérivateurs":
        t = "SA32"
    elif r["work"] == "La Longue Marche":
        lm_only.add(r["tag"])
    if t:
        topic_level[t].add(r["tag"])
        if r["tag"] not in st[t]:
            st[t][r["tag"]] = REGST.get(r["tag"], "")
runs = collections.defaultdict(collections.Counter)
IU = read(G / "INTERLINKS" / "ITEM_UNITS.tsv")
units = collections.defaultdict(set)
for r in IU:
    units[r["topic"]].add(r["unit"])
rows = []
for t in sorted(TITLE):
    sc = collections.Counter(st[t].values())
    n_st = len(st[t])
    n_pg = len(pages[t])
    rows.append(dict(topic=t, title=TITLE[t][:70], transcribed_pages=n_pg, items=items[t], claims_of_his=claims[t], flags=flags[t],
                     statements=n_st, proved=sc.get("Proved", 0), refuted=sc.get("Refuted", 0), known=sc.get("Known", 0),
                     open=sc.get("Open", 0), items_with_statements=len(items_linked[t]),
                     statements_per_100_pages=round(100 * n_st / n_pg, 1) if n_pg else 0.0,
                     runs="; ".join(f"{k} {v}" for k, v in runs[t].most_common(4)), companion_units=len(units[t])))
rows.sort(key=lambda r: (r["statements_per_100_pages"], r["statements"], -r["transcribed_pages"]))
for i, r in enumerate(rows, 1):
    r["rank"] = i
F = ["rank", "topic", "title", "transcribed_pages", "items", "claims_of_his", "flags", "statements", "proved", "refuted", "known",
     "open", "items_with_statements", "statements_per_100_pages", "runs", "companion_units"]
with open(G / "NEGLECT.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=F, delimiter="\t", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
L = ["# Neglect table: which areas the research has not reached (sets sweep 3's order)", "",
     f"Built {now} by `sweep2/_tools/build_neglect.py`, written by the broad agent a0c4bb37 (Claude Opus 5.5 at effort max). Rerun it after any change.",
     "",
     "The user, 18 Nov 22:3x UTC: sweep 3 goes deep, with \"all compute towards the ones that we've been neglecting\", so that each area gets its own foundation instead of everything resting on La Longue Marche and Les Dérivateurs.", "",
     "**The measures:**",
     "- **Transcribed pages:** distinct cote and scan pairs with a `\\scanpage` in the topic's transcriptions.",
     "- **Items, claims of his, flags:** from the sweep-2 tables.",
     "- **Statements:** research-register statements whose places fall on the topic's pages, through `HIS_PLACES`. The ANABELIAN_A1_SUCCESSOR places on \"cote 14\" are left out, because they are misplaced (`GLOBAL/MISPLACED_REGISTER_PLACES.tsv`).",
     "- **Units:** the companion units on the topic's pages.",
     "",
     "The ranking runs from least to most researched, by statements per 100 transcribed pages.", "",
     "| rank | topic | title | pages | items | his claims | statements (proved/refuted/known/open) | per 100 pages | items reached | runs | units |",
     "|---:|---|---|---:|---:|---:|---|---:|---:|---|---:|"]
for r in rows:
    L.append(f"| {r['rank']} | {r['topic']} | {r['title'][:46]} | {r['transcribed_pages']} | {r['items']} | {r['claims_of_his']} | "
             f"{r['statements']} ({r['proved']}/{r['refuted']}/{r['known']}/{r['open']}) | {r['statements_per_100_pages']} | "
             f"{r['items_with_statements']}/{r['items']} | {r['runs'][:60]} | {r['companion_units']} |")
zero = [r for r in rows if r["statements"] == 0]
tot_pg = sum(r["transcribed_pages"] for r in rows)
tot_st = sum(r["statements"] for r in rows)
top = sorted(rows, key=lambda r: -r["statements"])[:6]
L += ["", "## What it shows",
      f"- **{len(zero)} of 32 topics have no research-run statement on their pages:** {', '.join(r['topic'] for r in zero)}. Together they hold {sum(r['transcribed_pages'] for r in zero)} of {tot_pg} transcribed pages and {sum(r['items'] for r in zero)} items.",
      f"- **The research is concentrated:** {', '.join(r['topic'] + ' (' + str(r['statements']) + ')' for r in top)} carry {sum(r['statements'] for r in top)} of the {tot_st} statements on any page.",
      f"- **La Longue Marche itself** (cote 140) is not one of the 32 topics. {len(lm_only)} statements are placed there; the edition of La Longue Marche carries them.",
      "- **Les Dérivateurs** (SA32): its statements are placed by page of the manuscript, so they count at topic level until the scan concordance for cote 157 exists.",
      "- **Sweep 3's order** follows the rank. Among the topics with no statement, the topic with more transcribed pages comes first. Each neglected area gets a reading of its notes, his claims checked as items, and its own foundation (Part 0 pointers), before any research run is pointed at it."]
(G / "NEGLECT.md").write_text("\n".join(L) + "\n", encoding="utf-8")
print(now, "| topics", len(rows), "zero", len(zero), "| pages", tot_pg, "statements", tot_st)
for r in rows[:12]:
    print(r["rank"], r["topic"], r["transcribed_pages"], r["items"], r["statements"], r["statements_per_100_pages"])
