# SA14 (Picard): items, read decisions, flags and checks.
# Claude Opus 5.5 at effort max (a28ea31fa17dd65e1), horizontal sweep 1, 18 Nov 2026.
CLUSTERS = [
 ("SA14-1", "the programme's carry questions on these cotes: the Fourier compatibility check (cote 47), the seven theorems of cote 44, dating (= SA18-5)",
  r"Fourier compatibility|Fourier question|Fourier witness|second Fourier|^W0[1-8]|Theorem [1-7]:|Theorem [1-7] of cote 44|seven-theorem|admitted (vanishing )?lemma|Relative dating|dated letters?|compatibility gap remains"),
 ("SA14-12", "Michel Hua's project: credited links and comparisons for these cotes", r"\bHua\b"),
]
SECTION_MAP = {
 ("MPL_57_089-132", "1."): "SA14-1", ("MPL_57_089-132", "2."): "SA14-2", ("MPL_57_089-132", "3."): "SA14-3",
 ("MPL_57_089-132", "4."): "SA14-4", ("MPL_57_089-132", "5."): "SA14-4", ("MPL_57_089-132", "6."): "SA14-4",
 ("MPL_57_089-132", "7."): "SA14-11",
 ("MPL_57_226-270", "1."): "SA14-1", ("MPL_57_226-270", "2."): "SA14-5", ("MPL_57_226-270", "3."): "SA14-5",
 ("MPL_57_226-270", "4."): "SA14-5", ("MPL_57_226-270", "5."): "SA14-6", ("MPL_57_226-270", "6."): "SA14-12",
 ("MPL_57_226-270", "7."): "SA14-13", ("MPL_57_226-270", "8."): "SA14-13",
 ("MPL_57_271-315", "1."): "SA14-1", ("MPL_57_271-315", "2."): "SA14-7", ("MPL_57_271-315", "3."): "SA14-7",
 ("MPL_57_271-315", "4."): "SA14-2", ("MPL_57_271-315", "5."): "SA14-8", ("MPL_57_271-315", "6."): "SA14-7",
 ("MPL_57_271-315", "7."): "SA14-13",
 ("MPL_58_020-067", "Scope"): "SA14-13", ("MPL_58_020-067", "I."): "SA14-3", ("MPL_58_020-067", "II."): "SA14-3",
 ("MPL_58_020-067", "III."): "SA14-3", ("MPL_58_020-067", "IV."): "SA14-3", ("MPL_58_020-067", "V."): "SA14-6",
 ("MPL_58_020-067", "VI."): "SA14-1", ("MPL_58_020-067", "VII."): "SA14-16", ("MPL_58_020-067", "IX."): "SA14-13",
 ("MPL_58_020-067", "X."): "SA14-13",
 ("MPL_60_002-035", "A."): "SA14-10", ("MPL_60_002-035", "B."): "SA14-10", ("MPL_60_002-035", "C."): "SA14-10",
 ("MPL_60_002-035", "D."): "SA14-10", ("MPL_60_002-035", "E."): "SA14-10", ("MPL_60_002-035", "F."): "SA14-16",
 ("MPL_60_002-035", "G."): "SA14-11", ("MPL_60_002-035", "References"): "SA14-13",
 ("MPL_60_036-070", "Research register I"): "SA14-10", ("MPL_60_036-070", "Research register II"): "SA14-11",
 ("MPL_60_036-070", "Research register III"): "SA14-16", ("MPL_60_036-070", "RESULTS_STATE"): "SA14-16",
}
EXTRA_OBJECTS = {
 "SA14-2": "the universal vector extension and connections on the Picard scheme (Picard-omega, rigidified extensions), compared with Oda's Dieudonné/de Rham theory",
 "SA14-3": "Lefschetz theorems for the Picard group and the fundamental group (SGA 2): restriction to hyperplane sections, connectedness, depth, formal comparison, effectivity (the conditions Lef/Leff)",
 "SA14-4": "existence and properness of the Picard functor: the Seshadri argument, the valuative criterion, units and vertical divisors, separation, existence by rigidification and descent, finiteness (Igusa's inequality)",
 "SA14-5": "the analytic criterion and the algebraization of Picard: Picard groups of germs, Mittag-Leffler, formal characteristic-zero Picard groups, projectivity and GAGA",
 "SA14-6": "local Picard groups of punctured spectra: isolated singularities, cones, factoriality, henselian rings (an extension he calls conjectural)",
 "SA14-7": "relative Picard objects and Néron-Severi: quotient definitions, polarizations, the rational cone, specialization of Néron-Severi and its torsion, Igusa's example",
 "SA14-8": "gluing, pinching and noncomplete varieties; the Picard group of a curve with several components",
 "SA14-9": "the theorem of the cube and the Picard functor of a product: multiplication pullback, marked invertible sheaves, rigid groups, composition laws",
 "SA14-10": "L-functions of l-adic sheaves on curves over finite fields: determinants, functional equations, epsilon factors, weights and purity, boundary terms, local epsilon constants and conductors",
 "SA14-11": "reused commutative-algebra typescripts: Fitting ideals, reflexive modules, Hensel factorization, monogenic algebras, differents, divisors and ramification, graded rings",
 "SA14-13": "the dossier as a document: titles, pagination, letters, reused typescripts, references",
 "SA14-14": "sections of torsors and their classes; determinants of perfect complexes, Riemann-Roch and the Weil sheaf (cote 59)",
 "SA14-16": "the notes' links to the research register and the planning questions (motivic category, LM6 tool, RESULTS_STATE coverage)",
}
FORCE = {}
for f, k in (("K57-01", "SA14-9"), ("K57-02", "SA14-9"), ("K57-03", "SA14-4"), ("K57-04", "SA14-4"), ("K57-05", "SA14-2"),
             ("K57-06", "SA14-6"), ("K57-07", "SA14-4"), ("K57-08", "SA14-4"), ("K57-09", "SA14-8"), ("K57-10", "SA14-11"),
             ("K58-01", "SA14-11"), ("K58-02", "SA14-11"), ("K59-01", "SA14-14"), ("K59-02", "SA14-14")):
    for n in range(1, 8):
        FORCE[f"work:{f}#{n}"] = k
LMLENS = r"\bLM\d?\b|tower register|research register|RESULTS_STATE|planning question|result register|motivic category sought"
D = "2026-11-18"
READ = {
 "MPL_60_036-070#24": ("passage-read", "agrees", "the Fitting ideals of a quotient module (typescript exercise 10 f, cote 60, scan 064)",
                       "the typescript states d_k(M/N) in d_k(M), the reverse of the correct inclusion; the note's counterexample M=A, N=aA, k=0 is right"),
 "MPL_60_036-070#14": ("entry-read", "not checked", "", "an intermediate equality on scan 057 that does not follow from its neighbours (L15)"),
 "MPL_57_226-270#41": ("entry-read", "not checked", "", "Hua reverses the direction of the global-projectivity example"),
}
FLAGS = [
 ("note overstates or misreads the page", "MPL_60_036-070#24 (A02; cote 60, scan 064, typescript exercise 10 f)",
  "not an overstatement: the note is right and the page is wrong. The typescript reads 'd_k(M/N) ⊂ d_k(M)'; with d_k = Fitt_k (its own definition a_k = c_{n-k}(R)) the correct inclusion is Fitt_k(M) ⊂ Fitt_k(M/N) (Stacks 07ZA(5)); M=A, N=aA, k=0 gives (a) ⊄ 0. The next line, the convolution inclusion, is right. Recorded here so that sweep 2 checks whether the typed symbol could be ⊃ on the scan.",
  "MPL_60_036-070_transcription.tex scan 64 (exercise 10 f); MPL_60_036-070_notes.md A02"),
 ("the same thing noted with different readings or statements", "MPL_57_226-270#41 (P04; cote 57)",
  "the note says Michel Hua's reading reverses the direction of the global-projectivity example; to decide on the scan", "heading"),
 ("a link across folders", "SA14-1 (sections 1. of three cote 57 packages, VI. of cote 58) and SA18-5, SA19-3",
  "the Fourier check of cote 47 and the seven theorems of cote 44 are asked in four more packages here; one global object with SA18-5", "section titles"),
 ("a link across folders", "MPL_57_089-132 (section 2.), MPL_57_271-315 (4.), work:K57-05 and SA18-14",
  "the universal vector extension with connection (Picard-omega) on cote 57 is the object of cote 54's universal extension (SA18-14)", "headings, unit titles"),
 ("the LM/Dérivateurs lens", "MPL_58_020-067#78 (N77)",
  "'A geometric tool for LM6 is not an arithmetic reduction proof': the note weighs a cote 58 Lefschetz-type statement as a tool for the research run LM6", "heading"),
]
CHECKS = [
 ("MPL_60_036-070#24", D, "note checked against the page (scan 064); claim checked by computation: Fitt_0(A)=0 and Fitt_0(A/aA)=(a) for a nonzero nonunit a of a domain", "agrees: the typescript's first inclusion in 10 f is reversed; the convolution inclusion is right", "results_register/horizontal/inputs/SA14/pro/MPL_60_036-070_transcription.tex (scan 64, item f)"),
]
STATEMENTS = {
 "SA14-3": ("(notes) Grothendieck-Lefschetz comparison for Pic and pi_1 of a hyperplane section (the SGA 2 conditions), with depth and formal comparison", "stated and partly proved; several steps self-flagged", "SA18, SA19; SGA 2"),
 "SA14-4": ("(notes) existence and properness of the relative Picard functor by Seshadri's argument and by rigidification and descent", "proved in parts; conditional statements", "SA18-17 (Picard functor of abelian schemes)"),
 "SA14-10": ("(notes) functional equations of L-functions of l-adic sheaves on curves over finite fields, with epsilon factors and boundary terms", "worked with sign and normalization questions", "SA05, SA06, SA07 (motives), the Weil conjectures"),
 "SA14-11": ("(page, typescript) Fitting ideals: the quotient inclusion is printed reversed", "stated as an exercise (typescript), with an error", "Bourbaki-style exercises"),
}
