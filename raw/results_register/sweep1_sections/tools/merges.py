"""Sweep 1, scope `sections`: lineage and merges (MERGES.tsv).
Written by Claude Opus 5.5 at effort max (sweep 1, scope sections), 18 Nov 2026.
Sources, in order: (1) ANABELIAN_A1 ids carried by ANABELIAN_A1_SUCCESSOR; (2) the `checks` column of the SECTION_GHOSTS final
(each row names the earlier statement it checks: confirmed / repaired / refuted); (3) FERMAT_SUCCESSOR's audit of R1-R20
(report, section "Claim-by-claim audit"); (4) cross-run references in statements and notes ("LM6 E.8", "AS-A.3",
"SECTIONS\\_OVER\\_Q A.44", ...); (5) identical normalized statements across runs; (6) the main-line merges read by hand.
usage: python -I -B tools/merges.py"""
import csv, re, sys, json, pathlib, difflib, collections
csv.field_size_limit(10 ** 9); sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent.parent
REG = HERE.parent / "REGISTER.tsv"
SG_FINAL = pathlib.Path(r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\answers\SECTION_GHOSTS_final_20261118T1305Z_unzipped\SECTION_GHOSTS\SECTION_GHOSTS_results.csv")
SCOPE = ["SECTIONS_OVER_Q", "LM7_FERMAT_TOWER", "LM6_POINTS_AS_SECTIONS", "ANABELIAN_149_PUSH", "LM7_PUSH",
         "ANABELIAN_A1_SUCCESSOR", "SECTION_GHOSTS", "ANABELIAN_SUCCESSOR", "FERMAT_SUCCESSOR", "ANABELIAN_A1", "FLAGGED_149"]
allrows = {}
ids = collections.defaultdict(set)
with open(REG, encoding="utf-8", newline="") as fh:
    for r in csv.DictReader(fh, delimiter="\t"):
        ids[r["run"]].add(r["id"])
        if r["run"] in SCOPE:
            allrows[r["tag"]] = r
out = []
seen = set()


def add(canon, member, rel, reason, source):
    k = (canon, member, rel)
    if k in seen or canon == member:
        return
    seen.add(k)
    out.append((canon, member, rel, reason, source))


# (1) ANABELIAN_A1 -> ANABELIAN_A1_SUCCESSOR
for t, r in allrows.items():
    if r["run"] != "ANABELIAN_A1":
        continue
    s = allrows.get("ANABELIAN_A1_SUCCESSOR:" + r["id"])
    if not s:
        continue
    if s["statement"] == r["statement"] and s["status"] == r["status"]:
        add(s["tag"], t, "same", "carried unchanged by the successor run (identical statement and status)", "id carry")
    else:
        ratio = difflib.SequenceMatcher(None, r["statement"][:1500], s["statement"][:1500]).ratio()
        add(s["tag"], t, "refines", f"carried and rewritten by the successor (text similarity {ratio:.2f}); status {r['status']} -> {s['status']}", "id carry")
# (2) SECTION_GHOSTS final: checks column
RUNPAT = r"(SECTIONS_OVER_Q|GT_TOWER_CHECK|LM6_POINTS_AS_SECTIONS|LM6|LM7_PUSH|LM7_FERMAT_TOWER|LM7|LM4_SUCCESSOR|LM4|LM8_PUSH|LM8|ANABELIAN_149_PUSH|FERMAT_SUCCESSOR|EXIT_TOWER|DELTA_ON_GT)"
ALIAS = {"LM6": "LM6_POINTS_AS_SECTIONS", "LM7": "LM7_FERMAT_TOWER", "LM4": "LM4_SUCCESSOR", "LM8": "LM8_PUSH"}
with open(SG_FINAL, encoding="utf-8-sig", newline="") as fh:
    for r in csv.DictReader(fh):
        ck = re.sub(r"\s+", " ", r["checks (the earlier statement it checks, and confirmed / repaired / refuted)"]).replace("\\_", "_")
        for m in re.finditer(RUNPAT + r"\s+([A-Z][A-Za-z]?\d*(?:\.\d+)*[a-z]?)(?:[^:;]{0,60}?):\s*(confirmed|repaired|refuted|pending)", ck):
            run = ALIAS.get(m.group(1), m.group(1))
            oid, verdict = m.group(2), m.group(3)
            if verdict == "pending":
                continue
            rel = {"confirmed": "same", "repaired": "corrects", "refuted": "refuted by"}[verdict]
            canon = "SECTION_GHOSTS:" + r["id"].strip()
            member = f"{run}:{oid}"
            if rel == "refuted by":
                add(member, canon, "refuted by", f"SECTION_GHOSTS {r['id']} checks it: refuted ({ck[:160]})", "SECTION_GHOSTS final, checks column")
            else:
                why = "re-proved and confirmed" if rel == "same" else "repaired"
                add(canon, member, rel, f"SECTION_GHOSTS {r['id']} {why} {run} {oid} ({ck[:140]})", "SECTION_GHOSTS final, checks column")
# (3) FERMAT_SUCCESSOR audit of R1-R20 (report section 'Claim-by-claim audit'); mapping of R to earlier ids as the audit states it
FS = [
 ("FERMAT_SUCCESSOR:A.2", "LM6_POINTS_AS_SECTIONS:E.6", "same", "R1: finite-support conclusion retained, all-place descent explicit (Stoll 8.2 with erratum)"),
 ("FERMAT_SUCCESSOR:A.7", "LM6_POINTS_AS_SECTIONS:E.7", "same", "R2: Legendre cyclic-subgroup cover to Y0(4l), genus (l-3)/2"),
 ("FERMAT_SUCCESSOR:A.6", "LM6_POINTS_AS_SECTIONS:E.8", "corrects", "R3: the conclusion (reducible, twist with semisimplification 1+chi) is repaired; the cusp divisibility by l in E.8's proof is false (A.4): the Tate parameter is u^(2l)/256 times a principal unit"),
 ("FERMAT_SUCCESSOR:A.4", "LM6_POINTS_AS_SECTIONS:E.8", "corrects", "R3: refutes the cusp-divisibility step used for E.8 (and Steklov 2026's general ramification-divisibility proposition); counterexample l=5 over Q2"),
 ("FERMAT_SUCCESSOR:A.8", "LM6_POINTS_AS_SECTIONS:E.9", "same", "R4: every Selmer section of U_l, l>=5 prime, is cuspidal; re-proved from the repaired local representation (A.3-A.6), Stoll, Mazur"),
 ("FERMAT_SUCCESSOR:A.9", "LM6_POINTS_AS_SECTIONS:E.10", "same", "R5: Y1(7)(Q) is nonempty; (0,0) of order 7 on y^2-xy-4y=x^3-4x^2"),
 ("FERMAT_SUCCESSOR:A.10", "LM6_POINTS_AS_SECTIONS:E.11", "same", "R6: the cubic through X0(27), exact rational cusps, rank-zero descent"),
 ("FERMAT_SUCCESSOR:A.11", "LM6_POINTS_AS_SECTIONS:E.12", "same", "R7: the Selmer half of E.12 (odd n>=3); E.12's 'every section is Selmer' rests on Tool (1) (FERMAT_SUCCESSOR A.20)"),
 ("FERMAT_SUCCESSOR:A.16", "LM6_POINTS_AS_SECTIONS:E.12", "stronger", "A.16 adds the classical curves C_n for every n>=3, four cusp centres for even n (E.12 treats the plus curve only)"),
 ("FERMAT_SUCCESSOR:A.20", "LM6_POINTS_AS_SECTIONS:E.12", "refines", "the proper-to-affine step of E.12's last sentences, proved conditional on the supplied local Theorem 1.1 (Tool (1))"),
 ("FERMAT_SUCCESSOR:A.17", "LM7_FERMAT_TOWER:E.16", "refines", "R8: the torus quotient and its completed Kummer section set; the S3-invariant splitting unique up to geometric conjugation"),
 ("FERMAT_SUCCESSOR:B.16", "LM7_PUSH:A.4", "same", "R12: identifies the LM7_PUSH A.4 comparison; fibre equality 24 = 23 + 1"),
 ("FERMAT_SUCCESSOR:C.13", "LM7_PUSH:D.52", "refines", "R16: weight-nine obstruction proved conditional on the unrefereed existence inputs LM7_PUSH D.20, D.21, D.51, D.52"),
 ("FERMAT_SUCCESSOR:C.25", "LM7_FERMAT_TOWER:D.45", "corrects", "R17: an unrestricted D.45 next-layer exclusion is refuted once cusp conjugation is allowed; D.45 obstructs a fixed cusp frame only"),
 ("FERMAT_SUCCESSOR:C.6", "LM7_PUSH:E.58", "same", "R13/R14: reconstruction of LM7_PUSH E.58 and E.65: the two gentle lifts have Delta=1, their quotient Delta=0"),
 ("FERMAT_SUCCESSOR:C.6", "LM7_PUSH:E.65", "same", "R14: CM parity a continuous character; Delta on full GT^ still open (C.15)"),
 ("FERMAT_SUCCESSOR:C.15", "LM7_PUSH:E.3", "same", "R14: Delta on full GT^ (the extra CM coset), open in both"),
 ("FERMAT_SUCCESSOR:A.32", "LM6_POINTS_AS_SECTIONS:B.27", "refines", "R20: the exact rank-zero consequences for LM6 B.27 and ANABELIAN D.30"),
 ("FERMAT_SUCCESSOR:A.32", "ANABELIAN_149_PUSH:D.30", "refines", "R20: as for LM6 B.27"),
 ("FERMAT_SUCCESSOR:B.17", "LM6_POINTS_AS_SECTIONS:E.38", "same", "LM6 E.38 is the same nonclosed-image phantom mechanism in degree three"),
]
for c, m, rel, why in FS:
    add(c, m, rel, why, "FERMAT_SUCCESSOR report, audit of R1-R20 (read)")
# (6) main lines, read
MAIN = [
 # A1: point-section injectivity over finite fields (prime-to-p arithmetic group)
 ("ANABELIAN_A1_SUCCESSOR:A.1", "ANABELIAN_A1:A.1", "same", "A1 for proper curves of genus >= 2 over finite fields; the successor re-proves it by a direct characteristic-p configuration route (A.13-A.21, A.42-A.49, B.68) without the finite exceptional-set theorem"),
 ("ANABELIAN_A1_SUCCESSOR:A.1", "ANABELIAN_SUCCESSOR:A.3", "same", "ANABELIAN_A1 A.1 says so itself: 'AS-A.3 (AR.3), with precisely these hypotheses, is correct'"),
 ("ANABELIAN_A1_SUCCESSOR:A.1", "ANABELIAN_149_PUSH:A.30", "stronger", "A.30 left universal A1 unresolved; settled by ANABELIAN_SUCCESSOR A.3 / ANABELIAN_A1 A.1"),
 ("ANABELIAN_A1_SUCCESSOR:A.1", "ANABELIAN_149_PUSH:A.C2.22", "stronger", "A.C2.22 proves A1 for 46 of 48 ordinary genus-two moduli classes over F4; A.1 covers all"),
 ("ANABELIAN_A1_SUCCESSOR:A.1", "ANABELIAN_149_PUSH:A.C2.6", "stronger", "the odd-torsion-point route of A.C2.6 is no longer needed: A.1 holds for every genus-two curve over every finite field of characteristic 2"),
 ("ANABELIAN_A1_SUCCESSOR:A.1", "FLAGGED_149:B9", "stronger", "B9 left prime-to-p (*) open for proper and affine genus >= 2; A.1 settles proper curves over finite fields, and ANABELIAN_A1 A.33 (A.R5) extends to every hyperbolic curve over a finitely generated field of characteristic p (second Fable reading, part 2, section 3)"),
 ("ANABELIAN_SUCCESSOR:A.2", "ANABELIAN_149_PUSH:A.3", "refines", "both state the equivalence of equality of point sections with the covering conditions of cote 149, scan 36"),
 ("ANABELIAN_SUCCESSOR:A.1", "ANABELIAN_149_PUSH:A.3", "same", "collision <=> covering condition with p-primary differences (cote 149 scan 36)"),
 ("FLAGGED_149:B6", "ANABELIAN_149_PUSH:A.1", "refines", "full point-section injectivity in characteristic p through a semiabelian immersion; ANABELIAN_149_PUSH A.1 is the prime-to-p Kummer-kernel input"),
 # Fermat curves: Selmer sections
 ("FERMAT_SUCCESSOR:A.11", "SECTION_GHOSTS:C.5", "stronger", "SECTION_GHOSTS C.5 cites Steklov 2026 (arXiv 2602.17746v1) Thm A/5.14 for prime exponent >= 7; A.11 covers every odd n >= 3 with a repaired route (A.3-A.10)"),
 ("SECTION_GHOSTS:E.100", "LM6_POINTS_AS_SECTIONS:E.12", "stronger", "for even n the plus Fermat curve has no section already of its geometrically pro-2 abelian extension; strengthens the second sentence of E.12"),
 ("SECTIONS_OVER_Q:A.20", "LM6_POINTS_AS_SECTIONS:E.8", "refines", "the raw residual Legendre representation need not be unramified outside 2*5; E.8's assertion after the quadratic twist is not refuted"),
 # the tripod over Q: one question under several ids
 ("SECTIONS_OVER_Q:A.1", "ANABELIAN_149_PUSH:D.U1", "same", "Conjecture A for the tripod over Q: every noncuspidal section comes from a rational point (cote 149, scan 56)"),
 ("SECTIONS_OVER_Q:A.1", "LM6_POINTS_AS_SECTIONS:B.27", "same", "B.27's first item, point-surjectivity for tripod sections, is the same question"),
 ("SECTIONS_OVER_Q:A.1", "SECTION_GHOSTS:D.3", "same", "SECTION_GHOSTS D.3 records the same question as unconditionally undecided"),
 ("SECTIONS_OVER_Q:B.15", "ANABELIAN_149_PUSH:D.U4", "same", "birational lifting of every tripod section over Q: the splitting of 1->ker q_U->G_Q(t) x_{pi1(U),s} G_Q->G_Q->1"),
 ("SECTIONS_OVER_Q:B.15", "LM6_POINTS_AS_SECTIONS:F.15", "same", "the same splitting problem"),
 ("SECTIONS_OVER_Q:B.15", "FLAGGED_149:ZD10", "same", "the remaining birational lifting assertion of conjecture (b) for K=Q, U the tripod"),
 ("SECTIONS_OVER_Q:B.15", "ANABELIAN_149_PUSH:D.U2", "same", "the second half of B.15 (sections of G_Q(t)->G_Q in decomposition groups of rational places) is D.U2"),
 ("SECTION_GHOSTS:D.2", "SECTIONS_OVER_Q:A.1", "refines", "strongest proved reduction: (FS)_nil (SECTION_GHOSTS A.2) implies Conjecture A and birational lifting for locally ordinary sections"),
 # N2: normalizer of a procyclic subgroup of the full CM group
 ("ANABELIAN_A1_SUCCESSOR:B.118", "LM6_POINTS_AS_SECTIONS:A.22", "same", "existence or exclusion of a nontrivial closed procyclic C<=R with open arithmetic normalizer image in G_Q(i); the successor confines C to a strictly smaller residual intersection (B.111-B.117)"),
 # Delta on GT^
 ("LM7_PUSH:E.3", "FERMAT_SUCCESSOR:C.15", "same", "whether full GT^ reaches the extra CM coset, i.e. Delta on GT^"),
 ("SECTION_GHOSTS:E.191", "LM7_PUSH:E.3", "stronger", "E.191 proves Delta|GT^ = 0 for the historical character Delta: GT^_0 -> F_2 with the signed pure frames of E.95 (GT_TOWER_CHECK A.7); this settles E.3 IF E.95's frames give LM7_PUSH E.61/E.65's CM parity (E.201 reconstructs LM7 E.58's family, which suggests so); identification not yet checked"),
 ("SECTION_GHOSTS:E.191", "FERMAT_SUCCESSOR:C.15", "stronger", "as for LM7_PUSH E.3: Delta on full GT^, settled by E.191 if the characters coincide"),
 ("SECTION_GHOSTS:E.198", "SECTION_GHOSTS:E.191", "stronger", "GT^ strictly inside ker Delta strictly inside GT^_0, witness the square of E.197's full element"),
 # reconstruction over characteristic zero fields (B8)
 ("ANABELIAN_A1_SUCCESSOR:B.102", "FLAGGED_149:D7", "refines", "D7 is a composite row: its DVR assertion is true (re-proved by B.102, which extends it to every ordered rank when the divisible part of the value group vanishes); its arbitrary-valuation converse is false (D7, B.99); D7's status 'Refuted' covers only the extension"),
 ("ANABELIAN_A1_SUCCESSOR:B.52", "ANABELIAN_A1:B.52", "refines", "the remaining-field classification B8 restated after B.136-B.147"),
 ("ANABELIAN_A1_SUCCESSOR:B.52", "ANABELIAN_SUCCESSOR:F.18", "refines", "both record the open classification of characteristic-zero reconstruction fields with a henselian valuation"),
 ("ANABELIAN_A1_SUCCESSOR:B.52", "ANABELIAN_149_PUSH:F.9", "refines", "F.9 left the intrinsic classification of characteristic-zero reconstruction fields unresolved; B.52 is its current form"),
 # finiteness of Sec
 ("LM6_POINTS_AS_SECTIONS:D.8", "LM6_POINTS_AS_SECTIONS:D.1", "refines", "D.1 identifies cote 149 section 8 folio 33 (scan 65) as the finiteness of Sec(C/K); D.8 is its open state"),
 # supersingular-correspondence and nontrivial cover assertions
 ("ANABELIAN_A1_SUCCESSOR:B.67", "ANABELIAN_SUCCESSOR:A.57", "same", "the universal supersingular-correspondence assertion (A5/B5), open in both"),
 ("ANABELIAN_A1_SUCCESSOR:B.24", "ANABELIAN_SUCCESSOR:A.15", "refines", "the nontrivial-cover assertion A3 (ANABELIAN_SUCCESSOR) and the p-rank-zero cyclic cover question B4 (ANABELIAN_A1)"),
 ("ANABELIAN_A1_SUCCESSOR:B.32", "ANABELIAN_SUCCESSOR:A.96", "same", "least witnesses for plane quartics over F3 and F5 over all constant extensions, open in both"),
 ("ANABELIAN_A1_SUCCESSOR:B.12", "ANABELIAN_SUCCESSOR:A.103", "same", "free all-level vectors in M_P^F for genus-two curves in characteristic two"),
]
for c, m, rel, why in MAIN:
    add(c, m, rel, why, "read")
# (4) cross-run references in statements and notes
ABBR = {"AS": "ANABELIAN_SUCCESSOR", "AN": "ANABELIAN_149_PUSH", "LM6": "LM6_POINTS_AS_SECTIONS", "LM7": "LM7_FERMAT_TOWER",
        "LM7_PUSH": "LM7_PUSH", "SECTIONS_OVER_Q": "SECTIONS_OVER_Q", "SECTIONS": "SECTIONS_OVER_Q", "FLAGGED_149": "FLAGGED_149",
        "ANABELIAN_149_PUSH": "ANABELIAN_149_PUSH", "ANABELIAN_SUCCESSOR": "ANABELIAN_SUCCESSOR", "FERMAT_SUCCESSOR": "FERMAT_SUCCESSOR",
        "ANABELIAN_A1": "ANABELIAN_A1", "LM6_POINTS_AS_SECTIONS": "LM6_POINTS_AS_SECTIONS", "LM7_FERMAT_TOWER": "LM7_FERMAT_TOWER"}
REF = re.compile(r"\b(LM7_PUSH|LM7_FERMAT_TOWER|LM6_POINTS_AS_SECTIONS|SECTIONS_OVER_Q|ANABELIAN_149_PUSH|ANABELIAN_SUCCESSOR|ANABELIAN_A1|FERMAT_SUCCESSOR|FLAGGED_149|SECTIONS|LM6|LM7|AS|AN)[\s\-]+([A-Z]{1,3}\.?\d+(?:\.\d+)*[a-z]?)\b")
for t, r in allrows.items():
    blob = (r["statement"][:700] + " " + r["notes"]).replace("\\_", "_")
    for m in REF.finditer(blob):
        orun = ABBR[m.group(1)]
        oid = m.group(2)
        if orun == r["run"] or oid not in ids.get(orun, ()):
            continue
        head = blob[max(0, m.start() - 80):m.end() + 60]
        if re.search(r"strengthen|stronger|extends|extension of", head, re.I):
            rel = "stronger"
        elif re.search(r"confirm|is correct|re-prov|proves the", head, re.I):
            rel = "same"
        elif re.search(r"repair|correction (to|of)|corrects", head, re.I):
            rel = "corrects"
        elif re.search(r"\bfalse\b|refut", head, re.I):
            rel = "refines"
        else:
            continue  # a plain citation is a use, not a merge
        add(t, f"{orun}:{oid}", rel, "named in the statement: ..." + re.sub(r"\s+", " ", head)[:150] + "...", "text reference")
# (5) identical normalized statements across runs (other than the A1 carry)
groups = collections.defaultdict(list)
for t, r in allrows.items():
    if r.get("same_statement"):
        groups[r["same_statement"]].append(t)
for g, ts in groups.items():
    runs = {allrows[x]["run"] for x in ts}
    if len(runs) > 1 and not runs <= {"ANABELIAN_A1", "ANABELIAN_A1_SUCCESSOR"}:
        ts = sorted(ts, key=lambda x: allrows[x]["stamp"], reverse=True)
        for m in ts[1:]:
            add(ts[0], m, "same", "identical normalized statement (register hash " + g + ")", "register same_statement")
with open(HERE / "MERGES.tsv", "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["canonical tag", "member tag", "relation", "reason", "source"])
    w.writerows(out)
print(len(out), collections.Counter(o[2] for o in out), collections.Counter(o[4] for o in out))
