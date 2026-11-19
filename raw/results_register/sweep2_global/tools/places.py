"""Sweep 2, task 4 (by script): parse every manuscript place a row names into (work, cote, scans, pages, section).
Claude Opus 5.5 at effort max, 18 Nov 2026. Writes tools/places_parsed.tsv (one line per tag and place)."""
import sys, re, csv, json, collections
sys.path.insert(0, r"C:\Users\user\Documents\results_register\sweep2_global\tools")
import core
from core import ROWS

DER_RUNS = {r["run"] for r in ROWS if r["line"] == "Derivateurs"} | {"PRETOT", "TOTEX", "FINMON"}
LM_RUNS = {"LM1_GROUP_SCHEMES_rerun_20261112", "LM2_LOOP_EQUATIONS", "LM4_FINITE_GROUP_ACTIONS", "LM4_SUCCESSOR",
           "LM5_MULTI_GALOIS_TOPOI", "LM6_POINTS_AS_SECTIONS", "LM7_FERMAT_TOWER", "LM7_PUSH", "LM8_LIE_APPROXIMATIONS",
           "LM8_PUSH"}
ROMAN = r"(?:XX|XIX|XVIII|XVII|XVI|XV|XIV|XIII|XII|XI|X|IX|VIII|VII|VI|V|IV|III|II|I)"


def rng(s):
    """'35-36, 41' -> [35, 36, 41] (bounded)"""
    out = []
    for a, b in re.findall(r"(\d+)\s*(?:[-–—]+|to)\s*(\d+)|(\d+)", s) and [(m.group(1) or m.group(3), m.group(2) or "")
                                                                           for m in re.finditer(r"(\d+)(?:v|r|bis|ter)?\s*(?:[-–—]+\s*(\d+))?", s)]:
        a = int(a)
        if b and int(b) >= a and int(b) - a <= 60:
            out += list(range(a, int(b) + 1))
        else:
            out.append(a)
    return out


def parse(run, s):
    """[(work, cote, scans, pages, section, raw)] for one place string"""
    s0 = s
    s = s.replace("\\S", "§").replace("~", " ").replace("--", "–")
    res = []
    if s.strip().startswith("{") and '"cote"' in s:
        try:
            for d in (json.loads(x) for x in re.findall(r"\{[^{}]*\}", s)):
                if d.get("cote") or d.get("scan"):
                    res.append(("archive", d.get("cote", ""), d.get("scan", "").replace("--", "–"), d.get("page", ""), "", s0))
            return res
        except Exception:
            pass
    # Les Dérivateurs: chapter + ms. pages, or block ids (XIIb-a-B035, VIIc-C004, Ib-C003, II-C-003)
    for m in re.finditer(r"\b(" + ROMAN + r")([a-c]?)(?:-[a-c])?[\s.]*(?:ms\.?|manuscript pages?)\s*([0-9][0-9\s,–\-]*(?:bis|ter|quater|quinquies|prime|'|′)?)", s):
        res.append(("Les Dérivateurs", "", "", m.group(3).strip(" ,"), f"chapter {m.group(1)}{m.group(2)}", s0))
    for m in re.finditer(r"\b(" + ROMAN + r"[a-c]?)(?:-[a-c])?-([A-Z]\d{3})\b", s):
        res.append(("Les Dérivateurs", "", "", "", f"chapter {m.group(1)}, block {m.group(2)}", s0))
    if run in DER_RUNS and not res:
        for m in re.finditer(r"\b(" + ROMAN + r")[\s.]+(\d{1,3}(?:\s*[–-]\s*\d{1,3})?)\b", s):
            res.append(("Les Dérivateurs", "", "", m.group(2), f"chapter {m.group(1)}", s0))
    # archive cotes
    for m in re.finditer(r"(?:\bcote\s*|\bMPL\s*|^|;\s*|\()(\d{1,3}(?:-\d)?)(?=[\s;,:)]|$)(.{0,140})", s):
        cote = m.group(1)
        if not (1 <= int(cote.split("-")[0]) <= 200):
            continue
        tail = m.group(2)
        if run in DER_RUNS and not re.search(r"cote|MPL", s[max(0, m.start() - 6):m.end()]):
            continue
        sc = re.search(r"scans?\s*([0-9][0-9\s,–\-v]*)", tail)
        pg = re.search(r"(?:manuscript\s*(?:pp?\.)?|pp?\.|folios?|fols?\.)\s*([0-9][0-9\s,–\-vr]*)", tail)
        sec = re.search(r"(?:section|§)\s*([0-9][0-9.]*)", tail)
        bare = re.match(r"\s*;\s*([0-9][0-9\s,–\-]*)$", tail) if not sc else None
        res.append(("archive", cote, (sc.group(1) if sc else (bare.group(1) if bare else "")).strip(" ,"),
                    (pg.group(1) if pg else "").strip(" ,"), (sec.group(1) if sec else ""), s0))
    # La Longue Marche: section, folios, scans, with C3/C4 or (cote140-x)
    if run in LM_RUNS or re.search(r"\bLM\b|Longue Marche|C[134]\s*scans", s):
        for m in re.finditer(r"(?:(§|section\s*)([0-9][0-9.]*)[^;]{0,40}?)?(?:fols?\.?|folios?)\s*([0-9][0-9\s,–\-vr]*(?:verso)?)[^;]{0,20}?scans?\s*([0-9][0-9\s,–\-]*)", s, re.I):
            cote = re.search(r"cote\s*(140-\d)|\b(C[134])\b", s)
            c = (cote.group(1) or {"C1": "140-1", "C3": "140-3", "C4": "140-4"}[cote.group(2)]) if cote else "140-2"
            res.append(("La Longue Marche", c, m.group(4).strip(" ,"), m.group(3).strip(" ,"), m.group(2) or "", s0))
        for m in re.finditer(r"\b(C[134])\s*(?:§\s*([0-9.]+)\s*)?,?\s*scans?\s*([0-9][0-9\s,–\-]*)", s):
            res.append(("La Longue Marche", {"C1": "140-1", "C3": "140-3", "C4": "140-4"}[m.group(1)], m.group(3).strip(" ,"), "",
                        m.group(2) or "", s0))
        for m in re.finditer(r"\bLM\s*scans?\s*([0-9][0-9\s,–\-]*)", s):
            res.append(("La Longue Marche", "140-2", m.group(1).strip(" ,"), "", "", s0))
    # bare scans with no cote, in the archive runs (the run's cote is in its other rows)
    if not res and re.search(r"\bscans?\s*\d", s):
        sc = re.search(r"scans?\s*([0-9][0-9\s,–\-]*)", s)
        res.append(("?", "", sc.group(1).strip(" ,"), "", "", s0))
    # dedupe
    out, seen = [], set()
    for x in res:
        k = x[:5]
        if k not in seen:
            seen.add(k)
            out.append(x)
    return out


lines = []
unparsed = collections.Counter()
for r in ROWS:
    srcs = []
    hp = (r.get("his_places") or "").strip()
    if hp and hp.lower() not in ("none", "-", "n/a", "none."):
        srcs.append(("his_places", hp))
    for fld in ("statement", "notes"):
        t = r.get(fld) or ""
        for m in re.finditer(r"(?:cote\s*\d{1,3}(?:-\d)?[^.;]{0,60}?scans?\s*\d[\d\s,–\-]*|scans?\s*\d{1,3}(?:\s*[–-]\s*\d{1,3})?|"
                             + ROMAN + r"\s*ms\.\s*\d[\d\s,–\-]*)", t):
            srcs.append((fld, m.group(0)))
    for fld, s in srcs:
        ps = parse(r["run"], s)
        if not ps and fld == "his_places":
            unparsed[r["run"]] += 1
        for (work, cote, scans, pages, sec, raw) in ps:
            lines.append(dict(tag=r["tag"], run=r["run"], status=r["status"], field=fld, work=work, cote=cote, scans=scans,
                              pages=pages, section=sec, raw=raw[:200]))
with open(core.OUT / "tools" / "places_parsed.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(lines[0].keys()), delimiter="\t", lineterminator="\n")
    w.writeheader()
    w.writerows(lines)
print("place lines:", len(lines), "tags:", len({l['tag'] for l in lines}))
print("by work:", collections.Counter(l["work"] for l in lines))
dp = {(l["work"], l["cote"], l["scans"], l["pages"], l["section"]) for l in lines}
print("distinct places:", len(dp))
print("cotes:", collections.Counter(l["cote"] for l in lines if l["work"] in ("archive", "La Longue Marche")).most_common(25))
print("rows with a his_places string that parsed to nothing, by run:", unparsed.most_common())
