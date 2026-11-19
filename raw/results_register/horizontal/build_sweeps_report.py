#!/usr/bin/env python3
"""Build SWEEPS_REPORT_20261119.html: one self-contained page on the horizontal sweeps (sweeps 1, 2 and 3, and the
S6 sweep): what each was, what they found, coverage per topic, and what is left.

Every number on the page is read from the files at build time. The findings texts and the descriptions of the sweeps
are written here; each finding names its locator, and its check events are counted from the topic's CHECK_EVENTS
files at build time.

usage: python -I -B results_register/horizontal/build_sweeps_report.py

Written 19 Nov 2026 by Claude Opus 5.5 at effort max (agent a0c4bb37, the broad agent of sweeps 1 and 2)."""
import collections
import csv
import datetime
import glob as globmod
import html
import re
from pathlib import Path

csv.field_size_limit(2**31 - 1)

HERE = Path(__file__).resolve().parent            # results_register/horizontal
RR = HERE.parent                                  # results_register
D = RR.parent                                     # the project root (Documents)
S1, S2, S3 = HERE / "sweep1", HERE / "sweep2", HERE / "sweep3"
G = D / "grothendieck_archive_transcription_20261110"
TS = D / "TO_SEND"
OUT = HERE / "SWEEPS_REPORT_20261119.html"
TOPICS = [f"SA{i:02d}" for i in range(1, 33)]
NOT_IN_COVERAGE = ("140", "157")   # La Longue Marche and Les Derivateurs: not counted in COVERAGE_20261118.md
OPUS = "Claude Opus 5.5 at effort max"
PRO = "GPT-6 Astra (ChatGPT Pro mode)"
SOURCES = []


# ---------------------------------------------------------------- helpers
def rel(p):
    try:
        return Path(p).resolve().relative_to(D).as_posix()
    except Exception:
        return Path(p).name


def src(p):
    r = rel(p)
    if r not in SOURCES:
        SOURCES.append(r)
    return p


def read_tsv(p):
    p = Path(p)
    if not p.is_file():
        return []
    src(p)
    with p.open(encoding="utf-8-sig", errors="replace", newline="") as f:
        return [r for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)]


def text(p):
    p = Path(p)
    if not p.is_file():
        return ""
    src(p)
    return p.read_text(encoding="utf-8", errors="replace")


def esc(s):
    return html.escape(str(s), quote=True)


def fmt(n):
    return f"{n:,}" if isinstance(n, int) else str(n)


def pct(a, b):
    return 100.0 * a / b if b else 0.0


def norm_cote(c):
    m = re.fullmatch(r"\s*(?:MPL_)?0*(\d{1,3})(?:-0*(\d{1,2}))?\s*", c or "")
    if not m:
        return None
    return m.group(1) + (f"-{m.group(2)}" if m.group(2) else "")


RANGE = re.compile(r"(\d{1,4})\s*[-\u2013]\s*(\d{1,4})|(\d{1,4})")
SEG = re.compile(r"(\d{1,3}(?:-\d{1,2})?)\s*[/:]\s*(\d{1,4}(?:\s*[-\u2013]\s*\d{1,4})?"
                 r"(?:\s*(?:,|and)\s*\d{1,4}(?:\s*[-\u2013]\s*\d{1,4})?)*)")
PAREN = re.compile(r"\([^)]*\)?")


def scan_numbers(s):
    s = PAREN.sub(" ", s or "")
    out = []
    for a, b, c in RANGE.findall(s):
        if a:
            a, b = int(a), int(b)
            if a <= b and b - a <= 400:
                out.extend(range(a, b + 1))
        elif c:
            out.append(int(c))
    return out


def pairs_of(cote_field, scans_field):
    """(cote, scan) pairs named by a cote field and a scans field; 'c/s' and 'c:s' forms carry their own cote."""
    s = PAREN.sub(" ", scans_field or "")
    out = set()
    segs = SEG.findall(s)
    if segs:
        for c, r in segs:
            cc = norm_cote(c)
            if cc:
                out |= {(cc, n) for n in scan_numbers(r)}
        return out
    cc = norm_cote(cote_field)
    if cc:
        out |= {(cc, n) for n in scan_numbers(s)}
    return out


def in_coverage(pair):
    return not pair[0].split("-")[0] in NOT_IN_COVERAGE


def stamp(s):
    m = re.search(r"(\d{4})(\d{2})(\d{2})T(\d{2})(\d{2})Z", s or "")
    if not m:
        return ""
    months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
    return f"{int(m.group(3))} {months[int(m.group(2)) - 1]} {m.group(4)}:{m.group(5)} UTC"


# ---------------------------------------------------------------- topics, neglect
NEG = {r.get("topic"): r for r in read_tsv(S2 / "GLOBAL" / "NEGLECT.tsv")}


def ni(t, k):
    try:
        return int(float(NEG.get(t, {}).get(k) or 0))
    except ValueError:
        return 0


TITLE = {t: NEG.get(t, {}).get("title", "") for t in TOPICS}
RANK = {t: ni(t, "rank") for t in TOPICS}
PAGES = {t: ni(t, "transcribed_pages") for t in TOPICS}

# ---------------------------------------------------------------- sweeps 1 and 2
def placement(sdir, t):
    rs = read_tsv(sdir / t / "PLACEMENT.tsv")
    pairs = set()
    for r in rs:
        pairs |= pairs_of(r.get("cote"), r.get("scans"))
    return {"rows": len(rs), "read": sum(1 for r in rs if "read" in (r.get("basis") or "")),
            "passage": sum(1 for r in rs if "passage-read" in (r.get("basis") or "")), "pairs": pairs, "list": rs}


P1 = {t: placement(S1, t) for t in TOPICS}
P2 = {t: placement(S2, t) for t in TOPICS}


def topic_count(sdir, t, name):
    return len(read_tsv(sdir / t / name))


SW = {}
for key, sdir in (("1", S1), ("2", S2)):
    SW[key] = {
        "rows": sum((P1 if key == "1" else P2)[t]["rows"] for t in TOPICS),
        "read": sum((P1 if key == "1" else P2)[t]["read"] for t in TOPICS),
        "passage": sum((P1 if key == "1" else P2)[t]["passage"] for t in TOPICS),
        "items": sum(topic_count(sdir, t, "OBJECTS.tsv") for t in TOPICS),
        "flags": sum(topic_count(sdir, t, "FLAGS.tsv") for t in TOPICS),
        "corrections": sum(topic_count(sdir, t, "CORRECTIONS.tsv") for t in TOPICS),
        "events": sum(topic_count(sdir, t, "CHECK_EVENTS.tsv") for t in TOPICS)
        + sum(len(read_tsv(p)) for p in sorted((sdir / "GLOBAL").glob("CHECK_EVENTS*.tsv"))),
        "objects": len(read_tsv(sdir / "GLOBAL" / "GLOBAL_OBJECTS.tsv")),
        "themes": len(read_tsv(sdir / "GLOBAL" / "THEMES.tsv")),
        "links": len(read_tsv(sdir / "GLOBAL" / "LINKS.tsv")),
    }
GO = read_tsv(S2 / "GLOBAL" / "GLOBAL_OBJECTS.tsv")
SW["2"]["multi"] = sum(1 for r in GO if (r.get("n_topics") or "1").strip() not in ("", "0", "1"))
UNITS = read_tsv(S2 / "inputs" / "UNITS.tsv")
UNOTES = [u for u in UNITS if not (u.get("cls") or "").endswith("doubts")]
SW["2"]["entries"] = len(UNITS)
SW["2"]["notes"] = len(UNOTES)
SW["2"]["doubts"] = len(UNITS) - len(UNOTES)
SW["2"]["words"] = sum(int(u.get("words") or 0) for u in UNOTES if (u.get("words") or "").isdigit())
UNPLACED = len(read_tsv(S2 / "GLOBAL" / "UNPLACED.tsv"))
REPORTS = sorted((S2 / "REPORTS").glob("*.md"))
for p in REPORTS:
    src(p)
FLAGKINDS = collections.Counter()
MISREAD = collections.Counter()
for t in TOPICS:
    for r in read_tsv(S2 / t / "FLAGS.tsv"):
        k = (r.get("kind") or "").strip()
        FLAGKINDS[k] += 1
        if "suspected misreading" in k.lower():
            MISREAD[t] += 1

# pair -> topics and cote -> topics, from sweep 2's placement
PAIR_TOPICS = collections.defaultdict(set)
COTE_TOPICS = collections.defaultdict(collections.Counter)
for t in TOPICS:
    for r in P2[t]["list"]:
        for pr in pairs_of(r.get("cote"), r.get("scans")):
            PAIR_TOPICS[pr].add(t)
        c = norm_cote(r.get("cote"))
        if c:
            COTE_TOPICS[c][t] += 1


def topics_of_pair(pr):
    if pr in PAIR_TOPICS:
        return PAIR_TOPICS[pr]
    c = COTE_TOPICS.get(pr[0])
    return {c.most_common(1)[0][0]} if c else set()


# ---------------------------------------------------------------- sweep 3
S3T = [t for t in TOPICS if (S3 / t).is_dir()]
EVK = ("id", "date_utc", "who", "how", "result", "where")


def norm_row(r, keys=EVK):
    return "\t".join(re.sub(r"\s+", " ", (r.get(k) or "") if isinstance(r.get(k), str) else "").strip().lower()
                     for k in keys)


EV3, CO3, OVERLAP = {}, {}, 0
for t in S3T:
    seen, evs = set(), []
    for r in read_tsv(S3 / t / "CHECK_EVENTS.tsv"):
        k = norm_row(r)
        if k not in seen:
            seen.add(k)
            evs.append(r)
    for p in sorted((S3 / t / "readings").glob("*CHECK_EVENTS*.tsv")):
        for r in read_tsv(p):
            k = norm_row(r)
            if k in seen:
                OVERLAP += 1
            else:
                seen.add(k)
                evs.append(r)
    EV3[t] = evs
    cos, cseen = [], set()
    for p in [S3 / t / "CORRECTIONS.tsv"] + sorted((S3 / t / "readings").glob("*CORRECTIONS*.tsv")):
        for r in read_tsv(p):
            k = "\t".join(sorted((str(v) or "").strip().lower() for v in r.values() if isinstance(v, str)))
            if k not in cseen:
                cseen.add(k)
                cos.append(r)
    CO3[t] = cos


def check_type(how):
    h = (how or "").lower()
    if "refut" in h:
        return "refuted, refined statement"
    if "reading" in h or "image" in h:
        return "reading decided on the scan"
    if "independent" in h:
        return "independent re-proof"
    if "targeted" in h:
        return "targeted proof check"
    if "comput" in h or "certif" in h:
        return "computation"
    if "deriv" in h:
        return "re-derivation"
    if "used" in h:
        return "used and rechecked"
    if "background" in h:
        return "carried as background"
    return "other"


AGENT = re.compile(r"\ba[0-9a-f]{16}\b")
MODEL = re.compile(r"Claude (?:Opus|Fable|Sonnet) [\d.]+ at effort \w+")
NO_RE = re.compile(r"not read in sweep 3|placed only|not in any package|only cited", re.I)
PART_RES = [re.compile(r"read in part \(([^)]*)\)", re.I),
            re.compile(r"scans ([\d][\d\s,\u2013-]*(?:and [\d][\d\s,\u2013-]*)*) read", re.I),
            re.compile(r"read in sweep 3[^;:]*: scans ([\d][\d\s,\u2013-]*)", re.I),
            re.compile(r"\bread (\d{1,3}:[\d\s,\u2013-]+)", re.I)]
STRONG = re.compile(r"read in full|read mathematically|worked through|collated word by word|sweep-3 reading|"
                    r"read in sweep 3|read by reader", re.I)
IMGPART = re.compile(r"\b(\d{3}(?:\s*(?:,|and)\s*\d{3})*)\s+(?:checked\s+)?on the images?", re.I)
WEAK = re.compile(r"looked at|checked on the image|;\s*read\b|read on the scan", re.I)
SKIPCOLS = {"scans", "open_readings", "translate_to", "why", "cote", "cote_part", "edition_and_translation",
            "edition_ready", "translation_ready", "ready_for_edition", "ready_for_translation"}


def row_status(r):
    t = " ; ".join(v for k, v in r.items() if k not in SKIPCOLS and isinstance(v, str))
    if re.search(r"read in full|read mathematically", t, re.I):
        return "full", []
    parts = [m.group(1) for rx in PART_RES for m in rx.finditer(t)]
    if parts:
        return "part", parts
    if NO_RE.search(t):
        return "no", []
    if STRONG.search(t):
        return "full", []
    m = IMGPART.search(t)
    if m:
        return "part", [m.group(1)]
    if WEAK.search(t):
        return "full", []
    return "unmarked", []


def open_count(s):
    s = (s or "").strip()
    if re.fullmatch(r"\d+", s):
        return int(s), 0
    m = re.match(r"(\d+) unsure(?: marks)?(?:, (\d+) illegible)?", s)
    if m:
        return int(m.group(1)) + int(m.group(2) or 0), 0
    m = re.match(r"about (\d+)", s)
    if m:
        return int(m.group(1)), 0
    if s.lower() in ("", "-", "none", "minor", "none listed") or s.lower().startswith("none"):
        return 0, 0
    return 0, 1


L3 = {}
L3_LISTED, L3_COUNTONLY = set(), []
PAIRX = re.compile(r"(?<![\w.])(\d{1,3}(?:-\d{1,2})?)\s*[:/]\s*0*(\d{1,3})(?:\s*[-–]\s*0*(\d{1,3}))?(?![\d.])")
for t in S3T:
    listed, count_only, unmarked, opened, named = set(), 0, 0, 0, 0
    for r in read_tsv(S3 / t / "DELIVERABLES.tsv"):
        cote = r.get("cote") or r.get("cote_part") or ""
        scans = r.get("scans") or ""
        n_open, n_named = open_count(r.get("open_readings"))
        opened += n_open
        named += n_named
        st, parts = row_status(r)
        m = re.fullmatch(r"\s*(\d+)\s+scans?\s*", PAREN.sub(" ", scans))
        if st == "no":
            continue
        if st == "unmarked":
            unmarked += 1
            continue
        if st == "part":
            spec = " , ".join(re.sub(r"\b\d{1,3}(?:-\d{1,2})?\s*:", " ", re.sub(r"scans?", " ", x)) for x in parts)
            prs = pairs_of(cote, spec) if norm_cote(cote) else set()
            if not prs and m:
                count_only += int(m.group(1))
            listed |= prs
            continue
        if m:
            count_only += int(m.group(1))
            L3_COUNTONLY.append((t, cote, int(m.group(1))))
            continue
        prs = pairs_of(cote, scans)
        if prs:
            listed |= prs
        else:
            cm = re.search(r"\((\d+) scans?\)", scans)
            if cm:
                count_only += int(cm.group(1))
                L3_COUNTONLY.append((t, cote, int(cm.group(1))))
    from_deliverables = len(listed) + count_only
    for r in EV3[t] + CO3[t]:
        blob = " ".join(r.get(k) or "" for k in ("id", "where") if isinstance(r.get(k), str))
        for c, a, z in PAIRX.findall(blob):
            cc = norm_cote(c)
            a = int(a)
            z = int(z) if z else a
            if cc and a <= z <= 400 and z - a <= 60:
                listed |= {(cc, s) for s in range(a, z + 1)}
    L3_LISTED |= listed
    evs = EV3[t]
    agents = sorted({a for r in evs for a in AGENT.findall(r.get("who") or "")})
    types = collections.Counter(check_type(r.get("how")) for r in evs)
    dates = sorted({(r.get("date_utc") or "")[:10] for r in evs if re.match(r"\d{4}-\d{2}-\d{2}", r.get("date_utc") or "")})
    readings = [p for p in (S3 / t / "readings").glob("*.md")] if (S3 / t / "readings").is_dir() else []
    L3[t] = {"scans": len(listed) + count_only, "listed": listed, "count_only": count_only, "unmarked": unmarked,
             "from_deliverables": from_deliverables,
             "open": opened, "named": named, "events": len(evs), "corrections": len(CO3[t]),
             "agents": agents, "types": types, "dates": dates, "readings": len(readings),
             "study_words": len(text(S3 / t / "STUDY.md").split()),
             "depends": len(read_tsv(S3 / t / "DEPENDS.tsv"))}
listed_cotes = {c for c, _ in L3_LISTED}
L3_GLOBAL = len({p for p in L3_LISTED if in_coverage(p)}) + sum(
    n for t, cote, n in L3_COUNTONLY
    if not any(norm_cote(x) in listed_cotes for x in re.split(r"[+,]", cote)))
EV3_ALL = [r for t in S3T for r in EV3[t]]
TYPES3 = collections.Counter(check_type(r.get("how")) for r in EV3_ALL)
AGENTS3 = sorted({a for r in EV3_ALL for a in AGENT.findall(r.get("who") or "")})
MODELS3 = collections.Counter(m for r in EV3_ALL for m in MODEL.findall(r.get("who") or ""))
DATES3 = sorted({(r.get("date_utc") or "")[:10] for r in EV3_ALL if re.match(r"\d{4}-\d{2}-\d{2}", r.get("date_utc") or "")})
LIT = read_tsv(S3 / "LITERATURE_CHECK.tsv")
LITV = collections.Counter((re.split(r"[\s,;(]", (r.get("verdict") or "").strip().lower()) or ["?"])[0] for r in LIT)
LITWHO = collections.Counter(m for r in LIT for m in MODEL.findall(r.get("who") or ""))

# ---------------------------------------------------------------- the S6 sweep
S6D = RR / "sweep1_s6"
S6SUM = text(S6D / "SUMMARY.md")
m = re.search(r"all ([\d,]+) rows", S6SUM)
S6 = {"rows": m.group(1) if m else "?", "merges": len(read_tsv(S6D / "MERGES.tsv")),
      "flags": len(read_tsv(S6D / "FLAG_VERDICTS.tsv")), "events": len(read_tsv(S6D / "CHECK_EVENTS.tsv")),
      "placement": len(read_tsv(S6D / "PLACEMENT.tsv"))}
S6CORR = re.findall(r"^## \d+\. (.+)$", text(S6D / "CORRECTIONS.md"), re.M)

# ---------------------------------------------------------------- the check register
REG = read_tsv(RR / "CHECK_REGISTER.tsv")
REG_IDS = len({r.get("id") for r in REG})
REG_S3 = sum(1 for r in REG if "horizontal/sweep3" in (r.get("source_file") or "").replace("\\", "/"))

# ---------------------------------------------------------------- research prompts by topic (night prompts)
SENT_LOG = read_tsv(TS / "PRO" / "SENT_PRO.tsv")


def sent_time(folder):
    for r in SENT_LOG:
        if folder and folder in (r.get("prompt") or ""):
            return (r.get("sent_utc") or "").strip()
    return ""


def topic_dirs(base, rx=r"(?:^|_)(SA\d\d)(?:_|$)"):
    out = {}
    if base.is_dir():
        for p in sorted(base.iterdir()):
            mm = re.search(rx, p.name)
            if p.is_dir() and mm:
                out.setdefault(mm.group(1), p.name)
    return out


R_BUILT = {t for t in TOPICS if (D / "pro_prompt_builds" / f"RESEARCH_{t}").is_dir()}
R_WAIT = topic_dirs(TS / "PRO" / "1_Archive_research_by_topic")
R_SENT = topic_dirs(TS / "_SENT" / "PRO" / "1_Archive_research_by_topic")
R_RET = {}
if (G / "research_returns").is_dir():
    for p in sorted((G / "research_returns").iterdir()):
        mm = re.match(r"RESEARCH_(SA\d\d)_(?:checkpoint_(\d+)|(final(?:_INCOMPLETE)?))_(\d{8}T\d{4}Z)", p.name)  # 19 Nov: final_INCOMPLETE
        if mm:
            cur = R_RET.get(mm.group(1))
            if not cur or mm.group(4) > cur[2] or mm.group(3):
                R_RET[mm.group(1)] = ("final" if mm.group(3) else f"checkpoint {int(mm.group(2)):02d}", p.name, mm.group(4))


def research_state(t):
    if t in R_RET:
        kind, _, ts = R_RET[t]
        # 19 Nov 2026: a run silent for hours ends at its last checkpoint (the user's rule); once that checkpoint is taken
        # in (an intake file in sweep3/<topic>/), it counts as returned
        if kind != "final" and list((D / "results_register" / "horizontal" / "sweep3" / t).glob(f"INTAKE_RESEARCH_{t}_*.md")):
            return "returned", f"ended at {kind} ({stamp(ts)}), taken in"
        return ("returned" if kind == "final" else "running"), f"{kind} in, {stamp(ts)}"
    if t in R_SENT:
        return "sent", f"sent {sent_time(R_SENT[t]) or ''}".strip()
    if t in R_WAIT:
        return "waiting", "built, waiting to be sent"
    if t in R_BUILT:
        return "built", "built"
    return "none", "not built"


# ---------------------------------------------------------------- stage A topic dossiers (E small prompts)
E_BASE, E_SENT_BASE = TS / "PRO" / "E_Archive_small_prompts_54", TS / "_SENT" / "PRO" / "E_Archive_small_prompts_54"
E_WAIT_ALL = sorted(p.parent for p in E_BASE.glob("*/*/PROMPT.md")) if E_BASE.is_dir() else []
E_SENT_ALL = sorted(p.parent for p in E_SENT_BASE.glob("*/*/PROMPT.md")) if E_SENT_BASE.is_dir() else []
A_WAIT = {re.search(r"_(SA\d\d)_", p.name).group(1): p.name for p in E_WAIT_ALL if re.search(r"_(SA\d\d)_", p.name)}
A_SENT = {re.search(r"_(SA\d\d)_", p.name).group(1): p.name for p in E_SENT_ALL if re.search(r"_(SA\d\d)_", p.name)}
E_OTHER_WAIT = [p.name for p in E_WAIT_ALL if not re.search(r"_(SA\d\d)_", p.name)]
SA_SENT_DIR = G / "stage_a_20261118_sent"
A_RET = {}
if (SA_SENT_DIR / "returns").is_dir():
    for p in sorted((SA_SENT_DIR / "returns").iterdir()):
        mm = re.match(r"(SA\d\d)_(?:(v\d)_)?final_(\d{8}T\d{4}Z)", p.name)
        if mm and (mm.group(1) not in A_RET or mm.group(3) > A_RET[mm.group(1)][1]):
            A_RET[mm.group(1)] = (mm.group(2) or "", mm.group(3))
README_A = text(G / "stage_a_20261118" / "README_V2_20261118.md")
A_V1_SENT = {p.name[:4] for p in SA_SENT_DIR.iterdir() if re.match(r"SA\d\d", p.name)} if SA_SENT_DIR.is_dir() else set()


def dossier_state(t):
    if t in A_RET:
        v, ts = A_RET[t]
        note = ""
        if t == "SA02" and "version-1 SA02 (provisional)" in README_A and not v:
            note = " (version 1, provisional)"
        if t in A_WAIT:
            note += "; version 2 waiting"
        return "returned", f"final in, {stamp(ts)}{note}"
    if t in A_SENT:
        return "sent", "sent"
    if t in A_WAIT:
        return "waiting", "waiting to be sent"
    if t in A_V1_SENT:
        mm = re.search(r"%s died after (\d+) seconds" % t, README_A)
        return "sent", "version 1 sent 18 Nov" + (f"; it stopped after {mm.group(1)} s without a reply" if mm else "")
    return "none", "none"


# ---------------------------------------------------------------- working-through prompts (F)
F_BASE, F_SENT_BASE = TS / "PRO" / "F_Archive_working_through_200", TS / "_SENT" / "PRO" / "F_Archive_working_through_200"
F_WAIT = sorted(p.parent.name for p in F_BASE.glob("**/PROMPT.md")) if F_BASE.is_dir() else []
F_SENTL = sorted(p.parent.name for p in F_SENT_BASE.glob("**/PROMPT.md")) if F_SENT_BASE.is_dir() else []
TAG_TOPICS = {}
for r in GO:
    TAG_TOPICS[(r.get("tag") or "").strip()] = set(re.findall(r"SA\d\d", r.get("topics") or ""))


def f_topics(name):
    tags = re.findall(r"H[0-9A-Z]{3}", name.split("_OBJ_")[-1]) if "_OBJ_" in name else []
    out = set()
    for tg in tags:
        out |= TAG_TOPICS.get(tg, set())
    mm = re.search(r"_WT[AB]?_(\d{1,3}(?:-\d{1,2})?)_(\d{3})-(\d{3})", name)
    if mm:
        c = norm_cote(mm.group(1))
        for s in range(int(mm.group(2)), int(mm.group(3)) + 1):
            out |= topics_of_pair((c, s))
    return out


F_BY_TOPIC = {t: [0, 0] for t in TOPICS}
for names, idx in ((F_WAIT, 0), (F_SENTL, 1)):
    for nm in names:
        for t in f_topics(nm):
            if t in F_BY_TOPIC:
                F_BY_TOPIC[t][idx] += 1
F_UNMAPPED = sum(1 for nm in F_WAIT + F_SENTL if not f_topics(nm))

# ---------------------------------------------------------------- the Claude second pass (block prompts)
SPD = G / "second_pass"
BLOCKS = {}
PAGE_RX = re.compile(r"_(\d{1,3}(?:-\d{1,2})?)_scan(\d{3})\.tex")
if (SPD / "prompts").is_dir():
    src(SPD / "prompts")
    for p in sorted((SPD / "prompts").glob("PROMPT_*.md")):
        name = p.stem[len("PROMPT_"):]
        if "_" not in name:
            continue
        pkg, rng = name.rsplit("_", 1)
        t = p.read_text(encoding="utf-8", errors="replace")
        mm = re.search(r"Block: (\S+), (\d+) scans", t)
        prs = {(norm_cote(c), int(s)) for c, s in PAGE_RX.findall(t)}
        rm = re.fullmatch(r"(\d{1,3}(?:-\d{1,2})?)-(\d{3})-(\d{1,3}(?:-\d{1,2})?)-(\d{3})", rng)
        if not prs and rm and rm.group(1) == rm.group(3):
            prs = {(norm_cote(rm.group(1)), s) for s in range(int(rm.group(2)), int(rm.group(4)) + 1)}
        rm2, pm = re.fullmatch(r"(\d{3})-(\d{3})", rng), re.match(r"MPL_(\d{1,3}(?:-\d{1,2})?)_", pkg)
        if not prs and rm2 and pm:
            prs = {(norm_cote(pm.group(1)), s) for s in range(int(rm2.group(1)), int(rm2.group(2)) + 1)}
        BLOCKS[(pkg, rng)] = {"pkg": pkg, "rng": rng, "n": int(mm.group(2)) if mm else len(prs), "pairs": prs,
                              "done": False, "changes": 0, "hi": 0, "med": 0, "lo": 0, "doubt0": 0, "doubt1": 0,
                              "done_scans": 0}
if (SPD / "out").is_dir():
    src(SPD / "out")
    for f in sorted((SPD / "out").glob("*/*_changes.md")):
        pkg = f.parent.name
        rng = f.name[len(pkg) + 1:-len("_changes.md")] if f.name.startswith(pkg + "_") else f.stem
        b = BLOCKS.setdefault((pkg, rng), {"pkg": pkg, "rng": rng, "n": 0, "pairs": set(), "done": False,
                                           "changes": 0, "hi": 0, "med": 0, "lo": 0, "doubt0": 0, "doubt1": 0,
                                           "done_scans": 0})
        t = f.read_text(encoding="utf-8", errors="replace")
        b["done"] = True
        mm = re.search(r"^Scans: (\d+)", t, re.M)
        b["done_scans"] = int(mm.group(1)) if mm else b["n"]
        if not b["n"]:
            b["n"] = b["done_scans"]
        mm = re.search(r"Changes: (\d+)(?: \(high (\d+), medium (\d+), low (\d+)\))?", t)
        if mm:
            b["changes"] = int(mm.group(1))
            b["hi"], b["med"], b["lo"] = (int(x or 0) for x in mm.group(2, 3, 4))
        mm = re.search(r"Doubt marks: (\d+) in the first pass, (\d+) left", t)
        if mm:
            b["doubt0"], b["doubt1"] = int(mm.group(1)), int(mm.group(2))
PKGS = collections.OrderedDict()
for (pkg, rng), b in sorted(BLOCKS.items()):
    a = PKGS.setdefault(pkg, {"blocks": 0, "done": 0, "scans": 0, "done_scans": 0, "changes": 0, "pairs": set(),
                              "done_pairs": set()})
    a["blocks"] += 1
    a["scans"] += b["n"]
    a["pairs"] |= b["pairs"]
    if b["done"]:
        a["done"] += 1
        a["done_scans"] += b["done_scans"]
        a["changes"] += b["changes"]
        a["done_pairs"] |= b["pairs"]
BL_DONE = [b for b in BLOCKS.values() if b["done"]]
BL_TODO = [b for b in BLOCKS.values() if not b["done"]]
SP2_DONE_SCANS = sum(b["done_scans"] for b in BL_DONE)
SP2_TODO_SCANS = sum(b["n"] for b in BL_TODO)
SP2_TOPIC = collections.Counter()
for b in BL_DONE:
    for pr in b["pairs"]:
        for t in topics_of_pair(pr):
            SP2_TOPIC[t] += 1
SP2_DONE_COV = sum(b["done_scans"] for b in BL_DONE if b["pairs"] and all(in_coverage(pr) for pr in b["pairs"]))

# ---------------------------------------------------------------- the Pro second passes (SP packages)
SPP = G / "second_pass_pro_20261114"
SP_ROWS = read_tsv(SPP / "PACKAGES_20261115.tsv")
SP_WAIT = {}
SP_SENT = {}
for base, dst in ((TS / "PRO" / "2_Archive_second_passes", SP_WAIT), (TS / "_SENT" / "PRO" / "2_Archive_second_passes", SP_SENT)):
    if base.is_dir():
        for p in sorted(base.iterdir()):
            mm = re.search(r"_(SP\d\d)(_FINISH)?_", p.name + "_")
            if p.is_dir() and mm:
                dst[mm.group(1) + (mm.group(2) or "")] = p.name
SP_RET = {}
if (G / "second_pass_returns").is_dir():
    for p in sorted((G / "second_pass_returns").iterdir()):
        mm = re.match(r"(SP\d\d)_.*?_(?:checkpoint_(\d+)|(final))_(\d{8}T\d{4}Z)", p.name)
        if mm and (mm.group(1) not in SP_RET or mm.group(4) > SP_RET[mm.group(1)][1]):
            SP_RET[mm.group(1)] = ("final" if mm.group(3) else f"checkpoint {int(mm.group(2)):02d}", mm.group(4))
ROUTES = text(G / "SECOND_PASS_ROUTES_20261117.md")
mm = re.search(r"stopped after cp0?(\d+) \((\d+) of (\d+) scans\)", ROUTES)
SP04_DONE = (int(mm.group(2)), int(mm.group(3))) if mm else None
SP_STATE = []
for r in SP_ROWS:
    sp = (r.get("folder") or "")[:4]
    kind = (r.get("kind") or "").strip()
    scans = int(r.get("scans") or 0) if (r.get("scans") or "").isdigit() else 0
    built = (SPP / (r.get("folder") or "")).is_dir() or (SPP / "ALREADY_RAN" / (r.get("folder") or "")).is_dir() \
        or (SPP / "ALREADY_RAN" / sp).is_dir()
    if sp in SP_RET:
        k, ts = SP_RET[sp]
        st = f"{k} in, {stamp(ts)}"
        if sp + "_FINISH" in SP_WAIT:
            st += "; the finish prompt waits"
        cls = "running" if k != "final" else "returned"
        if sp == "SP04" and SP04_DONE:
            st = f"stopped after {k} ({SP04_DONE[0]} of {SP04_DONE[1]} scans); the finish prompt waits"
            cls = "partial"
    elif sp in SP_SENT:
        st, cls = f"sent {sent_time(SP_SENT[sp])}".strip(), "sent"
    elif sp in SP_WAIT:
        st, cls = "built, waiting to be sent", "waiting"
    elif built:
        st, cls = "built, not in the send queue", "built"
    else:
        st, cls = ("no folder: Pro first passes go to the Claude second pass (SECOND_PASS_ROUTES, section 3)"
                   if kind == "2W" else "no folder"), "none"
    SP_STATE.append({"sp": sp, "folder": r.get("folder") or "", "kind": kind, "scans": scans,
                     "cotes": r.get("cotes") or "", "state": st, "cls": cls})

# ---------------------------------------------------------------- the intake ledger: transcription units
LEDGER = text(D / "field_experts" / "INTAKE_LEDGER.md")
mm = re.search(r"built (\d+ \w+ \d{4} \d\d:\d\d UTC)", LEDGER, re.I)
LEDGER_TIME = mm.group(1) if mm else ""
mm = re.search(r"\*\*Transcription units: (\d+)\*\* \(([^)]*)\)", LEDGER)
LEDGER_UNITS_LINE = (mm.group(1), mm.group(2)) if mm else ("?", "")
UNITS_L = []
sec = re.search(r"^## 4\.(.*?)^## 5\.", LEDGER, re.M | re.S)
for line in (sec.group(1).split("\n") if sec else []):
    if not line.startswith("| ") or line.startswith("| Unit") or line.startswith("|---"):
        continue
    f = [x.strip() for x in line.strip().strip("|").split(" | ")]
    if len(f) < 7:
        continue
    UNITS_L.append({"unit": f[0], "kind": f[1], "received": f[2], "sp": re.sub(r"<br>.*", "", f[5]),
                    "status": f[6]})
CW_COTE_SP = {}
for s in SP_STATE:
    if s["kind"] == "CW":
        for c in re.split(r"\+", s["cotes"]):
            cc = norm_cote(c)
            if cc:
                CW_COTE_SP[cc] = s


def pro_unit_pages(unit):
    pairs = set()
    for d in globmod.glob(str(G / "returns" / (globmod.escape(unit) + "*unzipped"))):
        for f in Path(d).rglob("*_scan[0-9][0-9][0-9].tex"):
            mm2 = PAGE_RX.search(f.name)
            if mm2:
                pairs.add((norm_cote(mm2.group(1)), int(mm2.group(2))))
    return len(pairs)


UNIT_STATE = collections.OrderedDict()   # state -> [units, scans, scans_known, names]
PRO_NOT_PREP = []
CW_NONE = []
for u in UNITS_L:
    kind = u["kind"]
    if "Pro package" in kind:
        a = PKGS.get(u["unit"])
        if a:
            if a["done"] == a["blocks"]:
                st = "Pro package: second pass done"
            elif a["done"]:
                st = "Pro package: second pass partial"
            else:
                st = "Pro package: block prompts prepared, not run"
            sc, known = (a["done_scans"] if a["done"] == a["blocks"] else a["scans"] - a["done_scans"]), True
        else:
            st = "Pro package: no block prompts yet"
            sc = pro_unit_pages(u["unit"])
            known = sc > 0
            PRO_NOT_PREP.append((u["unit"], sc))
    elif "Codex" in kind:
        mm2 = re.match(r"cote (\S+)", u["unit"])
        c = norm_cote(mm2.group(1)) if mm2 else None
        s = CW_COTE_SP.get(c)
        nunits = re.search(r"(\d+) unit\(s\)", u["received"])
        nunits = int(nunits.group(1)) if nunits else 1
        if s is None:
            st = "Codex-web units: no second-pass package"
            CW_NONE.append((u["unit"], nunits))
        else:
            st = {"partial": "Codex-web units: Pro second pass partial", "running": "Codex-web units: Pro second pass running",
                  "returned": "Codex-web units: Pro second pass returned", "sent": "Codex-web units: Pro second pass sent",
                  "waiting": "Codex-web units: Pro second pass built, waiting",
                  "built": "Codex-web units: Pro second pass built, not queued"}.get(s["cls"], "Codex-web units: other")
        sc, known = 0, False
    else:
        st, sc, known = "control run: no second pass needed", 0, False
    e = UNIT_STATE.setdefault(st, [0, 0, 0])
    e[0] += 1
    e[1] += sc
    e[2] += 1 if known else 0

# ---------------------------------------------------------------- archive coverage
COV = text(G / "COVERAGE_20261118.md")
mm = re.search(r"\*\*All cotes:\*\* (\d+) scans; (\d+) blank or logo; (\d+) read before; \*\*(\d+) read for the first "
               r"time since\*\* \((\d+) by Work, (\d+) by Pro\); (\d+) given a second reading by Work since", COV)
COVN = dict(zip(("scans", "blank", "before", "first", "work", "pro", "second"), (int(x) for x in mm.groups()))) if mm else {}
TOTAL = COVN.get("scans", 12524)
NONBLANK = TOTAL - COVN.get("blank", 0)
L1_COV = len({p for t in TOPICS for p in P1[t]["pairs"] if in_coverage(p)})
L2_COV = len({p for t in TOPICS for p in P2[t]["pairs"] if in_coverage(p)})

# ---------------------------------------------------------------- findings (written here; checks counted from files)
FINDINGS = [
    dict(title="His “cohomologie absolue” is Weil-étale cohomology", topic="SA05", where="12:60-84; 15:172-178; the boxed conjecture on 12:75",
         text="The cohomology he calls absolute on these pages is Weil-étale cohomology. Over finite fields his statements hold. "
              "Over arithmetic bases with l inverted two of them fail: the l-adic comparison, and the boxed conjecture "
              "“H¹(S,A)(l) fini si l premier à S”. Counterexamples: S = Spec ℤ[1/l], and the Néron model of X₀(11) over "
              "ℤ[1/11l], through Tate's global Euler characteristic.",
         changes="The conjecture stands for S over a finite field. For S flat over ℤ the correction rows carry the refined statement.",
         found=f"sweep-3 reader a7b7747f with its readers aa713c8c and ac391f82, {OPUS}, 19 Nov",
         status="refuted over ℤ, refined statement recorded", files=[S3 / "SA05"],
         rx=r"X_0\(11\)|Weil|absolu|H\^1\(S|Z\[1/"),
    dict(title="The letter to Serre of 27.8.1965 and Griffiths' quintic", topic="SA06", where="14:44-47 (also 14:112)",
         text="14:44-47 are four typed pages of the letter to Serre dated Thil, 27.8.1965: the text printed in the "
              "Grothendieck-Serre correspondence (SMF 2001, pp. 232-234). The typed copy ends with an N.B. on the omitted Tate "
              "twists that the print lacks, and on 14:46 reads “A et B impliquent” where the print has “B implique”. "
              "Conjectures A, A′ and A″ modulo algebraic equivalence fail in that form: on a general quintic threefold the "
              "difference of two lines is homologically trivial and not algebraically trivial (Griffiths 1969; Clemens 1983).",
         changes="The statements hold with homological equivalence in place of algebraic equivalence; the refined forms are in the correction rows.",
         found=f"sweep-3 reader add83e0c (reading c14_c15rest_part1), {OPUS}, 19 Nov",
         status="identified; refuted in that form, refined statement recorded", files=[S3 / "SA06"],
         rx=r"\(14:4[4-7]\)|\(14:112\)|Griffiths|quintic"),
    dict(title="Lefschetz in degree 1, and the minimal class", topic="SA06", where="14:52-71",
         text="14:52-71 prove the Lefschetz standard conjecture in degree 1, l-adically. Question 2 on 14:71 reduces to the "
              "algebraicity of the minimal class θ^(g−1)/(g−1)! on a principally polarized abelian variety, which is open for a "
              "very general one of dimension at least 4.",
         changes="Places the open part of his question exactly: one algebraicity statement for one class.",
         found=f"sweep-3 reader add83e0c, {OPUS}, 19 Nov", status="proof re-derived; the reduced question is open",
         files=[S3 / "SA06"], rx=r"\(14:(5[2-9]|6\d|7[01])\)|minimal class"),
    dict(title="15:205 states the naive general Hodge conjecture", topic="SA06", where="15:205",
         text="15:205 states the general Hodge conjecture in the naive form, the form he showed false in 1969 "
              "(“Hodge's general conjecture is false for trivial reasons”, Topology 8).",
         changes="Dates the page before 1969 in substance, and marks the statement as superseded by his own correction.",
         found=f"sweep-3 reader add83e0c, {OPUS}, 19 Nov", status="identified", files=[S3 / "SA06", S3 / "SA07"],
         rx=r"15:205"),
    dict(title="Five-point counts on 148/033 (object H0HW)", topic="SA29-SA31, SA22", where="148/033; items SA22-7, SA29-Q1, SA30-6, SA31-Q1, SA31-5",
         text="The page counts 14 families and 16 orbits of five-point configurations: 5 × 60 + 11 × 120 = 1,620. The struck "
              "totals 900 and 1500 are corrected to 1020 and 1620, each by +120. The first row of objects is the 62 special "
              "configurations: μ₅ with D₅ (12), μ₄ ∪ {∞} with C₄ (30), μ₃ ∪ {0, ∞} with D₃ (20). The relator count, at least "
              "1,080, agrees with the research runs EXIT_TOWER (B.15, B.26) and LM4_SUCCESSOR (E.37, E.38). “3×40 = 3×40” is "
              "written over a struck “2×60 = 2×60” and leaves the totals unchanged.",
         changes="One object across four topics; his counts and the runs' counts agree.",
         found=f"a0c4bb37 (sweep 2, broad agent), {OPUS}, with inputs from ae4ae3dc ({OPUS}), 18 Nov",
         status="reading decided on the scan image", files=[S2 / "GLOBAL"], rx=r"148|H0HW|SA31-5|SA22-7|SA29-Q1|SA30-6|SA31-Q1"),
    dict(title="“Sans rigueur” at 29/139", topic="SA12", where="29/139, 29/041, 31/020, 33/023, 33/075, 29/125",
         text="The margin of 29/139 reads “Sans rigueur” and 29/041 reads “prouvé”: the status of these statements is his own. "
              "31/020 has a “<” slip of his and a transcription misreading of “+2” as “+1” (flag F32). 33/023 and 33/075 are "
              "slips of typescript n° 391. The month on 29/125 cannot be read (6 or 8).",
         changes="The SGA statements on these pages carry his own status marks; one misreading corrected.",
         found=f"sub-agent a65dbdc2 of a0c4bb37 (sweep 2), {OPUS}, 18 Nov", status="readings decided on the scan images",
         files=[S2 / "SA12"], rx=r"29|31/0|33/0"),
    dict(title="Remark a) on 136:12 proved; the Koszul sequences of 136:362", topic="SA08", where="136/2-141; 136/142-376",
         text="Remark a) on scan 12 is proved with Sullivan's forms. The first of the three Koszul sequences on 136:362 is not "
              "exact over ℤ; it is exact where i! is invertible. The three-data theorem as stated drops a condition, which the "
              "correction rows supply.",
         changes="Two statements of the de Rham notes need a hypothesis; one remark becomes a proved statement.",
         found=f"sweep-3 readers a1f628dd (136/2-141) and aa2156d1 (136/142-376), {OPUS}, 18-19 Nov",
         status="proved; refined statements recorded", files=[S3 / "SA08"], rx=r"Sullivan|Koszul|three|136:0?12\b"),
    dict(title="Cotes 137-138: 137:12 false over ℤ; pinned maps; oranges", topic="SA09", where="137:12; 138:99-100; 138:131",
         text="On 137:12, Λᵏ(Λʲ Ψ) strictly special is false over ℤ (k = j = 2: π₃ = ℤ/2). On 138:99-100 the category of "
              "C₀-pinned oriented maps is not rigid in general (a torus counterexample); the count needs the orbit sizes of the "
              "automorphisms. On 138:131 oranges of every order n have nontrivial holomorphic automorphisms z ↦ az (a > 0), so "
              "the exception list I-III is incomplete.",
         changes="Three statements refined; the counts that rest on rigidity need automorphism orbits.",
         found=f"sweep-3 reader a188625c, {OPUS}, 18 Nov", status="refuted, refined statements recorded",
         files=[S3 / "SA09"], rx=r"137:12|138:99|138:131|orange|pinned"),
    dict(title="Vers une géométrie des formes (cote 156)", topic="SA21", where="156-4 to 156-9; 156-7/64-65 and 97-99",
         text="“C4 automatique” is false (reader A). The orthomodular law at 156-7/97-99 fails, and so does the characterization "
              "by simplices (reader B). His conjecture of distributivity of the lattice of supports (156-7/64-65, 156-4/69) is "
              "refuted. Supports are Boolean in faithful magasins (reader C).",
         changes="The axioms of the 1986 text need these corrections before the forms can carry a theory.",
         found=f"sweep-3 readers a4e5251e (A), ae747b2d (B) and a770b79a (C), {OPUS}, 18-19 Nov",
         status="refuted, refined statements recorded", files=[S3 / "SA21"], rx=r"C4|orthomodular|simplic|distributiv|Boolean|bool"),
    dict(title="Cote 155: Tannakian reconstruction for bialgebroids", topic="SA20", where="155 (manuscript pages 1-5); 121/49-73; 153",
         text="The manuscript on cote 155 is Tannakian reconstruction in bialgebroid form, with the Takeuchi product.",
         changes="Identifies the subject of a short manuscript that had no name in the notes.",
         found=f"sweep-3 reader aff4deb1, {OPUS}, 18 Nov", status="identified; statements re-derived",
         files=[S3 / "SA20"], rx=r"Takeuchi|bialgebroid|Tannak"),
    dict(title="Tonight's second pass on cote 15", topic="SA05-SA07", where="MPL_15_139-194: blocks 15-139-157, 15-159-177, 15-178-194",
         text="The three blocks were checked against the scan images. Settled readings include g_φ, “algébrique” and "
              "“engendrée” on 139; Pic^abs and “réseaux de Hodge” on 161; a struck “est” on 163; H_ξ(W) and “coh. de De Rham” "
              "on 165; “(5.1.)” on 179; an inserted “physique” on 183. 184 and 186 are the backs of a reused English typescript; "
              "192 and 194 are a Bourbaki “Tribu n° 59”, upside down. Scans 179-194 come from Work (GPT-6.2 Astra at reasoning "
              "effort max), folders K15-06 and K15-07.",
         changes="The stalled Pro package is complete as an edition text for these scans.",
         found=f"a7b7747f (block 1) and a28ea31f (blocks 2 and 3), {OPUS}, 19 Nov", status="second pass done",
         files=[], rx="", block_pkg="MPL_15_139-194"),
    dict(title="159/20: his slip, and H03F is two pages", topic="SA04, SA32", where="159/20; items SA04-9 and SA32-4",
         text="On 159/20 both “c(1) = 1” and “(ν′ − μ)·1” are in the ink, so the sign is his slip (it should be +μ). SA04-9 and "
              "SA32-4 describe two different pages; they do not disagree.",
         changes="Closes a disagreement flag between two topics.", found=f"a0c4bb37 (sweep 2), {OPUS}, 18 Nov",
         status="reading decided on the scan image", files=[S2 / "GLOBAL"], rx=r"159|H03F|SA04-9|SA32-4"),
    dict(title="Cote 36: Deligne's hand", topic="SA13", where="36/3-8; 36/6; 32/31-32; 34/5-6; 39/20; 36/56",
         text="36/3-8 are in Deligne's hand, so SA13-34, -37 and -38 are his statements; 36/6 reads “63”, which note N20 "
              "misreads. 32/31-32 is a letter of Deligne. 34/5-6 has an omission, 39/20 an index slip and 36/56 a sign slip, "
              "all Grothendieck's.",
         changes="Three items re-attributed to Deligne; one note corrected.", found=f"sub-agent a84c887c of a0c4bb37 (sweep 2), {OPUS}, 18 Nov",
         status="readings decided on the scan images", files=[S2 / "SA13"], rx=r"36|32/3|34/|39/"),
    dict(title="EGA (SA23): 22/027-029 and 1/082", topic="SA23", where="22/027-029; 1/082; 2/045",
         text="The counterexample on 22/027-029 is correct. 1/082 reads “classes remarquables”, which the transcription misread. "
              "2/045 has O_C, a slip of his. Flag F01 stays open.",
         changes="One misreading corrected; one counterexample confirmed.", found=f"sub-agent a3d30d2d of a0c4bb37 (sweep 2), {OPUS}, 18 Nov",
         status="readings decided on the scan images; F01 open", files=[S2 / "SA23"],
         rx=r"1\.pdf page 82|2\.pdf page 45|22\.pdf page|K1-03#2|research_leads#41"),
    dict(title="The letter to Mumford, and Tate's hand", topic="SA14-SA19", where="the Mumford letter; 6:39; 47/009",
         text="The letter to Mumford withdraws his algebraicity conjecture for the modular families. Of the pages ascribed to "
              "Tate, only 6:39 is in Tate's hand. 47/009 has a χ slip of his.",
         changes="One conjecture marked as withdrawn by him; attributions corrected.", found=f"deep agent a28ea31f (sweep 2), {OPUS}, 18 Nov",
         status="readings decided on the scan images", files=[S2 / t for t in ("SA14", "SA15", "SA16", "SA18", "SA19")],
         rx=r"Mumford|6:39|6/039|47/009"),
    dict(title="Cotes 93, 84 and 102", topic="SA01-SA04", where="93/052; 84/120; 102",
         text="93/052 reads ‖yw − w‖, which both transcriptions misread. X_J on 84/120 is a slip of his. Cote 102 is headed "
              "“Pour EGA VI”.", changes="One misreading in two witnesses corrected; cote 102 placed with the EGA plans.",
         found=f"deep agent a6d42bf6 (sweep 2), {OPUS}, 18 Nov", status="readings decided on the scan images",
         files=[S2 / t for t in ("SA01", "SA02", "SA03", "SA04")], rx=r"93/052|84/120|102"),
    dict(title="Les Dérivateurs and the two meanings of “totally aspheric”", topic="SA32", where="157-3/345; 157-1/3; tags HTA1, HTA2",
         text="157-3/345 is headed “Contre-exemples pour la totale asphéricité”; 157-1/3 raises the f! question; the Sính "
              "typescript is hers. “Totally aspheric” has two meanings in the archive: Pursuing Stacks §65 A with cote 114 "
              "Prop. 4 (HTA1), and Les Dérivateurs XII (HTA2).",
         changes="Two concepts kept apart under two tags.", found=f"deep agent a34c0444 (sweeps 1-2), {OPUS}, 18 Nov",
         status="identified", files=[S2 / "SA32"], rx=r"157-3|157-1|aspher"),
    dict(title="Cote 67, cote 123, and a control run", topic="SA20, SA22, SA28", where="67/086; 67/098; 123; CTRL-145_2",
         text="The statement on 67/086 fails in characteristic 5; 67/098 reads √3 against 3. Cote 67 is dated 1977-78. Cote 123 "
              "holds the letter to Kostant. The Σ of control run CTRL-145_2 is a misreading.",
         changes="Dating and one characteristic-5 exception.", found=f"deep agent ae4ae3dc (sweeps 1-2), {OPUS}, 18 Nov",
         status="readings decided on the scan images", files=[S2 / t for t in ("SA20", "SA22", "SA28")],
         rx=r"67/08|67/09|123|CTRL-145"),
]


def finding_checks(fd):
    evs = []
    for d in fd["files"]:
        for p in sorted(Path(d).glob("CHECK_EVENTS*.tsv")) + sorted(Path(d).glob("readings/*CHECK_EVENTS*.tsv")):
            evs += read_tsv(p)
    seen, out = set(), []
    for r in evs:
        k = norm_row(r)
        if k in seen:
            continue
        seen.add(k)
        blob = " ".join(str(v) for v in r.values() if isinstance(v, str))
        if fd["rx"] and re.search(fd["rx"], blob):
            out.append(r)
    types = collections.Counter(check_type(r.get("how")) for r in out)
    models = collections.Counter(m for r in out for m in MODEL.findall(r.get("who") or ""))
    return len(out), types, models


# ---------------------------------------------------------------- readers and companions (added 19 Nov ~06 UTC)
# Criteria, from the files: readers-are-key-deliverables (a reader goes out when all its material is transcribed,
# ideally after its second pass, one reader per cote or dossier); pdf-overflow-and-visual-check (overfull boxes and a
# visual check before publication); COMPANION_DESIGN_20261118.md 2.7 and 4.1-4.5 (run A and run B per slice of 12-17
# pages, 1-2 hours each; a translation pass; every note on record gets a verdict; results enter by locator from the
# register); check-rubric (check types).
import math


def first_cote(src):
    m = re.match(r"^MPL_(\d+(?:-\d+)?)", src) or re.match(r"^(?:work:|codex:)?[A-Z]+(\d+(?:-\d+)?)-\d+", src) \
        or re.match(r"^(?:work:|codex:)?CTRL-?(\d+)", src)
    return m.group(1) if m else ""


MARK = re.compile(r"\\(?:unsure|illegible)\b")
TPAGES = {t: collections.defaultdict(set) for t in TOPICS}
TMARK = {t: collections.defaultdict(set) for t in TOPICS}
NOTE_WORDS = collections.Counter()
_seen = set()
for u in UNITS:
    t = (u.get("topic") or "").strip()
    if t not in TPAGES or not u.get("source_file"):
        continue
    if not (u.get("cls") or "").endswith("doubts") and (u.get("words") or "").isdigit():
        NOTE_WORDS[t] += int(u["words"])
    nf = D / u["source_file"]
    src_ = (u.get("entry_id") or "").split("#")[0].split(":records")[0].replace(":doubts", "")
    cand = nf.parent / (nf.name.replace("_mathnotes.md", "_transcription.tex").replace("_notes.md", "_transcription.tex")
                        .replace("_doubts.md", "_transcription.tex"))
    tex = cand if cand.is_file() else None
    if tex is None and nf.parent.is_dir():
        tx = sorted(nf.parent.glob("*_transcription.tex"))
        tex = tx[0] if tx else None
    if tex is None or (tex, t) in _seen:
        continue
    _seen.add((tex, t))
    c = norm_cote(first_cote(re.sub(r"^(work|codex):", "", src_)))
    if not c:
        continue
    chunks = re.split(r"\\scanpage\{(\d+)\}", tex.read_text(encoding="utf-8", errors="replace"))
    for i in range(1, len(chunks) - 1, 2):
        s = int(chunks[i])
        TPAGES[t][c].add(s)
        if MARK.search(chunks[i + 1]):
            TMARK[t][c].add(s)
DONE_PAIRS = {pr for b in BL_DONE for pr in b["pairs"]}
OUTMARK = {}
if (SPD / "out").is_dir():
    for f in (SPD / "out").glob("*/*_scan[0-9][0-9][0-9].tex"):
        m2 = PAGE_RX.search(f.name)
        if m2:
            OUTMARK[(norm_cote(m2.group(1)), int(m2.group(2)))] = bool(MARK.search(f.read_text(encoding="utf-8", errors="replace")))


def cote_measures(t, c):
    pg = TPAGES[t][c]
    done = {s for s in pg if (c, s) in DONE_PAIRS}
    openm = {s for s in pg if (OUTMARK[(c, s)] if (c, s) in OUTMARK else s in TMARK[t][c])}
    return len(pg), len(done), len(openm)


def reader_state(n, done):
    if n == 0:
        return "none", "not ready"
    return ("returned", "ready") if done >= n else ("waiting", "buildable with gaps")


# reader builds on file (pro_admin_readers_20261112/ALREADY_RAN; cotes from their prompts and their works)
RA = D / "pro_admin_readers_20261112" / "ALREADY_RAN"
READER_KEYS = {"DERIVATEURS": (["157"], r"D[ée]rivateurs"), "LONGUE_MARCHE": (["140"], r"Longue Marche"),
               "PURSUING_STACKS": (["134"], r"Pursuing Stacks"), "ESQUISSE": (["119"], r"Esquisse"),
               "EGA_V": (["24", "25"], r"EGA V\b")}
AUDIT = text(D / "braindump_board" / "OVERFULL_AUDIT_20261113.md")
READERS = {}
UNDER = text(D / "pro_admin_readers_20261112" / "UNDER_CONSTRUCTION" / "README.md")
if RA.is_dir():
    for p in sorted(RA.iterdir()):
        for k, (cotes, rx) in READER_KEYS.items():
            if p.is_dir() and p.name.endswith(k + "_READERS"):
                rows_ = [ln for ln in AUDIT.split("\n") if ln.startswith("|") and re.search(rx, ln)]
                for c in cotes:
                    READERS[c] = (p.name, ("in the overfull audit of 13 Nov: " + re.sub(r"\s+", " ", rows_[0])[:140])
                                  if rows_ else "no PDF check on file")
UNDER_COTES = collections.defaultdict(list)
for ln in UNDER.split("\n"):
    mm = re.match(r"\| (\d+) ([^|]+) \| ([^|]+) \|", ln)
    m3 = re.search(r"cotes? ((?:\d{1,3}(?:-\d{1,2})?(?:,\s*|\s+and\s+)?)+)", mm.group(3)) if mm else None
    if m3:
        for c in re.findall(r"\d{1,3}(?:-\d{1,2})?", m3.group(1)):
            if norm_cote(c):
                UNDER_COTES[norm_cote(c)].append(f"{mm.group(1)} {mm.group(2).strip()}")


def reader_build(c):
    base = c.split("-")[0]
    if c in READERS or base in READERS:
        nm, chk = READERS.get(c) or READERS.get(base)
        return f"built ({nm}); {chk}"
    if c in UNDER_COTES:
        return "prompt under construction (" + ", ".join(sorted(set(UNDER_COTES[c]))) + ")"
    return "none"


# research runs on the topic's pages, their intake, and the checked statements in the register
RUN_STATUS = {}
sec3 = re.search(r"^## 3\.(.*?)^## 4\.", LEDGER, re.M | re.S)
for line in (sec3.group(1).split("\n") if sec3 else []):
    if line.startswith("| ") and not line.startswith("| Run") and not line.startswith("|---"):
        f = [x.strip() for x in line.strip().strip("|").split(" | ")]
        if len(f) >= 9:
            RUN_STATUS[f[0].strip("*").strip()] = f[8]
ST_TOPIC = collections.defaultdict(set)
for r in read_tsv(RR / "sweep2_global" / "HIS_PLACES.tsv"):
    tag = (r.get("tag") or "").strip()
    if not tag or tag.startswith("ANABELIAN_A1_SUCCESSOR:B.11"):
        continue
    if re.search(r"D[ée]rivateurs", r.get("work") or ""):
        ST_TOPIC["SA32"].add(tag)
        continue
    c = norm_cote(r.get("cote") or "")
    if not c:
        continue
    hit = False
    for s in scan_numbers(r.get("scans") or ""):
        for t in TOPICS:
            if s in TPAGES[t].get(c, ()):
                ST_TOPIC[t].add(tag)
                hit = True
    if not hit and COTE_TOPICS.get(c):
        ST_TOPIC[COTE_TOPICS[c].most_common(1)[0][0]].add(tag)
for r in read_tsv(S2 / "GLOBAL" / "INTERLINKS" / "ITEM_REGISTER.tsv"):
    if (r.get("topic") or "") in TOPICS and (r.get("statement") or "").strip():
        ST_TOPIC[r["topic"]].add(r["statement"].strip())
STRONG_RX = re.compile(r"^T[1237]|targeted|independent|re-?proof|comput|certif|lean|refut", re.I)
REG_HOW = collections.defaultdict(list)
for r in REG:
    REG_HOW[(r.get("id") or "").strip()].append(r.get("how") or "")
COMP = {}
for t in TOPICS:
    tags = ST_TOPIC[t]
    runs = sorted({x.split(":")[0] for x in tags})
    untaken = [x for x in runs if not RUN_STATUS.get(x, "").startswith("taken in")]
    checked = sum(1 for x in tags if REG_HOW.get(x))
    strong = sum(1 for x in tags if any(STRONG_RX.search(h) for h in REG_HOW.get(x, [])))
    pages = sum(len(v) for v in TPAGES[t].values())
    done = sum(cote_measures(t, c)[1] for c in TPAGES[t])
    openp = sum(cote_measures(t, c)[2] for c in TPAGES[t])
    gaps = []
    if t not in S3T:
        state = ("none", "not yet")
        gaps.append("no sweep-3 reading")
    else:
        rs = research_state(t)[0]
        if rs != "returned":
            gaps.append({"running": "its research prompt is still running (checkpoints in, not taken in)",
                         "waiting": "its research prompt waits to be sent", "built": "its research prompt is built, not sent",
                         "sent": "its research prompt is sent, no return yet", "none": "no research prompt"}[rs])
        if untaken:
            gaps.append(f"{len(untaken)} of {len(runs)} research runs on its pages not taken in")
        if done < pages:
            gaps.append(f"second pass on {done} of {pages} pages")
        state = ("waiting", "can start with gaps") if gaps else ("returned", "can start")
    slices = math.ceil(pages / 15) if pages else 0
    COMP[t] = {"state": state, "gaps": gaps, "pages": pages, "done": done, "open": openp, "runs": len(runs),
               "untaken": len(untaken), "statements": len(tags), "checked": checked, "strong": strong,
               "slices": slices, "density": (NOTE_WORDS[t] / pages) if pages else 0.0,
               "open_items": ni(t, "open") + topic_count(S2, t, "FLAGS.tsv"),
               "f_prompts": F_BY_TOPIC[t][0] + F_BY_TOPIC[t][1]}
    rd = reader_state(pages, done)
    COMP[t]["reader"] = rd
ORDER_C = {"can start": 0, "can start with gaps": 1, "not yet": 2}
COMP_ORDER = sorted(TOPICS, key=lambda t: (ORDER_C[COMP[t]["state"][1]],
                                         len(COMP[t]["gaps"]), -(COMP[t]["done"] / COMP[t]["pages"] if COMP[t]["pages"] else 0.0),
                                         RANK[t] or 99))


# ---------------------------------------------------------------- html
CSS = """
:root{--bg:#f7f6f2;--fg:#1d1d1b;--muted:#5f5e58;--card:#ffffff;--border:#dedbd2;--accent:#2f5d8a;--accent2:#7a4e9c;
--good:#2e7d4f;--warn:#a86a12;--bad:#a83a32;--bar:#d8e3ee;--barfill:#2f5d8a;--code:#efece4;}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#161615;--fg:#e9e7e1;--muted:#a6a39a;--card:#21201e;
--border:#3a3935;--accent:#8db7e0;--accent2:#c3a2de;--good:#7fc79a;--warn:#e0b060;--bad:#ee8f86;--bar:#2c3540;--barfill:#8db7e0;--code:#2a2926;}}
:root[data-theme="dark"]{--bg:#161615;--fg:#e9e7e1;--muted:#a6a39a;--card:#21201e;--border:#3a3935;--accent:#8db7e0;
--accent2:#c3a2de;--good:#7fc79a;--warn:#e0b060;--bad:#ee8f86;--bar:#2c3540;--barfill:#8db7e0;--code:#2a2926;}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;}
main{max-width:1180px;margin:0 auto;padding:24px 16px 64px}
h1{font-size:1.7rem;margin:.2em 0 .1em}
h2{font-size:1.25rem;margin:2.2em 0 .6em;padding-bottom:.25em;border-bottom:1px solid var(--border)}
h3{font-size:1.02rem;margin:0 0 .35em}
p{margin:.45em 0}
a{color:var(--accent)}
.muted{color:var(--muted)}
.small{font-size:.86rem}
.tiles{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px;margin:16px 0}
.tile{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:10px 12px}
.tile .n{font-size:1.45rem;font-weight:650;line-height:1.2}
.tile .l{font-size:.82rem;color:var(--muted)}
.tablewrap{overflow-x:auto;-webkit-overflow-scrolling:touch;border:1px solid var(--border);border-radius:10px;background:var(--card);margin:10px 0 16px}
table{border-collapse:collapse;width:100%;font-size:.86rem}
th,td{padding:6px 9px;border-bottom:1px solid var(--border);text-align:left;vertical-align:top}
th{position:sticky;top:0;background:var(--card);font-weight:600;white-space:nowrap}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
tr:last-child td{border-bottom:none}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:12px}
.card{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:12px 14px;min-width:0}
.card .meta{font-size:.82rem;color:var(--muted);margin-bottom:.3em}
.badge{display:inline-block;font-size:.75rem;padding:1px 7px;border-radius:999px;border:1px solid var(--border);white-space:nowrap}
.b-returned,.b-done{color:var(--good);border-color:var(--good)}
.b-running,.b-sent,.b-partial{color:var(--accent);border-color:var(--accent)}
.b-waiting,.b-built{color:var(--warn);border-color:var(--warn)}
.b-none{color:var(--muted)}
.bars{display:grid;gap:8px;margin:10px 0}
.barrow{display:grid;grid-template-columns:minmax(120px,300px) 1fr 120px;gap:10px;align-items:center;font-size:.88rem}
.bar{height:12px;background:var(--bar);border-radius:6px;overflow:hidden}
.bar>span{display:block;height:100%;background:var(--barfill)}
@media (max-width:640px){.barrow{grid-template-columns:1fr 90px}.barrow .bar{grid-column:1 / span 2;grid-row:2}}
details{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:8px 12px;margin:8px 0}
summary{cursor:pointer;font-weight:600}
ul,ol{padding-left:1.3em}
li{margin:.25em 0}
code{background:var(--code);padding:0 4px;border-radius:4px;font-size:.85em;word-break:break-word}
.note{border-left:3px solid var(--accent2);padding:4px 10px;margin:10px 0;color:var(--muted);font-size:.9rem}
"""


def table(headers, rows, numcols=()):
    h = "".join(f'<th class="num">{esc(x)}</th>' if i in numcols else f"<th>{esc(x)}</th>" for i, x in enumerate(headers))
    body = []
    for r in rows:
        tds = []
        for i, x in enumerate(r):
            cell = x if isinstance(x, Markup) else esc(fmt(x) if isinstance(x, int) else x)
            tds.append(f'<td class="num">{cell}</td>' if i in numcols else f"<td>{cell}</td>")
        body.append("<tr>" + "".join(tds) + "</tr>")
    return f'<div class="tablewrap"><table><thead><tr>{h}</tr></thead><tbody>{"".join(body)}</tbody></table></div>'


class Markup(str):
    pass


def badge(cls, label):
    return Markup(f'<span class="badge b-{esc(cls)}">{esc(label)}</span>')


def bar(label, a, b, note=""):
    p = pct(a, b)
    return (f'<div class="barrow"><div>{esc(label)}</div><div class="bar"><span style="width:{min(p, 100):.1f}%"></span></div>'
            f'<div class="num small">{fmt(a)} / {fmt(b)} ({p:.1f} %){esc(note)}</div></div>')


def tile(n, label):
    return f'<div class="tile"><div class="n">{esc(fmt(n))}</div><div class="l">{esc(label)}</div></div>'


now = datetime.datetime.now(datetime.timezone.utc).strftime("%d %b %Y %H:%M UTC")
L3_TOPICS = len(S3T)
R_N = {k: sum(1 for t in TOPICS if research_state(t)[0] == k) for k in ("returned", "running", "sent", "waiting", "built", "none")}
A_N = {k: sum(1 for t in TOPICS if dossier_state(t)[0] == k) for k in ("returned", "sent", "waiting", "none")}
EV3_N = len(EV3_ALL)
CO3_N = sum(len(CO3[t]) for t in S3T)
not_l3 = [t for t in sorted(TOPICS, key=lambda t: RANK[t] or 99) if t not in S3T]
no_research = [t for t in sorted(TOPICS, key=lambda t: RANK[t] or 99) if t not in R_BUILT]

parts = []
A = parts.append
A(f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Archive sweeps report</title><style>{CSS}</style></head><body><main>
<h1>Archive sweeps report</h1>
<p class="muted">The horizontal sweeps over the Grothendieck archive at Montpellier: what each sweep was, what it found, how far it reached in
each of the 32 topics, and what is left. Built {esc(now)} by <code>results_register/horizontal/build_sweeps_report.py</code> from the files;
every count below is read from them at build time.</p>
<div class="tiles">
{tile(f"{len(S3T)} / 32", "topics read deeply (sweep 3)")}
{tile(SW['2']['entries'], "notes and doubts entries placed (sweep 2)")}
{tile(SW['2']['objects'], "global objects (sweep 2)")}
{tile(EV3_N + SW['1']['events'] + SW['2']['events'], "check events, sweeps 1-3")}
{tile(CO3_N + SW['2']['corrections'], "corrections and refinements, sweeps 2-3")}
{tile(L3_GLOBAL, "scans read in sweep 3")}
{tile(SP2_DONE_SCANS, "scans given the Claude second pass")}
{tile(f"{len(R_BUILT)} / {R_N['returned'] + R_N['running'] + R_N['sent']} / {R_N['returned'] + R_N['running']}", "research prompts built / sent / with a return")}
</div>""")

# 1. sweeps
A("<h2>1. The sweeps</h2>")
rows = [
    ["Sweep 1", "18 Nov, about 14:38-15:35 UTC",
     f"broad agent a0c4bb37, deep agents a28ea31f, a34c0444, ae4ae3dc, a6d42bf6, sub-agents a65dbdc2, a84c887c, a3d30d2d; all {OPUS}",
     "Every notes entry of the 32 topics placed under an item and a global object, mostly from index rows.",
     f"{fmt(SW['1']['rows'])} placement rows ({fmt(SW['1']['read'])} read); {fmt(SW['1']['items'])} items; {fmt(SW['1']['objects'])} objects; "
     f"{fmt(SW['1']['themes'])} themes; {fmt(SW['1']['flags'])} flags; {fmt(SW['1']['events'])} check events"],
    ["Sweep 2", "18 Nov, about 20:05-22:26 UTC",
     f"the same agents, {OPUS}",
     "Part 1: the gaps (notes filed since sweep 1, Codex sheet notes, Work folders, chat-B witnesses), every entry placed under one id "
     "rule. Part 2: the interlinks (what uses what, his claims against the register), WHAT_IS_WHERE, reports, the neglect ranking.",
     f"{fmt(SW['2']['notes'])} notes entries ({fmt(SW['2']['words'])} words) and {fmt(SW['2']['doubts'])} doubts entries, "
     f"{fmt(UNPLACED)} unplaced; {fmt(SW['2']['rows'])} placement rows "
     f"({fmt(SW['2']['read'])} read, {fmt(SW['2']['passage'])} by passage); {fmt(SW['2']['items'])} items; {fmt(SW['2']['objects'])} objects "
     f"({fmt(SW['2']['multi'])} in more than one topic); {fmt(SW['2']['themes'])} themes; {fmt(SW['2']['links'])} links; {fmt(SW['2']['flags'])} flags; "
     f"{fmt(SW['2']['corrections'])} corrections; {fmt(SW['2']['events'])} check events; {len(REPORTS)} reports"],
    ["Sweep 3", (DATES3[0] + " to " + DATES3[-1]) if DATES3 else "",
     f"{len(AGENTS3)} agents named in the check events (deep agents and their readers); " + "; ".join(f"{m} ({n} events)" for m, n in MODELS3.most_common()),
     "Deep reading of the least researched topics: each topic's pages read against the notes, statements re-derived or refuted, "
     "readings decided on the scans, a STUDY and RESEARCH_PACKAGES per topic, then one research prompt per topic.",
     f"{L3_TOPICS} topics; {fmt(L3_GLOBAL)} scans read; {fmt(EV3_N)} check events; {fmt(CO3_N)} corrections; "
     f"{sum(L3[t]['readings'] for t in S3T)} reading files; literature check: {len(LIT)} citations "
     f"({', '.join(f'{n} {k}' for k, n in LITV.most_common())}) by {', '.join(LITWHO) or OPUS}"],
    ["S6 sweep", "18 Nov", f"one agent, {OPUS}",
     f"The S6 research runs by {PRO}: one-line statements of every row placed, merged and flagged.",
     f"{S6['rows']} rows; {fmt(S6['merges'])} merges; {fmt(S6['flags'])} flag verdicts; {len(S6CORR)} corrections; {fmt(S6['events'])} check events"],
]
A(table(["Sweep", "When", "Who (model and effort)", "What it did", "Scale"], rows))
A(f'<p class="small muted">The check register (<code>results_register/CHECK_REGISTER.tsv</code>) holds {fmt(len(REG))} check rows on '
  f'{fmt(REG_IDS)} ids; {fmt(REG_S3)} of its rows come from sweep 3\'s files. Sweep 3\'s reading-level CHECK_EVENTS files repeat '
  f'{fmt(OVERLAP)} rows of the topic-level files; this page counts each row once.</p>')
A('<p class="small">Sweep 2 reports: ' + ", ".join(f'<a href="{esc(rel(p).split("results_register/horizontal/")[-1])}">{esc(p.stem)}</a>' for p in REPORTS) + "</p>")

# 2. findings
A("<h2>2. What they found</h2>")
A('<p class="muted small">Each finding with its place (cote:scan or cote/scan), what it changes, who found it, and the check events '
  'recorded at that place in the topic\'s files. “Check events” counts rows of CHECK_EVENTS whose text names the place; the types '
  'follow the check rubric.</p><div class="cards">')
for fd in FINDINGS:
    if fd.get("block_pkg"):
        a = PKGS.get(fd["block_pkg"], {})
        bl = [b for b in BLOCKS.values() if b["pkg"] == fd["block_pkg"] and b["done"]]
        chk = (f"second pass against the scan images: {len(bl)} blocks, {sum(b['done_scans'] for b in bl)} scans, "
               f"{sum(b['changes'] for b in bl)} changes (high {sum(b['hi'] for b in bl)}, medium {sum(b['med'] for b in bl)}, "
               f"low {sum(b['lo'] for b in bl)}); doubt marks {sum(b['doubt0'] for b in bl)} in the first pass, "
               f"{sum(b['doubt1'] for b in bl)} left")
    else:
        n, types, models = finding_checks(fd)
        chk = (f"{n} check event{'' if n == 1 else 's'}: " + ", ".join(f"{k} {v}" for k, v in types.most_common()) +
               (f"; by {', '.join(models)}" if models else "")) if n else "no check event names this place in the files searched"
    A(f'<div class="card"><h3>{esc(fd["title"])}</h3><div class="meta">{esc(fd["topic"])} · {esc(fd["where"])}</div>'
      f'<p>{esc(fd["text"])}</p><p><b>What it changes.</b> {esc(fd["changes"])}</p>'
      f'<p class="small"><b>Found by</b> {esc(fd["found"])}.</p><p class="small"><b>Checked:</b> {esc(chk)}.</p>'
      f'<p>{badge("done", fd["status"])}</p></div>')
A("</div>")
A("<h3 style='margin-top:1.4em'>Refutations recorded in sweep 3, by topic</h3>")
A('<p class="muted small">Every sweep-3 check event of type “refuted, with the refined statement”, as the files give it (id and result, shortened).</p>')
for t in S3T:
    ref = [r for r in EV3[t] if "refut" in (r.get("how") or "").lower()]
    if not ref:
        continue
    lis = "".join("<li><code>" + esc((r.get("id") or "")[:60]) + "</code> " +
                  esc(re.sub(r"\s+", " ", r.get("result") or "")[:330]) + "</li>" for r in ref)
    A(f"<details><summary>{esc(t)} {esc(TITLE[t])}: {len(ref)}</summary><ul class='small'>{lis}</ul></details>")
if S6CORR:
    A("<details><summary>The S6 sweep's corrections: " + str(len(S6CORR)) + "</summary><ol class='small'>" +
      "".join(f"<li>{esc(c)}</li>" for c in S6CORR) + "</ol></details>")

# 3. coverage
A("<h2>3. Coverage</h2>")
A('<div class="note">Levels: <b>1</b> the topic\'s notes entries were placed (sweep 1); <b>2</b> the gaps were placed and the '
  'interlinks built (sweep 2); <b>3</b> the topic\'s pages were read in depth (sweep 3). “Read” in sweeps 1-2 means the entry itself was '
  'read, not only its index row. Sweep-3 scans: the scan ranges of the DELIVERABLES rows marked read, together with every scan that a '
  'sweep-3 check event or correction names; rows the tables leave unmarked are not counted.</div>')
rows = []
for t in TOPICS:
    l3 = L3.get(t)
    rs, rlabel = research_state(t)
    ds, dlabel = dossier_state(t)
    st = f"{ni(t, 'statements')}"
    if ni(t, "statements"):
        st += f" ({ni(t, 'proved')} proved, {ni(t, 'refuted')} refuted, {ni(t, 'known')} known, {ni(t, 'open')} open)"
    rows.append([
        Markup(f"<b>{esc(t)}</b> <span class='small muted'>{esc(TITLE[t])}</span>"), RANK[t] or "", PAGES[t],
        f"{fmt(P1[t]['rows'])} / {fmt(P1[t]['read'])}",
        f"{fmt(P2[t]['rows'])} / {fmt(P2[t]['read'])}",
        topic_count(S2, t, "OBJECTS.tsv"), topic_count(S2, t, "FLAGS.tsv"),
        (f"{fmt(l3['scans'])} ({pct(l3['scans'], PAGES[t]):.0f} %)" if l3 else "—"),
        (l3["events"] if l3 else "—"), (l3["corrections"] if l3 else "—"),
        st, badge(ds, dlabel), badge(rs, rlabel),
        f"{F_BY_TOPIC[t][0] + F_BY_TOPIC[t][1]}" + (f" ({F_BY_TOPIC[t][1]} sent)" if F_BY_TOPIC[t][1] else ""),
        SP2_TOPIC.get(t, 0),
    ])
A(table(["Topic", "Neglect rank", "Pages", "Sweep 1 rows / read", "Sweep 2 rows / read", "Items", "Flags",
         "Sweep 3 scans read", "Sweep 3 checks", "Sweep 3 corrections", "Research-run statements",
         "Stage A dossier", "Research prompt", "Working-through prompts", "Second pass (scans)"],
        rows, numcols=(1, 2, 5, 6, 8, 9, 14)))
A('<p class="small muted">Pages: distinct cote and scan pairs in the topic\'s transcriptions (NEGLECT.tsv); topics share cotes, so the '
  'column does not add up to the archive. Research-run statements: research-register statements whose places fall on the topic\'s pages. '
  'Working-through prompts are counted for every topic their objects or pages belong to. Second pass: scans of finished Claude '
  'second-pass blocks that fall on the topic\'s pages.</p>')
A("<h3>Percentages</h3><div class='bars'>")
A(bar("Topics at level 1 (sweep 1)", sum(1 for t in TOPICS if P1[t]["rows"]), 32))
A(bar("Topics at level 2 (sweep 2)", sum(1 for t in TOPICS if P2[t]["rows"]), 32))
A(bar("Topics at level 3 (sweep 3)", L3_TOPICS, 32))
A(bar("Topics with a research prompt built", len(R_BUILT), 32))
A(bar("Topics with a stage A dossier returned", A_N["returned"], 32))
A(bar("Topic pages in topics at level 3", sum(PAGES[t] for t in S3T), sum(PAGES.values())))
A(bar("Archive scans named by placed sweep-1 entries", L1_COV, TOTAL))
A(bar("Archive scans named by placed sweep-2 entries", L2_COV, TOTAL))
A(bar("Archive scans read in sweep 3", L3_GLOBAL, TOTAL))
A(bar("Archive scans with a first reading", NONBLANK, TOTAL, " non-blank"))
A(bar("Archive scans given a second reading by Work since 18 Nov", COVN.get("second", 0), TOTAL))
A(bar("Archive scans given the Claude second pass", SP2_DONE_COV, TOTAL))
A("</div>")
A(f'<p class="small muted">The archive: {fmt(TOTAL)} scans in COVERAGE_20261118.md, of which {fmt(COVN.get("blank", 0))} are blank or the logo '
  f'sheet; La Longue Marche (140) and Les Dérivateurs (157) are finished texts and are not counted there, so their pages are left out of '
  f'the archive percentages (they stay in the topic columns). Every non-blank scan has a first reading: {fmt(COVN.get("before", 0))} before '
  f'18 Nov and {fmt(COVN.get("first", 0))} since ({fmt(COVN.get("work", 0))} by Work, GPT-6.2 Astra at reasoning effort max; '
  f'{fmt(COVN.get("pro", 0))} by Pro, {PRO}). “Named by placed entries” counts the scans that the placed notes entries cite; an entry '
  f'that cites only its first scan counts one.</p>')

# 4. what is left
# 4. readers and companions
A("<h2>4. Readers and companions: how far each topic is</h2>")
A('<div class="note">Criteria from the files. <b>Reader</b> (readers-are-key-deliverables): a reader goes out when all its material '
  'is transcribed, ideally after its second pass, bundled one reader per cote or dossier; before publication every PDF gets the '
  'overfull-box count and a look at the rendered pages (pdf-overflow-and-visual-check). So: <i>ready</i> = every page read and '
  'second-passed; <i>buildable with gaps</i> = every page read, the second pass incomplete; <i>not ready</i> = pages without a '
  'reading. <b>Companion</b> (COMPANION_DESIGN_20261118.md 2.7, 4.1-4.5): run A and run B per slice of 12-17 pages, 1-2 hours '
  'each, then a translation pass; every note on record gets a verdict in run A; results enter by locator from the register, '
  'with their check events by type (check-rubric). So: <i>can start</i> = read in sweep 3, notes placed, the research returns '
  'in and taken in, the second pass done; <i>can start with gaps</i> = read in sweep 3, with the gaps listed; <i>not yet</i> = no '
  'sweep-3 reading. <b>Left open by the files:</b> how many open ink readings a reader may carry; whether a reader needs the '
  'second pass or only prefers it (“ideally”); whether run A waits for the research returns or takes them in later by '
  'locator (4.5); which pages have the Work second witness that run A wants for Pro-first pages (4.3; the round-9 '
  'readings are not listed by scan); and any effort figure beyond the run cut of 2.7. The effort column is an estimate.</div>')
RS_N = collections.Counter(COMP[t]["reader"][1] for t in TOPICS)
CS_N = collections.Counter(COMP[t]["state"][1] for t in TOPICS)
ALLP = sum(COMP[t]["pages"] for t in TOPICS) or 1
A("<div class='bars'>")
for lab in ("ready", "buildable with gaps", "not ready"):
    A(bar(f"Reader: {lab} (topics)", RS_N.get(lab, 0), 32))
    A(bar(f"Reader: {lab} (topic pages)", sum(COMP[t]["pages"] for t in TOPICS if COMP[t]["reader"][1] == lab), ALLP))
for lab in ("can start", "can start with gaps", "not yet"):
    A(bar(f"Companion: {lab} (topics)", CS_N.get(lab, 0), 32))
    A(bar(f"Companion: {lab} (topic pages)", sum(COMP[t]["pages"] for t in TOPICS if COMP[t]["state"][1] == lab), ALLP))
A("</div>")
rows = []
for t in TOPICS:
    cm = COMP[t]
    cotes = sorted(TPAGES[t], key=lambda c: (int(c.split("-")[0]), c))
    builds = sorted({reader_build(c) for c in cotes} - {"none"})
    rows.append([Markup(f"<b>{esc(t)}</b> <span class='small muted'>{esc(TITLE[t])}</span>"), cm["pages"], cm["done"], cm["open"],
                 badge(*cm["reader"]), "; ".join(builds) or "none",
                 Markup(f"{badge(*cm['state'])}<br><span class='small'>{esc('; '.join(cm['gaps']) or 'inputs in place')}</span>"),
                 f"{cm['statements']} ({cm['checked']} with a check, {cm['strong']} with a targeted check, re-proof, computation or refutation: rubric types 1-3 and 7)",
                 f"{cm['runs']} ({cm['untaken']} not taken in)",
                 f"≈ {cm['slices']} slices: {2 * cm['slices']} Pro runs (≈ {2 * cm['slices']}-{4 * cm['slices']} h), {cm['slices']} "
                 f"translation passes; notes {cm['density']:.0f} words a page; {cm['open_items']} open items; "
                 f"{cm['f_prompts']} working-through prompts built (estimate)"])
A(table(["Topic", "Pages with a reading", "Second pass done", "Pages with open ink readings", "Reader", "Reader build",
         "Companion", "Research statements on its pages", "Research runs on its pages", "Companion effort (estimate)"],
        rows, numcols=(1, 2, 3)))
A('<p class="small muted">Pages: the scans of each topic\'s transcriptions (the transcription beside each placed notes file; a '
  'package that spans two cotes counts under its first). Open ink readings: pages whose newest text (the second pass where it is '
  'done) still carries an \\unsure or \\illegible mark. Statements: research-register statements whose places fall on the '
  'topic\'s pages (HIS_PLACES), or that sweep 2 linked to the topic\'s items (ITEM_REGISTER), so the count differs from NEGLECT.tsv, which also counts topic-level cote places; checks from CHECK_REGISTER.tsv. Runs taken in: the intake ledger, section 3. Effort: slices of '
  'about 15 pages, run A and run B per slice at 1-2 hours each (design 2.7; SP04, 120 scans in one run, crashed after 5 hours), '
  'one translation pass per slice; the notes density and the open items (open statements and sweep-2 flags) say where a '
  'slice will run long.</p>')
uneven = []
for t in TOPICS:
    cs = sorted(TPAGES[t], key=lambda c: (int(c.split("-")[0]), c))
    states = {reader_state(*cote_measures(t, c)[:2])[1] for c in cs}
    if len(cs) > 1 and len(states) > 1:
        for c in cs:
            n, d, o = cote_measures(t, c)
            uneven.append([t, c, n, d, o, badge(*reader_state(n, d)), reader_build(c)])
A("<details><summary>Per cote, for the topics whose cotes are at different states: " + str(len(uneven)) + " rows</summary>" +
  table(["Topic", "Cote", "Pages", "Second pass done", "Open ink readings", "Reader", "Reader build"], uneven, numcols=(2, 3, 4)) +
  "</details>")
A("<p><b>Order in which the companions could start</b> (state first, then the fewest gaps, then the largest share of pages "
  "second-passed, then the neglect ranking): " + ", ".join(f"{esc(t)} ({esc(COMP[t]['state'][1])})" for t in COMP_ORDER) + ".</p>")

A("<h2>5. What is left</h2>")
A("<h3>5.1 Pages without a second pass, by unit</h3>")
A(f'<p class="small muted">Units from the intake ledger (built {esc(LEDGER_TIME)}: {esc(LEDGER_UNITS_LINE[0])} transcription units, '
  f'“{esc(LEDGER_UNITS_LINE[1])}”), with the Pro packages recounted against the block files now. Scans: from the block prompts, or '
  f'counted from the package\'s page files where it has no prompts; the files give no per-unit scan count for the Codex-web units.</p>')
rows = [[k, v[0], (fmt(v[1]) if v[2] else "—")] for k, v in UNIT_STATE.items()]
A(table(["State", "Units", "Scans"], rows, numcols=(1, 2)))
A(f"<p>Claude second pass ({OPUS}): {len(BLOCKS)} block prompts; {len(BL_DONE)} done ({fmt(SP2_DONE_SCANS)} scans, "
  f"{fmt(sum(b['changes'] for b in BL_DONE))} changes); <b>{len(BL_TODO)} prepared and not run ({fmt(SP2_TODO_SCANS)} scans)</b>.</p>")
rows = []
for pkg, a in PKGS.items():
    if a["done"] < a["blocks"]:
        rows.append([pkg, f"{a['done']} / {a['blocks']}", a["scans"] - a["done_scans"] if a["done"] else a["scans"]])
A("<details><summary>Packages with block prompts not yet run: " + str(len(rows)) + "</summary>" +
  table(["Package", "Blocks done / prepared", "Scans left"], rows, numcols=(2,)) + "</details>")
rows = [[u, (sc if sc else "—")] for u, sc in sorted(PRO_NOT_PREP)]
A("<details><summary>Pro packages with no block prompts yet: " + str(len(rows)) + f" ({fmt(sum(sc for _, sc in PRO_NOT_PREP))} scans counted)</summary>" +
  table(["Package", "Scans (page files)"], rows, numcols=(1,)) + "</details>")
rows = [[s["sp"], s["kind"], s["cotes"], s["scans"], badge(s["cls"], s["state"])] for s in SP_STATE]
A(f"<p>Pro second passes for the Codex-web material and the Pro first passes ({PRO}; <code>second_pass_pro_20261114/PACKAGES_20261115.tsv</code>):</p>")
A(table(["Package", "Kind", "Cotes", "Scans", "State"], rows, numcols=(3,)))
A("<details><summary>Codex-web cotes in no second-pass package: " + str(len(CW_NONE)) + f" ({sum(n for _, n in CW_NONE)} units)</summary><p class='small'>" +
  ", ".join(f"{esc(u)} ({n})" for u, n in CW_NONE) + "</p></details>")

A("<h3>5.2 Readings left open for the ink</h3>")
rows = [[t, TITLE[t], L3[t]["open"], L3[t]["named"], MISREAD.get(t, 0)] for t in S3T]
A(table(["Topic", "Title", "Unsure or illegible marks still open (where the table counts them)",
         "Rows naming open readings in words", "Sweep-2 flags: suspected misreading"], rows, numcols=(2, 3, 4)))
A(f'<p class="small">Across all 32 topics sweep 2 flagged {sum(MISREAD.values())} suspected misreadings. Readings that the ink could '
  'not decide: the month on 29/125 (6 or 8); flag F01 of SA23. Pages with no transcription anywhere: 15:140, 12:69 and 12:97-98 '
  '(SA05 readers).</p>')
blk_left = sum(b["doubt1"] for b in BL_DONE)
A(f'<p class="small">In the finished second-pass blocks, {fmt(sum(b["doubt0"] for b in BL_DONE))} doubt marks of the first pass came '
  f'down to {fmt(blk_left)}.</p>')

A("<h3>5.3 Topics not yet swept at level 3</h3>")
rows = [[t, TITLE[t], RANK[t], PAGES[t], ni(t, "statements"), badge(*dossier_state(t))] for t in not_l3]
A(table(["Topic", "Title", "Neglect rank", "Pages", "Research-run statements", "Stage A dossier"], rows, numcols=(2, 3, 4)))
A(f"<p>{len(not_l3)} topics, {fmt(sum(PAGES[t] for t in not_l3))} topic pages, wait for sweep 3.</p>")

A("<h3>5.4 Research prompts</h3>")
rows = [[t, TITLE[t], badge(*research_state(t))] for t in TOPICS if t in R_BUILT]
A(table(["Topic", "Title", "Night research prompt"], rows))
A(f"<p>Not yet built ({len(no_research)} topics): " + ", ".join(esc(t) for t in no_research) + ".</p>")
SA02_V2 = " (SA02's version 2 among them)" if "SA02" in A_WAIT and "SA02" in A_RET else ""
A(f"<p>Stage A topic dossiers: {A_N['returned']} returned, {A_N['sent']} sent without a return yet; {len(A_WAIT)} dossier "
  f"prompts wait to be sent{SA02_V2}. "
  f"Other small prompts waiting: {len(E_OTHER_WAIT)} (" + ", ".join(esc(x) for x in E_OTHER_WAIT[:6]) +
  (", …" if len(E_OTHER_WAIT) > 6 else "") + f"). Working-through prompts: {len(F_WAIT)} waiting, {len(F_SENTL)} sent"
  f"{f'; {F_UNMAPPED} not mapped to a topic' if F_UNMAPPED else ''}.</p>")

A("<h3>5.5 Prompts waiting to be sent</h3><ul>")
A(f"<li>Night research prompts: {len(R_WAIT)} (" + ", ".join(esc(t) for t in sorted(R_WAIT)) + ").</li>")
def sp_wait_scans(k):
    if k.startswith("SP04") and k.endswith("_FINISH") and SP04_DONE:
        return SP04_DONE[1] - SP04_DONE[0]
    return next((s["scans"] for s in SP_STATE if s["sp"] == k[:4]), "?")


A("<li>Pro second passes: " + ", ".join(f"{esc(k)} ({sp_wait_scans(k)} scans)" for k in SP_WAIT) +
  (f"; SP04_FINISH carries the {SP04_DONE[1] - SP04_DONE[0]} scans SP04 did not reach" if SP04_DONE else "") + ".</li>")
A(f"<li>Claude second-pass blocks prepared and not run: {len(BL_TODO)} ({fmt(SP2_TODO_SCANS)} scans).</li>")
A(f"<li>Stage A dossiers: {len(A_WAIT)}; other small prompts: {len(E_OTHER_WAIT)}; working-through prompts: {len(F_WAIT)}.</li></ul>")

# 5. next
A("<h2>6. Next</h2><ol>")
A(f"<li>Sweep 3 for the {len(not_l3)} topics still at level 2, in neglect order: " + ", ".join(esc(t) for t in not_l3[:8]) +
  ", …; as for the first 12, each ends with its research prompt.</li>")
A(f"<li>Send the {len(R_WAIT)} waiting night research prompts, two per account at a time, and take in the "
  f"{R_N['running']} running ones at their checkpoints.</li>")
A(f"<li>Run the {len(BL_TODO)} prepared Claude second-pass blocks ({fmt(SP2_TODO_SCANS)} scans), and build block prompts for the "
  f"{len(PRO_NOT_PREP)} Pro packages that have none.</li>")
A(f"<li>Send the {len(SP_WAIT)} waiting Pro second passes; give the {len(CW_NONE)} Codex-web cotes outside every package a package.</li>")
A(f"<li>Decide the open readings on the images: the counted unsure marks of the sweep-3 topics and the {sum(MISREAD.values())} "
  "suspected misreadings of sweep 2.</li>")
A(f"<li>Send the {len(A_WAIT)} waiting stage A topic dossiers (claim checks and literature searches per topic).</li></ol>")

# sources and limits
A("<h2>Sources and limits</h2>")
A('<p class="small">What the files do not give: per-scan lists for the Codex-web units and for the SP04 and SP14 checkpoints; '
  'per-scan lists of the Work second readings (so they are not combined with the Claude second pass); read status for '
  f'{sum(L3[t]["unmarked"] for t in S3T)} DELIVERABLES rows that say neither read nor unread; the start and end times of sweep 3 '
  '(the dates come from its check events). The descriptions of the sweeps and the findings are written in the script; their numbers '
  'come from the files.</p>')
A("<details><summary>Files read for this page: " + str(len(SOURCES)) + "</summary><ul class='small'>" +
  "".join(f"<li><code>{esc(s)}</code></li>" for s in SOURCES) + "</ul></details>")
A("</main></body></html>")

page = "\n".join(parts)
for bad in (str(D), str(D).replace("\\", "/"), "Users/", "Users\\"):
    assert bad not in page, f"local path in page: {bad}"
assert not re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", page), "e-mail-like string in page"
OUT.write_text(page, encoding="utf-8")
print(f"wrote {rel(OUT)} ({len(page):,} bytes)")
print(f"sweep1 rows {SW['1']['rows']} items {SW['1']['items']} objects {SW['1']['objects']} events {SW['1']['events']}")
print(f"sweep2 entries {SW['2']['entries']} rows {SW['2']['rows']} items {SW['2']['items']} objects {SW['2']['objects']} "
      f"flags {SW['2']['flags']} corrections {SW['2']['corrections']} events {SW['2']['events']}")
print(f"sweep3 topics {L3_TOPICS} scans {L3_GLOBAL} events {EV3_N} corrections {CO3_N} overlap {OVERLAP}")
print("sweep3 per topic:", {t: (L3[t]['scans'], L3[t]['count_only'], L3[t]['unmarked']) for t in S3T})
print(f"coverage L1 {L1_COV} L2 {L2_COV} L3 {L3_GLOBAL} SP2 {SP2_DONE_COV} of {TOTAL}")
print(f"blocks {len(BLOCKS)} done {len(BL_DONE)} ({SP2_DONE_SCANS} scans) todo {len(BL_TODO)} ({SP2_TODO_SCANS} scans)")
print("units:", dict(UNIT_STATE))
print("research:", R_N, "dossiers:", A_N, "F:", len(F_WAIT), len(F_SENTL), F_UNMAPPED)
print("register rows", len(REG), "ids", REG_IDS, "from sweep3", REG_S3)
