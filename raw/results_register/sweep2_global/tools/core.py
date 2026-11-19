"""Core of sweep 2 (Claude Opus 5.5 at effort max, 18 Nov 2026): ids, aliases, reference parsing.
Read-only on every input; writes nothing."""
import sys, re, csv, collections
sys.path.insert(0, r"C:\Users\user\Documents\results_register\sweep2_global\tools")
from load import *  # noqa
import prompts as PR  # noqa


def norm_status(s):
    s = (s or "").strip()
    if not s:
        return "?"
    w = s.split()[0].strip(".,;:()")
    syn = {"false": "Refuted", "undecided": "Open", "verified": "Proved", "computed": "Proved"}
    if w.lower() in syn:
        return syn[w.lower()]
    for k in ("Proved", "Refuted", "Known", "Open", "Conditional", "Unresolved"):
        if w.lower().startswith(k.lower()):
            return k
    return w[:20]


def one_line(s, n=None):
    s = re.sub(r"\s+", " ", (s or "").replace("\t", " ")).strip()
    return s if n is None else s[:n]


def load_all():
    rows = load_register()
    for r in rows:
        r["supplementary"] = ""
    # FINMON is absent from the register: its checkpoint-20 folder holds encoded files; the decoded table is read here.
    with open(FINMON_RESULTS, encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            rid = (row.get("id") or "").strip()
            if not rid:
                continue
            rows.append(dict(
                tag=f"FINMON:{rid}", run="FINMON", line="Derivateurs", id=rid, status=norm_status(row.get("status")),
                status_raw=one_line(row.get("status"), 120), statement=one_line(row.get("statement")),
                where_proved=one_line(row.get("where_proved"), 300), depends_on=one_line(row.get("depends_on"), 500),
                uses="", lineage="", his_places=one_line(row.get("manuscript_pages_settled"), 300),
                check_events="0", check_types="", check_docs="0", check_doc_kinds="", same_statement="",
                notes=one_line(row.get("notes"), 400),
                ret="derivateurs_companion_20261109/pro_prompts_max_20261112_work/FINMON/FINMON_checkpoint_20_decoded_20261117",
                ret_kind="checkpoint", ret_num="20", stamp="20261117T0241Z",
                results="derivateurs_companion_20261109/pro_prompts_max_20261112_work/FINMON/FINMON_checkpoint_20_decoded_20261117/FINMON_results.csv",
                supplementary="1"))
    return rows


ROWS = load_all()
BYTAG = {r["tag"]: r for r in ROWS}
RUNS = sorted({r["run"] for r in ROWS})
IDS = collections.defaultdict(set)
for r in ROWS:
    IDS[r["run"]].add(r["id"])


def nkey(i):
    return re.sub(r"[\s.\-_:]", "", i).upper()


NORM = collections.defaultdict(lambda: collections.defaultdict(set))
for _run in RUNS:
    for _i in IDS[_run]:
        NORM[_run][nkey(_i)].add(_i)

# run aliases, in the order a bare alias is tried
ALIAS = {
    "LM1": ["LM1_GROUP_SCHEMES_rerun_20261112"], "LM1_GROUP_SCHEMES": ["LM1_GROUP_SCHEMES_rerun_20261112"],
    "LM2": ["LM2_LOOP_EQUATIONS"], "LM4": ["LM4_FINITE_GROUP_ACTIONS", "LM4_SUCCESSOR"],
    "LM5": ["LM5_MULTI_GALOIS_TOPOI"], "LM6": ["LM6_POINTS_AS_SECTIONS"], "LM7": ["LM7_FERMAT_TOWER", "LM7_PUSH"],
    "LM8": ["LM8_LIE_APPROXIMATIONS", "LM8_PUSH"], "LM4_FINITE": ["LM4_FINITE_GROUP_ACTIONS"],
    "TOTASPH": ["TOTAL_ASPHERICITY"], "TOTAL_ASPH": ["TOTAL_ASPHERICITY"], "TOTAL_EXACT": ["TOTEX"],
    "TOTAL_EXACT_2": ["TOTEX2"], "PRESHEAF_TOTALITY": ["PRETOT"], "REVERSIBLE_LOCALIZERS": ["REVLOC"],
    "FRAISSE_EXACT": ["FREX"], "F149": ["FLAGGED_149"], "FLAGGED": ["FLAGGED_149"], "SECTIONS": ["SECTIONS_OVER_Q"],
    "GHOSTS": ["SECTION_GHOSTS"], "DELTA": ["DELTA_ON_GT"], "CK": ["CYCLOTOMIC_KERNEL"],
    "CYCLOTOMIC": ["CYCLOTOMIC_KERNEL"], "AS": ["ANABELIAN_SUCCESSOR"], "AP": ["ANABELIAN_149_PUSH"],
    "AN": ["ANABELIAN_SUCCESSOR", "ANABELIAN_149_PUSH"], "ANABELIAN": ["ANABELIAN_SUCCESSOR", "ANABELIAN_149_PUSH"],
    "ANABELIAN_149": ["ANABELIAN_149_PUSH"], "A1": ["ANABELIAN_A1"], "EXIT": ["EXIT_TOWER", "EXIT_ONE_TYPE"],
    "EXIT_ONE": ["EXIT_ONE_TYPE"], "DF": ["DER_FOLLOWUP"], "DL": ["DER_LOCALIZERS"], "GT": ["GT_TOWER_CHECK"],
    "S6_01": ["S6_01_INVARIANTS"], "S6_02": ["S6_02_FAMILY", "S6_02_PUSH"], "S6_03": ["S6_03_CDP"],
    "S6_04": ["S6_04_MAPS_MANIFOLDS"], "S6_05": ["S6_05_ARITHMETIC"], "S6_06": ["S6_06_BLIND"],
    "Q03": ["Q03_DEPOSIT"],
}
for _run in RUNS:
    ALIAS.setdefault(_run, [_run])
# short aliases that are ordinary words or group names elsewhere: only with a hyphen or colon right after them
WEAK = {"AS", "AP", "A1", "GT", "DF", "DL", "AN", "CK"}
ID_RE = (r"[A-Z]{1,4}\d*[A-Z]{0,3}(?:\.(?:\d+|[A-Z]{1,3}\d*|[a-z]{1,2}\d+))+[a-z]?(?:\([ivxa-h]+\))?"
         r"|[A-Z]\d+[a-z]+\d*(?:-[a-z]+)*"
         r"|[A-Z]{1,3}\d+[a-z]?(?:\.\d+)*(?:\([ivxa-h]+\))?"
         r"|[A-Z]\d*:[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*")
ALIAS_RE = re.compile(
    r"(?<![A-Za-z0-9_\\])(" + "|".join(sorted((re.escape(a) for a in ALIAS), key=len, reverse=True)) + r")"
    r"((?:\\_|[\s:~]|-(?=[A-Z]))+)(?:checkpoint\s*\d+\s*)?\(?(" + ID_RE + r")")


HOW = {}


def find_id(run, tok, parent=True):
    """the id of run that tok names, or None. HOW[(run, tok)] records 'parent' or 'dotted' matches."""
    if not tok:
        return None
    t = re.sub(r"\([ivxa-h]+\)\)?$", "", tok.strip(" .,;[]{}*`")).strip(" .,;()[]{}*`")
    if t in IDS[run]:
        return t
    c = NORM[run].get(nkey(t))
    if c and len(c) == 1:
        return next(iter(c))
    if run == "ANABELIAN_SUCCESSOR" and t.startswith("FF."):
        return find_id(run, "F." + t[3:], parent)
    m = re.fullmatch(r"([A-Z]{1,2})(\d+)\.(\d+)", t)          # E25.1 -> E.25.1
    if m:
        for cand in (f"{m.group(1)}.{m.group(2)}.{m.group(3)}", f"{m.group(1)}.{m.group(2)}"):
            if cand in IDS[run]:
                HOW[(run, tok)] = "dotted"
                return cand
    m = re.fullmatch(r"(.*\.\d+)[a-z](?:\d+|-[a-z])?", t)              # D.37f, D.2.22t19, D.2.45e-k -> the row
    if parent and m and m.group(1) in IDS[run]:
        HOW[(run, tok)] = "parent"
        return m.group(1)
    if parent and t.count(".") >= 2:                            # E.97.1 -> E.97 (a part of the row)
        p = t.rsplit(".", 1)[0]
        while p.count(".") >= 1:
            if p in IDS[run]:
                HOW[(run, tok)] = "parent"
                return p
            p = p.rsplit(".", 1)[0]
    return None


RANGE_RE = re.compile(r"(?<![A-Za-z0-9])(" + ID_RE + r")\s*(?:–|--|-|—|to)\s*([A-Z]{0,4}[\d.]*\d)\b")


def expand_range(run, a, b):
    """ids of run from a to b (b a full id or a bare number)"""
    ma = re.match(r"^(.*?)(\d+)$", a)
    mb = re.match(r"^(.*?)(\d+)$", b)
    if not ma or not mb:
        return []
    pre, n1 = ma.group(1), int(ma.group(2))
    preb, n2 = mb.group(1), int(mb.group(2))
    if preb and nkey(preb) != nkey(pre):
        return []
    if not (0 <= n2 - n1 <= 150):
        return []
    out = []
    for k in range(n1, n2 + 1):
        i = find_id(run, f"{pre}{k}")
        if i:
            out.append(i)
    return out


def ids_in(run, text):
    """ids of run named in a text fragment, ranges expanded"""
    out = []
    for m in RANGE_RE.finditer(text):
        out += expand_range(run, m.group(1), m.group(2))
    for m in re.finditer(r"(?<![A-Za-z0-9_])(?:" + ID_RE + r")(?![_A-Za-z0-9])", text):
        i = find_id(run, m.group(0))
        if i:
            out.append(i)
    return list(dict.fromkeys(out))


ID_LIST = re.compile(r"((?:" + ID_RE + r")(?:(?:\s*(?:,|and|–|--|-|—|to|&|/)\s*|\s+)(?:" + ID_RE + r"|\d+(?:\.\d+)*(?![\w])))*)")


def cross_refs(text, own_run):
    """[(run, id or None, start, end)] for 'ALIAS id(, id)*' in text.
    A bare alias goes to the first candidate run that has the id."""
    out = []
    for m in ALIAS_RE.finditer(text):
        alias, sep = m.group(1), m.group(2)
        if alias in WEAK and not re.search(r"[-:]", sep):
            # a short alias with a space only before a dotted id of the run it names (AN D.30, GT C.2.1, DF A.4)
            if not (alias in ("AN", "GT", "DF", "DL") and "." in m.group(3)) and alias != "CK":
                continue
        cands = ALIAS[alias]
        tail = text[m.start(3):]
        mm = ID_LIST.match(tail)
        seg = mm.group(1) if mm else m.group(3)
        hit = False
        for run in cands:
            if run == own_run and len(cands) > 1:
                continue
            got = ids_in(run, seg)
            if got:
                out += [(run, i, m.start(), m.start(3) + len(seg)) for i in got]
                hit = True
                break
        if not hit:
            out.append(("|".join(cands), None, m.start(), m.start(3) + len(seg)))
    return out
