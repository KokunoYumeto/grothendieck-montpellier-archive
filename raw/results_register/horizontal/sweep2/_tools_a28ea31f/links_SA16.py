# SA16 (Courbes elliptiques): interlinking data, sweep 2 part 2. Claude Opus 5.5 at effort max, a28ea31fa17dd65e1.
ORDER = ["SA16-6", "SA16-7", "SA16-15", "SA16-1", "SA16-2", "SA16-19", "SA16-8", "SA16-3", "SA16-4", "SA16-5", "SA16-9",
         "SA16-10", "SA16-11", "SA16-13", "SA16-14", "SA16-12", "SA16-21", "SA16-22", "SA16-20", "SA16-16", "SA16-18", "SA16-17"]
STATUS = {
    "SA16-6": ("reused typescript", "Bourbaki-style pages on completion and filtered modules, used as paper; no claim of his."),
    "SA16-7": ("reused typescript", "Pages on valuations (n. 272) used as paper."),
    "SA16-15": ("his claims, partly checked", "Normality of quadratic extensions under a DVR hypothesis (v(2) = 1, signed radicands)."),
    "SA16-1": ("his text; known", "The Riemann-Roch construction of Weierstrass coordinates over a base; standard since Deligne's Formulaire and Katz-Mazur ch. 2. Some propositions cancelled and restated on the pages."),
    "SA16-2": ("his calculations and another author's text; known", "His invariant -27c^2/(b^3 - 27c^2) = 1 - J/1728 (cote 62); the Tate-Deligne Formulaire (cote 63, two versions). One slip of his on 62:19, decided in sweep 1."),
    "SA16-19": ("known", "Automorphisms at j = 0 and 1728 in every characteristic (order 24 for p = 2, 12 for p = 3)."),
    "SA16-8": ("his text; known", "Invariant differentials and the Hodge line."),
    "SA16-3": ("his claims; known in substance", "Representability of moduli of structured elliptic curves; known from Deligne-Rapoport (1973) and Katz-Mazur (1985). Several steps unproved on his pages."),
    "SA16-4": ("his text; classical", "The lambda-line and the S3 action; classical."),
    "SA16-5": ("his construction, partly open on the pages", "Trisections, S3-torsors and Brauer-Severi curves; he marks steps 'à expliciter', 'lui donner un sens'."),
    "SA16-9": ("his construction", "Level 2 and level 4 structures, the octahedral S4 configuration."),
    "SA16-10": ("his construction", "The Legendre pinning; the same normal form is used by the section-conjecture runs."),
    "SA16-11": ("his construction", "Four-pointed lines, Klein cover, doubling map."),
    "SA16-13": ("planning question and his remarks", "The cusp and congruence levels (B5)."),
    "SA16-14": ("his claims; known", "The Gauss-Manin connection on the moduli of elliptic curves; known (Katz-Oda 1968)."),
    "SA16-12": ("classical", "The transcendental theory of elliptic functions."),
    "SA16-21": ("another author's text", "An English typescript on Mordell-Weil and minimal models (cote 63, scans 3-14), title not recorded."),
    "SA16-22": ("another author's text; settled since", "A French typescript with the CM table; its 'peut-être une autre valeur' after 163 is settled (no tenth discriminant: Heegner, Baker, Stark); Frobenius integrality proved by Deligne (1974)."),
    "SA16-20": ("another author's text", "A. O. L. Atkin's typescripts on congruences for modular forms (1968) and congruence Hecke operators."),
    "SA16-16": ("credited comparison", "Michel Hua's readings for these cotes."),
    "SA16-18": ("planning", "Questions about other cotes."),
    "SA16-17": ("documents", "Title sheets, dates, page counts, reused paper."),
}
DEPENDS = [
    ("SA16-2", "SA16-1", "his page", "62:4-11 (Propositions 1-3, the cubic embedding on 62:9, the discriminant on 62:11)", "the Weierstrass cubic is read off the pole filtration"),
    ("SA16-8", "SA16-1", "proof", "62:14 (normalization by an invariant derivation)", "the invariant differential in Weierstrass coordinates"),
    ("SA16-19", "SA16-2", "proof", "63:30 (Formulaire 6.9 (IV), (V))", "j = 0, 1728 are read off c4, c6"),
    ("SA16-3", "SA16-2", "his page", "62:12-13", "structured curves are represented by coefficient points up to G(S)-conjugacy"),
    ("SA16-4", "SA16-2", "proof", "62:23-25", "j as a function of lambda"),
    ("SA16-5", "SA16-4", "his page", "62:28-50", "S3 on P1 minus three points, H^1(S, S3), Brauer-Severi descent of the invariant"),
    ("SA16-9", "SA16-4", "proof", "cote 62-64 level-structure pages", "level 2 is the lambda datum; level 4 adds the octahedral S4"),
    ("SA16-10", "SA16-9", "proof", "", "the pinning uses level-2 data"),
    ("SA16-10", "SA16-4", "proof", "", "the Legendre normal form lives on the lambda-line"),
    ("SA16-11", "SA16-4", "proof", "", "cross-ratio of four-pointed lines"),
    ("SA16-11", "SA16-9", "proof", "", "the Klein cover and doubling use level structures"),
    ("SA16-13", "SA16-3", "proof", "", "the cusp of the moduli curve"),
    ("SA16-13", "SA16-12", "proof", "", "the analytic punctured disc at the cusp"),
    ("SA16-14", "SA16-3", "proof", "", "Gauss-Manin on the universal curve over the moduli"),
    ("SA16-14", "SA16-8", "proof", "", "the Hodge line inside H^1_dR"),
    ("SA16-12", "SA16-2", "proof", "", "the Weierstrass p-function satisfies the cubic"),
    ("SA16-21", "SA16-2", "proof", "63:3-14", "minimal models are built on Weierstrass equations and the discriminant"),
    ("SA16-22", "SA16-2", "proof", "63:78-81", "the j-values of the CM curves"),
    ("SA16-22", "SA16-19", "proof", "", "j = 0 and 1728 are the CM cases d = 3, 4"),
    ("SA16-20", "SA16-13", "proof", "63:41-60", "congruences for coefficients at levels"),
    ("SA16-2", "SA16-3", "his page", "63:32 margin 'Sur le site modulaire ...'", "his NB on the Formulaire's Prop. 7.1 reads it on the moduli stack"),
]
ITEMLINKS = {
    "SA16-1": [("known", "Deligne's Formulaire (Antwerp IV, LNM 476, 1975), §1; Katz-Mazur (1985), ch. 2", "literature", "")],
    "SA16-2": [("known", "Deligne, 'Courbes elliptiques: formulaire d'après J. Tate' (Antwerp IV, LNM 476, 1975)", "literature", "his normalization 1 - j/1728 differs from the classical j by an affine change")],
    "SA16-3": [("known", "Deligne-Rapoport (1973); Katz-Mazur (1985)", "literature", "moduli of elliptic curves with level structure")],
    "SA16-4": [("same object in a run", "SECTIONS_OVER_Q (Legendre family), FERMAT_SUCCESSOR:A.7 (cyclic Legendre covers)", "register", "the runs use the object; they neither prove nor refute his claims")],
    "SA16-10": [("same object in a run", "SECTIONS_OVER_Q:A.74 (the formal Legendre Tate parameter q = t^2 F(t)/256)", "register", "the Legendre Tate constant 1/256 was checked in sweep 1")],
    "SA16-13": [("same object in a run", "SECTIONS_OVER_Q:A.67, A.74 (point and cusp sections compared through the Legendre Tate parameter)", "register", "")],
    "SA16-12": [("known", "the classical theory of elliptic functions", "literature", "")],
    "SA16-14": [("known", "Katz-Oda (1968): the Gauss-Manin connection", "literature", "")],
    "SA16-19": [("known", "Aut(E) at j = 0, 1728 (e.g. Silverman, The Arithmetic of Elliptic Curves, Appendix A)", "literature", "")],
    "SA16-22": [("settled in the literature", "class number one: no tenth discriminant (Heegner 1952, Baker 1966, Stark 1967); Weil conjectures: Deligne 1974", "literature", "")],
    "SA16-20": [("another author's text", "Atkin's typescripts", "document", "")],
    "SA16-21": [("another author's text", "English typescript, cote 63", "document", "")],
}
ENTRYLINKS = {
    "codex:H63-04#1": [("decided on the scan", "the margins of 63:30-33 are probably his; 'faux si S pas connexe' is right (over a non-connected S, the automorphism +1 on one component and -1 on another); 'structure ?' (order 24) is SL2(F3)",
                        "passage read and proof", "REPORTS/hands_formulaire_and_tate.md")],
    "codex:H63-08#1": [("settled in the literature", "no tenth discriminant after 163 (Heegner, Baker, Stark); Frobenius eigenvalues on H^i are algebraic integers of absolute value q^(i/2) (Deligne 1974)",
                        "literature", "the typescript predates both")],
}
CORRECTIONS = [
    ("SA16 FLAGS (part 1) on codex:H63-04#1", "my part-1 flag listed 'Reste à prouver' (63:32) among the handwritten margins", "it is typed: the Formulaire's own proof of Prop. 7.1", "passage read 63:32"),
    ("Formulaire, Prop. 6.9 (I), cote 63 scan 30", "'les seuls automorphismes de E sont l'identité et la symétrie' (c4, c6 invertible)", "true for S connected, or for the sheaf Aut_S(E) = Z/2; false as stated for non-connected S, as his margin says", "proof; passage read 63:30"),
    ("MPL_62_002-050#34 (B03), cote 62 scan 19", "the note says the sheet does not settle which formula for j is meant", "the sheet opens with -27c^2/(b^3 - 27c^2) = j, the definition giving the boxed formula; 'b^3/c^2 = j' is a slip (sweep-1 passage read)", "passage read (sweep 1)"),
    ("SA16-22, codex:H63-08#1", "the typescript leaves 'peut-être une autre valeur' after 163", "settled: there is none (Heegner 1952, Baker 1966, Stark 1967)", "literature"),
]
INTRO = """
SA16 is cotes 62-64 (Courbes elliptiques). Cote 62 holds his manuscript: Weierstrass coordinates over a base, the
discriminant and his normalization of j, the moduli problem, the lambda-line and S3, trisections and Brauer-Severi
descent, level 2 and level 4, with reused Bourbaki-style typescripts as paper. Cote 63 holds other authors' typescripts:
the Tate-Deligne Formulaire in two versions (with his pencil margins), Atkin's congruence papers, an English typescript
on Mordell-Weil and minimal models, and a French CM table. Cote 64 holds the transcendental theory and the cusp.
Readings decided on the scans in sweep 2: REPORTS/hands_formulaire_and_tate.md.
"""
