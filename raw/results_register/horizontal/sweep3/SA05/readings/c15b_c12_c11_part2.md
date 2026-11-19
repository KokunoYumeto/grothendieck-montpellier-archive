# SA05 sweep 3, stretch c15b_c12_c11, part 2: cote 12, scans 51-149

Claude Opus 5.5 at effort max (agent ac391f829fcbd7a41), sweep 3 reader (c15b_c12_c11 part 2), launched by agent
a7b7747fd6dd29f87 (Claude Opus 5.5 at effort max), which was launched by agent a28ea31fa17dd65e1 (Claude Opus 5.5 at
effort max) at the main session's word. Started 19 Nov 2026 (UTC). Brief: `sweep3/READER_BRIEF.md`. Merged by
a7b7747fd6dd29f87 into `c15b_c12_c11.*`.

Packages read: `MPL_12_051-098` (Pro transcription, folder `MPL_12_051-098_unzipped`), `MPL_12_099-149` (folder
`MPL_12_099-149_unzipped`). Second witnesses: Codex web K12-04 to K12-09; Michel Hua's project
(`transcripts/12/12.modern.tex`, his page p = our scan p + 1), credited where used. Scans: `03_theorie_des_motifs/12.pdf`.

## Pages and state (kept current)

- Package 1 (51-98). His pages: 51, 53-57, 59-60, 62-65, 67, 71, 73-80, 82, 84, 86-95. Cancelled drafts: 52, 58.
  Reused typed: 61, 72. Cover: 96. Not in the folder: 66, 68-70, 81, 83, 85, 97-98 (not blank; item 22).
- Package 2 (99-149). His pages: 101, 104-109, 111-116, 118, 125, 127, 129, 131, 133, 135, 137, 140-142, 144-149.
  Covers: 99, 139, 143. Reused: 119 (a printed galley). 120 and 122, marked reused_typed in the inventory, are his
  pages on reused sheets (read as his). Not in the folder: 100, 102-103, 110, 117, 121, 123-124, 126, 128, 130, 132, 134,
  136, 138 (only 103, 110, 124 blank; item 22).
- State (19 Nov 2026): all assigned pages read (75 transcribed faces: 66 his pages, 34 + 32 counting 120 and 122; 2 cancelled
  drafts; 3 reused, 61, 72, 119; 4 covers); 41 check events, 24 corrections, 8 hunches. The scans absent from both packages are
  not all blank (item 22): 69 and 97-98 are his and untranscribed.

## Items, in page order

### 1. Weight and dimension-type bounds for H^i of a smooth variety (12:51, end of his §12) — SA05-9

- **Place.** 12:51 (the last page of §12, "L(K) -> M^+(K) and birational invariants", 12:42-51, part 1's pages). Notation
  from 12:30-35 (part 1's pages): M_i^+ = effective motives of weights <= i; D_i = the dimension-type (level) filtration,
  the smallest thick filtration above the weights that is stable under twisting by xi = Z(-1) (Michel Hua's project,
  section "La filtration par le niveau": "la plus petite filtration épaisse qui majore celle par le poids").
- **What he does.** For X smooth of dimension n over K: H^i_!(X) in M_i^+, "mieux" H^{n+k}_! in xi^k M^+_{n-k}; H^i(X) in
  D_i and in D_n; H^i(X) in M_i^+ + xi M_{i-1}^+ + ... (i <= n) and in xi^{i-n}[M^+_{2n-i} + xi M^+_{2n-i-1} + ...]
  (i >= n); cl H^i(X) in the sum of the Gr_alpha, i <= alpha <= min(2i, 2n); "plus gén.": with a coefficient M pure of
  weight rho, rho + i <= alpha <= rho + min(2i, 2n).
- **Checked.** Re-derived through the weight spectral sequence of a normal-crossing compactification and hard Lefschetz on
  the strata (check event). Right for the l-adic and Hodge realizations (Deligne, Hodge II, Publ. IHES 40 (1971), 8.2.4;
  Weil II, Publ. IHES 52 (1980), 3.3.1; locators unverified). The coefficient version needs his hypothesis "motif
  constant tordu" (written on 12:73): with unipotent local monodromy the upper bound fails (the Legendre-family example
  in the check event; the Pro notes N002 and N064 make the same point).
- **Wrong.** The circled insertion "et in Ob M_n^+(K)" for all i is false for i > n (correction). "Gr_i" for Gr_alpha is
  a slip of the pen, decided on the scan.
- **Open.** Nothing on the page. Motivically these bounds rest on the standard conjectures (SA05-2) and resolution.

### 2. Cancelled drafts 12:52 and 12:58

- 12:52: a cancelled draft of the end of §12 (the Albanese "à isogénie près" of a surface from its class in L(k); the maps
  L_i(K)/L_{i-1}(K) -> D_i M^+(K)/D_{i-1} M^+(K) and -> Z^{sigma_i(K)}, "injectif, ou bijectif, du moins mod torsion").
  12:58: a cancelled draft (xi-twists and a coniveau calculation; Pro note N014). Not studied.

### 3. Galois characterization of the filtrations (12:53-55, his §13) — SA05-9, with SA05-8

- **What he does.** M_l^+(X) is the ring of classes of twisted-constant Q_l-sheaves that come from motives; M^+(X) ->
  M_l^+(X) is bijective for X of finite type over Z, "car il résulte des conjectures de Tate" that non-isomorphic simple
  motives have realizations without a common simple factor. Then: cl(E) in M_i(X) iff every Frobenius eigenvalue at every
  closed point x has absolute value N(x)^{i/2} (margin "Conjectures de Weil et Riemann"); cl(E) in M^+(X) iff the
  characteristic polynomials of Frob_x^{-1} have integer coefficients (margin "Conjectures de Tate"); membership in D_i
  by twisting: 1) i = 0: E of even degree 2beta and E(beta) effective, i.e. the rho(x)/N(x)^beta are algebraic integers
  (N.B.: then roots of unity), equivalently pi_1(X) acts on T_l(E)(beta) through a finite quotient; 2) i >= 1: the
  largest twist that brings E to degree i-1 or i must be effective. 12:55: "comment caractériser T_l(E_i) ... du pt de
  vue Galoisien ?"; over a finite field "purement arithmétique en termes de Frobenius"; "cet énoncé ne se généralise
  guère via filtration de pi_1, comme on voit sur X = Spec corps fini".
- **Checked.** Injectivity from Tate + semisimplicity; the D_0 and D_i tests with Kronecker's theorem (check events).
- **Open (his).** Effectivity by integrality is a conjecture: over F_q it says that every Weil q-integer of weight w
  occurs in some H^w, the "conjecture forte" of 15:100-106 (SA06-9); weight 1 is Honda-Tate (hunch H2 on the weak form).
  The Galois characterization of the level-i part over a number field (12:55): hunch H3.

### 4. Galois invariants, commutation theorems, the Lie pro-motive (12:56-57, 12:59, his §14) — SA05-8

- **What he does.** For X proper smooth over K of finite type: Tate's conjecture H^{2i}(Xbar,Q_l(i))^pi = A^i(X/K) (x)
  Q_l, sharpened: the ring U^i(X/K) of algebraic correspondences acting in degree i is semisimple ("via Hodge"), U^i (x)
  Q_l is the commutant of pi in End H^i, and the enveloping algebra of pi is the commutant of U^i ("donc l'action de pi
  est semi-simple"); "le deuxième énoncé + injectivité ... entraîne tout". N.B.: this sees only the Q_l-spans of the
  algebraic data and only the enveloping algebra of the image of pi. Over all finite extensions: the same with the Lie
  algebra g_l(Kbar/K). Question: the image of g_l in End H^i, "une sous Algèbre de Lie réductive", inside
  H^{2n-i} (x) H^i(n). 12:59: for M semisimple, g_l -> End(M_l) should come from a motive g_M in Mcheck (x) M independent of
  l ("un motif en Algèbres de Lie"); over all M a canonical "promotif fondamental", constructible from the tensor
  category; "Quelle est la partie 'Algébrique' de ce promotif ?": all of it over a finite field, otherwise (he thinks)
  the scalars only.
- **Checked.** The double-commutant deduction (check event). For i = 1 and abelian varieties this is Faltings's theorem
  (Invent. Math. 73 (1983)) and, over finite fields, Tate's (Invent. Math. 2 (1966)); locators unverified.
- **Wrong.** His guess on the algebraic part fails over fields with a CM subfield and in characteristic p (check event,
  correction).
- **What it is (mine).** g_M is the Lie algebra of the motivic Galois group G_M, as a motive; the question on the image of
  g_l is the Mumford-Tate conjecture (Bogomolov 1980 for the algebraicity on abelian varieties; open in general).

### 5. Absolute cohomology: the requirements (12:60, 12:62-65, 12:67; his §15) — SA05-10

- **What he does.** Besides R f_*, "absolute" functors H^*(X,M) from RGamma_X: D^b(M(X)) -> D^b(Ab), with: 1) commutation
  with essentially affine limits (reduction to X of finite type over Z); 2) transitivity RGamma_X = RGamma_Y Rf_*
  (Leray); 3) H^i = 0 for i < 0, H^0(X,M) = Hom(Q_X(0),M), hyperext Ext^i(X;M,N) = H^i(X,RHom(M,N)), Hom = Ext^0 "par le
  n° 7", the hope that Ext^1 is the group of extension classes, and "Pourtant, je doute que les Ext^i (i>0) soient
  effaçables ..... [quid ... Ind-motifs ???]"; 4) maps to l-adic cohomology, isomorphisms after (x) Q_l for X of finite
  type over Z, H^i(X,M) of finite type over Q; "en particulier" H^i(k,M) = 0 for i > 0 over an algebraically closed k;
  N.B. no such precise relations over algebraically closed fields, "comme on voit par calcul explicite ... pour K
  clôture algébrique d'un corps fini". Tate's conjecture restated: A^i(X) (x) Q = Gamma_k(R^{2i} f_* Q_X(i)) and (boxed)
  A^i(X) = Im[H^{2i}(X,Q(i)) -> H^{2i}(X,Q_l(i))]; over Fbar_p: H^i(X,Q(j)) = 0 (i != 2j, 2j+1), A^j(X) (x) Q (i = 2j,
  canonical), A^j(X) (x) Q (i = 2j+1, "pas canonique"); over an algebraically closed field the image of H^j(X,Q(i)) in
  l-adic cohomology is zero for j != 2i ("question de poids"). 12:67: "th. de dualité absolue" for X of finite type over
  Z, regular of dimension n: values in Q(n)[2n+1], H^i(X,M) dual to Ext_!^{2n+1-i}(X;M,Q(n)), H^i_! dual to
  Ext^{2n+1-i}; no "!" when X is proper over Spec Z.
- **Checked.** The l-adic comparison is refuted as stated (X = Spec Z[1/l]); the vanishing over algebraically closed
  fields conflicts with his own finite-field computation (check events, corrections). The shift 2n+1 matches arithmetic
  duality with finite coefficients (Spec O_K: n = 1, H^3_c(X, mu_m) = Z/m; Milne, Arithmetic Duality Theorems, II.3,
  locator unverified); with Q coefficients the archimedean places and the odd-degree classes of 12:71 must be added,
  which the page does not do.
- **What it is (mine).** Over finite fields these requirements describe Lichtenbaum's Weil-étale cohomology with Q
  coefficients (hunch H1); in general the "absolute" theory with the l-adic comparison corrected at l is the
  Beilinson/Bloch-Kato picture.
- **Open (his).** Effaceability of the Ext^i (12:63); the comparison 4) as refined; absolute duality with Q coefficients.

### 6. Reused typed leaves 12:61 and 12:72

- 12:61: a cancelled typescript fragment of an EGA-style text ("par le changement de base X' -> X. On aura expliqué au
  préalable"). 12:72: an upside-down typescript of an EGA IV §11.9 draft ("une démonstration plus sympatique et
  élémentaire de 11.9.6. Quant à 11.9.3. (ii) ...", a lemma with "B_h libre sur A_h"). Not studied.

### 7. Absolute cohomology over a finite field: Hochschild-Serre and weights (12:71, 12:73) — SA05-10, SA05-9

- **What he does.** 12:71: X projective smooth geometrically connected over F_q: 0 -> H^{i-1}(Xbar,Q_l(j))_pi ->
  H^i(X,Q_l(j)) -> H^i(Xbar,Q_l(j))^pi -> 0; H^i = 0 unless i = 2j, 2j+1; i = 2j: Tate (A^j(X/k) (x) Q_l); i = 2j+1:
  coinvariants, "Tate + action semi-simple"; over all k_n: A^j(Xbar) (x) Q_l in degrees 2j and 2j+1; "du pt de vue
  motifs" H^{2j+1}(Xbar,Q(j)) = A^j(Xbar) (x) Q "mais pas canoniquement en k !", margin "Remplacer k par k_n revient à
  multiplier l'isom obtenu par n". 12:73: S smooth of finite type over F_p, M a twisted-constant motive of weight rho:
  H^i(S,M_l) = 0 unless -2i <= rho <= -i+1 (i >= 2), "-2 <= rho <= 1" (i = 1), rho = 0 (i = 0).
- **Checked.** Both (check events); 12:73's i = 1 line is a slip (correction).
- **What it is (mine).** The odd-degree classes, identified with A^j through a choice tied to the base field and scaled by
  n under k -> k_n, are the classes of Lichtenbaum's Weil-étale cohomology, cup product with the generator of
  H^1(W_k, Z) (hunch H1).

### 8. Rational points and the cohomology of abelian schemes (12:74-80, his §16) — SA05-10

- **What he does.** A_K over K of finite type, spread out to an abelian scheme A over S regular of finite type over Z,
  A_K(K) = A(S) finitely generated (Mordell-Weil-Néron-Lang). T_mot(A) = R^1 f*_* Q_{A*}(1), a twisted-constant motive on
  S, "pur de poids 1" (weight -1: correction), recovering A_K up to isogeny by Tate. Heuristic: A(S) (x) Q =
  H^1(S,T_mot(A)), H^0 = 0 by weights; through Kummer this is equivalent to the boxed "H^1(S,A)(l) fini si l premier à
  S", true for S = Spec F_q by Lang. 12:76-77: for S over F_p, Leray for S -> Spec F_p, A^fix -> R^0 f_* A -> M (M of finite
  type over Z), Lang for A^fix, the diagram (b) comparing the Kummer sequences over S and Sbar; 12:78: H^2(S,A) need not
  vanish (S a curve, A = J x S: H^2(S,T_l A) = End(J) (x) Q_l, "qui est non nul"); 12:79: H^1(S,A)(l) = H^1(Sbar,Abar)^pi(l)
  (margin "surj. à noyau fini"), so the conjecture says H^1(Sbar,Abar)(l)^pi is finite; "± équiv. (via des jacobiennes)"
  to Br(S) -> Br(X) surjective mod finite groups for a relative curve X/S; margins: H^i(S,A)(l) finite for i >= 3, "les
  seuls qui restent sont H^0 et H^2 pour A, et H^1, H^2 pour T_l(A)". 12:80: rank H^1(Sbar,T_l Abar)^pi = rank A(K),
  "essentiellement équivalente à la conjecture de Birch-Swinnerton Dyer".
- **Checked.** The Kummer equivalence; the weight -1 and its consequences; the curve example; the Brauer reformulation;
  the BSD form over function fields (check events).
- **Wrong.** The weight (correction). The boxed conjecture over arithmetic S with l invertible (refuted: X_0(11) over
  Spec Z[1/11l]); the sequences "-> 0" on 12:76-77 and "H^1(F_p,M) = (M (x) Q/Z)^pi" (12:76; he corrects it himself on
  12:79). None of these touches his conclusion over F_p.
- **What is proved, what is open.** Over F_p: the equivalences "A(S)(x)Q = H^1(S,T_mot) <=> H^1(S,A)(l) finite <=>
  H^1(Sbar,Abar)(l)^pi finite <=> rank = dim of the invariants" are right (the last with semisimplicity at 1); the
  statements themselves are Tate's conjecture/BSD over function fields (Tate 1966; Milne, Annals 102 (1975); known for
  example when the Tate conjecture holds for the associated surface; locators unverified). Open (his): the conjecture
  itself; the Brauer surjectivity (12:79, "Prouver que ... ??").
- **Sweep-2 flag N037/N041** ("a later vanishing contradicts the degree-two example"): the example here is 12:78; the
  later page is 12:82 (decided under item 9).

### 9. A curve over a finite field: H^i(C,A) and a punctured curve (12:82) — SA05-10; sweep-2 flag N037/N041 decided

- **What he does.** C smooth proper over F_q, A an abelian scheme over C: "Des conjectures de Weil, résulte que
  H^i(C,A) = 0 si i >= 2 et sans doute, utilisant Tate, on doit avoir H^1(C,A) = 0"; for U = C - {x}, H^1(U,A) =
  H^2_x(C,A) = H^1(K_x,A), dual of H^0(K_x,A*) "par Tate", "donc essentiellement un p-groupe, modulo groupe fini ! OK.";
  generalizes to X regular minus a regular divisor.
- **Decided.** The ink has "i >= 2". The flag is right: 12:78 is right and 12:82 is wrong at i = 2 (check event,
  correction); Michel Hua's project reaches the same verdict. "H^1(C,A) = 0" should be "finite". His conclusion survives:
  H^2_x(C,A)(l) is finite, so H^1(U,A)(l) is finite iff H^1(C,A)(l) is.

### 10. Computations for Q_l(1) and G_m (12:84) — SA05-10

- **What he does.** X of finite type over Z: H^0(X,Q_l(1)) = 0; H^3(X,Q_l(1)) = T_l H^3(X,G_m), "p.ex. Z_l" for a curve over
  F_p; H^i(X,Q_l(1)) = T_l H^i(X,G_m) = 0 for i >= 4 "??"; Artin's conjecture: H^2(X,G_m) finite for X proper over Z,
  "Vrai si X courbe projective lisse sur F_p, mais faux quand on lui enlève des pts --- le rang du H^2 augmente
  d'autant"; how big is H^3(X,Q_l(1)) ("il décroît en passant à un ouvert").
- **Checked.** The curve case and the open curves (corank r - 1 for r points removed); the vanishing for i >= 4 over F_p
  by weights (check event). Open: Artin's conjecture (the Brauer group of a proper scheme over Z is finite); his
  question on H^3 for arithmetic X.

### 11. Positive forms (12:86-89, his §17) — SA05-11

- **What he does.** Over k algebraically closed, semisimple motives pure of weight rho; Phi(M) = Gamma_k Hom(M (x) M,
  Q(-rho)), the symmetric (rho even) or alternating (rho odd) part Phi^s(M); Phi^s(M) (x) Phi^s(N) -> Phi^s(M (x) N),
  injective, not bijective; Phi^s(M' x M'') = Phi^s(M') x Phi^s(M'') x B(M',M''); a closed convex cone Phi^+(M) with
  (i) nonempty interior, (ii) interior = nondegenerate ("pseudo-amples", "amples"), (iii) pull-back along M -> N,
  (iv) ample restricts to ample on a subobject, so N = M + M^perp, (v) sums, (vi) tensor products, (vii) rho = 0:
  ample = positive definite, (viii) Phi^s(Q(rho)) = Q with ample = positive. Consequences: twist invariance, positive
  definiteness on Gamma_k M for rho = 0, reduction to isotypic pieces I (x)_A V with A = End(I) a division algebra.
- **Checked.** All the consequences (check event). These are the axioms of a polarization of a Tannakian category
  (Saavedra 1972; Deligne-Milne 1982, §5); over C the polarizations of a pure Hodge structure satisfy them (Hodge-Riemann).
- **Wrong.** The cross-term target Q(rho) for Q(-rho); "(iv) et (vi)" for (iv) and (vii) (corrections, slips).
- **Open (his).** That motives carry such cones: the Hodge standard conjecture (SA05-2), known in characteristic 0 through
  Hodge theory for the homological motives that are known to be semisimple, open in characteristic p beyond surfaces.

### 12. The dictionary: L-functions and cohomology with Galois action (12:90-95) — SA05-10, SA05-9

- **What he does.** The pre-lambda-ring R(N;k) of finite projective k-modules with an endomorphism; P(t) = det(t - f),
  Q(t) = det(1 - tf); L(V,f) = 1/det(1 - ft) gives R(N;k) -> 1 + k[[t]]^+, "injectif" for k a field (unique
  factorization); Lambda = L'/L = (1/t) sum Tr(f^n) t^n, invertible by exp of the integral in characteristic 0, not
  injective in characteristic p. By the Lefschetz-Weil-Grothendieck formula, L(X,F) over F_p is the image of chi(F) =
  sum (-1)^i cl H^i_!(Xbar,F); with the Weil conjectures it splits into the weight pieces h^i(F) (zeros and poles grouped
  by absolute value); for X complete smooth and F twisted of weight rho, h^i(F) = H^{i-rho}. Removing a closed set of
  dim < n changes L by factors of weight <= 2n-2+rho (margin: the weights of "la bonne filtration N° 12"); the birational
  invariant L(X,F) mod weight <= 2n-2+rho is cl H^{2n}_! - cl H^{2n-1}_!; for F = Q_l: pi_0(Xbar) as a Frobenius set and
  the Albanese (margin "Modulo conjectures de Tate"); with the levels one recovers more, the "invariants birationnels
  fondamentaux" of the notes on motives. Question (12:95): for f: X -> Y smooth proper and F twisted-constant, does L(X,F)
  modulo the L(f^{-1}(Y'),F) recover the fundamental birational invariants of the generic fibre; which hypotheses are
  needed "??".
- **Checked.** The traces formula and inversion; the weight bookkeeping; the coarse invariant (check events).
- **Wrong.** The injectivity misses the nilpotent classes (refined: f invertible); "poids 2n" for 2n + rho.
- **Open (his).** The relative question of 12:95.

### 13. Cover 12:96

- "Poids et niveaux des espaces de cohomologie l-adiques (base var. quelconque)": the cover of the dossier that follows
  (12:101-118, item 14). Pro note N061.

### 14. Plan of an article: "Filtration et poids des espaces de cohomologie des variétés algébriques" (12:99) — SA05-9

- Cover sheet with a plan: 0. Introduction; 1. weights and levels for a pro-Galois module over a field; 2. a scheme minus a
  normal-crossing divisor; 3-5. weights and levels of H^i (X smooth), H^i_! (X separated), H^i (X arbitrary); 6. X proper:
  the largest quotient of weight i, resolution; 7. X proper smooth: filtration by levels, Serre's virtual Betti
  numbers; 8. counterexamples; 9. twisted coefficients. References: SGA 4, "P. Deligne / Hodge", Tate's conjectures,
  "Kleimann(?) conj. standard", Weil, "Deligne-Grothendieck SGA 7". The references date the dossier to about 1968-1970
  or later (Deligne's Hodge theory, SGA 7; Deligne's degeneration theorem is used on 12:108, 12:114).

### 15. An example sheet: P^2 minus curves (12:101) and weights/levels of H^1, H^2 (12:104) — SA05-9

- 12:101: X = P^2 - T', Y = T - T', U = P^2 - T (T connected, T' disconnected, in the smooth locus, each component of T'
  meeting ... in at most one point): diagrams of H^1_!, H^0 and the normalization Ytilde, an injectivity "inj?" left
  open. 12:104: tables: H^1 has pieces (weight 0, level 0), (1,1), (2,0) (proper case or H^1_!: weights 0, 1; smooth
  case: 1, 2); H^2 weights 0..4 with levels 0,1,2,1,0; "morceaux purs sont semi-simples"; the pure piece of weight 2 is
  an extension by a Tate motive Q(-1)^r; for H^2_! "il semble qu'il puisse y avoir mélange de poids dans le mauvais
  ordre" (an extension of an effective motive of weight 0 by one of weight 1). The tables agree with item 16 (weights
  i..2i and levels for H^i of a smooth variety; 0..i for H^i_!). The "wrong order" remark is a question he does not
  settle; in the weight filtration of mixed theory the order is fixed (W_k increasing), so a non-split extension of a
  weight-0 piece by a weight-1 piece in the "wrong" direction cannot occur in a mixed structure (Deligne, Hodge II):
  hunch H5.

### 16. Weights and levels of l-adic cohomology of singular or open varieties (12:105-110) — SA05-9

- **What he does.** A) constant coefficients over a field (resolution admitted): 1) X smooth quasi-projective: Proposition 1
  (H^i_! of weights 0..i; weight i = image in H^i(X'); for i >= n weights 2(i-n)..i, levels 0..2n-i), Remark (the
  filtration is the weight filtration, independent of the compactification; degeneration for weight reasons), the two
  tables, Corollaire 1 by duality (H^i of weights i..2n with levels 2n-i..0 for i >= n; weights i..2i with levels i..0
  for i <= n; margins "tous les morceaux ... effectifs", "niveau <= Inf(i,n)"); 2) smooth non-quasi-projective (Nagata;
  for non-separated X only H^i, through a Cech spectral sequence; margin "Question le niveau ne serait-il <= 2n-i ?");
  3) H^i_! for X singular separated: effective, weights <= i, level <= Inf(i,2n-i); 4) H^i for X singular: effective,
  weights <= 2i, level <= i and <= n. B) twisted coefficients on smooth X: F = R^j g_* Q_l, Leray degenerates "D'après
  Deligne", H^i(X,F) a piece of H^{i+j}(Y): weights i+j..2n+2j, levels 2n-i+j..0; margin questions (2n+j? 2i+j? weights
  of H^i_! >= j?); X proper: H^i(X,F) pure of weight i+j "(et semi-simple ici...)". 12:109: Zariski-local "sympathique"
  coefficients via compact supports and duality; C) arbitrary X with effective coefficients of weight and level j.
- **Checked.** Proposition 1, Corollaire 1, A 3) and A 4), B 1) (check events).
- **Wrong.** C) 2) omits j (correction). His three margin questions on 12:108 have negative answers (Legendre family;
  check event), which he does not settle.
- **Status.** Known: these are Deligne's theorems on the weights of the cohomology of arbitrary varieties (Hodge III,
  8.2.4; Weil II, 3.3); the level statements are the Hodge-number bounds of Hodge III 8.2.4 read through the generalized
  Hodge conjecture (for the coniveau reading of "niveau") — open in that reading, known for Hodge numbers.

### 17. Admissible l-adic sheaves and virtual motives (12:111-115) — SA05-9, SA05-13

- **What he does.** l fixed, schemes prime to l, constructible Q_l-sheaves. 2.1 special of weight i (a twisted-constant
  subquotient of R^i f_* Q_l, f projective smooth of relative dimension i); Lemma 2.2 a)-e) with proofs (disjoint unions,
  Künneth, base change, Lefschetz, Q_l(-i) = R^{2i} of P^i); Cor. 2.3. 3.1 effectively admissible sheaves (filtrations
  with pieces i_!(G), G special after a finite radicial extension), weights in Phi; 3.2-3.3 stability, tensor products,
  duality; 4.1-4.2 levels. Théorème 5.1: R^i_! f_* of a strictly special F of weight j is effectively admissible with
  weights <= i+j, levels <= Inf(i+j,2n-i+j), the table for i >= n (margins: Lefschetz, Deligne, strong resolution for
  the perfect closures of the residue fields, "1/2 simplicité arithmétique ?"). 5.2 with the semisimplicity part of Tate;
  5.3 without it; 5.4 the dual statement for R^i f_* on smooth X; 6. the general R^nu f_*, starting with an immersion.
- **Checked.** 2.2-4.2 and 5.1 (check events). **Wrong.** 3.3 d) "{n - i}" for {2n - i}; 2.1 "localement constant"
  needs finite monodromy (corrections).
- **Decided.** The sweep-2 flag on 5.4's level bound: the ink and the mathematics give 2n-i+j (check event, correction).
- **What it is (mine).** A theory of "effective mixed sheaves with weights and levels" built from geometric pieces, in
  the spirit of what became Deligne's mixed sheaves (Weil II, 1.2) and Beilinson-Bernstein-Deligne-Gabber's "faisceaux
  d'origine géométrique" (Astérisque 100, 6.2.4; locator unverified), with an extra level filtration that the later theory
  does not have; hunch H6.
- **Open (his).** 5.2 needs the semisimplicity part of Tate's conjecture; the level statements need the (generalized)
  standard conjectures for their motivic meaning.

### 18. The immersion case: worksheets (12:116, 12:118, 12:120, 12:122) — SA05-9

- **What he does.** 12:116: §6, R^nu f_* of an effectively admissible sheaf, starting with an open immersion f: X -> Y, X
  regular: Y' -> Y a resolution with Y' - X a normal-crossing divisor Z = sum Z_i, R^q g_* Q_l = sum over i_1 < ... < i_q
  of Q_l on Z_{i_1} cap ... cap Z_{i_q}, twisted by (-q), pure of weight 2q (purity); bounds for E_2^{pq}. 12:118: tables of
  weights and levels of the E_2^{i-q,q}, summary for i <= n-1 (weights 0..2i, levels 0..i..0); i >= n. 12:120: the table
  for i >= n (weights 2(i-n)+2..2n, levels 0..2n-i-1..0), the summary by i (levels <= Inf(i,n-1), weights <= 2Inf(i,n));
  for F strictly special of weight j "poids <= 2Inf(i,n) + j ?", levels <= Inf(i,n-1) + j; the general case conjectured with
  n = d_y(f) (a local relative dimension), margin "peut-on remplacer par n-1 si f de dim <= n-1 ?". 12:122: F strictly
  special of weight j, X regular, F = R^j p_* Q_l: Deligne's degeneration makes R^i f_*(F) a piece of R^{i+j}(fp)_*; Y' of
  dimension <= n+j (the page stops).
- **Checked.** The i <= n-1 summary (check event). **Wrong.** "+ j" for "+ 2j" in the weight bound (Legendre family at a
  cusp; check event, correction); his own 12:122 points to 2j.
- **Open (his).** The general relation with the local dimension d_y(f) (12:120), as a conjecture; his margin question.

### 19. Dévissage of Q_l-sheaves (12:125-137) — SA05-9

- **What he does.** Q_l-sheaves admissible of type <= d (locally a filtration whose graded pieces are essentially constant
  subquotients of R^n g_* Q_l, g projective smooth with connected fibres of dimension <= d); Lemma 1 (thick abelian
  subcategory), Lemma 2 (inverse images), Lemma 3 (R^i_! f of type <= d+d' for f of relative dimension <= d'; induction,
  a dense smooth open, Artin's factorization down to curves, resolution of V), Proposition 4 (R^n i_* for an open
  immersion into an excellent X of dimension <= d: (d+d'-1)-admissible; noetherian induction, resolution to a
  normal-crossing complement, purity for Q_l, then the general F as a factor of R^n f_* Q_l with fibres of dimension 1).
- **Checked.** The steps listed in the check event; the use of the "th. de complète réductibilité" (semisimplicity) is
  where the proof is conditional. **What it is (mine).** Hunch H6.

### 20. Smooth integral motives over a base (12:140-142) — SA05-13

- **What he does.** S normal integral, generic point Spec K. A smooth isomotive: a semisimple isomotive over K with T_l(M)
  unramified over S[1/l] for every l; "Conjecturalement, il suffit que ce soit vrai pour un l premier à toutes les car.
  résiduelles (=> il suffit ... pour deux l != l')". A smooth motive (char K = 0): (M, {E_l}, {alpha_l}) with E_l
  twisted-constant l-adic sheaves on S[1/l] and alpha_l: E_l (x) Q_l = T_l(M), integral for almost all l; morphisms;
  N.B.: fully faithful into motives over K, Hom of finite type over Z, abelian, thick image, exact functor to isomotives.
  12:141: finite commutative groups unramified at each S[1/l] form a thick subcategory with quotient the smooth
  isomotives; tensor structure; isogenies; R^i f_*(Z_X) for X proper smooth over S; the contravariant functor phi from
  commutative group schemes A (abelian scheme A^0 with finite A/A^0): M = R^1 f_* Q, E_l = Hom(A[l^infty], Q_l/Z_l).
  12:142: phi fully faithful; essential image = the motives whose quotient mod torsion comes from an abelian scheme; this
  needs M effective of weight 1, and sufficiency is the question "T_l(A) unramified over S_l for all l => good reduction
  over S": true for dim S = 1 (Néron-Ogg-Shafarevich) or in characteristic 0, "mais peut-être pas en général [précisément
  local régulier de dim 2 d'inégales caractéristiques]"; a counterexample would come from a finite subgroup of A_K not
  extending to a finite flat subgroup of A, and then one of prime order. Margin "Pb": with this definition, pull-backs
  (fibres at s in S) are not defined, already for effective motives of weight 1.
- **Checked.** The two-primes deduction; the reduction to non-extending subgroups; full faithfulness (check events).
- **Open (his).** The one-prime independence conjecture (known for abelian varieties); good reduction over regular local
  bases of dimension 2 in mixed characteristic (hunch H7); the definition of fibres of smooth motives (his "Pb"), the
  problem that relative motives were later built to solve.

### 21. Abstract semisimple motives: pseudo-abelian envelopes (12:143-149) — SA05-12

- **What he does.** Cover 12:143 "Enveloppes pseudo-abéliennes de catégories multiplicatives (Construction abstraite de
  Catégories de motifs)". 12:144-146: the universal problem (additive functors V° -> C into abelian categories, exact
  functors from M); for V Q-linear with finite-dimensional semisimple End(X): M^# of pairs (X, pi), the fully faithful
  h^#, the equivalence Fonc add(M,C) -> Fonc add(V,C) with quasi-inverse Im H(pi) (margin: C additive with split
  idempotents suffices). 12:147-148: M is abelian semisimple: (i) chain conditions, (ii) "Tout morphisme u: P -> Q est
  « direct »", proved through R = P x Q and the regularity of semisimple rings (vu = pi, uv = varpi). 12:149: bi-additive
  functors extend; a symmetric associative unital box on V gives (x) on M; in characteristic 0 all covariant tensor
  operations (wedge^n, S^n).
- **Checked.** All of it (check events); the sweep-2 flag on (ii) is decided for our reading "morphisme".
- **What it is.** Jannsen's lemma (1992) and the Karoubi envelope; with V = numerical correspondences it gives Jannsen's
  semisimple category of numerical motives (Invent. Math. 107 (1992)), which Grothendieck's construction anticipates.

### 22. Reused and typed leaves in 12:99-149, and the scans outside both packages

- In the packages: 12:119, a printed galley "Lecture Notes in Mathematics 41, Local Cohomology, A Seminar given by A.
  Grothendieck, Notes by R. Hartshorne, 1967", margin "20.3.68 1. Korrektur" (reused; not studied). 12:120 and 12:122 are
  marked "reused_typed" in the inventory, but the scanned faces are his manuscript calculations (items 18); the typed
  matter is on the reverse (Pro note on 12:120-122). 12:139 and 12:143 covers.
- Outside both packages and outside Codex web K12-04 to K12-09, not blank (check event; not transcribed by us): 12:69 his
  page (absolute duality over F_p, continuing 12:67); 12:97-98 his typescript "Filtration et poids des espaces de
  cohomologie des variétés algébriques par A. GROTHENDIECK", 0. Introduction (the article of 12:99); 12:121, 12:123 a typed
  report (points 4-5: the theory of motives; the lambda-structure on K'(X) from perfect complexes, "le plus important
  problème resté en suspens" of the IHES seminar 1966/67), author not determined; 12:100, 12:102 an English typescript "2.
  Formalism of Algebraic Cohomology Classes" with handwritten corrections; 12:117 a typed message dated 27 March 1968
  addressed to "Monsieur GROTHENDIECK" (dates the sheets around 12:116-120 to 1968 or later, with the galley of 12:119);
  12:66, 12:68, 12:81 cancelled EGA IV draft typescripts; 12:70, 12:83, 12:85 typescripts not identified; 12:126-138 (even)
  a Bourbaki draft "§ 3. Groupes engendrés par des réflexions"; 12:103, 12:110, 12:124 blank.

## Hunches

- **H1 (SA05-10).** His absolute cohomology over a finite field, with H^{2j+1}(X,Q(j)) = A^j(X) (x) Q "pas canonique" and
  the factor n under k -> k_n (12:65, 12:71), is Lichtenbaum's Weil-étale cohomology with Q coefficients: H^{2j+1}_W =
  H^{2j}_W cup e, e the generator of H^1(W_k,Z) = Z (Frobenius), and restriction to k_n sends e to n e_n (Lichtenbaum,
  Compositio 141 (2005); Geisser, Math. Ann. 330 (2004); locators unverified). His 12:79 warning "Attention ... coh.
  galoisienne de Zhat !" is the Weil-group/Galois-group distinction that the Weil-étale topology was made to handle.
  Over arithmetic bases his l-adic comparisons (12:63-64, 12:75) need the Bloch-Kato condition at l (the refutations
  above); the corrected statements are the Bloch-Kato/Beilinson conjectures and the Weil-étale programme (Flach-Morin).
- **H2 (SA05-9, SA06-9).** The weak form of "effective iff integral eigenvalues" over F_q (12:54) follows from
  Honda-Tate: for a Weil q-integer pi of weight w, split the slopes equally, s(P)/w at each P over p; after raising to a
  power that makes the valuations integral and the ideal principal, a Weil q^m-integer pi_1 of weight 1 exists with
  pi^{mN} = pi_1^{wN}, so pi^{mN} occurs in H^w(A^w) for the abelian variety A of pi_1. The step to verify is the
  existence half of Tate's argument (Sém. Bourbaki 352 (1968), locator unverified). The strong form (no power) is the
  open "conjecture forte" of 15:100-106.
- **H3 (SA05-9).** The Galois characterization of the level asked on 12:55: over a number field, through p-adic Hodge
  theory (the spread of the Hodge-Tate weights at a place over p), conditional on the generalized Hodge conjecture and
  Fontaine-Mazur; over finite fields, through Newton polygons (Mazur's "Newton above Hodge"; Ogus). Not checked.
- **H4 (SA05-8).** Hom(Z(0), g) for the fundamental Lie pro-motive (12:59) is Lie Z(G_K), isomorphic to the
  Gamma_K-invariants of the Lie algebra of the Serre group of Q^cm: of dimension 1 + [E:Q]/2 for E the largest CM subfield
  of K, and 1 when K has none (conditional on the motivic Galois group being pro-reductive with abelianization the Serre
  group, as Deligne's theorem on Hodge cycles on CM abelian varieties gives in the absolute Hodge setting).
- **H5 (SA05-9).** The worry of 12:104 ("mélange de poids dans le mauvais ordre" in H^2_!) is excluded by Deligne's
  weight filtration: it is increasing and morphisms are strict for it, so an extension with a weight-1 subobject and a
  weight-0 quotient splits (Hodge II). Settled since.
- **H6 (SA05-9).** The "special/admissible" sheaves of 12:111-137 are the sheaves of geometric origin of
  Beilinson-Bernstein-Deligne-Gabber (Astérisque 100, 6.2.4; locator unverified) with an extra level filtration; his
  Proposition 4 (stability under Rj_*) is their 6.1.2-type stability, in characteristic 0 with resolution, in
  characteristic p later through alterations.
- **H7 (SA05-13).** His suspected failure of the good-reduction criterion over regular local rings of dimension 2 in
  mixed characteristic (12:142) is the extension problem of abelian schemes studied by Vasiu and Zink (Doc. Math. 15
  (2010), "Purity results for p-divisible groups and abelian schemes over regular bases of mixed characteristic";
  locator unverified), who prove extension for "healthy" regular schemes; I cannot settle the general case from memory.
  His reduction to finite subgroups that do not extend is the right test.
- **H8 (SA05-11).** The axioms (i)-(viii) of 12:87-88 are exactly a "graded polarization" (Saavedra VI; Deligne-Milne
  §5). Over a finite field the positivity of the forms of weight 0 on Gamma_k M is the Hodge standard conjecture in
  disguise; his isotypic reduction I (x)_A V turns it into positivity of a hermitian form over the division algebra A with
  its Rosati-type involution.

## Dependencies (ids from sweep2/SA05/WHAT_IS_WHERE.md)

- 12:51 uses SA05-9 (weights M_i^+ and levels D_i, 12:30-35, part 1's pages) and SA05-12 (motives over X).
- 12:53-55 use SA05-8 (realizations, Tate), SA05-9; 12:54 is the finite-field "conjecture forte" of SA06-9 (15:100-106).
- 12:56-59 use SA05-8, SA05-2 (standard conjecture B for semisimplicity "via Hodge"), SA05-11; 12:57 N.B. a)-b) (only
  Q_l-spans and enveloping algebras are characterized) is the linear-versus-nonlinear distinction of SA05-14.
- 12:60-73 (SA05-10) use SA05-12 ("par le n° 7": Hom = Ext^0), SA05-9 (weights, 12:51 -> 12:73), SA05-18 (Frobenius and
  weights over finite fields).
- 12:74-84 (SA05-10) use 12:73 (weights), Tate's theorem for abelian varieties over finite fields (Tate 1966), Lang's
  theorem, local duality; the Brauer reformulation links to cote 15:173-178 (absolute cohomology of Z(n), SA05-10).
- 12:86-89 (SA05-11) use SA05-2 (Hodge-type standard conjecture), SA05-12 (semisimple motives).
- 12:90-95 (SA05-10, SA05-9) use §12's "invariants birationnels fondamentaux" (12:42-51, part 1's pages).
- 12:99-122 (SA05-9) use SA05-2 (hard Lefschetz, "Lefschetz fort"), Deligne's degeneration and Hodge theory, resolution.
- 12:125-137 (SA05-9) use SA05-9 and semisimplicity (SA05-8); 12:140-142 (SA05-13) use SA05-8, SA05-12 and Néron models.
- 12:143-149 (SA05-12) use SA05-1 (correspondences) and SA05-11 (semisimplicity); used by SA05-8 (tensor structure).
- SA05-16 (the cote 16 programme): no explicit reference on these pages; the only contact is the use of hard Lefschetz.
  SA05-15 (Oda): not mentioned by him on these pages (Pro note N063 adds it).

## Deliverable state

- **Passes.** Pro transcription packages MPL_12_051-098 (frozen 17 Nov 2026) and MPL_12_099-149 (ChatGPT Pro mode; the
  model and effort are in the package register, which I did not open); Codex web K12-04 to K12-09 (GPT-6.2 Astra at
  reasoning effort max, ChatGPT Work), covering the same scans; Michel Hua's project's modernised reading as a witness;
  this sweep-3 reading (Claude Opus 5.5 at effort max), with 41 check events and 24 corrections.
- **Readings decided on the scans here.** 12:51 (Gr_i, 2n), 12:65 (A^j), 12:73 (rho <= 1 in the ink, slip), 12:76,
  12:82 ("i >= 2"), 12:87 (Q(rho)), 12:89 ((vi)), 12:115 (2n-i+j, sweep-2 flag decided), 12:148 ("morphisme", sweep-2
  flag decided). Open readings left: the xi/zeta alternatives of 12:51-58 (Pro doubts), the struck words at the end of
  12:59, 12:112 3.3 d) ("n-i" or "2n-i" in the ink), 12:122 ("2Inf(2q,...)"), 12:148 ("pr_2"), and the Pro doubts files.
- **Not complete.** The packages omit non-blank scans (item 22): his 12:69 and 12:97-98 must be transcribed before cote 12
  can be edited as a whole; the typed report 12:121/123 and the English typescript 12:100/102 should at least be
  identified in the edition. The transcribed pages are ready to be edited as a transcription edition, with the corrections
  above entered as apparatus notes (his slips and errors are kept in the text and noted, never normalized).

## Not yet read

- None of my assigned pages. The omitted scans of item 22 were identified on the images, not transcribed or studied.
