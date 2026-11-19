"""The checkedness ledger: how often each claim has been worked over, by whom and how (18 Nov 2026).

The user, 18 Nov 2026 (USER_INPUTS.md P6820): "when noting the degree to which a claim is checked, always check how
often it's been reworked by different Astra instances and how many Fable intakes have taken place on that ... a degree
to which the claims are checked ledger should probably be constructed ... there's probably a lot more checks than you
think that have already happened. And actually constructing that will also show what hasn't been checked to any large
degree as well." Brief: results_register/CHECKEDNESS_BRIEF.md. Written and run by Claude Opus 5.5 at effort max.

Reads files only (no models, no git, no network); writes only into results_register/checkedness/:
- CHECKEDNESS_LEDGER.tsv  one row per claim lineage (canonical tag, member tags, status now and history, counts by
                          check type, by whom, first and last dates, strongest check);
- CHECKEDNESS_EVENTS.tsv  every iteration and check event the counts are made of (one row per event and lineage);
- LEAST_CHECKED.md        the proved claims that matter most with the fewest real checks, by line;
- S6_CASE.md              the 246 printed S6_10 rows without a CHECK_EVENTS.tsv line and the 286 rows awaiting the
                          credit comparison: how often each has been iterated over, and by what;
- checkedness_stats.json  the numbers METHOD.md quotes.
Sources: results_register/REGISTER.tsv; every results table of every return we hold (working copies, the
github_backup_20261113 repositories' pro_returns folders, _from_earlier_checkpoints/, retained/checkpoint_NN/); every
CHECK_EVENTS-like TSV in those folders; the S6_09 and S6_10 inventories with their check_record JSON; the prompts
(R-items, tasks, the "checked where you use them" clause); intake, expert, referee, review and note documents
(field_experts check_ledger.jsonl, INTAKE_LEDGER*.tsv, the S6 reviews and intakes); in-run review files of each
return; results_register/sweep1_*/MERGES.tsv when they exist.

Run: python -I -B C:/Users/user/Documents/results_register/checkedness/build_checkedness.py
"""
import collections
import csv
import datetime
import hashlib
import json
import pathlib
import re
import sys
import zipfile

sys.stdout.reconfigure(encoding="utf-8")
csv.field_size_limit(10 ** 9)
DOC = pathlib.Path(r"C:\Users\user\Documents")
OUT = DOC / "results_register" / "checkedness"
REG = DOC / "results_register"
FE = DOC / "field_experts"
GB = DOC / "github_backup_20261113"
S6W = DOC / "s6_pro_prompts_20261112_work"
sys.path.insert(0, str(FE))
import build_check_ledger as B  # noqa: E402

ASTRA = "GPT-6 Astra (ChatGPT Pro mode)"
OPUS_MAX = "Claude Opus 5.5 at effort max"
TODAY = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

# ------------------------------------------------------------------------------------------------ names and aliases
ALIAS = {
    "LM1": "LM1_GROUP_SCHEMES_rerun_20261112", "LM1_GROUP_SCHEMES": "LM1_GROUP_SCHEMES_rerun_20261112",
    "LM2": "LM2_LOOP_EQUATIONS", "LM4": "LM4_FINITE_GROUP_ACTIONS", "LM5": "LM5_MULTI_GALOIS_TOPOI",
    "LM6": "LM6_POINTS_AS_SECTIONS", "LM7": "LM7_FERMAT_TOWER", "LM8": "LM8_LIE_APPROXIMATIONS",
    "AP": "ANABELIAN_149_PUSH", "ANABELIAN_149": "ANABELIAN_149_PUSH", "CK": "CYCLOTOMIC_KERNEL",
    "SQ": "SECTIONS_OVER_Q", "TOTASPH": "TOTAL_ASPHERICITY", "TOTAL_EXACT": "TOTEX", "TOTAL_EXACT_2": "TOTEX2",
    "PRESHEAF_TOTALITY": "PRETOT", "REVERSIBLE_LOCALIZERS": "REVLOC", "FRAISSE_EXACT": "FREX", "FRAISSE": "FREX",
    "INV": "S6_01_INVARIANTS", "S6_01": "S6_01_INVARIANTS", "FAM": "S6_02_FAMILY", "S6_02": "S6_02_FAMILY",
    "PUSH": "S6_02_PUSH", "CDP": "S6_03_CDP", "S6_03": "S6_03_CDP", "MAPS": "S6_04_MAPS_MANIFOLDS",
    "S6_04": "S6_04_MAPS_MANIFOLDS", "ARI": "S6_05_ARITHMETIC", "S6_05": "S6_05_ARITHMETIC",
    "S6_BLIND_NIGHT": "S6_06_BLIND", "06_S6_BLIND_NIGHT": "S6_06_BLIND", "S6_06": "S6_06_BLIND",
    "09_S6_PAPERS": "S6_09_PAPERS", "S6_09": "S6_09_PAPERS", "S6_10": "S6_10_PAPERS", "Q03": "Q03_DEPOSIT",
    "TOTASPH_": "TOTAL_ASPHERICITY", "SECTION_GHOSTS_PROMPT": "SECTION_GHOSTS_PROMPT",
}
PROMPT_DIR_RUN = {  # prompt folder name (without NN_ prefix) -> run
    "FRAISSE_EXACT": "FREX", "REVERSIBLE_LOCALIZERS": "REVLOC", "TOTAL_EXACT": "TOTEX", "TOTAL_EXACT_2": "TOTEX2",
    "PRESHEAF_TOTALITY": "PRETOT", "S6_BLIND_NIGHT": "S6_06_BLIND", "S6_PAPERS": "S6_09_PAPERS",
    "S6_PAPERS_LADDER": "S6_10_PAPERS", "TOTAL_ASPHERICITY": "TOTAL_ASPHERICITY", "FINMON_CP2": "FINMON_CP2",
    "LM1_GROUP_SCHEMES": "LM1_GROUP_SCHEMES_rerun_20261112",
}
BARE_DEFAULT = {"S6_02_PUSH": "S6_02_FAMILY", "ANABELIAN_A1_SUCCESSOR": "ANABELIAN_A1"}
LINE_OF_INV = "S6"
IDTOK = r"(?:[A-Z][A-Za-z0-9]{0,5}(?:\.[A-Za-z0-9]{1,5}){1,4}|[A-Z]{1,4}\d{1,4}[a-z]?)"
ID_RX = re.compile(r"(?<![A-Za-z0-9_.:/\\-])(" + IDTOK + r")(?:\s*[–-]\s*(" + IDTOK + r"|\d{1,4}))?(?![A-Za-z0-9])")
S6LAB_RX = re.compile(r"(?<![A-Za-z0-9_])((?:inv|fam|push|cdp|maps|mapsI{1,3}|mapsaudit|ari|night|ii|iii|iv|v|vi|i|wb|"
                      r"cg|corr|repair|course|sup)[A-Za-z]*:[A-Za-z0-9:._\-]*[A-Za-z0-9])")
STATUS_KEYS = ("Proved", "Refuted", "Known", "Open", "Conditional", "Unresolved")


def norm_status(s):
    s = (s or "").strip()
    if not s:
        return "?"
    low = s.lower()
    if low.startswith("historical record:"):  # S6_10 rows carried from the compendium: the recorded status
        rest = low.split(":", 1)[1].strip()
        if rest.startswith(("classical", "known")):
            return "Known"
        if rest.startswith(("refuted", "false")):
            return "Refuted"
        if rest.startswith("open"):
            return "Open"
        return "Proved"
    if low.startswith("current scoped check") or low.startswith("proved") or low.startswith("verified") \
            or low.startswith("computed"):
        return "Proved"
    w = s.split()[0].strip(".,;:()")
    syn = {"false": "Refuted", "undecided": "Open", "verified": "Proved", "computed": "Proved", "disproved": "Refuted"}
    if w.lower() in syn:
        return syn[w.lower()]
    return next((k for k in STATUS_KEYS if w.lower().startswith(k.lower())), w[:20])


def norm_text(s):
    s = re.sub(r"\\[a-zA-Z]+\*?", " ", s or "")
    s = re.sub(r"[^0-9a-zA-Z]+", " ", s).lower()
    return re.sub(r"\s+", " ", s).strip()


STOP = set("the and for with that this are from its which over every each into not one two all has have any".split())


def toks(s):
    return {w for w in norm_text(s).split() if len(w) >= 4 and w not in STOP}


def one_line(s, n=None):
    s = re.sub(r"\s+", " ", (s or "").replace("\t", " ")).strip()
    return s if n is None else s[:n]


def nice_stamp(st):
    m = re.match(r"(\d{4})(\d\d)(\d\d)T(\d\d)(\d\d)Z", st or "")
    return f"{m.group(1)}-{m.group(2)}-{m.group(3)} {m.group(4)}:{m.group(5)}" if m else (st or "")


def date_of(st):
    """normalized date string YYYY-MM-DD (or YYYY-MM-DD HH:MM) from a stamp or a free date."""
    if not st:
        return ""
    m = re.match(r"(\d{4})(\d\d)(\d\d)T(\d\d)(\d\d)Z", st)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)} {m.group(4)}:{m.group(5)}"
    m = re.search(r"(20\d\d)-(\d\d)-(\d\d)(?:[ T](\d\d):(\d\d))?", st)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}" + (f" {m.group(4)}:{m.group(5)}" if m.group(4) else "")
    m = re.search(r"(\d{1,2}) (Nov|November|Oct|October) (2026)", st)
    if m:
        return f"2026-{'11' if m.group(2).startswith('N') else '10'}-{int(m.group(1)):02d}"
    return ""


def mtime_stamp(p):
    return datetime.datetime.fromtimestamp(p.stat().st_mtime, datetime.timezone.utc).strftime("%Y%m%dT%H%MZ")


def who_model(w, fallback=ASTRA):
    """model and effort from a who string."""
    w = w or ""
    m = re.search(r"\b(Fable|Opus|Sonnet)\s*\)?\s*(\d\.\d)", w)
    if "claude" in w.lower() or m:
        if not m:
            return "Claude (model not named in this record)"
        e = re.search(r"effort[\s:=]*\"?(max|xhigh|high|medium|low)", w, re.I)
        e2 = re.search(r"session's default effort[^)]*\)?", w)
        if e:
            return f"Claude {m.group(1)} {m.group(2)} at effort {e.group(1).lower()}"
        if e2:
            return f"Claude {m.group(1)} {m.group(2)} at the session's default effort (none set at launch)"
        return f"Claude {m.group(1)} {m.group(2)}"
    if re.search(r"astra|gpt-6|chatgpt|openai", w, re.I):
        return ASTRA
    return fallback


# ------------------------------------------------------------------------------------------------ 1. the register
register = {}
with open(REG / "REGISTER.tsv", encoding="utf-8", newline="") as fh:
    for r in csv.DictReader(fh, delimiter="\t"):
        register[r["tag"]] = r
print(f"register: {len(register)} rows")
LINE_OF_RUN = {r["run"]: r["line"] for r in register.values()}

# ------------------------------------------------------------------------------------------------ 2. snapshots
REPOS = [("grothendieck-longue-marche", "raw/pro_returns", "Longue Marche / archive"),
         ("grothendieck-derivateurs", "raw/pro_returns", "Derivateurs"),
         ("grothendieck-derivateurs", "pro_returns", "Derivateurs"),
         ("s6-complex-structure-workbench", "pro_returns", "S6")]
SKIP_PREFIX = ("MPL_", "SP0", "SP1", "SP2", "SP3", "CTRL", "P0", "P1")


def canon_run(run):
    run = re.sub(r"^\d+_", "", run)
    return ALIAS.get(run, run) if run in ("FRAISSE_EXACT", "REVERSIBLE_LOCALIZERS", "TOTAL_EXACT", "TOTAL_EXACT_2",
                                           "PRESHEAF_TOTALITY", "S6_BLIND_NIGHT") else run


snap_specs = []  # (run, kind, num, stamp, kind_of_source, path or (zip, member), programme)
seen_dirs = set()


def add_folder(d, prog, src):
    if d in seen_dirs or not d.is_dir():
        return
    seen_dirs.add(d)
    run, kind, num, st = B.parse_return(d)
    if run.endswith("_checkpoint"):
        run, kind = run[: -len("_checkpoint")], "checkpoint"
    run = canon_run(run)
    snap_specs.append(dict(run=run, kind=kind, num=num, stamp=st or mtime_stamp(d), src=src, folder=d, prog=prog))
    # earlier checkpoints carried into this one
    ef = d / "_from_earlier_checkpoints"
    if ef.is_dir():
        for g in sorted(ef.iterdir()):
            if g.is_dir():
                add_folder(g, prog, src + " (carried earlier checkpoint)")
    for sub in (d, *[x for x in d.iterdir() if x.is_dir() and not x.name.startswith("_")]):
        ret = sub / "retained"
        if ret.is_dir():
            for g in sorted(ret.glob("checkpoint_*")):
                m = re.match(r"checkpoint_(\d+)", g.name)
                if g.is_dir() and m:
                    seen_dirs.add(g)
                    snap_specs.append(dict(run=run, kind="checkpoint", num=int(m.group(1)), stamp="",
                                           src=src + " (retained checkpoint)", folder=g, prog=prog))


for r in B.find_returns():
    add_folder(DOC / r["folder"], r["programme"], "working copy")
for repo, sub, prog in REPOS:
    base = GB / repo / sub
    if base.is_dir():
        for d in sorted(base.iterdir()):
            if d.is_dir() and not d.name.startswith(SKIP_PREFIX):
                add_folder(d, prog, f"github_backup_20261113/{repo}")
# the first LM1 run (folder without a return suffix) and zips holding a main results table
lm1 = DOC / "longue_marche_pro_pilot_20261104" / "answers" / "LM1_GROUP_SCHEMES"
if lm1.is_dir():
    seen_dirs.add(lm1)
    snap_specs.append(dict(run="LM1_GROUP_SCHEMES_first", kind="return", num=None, stamp=mtime_stamp(lm1),
                           src="working copy (first LM1 run)", folder=lm1, prog="Longue Marche / archive"))
for zp in sorted((DOC / "longue_marche_pro_pilot_20261104" / "answers").glob("*.zip")) + \
        sorted((S6W / "returns").glob("*.zip")):
    fake = zp.with_suffix("")
    run, kind, num, st = B.parse_return(fake)
    if run.endswith("_checkpoint"):
        run, kind = run[: -len("_checkpoint")], "checkpoint"
    snap_specs.append(dict(run=run, kind=kind, num=num, stamp=st or mtime_stamp(zp), src="zip " + zp.name,
                           folder=None, zip=zp, prog=""))


def read_results_csv_text(text):
    rows = []
    rd = csv.DictReader(text.splitlines())
    for row in rd:
        rid = (row.get("id") or "").strip()
        if rid:
            rows.append(row)
    return rows, rd.fieldnames or []


snapshots = []  # dicts: run, kind, num, stamp, src, folder, rows(list of dict), fields, hash
by_hash = {}
for sp in snap_specs:
    text = None
    if sp.get("zip"):
        try:
            z = zipfile.ZipFile(sp["zip"])
            mem = [i for i in z.infolist() if i.filename.rsplit("/", 1)[-1] == f"{sp['run']}_results.csv"]
            if not mem:
                continue
            mem.sort(key=lambda i: i.filename.count("/"))
            text = z.read(mem[0]).decode("utf-8-sig", errors="replace")
        except Exception:
            continue
        resname = f"{sp['zip'].name}!{mem[0].filename}"
    else:
        f = B.results_in(sp["folder"])
        if sp["src"].endswith("(retained checkpoint)"):
            cands = sorted(sp["folder"].glob("*_results.csv"))
            f = cands[0] if cands else None
        if not f:
            continue
        try:
            text = f.read_text(encoding="utf-8-sig", errors="replace")
        except OSError:
            continue
        resname = f.relative_to(DOC).as_posix()
    h = hashlib.sha1(text.encode("utf-8", errors="replace")).hexdigest()
    key = (sp["run"], h)
    if key in by_hash:  # the same table filed twice (working copy and backup): keep the better-labelled one
        o = by_hash[key]
        if (o["num"] is None and sp["num"] is not None) or (not o["stamp"] and sp["stamp"]):
            o.update(kind=sp["kind"], num=sp["num"], stamp=sp["stamp"] or o["stamp"])
        o["also"].append(sp["src"])
        continue
    rows, fields = read_results_csv_text(text)
    if not rows:
        continue
    s = dict(sp, rows=rows, fields=fields, hash=h, results=resname, also=[])
    snapshots.append(s)
    by_hash[key] = s


def snap_order(s):
    return (s["stamp"] or "", s["num"] or 0, 1 if s["kind"] == "final" else 0)


snaps_by_run = collections.defaultdict(list)
for s in snapshots:
    snaps_by_run[s["run"]].append(s)
for run, ss in snaps_by_run.items():
    # retained checkpoints have no stamp: place them by number before the stamped ones of the same run
    stamped = sorted([x for x in ss if x["stamp"]], key=snap_order)
    first = stamped[0]["stamp"] if stamped else ""
    for x in ss:
        if not x["stamp"]:
            x["stamp_est"] = True
            x["stamp"] = first[:9] + f"00{(x['num'] or 0):02d}Z" if first else ""
    ss.sort(key=lambda x: (x["stamp"], x["num"] or 0, 1 if x["kind"] == "final" else 0))
print(f"snapshots: {len(snapshots)} results tables of {len(snaps_by_run)} runs")


def snap_label(s):
    lab = "final" if s["kind"] == "final" else (f"cp{s['num']:02d}" if s["num"] is not None else "return")
    return lab


# nodes
nodes = {}  # tag -> dict


def node(tag, run, rid, line):
    if tag not in nodes:
        nodes[tag] = dict(tag=tag, run=run, id=rid, line=line, hist=[], statement="", status="?", first="", last="",
                          revisions=0, in_register=tag in register, raw=None, kind="row")
    return nodes[tag]


ids_by_run = collections.defaultdict(set)
newest_raw = {}  # run -> newest snapshot
for run, ss in snaps_by_run.items():
    line = LINE_OF_RUN.get(run) or next((x["prog"] for x in ss if x["prog"]), "") or \
        ("S6" if run.startswith(("S6_", "Q03")) else "")
    for s in ss:
        seen = collections.Counter()
        for row in s["rows"]:
            rid = row["id"].strip()
            seen[rid] += 1
            key = rid if seen[rid] == 1 else f"{rid}#{seen[rid]}"
            tag = f"{run}:{key}"
            n = node(tag, run, key, line)
            st = norm_status(row.get("status"))
            sh = norm_text(row.get("statement"))[:4000]
            if n["hist"] and n["hist"][-1]["sh"] and sh and n["hist"][-1]["sh"] != sh:
                old = toks(n["hist"][-1]["text"])
                new = toks(row.get("statement") or "")
                if old and new and len(old & new) / max(1, len(old | new)) < 0.9:
                    n["revisions"] += 1
            n["hist"].append(dict(stamp=s["stamp"], label=snap_label(s), status=st, sh=sh,
                                  text=one_line(row.get("statement"), 600), est=s.get("stamp_est", False)))
            n["statement"] = one_line(row.get("statement"))
            n["status"] = st
            n["raw"] = row
            ids_by_run[run].add(key)
    newest_raw[run] = ss[-1]
for t, n in nodes.items():
    n["first"] = n["hist"][0]["stamp"] if n["hist"] else ""
    n["last"] = n["hist"][-1]["stamp"] if n["hist"] else ""
    nr = newest_raw.get(n["run"])
    if nr and n["hist"] and n["hist"][-1]["stamp"] < nr["stamp"]:
        n["dropped"] = f"absent from the newest table ({snap_label(nr)}); last {n['hist'][-1]['label']} {n['status']}"
missing_reg = [t for t in register if t not in nodes]
for t in missing_reg:  # register rows whose table this script could not reread: take them from the register
    r = register[t]
    n = node(t, r["run"], r["id"], r["line"])
    n["status"] = r["status"]
    n["statement"] = r["statement"]
    n["first"] = n["last"] = r["stamp"]
    n["hist"].append(dict(stamp=r["stamp"], label=r["ret_kind"] + (str(r["ret_num"]) if r["ret_num"] else ""),
                          status=r["status"], sh=norm_text(r["statement"]), text=r["statement"][:600], est=False))
    ids_by_run[r["run"]].add(r["id"])
print(f"nodes from results tables: {len(nodes)}; register rows not reread: {len(missing_reg)}")

RUN_FIRST = {run: ss[0]["stamp"] for run, ss in snaps_by_run.items()}
RUN_LAST = {run: ss[-1]["stamp"] for run, ss in snaps_by_run.items()}

# ------------------------------------------------------------------------------------------------ 3. events
events = []  # dict(node, kind, sub, who, actor, date, source, detail)
EV_SEEN = set()


def add_event(tag, kind, who, actor, date, source, detail, sub="", dedupe=None):
    if tag not in nodes:
        return False
    key = dedupe or (tag, kind, actor, date[:10], norm_text(detail)[:160], source)
    if key in EV_SEEN:
        return False
    EV_SEEN.add(key)
    events.append(dict(node=tag, kind=kind, sub=sub, who=who, actor=actor, date=date, source=source,
                       detail=one_line(detail, 300)))
    return True


def type_norm(t):
    s = (t or "").strip().lower()
    if s in ("d",):
        return "T1"
    if s == "c":
        return "T3"
    if s == "s":
        return "T4"
    if s == "r" or s.startswith("refuted") or "refuted, with" in s:
        return "T7"
    if s == "e" or "editorial" in s or "alias" in s or "scope-record" in s or "a-identity" in s \
            or "audit boundary" in s or "correction in this run" in s or s.startswith("count of register"):
        return "EDIT"
    if "used and rechecked" in s or "checked in use" in s:
        return "T4"
    if "carried as background" in s:
        return "T5"
    if re.search(r"re-?proof|re-?derivation|new (complete |uniform )?proof|peer recheck|second re-proof|blind", s):
        return "T2"
    if re.search(r"proof read|proof reading|second reading|full proof|complete proof|proof check|reread|re-read", s):
        return "T1"
    if re.search(r"comput|certificate|replay|finite-field verification|executable|program", s):
        return "T3"
    if "source" in s or "literature" in s or "credit" in s:
        return "SRC"
    if re.search(r"check|review|reading|verif|audit", s):
        return "T1"
    return "OTHER"


INV10 = {}  # label -> inventory row (S6_10)
INV9 = {}   # printed_label -> row (S6_09)
s6_10_dir = None
for s in sorted(snaps_by_run.get("S6_10_PAPERS", []), key=snap_order):
    pass
cands10 = sorted((S6W / "returns").glob("S6_10_PAPERS_*_unzipped"))
for d in cands10:
    f = d / "S6_10_PAPERS" / "S6_10_PAPERS_inventory.csv"
    if f.exists():
        s6_10_dir = d / "S6_10_PAPERS"
cands9 = sorted((S6W / "returns").glob("S6_09_PAPERS_final_*_unzipped"))
s6_09_inv = (cands9[-1] / "S6_09_PAPERS_inventory.csv") if cands9 else None


def resolve_s6_label(lab):
    if lab in INV10:
        return f"S6_10_PAPERS:{lab}"
    if lab in INV9:
        return f"S6_09_PAPERS:{lab}"
    return None


# 3a. the S6 inventories as nodes (their rows re-state the source rows, in paper form)
same_edges = []  # (a, b, why)
if s6_09_inv and s6_09_inv.exists():
    st9 = s6_09_inv.parent.name
    m9 = re.search(r"(20\d{6}T\d{4}Z)", st9)
    for r in csv.DictReader(open(s6_09_inv, encoding="utf-8-sig", newline="")):
        lab = r["printed_label"].strip()
        if not lab:
            continue
        INV9[lab] = r
        t = f"S6_09_PAPERS:{lab}"
        n = node(t, "S6_09_PAPERS", lab, "S6")
        n["kind"] = "inventory"
        n["statement"] = one_line(r.get("statement_as_printed"), 600)
        n["first"] = n["last"] = m9.group(1) if m9 else ""
        src = f"{r['source_run']}:{r['source_id'].strip()}"
        oc = (r.get("check_outcome") or "").lower()
        # S6_09 has no status column: its check_outcome says how its writing check went, so the status is the
        # source row's, unless the writing check refuted it
        if re.search(r"refut|\bfalse\b|counterexample", oc):
            n["status"] = "Refuted"
        elif src in nodes:
            n["status"] = nodes[src]["status"]
        elif re.search(r"known|classical", (r.get("kind") or "").lower() + " " + (r.get("credited_to") or "").lower()[:80]):
            n["status"] = "Known"
        else:
            n["status"] = "Proved"
        n["hist"].append(dict(stamp=n["first"], label="final", status=n["status"], sh="", text="", est=False))
        if src in nodes:
            same_edges.append((t, src, "S6_09 inventory source row"))
if s6_10_dir:
    m10 = re.search(r"(20\d{6}T\d{4}Z)", s6_10_dir.parent.name)
    st10 = m10.group(1) if m10 else ""
    for r in csv.DictReader(open(s6_10_dir / "S6_10_PAPERS_inventory.csv", encoding="utf-8-sig", newline="")):
        lab = r["label"].strip()
        INV10[lab] = r
        t = f"S6_10_PAPERS:{lab}"
        n = node(t, "S6_10_PAPERS", lab, "S6")
        n["kind"] = "inventory"
        try:
            notes = json.loads(r["notes"]) if r["notes"].strip().startswith("{") else {}
        except Exception:
            notes = {}
        n["statement"] = one_line(notes.get("source_statement") or "", 600)
        n["status"] = norm_status(r["status"])
        n["first"] = n["last"] = st10
        n["printed"] = not r["in_compendium_only_because"].strip()
        n["main"] = r["main_or_supporting"].strip().lower().startswith("main")
        n["paper"] = r["paper"]
        n["credit_pending"] = "comparison pending" in r["credited_to"]
        n["hist"].append(dict(stamp=st10, label=s6_10_dir.parent.name.split("_unzipped")[0][-28:], status=n["status"],
                              sh="", text="", est=False))
        src = f"{r['source_run']}:{r['source_id'].strip()}"
        if src in nodes:
            same_edges.append((t, src, "S6_10 inventory source row"))
        if r.get("s6_09_label", "").strip() and f"S6_09_PAPERS:{r['s6_09_label'].strip()}" in nodes:
            same_edges.append((t, f"S6_09_PAPERS:{r['s6_09_label'].strip()}", "S6_10 inventory s6_09_label"))
print(f"S6 inventories: S6_09 {len(INV9)} rows, S6_10 {len(INV10)} rows")

# 3b. CHECK_EVENTS-like files in every snapshot folder
EV_DIR_SKIP = {"build", "history", "sources", "literature", "papers", "node_modules", ".git", "data", "images",
               "verification_images", "_from_earlier_checkpoints", "retained", "tex", "pdf", "research", "evidence"}
EV_NAME = re.compile(r"(check_?events|_events\.tsv$|checks\.tsv$|check_coverage|current_check_events)", re.I)


def walk_files(d, depth, pred, skip=EV_DIR_SKIP, k=0, out=None):
    out = [] if out is None else out
    if k > depth:
        return out
    try:
        items = list(d.iterdir())
    except OSError:
        return out
    for p in items:
        if p.is_dir():
            if p.name not in skip:
                walk_files(p, depth, pred, skip, k + 1, out)
        elif p.is_file() and pred(p):
            out.append(p)
    return out


def ref_tag(run, sid):
    """resolve a statement id written in a run's own file to a node tag."""
    sid = (sid or "").strip().strip("`*")
    if not sid:
        return None
    if run == "S6_10_PAPERS" or ":" in sid:
        t = resolve_s6_label(sid)
        if t:
            return t
    if f"{run}:{sid}" in nodes:
        return f"{run}:{sid}"
    m = re.match(r"([A-Z][A-Z0-9_]+)[\s:]+(" + IDTOK + r")", sid)
    if m:
        r2 = ALIAS.get(m.group(1), m.group(1))
        if f"{r2}:{m.group(2)}" in nodes:
            return f"{r2}:{m.group(2)}"
    m = re.match(r"(" + IDTOK + r")", sid)
    if m and f"{run}:{m.group(1)}" in nodes:
        return f"{run}:{m.group(1)}"
    return None


ev_files = 0
deferred_ev = []
unresolved_ev = collections.Counter()
unresolved_samples = collections.defaultdict(list)
for s in snapshots:
    if not s.get("folder") or s["src"].endswith("(retained checkpoint)"):
        continue
    files = walk_files(s["folder"], 5, lambda p: p.suffix.lower() == ".tsv" and EV_NAME.search(p.name))
    for f in files:
        try:
            rows = list(csv.reader(open(f, encoding="utf-8-sig", newline=""), delimiter="\t"))
        except Exception:
            continue
        if not rows:
            continue
        hl = [h.strip().lower() for h in rows[0]]
        i_id = next((i for i, h in enumerate(hl) if h in ("statement_id", "statement", "target_id", "label", "id")), None)
        i_ty = next((i for i, h in enumerate(hl) if h.startswith("type") or h == "method"), None)
        if i_id is None or i_ty is None:
            continue
        i_dt = next((i for i, h in enumerate(hl) if h == "date"), None)
        i_who = next((i for i, h in enumerate(hl) if h in ("who", "checker", "reader")), None)
        i_out = next((i for i, h in enumerate(hl) if h in ("outcome", "exact_scope", "scope")), None)
        ev_files += 1
        rel = f.relative_to(DOC).as_posix()
        for row in rows[1:]:
            if len(row) <= max(i_id, i_ty):
                continue
            tag = ref_tag(s["run"], row[i_id])
            if not tag:
                deferred_ev.append((s, f, row, i_id, i_ty, i_dt, i_who, i_out))
                unresolved_ev[s["run"]] += 1
                if len(unresolved_samples[s["run"]]) < 6:
                    unresolved_samples[s["run"]].append(row[i_id][:60] + " @ " + f.name)
                continue
            ty = type_norm(row[i_ty])
            who = row[i_who] if i_who is not None and len(row) > i_who else ASTRA
            date = date_of(row[i_dt]) if i_dt is not None and len(row) > i_dt else date_of(s["stamp"])
            outc = row[i_out] if i_out is not None and len(row) > i_out else ""
            add_event(tag, ty, who_model(who), s["run"], date or date_of(s["stamp"]), rel,
                      f"{row[i_ty].strip()}: {outc}", sub="run CHECK_EVENTS",
                      dedupe=(tag, ty, norm_text(who)[:40], (date or "")[:10], norm_text(outc)[:200]))
print(f"check-event files read: {ev_files}; events so far: {len(events)}; unresolved ids: {sum(unresolved_ev.values())}")
for r_, v_ in unresolved_samples.items():
    print("   unresolved", r_, unresolved_ev[r_], v_)

# 3c. the S6_10 inventory's check_record JSON (current events, S6_09 writing checks, the ledger of our reviews)
S6_DOC_EVENTS = []  # (tag, doc key, who, date, verb, detail) to be merged with the document scan
if s6_10_dir:
    for lab, r in INV10.items():
        t = f"S6_10_PAPERS:{lab}"
        try:
            cr = json.loads(r["check_record"])
        except Exception:
            continue
        for e in cr.get("current_writing_events") or []:
            raw = e.get("raw_event") or {}
            outc = raw.get("outcome") or e.get("scope") or ""
            ty = type_norm(raw.get("type") or e.get("type"))
            who = raw.get("who") or e.get("who") or ASTRA
            add_event(t, ty, who_model(who), "S6_10_PAPERS", date_of(raw.get("date") or e.get("date") or "2026-11-18"),
                      f"{s6_10_dir.relative_to(DOC).as_posix()}/{e.get('source') or 'inventory'}",
                      f"{raw.get('type') or e.get('type')}: {outc}", sub="S6_10 inventory event",
                      dedupe=(t, ty, norm_text(who)[:40], date_of(raw.get("date") or "2026-11-18")[:10],
                              norm_text(outc)[:200]))
        wc = cr.get("s6_09_writing_check")
        if isinstance(wc, (dict, list)):
            wc = json.dumps(wc, ensure_ascii=False)
        if isinstance(wc, str) and wc.strip():
            # the field comes in several forms (text, JSON objects, JSON lists): read it as text
            txt = wc
            if wc.strip()[:1] in "{[":
                try:
                    obj = json.loads(wc)
                    obj = obj if isinstance(obj, list) else [obj]
                    txt = " ".join(" ".join(str(v) for v in (o.values() if isinstance(o, dict) else [o])) for o in obj)
                except Exception:
                    pass
            if re.search(r"pending|not (?:read|checked|re-?derived|reread)|no proof", txt[:400], re.I) and \
                    not re.search(r"full|complete|whole|entire", txt[:400], re.I):
                ty = "OTHER"
            elif re.search(r"full|complete|whole|entire|re-?derived|followed|read", txt, re.I):
                ty = "T1"
            else:
                ty = type_norm(txt[:200])
            d0 = date_of(txt) or "2026-11-17"
            add_event(t, ty, ASTRA, "S6_09_PAPERS", d0,
                      "S6_09_PAPERS inventory (writing check, as carried in the S6_10 inventory)",
                      f"S6_09 writing check: {one_line(txt, 260)}", sub="S6_09 writing check")
        rc = cr.get("s6_09_recorded_checks")
        if isinstance(rc, str):
            for part in rc.split(" | "):
                part = part.strip()
                if part.startswith("["):
                    try:
                        for c in json.loads(part):
                            S6_DOC_EVENTS.append((t, c.get("locator", ""), f"{c.get('reviewer', '')} effort {c.get('effort', '')}",
                                                  date_of(c.get("date", "")), "checked in",
                                                  f"{c.get('scope', '')}; {c.get('outcome', '')}"))
                    except Exception:
                        pass
        led = cr.get("ledger") or ""
        for part in str(led).split(" || "):
            m = re.match(r"(checked in|discussed in) (\S+\.md) \(([^,]+), (\d{4}-\d\d-\d\d)\)", part.strip())
            if m:
                S6_DOC_EVENTS.append((t, m.group(2), m.group(3), m.group(4), m.group(1), "named in the S6 check ledger"))
print(f"events after the S6_10 inventory: {len(events)}; S6 ledger document entries: {len(S6_DOC_EVENTS)}")

# ------------------------------------------------------------------------------------------------ 4. cross-run edges
RUN_NAMES = sorted(set(list(snaps_by_run) + list(ALIAS)), key=len, reverse=True)
RUN_RX = re.compile(r"(?<![A-Za-z0-9_])(" + "|".join(re.escape(n) for n in RUN_NAMES) + r")(?![A-Za-z0-9_])")


def canon(n):
    return ALIAS.get(n, n)


def expand(run, a, b):
    """ids of run from a to b (a range like E.59–E.73 or E.59–73)."""
    out = [a]
    if not b:
        return out
    ma = re.match(r"(.*?)(\d+)$", a)
    mb = re.match(r"(.*?)(\d+)$", b)
    if not ma or not mb:
        return out + [b]
    pa, na = ma.group(1), int(ma.group(2))
    pb, nb = (mb.group(1) or pa), int(mb.group(2))
    if pb != pa or nb <= na or nb - na > 60:
        return out + [b]
    return [f"{pa}{k}" for k in range(na, nb + 1)]


def refs_in(text, default_run=None, valid_only=True):
    """[(run, id)] named in a text: an id counts for the nearest run name before it in the text (or default_run)."""
    out = []
    if not text:
        return out
    marks = [(m.start(), m.end(), "run", canon(m.group(1))) for m in RUN_RX.finditer(text)]
    marks += [(m.start(), m.end(), "id", (m.group(1), m.group(2))) for m in ID_RX.finditer(text)]
    marks.sort()
    cur = default_run
    last_end = -1
    for st, en, kind, val in marks:
        if st < last_end:
            continue
        if kind == "run":
            cur = val
            last_end = en
            continue
        if not cur:
            continue
        for x in expand(cur, val[0], val[1]):
            if not valid_only or x in ids_by_run.get(cur, ()):
                out.append((cur, x))
        last_end = en
    return out


NUMERIC_RUNS = {r for r, ids in ids_by_run.items() if ids and sum(1 for x in ids if re.fullmatch(r"\d+(?:\.\d+)+", x)) > len(ids) / 2}


def refs_pos(text, default_run=None):
    """like refs_in, with the position of each id: [(run, id, start, end)]."""
    out = []
    marks = [(m.start(), m.end(), "run", canon(m.group(1))) for m in RUN_RX.finditer(text)]
    marks += [(m.start(), m.end(), "id", (m.group(1), m.group(2))) for m in ID_RX.finditer(text)]
    marks.sort()
    cur, last_end = default_run, -1
    for st, en, kind, val in marks:
        if st < last_end:
            continue
        if kind == "run":
            cur, last_end = val, en
            continue
        if cur:
            for x in expand(cur, val[0], val[1]):
                if x in ids_by_run.get(cur, ()):
                    out.append((cur, x, st, en))
        last_end = en
    return out


cross = []  # (from tag, to tag, kind, verdict, column)
own_prompt_checks = []  # (from tag, prompt run, item label, verdict, column)
for run, s in newest_raw.items():
    for row in s["rows"]:
        tag = f"{run}:{row['id'].strip()}"
        if tag not in nodes:
            continue
        for col, val in row.items():
            if not col or not val:
                continue
            c = col.lower()
            if c in ("id", "status"):
                continue
            if c.startswith("checks"):
                # "RUN ID: confirmed" etc.
                for m in re.finditer(r"([A-Z][A-Z0-9_]+)[\s:-]+(" + IDTOK + r")(?:\s*[–-]\s*(" + IDTOK + r"))?"
                                     r"[^;|]{0,90}?\b(confirmed|repaired|refuted|corrected|refined|scope compared)", val):
                    r2 = canon(m.group(1))
                    if r2.endswith("_PROMPT"):  # an R-item of the run's own prompt: resolved once the prompts are read
                        own_prompt_checks.append((tag, r2[: -len("_PROMPT")], m.group(2), m.group(4), col))
                        continue
                    for x in expand(r2, m.group(2), m.group(3)):
                        if f"{r2}:{x}" in nodes and r2 != run:
                            cross.append((tag, f"{r2}:{x}", "checks", m.group(4), col))
                continue
            if c.startswith("stated_value_compared"):
                agree = (row.get("agrees_with_stated_value") or "").strip()
                for r2, x in refs_in(val):
                    m2 = re.search(re.escape(f"{x}") + r"\s*:\s*([a-z][^;]{0,40})", agree)
                    verdict = (m2.group(1) if m2 else agree)[:60] or "compared"
                    cross.append((tag, f"{r2}:{x}", "blind", verdict, col))
                continue
            if c.startswith("a1_id"):
                x = val.strip()
                if f"ANABELIAN_A1:{x}" in nodes:
                    same_edges.append((tag, f"ANABELIAN_A1:{x}", "A1_id column (carried row)"))
                continue
            for r2, x in refs_in(val):
                if r2 == run or f"{r2}:{x}" not in nodes:
                    continue
                kind = "uses" if c.startswith("depends_on") else "names"
                cross.append((tag, f"{r2}:{x}", kind, "", col))
print(f"cross-run references from rows: {len(cross)}; same-claim edges so far: {len(same_edges)}")

# 4b. prompts: R-items, tasks, leads; the "checked where you use them" clause
PROMPT_ROOTS = [DOC / "longue_marche_pro_pilot_20261104" / "pro_prompts_draft_20261111" / "ALREADY_RAN",
                DOC / "longue_marche_pro_pilot_20261104" / "pro_prompts_draft_20261111",
                DOC / "grothendieck_archive_montpellier" / "pro_prompts_archive_20261112" / "ALREADY_RAN",
                DOC / "derivateurs_companion_20261109" / "pro_prompts_max_20261112" / "ALREADY_RAN",
                DOC / "derivateurs_companion_20261109" / "pro_prompts_20261110" / "ALREADY_RAN",
                DOC / "s6_pro_prompts_20261112" / "ALREADY_RAN", DOC / "s6_pro_prompts_20261112_sent"]
prompt_of = {}
for root in PROMPT_ROOTS:
    if not root.is_dir():
        continue
    for d in sorted(root.iterdir()):
        p = d / "PROMPT.md"
        if not d.is_dir() or not p.exists():
            continue
        name = re.sub(r"^\d+_", "", d.name)
        run = PROMPT_DIR_RUN.get(name, name)
        if run not in snaps_by_run and run + "_rerun_20261112" in snaps_by_run:
            run = run + "_rerun_20261112"
        if run in snaps_by_run and run not in prompt_of:
            prompt_of[run] = p
ITEM_LINE = re.compile(r"^\s*[-*]\s*\*\*\s*(R\d+|L\d+|Lead\s*\d+|Task\s+[A-H]\.\d+|[A-H]\d{1,2}|[A-H]\.\d{1,2})\b[^*]*\*\*")
CLAUSE = re.compile(r"checked where (?:you|they are) use|checked step by step where used|check(?:ed)? (?:them )?where (?:you )?use|"
                    r"checked while (?:you )?(?:use|using)|check[- ]while[- ]working", re.I)
prompt_items = {}  # run -> {label: [(tag, rkind)]}
prompt_clause = {}
prompt_header = {}
for run, p in prompt_of.items():
    text = p.read_text(encoding="utf-8", errors="replace")
    prompt_clause[run] = bool(CLAUSE.search(text))
    prompt_header[run] = one_line(" ".join(text.splitlines()[:6]), 300)
    items = {}
    cur, buf = None, []

    def flush():
        if cur:
            refs = refs_in(" ".join(buf), default_run=None)
            if cur.startswith("R") and run in BARE_DEFAULT:
                refs += refs_in(" ".join(buf)[:400], default_run=BARE_DEFAULT[run])
            items.setdefault(cur, [])
            for r2, x in refs:
                if r2 != run and (f"{r2}:{x}", r2) not in items[cur]:
                    items[cur].append((f"{r2}:{x}", r2))
    for ln in text.splitlines():
        m = ITEM_LINE.match(ln)
        if m or ln.startswith("#"):
            flush()
            cur = re.sub(r"\s+", " ", m.group(1)).replace("Lead ", "L").replace("Lead", "L") if m else None
            buf = [ln] if m else []
        elif cur:
            buf.append(ln)
    flush()
    prompt_items[run] = {k: v for k, v in items.items() if v}
for fr, prun, lab, verdict, col in own_prompt_checks:
    for t2, r2 in prompt_items.get(prun, {}).get(lab, []):
        cross.append((fr, t2, "checks", verdict, f"{col} (prompt item {lab})"))
n_items = sum(len(v) for v in prompt_items.values())
# check events whose id field names another run's row or a prompt item (R12, R9/GALOIS A.1-A.2)
late_ok = 0
for s_, f_, row, i_id, i_ty, i_dt, i_who, i_out in deferred_ev:
    sid = row[i_id]
    tags = [f"{a}:{b}" for a, b in refs_in(sid)]
    for m in re.finditer(r"\b(R\d+)\b", sid):
        tags += [t2 for t2, r2 in prompt_items.get(s_["run"], {}).get(m.group(1), [])]
    for tag in dict.fromkeys(tags):
        ty = type_norm(row[i_ty])
        who = row[i_who] if i_who is not None and len(row) > i_who else ASTRA
        date = date_of(row[i_dt]) if i_dt is not None and len(row) > i_dt else date_of(s_["stamp"])
        outc = row[i_out] if i_out is not None and len(row) > i_out else ""
        ty2 = "T4" if ty in ("T1", "T4") and nodes.get(tag, {}).get("run") != s_["run"] else ty
        if add_event(tag, ty2, who_model(who), s_["run"], date or date_of(s_["stamp"]), f_.relative_to(DOC).as_posix(),
                     f"{row[i_ty].strip()} (input {sid.strip()[:40]}): {outc}", sub="run CHECK_EVENTS (input of the run)"):
            late_ok += 1
print(f"check events resolved through prompt items and other runs' ids: {late_ok}")
print(f"prompts read: {len(prompt_of)}; items naming earlier rows: {n_items}; "
      f"with the check-where-used clause: {sum(prompt_clause.values())}")

ANS_COLS = ("answers", "item_of_the_prompt", "r_items", "checks", "depends_on", "where_proved", "notes")
ITEM_REF = re.compile(r"(?<![A-Za-z0-9.])(R\d+|L\d+|Lead\s*\d+|Task\s+[A-H]\.\d+|[A-H]\d{1,2}|[A-H]\.\d{1,2})(?![0-9.])")
prompt_links = []  # (from tag, to tag, item label, item kind)
for run, items in prompt_items.items():
    s = newest_raw.get(run)
    if not s:
        continue
    for row in s["rows"]:
        tag = f"{run}:{row['id'].strip()}"
        labs = set()
        for col, val in row.items():
            if not col or not val:
                continue
            c = col.lower()
            if not c.startswith(ANS_COLS):
                continue
            for m in ITEM_REF.finditer(val):
                lab = re.sub(r"\s+", " ", m.group(1)).replace("Lead ", "L").replace("Lead", "L")
                if c.startswith(("answers", "item_of", "r_items", "checks")) or lab.startswith("R"):
                    labs.add(lab)
        for lab in labs:
            for t2, r2 in items.get(lab, []):
                prompt_links.append((tag, t2, lab, "R" if lab.startswith("R") else "task"))
    # items no row refers to: the prompt still restated them to the run (background)
    used = {(t2, lab) for (fr, t2, lab, k) in prompt_links if fr and fr.startswith(run + ":")}
    for lab, lst in items.items():
        for t2, r2 in lst:
            if (t2, lab) not in used:
                prompt_links.append((None, t2, lab, "background:" + run))
print(f"prompt links: {sum(1 for x in prompt_links if x[0])} row links, "
      f"{sum(1 for x in prompt_links if not x[0])} items restated without a row naming them")

# 4c. sweep 1 (Claude Opus 5.5 at effort max, four agents, 18 Nov): merges, when they exist, and their own check events
sweep_merges = 0
sweep_links = []  # (canonical, member, relation, reason, file)
for f in sorted(REG.glob("sweep1_*/MERGES.tsv")):
    try:
        rd = list(csv.reader(open(f, encoding="utf-8", newline=""), delimiter="\t"))
    except Exception:
        continue
    for row in rd[1:]:
        if len(row) < 3:
            continue
        a, b, rel = row[0].strip(), row[1].strip(), row[2].strip().lower()
        if a not in nodes or b not in nodes:
            continue
        if rel in ("same", "corrects"):
            same_edges.append((b, a, f"sweep 1 '{rel}' ({f.parent.name})"))
            sweep_merges += 1
        else:
            sweep_links.append((a, b, rel, row[3] if len(row) > 3 else "", f.relative_to(DOC).as_posix()))
print(f"sweep 1: {sweep_merges} lineage edges ('same', 'corrects'); {len(sweep_links)} other relations kept as links")

# 4d. identical statements across runs (the register's same_statement hash, recomputed on every node)
by_text = collections.defaultdict(list)
for t, n in nodes.items():
    k = norm_text(n["statement"])
    if len(k) >= 60:
        by_text[k].append(t)
for k, ts in by_text.items():
    if len({nodes[t]["run"] for t in ts}) > 1:
        for a in ts[1:]:
            same_edges.append((a, ts[0], "identical statement text"))

# 4e. probable restatements across runs (text overlap; heuristic, not merged)
tokset = {}
df = collections.Counter()
for t, n in nodes.items():
    if n["kind"] == "inventory":
        continue
    ts = toks(n["statement"])
    if len(ts) >= 12:
        tokset[t] = ts
        df.update(ts)
inv_index = collections.defaultdict(list)
for t, ts in tokset.items():
    rare = sorted(ts, key=lambda w: (df[w], w))[:10]
    for w in rare:
        if df[w] <= 40:
            inv_index[w].append(t)
pair_hits = collections.Counter()
for w, ts in inv_index.items():
    if len(ts) > 40:
        continue
    for i, a in enumerate(ts):
        for b in ts[i + 1:]:
            if nodes[a]["run"] != nodes[b]["run"]:
                pair_hits[(a, b) if a < b else (b, a)] += 1
restate = []
for (a, b), h in pair_hits.items():
    if h < 3:
        continue
    A, Bt = tokset[a], tokset[b]
    j = len(A & Bt) / len(A | Bt)
    if j >= 0.6:
        restate.append((a, b, round(j, 2)))
print(f"probable restatements across runs (Jaccard >= 0.6): {len(restate)}")

# ------------------------------------------------------------------------------------------------ 5. lineages
parent = {t: t for t in nodes}


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[ra] = rb


RANK = lambda why: (0 if ("inventory" in why or "A1_id" in why) else 1 if why == "identical statement text" else 2)
comp_runs = {t: collections.Counter([nodes[t]["run"]] if nodes[t]["kind"] == "row" else []) for t in nodes}
blocked = []
for a, b, why in sorted(same_edges, key=lambda e: RANK(e[2])):
    if a not in nodes or b not in nodes:
        continue
    ra, rb = find(a), find(b)
    if ra == rb:
        continue
    ca, cb = comp_runs[ra], comp_runs[rb]
    if any(ca[r] and cb[r] for r in cb):  # a lineage holds at most one row of each run
        blocked.append((a, b, why))
        continue
    parent[ra] = rb
    comp_runs[rb] = ca + cb
print(f"lineage edges blocked by the one-row-per-run rule: {len(blocked)}")
# a later run's row that checks an earlier one and confirms it restates the same claim
for fr, to, kind, verdict, col in cross:
    if kind == "checks" and verdict in ("confirmed",):
        pass  # kept as a check event, not merged: the checking row may state more than the checked one
members = collections.defaultdict(list)
for t in nodes:
    members[find(t)].append(t)


def origin_key(t):
    n = nodes[t]
    return (0 if n["kind"] == "row" else 1, n["first"] or "9", 0 if n["in_register"] else 1, t)


lineage_of = {}
lineages = {}
for root, ts in members.items():
    ts.sort(key=origin_key)
    canon_tag = ts[0]
    for t in ts:
        lineage_of[t] = canon_tag
    lineages[canon_tag] = ts
print(f"lineages: {len(lineages)} (from {len(nodes)} nodes)")


def lin(t):
    return lineage_of.get(t)


# ------------------------------------------------------------------------------------------------ 6. iteration events
def run_line(run):
    return LINE_OF_RUN.get(run) or ("S6" if run.startswith(("S6_", "Q03")) else "")


# 6a. a later run's row that checks an earlier statement, the blind comparisons, the carried rows
# one event per lineage, run and verdict: several rows of one run comparing with one claim are one iteration
grouped = collections.defaultdict(list)
for fr, to, kind, verdict, col in cross:
    if kind in ("checks", "blind"):
        v = verdict.lower()
        if kind == "checks":
            ty = "T7" if v.startswith("refuted") else ("REPAIR" if v in ("repaired", "corrected", "refined") else
                                                        ("T2" if v == "confirmed" else "SRC"))
        else:
            ty = "T2" if v.startswith("agree") else ("T7" if v.startswith("disagree") else "BLIND?")
        grouped[(lin(to), nodes[fr]["run"], ty, kind)].append((fr, to, verdict, col))
for (L, frun, ty, kind), lst in grouped.items():
    fr, to, verdict, col = lst[0]
    rows_ = ", ".join(dict.fromkeys(nodes[x[0]]["id"] for x in lst))
    d = date_of(nodes[fr]["last"])
    if kind == "checks":
        add_event(to, ty, ASTRA, frun, d, f"{frun} results, column '{col}'",
                  f"{frun} row(s) {rows_} check it: {verdict}", sub="later run's check column", dedupe=(L, ty, frun, kind))
    else:
        add_event(to, ty, ASTRA, frun, d, f"{frun} results, stated_value_compared",
                  f"blind re-derivation in {frun}, row(s) {rows_}: {verdict}", sub="blind re-derivation",
                  dedupe=(L, ty, frun, kind))
for fr, to, kind, verdict, col in cross:
    frn, ton = nodes[fr], nodes[to]
    d = date_of(frn["last"])
    if kind in ("checks", "blind"):
        continue
    elif kind == "uses":
        clause = prompt_clause.get(frn["run"], False)
        ty = "T4" if clause else "USE"
        add_event(to, ty, ASTRA, frn["run"], d, f"{frn['run']} results, depends_on of row {frn['id']}",
                  f"used by {frn['run']} {frn['id']}" + (" (its prompt: inputs are checked where used)" if clause else ""),
                  sub="used by a later run", dedupe=(lin(to), ty, frn["run"], "use"))
    else:
        add_event(to, "NAMED", ASTRA, frn["run"], d, f"{frn['run']} results, column '{col}' of row {frn['id']}",
                  f"named by {frn['run']} {frn['id']}", sub="named by a later run", dedupe=(lin(to), "NAMED", frn["run"]))
for fr, to, lab, k in prompt_links:
    if fr:
        frn = nodes[fr]
        clause = prompt_clause.get(frn["run"], False)
        if k == "R":
            ty = "T4" if clause else "USE"
            add_event(to, ty, ASTRA, frn["run"], date_of(frn["last"]), f"{prompt_of[frn['run']].relative_to(DOC).as_posix()} item {lab}",
                      f"prompt input {lab} of {frn['run']}, used by its row {frn['id']}"
                      + (" (inputs are checked where used)" if clause else ""), sub="prompt R-item used",
                      dedupe=(lin(to), ty, frn["run"], "use"))
        else:
            add_event(to, "REWORK", ASTRA, frn["run"], date_of(frn["last"]),
                      f"{prompt_of[frn['run']].relative_to(DOC).as_posix()} item {lab}",
                      f"taken up as task {lab} of {frn['run']} (row {frn['id']})", sub="prompt task answered",
                      dedupe=(lin(to), "REWORK", frn["run"]))
    else:
        r2 = k.split(":", 1)[1]
        add_event(to, "PROMPT", ASTRA, r2, date_of(RUN_FIRST.get(r2, "")),
                  f"{prompt_of[r2].relative_to(DOC).as_posix()} item {lab}",
                  f"restated as {lab} in the prompt of {r2}; no row of {r2} names the item", sub="prompt background",
                  dedupe=(lin(to), "PROMPT", r2))
for a, b, j in restate:
    ea, eb = (a, b) if (nodes[a]["first"] or "9") <= (nodes[b]["first"] or "9") else (b, a)
    if lin(ea) == lin(eb):
        continue
    add_event(ea, "RESTATE", ASTRA, nodes[eb]["run"], date_of(nodes[eb]["first"]),
              f"{nodes[eb]['run']} results (text overlap {j})", f"probably restated as {eb} (Jaccard {j})",
              sub="text match", dedupe=(lin(ea), "RESTATE", nodes[eb]["run"]))
# 6a'. same-claim edges the one-row-per-run rule kept apart, and the sweep's other relations: links, not merges
for a, b, why in blocked:
    ea, eb = (a, b) if (nodes[a]["first"] or "9") <= (nodes[b]["first"] or "9") else (b, a)
    if nodes[eb]["run"] != nodes[ea]["run"]:
        add_event(ea, "REWORK", ASTRA, nodes[eb]["run"], date_of(nodes[eb]["first"]), why,
                  f"restated or re-derived as {eb} ({why}; kept as a link: its lineage already holds a row of that run)",
                  sub="same-claim link", dedupe=(lin(ea), "REWORK", nodes[eb]["run"]))
for a, b, rel, reason, f in sweep_links:
    na, nb = nodes[a], nodes[b]
    if rel.startswith("refuted"):
        add_event(b, "T7", OPUS_MAX + " (sweep 1)", "doc:" + f, "2026-11-18", f, f"refuted by {a}: {reason}",
                  sub="sweep 1 relation")
    elif rel.startswith("settled"):
        add_event(b, "REWORK", ASTRA, na["run"], date_of(na["first"]), f, f"settled by {a}: {reason}",
                  sub="sweep 1 relation", dedupe=(lin(b), "REWORK", na["run"]))
    else:
        early, late = (b, a) if (nb["first"] or "9") <= (na["first"] or "9") else (a, b)
        if nodes[late]["run"] != nodes[early]["run"]:
            add_event(early, "REWORK", ASTRA, nodes[late]["run"], date_of(nodes[late]["first"]), f,
                      f"{rel} form stated by {late} (sweep 1: {reason})", sub="sweep 1 relation",
                      dedupe=(lin(early), "REWORK", nodes[late]["run"]))
for f in sorted(REG.glob("sweep1_*/CHECK_EVENTS.tsv")):
    rd = list(csv.DictReader(open(f, encoding="utf-8-sig", newline=""), delimiter="\t"))
    for r in rd:
        sid = (r.get("statement") or r.get("statement tag") or r.get("statement_id") or "").strip()
        tags = [sid] if sid in nodes else [f"{a}:{b}" for a, b in refs_in(sid)]
        for t in tags:
            ty = type_norm(r.get("type"))
            add_event(t, ty, who_model(r.get("who")), "doc:" + f.relative_to(DOC).as_posix(), date_of(r.get("date")),
                      f.relative_to(DOC).as_posix(), f"{r.get('type')}: {r.get('outcome')}", sub="sweep 1 CHECK_EVENTS")

# 6b. members in other runs: the claim was carried or re-written by that run
for c, ts in lineages.items():
    runs = []
    for t in ts:
        r = nodes[t]["run"]
        if r not in runs:
            runs.append(r)
    for t in ts:
        n = nodes[t]
        if n["run"] == nodes[c]["run"]:
            continue
        why = "carried into the paper inventory" if n["kind"] == "inventory" else "a row of this run states it"
        add_event(t, "REWORK", ASTRA, n["run"], date_of(n["first"]), "lineage member " + t, why, sub="member row",
                  dedupe=(c, "REWORK", n["run"]))
# 6c. computations named in the proof itself
CODE_RX = re.compile(r"(\bcode/|\.py\b|\.sage\b|\.gp\b|\.m2?\b|\.lean\b|\bscript\b|\bprogram\b|\bcertificate\b|"
                     r"\bcomputed\b|\bcomputation\b|\bSage\b|\bMagma\b|\bGAP\b|\bPARI\b|\bArb\b|interval arithmetic|"
                     r"exhaustive search|brute[- ]force)", re.I)
for run, s in newest_raw.items():
    for row in s["rows"]:
        tag = f"{run}:{row['id'].strip()}"
        blob = " ".join([row.get("where_proved") or "", row.get("notes") or "", row.get("where_checked") or ""])
        m = CODE_RX.search(blob)
        if m and tag in nodes:
            add_event(tag, "T3P", ASTRA, run, date_of(s["stamp"]), f"{s['results']} (where_proved/notes)",
                      f"computation in its own proof: ...{one_line(blob[max(0, m.start() - 60): m.end() + 80])}...",
                      sub="code named in the proof", dedupe=(lin(tag), "T3P", run))
print(f"events after cross-run iterations: {len(events)}")

# 6d. in-run review files (sub-agent reviews, audits, second readings) and progress reviews
REV_NAME = re.compile(r"(review|audit|referee|second_read|recheck|reread|adversarial|root_audits|peer)", re.I)
REV_SKIP = re.compile(r"(visual|render|typeset|manifest|sha256|packag|pdf|image|layout|source_review|pipeline|authoriz|"
                      r"spool|retention|snapshot|bibliograph|citation|cited|source_audit|locator|language|"
                      r"cross_reference|metadata|figure|preview|compile|font|overfull|name_reconciliation|legacy|assembly)", re.I)
PROG_NAME = re.compile(r"(progress_review|progress_assess|movement_review|MOVEMENT_REVIEWS|PROGRESS_LEDGER|"
                       r"hourly_assess|hour\d+_|_hour\b|fifth_hour|sixth_hour|eighth_hour|ninth_hour)", re.I)
inrun_files = 0
for run, s in newest_raw.items():
    if not s.get("folder"):
        continue
    files = walk_files(s["folder"], 4, lambda p: p.suffix.lower() in (".md", ".txt", ".json", ".tsv", ".csv")
                       and (REV_NAME.search(p.name) or PROG_NAME.search(p.name)) and not REV_SKIP.search(p.name)
                       and p.stat().st_size <= 400_000 and not EV_NAME.search(p.name),
                       skip=(EV_DIR_SKIP - {"research"}) | {"code"})
    for f in files:
        try:
            text = f.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        inrun_files += 1
        prog = bool(PROG_NAME.search(f.name)) and not REV_NAME.search(f.name)
        rel = f.relative_to(DOC).as_posix()
        hit = set()
        for m in ID_RX.finditer(text):
            for x in expand(run, m.group(1), m.group(2)):
                if x in ids_by_run[run]:
                    hit.add(x)
        for m in S6LAB_RX.finditer(text) if run in ("S6_10_PAPERS", "S6_09_PAPERS") else []:
            t = resolve_s6_label(m.group(1))
            if t:
                hit.add(t)
        for x in hit:
            tag = x if ":" in x else f"{run}:{x}"
            add_event(tag, "PROGRESS" if prog else "INRUN", ASTRA, run, date_of(s["stamp"]), rel,
                      ("named in the run's progress review " if prog else "named in an in-run review file ") + f.name,
                      sub="in-run file", dedupe=(lin(tag), "PROGRESS" if prog else "INRUN", rel))
print(f"in-run review and progress files read: {inrun_files}; events: {len(events)}")

# ------------------------------------------------------------------------------------------------ 7. our documents
notes_rows = {r["note"]: r for r in csv.DictReader(open(FE / "INTAKE_LEDGER_NOTES.tsv", encoding="utf-8"), delimiter="\t")}
jl = [json.loads(x) for x in open(FE / "check_ledger.jsonl", encoding="utf-8")]
jl_by_doc = collections.defaultdict(list)
for x in jl:
    jl_by_doc[x["doc"]].append(x)
docs = {}


def add_doc(rel, kind="", author="", date="", runs=()):
    rel = rel.replace("\\", "/")
    p = DOC / rel
    if not p.exists() or p.suffix.lower() != ".md":
        return
    d = docs.setdefault(rel, dict(rel=rel, kind="", author="", date="", runs=set()))
    d["kind"] = d["kind"] or kind
    d["author"] = d["author"] or author
    d["date"] = d["date"] or date
    d["runs"] |= set(runs)


DOC_SKIP = re.compile(r"(INTAKE_LEDGER|INTAKE_TODO|CHECK_LEDGER|REGISTRY|READING_AUDIT|MATH_TODO|CLAIMS_FROM_NOTES|"
                      r"FOLLOWUPS_FROM_NOTES|GAP_FROM_NOTES|NOTES_GAP|GROTHENDIECK_CLAIMS_MAP|UNPROMPTED_IDEAS|PLAYBOOK|"
                      r"METHODOLOGY|^BRIEF|PROMPT|README|_before_|AS_SENT|MANIFEST|PORT_INTO|PROGRAMS\.md|WHO_WROTE)", re.I)
for rel, rows in jl_by_doc.items():
    add_doc(rel, rows[0]["kind"], "; ".join(rows[0].get("author_agents") or []), rows[0]["date"], [x["run"] for x in rows])
for rel, r in notes_rows.items():
    add_doc(rel, r["kind"], r["author"], r["date"], [x.strip() for x in r["runs"].split(",") if x.strip()])
for r in csv.DictReader(open(FE / "INTAKE_LEDGER.tsv", encoding="utf-8"), delimiter="\t"):
    if r["kind"] != "research":
        continue
    for col in ("intakes", "expert"):
        for x in r[col].split("<br>"):
            m = re.match(r"\s*`([^`]+)`\s*\((.*)\)", x)
            if m:
                inner = m.group(2)
                kind = "expert" if col == "expert" else ("prompt items" if inner.startswith("prompt items") else "intake")
                au = "; ".join(re.findall(r"(?:[0-9a-f]{8}|main session) \([^)]*\)", inner))
                add_doc(m.group(1), kind, au, "", [r["run"]])
# the S6 reviews and intakes, and intake folders newer than the ledgers
for p in list((S6W / "reviews").rglob("*.md")) + list((S6W / "intake").glob("*.md")) + \
        list((S6W / "checkpoint_intake_20261115").glob("*.md")) + list((DOC / "pro_intake_20261117").glob("*.md")) + \
        list((DOC / "pro_intake_20261116").glob("*.md")) + list((DOC / "claude_math_notes").glob("*.md")):
    if "/scripts/" in p.as_posix() or "/out/" in p.as_posix():
        continue
    add_doc(p.relative_to(DOC).as_posix())
for rel in list(docs):
    if DOC_SKIP.search(rel.rsplit("/", 1)[-1]) or rel.startswith("results_register/"):
        docs.pop(rel)


def doc_class(rel, kind):
    n = rel.rsplit("/", 1)[-1]
    if re.search(r"REFEREE|PEER_REVIEW", n, re.I) or kind == "referee":
        return "referee"
    if re.search(r"(^REVIEW|_REVIEW\.md$|READING_|SECOND_READING|CHECK_OF_|DRAFT_CHECK|G6_VERDICT|SENSE_CHECK|^FINDINGS)",
                 n, re.I) and not re.search(r"POSITION|RESPONSE", n):
        return "review"
    if kind in ("intake",) or re.search(r"INTAKE|FIRST_LOOK|LATE_ROWS|IMPLICATIONS|REVIEW_REGISTER", n, re.I):
        return "intake"
    if kind == "prompt items" or re.search(r"PUSH_ITEMS|BLOCK_FOR|PROMPT_UPDATES|NEXT_PROMPT", n):
        return "prompt items"
    if kind == "literature" or re.search(r"LITERATURE|COMPARISON|GENERALIZED", n):
        return "literature"
    if kind in ("main-session notes", "my notes") or rel.startswith("claude_math_notes/"):
        return "notes"
    return "expert"


HEAD_AUTHOR = re.compile(r"(Claude\s*\(?\s*(?:Fable|Opus|Sonnet)\s*\d\.\d[^\n]{0,80})", re.I)


def doc_author(d, text):
    if d["author"]:
        ms = re.findall(r"\((Claude [^)]*\)?)\)", d["author"])
        if ms:
            return "; ".join(sorted({who_model(m) for m in ms}))
        if "Claude" in d["author"]:
            return who_model(d["author"])
    head = "\n".join(text.splitlines()[:14])
    m = HEAD_AUTHOR.search(head)
    if m:
        frag = m.group(1)
        e = re.search(r"effort[\s:]*\**(max|xhigh|high|medium|low)", head, re.I)
        w = who_model(frag + (f" effort {e.group(1)}" if e and "effort" not in frag else ""))
        return w
    return "author not identified in our records"


CHECK_VERB = re.compile(r"\b(re-?deriv\w*|recomput\w*|re-?prov\w*|by hand|own (?:code|script|program|computation|"
                        r"sympy|check)|checked\b|verified|holds\b|confirmed|proved as claimed|followed the (?:argument|proof)|"
                        r"read in full|line by line|step by step|proof read|correct\b|consistent\b|\*\*proved\b|"
                        r":\s*proved\b)", re.I)
# in intakes and expert notes only first-hand words count (a line that reports someone else's check does not)
STRONG_CHECK = re.compile(r"(\b[Rr]e-?deriv\w*|\b[Rr]ecomput\w*|\b[Rr]e-?prov\w*|\bby hand\b|\b[Oo]wn (?:code|script|program|"
                          r"computation|sympy|mpmath|grid|check)|\bI (?:checked|verified|re-?derived|recomputed|followed|"
                          r"reproduced)|\bread in full\b|\bline by line\b|\bfollowed the (?:argument|proof)|"
                          r"\bHolds\b|\*\*[Hh]olds|\bproved as claimed\b)")
NEG = re.compile(r"\b(unverified|not (?:checked|verified|read|re-?derived|recomputed|opened|followed)|did not (?:check|"
                 r"re-?derive|read|verify|recompute|follow)|undetermined|unchecked|was not run|not by me|unread|"
                 r"checked (?:in|by) (?:the |its |an? )?[A-Z]\w+|according to|the (?:run|return|report|answer) "
                 r"(?:says|states|claims))", re.I)
FAULT_VERB = re.compile(r"\b(refut\w*|false\b|wrong\b|gap\b|error\b|fails?\b|counterexample|does not hold|invalid)", re.I)
doc_events = 0
doc_stats = {}
for rel, d in sorted(docs.items()):
    p = DOC / rel
    try:
        if p.stat().st_size > 3_000_000:
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        continue
    cls = doc_class(rel, d["kind"])
    if re.search(r"\bby script\b", " ".join(text.splitlines()[:3])) and not HEAD_AUTHOR.search(" ".join(text.splitlines()[:6])):
        doc_stats[rel] = dict(cls="script listing (no reader)", who="", date="", lineages=0)
        continue  # a listing made by a script is not a reading
    who = doc_author(d, text)
    date = date_of(B.stamp_of(p.name)) or date_of(d["date"]) or date_of(" ".join(text.splitlines()[:8])) or \
        date_of(mtime_stamp(p))
    single = None
    runs_named = {canon(m.group(1)) for m in RUN_RX.finditer(text)} & set(snaps_by_run)
    dr = {x for x in d["runs"] if x in snaps_by_run}
    if len(dr) == 1:
        single = next(iter(dr))
    elif len(runs_named) == 1:
        single = next(iter(runs_named))
    if "S6_02_REVIEW_FABLE" in rel:
        single = "S6_02_FAMILY"
    elif rel.endswith(("INTAKE_S6_01.md", "READING_S6_01_A1.md")):
        single = "S6_01_INVARIANTS"
    elif rel.endswith("INTAKE_S6_05_FINAL.md"):
        single = "S6_05_ARITHMETIC"
    if not single:  # the subject of the title: the first run its first heading names
        for ln0 in text.splitlines()[:3]:
            m0 = [canon(m.group(1)) for m in RUN_RX.finditer(ln0) if canon(m.group(1)) in snaps_by_run]
            if ln0.startswith("#") and m0:
                single = m0[0]
                break
    hits = {}  # lineage -> (best class code, line)
    section = None
    sec_verdict, sec_used = None, True
    for ln in text.splitlines():
        if ln.startswith("#"):
            rn = [canon(m.group(1)) for m in RUN_RX.finditer(ln)]
            rn = [x for x in rn if x in snaps_by_run]
            section = rn[0] if rn else (section if section and not ln.startswith("# ") else None)
            # a verdict in a review's or referee's heading ("... : proved") belongs to the first id of its section
            sec_verdict, sec_used = None, True
            hv = re.search(r"(?::|—|–|\s-)\s*\**\s*(proved|correct|holds|confirmed|refuted|false|wrong|gap)\b", ln, re.I)
            if cls in ("referee", "review") and hv and not re.search(r"unverified|unproved", ln, re.I):
                sec_verdict, sec_used = ("fault" if hv.group(1).lower() in ("refuted", "false", "wrong", "gap") else "check"), False
            elif cls in ("referee", "review") and not NEG.search(ln):
                if CHECK_VERB.search(ln):
                    sec_verdict, sec_used = "check", False
                elif FAULT_VERB.search(ln):
                    sec_verdict, sec_used = "fault", False
        default = section or single
        refs = refs_pos(ln, default_run=default)
        if default in NUMERIC_RUNS:  # runs numbered 4.3, 5.1 (Q03_DEPOSIT): bare numbers count only in its own documents
            for m in re.finditer(r"(?<![\w.])(\d{1,2}\.\d{1,2}(?:\.\d{1,2})?)(?![\w.])", ln):
                if m.group(1) in ids_by_run[default]:
                    refs.append((default, m.group(1), m.start(), m.end()))
        for m in S6LAB_RX.finditer(ln):
            t = resolve_s6_label(m.group(1))
            if t:
                refs.append((None, t, m.start(), m.end()))
        if not refs:
            continue
        refs.sort(key=lambda r: r[2])
        cv = CHECK_VERB if cls in ("referee", "review") else STRONG_CHECK
        for i, (r2, x, st, en) in enumerate(refs):
            # the words that belong to this id: up to the next id (at most 80 characters), or, for an id inside a
            # list (ids separated by commas or "and"), the words just before the list
            nxt = refs[i + 1][2] if i + 1 < len(refs) else len(ln)
            win = ln[en: min(nxt, en + 80)]
            j = i
            while j > 0 and re.fullmatch(r"[\s,;and&]*", ln[refs[j - 1][3]: refs[j][2]] or ""):
                j -= 1
            pre = ln[max(0, refs[j][2] - 80): refs[j][2]] if (not win.strip(" ,;.)") or j < i) else ""
            seg = pre + " " + win
            if NEG.search(seg) or re.search(r"\b(?:if|whether|assuming|unless|once|until|suppose)\b[^.;:|]*$",
                                             ln[max(0, st - 30): st], re.I):
                verb = "named"
            else:
                verb = "check" if cv.search(seg) else ("fault" if FAULT_VERB.search(seg) else "named")
            if not sec_used and verb == "named":
                verb = sec_verdict
            sec_used = True
            tag = x if r2 is None else f"{r2}:{x}"
            L = lin(tag)
            if not L:
                continue
            rank = {"check": 2, "fault": 1, "named": 0}[verb]
            if L not in hits or rank > hits[L][0]:
                hits[L] = (rank, verb, tag, one_line(ln, 220))
    ev_kind = {"referee": {"check": "T1", "fault": "T1", "named": "REFEREE_NAMED"},
               "review": {"check": "T1", "fault": "T1", "named": "REVIEW_NAMED"},
               "intake": {"check": "INTAKE_CHECK", "fault": "INTAKE", "named": "INTAKE"},
               "prompt items": {"check": "PROMPT_ITEM", "fault": "PROMPT_ITEM", "named": "PROMPT_ITEM"},
               "literature": {"check": "SRC", "fault": "SRC", "named": "SRC"},
               "notes": {"check": "T6", "fault": "T6", "named": "T6"},
               "expert": {"check": "EXPERT_CHECK", "fault": "T6", "named": "T6"}}[cls]
    for L, (rank, verb, tag, ln) in hits.items():
        k = ev_kind[verb]
        if add_event(tag, k, who, "doc:" + rel, date, rel, f"{cls} ({verb}): {ln}", sub=cls, dedupe=(L, "doc", rel)):
            doc_events += 1
    doc_stats[rel] = dict(cls=cls, who=who, date=date, lineages=len(hits))
# entries of the S6 check ledger and the S6_09 recorded checks, where my scan did not already attribute the document
for tag, loc, who, date, verb, detail in S6_DOC_EVENTS:
    key2 = "/".join(re.sub(r"^.*?reviews/", "reviews/", loc.split(",")[0].strip()).split("/")[-2:])
    rel = next((r for r in docs if r.endswith(key2)), None)
    if not rel:
        continue
    L = lin(tag)
    cls = doc_stats.get(rel, {}).get("cls") or doc_class(rel, "")
    k = {"referee": "T1", "review": "T1", "intake": "INTAKE", "expert": "T6", "notes": "T6", "literature": "SRC",
         "prompt items": "PROMPT_ITEM"}[cls]
    if verb == "discussed in":
        k = "T6"
    if verb == "checked in" and "READING_" in rel:
        k = "T1"
    add_event(tag, k, who_model(who), "doc:" + rel, date, rel, f"{cls} (S6 check ledger: {verb}) {detail}",
              sub=cls, dedupe=(L, "doc", rel))
# intake CHECK_EVENTS files (typed by the intake itself)
for f in [DOC / "pro_intake_20261117" / "CHECK_EVENTS.tsv", S6W / "intake" / "S6_10_INTAKE_CHECK_EVENTS.tsv"]:
    if not f.exists():
        continue
    for r in csv.DictReader(open(f, encoding="utf-8-sig", newline=""), delimiter="\t"):
        sid = r.get("statement_id", "")
        tags = []
        for m in S6LAB_RX.finditer(sid):
            t = resolve_s6_label(m.group(1))
            if t:
                tags.append(t)
        tags += [f"{a}:{b}" for a, b in refs_in(sid)]
        for t in tags:
            ty = type_norm(r.get("type"))
            if ty == "EDIT":
                continue
            add_event(t, ty, who_model(r.get("who")), "doc:" + f.relative_to(DOC).as_posix(), date_of(r.get("date")),
                      f.relative_to(DOC).as_posix(), f"{r.get('type')}: {r.get('outcome')}", sub="intake CHECK_EVENTS")
print(f"documents read: {len(doc_stats)}; document events: {doc_events}; all events: {len(events)}")

# ------------------------------------------------------------------------------------------------ 8. aggregation
REAL = {"T1", "T2", "T3", "T4", "INTAKE_CHECK", "EXPERT_CHECK"}
STRENGTH = [  # rubric order, strongest first
    ("T1", "targeted proof check"), ("INTAKE_CHECK", "targeted proof check (claimed in an intake line)"),
    ("EXPERT_CHECK", "targeted proof check (claimed in an expert note)"), ("T2", "independent re-proof"),
    ("T3", "computation or formal certificate"), ("T4", "checked in use by a later run"),
    ("T3P", "computation inside its own proof"), ("INRUN", "named in an in-run review file (scope not parsed)"),
    ("REFEREE_NAMED", "named in a referee report"), ("REVIEW_NAMED", "named in a review"),
    ("T5", "survived exposure"), ("EXPOSURE", "survived exposure"), ("T6", "discussed by an expert or in notes"),
    ("INTAKE", "read in an intake (register level, not a proof check)")]
events_by_lin = collections.defaultdict(list)
for e in events:
    L = lin(e["node"])
    if L:
        e["lineage"] = L
        events_by_lin[L].append(e)

# dependents: rows that use a member (within its run, from the register's edges and depends_on, and across runs)
dependents = collections.Counter()
reg_edges = REG / "EDGES.tsv"
with open(reg_edges, encoding="utf-8", newline="") as fh:
    for r in csv.DictReader(fh, delimiter="\t"):
        if r["kind"] in ("uses", "names") and r["to"] in nodes and r["from"] in nodes:
            if lin(r["to"]) != lin(r["from"]):
                dependents[(lin(r["to"]), lin(r["from"]))] += 1
for fr, to, kind, verdict, col in cross:
    if kind == "uses" and lin(to) != lin(fr):
        dependents[(lin(to), lin(fr))] += 1
for fr, to, lab, k in prompt_links:
    if fr and lin(to) != lin(fr):
        dependents[(lin(to), lin(fr))] += 1
dep_count = collections.Counter()
dep_runs = collections.defaultdict(set)
for (a, b), _ in dependents.items():
    dep_count[a] += 1
    dep_runs[a].add(nodes[b]["run"])

ledger = []
for c, ts in lineages.items():
    evs = events_by_lin.get(c, [])
    n0 = nodes[c]
    origin_run = n0["run"]
    runs_members = []
    for t in ts:
        if nodes[t]["run"] not in runs_members:
            runs_members.append(nodes[t]["run"])
    # status now: the newest member
    current = [t for t in ts if not nodes[t].get("dropped")]
    newest = max(current or ts, key=lambda t: (nodes[t]["last"] or "", 1 if nodes[t]["kind"] == "row" else 0))
    status_now = nodes[newest]["status"] if current else "Dropped"
    # history across members, changes only
    hist = []
    for t in ts:
        for h in nodes[t]["hist"]:
            hist.append((h["stamp"], nodes[t]["run"], h["label"], h["status"], h["est"]))
    hist.sort()
    hist_c = []
    for h in hist:
        if not hist_c or (h[1], h[3]) != (hist_c[-1][1], hist_c[-1][3]):
            hist_c.append(h)
    n_snap = len(hist)
    hist_s = "; ".join(f"{nice_stamp(h[0])}{'~' if h[4] else ''} {h[1]} {h[2]} {h[3]}" for h in hist_c)
    if len(hist_c) > 14:
        hh = hist_c[:4] + hist_c[-8:]
        hist_s = "; ".join(f"{nice_stamp(h[0])} {h[1]} {h[2]} {h[3]}" for h in hh[:4]) + f"; ... ({len(hist_c) - 12} more) ...; " + \
            "; ".join(f"{nice_stamp(h[0])} {h[1]} {h[2]} {h[3]}" for h in hh[4:])
    statuses_seen = [h[3] for h in hist_c]
    revisions = sum(nodes[t]["revisions"] for t in ts)
    k = collections.defaultdict(list)
    for e in evs:
        k[e["kind"]].append(e)
    # distinct runs that reworked it (later runs: member rows, check columns, blind re-derivations, tasks, writing checks)
    rework_runs = {e["actor"] for e in evs if not e["actor"].startswith("doc:") and e["actor"] != origin_run
                   and e["kind"] in ("REWORK", "T1", "T2", "T3", "REPAIR", "T7")}
    used_runs = {e["actor"] for e in k.get("T4", []) if not e["actor"].startswith("doc:")}
    use_nocheck = {e["actor"] for e in k.get("USE", [])}
    named_runs = {e["actor"] for e in k.get("NAMED", []) + k.get("RESTATE", []) + k.get("PROMPT", [])}
    checked_runs = rework_runs | used_runs
    exposure_runs = (use_nocheck | named_runs) - checked_runs - {origin_run}
    t1 = k.get("T1", [])
    t1_claude = [e for e in t1 if e["actor"].startswith("doc:")]
    t1_inrun = [e for e in t1 if e["actor"] == origin_run]
    t1_later = [e for e in t1 if not e["actor"].startswith("doc:") and e["actor"] != origin_run]
    intake_docs = {e["actor"] for e in k.get("INTAKE", []) + k.get("INTAKE_CHECK", [])}
    expert_docs = {e["actor"] for e in k.get("T6", []) + k.get("EXPERT_CHECK", [])}
    referee_docs = {e["actor"] for e in t1_claude}
    real = len(t1) + len(k.get("T2", [])) + len(k.get("T3", [])) + len(used_runs) + len(k.get("INTAKE_CHECK", [])) + \
        len(k.get("EXPERT_CHECK", []))
    whom = collections.Counter()
    for e in evs:
        if e["kind"] in ("NAMED", "PROMPT", "RESTATE", "EDIT", "OTHER", "PROGRESS"):
            continue
        whom[e["who"]] += 1
    dates = sorted([e["date"] for e in evs if e["date"]] + [date_of(h[0]) for h in hist if h[0]])
    have = set(k)
    if exposure_runs:
        have.add("EXPOSURE")
    strongest = next((lab for code, lab in STRENGTH if code in have), "none recorded")
    if "T1" in have:
        who_s = "by Claude" if t1_claude else ("by a later run" if t1_later else "in its own run")
        strongest = f"targeted proof check ({who_s})"
    refuted = [e for e in k.get("T7", [])] + [e for e in k.get("REPAIR", [])]
    is_main = any(nodes[t].get("main") for t in ts)
    ledger.append(dict(
        canonical_tag=c, line=n0["line"] or run_line(origin_run), status_now=status_now, status_now_from=newest,
        members="; ".join(ts), n_members=len(ts), runs=", ".join(runs_members), n_runs=len(runs_members),
        statement=one_line(n0["statement"] or nodes[newest]["statement"], 240),
        status_history=hist_s, snapshots=n_snap, statuses_seen=" > ".join(dict.fromkeys(statuses_seen)),
        within_run_revisions=revisions,
        runs_reworked=len(rework_runs), runs_reworked_names=", ".join(sorted(rework_runs)),
        runs_used_rechecked=len(used_runs), runs_used_rechecked_names=", ".join(sorted(used_runs)),
        targeted_checks=len(t1), targeted_in_own_run=len(t1_inrun), targeted_by_later_runs=len(t1_later),
        targeted_by_claude=len(t1_claude), intake_line_checks=len(k.get("INTAKE_CHECK", [])),
        expert_line_checks=len(k.get("EXPERT_CHECK", [])),
        independent_reproofs=len(k.get("T2", [])), computations=len(k.get("T3", [])),
        computation_in_own_proof=len(k.get("T3P", [])), source_checks=len(k.get("SRC", [])),
        in_run_review_files=len(k.get("INRUN", [])), progress_reviews=len(k.get("PROGRESS", [])),
        intakes_read=len(intake_docs), referee_or_review_docs=len(referee_docs | {e["actor"] for e in k.get("REFEREE_NAMED", []) + k.get("REVIEW_NAMED", [])}),
        expert_discussions=len(expert_docs), prompt_items=len({e["actor"] for e in k.get("PROMPT_ITEM", [])}),
        survived_exposure_runs=len(exposure_runs) + len(k.get("T5", [])),
        survived_exposure_names=", ".join(sorted(exposure_runs)),
        refuted_or_repaired_events=len(refuted),
        refutations="; ".join(one_line(e["detail"], 120) for e in refuted[:3]),
        real_checks=real, by_whom="; ".join(f"{w}: {n}" for w, n in whom.most_common()),
        first_date=dates[0] if dates else "", last_date=dates[-1] if dates else "",
        strongest_check=strongest, dependents=dep_count.get(c, 0), dependent_runs=len(dep_runs.get(c, ())),
        main_row="yes" if is_main else "",
        printed_s6_10="yes" if any(nodes[t].get("printed") for t in ts) else "",
        credit_pending="yes" if any(nodes[t].get("credit_pending") for t in ts) else "",
        in_register="yes" if any(nodes[t]["in_register"] for t in ts) else "no"))

COLS = ["canonical_tag", "line", "status_now", "status_now_from", "n_members", "members", "n_runs", "runs", "statement",
        "status_history", "snapshots", "statuses_seen", "within_run_revisions", "runs_reworked", "runs_reworked_names",
        "runs_used_rechecked", "runs_used_rechecked_names", "targeted_checks", "targeted_in_own_run",
        "targeted_by_later_runs", "targeted_by_claude", "intake_line_checks", "expert_line_checks",
        "independent_reproofs", "computations", "computation_in_own_proof", "source_checks", "in_run_review_files",
        "progress_reviews", "intakes_read", "referee_or_review_docs", "expert_discussions", "prompt_items",
        "survived_exposure_runs", "survived_exposure_names", "refuted_or_repaired_events", "refutations",
        "real_checks", "by_whom", "first_date", "last_date", "strongest_check", "dependents", "dependent_runs",
        "main_row", "printed_s6_10", "credit_pending", "in_register"]
ledger.sort(key=lambda x: (x["line"], x["canonical_tag"]))
OUT.mkdir(exist_ok=True)
with open(OUT / "CHECKEDNESS_LEDGER.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(COLS)
    for x in ledger:
        w.writerow([x[c] for c in COLS])
ECOLS = ["lineage", "node", "kind", "sub", "who", "actor", "date", "source", "detail"]
with open(OUT / "CHECKEDNESS_EVENTS.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(ECOLS)
    for e in sorted(events, key=lambda e: (e.get("lineage") or "", e["date"], e["kind"])):
        if e.get("lineage"):
            w.writerow([e.get(c, "") for c in ECOLS])
print(f"ledger rows: {len(ledger)}; events written: {sum(1 for e in events if e.get('lineage'))}")

# ------------------------------------------------------------------------------------------------ 9. stats
L_by = {x["canonical_tag"]: x for x in ledger}
stats = dict(built=TODAY, register_rows=len(register), snapshots=len(snapshots), runs=len(snaps_by_run),
             nodes=len(nodes), lineages=len(ledger), events=len(events),
             snapshots_by_run={r: len(v) for r, v in sorted(snaps_by_run.items())},
             prompts=len(prompt_of), prompt_items=n_items, prompts_with_clause=sum(prompt_clause.values()),
             documents=len(doc_stats), doc_classes=dict(collections.Counter(d["cls"] for d in doc_stats.values())),
             event_kinds=dict(collections.Counter(e["kind"] for e in events)),
             unresolved_check_event_ids=dict(unresolved_ev), restatements=len(restate),
             same_edges=dict(collections.Counter(w for _, _, w in same_edges)),
             cross_refs=dict(collections.Counter(k for _, _, k, _, _ in cross)))
by_line = collections.defaultdict(collections.Counter)
for x in ledger:
    if x["status_now"] != "Proved":
        continue
    by_line[x["line"]]["proved"] += 1
    by_line[x["line"]]["strongest: " + x["strongest_check"]] += 1
    by_line[x["line"]]["real_checks=0"] += x["real_checks"] == 0
    by_line[x["line"]]["reworked by >=1 later run"] += x["runs_reworked"] >= 1
    by_line[x["line"]]["read in >=1 intake"] += x["intakes_read"] >= 1
stats["proved_by_line"] = {k: dict(v) for k, v in by_line.items()}
dist = collections.defaultdict(collections.Counter)
for x in ledger:
    if x["status_now"] == "Proved":
        dist[x["line"]][min(x["real_checks"], 10)] += 1
stats["real_check_distribution"] = {k: dict(sorted(v.items())) for k, v in dist.items()}
(OUT / "checkedness_stats.json").write_text(json.dumps(stats, indent=1, ensure_ascii=False), encoding="utf-8")


# ------------------------------------------------------------------------------------------------ 10. LEAST_CHECKED.md
def importance(x):
    return x["dependents"] + 3 * x["dependent_runs"] + (8 if x["main_row"] else 0) + 2 * x["prompt_items"] + \
        (2 if x["runs_used_rechecked"] or x["survived_exposure_runs"] else 0)


def short(x, n=110):
    return one_line(x["statement"], n).replace("|", "/")


md = ["# Least-checked claims that matter most (by line)", "",
      f"Built {TODAY} by `results_register/checkedness/build_checkedness.py` (a script; no model) from the files named in "
      "METHOD.md. Written by Claude Opus 5.5 at effort max. GPT-6 Astra (ChatGPT Pro mode), short Astra 6 Pro, wrote and "
      "checked inside every research run; the Claude documents are intakes, referee reports, reviews and notes by Claude "
      "Fable 5.2 and Claude Opus 5.5 at the efforts given in the ledger's by_whom column.", "",
      "**Real checks** count targeted proof checks (in the run itself, by a later run, or by Claude), independent "
      "re-proofs, computations recorded as check events, later runs that used the claim under a prompt that says inputs "
      "are checked where used, and intake or expert lines that say the claim was re-derived or checked. They do not "
      "count register intakes, survived exposure, discussion, or an id named in a review file whose scope was not parsed.",
      "", "**Importance** is the number of rows that use the claim (within and across runs, and prompt items built on it), "
      "with weight for later runs that depend on it and for the main rows of S6_10. The tables list proved claims "
      "with importance at least 3, sorted by real checks (fewest first), then by importance.", ""]
for line in sorted({x["line"] for x in ledger if x["line"]}):
    xs = [x for x in ledger if x["line"] == line and x["status_now"] == "Proved"]
    imp = [x for x in xs if importance(x) >= 3]
    imp.sort(key=lambda x: (x["real_checks"], -importance(x), x["canonical_tag"]))
    zero = sum(1 for x in xs if x["real_checks"] == 0)
    zero_imp = sum(1 for x in imp if x["real_checks"] == 0)
    dist_s = collections.Counter(x["strongest_check"] for x in xs)
    order_s = ["targeted proof check (by Claude)", "targeted proof check (by a later run)",
               "targeted proof check (in its own run)"] + [lab for _, lab in STRENGTH] + ["none recorded"]
    md += [f"## {line}", "",
           f"{len(xs)} proved lineages; {zero} have no real check recorded; of the {len(imp)} that others depend on "
           f"(importance >= 3), {zero_imp} have none. Strongest check each proved lineage has had:", "",
           "| Strongest check | Proved lineages |", "|---|---|"]
    md += [f"| {k} | {v} |" for k, v in sorted(dist_s.items(), key=lambda kv: (order_s.index(kv[0]) if kv[0] in order_s else 99))]
    md += ["", "| Claim | Importance (users; later runs) | Real checks | Strongest check | Iterations | Statement |",
           "|---|---|---|---|---|---|"]
    for x in imp[:45]:
        it = (f"snapshots {x['snapshots']}; later runs that reworked it {x['runs_reworked']}; intakes {x['intakes_read']}; "
              f"exposure {x['survived_exposure_runs']}")
        md.append(f"| `{x['canonical_tag']}` | {importance(x)} ({x['dependents']}; {x['dependent_runs']}) | {x['real_checks']} | "
                  f"{x['strongest_check']} | {it} | {short(x)} |")
    md.append("")
(OUT / "LEAST_CHECKED.md").write_text("\n".join(md) + "\n", encoding="utf-8")

# ------------------------------------------------------------------------------------------------ 11. S6_CASE.md
ce10 = set()
if s6_10_dir:
    for r in csv.DictReader(open(s6_10_dir / "CHECK_EVENTS.tsv", encoding="utf-8-sig", newline=""), delimiter="\t"):
        ce10.add(r["statement_id"].strip())
nol = [lab for lab, r in INV10.items() if not r["in_compendium_only_because"].strip() and lab not in ce10]
pend = [lab for lab, r in INV10.items() if "comparison pending" in r["credited_to"]]


def s6_row(lab):
    t = f"S6_10_PAPERS:{lab}"
    L = lin(t)
    x = L_by[L]
    evs = events_by_lin.get(L, [])
    own10 = [e for e in evs if e["actor"] == "S6_10_PAPERS" and e["kind"] in ("T1", "T2", "T3", "T4")]
    all10 = [e for e in evs if e["actor"] == "S6_10_PAPERS" and e["sub"] in ("S6_10 inventory event", "run CHECK_EVENTS")]
    blind = [e for e in evs if e["sub"] == "blind re-derivation"]
    s609 = [e for e in evs if e["actor"] == "S6_09_PAPERS" and e["kind"] == "T1"]
    claude = {e["actor"] for e in evs if e["actor"].startswith("doc:") and e["kind"] not in ("PROMPT_ITEM",)}
    claude_chk = {e["actor"] for e in evs if e["actor"].startswith("doc:") and e["kind"] in REAL}
    src_runs = [r for r in x["runs"].split(", ") if r not in ("S6_09_PAPERS", "S6_10_PAPERS")]
    src_snaps = sum(len(nodes[t]["hist"]) for t in lineages[L] if nodes[t]["kind"] == "row")
    holders = {nodes[t]["run"] for t in lineages[L]} | {e["actor"] for e in blind}
    return dict(lab=lab, paper=INV10[lab]["paper"], main="main" if INV10[lab]["main_or_supporting"].lower().startswith("main") else "",
                lineage=L, src=", ".join(src_runs), status=x["status_now"], snaps=src_snaps, s610=len(own10),
                all10=len(all10), types10=collections.Counter(e["kind"] for e in all10), s609=len(s609),
                blind=len(blind), claude=len(claude), claude_chk=len(claude_chk), real=x["real_checks"],
                strongest=x["strongest_check"], runs=len(holders), hist=x["statuses_seen"])


md = ["# The S6 case: how often the unrecorded and the credit-pending S6_10 rows have been iterated over", "",
      f"Built {TODAY} by `build_checkedness.py` (script; no model). Written by Claude Opus 5.5 at effort max. The S6_10 "
      "intake (`s6_pro_prompts_20261112_work/intake/S6_10_INTAKE_20261118.md`, Claude Opus 5.5 at effort max) found "
      f"{len(nol)} printed rows with no line in CHECK_EVENTS.tsv and {len(pend)} rows whose credit comparison is "
      "pending. The question here is the user's: are they not checked, and how many times have they been iterated over?",
      "", "Every count below is per row and comes from `CHECKEDNESS_EVENTS.tsv` (one row per event, with its file). Columns:",
      "- **Checkpoints** = results tables of the source run in which the row stands (each checkpoint we hold; a row of "
      "S6_06_BLIND that stood through 17 checkpoints counts 17). These are one Astra instance carrying the row, not "
      "separate checks.",
      "- **Runs** = distinct runs that hold the row, re-wrote it or re-derived it: the source run, S6_09_PAPERS, "
      "S6_10_PAPERS, and S6_06_BLIND where it re-derived the row blind. All are GPT-6 Astra (ChatGPT Pro mode).",
      "- **S6_10 checks / events** = this writing run's own check events on the row (targeted proof checks, "
      "re-proofs, computations, uses), then all its events (editorial reconciliations and alias records included). "
      "They come from the inventory's check_record JSON and records/*.tsv, which hold the events CHECK_EVENTS.tsv "
      "omits, and are deduplicated against CHECK_EVENTS.tsv.",
      "- **S6_09** = the S6_09 writing check carried in the inventory (GPT-6 Astra (ChatGPT Pro mode), 17 Nov: "
      "whole statement and proof read, proof re-derived).",
      "- **Blind** = S6_06_BLIND rows that re-derived the row's stated value without its proof (one per run).",
      "- **Claude docs (checks)** = distinct Claude documents (intakes, reviews, referee reports, expert notes) that "
      "name the row, then those whose line about it records a check or re-derivation.", ""]
TYPE_NAME = {"T1": "targeted proof check", "T2": "independent re-proof", "T3": "computation", "T4": "used and rechecked",
             "T7": "refuted, with correction", "EDIT": "editorial or alias record", "SRC": "source check",
             "OTHER": "other", "T5": "carried as background"}
for title, labs in (("The printed rows with no line in CHECK_EVENTS.tsv", nol), ("The rows awaiting the credit comparison", pend)):
    rows = [s6_row(l) for l in labs if lin(f"S6_10_PAPERS:{l}")]
    zero_cur = sum(1 for r in rows if r["s610"] == 0)
    md += [f"## {title} ({len(rows)})", ""]
    by_paper = collections.Counter(r["paper"] for r in rows)
    med = sorted(r["real"] for r in rows)
    ty = collections.Counter()
    for r in rows:
        ty.update(r["types10"])
    md += [f"- By paper: " + ", ".join(f"{p} {n}" for p, n in sorted(by_paper.items())) + f"; main rows: "
           f"{sum(1 for r in rows if r['main'])}.",
           f"- **They are checked in S6_10 itself:** {len(rows) - zero_cur} of the {len(rows)} rows have at least one "
           f"S6_10 check event of their own outside CHECK_EVENTS.tsv; {zero_cur} have none. Their S6_10 events by type: "
           + ", ".join(f"{TYPE_NAME.get(k, k)} {v}" for k, v in ty.most_common()) + ".",
           f"- Earlier iterations: an S6_09 writing check on {sum(1 for r in rows if r['s609'])} rows; a blind "
           f"re-derivation on {sum(1 for r in rows if r['blind'])}; a Claude document names "
           f"{sum(1 for r in rows if r['claude'])} (and records a check or re-derivation of "
           f"{sum(1 for r in rows if r['claude_chk'])}).",
           f"- Checkpoints of the source run in which the row stands: median "
           f"{sorted(r['snaps'] for r in rows)[len(rows) // 2] if rows else 0}; runs that hold or re-derived it: "
           + ", ".join(f"{k} runs: {v} rows" for k, v in sorted(collections.Counter(r["runs"] for r in rows).items())) + ".",
           f"- Real checks per row (all sources): median {med[len(med) // 2] if med else 0}, maximum "
           f"{med[-1] if med else 0}; rows with none: {sum(1 for r in rows if r['real'] == 0)}.", "",
           "| Label | Paper | Main | Source run | Status | Checkpoints | Runs | S6_10 checks / events | S6_09 | Blind | Claude docs (checks) | Real checks | Strongest |",
           "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in sorted(rows, key=lambda r: (r["paper"], r["real"], r["lab"])):
        md.append(f"| `{r['lab']}` | {r['paper']} | {r['main']} | {r['src']} | {r['status']} | {r['snaps']} | {r['runs']} | "
                  f"{r['s610']} / {r['all10']} | {r['s609']} | {r['blind']} | {r['claude']} ({r['claude_chk']}) | "
                  f"{r['real']} | {r['strongest']} |")
    md.append("")
(OUT / "S6_CASE.md").write_text("\n".join(md) + "\n", encoding="utf-8")
print("written: CHECKEDNESS_LEDGER.tsv, CHECKEDNESS_EVENTS.tsv, LEAST_CHECKED.md, S6_CASE.md, checkedness_stats.json")
for line, c in stats["proved_by_line"].items():
    print(line, dict(c))
