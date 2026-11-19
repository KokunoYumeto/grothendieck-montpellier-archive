# SA07 (Théorie des motifs, part 3: cotes 15 (195-228), 18, 10, 16, 19, and the shared 16+47+54+44): items, flags, checks.
# Claude Opus 5.5 at effort max (a28ea31fa17dd65e1), horizontal sweep 1, 18 Nov 2026.
# MPL_16+47+54+44 is shared with SA18 and SA19: SA07-11..14, SA07-20 are SA18-11..14, SA18-20.
CLUSTERS = [
 ("SA07-13", "the Fourier transform of abelian varieties (cote 47) (= SA18-13)", r"^F\d+ — Cote 47"),
 ("SA07-20", "orbit calculations in tensor squares (cote 16) (= SA18-20)", r"^D\d+\. Cote 16"),
 ("SA07-14", "duality of abelian varieties, the universal extension, intermediate Jacobians, the seven theorems of cote 44 (= SA18-14)", r"^D\d+\. Cote (54|44)"),
]
SECTION_MAP = {
 ("MPL_16+47+54+44", "Integral models"): "SA07-11",
 ("MPL_16+47+54+44", "Abstract Lefschetz"): "SA07-12",
 ("MPL_16+47+54+44", "Fourier transforms"): "SA07-13",
 ("MPL_16+47+54+44", "Abelian duality"): "SA07-14",
 ("MPL_15_195-228+18_002-017", "Answers"): "SA07-19",
 ("MPL_15_195-228+18_002-017", "Cote 15"): "SA07-1",
 ("MPL_15_195-228+18_002-017", "Cote 18"): "SA07-2",
 ("MPL_15_195-228+18_002-017", "Structural"): "SA07-3",
 ("MPL_15_195-228+18_002-017", "The four linear"): "SA07-4",
 ("MPL_15_195-228+18_002-017", "Reused"): "SA07-5",
 ("MPL_15_195-228+18_002-017", "Additional tests"): "SA07-1",
 ("MPL_15_195-228+18_002-017", "Standing question"): "SA07-9",
 ("MPL_18_018-062", "1."): "SA07-6",
 ("MPL_18_018-062", "2."): "SA07-7",
 ("MPL_18_018-062", "3."): "SA07-2",
 ("MPL_18_018-062", "4."): "SA07-3",
 ("MPL_18_018-062", "5."): "SA07-5",
 ("MPL_18_018-062", "6."): "SA07-10",
 ("MPL_18_018-062", "7."): "SA07-9",
}
EXTRA_OBJECTS = {
 "SA07-1": "reconstruction of varieties and places from their motivic realizations: fibre functors at places, comparison of characteristic-p and characteristic-0 fibres, path torsors and the place-to-torsor map, motivic rigidity, the j-family test (cote 15, scans 195-228)",
 "SA07-2": "periods: the period torsor, his 'conjecture de transcendance N° 1' (genericity of the period point), the strong and elliptic period conjectures, Hodge splittings, archimedean lattices and cocycles (cotes 15, 18)",
 "SA07-3": "the motivic category and its groups: correspondence rings, Lefschetz and Tate gradings, the A-D dictionary, the arithmetic exact sequence, Nori/Ayoub, numerical semisimplicity (cotes 15, 18) (with SA05-8, SA06-2)",
 "SA07-4": "linear versus nonlinear comparisons (= SA05-14, SA06-1)",
 "SA07-5": "reused typescripts: Lie theory and representations, Cartan subalgebras, root systems and Coxeter groups, group germs, triality, distributions and formal charts, Dedekind domains and Krull-Akizuki",
 "SA07-6": "cycle classes, orientations and comparison maps: the cycle-class scalar, degree shifts, Tate-line maps, real descent of the integral lattice (cote 18)",
 "SA07-7": "real structures and Hodge theory of motives: commuting conjugations, real Frobenius, real points, Weil forms and polarization, the Oda comparison (cote 18)",
 "SA07-9": "the dossiers as documents: covers, pagination, source numbers, letterhead",
 "SA07-10": "steps he marks as unverified, withdrawn or to check on cote 18 (register SF01-SF36)",
 "SA07-11": "integral models and local duality (= SA18-11)",
 "SA07-12": "abstract Lefschetz algebras and the standard conjectures (= SA18-12)",
 "SA07-15": "polarizations and Weil forms: adjoints, the Weil condition, twisting a polarization, the positive cone, admissible filtrations and splittings (cote 10)",
 "SA07-16": "operations on representation rings: restriction to a maximal torus, recovering an algebra of operations, functions on the character group, the additive group in characteristic p (cote 10)",
 "SA07-17": "Lefschetz elements and their converse, local Picard groups, cohomology and the Brauer group (cote 16)",
 "SA07-18": "homological formalism: relative exactness, derived functors, extraordinary inverse images, injective envelopes, adjoints and gluing data, sites and fibre toposes (cote 19)",
 "SA07-19": "the notes' answers to the planning questions (A-D, linear and nonlinear, S15)",
}
FORCE = {}
for f, k in (("K10-01", "SA07-15"), ("K10-02", "SA07-15"), ("K10-03", "SA07-15"), ("K10-04", "SA07-3"), ("K10-05", "SA07-16"),
             ("K10-06", "SA07-16"), ("K10-07", "SA07-16"), ("K16-02", "SA07-17"), ("K19-01", "SA07-18"), ("K19-02", "SA07-18"),
             ("K19-03", "SA07-18"), ("K19-04", "SA07-18"), ("K19-05", "SA07-18"), ("K19-06", "SA07-18")):
    for n in range(1, 8):
        FORCE[f"work:{f}#{n}"] = k
LMLENS = r"\bLM\d?\b|S15|register|planning"
D = "2026-11-18"
READ = {
 "MPL_18_018-062#43": ("passage-read", "agrees", "his 'conjecture de transcendance N° 1': the period point on the period torsor P_{v,k} is generic (cote 18, scan 059)",
                       "the page reads 'Pour la conjecture [inserted: de transcendance] N° 1, ce point ainsi donné sur P_{v,k} est générique ...', margin 'π transcendant sur k_0'"),
}
FLAGS = [
 ("a link across folders", "MPL_18_018-062#43 (P17), #51 (P25), MPL_15_195-228+18_002-017#59 (P15), #66 (P22)",
  "Grothendieck's period conjecture is written on cote 18, scan 059 ('conjecture de transcendance N° 1': genericity of the period point) and in a strong and an elliptic form on cote 15/18; one object, SA07-2, for the history of the period conjecture", "transcription MPL_18_018-062 scan 59 (read); headings"),
 ("the LM/Dérivateurs lens", "MPL_15_195-228+18_002-017#93 (B05)",
  "'The open LM6 normalizer item needs an additional character step': the note reads the linear/nonlinear comparison through the research run LM6 (N2)", "heading"),
 ("a link across folders", "SA07-1 (cote 15, scans 195-228) with SA05-14, SA06-1 and the anabelian research line",
  "the reconstruction of places and varieties from motivic fibre functors (the place-to-torsor map, motivically pointed schemes) is the motivic counterpart of points as sections; recorded as a link, not a lens", "headings A13-A40"),
 ("a link across folders", "MPL_16+47+54+44 (shared with SA18, SA19)",
  "SA07-11..14, SA07-20 are SA18-11..14, SA18-20", "NOTES_INDEX of SA07, SA18, SA19"),
 ("a link across folders", "SA07-7 (cote 18), SA06-10 (cote 15)",
  "real structures, real Frobenius, polarizations and real fibre functors: one object across cotes 15 and 18", "section titles"),
]
CHECKS = [
 ("MPL_18_018-062#43", D, "note checked against the page (scan 059)", "agrees: the page states the genericity of the period point as 'la conjecture de transcendance N° 1'", "results_register/horizontal/inputs/SA07/pro/MPL_18_018-062_transcription.tex:970-984"),
]
STATEMENTS = {
 "SA07-2": ("(page, cote 18 scan 059) the point of the period torsor given by the comparison isomorphism is generic ('conjecture de transcendance N° 1'); in today's terms: the transcendence degree of the periods equals the dimension of the motivic Galois group (mine)", "conjectured on the page", "SA05-8, SA06-2"),
 "SA07-1": ("(notes) varieties and places recovered from fibre functors and path torsors of motives", "conjectures and questions on the pages", "SA05-14; the anabelian line"),
}
