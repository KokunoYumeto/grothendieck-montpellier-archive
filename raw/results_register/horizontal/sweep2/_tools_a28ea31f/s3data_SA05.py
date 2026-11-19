DEPENDS = [
    ("SA05-18", "uses", "SA05-8", "read", "15:3 (the gerbe of fibre functors of M and its band G; Tate, Tate-Honda)", "was 'proof' in sweep 2"),
    ("SA05-18", "uses", "SA05-9", "read", "15:7 (the grading i*: |lambda| = p^(nu/2)); 15:13 (epsilon i = squaring)", "was 'proof' in sweep 2"),
    ("SA05-19", "uses", "SA05-18", "read", "15:11 ('l'argument de Serre sur la courbe elliptique d'invariant de Hasse nul': the supersingular quaternion algebra)", "was 'proof' in sweep 2"),
    ("SA05-18", "uses", "SA15-2", "read", "15:3 (T_p: crystalline cohomology with values in F-crystals over Q_p)", "other topic"),
    ("SA05-21", "uses", "SA05-8", "read", "13:16 ('motive-theoretic galois theory') and 13:4-6 (Hodge structures on Rep(G))", "as in sweep 2"),
    ("SA05-21", "uses", "SA06-4", "read", "13:14, 13:19-20 (the contradiction with Tate's conjecture)", "other topic"),
]
CORRECTIONS = [
    ("sweep2 SA05-18 statement", "'motives over finite fields ... (cote 15, scans 2-14)'", "refined: 15:2-14 construct the motivic Galois gerbe of F_p: the Weil-number group, the H-gerbe class xi in H^2(Q, H) = H^2(Q, H^0) x H^2(Q, mu_2), trivial at l != p, the Frobenius character at p, nonzero mu_2-component at p and infinity", "read 15:2-14"),
    ("sweep3/SA05/HUNCHES.md H2 and RESEARCH_PACKAGES.md RP-SA05-2 (mine, earlier the same night)", "'the class xi in H^3(Brd(O), A*) of 15:19 is nontrivial for some Brandt groupoids'", "withdrawn: the class vanishes under his condition (C), which holds for maximal orders; RP-SA05-2 merged into RP-SA06-1", "his 15:74-78 (strict Picard categories) and 15:40 ('splittée'); SGA 4 XVIII 1.4"),
    ("MPL_12_150-168+15_002-033, even scans 4-12 of cote 15", "read as part of the motives package", "they are a reused typescript of Lipman, Publ. IHES 36 (1969), §25, pp. 159-163 (E8 singularity, factoriality); not his text; they date his pages to 1969 or later", "read 15:4-12"),
]
CHECKS = [
    ("MPL_12_150-168+15_002-033 (15:5)", "checked that the torsion of Gamma' = Gamma / <roots of unity, p> is Z/2: a torsion class is a root of unity times p^(m/n), and the weight condition |lambda| = p^(nu/2) forces m/n in (1/2)Z; generator sqrt(p)", "agrees", "sweep3/SA05/STUDY.md §1"),
    ("MPL_12_150-168+15_002-033 (15:13)", "checked epsilon i(lambda) = lambda^2 against the weights (Q(-1) has weight 2)", "agrees", "sweep3/SA05/STUDY.md §1"),
    ("MPL_12_150-168+15_002-033 (15:11)", "re-derived 'Serre's argument': a fibre functor over R would embed the quaternion algebra End^0 of a supersingular elliptic curve (ramified at p and infinity) into M_2(R), impossible for a division algebra of dimension 4", "agrees", "sweep3/SA05/STUDY.md §1"),
    ("MPL_12_150-168+15_002-033 (15:9-11)", "checked the local invariants: the mu_2-components are nonzero exactly at p and infinity, consistent with sum of inv = 0 and with the quaternion algebra B_{p,infinity}", "agrees", "sweep3/SA05/STUDY.md §1"),
    ("MPL_12_150-168+15_002-033 (15:22)", "checked his conditions Pic(A) = 0, Phi n A* = {1}, Phi A* = K* for A = Z and a definite quaternion algebra: Nrd(E*) = Q_{>0} by the Hasse-Schilling-Maass norm theorem", "agrees", "sweep3/SA05/STUDY.md §2"),
]
READ = {
    ("MPL_12_150-168+15_002-033", "15"): ("read in full (his odd scans 3-33; Lipman typescript on even scans 4-12 identified)", "motivic gerbe of F_p; Deuring categories"),
    ("MPL_12_150-168+15_002-033", "12"): ("not read in sweep 3", "abstract motives (M notes)"),
}
READY = {}
EXTRA_DELIV = [
    ("H13-01, J13-01..05 (Codex)", "13", "2-20 and J13 pages", "", "", "", "Codex web transcription with sheet notes; no Pro transcription", "read 13:2-20 (part 2, against the scans)", "after a check pass on the J13 pages; H13-01 (the letter) checked on scans 14, 19, 20", "the letter is English, in his hand"),
]
