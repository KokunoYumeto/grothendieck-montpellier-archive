# SA07 (Théorie des motifs III), sweep 3: periods, real structures, the comparison programme (cote 18)

Claude Opus 5.5 at effort max (agent a28ea31fa17dd65e1), 18 Nov 2026. Read in sweep 3: cote 18, scans 2-62, every
page of his hand in full (`MPL_15_195-228+18_002-017` pages 18:2-17, `MPL_18_018-062`), from the Pro transcription.
The interleaved reused typescripts (Bourbaki drafts "Tribu n° 59, Systèmes de racines", n° 370 Haar measure, n° 392
valuations, n° 413 formal kernels and distributions, and an English translation of a paper on direct images, 18:44) were
identified and not studied. Not read in sweep 3: cotes 10, 16, 19 (Work folders) and cote 15, scans 195-228 (reused Lie
typescripts). The order follows sweep2/SA07/WHAT_IS_WHERE.md; places are cote:scan.

## 1. The programme of cote 18 (18:4-5, 18:10, 18:42-43)

- **18:4** cover "Motifs et cristaux sur corps local". **18:5** "Descriptions conjecturales des motifs sur corps de
  nombres k": six realizations, 1) "double viseur" Betti-De Rham, 2) Betti-Hodge, 3) Hodge structure (k = Q̄),
  4) Betti-Gauss-Manin, 5) Betti-Tate, 6) "De Rham filtré cristallin"; and "Description conjecturale des groupes
  p-divisibles mod isogénie (plus généralement des pseudo-motifs) sur un corps local" [fraction field of a complete DVR
  with perfect residue field]: 3') Hodge-Tate structure (a finite Q_p-module N with a bigrading of N (x) C after a
  finite extension), 2') "double viseur Tate-Hodge", 5') the l-adic Galois module, 6') "cristal filtré [vectoriel de
  dimension finie sur K, une application sigma-semilinéaire, et filtration]". Then: **"Par quoi remplacer 1', 4' ??"**
- **18:43** "Pbs": 1) Betti and De Rham: a) compare the De Rham and Betti lattices, b) compare Betti lattices for
  different topologies, c) compare real structures and splittings in De Rham; 2) Betti and l-adic: compare Betti lattices
  for different topologies inside l-adic cohomology; 3) De Rham and p-adic over a complete discretely valued field of
  residue characteristic p: "comparaison possible entre cohomologie p-adique et cohomologie de De Rham ?"; 4) a
  definition of p-adic cohomology in characteristic p.
- What it is (mine): 6') is the filtered phi-module, and the question "what replaces 1' (the Betti-De Rham comparison)"
  is the problem of the "mysterious functor", answered by Fontaine's period rings and the crystalline comparison theorem
  (Fontaine-Messing 1987, Faltings 1989, Tsuji 1999) and by Colmez-Fontaine (2000) for the essential image. Status: his
  question; settled since.

## 2. Cycle classes: the factor 2 i pi (18:15, 17, 19, 21, 23, 25, 27, 29) — SA07-6

- He compares the analytic (= algebraic, de Rham) fundamental class P_an of a codimension-p subvariety with the
  topological one P_top. Reduction to a point on a disc (18:15); there P_an(1_Y) is the class of dz/z on X - a, and
  lambda = integral of dz/z over the unit circle = 2 i pi (18:17). **Boxed: P_an(1_Y) = 2 i pi P_top(1_Y)**; in
  codimension p, (2 i pi)^p, with the commutative diagram for any class (18:17, 21) and for proper maps of relative
  codimension p: f_*^top corresponds to (2 i pi)^(-p) f_*^an (18:23).
- 18:19: for X smooth over k with an unchosen isomorphism k = C, P_sigma^(p) = (1/sigma(2 i pi))^p P_alg: the
  integral lattice H^2p(X_sigma, Z) inside algebraic de Rham cohomology "dépend beaucoup de sigma, pi étant
  transcendant"; complex conjugation changes P_sigma^(p) into -P_sigma^(p) (for p odd), so the lattices do not change.
- 18:25: correspondences act compatibly on Betti and de Rham once P_top(z) = (2 i pi)^(-n) P_alg(z) ("Ouf !").
- 18:27-29: for K a topological field isomorphic to C (isomorphism not chosen), xi(Z(-1)) = Z is fixed up to sign by an
  orientation of P^1_K, i.e. a choice of sqrt(-1); then alpha_infinity(u) = (2 sqrt(-1) pi)^(-1) v, v the canonical
  generator of H^1(P^1, Omega^1).
- Checked: the residue computation and the normalization (check events SA07-S3-1, -2). Known since: the de Rham cycle class
  is (2 pi i)^p times the Betti class (Deligne, "Hodge cycles on abelian varieties", in LNM 900 (1982), §1).

## 3. Motives over R and the real Frobenius (18:31-41) — SA07-7

- 18:32-34: K isomorphic to C, M a motive over K: Betti(M) (x) K = DR(M) canonically; the real structure and the Hodge
  filtration give the Hodge bigrading of DR(M) independently of the choice of K = C. A motive over R gives (a) a Hodge
  structure V, (b) an automorphism f_R of order 2 of V_K, real and Q-rational, which exchanges the Hodge filtration with
  its opposite: **the real Frobenius f_R in G(Q)**, of order 2, generating G/G^0, with f_R i(lambda) f_R^-1 = i(lambda')
  for i: S_R -> G_R, i.e. i(lambda^-1) on U_R. "Le foncteur M -> (structure de Hodge, f_R) est pleinement fidèle en
  vertu des conj. de Hodge."
- 18:35: the "twisted Betti" fibre functor W (x + iy with x = fx, y = -fy): a second fibre functor, isomorphic to Betti as
  an additive functor but, he says, probably not as a tensor functor: it is Betti twisted by the cocycle f_R.
- 18:36-38: alpha in P(C) and conj(alpha) = f_infinity alpha; **epsilon(f_infinity) = -1** (boxed), so f_infinity != 1
  and R(alpha) = C as soon as M contains the Tate motive; f_infinity = 1 only if M is a sum of tensor powers of Q(2)
  [granting Hodge]; 18:37: the torsor P = Isom(T_B (x) R, T_DR) over G_R is the one given by the 1-cocycle f_infinity of
  Z/2 in G(C).
- 18:39-41: the Hodge decomposition phi does not depend on the isomorphism K = C; over a number field K, for each
  archimedean place T, H^{pq}_T and the real subspaces are vector spaces over K_r, the largest totally real subfield.
- Checked: epsilon(f_infinity) = -1 (complex conjugation reverses the orientation of P^1(C), so acts by -1 on H^2 =
  Q(-1)_B), and the Q(2) remark (conjugation acts on Q(n)_B by (-1)^n) (check events SA07-S3-3, -4). Known since: the real
  Frobenius F_infinity of Deligne ("Valeurs de fonctions L et périodes d'intégrales", Proc. Symp. Pure Math. 33, part 2,
  1979, 0.2.5; Tannakian categories over R: Deligne-Milne, Tannakian categories, LNM 900, §4).

## 4. Periods: "conjecture de transcendance N° 1" in its full form (18:6, 18:11-13, 18:45, 18:47-49) — SA07-2

- **18:11** (the centre). For a motive over k with motivic group G (dim g): the three comparison torsors
  P = Isom(T_B (x) k, T_DR), P' = Isom(T_DR, T_Hdg) containing the variety Q of Hodge splittings (Levi subgroups of the
  parabolic B' of the Hodge filtration; dim B' = b, unipotent radical U' of dim u, Levi L' of dim l, u + l = b), and
  P'' = Isom(T_Hdg, T_B (x) k); the period points alpha in P(C), beta in Q(C), gamma in P''(C) with beta alpha =
  gamma^-1; Fil (the variety of filtrations of T_B in the class of the Hodge filtration, dim g - b) and Big (bigradings,
  dim g - l), Big -> Fil a torsor under a unipotent group of dim u; phi = q(alpha) in Fil(C) (the period point),
  psi = r(gamma) in Big(C). With "(2 i pi)^n in k(alpha) si Q(-n) in Ob M", his conclusions:
  trdeg k(alpha)/k = g, trdeg k(beta)/k = u, trdeg k(gamma)/k = g, trdeg K/k(beta) = g, trdeg K/k(alpha) =
  trdeg K/k(gamma) = u (K = k(alpha, beta)), trdeg Q(phi)/Q = g - b, trdeg Q(psi)/Q = g - l.
  These are the "generic point" statements: each period point is a generic point of its variety over k. The first is
  Grothendieck's period conjecture as later written by André; the statements on beta (the Hodge splitting) and psi go
  beyond it.
- Checked: the numbers are consistent with each other and with the dimensions (u + l = b; trdeg K/k = g + u computed
  three ways) (check event SA07-S3-5).
- **18:12-13** test case, elliptic curves over Q̄ with G = GL(2) or the CM torus: a) is trdeg Q(g) = dim G (4 or 2)?
  b) does the locus of g generate G? c) the Hodge splitting gives h in C/Q̄: "Peut-on avoir h in Q̄, ou h est-il tjrs
  transcendant sur Q [cas où C n'a pas de multiplication complexe]". Known: a) in the CM case trdeg = 2 (Chudnovsky
  1976, algebraic independence of pi and a period); open for non-CM curves (only trdeg >= 2 known, Chudnovsky). c) see
  HUNCHES H1.
- **18:45**: C, C' non-CM, non-isogenous, A = C x C', G isogenous to SL2 x SL2 x G_m (dim 7), the Borel B of dim 5:
  "K de degré de transcendance <= 5 sur k ... et non pas égal à dim G - 1 = 6", for every embedding k in C. The field K
  is the one of 18:42 ("variation du réseau discret en termes d'une place archimédienne"): comparing the Betti lattices of
  two embeddings, the comparison fixes the Hodge filtration, so it lies in a Borel-type subgroup; his point is a bound
  by dim B, not dim G - 1. Status: his claim, reasoned on the page; not re-derived here (needs the definition of K on the
  pages before 18:45, which the transcription does not give in one place).
- **18:47-49**: for M over k algebraically closed in C, each place v gives a lattice M_v^Z in prod_l M(l); for places
  v_1, ..., v_n a point of [(prod P_i)/G](Q̂); the transcendence degree of that point is at most (n - 1) d (d = dim G),
  "au lieu de (n - 1) m^2"; granting "la conjecture de Tate renforcée" (Galois image of finite index in G(Ẑ)), the g_i can
  be made generic for every l, if one grants a lemma: in a coset P = U a of a compact open U in G(Q̂), G connected over Q,
  there is an element all of whose components are generic over Q. Checked: the lemma is true (check event SA07-S3-6:
  proper Q-subvarieties are countable and each meets the l-adic manifold G(Q_l) in a Haar-null set).
- **18:6**: a diagram with G(Q_p) in G(C), G'(C), an extension E of pi by G'(C) with two splittings sigma_1, sigma_2,
  chi: pi -> Q_p*, j_2: G_m(Q_p) -> G'(Q_p): phi(gamma) = sigma_1(gamma)^-1 sigma_2(gamma) = u(gamma) j_2(chi(gamma)^-1);
  Ker u is "connu", Pi_1 = pi / Ker u "est un groupe analytique p-adique" with chi_1: Pi_1 -> Q_p*. A reconstruction of
  the image of Galois from the two splittings (Hodge-Tate and the Galois one): see HUNCHES H3.

## 5. Mixed Hodge structures (18:9)

- The Tate twist of a mixed Hodge structure: W_i(E(n)) = W_{i+2n}(E), F^i(E(n)) = F^{i+n}(E), with
  Gr^W_i(E(-1)) = (Gr^W_i E)(-1). Checked against Deligne's convention (Hodge II, 2.1.13): agrees (check event SA07-S3-7).
  The page uses W increasing and F decreasing as in Hodge II, so it is 1970 or later.

## What is wrong, open, connected

- Wrong: nothing found on these pages. The transcription's question marks (133 + 268 open readings) do not touch the
  mathematics read above except "double viseur(?)" (18:5), which the mathematics supports.
- Open (his): the full period conjecture with the Hodge splitting (18:11); non-CM elliptic curves (18:13 a, c); the
  bound of 18:45; the integral comparison of Betti lattices for different embeddings (18:43, 18:47-49).
- Connected: SA07-1 (fibre functors), SA07-3 (the motivic category), SA05-8 (the motivic Galois group), SA05-21 (the
  Hodge group, letter to Mumford, 1965), SA15-18 (Hodge-Tate, cote 6), SA15-15 (p-adic cohomology, cote 7: problem 4 of
  18:43 is the cote 7 draft).
