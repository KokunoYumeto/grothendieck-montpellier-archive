# SA15 (Cristaux): items, read decisions, flags and checks.
# Claude Opus 5.5 at effort max (a28ea31fa17dd65e1), horizontal sweep 1, 18 Nov 2026.
# The Pro notes are filed per scan ("Scan 061"); each entry was placed from the first lines of its body (entry-read).
DEFAULT_BASIS = "entry-read"
CLUSTERS = []
BODY_RULES = [
 (r"\*\*C7\.", "SA15-1"),
 (r"\*\*ER\.01", "SA15-12"),
 (r"\*\*ER\.02", "SA15-13"),
 (r"\*\*ER\.08", "SA15-13"),
 (r"\*\*E\.35", "SA15-8"),
 (r"\*\*(E|ER)\.", "SA15-2"),
 (r"\*\*L\.", "SA15-3"),
 (r"\*\*R\.01", "SA15-12"),
 (r"\*\*R\.02", "SA15-7"),
 (r"\*\*R\.(05|06|08|09)", "SA15-4"),
 (r"\*\*R\.1[0-5]", "SA15-7"),
 (r"\*\*S\.0(21|23|30|39|41|47|53|55|57|59)", "SA15-4"),
 (r"\*\*S\.0(66|70|74)", "SA15-7"),
 (r"\*\*T\.", "SA15-6"),
]
EXTRA_OBJECTS = {
 "SA15-1": "the infinitesimal and crystalline site: de Rham cohomology as infinitesimal cohomology, nilpotent invariance, cosimplicial resolutions, differential operators of infinite order, the analytic comparison and its conjecture (cote 7, scans 061-072)",
 "SA15-2": "F-crystals and Frobenius structures: Frobenius twists F_M: M^(p) -> M, local freeness and finite presentation, conjectural constructions, compatibility with shifts and connecting maps, stacks of such structures, descent (cote 8, scans 002-022, 078-080)",
 "SA15-3": "Dieudonné-Manin: classification of F-isocrystals up to isogeny, slopes, lattices, connections and curvature, period equations, semilinear representations (cote 8, scans 025-058)",
 "SA15-4": "reused 'Tribu' typescripts on jets and contact: jet embeddings in characteristic zero, immersions, submersions, subimmersions, orbit maps (cote 8, scans 019-059)",
 "SA15-6": "Tannakian categories of crystals: fibre functors over Q_p, neutralization, full faithfulness, torsors, Frobenius as a group element, the local Galois diagram, Hodge structures (cote 8, scans 061-075)",
 "SA15-7": "a reused typescript on purity, base change, coefficient twists and modular weights (cote 8, scans 032, 062-076)",
 "SA15-8": "a boxed formula for groups of multiplicative type (cote 8, scan 078), matching Bergh-Rydh",
 "SA15-9": "integral de Rham and Hodge cohomology: free and torsion parts against H^n(X,O) and H^0(Omega^n) (cote 4)",
 "SA15-10": "duality of modules over truncated rings A_n: the reduced module, functionals, two duals and their pairing (cote 9)",
 "SA15-11": "deformations and the Hodge summand: descent of the Hodge piece, stratification, a polarization (cote 9)",
 "SA15-12": "the dossier as a document: the institutional cover, the 'Tribu' document numbers",
 "SA15-13": "rational double points and local square classes H^1(A, mu_2) (cote 8, scans 003, 017)",
}
FORCE = {}
for f, k in (("K4-01", "SA15-9"), ("K8-01", "SA15-2"), ("K9-01", "SA15-10"), ("K9-02", "SA15-11")):
    for n in range(1, 8):
        FORCE[f"work:{f}#{n}"] = k
D = "2026-11-18"
READ = {}
FLAGS = [
 ("a link across folders", "SA15-3 (cote 8, L-series) and SA18-8, SA19-6, SA14-2",
  "Dieudonné theory appears in four topics: F-isocrystals up to isogeny here, Cartier/Dieudonné for Picard p-torsion (SA18-8), formal groups and Witt rings (SA19-6), Oda's comparison (SA14-2, SA16-8)", "entry bodies; headings"),
 ("a link across folders", "SA15-6 (cote 8, T-series) and the motives topics SA05-SA07",
  "fibre functors over Q_p, Frobenius as an element of the motivic group and the Hodge agenda ('Hodge (simple, généralisée)', scan 075) are the Tannakian side of the motives topics", "entry bodies"),
 ("a link across folders", "SA15-1 (cote 7, scans 061-072) and SA16-8",
  "de Rham cohomology through infinitesimal neighbourhoods (cote 7) is the object behind Oda's comparison of the Hodge line (cote 62)", "entry bodies"),
 ("note overstates or misreads the page", "MPL_7_061-072+8_001-078 (all 80 entries)",
  "the notes are filed under 'Scan NNN' headings, one or more reader series (C7, E, ER, L, R, S, T) inside each; NOTES_INDEX gives no kind and no subject, so the index rows alone cannot place them. Not a misreading; an indexing gap.", "NOTES_INDEX.tsv of SA15"),
]
CHECKS = []
STATEMENTS = {
 "SA15-1": ("(notes) de Rham cohomology computed on the infinitesimal site is invariant under nilpotent thickenings; an analytic analogue is conjectured (scan 070)", "sketched, with a conjecture", "SA16-8 (Oda)"),
 "SA15-3": ("(notes) F-isocrystals over a perfect field classified up to isogeny by slopes", "worked, with the author's limitation 'unicité à isogénie près (mais pas d'existence ...)' (scan 050)", "SA18-8, SA19-6"),
}
