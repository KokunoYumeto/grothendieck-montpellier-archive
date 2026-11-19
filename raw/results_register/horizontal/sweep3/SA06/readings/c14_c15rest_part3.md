# SA06 sweep 3, stretch c14_c15rest, part 3: cote 15, scans 87-95, 109-126, 138 and 170-206

Claude Opus 5.5 at effort max, c14_c15rest (launched by a28ea31fa17dd65e1, Claude Opus 5.5 at effort max), sweep 3
reader, 19 Nov 2026. Parts 1 and 2 (cote 14) are by the sub-readers c14_c15rest_part1 and c14_c15rest_part2 (both
Claude Opus 5.5 at effort max) and are merged into c14_c15rest.md.

**Witnesses.** 15:87-95 and 109-126, 138: Pro package MPL_15_087-138 (text), Codex web K15-03 (87-102), K15-04
(103-119), K15-05 (120-138) as second witness. 15:170-206: see the second block below. Blank (ink measured at 40 dpi,
same profile as the cote's other blanks): 15:116. P3-nn below is row nn of c14_c15rest_part3_CHECK_EVENTS.tsv. Scans 128-137 were read in sweep 3 (STUDY.md §§1-2); 15:96-108 too.

## A. 15:88-94 (his pages): Frobenius as a Zariski generator; compactness of Ker(epsilon) is the Riemann hypothesis (SA06-9)

The odd scans 87-95 are reused typescripts (section D). His pages are the even scans 88, 90, 92, 94. They come
straight after 15:84-86 (STUDY §2: the compact part of a commutative motivic Galois group) and before 15:96-106
(STUDY §1: the strong and weak conjectures on Frobenius eigenvalues), and they supply the frame that 15:100 uses.

- **15:88.** For an arbitrary band L, the coradical L' = corad(L) is commutative, gives a quotient gerbe with band L',
  i.e. an algebraic group H, and "ce qui précède" (15:84-86) gives (Ker(epsilon: H -> G_m))^0 a compact torus. Then the
  finite-field case: a category of motives with a tensor endomorphism of the identity that is "générateur"; L is then
  commutative, a group G of multiplicative type with an element f ("frobenius") generating G in the Zariski sense.
- **15:90.** The dictionary: (a) T of multiplicative type over Q with f in T(Q) generating T <=> (b) a subgroup M of
  Q̄* stable under Gal(Q̄/Q) => (c) a full subcategory of the Q-vector spaces with a semisimple endomorphism, stable
  under tensor product, sum and subobjects. A cocharacter j: G_m -> T is a Galois-invariant j*: M -> Z (a tensor
  grading); epsilon: T -> G_m with epsilon j(lambda) = lambda^alpha is a rank-1 object Lambda of degree alpha. Then
  (a) T^0/Im j compact => (b) there is q > 0 with |m| = q^(j*(m)/alpha) for all m in M <=> (c) on every object of
  degree i the eigenvalues of f have absolute value q^(i/alpha).
- **15:92.** Proof of (a) => (c): T_R^0 = U.S_R with U the maximal compact subtorus and S = Im j; f^nu = u j(x);
  eigenvalues of absolute value x^(i/nu); epsilon(f)^nu = x^alpha, so x^(i/nu) = q^(i/alpha). Then (margin "?") "on
  sait que a équivaut au fait que M est ... munissable d'une structure 'positive' du style motivique".
- **15:94.** With Q' the maximal totally real field of Q̄ (= 𝕂 of 15:128) and alpha = 2: (a) <=> every lambda in M
  has a power in Q'(i)* and lambda lambda-bar = q^(j*(lambda)). Cor.: if all conjugates of lambda have the same absolute
  value, some power lambda^r lies in Q'(i) (so the condition does not depend on the embedding). Proposition, for
  lambda in Q̄* and q > 0 rational, equivalent: (i) all conjugates have |lambda_alpha| = q^(i/2); (ii bis) a power
  lambda^n in Q'(i) with lambda^n times its conjugate = q^(in); (ii) lambda in Q'(i) and lambda lambda-bar = q^i; (iii)
  lambda is an eigenvalue of f in a representation of some (G, f, j, epsilon) with epsilon j(lambda) = lambda^2,
  Ker(epsilon) compact, epsilon(f) = q; (iv) a commutative Q-algebra with positive involution ("algèbre de Riemann"),
  f f' = q^i, and a Q-homomorphism to Q̄ sending f to lambda. Margin: a real such lambda is totally real and
  lambda = (q^(1/2))^i, "cas trivial".

**What is proved, and what I checked** (check events P3-01 to P3-08):
- (a) <=> (b) of 15:90 (re-proved): a Q-point f is a Galois-equivariant map X*(T) -> Q̄*; f generates T iff that map
  is injective; its image is M. (b) => (c): Rep_Q(T) is the category of pairs (E, phi) with phi semisimple and
  eigenvalues in M; morphisms commuting with f commute with T because f is Zariski-dense. The converse (c) => (b)
  needs the subcategory to be stable under duals too (otherwise the eigenvalues form only a monoid); his arrow is
  marked doubtful in both witnesses.
- (b) <=> (c) and (a) => (c) as on 15:92 (re-proved; T_R^0 = U.S_R holds because the maximal split subtorus maps to
  the anisotropic T^0/S, so lies in S_R, and S is not in U since epsilon j is not trivial). The absolute values are
  |x| and q = |epsilon(f)|.
- The converse (b) => (a), which 15:94 uses ("La condition a équivaut à"), re-proved: for weight-0 characters m every
  conjugate has |m| = 1, so every complex conjugation acts by -1 on X*(T^0/S) (x) Q, which is R-anisotropy.
- The Cor. of 15:94 (re-proved): if t = |lambda|^2 for all conjugates, |N(lambda)| = t^(d/2) with d = [Q(lambda):Q], so
  t^d is rational and lambda^d is a Weil number in the sense of 15:131 (STUDY §1), hence in Q'(i). A power is needed:
  lambda = 2^(1/4) has all conjugates of absolute value 2^(1/4), |lambda|^2 = sqrt 2 is irrational, lambda^4 = 2.
- The Proposition of 15:94 (re-proved): (i) <=> (ii) is 15:131-132; (ii bis) => (i) because complex conjugation is
  central on Q'(i); (iii) => (i) is the 15:92 argument (Ker(epsilon)^0 compact <=> G^0/Im j compact, since
  (Ker epsilon)^0 . Im j = G^0 with finite intersection); (i) => (iii) by taking M generated by the conjugates of lambda
  and q, j*(lambda_alpha) = i, j*(q) = 2 (well defined by taking absolute values), and this needs q != 1; (ii) <=> (iv)
  with A = Q(lambda) and complex conjugation (a commutative algebra with positive involution is a product of CM and
  totally real fields: STUDY §2).

**Wrong** (CORRECTIONS): the margin of 15:94 drops a sign: a real lambda is +-(q^(1/2))^i. In (iii), q = 1 must be
excluded. 15:92 writes x^(i/nu) for |x|^(i/nu). None of these affects the conclusions.

**Open.** 15:92's claim that (a) is equivalent to the existence of a "positive" structure of motivic type is marked
"?" by him; it is the existence of polarizations on a graded Tannakian category with commutative group, known in that
theory (Saavedra Rivano, Catégories tannakiennes, LNM 265, 1972, ch. VI; Deligne-Milne, Tannakian categories, LNM 900,
1982, §5; locators unverified). Status: known; 15:94 is the Weil-number half of the Honda-Tate frame (Tate, Sém.
Bourbaki 352, 1968; Milne, Motives over finite fields, 1994; locators unverified).

## B. 15:110-114 (his pages): the Weil-number torus G(q), the decomposition-field cocharacter and the norm-one torus G' (SA06-9)

- **15:110.** M(q) = the lambda in L (CM, Galois over Q) with lambda lambda-bar = q^i that are units away from p; M_0(q)
  (weight 0) mod torsion embeds in (Z^P)', P the primes of L over p (margin: M_0(q) = M_0(p)). Assume the primes of K
  over p split in L. A prime 𝔭 over p gives the linear form lambda -> v_𝔭(lambda), whose Galois conjugates "engendre
  M̌ mod torsion", hence a cocharacter nu_L: G_m,L -> G_L. With Gamma_𝔭 the decomposition group, L_0 = L^(Gamma_𝔭),
  K_0 = L_0 ∩ K: L_0 is the smallest field of definition of nu; the completion of L_0 at 𝔭_0 is that of "Z_ℓ" (ink);
  (L_0, 𝔭_0) is unique up to unique isomorphism (via the relative henselization of Z_(p)); L_0 is totally imaginary
  because tau𝔭 != 𝔭.
- **15:112.** (Z^P)' is the character group of G' = prod_(K_0/Q) U = Ker(prod_(L_0/Q) G_m -> prod_(K_0/Q) G_m), U the
  norm-one torus of L_0/K_0, so G'(Q) = Ker(N: L_0* -> K_0*); a homomorphism phi: G' -> G, an isogeny onto G^(0u);
  nu_(L_0) "se factorise par G'_(L_0)" via nu'. Inserted: "f_0 = f j(p^(1/2)) (de G^(0u)(Q))" lifts to G'(Q) only if
  phi is an isomorphism, i.e. M(q)/torsion = (Z^P)'.
- **15:114.** Margin "demander à Serre ?". It is not so in general, even (reading doubtful) for K_0 = Q: an example
  where Z/2 acts non-trivially on Pic(A), A the integers of L, suffices; Z/2 acts on Pic(A) "par symétrie", so Pic(A)
  not a 2-group suffices.

**Checked** (P3-09 to P3-15):
- (Z^P)' is the minus part {n : n_(tau𝔮) = -n_𝔮}: weight-0 elements have v_𝔮(u) + v_(tau𝔮)(u) = v_𝔮(u u-bar) = 0;
  the kernel of M_0(q) -> Z^P is the roots of unity (Kronecker). As a Galois module (Z^P)^- = Ind from
  Gamma_𝔭 x <tau> of Z with tau acting by -1, which is X*(R_(K_0/Q) R^1_(L_0/K_0) G_m): his G' is right
  ([L_0:K_0] = 2 because tau is central and not in Gamma_𝔭).
- The stabilizer of v_𝔭 is Gamma_𝔭 (the forms v_𝔮 are distinct on M(q) (x) Q because M_0 has finite index in
  (Z^P)^-, by 15:96); (L_0)_(𝔭_0) = Q_p because the decomposition field has e = f = 1 at 𝔭_0; L_0 is CM because tau
  is central and not in Gamma_𝔭. The Galois conjugates of v_𝔭 generate a subgroup of finite index of M̌ mod
  torsion, not always all of it (Pro note CM02b: cokernel Z/3 for Q(sqrt(-23)), p = 2).
- **15:110, "Z_ℓ": reading decided on the scan** (250 dpi): the subscript is his looped ℓ, in both witnesses; the
  mathematics needs Z_p (his slip, like the "2" for p of 15:40).
- **15:112, the inserted f_0: reading decided on the scan**: "= f j(p^(1/2))", exponent +1/2, base p. Its
  character value is epsilon(f j(p^(1/2))) = qp, not 1 (Pro note FR15), so it is not in G^(0u). The weight-zero
  Frobenius is f j(q^(-1/2)), which lies in G^(0u)(Q(sqrt q)); its square f^2 j(q^(-1)) lies in U(Q).
- The factorization of nu through G' is **refuted** (P3-13): epsilon∘phi is trivial while epsilon∘nu = v_𝔭(q) > 0.
  Refined statement: with psi(m) = (v_𝔮(m) - v_(tau𝔮)(m))_𝔮 (the map dual to phi) and nu'' the cocharacter
  n -> n_𝔭 of G', 2nu = phi∘nu'' + v_𝔭(q) j: only the weight-zero part of nu factors through G'.
- The lifting criterion (P3-14, re-proved): for the canonical weight-zero Frobenius point (the point of
  D(M_0/torsion) whose evaluation on M_0 is the inclusion), a lift f' in G'(Q) = Ker(N_(L_0/K_0)) evaluates (Z^P)^-
  into L*, each value a norm-one p-unit, hence in M_0(q), with divisor n; so every n in (Z^P)^- is a divisor of an
  element of M_0(q) and phi is an isomorphism. The necessity therefore holds, and it rests on M_0(q) being the full
  group of norm-one p-units of L, which answers the caution of Pro note FR16 (a bare isogeny such as 2: G_m -> G_m
  does have rational lifts).
- 15:114 (P3-15, re-proved): for L = L_0 imaginary quadratic and p = 𝔭 tau𝔭, the image of M_0 in (Z^P)^- = Z is
  the multiples of the order of [𝔭]^2; complex conjugation acts on Pic(A) by inversion, so non-trivial action means
  Pic(A) is not of exponent 2, and by Chebotarev some split p lies in a class of order > 2. His "Pic(A) not a
  2-group" is sufficient, not necessary (Z/4 also works). Example: Q(sqrt(-23)), p = 2, [𝔭] of order 3 (Pro FR14).
- The cokernel in general (P3-26, re-proved): for n in (Z^P)^- put 𝔞_n = prod 𝔮^(n_𝔮), so tau𝔞_n = 𝔞_n^(-1).
  n -> [𝔞_n] maps coker(M_0(q) -> (Z^P)^-) to Cl(L), with kernel inside E_K^+/N_(L/K)(E_L) (if 𝔞_n = (alpha),
  alpha alpha-bar is a totally positive unit e of K, and n is reached iff e is a relative norm of a unit; this group
  is killed by 2). So up to a 2-group the obstruction to lifting the Frobenius is the subgroup of Cl(L) generated by
  the classes of the minus-divisors at p, on which conjugation acts by inversion: the precise form of 15:114.

**Wrong** (CORRECTIONS): Z_ℓ for Z_p (110); f_0 (112); the factorization of nu (112); "engendre M̌ mod torsion"
(110, finite index only).

**Open.** None of his own beyond the "demander à Serre ?", which 15:114 answers. Status: known in substance as the
Weil-number torus with its p-adic (slope) cocharacter (Langlands-Rapoport, Shimuravarietäten und Gerben, 1987;
Milne 1994; locators unverified); his explicit norm-one torus G' and the class-group obstruction to lifting the
Frobenius are his own working of it.

## C. 15:117-125 (his pages): real fibre functors, polarizations, the finite-field cocharacter i (SA06-10)

(The Artin-Tate quotient of SA06-10 is on 15:135-137, read in STUDY §2; 15:138 is a reused errata sheet. On this
stretch SA06-10 is 15:117-125.)

- **15:117.** Margin: "N.B. On n'utilise que les éléments de structure 1, 2, 3" (the numbered "éléments de structure
  motiviques" of the cote-14 cover, 14:2: part 1 of this stretch). G connected over Q from a motivic situation M,
  U = Ker(G^0 -> G_m by epsilon). Proposition 1, equivalent: (i) U is a torus; (ii) epsilon is primitive in the
  characters of G^0; (iii) M_R has an ("unmodified") fibre functor, i.e. the gerbe 𝒢_R is not empty. Always so if M
  has even degrees (j(mu_2) = 1). Proposition 2, equivalent: (i) U = U^0 x mu_2; (ii) epsilon is a square;
  (iii) 𝒢_R is empty. Proofs: (i) => (ii) and (1 ii) <=> not (2 ii) from j with epsilon j(lambda) = lambda^2;
  (iii) => (ii) because odd-degree objects of M_R have even rank (fundamental alternating form); (i) => (iii) because
  H^2(R, T) = 0 for a compact torus T; even degrees give j = 2j', epsilon j' = id. Cor.: the even part M^pair (group
  G/j(mu_2)) has a real fibre functor.
- **15:119.** Cor. in the case of Prop. 2: "G^0 = U^0 x G_m, epsilon = pr_2, j(lambda) = inj_1(lambda)^2" (ink); the
  Tannakian structure of M_R is determined by G and the unique non-zero element of H^2(R, U) (from H^2(R, mu_2)); an
  object E of degree 1 and rank 2 generates an already R-twisted subcategory on which U^0 acts trivially. If 𝒢_R is
  not empty, its isomorphism classes form a torsor under H^1(R, U) = 2U(R) (non-canonically (Z/2)^(dim U)); each
  object gives a polarizing structure i_1: mu_2,C -> G^0_C with epsilon i_1 = id, i_1 i_1-bar = j, these form a torsor
  under 2U(R), and the map H^0(𝒢_R) -> Pol is equivariant, hence bijective (15:121: "se déterminent mutuellement").
- **15:121.** "À voir": do the automorphisms of (G^0_R, epsilon, j), of (G^0_Q, epsilon, j) or of (G, epsilon, j) act
  transitively on Pol(G)? Can a polarization, or a packet, be singled out? For motives over F_q, q = p^n: a
  distinguished conjugacy class of i: G_m,C -> G_C with i-bar i = j, epsilon i = id, given for commutative G
  (M in L CM) by lambda -> (1/n) v_𝔭(lambda), with "[v_p(lambda) v_p(lambda-bar) = v_p(lambda lambda-bar) = j*(lambda);
  v_p(q) = 1]". Boxed caveat: this form is not always integer-valued, "même sur le ss-groupe de M où j = 0" (reading
  of the Codex witness, which the ink supports), example q = p != 2, L = Q(sqrt(.)) (blotted) of class number 1,
  p = 3, 7, 11. Margin: i and its distinct conjugates (2n of them if [K:Q] = n) generate the cocharacters of G^0. An
  automorphism of G^0 respecting i is the identity; the effectivity structure of M, M_R, M_C is determined by i.
- **15:123.** Hence privileged classes of polarizing structures: the i|mu_2. The differences i - i' form "un
  sous-groupe d'indice fini de Hom(G_m,C, G^0_C)", but say nothing on the restrictions to mu_2 ("Question semble
  secondaire"); a packet of privileged real fibre functors. A canonical involution u -> u' of G from complex
  conjugation on M (central in Gal(L/Q)): the symmetry on Ker j*, the identity on Im j, complex conjugation on the
  cocharacters.
- **15:125.** It does not seem that this involution comes from an involution of the gerbe 𝒢 (no covariance with the
  conjectural fundamental element of H^2(Q, U), "qui serait d'ordre divisant 2").

**Checked** (P3-16 to P3-25):
- Prop. 1 and 2 (re-proved, for G commutative, the frame of 15:84-88): Ker(epsilon) has component group Z/k with
  epsilon = k epsilon', and k divides j*(epsilon) = 2, which gives the dichotomy; in the square case
  epsilon'(j(-1)) = -1 while epsilon' is trivial on U^0, so U = U^0 x j(mu_2); a rank-1 object of degree 1 (the
  character epsilon') cannot carry a non-degenerate alternating form, so no real fibre functor; H^2(R, S^1) =
  S^1/{z/z-bar} = 0 and H^2(R, mu_2) = Z/2 (Pro note T04 computes the same). For G not commutative Prop. 1 fails as
  written: for an elliptic curve over Q without CM, G = GL_2, epsilon = det is primitive and the Betti realization is a
  real fibre functor, but U = SL_2 is not a torus (nor compact). So the propositions are for commutative G (motives over
  finite fields, 15:88); in general (i) must read "U connected", and (i) => (iii) then needs an argument the page does
  not give.
- The torsor statements of 15:119 (re-proved): for a compact torus U, H^1(R, U) = X_*(U)/2 = 2U(R) canonically
  (x -> x(-1)); the two torsors under 2U(R) and an equivariant map give a bijection.
- **15:119, the Cor.: reading decided on the scan**: "epsilon = pr_2, j(lambda) = inj_1(lambda)^2" with subscript 1
  (both witnesses agree), after a cancelled "pr_2(lambda)^2". **Refuted, with the refinement**: Ker(pr_2) = U^0 is
  connected, which contradicts Prop. 2 (i). In the case of Prop. 2, (u, lambda) -> u j(lambda) is an isomorphism
  U^0 x G_m -> G^0 (j(-1) is not in U^0), under which epsilon = pr_2^2 (lambda -> lambda^2) and j = inj_2.
- 15:121, the cocharacter i (re-proved): with v_p normalized by v_p(q) = 1, v_p(lambda) + v_p(lambda-bar) =
  v_p(lambda lambda-bar) = j*(lambda), so i + i-bar = j and epsilon i = id. **Reading decided on the scan**: the ink has
  "v_p(lambda) v_p(lambda-bar)" with no "+"; the sum is meant.
- The caveat (computation): his example L = Q(sqrt(-p)) gives v_p(sqrt(-p)) = 1/2, a non-integral value in weight 1;
  in weight 0 it gives nothing, since 𝔭 = tau𝔭 there forces v_𝔭 = 0 on norm-one elements. A weight-0 example:
  L = Q(i, sqrt 5), p = q = 5, phi = (1 + sqrt 5)/2: N(1 + i phi) = (5 + sqrt 5)/2 . (5 - sqrt 5)/2 = 5, so
  𝔓 = (1 + i phi) is a prime over 5 with e = 2 and tau𝔓 != 𝔓, and u = (1 + i phi)/(1 - i phi) has u u-bar = 1 and
  v_p(u) = 1/2. His caveat is right.
- The restriction i|mu_2 of 15:123 (computation): it is well defined when the values of i have odd denominators
  (x -> x^d is the identity of mu_2 for d odd) and undefined when a denominator is even. Even denominators occur in the
  case of Prop. 1: L = Q(i), p = 5 = pi pi-bar, q = 25, lambda = 5 pi^2 = 15 + 20i, lambda lambda-bar = 625 = q^2, so
  i(lambda) = v_pi(lambda)/v_pi(25) = 3/2, while M has only even degrees (epsilon primitive, real fibre functors
  exist). So the "paquet de R-foncteurs fibres privilégiés" of 15:123 needs a definition when i is fractional
  (hunch c15-H2).
- "Sous-groupe d'indice fini" (15:123, re-proved): epsilon(i - i') = 0, so the differences lie in X_*(U^0), of corank 1;
  they can have finite index only there (Pro note T12 finds the same).
- The involution (re-proved): lambda-bar = q^(j*(lambda))/lambda gives c(m) = j*(m)q - m, so c acts by -1 on
  X*(U) = X*(G^0)/Zq: it is inversion on U and sends h to -h in H^2(Q, U) (Pro note T16). If 2h = 0, as he expects,
  the class is invariant, so the reason given on 15:125 is not an obstruction; what remains is whether a lift to the
  gerbe can be chosen of order 2.

**Wrong** (CORRECTIONS): the Cor. of 15:119; the missing "+" on 15:121; "même sur le ss-groupe où j = 0" with the
example Q(sqrt(-p)); the finite-index target on 15:123; the reason given on 15:125.

**Open (his).** The transitivity question of 15:121 ("À voir"); the choice of privileged polarizations (15:121-123),
which needs i integral on mu_2; the lift of the involution to the gerbe (15:125); the "élément fondamental conjectural"
of H^2(Q, U). Strongest reduction on the pages: Prop. 1-2 reduce the existence of real fibre functors to the
primitivity of epsilon; 15:119 reduces the real fibre functors to the polarizing structures (a bijection of torsors).
Status: known in substance (Deligne-Milne 1982, §§4-5, polarizations and real fibre functors; Serre's argument for
supersingular curves, 15:11, SA05-18; locators unverified); his: Prop. 1-2 in this form, the torsor bijection of
15:119-121, the cocharacter i over F_q and the canonical involution.

## D. Reused leaves in 15:87-138 of this stretch (SA06-11; identified, not studied)

- 15:87: English typescript p. 86, section VI (reflexive modules over a noetherian integrally closed domain, Theorem
  VI.5, "the thesis of the author, Chapter II, Lemma 0.1"); author unidentified (Pro notes).
- 15:89, 91, 93: French typescript leaves of SGA 4 VIII (Remarque 3.13 on conservative families of fibre functors at
  very dense sets; the end of the proof of 9.4, descent of étale sheaves), typescript pp. 42-43, 88 (locators
  unverified).
- 15:95, 109: R. Steinberg, Regular elements of semi-simple algebraic groups, Publ. Math. IHÉS 25 (1965), §§1-2,
  typescript pp. "-7-", "-10-" (identified in the Pro notes; locator unverified).
- 15:111, 113, 115, 120, 122, 124, 126: an English typescript (pp. 74-86) of the projectivity criterion of
  B. G. Moishezon, Izv. Akad. Nauk SSSR 28 (1964), 179-224: his margins cite pp. 208, 210, 213 of the original
  (identification as in the Pro notes; translator unknown).
- 15:118: an errata sheet ("Page 33", "Page 35 ... supprimer 'lisse sur k'"), with a cancelled correction compared in
  the Pro notes to SGA 3 VIII 7.13(b).
- 15:138: a Bourbaki errata sheet ("n° 505", p. 16) for Topologie générale IX (Polish, Souslin and Lusin spaces).

## Witnesses for 15:170-206

- 170-171, 179-194: Pro MPL_15_170-194r (text); Codex K15-06 (179-183), K15-07 (184-194), B15-01 (170, 171, 181, 188).
- 172-178: no page of MPL_15_170-194r; the Pro checkpoint MPL_15_139-194_checkpoint_01 (pages, doubts and inventory,
  no notes file) is the text; Codex K15-06 is the second witness.
- 195-206: the Pro package MPL_15_195-228+18_002-017 exists (its README: root and pages/ authoritative; a second Pro
  chat, `_chatB_unzipped`, is a further witness) and is the text; Codex K15-08 is the second witness. The launch
  prompt pointed at the Codex folders for 172-178 and 195-206; the Pro transcriptions were read instead.
- Covers and titles (his): 172, 180, 182, 189, 190. 181: a private administrative document (redacted in the Pro
  transcription), not read. 175: a cancelled draft (read with keepdel).

## E. 15:170 (his agenda, SA06-14)

"Foncteurs fibres motiviques, et groupes fondamentaux motiviques. À examiner:" 0) abelian varieties "à la Weil"
attached to pure motives of odd weight, Hodge-Riemann conditions; 1) extension of the groups defined by "des
présentiques" (Pro) or "des places arithmétiques" (Codex B15-01), unresolved on the image, then "Groupe fondamental
motivique" (underlined); 2) relations with class field theory; 3) the case of the spectrum of a finite field, the
motivic problem of "points" (Pro; Codex "parties") with values in R "???"; 4) the role of motivic fundamental groups
in comparing canonical lattices (Hodge: two transcendental lattices for different places, the transcendental lattice
and the Hodge lattice; l-adic: two transcendental lattices); 5) relations of 4) with his old notes; 6) L-functions,
functional equation; 7) "Structures positives" (Pro; Codex "pratiques"); 8) a topology to put on Z; 9) the Riemann
hypothesis "??", margin: Hodge-type positivity by reducing to questions on divisors, by blowing up, "ou variétés de
drapeaux ??" (Codex; Pro "ou vertu des pinceaux ??").

**Readings decided on the scan** (250 dpi): the left-margin marks stand beside the items they mark: "OK *" beside 1),
"OK" beside 3), "*" beside 4), "OK" beside 7). Both witnesses set them as margins after items 0, 2, 3 and 6, which
attaches them to the wrong items in a reading. Item 9's margin ends "ou Variétés de / drapeaux ??" (Codex right);
item 7 reads "Structures positives" (Pro right, medium confidence). The items marked OK, 1, 3 and 7, are the ones the
dossier treats: the motivic fundamental group (15:189-205), finite fields and real points (15:84-138), positivity
(15:117-125).

- **What the rest of the dossier does with it** (read): item 3 is 15:84-138 (Weil numbers, real fibre functors,
  15:117-125); item 4 is 15:191-205 (the fibre functors xi_l, xi_p, xi_infinity, xi_Z and their lattices); item 8 is
  close to the absolute cohomology of 15:172-178 (Spec Z with H^3(Spec Z, Q(1)) = Q); item 9's margin is the
  Hodge-index route to the standard conjectures (cote 14: SA06-4 to SA06-6, parts 1-2 of this stretch).
- Sweep 2 placed SA06-14 at "cote 15, scan 179": the agenda is on scan 170 (correction).
- Status: his agenda; no claims to check. "VA à la Weil" reads as Weil's intermediate Jacobians (Weil, On Picard
  varieties, Amer. J. Math. 74 (1952); locator unverified), which are abelian varieties by a Hodge-Riemann argument.

## F. 15:172-179 (his pages): "Calculs de cohomologie absolue des Motifs de Tate Z(n)" and a Brauer-group draft (SA06-16)

Sweep 2's title for SA06-16 ("étale cohomology of curves over finite fields") does not fit the pages: the objects are
F_q, Spec Z and its open subsets U, and schemes with factorial strict local rings.

- **15:173.** pi = Gal(F̄_q/F_q) = Ẑ generated by f; for a finite Z_l-module M, H^0 = Ker(1 - f), H^1 = Coker(1 - f),
  H^i = 0 for i >= 2; H^0(pi, Z_l(n)) = 0 (n != 0); H^1(pi, Z_l(n)) = Z_l/(1 - q^n) non-canonically: Z_l (n = 0), 0 if
  l does not divide 1 - q^n (n not divisible by omega_l(q), the order of q mod l), Z/l^(v_l(1 - q^n)) otherwise;
  rationally H^i(pi, Q_l(n)) = 0 (n != 0), H^0 = H^1 = Q_l (n = 0). Then the "absolute" motivic groups:
  ℍ^i(F_q, Q(n)) = 0 for n != 0; ℍ^0(F_q, Q) = ℍ^1(F_q, Q) = Q; integrally ℍ^0(F_q, Z) = ℍ^1(F_q, Z) = Z,
  ℍ^1(F_q, Z(n)) = Z/(1 - q^n) for n != 0 ("mod p-primary ?"); H^i(Spec Z, Z(1)) = Z for i = 3, else 0;
  ℍ^i(Spec Z, Z) = Z for i = 0, else 0. Margin: H^i(Spec Z, Q(n)) = H^i(U, Q(n)) for U open and "n != 0".
- **15:174.** Purity i_x^! M = i_x^* M(-1)[-2] and the localization sequence for X = Spec Z, U open, S = X - U; for
  M = Q(n): the restriction is an isomorphism for n != 1; for n = 1 the six-term sequence with Q^S twice gives
  "H^i(X, Q(1)) = 0 sauf pour i = 3, où on trouve Q !".
- **15:175.** Cancelled draft: crossed homomorphisms of Z, Z^1(Z, M) = M, B^1 = (1 - f)M, H^1(Z, M) = M/(1 - f)M.
- **15:176.** When the strict local rings are factorial, H^1(X, Div^0) = 0, whence Prop. 5.4 (under 5.1 a), X
  irreducible with generic point y): H^2(X, G_m) -> H^2(X, R_X*) -> H^2(y, G_m) = Br(y) are injective; Cor. 5.5:
  Br(X) -> Br(K) is injective; Th. 5.6 a): for X local, xi in H^2(X, G_m) lies in Br(X) iff some finite étale
  surjective X' -> X kills it.
- **15:177-178.** Local cohomology H^i_x(G_m) = Z (i = 1), 0 otherwise; H^i_S(X, G_m) = H^(i-1)(S, Z) = Z^S, 0,
  (Q/Z)^S, 0 for i = 1, 2, 3, >= 4; for Spec Z: H^0 = Z* = {+-1}, H^1 = H^2 = 0, H^3 = Q/Z (sum of invariants);
  H^0(U, G_m) = Z/2 + Z^S, H^1 = 0, H^2 = Ker((Q/Z)^S -> Q/Z), H^i = 0 (i >= 3); Kummer: H^1(U, mu_(l^n)) = (Z/l^n)^S,
  H^2 = Ker((Z/l^n)^S -> Z/l^n); H^1(U, Z_l(1)) = Z_l^S, H^2(U, Z_l(1)) = Ker(Z_l^S -> Z_l) ("petite modification l = 2
  en dim 0"); H^i(X, Q(1)) = 0, 0, 0, Q for i = 0, 1, 2, 3.
- **15:179.** For X noetherian without embedded primes, (5.1.) 0 -> G_m -> R_X* -> Div_X -> 0 (étale sheaf of Cartier
  divisors); H^p(X, R_X*) is torsion for p > 0 (crossed paragraph), so d: H^i(X, Div_X) -> H^(i+1)(X, G_m) is
  bijective mod torsion for i >= 1; margin "Donner le corollaire 5.4."; factoriality gives an isomorphism of étale
  sheaves (the page stops at the colon).

**Checked** (P3-27 to P3-34):
- 15:173 (re-proved): cohomology of Ẑ with Z_l-coefficients (cd 1, H^1 = coinvariants); the three cases of
  H^1(pi, Z_l(n)) (f acts by q^n; l | 1 - q^n iff omega_l(q) | n, for l odd; for l = 2 always). His integral values
  for F_q agree with K_(2n-1)(F_q) = Z/(q^n - 1) for n >= 1 (Quillen, Ann. of Math. 96 (1972); locator unverified)
  and with ℍ^1(F_q, Z) = Z (the Weil group Z, not Ẑ: hunch c15-H4).
- 15:174 and 178 (re-proved): with H^1(U, Q(1)) = Q^S mapping isomorphically to Q^S by valuations, and
  H^2(U, Q(1)) = Ker(Q^S -> Q) mapping injectively to Q^S, the sequence gives H^1 = H^2 = 0 and H^3(X, Q(1)) =
  Q^S/Ker(sum) = Q. For n != 1 the residue terms are the cohomology of Q(n - 1) on S, which vanishes: restriction is an
  isomorphism. **The margin of 15:173 says n != 0; the computation of 15:174 shows n != 1 is the condition**
  (for n = 1 the restriction is not an isomorphism; for n = 0 it is). Both witnesses read n != 0: his slip, corrected
  by his own next page.
- 15:177-178 (re-proved): purity for G_m on a regular one-dimensional scheme; H^2(S, Z) = H^1(S, Q/Z) = (Q/Z)^S;
  the values for Spec Z agree with Artin-Verdier (Pic Z = Br Z = 0, H^3 = Q/Z; Milne, Arithmetic Duality Theorems,
  II.2; locator unverified), the real place being the "petite modification l = 2" he reserves.
- 15:176 and 179 (re-proved): with factorial strict local rings Div = sum over codimension-1 points of (i_x)_* Z, so
  H^1(X, Div) = sum Hom_cont(Gal, Z) = 0 and H^2(G_m) -> H^2(R*) is injective; R^1 j_* G_m = 0 (Hilbert 90 on the
  strict henselizations), so H^2(X, j_* G_m) -> H^2(y, G_m) is injective (edge map). H^p(X, R*) is torsion for
  p > 0 (higher Galois cohomology is torsion), hence the bijectivity mod torsion. Known: Grothendieck, Le groupe de
  Brauer I-II, in Dix exposés (1968) (locators unverified). Th. 5.6 a) is the classical criterion (an Azumaya algebra
  over a local ring splits on a finite étale cover; conversely descent of a matrix algebra); known, same source.
- **15:179, "(1.1.)" and the margin: readings decided on the scan**: the equation number is "(5.1.)" and the margin
  "Donner le corollaire 5.4." (Codex K15-06 reads the same; the Pro text has "(1.1.)" and "donne le(?) corollaire
  3.4.(?)"). The draft is numbered §5: 179 (5.1) comes before 176 (5.3-5.6) in its order, the sheets are filed in
  reverse.

**Open (his).** "(mod p-primary ?)" on 173 (the p-part of the integral groups); "= 0 ?" for H^3(U, Q(1)) (174;
answered by 178: 0 for U != X); "[est-ce nul ??]" (174), which the SA05 reader of the same pages answers: no,
H^1(Spec Z, Q(n)) = K_(2n-1)(Z) (x) Q = Q for odd n >= 3 (Borel). 15:172-178 were read independently in
sweep3/SA05/readings/c15b_c12_c11.md §1.6 (Claude Opus 5.5 at effort max, agent a7b7747fd6dd29f87), which places them
under SA05-10 and reaches the same checks and the same correction (n != 1).

## G. 15:182-187 (his pages): "Généralités fonctoriello-catégoriques sur la distribution des frobenius dans les groupes de Galois motiviques" (SA06-15)

- **15:183.** M motives of finite type over S of finite type over Z; assume even degrees (otherwise use M^pair, as the
  Cor. of 15:117 allows); a closed point s gives "R-points motiviques" (real fibre functors) of M; fix one, with group
  G_R. Replace s by pairs s' = (s, i), i: G_m,C -> G^(s)_C "de type préférentiel" (15:121); each s' gives a real
  point of M, a class xi(s') in H^1(R, G^00_R) (G^00 = Ker(epsilon on G^0_R)), and u(s'): G(s)_R -> G_R^(xi(s'))
  compatible with epsilon and j, determined up to conjugation by G^00_R(R).
- **15:185.** A polarization pi on G^0_R, given by i: mu_2,C -> G^0_C; v(s') = u(s')_C ∘ (i(s')|mu_2); the transported
  polarization must be the one defined by the v(s'): for xi(s') constant, the polarizations of the various v(s') must
  coincide, "une condition non tautologique sur la distribution des u(s')"; but the polarizations of a real group H
  given by mu_2 -> H_C form a finite set "si G est commutatif en tous cas !" (margin "? à vérifier"). "Conformément aux
  conjectures de Tate magnifiées", the u(s') recover the effectivity structure:
- **15:187.** the cone expressing effectivity is generated by the rays defined by the v(s'): an "analytic" form of the
  fact that the eigenvalues of the Frobenius f(s') in G_R^(xi(s'))(R), in every representation, even of
  G_C^(xi(s')), are algebraic integers, "une condition arithmétique assez draconienne !".

**Checked** (P3-35 to P3-37):
- The finiteness (re-proved): for H commutative, Hom(mu_2, H_C) = 2H(C) is finite; for H not commutative it is finite
  only up to conjugation. His qualification is right.
- The effectivity cone (re-proved): a representation is effective (all Frobenius eigenvalues integral at p) iff all
  its weights pair non-negatively with every conjugate of every u(s')_C ∘ i(s'), the slope cocharacters; so the cone
  is the dual of the cone generated by these cocharacters. Rays need the cocharacters, not their restrictions v(s') to
  mu_2 (the reading "v" is doubtful in the Pro text).
- The torsor statements of 15:183 follow from 15:119 (real fibre functors form a torsor under H^1(R, U); the choice of
  i picks one): agrees, with the integrality caveat of §C (i|mu_2 needs odd denominators).

**Open (his).** The "condition non tautologique" is not stated as a theorem; "conjectures de Tate magnifiées" and the
recovery of effectivity from the u(s') are conjectural. Known in substance as the motivic Sato-Tate frame (Serre,
Propriétés conjecturales des groupes de Galois motiviques et des représentations l-adiques, in Motives, Proc. Symp.
Pure Math. 55 (1994), §13; locator unverified).

## H. 15:189-205 (his pages): "Théorie de Galois des Motifs. Généralités" and "Foncteurs fibres motiviques et groupe fondamental motivique" (SA06-15)

- **15:191.** X connected. 1°) X_red of characteristic p > 0: the fundamental pro-torsor (T_alpha) has no sections in
  general; one has (i) l-adic points xi_l^(alpha) in T_alpha(Z_l), l != p, "provenant sans doute" from points over the
  henselization Z̃_(l); (ii) a crystalline point xi_p^(alpha) in T_alpha(W_p(k)) for k perfect over X, with the
  supplementary structure F and V, semilinear (box), "DeRham-Hodge" (margin: work in the derived category, keep the
  Hodge-de Rham filtration); (iii) its reduction in T_alpha(k). Even for X = Spec F_q there are non-trivial
  obstructions in H^2(Q, G). With fibre functors inducing the canonical one on effective motives of weight 0, the
  points of T_alpha(Z_l) are "sans doute" unique up to isomorphism (Lang), likewise those of T_alpha(W_p(k)) for k
  finite, more generally k perfect of dimension <= 1 (?); in general T_alpha(k) has several classes, but perhaps
  T_infinity(k) = lim T_alpha(k) has one, the de Rham-Hodge one. Margin: relation with the "problème galoisien ??",
  "cf Manin".
- **15:193.** The xi_l depend on a geometric point up to non-unique isomorphism (pi_1(X) acts); the xi_p^alpha depend
  on a point with values in a perfect field, with no isomorphisms between different k-points ("c'est la 'partie
  continue' du H^1 préc. qui va faire des ennuis"); for k algebraically closed they are conjugate under automorphisms
  of k; pi_1(X) does not act on xi_p, the automorphisms of k over k(x) act semilinearly; F, V with FV = p. Notation:
  xi_(x̄,l), xi_(x,l), xi_(x,p), xi^0_(x,p).
- **15:195.** 2°) X dominating Spec Z: (i) xi_l in T(Z_l) for all l; (ii) xi_(x,p), xi^0_(x,p) at points of
  characteristic p, and the "connexion" between xi_(y,p) and xi_(x,p) (x) W(k), "en général pas isomorphes, sans
  doute"; (iii) at points with values in a field of characteristic 0, xi_(x,infinity) in T_alpha(k) by Hodge-de Rham,
  with two filtrations (margin: the Hodge filtration, graded pieces H^q(X, Omega^p) (reading below), proper to the de
  Rham functor and not coming from a filtration of the motive; and the arithmetic one, matching the canonical
  filtration of motives, trivial for simple motives).
- **15:197-199.** No pi_1-action on xi_(x,infinity); automorphisms of the coefficient field act semilinearly; for
  h = Q a point xi_(x,infinity) in T_alpha(Q), a trivialization of T_Q; two need not be isomorphic; no canonical, and
  perhaps no, isomorphism between xi_(x,infinity) (x) Q_l and xi_(x̄,l) (x) Q_l, "Ainsi, tout pt rat/Q définit une
  classe de coh dans H^2(Q_l, G_l^(0(alpha)))" (ink 2, see below); margin: "en fait, ils sont déjà non isom sur les
  Motifs de poids et niveau 0"; in general replace Q_l by Q_l (x) k, "particulièrement intéressant" for k a number
  field. (iv) a complex point x gives xi_(x,Z) in T_alpha(Z) (an integral lattice), with xi_(x,Z) (x) Z_l = xi_(x,l)
  and xi_(x,Z) (x) C = xi_(x,infinity), and an "involutive" isomorphism xi_(x,Z) = xi_(tau x,Z).
- **15:201.** For a real place a: the involution tau on xi_(a,Z) (not to be confused with the semilinear endomorphism of
  xi_(ā,infinity)); invariants xi_(a,infinity) in T_alpha(R), xi_(ā,infinity) in T_alpha(C), xi_(ā,Z) in T_alpha(Z).
- **15:203.** The Hodge decomposition (transcendental) is determined by the semilinear involution tau' from
  xi_(x,infinity) = xi_(x,R) (x) C, xi_(x,R) = xi_(x,Z) (x) R; for k(a) real a second one tau'' from the real de Rham
  structure; "tau = tau' tau'' = tau'' tau'" (margin "à vérifier"); tau on xi_(a,l) is the Frobenius at the real
  place, an element of pi_1(X) (margin "à vérifier").
- **15:205.** f_infinity acts on xi_(x,Z), extended linearly to tau = f_infinity. N.B.: the Hodge conjecture interprets
  the arithmetic (motivic, level) filtration in terms of the Hodge filtration and f_infinity: "La partie de niveau
  <= rho dans xi_(x,Q)(F) n'est autre que xi_(x,Q)(F) ∩ xi_(x,infinity)(F)^(rho) ∩ f_infinity xi_(x,infinity)(F)^(rho)";
  the last subspace is motivic, the two Hodge terms are not. (Continues on 207, outside this stretch.)

**Checked** (P3-38 to P3-46):
- 15:191 "no sections" (targeted check): over F_q the motivic gerbe has no Q-valued fibre functor (the supersingular
  quaternion algebra, ramified at p and infinity, cannot act on a 2-dimensional Q-space): agrees (Milne, Motives over
  finite fields, 1994; Serre's argument, 15:11, SA05-18).
- Uniqueness (re-proved, conditionally): if G_alpha has a smooth connected model over Z_l (resp. W(k)), Hensel's lemma
  gives H^1(Z_l, 𝒢) = H^1(F_l, 𝒢) = 1 by Lang, and H^1(W(k), 𝒢) = H^1(k, 𝒢_k) = 1 for k perfect of cohomological
  dimension <= 1 by Steinberg's theorem (H^1(k, G) = 0 for connected linear G; Steinberg, Publ. Math. IHÉS 25 (1965),
  Th. 1.9; locator unverified), the paper whose typescript is reused on 15:95, 97, 99, 109 (hunch c15-H2). His
  "sans doute" is the model hypothesis.
- 15:197 margin (re-proved): on Artin motives the torsor of isomorphisms between the de Rham fibre functor (x) Q_l and
  the l-adic one is the Gal(Q̄/Q)-torsor Spec(Q̄ (x) Q_l), which has no Q_l-point: they are already non-isomorphic in
  weight and level 0. Agrees.
- **15:197, "H^2(Q_l, ...)": reading decided on the scan** (250 dpi, medium confidence): the exponent is a 2. Two
  fibre functors over Q_l differ by a torsor under the automorphism group of one of them: the class lies in H^1, not
  H^2 (Pro note A04 leaves the reading open). His slip.
- 15:199 (targeted check): the Betti lattice and the comparisons xi_Z (x) Z_l = xi_l (Artin), xi_Z (x) C = xi_infinity
  (de Rham), and complex conjugation of the point: agrees (SGA 4 XI and XVI; Deligne, Valeurs de fonctions L et
  périodes d'intégrales, Proc. Symp. Pure Math. 33 (1979), §§0-1; locators unverified).
- 15:203 (independent re-proof of his "à vérifier"): F_infinity is defined on the Betti Z-lattice, so it commutes with
  tau' (conjugation of coefficients); the comparison identifies F_infinity (x) c with 1 (x) c on the real de Rham side,
  i.e. tau'' = F_infinity tau'; hence tau' tau'' = tau'' tau' = F_infinity. Agrees (Pro note A07 says commutativity
  does not follow from semilinearity alone: it follows from F_infinity being defined over Z). The Hodge decomposition
  is H^(p,q) = F^p ∩ tau'(F^q): agrees. tau on xi_(a,l) is the real Frobenius in pi_1(X) by compatibility of the Artin
  comparison with complex conjugation: agrees (same sources).
- **15:195 margin: reading decided on the scan** (medium confidence): the graded pieces read "H^q(X, Omega^p)" (the
  letter after X is a looped capital with superscript p; there is no Q), and the second filtration is
  "(arithmétique)", matching 15:205's "filtration arithmétique"; the Pro text has "H^i(X, Q_l(?))" and
  "caractéristique(?)". The mathematics needs H^q(X, Omega^p).
- **15:205, the level formula: refuted as stated, with the refined statement** (reading confirmed on the scan). With
  f_infinity F^rho = complex conjugate of F^rho (F^rho is defined over R), the formula says: the level <= rho part of
  the Betti realization is H_Q ∩ F^rho ∩ F̄^rho = H_Q ∩ F^rho, the form of Hodge's general conjecture that he
  himself refuted in 1969 (Hodge's general conjecture is false for trivial reasons, Topology 8 (1969), 299-303;
  locator unverified). A counterexample computed here: E = C/(Z + Z tau) with tau a non-real cubic irrationality
  (so E has no CM), F = h^1(E)^(x)3, weight 3, rho = 1 (types (2,1), (1,2)). With a symplectic basis alpha, beta and
  omega = alpha + tau beta, a rational vector v lies in F^1 iff <v, omega^(x)3> = 0; on the tensor basis the values are
  +-tau^k (k = 0, ..., 3), whose Q-span is Q(tau), of dimension 3. So H_Q ∩ F^1 has dimension 8 - 3 = 5, odd, hence it
  is not a Hodge substructure of odd weight and cannot come from a submotive. The level <= 1 part is the
  H^1(E)(-1)-isotypic part, of dimension 4 (MT = GL_2). Refined statement (his 1969 correction, the generalized Hodge
  conjecture, open): the level <= rho part is the largest Q-sub-Hodge structure contained in the Hodge piece.

**Wrong** (CORRECTIONS): 173 margin "n != 0" (n != 1); 179 "(1.1.)" and "corollaire 3.4" (Pro readings); 195 margin
(Pro reading); 197 "H^2" (H^1); 205 the level formula.

**Open (his).** The uniqueness of T_infinity(k) (191); the "problème galoisien" with Manin (191); the comparison of
xi_(y,p) with xi_(x,p) (x) W(k) (195); the class of a rational point over Q_l (x) k for k a number field (199).
Status: known in substance as the realizations of motives with their comparison isomorphisms and integral structures
(Deligne 1979; Fontaine-Messing and the crystalline comparison; Oda, Ann. Sci. ÉNS 2 (1969), Cor. 5.11, for H^1, as
cited in the Pro notes); his: the organisation as points of one fundamental pro-torsor at every place, the
non-isomorphism statements, and the "partie continue" warning.

## I. Reused leaves in 15:170-206 (SA06-11; identified, not studied)

- 15:171, 192, 194, 196, 198, 200, 202, 204, 206: Bourbaki "Tribu n° 59" sheets: "Systèmes de racines (20)",
  "Algèbres de Lie semi-simples (9) to (3)" and "Décisions sur les algèbres de Lie semi-simples (n° 400)", filed in
  reverse page order.
- 15:184, 186, 188: the Moishezon projectivity typescript again (pp. 70-73; margins cite pp. 202, 208).
- 15:181: a private administrative document (redacted), not mathematics.

## Hunches (part 3; "(mine)": none is a statement of the pages)

**c15-H1. The privileged polarizations of 15:121-123 and the real points of 15:183 need the slope cocharacter on a
cover.** Grounds: his caveat (15:121) that lambda -> v_𝔭(lambda)/v_𝔭(q) is not integral; i|mu_2 is defined exactly
when the denominators are odd; even denominators occur with even degrees (q = 25, lambda = 15 + 20i, slope 3/2). The
natural repair is the Weil-number protorus with its slope cocharacter defined on the protorus with character group Q,
as in the pseudo-motivic Galois group of Langlands-Rapoport (Shimuravarietäten und Gerben, J. reine angew. Math. 378
(1987)) and Milne 1994 (locators unverified); the parity of the slope denominators then decides whether a privileged
real point exists. Pages: 15:121-123, 183-185. Links: SA06-9, SA06-10, SA05-18.

**c15-H2. The reused Steinberg leaves were in his hands for a reason.** Grounds: 15:95 is Steinberg's Theorem 1.10 on
perfect fields of dimension <= 1, and 15:191 invokes exactly "k parfait de dim <= 1 (?)" for the uniqueness of the
crystalline points. Steinberg's paper is of 1965, which bounds 15:191 from below. Pages: 15:95, 97, 99, 109, 191.

**c15-H3. 15:195-205 predate his 1969 note, and that note repairs this page.** Grounds: the level formula of 15:205 is
the naive general Hodge conjecture (refuted above with a cubic tau, and by him in Topology 8 (1969)); together with
c15-H2 this places 15:191-205 between 1965 and 1968. Links: SA06-4 (the standard conjectures, the letter to Serre of
27.8.1965 in part 1), SA06-2.

**c15-H4. The "cohomologie absolue des motifs de Tate" is the integral Weil-étale cohomology.** Grounds: 15:173-178
give ℍ^0(F_q, Z) = ℍ^1(F_q, Z) = Z (étale cohomology gives Z and 0), ℍ^1(F_q, Z(n)) = Z/(q^n - 1) (Quillen's
K-groups), H^3(Spec Z, Q(1)) = Q and H^3(Spec Z, Z(1)) = Z: F_q behaves as a circle and Spec Z as a closed
3-manifold with a fundamental class, the picture of Artin-Verdier duality (1964) and of Lichtenbaum's Weil-étale
cohomology (Compositio Math. 141 (2005) for varieties over finite fields; Ann. of Math. 170 (2009) for number rings;
locators unverified). His agenda item 8, "Topologie à mettre sur Z", points the same way. Pages: 15:170, 173-178.
Links: SA06-14, SA06-16.

**c15-H5. "La partie continue du H^1" (15:193) is the moduli of F-crystals.** Grounds: isocrystals with G-structure
over an algebraically closed field are discrete (Dieudonné-Manin, his "cf Manin"; Kottwitz's B(G), Compositio
Math. 56 (1985)), while integral F-crystals vary in continuous families (Rapoport-Zink, Period spaces for p-divisible
groups, 1996); that is the obstruction he expects to the isomorphism of crystalline points at different k-points.
Links: SA15 (crystals), SA06-8 (the crystalline side of the Deuring gerbe, 15:42-56).

**c15-H6. 15:183-187 is the motivic Sato-Tate frame, with an effectivity criterion.** Grounds: Frobenius classes at
closed points placed in the compact form G^00 twisted by xi(s'), and the "condition non tautologique" on polarizations
(Serre 1994, §13; Serre, Lectures on N_X(p), 2012, ch. 8; locators unverified). His further claim, that the u(s')
recover effectivity (a motive is effective iff its Frobenius eigenvalues are integral at every closed point), is a
"conjecture de Tate magnifiée" that I know no reference for. Links: SA06-2 (the character cone of cote 14).

**c15-H7. The obstruction to lifting Frobenius to the norm-one torus is class-group theoretic.** Grounds: P3-26: up
to a 2-group, coker(M_0(q) -> (Z^P)^-) is the subgroup of Cl(L) generated by the minus-divisors at p. This is the
same group that governs which Shimura-Taniyama divisors are principal; it bears on the strong conjecture of 15:100
without powers (STUDY H4, RP-SA06-2). Pages: 15:110-114, 96-100.

## Dependencies (part 3)

| Piece | Uses | Page that shows it |
|---|---|---|
| SA06-9 (15:94) | SA06-9 (15:131-132, STUDY §1) | the Cor. needs the equivalence (a) <=> (c) of 15:131 |
| SA06-9 (15:110-112) | SA06-9 (15:96, STUDY §1) | finite index of M_0(q) in (Z^P)^- (the Proposition of 15:96) |
| SA06-9 (15:88) | SA06-9 (15:84-86, STUDY §2) | "ce qui précède prouve que (Ker epsilon)^0 est un tore compact" |
| SA06-10 (15:117) | SA06-2 (14:2) | margin "On n'utilise que les éléments de structure 1, 2, 3" |
| SA06-10 (15:117-119) | SA05-18 (15:11) | Prop. 2 is Serre's argument (no real fibre functor when epsilon is a square) |
| SA06-10 (15:119) | SA06-8 (15:52) | the rank-2 degree-1 object generating an R-twisted subcategory (the quaternionic line) |
| SA06-10 (15:121-123) | SA06-9 (15:110) | i from the valuation at 𝔭 on M(q) in L |
| SA06-15 (15:183-187) | SA06-10 (15:117-123) | M^pair, real fibre functors, i "de type préférentiel" |
| SA06-15 (15:187) | SA06-2 (cote 14) | the effectivity cone |
| SA06-15 (15:191-193) | SA15 | F, V with FV = p on the crystalline points |
| SA06-15 (15:191) | SA06-11 (15:95, Steinberg) | "k parfait de dim <= 1" |
| SA06-15 (15:205) | SA06-4 | the Hodge conjecture as a statement about the level filtration |
| SA06-14 (15:170) | SA06-9, -10, -15, -16, SA06-4 | items 3, 4, 8, 9 |
| SA06-16 (15:172-179) | nothing in SA06 | known étale cohomology (Artin-Verdier, Brauer I-II) |

## Deliverable state (part 3)

| Scans | Passes | Open readings on his pages (unsure / illegible marks) | Decided here on the scan | Ready? |
|---|---|---|---|---|
| 15:87-95 | Pro MPL_15_087-138 + notes; Codex K15-03 | 91 / 3 on 4 pages | none needed | after collation with K15-03 |
| 15:109-126, 138 | Pro MPL_15_087-138 + notes; Codex K15-04, K15-05 | 115 / 0 on 8 pages | 110 Z_l; 112 f_0; 119 inj_1; 121 no "+"; caveat box (Codex reading) | after collation; the caveat box should take the Codex reading |
| 15:170-171, 179-194 | Pro MPL_15_170-194r + notes; Codex K15-06, K15-07, B15-01 | 140 / 0 on 11 pages | 179 "(5.1.)", "corollaire 5.4" | after collation (the Pro text has the two misreadings on 179) |
| 15:172-178 | Pro checkpoint only (MPL_15_139-194_checkpoint_01: pages, doubts, inventory, no notes); Codex K15-06 | 42 / 0 on 7 pages | none | needs the final Pro pass or a second pass; the checkpoint text reads well |
| 15:195-206 | Pro MPL_15_195-228+18_002-017 (chat A, with chat B witness) + notes; Codex K15-08 | 76 / 4 on 6 pages | 195 margin; 197 "H^2"; 205 formula confirmed | after collation |

Pages read in part 3: his pages 88, 90, 92, 94, 110, 112, 114, 117, 119, 121, 123, 125, 170, 172-180, 182, 183, 185,
187, 189-191, 193, 195, 197, 199, 201, 203, 205 (36, including covers and the cancelled 175); reused leaves
identified: 87, 89, 91, 93, 95, 109, 111, 113, 115, 118, 120, 122, 124, 126, 138, 171, 184, 186, 188, 192, 194, 196,
198, 200, 202, 204, 206 (27); 181 private, 116 blank.

## Counts (part 3)

63 pages read (36 of his, including covers and the cancelled 175; 27 reused leaves identified in one line each);
48 check events; 25 corrections; 7 hunches (c15-H1 to c15-H7). Claude Opus 5.5 at effort max, c14_c15rest,
19 Nov 2026.
