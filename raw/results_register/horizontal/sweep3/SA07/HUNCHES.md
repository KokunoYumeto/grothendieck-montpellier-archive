# SA07 hunches (sweep 3)

Claude Opus 5.5 at effort max (agent a28ea31fa17dd65e1), 18 Nov 2026. Each hunch: what may be true, the grounds, the
pages, the links. "(mine)" throughout: none of these is on the pages as a statement.

**H1. The Hodge splitting of an elliptic curve over Q̄ is algebraic exactly in the CM case (18:13 c).**
Grounds: with CM the Hodge decomposition of H^1_dR is the eigenspace decomposition of the CM field, defined over Q̄, so
h is algebraic. Without CM, h is tied to the value at tau (j(tau) in Q̄) of the non-holomorphic Eisenstein series
E2*(tau) = E2(tau) - 3/(pi Im tau), suitably normalized by the period; Masser (1975) treats the CM values; Nesterenko
(1996) gives trdeg Q(q, E2(q), E4(q), E6(q)) >= 3, which may force h transcendental. Pages: 18:11-13. Links: SA16-12
(the transcendental theory of elliptic curves), SA16-22 (CM).

**H2. The beta-part of 18:11 is the period conjecture for the periods together with their complex conjugates.**
Grounds: the Hodge splitting of T_DR (x) C is the complex conjugate of the Hodge filtration in Betti coordinates, so
k(beta) lies in k(alpha, conj(alpha)); 18:36 shows the role of conj(alpha) = f_infinity alpha over R. Then trdeg
K/k = g + u says the conjugate periods add exactly u = dim U' new transcendentals. Pages: 18:11, 18:36-38.

**H3. 18:6 is an early form of Sen's theorem.**
Grounds: two splittings of an extension of the Galois group pi by G'(C) (the Hodge-Tate one and the Galois one), a
character chi: pi -> Q_p*, and the conclusion that pi / Ker u is a p-adic analytic group with chi_1 -> Q_p*: the image
of Galois is a p-adic Lie group carrying the Hodge-Tate cocharacter. Sen (Annals 1973) proved that the Lie algebra of the
image contains the Hodge-Tate (Sen) operator. Pages: 18:5-6. Links: SA15-18 (cote 6 Tate-Hodge questions).

**H4. 18:5 is the earliest written form of the "mysterious functor" problem.**
Grounds: the parallel lists (Betti-De Rham, ..., De Rham filtré cristallin) and (Hodge-Tate, Tate-Hodge, Tate,
cristal filtré) with "Par quoi remplacer 1', 4' ??"; the problem was stated at the ICM 1970 ("Groupes de Barsotti-Tate et
cristaux"). The cote 18 pages are 1970 or later (mixed Hodge structures on 18:9) and earlier than Fontaine's period rings.
Dating needs the archive's chronology. Links: SA15-15, SA15-16, SA15-18.

**H5. A two-embedding period conjecture (18:42-45).**
Grounds: comparing the Betti lattices of two complex embeddings through de Rham fixes the Hodge filtration, so the
comparison lies in a parabolic and its field has transcendence degree at most the parabolic's dimension (he finds 5 for a
product of two non-CM curves, against dim G - 1 = 6). Hunch: equality holds generically, and the statement is a period
conjecture for the motive "M over k with two embeddings". Pages: 18:42-45.

**H6. The adelic comparison of Betti lattices is provable for non-CM elliptic curves (18:47-49).**
Grounds: his argument needs "la conjecture de Tate renforcée" (Galois image of finite index in G(Ẑ)) and a genericity
lemma; the lemma holds (check event SA07-S3-6), and the finite-index statement is Serre's open image theorem (1972) for
non-CM elliptic curves over number fields. So the genericity conclusion should be a theorem for those curves, and for
products of non-isogenous ones (Serre's results on products). Pages: 18:47-49.

**H7. The twisted Betti functor (18:35) is tensor-isomorphic to Betti over C but not over Q in general.**
Grounds: two Q-valued fibre functors differ by a G-torsor over Q; his twist by the order-2 element f_R gives the torsor
of the cocycle f_R, whose class need not vanish in H^1(Q, G). He writes "Il semble que ... ne sont pas ⊗ isom". Test on
G = G_m (Tate motives): the twist is by -1 and the classes are in Q*/Q*^2.
