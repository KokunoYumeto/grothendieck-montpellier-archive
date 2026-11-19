DEPENDS = [
    ("SA07-2", "uses", "SA07-1", "read", "18:11 (P = Isom(T_B (x) k, T_DR), P', P'': torsors between fibre functors)", "was 'proof' in sweep 2"),
    ("SA07-2", "uses", "SA07-7", "read", "18:36-38 (conj(alpha) = f_infinity alpha; R(alpha) = C)", "was 'proof' in sweep 2"),
    ("SA07-2", "uses", "SA05-8", "read", "18:11, 18:13 (the motivic Galois group G, dim g; GL(2) or the CM torus)", "other topic"),
    ("SA07-7", "uses", "SA07-3", "read", "18:34, 18:37 (f_R in G(Q), G = Aut_(x)(T_B) of the category of motives over R)", "was 'proof' in sweep 2"),
    ("SA07-6", "uses", "SA07-18", "read", "18:21 (i^!(C), i^!(Omega_X): local cohomology with supports)", "was 'proof' in sweep 2"),
    ("SA07-6", "uses", "SA07-3", "read", "18:25 (correspondences z in A^n(X x Y) act on Betti and de Rham)", "was 'proof' in sweep 2"),
    ("SA07-2", "uses", "SA07-6", "read", "18:19, 18:27-29 ((2 i pi)^n in k(alpha) when Q(-n) is in the category; lattices depend on sigma)", "new"),
    ("SA07-2", "uses", "SA15-18", "read", "18:5 (3' Hodge-Tate structure, 2' Tate-Hodge, 6' filtered crystal: the p-adic side)", "other topic"),
    ("SA07-2", "uses", "SA15-15", "read", "18:43 problem 4 (p-adic cohomology in characteristic p)", "other topic"),
]
CORRECTIONS = [
    ("sweep2 SA07-2 status", "'periods: the period torsor, his conjecture de transcendance N° 1 (genericity of the period point)'",
     "refined: 18:11 states generic-point conjectures for the three comparison points alpha (Betti-De Rham), beta (the Hodge splitting) and gamma (Hodge-Betti), and for the period point phi in Fil and psi in Big, with the trdeg list", "read 18:11"),
    ("sweep2 SA07-6 status", "'his text; known'", "made precise: P_an = (2 i pi)^p P_top (18:17, 18:21, 18:23); known as the normalization of Deligne, LNM 900, §1", "read 18:15-25"),
]
CHECKS = [
    ("MPL_15_195-228+18_002-017 (18:17)", "recomputed lambda = integral of dz/z over the unit circle = 2 i pi, the constant between P_an and P_top in codimension 1", "agrees with the page", "sweep3/SA07/STUDY.md §2"),
    ("MPL_15_195-228+18_002-017 (18:21, 18:23)", "re-derived the codimension-p factor (2 i pi)^p from the local product structure (p transverse discs, Künneth)", "agrees with the page; known (Deligne, LNM 900, §1)", "sweep3/SA07/STUDY.md §2"),
    ("MPL_18_018-062 (18:36)", "recomputed epsilon(f_infinity): complex conjugation reverses the orientation of P^1(C), so acts by -1 on H^2(P^1(C), Q) = Q(-1)_B", "agrees: epsilon(f_infinity) = -1", "sweep3/SA07/STUDY.md §3"),
    ("MPL_18_018-062 (18:38)", "checked the remark 'f_infinity = id only for sums of tensor powers of Q(2)': conjugation acts on Q(n)_B by (-1)^n", "agrees", "sweep3/SA07/STUDY.md §3"),
    ("MPL_15_195-228+18_002-017 (18:11)", "checked the transcendence-degree list against the dimensions: b = u + l, dim Big = g - l = (g - b) + u, trdeg K/k = g + u computed from alpha, beta and gamma", "consistent", "sweep3/SA07/STUDY.md §4"),
    ("MPL_18_018-062 (18:49)", "proved the lemma: in a coset U a of a compact open subgroup of G(Q̂), G connected over Q, an element whose components are generic over Q exists (countably many proper Q-subvarieties, each Haar-null in G(Q_l))", "agrees: the lemma is true", "sweep3/SA07/STUDY.md §4"),
    ("MPL_15_195-228+18_002-017 (18:9)", "compared the Tate twist of a mixed Hodge structure with Deligne, Hodge II, 2.1.13", "agrees", "sweep3/SA07/STUDY.md §5"),
]
READ = {
    ("MPL_15_195-228+18_002-017", "18"): ("read in full (his pages 18:4-6, 9-13, 15, 17; reused typescripts identified)", "periods and comparison programme"),
    ("MPL_18_018-062", "18"): ("read in full (his pages; reused Bourbaki typescripts n. 59, 370, 392, 413 and a translated paper identified, not studied)", "cycle classes, real Frobenius, Betti lattices"),
}
READY = {
    ("MPL_15_195-228+18_002-017", "15"): "the stretch is mostly reused Lie typescripts (not his): an appendix of the edition at most; check the 199 open readings first",
}
EXTRA_DELIV = [
    ("Codex folders K10-01..07, K16-02, K19-01..06", "10, 16, 19", "see the folders' inventories", "", "", "", "Codex web transcription with Work math notes and Codex sheet notes; no Pro transcription", "not read in sweep 3", "after an independent second transcription or a check pass", "single transcription"),
]
