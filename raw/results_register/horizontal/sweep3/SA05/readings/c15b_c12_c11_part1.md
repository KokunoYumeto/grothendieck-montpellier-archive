# SA05 sweep 3, stretch c15b_c12_c11, part 1: cote 11 scans 2-58, cote 12 scans 2-50

Claude Opus 5.5 at effort max (agent aa713c8c5c2c8b9d6), sweep 3 reader part 1, launched by agent a7b7747fd6dd29f87
(Claude Opus 5.5 at effort max). Started 19 Nov 2026 about 00:31 UTC, cut by the weekly limit, resumed about 01:27 UTC.
Brief: `sweep3/READER_BRIEF.md`. Witnesses: the Pro transcription (GPT-6 Astra, ChatGPT Pro mode), read with
readtex2.py; the Work second readings K11-01 to K12-03 (GPT-6.2 Astra at reasoning effort max, ChatGPT Work), read
blind of Pro; Michel Hua's project (`11.modern.tex`, `12.modern.tex`), credited where used. Scans checked on
`03_theorie_des_motifs/11.pdf` and `12.pdf`; renders in my scratch folder `sa05p1/`.

## State (kept current)

| Pages | State |
|---|---|
| 11:2-42 (`MPL_11_002-042`) | read: his 24 pages, items 1-4; typescript identified |
| 11:43-58 (`MPL_11_043-058+56`) | read: his 7 pages, items 5-6; typescript identified |
| 12:2-50 (`MPL_12_002-050`) | read: his 45 pages, items 7-10 (K12 witnesses not compared) |

## The split of MPL_11_002-042, checked on the pages

- Blank: 11:2 and 11:33 (renders; no page files, as the package says).
- His: the odd scans 3-31 and the scans 34, 36, 38, 40, 42.
- Reused typescript: the even scans 4-32 and the odd scans 35-41. **It is a typescript of Mumford's Geometric Invariant
  Theory, chapters 2 and 3** (internal folios -2.13- to -2.33- and -3.1- to -3.13-): 11:6 "Chapter 3. An elementary
  example" (PGL(n) acting on (P_n)^(m+1) over Z), 11:4 its §1 (SL(n+1)-linearizations, Definition 3.1), 11:12
  Proposition 2.18 (relative ampleness and stability), 11:8-14 the function nu^L(x, delta) on the flag complex
  Delta(G), 11:16 "conjecture of Tits". The Pro notes found the textual parallels (their B6: Mumford-Fogarty, 2nd ed.,
  ch. 2-3). So the item SA05-7 ("a reused typescript on spherical buildings: Tits's centre conjecture") is the GIT
  typescript; the Tits conjecture there is Mumford's citation (a most-responsible one-parameter subgroup), settled by
  Kempf, Ann. of Math. 108 (1978), and Rousseau (1978) (locators unverified). Not studied further.

## Item 1. The category of correspondences V^A (11:3-15) — SA05-1

**Places.** 11:3 definition; 11:5 associativity; 11:7 units; 11:9 which formulas were used, the graph map phi;
11:11 phi is a functor, the action psi; 11:13 psi is a functor; 11:15 the square commutes, transposition.

**What he does.** V a category with products of two objects (and a final object); A: V -> C a "bivariant" functor to
graded algebras, with f^* and f_* and an exchange (base-change) condition "dont le besoin sera vu dans la suite". V^A
has the objects of V and Hom(X, Y) = A(X x Y); v o u = p_31*(p_32^*(v) p_21^*(u)) (indices in matrix order: p_31 is
the projection to X x Z); units Delta_X = delta_X*(1); phi(f) = Gamma_f*(1); psi(X) = A(X) with
u(x) = p_2*(u p_1^*(x)); psi phi = omega A (omega forgets the algebra structure); the transposition s.

**What is proved.** All of it, by base change ("échange") and the projection formula; 11:9 notes that associativity
uses them only for squares of projections, the units also for the diagonals and their products with Y.

**What I checked** (check events 1-6).
- Associativity (11:5): both sides reduce to p_XT*(p_ZT^*w p_YZ^*v p_XY^*u), through the cartesian squares
  X x Y x Z x T = (X x Y x Z) x_(X x Z) (X x Z x T) and = (X x Y x T) x_(Y x T) (Y x Z x T).
- Signs. With pushforwards right-linear, f_*(x f^*y) = f_*(x) y (the convention of his 11:7 margin), moving a class y
  to the left of f_* costs (-1)^(deg y . reldim f). So the first computation of 11:5 carries (-1)^(deg w . dim Y), the
  unit u o Delta_X carries (-1)^(deg u . dim X), Delta_X o v carries none (his margin: "signe (-1)^(uX); pas de signe
  pour calculer Delta_X o v = v": right), and 11:13 carries (-1)^(deg v . dim X). All are 1 when pushforwards have even
  degree, as in a Weil cohomology (degree 2 dim), so V^A is a category there; with odd-degree pushforwards (manifolds of
  odd dimension) the composition needs a sign to be associative and unital. The factor written beside the step on
  11:5 reads (-1)^(w̄ Ȳ) on the ink (Pro: deleted, exponent w̄ and the bar of nu'_*): either reading is deg w times the
  relative dimension of nu', which is dim Y, the exact sign of that step. Whether he struck it the image does not decide.
- phi is a functor (11:11): the squares are cartesian and transverse (graphs over different factors);
  lambda^* lambda'_*(1) = Gamma_f*(1) from the cartesian square with vertex X; p_31 nu = Gamma_gf.
- psi (11:13): Delta_X(x) = x by the right projection formula; v(u(x)) = (v o u)(x) by base change over Y.
- 11:15: phi(f)(x) = p_2* Gamma_f*(x) = f_*(x), since p_2 Gamma_f = f.
- Transposition: t(v o u) = (-1)^(deg u deg v) (tu o tv), the Koszul sign of the swap; his margin "vérifier que c'est
  multiplicatif!" is answered: anti-multiplicative, with no sign on even classes.

**What is wrong** (ink checked). His slips: 11:15 "p_2* Gamma_f*(x) = x" for f_*(x); 11:15 "si f: Y -> X" for
f: X -> Y (A(f)^*: A(Y) -> A(X) and phi(f) in A(X x Y) need it); both also in K11-01 (its S15.1, S15.2). Readings:
11:5 "p_{YY(?)}^*(u)" reads p_XY^*(u); 11:13 "p_{XZ(?)}^*(u)" reads p_XY^*(u).

**What is open.** Nothing in the mathematics; the exact exchange hypothesis is left to "la suite" (11:3), and 11:9
says which cases are used. Known as definitions: Manin, Mat. Sb. 77 (1968); Kleiman, "Algebraic cycles and the Weil
conjectures", Dix exposés (1968) (locators unverified).

## Item 2. Transposition, duality and stable systems A' ⊂ A (11:17-25) — SA05-1, SA05-12

**Places.** 11:17 phi^* = s phi° and transposition; 11:19 remark on monoids and signs; 11:21 stable systems;
11:23 A_sp and maps "of type A'"; 11:25 the stable system generated by given classes.

**What he does and what is proved.**
- 11:17: psi phi^* = omega^* A° ("vérifier"); with a final object e and A(e) = k the A(X) are gauged by f_*: A(X) -> k,
  and for Poincaré algebras f_* is known from f^*. Claim: if u in A(X x Y) is central, u~ and (su)~ are transposes for
  k_X, k_Y: g_*(y u_*(x)) = f_*(u^*(y) x), "mod. signe!". Proof by the two projection formulas and u central.
- 11:19: only the monoid structure of the A(X) was used; with signs one needs graded monoids with involutions sigma^i
  (sigma^i = id for i even) and degrees d(A) fixing deg f_* = d(B) - d(A), to say how the left projection formula
  carries signs when the right one holds.
- 11:21: A' ⊂ A (1 in A'(X), stable under the sign) is stable (1°: under f^*, f_*, products) iff 2°: a) u_*(x) in A'
  for u, x in A'; b) x ⊠ y in A'; c) every graph gamma_f in A'. NB: these A' are the subcategories of V^A with all
  objects, stable under ⊠ of arrows, containing the gamma_f and their transposes.
- 11:23-25: A_sp, the smallest stable system, contains the f_*(1_Y), and "dans beaucoup de cas" equals them (smooth
  projective varieties, "si on admet la résolution des singularités"); maps of type A', (x_i) -> u(x_1 ⊠ ... ⊠ x_n)
  with u in A', are closed under composition; the stable system generated by A' and classes E_X is the set of values
  of such maps on the E_X.

**What I checked** (events 7-11). 11:17: correct, with the sign (-1)^(deg y . dim X) of the left projection formula
and u central (u of even degree); exact for a Weil cohomology. 11:19: his rule is the one I used on 11:5-13
((-1)^(deg y . deg f_*)), and 11:34's margin repeats it. 11:21: both directions re-derived; f^*(y) = (s gamma_f)_*(y)
by the right projection formula, and s gamma_f = sigma_*(gamma_f) lies in A' by the direct images just proved. 11:23:
composition of maps of type A': chi(phi, psi)(x, y) = (w o (u ⊠ v))(x ⊠ y), up to the Koszul sign of reordering.

**What is wrong.** 11:23: A_sp(X) is the group generated by the f_*(1_Y), not their set (Michel Hua's project: "the
set is not closed under products: E·E = -[pt] on a blow-up"). For a Weil cohomology on smooth projective varieties
it is the group of algebraic classes: each cl(Z) is f_*(1) for a resolution of Z (Hironaka, characteristic 0); in
characteristic p, de Jong's alterations give it with Q coefficients (cl(Z) = f_*(1)/deg f). 11:25: if stable systems
are additive, B(X) must be the finite sums of such values (also Michel Hua's project); in the monoid frame of 11:19
it stands as written. Reading: 11:17 "≥(?)" is "=" on the ink (then "mod. signe!").

**What is open.** "vérifier" for psi phi^* = omega^* A° (11:17): it holds by the 11:15 computation with the transposed
graph (f^*(y) = (s gamma_f)_*(y), as 11:21 uses). The NB of 11:21 ("il suffit s delta_X") I did not check.

## Item 3. Poincaré algebras, f_* by duality, tensor products and their signs (11:27-31) — SA05-1

**What he does.** 11:27: Poincaré algebras (graded, projective of finite type, degrees >= 0, k_A of degree d°(A) with
k_A(xy) strictly non-degenerate); morphisms are algebra maps f^*; f_* is defined by k_A(f^*(b) a) = k_B(b f_*(a)); he
lists functoriality, the projection formula f_*(a) b = f_*(a f^* b) and k_B f_* = k_A. 11:29: A ⊗ B is the coproduct
with k_(A⊗B) = k_A ⊗ k_B; he computes how (f x g)_* differs from f_* ⊗ g_* under four sign conventions and boxes
(f x g)_* = (f_* ⊗ord g_*)(id_A ⊗ [sign on B']^(deg f)), "Il n'y a aucun signe dès que f est pair". 11:31: for even f
the symmetry s(x ⊗ y) = (-1)^(xy) y ⊗ x is compatible; base change for X x S -> Y x S and for the graph square of
X -> Y -> Z; margin "Question: ... Suffit-il que le produit fibré existe dans V et que les dim. soient correctes?"

**What I checked** (events 12-17).
- 11:27: functoriality and k_B f_* = k_A re-derived. With b on the left in the defining identity the left formula
  b f_*(a) = f_*(f^*(b) a) holds exactly; the right formula he writes holds up to (-1)^(deg b (d°B - d°A)), so exactly
  when the degrees d° are even (the convention 11:34 adopts).
- 11:29: re-derived all three discrepancy factors he states: (-1)^(ag+bf+Bf) (twisted k and ⊗), (-1)^(a'g+bf)
  (ordinary k, twisted ⊗), (-1)^(bf+AB+A'B') (twisted k, ordinary ⊗): all right. For ordinary k and ⊗ the true rule
  is (f x g)_*(a' ⊗ b') = (-1)^(deg f (d°B' - deg b')) f_*(a') ⊗ g_*(b'): the dual test element b has degree
  d°B' - deg b'. The ink has "(-1)^(bf) = (-1)^(B'f -" with the exponent unfinished (Pro drops the dash); the boxed
  operator on B' must be read as (-1)^(deg f (d°B' - deg)). No sign when deg f is even: right.
- 11:31: the symmetry check (even f, g) and the two base-change formulas for X x S -> Y x S re-derived; the graph
  square λ'^* λ_* = Gamma_f* Gamma_gf^* is the standard consequence of the Künneth form of the graph class (not
  re-derived).
- **His question answered (no).** In V = smooth projective varieties, take a conic C ⊂ P^2 and a tangent line L. The
  fibre product in V exists (V-objects are reduced, so maps into L x_(P^2) C = Spec k[e]/e^2 factor through the
  reduced point) and has the expected dimension 0, but i_L^* i_C*(1) has degree 2 while the base-changed class has
  degree 1. The right hypothesis is transversality (the scheme fibre product smooth of the expected dimension, or
  Tor-independence); with proper but non-transverse intersection one needs the multiplicities (refined Gysin maps),
  with excess dimension the excess intersection formula (Fulton, Intersection Theory, ch. 6; locator unverified).
  Michel Hua's project notes the excess case: the square of two diagonals fails by the Euler class.

**What is wrong.** Only the unfinished exponent of 11:29 (reading correction) and the right projection formula of
11:27 for odd d° (sign). **Open (his):** the general exchange axiom, which his later page 11:46 recalls ("axiome
cartésien oublié!", by Michel Hua's project; to be seen there).

## Item 4. Bivariant algebras, simplicial bivariant algebras and stable systems on X^n (11:34-42) — SA05-1, SA05-12

**What he does.** 11:34: the bivariant category: (f_*, f^*) with f_* B-linear on both sides ("Il faut choisir entre
l'une et l'autre formule!", sign (-1)^(delta j)), k_B f_* = k_A; isomorphisms; with phi_A: A -> Hom(A, k),
x -> k(- x), f_* is characterized by k(y f_*(x)) = k(f^*(y) x). 11:36: f_* raises degrees by d(B) - d(A); he works
with graded anticommutative algebras with a degree d(A), f_* of degree d(B) - d(A), and not only Poincaré algebras
("les constructions universelles ... en feront de tte façon sortir"). 11:38: A ⊗ B is not a product in C (no
canonical diagonal), but is one when A, B are Poincaré algebras; simplicial bivariant algebras on finite non-empty
sets; "spécial" = Künneth; an equivalence with Poincaré algebras. 11:40: a Proposition: A_n ⊂ H^*(X^n) stable under
the symmetric group; (i) a) correspondences in A act within the A_n, b) ⊠ and 1, c) the graphs of the elementary
surjections and injections [1,n+1] -> [1,n], [1,n] -> [1,n+1]; (ii) subalgebras stable under images by projections
and the direct images by the diagonal injections; (iii) the A_(n+m) as sets of maps closed under composition, ⊠,
identities, simplicial maps. 11:42: a second draft: gauged algebras, simplicial gauged algebras, A(.) -> (A_0, Delta)
fully faithful with Delta in (A ⊗ A)^(d(A)) ("il convient de préciser les axiomes"; margin "à vérifier; ... δ_*");
Ex. 1) a cohomology with Künneth and Poincaré on complete non-singular varieties of dimension d gives
I -> H^*(X^I); (*) isomorphisms need not have f_*(1) = 1.

**What I checked** (events 18-22).
- 11:34: the isomorphisms: f^* bijective and f_*(1) invertible, since f_*(x) = f^*^(-1)(x) f_*(1) by B-linearity;
  the equivalence "morphism <=> (***)" re-derived both ways (phi_B injective); the margin sign (-1)^(delta j) is the
  sign of my 11:5-13 checks.
- 11:36: the degree shift d(B) - d(A) re-derived (the lines "phi_A(f_*(x))" and "d - i'" are slips or misreadings for
  phi_B(f_*(x)) and d - i; harmless; not decided on the ink).
- 11:38: re-derived that A ⊗ B is a product in C for Poincaré A, B over a field: h^* is forced by the coproduct of
  algebras, h_* by duality (phi_(A ⊗ B) bijective), and p_* h_* = f_* by pairing. The equivalence needs "spéciales"
  (Michel Hua's project: the constant object I -> P is a counterexample otherwise); with it, P -> (I -> P^(⊗I)) is a
  quasi-inverse (alpha^* from the coproduct, alpha_* by duality).
- 11:40: (i) <=> (ii) is the case X^. of 11:21's 1° <=> 2° (elementary surjections, injections and permutations
  generate all maps of finite sets).
- 11:42: delta_* is determined by Delta = delta_*(1): delta_*(a) = delta_*(delta^*(a ⊗ 1)) = (a ⊗ 1) Delta, since
  delta^* (multiplication) is onto; this answers the first step of his margin. The axioms he leaves open are those of a
  commutative Frobenius structure: (a ⊗ 1) Delta = (1 ⊗ a) Delta, symmetry, the counit identity (k ⊗ id)(Delta (a ⊗ 1))
  = a (11:7), coassociativity. The isomorphism example of (*) checked: k_B(y sigma) = k_A(y).

**What is wrong** (ink checked). 11:40 (i) a): the ink has "u(x) ∈ H^*(X^m)", the condition needs u(x) ∈ A_m; 11:42:
the ink has "nulles en degré ∉ [1, d(A)]", the unit and "k de degré 0" need [0, d(A)] (both also in Michel Hua's
project). 11:38: "spéciales" missing in the equivalence (Michel Hua's project).

**What is open (his).** The axioms on Delta and the full faithfulness (11:42, "à vérifier"), clear for special
objects; the Proposition of 11:40 has no written proof (it follows from 11:21).

## The split of MPL_11_043-058+56 (cote 11 part), checked on the pages

His: 11:44, 46, 48, 51, 53, 55, 57; 11:50 blank (no page file). Reused typescript: 11:43, 45, 47, 49, 52, 54, 56, 58 are
further leaves of the same Mumford GIT typescript, chapter 3: 11:43 folio -3.7- (Corollary 3.2, normalizing points),
11:45 -3.6- and 11:47 -3.4- (proof of Proposition 3.1, U_R ≅ PGL(n) x A^(n nu - n)), 11:49 -3.3- (the determinants D,
R-partitions, Definitions 3.2-3.3), 11:52 -3.18- and 11:54 -3.17- (Corollary 3.7, Theorem 3.8: the geometric quotient
of U_stable), 11:56 -3.15- and 11:58 -3.14- (the stability criterion through the cone C_x). Not studied.

## Item 5. The correspondence formalism on X^I, second draft (11:44-48) — SA05-1

**What he does.** 11:44: variants (compact topological manifolds; k a ring when Poincaré duality holds integrally);
2) the Chow ring gauged by degree, or its quotients (numerical, homological, algebraic equivalence, Picard, Albanese),
give simplicial gauged bivariant rings "qui n'a plus aucune tendance à être spécial, et dont les composantes n'ont pas
trop envie d'être de Poincaré"; 3) K(X) gauged by chi in degree 0. Correspondences: C in A(I ⊔ I') acts by
x -> alpha'_*(C alpha^*(x)) (margin "il y a un choix: prendre Cy ou yC!"); the actions are known from the products and
the alpha^*, alpha_* of the face operators. 11:46: A(I'; I) = A(I ⊔ I'), v o u = p_31*(p_21^*(u) p_32^*(v)) (u now
before v, the other order than 11:3), and (v o u)~ = v~ o u~, "OK mod signes"; in a figure beside the base-change step
alpha'^* gamma'_* = p_32* p_21^*: "axiome cartésien oublié !". 11:48: Delta_I = delta_*(1) for the fold
I ⊔ I -> I and Delta_I~ = id; the page stops ("Il faut encore [vérifier] l'associativité ... On voit que sous ces
conditions,").

**What I checked** (events 23-25). 11:46: both sides re-derived to p_3*(p_21^*u p_32^*v p_1^*x) up to the Koszul sign
of u, v and one projection-formula sign; the square X^(I ⊔ I' ⊔ I'') = X^(I ⊔ I') x_(X^I') X^(I' ⊔ I'') is a product
square, so base change holds for it in any Künneth theory; his "axiome cartésien oublié" is right: the axioms of 11:42
must include base change for these squares. 11:48: Delta~ = id re-derived (right projection formula). 11:44: "not
special" right (Künneth fails for Chow groups and for cycles modulo any adequate relation: NS(E x E) of a CM
elliptic curve has rank 4 > 2). "Pas de Poincaré" needs a qualification: modulo numerical equivalence with Q
coefficients the components are Poincaré algebras (non-degenerate by definition, finite-dimensional through any Weil
cohomology); modulo homological equivalence they are Poincaré iff hom = num, i.e. iff the standard conjecture D holds
for the X^I (link SA05-2).

## Item 6. The tautological subalgebras of H^*(X^k) (11:51-57) — SA05-1, SA05-12

**What he does.** 11:51: (1) in H^*(X), 1 and the point class y (degree n, the top degree), y^2 = 0; (2) in
H^*(X x X), y_1, y_2, the diagonal delta, with y_1 y_2 = y_1 delta = y_2 delta, delta^2 = chi y_1 y_2 (chi the
Euler-Poincaré characteristic), "base" 1; y_1, y_2, delta; y_1 y_2; (3) in H^*(X^3), y_i, delta_ij, the small diagonal
delta, ten relations, a "base" of 1 + 6 + 7 + 1 elements. 11:53: generators for X^k: the k transforms of y, and in
degree rn the C(k, r+1) transforms of the diagonal of r+1 factors; "relations" left blank. 11:55-57: the classes
epsilon_(R,J) of the partial diagonals Z_(R,J) (R a partition of I, the block J fixed at a point) and their products:
0 if J ∩ J' ≠ ∅; reduction to J = J' = ∅ with R'' (generated by R, R') coarse; s + s' <= k + 1; equality gives the small
diagonal ("! vérifier OK"), k > s + s' gives 0 by degree, k = s + s' gives "chi(?) y_(X^k)" ("! vérifier"); stability
under ⊠, pullbacks and pushforwards by projections, composition; box: "engendré, via ⊠, par y, et les delta_I".

**What I checked** (events 26-29).
- 11:51: every relation re-derived: the transverse intersections (y_1 delta = y_1 y_2; delta_12 delta_23 = delta), the
  self-intersection delta^2 = chi y_1 y_2, and delta_12 delta = chi y_1 y_2 y_3 by excess along the small diagonal (excess
  bundle T_X). For n odd, delta^2 = -delta^2 forces chi y_1 y_2 = 0, consistent with chi = 0 in odd dimension.
- 11:55-57, the unpointed rule: put a graph on the classes of R and R' (vertices) with one edge per element of I; it is
  connected (R'' coarse), with cycle rank b = k - s - s' + 1 >= 0. b = 0 (a tree): transverse, the product is the small
  diagonal; b = 1: excess T_X along the small diagonal, the product is chi times the point class of X^k; b >= 2: zero by
  degree. So his "chi(?)" is right (also Michel Hua's project, by the excess formula), with the instances
  delta.delta = chi y_1 y_2, delta_12 delta = chi y_1 y_2 y_3, delta_12 delta_23 = delta.
- Pushforward along X^I -> X^(I - {i}): the class with i removed if i is in J or in a block of two or more; 0 if {i} is a
  free singleton; for the small diagonal, delta_(I - {i}) (Michel Hua's project: "not delta_I"). The box (generation
  by y and the delta_I under ⊠) holds.

**What is wrong.**
- **The degree-2n "base" of 11:51 (3) is not free in general; the exact relation.** Let
  M = delta - (delta_12 y_3 + delta_23 y_1 + delta_31 y_2) + (y_1 y_2 + y_2 y_3 + y_3 y_1) in H^(2n)(X^3). Pairing with
  u ⊗ v ⊗ w: M vanishes on every triple with a factor of degree 0, and equals the integral of uvw on positive degrees.
  So M = 0 iff the integral of uvw vanishes for all u, v, w of positive degree: this holds for every curve and every
  surface with b_1 = 0 (K3, P^2, rational surfaces), where the seven classes span at most six dimensions. This is the
  cohomological form of the Gross-Schoen modified diagonal (curves; Gross-Schoen, Ann. Inst. Fourier 45, 1995) and of
  the Beauville-Voisin relation (K3; J. Algebraic Geom. 13, 2004) (locators unverified). Where H^*(X) lives only in
  degrees 0 and n (P^1, spheres), even delta = y_1 + y_2 (Michel Hua's project: "spanning families, free only
  generically").
- **The pointed-block product rule of 11:55 is incomplete.** "(Π y_i over J~ ∪ J~')..." holds only when the block's
  class graph is a tree; otherwise the product is 0. Example on X^2: R = {{1,2}} with J = {1,2} (class y_1 y_2) and
  R' = {{1,2}} with J' = ∅ (class delta): the rule gives y_1 y_2, the product is 0 (degree 3n > 2n). Complete rule:
  the product is the ⊠ over the blocks A'' of R'' of: unpointed, b = 0 the small diagonal of X^(A''), b = 1 chi times
  its point class, b >= 2 zero; pointed by one of J, J', b = 0 the product of the y_i, b >= 1 zero; pointed by both,
  zero (Michel Hua's project also completes the pointed case).
- Slips (the ink, read alike by the Pro transcription and K11-04): 11:51 "delta ∈ H^n(X)" for H^n(X x X); the degree-2n
  "base" of X x X written "y_1 y_2 y_3" for y_1 y_2. Reading: Pro "delta_1(?) y_2" is a struck delta followed by
  y_1 y_2 (K11-04).

**What is open (his).** The relations for general k (11:53, blank): the rule above with the relation M and its
analogues gives them. **What it is (mine).** The smallest stable system of 11:40 containing the point class: the
subring of H^*(X^k) generated by the diagonals and the point class. Its Chow-theoretic version, with a canonical
0-cycle in place of y, is the subject of the Beauville-Voisin and Voisin conjectures on the tautological rings of
powers of K3 and hyperkähler varieties (hunch H4).

## Placements of sweep 2 that the pages of cote 11 do not bear out

- SA05-2 (the standard conjectures as he lettered them), places "cote 11, scans 3, 16, 21, 23, 27, 34": none of these
  letters a standard conjecture; 11:16 is the GIT typescript ("conjecture of Tits"). The Pro notes agree ("do not give
  a fresh A-D list"; their concordance draft C = printed B comes from cote 16).
- SA05-15 (Oda), places "cote 11, scans 17, 27, 34, 42": no Oda content on these pages (transposition, Poincaré
  algebras, bivariant algebras).
- SA05-3 (quadrics), places "cote 11, scans 2, 30": 11:2 is blank and 11:30 GIT typescript; the quadrics are on cote 56
  scan 2 ("Cas des Quadriques"), in the same package: the places are cote 56's.
- SA05-4 (group-scheme text), place "cote 11, scan 16": GIT typescript (reductive groups, parabolics), not that text.
- SA05-7: see the split above (Mumford's GIT).

## The split of MPL_12_002-050, checked on the pages

His: 12:2-8, 10, 12-19, 23-50. 12:20 and 12:22 have no page file. 12:21 is a plan sheet, not a cover: a numbered plan
1)-19) for a treatise "motifs sur X" (M^+(X), variance, limits, T_l, M(X), Hom/RHom, twisted constant motives,
filtrations, rings M^+(X), the topological meaning of levels, L(k) -> M^+(k) and birational invariants, the Tate
conjecture, absolute cohomology, rational points, positive forms, L-functions, Hodge cohomology). 12:9 and 12:11 are not
reused typescripts: they carry the printed IHES letterhead "91 - BURES-SUR-YVETTE 928 48-53", 12:9 with his text above
it, 12:11 the letterhead alone. Département 91 (Essonne) exists from 1 January 1968, so 12:9 is written in 1968 or later
(hunch H5; dating from my knowledge, unverified).

## Item 7. "Esquisse d'une théorie des motifs" (12:2-14) — SA05-12, SA05-8, SA05-9, SA05-18

**What he does.** 12:2: the plan (effective motives M^+(k), semisimple abelian with ⊗; realizations T_DR, T_Hdg, T_B,
T^l, faithful; grading h^i; M^(+1)(k)° ≃ Isab(k); full faithfulness under extension of algebraically closed fields;
Q(-1) and M(k) with a universal property for Künneth functors with T(Q(-1)) invertible). 12:3-4: the level (niveau);
decomposition by pure levels; level <= dim X; the coniveau filtration on H^i(X, Q_l) is the image of the largest
submotive of level <= i - 2j, hence (resolution and standard conjectures) its dimensions are independent of l. 12:4-6: rigid
⊗-categories, fibre functors, (C, F) ≃ (Modf(G), oubli), semisimple <=> pro-reductive, F' = P x^G F ("à prouver"), a
fibre functor over a finite extension for C of finite type, gerbes. 12:6-8: motives over a regular connected S
(Hom on the generic fibre), Betti fibre functors, Serre's counterexample in characteristic p (supersingular curves),
association of F with geometric points. 12:9-14: G -> pi_1(S, xi) through G/G^0, (*) bijective under Tate/Hodge and iff
G is connected over algebraically closed fields; phi_l: pi_1 -> G(Q_l), psi_l phi_l = id; the Tate conjecture as
Zariski density of the l-adic image; over a finite field Frob_(k,F) in Z(Q), Tate => G commutative, an extension of
Ẑ by a protorus; Frobenius classes f_s in the adjoint quotient I_G(Q) = T/W.

**What I checked** (events 30-34). M^(+1)° ≃ Isab (h^1 against abelian varieties up to isogeny) and full faithfulness
over algebraically closed extensions for numerical motives: right (rigidity of cycles modulo numerical equivalence).
Level: "h^i(X) of level <= 2n - i for i > n" follows from hard Lefschetz; the injection h^i(X) -> h^i(Y) for a linear
section of dimension i is weak Lefschetz. Coniveau = image of the largest submotive of level <= i - 2j: one inclusion is
direct (a correspondence of degree j from a variety of dimension i - 2j has support of codimension >= j), the other is
Deligne's Filt^j = Im H^(i-2j)(Z~)(-j) plus the standard conjectures; l-independence is unconditional in characteristic 0
(comparison with Betti) and open in characteristic p, as he makes it conditional. Tannakian statements: Saavedra (1972),
Deligne-Milne (1982); "a fibre functor over a finite extension" is Deligne, Catégories tannakiennes (1990) (locators
unverified). psi_l phi_l = id re-derived (Artin motives). Over F_q: Tate => G commutative, G/G^0 = Ẑ, G^0 a protorus:
the frame of SA05-18 (15:3-14). Frob_(k,F) in the centre, defined over Q: right (inner twists fix the centre).

**What is wrong or loose.** 12:2 §5: the universal property needs T defined on correspondences (not only on V(k)°) and
compatible with the chosen equivalence; a Weil cohomology satisfies Künneth with T(Q(-1)) invertible but factors
through numerical motives only if hom = num (standard conjecture D). 12:8 Ex. 4: "du moins si k dénombrable" is not
needed: over an algebraically closed k the Artin motives are sums of the unit, so every fibre functor is associated.

## Item 8. Structures on the motivic Galois group; Mumford-Tate (12:15-19) — SA05-8, SA05-9, SA05-21

12:15-17: a ⊗-grading of type Pi <=> D_K(Pi) -> G, central iff it comes from the objects; the weight w: G_m -> G;
Hodge cocharacters i_1 i_2 = w with complex conjugation exchanging them; epsilon: G -> G_m from Q(-1) with
epsilon(w(lambda)) = lambda^2; a filtered fibre functor is recovered from the graded one by a torsor under the unipotent
group H. 12:17-19: the Mumford-Tate group as the smallest Q-subgroup with i_1, i_2 in it (connected); its invariants in
tensor spaces are the classes of type (0,0); for V from a motive, G -> G_0 (motivic) and "La conjecture de Hodge
s'interprète en disant que G = G_0". **Checked** (event 35): all right (Deligne, Hodge cycles on abelian varieties, 1982,
§3; locator unverified); epsilon w = lambda^2 is SA05-18's epsilon i(lambda) = lambda^2. **Remark:** his hypothesis "on
an extension K' an isomorphism F ≃ Gr F compatible with filtrations" is automatic in characteristic 0: the torsor is
under a unipotent group, and H^1(K, U) = 0, so filtrations of fibre functors split over K itself.

## Item 9. Motives over a base: axioms (12:21-41) — SA05-12, SA05-9, SA05-10

**What he does.** 12:23-29: M^+(X) for every noetherian X: Q-linear abelian, ⊗, D^b, f^*, Rf_* (proper or Y excellent),
projection formula, limits, T_l faithful exact to constructible Q_l-sheaves compatible with f^*, Rf_*, f^!, Künneth;
Q(-1) = R^2 f_* 1 on P^1_X; R^(2d) f_* 1 = 1(-d); purity Ri^! 1 = 1(-d); M(X) by inverting Q(-1). 12:30-31: l-independence
of characteristic polynomials of endomorphisms by the trace in End(1) = Q. 12:31-36: the weight filtration M_i^+, its
behaviour under R^j f_! (weights <= i + j) and R^j f_* (<= i + 2j), the "type dimensionnel" D_i (level up to Tate
twists), D_i ⊗ D_j ⊂ D_(i+j), Q(-j) in D_0. 12:36-41: twisted constant motives, the rings M^+(X) = Z^(Sigma^+), xi the
class of Q(-1), M(X) = M^+(X)[1/xi], the sets sigma_i(X), duality x -> x^v xi^i.

**What I checked** (events 36-38). The trace argument (12:30-31): right (rigid contraction, ⊗-functors preserve traces,
characteristic polynomials from the traces of the exterior powers). The weight bounds for R^j f_! and R^j f_* are
Deligne's (Weil II 3.3.1; Hodge II) (locator unverified). The duality "∨ = xi^(-i) on sigma_i" follows from a polarization
of each simple pure motive (M ≃ M^v(-i)), i.e. from the Hodge standard conjecture (SA05-11), as his "théorie projetée".

**What is wrong.** 12:34 "en particulier tous équiv. can. à C_0(X)": twisting gives C_i ≃ C_(i+2j), so there are two
classes, C_0 and C_1 (his own 12:39 uses M_0 and M_1); 12:38-39 "xi est de degré 1": Q(-1) has weight 2 (his 12:32
"Z(-1) in M_2^+" and the product M_1 ⊗ M_1 -> M_0, u, v -> xi^(-1) uv, both need degree 2). 12:36-37: "Ext^i nuls (i > 0)"
on the twisted constant motives holds for pure motives only; in the mixed frame of 12:23 (Rf_*, f^!, constructible
realizations) the category contains Q(0), Q(1) and is "stable par extensions", so it contains Kummer motives:
Ext^1(Q(0), Q(1)) ⊇ k^* ⊗ Q over a field k (Deligne's 1-motives). 12:27 "Z_S(-d)" for 1_S(-d) in a Q-linear category,
and 12:28 "M(-1) = M ⊗ Q(+1)" for M ⊗ Q(-1) (readings or slips, not decided on the ink).

**Open (his programme).** An abelian category of mixed motives over X with exact faithful T_l (the motivic
t-structure) is conjectural; the triangulated theory exists (Voevodsky; Ayoub; Cisinski-Déglise, 2019).

## Item 10. Coniveau, L(K) -> M^+(K) and birational invariants (12:42-50) — SA05-9, SA05-14

**What he does.** 12:42: the coniveau spectral sequence E_1^(pq) = ⊕_(x in X[p]) H^(q-p)(x, Q_l(-p)) => H^n should come
from motives (from E_2, or with ind-motives); the coniveau >= p part is "visiblement de type dimensionnel <= n - 2p", and
"on veut que ce soit exactement" the part of that type, for X projective ("penser à X de dim 1!"). 12:43-45: L(K), the
group of schemes of finite type over K modulo cut and paste (the Grothendieck ring of varieties), and
sigma: L(K) -> M^+(K), cl(X) -> sum (-1)^i cl H^i_!(X), giving Serre's virtual Betti numbers; the dimension filtration
gives gr_n L(K) -> Z^(sigma_n ∪ xi sigma_(n-1) ∪ ...). 12:46-48: the birational invariants gamma_i(X): the part of level
exactly i of H^i(X), equivalently the image of H^i(X) in lim_U H^i(U); H^i(X) -> H^i(U) injective mod D_(i-2), bijective
mod D_(i-1); gamma^i(X) is functorial, injective for dominant maps. 12:48-50: questions: do homs of the gamma's come
from embeddings into purely transcendental extensions; Ex. 1) curves C, C' with J -> J' of finite kernel: is there a
dominant C' x P^N ⇢ C?; 2) gamma^i(R) = 0 for i > 0 => R unirational?; is gr_n L(K) modulo ruled classes = Z^(sigma_n)?;
gamma_n(X) = 0 => X ruled? "Pour une surface: si la cohomologie H^2 est algébrique, la surface est-elle réglée ??",
margin "Non en car. p > 0, prendre E x E avec E d'invariant de Hasse nul."

**What I checked** (events 39-42). sigma is additive (long exact sequence of H_c) and multiplicative (Künneth): it is the
motivic measure of K_0(Var_K) (Gillet-Soulé 1996; Guillén-Navarro Aznar 2002; locators unverified). H^i(X) -> H^i(U):
kernel supported on X - U (coniveau 1, type <= i - 2), cokernel in H^(i+1)_Z(X) ≅ H^(i-1)(Z~)(-1) (type <= i - 1):
right; injectivity for dominant maps: right (multisection argument). The coniveau statement of 12:42 is Grothendieck's
generalized Hodge conjecture in motivic form (open); "exactement le morceau de type dimensionnel n - p" must read
n - 2p (his previous line; not decided on the ink). His margin E x E: right (a supersingular abelian surface has
rho = 6 = b_2 and is not ruled).

**His questions answered (no).**
- Ex. 1 (12:49): yes for g(C) <= 1 (C' -> J' -> E through the dual surjection), no for g(C) >= 2: a dominant
  C' x P^N ⇢ C factors through C' (the P^N-fibres map to points), so it forces a dominant C' -> C; for C ≇ C' of the
  same genus g >= 2 with isogenous (even isomorphic) Jacobians, Riemann-Hurwitz forces degree 1, a contradiction. Such
  pairs exist (non-isomorphic genus-2 curves with isomorphic Jacobians: Hayashida-Nishi 1965; locator unverified).
- Ex. 2 and 12:50 in characteristic 0: Enriques surfaces (q = p_g = 0, H^2 algebraic, Kodaira dimension 0) have
  gamma^i = 0 for all i > 0 and are neither ruled nor unirational; bielliptic surfaces and surfaces of general type with
  p_g = q = 0 (Godeaux, Barlow) also have H^2 algebraic without being ruled.
- "gr_n L(K) modulo the ruled subgroup = Z^(sigma_n)?": no. Larsen-Lunts (Mosc. Math. J. 3, 2003): K_0(Var_K)/(L) is
  free on the stable birational classes (characteristic 0; locator unverified), and gamma_2 does not separate an
  Enriques surface from a ruled surface.

## Hunches

- **H1 (dating, cote 11).** His correspondence pages are written on the backs of a pre-publication typescript of
  Mumford's GIT (published 1965): 1964-65 or later.
- **H2 (Frobenius algebras).** His special simplicial bivariant algebras (11:38, 11:42) are symmetric monoidal functors
  on finite sets with push and pull, and a Poincaré algebra is a commutative Frobenius algebra; the axioms he leaves open
  on Delta are the Frobenius axioms. H^*(X^.) satisfies base change only for product squares: Frobenius, not "special"
  in Lack's sense (mu delta = chi times the point class, not 1). Literature: Abrams (1996) for 2D TQFTs; Lack, Composing
  PROPs, TAC 13 (2004), cospans of finite sets and special Frobenius algebras (locators unverified). Michel Hua's project
  lists "Frobenius algebra" among its keywords.
- **H3 (exchange).** The exchange axiom his 11:3, 11:31 and 11:46 circle is transversality; with multiplicities or excess
  it is the refined Gysin formalism (Fulton, ch. 6). His question of 11:31 has a one-line counterexample (tangent line to a
  conic).
- **H4 (tautological rings).** His 11:51-57 computes the subring of H^*(X^k) generated by the point class and the
  diagonals. The relation M = 0 of item 6 (curves, surfaces with b_1 = 0) is the cohomological shadow of the Gross-Schoen
  modified diagonal (curves) and the Beauville-Voisin relation (K3); in Chow, with a canonical 0-cycle for y, this is the
  Beauville-Voisin and Voisin conjecture on tautological rings of powers (Yin, 2015, for K3; locators unverified). A
  page of 1964-68 that writes down the cohomological tautological relations of X^3 is worth a note in the companion.
- **H5 (dating, cote 12).** The IHES letterhead with "91" dates 12:9 (and the Esquisse with it) to 1968 or later.
- **H6 (birational motives).** 12:43-50 is the programme of the motivic measure of K_0(Var) and of birational motives:
  his gamma^i are the birational motives of Kahn-Sujatha (locator unverified); his questions are answered by Enriques
  surfaces and Larsen-Lunts (item 10).

## Dependencies

- SA05-1 (11:3-15) is used by items 2-6 (all of cote 11) and by SA05-12 (12:2 §5: motives from correspondences).
- 11:23 (A_sp, the algebraic classes) and 11:40-57 (stable systems, tautological subrings) use SA05-1 and feed SA05-12.
- 11:44 and 12:2 §5 meet SA05-2 through conjecture D (hom = num); 12:41 uses SA05-11 (polarizations).
- Item 7 is the frame of SA05-8 (motivic Galois group) and of SA05-18 (12:13: G over F_q commutative, Ẑ by a protorus;
  15:3-14); 12:7 cites Serre's supersingular argument, as 15:11 does. Item 8 uses SA05-9 (weights) and is SA05-21's
  Mumford-Tate group. Items 9-10 are SA05-9 (weights, levels) and SA05-10 (absolute cohomology, in the 12:21 plan).
- Items 9-10 need resolution of singularities as he says (12:4, 11:23); de Jong's alterations replace it with Q
  coefficients.

## Deliverable state

- Passes: Pro transcription (GPT-6 Astra, ChatGPT Pro mode) of every page; Work second readings K11-01 to K11-04 and
  K12-01 to K12-03 (GPT-6.2 Astra at reasoning effort max, ChatGPT Work), blind; Michel Hua's project's modern
  readings of cotes 11 and 12; this sweep-3 reading.
- Corrections to apply: the rows of `c15b_c12_c11_part1_CORRECTIONS.tsv` (his slips noted in the edition's apparatus,
  three readings changed: 11:5, 11:13, 11:17, plus 11:29's unfinished exponent and 11:51's struck delta).
- Open readings: 11:5 whether the sign factor is struck; 11:29 the boxed operator "[(-1)^B]_(B')"; 11:36 two
  notational lines; 12:27 "Z_S", 12:28 "Q(+1)", 12:42 "n - p" (not decided on the ink). The K12-01 to K12-03 witnesses
  I did not compare (budget).
- Ready to be edited as a transcription edition: cote 11 scans 2-58, yes, with the corrections; cote 12 scans 2-50,
  yes, after the three open readings of 12:27-42 are looked at on the ink.

