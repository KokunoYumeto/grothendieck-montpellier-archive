# SA15 (Cristaux): interlinking data, sweep 2 part 2. Claude Opus 5.5 at effort max, a28ea31fa17dd65e1.
ORDER = ["SA15-14", "SA15-1", "SA15-2", "SA15-3", "SA15-6", "SA15-15", "SA15-9", "SA15-10", "SA15-16", "SA15-11", "SA15-18",
         "SA15-17", "SA15-19", "SA15-20", "SA15-8", "SA15-13", "SA15-4", "SA15-7", "SA15-12"]
STATUS = {
    "SA15-14": ("his text; known", "Divided powers (cote 5): PD-ideals, Gamma_A, the universal PD-Artinian ring W^(nu), valuations of n!, the DVR condition e <= p-1 (Berthelot 1974; Berthelot-Ogus 1978, §3)."),
    "SA15-1": ("his text and conjectures; known since", "The infinitesimal and crystalline site (cote 5, 28-31; cote 6, 2-21; cote 7, 3-15 and 54-72), the 'projet de théorie' of cote 6; crystalline cohomology is Berthelot's (1974)."),
    "SA15-2": ("his text; known", "F-crystals, p-crystals, Dieudonné crystals, bi-crystals of weight i and bi-isocrystals (cote 5, 15-20; cote 6, 8-12, 16)."),
    "SA15-3": ("his notes; known", "Dieudonné-Manin (Manin 1963); Barsotti's question and Manin's reports on formal groups (6:47-51)."),
    "SA15-6": ("his notes; known", "Tannakian categories of crystals (Saavedra 1972)."),
    "SA15-15": ("his programme and another's letter; known since", "p-adic cohomology before crystals: the letter docketed 'Lettre Deligne / sur coh. p-adiques' (5:49-53) and the cote 7 draft on Washnitzer-Monsky, de Rham comparison, Gauss-Manin (7:16-53); Monsky-Washnitzer (1968), later rigid cohomology."),
    "SA15-9": ("his text, partly admitted; known in substance", "Integral de Rham and Hodge cohomology, unit-root eigenvalues and semisimple parts (cote 4, numbered 8.1-8.5); 'Nous admettrons ... cohomologie cristalline' (4:4)."),
    "SA15-10": ("his text; known", "Duality of Dieudonné modules over truncated Witt rings A_n (cote 9, 2-8)."),
    "SA15-16": ("his conjectures, some withdrawn on the page; known since", "Crystalline Dieudonné theory of abelian schemes and Barsotti-Tate groups: 'je m'étais canulé' (6:22), section 2.7 retracts the preceding conjectures (6:27); Messing (1972), Mazur-Messing (1974), Berthelot-Breen-Messing (1982)."),
    "SA15-11": ("his text; known", "Deformations and the Hodge summand of ordinary abelian schemes, the Hasse invariant as a section of omega^(p-1) (cote 9, 15-29); Serre-Tate local moduli (Katz 1981)."),
    "SA15-18": ("his questions and conjectures; proved since", "Hodge-Tate theory (cote 6, 38-46), in his hand except the faint sheet 39 (Tate's); the decomposition is Tate's (1967) and Faltings' (1988)."),
    "SA15-17": ("his conjectures; known", "Reduction of elliptic curves over p-adic fields: ordinary good reduction and the extension class (cote 6, 33-37); Serre-Tate canonical lifts."),
    "SA15-19": ("his text, cover 14 March 1967; known", "Good reduction of abelian schemes and p-divisible groups (cote 100, odd scans 3-53 and 48-53); the criterion is SGA 7 IX; with 9:11-14 on inertia characters and the Serre-Tate 'THEOREM 12' leaf (5:4)."),
    "SA15-20": ("another's letter; known", "Étale duality without relative purity (5:50), SGA 4 XVIII."),
    "SA15-8": ("his formula and notes", "A boxed formula for groups of multiplicative type (8:78, matching Bergh-Rydh) and the canonical obstruction class to lifting over Z/n^2 (8:79-81, 'd'après Illusie')."),
    "SA15-13": ("his notes", "Rational double points and H^1(A, mu_2) (cote 8)."),
    "SA15-4": ("reused typescripts", "'Tribu' typescripts on jets and contact."),
    "SA15-7": ("reused typescript", "Purity, base change, coefficient twists (cote 8)."),
    "SA15-12": ("documents", "Covers, 'Tribu' numbers; in sweep 2 also the reused sheets of cote 100 (EGA III-IV errata and page proofs, English typescripts on quotients, letters of 7 April 1967 and of L. Illusie, 24 Feb 1968), printed leaves of cote 5, the EGA typescript on differentials (5:46-48), the spectral-theory typescript n. 357 (6:42-46)."),
}
DEPENDS = [
    ("SA15-1", "SA15-14", "his page", "5:21 cover 'Th. de De Rham à puissances divisées'; 5:28-31 the site built on PD-envelopes", ""),
    ("SA15-2", "SA15-1", "his page", "6:8 'p-crystal ... muni d'un morphisme de cristaux'", ""),
    ("SA15-3", "SA15-2", "proof", "", "classification of F-isocrystals"),
    ("SA15-6", "SA15-2", "proof", "", "tannakian categories of F-isocrystals"),
    ("SA15-1", "SA15-15", "his page", "7:54-60 'On va introduire des sites ad-hoc' after the Washnitzer-Monsky discussion of 7:18-53", "the site answers the problems of the cote 7 draft"),
    ("SA15-9", "SA15-1", "his page", "4:4 'Nous admettrons que ces relations restent valables dans le cas de la cohomologie cristalline'", ""),
    ("SA15-9", "SA15-2", "his page", "4:2 F and V on H^i(X) (x) W", ""),
    ("SA15-10", "SA15-16", "his page", "9:2 'dualité des modules de Dieudonné' for dual Barsotti-Tate groups", ""),
    ("SA15-16", "SA15-1", "his page", "6:22-23 H^1 crystalline de Rham and the Dieudonné module", ""),
    ("SA15-16", "SA15-2", "his page", "6:22 'on peut transposer F en un V'", ""),
    ("SA15-16", "SA15-14", "proof", "", "deformations of p-divisible groups need divided powers"),
    ("SA15-11", "SA15-16", "proof", "", "the Hodge filtration of the Dieudonné crystal under deformation"),
    ("SA15-18", "SA15-16", "proof", "", "Hodge-Tate for p-divisible groups first"),
    ("SA15-17", "SA15-16", "his page", "6:31-37 (3.1 the universal extension; 'relèvements de Serre')", ""),
    ("SA15-19", "SA15-16", "his page", "100:51 'bonne réduction' of G and prolongation of its p-divisible group", ""),
    ("SA15-19", "SA15-17", "proof", "", "the elliptic case first (cote 6)"),
]
ITEMLINKS = {
    "SA15-14": [("known", "Berthelot (1974); Berthelot-Ogus (1978), §3; the Stacks Project, divided power algebra", "literature", "")],
    "SA15-1": [("known since", "Grothendieck, 'Crystals and the de Rham cohomology of schemes' (1968); Berthelot (1974)", "literature", "")],
    "SA15-2": [("known", "F-crystals (Mazur; Katz; Berthelot-Ogus)", "literature", "")],
    "SA15-3": [("known", "Manin (1963)", "literature", "")],
    "SA15-6": [("known", "Saavedra (1972)", "literature", "")],
    "SA15-15": [("known since", "Monsky-Washnitzer (1968); rigid cohomology (Berthelot)", "literature", "the letter's doubts about constant Z_p coefficients are borne out")],
    "SA15-9": [("known in substance", "Mazur (1972); Illusie (1979), de Rham-Witt", "literature", "")],
    "SA15-10": [("known", "Oda (1969); Fontaine (1977)", "literature", "")],
    "SA15-16": [("known since", "Messing (1972); Mazur-Messing (1974); Berthelot-Breen-Messing (1982)", "literature", "")],
    "SA15-11": [("known", "Serre-Tate local moduli (Katz 1981); the Hasse invariant", "literature", "")],
    "SA15-18": [("proved since", "Tate (1967); Faltings (1988)", "literature", "")],
    "SA15-17": [("known", "Serre-Tate canonical lifts (Lubin-Serre-Tate 1964)", "literature", "")],
    "SA15-19": [("known", "SGA 7 IX (the p-divisible good-reduction criterion); Serre-Tate (1968); register ANABELIAN_149_PUSH:B.11 (Known) cites the SGA 7 criterion and B.11f proves a curve version", "literature and register", "")],
    "SA15-20": [("known", "SGA 4 XVIII", "literature", "")],
}
ENTRYLINKS = {
    "MPL_6_038-067+7_001-060#17": [("proved since", "the Hodge-Tate decomposition (Tate 1967 for p-divisible groups; Faltings 1988)", "literature", "the conjecture on 6:45 is in his hand (REPORTS/hands_formulaire_and_tate.md)")],
    "MPL_6_038-067+7_001-060#18": [("proved since", "the canonical isomorphism with H^q(X, Omega^p) after C_p-extension (Faltings 1988)", "literature", "his hand, 6:45")],
}
CORRECTIONS = [
    ("SA15 PLACEMENT (part 1), MPL_5+6_001-037 #5-#7", "placed as documents", "the 'THEOREM 12' leaf (5:4) is Serre-Tate's good reduction of CM abelian varieties: moved to SA15-19", "entry read"),
    ("MPL_5+6_001-037 #24, #25, #27", "placed under divided powers", "the upside-down reused typescript on 5:10 (a divisor of A^5): moved to SA15-12", "entry read"),
    ("MPL_5+6_001-037 #37, #38", "divided powers", "a proof-correction list for another document (5:14): SA15-12", "entry read"),
    ("MPL_5+6_001-037 #114-#118, #125-#129", "divided powers", "isolated printed leaves (5:34 quasi-functions on an abelian variety; 5:36 a height-type estimate): SA15-12", "entry read"),
    ("MPL_5+6_001-037 #189-#193, #199-#205", "divided powers", "an EGA typescript on differentials of complete semi-local rings (5:46, 5:48): SA15-12", "entry read"),
    ("MPL_5+6_001-037 #207-#210", "p-adic cohomology", "the duality part of the letter docketed 'Lettre Deligne' (5:50): new item SA15-20", "entry read"),
    ("MPL_5+6_001-037 #338, #339", "crystalline site", "bicrystals at every prime (6:16): SA15-2", "entry read"),
    ("MPL_6_038-067+7_001-060 #10, #16, #20, #21", "Hodge-Tate", "the reused spectral-theory typescript n. 357 (6:42-46): SA15-12", "entry read"),
    ("MPL_6_038-067+7_001-060 #104-#110", "crystalline site", "7:16-17 are about the p-adic cohomology candidate ('C'est faux malheureusement'): SA15-15", "entry read"),
    ("MPL_8_079-081+9+4+100 #24-#26", "duality over A_n", "the cancelled sheet 9:9 on the Gauss-Manin connection: SA15-15", "entry read"),
    ("MPL_8_079-081+9+4+100 #27-#40", "duality over A_n", "9:11-14 are on inertia characters and potentially good reduction: SA15-19", "entry read"),
    ("MPL_8_079-081+9+4+100, 45 notes on even scans 6-46 of cote 100", "good reduction", "those sheets are reused paper (English quotient-theory typescripts, a preface of 27 Oct 1963, EGA III-IV errata and page proofs, letters): SA15-12", "entry read"),
    ("SA15-15 statement (part 1)", "'the letter sur coh. p-adiques' without a writer", "its cover (5:49) reads 'Lettre Deligne / sur coh. p-adiques' (surname marked uncertain at the final letters by the note)", "entry read"),
    ("SA15 FLAGS (part 1) on the 'Gribouillis de Tate'", "the hands open", "decided on the images: only 6:39 is in another hand (Tate's); 6:38 and 6:40-46 are his", "passage read 6:38-45"),
]
INTRO = """
SA15 is cotes 4-9 and 100 (Cristaux). Cote 5: divided powers, the crystalline site, F-objects, printed and typed leaves,
a seminar programme, and a letter docketed 'Lettre Deligne / sur coh. p-adiques'. Cote 6: the 'projet de théorie' on
crystals (sections 1.1-3.2: crystals, p-crystals, Dieudonné crystals, the cohomology theory wanted, abelian schemes and
Barsotti-Tate groups), the reduction of elliptic curves, Tate-Hodge questions, Barsotti's question, deformations of
Barsotti-Tate extensions. Cote 7: stratified cohomology, the de Rham and p-adic cohomology draft around Washnitzer-Monsky,
the crystalline site. Cote 8: Frobenius and the lifting obstruction. Cote 9: duality of Dieudonné modules, the Hodge
summand and the Hasse invariant. Cote 4: integral de Rham and Hodge cohomology. Cote 100: 'Bonne réduction et groupes
p-divisibles' (March 1967) on odd scans, reused sheets on even scans. Sweep 2 read all 1,049 notes of the three new Pro
packages and moved 109 placements (REPORTS/SA15_reread.md).
"""
