"""Sweep 1, scope `sections`: placement of every register row in the handbook outline (by script, with read overrides).
Written by Claude Opus 5.5 at effort max (sweep 1, scope sections), 18 Nov 2026. Reads REGISTER.tsv (scope rows) and the
SECTION_GHOSTS final results table (18 rows newer than the register); writes ../PLACEMENT.tsv.
usage: python -I -B tools/place.py"""
import csv, re, sys, pathlib, collections
csv.field_size_limit(10 ** 9); sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent.parent
REG = HERE.parent / "REGISTER.tsv"
SG_FINAL = pathlib.Path(r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\answers\SECTION_GHOSTS_final_20261118T1305Z_unzipped\SECTION_GHOSTS\SECTION_GHOSTS_results.csv")
SCOPE = ["SECTIONS_OVER_Q", "LM7_FERMAT_TOWER", "LM6_POINTS_AS_SECTIONS", "ANABELIAN_149_PUSH", "LM7_PUSH",
         "ANABELIAN_A1_SUCCESSOR", "SECTION_GHOSTS", "ANABELIAN_SUCCESSOR", "FERMAT_SUCCESSOR", "ANABELIAN_A1", "FLAGGED_149"]
SECT = {
 "I.1.4": ("I.1 GT^ and its finite subgroups", "Involutions, real structures and finite actions in the profinite mapping class groups"),
 "I.1.5": ("I.1 GT^ and its finite subgroups", "The character Delta, CM parities and images in GT^"),
 "I.3.2": ("I.3 Dessins and the Galois action", "Covers, Hom spaces, isotopy and fields of moduli"),
 "I.4.1": ("I.4 Anabelian geometry and sections", "Fundamental groups and sections: cusps, packets, tangential points, first properties"),
 "I.4.2": ("I.4 Anabelian geometry and sections", "Points as sections over finite fields (A1): point-section injectivity, collisions, covering tests"),
 "I.4.3": ("I.4 Anabelian geometry and sections", "Point sections over p-adic, henselian and finitely generated fields"),
 "I.4.4": ("I.4 Anabelian geometry and sections", "The section conjecture over number fields: Selmer sections, finite descent, modular curves"),
 "I.4.5": ("I.4 Anabelian geometry and sections", "The tripod over Q: Conjecture A (cote 149, scan 56) and the Legendre route"),
 "I.4.6": ("I.4 Anabelian geometry and sections", "Nilpotent, metabelian and cuspidally central quotients: section ghosts and their obstructions"),
 "I.4.7": ("I.4 Anabelian geometry and sections", "Birational sections, valuations and the lifting problem (cote 149, scan 127)"),
 "I.4.8": ("I.4 Anabelian geometry and sections", "Anabelian reconstruction: Hom theorems, pinned reconstruction, fields of reconstruction"),
 "I.4.9": ("I.4 Anabelian geometry and sections", "Specialization, good reduction and residue actions"),
 "I.4.10": ("I.4 Anabelian geometry and sections", "Centralizers, normalizers and outer arithmetic actions"),
 "I.4.11": ("I.4 Anabelian geometry and sections", "Configuration spaces and cuspidalization"),
 "I.5.1": ("I.5 The Fermat curves", "Fermat curves as covers of the tripod: models, homology, Jacobians, CM"),
 "I.5.2": ("I.5 The Fermat curves", "The Fermat tower: Kummer homomorphism and the universal measure"),
 "I.5.3": ("I.5 The Fermat curves", "Fermat's theorem for sections: Selmer sections of Fermat curves and their twists"),
 "I.5.4": ("I.5 The Fermat curves", "Sections of nilpotent quotients of the Fermat curves"),
 "I.5.5": ("I.5 The Fermat curves", "GT^ and the Fermat tower: images, markings, CM and lifts"),
 "I.5.6": ("I.5 The Fermat curves", "His questions on the Fermat tower (cote 145, section 51): the manuscript dictionary"),
}


def num(i):
    m = re.search(r"(\d+)", i.split(".", 1)[1] if "." in i else i)
    return int(m.group(1)) if m else 0


def kw(s, pat):
    return re.search(pat, s, re.I) is not None


FF = (r"finite field|\\mathbf F|\\mathbb F|F_\{?[2-9q]|over \$?\\?(?:mathbf|mathbb)?\{?F|characteristic (two|three|\$?p)|"
      r"genus-two|genus two|plane quartic|class number|p-rank|two-rank|supersingular|Lang|witness|Raynaud|Prym|Frobenius order|J_C|collision")


def place(r):
    run, i, s, wp = r["run"], r["id"], r["statement"][:600], r["where_proved"]
    m = re.match(r"[A-Za-z]+", i)
    p = m.group(0) if m else ""
    n = num(i)
    fs = [x for x in re.findall(r"([A-Za-z0-9_]+)\.tex", wp) if not x.endswith("_paper")]
    f = fs[0] if fs else ""
    if run == "SECTIONS_OVER_Q":
        if p in ("B", "C"):
            return "I.4.7"
        if p == "D":
            return "I.4.4" if n <= 4 else "I.4.8"
        if f.startswith("legendre") or kw(s[:200], r"Legendre"):
            return "I.4.5"
        if f.startswith("birational") or f.startswith("cyclotomic"):
            return "I.4.7"
        if f.startswith("local_rings"):
            return "I.4.8"
        if kw(s[:160], r"Fermat"):
            return "I.5.4"
        return "I.4.6"
    if run == "SECTION_GHOSTS":
        if p == "D":
            return "I.4.5"
        if i == "C.5":
            return "I.5.3"
        if p == "E" and (f.startswith("part_E_gt") or 188 <= n <= 198 or n in (201, 203, 204, 207)):
            return "I.1.5"
        if p == "E" and (f in ("part_E_symmetry_audit", "part_E_positive_tower_audit", "part_E_arithmetic_cm_base")
                         or 50 <= n <= 59 or 90 <= n <= 97):
            return "I.1.4"
        if p == "E" and (f == "part_E_fermat_audit" or 98 <= n <= 100):
            return "I.5.4"
        if p == "E" and (f == "part_E_finite_field_sections" or n == 218):
            return "I.4.2"
        return "I.4.6"
    if run == "LM7_FERMAT_TOWER":
        if p == "A":
            return "I.5.6" if n <= 3 else "I.5.1"
        if p in ("B", "C"):
            return "I.5.1"
        if p == "D":
            return "I.5.2" if n <= 23 else "I.5.5"
        return "I.5.4"
    if run == "LM7_PUSH":
        if p in ("A", "B", "C"):
            return "I.5.4"
        if p == "D":
            return "I.5.5"
        if p == "E":
            return "I.1.5" if kw(s[:250], r"\\mathrm\{GT\}|gentle|\\Delta|CM parity") else "I.5.5"
        if p == "F":
            return "I.4.3" if kw(s[:250], r"\\mathbb Q_\{?\d|Q_5|Q_p|local") else "I.4.6"
    if run == "LM6_POINTS_AS_SECTIONS":
        if p == "A":
            return "I.4.10" if kw(s[:300], r"normalizer|centralizer|commut|peripheral outer") else "I.4.8"
        if p == "B":
            return "I.4.3" if kw(s[:300], r"\\mathbb Q_p|sub-\$p\$-adic|p-adic") else "I.4.4"
        if p == "C":
            return "I.1.4"
        if p == "D":
            return "I.4.4"
        if p == "E":
            return "I.4.5" if n <= 5 else ("I.5.3" if n <= 12 else "I.5.4")
        if p == "F":
            return "I.4.1" if i in ("F.39", "F.45", "F.46") else "I.4.7"
    if run == "ANABELIAN_149_PUSH":
        if p == "A":
            return "I.4.2"
        if p in ("B", "C"):
            return "I.4.3" if kw(s[:200], r"point-section|distinguishes tori") else "I.4.9"
        if p == "D":
            if i == "D.U1" or kw(s[:200], r"Legendre|modular unit|lambda"):
                return "I.4.5"
            if i in ("D.1", "D.U2", "D.U3", "D.U4") or kw(s[:200], r"birational|Q\(t\)|ultralimit"):
                return "I.4.7"
            if kw(s[:200], r"Fermat"):
                return "I.5.3"
            return "I.4.4"
        if p == "E":
            return "I.3.2"
        if p == "F":
            return "I.4.8"
        if p == "G":
            return "I.4.1"
    if run == "ANABELIAN_SUCCESSOR":
        return "I.4.2" if p == "A" else "I.4.8"
    if run in ("ANABELIAN_A1", "ANABELIAN_A1_SUCCESSOR"):
        if p == "A":
            return "I.4.11" if i in ("A.2", "A.3") or f.startswith("A_configuration") or kw(s[:200], r"configuration") else "I.4.2"
        if p == "C":
            if i == "C.1":
                return "I.4.3"
            return "I.4.11" if kw(s[:300], r"Mochizuki 2007|cuspidaliz|configuration") else "I.4.8"
        if p == "B":
            if 90 <= n <= 96:
                return "I.4.9"
            if 97 <= n <= 105 or n in (124, 125):
                return "I.4.7"
            if 111 <= n <= 118:
                return "I.4.10"
            if n <= 44 or n in (67, 68) or 80 <= n <= 89 or 130 <= n <= 133 or n in (141, 145):
                return "I.4.2"
            if kw(s[:300], FF) and not kw(s[:300], r"henselian|K_p|reconstruct|topos|\\mathbb Q_p|transcendence"):
                return "I.4.2"
            return "I.4.8"
    if run == "FERMAT_SUCCESSOR":
        if p == "A":
            if n <= 2:
                return "I.4.4"
            if 59 <= n <= 71:
                return "I.4.6"
            return "I.5.3"
        if p == "B":
            return "I.5.4"
        if p == "C":
            return "I.5.5"
        if p == "D":
            return "I.5.6"
    if run == "FLAGGED_149":
        if p == "A":
            return "I.4.1"
        if p == "B":
            return "I.4.3" if i in ("B1", "B7") else "I.4.2"
        if p in ("C", "D", "E"):
            return "I.4.7"
        if p == "F":
            return "I.4.9" if i.startswith("F17") else ("I.4.10" if i.startswith("F8") else "I.4.8")
        if p == "G":
            return "I.3.2" if i == "G7" else "I.1.4"
        if p == "Z":
            return "I.3.2"
        if p == "ZCF":
            return "I.4.7" if i in ("ZCF9", "ZCF10", "ZCF12") else "I.4.10"
        if p == "ZD":
            return "I.4.1" if i in ("ZD1", "ZD2") else "I.4.7"
    return "?"


# rows whose place was decided by reading the statement (or the proof), with the reason
READ = {
 "SECTIONS_OVER_Q:A.1": ("I.4.5", "the two principal assertions of the run: Conjecture A and birational lifting for the tripod"),
 "SECTIONS_OVER_Q:A.24": ("I.4.5", "the Legendre route to A1, its remaining gate"),
 "SECTION_GHOSTS:A.2": ("I.4.6", "main question (FS)_nil of the ghost line; its manuscript consequence is D.2 (I.4.5)"),
 "SECTION_GHOSTS:A.4": ("I.4.5", "Stix 2015 Cor. 5/6 applied to locally ordinary full sections of the tripod"),
 "SECTION_GHOSTS:A.5": ("I.4.5", "conditional implication (FS)_nil => Conjecture A for locally ordinary sections"),
 "SECTION_GHOSTS:E.100": ("I.5.3", "plus Fermat curve, even n: no section already of the pro-2 abelian extension (strengthens LM6 E.12, second sentence)"),
 "SECTION_GHOSTS:C.4": ("I.1.5", "compact finite separation; the topological inference of GT_TOWER_CHECK A.4.1"),
 "SECTION_GHOSTS:E.218": ("I.4.2", "finite-field tripod: a finite pro-ell quotient separates interior point sections from cusp sections"),
 "LM6_POINTS_AS_SECTIONS:B.27": ("I.4.5", "the run's open main question: point-surjectivity for tripod sections over number fields"),
 "LM6_POINTS_AS_SECTIONS:F.15": ("I.4.7", "the birational lifting problem for the tripod over Q (same as ANABELIAN_149_PUSH D.U4)"),
 "LM6_POINTS_AS_SECTIONS:A.22": ("I.4.10", "normalizer of a procyclic subgroup of the full CM group (same question as ANABELIAN_A1_SUCCESSOR B.118 = N2)"),
 "LM6_POINTS_AS_SECTIONS:E.12": ("I.5.3", "Fermat's theorem for Selmer sections, odd n; its last two sentences rest on Tool (1)"),
 "ANABELIAN_A1_SUCCESSOR:B.118": ("I.4.10", "N2 gate; same question as LM6 A.22"),
 "ANABELIAN_149_PUSH:A.30": ("I.4.2", "universal A1; settled by ANABELIAN_SUCCESSOR A.3 = ANABELIAN_A1 A.1"),
 "FLAGGED_149:B9": ("I.4.2", "prime-to-p point question of cote 149 scans 35-36; settled for proper curves by ANABELIAN_SUCCESSOR A.3"),
 "FERMAT_SUCCESSOR:A.1": ("I.4.4", "Selmer sections in finite etale neighbourhoods (Harari-Stix 2.1)"),
 "FERMAT_SUCCESSOR:A.2": ("I.4.4", "finite support + Selmer => point or cusp (Stoll 8.2 with erratum)"),
 "LM7_FERMAT_TOWER:E.16": ("I.5.4", "torus quotient T=G_m^{0,1,inf}/G_m and its sections; also FERMAT_SUCCESSOR A.17"),
 "LM7_PUSH:E.3": ("I.1.5", "whether full GT^ reaches the extra CM coset (Delta on GT^)"),
 "FERMAT_SUCCESSOR:C.15": ("I.1.5", "Delta on full GT^ (open; same question as LM7_PUSH E.3)"),
 "FERMAT_SUCCESSOR:C.19": ("I.1.5", "the multiplier-one group is torsion-free"),
 "FERMAT_SUCCESSOR:C.6": ("I.1.5", "two gentle lifts with Delta=1, quotient Delta=0 (R14)"),
}
if __name__ == "__main__":
    rows = []
    with open(REG, encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if r["run"] in SCOPE:
                rows.append(r)
    known = {r["tag"] for r in rows}
    extra = []
    with open(SG_FINAL, encoding="utf-8-sig", newline="") as fh:
        for r in csv.DictReader(fh):
            t = "SECTION_GHOSTS:" + r["id"].strip()
            if t not in known:
                extra.append(dict(tag=t, run="SECTION_GHOSTS", id=r["id"].strip(),
                                  status=((r["status"] or "?").split() or ["?"])[0].strip(".,;:"),
                                  statement=re.sub(r"\s+", " ", r["statement"]), where_proved=r["where_proved"], final_only=True))
    out = []
    cnt = collections.Counter()
    for r in rows + extra:
        code = place(r)
        how, note = "script", ""
        if r["tag"] in READ:
            code, note = READ[r["tag"]]
            how = "read"
        if r.get("final_only"):
            note = (note + "; " if note else "") + "row of the SECTION_GHOSTS final (13:05 UTC), not in REGISTER.tsv"
        ch, se = SECT.get(code, ("?", "?"))
        out.append((r["tag"], "I. The Galois theory of the tower", ch, f"{code} {se}", how, note, r["status"]))
        cnt[code] += 1
    with open(HERE / "PLACEMENT.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["tag", "part", "chapter", "section", "how placed", "note", "status"])
        w.writerows(out)
    print(len(out), "rows;", dict(sorted(cnt.items())))
