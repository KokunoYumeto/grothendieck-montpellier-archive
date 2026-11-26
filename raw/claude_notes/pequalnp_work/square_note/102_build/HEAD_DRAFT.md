**The attached files.** Besides this file there is one ZIP, `102_VPVNP_SQUARE.zip`. Unpack it once; there is no ZIP inside it. Everything you need that isn't a published source is in it, so don't rely on any earlier conversation.

# The square decides: Valiant's conjecture after the Anthropic and OpenAI preprints, and the Euclidean unit square as a price

You are GPT-6 Astra (ChatGPT Pro mode). This is research and paper writing in one task: write the paper below while
you push its open theorem.

## Why this matters

Valiant conjectured in 1979 that the permanent has no arithmetic circuits of polynomial size: VP ≠ VNP, the algebraic
counterpart of P ≠ NP. Mulmuley and Sohoni's geometric complexity theory (SIAM J. Comput. 31(2), 2001) aims at its
border form: the padded permanent does not lie in the orbit closure of a determinant of polynomial size. On 23 and 24
November 2026 two preprints claimed proofs of VP ≠ VNP over every field, each with a Lean 4 formalization. No human
mathematician has checked either; read both as claims, and use their statements with their locators.

- **The Anthropic preprint**, "VP ≠ VNP over every field", by Claude (the result was found by an internal research
  Claude model). Its LaTeX source is attached as `literature/anthropic_vp_vnp_hexagon_2611.00954v1/main.tex` (the
  version deposited on Hexagon as hexagon:2611.00954v1), with its Lean statement file
  `literature/anthropic_vp_vnp_Statement.lean`. Theorem 1.1: there is an absolute c > 0 and, for each characteristic,
  an m₀, such that over every field every circuit for the Hamiltonian cycle polynomial HC_m, and for PERM_m outside
  characteristic two, has more than m^(c (log m)^(1/3)) gates for m ≥ m₀. Theorem 1.4: the same for circuits that
  approximate (border complexity). Corollary 1.2: VP ⊊ VNP. Remark N.6, the one numbered statement not formalized: over
  fields of characteristic other than two, PERM_m is not approximated by determinants of affine matrices of size
  m^(c (log m)^(1/3)), which over C is Mulmuley and Sohoni's conjecture.
- **The OpenAI preprint**, "VP and VNP are different" (`literature/openai_vp_vnp_Paper.tex`, the LaTeX source).
  Theorem 1.1: over every field, border circuits for an explicit VNP family f_n need exp(Ω((log n)^(5/4))) gates.
  Corollary 1.2: the same for the directed Hamiltonian cycle polynomial and, outside characteristic two, the permanent,
  and for border determinantal complexity.

Both proofs turn on one geometric question about wires in tensor networks, and neither paper decides it: can wires be
priced below their Euclidean length? In the Anthropic preprint it is the alternative of Theorem 2.2, the flat or the
contracting hypothesis of Definition 2.1 ("We do not know which of the two hypotheses holds, even over R", p. 6). In the
OpenAI preprint it is whether a strict shortening exists (Theorem 1.3). The branches give very different bounds: the
flat case 2^(c (log m)^(4/3)), the contracting case 2^(c (log m)²/log log m) (Anthropic, end of §2.2, p. 8), and a
strict shortening 2^(n^σ) for some σ > 0 (OpenAI, Theorem 1.3). So the answer decides whether the claimed separation is
quasi-polynomial or close to exponential.

Two runs of ours (GPT-6 Astra, ChatGPT Pro mode) worked on this question on 24 and 25 November 2026. They did not decide
it, but they reduced it to one four-point metric, the unit square, and to sharp equivalent forms: a dichotomy of
exponents, a prescribed family of finite rational linear systems, and a classical sums-of-squares exponent. This run
starts where they stopped, and its task is to decide the square.

## Where it stands

- **The two hypotheses, as the Anthropic preprint states them** (Definition 2.1, pp. 4–5). V is a finite set of
  parties; a V-tensor is an element of ⊗_{v∈V} k^{n_v}; the product of two V-tensors is their tensor product taken party
  by party; s is a restriction of t if s = (⊗_v A_v) t for linear maps A_v. A spectral point on V (after Strassen) is a
  function φ from V-tensors to [0, ∞) with φ(1) = 1, φ(st) = φ(s)φ(t), and φ(s) ≤ Σ_j φ(t_j) whenever s = Σ_j s_j with
  every s_j a restriction of t_j. The wire ⟨q⟩_{uv} is the q × q identity in the indices of u and v; for every spectral
  point there is a pseudometric d_φ on V with φ(⟨q⟩_{uv}) = q^{d_φ(u,v)}. The contracting hypothesis: there are an
  integer μ ≥ 2 and a real s with 1 ≤ s and s² < μ such that for V = Mat_μ(F₂) and every spectral point φ on V,
  E_{a, rk W = μ} d_φ(a, a + W)² ≤ s² E_{a, rk W = 1} d_φ(a, a + W)². The flat hypothesis: for every finite subset V of a
  Euclidean space and every ε > 0 there are a spectral point φ on V and c ≥ 0 with |c d_φ(u, v) − ‖u − v‖| ≤ ε for all
  u, v ∈ V. A price on V is a pointwise limit of functions c d_φ with c ≥ 0 (def_price, p. 5).
- **Theorem 2.2 and the common part** (thm_alt, p. 6; §2.2, pp. 6–8): over every field one of the two hypotheses
  holds. A tensor of rank r or less across a split is a restriction of a product of wires through two hubs joined by a
  wire of dimension r (lem_hubs); the identity for two crossing wires (prop_identity) and averaging over fine chains give
  the Bruhat–Tits inequality for every price (thm_cn), so every price is induced by a map into a CAT(0) space
  (prop_random, prop_space). The spectral points the argument uses come from Zorn's lemma (prop_gauge).
- **The strict shortening, as the OpenAI preprint states it** (lines 195–230 of its source). C_{D,m} consists of
  width-m cables on the D coordinate diameters of the Euclidean unit ball; a strict shortening is a finite sum identity
  for C_{D,m} over a field, using A networks in the ball each of cost w or less, with w + 2D log₂ A < 2Dm; existence
  depends only on the characteristic.
- **The input (H_A).** Our two runs use two statements of the Anthropic preprint as unrefereed inputs: Theorem A.6
  (cover duality) and Proposition C.3 (the CAT(0) embedding of prices, "C3" or "the price-space theorem" below). Every
  conditional result below names which of them it uses.
- **The hinge, as our two runs leave it**, in the strongest form a different model has checked (see the check below).
  For a fixed field:
  - with no input: a strict planar shortening makes some finite planar Euclidean configuration a nonprice;
  - under C3 alone, these are equivalent: the unit square e is not a price; the square with its centre e′ is not a
    price; some finite planar Euclidean configuration is not a price; every finite price is a tree pseudometric; no
    strict four-point tree violation exists. Over C, the prices in that branch are exactly the tree pseudometrics
    (run 98, PG-CROSSPOLY-GATE's last clause and PG-TREE-C; run 99, Q1, Q2 and Q1c-4);
  - under C3 and A.6: all of the above ⟺ a strict planar shortening exists (run 99, thm:square-shortening-equivalence;
    run 98, SH-15); for each fixed dimension D, there is no D-strict shortening ⟺ every finite subset of R^D is a price
    (run 98, PG-CROSSPOLY-GATE; run 99, Q1d-7); and flatness ⟺ no strict shortening in any dimension (run 98, SH-08;
    run 99, Q3a with no input and Q3b, which proves it again with a shortening that uses only nonantipodal wires between
    the terminals);
  - the crossing (partial-transpose) exponent ρ exists and takes exactly two values: ρ = 1 if the square is not a
    price, ρ = √2 if it is (run 99, Q1, crossing_exponent_gap.tex and cycle_search.tex). So a fixed superlinear lower
    bound for ρ decides the branch. This uses C3, A.6 and two further inputs that no second model has checked: the upper
    bound P(q) ≤ q^(√2+o(1)) (from the preprint's Proposition B.2 and Khoruzhii's counting) and the two-hub cost bound
    F(β) < 4 for β < √2 (prop:optimal-crossing-hubs). The ratio R_square is exactly 2 or 2√2 (run 99, Q1);
  - for the Bugár–Vrana crossing-operator endpoint, r(C_2) = inf_N p₀(C_{2^N})^(1/N) is exactly 2 if the complex
    square is absent and 2^(√2) if present (run 98, PG-OP-COMPLETE);
  - in four parties the prices are exactly the tree pseudometrics if the square is absent, and exactly the
    CAT(0)-embeddable four-point pseudometrics if it is present; in three parties every pseudometric is a price, over
    every field (run 98, PG-FOUR-CONDITIONAL, PG-TREE-ALL, PG-THREE).

  Strict shortening implies contraction (run 99, Q3c, from Q3a and the preprint's Theorem D.2), and the converse is
  open (Q3d below). So the two preprints' dichotomies are not known to coincide.
- **The square as finite linear algebra** (run 98, PG-OP-SOS-DUALITY, PG-OP-DETERMINISTIC, PG-OP-COMPRESSED; its own
  audit passed all three as written). For each dyadic dimension q = 2^N: choose the first power-of-two Schur-copy count
  n satisfying an explicit integer inequality, then the lexicographically first maximum-dimension Specht type with q
  rows or fewer. The resulting rational linear system asks for a symmetric equivariant operator with partial-transpose
  symmetry, trace 1, and support only on types of entropy (5/4) log₂ q or more. The complex square is present ⟺ every
  system of the family is feasible; it is absent ⟺ some system fails, and a failure yields a rational two-cut
  decomposition by Gaussian elimination. The proof turns an exact dual operator into a short complex bilinear
  sums-of-squares identity. No instance has been solved; the dimensions are very large. PG-OP-COMPRESSED gives an
  alternative encoding on Sym^n((Q^q)^⊗4).
- **What is excluded already** (run 98): no strict shortening exists at any width m ≤ 6, in any dimension, for any
  number of terms and any finite layout, over every field (SH-60b, with SH-55d and SH-57 to SH-60; at width 5 by 273
  one-minimum and 439 two-minimum exact rational certificates covering all 285 remaining minimum branches). Width 7 is
  the first width not excluded; a planar shortening with exactly two terms needs width 8 or more (SH-38). A geometric
  mean of crossing cut ranks fails the spectral-extension hypothesis needed for a non-tree price (EX-21).
- **The fields.** Shortening and price sets depend only on the characteristic (run 98, EX-07; run 99, Q4e). A finite
  complex nonprice has a number-field certificate valid outside the primes dividing an explicit integer D (run 99, Q4a).
  The complex square is absent ⟺ bounded-width cycle certificates exist over infinitely many primes ⟺ over all
  sufficiently large primes (run 98, PG-CYCLE-SPECIALIZATION). Characteristic two is not decided by an almost-all-primes
  statement. There, under C3 and A.6, the crossing exponent is again 1 or √2, and its exact gate can be restricted to
  combined integer Hamming-weight blocks with subexponential overhead; the finite bounds P(8) ≤ 16 and P(32) ≤ 132 do not
  decide it (run 99, Q4d). In characteristic two the permanent equals the determinant.
- **Contraction** (run 98, SH-09, SH-33, PG-IN-GATE, PG-HILB2; run 99, Q3d). Whether strict shortening and contraction
  coincide is reduced exactly to the mutual exclusion of flatness and contraction (SH-09). Contraction is equivalent to
  √rank(A − B) on Mat_μ(F₂) not being a price for some μ ≥ 3 (run 99, Q3d); that metric embeds in a CAT(0) space, and
  Euclidean (Hilbert) maps have the sharp squared ratio 2(1 − 2^(−μ)); on Mat_2(F₂) every Hilbert map has squared ratio
  3/2 or less (PG-HILB2). A seven-party cover exponent of 1/128 or less, or a balanced restriction of K_(r,r) to two
  r-cliques with exponent r²/2048 or less for some r divisible by 4, would give explicit contraction (SH-33); so would a
  uniform Izeki–Nayatani invariant bound (PG-IN-GATE).
- **The classical form.** The planar hinge is a complex sums-of-squares question: for complex bilinear forms B_ℓ with
  (Σ_{i≤q} a_i²)(Σ_{j≤q} b_j²) = Σ_{ℓ≤R} B_ℓ(a, b)², let P_C(q) be the least R. With σ_C the complex crossing
  quantity of run 99, σ_C ≤ 2P_C ≤ 4σ_C, so the two-value gap of ρ carries over: under the inputs of the last hinge
  bullet, the square is a price ⟺ the complex Hurwitz exponent lim log_q P_C(q) is √2, and otherwise it is 1 (run 99,
  Q1; run 98, RT-SOS). The lower bound side is in Yilin
  Liu's noncommutative circuit paper (hexagon:2611.00994, "Two crossing cuts"); the upper bound is Khoruzhii's, as that
  paper cites it. Liu's second post (hexagon:2611.00972) treats asymptotic tensor rank. Both are attached in LaTeX.
- **The direct-case exponent** (run 98, Q3: EX-29, EX-30, EX-42, EX-47, EX-48). A fixed-power ceiling of 4/3 covers
  common-origin radii with polynomially many labelled hubs, subpolynomially many adaptive hubs, and two hubs with
  arbitrary segment centres; the orthogonal equal-width model gives exactly 5/4; the supremum over all hub-displacement
  arguments is undecided.
- **The check by a different model** (Claude Opus 5.5 at effort max, 25 November 2026; `ours/GATE1_CHECK_20261125.md`
  with its check events). Targeted proof checks on both finals of run 98's PG-CROSSPOLY-GATE, PG-FOUR-CONDITIONAL
  and SH-08, and of run 99's Q3b and its planar reduction and exponent theorem: all hold under A.6 and C3, and no step
  failed. Two corrections of record: run 99's register states Q3b under C3 alone, and the header of its √2 theorem names
  C3 alone, while both proofs also use A.6. PG-FOUR-CONDITIONAL over a general field rests on Wigderson and Zuiddam
  (2025), Theorem 12.23, which the check did not open; over C run 98's PG-TREE-C covers that step. Read at statement
  level only: SH-60b, SH-38, EX-29, EX-30, and the two inputs named in the last hinge bullet.
- **The two preprints checked where our runs rest on them**: run 99 reconstructed Anthropic's Appendices C and D and
  OpenAI's direct geometric step (cost terms, selector cost, the 5/4 threshold) without finding a fault (Q7b, Q7c).
  These are targeted checks by the same model, not a rerun of either Lean development.
- **Geometric complexity theory** (`ours/GCT_NODES.md`, the nodes of the pequalnp.com board): L-gct-006 (the padding
  lemma), L-gct-010 (the border bound m²/2 of Landsberg, Manivel and Ressayre), L-gct-011 (the Mulmuley–Sohoni
  conjecture for every fixed exponent), L-gct-028, and the board's checked superquadratic border bounds L-gct-070 and
  L-gct-074. Occurrence obstructions cannot give superpolynomial bounds (Bürgisser, Ikenmeyer and Panova,
  arXiv:1604.06431, attached).

## The paper

**"The square decides: wire prices, strict shortenings and the hinge of the two claimed proofs of VP ≠ VNP"**, with a
subtitle naming its main theorems. It opens with Valiant's conjecture and Mulmuley and Sohoni's programme, states both
claimed theorems with their Lean status, and treats them as unrefereed throughout; its abstract names (H_A) and both
preprints as unrefereed inputs. It explains, in prose a newcomer follows, the question both proofs leave open: wires,
hubs and prices; why Euclidean length is the borderline; why one four-point metric decides the planar case. It states
the hinge once, in its strongest form, with exact hypotheses, and proves it. Then it proves this run's theorems. The
results of runs 98 and 99 that the paper uses are our unpublished work: the paper proves each of them, condensed, with
its own proof, and never cites them as published. It credits Strassen's asymptotic spectrum, Christandl, Vrana and
Zuiddam, Bugár and Vrana, Bruhat and Tits and the CAT(0) literature, Izeki and Nayatani, Hurwitz and Khoruzhii, Liu,
Mulmuley and Sohoni, Bürgisser, Ikenmeyer and Panova, and both preprints, by their statements and pages.

## The research

1. **The main question: is the unit square a price over C?** Let e be the metric of the unit square on V = {1, 2, 3, 4}
   (sides 1, diagonals √2) and e′ the square with its centre. Decide whether e is a price over C. By the hinge above
   this decides, under (H_A), whether the complex crossing exponent is 1 or √2, whether every price is a tree
   pseudometric, whether planar strict shortenings exist, and the complex Hurwitz exponent. Attack it on every route
   below, the main question taking most of the time, and take the next route when one stalls.
   - (a) **The prescribed rational systems.** Write out the system of PG-OP-DETERMINISTIC for q = 2, 4, 8, … in order,
     with every dimension computed. Reduce each by its symmetries (the Specht type, the partial transpose, the Gram
     adjustment, the trace condition) to the smallest equivalent system, prove each reduction, and solve the reduced
     systems exactly, by program, with certificates: a feasible point, or a failure with its rational two-cut
     decomposition. A failure at any q proves the square absent. Then decide feasibility for every q: find the
     structure that makes all systems feasible, or the q at which one fails.
   - (b) **The exponent.** Prove a fixed superlinear lower bound for the crossing exponent, which forces the branch √2,
     or prove the exponent is 1. Use the sufficient condition of run 99, Q1d-8: g_α(U_r W^n) ≥ r·2^((1+δ)n) for one
     fixed δ > 0, all r, n ≥ 1 and α along a sequence tending to 0, for the two equally weighted crossing-cut operator
     mean. Decide whether it holds.
   - (c) **Shortenings beyond width 6.** Decide width 7 with the exact-certificate method of SH-60b, then width 8, and
     prove the general statement the certificates reveal: an exclusion for every width, which proves the square a
     price, or a strict shortening at some width, which proves it absent.
   - (d) **Prices beyond trees.** Construct a non-tree price over C (which proves the square present by run 99, Q1), or
     prove every price is a tree pseudometric (absent). Test every spectral construction available: the quantum
     functionals of Christandl, Vrana and Zuiddam, their extensions, and the operator means of Bugár and Vrana, on e and
     e′.
2. **Characteristic two.** Decide whether the unit square is a price over F₂ (equivalently over every field of
   characteristic two). Start from run 99's Q4d: the Hamming-weight block reduction, the exact local rank bounds of the
   Fermat-curve deformation, and the finite bounds P(8) ≤ 16 and P(32) ≤ 132. Remaining there: charged bad-branch
   recursions and larger symbol classes. In characteristic two the permanent is the determinant; say what the answer
   means for the two preprints there.
3. **Contraction and strict shortening.** Prove or refute that contraction implies a strict shortening (run 99, Q3d),
   that is, the mutual exclusion of flatness and contraction (run 98, SH-09). The exact obstacle: pass from the nonprice
   √rank(A − B) on Mat_μ(F₂), μ ≥ 3, to a Euclidean nonprice. Decide also the sufficient gates of SH-33 and PG-IN-GATE.
4. **One statement of the hinge.** Runs 98 and 99 proved the hinge twice: SH-08, SH-15 and PG-CROSSPOLY-GATE in run 98,
   Q3a, Q3b and thm:square-shortening-equivalence in run 99; run 99's proof gives a shortening with nonantipodal wires
   only. Compare the two proofs, state the result once in its strongest form with its exact inputs (C3 alone where only C3
   is used, C3 and A.6 where both are), and prove it in the paper. Then prove the two inputs of the exponent
   theorem that no second model has checked, P(q) ≤ q^(√2+o(1)) and F(β) < 4 for β < √2, in full.
5. **The direct-case exponent.** Decide the supremum of the exponent that hub-displacement arguments give, with the
   matching limit of the method (run 98, Q3: the 4/3 ceilings EX-29, EX-30, EX-42, exactly 5/4 in the orthogonal
   equal-width model, EX-47 and EX-48 open).
6. **(H_A) and the preprints checked where this run rests on them.** Check, as a referee who wants to find the error,
   the proofs of Anthropic's Theorem A.6 and Proposition C.3 and of the Theorem D.2 that Q3c uses. An error found is a
   result of this run: state the passage, the statement it needs, and a counterexample or the missing step.

Record every check event. Every statement of the papers is proved in them or cited with an exact locator.

