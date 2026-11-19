DEPENDS = [
    ("SA06-8", "uses", "SA06-9", "read", "15:40, 15:44 (Frobenius f acts by (p, (0,1), p); E -> E^(p) = E/Ker F_E is the prime ideal m over p)", "was 'proof' in sweep 2"),
    ("SA06-8", "uses", "SA05-18", "read", "15:52 (no real fibre functor; the quaternionic realization at infinity, the counterpart of 15:11)", "other topic"),
    ("SA06-8", "uses", "SA05-19", "read", "15:34, 15:66, 15:68 (Deuring categories, Brd(C), Ram(C/A) = sum Z/e_p: the definitions of 15:16-22)", "other topic; same object"),
    ("SA06-8", "uses", "SA15-2", "read", "15:42, 15:54-56 (F-crystals of rank 2 and slope 1/2 over F̄_p with the Tate functor; descents with F^2 + p = 0)", "other topic"),
    ("SA05-18", "uses", "SA06-9", "read", "15:5 and 15:14 use the Weil-number group that 15:100-104 define (M(q), M(p^infinity))", "other topic"),
    ("SA06-10", "uses", "SA06-9", "read", "15:135-137 (commutative motivic Galois groups: Q(1), Artin motives, G' x G_m)", "was 'proof' in sweep 2 (SA06-10 uses SA06-2)"),
    ("SA06-9", "uses", "SA06-4", "read", "15:100 ('Cela déterminerait ... le groupe de Galois motivique': the determination presupposes Tate's conjecture, as 15:3 says)", "was 'proof' in sweep 2"),
]
CORRECTIONS = [
    ("MPL_15_034-086, cote 15 scan 40", "'ramifié exactement en 2(?) et $\\infty$'", "the ink reads '2' (decided on the scan image, 250 dpi); the mathematics needs p: his slip of the pen. Read: 'en 2 [lire p] et infinity'", "the page's E^(p) = E/Ker F_E, the prime ideal m over p, Z_p*/Z_p*^2 '(= Z/2Z si p != 2)'"),
    ("MPL_15_034-086, cote 15 scan 86", "'chaque L_i ext. quadratique d'un corps de nb K_i tt. réel'", "each L_i is a CM field (involution = complex conjugation) or a totally real field (trivial involution); the conclusion (H^u compact) stands", "positive involutions on commutative semisimple algebras; Frobenius sqrt(p) gives a totally real factor; his own corollary on 15:130"),
    ("sweep2 SA06-8 status", "'his text; known in substance'", "refined: known in substance (Deuring 1941); his own: the Brandt Picard category and the 2-equivalence of 15:78, the adelic mu_2-torsor and the Deuring element (15:42-54), the quaternionic realization (15:52); open: the determination of xi_p (15:54)", "read 15:34-78"),
    ("sweep2 SA06-9 status", "'known conditionally'", "refined: 15:100-106 state a strong and a weak conjecture on Frobenius eigenvalues; weight 1 of both is Honda-Tate (1968); weight > 1 open as stated", "read 15:96-108, 15:128-133"),
]
CHECKS = [
    ("MPL_15_034-086 (15:40)", "re-derived that for p invertible in A' the rigidified pair (m, rho-bar = p) maps to the class of p in A'*/A'*^2 = H^1(S', mu_2): m_A' = O_A', and changing the trivialization by a central unit lambda multiplies it by Nrd(lambda) = lambda^2", "agrees", "sweep3/SA06/STUDY.md §3"),
    ("MPL_15_034-086 (15:40)", "re-derived the group over Z_p: pairs (m^k, t) modulo central units give Z_p*/Z_p*^2 x Z/2, with (m, p) of order 2 because m^2 = pO and Nrd(p) = p^2", "agrees", "sweep3/SA06/STUDY.md §3"),
    ("MPL_15_034-086 (15:42)", "checked Gamma' = Gamma'_0 x f(+-1) and Gamma = Gamma'_0 = H^1(𝔸, mu_2): f = (p, (0,1), p) projects to the generator of the Z/2 factor; p is a square in R (his margin)", "agrees", "sweep3/SA06/STUDY.md §3"),
    ("MPL_15_034-086 (15:74-78)", "checked the Proposition (the commutativity constraint does not depend on X: P(LM)P^-1 = (PLP^-1)(PMP^-1)) and the Conclusion (Eq(C) strict Picard, all canonically equivalent); consequence: the Gr-category class of 15:19 vanishes under (C), since a strictly commutative Picard category over a point is split (SGA 4 XVIII 1.4; Ext^2_Z = 0); (C) holds for maximal orders", "agrees", "sweep3/SA06/STUDY.md §3"),
    ("MPL_15_034-086 (15:86)", "checked the structure of B = prod L_i against the classification of commutative semisimple algebras with positive involution", "refined: totally real factors with trivial involution are missing (e.g. Frobenius sqrt(p)); conclusion unaffected", "sweep3/SA06/STUDY.md §2"),
    ("MPL_15_087-138 (15:96)", "re-derived the Proposition (x = y^2/N(y), div x = 2h(p - p'), x sigma(x) = 1) and the N.B. (lambda lambda-bar = p^i with p not split gives lambda = p^(i/2) times a root of unity: mu = lambda^2/p^i is a unit of absolute value 1 everywhere, Kronecker)", "agrees (the h of the statement is twice the class number)", "sweep3/SA06/STUDY.md §1"),
    ("MPL_15_087-138 (15:129-132)", "checked the Proposition (a)<=>(b)<=>(b')<=>(b'')<=>(c) on numbers with all |lambda_alpha|^2 = Q, the corollary of 15:130 and the Remark of 15:132-133", "agrees; standard", "sweep3/SA06/STUDY.md §1"),
    ("MPL_15_087-138 (15:102)", "checked that G/G^0 is dual to the roots of unity (all in Q^CM), hence to Ẑ, and that M(p^infinity) = lim M(q) under lambda -> lambda^m is torsion-free", "agrees", "sweep3/SA06/STUDY.md §1"),
    ("MPL_15_087-138 (15:106 margin)", "compared 'Résulte probablement de la théorie des multiplications complexes: cf. Taniyama-Shimura' with the literature: weight 1 is Honda's theorem (1968), proved by lifting to CM abelian varieties", "agrees", "sweep3/SA06/STUDY.md §1"),
]
READ = {
    ("MPL_15_034-086", "15"): ("read in full (his pages 34-56, 60-61, 66, 68, 70, 72, 74, 76, 78, 84, 86; reused typescripts on 67-79 odd and 85 identified, not studied); scan 40 checked on the image", "Deuring gerbes, Brandt Picard category, compact part of commutative motivic groups"),
    ("MPL_15_087-138", "15"): ("read in part (scans 96-108, 128-137)", "Weil numbers, CM fields, commutative motivic Galois groups; 87-95 and 109-126 (real fibre functors, Artin-Tate) not read in sweep 3"),
}
READY = {
    ("MPL_15_034-086", "15"): "his pages 34-86: ready for an edition after a check pass on the open readings; scan 40 settled ('2', his slip for p); the reused typescripts go to an appendix or out",
}
EXTRA_DELIV = [
    ("Codex folders K14-02, K14-03, K14-04, K14-08, K14-09, K15-02, K15-05, K15-06, K15-07, B15-01", "14, 15", "see the folders' inventories", "", "", "", "Codex web transcription with Work math notes; a second witness where a Pro package covers the same scans", "not read in sweep 3", "after the two witnesses are compared", "K15-02 and B15-01 cover the Deuring pages"),
]
