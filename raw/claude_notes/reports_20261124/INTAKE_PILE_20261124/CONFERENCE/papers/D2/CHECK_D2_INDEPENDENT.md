# Independent check of D2, "Classifying spaces of finite monoids with bounded homology"

Checker: abe075dcdd909eea0 (Claude Opus 5.5 at effort max), 25 Nov 2026, on the brief of the main session 329fb1e6
(Claude Opus 5.5 at effort max), `agent_notes/abe075dc_D2_CHECK_BRIEF_20261125.md`. The paper was written by
afceadd46f7598ec4 (Claude Fable 5.2 at effort max) and revised after the literature gate of a848636d0bbf3ae4b (Claude
Fable 5.2 at effort max). I did not write any part of it and did not edit it. I am a different Claude model, not a
different model family: this check does not replace the re-proof by another model family named in `PROVENANCE.md`.

Checked text: `src/D2_paper.tex` as of 25 Nov 2026 (891 lines, 46,330 bytes). Line numbers below refer to that file.
Numbering is that of the built paper (`src/D2_paper.aux`).

## 1. Verdicts

| Statement | Verdict |
|---|---|
| Theorem 2.1 [thm:K], in the new form (finite skeleta, local at p, lens spaces) | **correct**; every step checked; (K1), (K2), (K3) confirmed in Atiyah 1961 |
| Corollary 2.2 [cor:finitepi] | correct |
| Remark 2.3 (a) (Miller; the example Z/p² → Z/p) | correct; Miller's Theorem B and Theorem 10.1 opened |
| Remark 2.3 (b) (Palmer-Wu) | correct, with one unstated standard step (type F_n for every n ⇒ one classifying space with finite skeleta), see R6 |
| Lemma 3.1 (a), (b), (c) [lem:known] | correct; (c) direct argument checked; Sweeney Lemma 2.1 and Steinberg p. 7 opened |
| Lemma 3.2 [lem:je] | correct |
| Theorem 1.1 [thm:main], including the passage from H_k(M; F_p) to H^q(BM; Z_(p)) | correct |
| Theorem 1.2 [thm:equiv], including (iii) ⇒ (i) | correct; Hatcher Proposition 4C.1 opened |
| Corollary 3.3 [cor:swan] | correct |
| Corollary 3.4 [cor:cd], new form (H = eMe trivial) | **correct**; the free action of H on eM checked; Gray-Pride Lemmas 2-4, Theorem 2 and Swan Corollary 1 opened |
| Remark 3.5 [rem:cd] | correct; Gray-Steinberg Theorem 6.27 and Corollary 6.7 opened; one observation added (§2.6) |
| Theorem 1.3 [thm:BB] | statement matches Ben-Bassat's Theorem C (aperiodic included); his proof not read by me |
| Corollary 1.4 [cor:class] | correct |
| Corollary 1.5 [cor:conj] | main claim correct (RP² is a counterexample; quotation of Conjecture 7.1 verbatim); **the last clause is wrong as worded**: "every connected finite CW complex with non-trivial fundamental group" includes complexes with infinite fundamental group, which do not satisfy the conjecture's hypothesis. Repair R1 |
| Remark 4.1 [rem:onlyv1] | correct; Carcacía-Campos Theorem 6.2 and its proof opened |
| Remark 5.1 [rem:rational] | correct |
| Proposition 5.2 [prop:M6] (a), (b), (c) | correct; recomputed by my own program, including the sphere maps s_n |
| Proposition 5.3 [prop:M23] | correct; recomputed by my own program; homology mod p also computed by a method that does not use the paper's resolution |

No mathematical error was found in any proof. One statement is wrong as worded (Corollary 1.5, last clause); the other
repairs are citation precision, credit and records.

## 2. The proofs, item by item

### 2.1 My own attempt before reading the proofs

Before reading Sections 2-3 I wrote down proofs of Theorems 1.1 and 1.2 from Theorem 2.1 (finitely generated
homology, universal coefficients, the map B(eMe) → BM onto U(M), Sylow subgroups) and the idea of Theorem 2.1 (the flat
bundle of ρ, Atiyah's theorem for a cyclic p-group, nilpotence of the reduced class forced by the cohomological
bound). These agree with the paper's routes. For Corollary 3.4 I had only the idea that H acts freely on eM; the
paper's proof supplies the rest. Notes: `agent_notes/abe075dcdd909eea0_NOTES.md`, D2 section.

### 2.2 Theorem 2.1 (lines 203-276) and (K1)-(K3) (lines 166-201)

- **(K1), (K2).** With K_q(Y) = ker(K(Y) → K(Y^{q-1})): Atiyah 1961, §2, defines exactly this filtration and states
  that it makes K(X) a filtered ring (K_p · K_q ⊂ K_{p+q}); (2.2) gives K_{2q-1} = K_{2q}, so the odd quotients vanish;
  Proposition (2.4) gives the spectral sequence with E_2 = H^p(X; Z) and E_∞ = K_p/K_{p+1}, so the even quotients are
  subquotients of H^q(Y; Z). Both properties hold as stated. Atiyah-Hirzebruch 1961 was not opened (not on our disk).
- **(K3).** Atiyah (8.1): for G cyclic, α: R(G)^ → K(B_G) is an isomorphism of filtered groups, where K(B_G) is the
  inverse limit over finite skeleta (Atiyah §7). Atiyah (6.11): if G is a p-group, R(G) → R(G)^ is a monomorphism.
  The lens-space skeleta L^{2j+1} are cofinal among the skeleta of the CW structure on L = S^∞/C, and α_j is Atiyah's α
  restricted to L^{2j+1}. So (K3) holds and is correctly attributed.
- **Lens spaces.** Hatcher, Example 2.43: one cell in each dimension, cellular boundary maps alternately 0 and
  multiplication by the order, the infinite lens space a K(Z_m, 1). The cohomology stated in the paper (Z/p^a in even
  degrees 2 ≤ q ≤ 2j, zero in odd degrees below 2j+1) follows from that cellular complex; Hatcher states the homology,
  not the cohomology (R4, optional).
- **Set-up.** The map L → BG (Hatcher Proposition 1B.9, opened), cellular approximation, the flat bundle
  V = X̃ ×_{π_1 X} C^d, and h*V ≅ S^∞ ×_C σ via an equivariant lift: correct.
- **Step 1.** v_m has rank 0 at every vertex, so v_m ∈ K_1(X^m) and w_m = v_m^{n+1} ∈ K_{n+1}(X^m) by (K1); for m ≤ n
  the group K_{n+1}(X^m) is the kernel of the identity: correct.
- **Step 2** (the induction the brief asked about). For m > n and Y = X^{m+1}: Y^{m-1} = X^{m-1}, Y^m = X^m;
  K_q(Y) ⊗ Z_(p) is the kernel after tensoring (flatness); w_{m+1} ⊗ 1 restricts to w_{m-1} ⊗ 1 = 0, so it lies in
  K_m(Y) ⊗ Z_(p). The cellular cochain complexes of X^{m+1} and X agree in degrees ≤ m+1, so H^m(Y; Z) = H^m(X; Z), and
  H^m(X; Z) ⊗ Z_(p) = H^m(X; Z_(p)) = 0 (finitely generated cochain groups, flatness). Hence the m-th graded quotient
  vanishes after localization, w_{m+1} ⊗ 1 ∈ K_{m+1}(Y) ⊗ Z_(p), and w_m ⊗ 1 = 0. Correct; the base cases m ≤ n are
  Step 1 and the step from m-1 to m uses only m > n.
- **Step 3.** h is cellular, so h(L^{2j+1}) ⊂ X^{2j+1}; the pull-back of w_{2j+1} is α_j((σ - d)^{n+1}). K_1(L^{2j+1})
  has the finite filtration K_1 ⊃ ... ⊃ K_{2j+2} = 0 with odd quotients 0 (including q = 2j+1) and even quotients
  subquotients of Z/p^a, so it is a finite p-group A with A ≅ A ⊗ Z_(p); flatness makes K_1 ⊗ Z_(p) → K ⊗ Z_(p)
  injective. Hence α_j((σ - d)^{n+1}) = 0 for every j and (σ - d)^{n+1} = 0 in R(C) by (K3). Correct.
- **Step 4.** (χ_σ(g) - d)^{n+1} = 0, so χ_σ(g) = d, so all eigenvalues of the finite-order matrix σ(g) are 1 and
  σ(g) = 1. Correct.

### 2.3 Corollary 2.2 and Remark 2.3

- Corollary 2.2: the regular representation of the finite group π_1(X) is faithful; the image of a Sylow p-subgroup
  is a Sylow p-subgroup of f_*(G) and is trivial. (b) from (a) for every prime. Correct.
- Remark 2.3 (a): Miller, Theorem B (p. 40: X finite-dimensional, G a torsion group, pointed maps BG → X trivial on
  π_1) and Theorem 10.1 (pp. 84-85, the proof by covering spaces and K-theory) are as described. The example: a
  generator y of H²(B(Z/p); Z) = Hom(Z/p, Q/Z) pulls back to p times a generator x of H²(B(Z/p²); Z); y^k ↦ p^k x^k = 0
  for k ≥ 2 because H^{2k}(B(Z/p²); Z) = Z/p²; odd degrees vanish. Correct.
- Remark 2.3 (b): Palmer-Wu, Theorem A (V(G) acyclic) and properties (1) (G → V(G) injective) and (4) (V(G) of type
  F_n iff G is), recalled from [Tho80, WWZZ25] in their introduction: as cited. Palmer-Wu define type F_∞ as type F_n
  for each n. That such a group has one classifying space with finitely many cells in each dimension, which is what
  Theorem 2.1 needs, is a standard fact that the paper uses without saying so (R6).

### 2.4 Lemmas 3.1 and 3.2

- 3.1 (a): the presentation of π_1 of a CW complex with one 0-cell; for mm' = 1 the relation reads η(m)η(m') = 1,
  consistent with η(1) = 1. Correct. McDuff's Lemma 1 not opened (as instructed); Ben-Bassat cites it for this
  statement in his Example 3.4. Quillen, Higher algebraic K-theory I, §1, Proposition 1 (opened): the fundamental
  group of BC at X is the automorphism group of X in the groupoid with all arrows inverted. As cited.
- 3.1 (b): Ben-Bassat §7 (opened): η surjective and U(M) finite, by replacing inverses with positive powers. As cited.
- 3.1 (c): e = axb gives e = (eae)x(ebe); one-sided inverses in the finite monoid H are two-sided; η(e) = 1 and
  η(eme) = η(m). Correct. Sweeney §2.1 and Lemma 2.1 (group completion H/⟨⟨C(j,i)⟩⟩, attributed there to [Lar72,
  Lemme II.3] and [HM03, p. 848]) and Steinberg p. 7 ("the well-known fact G(S) = G/⟨⟨C_ba⟩⟩") are as cited.
- 3.2: r: 1 → e and s: e → 1 given by e; r∘s = ee = id_e, so [s] = [r]^{-1} in the groupoid; for h ∈ H,
  s∘h∘r = ehe = h as an arrow 1 → 1. So conjugation by [r] carries the class of h at e to η(h) at 1, and (j_e)_* = η|_H
  up to an inner automorphism. Ben-Bassat's introduction (j_e, every object a retract of 1) and his Lemma 2.4
  (= `lem:gen`: if every object is a retract of c_0, B D(c_0, c_0) → B D is a homotopy equivalence) are as cited.
  Correct.

### 2.5 Theorems 1.1 and 1.2

- Theorem 1.1 (lines 392-408). H_k = H_k(BM; Z) finitely generated (finitely many cells per dimension).
  H_k(M; F_p) = 0 for k ≥ k_0 gives H_k ⊗ F_p = 0, so H_k is finite of order prime to p for k ≥ k_0; for q > k_0,
  H^q(BM; Z) = Hom(H_q, Z) ⊕ Ext(H_{q-1}, Z) is finite of order prime to p, and H^q(BM; Z_(p)) = H^q(BM; Z) ⊗ Z_(p) = 0.
  Corollary 2.2 (a) applied to j_e and Lemma 3.1 (c) finish. The bounded case: H_k(M; F_p) = H_k ⊗ F_p ⊕ Tor(H_{k-1},
  F_p). Correct.
- Theorem 1.2 (lines 410-421). (iii) ⇒ simply connected by Theorem 1.1 and Lemma 3.1 (a); finitely generated homology
  vanishing above n; Hatcher Proposition 4C.1 (opened: a simply connected CW complex with chosen cyclic decompositions
  of its homology is homotopy equivalent to a complex with one generator cell per cyclic summand and one relator cell
  per finite summand) gives a finite complex. Correct.

### 2.6 Corollaries 3.3, 3.4 and Remark 3.5

- Corollary 3.3: the contrapositive of Theorem 1.1. Correct. The paragraph after it: Ben-Bassat's Example 3.4 (opened)
  contains two monoids on one 11-element set; the one with a = 1 has BM ≃ BC_2 ∨ S² and universal group C_2, as the
  paper says (R7 names the case). Sweeney's Table 1 and Examples 5.4, 5.5 (classifying spaces M(C_2, 3) and M(C_2, 2))
  are as cited.
- **Corollary 3.4** (lines 437-465). A ↦ eA is exact (e idempotent) and additive, takes Z to the trivial ZH-module.
  For x ∈ eM: x lies in the minimal ideal K, MxM = K ∋ e, so e = axb; (eae)(xbe) = eaxbe = e, and xbe = e(xb)e ∈ H, so
  xbe = (eae)^{-1} =: g; with y = beg^{-1}, xy = e; hence hx = h'x implies h = h'. So H acts freely on eM, Z[eM] is a
  free ZH-module, free ZM-modules go to free ZH-modules and projectives to projectives (direct summands), and a
  finite projective resolution of Z over ZM gives one over ZH. Swan, Corollary 1 (opened: p | |π| ⇒ H^i(π, Z) has a
  nonzero p-primary part for infinitely many i) forces H = 1; then U(M) = η(H) = 1; balance of Tor gives bounded
  homology; Theorem 1.2. Correct. The citation of Gray-Pride (functor A ↦ eA, Lemma 2 exactness, Lemmas 3-4 freeness,
  Theorem 2) matches their text. The right-module case is symmetric (Me, right action of H).
- Remark 3.5: Gray-Steinberg, Theorem 6.27 (an equivariant classifying space of dimension max{cd M, 3}) and Corollary
  6.7 (M\X ≃ BM) give a finite-dimensional BM from finite cohomological dimension, as cited; Steinberg's Theorem A gives
  H_n(S¹) = H_n(G) for n ≥ 3, so bounded homology forces G = 1 by Swan, as stated. The question is honestly left open.
- **Observation for Remark 3.5 (not a repair).** If the homology of M is bounded, BM is homotopy equivalent to a finite
  complex (Theorem 1.2), so by Miller's Theorem A (p. 39, opened: for G locally finite and X connected and
  finite-dimensional, the space of pointed maps BG → X is weakly contractible) the map j_e: BH → BM is null-homotopic.
  So no invariant of the homotopy class of j_e can decide whether H = 1; an answer to the question must use the monoid
  itself, as Corollary 3.4 does through the free action on eM. The writer may add this sentence to Remark 3.5.

### 2.7 Section 4, Remarks 4.1 and 5.1

- Corollary 1.4 (a), (b): from Theorems 1.2 and 1.3. Correct.
- Corollary 1.5: Conjecture 7.1 is quoted verbatim from Ben-Bassat §7 (opened); RP² has fundamental group of order 2
  and is not ≃ BM for a finite M by Corollary 1.4 (a). Correct. The last clause, "and so is every connected finite CW
  complex with non-trivial fundamental group", counts S¹ (infinite fundamental group) as a counterexample, which it is
  not: the conjecture assumes π_1(X) finite. The proof (lines 494-498) proves the right statement. Repair R1.
- Remark 4.1: Ben-Bassat v1 is dated 28 Oct 2026 (abstract page saved 12 Nov); I did not refetch arXiv on 25 Nov.
  Carcacía-Campos, Theorem 6.2 and its proof (opened): B C_{Z/2,n} ≅ RP^n via the boundary of the cross-polytope with
  the antipodal action; for n = 2 the three-object category with Hom(i, j) = Z/2 for i < j, nine arrows. Correct. That
  paper attributes this three-object model of RP² to Tanaka ([23, Example 3.8] there); R9 (optional credit).
- Remark 5.1: correct.

### 2.8 The examples, recomputed

Program: my own, written for this check, independent of `checks/d2_examples_check.py` and of the runs' programs; pure
Python integers for lattices (kernels by unimodular row reduction, lattice equality by echelon bases and membership),
numpy for ranks mod p; no python-flint. Code and outputs (run with `python -I -B`):
`<local>/Documents\agent_notes\abe075dc_D2_check_code\` (`d2lib.py`, `homol_fp.py`, `check_m6.py`,
`check_m23.py`, `selftest.py`, `out\`). Self-tests: Z/2, Z/3 and Fiedorowicz's 5-element monoid L_0 (≃ S²) give the
known homology mod 2 and mod 3 by both homology methods.

**Proposition 5.2 (M_6).**
- Monoid axioms on all 216 triples; aperiodic (y² = y³ = x_00); M_6 is Sweeney's Example 5.2 (opened; H_1 = 0,
  H_i = Z for i ≥ 2 there) with an identity adjoined, as the paper says.
- (a) U(M_6) = 1: every generator is forced trivial by the idempotents and cancellation.
- (b) e, u, a, b, c, t is a Z-basis of ZM_6 (invariant factors all 1) and the products are exactly those listed;
  Re = Ze ⊕ Za, Ru = Zu ⊕ Zb ⊕ Zc ⊕ Zt. The resolution is exact over Z in degrees 0-5, by comparing the kernel lattice
  of each d_n with the image lattice of d_{n+1} (not by ranks and saturation); since d_n = d_3 for n ≥ 3 this gives
  all degrees. Without the paper's resolution: the normalized bar complex mod 2, 3, 5, 7 and 1000000007 gives
  dim H_k = 1, 0, 1, 1, 1 for k = 0..4; a free resolution built by my program (greedy generators of each kernel)
  gives dim H_k(BM_6; F_p) = 1, 0, 1, 1, ..., 1 for k = 0..9 and the same five primes.
- (c) z_n is a cycle for n = 2..7, f_n is a cocycle for n = 2..6 (all (n+1)-tuples), ⟨f_n, z_n⟩ = 1 for n = 2..7.
  The Δ-complex D_n: for n = 2..6 every face of every simplex goes to the corresponding nerve face of its label tuple
  (so s_n is simplicial), no label is 1, and the image of ζ_n is z_n; D_2, D_3, D_4 have the integral homology of
  S², S³, S⁴. The rest of (c) (wedge map, homology isomorphism, simply connected, Hatcher Corollary 4.33, opened) is
  correct.

**Proposition 5.3 (M_23).**
- 23 distinct pairs; closed under the product; identity and associativity on all 12,167 triples; x_ij x_kl = x_il;
  a, b, c, g idempotent; d² = x_20, e² = x_22, f² = x_24, cubes equal squares; aperiodic; no product of two non-identity
  elements is 1; U(M_23) = 1.
- x_00, c - x_00, 1 - c, a - x_00 idempotent; Z-ranks of P, E, F, G are 3, 10, 10, 4; terms 3, 10, 13, 8, 3; each value
  of d_k is fixed by its idempotent and lies in the target summand; ker ε = im d_1, ker d_k = im d_{k+1} (k = 1, 2, 3)
  as lattices, d_4 injective; image ranks 1, 2, 8, 5, 3. Augmentations of the generators 1, 0, 0, 0, so
  H_k(M_23; Z) = Z, 0, Z, 0, Z.
- Without the paper's resolution: my free resolution gives dim H_k(BM_23; F_p) = 1, 0, 1, 0, 1, 0, 0 for k = 0..6 and
  p = 2, 3, 5, 7, 1000000007; the normalized bar complex gives 1, 0, 1 for k = 0..2 (p = 2, 3, 1000000007).
- u is normalized and a 2-cocycle (all triples). My implementation of the comparison map F_k(ε) = ε s(F_{k-1}(d_k ε))
  into the normalized left bar resolution is a chain map in degrees 1-4; z_2 (4 cells) and z_4 (108 cells) are cycles
  of the cellular chain complex; ⟨u, z_2⟩ = -1 and ⟨u ⌣ u, z_4⟩ = 1, the values of the paper. Since H_2 = H_4 = Z and
  H_3 = 0, these values alone show that [u] and [u]² generate H² and H⁴, whatever chain map produced z_2 and z_4.
- The deduction BM_23 ≃ S² ∪_h e⁴ ≃ CP² (Corollary 3.4, Hatcher 4C.1, Hopf invariant ±1, π_3(S²) = Z generated by the
  Hopf map, Hopf invariant a homomorphism) is correct; locators in R5. Ben-Bassat's monoids of type CP² have 1795
  elements (his Example in §6) and 122 elements (his Appendix), as the paper says.

## 3. Citations

| Reference | Locator in the paper | Opened by me | Result |
|---|---|---|---|
| Atiyah 1961 | §2 (K1, K2); (8.1), (6.11) (K3) | yes (Numdam copy, text) | as cited; give §2 its exact places (R3) |
| Atiyah-Hirzebruch 1961 | §2 | no (not on disk) | remains from memory |
| Ben-Bassat arXiv:2610.38760v1 | Thm C, Conj 7.1, Ex 3.4, §7, Lemma 2.4, introduction | yes (TeX source) | as cited; Ex 3.4 case a = 1 (R7); Fiedorowicz's conjecture is his Conjecture 1.1 (R2) |
| Carcacía-Campos arXiv:2611.09718v1 | Thm 6.2 | yes | as cited; credit to Tanaka there (R9) |
| Fiedorowicz 1984 | p. 323 | **no (not opened, as instructed)** | the page comes from Ben-Bassat §1; Martinian-Steinberg p. 1 quote the sentence without a page (R2) |
| Gray-Pride arXiv:1003.3227 | Lemmas 2-4, Thm 2 | yes | as cited; journal pages from Steinberg's bibliography (R8) |
| Gray-Steinberg arXiv:1706.04387v1 | Thm 6.27, Cor 6.7 | yes | as cited; journal data (R8) |
| Hatcher | Ex 2.43, Prop 1B.9, Cor 4.33, §4.B, Prop 4C.1 | yes (text of the book) | as cited; Ex 2.43 gives homology (R4); π_3(S²) is Example 4.51 (R5) |
| Martinian-Steinberg arXiv:2511.12657v1 | p. 1, Cor 5.15, Thm C, Cor 5.16 | yes | as cited, except the page 323 (R2) |
| McDuff 1979 | Lemma 1 | **no (not opened, as instructed)** | cited as quoted by Ben-Bassat (Example 3.4) and Sweeney; the paper carries its own proof |
| Miller 1984 | Thm B p. 40, Thm 10.1 pp. 84-85 | yes | as cited |
| Palmer-Wu arXiv:2510.16879v1 | Thm A, properties (1), (4) | yes | as cited; one standard step unstated (R6) |
| Quillen 1973 | §1, Prop 1 | yes | as cited |
| Steinberg arXiv:2405.06594v1 | Thm A, Thm 3.1, p. 7 | yes | as cited |
| Swan 1960 | Cor 1, Cor 2 | yes | as cited |
| Sweeney arXiv:2502.05276v2 | Prop 2.2, Cor 2.3, §2.1, Lemma 2.1, Ex 5.2, Table 1, Ex 5.4, 5.5 | yes | as cited (§2.3 defines H_i(M; D) as Tor) |

## 4. Repairs, with exact wording

Each repair gives the text to find in `src/D2_paper.tex` (the line numbers of the version checked) and its replacement.
Line breaks inside the TeX are as in the file; a replacement may be re-wrapped.

**R1 (statement wrong as worded; Corollary 1.5, lines 129-130).** Replace

```tex
false. The real projective plane $\RP^2$ is a counterexample, and so is every
connected finite CW complex with non-trivial fundamental group.
```

by

```tex
false. The real projective plane $\RP^2$ is a counterexample, and so is every
connected finite CW complex whose fundamental group is finite and non-trivial.
```

The proof (lines 494-498) needs no change.

**R2 (citation; introduction, lines 108-109).** Replace

```tex
statement, suggested by Fiedorowicz (\cite[p.~323]{Fie}, as quoted in
\cite[p.~1]{MS}) and stated as a conjecture in \cite{BB}.
```

by

```tex
statement, suggested by Fiedorowicz (\cite[p.~323]{Fie}; the sentence is quoted
in \cite[p.~1]{MS}, and the page is given in \cite[\S1]{BB}) and stated as
Conjecture~1.1 in \cite{BB}.
```

**R3 (citation; Section 2, lines 173-174).** Replace

```tex
We use two properties of this filtration, both contained in the spectral
sequence of Atiyah and Hirzebruch \cite[\S2]{AH} (see also \cite[\S2]{At}),
```

by

```tex
We use two properties of this filtration, both contained in the spectral
sequence of Atiyah and Hirzebruch \cite[\S2]{AH} (see also \cite[\S2]{At}, where
the filtration is defined and shown to be multiplicative, and (2.2) and
Proposition~(2.4) there),
```

**R4 (optional precision; line 189).** Replace

```tex
$q<2j+1$ \cite[Example~2.43]{Ha}.
```

by

```tex
$q<2j+1$, as one reads off from the cellular chain complex of
\cite[Example~2.43]{Ha}, whose boundary maps are alternately $0$ and
multiplication by $p^a$.
```

**R5 (locators; Proposition 5.3, lines 744-745).** Replace

```tex
$\pi_3(S^2)$ is infinite cyclic, generated by the Hopf map, whose Hopf
invariant is $1$, and the Hopf invariant is a homomorphism \cite[\S4.B]{Ha},
```

by

```tex
$\pi_3(S^2)$ is infinite cyclic, generated by the Hopf map
\cite[Example~4.51]{Ha}, whose Hopf invariant is $1$, and the Hopf invariant is
a homomorphism \cite[\S4.B, Proposition~4B.1]{Ha},
```

**R6 (unstated step; Remark 2.3 (b), lines 317-318).** Replace

```tex
$\Gamma$ which has the integral homology of a point and admits a
classifying space $B\Gamma$ with finitely many cells in each dimension.
```

by

```tex
$\Gamma$ which has the integral homology of a point and is of type $F_n$ for
every $n$; such a group admits a classifying space $B\Gamma$ with finitely many
cells in each dimension.
```

and add a reference for the last clause. It is a standard fact about finiteness properties of groups; I have not
opened a source for it and give none.

**R7 (precision; after Corollary 3.3, line 429).** Replace

```tex
For instance the monoid with $11$ elements of \cite[Example~3.4]{BB}, whose
```

by

```tex
For instance the monoid with $11$ elements of \cite[Example~3.4]{BB} with $a=1$, whose
```

Optional addition, after "homology in infinitely many degrees." (line 431):

```tex
With $a=g$ the same example gives a monoid with trivial universal group whose
classifying space is, by \cite[Theorem~A]{BB}, the cofibre of
$\RP^1\subset\RP^\infty$; its homology is $\Z/2$ in every odd degree $\ge3$.
```

The homology is my computation from the long exact sequence of the cofibre. This is a second instance, with torsion,
of the phenomenon of Proposition 5.2.

**R8 (bibliography, lines 863 and 865).** In line 863 replace `(2011); arXiv:1003.3227v1.` by

```tex
(2011), no.~12, 3005--3024; arXiv:1003.3227v1.
```

and in line 865 replace `Algebr.\ Geom.\ Topol.\ 22 (2022);` by

```tex
Algebr.\ Geom.\ Topol.\ 22 (2022), no.~7, 3083--3170;
```

The data are as given in the bibliographies of Steinberg, arXiv:2405.06594v1, refs. [6] and [7], and of
Martinian-Steinberg, ref. [10].

**R9 (optional credit; Remark 4.1, lines 507-508).** Replace

```tex
$\RP^2$, the quotient of the octahedron by the antipodal map
\cite[Theorem~6.2]{CC}.
```

by

```tex
$\RP^2$, the quotient of the octahedron by the antipodal map
\cite[Theorem~6.2]{CC}; there this three-object model of $\RP^2$ is attributed
to Tanaka.
```

**R10 (records; Section 6).**

Lines 812-813: replace

```tex
The present form of the proof of
Theorem~\ref{thm:K} has been read by nobody but its writer.
```

by

```tex
The present form of the proof of Theorem~\ref{thm:K}, Lemma~\ref{lem:je}, the
proofs of Theorems~\ref{thm:main} and~\ref{thm:equiv} and of
Corollary~\ref{cor:cd}, and the two examples were checked on 25 November 2026
by Claude Opus~5.5 at effort max, who recomputed the examples with a program of
its own, independent of the writer's program and of the runs' programs.
```

Line 814: replace `the writer ran a program of his own,` by `the writer ran a program of its own,`.

Lines 830-831: replace

```tex
The locators in \cite{AH},
\cite[\S2]{At}, \cite{Ha} and \cite{Qu} are given from memory.
```

by

```tex
The checker opened \cite[\S2]{At}, \cite{Ha} at the places cited and
\cite[\S1, Proposition~1]{Qu}; the locator in \cite{AH} is given from memory.
```

Lines 836-837: replace

```tex
has been read by nobody but the writer and the reader
who proposed it.
```

by

```tex
has been read by the writer, by the reader who proposed it and by the checker.
```

`PROVENANCE.md`: add this check to the table of contributors. Move Atiyah §2, Hatcher (Example 2.43, Proposition 1B.9,
Corollary 4.33, §4.B) and Quillen §1 Proposition 1 to "opened". Atiyah-Hirzebruch, McDuff and Fiedorowicz stay
unopened.

## 5. Not covered

- The re-proof by another model family (PROVENANCE, "What the re-proof by another model family must cover"): this check
  is by a Claude model. Its item 4 (dropping "finitely many cells in each dimension" from Theorem 2.1; a census of small
  monoids with U(M) ≠ 1) was not in my brief and was not done.
- Ben-Bassat's proof of Theorem C: statement checked, proof not read by me.
- arXiv was not refetched for the version state of arXiv:2610.38760 (Remark 4.1).
- No literature search (not in the brief; the gate of a848636d0bbf3ae4b, Claude Fable 5.2 at effort max, made it).

## Addendum, 25 November 2026 (later the same day): the pieces written after this check

Asked by the main session 329fb1e6 (Claude Opus 5.5 at effort max) after afceadd46f7598ec4 (Claude Fable 5.2 at effort
max) had applied the repairs (paper now 14 pages). Checker: abe075dcdd909eea0 (Claude Opus 5.5 at effort max). Checked
text: the revised `src/D2_paper.tex` (977 lines); line numbers below refer to it. The paper was not edited.

### Verdicts

| Piece | Verdict |
|---|---|
| Remark 2.3 (b), lines 322-337: a group of type F_n for every n has a classifying space with finitely many cells in each dimension (skeleton by skeleton, Schanuel's lemma) | **correct**; replaces R6 without a reference |
| Paragraph "The monoid with five elements", lines 677-695, and its announcement, lines 560-563 | **mathematics correct**, recomputed; **one credit repair needed** (A2): Fiedorowicz published a proof in 2002 |
| The R7 sentence after Corollary 3.3, lines 447-459 (case a = g) | **correct as revised**; the writer's correction is right |
| End of Remark 3.5, lines 501-508 (j_e and Miller's Theorem A) | correct |

### A1. Remark 2.3 (b)

The argument, step by step. (i) Z is a finite complex of dimension n ≥ 2 with π_1 = Γ and (n-1)-connected universal
covering Z̃. By Hurewicz, π_n(Z) = π_n(Z̃) ≅ H_n(Z̃), compatibly with the action of Γ. (ii) Since dim Z = n,
H_n(Z̃) is the kernel of C_n(Z̃) → C_{n-1}(Z̃), and 0 → H_n(Z̃) → C_n → ... → C_0 → Z → 0 is exact with finitely
generated free ZΓ-modules C_i. (iii) For a classifying space Y with finite (n+1)-skeleton, 0 → B_n(Ỹ) → D_n → ... →
D_0 → Z → 0 is exact, and B_n(Ỹ) is the image of the finitely generated D_{n+1}. The generalized Schanuel lemma makes
H_n(Z̃) plus finitely generated free modules isomorphic to B_n(Ỹ) plus finitely generated free modules, so H_n(Z̃) is
finitely generated. (iv) Attaching finitely many (n+1)-cells along ZΓ-generators of π_n(Z) attaches, in the universal
covering, cells along all their translates. That kills H_n, changes neither the lower homology nor π_1, and so makes
the universal covering n-connected (Hurewicz). (v) The start is the finite 2-skeleton of a classifying space with
finite 2-skeleton (type F_2). The union of the successive complexes has the stage-k complex as its k-skeleton (finite)
and a universal covering with all homotopy groups zero, hence contractible (Whitehead): it is a K(Γ, 1). Step (v) is
left implicit in "built skeleton by skeleton"; that is acceptable. Optional: add "The union of these complexes is the
required classifying space." after "$n$-connected." (line 336). The deduction that follows (H^q(X; Z) = 0 for q > 0,
injectivity on π_1) is unchanged and correct. Repair R6 is answered: the remark no longer needs a reference.

### A2. The paragraph on the five-element monoid

Mathematics, checked by hand and recomputed by my program `check_m5.py` (in
`<local>/Documents\agent_notes\abe075dc_D2_check_code\`, output `out\check_m5.out`, run with `python -I -B`):
- M_5 = {1, x_ij} is a submonoid of M_6 with x_ij x_kl = x_il; U(M_5) = 1 (idempotents).
- e, u, a, b, c is a Z-basis of ZM_5; R'e = Ze ⊕ Za, R'u = Zu ⊕ Zb ⊕ Zc.
- 0 → R'e → R'u → R'e → Z → 0 with d_1(s) = sa, d_2(s) = sb is exact over Z (kernel and image lattices compared):
  d_1 sends u, b, c to a, 0, 0, and d_2 sends e, a to b, c.
- Hence H_*(M_5; Z) = Z, 0, Z, 0, ...
- The same homology without the resolution:
  - the integral normalized bar complex has ranks of d_2, d_3, d_4 equal to 4, 11, 53 and no torsion, so H_1 = 0,
    H_2 = Z, H_3 = 0;
  - the bar complex mod 2, 3, 5, 7 and 1000000007 gives 1, 0, 1, 0, 0 in degrees 0-4;
  - my own free resolution gives 1, 0, 1, 0, ..., 0 in degrees 0-8.
- For n = 2 the labels of s_2 are x_01, x_00, x_10 only, so s_2 maps into the subcomplex BM_5. z_2 is a cycle there,
  f_2 is a cocycle on BM_5, and f_2(z_2) = 1. So s_2: S² → BM_5 is a homology isomorphism between simply connected
  complexes, hence a homotopy equivalence (Hatcher, Corollary 4.33).
- In M_6, yw = x_00 w and wy = w x_00 for every w ≠ 1, so y "has the same products as x_00"; M_5 ∪ {y} = M_6, whose
  classifying space is the wedge by Proposition 5.2 (c).

All correct.

**Credit (repair needed).** Lines 679-681 say that the classifying space being S² is "left as an exercise" in
\cite[p.~323]{Fie} and that "The proof of Proposition 5.2 contains a proof of this." Fiedorowicz himself published a
proof. In Z. Fiedorowicz, *A counterexample to a group completion conjecture of J C Moore*, Algebr. Geom. Topol. 2
(2002), 33-35, arXiv:math/0202260 (copy in `agent_notes/GATES_D2_FREX_sources/arxiv_math_0202260/`, opened by me), the
Lemma on pp. 33-34 takes this five-element monoid. It notes π_1(BP) = UP = 1 because the x_ij are idempotent, and
computes H_*(BP) = Tor^{Z[P]}(Z, Z) = H_*(S²) from an explicit projective resolution of length 2 of right
Z[P]-modules. Other published accounts:
- Steinberg, Theorem 3.1 with the remark on p. 8, for every finite rectangular band (a wedge of (|A|-1)(|B|-1)
  2-spheres; for 2 × 2 "as was first noted in" Fiedorowicz 1984);
- Ben-Bassat, Example 1.2, which recalls the computation and cites [Fie84, Fie02];
- Sweeney (v2), Example 3.1, which reproduces the resolution of "p. 34 of [Fie02]".

As written, the paragraph reads as if the paper supplied a missing proof.

I could not check the words "left as an exercise": Fiedorowicz 1984 stayed unopened for me, as instructed. Section 6
of the revised paper says that the coordinating session opened its pp. 321-324 and found the cited statements as
given. That claim rests on its reading.

Replace (lines 679-681)

```tex
This is the monoid of \cite[p.~323]{Fie}, where it is
left as an exercise that its classifying space is equivalent to $S^2$. The
proof of Proposition~\ref{prop:M6} contains a proof of this.
```

by

```tex
This is the monoid of \cite[p.~323]{Fie}, where it is
left as an exercise that its classifying space is equivalent to $S^2$.
Fiedorowicz published a proof, by a projective resolution of length~$2$, in
\cite[Lemma, pp.~33--34]{Fie02}, and the case of every finite rectangular band
is in \cite[Theorem~3.1 and p.~8]{St}. The proof of
Proposition~\ref{prop:M6} contains another proof.
```

add to the bibliography, after `\bibitem{Fie}` (line 945):

```tex
\bibitem{Fie02} Z.~Fiedorowicz, A counterexample to a group completion
 conjecture of J.~C.~Moore, Algebr.\ Geom.\ Topol.\ 2 (2002), 33--35;
 arXiv:math/0202260.
```

and in "What is whose" (line 825) replace `suggestion that became Theorem~\ref{thm:BB} are Fiedorowicz's \cite{Fie};`
by

```tex
suggestion that became Theorem~\ref{thm:BB} are Fiedorowicz's \cite{Fie}, and
so is the first published proof of that statement \cite{Fie02};
```

Records (lines 884-886): replace

```tex
were
added after that check and have been read only by the writer; a second
program of the writer confirms the statements on $M_5$.
```

by

```tex
were
added after that check; the checker checked both the same day, recomputing
the statements on $M_5$ with its own program, and a second program of the
writer confirms them as well.
```

### A3. The R7 sentence (lines 447-459)

Correct as revised. The case a = 1 is named. The case a = g has classifying space the cofibre of RP¹ ⊂ RP^∞ by
Ben-Bassat's Theorem A, as his Example 3.4 says. It is simply connected (a 2-cell kills the generator of π_1 = Z/2).
From the long exact sequence of the cofibre its reduced homology is: H_1 = 0; H_2 = ker(H_1(RP¹) = Z → H_1(RP^∞) =
Z/2) ≅ Z; Z/2 in odd degrees ≥ 3; zero in even degrees ≥ 4. The writer's correction is right. My optional sentence
(R7) had omitted the Z in degree 2: incomplete, though it did not say "only". "The converse of Corollary 3.3 fails"
holds, in its integral form (this case and M_6) and in its mod-2 form (this case).

### A4. The end of Remark 3.5 (lines 501-508)

Correct. Miller's Theorem A (p. 39) concerns pointed maps. A map from the connected BH to a connected complex is freely
homotopic to a pointed one, so every map BH → BM is null-homotopic once BM is homotopy equivalent to a finite complex.
