# SA06 (Théorie des motifs, part 2: cotes 14, 15): items, read decisions, flags and checks.
# Claude Opus 5.5 at effort max (a28ea31fa17dd65e1), horizontal sweep 1, 18 Nov 2026.
CLUSTERS = [
 ("SA06-1", "linear versus nonlinear statements: Tate Hom against anabelian Hom, semisimplicity and centres, polarizations and real structures, weights and cyclotomic normalizers (= SA05-14)",
  r"linear statement|non-linear statement|Tate Hom and anabelian Hom|Semisimplicity and centres|Weights and cyclotomic normalizers|Polarizations and real structures"),
 ("SA06-17", "Michel Hua's project: findings and section titles for cotes 14 and 15 (credited)", r"\bHua\b"),
]
SECTION_MAP = {
 ("MPL_14_002-044", "The requested table"): "SA06-1",
 ("MPL_14_002-044", "Effectivity"): "SA06-2",
 ("MPL_14_002-044", "Albanese"): "SA06-3",
 ("MPL_14_002-044", "Tate classes"): "SA06-4",
 ("MPL_14_002-044", "Reused typed"): "SA06-11",
 ("MPL_14_002-044", "Standing question"): "SA06-13",
 ("MPL_14_087-132", "1."): "SA06-3",
 ("MPL_14_087-132", "2."): "SA06-11",
 ("MPL_14_087-132", "3."): "SA06-5",
 ("MPL_14_087-132", "4."): "SA06-6",
 ("MPL_14_087-132", "5."): "SA06-7",
 ("MPL_14_087-132", "6."): "SA06-12",
 ("MPL_14_087-132", "7."): "SA06-13",
 ("MPL_14_087-132", "8."): "SA06-13",
 ("MPL_15_034-086", "Scope"): "SA06-13",
 ("MPL_15_034-086", "Planning"): "SA06-12",
 ("MPL_15_034-086", "Deuring"): "SA06-8",
 ("MPL_15_034-086", "Brandt"): "SA06-8",
 ("MPL_15_034-086", "Compact tori"): "SA06-9",
 ("MPL_15_034-086", "Reused"): "SA06-11",
 ("MPL_15_087-138", "Requested table"): "SA06-1",
 ("MPL_15_087-138", "Frobenius, norms"): "SA06-9",
 ("MPL_15_087-138", "Valuation descent"): "SA06-9",
 ("MPL_15_087-138", "Real fibre functors"): "SA06-10",
 ("MPL_15_087-138", "Lefschetz correspondences"): "SA06-2",
 ("MPL_15_087-138", "Reused texts"): "SA06-11",
 ("MPL_15_087-138", "Title sheets"): "SA06-13",
 ("MPL_15_087-138", "Proof E"): "SA06-10",
 ("MPL_15_087-138", "Context searches"): "SA06-13",
 ("MPL_15_087-138", "Primary references"): "SA06-13",
 ("MPL_15_170-194r", "Status"): "SA06-13",
 ("MPL_15_170-194r", "1."): "SA06-14",
 ("MPL_15_170-194r", "2."): "SA06-3",
 ("MPL_15_170-194r", "3."): "SA06-10",
 ("MPL_15_170-194r", "4."): "SA06-15",
 ("MPL_15_170-194r", "5."): "SA06-2",
 ("MPL_15_170-194r", "6."): "SA06-2",
 ("MPL_15_170-194r", "7."): "SA06-11",
 ("MPL_15_170-194r", "8."): "SA06-12",
}
EXTRA_OBJECTS = {
 "SA06-2": "effectivity of motives and the motivic group: the character cone, cocharacters, Tate effectivity, the Lefschetz sl2 and its lowering operators, Nori-Ayoub, the numerical quotient, the exact sequence over Q, the period torsor (cotes 14, 15)",
 "SA06-3": "algebraic and Albanese equivalence of cycles: intersection constructions, algebraic homomorphisms, transposition, zero-cycles, the universal cycle, Abel-Jacobi, Künneth projectors of curves (cote 14)",
 "SA06-4": "Tate classes and the letter to Serre: formulations of the Tate conjecture, a quintic threefold test, powers of elliptic curves (Mumford), the Frobenius wording (cote 14)",
 "SA06-5": "ampleness and positivity: the Nakai-Mumford criterion, numerical criteria, constants fields, polar cones (cote 14, scans 094-100)",
 "SA06-6": "Lefschetz theorems, global and local: restriction and Gysin tables, invariant cycles, affine complements and punctured cones, small-dimensional examples (cote 14, scans 103-117)",
 "SA06-7": "boundedness of families of cycles, representability, zero-cycles and the Albanese, the generic motive (cote 14, scans 118-131)",
 "SA06-8": "Deuring gerbes: supersingular elliptic curves, quaternion orders, their Brandt and Picard categories, crystalline orientations, real gerbes (cote 15, scans 034-078)",
 "SA06-9": "CM motives over finite fields: Frobenius as a character, norms, CM fields, compact tori, the maximal CM quotient and valuation descent (cote 15)",
 "SA06-10": "real fibre functors, polarizations and gerbes; effectivity from a cocharacter; the Artin-Tate arithmetic quotient and rational Artin correspondences (cote 15)",
 "SA06-11": "reused typed and printed leaves: sheaf double commutants, Morita, reflection groups and chambers, foundations sheets, algebraic-group results, Lie and root-system leaves",
 "SA06-12": "the notes' answers to the programme's planning questions (A-D lettering, cote 16, S15, periods, the results register)",
 "SA06-13": "the dossiers as documents: titles, covers, page counts, internal pagination, references, context searches",
 "SA06-14": "his agenda of scan 170: odd-weight motives and Weil-type abelian varieties, positivity, class fields, L-functions and the Riemann hypothesis",
 "SA06-15": "fibre functors in characteristic p: the fundamental object, crystalline and de Rham-Hodge realizations, Oda, Lang, FV=p, p-adic points (cote 15, scans 186-203)",
 "SA06-16": "étale cohomology of curves over finite fields: Tate twists, change of coefficients, H^1, the Brauer group (cote 15, scans 172-176)",
}
FORCE = {}
for f, k in (("K14-02", "SA06-3"), ("K14-03", "SA06-3"), ("K14-04", "SA06-4"), ("K14-05", "SA06-3"), ("K14-06", "SA06-3"),
             ("K14-08", "SA06-6"), ("K14-09", "SA06-7"), ("K15-02", "SA06-8"), ("K15-05", "SA06-10"), ("K15-06", "SA06-16"),
             ("K15-07", "SA06-15"), ("K15-08", "SA06-15")):
    for n in range(1, 8):
        FORCE[f"work:{f}#{n}"] = k
FORCE["MPL_14_087-132#74"] = "SA06-1"
LMLENS = r"\bLM\d?\b|results register|Results|register questions|Ledger effect|R LM6|S15|README"
D = "2026-11-18"
READ = {}
FLAGS = [
 ("the LM/Dérivateurs lens", "MPL_14_087-132#79 (M20; cote 14, scan 129)",
  "'deleted Cartan normalizer; R LM6 A.50 and A.22': a deleted line on cote 14 is read against the research run LM6's normalizer question (N2)", "heading"),
 ("a link across folders", "SA06-2 (cotes 14, 15) with SA05-8, SA05-2, SA18-12, SA15-6",
  "the motivic group, the Lefschetz sl2, the A-D lettering and the exact sequence over Q are asked in cotes 11, 12, 14, 15, 16: one object family", "section titles"),
 ("a link across folders", "SA06-8 (Deuring gerbes, cote 15) with SA16 (elliptic curves) and SA18-3 (quaternion and quadratic forms)",
  "supersingular elliptic curves and quaternion orders are an elliptic-curve object seen from motives", "headings"),
 ("a link across folders", "SA06-3, SA06-7 (cote 14) and SA18-14, SA19, SA14",
  "algebraic equivalence, the Albanese and boundedness of cycles: the same objects as the intermediate Jacobians of cote 44 (SA18-14)", "headings"),
 ("the same thing noted with different readings or statements", "MPL_15_170-194r#32 (PD10), #36 (PD14), #9 (PD16), #22 (HG03)",
  "four notes record differences from Michel Hua's reading of cote 15 (nonunique isomorphism; the 'canonical points' heading; a completed sentence and renumbering; an even-degree restriction); to decide on the scans", "headings"),
 ("a link across folders", "MPL_14_002-044#50 (A11), MPL_14_087-132#46 (Z01)",
  "his question on zero-cycles has a later negative answer (Mumford's theorem): a his-claim with a known outcome, to be linked to the literature in sweep 2", "headings"),
]
CHECKS = []
STATEMENTS = {
 "SA06-8": ("(notes) the category of supersingular elliptic curves as a gerbe banded by quaternion orders (Deuring), with orientations", "worked, with explicit unfinished identifications", "SA16"),
 "SA06-9": ("(notes) the motivic group of CM motives over a finite field through Frobenius characters and norms", "worked, with corrected examples", "SA05-8; Serre torus, Taniyama group"),
 "SA06-3": ("(notes) correspondences between Albanese and Picard varieties defined by algebraic cycles, with transposition", "partly proved; Theorem 3.1 self-flagged", "SA18-14, SA14"),
}
