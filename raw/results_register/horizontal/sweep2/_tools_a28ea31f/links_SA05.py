# SA05 (Théorie des motifs I): interlinking data, sweep 2 part 2. Claude Opus 5.5 at effort max, a28ea31fa17dd65e1.
ORDER = ["SA05-1", "SA05-2", "SA05-16", "SA05-11", "SA05-12", "SA05-20", "SA05-8", "SA05-9", "SA05-21", "SA05-10", "SA05-13",
         "SA05-18", "SA05-19", "SA05-14", "SA05-15", "SA05-3", "SA05-4", "SA05-5", "SA05-7", "SA05-17"]
STATUS = {
    "SA05-1": ("his construction; known as definitions", "The category of correspondences V^A of a cohomology theory (Manin 1968; Kleiman 1968)."),
    "SA05-2": ("conjectures, open", "The standard conjectures as he lettered them (A-D); Lefschetz type open in general, known for abelian varieties in characteristic 0 (Lieberman 1968); Hodge type known in characteristic 0."),
    "SA05-16": ("his programme, open", "The cote 16 programme: the Lefschetz correspondence ring and the singular-hypersurface question."),
    "SA05-11": ("his claims; known in characteristic 0", "Positive forms and polarizations; the Hodge standard conjecture holds in characteristic 0 (Hodge-Riemann) and is open in characteristic p beyond surfaces."),
    "SA05-12": ("his construction; known as definitions", "Abstract motives, projectors, Künneth, Tate inversion, effectivity, niveau (MPL_12_150-168, M notes); numerical motives are semisimple (Jannsen 1992)."),
    "SA05-20": ("his text; known", "The tannakian text of cote 10 (B series): the plan of a treatise on tensor categories; Saavedra (1972), Deligne-Milne (1982)."),
    "SA05-8": ("his claims; known in part", "The motivic Galois group (conditional on the standard conjectures; unconditional variants: André 1996, Nori, Ayoub); with the Serre group S_K and CM structures (cote 15, 139-168)."),
    "SA05-9": ("his claims; known in part", "Weights and levels; weights by Deligne (Weil I, II)."),
    "SA05-21": ("his conjectures, withdrawn by him; settled since", "The Hodge group and the letter to Mumford (Algiers, 1 Nov 1965): decided on the scans in part 2."),
    "SA05-10": ("his claims; open in general", "Absolute cohomology of motives and arithmetic; with 'Calculs de cohomologie absolue des Motifs de Tate Z(n)' (cote 15, 172-178)."),
    "SA05-13": ("his conjectures, open", "Smooth integral motives over a base; the one-prime independence conjecture."),
    "SA05-18": ("his notes; known conditionally", "Motives over finite fields (cote 15, 2-14), = H046; Milne (1994), conditional on the Tate conjecture."),
    "SA05-19": ("his notes; known in substance", "Deuring's gerbes and norm categories (cote 15, 16-32), = H045; Deuring (1941)."),
    "SA05-14": ("his question; known in parts", "Linear against nonlinear: Hom of Jacobians against Hom of curves (Faltings 1983; Mochizuki 1999)."),
    "SA05-15": ("known", "Oda (1969)."),
    "SA05-3": ("= SA18-16", "See SA18."),
    "SA05-4": ("= SA18-2", "A cancelled group-scheme text, with the B10-01..03 sections 10-11 (affine group preschemes)."),
    "SA05-5": ("= SA18-3", "Delzant's offprint."),
    "SA05-7": ("reused typescript; proved since", "Tits's centre conjecture for spherical buildings, a theorem since 2006-2013 (Mühlherr-Tits; Leeb-Ramos-Cuevas; Ramos-Cuevas)."),
    "SA05-17": ("documents and registers", "Titles, page counts, reused typescripts (EGA 0, reflexive modules, invariant forms, valuations), the papers list of K18-01."),
}
DEPENDS = [
    ("SA05-2", "SA05-1", "proof", "", "the standard conjectures are statements on correspondences"),
    ("SA05-16", "SA05-2", "his page", "cote 16 (the Lefschetz correspondence ring)", ""),
    ("SA05-11", "SA05-2", "proof", "", "the Hodge standard conjecture gives the positivity"),
    ("SA05-12", "SA05-1", "proof", "12:150-151 (M01)", "motives as the pseudo-abelian envelope of correspondences"),
    ("SA05-12", "SA05-2", "our note", "MPL_12_150-168+15_002-033 M02-M04", "semisimplicity and numerical equivalence"),
    ("SA05-12", "SA05-11", "our note", "M17 'Positive trace is the semisimplicity ...'", ""),
    ("SA05-8", "SA05-12", "proof", "", "the Tannaka group of the category of motives"),
    ("SA05-8", "SA05-20", "proof", "", "the tannakian formalism"),
    ("SA05-9", "SA05-12", "proof", "", "weights and niveau on motives"),
    ("SA05-21", "SA05-8", "his page", "13:16 'considerations of motive-theoretic galois theory'", "the modular varieties gamma/Gamma"),
    ("SA05-10", "SA05-12", "proof", "", "Ext groups of motives"),
    ("SA05-13", "SA05-12", "proof", "", ""),
    ("SA05-18", "SA05-8", "proof", "", "the motivic Galois group of F_q: the Weil-number protorus"),
    ("SA05-18", "SA05-9", "proof", "", "weights of Frobenius"),
    ("SA05-19", "SA05-18", "proof", "", "Deuring's gerbe is the supersingular part"),
    ("SA05-14", "SA05-12", "proof", "", "Hom of motives against Hom of curves"),
]
ITEMLINKS = {
    "SA05-1": [("known", "Manin (1968); Kleiman (1968, 1972)", "literature", "")],
    "SA05-2": [("open", "the standard conjectures; Lieberman (1968) for abelian varieties in characteristic 0", "literature", "")],
    "SA05-11": [("known in characteristic 0", "Hodge-Riemann bilinear relations; open in characteristic p beyond surfaces", "literature", "")],
    "SA05-12": [("known", "Kleiman (1972); Jannsen (1992), numerical motives are semisimple", "literature", "")],
    "SA05-20": [("known", "Saavedra (1972); Deligne-Milne (1982)", "literature", "")],
    "SA05-8": [("known in part", "Deligne-Milne (1982); André (1996); Nori; Ayoub", "literature", "")],
    "SA05-9": [("known in part", "Deligne, Weil I-II", "literature", "")],
    "SA05-21": [("known since", "Griffiths transversality (1968); Griffiths-Robles-Toledo (2014): quotients of non-classical flag domains are not algebraic; Borel density for his margin question", "literature", "")],
    "SA05-18": [("known conditionally", "Milne, 'Motives over finite fields' (1994)", "literature", "")],
    "SA05-19": [("known in substance", "Deuring (1941)", "literature", "")],
    "SA05-14": [("known in parts", "Faltings (1983); Mochizuki (1999)", "literature", "")],
    "SA05-7": [("proved since", "Tits's centre conjecture (Mühlherr-Tits; Leeb-Ramos-Cuevas; Ramos-Cuevas, 2006-2013)", "literature", "")],
}
ENTRYLINKS = {
    "codex:H13-01#1": [("decided on the scan", "he withdraws the conjecture that the modular families of Hodge structures on gamma/Gamma are algebraic: as stated it contradicts Tate's conjecture (case G(R) compact, a simply connected projective homogeneous space); he keeps a necessary genericity condition (13:20)",
                        "passage read 13:14, 13:19, 13:20", "REPORTS/mumford_letter_cote13.md"),
                       ("known since", "Griffiths transversality (1968); Griffiths-Robles-Toledo (2014)", "literature", "")],
}
CORRECTIONS = [
    ("codex:H13-01#1", "filed as 'steps the writer marks as unverified'", "the letter withdraws a conjecture ('a bit rash with the conjectures I told you about Hodge structures') and states a replacement necessary condition", "passage read 13:14-20"),
    ("SA05-18, SA05-19 (part 1)", "new SA05 items for the cote 15 half of MPL_12_150-168+15_002-033", "the same objects as SA06-9/H046 and SA06-8/H045: to be merged in the global build", "item comparison"),
]
INTRO = """
SA05 is cotes 10-13 and parts of 14-18 (Théorie des motifs I): correspondences and the standard conjectures (cote 11-12),
abstract motives and the motivic Galois group (cote 12, MPL_12_150-168), the tannakian text and a group-scheme text
(cote 10, B series), the Hodge group and the letter to Mumford (cote 13), motives over finite fields and Deuring's gerbes
(cote 15, 2-32), the Serre group and CM structures, absolute cohomology of Z(n) (cote 15, 139-178), the cote 16
programme. Reading decided on the scans in sweep 2: REPORTS/mumford_letter_cote13.md.
"""
