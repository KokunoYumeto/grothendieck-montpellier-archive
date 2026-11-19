"""Sweep 1, scope `sections`: verdicts on the register's flags (FLAG_VERDICTS.tsv).
Written by Claude Opus 5.5 at effort max (sweep 1, scope sections), 18 Nov 2026.
Flags: (a) a proved row citing a refuted row; (b) a dependency naming no id of its run; (c) found in this sweep: a proved row
whose register `uses` edge points to an Open row of its run. Verdicts for (a) and (c) were decided by reading the statements
(and, where named, the proof text); (b) by script with the resolutions read from the rows' own text.
usage: python -I -B tools/flags.py"""
import csv, re, sys, json, pathlib, collections
csv.field_size_limit(10 ** 9); sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent.parent
REGD = HERE.parent
SCOPE = ["SECTIONS_OVER_Q", "LM7_FERMAT_TOWER", "LM6_POINTS_AS_SECTIONS", "ANABELIAN_149_PUSH", "LM7_PUSH",
         "ANABELIAN_A1_SUCCESSOR", "SECTION_GHOSTS", "ANABELIAN_SUCCESSOR", "FERMAT_SUCCESSOR", "ANABELIAN_A1", "FLAGGED_149"]
rows, ids = {}, collections.defaultdict(dict)
with open(REGD / "REGISTER.tsv", encoding="utf-8", newline="") as fh:
    for r in csv.DictReader(fh, delimiter="\t"):
        ids[r["run"]][r["id"]] = r["status"]
        if r["run"] in SCOPE:
            rows[r["tag"]] = r
flags = []
with open(REGD / "FLAGS.tsv", encoding="utf-8", newline="") as fh:
    for f in csv.DictReader(fh, delimiter="\t"):
        if f["tag"].split(":")[0] in SCOPE and not f["flag"].startswith("proved; no check"):
            flags.append(f)
SOUND = "sound: uses the refutation, not the refuted claim"
# (a) proved row cites a refuted row: verdict notes by proved tag (read)
A = {
 "ANABELIAN_149_PUSH:B.10": "uses B.9's corrected description (splittings by Z1, inertia classes by H1) in place of the literal L4 torsor",
 "ANABELIAN_149_PUSH:B.18": "example computed with B.9's corrected torsor description",
 "ANABELIAN_149_PUSH:B.19": "example computed with B.9's corrected torsor description",
 "ANABELIAN_149_PUSH:F.2": "F.2 is the construction witnessing the negative statement F.1 (nonalgebraic relative G_m endomorphism); same negative content",
 "ANABELIAN_A1:B.22": "works with the explicit curve and point of B.23, the object of the counterexample",
 "ANABELIAN_A1:B.26": "works with the explicit curve and point of B.23",
 "ANABELIAN_A1:B.27": "works with the explicit curve and point of B.23",
 "ANABELIAN_A1_SUCCESSOR:B.22": "works with the explicit curve and point of B.23",
 "ANABELIAN_A1_SUCCESSOR:B.26": "works with the explicit curve and point of B.23",
 "ANABELIAN_A1_SUCCESSOR:B.27": "works with the explicit curve and point of B.23",
 "ANABELIAN_A1_SUCCESSOR:B.56": "uses B.53's setting (A=Z_(p)^sh, K_p, I=G_{K_p}) and computes the actual Kummer kernel",
 "ANABELIAN_A1_SUCCESSOR:B.57": "uses B.53's setting; the larger small-prime kernels it computes are true and, per the report, no longer obstruct reconstruction (B.137-B.138)",
 "ANABELIAN_A1_SUCCESSOR:B.137": "uses B.53's fixed local inertia group; settles the lower-central union for every prime",
 "ANABELIAN_A1_SUCCESSOR:B.96": "the constant-curve case, contrasted with B.93's counterexample to the uniqueness expectation of cote 142, scan 096",
 "ANABELIAN_A1_SUCCESSOR:B.105": "defines the subgroup R_x that accounts for B.101's noninjective boundary homomorphism",
 "ANABELIAN_A1_SUCCESSOR:B.125": "uses B.101 to choose the compactification data; the criterion is stated with R_x",
 "ANABELIAN_SUCCESSOR:A.18": "a genus-two computation; A.12 shows the genus-two test does not extend to genus three, which delimits A.18's scope (statement level)",
 "ANABELIAN_SUCCESSOR:A.47": "computes with A.81's counterexample family (statement level)",
 "ANABELIAN_SUCCESSOR:A.48": "A.86's explicit curve over F_2^38 is cited as the example that makes a hypothesis of A.48 necessary (statement level)",
 "ANABELIAN_SUCCESSOR:A.60": "the degree-35 example of the mechanism of A.59's degree-7 counterexample",
 "ANABELIAN_SUCCESSOR:A.75": "general bound r_n, using A.70's example over F_16",
 "ANABELIAN_SUCCESSOR:A.79": "a group-theoretic model of A.81's mechanism",
 "ANABELIAN_SUCCESSOR:A.82": "counts the parameters of A.81's family",
 "ANABELIAN_SUCCESSOR:A.85": "bounds the conductors in A.81's family",
 "FERMAT_SUCCESSOR:A.48": "states the corrected distinction (intrinsic versus cocycle ramification) forced by A.4's counterexample",
 "FERMAT_SUCCESSOR:B.15": "computes with B.7's construction (infinitely ramified noncuspidal class-two sections that lift to class three)",
 "FERMAT_SUCCESSOR:B.17": "identifies LM6 E.38 with B.7's mechanism",
 "FERMAT_SUCCESSOR:B.24": "local-order law; B.7's lifts are among its inputs",
 "FERMAT_SUCCESSOR:B.31": "zero-abelian class-three slice; B.7's lifts are among its inputs",
 "FERMAT_SUCCESSOR:B.33": "parametrizes all cocycles unramified outside 3 and 7, including B.30's family",
 "FLAGGED_149:B8": "B7 shows what prime-to-p abelianization loses; B8 recovers points through nonabelian quotients",
 "FLAGGED_149:F17.6": "uses the compact-type genus-two counterexample construction of F17.2",
 "FLAGGED_149:G3": "uses the complete-curve translation statement, which B4 keeps; B4 refutes only the open-subset form of scan 37",
 "FLAGGED_149:ZCF2": "B7 is cited for scope; ZCF2 is a general lemma on profinite extensions",
 "FLAGGED_149:ZCF11": "cites F17.2 and F17.4 as the examples that delimit the reformulation of scan 102 (proof text read: F17.4 'constructs an outer action which is itself nongeometric')",
 "FLAGGED_149:ZD3": "uses the DVR part of D7, which is true (re-proved by ANABELIAN_A1_SUCCESSOR B.102); D7's 'Refuted' covers only its arbitrary-valuation converse; see CORRECTIONS (split D7)",
 "LM6_POINTS_AS_SECTIONS:F.9": "adds the open-stabilizer hypothesis that F.41's discontinuous action shows to be necessary",
 "LM6_POINTS_AS_SECTIONS:F.47": "a second discontinuous semilinear action of the type of F.41, over Q(i)",
 "LM7_FERMAT_TOWER:A.11": "uses A.9's flat replacement of the premature exact sequences",
 "LM7_FERMAT_TOWER:A.14": "uses A.13's corrected image of definition (171)",
 "LM7_FERMAT_TOWER:E.16": "uses the exact norm comparison with kernel (R_n/Z Norm) that C.2 proves in place of the false rank-two identification",
 "LM7_FERMAT_TOWER:E.19": "no contradiction: E.17 (two cusp sections conjugate in the rank-two toric quotient) and E.19 (three cusps distinct in the pro-3 abelianization) concern different quotients; E.19 uses E.17 to show the toric quotient is too small",
 "LM7_PUSH:A.17": "local theorem for metabelian sections; consistent with A.5, whose mixed example is only class two (A.18: no metabelian lift)",
 "LM7_PUSH:A.18": "proves that A.5's and A.6's class-two examples have no metabelian or marked-depth lift",
 "LM7_PUSH:A.43": "A.12 (no universal finite-precision decision program) delimits A.43's finite tests",
 "LM7_PUSH:B.1": "cites B.2 for scope: the class-two image need not be a point or cusp image (statement level)",
 "LM7_PUSH:C.3": "the corrected germ formalism after C.4",
 "LM7_PUSH:C.5": "the corrected germ formalism after C.4",
 "LM7_PUSH:C.6": "the classification that C.4 and C.11 force (C.11 disproves the verbatim pure-residue extension)",
 "LM7_PUSH:C.7": "the obstruction of A.4 survives finite extensions, as C.4 shows for the R2 class",
 "LM7_PUSH:C.12": "the corrected number-field criterion with its retained arithmetic term (after C.11)",
 "LM7_PUSH:C.14": "the explicit construction behind C.12, after C.11",
 "SECTIONS_OVER_Q:A.30": "gives the correct action at the birational level after A.8 (4t(1-t) and j/1728 are not self-maps of U)",
 "SECTION_GHOSTS:C.4": "uses A.101's noncompactness to limit the pentagon analogy",
}
A_DEFAULT = {
 "LM7_PUSH": "computes with the explicit sections of A.5/A.6 (the counterexamples to Leads 2 and 3)",
 "SECTIONS_OVER_Q": "uses A.49's local comparison of s_5 with a cusp in the full congruence quotient (the counterexample to L12(ii))",
}
out = []
for f in flags:
    t = f["tag"]
    r = rows[t]
    if f["flag"].startswith("proved item cites"):
        note = A.get(t) or (A_DEFAULT.get(r["run"]) if r["run"] in A_DEFAULT else "")
        if r["run"] == "LM7_PUSH" and t not in A and re.search(r"F\.4", f["detail"]):
            note = "computes the actual fixed groups after F.4 (total orders of residue invariants do not determine vanishing)"
        how = "read (statement)" if note else "not decided"
        out.append((t, "proved item cites a refuted row: " + f["detail"], SOUND if note else "unread", r["where_proved"][:160], note, how))
# (b) dependency names no id: resolve each token
ROMAN = re.compile(r"^(XIII|XII|XI|X|IX|VIII|VII|VI|V|IV|III|II|I)\.?\d")
SG_OVR = {  # SECTION_GHOSTS rows whose unprefixed ids belong to the run they audit (read in the rows' text and sources)
 "LM4_SUCCESSOR": {"A.8", "E.59", "E.91", "E.92", "E.94", "E.97", "E.55"},
 "LM6_POINTS_AS_SECTIONS": {"E.98", "E.99", "E.100"},
}
for f in flags:
    if not f["flag"].startswith("dependency"):
        continue
    t = f["tag"]
    r = rows[t]
    run, rid = r["run"], r["id"]
    dep = r["depends_on"].replace("\\_", "_")
    for tok in [x.strip() for x in f["detail"].split(",") if x.strip()]:
        target, verdict = "", ""
        if ROMAN.match(tok) or re.match(r"^(ANT|CFT|ADT)\d", tok) or (re.match(r"^A\d\.\d", tok) and "Kahn" in dep):
            m = re.search(r"([A-Za-z][A-Za-z0-9_\-]*(?: (?:ADT|AV|CFT|ANT|LEC))?)[ ,;]*(?:Proposition |Theorem |Lemma )?(?:[IVXA]*\.?\d[\d.()a-z\-–]*[ ,/]*(?:and )?)*" + re.escape(tok), dep)
            verdict, target = "the literature", f"{m.group(1) if m else '?'} {tok}"
        elif re.match(re.escape(rid) + r"\.\d+$", tok) or (run == "LM7_FERMAT_TOWER" and re.match(r"^E\d+\.\d+$", tok)):
            verdict, target = "a sub-label inside the row's own proof", f"{t} ({tok})"
        elif re.match(r"^[A-Z]\.\d+\.\d+$", tok) and re.sub(r"\.\d+$", "", tok) in ids[run] and (run != "SECTION_GHOSTS" or tok.startswith("E.")):
            verdict, target = "a sub-label of another row of the run", f"{run}:{re.sub(r'.\d+$', '', tok)} ({tok})"
        else:
            other = None
            if run == "SECTION_GHOSTS":
                if re.match(r"^E\.\d+\.\d+$", tok) and tok.startswith(rid + "."):
                    other = None
                elif rid in SG_OVR["LM4_SUCCESSOR"] and tok != "D.50":
                    other = "LM4_SUCCESSOR"
                elif tok == "D.50":
                    other = "LM7_PUSH"
                elif rid in SG_OVR["LM6_POINTS_AS_SECTIONS"]:
                    other = "LM7_FERMAT_TOWER" if tok == "E.25" else "LM6_POINTS_AS_SECTIONS"
                elif re.match(r"^(A\.4\.\d+|C\.\d+\.\d+)$", tok):
                    other = "GT_TOWER_CHECK"
                else:
                    other = "SECTIONS_OVER_Q"
            elif run == "FERMAT_SUCCESSOR":
                other = "LM7_FERMAT_TOWER" if tok in ("D.61", "D.32", "D.45") else "LM7_PUSH"
            elif run == "LM6_POINTS_AS_SECTIONS":
                other = {"E.115": "LM7_FERMAT_TOWER", "E.117": "LM7_FERMAT_TOWER", "F17.7": "FLAGGED_149", "F.48": "LM5_MULTI_GALOIS_TOPOI"}.get(tok)
            if other and tok in ids.get(other, {}):
                verdict, target = "another run's id", f"{other}:{tok} ({ids[other][tok]})"
            elif other:
                base = re.sub(r"\.\d+$", "", tok)
                verdict, target = ("a sub-label of another run's row", f"{other}:{base} ({tok})") if base in ids.get(other, {}) else ("another run's id, not in its newest register", f"{other}:{tok}")
            elif re.match(re.escape(rid) + r"\.\d+$", tok):
                verdict, target = "a sub-label inside the row's own proof", f"{t} ({tok})"
            else:
                verdict, target = "nothing found", ""
        out.append((t, "dependency names no id of the run: " + tok, verdict, target, "", "script, with the audited run read from the row's text"))
# (c) proved row uses an Open row of its run (found in this sweep)
C = {
 "ANABELIAN_149_PUSH:F.16": ("ANABELIAN_149_PUSH:F.9", "no premise: F.9 is the open classification; F.16's own dependencies are CHW2024, Kummer theory, Dirichlet units"),
 "FLAGGED_149:ZCF2": ("FLAGGED_149:ZCF6", "citation of scope, not a premise (proof text read: CF_Z_agent.tex 105-109, 715-722, 935-940 cite ZCF6 only as what remains open)"),
 "FLAGGED_149:ZCF11": ("FLAGGED_149:ZCF6", "citation of scope, not a premise (proof text read)"),
 "FLAGGED_149:ZCF12": ("FLAGGED_149:ZCF6", "citation of scope, not a premise (proof text read)"),
 "LM6_POINTS_AS_SECTIONS:A.52": ("LM6_POINTS_AS_SECTIONS:A.22", "uses A.22's setting (the candidate subgroup C); A.22 records restrictions proved on any candidate (statement level)"),
 "LM6_POINTS_AS_SECTIONS:C.15": ("LM6_POINTS_AS_SECTIONS:C.12", "uses the fibre calculation recorded inside the Open row C.12 (statement level); the Open row mixes proved computations and the open classification"),
 "LM6_POINTS_AS_SECTIONS:D.10": ("LM6_POINTS_AS_SECTIONS:D.8", "uses Proposition D-literal-minimum, which is proved but filed inside the Open row D.8; split D.8 (CORRECTIONS)"),
 "LM6_POINTS_AS_SECTIONS:F.39": ("LM6_POINTS_AS_SECTIONS:F.24", "uses the proved half of F.24 (the local conditions characterize the geometric tangent subtorsor over Q, Prop. F-local-global-units); split F.24 (CORRECTIONS)"),
 "LM6_POINTS_AS_SECTIONS:F.45": ("LM6_POINTS_AS_SECTIONS:F.24", "as F.39: the proved half of F.24 over Q"),
 "LM6_POINTS_AS_SECTIONS:F.46": ("LM6_POINTS_AS_SECTIONS:F.24", "as F.39, over K=Q"),
 "LM7_PUSH:E.6": ("LM7_PUSH:E.3", "uses the 24 candidates defined in E.3's analysis, not an answer to E.3 (statement level)"),
 "LM7_PUSH:E.46": ("LM7_PUSH:E.3", "a further finite test on E.3's candidates"),
 "LM7_PUSH:E.50": ("LM7_PUSH:E.3", "a further finite test on E.3's candidates"),
 "LM7_PUSH:E.65": ("LM7_PUSH:E.3", "names E.3 as the remaining task ('The remaining Task E.3 is precisely ...'); not a premise"),
 "SECTION_GHOSTS:C.4": ("SECTION_GHOSTS:A.7", "false edge: the 'A.7' of C.4 is GT_TOWER_CHECK A.7 ('it does not verify A.7 or the explicit compiler A.4.57'), not SECTION_GHOSTS A.7"),
 "SECTION_GHOSTS:E.2": ("SECTION_GHOSTS:A.7, SECTION_GHOSTS:E.1", "false edges: E.2's A.7 is GT_TOWER_CHECK A.7, and E.1 is named only to place the pending A.4.57 outside E.2's list"),
}
for t, (o, note) in C.items():
    out.append((t, "proved row uses an Open row of its run (found in sweep 1): " + o, "no inconsistency", rows[t]["where_proved"][:160], note, "read"))
with open(HERE / "FLAG_VERDICTS.tsv", "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["tag", "flag", "verdict", "place", "note", "how decided"])
    w.writerows(out)
c = collections.Counter((o[1].split(":")[0], o[2]) for o in out)
for k, v in sorted(c.items()):
    print(v, k)
