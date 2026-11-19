"""Sweep 2, task 1: close the dependency graph (Claude Opus 5.5 at effort max, 18 Nov 2026).
Reads the register (read-only), the runs' results tables and prompts; writes GRAPH_EDGES.tsv, UNRESOLVED.tsv and
tools/resolve_stats.txt in results_register/sweep2_global/."""
import sys, re, csv, collections, json
sys.path.insert(0, r"C:\Users\user\Documents\results_register\sweep2_global\tools")
import core
from core import ROWS, BYTAG, RUNS, IDS, find_id, ids_in, cross_refs, ID_RE, RANGE_RE, ALIAS

OUTD = core.OUT
PRED = {"S6_02_PUSH": "S6_02_FAMILY", "LM7_PUSH": "LM7_FERMAT_TOWER", "LM8_PUSH": "LM8_LIE_APPROXIMATIONS",
        "LM4_SUCCESSOR": "LM4_FINITE_GROUP_ACTIONS", "ANABELIAN_A1_SUCCESSOR": "ANABELIAN_A1", "TOTEX2": "TOTEX",
        "SECTION_GHOSTS": "SECTIONS_OVER_Q", "ANABELIAN_SUCCESSOR": "ANABELIAN_149_PUSH",
        "ANABELIAN_149_PUSH": "FLAGGED_149", "FERMAT_SUCCESSOR": "LM6_POINTS_AS_SECTIONS",
        "GT_TOWER_CHECK": "EXIT_TOWER", "EXIT_TOWER": "EXIT_ONE_TYPE"}
SEXTRA = core.load_extra()


def norm_text(s):
    s = (s or "").replace("\\_", "_").replace("~", " ").replace("−", "-")
    s = re.sub(r"\\(?:textup|emph|textbf|textit|mathrm)\{([^{}]*)\}", r"\1", s)
    # glued forms such as POLESB.2B.5
    s = re.sub(r"\b(" + "|".join(sorted((re.escape(r) for r in RUNS), key=len, reverse=True)) + r")([A-Z]\.\d)", r"\1 \2", s)
    s = re.sub(r"(\.\d+)([A-Z]\.\d)", r"\1 \2", s)      # B.2B.5 -> B.2 B.5 (P3F.22 stays whole)
    return s


# ---------- prompt rows: R1.., L1.., Lead k -> the tags they name ----------
PROMPT_ROWS = {}   # run -> {key: (text, [tags])}
for run in RUNS:
    p, rr = core.PR.prompt_rows(run)
    tab = {}
    for k, v in rr.items():
        t = norm_text(v)
        tags = []
        # the row's sources are in its leading parenthesis: "R4 (LM7_PUSH E.65; refereed ...). ... LM7_PUSH E.3, open, is
        # exactly ..." uses E.65 and only names E.3. Only when the parenthesis names no item is the whole row read.
        par = re.match(r"\s*(?:\*\*)?\s*\(((?:[^()]|\([^()]*\))*)\)", t)
        src = par.group(1) if par else ""
        for (orun, oid, a, b) in cross_refs(src, run):
            if oid:
                tags.append(f"{orun}:{oid}")
        if not tags and src:
            # "(SECTIONS_OVER_Q checkpoint 17). A.44: ..." names its run in the parenthesis and its ids after it
            named = [a for a in ALIAS if re.search(r"(?<![A-Za-z0-9_])" + re.escape(a) + r"(?![A-Za-z0-9_])", src) and len(a) >= 4]
            if named:
                cand_runs = ALIAS[max(named, key=len)]
                after = t[par.end():par.end() + 400]
                for r2 in cand_runs:
                    got = ids_in(r2, after)
                    if got:
                        tags = [f"{r2}:{i}" for i in got]
                        break
        if not tags and run in PRED and src:
            tags = [f"{PRED[run]}:{i}" for i in ids_in(PRED[run], src)]
        if not tags and not par:
            for (orun, oid, a, b) in cross_refs(t, run):
                if oid:
                    tags.append(f"{orun}:{oid}")
        tab[k] = (v, list(dict.fromkeys(tags)))
        if k.startswith("Lead "):
            tab["L" + k.split()[1]] = tab[k]
    PROMPT_ROWS[run] = (str(p.relative_to(core.DOC)) if p else "", tab)

# ---------- classification of a reference fragment ----------
LIT_SRC = re.compile(
    r"(?<![A-Za-z])(SGA\s?\d|SGA|EGA|FGA|HTT|HA|SAG|Stacks|Kerodon|Tag\s?[0-9A-Z]{4}|bib:|external|BC_|CF_|LA_|ROOT_|FF_|AR_|AG_|AC_|"
    r"A_[A-Z]|F-[A-Z]|R-[A-Z]|arXiv|Milne|Serre|Silverman|Neukirch|Hartshorne|Lurie|Cisinski|Maltsiniotis|Quillen|Stix|"
    r"Mochizuki|Nakamura|Tamagawa|Ihara|Drinfeld|Deligne|Faltings|Harbater|Schneps|Lochak|Boggi|Zalesskii|Farb|Margalit|"
    r"Hatcher|Goerss|Jardine|Heller|Thomason|Isbell|Mitchell|Adámek|Ad\\'amek|Kaledin|Bousfield|Kan|Dwyer|Riehl|Verity|"
    r"Joyal|Lenz|Raptis|Bellingeri|Saïdi|Saidi|Tsujimura|Hoshi|Minamide|Harari|Stoll|Ribet|Wittenberg|Harpaz|"
    r"Mazur|Kisin|Wiles|Coleman|Anderson|Ihara|Kaneko|Ichimura|Otsubo|Ross|Gross|Rohrlich|Fontaine|Jannsen|Kahn|Priddy|"
    r"Ravenel|Miller|Snaith|Boyde|James|Leary|Baumslag|Dyer|Heath|Bartholdi|Mikhailov|Engel|Peters|Grauert|Chen|Graf|"
    r"Kovacs|Thomas|Motohashi|Gorodnik|Nevo|Carneiro|Vaaler|Lekkas|Petridis|Atiyah|Hirzebruch|LeBrun|Bryant|Calabi|"
    r"Gray|Steinberg|Hubicka|Nesetril|Fra[iï]ss[eé]|Street|Walters|Berger|Kaufmann|Chacholski|Scherer|May|Stephan|"
    r"Zakharevich|Dominguez|Segovia|Yang|Katz|Lang|Illusie|Temkin|Carlson|Haine|Wolf|Bakalov|Kirillov|Jansen|Kerckhoff|"
    r"Herfort|Ribes|Collas|Marin|Tsunogai|Yasuda|Geyer|Cornut|Baker|Petsche|Matsumoto|Oda|Pop|Hensel|Kuhlmann|Jarden|"
    r"Calegari|Dimitrov|Tang|Zywina|Poonen|Nekovar|Bloch|Kato|Soulé|Hain|Pridham|Wojtkowiak|Furusho|Brown|Goncharov|"
    r"Hochschild|Shapiro|Tate|Weil|Lefschetz|Grothendieck|Bourbaki|Kurosh|Higman|Neumann|Hall|Gaschütz|Wilson|"
    r"Fried|Völklein|Malle|Matzat|Belyi|Birman|Dehn|Nielsen|Thurston|Teichm|Harer|Mumford|Knudsen|Deligne|Hain)")
LIT_LOC = re.compile(r"(Theorem|Thm|Lemma|Lem|Proposition|Prop|Corollary|Cor|Remark|Rem|Example|Ex\.|Definition|Def|"
                     r"Section|Sect|§|Appendix|Chapter|Ch\.|Exercise|Eq|eq\.|equation|p\.|pp\.|page|Tag\s?[0-9A-Z]{4}|"
                     r"\b[IVX]+\s?\.?\s?\d|\b\d+\.\d+|\[\d|Main Theorem)")
HIS = re.compile(r"(\bcote\s?\d|\bMPL\s?\d|\bscans?\s?\d|\bfolios?\b|\bfols?\.\s?\d|\bmanuscript\s?(?:p|pp|page)|"
                 r"\bms\.\s?\d|\b[IVX]{1,5}\s?ms\.|\bLM\s?(?:scan|folio|§|section)|\bhis (?:page|text|manuscript|claim))", re.I)
CODE = re.compile(r"(code/|\.py\b|\.sage\b|\.gp\b|\.m\b|\.json\b|\.cpp\b|\.out\b|certificate|computer algebra|GAP\b|Magma\b|"
                  r"PARI|Sage\b|program|script|interval arithmetic|exact computation|computed)", re.I)
STD = re.compile(r"(theorem|lemma|formula|duality|reciprocity|sequence|criterion|principle|bound|inequality|"
                 r"Yoneda|Riemann|Hurwitz|Hilbert|Nakayama|Kummer|Hensel|Chebotarev|Dirichlet|Frattini|Schur|Sylow|"
                 r"Burnside|Zorn|Whitehead|Hurewicz|Seifert|van Kampen|Mayer|Vietoris|Künneth|Serre spectral|Lyndon|"
                 r"Hochschild|Shapiro|Poincaré|Lefschetz|Grothendieck|Quillen|Dold|Kan|Morita|Galois|Brauer|Tate|"
                 r"Weil|Néron|Ogg|Shafarevich|Faltings|Mordell|Siegel|Baker|Thue|Mazur|Merel|Ihara|Belyi|Fermat)", re.I)


def classify_rest(rest):
    """class of a fragment with no internal id: (kind, normalized target or reason)"""
    r = rest.strip(" ,;.()[]")
    if not r or r.lower() in ("none", "n/a", "-", "definitions", "definitions only", "nothing"):
        return None
    if HIS.search(r):
        return ("cites his place", r)
    if LIT_SRC.search(r):
        if LIT_LOC.search(r):
            return ("cites literature", r)
        return ("unresolved:literature named without locator", r)
    if CODE.search(r):
        return ("uses computation", r)
    if STD.search(r):
        return ("unresolved:standard result named without locator", r)
    return ("unresolved:proof step described, no item named", r)


PROMPT_ROW_RE = re.compile(r"(?<![A-Za-z0-9.:\-_\\])((?:R|L)\d+[a-z]?|Lead\s+\d+[a-z]?)(?![.\d:A-Za-z_])")
LITKEY = re.compile(r"(?<![A-Za-z0-9.])(?:[A-Za-z]{1,3}_)?(?:[A-Z]{2,6}[a-z]?(?:19|20)?\d{2}|[a-z]{0,2}[A-Z][a-zà-ÿ]+(?:[-–][A-Z][a-zà-ÿ]+)*(?:19|20)\d{2}[a-z]?)(?![\d.])")
NOTATION = re.compile(r"[A-Z]\d{1,2}|[A-Z]{1,2}\d?\([A-Za-z0-9_^]+\)")


def row_ref_ids(run, key, after):
    """'R6 C.3.3': the id after a prompt row, in the run(s) that the row names"""
    tab = PROMPT_ROWS.get(run, ("", {}))[1]
    if key not in tab:
        return []
    runs = list(dict.fromkeys(tg.split(":", 1)[0] for tg in tab[key][1]))
    m = re.match(r"\s*(" + ID_RE + r"(?:\s*(?:,|and|–|--|-|—|to|&)\s*(?:" + ID_RE + r"|\d+))*)", after)
    if not m or not runs:
        return []
    out = []
    for r2 in runs:
        got = ids_in(r2, m.group(1))
        out += [f"{r2}:{i}" for i in got]
    return out


def resolve_fragment(run, frag, field):
    """[(kind, to, how)] for one fragment of a reference field"""
    out = []
    t = norm_text(frag)
    # file names (ANABELIAN_A1_SUCCESSOR_paper.tex, sections/A.tex) name places in the return, not items
    t = re.sub(r"[\w./\-]+\.(?:tex|pdf|py|md|csv|json|out|sage|cpp|txt)", " ", t)
    # 1. cross-run references
    spans = []
    for (orun, oid, a, b) in cross_refs(t, run):
        spans.append((a, b))
        if oid:
            out.append(("uses" if field in ("depends_on", "where_proved") else "names", f"{orun}:{oid}", "cross-run alias"))
        else:
            out.append(("unresolved:cross-run id not found in the named run", f"{orun}: {t[a:b]}", "cross-run alias"))
    rest = t
    for a, b in sorted(spans, reverse=True):
        rest = rest[:a] + " " + rest[b:]
    # 2. literature marker: ids after it are locators, not ours
    lm = LIT_SRC.search(rest)
    lk = LITKEY.search(rest)
    if lk and (not lm or lk.start() < lm.start()):
        lm = lk
    head = rest[:lm.start()] if lm else rest
    # 3. prompt rows (R1, L15, Lead 3); 'R6 C.3.3' is the id C.3.3 of the run that R6 names
    tab = PROMPT_ROWS.get(run, ("", {}))[1]
    rel_kind = "uses" if field in ("depends_on", "where_proved") else "names"
    for m in list(PROMPT_ROW_RE.finditer(head)):
        key = re.sub(r"\s+", " ", m.group(1))
        if find_id(run, key, parent=False) or key not in tab:
            continue                 # an id of the run itself, or notation (L3, R2 as a ring), not a prompt row
        after = head[m.end():m.end() + 80]
        specific = row_ref_ids(run, key, after)
        if specific:
            for tg in specific:
                out.append((rel_kind, tg, f"prompt row {key} with an id of the run it names"))
            mm = re.match(r"\s*(" + ID_RE + r"(?:\s*(?:,|and|–|--|-|—|to|&)\s*(?:" + ID_RE + r"|\d+))*)", after)
            head = head[:m.start()] + " " * (m.end() - m.start() + (len(mm.group(0)) if mm else 0)) + head[m.end() + (len(mm.group(0)) if mm else 0):]
            continue
        tags = tab[key][1]
        if tags:
            for tg in tags:
                out.append((rel_kind, tg, f"prompt row {key}"))
        else:
            out.append(("answers prompt item", f"PROMPT:{run}:{key}", "prompt row (no tag)"))
        head = head[:m.start()] + " " * (m.end() - m.start()) + head[m.end():]
    # 4. own ids, then the predecessor's, then the prompt rows' tags
    found = []
    how_of = {}
    for m in RANGE_RE.finditer(head):
        got = core.expand_range(run, m.group(1), m.group(2))
        if got:
            found += got
            head = head.replace(m.group(0), " ", 1)
    for m in re.finditer(r"(?<![A-Za-z0-9_])(?:" + ID_RE + r")(?![_A-Za-z0-9])", head):
        tok = m.group(0)
        i = find_id(run, tok)
        if i:
            found.append(i)
            if core.HOW.get((run, tok)):
                how_of[i] = f"own id ({tok} read as its {core.HOW[(run, tok)]} {i})"
            continue
        if NOTATION.fullmatch(tok) or ("." not in tok and ":" not in tok and frag.strip(" .;,()") != tok):
            continue                 # F3, SL2, GT0, PD2, Q576: notation, not an item
        if re.fullmatch(r"[A-Z]{3,}\d+(?:\.\d+)*", tok) or head[max(0, m.start() - 2):m.start()] in ("\S", "§", "\S "):
            continue                 # GPS6.1, CCS7.2: a source key and section; \S4.2: a section of the paper
        # not ours: try the tags of the prompt rows, then the predecessor run
        cand = sorted({tg for (_, tgs) in tab.values() for tg in tgs if tg.split(":", 1)[1] == tok})
        if len(cand) == 1:
            out.append((rel_kind, cand[0], "bare id found in the prompt rows"))
            continue
        ctx = [r2 for r2 in ROW_CTX.get(CUR[0], []) if find_id(r2, tok)]
        if len(ctx) == 1:
            out.append((rel_kind, f"{ctx[0]}:{find_id(ctx[0], tok)}", "bare id; its run is named elsewhere in the row"))
            continue
        if run in PRED and find_id(PRED[run], tok):
            out.append((rel_kind, f"{PRED[run]}:{find_id(PRED[run], tok)}", "bare id found in the predecessor run"))
            continue
        pr = [r2 for r2 in PROMPT_RUNS.get(run, []) if find_id(r2, tok)]
        if len(pr) == 1:
            out.append((rel_kind, f"{pr[0]}:{find_id(pr[0], tok)}", "bare id; the only run named in the prompt that has it"))
            continue
        if re.fullmatch(r"[A-Z]{1,3}\d*(?:\.\d+)+[a-z]?|[A-Z]{1,2}\d+", tok) and not re.fullmatch(r"[IVX]+\d*(?:\.\d+)*", tok):
            others = [r2 for r2 in RUNS if r2 != run and find_id(r2, tok)]
            out.append(("unresolved:id not in its run", f"{run}: {tok}", "candidates: " + ",".join(others[:6]) if others else "no run has it"))
    for i in dict.fromkeys(found):
        if field in ("depends_on", "where_proved"):
            out.append(("uses", f"{run}:{i}", how_of.get(i, "own id")))
    # 5. what is left
    leftover = re.sub(r"(?<![A-Za-z0-9])(?:" + ID_RE + r")", " ", rest)
    leftover = re.sub(r"\s+", " ", leftover).strip(" ,;.()[]")
    if leftover and field == "depends_on":
        c = classify_rest(leftover if not lm else rest[lm.start():] if not head.strip(" ,;.") else leftover)
        if c and not (c[0].startswith("unresolved:proof step") and found and len(leftover) < 4):
            out.append((c[0], c[1][:200], "fragment class"))
    return out


REL_PATTERNS = [
    ("checks", r"confirm|check|audit|verif|followed|re-?derived|recomput|rechecked|read in full|proofs? read"),
    ("refutes", r"refut|counterexample to|is false|fails for|disprov|false as stated"),
    ("corrects", r"correct(?:s|ed|ion)\b|repair|erratum|gap in|replaces? the (?:flawed|false)"),
    ("strengthens", r"strengthen|sharpen|improv|generali[sz]|extends? |stronger|removes? the (?:hypothesis|assumption)"),
    ("refines", r"refine|precise form|exact form|special case|restricted form"),
    ("restates", r"restat|same (?:statement|as|result)|is exactly|identical|re-?prov|reproduc|recover|equivalent to"),
]
NEG = re.compile(r"\b(not|no|without|neither|nor|never|does not|did not|cannot)\b[^.;]{0,25}$")


def relation(text, a, b, own_status):
    """the relation named by the words just before (and right after) a reference; negated words are skipped"""
    before = text[max(0, a - 70):a].lower()
    after = text[b:b + 30].lower()
    for kind, pat in REL_PATTERNS:
        for m in re.finditer(pat, before):
            if not NEG.search(before[:m.start()]):
                return kind
    for kind, pat in REL_PATTERNS:
        m = re.search(pat, after)
        if m and not NEG.search(after[:m.start()]):
            return kind
    return None


PROMPT_RUNS = {run: list(dict.fromkeys(tg.split(":", 1)[0] for (_, tgs) in tab.values() for tg in tgs))
               for run, (_, tab) in PROMPT_ROWS.items()}
ROW_CTX = {}
CUR = [None]
for _r in ROWS:
    _t = norm_text(" ".join(_r.get(k, "") or "" for k in ("statement", "notes", "depends_on", "where_proved", "his_places")))
    ROW_CTX[_r["tag"]] = list(dict.fromkeys(x[0] for x in cross_refs(_t, _r["run"]) if x[1]))
edges = []
unres = []
seen = set()
old = set()
with open(core.RR / "EDGES.tsv", encoding="utf-8", newline="") as f:
    for e in csv.DictReader(f, delimiter="\t"):
        old.add((e["from"], e["to"]))


def add(frm, to, kind, field, how, ev):
    key = (frm, to, kind)
    if key in seen or frm == to:
        return
    seen.add(key)
    if kind.startswith("unresolved:"):
        unres.append((frm, field, kind.split(":", 1)[1], to, how, ev))
    else:
        edges.append((frm, to, kind, field, how, "yes" if (frm, to) in old else "", ev))


for r in ROWS:
    tag, run = r["tag"], r["run"]
    CUR[0] = tag
    # depends_on and where_proved: the dependencies
    for field in ("depends_on", "where_proved"):
        val = r.get(field, "") or ""
        if not val.strip():
            continue
        for frag in re.split(r";|\s\|\s", val):
            if not frag.strip():
                continue
            for kind, to, how in resolve_fragment(run, frag, field):
                if field == "where_proved" and kind not in ("uses", "names") and not kind.startswith("unresolved:cross"):
                    continue          # where_proved names files and sections; only its item references are kept
                add(tag, to, kind, field, how, frag.strip()[:200])
    # statement, notes: names of other runs' items, with the relation read from the words around them
    for field in ("statement", "notes"):
        t = norm_text(r.get(field, ""))
        for (orun, oid, a, b) in cross_refs(t, run):
            if not oid:
                add(tag, f"{orun}: {t[a:b]}", "unresolved:cross-run id not found in the named run", field, "cross-run alias", t[max(0, a - 60):b + 40])
                continue
            rel = relation(t, a, b, r["status"]) or "names"
            add(tag, f"{orun}:{oid}", rel, field, "cross-run alias, relation from the words around it", t[max(0, a - 80):b + 40])
        for m in PROMPT_ROW_RE.finditer(t):
            key = re.sub(r"\s+", " ", m.group(1))
            tab = PROMPT_ROWS.get(run, ("", {}))[1]
            if key in tab and tab[key][1] and not find_id(run, key, parent=False):
                specific = row_ref_ids(run, key, t[m.end():m.end() + 80])
                rel = relation(t, m.start(), m.end(), r["status"]) or "names"
                for tg in (specific or tab[key][1]):
                    add(tag, tg, rel, field, f"prompt row {key}" + (" with an id of the run it names" if specific else ""),
                        t[max(0, m.start() - 80):m.end() + 40])
    # extra columns: continuations and answers
    ex = SEXTRA.get(tag, {})
    for k, v in ex.items():
        v = (v or "").strip()
        if not v or v.lower() in ("none", "-", "n/a"):
            continue
        if k.startswith("A1_id"):
            i = find_id("ANABELIAN_A1", v)
            if i:
                add(tag, f"ANABELIAN_A1:{i}", "restates", k, "continues the checkpoint-03 number (A1_id column)", v)
        elif k.startswith("answers") or k.startswith("item_of_the_prompt") or k.startswith("R_items"):
            tab = PROMPT_ROWS.get(run, ("", {}))[1]
            for piece in re.split(r"[;,]", v):
                piece = piece.strip()
                if not piece:
                    continue
                key = re.sub(r"\s+", " ", piece)
                if key in tab and tab[key][1]:
                    for tg in tab[key][1]:
                        add(tag, tg, "answers prompt item", k, f"answers {key}", v[:200])
                else:
                    add(tag, f"PROMPT:{run}:{key[:60]}", "answers prompt item", k, "answers (no tag)", v[:200])
    # his places column
    hp = (r.get("his_places") or "").strip()
    if hp and hp.lower() not in ("none", "-", "n/a", "none."):
        if HIS.search(norm_text(hp)) or re.search(r"\b1[0-9]{2}\b\s*;|\bcote|\bms\.|§|scan|folio", hp, re.I):
            add(tag, f"PLACE: {hp[:200]}", "cites his place", "his_places", "manuscript column", hp[:200])
        for (orun, oid, a, b) in cross_refs(norm_text(hp), run):
            if oid:
                add(tag, f"{orun}:{oid}", "names", "his_places", "cross-run alias in the manuscript column", hp[:200])

cols = ["from", "to", "kind", "field", "how", "in_sweep0", "evidence"]
with open(OUTD / "GRAPH_EDGES.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(cols)
    for e in edges:
        w.writerow([re.sub(r"\s+", " ", str(x)) for x in e])
with open(OUTD / "UNRESOLVED.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["tag", "field", "class", "fragment", "how", "evidence"])
    for u in unres:
        w.writerow([re.sub(r"\s+", " ", str(x)) for x in u])
with open(OUTD / "tools" / "prompt_rows.json", "w", encoding="utf-8") as f:
    json.dump({k: {"prompt": v[0], "rows": {kk: {"text": vv[0][:400], "tags": vv[1]} for kk, vv in v[1].items()}}
               for k, v in PROMPT_ROWS.items()}, f, ensure_ascii=False, indent=1)
st = collections.Counter(e[2] for e in edges)
su = collections.Counter(u[2] for u in unres)
cross = sum(1 for e in edges if ":" in e[1] and e[1].split(":")[0] in RUNS and e[1].split(":")[0] != e[0].split(":")[0])
lines = [f"edges {len(edges)}; cross-run {cross}; unresolved {len(unres)}", "edges by kind:"]
lines += [f"  {k}\t{v}" for k, v in st.most_common()]
lines += ["unresolved by class:"] + [f"  {k}\t{v}" for k, v in su.most_common()]
(OUTD / "tools" / "resolve_stats.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
