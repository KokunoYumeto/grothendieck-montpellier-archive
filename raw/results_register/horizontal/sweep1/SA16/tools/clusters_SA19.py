# SA19 (Jacobiennes): items, read decisions, flags and checks.
# Claude Opus 5.5 at effort max (a28ea31fa17dd65e1), horizontal sweep 1, 18 Nov 2026.
# MPL_16+47+54+44 is shared with SA18 and SA07: its items SA19-11..14, SA19-20 are the same objects as SA18-11..14, SA18-20.
CLUSTERS = [
 ("SA19-13", "the Fourier transform of abelian varieties (cote 47): kernels and inversion, determinant lines, Chern classes, Riemann-Roch and integrality (= SA18-13)",
  r"^F\d+ — Cote 47"),
 ("SA19-20", "orbit calculations in tensor squares (cote 16, scans 25-29) (= SA18-20)", r"^D\d+\. Cote 16"),
 ("SA19-14", "duality of abelian varieties, the universal vector extension, intermediate Jacobians and the seven theorems of cote 44 (= SA18-14)",
  r"^D\d+\. Cote (54|44)"),
]
SECTION_MAP = {
 ("MPL_16+47+54+44", "Integral models"): "SA19-11",
 ("MPL_16+47+54+44", "Abstract Lefschetz"): "SA19-12",
 ("MPL_16+47+54+44", "Fourier transforms"): "SA19-13",
 ("MPL_16+47+54+44", "Abelian duality"): "SA19-14",
 ("MPL_43_094-142", "Arithmetic, Jacobians"): "SA19-1",
 ("MPL_43_094-142", "Functor foundations"): "SA19-2",
 ("MPL_43_094-142", "Cote 47"): "SA19-3",
 ("MPL_43_094-142", "Reused typescripts"): "SA19-4",
 ("MPL_43_094-142", "Standing registers"): "SA19-8",
}
EXTRA_OBJECTS = {
 "SA19-1": "generalized Jacobians and geometric class field theory: modulus, ray class groups, norms, reciprocity, ideles, S-units; the planning question on the 1983 injectivity argument",
 "SA19-2": "duality for commutative group schemes over local fields and over curves: the site, Ext groups, Cartier-Serre-Pontryagin squares, supports, completion limits, henselization",
 "SA19-3": "cote 47's Fourier test and the seven theorems of cote 44, read against Oda: Dieudonne modules, Frobenius and Verschiebung, Cartier duality, alpha_p subgroups (with SA18-5, SA18-13, SA18-14)",
 "SA19-4": "reused typescripts: homotopy of Thom complexes (Atiyah), Stiefel manifolds, a multiplicity lemma and flatness, proper pushforward, Euler characteristics, depth, soft and fine sheaves",
 "SA19-5": "local cohomology and local relative Jacobians: rings attached to chains of primes, simplicial and cosimplicial coefficients, purity, double duality",
 "SA19-6": "formal groups, Witt rings and power-series operations; ind-completion and socle filtrations",
 "SA19-7": "classification sketches and gluing constructions for categories of curves (cote 43, scans 178-184)",
 "SA19-8": "the dossier as a document: reading conventions, author flags, withdrawals, titles, sheet counts",
 "SA19-11": "integral models and local duality (= SA18-11)",
 "SA19-12": "abstract Lefschetz algebras and the standard conjectures (= SA18-12)",
}
FORCE = {}
for f, k in (("K43-01", "SA19-1"), ("K43-02_2", "SA19-2"), ("K43-03", "SA19-6"), ("K43-04_2", "SA19-5"), ("K43-05", "SA19-5"),
             ("K43-06", "SA19-5"), ("K43-07_2", "SA19-2"), ("K43-08", "SA19-2"), ("K43-09", "SA19-7"), ("K43-10", "SA19-6")):
    for n in range(1, 8):
        FORCE[f"work:{f}#{n}"] = k
LMLENS = r"\bLM\d?\b|1983 bridge|WG ?H\d"
D = "2026-11-18"
READ = {
 "MPL_43_094-142#76": ("passage-read", "agrees", "a fibre-length criterion for flatness over a discrete valuation ring (cote 43, scan 110)",
                       "the counterexample R+k over k[[t]] is correct; the page's own later 'on ne peut avoir égalité' points to equality as the intended condition"),
 "MPL_43_094-142#75": ("passage-read", "agrees", "the same multiplicity lemma, questioned by its author ('J'ignore si les assertions sont vraies')", ""),
}
FLAGS = [
 ("suspected misreading", "MPL_43_094-142#76, #75 (cote 43, scan 110; transcription line 753)",
  "'Si l'inégalité est vérifiée, alors F est plat' is false as written (R06's counterexample R+k over k[[t]]: lengths 2 and 1, not flat), while equality of the fibre lengths does give flatness and the page goes on 'on ne peut avoir égalité' (line 768). The ink may read 'l'égalité', or the slip is his; the displayed sign is itself uncertain ('\\geq|>'). Decide on the scan.",
  "MPL_43_094-142_transcription.tex:741-768; MPL_43_094-142_notes.md R05-R06"),
 ("a link across folders", "MPL_43_094-142 (F01-F22) and SA18 (MPL_45, MPL_46, MPL_16+47+54+44)",
  "the cote 47 Fourier test and the seven cote 44 theorems are asked again here, with the Oda comparison; same objects as SA18-5, SA18-13, SA18-14 and SA18-8", "headings"),
 ("a link across folders", "work:K43-01 (cote 43, scans 4-10) and MPL_43_094-142 (A01-A27)",
  "geometric class field theory (modulus, norms, reciprocity) on the early sheets of cote 43, and the generalized-Jacobian questions of the Pro package, are one object, SA19-1", "unit titles; headings"),
]
CHECKS = [
 ("MPL_43_094-142#76", D, "note checked against the page (scan 110); counterexample checked by computation: F=R+R/t over R=k[[t]] has special-fibre length 2, generic length 1, and Tor_1(F,R/t)=R/t is not zero", "agrees: the inequality-to-flatness sentence is false as written; equality is the condition", "results_register/horizontal/inputs/SA19/pro/MPL_43_094-142_transcription.tex:741-768"),
]
STATEMENTS = {
 "SA19-2": ("(notes) a duality theorem for commutative group schemes over a local field or a curve, with supports and completions", "stated with marked open checks (D16-D28)", "SA14 (Picard), SA18 (abelian varieties)"),
 "SA19-1": ("(notes) generalized Jacobians as the geometric side of class field theory for curves over finite fields", "worked in parts", "SA14 (Picard), SA16 (elliptic curves)"),
}
