# SA18 (Variétés abéliennes): items, read decisions, flags and checks.
# Claude Opus 5.5 at effort max (a28ea31fa17dd65e1), horizontal sweep 1, 18 Nov 2026.
# Packages shared with other topics: MPL_16+47+54+44 (also SA19, SA07), MPL_11_043-058+56 (also SA05); their items here
# are reused there (cross_topic).
CLUSTERS = [
 ("SA18-5", "the programme's carry questions: a second Fourier witness (cote 47) and earlier forms of the seven Jacobian theorems (cote 44); chronology and priority",
  r"Fourier witness|second Fourier|Jacobian theorems|seven Jacobian|earlier-form question|Laumon parallel|programme connection|Mumford correspondence|August 1[26]|later authorial reassessment|divisor-case precursor|witness searching|Folder chronology|root-data draft|intermediate Jacobian$|Oda addresses"),
 ("SA18-12", "abstract Lefschetz algebras and the standard conjectures (Lefschetz type, Hodge type, numerical versus homological equivalence, Künneth projectors)",
  r"standard-conjecture|Lefschetz|standard conjectures|Künneth|Numerical motives|Cayley–Hamilton|Positivity kills|Polarization independence|Hodge reference|low-dimensional list|matrix-unit|exterior-algebra model|matrix-algebra model|five-dimensional example|Intrinsic projectors|Hyperplane reduction|weak variants|nilpotent kernel|injective map needs an algebraic splitting|Endpoint calculations|Compare definitions before letters"),
 ("SA18-13", "the Fourier transform of abelian varieties (cote 47): kernels and inversion, determinant lines, Chern classes, Riemann-Roch and integrality",
  r"^F\d+ — Cote 47|Fourier transform|determinant factor|anti-diagonal kernel|Chern|Todd|Kleiman attribution|integrality claim|formal-power heuristic"),
 ("SA18-14", "duality of abelian varieties, the universal vector extension, intermediate Jacobians and the seven theorems of cote 44",
  r"^D\d+\. Cote (54|44)|universal extension|intermediate Jacobians|Tate-module|Matsusaka|primitive-decomposition|generic freeness"),
 ("SA18-20", "orbit calculations in tensor squares (cote 16, scans 25-29)",
  r"^D\d+\. Cote 16"),
 ("SA18-8", "Picard p-torsion, Cartier duality, restricted Lie algebras of height one, and Oda's comparison",
  r"Picard p-torsion|p-torsion|Cartier|restricted Lie|height-one|Oda gives|Oda supplies|Elliptic examples provide|Global units explain|differential conclusion|transpose|symmetric-power|commutativity test"),
 ("SA18-7", "relative Frobenius and Verschiebung; infinitesimal group schemes and Frobenius kernels; affineness",
  r"Frobenius|Verschiebung|“Ver”|Ver.? are|infinitesimal|affineness|Perfection does not|de préschémas"),
]
SECTION_MAP = {
 ("MPL_45_033-080", "I."): "SA18-5",
 ("MPL_45_033-080", "II."): "SA18-1",
 ("MPL_45_033-080", "III."): "SA18-2",
 ("MPL_45_033-080", "IV."): "SA18-3",
 ("MPL_45_033-080", "V."): "SA18-4",
 ("MPL_45_033-080", "VII."): "SA18-19",
 ("MPL_46_002-048", "Scope"): "SA18-19",
 ("MPL_46_002-048", "I."): "SA18-5",
 ("MPL_46_002-048", "II."): "SA18-6",
 ("MPL_46_002-048", "III."): "SA18-7",
 ("MPL_46_002-048", "IV."): "SA18-8",
 ("MPL_46_002-048", "V."): "SA18-9",
 ("MPL_46_002-048", "VI."): "SA18-10",
 ("MPL_46_002-048", "VII."): "SA18-4",
 ("MPL_46_002-048", "IX."): "SA18-19",
 ("MPL_46_002-048", "XI."): "SA18-19",
 ("MPL_16+47+54+44", "Integral models"): "SA18-11",
 ("MPL_16+47+54+44", "Abstract Lefschetz"): "SA18-12",
 ("MPL_16+47+54+44", "Fourier transforms"): "SA18-13",
 ("MPL_16+47+54+44", "Abelian duality"): "SA18-14",
 ("MPL_11_043-058+56", "Answers"): "SA18-15",
 ("MPL_11_043-058+56", "A."): "SA18-15",
 ("MPL_11_043-058+56", "B."): "SA18-16",
 ("MPL_11_043-058+56", "C."): "SA18-2",
 ("MPL_11_043-058+56", "D."): "SA18-3",
 ("MPL_11_043-058+56", "E."): "SA18-15",
 ("MPL_11_043-058+56", "Primary"): "SA18-19",
}
EXTRA_OBJECTS = {
 "SA18-1": "infinitesimal theory of group schemes: hyperalgebras (distributions), deformations, Lie algebra cohomology H0, H1, H2 and rigidity",
 "SA18-2": "forms of tori and reductive group schemes: nonabelian H1 and its fibres, outer automorphisms, pinnings, maximal tori, the reductive centre and the Weyl group",
 "SA18-3": "quadratic and bilinear forms over rings and fields: the Witt ring, discriminant, Clifford and Stiefel-Whitney invariants, characteristic two; Delzant's offprint",
 "SA18-4": "reused typescripts and sheets: ordered fields, local subrings, soft sheaves, isotropic subspaces, hermitian forms, exterior contractions, uniform structures, Coxeter pages, injective modules",
 "SA18-6": "torsors under twisted groups, Lang's theorem and unit Frobenius modules",
 "SA18-9": "étale sheaves and cohomological triviality; the axioms a) and b)",
 "SA18-10": "Brauer-Severi schemes, linear systems and descent; the Picard obstruction",
 "SA18-11": "integral models and local duality: exterior models, discriminant pairings, resolution, Brauer quotients, injective modules, the different, trace duality, EGA/SGA corrections",
 "SA18-15": "correspondences and the construction of motives: correspondence rings, tautological classes, excess intersection, Euler characteristics, the sorted-weight cone",
 "SA18-16": "the cohomology of quadrics (even, odd, affine, cones): Gysin maps, specialization, local and compact supports, torsion",
 "SA18-17": "the Picard functor of an abelian scheme and its automorphisms: cohomological flatness, translations, equivalence of divisors, Pic and Alb, Hom and rational sections",
 "SA18-18": "coherent analytic sheaves on compact Stein spaces; dimension in fibres (cote 55)",
 "SA18-19": "the dossier as a document: titles, headings, pagination, references, citation conventions",
}
FORCE = {}
for f, k in (("K45-01", "SA18-1"), ("K45-02", "SA18-1"), ("K46-01_2", "SA18-6"), ("K46-02", "SA18-10"), ("K46-03", "SA18-6"),
             ("K49-01", "SA18-17"), ("K50-01", "SA18-17"), ("K51-01", "SA18-17"), ("K51-02", "SA18-17"), ("K52-01", "SA18-17"),
             ("K54-01", "SA18-14"), ("K55-01", "SA18-18"), ("K56-01", "SA18-16"), ("K56-02", "SA18-16"), ("K56-03", "SA18-2")):
    for n in range(1, 8):
        FORCE[f"work:{f}#{n}"] = k
FORCE.update({"MPL_11_043-058+56#1": "SA18-12", "MPL_46_002-048#12": "SA18-5", "MPL_11_043-058+56#27": "SA18-19",
              "MPL_11_043-058+56#98": "SA18-19", "MPL_11_043-058+56#28": "SA18-15"})
LMLENS = r"\bLM\d?\b|Kummer run|WG ?H\d|reviewed descent item|section-class item|register boundaries"
D = "2026-11-18"
READ = {
 "MPL_46_002-048#34": ("passage-read", "agrees", "logarithmic differential on rational functions modulo units, in characteristic p (cote 46, scan 021)",
                       "the page's own preceding sentence asks for f = g^p h with h a unit; the displayed 'i.e.' injectivity of R*/O* -> Omega(K)/Omega(O) omits the p-th powers, as the note says"),
 "MPL_46_002-048#63": ("passage-read", "agrees", "a monomorphism of the dual projective space into P(Q) and its image P(E) (cote 46, scan 047)",
                       "the transcription has '\\inserted{mono}morphisme'; Hua prints 'épimorphisme'; the note records the difference without deciding it"),
}
FLAGS = [
 ("the same thing noted with different readings or statements", "MPL_46_002-048#63 (N61; cote 46, scan 047)",
  "our transcription reads an inserted 'mono' ('un monomorphisme P^ -> P(Q), je dis que c'est un isom sur un P(E)'), Michel Hua's project prints 'épimorphisme'. The mathematics favours 'mono' for the morphism of schemes: a closed immersion with image P(E) corresponds to the module epimorphism Q -> E, which may be what Hua's arrow records. To decide on the scan.",
  "MPL_46_002-048_transcription.tex:1122; MPL_46_002-048_notes.md N61-N62"),
 ("a link across folders", "MPL_16+47+54+44 (85 entries) and MPL_11_043-058+56 (107 entries)",
  "the same Pro packages are indexed under several topics: MPL_16+47+54+44 under SA18, SA19 and SA07; MPL_11_043-058+56 under SA18 and SA05. Their entries are placed with the same items in each topic (cross_topic).",
  "NOTES_INDEX.tsv of SA18, SA19, SA07, SA05"),
 ("a link across folders", "MPL_45_033-080 (I. carry questions) and MPL_46_002-048 (I.) and MPL_16+47+54+44 (F1-F20, D08-D14)",
  "the 'second Fourier witness' (cote 47) and the 'seven Jacobian theorems' (cote 44) are asked in three packages; one item SA18-5 with the cote 47 and cote 44 objects in SA18-13 and SA18-14",
  "headings"),
]
CHECKS = [
 ("MPL_46_002-048#34", D, "note checked against the page (scan 021); claim checked by computation: dlog(t^p) = p dt/t = 0 in characteristic p while t^p is not a unit", "agrees: the displayed injection is false as written; the page's own condition f = g^p h names the missing quotient by p-th powers", "results_register/horizontal/inputs/SA18/pro/MPL_46_002-048_transcription.tex:620-651"),
 ("MPL_46_002-048#63", D, "reading weighed against the mathematics (no scan): 'mono' versus Hua's 'épimorphisme' in 'un ...morphisme P^ -> P(Q), je dis que c'est un isom sur un P(E)'", "the mathematics favours 'mono' (an immersion onto P(E)); not decided on the ink", "results_register/horizontal/inputs/SA18/pro/MPL_46_002-048_transcription.tex:1122"),
 ("MPL_46_002-048#64", D, "claim checked by reasoning: a monomorphism P^1 -> P^2 need not have linear image (the conic)", "agrees", "results_register/horizontal/inputs/SA18/pro/MPL_46_002-048_notes.md (N62)"),
]
STATEMENTS = {
 "SA18-13": ("(notes) a Fourier transform on abelian varieties with kernel, inversion and Chern-class integrality, on cote 47", "stated with partial proofs, verification left unfinished (scan 8)", "SA19 (Jacobians), SA07 (motives), SA14 (Picard)"),
 "SA18-12": ("(notes) an abstract algebra of Lefschetz operators behind the standard conjectures", "sketched", "SA07, SA05, SA06 (motives)"),
 "SA18-14": ("(notes) duality of abelian schemes through the universal extension; seven theorems on intermediate Jacobians (cote 44)", "stated, partly proved", "SA19 (Jacobians), SA14 (Picard)"),
 "SA18-8": ("(notes) Picard p-torsion of a variety in characteristic p through Cartier duality and restricted Lie algebras", "worked, with a noninjective display (N32)", "SA14 (Picard), SA15 (crystals)"),
}
