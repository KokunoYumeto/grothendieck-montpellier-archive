# SA05 (Théorie des motifs, part 1: cotes 11, 12): items, read decisions, flags and checks.
# Claude Opus 5.5 at effort max (a28ea31fa17dd65e1), horizontal sweep 1, 18 Nov 2026.
# First reading only: the provisional Pro dossier SA04_v1_final (GPT-6 Astra, ChatGPT Pro mode), whose 380 entries are all
# 'pending', one item per entry, no merges; its package list equals SA05's.
# MPL_11_043-058+56 is shared with SA18: SA05-1, -3, -4, -5 contain the same objects as SA18-15, -16, -2, -3.
CLUSTERS = [
 ("SA05-2", "Grothendieck's standard conjectures as he lettered them (draft and printed A-D): Lefschetz operators, the inverse and lowering maps, the content of each letter",
  r"lettering|conjecture letters|Standard-conjecture dictionary|A–D dictionary|inverse-map calculation|lowering operator|^CL0\d|Quantifiers and the contribution|lettering table"),
 ("SA05-14", "linear versus nonlinear statements: Hom of Jacobians against Hom of curves, the anabelian analogies (cote 12)",
  r"Linear statement|^LN0\d|nonlinear comparison"),
 ("SA05-15", "Oda's comparison of de Rham/Dieudonné realizations in characteristic p", r"\bOda\b|^ODA"),
 ("SA05-16", "the cote 16 programme: the Lefschetz correspondence ring and the singular-hypersurface questions", r"cote 16|cote 14 continue|singular-hypersurface"),
]
SECTION_MAP = {
 ("MPL_11_002-042", "Findings"): "SA05-17",
 ("MPL_11_002-042", "Question 1"): "SA05-2",
 ("MPL_11_002-042", "Question 2"): "SA05-1",
 ("MPL_11_002-042", "Handwritten questions"): "SA05-1",
 ("MPL_11_002-042", "Connections to cote 16"): "SA05-1",
 ("MPL_11_002-042", "Lettering comparison"): "SA05-2",
 ("MPL_11_002-042", "Reading questions"): "SA05-1",
 ("MPL_11_002-042", "Explicit editorial"): "SA05-1",
 ("MPL_11_002-042", "Reused typed sheets"): "SA05-7",
 ("MPL_11_002-042", "Standing question"): "SA05-17",
 ("MPL_11_002-042", "Results-state"): "SA05-17",
 ("MPL_11_043-058+56", "Answers"): "SA05-1",
 ("MPL_11_043-058+56", "A."): "SA05-1",
 ("MPL_11_043-058+56", "B."): "SA05-3",
 ("MPL_11_043-058+56", "C."): "SA05-4",
 ("MPL_11_043-058+56", "D."): "SA05-5",
 ("MPL_11_043-058+56", "E."): "SA05-1",
 ("MPL_11_043-058+56", "Primary"): "SA05-17",
 ("MPL_12_002-050", "Answers"): "SA05-8",
 ("MPL_12_051-098", "0."): "SA05-17",
 ("MPL_12_051-098", "1."): "SA05-8",
 ("MPL_12_051-098", "5."): "SA05-17",
 ("MPL_12_051-098", "9."): "SA05-17",
 ("MPL_12_099-149", "2."): "SA05-17",
 ("MPL_12_099-149", "4."): "SA05-9",
 ("MPL_12_099-149", "5."): "SA05-9",
 ("MPL_12_099-149", "6."): "SA05-14",
 ("MPL_12_099-149", "7."): "SA05-13",
 ("MPL_12_099-149", "8."): "SA05-12",
 ("MPL_12_099-149", "9."): "SA05-15",
 ("MPL_12_099-149", "10."): "SA05-12",
 ("MPL_12_099-149", "11."): "SA05-17",
 ("MPL_12_099-149", "12."): "SA05-17",
 ("MPL_12_099-149", "13."): "SA05-17",
}
EXTRA_OBJECTS = {
 "SA05-1": "the category of correspondences V^A of a cohomology theory A (Hom(X,Y)=A(X x Y)): composition, units, graphs and transposes, signs, degree rules, stable systems A' in A, Poincaré algebras, tautological classes (cote 11)",
 "SA05-3": "the cohomology of quadrics (= SA18-16)",
 "SA05-4": "a cancelled group-scheme text: reductive centre, maximal tori, the Weyl group (= SA18-2, its cote 11 part)",
 "SA05-5": "Delzant's offprint: the Witt ring, Stiefel-Whitney and Clifford invariants, Brauer generation (= SA18-3, its cote 11 part)",
 "SA05-7": "a reused typescript on spherical buildings: Tits's centre conjecture, geodesics, parabolic characters, proper actions, descent and quotients (cote 11)",
 "SA05-8": "the motivic Galois group: fibre functors, arithmetic quotients, Hodge groups, the exact sequence over Q, the Tannakian formalism, the period torsor and the period conjecture (cote 12)",
 "SA05-9": "weights and levels of motives and l-adic sheaves: weight bounds, coniveau, dimension type, Hodge level, admissibility, direct images, spectral-sequence degeneration (cote 12)",
 "SA05-10": "absolute cohomology of motives and arithmetic: Ext and effaceability, Ind-motives, the finiteness conjectures (Tate, BSD, Sha, Brauer), the G_m calculation, rational points, zeta and L-invariants (cote 12, scans 051-098)",
 "SA05-11": "positive forms and polarizations: the positive cone, orthogonal splitting, semisimplicity and isotypic components (cote 12)",
 "SA05-12": "abstract motives: the universal pseudo-abelian additive target, projectors and their splitting, semisimplicity, Schur projectors in characteristic zero, Lefschetz structures, Galois descent (cote 12, scans 137-149)",
 "SA05-13": "smooth integral motives over a base: the one-prime independence conjecture, integral structures, extension over the base, the essential image (cote 12)",
 "SA05-17": "the dossiers as documents and registers: evidence keys, title sheets, page counts, results-register uptake, references",
}
BODY_RULES = []
FORCE = {}
for f, k in (("K11-01", "SA05-1"), ("K11-02", "SA05-1"), ("K11-03", "SA05-1"), ("K11-04", "SA05-1"), ("K12-01", "SA05-8"),
             ("K12-02", "SA05-8"), ("K12-03", "SA05-9"), ("K12-04", "SA05-10"), ("K12-05", "SA05-10"), ("K12-06", "SA05-11"),
             ("K12-07", "SA05-9"), ("K12-08", "SA05-9"), ("K12-09", "SA05-12")):
    for n in range(1, 8):
        FORCE[f"work:{f}#{n}"] = k
# cote 12, scans 051-098, notes in scan order (MPL_12_051-098, section 3): by number
for n in range(13, 77):
    i = n - 12  # N001..N064
    k = ("SA05-9" if i in (1, 2, 7, 14, 30, 31, 50, 57, 58) else
         "SA05-11" if 46 <= i <= 56 else
         "SA05-8" if i in (3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17) else
         "SA05-15" if i == 63 else
         "SA05-10")
    FORCE[f"MPL_12_051-098#{n}"] = k
FORCE.update({"MPL_12_002-050#4": "SA05-12", "MPL_12_002-050#5": "SA05-8", "MPL_12_002-050#6": "SA05-12",
              "MPL_12_002-050#7": "SA05-9", "MPL_12_002-050#8": "SA05-9", "MPL_12_002-050#9": "SA05-8",
              "MPL_12_002-050#1": "SA05-14", "MPL_12_002-050#3": "SA05-2",
              "MPL_11_002-042#60": "SA05-15", "MPL_11_002-042#61": "SA05-1",
              "MPL_11_043-058+56#1": "SA05-2"})
LMLENS = r"\bLM\d?\b|prime-to-p point problem|Results-register|results-register|RESULTS_STATE|tower register"
D = "2026-11-18"
READ = {
 "MPL_12_099-149#26": ("entry-read", "not checked", "", "Hodge level bound of Corollary 5.4 tested on an elliptic curve"),
 "MPL_12_099-149#71": ("entry-read", "not checked", "", "'Tout morphisme u:P->Q est direct' against Hua's 'monomorphismes'"),
}
for n in range(13, 62):
    READ.setdefault(f"MPL_11_002-042#{n}", ("entry-read", "not checked", "", "coded heading; placed from the note's witness anchor"))
FLAGS = [
 ("suspected misreading", "MPL_12_099-149#26 (W21; cote 12, scan 115, opening display)",
  "the transcription reads the level bound '2(n−i+j)'; for an elliptic curve (n=i=1, j=0) it gives level 0 at weight 1, but H^1 has Hodge level 1; the expression '2n−i+j' of scan 108 (and of Hua's reading) passes. The parentheses may be a misreading, or the slip is his. Decide on the scan.",
  "MPL_12_099-149_notes.md W21; the test is mine and the note's"),
 ("the same thing noted with different readings or statements", "MPL_12_099-149#71 (M08; cote 12, scan 148, line 20)",
  "our reading 'Tout morphisme u:P->Q est \"direct\"' against Michel Hua's account (a condition first for monomorphisms, then corrected to all morphisms); to decide on the scan", "MPL_12_099-149_notes.md M08"),
 ("the same thing noted with different readings or statements", "MPL_12_051-098#53 (N041; cote 12)",
  "a later vanishing on the pages contradicts the earlier degree-two example (N037: the constant Jacobian gives a nonzero degree-two term); the pages are in tension with themselves, the note records it", "headings N037, N041"),
 ("a link across folders", "MPL_11_043-058+56 (107 entries, shared with SA18)",
  "SA05-1, SA05-3, SA05-4, SA05-5 are the same objects as SA18-15, SA18-16, SA18-2, SA18-3", "NOTES_INDEX of SA05 and SA18"),
 ("a link across folders", "SA05-2 (standard-conjecture lettering) with SA18-12 and the MPL_11_043-058+56 planning answer",
  "the draft and printed lettering of the standard conjectures is asked in cote 11, cote 12 and the shared package; one object with SA18-12", "headings"),
 ("the LM/Dérivateurs lens", "MPL_12_099-149#45 (LN07)",
  "'The prime-to-p point problem is not answered here': the note reads cote 12 through the research run's point-section question (ANABELIAN A1)", "heading"),
 ("note overstates or misreads the page", "SA04_v1_final (provisional Pro dossier, first reading)",
  "not a misreading: the dossier is a scaffold; all 380 entries 'pending', one item per entry, no claims, links or readings. Its only content beyond the index is the Codex leads B12-01/B12-02 (scan 123: Deligne's theorem 'modulo a Lefschetz theorem', the word uncertain; scan 134: 'référence introuvable !!').",
  "grothendieck_archive_transcription_20261110/stage_a_20261118_sent/returns/SA04_v1_final_20261118T1335Z_unzipped/SA04_dossier.md"),
]
CHECKS = [
 ("MPL_12_099-149#26", D, "claim checked by computation: for an elliptic curve (n=i=1, j=0) the bound 2(n-i+j)=0 contradicts Hodge level 1 of H^1, while 2n-i+j=1 agrees", "the note's test is right; the reading is to be decided on the scan", "results_register/horizontal/inputs/SA05/pro/MPL_12_099-149_notes.md (W21)"),
]
STATEMENTS = {
 "SA05-1": ("(notes) from any 'cohomology' A with Künneth and Poincaré duality, a category with Hom(X,Y)=A(X x Y), composition by pullback, product and pushforward", "worked out with sign and centrality warnings ('Mais c'est faux', 'att. signe!')", "SA18-15; SA06, SA07 (motives)"),
 "SA05-8": ("(notes) the motivic Galois group as the group of a fibre functor, with arithmetic quotients and an exact sequence over Q", "programme, partly conjectural", "SA06, SA07, SA15-6"),
 "SA05-9": ("(notes) weight and level bounds for direct images of l-adic sheaves and motives", "stated, with a disputed bound (W21)", "SA14-10, SA06, SA07"),
}
