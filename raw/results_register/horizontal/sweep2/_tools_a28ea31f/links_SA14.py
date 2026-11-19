# SA14 (Picard): interlinking data, sweep 2 part 2. Claude Opus 5.5 at effort max, a28ea31fa17dd65e1.
ORDER = ["SA14-11", "SA14-18", "SA14-9", "SA14-4", "SA14-7", "SA14-5", "SA14-3", "SA14-6", "SA14-8", "SA14-17", "SA14-2",
         "SA14-14", "SA14-10", "SA14-1", "SA14-16", "SA14-12", "SA14-13"]
STATUS = {
    "SA14-11": ("reused typescripts; known", "Commutative algebra (Fitting ideals, reflexive modules, Hensel factorization, Koszul, Cohen-Macaulay), used as paper and sometimes annotated."),
    "SA14-18": ("his text; known", "Pseudomorphisms (cote 57, scans 166-171); the notion is EGA IV §20.2's. The quasi-coherence proposition is withdrawn on the page."),
    "SA14-9": ("his text; known", "The theorem of the cube and the Picard functor of a product; an English letter (A57-02) on Corr and Raynaud's construction."),
    "SA14-4": ("his text; known", "Existence and properness of the Picard functor (FGA; Kleiman 2005): the Seshadri argument, divisors and frames (57:157-164), the Picard functor and its three variants (57:173-179)."),
    "SA14-7": ("his text; known", "Relative Picard objects and Néron-Severi (SGA 6 XIII)."),
    "SA14-5": ("his text; known", "The analytic criterion and the algebraization of Picard (SGA 2 XII)."),
    "SA14-3": ("his text; known", "Lefschetz theorems for Pic and pi_1 (SGA 2 X-XII)."),
    "SA14-6": ("his text; known in substance", "Local Picard groups of punctured spectra (SGA 2 XI; Boutot 1978); one extension he calls conjectural; 'Local Picard schemes' in English (A57-01)."),
    "SA14-8": ("his text; known", "Gluing, pinching and the Picard group of curves with several components (cote 57, scans 147-156)."),
    "SA14-17": ("his claim, marked 'à vérifier'; the mechanism is known", "The Kummer class for the Picard of a curve: xi_n = delta_n(eta) (57:144), decided on the scan in part 2."),
    "SA14-2": ("his text; known", "The universal vector extension and connections on Pic (Mazur-Messing 1974); Oda."),
    "SA14-14": ("his text; known", "Sections of torsors and their classes; determinants of perfect complexes and Riemann-Roch (Knudsen-Mumford 1976; Deligne 1987); the Weil sheaf (cote 59)."),
    "SA14-10": ("his text; known", "L-functions of l-adic sheaves on curves over finite fields, functional equations, epsilon factors (SGA 4 1/2, SGA 5; product formula: Laumon 1987)."),
    "SA14-1": ("the notes' carry questions", "FW and JAC notes read cote 57 against the cote 47 Fourier check and the cote 44 theorems; FW01-FW02 conclude no second witness."),
    "SA14-16": ("the notes' links", "Links to the research register and planning questions."),
    "SA14-12": ("credited comparison", "Michel Hua's readings for these cotes."),
    "SA14-13": ("documents", "Titles, covers, the Benjamin letter (Massy, 21 Nov 1966), reused typescripts."),
}
DEPENDS = [
    ("SA14-7", "SA14-4", "proof", "", "Néron-Severi is a quotient of the Picard scheme"),
    ("SA14-5", "SA14-4", "proof", "", "algebraization of the formal Picard functor"),
    ("SA14-3", "SA14-5", "proof", "", "Lefschetz for Pic passes through formal completion along a hyperplane section"),
    ("SA14-6", "SA14-3", "proof", "", "local Picard groups enter the local Lefschetz conditions (SGA 2 XI)"),
    ("SA14-8", "SA14-4", "proof", "", "Pic of a curve with several components"),
    ("SA14-17", "SA14-8", "his page", "57:144 (E = Pic^0 of the pinched curve Z)", "the generalized Jacobian of X with Y collapsed"),
    ("SA14-17", "SA14-4", "his page", "57:144 (P = Pic^1_{Z/S}, its class eta)", "the degree-one torsor"),
    ("SA14-2", "SA14-4", "proof", "", "the universal extension of Pic^0"),
    ("SA14-14", "SA14-4", "proof", "", "torsors under the Picard scheme and their classes"),
    ("SA14-10", "SA14-14", "proof", "", "epsilon factors and the functional equation through determinants of cohomology"),
    ("SA14-4", "SA14-18", "his page", "57:166-179 (the Picard functor section follows the pseudomorphisms)", "order of the sections; the use is not spelled out on the pages"),
    ("SA14-9", "SA14-4", "proof", "", "the Picard functor of a product"),
    ("SA14-1", "SA14-17", "our note", "MPL_57_133-179 FW01-FW07", "the carry question tested on 57:144"),
    ("SA14-1", "SA18-13", "our note", "FW01 (47:7-8)", "the cote 47 Fourier check (other topic)"),
]
ITEMLINKS = {
    "SA14-4": [("known", "FGA (Technique de descente V-VI); Kleiman, 'The Picard scheme' (2005)", "literature", "")],
    "SA14-7": [("known", "SGA 6 XIII", "literature", "")],
    "SA14-5": [("known", "SGA 2 XII", "literature", "")],
    "SA14-3": [("known", "SGA 2 X-XII", "literature", "")],
    "SA14-6": [("known", "SGA 2 XI; Boutot, Schéma de Picard local (1978)", "literature", "")],
    "SA14-8": [("known", "Bosch-Lütkebohmert-Raynaud, Néron Models, ch. 9", "literature", "")],
    "SA14-9": [("known", "the theorem of the cube (Mumford, Abelian Varieties)", "literature", "")],
    "SA14-2": [("known", "Mazur-Messing (1974)", "literature", "")],
    "SA14-14": [("known", "Knudsen-Mumford (1976); Deligne, 'Le déterminant de la cohomologie' (1987)", "literature", "")],
    "SA14-10": [("known", "SGA 4 1/2, SGA 5; Laumon (1987) product formula", "literature", "")],
    "SA14-18": [("known", "EGA IV §20.2 (pseudo-morphismes)", "literature", "")],
    "SA14-17": [("known in the literature (same mechanism)", "the splitting obstruction of the abelianized fundamental group extension is the divisibility of the degree-one Albanese/Picard torsor class (Harari-Szamuely 2009, Thm 1.2; register SECTION_GHOSTS:P.10, Known)", "register and literature", ""),
                ("same object in a run", "ANABELIAN_A1_SUCCESSOR:B.68 (generalized Jacobian, Kummer sequence, Abel map); ANABELIAN_149_PUSH:A.1 (prime-to-p Kummer kernel of a semiabelian variety)", "register", "")],
}
ENTRYLINKS = {
    "MPL_57_133-179#3": [("decided on the scan", "57:144: 'à vérifier' qualifies xi_n = delta_n(eta); the mechanism is known (Harari-Szamuely 2009, Thm 1.2; register SECTION_GHOSTS:P.10)", "passage read and literature", "REPORTS/cote57_scan144_a_verifier.md")],
    "MPL_57_133-179#78": [("decided on the scan", "57:144: the self-flagged step is xi_n = delta_n(eta); the mechanism is known (Harari-Szamuely 2009)", "passage read and literature", "REPORTS/cote57_scan144_a_verifier.md")],
}
CORRECTIONS = [
    ("SA14 FLAGS (part 1) on MPL_57_133-179 FW01-FW07, JAC01-JAC08", "my flag suspected the notes of reading the 57:144 'à vérifier' as the cote 47 Fourier check", "they do not: FW01, FW02 and SF07 say it is the Kummer-boundary comparison xi_n = delta_n(eta); the cote 47 gap is a different one (47:7-8)", "passage read 57:144; notes read in full"),
    ("SA14 placement, MPL_57_133-179 R and SF notes (part 1)", "placed by the first scan they cite", "kept; the sections of the text (133-140, 141-146, 147-156, 157-164, 165-171, 172-179) agree with the pages read in part 2 (142-144)", "passage read"),
]
INTRO = """
SA14 is cotes 57-60 (Picard): the existence and properness of the Picard functor, Lefschetz theorems and local Picard
groups (SGA 2), algebraization, Néron-Severi, the theorem of the cube, the Picard of curves with several components and
the Kummer class of the degree-one torsor (cote 57, scans 133-179, new in sweep 2), the universal vector extension, the
determinant and Riemann-Roch (cote 59), and l-adic L-functions on curves (cote 60). Reading decided on the scan in sweep 2:
REPORTS/cote57_scan144_a_verifier.md. A theme only, no dependency: SA23-24 (connections on fibre products, cote 23) and
SA14-2 (connections on the Picard scheme); the sweep-1 pointer that sent SA23-24 to SA19 was a parsing artifact
(REPORTS/sweep1_pointers_into_my_topics.md).
"""
