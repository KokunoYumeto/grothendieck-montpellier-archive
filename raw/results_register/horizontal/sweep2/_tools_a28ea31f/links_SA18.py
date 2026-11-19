# SA18 (Variétés abéliennes): interlinking data, sweep 2 part 2. Claude Opus 5.5 at effort max, a28ea31fa17dd65e1.
ORDER = ["SA18-21", "SA18-1", "SA18-7", "SA18-2", "SA18-6", "SA18-9", "SA18-10", "SA18-3", "SA18-16", "SA18-17", "SA18-8",
         "SA18-14", "SA18-13", "SA18-11", "SA18-15", "SA18-12", "SA18-20", "SA18-18", "SA18-5", "SA18-4", "SA18-19"]
STATUS = {
    "SA18-21": ("his notes; known", "Schemes and group schemes over a field (cote 53): components, geometric irreducibility, finite étale schemes, Hom(G, G_m); questions open on the sheets."),
    "SA18-1": ("his text; known", "Hyperalgebras and the infinitesimal theory of group schemes (SGA 3 II, VII_A)."),
    "SA18-7": ("his text; known", "Relative Frobenius and Verschiebung, Frobenius kernels (SGA 3 VII_A)."),
    "SA18-2": ("his text; known", "Forms of tori and reductive group schemes, isotriviality over a field (SGA 3 VIII-X, XXIV)."),
    "SA18-6": ("his text; known", "Torsors under twisted groups and Lang's theorem (Lang 1956)."),
    "SA18-9": ("his notes", "Étale sheaves and cohomological triviality; axioms a) and b)."),
    "SA18-10": ("his text; known", "Brauer-Severi schemes and descent; the Picard obstruction (Le groupe de Brauer I)."),
    "SA18-3": ("another author's offprint and his notes; known", "Quadratic forms, the Witt ring, Delzant's Stiefel-Whitney classes (1962); the lambda-structure (C45-01)."),
    "SA18-16": ("his text; known", "The cohomology of quadrics (SGA 7 XII)."),
    "SA18-17": ("his text; known", "The Picard functor of an abelian scheme and its automorphisms."),
    "SA18-8": ("his text; known", "Picard p-torsion, Cartier duality, Oda's comparison (Oda 1969)."),
    "SA18-14": ("his claims; known in substance", "Duality of abelian varieties, the universal vector extension (Mazur-Messing 1974), intermediate Jacobians; the seven theorems of cote 44."),
    "SA18-13": ("his construction; known since", "The Fourier transform of abelian schemes (cote 47): Lemma 2 admitted, a compatibility left open, a slip in the Chern-class expansion (47:9, decided in part 2); the inversion theorem is Mukai's (1981)."),
    "SA18-11": ("his claims; partly known", "Integral models and local duality: exterior models, discriminant pairings, Brauer questions (SGA 7 IX)."),
    "SA18-15": ("his construction; known as definitions", "Correspondences and the construction of motives."),
    "SA18-12": ("conjectures, open", "Abstract Lefschetz algebras and the standard conjectures; open in general, known for abelian varieties in characteristic 0 (Lieberman 1968)."),
    "SA18-20": ("his calculations", "Orbit calculations in tensor squares (cote 16, scans 25-29); checked by the second pass (D16-D20)."),
    "SA18-18": ("his notes; known", "Coherent analytic sheaves on compact Stein spaces."),
    "SA18-5": ("planning", "The programme's carry questions (cote 47 Fourier witness, cote 44)."),
    "SA18-4": ("reused typescripts", "Used as paper."),
    "SA18-19": ("documents", "Titles, headings, pagination."),
}
DEPENDS = [
    ("SA18-1", "SA18-21", "proof", "", "distributions of a group scheme over a field"),
    ("SA18-7", "SA18-1", "proof", "", "Frobenius kernels are infinitesimal group schemes"),
    ("SA18-2", "SA18-21", "proof", "", "tori and reductive groups over a field first"),
    ("SA18-6", "SA18-2", "his page", "cote 46 (Lang theorem, Lie(f) = 0 étaleness; research lead scans 6-9)", "torsors under twisted forms"),
    ("SA18-6", "SA18-7", "proof", "", "the Lang map is built from Frobenius"),
    ("SA18-10", "SA18-6", "proof", "", "Brauer-Severi schemes are torsors under PGL_n"),
    ("SA18-16", "SA18-3", "proof", "", "a quadric is the zero locus of a quadratic form"),
    ("SA18-8", "SA18-7", "proof", "", "Cartier duality exchanges Frobenius and Verschiebung"),
    ("SA18-8", "SA18-17", "proof", "", "p-torsion of the Picard scheme"),
    ("SA18-14", "SA18-17", "proof", "", "the dual abelian scheme is Pic^0"),
    ("SA18-13", "SA18-14", "his page", "47:3-4 ('faisceau de Weil', Poincaré bundle on A x B)", "the kernel of the transform"),
    ("SA18-13", "SA18-17", "his page", "47:4 ('th. du carré', Künneth in the proof of Prop. 1)", ""),
    ("SA18-11", "SA18-14", "proof", "", "local duality pairs A with its dual"),
    ("SA18-12", "SA18-15", "proof", "", "Lefschetz operators are correspondences"),
    ("SA18-20", "SA18-12", "his page", "cote 16, scans 25-29", "orbits of the structures of the cote 16 programme"),
    ("SA18-5", "SA18-13", "our note", "MPL_16+47+54+44 F and R notes", "the carry question on the Fourier witness"),
    ("SA18-5", "SA18-14", "our note", "", "the carry question on the seven theorems of cote 44"),
]
ITEMLINKS = {
    "SA18-21": [("known", "SGA 3 VI_A; EGA IV §4", "literature", "")],
    "SA18-1": [("known", "SGA 3 II and VII_A; Demazure-Gabriel", "literature", "")],
    "SA18-7": [("known", "SGA 3 VII_A", "literature", "")],
    "SA18-2": [("known", "SGA 3 VIII-X (isotriviality: X), XXIV", "literature", "")],
    "SA18-6": [("known", "Lang (1956)", "literature", "")],
    "SA18-10": [("known", "Grothendieck, Le groupe de Brauer I", "literature", "")],
    "SA18-3": [("known", "Delzant (1962); Witt rings", "literature", "")],
    "SA18-16": [("known", "SGA 7 XII", "literature", "")],
    "SA18-8": [("known", "Oda (1969)", "literature", "")],
    "SA18-14": [("known", "duality of abelian schemes; universal vector extension (Mazur-Messing 1974)", "literature", "")],
    "SA18-13": [("known since", "Mukai (1981), the Fourier-Mukai transform and its inversion", "literature", "his cote 47 heuristics precede it")],
    "SA18-11": [("known in part", "SGA 7 IX (Grothendieck's pairing)", "literature", "")],
    "SA18-12": [("open", "the standard conjectures; known for abelian varieties in characteristic 0 (Lieberman 1968)", "literature", "")],
}
ENTRYLINKS = {
    "work:K47-01#3": [("decided on the scan", "47:9: the Chern-class coefficients have chi^(k-1) where chi^k is right (his slip); the divisibility claim with k! chi^(k-2) is true but weaker than the corrected k! chi^(k-1)",
                       "passage read at 220 dpi and recomputation", "REPORTS/cote47_scan009_chi_factor.md")],
}
CORRECTIONS = [
    ("cote 47 scan 9, the total Chern class of phi_L", "(1 - D'/chi)^chi expanded with coefficients chi(chi-1)...(chi-k+1)/(k! chi^(k-1))", "the coefficients are chi(chi-1)...(chi-k+1)/(k! chi^k); the page's own linear term -D' shows it", "recomputation; passage read 47:9"),
    ("cote 47 scan 9, the divisibility claim", "(chi-1)...(chi-k+1)/(k! chi^(k-2)) delta'^k integral", "integrality of c_k gives the stronger (chi-1)...(chi-k+1)/(k! chi^(k-1)) delta'^k integral; the page's statement is true but weaker", "recomputation"),
    ("SA18 FLAGS (part 1) on work:K47-01#6", "kind 'suspected misreading'", "decided: a slip of his; the ink reads as transcribed", "passage read 47:9"),
]
INTRO = """
SA18 is cotes 45-56 (Variétés abéliennes), with the shared package MPL_16+47+54+44. Group schemes (cotes 45, 46, 48, 53),
quadratic forms and quadrics (45, 56), the Picard functor of abelian schemes (49-52), the Fourier transform (47), duality
and intermediate Jacobians (44 via 54), integral models (cote 16 package), Stein spaces (55). Reading decided on the scan
in sweep 2: REPORTS/cote47_scan009_chi_factor.md. The second-pass verdicts on MPL_16+47+54+44 are in this folder's
CHECK_EVENTS.
"""
