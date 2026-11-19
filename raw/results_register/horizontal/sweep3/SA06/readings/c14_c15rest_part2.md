# SA06, cote 14, scans 59-132: sweep 3 reading (sub-stretch c14_c15rest_part2)

Claude Opus 5.5 at effort max, `c14_c15rest_part2`, sweep 3 reader, launched by `c14_c15rest` (Claude Opus 5.5 at effort
max) at the word of agent a28ea31fa17dd65e1 (Claude Opus 5.5 at effort max); started 19 Nov 2026. Written as the reading
goes, page by page.

Witnesses. Scans 59-86: Codex web `K14-05` (59-71, 73) and `K14-06` (74-86) are the only text (no Pro transcription).
Scans 87-132: the Pro package `MPL_14_087-132` is the text; Codex web `K14-07`, `K14-08`, `K14-09` are the second witness.
Blank scans, not read (ink measured): 72, 105, 110, 119, 125, 130. Michel Hua's project
(`transcripts/14/14.modern.tex`; his page p = our scan p + 1) is used as a credited witness only.

## Items, in page order

### 1. SA06-3 (later part): § 2 « Application à l'algébricité de certains homomorphismes de V.A. ou d'espaces de cohomologie l-adiques », 14:59-71 (text: K14-05)

**Places.** The numbered text begins on 14:52 (« 1. Un lemme de théorie des intersections », Th. 1.1 to Rem. 1.8, read by
part 1) and § 2 begins on 14:58 (Prop. 2.1, statement). In my stretch: 14:59 end of 2.1 and its cohomological square;
14:59-61 proof and « Variante »; 14:61 a crossed-out « Corollaire 2.2 »; 14:62 Cor. 2.2 (transposition) and Prop. 2.3
(bracketed, margin « devrait remonter au N°1 »); 14:62-64 Prop. 2.4; 14:64-65 Cor. 2.5; 14:65-68 Cor. 2.6 (margin
« Th ? »); 14:68-70 Prop. 2.7; 14:71 « Questions ». Pencil sheet numbers 58-70 on scans 59-71 (sheet = scan - 1).

**What he does.** X, Y smooth projective connected over k algebraically closed, of dimensions n and m; A = Albanese,
B = Pic^00 (the reduced Picard variety), A_X = B_X^*. A 1-cycle z on X x Y gives u_Z: B_X -> A_Y with
u(cl D) = S_Y(tZ(D)) for D algebraically equivalent to 0 on X with tZ(D) defined; cohomologically u^(1) corresponds to
psi_X a(gamma(z)) phi_Y^(1), with phi_Y: H^1(A_Y) -> H^1(Y) and psi_X: H^(2n-1)(X)(n-1) -> H^1(B_X) (the action of the
Poincaré divisor). Construction (14:60): C = pi_*((1_Y x Theta).(z x 1_B)) in Z^m(Y x B_X), z(Theta(b)) = C(b), and
Th. 1.1 applied to C gives u(b) = S_Y(z(Theta(b))). Variante (14:61): u_Z is the divisorial correspondence
Theta_Y o Z o tTheta_X on B_X x B_Y (the display after it is left as « ... - »). Cor. 2.2 (14:62): t(u_Z) = u_(tZ).
Prop. 2.3 (14:62, bracketed): in the setting of 1.1, t(u_Z): B_X -> B_Y sends cl(D) to cl(tZ(D)); N.B. this should give
another proof of 1.1 through a morphism Pic_(X/k) -> Pic_(Y/k). Prop. 2.4 (14:62-64): a(gamma(z)): H^1(Y,Q_l) ->
H^(2n-1)(X,Q_l)(n-1) is an isomorphism iff u_Z is an isogeny; its inverse is then a(t gamma(D)) for a unique D in
Cl(X,Y) (x) Q, which defines u_Z^(-1); D can be integral iff u is an isomorphism; if Ker u (as a group scheme) has order N,
D = N^(-r) D_0 with D_0 integral, but not M^(-r) D_0 when M misses a prime divisor of N. Cor. 2.5 (14:64-65): the integral
version: u is an isogeny of degree prime to l iff H^1(Y,Z_l) -> H^(2n-1)(X,Z_l)(n-1)/torsion is bijective, and
H^(2n-1)(X,Z_l) is moreover torsion-free iff the map itself is bijective. Cor. 2.6 (14:65-68): for ample classes
zeta_1, ..., zeta_(n-1), cup product with eta = zeta_1...zeta_(n-1): H^1(X,Q_l) -> H^(2n-1)(X,Q_l)(n-1) is an isomorphism,
and its inverse is given by a unique element of Cl(X,X) (x) Q, independent of l. The proof goes through a curve
v: C -> X: u = v_* o (duality) o v^*, and (i) polarization <=> (ii) isogeny <=> (iii) v^* has finite kernel <=> (iv)
v_*: A_C -> A_X is surjective, the last « bien connu » for a general complete-intersection curve. Prop. 2.7 (14:68-70),
the other direction: D in A^1(X x Y) with u_D: A_Y -> B_X an isogeny gives a Q-1-cycle Z inverting a(gamma(D)), with
u_Z = u_D^(-1); proof by the squares of 14:69-70 (mu = psi_X lambda phi_X, psi_X^(-1) = lambda phi_X mu^(-1),
phi_X^(-1) = mu^(-1) psi_X lambda, mu being H^1 of the isogeny of 2.6). Questions (14:71): 1) is there always an INTEGRAL
cycle inverting H^1(A_X) -> H^1(X)? It would suffice that, for N large, the generic fibre of Sym^N(X) -> A_X have a
rational point; 2) is there always an integral cycle inverting H^(2n-1)(X)(n-1) -> H^1(B_X)? If 1) is yes, it suffices to
answer 2) for abelian varieties.

**What is proved.** 2.1 (given 1.1, 1.6, 1.7), 2.2 (« par voie cohomologique », not written out), 2.4, 2.5, 2.6 and 2.7 are
proved on the pages, up to standard facts he cites (« bien connu »: surjectivity of A_C -> A_X; intersection theory).
2.3 is only stated (« Vérification de 2.3. par AQT », the abbreviation unresolved). The crossed-out Cor. 2.2 of 14:61
(« Tout homomorphisme B_X -> A_Y est défini par un Z_1 in Cyc_1(X x Y) ») is not claimed: over Q it follows from 2.6-2.7
together with divisorial correspondences; integrally it is the kind of statement the Questions of 14:71 leave open.

**What I checked** (check events in the TSV). The construction and dimension count of 14:60; the numerical invariance of
14:61 (projection formula, then 1.1, whose own numerical invariance rests on divisors: numerical implies algebraic up to
torsion, Matsusaka, and Hom is torsion-free); Cor. 2.2 on an example (X = Y = E elliptic, Z the graph of alpha:
u_Z = alpha o lambda^(-1), t(u_Z) = alpha^dagger o lambda^(-1) = u_(tZ), since S(alpha^*([P]-[0])) = alpha^dagger(P);
no sign in Mumford's normalization); Prop. 2.4 including the denominators (an isogeny u of degree N has v with
v o u = [N]; M^r u^(-1) is a homomorphism iff Ker u is killed by M^r); Cor. 2.5 with Z_l coefficients using the sheet 14:73
(phi_Y is an isomorphism over Z_l, psi_X is onto with kernel (NS(X){l})^dual); Cor. 2.6 by an independent argument
(u = g^dual o delta o g with g = v^*, delta the Abel-Jacobi isomorphism of the curve, which is minus a principal
polarization, so u = -phi_(g^*M) is an isogeny iff g has finite kernel); the inverse formulas of 2.7; the sufficiency in
Question 1 and the reduction in Question 2.

**What is wrong.**
- 14:59, proof of 2.1: « psi_X a(gamma(z)) phi_X^(1) » (the ink has phi_X) must be phi_Y^(1): the composite starts at
  H^1(A_Y), as the square on the same page shows (author's slip; Codex S1).
- 14:63, end of 2.4: « diviseurs premiers de n » (a small n in the ink): read N = card Ker u.
- 14:64, insertion « le meilleur dénominateur possible étant donné par card Ker u »: the least denominator is the exponent
  of the group scheme Ker u (u = [2] on a g-dimensional abelian variety, char != 2: order 2^(2g), denominator 2).
  card Ker u is a possible denominator with the same prime factors, so his final clause (« ne peut être meilleur qu'une
  puissance de N », the primes of N) stands. Michel Hua's project notes the same (« le meilleur est l'exposant »).
- 14:67, (i) « L'hom B_X -> A_X = B_X^* est un hom de polarisation »: true up to a universal sign. With the identification
  Pic^0(C) -> Alb(C) of 2.1 (cl D -> S_C(D)), u_Delta for a curve is minus the principal polarization in Mumford's
  normalization (on an elliptic curve, x -> O(x - 0) is -phi_(O(0))). The equivalences (i)-(iv) hold with « u or -u is a
  polarization »; his own margin « Attention aux signes éventuels ! » (14:62) covers it.
- 14:65, Cor. 2.5: « il suffit » can be « il faut et il suffit » (given the first condition); not an error.

**What is open.** The two Questions of 14:71 (hunches c14b-H1, c14b-H2); « AQT » on 14:62.

**Readings decided on the scan** (Codex web K14-05 is the only text). 14:59: phi_X^(1) in the ink (above). 14:62:
« Corollaire 2.? » is 2.2 (renumbered after the crossed-out 2.2 of 14:61); « par AQT »: three capitals, the first retraced,
expansion unknown. 14:63: « de n ». 14:64: the boxed insertion « étant donné par card Ker u ». 14:65 margin: « Th ? C'est
un cas particulier important du "Lefschetz vach..." donnant Lefschetz des surfaces... »; the adjective's ending is not
resolved (Codex « vache(?) », Michel Hua's project « vachement »); the sense is hard Lefschetz, and for n = 2 Cor. 2.6 is
the whole hard Lefschetz theorem of a surface (the only non-trivial degree is H^1 -> H^3). 14:71: « pour n [grand, struck]
convenable (donc n grand) ».

### 2. The sheet 14:73 (with the blank verso 14:72): Kummer, Néron-Severi torsion and H^(2n-1) (SA06-3, preliminaries)

**What he does.** X proper over k separably closed, N and l prime to the characteristic: H^1(X, mu_N) = Pic(X)[N],
0 -> Pic^0(X)[N] -> H^1(X, mu_N) -> NS(X)[N] -> 0, H^1(X, Z_l(1)) = T_l(Pic^0) (using that Pic^tau/Pic^0 is finite);
for X normal, B_X = Pic^00, A_X = B_X^*, phi_X^*: H^1(A_X, Z_l) -> H^1(X, Z_l). For X smooth of pure dimension n,
Poincaré duality gives 0 -> (NS(X)[N])^dual -> H^(2n-1)(X, Z/N) -> A_X[N](-n) = H^1(B_X, Z/N)(1-n) -> 0 and, in the
limit, 0 -> (NS(X){l})^dual -> H^(2n-1)(X, Z_l)(n-1) -> H^1(B_X, Z_l) -> 0, the last arrow a « hom algébrique » (psi_X).

**Checked.** All of it, including the twists (computation in the TSV): dualizing the Kummer sequence gives
H^(2n-1)(X, Z/N) = H^1(X, mu_N)^dual(1-n), and (B_X[N])^dual = A_X[N](-1) by the Weil pairing. phi_X^* is an isomorphism
over Z_l, not only « mod torsion » as 14:56 and 14:59 say (A_X^dual = Pic^0_red). The limit sequence as written is right.

**Wrong (minor).** At finite level the Néron-Severi term needs the twist (1-n): (NS(X)[N])^dual(1-n). He struck a « (-n) »
there and left the term untwisted; over a separably closed field the twist is invisible.

**Role.** This sheet supplies the « isom mod torsion » and the exact torsion of H^(2n-1)(X, Z_l) used in 2.1 and 2.4-2.5.
Michel Hua's project reads it with the next sheet (our 14:74) as « Deux feuillets : Picard, Albanese et cohomologie
entière ».

### 3. SA06-3: « Relations entre Alb^0_X, Pic^00_X et H^1(X), H^(2n-1)(X) », 14:74 (text: K14-06)

**What he does.** X smooth projective connected of dimension n over k algebraically closed. Four comparisons, each
« à torsion près »: pi_1^l(Alb) <- pi_1(X)^ab(l) <- H^(2n-1)(X)(n) [« c'est tjrs surjectif ? »];
pi_1(Pic^00) = H^1(Alb)(1) -> H^1(X)(1) [« c'est tjrs injectif »]; H^1(Alb) -> H^1(X) [« tjrs injectif »];
H^1(Pic^00) = pi_1(Alb)(-1) <- H^(2n-1)(X)(n-1). Summary: representing abelian varieties by their H^1, Alb_X corresponds to
H^1(X) and Pic_X to H^(2n-1)(X)(n-1).

**Checked** (TSV). H^(2n-1)(X, Z_l)(n) = pi_1(X)^ab (x) Z_l exactly (Poincaré duality against H^1(X, Q_l/Z_l)), and
pi_1(X)^ab (x) Z_l -> T_l(Alb_X) is onto with finite kernel. The question « c'est tjrs surjectif ? » has the answer yes: a
connected étale isogeny of Alb_X pulls back to a connected cover of X, otherwise the Albanese map would lift through it
(Michel Hua's project gives the same answer). H^1(Alb) -> H^1(X) is even an isomorphism over Z_l; T_l(Pic^00) =
H^1(Alb)(1) and H^1(Pic^00) = T_l(Alb)(-1) are the Weil pairing. Nothing wrong on the page.

### 4. SA06-3: an axiomatics of abelian varieties up to isogeny, 14:76, 78, 80-81, 83, 85 (text: K14-06)

**Places.** Handwritten on the backs of reused typescripts (14:75, 77, 79, 82, 84, 86, below), in scan order 76, 78, 80, 81,
83, 85; parts « I ① ② ③ » (76), « ① ② » (78), « 3) » (80). It continues on 14:87 and 14:89 (item 6).

**What he does.** 14:76: VA, the additive category of abelian varieties over k algebraically closed; the duality functor
A -> A^*; the contravariant functor A -> C^*(A) to graded commutative rings (cycles modulo algebraic equivalence),
C^0 = Z; dimension, additive and invariant under duality; C^n(A) = Z, « isom can, mais pas fonctoriel sauf pour isom. »;
the covariant law and the projection formula (containing the transposition formula), from which the Pontryagin product
follows formally; « Application fondamentale »: C^1(A) -> Hom(A, A^*)^alt, through C^1(A x A); N.B. « On pourrait définir
axiomatiqmt A^* par cette formule »: C^1(A x B)/(C^1(A) x C^1(B)) = Hom(A, B^*). 14:78: the faithful additive functors
A -> T_l(A) (x) Q_l and A -> H^1(A, Q_l) = Hom(T(A), Q_l); H^*(A) = Lambda^* H^1(A); the square H^1(A^*) =
Hom(H^1(A), Q_l(-1)) (« carré comm. à isom près »); the cycle class gamma_A^(2i): C^i(A) -> H^(2i)(A)(i) =
Lambda^(2i) H^1 (i), compatible with products; the top-degree identifications eta_A: Lambda^(2n) H^1(A) = Q_l(-n) and its
dual for A^*, with « vérifier s'il n'y a pas un signe ! ». 14:80-85: for u between abelian varieties, the Gysin map
u_*: H^i(A) -> H^(i+2(n'-n))(A')(n'-n) defined by transposition; u_*(1_A) is the class of the image cycle, d times the
class of the image B (d = degree of A -> B), zero if u(A) has dimension < n; in terms of u_1 = T(u): T(A) -> T(A'), it is
the decomposable multivector obtained from Lambda^(2n) u_1, normalized by the determinant isomorphism
Lambda^(2n') H^1(A') = Lambda^(2n) H^1(A) (x) Lambda^(2(n'-n)) K (K = Ker(H^1(A') -> H^1(A))); with
H^i(A) = Lambda^(2n-i) T(A)(-n) (Poincaré duality), u_* is Lambda^(2n-i) u_1 (x) Q_l(-n); hence u_*(1) determines the image
of u_1 when u_1 is injective.

**What is proved.** Nothing is claimed beyond classical facts (Weil; NS(A x B) = NS(A) + NS(B) + Hom(A, B^dual);
NS(A) = symmetric homomorphisms A -> A^dual, whose Weil forms are alternating, hence « alt »; H^* = Lambda^* H^1). The
computation of u_* from T_l(u) on 14:83-85 is correct, except for one normalization (below).

**Checked** (TSV). 14:76 statements against the classical theory; the square of 14:78; on 14:80-85 the Gysin
identification u_* = Lambda^(2n-i) u_1 (x) Q_l(-n) on A x 0 in A x E and on [m] of an elliptic curve; the normalization of
14:83 (refuted, below).

**What is wrong.**
- 14:80, « 3) Soit u: A' -> A ... définissant u_*: H^*(A) -> H^*(A') par transposition ... u_*(1_A) = d.1_A' »: with
  u: A' -> A the transpose of u^(2n) goes from H^*(A') to H^*(A) (u_*(1_A') = d.1_A). The rest of 14:80-85 uses
  u: A -> A' (u^1: H^1(A') -> H^1(A), u_1: T(A) -> T(A')): read u: A -> A' from the start (u^(2n): H^(2n)(A') -> H^(2n)(A),
  zero iff u(A) != A').
- 14:81, « la classe du cycle image u(A) in C^(n'-n)(A) »: in C^(n'-n)(A').
- 14:83, « la classe caractéristique de H^(2n)(A)(n) fois la classe cherchée u_*(1_A) ... corresponde d fois [underlined]
  la classe caractéristique de H^(2n')(A')(n') »: refuted; the factor is 1. In the same-dimension case the determinant
  isomorphism is Lambda^(2n) u^*, which sends the point class of A' to d times the point class of A (14:80 itself), so
  [pt_A] (x) u_*(1_A) = [pt_A] (x) d corresponds to [pt_A'], not to d [pt_A']; in general [pt_A] (x) d gamma(B) corresponds
  to [pt_A'] (projection formula). With « d fois » one would get u_*(1_A) = d^2 gamma(B), against 14:81 and against
  Lambda^(2n) u_1 on 14:85.
- 14:83, « N.B. d est aussi le contenu de T_Z_l(A) dans T_Z_l(A') »: only the l-primary part of d is the index of T_l(A)
  in its saturation; the prime-to-l part (and the inseparable part in characteristic p) is invisible to T_l.
- 14:83, last line « s'identifie : Lambda^(2n-1) u_1 (x) Q_l(-n) » (Codex reading): Lambda^(2n-i), as the square above it
  says.
- 14:85, « la connaissance de u_*(1) détermine l'image de u_1: T_l(A) -> T_l(A') »: true for the Q_l-image; over Z_l the
  class determines only the saturated image and the index d_l, not the image lattice.

**Open.** The sign of 14:78 (identification of the two top-degree classes through H^1(A^*) = H^1(A)^dual(-1)); it
depends on the sign convention of the Weil pairing and is not settled on the page.

### 5. Reused typescripts in 14:75-86 (SA06-11; not in sweep 2's page list for SA06-11)

- 14:75: English typescript, page « 7 »: cogroup structures on A = K[t] (counit, associativity (3.1)), showing
  m(t) = t (x) 1 + 1 (x) t + alpha t (x) t; a page of a paper on group objects/Hopf algebras, author not identified.
- 14:77 (« - 20 - »), 14:86 (« - 21 - »), 14:84 (« - 22 - »), 14:82 (« - 23 - »), 14:79 (« - 25 - »): French typescript
  on the cohomology of sites (Čech cohomology through covering sieves, forgetting the module structure, Prop. 3.1 and
  Def. 3.2 « C-acyclique », Prop. 3.3, Def. 3.5, « N° 3. Critères d'acyclicité »), citing (2.4.14.II) and (3.5.4.III):
  in content the material of SGA 4 Exposé V (Verdier) in an early numbering (identification by content; locator
  unverified). Not studied.

### 6. SA06-3: homomorphisms of abelian varieties and Néron-Severi groups, 14:87, 89 (text: MPL_14_087-132; second witness K14-07)

**What he does.** 14:87 « Relations entre hom. de V.A. et groupes de N.S. »: C^1(A) -> H^2(A)(1) = Lambda^2 H^1(A)(1) ->
Hom(H^1(A^*), H^1(A)) (« déduit de l'accouplement H^1(A) x H^1(A^*) -> Q_l(+1?) »), Hom(A, A^*) -> C^n(A x A^*) by the
« application "graphe" (pas additive!) », u-bar = (id, u): A -> A x A^*, its action on H^1(A x A^*) = H^1(A) + H^1(A^*)
by (id, u^1). 14:89: a homomorphism u: A -> B is known from the cohomology class of its graph, because that class
determines T_Q_l(Gamma) in T_Q_l(A x B) (14:85); likewise an abelian subvariety is known from its class;
C^1(A x B)/(C^1(A) x C^1(B)) = Hom(A, B^*) read in cohomology as Lambda^2(H^1(A) + H^1(B))(1) modulo the two factors =
H^1(A) (x) H^1(B)(1) = Hom(T_l(A), T_l(B^*)); then « Question Prouver que pour qu'une classe de H^1(A) (x) H^1(B)(1)
soit algébrique ... », cut off at the foot of the page.

**Checked.** The decomposition Lambda^2(V + W) = Lambda^2 V + V (x) W + Lambda^2 W and V (x) W(1) = Hom(T(A), T(B^*));
the determination of u by its graph class (a non-zero decomposable class determines its subspace; an abelian subvariety
is determined by its V_l). **Wrong:** the pairing H^1(A) x H^1(A^*) takes values in Q_l(-1), not Q_l(+1) (14:78 itself
writes H^1(A^*) = Hom(H^1(A), Q_l(-1)); the Pro reading carries a « (?) »; Michel Hua's project makes the same remark).
**Open:** the unfinished Question; over a finite field its natural completion (the Galois-invariant classes are
algebraic) is Tate's theorem for divisors on A x B (Tate 1966), over number fields Faltings (1983) (locators
unverified), see SA06-4.

### 7. SA06-3 / SA06-1: « Anneaux de classes de cycles sur une variété projective non singulière sur un corps k alg. clos », 14:91 (title sheet) and 14:92

**What is on the page** (decided on the scan image). A box « théorie discrète » with A_num, A_tau, A_alg and the two
homological rings A_(Q_l-hom), A_(Z_l-hom) (a first placement of the latter two is hatched out, with a balloon « car. 0 /
en remplaçant théorie sing. entière »); arrows A_tau -> A_num and A_tau -> A_(Q_l-hom) marked « ? ≃ », A_alg ->
A_(Z_l-hom) marked « ? ≃ » with a small circled mark (Pro « t0(?) »); braces « groupe libre de type fini ? » (A_num,
A_tau), « Groupe fini ? » (kernel of A_alg -> A_tau), « V.A. ? » (kernel of A_pic -> A_alg); a box « théorie continue »
with A_lin -> A_alb -> A_pic, each marked « ≃ ? », and « flèches toutes surjectives »; on the left G_alg K -> G_top K and
CK, « flèches qui sont des isom mod torsion »; margin « Autres équivalences : l'équivalence ... r et l'équivalence de Weil
wh(?) et W définis par Liebermann ..... ».

**Status of his questions** (known results, cited; the same assessment is in Michel Hua's project, credited): A_num is
free of finite type (yes); A_tau -> A_num and A_tau -> A_hom are not isomorphisms in general (Griffiths 1969); A_tau is
not of finite type, even (x) Q (Clemens 1983); A_lin -> A_alb is not an isomorphism for 0-cycles on surfaces with p_g > 0
(Mumford 1969); the kernel of A_pic -> A_alg is an abelian variety for divisors and 0-cycles, and in codimension 2 there
is Murre's algebraic representative (1985) (all locators unverified). The finiteness of the torsion of A_alg (« Groupe
fini ? ») is classical for divisors; in codimension >= 2 I know of results producing infinite torsion phenomena (Schoen;
Totaro 2016) but have not checked which statement they prove (locator unverified). The page asks; it proves nothing.

### 8. SA06-5: « Mumford-Nakai / Cycles algébriques amples », 14:93 (title sheet), 14:94-96, 98, 100

**What he does.** 14:94: « Th de Mumford-Nakai », X projective over a field, L invertible: a) ample <=> b) chi(F (x) L^n)
-> +infinity for every coherent F with dim supp >= 1 <=> b') the same for O_Z, Z integral of dim >= 1 <=> b'') for Z
integral of dimension 1 (resp. >= 2) some n_Z > 0 with chi(L^n (x) O_Z) >= 2 (resp. >= 1) <=> c), c'), c'') the same with
dim H^0; margins « Critère numérique (X irréd. de dim d): D.C > 0 si C courbe irréd., D^d > 0 (intersections calculées
dans CK(X)!) » and « N.B. le critère implique la condition d'amplitude de A. Weil ». 14:95: a) => b), c) « bien connu »;
the rest by induction on d through Lemma 1 (if L is ample on all integral subschemes of dimension < d, H^i(X, L^n) = 0
for i >= 2 and n >= n_0) and Lemma 2 (if moreover some L^n has a section, X -> P H^0(X, L^n) is everywhere defined and
non-constant for n >= n_0), both « cf lettre de Mumford »; Questions: can one drop the existence of a section in d), d')
(struck on 14:94)? can one drop projectivity? 14:96: for a surface, the cones P^+ (effective), Q^+ (x^2 >= 0, x.a >= 0),
R (ample) in NS: int Q^+ in P^+, hence by polarity (Q^+ self-dual) P^(+0) in Q^+; boxed: x in R <=> x.P > 0 and x^2 > 0
(Nakai); R = int(P^0), R-bar = P^0 (inside Q); Question « xP > 0 => x in R ? », reduced to a class with D^2 = 0, where
chi(nD) = chi(O) + n chi(D) and Mumford's h^0 >= chi force the linear coefficient to be negative. 14:98, 14:100: nef cones
P_i^(+0) in A^i and effective cones P_i^+ in A_i, alpha_i: A^i -> A_(d-i); Questions alpha_(d-1)(P_(d-1)^(+0)) in P_1^+ ?,
P_i^(+0).P_(d-i)^(+0) >= 0 ?, P_i^(+0) P_j^(+0) in P_(i+j)^(+0) ?; « D.C >= 0 => D^i X_i >= 0 ?? », settled for D^3 by
expanding (D' + nD)^3 with D' ample.

**Checked.** For curves over an algebraically closed field b'') and c'') say exactly deg(L|Z) > 0 (chi(O_Z) <= 1 and a
bundle of degree <= 0 on an integral curve has h^0 <= 1). The cone relations of 14:96 (Riemann-Roch for int Q^+ in P^+;
Hodge index for self-duality of Q^+; Nakai for R = int P^0): this is Kleiman's criterion for surfaces, derived from Nakai.
The cubic expansion of 14:100: D nef gives D' + nD ample for D' ample, so n^3 D^3 + O(n^2) > 0 and D^3 >= 0. The Pro
note P05's threefold (re-derived): on V = P_S(O + H) over Mumford's surface S with L strictly nef and L^2 = 0,
D = xi + pi^*L has D.C > 0 for every curve and D^3 = H^2 + 3 H.L > 0, but D^2.S_0 = L^2 = 0 on the section S_0.

**What is wrong.**
- 14:94 margin « Critère numérique: D.C > 0 ..., D^d > 0 »: for d >= 3 positivity on curves and on X does not give
  ampleness (the threefold above; Ramanujam's example, Hartshorne, Ample subvarieties 1970, I.10.8, locator unverified);
  Nakai's criterion needs (D|V)^(dim V) > 0 for every integral V. For d = 2 the margin is the criterion.
- 14:94 b''), c'') with the thresholds « >= 2 »: over a non-closed field false as stated (Pro note P02: P^1_C as an
  R-scheme, L = O); over an algebraically closed field the curve case is fine.
- 14:95, b'') => c''): b'') gives chi >= 1 at a single n_Z, while Lemma 1 controls H^i only for n >= n_0; the step needs
  chi(L^n (x) O_Z) >= 1 for some n >= n_0. Lemma 1 itself is attributed to Mumford's letter and not proved; what I can
  prove (the standard restriction argument) is that h^i(L^n) is eventually constant for i >= 2, which suffices for the
  chi -> infinity route of Nakai's proof but not for the lemma as stated.
**Open on the pages, settled since.** « xP > 0 => x in R ? »: no (Mumford's ruled surface: L.C > 0 for all curves,
L^2 = 0; Hartshorne 1970 I.10.6, locator unverified); his reduction (D^2 = 0 forces a non-positive linear coefficient,
i.e. D.K >= 0) is exactly the shape of Mumford's example (D.K = 2g - 2 > 0). « P_i^(+0).P_(d-i)^(+0) >= 0 ? » and the
product closure: no in general (Debarre-Ein-Lazarsfeld-Voisin 2011: nef classes of codimension 2 <= i <= n-2 on E^n, E with
complex multiplication, n >= 4, need not be pseudo-effective; Pro note P08). alpha_(d-1)(P_(d-1)^(+0)) in P_1^+-bar: yes,
as the dual of the pseudo-effective divisor cone is the closed movable cone of curves (Boucksom-Demailly-Paun-Peternell,
in characteristic 0; locator unverified). Pro note P06 records the parallel questions in his letter to Mumford of 31
August 1964, § 5, with Mumford's « NO ».

### 9. SA06-6: Lefschetz conjectures for algebraic cycles, global and local, 14:102-103, 106-109, 111-117 (and the cancelled remark 14:114)

**Places.** 14:102 title sheet « conjectures de Lefschetz pour cycles Algébriques: Extension aux Jac. inter., Conjectures
locales »; 14:103 a surface and its hyperplane section; 14:106-109 « Conjectures "Lefschetz" locales »; 14:111-113
« Conjectures "Lefschetz" » (global), 14:115-116 the checks for n = 2, 3, 4, 14:117 « Notations ». 14:114 is his own
cancelled remark (sweep 2 filed it among reused leaves).

**What he does.** Notation (14:111, 117): A^i_r = Chow groups, A^i_a = cycles modulo algebraic equivalence, A^i_tau modulo
tau-equivalence; J = A_r^a (algebraically trivial part), N = A_a, 0 -> J -> A -> N -> 0, M and I the primitive parts of
N and J; « Il ne semble pas qu'il y ait une définition raisonnable de la "partie primitive" de A^*(X) ». 14:103 (X a
surface, Y a smooth hyperplane section): NS(X) -> NS(Y) = Z onto mod finite, kernel of rank rho - 1; J^1(X) -> J^1(Y)
injective « exc. p »; the kernel K of Pic X -> Pic Y meets J^1(X) in a finite group, so is of finite type; K maps into
M^1(X) -> J^1(Y)/Im J^1(X) (« partie mobile »), and « en général » this is injective mod finite, so K is finite: « Je
présume qu'il en est ainsi si les positions limites de Y dans les pinceaux plans contenant Y sont des courbes
irréductibles ». Global (14:111-112), X^n smooth projective, Y a smooth hyperplane section: ① restriction
A_r^i(X) -> A_r^i(Y) bijective for 2i <= n-2, injective for 2i = n-1 (with A^tau, A_a, A_tau consequences), injective on
A^tau for 2i = n; ② Gysin A_i(Y) -> A_i(X) bijective for 2i <= n-3, surjective for 2i = n-2 (bijective on A_a), surjective
on A_tau for 2i = n-1; ③ hard Lefschetz: E^(n-2i): A_a^i -> A_a^(n-i) and E^(n-2i+1): A_r^i(X)^tau -> A_r^(n-i+1)(X)^tau
bijective mod finite groups, hence E^p: A_r^i -> A_r^(i+p) injective mod finite for p <= n-2i, surjective mod finite for
p >= n-2i+1; ②' for the affine U = X - Y, A_i(U) = 0 (2i <= n-2), A_i^a(U) = 0 (2i = n-1); ③' for the punctured affine cone
E over X, finiteness of A_r^i(E) for 2i >= n+2 and of A_a^i(E) for 2i >= n+1, with « On doit avoir » A_a^i(E) = M_a^i(X),
A_r^i(E)^a = I^i(X) mod finite in the complementary ranges. All marked « exc. p » with question marks. Local (14:106-109),
A strictly local noetherian, X = Spec A minus the closed point, Y = X ∩ V(f), both regular, U = X - Y, N the dimension:
vanishing mod finite of N^i, J^i, A^i in high degrees; restriction J^i, N^i, A^i(X) -> (Y) bijective / injective / zero in
ranges; A^i(X) -> A^i(U) iso mod finite; Problems: define intersection forms N^i(X) x N^i(X) -> Z, a theory of vanishing
cycles, a natural complement of J^1(X) in J^1(Y) with J^1(X) = J^1(Y)^pi; « Interpréter le th. de l'index de Hodge pour
les surfaces projectives en termes de la négativité d'une certaine forme définie sur N^1(X) »; N = 2: « N^1(X) fini :
c'est le th. de Mumford-Hodge ». The checks of 14:115-116 mark many rows « OK » and several « OK si équiv. rat. = équiv.
d'Albanese », others « ? », « question "intime" », « question "numérique" ». 14:114 (cancelled): for A complete local with
equidimensional components and U = S_f, « cd U <= dim A », with a reduction to a finite extension of k[[t_1..t_n]].

**Checked** (TSV). The surface case of 14:103 (kernel rank rho - 1; injectivity of Pic^0 up to p-torsion by Lefschetz for
H^1(-, mu_l)); his presumption tested on X = P^1 x P^1, Y a conic: there K = Z.O(1,-1) is infinite, but every pencil of
conics contains line pairs, so his irreducibility condition excludes this case, consistently. The divisor cases of ① are
the Grothendieck-Lefschetz theorems (SGA 2 XII; Pic(X) -> Pic(Y) injective for n >= 3, bijective for n >= 4) and the n = 3
rows of 14:115 marked OK are right (Pic^tau via H^1 and the torsion of H^2). The punctured cone: CH^i(E) =
coker(h: CH^(i-1)(X) -> CH^i(X)) (G_m-bundle). The generic logical test of 14:108 (N = 4, ②): J^1 bijective and N^1
injective give A^1 injective, not bijective (Pro note L07).

**What is wrong** (beyond the open conjectures).
- 14:112, ③ for A_a: « E^(n-2i): A_a^i -> A_a^(n-i) bijectif mod groupes finis » fails in characteristic 0: on a general
  quintic threefold (n = 3, i = 1) E.NS(X) has rank 1 while A_a^2 contains the Griffiths group, non-torsion (Griffiths
  1969) and of infinite rank (Clemens 1983). ③ for A_r (b), surjectivity of E: CH^1 -> CH^2 on a surface): fails on a K3
  (Pro note L11; Beauville-Voisin 2004). His own 14:115 leaves the n = 3 row « A_a^1 -E-> A_a^2 » without « OK ».
- 14:113, ③': the cone has dimension n+1, not « 2n+1 » (Pro and Codex both read 2n+1); A_r^2(E) is not finite for n = 2
  when p_g(X) > 0: for a smooth quartic K3 surface X, CH^2(E) = CH_0(X)/h.Pic(X) contains the degree-zero part of
  CH_0(X) (h.Pic(X) lies in Z.c_X by Beauville-Voisin), which is uncountable (Mumford).
- 14:113: « A_r^i(U) = A_r^i(X)/Im A_r^i(Y) » must have Im A_r^(i-1)(Y) (Gysin from a divisor; Pro note L12).
- 14:113: M_a^i = Ker(L^(n-2i): A_a^i -> A_a^(n-i)) and I^i = Ker(L^(n-2i+1): J^i -> J^(n-i+1)) are the kernels of the very
  maps ③ declares bijective mod finite, so they would be finite; the primitive parts are Ker L^(n-2i+1) on A_a^i (as for
  H^(2i)) and Ker L^(n-2i+2) on J^i (as for H^(2i-1)) (both witnesses agree on the exponents; Pro note L13 for M).
- 14:115, n = 2, ③ for the J-part: written « A_r^0(X)^tau -> A^2(X) » and « A_r^1(X)^tau -id-> A_r^1(X)^tau » (both witnesses):
  the formula of 14:112 gives E^3: A^0 -> A^3 = 0 and E^1: Pic^tau(X) -> CH_0(X)^tau; the latter is bijective mod finite iff
  rational and Albanese equivalence agree for 0-cycles on X (then it is the isogeny of Cor. 2.6, 14:65), so it fails for
  p_g > 0 (Mumford). The « id » row copies the A_a pattern.
- 14:115, n = 3, ②: « A_0^r(Y) -> A_0^r(X) bijectif ... O.K. » is right only under his marginal condition « si équiv. rat.
  = équiv. Alb. »: for X = P^3 and Y a smooth quartic, CH_0(P^3) = Z while CH_0(Y) is huge (Mumford). The same condition
  governs ②' (A_0(U) = 0) for n = 2, 3, 4, which fails for p_g > 0 (Bloch-Srinivas 1983: CH_0(X) supported on a divisor
  forces H^(n,0)(X) = 0; locator unverified).
- 14:114 (cancelled): « cd U <= dim A » needs a separably closed residue field (A = k[[t]], f = t: cd k((t)) = cd k + 1).
  For strictly henselian quasi-excellent A it is Gabber's affine Lefschetz theorem (Illusie-Laszlo-Orgogozo, Travaux de
  Gabber, Exp. XV; locator unverified).

**Open.** The Chow-theoretic Lefschetz statements ① and ② for codimension >= 2 with Q-coefficients modulo the
0-cycle/Albanese obstruction (a Bloch-Beilinson consequence; known for complete intersections of small degree,
Paranjape 1994; locator unverified); the local programme in its finite-group form; his problems (intersection forms on
N^i of punctured spectra, vanishing cycles, J^1(X) = J^1(Y)^pi).

### 10. SA06-7: boundedness, representability, zero-cycles and the generic member, 14:118, 120-121, 123, 126, 128, 131

**What he does.** 14:118: 1) numerically trivial cycles modulo rational equivalence are described by finitely many
algebraic families => num = tau and A_a^i(X) of finite type; 2) (x,y) - (x,b) - (a,y) + (a,b) « ~_a 0 »; 1) and 2) =>
the A_r^i(X)^a are abelian varieties, the products A_r^i(X)^a x A_r^j(Y)^a -> A_r^(i+j)(X x Y)^a vanish, A_0(X)^a = Alb(X),
and 2) <=> A_0(X x Y)^a = A_0(X)^a x A_0(Y)^a. 14:120: X projective, M in K(X): bounded families of locally free sheaves
(i) <=> (ii) quotients of O(-n)^N with Hilbert polynomials in a finite set <=> (iii) one fixed shift xi + gamma(A) by
quotients of one B; proofs, (ii) => (iii) unfinished. 14:121, 123: for M' in Z^i(X) (X smooth), (i) bounded, (ii)
numerically bounded with a fixed effective translate, (iii) (i-1)! zeta = c^i(xi) for a bounded M in K(X), (iv) M' in the
image of a bounded M in K^(i)(X), (v) numerically bounded; « équivalentes » struck, and 14:123 keeps (ii) => (i) <=> (iv)
=> (iii) => (v) (« R.R. » for the factor (i-1)!). 14:126: a chain 1°) products of algebraically trivial cycles vanish
<=> 1° bis) on X x Y => 2°) A_0(X)^a x A_0(Y)^a -> A_0(X x Y)^a zero <=> 2° bis) <=> 3°) the « rectangle » ~ 0 <=> 3° bis)
<=> 4°) on an abelian variety (x+y) - (x) - (y) + (0) ~ 0, i.e. x -> (x) - (0) is a homomorphism A -> A_0(A)^tau («
évid. surjectif ! ») <=> 4° bis) A_0(A)^a -> A is an isomorphism <=> 5°) for every X, A_0(X)^a -> Alb (written « Alb(A) »)
is an isomorphism; 6°) A_0(X x Y)^a = A_0(X)^a x A_0(Y)^a; a brace groups 2°-6° bis. 14:128: the proofs of 3 => 4 (push
forward by addition) and of the bijectivity of A -> A_0(A)^tau. 14:131: the generic member Y(y) of a family of
subvarieties parametrized by a rational S, with base locus C and the blow-up X' of C: boxed A(Y(y)) = Im A(X) + Im A(C),
i.e. A^i(Y(y)) = Im A^i(X) + Im A^(i-j)(C).

**Checked** (TSV). The relation in 2) on 14:118 is written « ~ » with a subscript « a » (decided on the scan); all its
consequences need rational equivalence (for algebraic or Albanese equivalence it is trivially true; Pro note Z02).
The chain of 14:126: 1° bis => 2° (top degrees), 2° <=> 3° (the classes x - a generate), 3° bis => 4° (push forward along
addition A x A -> A), 4° <=> 4° bis (Pro note Z04), 5° => 4° bis and 5° => 6° (Alb(X x Y) = Alb X x Alb Y). Not
justified on the page: 4° => 3° bis and 4° bis => 5° (a K3 surface has Alb = 0, so 4° bis says nothing about it).
14:120, (ii) => (iii): R = Ker(O(-n)^N -> G) is locally free and bounded, hence a quotient of O(-n')^(N') for one
(n', N'), and xi + gamma(O(-n)^N) = gamma(F + R) (as Pro note B02). 14:131 by an independent argument: the incidence
variety is a projective bundle over X - C, localization gives generation by CH(X) and CH(C x S), and
CH(C_k(S)) = CH(C) for S rational; the formula is for the generic member over k(S), not over its algebraic closure.

**What is wrong / settled since.** 1) is false: Mumford (1969) excludes a finite-dimensional parametrization of CH_0 of
a surface with p_g > 0 (Pro note Z01), Griffiths (1969) gives num != tau, Clemens (1983) A_a^2 not of finite type. 2)
modulo rational equivalence is false over C already for X = Y an elliptic curve (the Albanese kernel of E x E is non-zero
by Mumford and is generated by such rectangles, Bloch 1976; locators unverified); Grothendieck himself records this
failure in his letter of 20 November 1968 (Pro note Z03). Hence 4°, 4° bis, 5° fail over C for abelian surfaces; over
an algebraically closed field of transcendence degree 0 over the prime field they are Bloch-Beilinson-type conjectures.
14:126, 5°: the target is Alb(X). 14:121: K-equivalence is not defined in the dossier.

### 11. Reused leaves in 14:87-132 (SA06-11; one line each, not studied)

- 14:88 (« - 24 - », Prop. 3.4, C-acyclicity not intrinsic), 14:90 (« - 19 - », Cor. 2.5, Čech/Cartan-Leray spectral
  sequence): the same French typescript on cohomology of sites as 14:77-86.
- 14:97: a page of editorial comments on a draft of EGA 0_IV (« paragraphe Cohen », formally smooth algebras, fields of
  representatives, « ma rédaction », a suggested order of corollaries); 14:99: typescript « 0_IV Différentielles et
  dérivations » (Prop. 1.1, Déf. 1.2, Cor. 1.3: liftings over a square-zero extension form a torsor under Dér_A(B, J));
  14:101: Lemmas B and C of the same « Cohen » draft (E_(i,n), truncated symmetric algebras).
- 14:104: typescript page « - 115 - » of a draft on the dimension formula (Cor. 1-3, formulas (13), (14)), with his
  margins (« formule hybride, donner plutôt deux formules »).
- 14:122 (typed p. 3), 14:124 (typed p. 2): a typescript on group schemes (transporters, normalizers, representability,
  a tangent-space lemma) in the S.G.A.D. setting; 14:127 (p. 25, margin « Conserver le texte ci-contre, barré par
  erreur »), 14:129 (p. 24 bis): SGA 3 Exp. XIII § 3 material (generic Cartan subgroups, Lemma 3.4), identified by the
  Pro note F12.
- 14:132: rotated pencil fragments (x^2, x^3 - y^2, k[y], k[x,y]/xy) on IHÉS stationery.

## Hunches

- **c14b-H1 (14:71, Question 2; 14:61, crossed-out Cor. 2.2).** For an abelian variety A his Question 2 asks for an
  integral 1-cycle on A x A^dual inverting psi_A: H^(2g-1)(A)(g-1) -> H^1(A^dual), i.e. an integral algebraic
  representative of the Künneth component of the Fourier class c_1(P)^(2g-1)/(2g-1)!. For principally polarized A this is
  governed by the algebraicity of the minimal class theta^(g-1)/(g-1)! (cup with it is the integral inverse of the
  Lefschetz map H^1 -> H^(2g-1) for a unimodular polarization). That class is algebraic for Jacobians (Poincaré's formula)
  and open for a very general principally polarized A of dimension g >= 4; Beckmann-de Gaay Fortman (Compositio 2023)
  tie the integral Hodge conjecture for one-cycles on abelian varieties to it and to an integral Fourier transform
  (locator unverified). The l-adic question in characteristic p is the same problem. With his reduction (Q1 + Q2 for
  abelian varieties => Q2 for X, re-proved in the TSV), the dossier poses in 1964-65 a question that is still open, and the
  crossed-out Cor. 2.2 (« Tout homomorphisme B_X -> A_Y est défini par un Z_1 ») is its integral form. Links: SA18-14
  (cote 44, intermediate Jacobians), the integral Hodge conjecture literature (Voisin; Benoist-Ottem).
- **c14b-H2 (14:71, Question 1).** Question 1 is equivalent to: the tautological point of A_X over K = k(A_X) is the
  Albanese image of a degree-zero 0-cycle on X_K; equivalently 1 lies in the right ideal I of End(A_X) formed by the
  Albanese actions u_Gamma of correspondences Gamma from A_X to X (I contains v_* Hom(A_X, J(C)) for every curve
  v: C -> X, since every homomorphism to a Jacobian is a divisorial correspondence, and has finite index). The answer is
  yes for curves (Sym^N C a projective bundle, as Michel Hua's project notes) and for abelian varieties, and whenever some
  curve has J(C) -> A_X split; in general it is open to me. It connects with Wittenberg's work on Albanese torsors and 0-cycles
  of degree one (Math. Ann. 2008) and with Voisin's universal codimension-2 cycles (locators unverified), and inside the
  dossier with the cycle U that 14:32 says one cannot a priori find (Michel Hua's project's cross-reference).
- **c14b-H3 (14:52-71).** § 1-2 of this text is a complete l-adic proof, over any algebraically closed field, of the
  Lefschetz standard conjecture in degree 1 with both directions (Cor. 2.6 and Prop. 2.7: the inverses of
  H^1 -> H^(2n-1)(n-1) and of the comparison maps are Q-correspondences, unique and independent of l), together with
  the integral bookkeeping (Cor. 2.5, the exact denominators). The margin « Th ? » shows he meant to promote it; his letter
  to Serre (14:51, « Pour inverser phi_X, on utilise le th de Lefschetz et le cas particulier des V.A. qui est trivial »)
  announces exactly this. In the printed record this is the degree-1 case of B(X) attributed to the Albanese/Picard
  theory (Grothendieck, Standard conjectures, 1969; Kleiman 1968 and 1994; Lieberman 1968; locators unverified). Worth a
  dating check against the letter of 27 August 1965.
- **c14b-H4 (14:76-89).** The axiomatic sheets assemble the toolkit (duality, cycle rings with the projection formula and
  the Pontryagin product, H^* = Lambda^* H^1, the Gysin map as Lambda T_l(u), divisorial correspondences as Hom(A, B^*),
  homomorphisms determined by graph classes) that Lieberman (1968) used to prove the Lefschetz standard conjecture for
  abelian varieties and that Beauville and Deninger-Murre later organized through the Fourier transform. The unfinished
  « Question » of 14:89 is the divisor case of the Tate conjecture for A x B (SA06-4); if these sheets predate 1966,
  Tate's theorem answers his question over finite fields.
- **c14b-H5 (14:106-109, 14:113, 14:114).** The local programme reads the Hodge index theorem as a negativity statement
  on N^1 of a punctured spectrum (N = 3: for the cone over a surface Z, N^1 is NS(Z) modulo the hyperplane class, where the
  form is negative definite: the primitive Hodge index), with Mumford's negativity for surface singularities as N = 2.
  This is a local form of the standard conjecture of Hodge type; the cancelled 14:114 (local cohomological dimension) is
  the étale-cohomological input such a local Lefschetz theory needs, now Gabber's affine Lefschetz theorem. Testing the
  local finiteness claims on cones over surfaces with p_g > 0 should refute them as in ③' (14:113), through the local
  Chow groups of the vertex (Srinivas's work on cones; locator unverified).
- **c14b-H6 (14:111-117, 14:118, 14:126).** His conditionals « si équiv. rat. = équiv. d'Albanese » isolate exactly the
  0-cycle obstruction that Mumford (1969) and Bloch-Srinivas (1983) settled negatively over C; what survives of the global
  programme is its Q-form over number fields or modulo homological equivalence, i.e. Bloch-Beilinson (Chow-theoretic
  Lefschetz, Paranjape's connectivity for low degree) and the standard conjectures B and D (his « question numérique »).
  The open logical step on 14:126 (Albanese kernels of all X from those of abelian varieties) would follow from
  Kimura-O'Sullivan finite-dimensionality plus motivic Kuga-Satake-type statements for surfaces; I know no proof.
- **c14b-H7 (14:131).** The boxed formula for the generic member through a base locus C is the mechanism of later
  Noether-Lefschetz-type computations of Chow groups of generic hypersurface sections containing a subvariety; it is
  correct over k(S) and could serve as a lemma in an edition's commentary (locator of a printed form not searched).

## Dependencies (item ids from sweep2/SA06/WHAT_IS_WHERE.md; the page that shows each)

- SA06-3 (14:59-71) uses SA06-3's § 1: Th. 1.1, Th. 1.6, Cor. 1.7 (14:52-57; cited on 14:59 « En vertu de 1.7 », 14:60
  « On applique alors 1.1 », 14:61 « de 1.6 »), and the sheets 14:73-74 (the « isom mod torsion » of 14:59 and the torsion of
  H^(2n-1) used in Cor. 2.5).
- SA06-4 (letter to Serre) -> SA06-3: 14:51 announces the inversion of phi_X by Lefschetz and the abelian case, carried out on
  14:65-70.
- SA06-3 (Cor. 2.6, 14:65) -> SA06-6: the J-part of ③ on 14:112 for i = 1 (Pic^tau -> CH_0^tau via E^(n-1)) is Cor. 2.6
  once rational and Albanese equivalence agree (14:115-116 margins).
- SA06-3 (14:92 table of equivalences) -> SA06-6 and SA06-7: the rings A_r, A_a, A_tau, A_alb of 14:111, 14:117, 14:118 and
  14:126 are the rows of the table; SA06-1 (14:92) is the same page.
- SA06-7 (14:118: « les A_r^i(X)^a sont des V.A. ») -> SA06-6: the notation J^i on 14:103-117 presupposes it.
- SA06-5 (14:96 Hodge index, cones) -> SA06-6 (14:108: the Hodge index as negativity of a form on N^1).
- SA06-3 (14:71 Question 1) <-> SA06-3 (14:32, the cycle U; Michel Hua's project).
- Across topics: SA18-14 (cote 44, 44/002-009 per the Pro notes: abelian varieties P^i, a proposed num = tau, positivity of a
  divisor correspondence) for 14:92, 14:94-100 and 14:118; SA06-4 for the Question of 14:89 (Tate classes).
- SA06-11 (reused leaves): 14:75, 77, 79, 82, 84, 86, 88, 90, 97, 99, 101, 104, 122, 124, 127, 129, 132 (sweep 2's list
  lacks 75-86 and wrongly contains 114, which is his own cancelled remark).
- SA06-12 (planning answers): the Pro notes' M01-M14 read 14:87-117 against cote 16 questions; not used here beyond the
  notation safeguard L16 (N = A_a, not numerical). SA06-13: 14:91, 14:93, 14:102 are title sheets; 14:117 is a notation
  sheet.

## Deliverable state of scans 59-132

- **Passes.** 59-86: Codex web only (K14-05: 59-71, 73; K14-06: 74-86), each with its notes, math notes, doubts and audit;
  no Pro transcription, no second witness. 87-132: Pro `MPL_14_087-132` (frozen 15 Nov 2026, notes and doubts) and Codex
  web K14-07, K14-08, K14-09 as second witness. Blank: 72, 105, 110, 119, 125, 130. This reading (sweep 3) decided on the
  scan image: 14:59, 61, 62, 63, 64, 65, 71, 73, 80, 81, 83, 92, 118, 126 (targeted crops, not full collations).
- **Open readings.** 14:62 « AQT »; 14:65 the adjective after « Lefschetz » (« vache... »); 14:63 the left member « D_0 = »;
  14:83 « classe cherchée/dernière »; 14:92 the circled mark on A_alg -> A_(Z_l-hom) and the margin « l'équivalence ... r
  ... wh(?) et W définis par Liebermann »; 14:116 « intime(?) »; 14:126 « Alb(A) » (ink not checked); the Pro doubts file
  for 87-132 (not read in full).
- **Ready for a transcription edition?** 87-132: yes after merging the Pro doubts with the K14-07/08/09 readings (two
  witnesses exist) and adding the one-line identifications of the reused typescripts. 59-86: not yet: a single
  witness; the 13 handwritten pages (59-71, 73, 74, 76, 78, 80, 81, 83, 85) need a second full transcription pass before
  an edition; the reused typescripts (75, 77, 79, 82, 84, 86) need only identification lines.
- **For the companion.** The corrections filed here (24 rows across the stretch) are mathematical, not readings; the
  substantial ones are 14:83 (factor d), 14:112-113 (③, ③', primitive exponents), 14:115 (n = 2 indices), 14:118 and
  14:126 (the 0-cycle chain), 14:94-95 (the numerical criterion and b'').


## Counts

68 transcribed pages read (scans 59-132 less the blanks 72, 105, 110, 119, 125, 130; reused typescripts identified in one
line each); 41 check events; 24 corrections; 7 hunches (c14b-H1 to c14b-H7). Claude Opus 5.5 at effort max,
c14_c15rest_part2, 19 Nov 2026.
