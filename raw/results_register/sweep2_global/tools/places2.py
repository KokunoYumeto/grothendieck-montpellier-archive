"""Sweep 2, task 4: HIS_PLACES.tsv and PLACES_INDEX.tsv. Every place in his manuscripts that a row names, normalized
per run format, with the transcription that holds it and his first words there (a few words, from the transcription
inventory). Claude Opus 5.5 at effort max, 18 Nov 2026. Read-only on every input."""
import sys, re, csv, json, collections, pathlib
sys.path.insert(0, r"C:\Users\user\Documents\results_register\sweep2_global\tools")
import core
from core import ROWS

csv.field_size_limit(10 ** 9)
DOC = core.DOC
ARCH = DOC / "grothendieck_archive_transcription_20261110" / "returns"
LMD = DOC / "longue_marche_pro_pilot_20261104"
ROMAN = r"(?:XX|XIX|XVIII|XVII|XVI|XV|XIV|XIII|XII|XI|X|IX|VIII|VII|VI|V|IV|III|II|I)"
DER = {r["run"] for r in ROWS if r["line"] == "Derivateurs"} | {"PRETOT", "TOTEX", "FINMON"}
LM = {"LM1_GROUP_SCHEMES_rerun_20261112", "LM2_LOOP_EQUATIONS", "LM4_FINITE_GROUP_ACTIONS", "LM4_SUCCESSOR",
      "LM5_MULTI_GALOIS_TOPOI", "LM6_POINTS_AS_SECTIONS", "LM7_FERMAT_TOWER", "LM7_PUSH", "LM8_LIE_APPROXIMATIONS", "LM8_PUSH"}
# the run's cote when its column names none (from the prompts)
DEFAULT_COTE = {"ANABELIAN_149_PUSH": "149", "ANABELIAN_A1": "149", "ANABELIAN_A1_SUCCESSOR": "149",
                "ANABELIAN_SUCCESSOR": "149", "CYCLOTOMIC_KERNEL": "149", "FLAGGED_149": "149", "SECTIONS_OVER_Q": "149",
                "SECTION_GHOSTS": "149", "EXIT_ONE_TYPE": "147", "EXIT_TOWER": "147"}
FORMAT = {}   # run -> header of the manuscript column
for r in ROWS:
    if r["run"] in FORMAT:
        continue
    p = core.results_path(r["results"]) if r["run"] != "FINMON" else core.FINMON_RESULTS
    if p:
        with open(p, encoding="utf-8-sig", newline="") as f:
            hdr = next(csv.reader(f))
        FORMAT[r["run"]] = next((h for h in hdr if h.startswith("manuscript")), "")


def nums(s):
    out = []
    for m in re.finditer(r"(\d+)\s*(?:v|r|bis|ter|verso|recto|prime)?\s*(?:(?:[-–—]+|to)\s*(\d+))?", s):
        a = int(m.group(1))
        b = int(m.group(2)) if m.group(2) else None
        if b and b >= a and b - a <= 80:
            out += list(range(a, b + 1))
        else:
            out.append(a)
    return out


def parse(run, s):
    """[(work, cote, scans list, pages text, section text)]"""
    s = s.replace("\\S", "§").replace("~", " ").replace("--", "–").replace("\u2009", " ")
    out = []
    if s.strip().startswith("{") and '"cote"' in s:
        for x in re.findall(r"\{[^{}]*\}", s):
            try:
                d = json.loads(x)
            except Exception:
                continue
            if d.get("cote") or d.get("scan"):
                out.append(("Montpellier archive", d.get("cote") or DEFAULT_COTE.get(run, ""), nums(d.get("scan", "")),
                            d.get("page", ""), ""))
        return out
    fmt = FORMAT.get(run, "")
    if run in DER:
        for m in re.finditer(r"\b(" + ROMAN + r")([a-c]?)(?:-[a-c])?[\s.]*(?:ms\.?|manuscript pages?)?\s*(\d[\d\s,–\-]*(?:bis|ter|quater|quinquies|prime|'|′)?)", s):
            if re.search(r"ms|manuscript|\.", s[m.start():m.end()]) or re.match(r"\s*\d", s[m.end(2):]):
                out.append(("Les Dérivateurs", "", [], m.group(3).strip(" ,"), f"chapter {m.group(1)}{m.group(2)}"))
        for m in re.finditer(r"\b(" + ROMAN + r"[a-c]?)(?:-[a-c])?-([A-Z]\d{3})\b", s):
            out.append(("Les Dérivateurs", "", [], "", f"chapter {m.group(1)}, block {m.group(2)}"))
        for m in re.finditer(r"\b(1[0-6]\d(?:-\d)?)/(\d{3}(?:,\d{3})*)", s):        # 134-8/049,053: cote/scans
            out.append(("Montpellier archive", m.group(1), nums(m.group(2)), "", ""))
        return out
    if run in LM or "folio" in fmt:
        for m in re.finditer(r"(?:§+\s*([0-9][0-9.,\s–]*)|[Ss]ection\s*([0-9][0-9.]*))?[^;]{0,60}?(?:fols?\.?|folios?)\s*([0-9][0-9\s,–\-vr]*(?:verso)?)[^;]{0,30}?scans?\s*([0-9][0-9\s,–\-]*)", s):
            ctx = s[max(0, m.start() - 30):m.end() + 30]
            mc = re.search(r"cote\s*(1[0-9]{2}(?:-\d)?)|MPL\s*(1[0-9]{2})|\b(C[134])\b", ctx)
            if mc and (mc.group(1) or mc.group(2)):
                c = mc.group(1) or mc.group(2)
            elif mc:
                c = {"C1": "140-1", "C3": "140-3", "C4": "140-4"}[mc.group(3)]
            else:
                c = DEFAULT_COTE.get(run, "140-2")
            fol = nums(m.group(3))
            if c == "140-2" and not mc and fol:                       # the folio fixes the volume: 1-292, 293-650, 651-
                c = "140-2" if max(fol) <= 292 else ("140-3" if max(fol) <= 650 else "140-4")
            work = "La Longue Marche" if c.startswith("140") else "Montpellier archive"
            out.append((work, c, nums(m.group(4)), m.group(3).strip(" ,"), (m.group(1) or m.group(2) or "").strip(" ,")))
        for m in re.finditer(r"\b(C[134])\s*(?:§\s*([0-9.]+)\s*,?\s*)?scans?\s*([0-9][0-9\s,–\-]*)", s):
            out.append(("La Longue Marche", {"C1": "140-1", "C3": "140-3", "C4": "140-4"}[m.group(1)], nums(m.group(3)), "",
                        m.group(2) or ""))
        for m in re.finditer(r"\bLM\s*scans?\s*([0-9][0-9\s,–\-]*)", s):
            out.append(("La Longue Marche", "140-2", nums(m.group(1)), "", ""))
        if run in LM and not out:
            m = re.match(r"\s*§+\s*([0-9.]+)\s*;\s*(?:fol\.?|folios?)?\s*([0-9][0-9\s,–\-vr]*)\s*;\s*(?:scans?)?\s*([0-9][0-9\s,–\-]*)", s)
            if m:
                out.append(("La Longue Marche", "140-2", nums(m.group(3)), m.group(2), m.group(1)))
    # archive: explicit cote, or the run's default cote
    for m in re.finditer(r"(?:\bcote\s*|\bMPL\s*)(1?\d{1,2}(?:-\d)?)\b", s):
        tail = s[m.end():m.end() + 160]
        sc = re.search(r"scans?\s*([0-9][0-9\s,–\-]*)", tail)
        pg = re.search(r"manuscript\s*(?:pp?\.)?\s*([0-9][0-9\s,–\-v]*)|pp?\.\s*([0-9][0-9\s,–\-v]*)", tail)
        sec = re.search(r"(?:section|§)\s*([0-9][0-9.]*)", tail)
        out.append(("Montpellier archive", m.group(1), nums(sc.group(1)) if sc else [],
                    ((pg.group(1) or pg.group(2)) if pg else "").strip(" ,"), sec.group(1) if sec else ""))
    if not out and run in DEFAULT_COTE:
        c = DEFAULT_COTE[run]
        if "(cote; page; scan)" in fmt or "(section; page; scan)" in fmt or "(section; folio; scan)" in fmt:
            parts = [p.strip() for p in s.split(";")]
            if len(parts) >= 3 and re.search(r"\d", parts[-1]):
                lead = parts[0]
                cote = c if not re.fullmatch(r"1[0-9]{2}", lead) else lead
                sec = "" if re.fullmatch(r"1[0-9]{2}", lead) else lead
                out.append(("Montpellier archive", cote, nums(parts[2]), parts[1], sec))
        if not out:
            mm = re.match(r"\s*(?:cote\s*)?(1[0-9]{2})\s*;\s*([0-9][0-9\s,–\-]*)(?:;|$)", s)
            if mm:
                out.append(("Montpellier archive", mm.group(1), nums(mm.group(2)), "", ""))
            else:
                sc = re.search(r"scans?\s*([0-9][0-9\s,–\-]*)", s)
                if sc:
                    out.append(("Montpellier archive", c, nums(sc.group(1)), "", ""))
    seen, res = set(), []
    for w, c, scs, pg, sec in out:
        k = (w, c, tuple(scs), pg, sec)
        if k not in seen and (scs or pg or sec):
            seen.add(k)
            res.append((w, c, scs, pg, sec))
    return res


# transcription inventories of the archive returns: (cote, scan) -> (file, heading, first words)
INV = {}
for d in sorted(ARCH.glob("MPL_*_unzipped")):
    m = re.match(r"MPL_(\d+(?:-\d)?)_(\d+)-(\d+)_unzipped$", d.name)
    if not m:
        continue
    cote = m.group(1)
    invs = list(d.glob("*_inventory.csv"))
    if not invs:
        continue
    with open(invs[0], encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            try:
                sc = int(row.get("scan") or 0)
            except ValueError:
                continue
            key = (cote, sc)
            ent = INV.setdefault(key, {"file": str((d / "pages").relative_to(DOC)) + f"\\{d.name[:-9]}_scan{sc:03d}.tex",
                                       "heading": "", "first": ""})
            kind = (row.get("kind") or "").lower()
            w = (row.get("first_words_or_objects") or "").strip()
            if kind == "text" and "heading" in (row.get("position") or "").lower() and not ent["heading"]:
                ent["heading"] = w
            elif kind == "text" and len(re.findall(r"[A-Za-zÀ-ÿ]{2,}", w)) >= 2 and len(ent["first"]) < 90:
                ent["first"] = (ent["first"] + " … " + w) if ent["first"] else w
            elif kind in ("display", "drawing", "diagram") and not ent["first"]:
                ent["first"] = f"[{kind}: {w}]"
            elif kind == "text" and "heading" not in (row.get("position") or "").lower() and re.match(r"\s*\d+\.\s+[A-ZÀ-Ý]", w) and not ent["heading"]:
                ent["heading"] = w
# La Longue Marche packages: (cote, scan) -> package
PKG = {}
for line in (LMD / "PACKAGES.md").read_text(encoding="utf-8").splitlines():
    m = re.match(r"\|\s*(LM_P\d+(?:-\d+)?)\s*\|\s*cote\s*(140-\d)[^|]*\|\s*(\d+)\s*[–-]\s*(\d+)\s*\|", line)
    if m:
        for sc in range(int(m.group(3)), int(m.group(4)) + 1):
            PKG.setdefault((m.group(2), sc), m.group(1))
for d in LMD.glob("LM_C[34]-*"):
    m = re.match(r"LM_C([34])-(\d+)-(\d+)$", d.name)
    if m:
        for sc in range(int(m.group(2)), int(m.group(3)) + 1):
            PKG.setdefault((f"140-{m.group(1)}", sc), d.name)

# one-sentence readings of the most-cited pages, by Claude Opus 5.5 at effort max (sweep 2), from the transcription
SAID = {
    ("149", 35): "He notes that the injectivity (points to sections) holds in characteristic p once radicial parts are inverted, "
                 "but that with prime-to-p fundamental groups the injectivity of (**) is false already for an elliptic curve "
                 "made anabelian by removing a point.",
    ("149", 36): "He suggests that the injectivity of (*) may hold without any hypothesis on the characteristic: in characteristic "
                 "p, two points with the same prime-to-p section differ by p-power torsion of the generalized Jacobian (zero for "
                 "a torus), and the same holds on every prime-to-p cover; he asks whether P = Q follows (the question A1).",
    ("149", 56): "He states Conjecture A: for an anabelian curve U over a field finitely generated over Q, every section comes from "
                 "a rational point or from a rational cusp (with the centralizer precisions 1 and L_i), and derives the birational "
                 "consequence for E_L -> E_K by passing to the limit.",
}
lines = []
for r in ROWS:
    srcs = []
    hp = (r.get("his_places") or "").strip()
    if hp and hp.lower() not in ("none", "-", "n/a", "none."):
        srcs.append(("manuscript column", hp))
    for fld in ("statement", "notes"):
        t = r.get(fld) or ""
        for m in re.finditer(r"(?:cote\s*\d{1,3}(?:-\d)?[^.;]{0,60}?scans?\s*\d[\d\s,–\-]*|\b(?:" + ROMAN + r")\s*ms\.\s*\d[\d\s,–\-]*|\bscans?\s*\d{1,3}(?:\s*[–-]\s*\d{1,3})?)", t):
            srcs.append((fld, m.group(0)))
    for fld, s in srcs:
        for (work, cote, scans, pages, sec) in parse(r["run"], s):
            if fld != "manuscript column" and not cote and work != "Les Dérivateurs":
                cote = DEFAULT_COTE.get(r["run"], "")
                if not cote:
                    continue
            if cote.startswith("140"):
                work = "La Longue Marche"
            first = scans[0] if scans else None
            inv = INV.get((cote, first)) if first is not None else None
            pkg = PKG.get((cote, first)) if first is not None else None
            said = ""
            src = ""
            if (cote, first) in SAID:
                said = SAID[(cote, first)] + " (read by Claude Opus 5.5 at effort max, sweep 2)"
                src = inv["file"] if inv else ""
            elif inv:
                said = (f"heading «{inv['heading'][:60]}»; " if inv["heading"] else "") + (f"begins «{inv['first'][:110]}»" if inv["first"] else "")
                src = inv["file"]
            elif pkg:
                src = f"longue_marche_pro_pilot_20261104\\{pkg} (scan images; transcription in answers\\{pkg}_transcription.tex where returned)"
            if not said:
                said = "row text: " + r["statement"][:160]
            lines.append(dict(tag=r["tag"], status=r["status"], work=work, cote=cote,
                              scans=",".join(map(str, scans[:40])), page_or_folio=pages[:60], section=sec[:60],
                              what_he_says_there=said, source=src, linked_from=fld, raw=s[:160]))
cols = list(lines[0].keys())
with open(core.OUT / "HIS_PLACES.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols, delimiter="\t", lineterminator="\n")
    w.writeheader()
    for l in lines:
        w.writerow({k: re.sub(r"\s+", " ", str(v)) for k, v in l.items()})
idx = collections.defaultdict(list)
for l in lines:
    for sc in (l["scans"].split(",") if l["scans"] else [""]):
        idx[(l["work"], l["cote"], sc, l["page_or_folio"] if not sc else "", l["section"] if l["work"] == "Les Dérivateurs" else "")].append(l)
with open(core.OUT / "PLACES_INDEX.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["work", "cote", "scan", "page_or_folio", "chapter_or_section", "what_he_says_there", "source", "n_tags", "tags"])
    for k, ls in sorted(idx.items(), key=lambda kv: (kv[0][0], kv[0][1], int(kv[0][2]) if kv[0][2].isdigit() else 0, kv[0][3], kv[0][4])):
        work, cote, sc, pg, sec = k
        inv = INV.get((cote, int(sc))) if sc.isdigit() else None
        said = ((f"heading «{inv['heading'][:60]}»; " if inv["heading"] else "") + (f"begins «{inv['first'][:110]}»" if inv["first"] else "")) if inv else ""
        if sc.isdigit() and (cote, int(sc)) in SAID:
            said = SAID[(cote, int(sc))] + " (read by Claude Opus 5.5 at effort max, sweep 2)"
        tags = sorted({l["tag"] for l in ls})
        w.writerow([work, cote, sc, pg, sec, said, inv["file"] if inv else "", len(tags), " ".join(tags)])
print("place lines", len(lines), "tags", len({l['tag'] for l in lines}), "index entries", len(idx))
print(collections.Counter(l["work"] for l in lines))
print("with his first words:", sum(1 for l in lines if not l["what_he_says_there"].startswith("row text")))
print(collections.Counter(l["cote"] for l in lines if l["work"] != "Les Dérivateurs").most_common(20))
