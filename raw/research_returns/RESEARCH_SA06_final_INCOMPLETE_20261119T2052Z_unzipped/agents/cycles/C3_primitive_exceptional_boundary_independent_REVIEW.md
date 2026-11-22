# Independent audit of the entire primitive exceptional-boundary argument

**Final-file addendum, 2026-11-19 15:18:49 UTC:** I have now read the actual rewritten Step 3 in `../frobenius/C3_primitive_exceptional_boundary.tex`, including PB.10–PB.13 and the moved formal-existence citations in Step 4.  The final free integral tensor-quotient proof passes exactly as stated.  All other mathematical steps agree with the fully reviewed original.  Stacks 01XS, Lemmas 30.8.1–30.8.2 and their projective-space cohomology calculation, was additionally freshly opened for the ambient Euler calculation.

**Reviewer:** GPT-6 Astra Pro, `/root/cycles`, run RESEARCH_SA06.  This is an independent agent re-proof, not independent-model verification.

**Completed:** 2026-11-19 15:17:33 UTC.

**Reviewed object:** `../frobenius/C3_primitive_exceptional_boundary_draft.tex`, all of PB.1–PB.18, including the original Witt-lift proof of Step 3.  I also independently checked the author's subsequently proposed integral quotient replacement for that step.  The auxiliary proposition passes in its stated geometric scope for every characteristic (p>0), every (s\geq1), and every (m\geq0).  This receipt does not certify a new combined local construction or its geometric choices.

## 1. Exact relative class and the entire Chow kernel

I rechecked the locally split rank-one square-zero Milnor sequence, the exponent-(p) kernel, and the canonical conormal differential map, using the previously independently audited all-degree auxiliary.  Divisibility of (H^{n-1}(V,\mathcal K_n^M)) makes the relative cohomology map injective.  Thus an absolute class reducing to zero has a unique relative lift.  This uniqueness is used correctly; it is not replaced by a choice-dependent first-order class.

The integral Chow decomposition follows from the explicit point-blow-up and projective-bundle formulas with arbitrary products.  It retains the complete Picard group of the curve.  I independently rederived the elementary positive-adjoint argument: multiplication by (b) is injective in negative weight, and its square is injective at weight at most (-2), including the weight-(-2) endpoint.  At degree (s-1) the weight is (-m-2).  Consequently the equations (b\alpha=0), (e\alpha+bv=0) force (v=\alpha=0) over the integral free lattices.  The remaining kernel is exactly the Smith kernel with (d_jQ_j=0).  No torsion invariant factor is discarded or inverted.

## 2. Saturation, including primes dividing Smith coefficients

The original typed Witt argument is valid.  Cubic Picard classes lift because (H^2(\mathcal O_W)=0); the prescribed hyperplane class can be included in an integral basis because it has degree one on a line.  The Euler and conormal sequences identify the relevant (H^1(\Omega_W^1(A))) over the Witt ring with a free rank-four projective-space cohomology module.  Only the fixed multidegree ((0;1,\ldots,1)) is used, so no comparison of the complete Chow rings of the two fibres is assumed.  The resulting torsion-free target kills every saturation vector (w_j).

The proposed simpler replacement also passes, and makes this step entirely integral.  Define

\[
\Psi:B_s\longrightarrow\bigotimes_i\bigl(\operatorname{Pic}(W_i)/\mathbb Z A_i\bigr)
\]

by the indicated multidegree projection followed by the quotient.  Each factor is free.  Every contribution of (bv\) to that multidegree inserts an (A_i\), while the projective-space contribution has the wrong multidegree.  Hence (\Psi(bv)=0\), and torsion-freeness implies (\Psi(w_j)=0\) from (bv_j=d_jw_j\).  The map (\Phi_k\) factors through (\Psi\), because (\mu_{A_i}=0\) follows from the ambient Euler sequence.  Thus (\Phi_k(w_j)=0\) in every characteristic, without any division or Witt lift.

## 3. Actual line bundles and the curve-product term

I checked (H^2(V,L^n)=0\) for every positive (n\), and the displayed (H^1\) calculations.  Successive Picard lifting therefore gives a compatible system of invertible sheaves.  Projective formal existence, regularity of the excellent completion map, Popescu, finite-presentation descent, and the henselian smooth lifting lemma give an actual line bundle on the fixed \(\mathcal Z\), preserving a prescribed finite jet.  Only finitely many individual lifts are required.

The definition

\[
\widetilde K=\mathcal O_{\mathcal Z}(-V)\otimes q^*L_T^{-1}
\]

is an actual identity of line bundles and does not assume a nonexistent map to (C\).  For (Q\in\operatorname{Pic}^0(C)(k)\), the product \(c_1(\widetilde K)c_1(\widetilde Q)\) reduces to zero because its reduction is a product on the curve.  Its relative lift is unique.  Changing \(\widetilde Q\) changes the differential by \(a'\smile d\log K_C\), which vanishes by curve cohomological degree two.  Hence the differential depends only on (Q\), is additive, and vanishes because its source is divisible and its target is killed by (p\).  The proof correctly asserts only vanishing of this differential, not vanishing of the relative Milnor class itself.

## 4. Exact exceptional identity and final contradiction

The projection formula and the actual normal-line identity give PB.18 in integral Chow groups.  The first summands have a nil line factor \(\widetilde Q_j^{d_j}\) and are killed by the saturated lattice calculation.  The second summands have the unique relative curve-product class just treated, so their differential is zero after multiplication by the actual divisor polynomial (v_j\).  Each summand reduces to zero separately, making uniqueness of the relative lift applicable to their sum.

The finite-stage argument is correct: the line bundles, divisor polynomials and finite rational-equivalence witnesses descend to a single pointed étale neighbourhood.  Properness allows the base to be shrunk so that its whole source is regular; over perfect (k\) it is smooth.  The first infinitesimal fibre remains the same.  The integral Milnor–Bloch formula and its multiplicative compatibility are applied on this smooth model, then pulled to (E\).  They are not asserted on the nonreduced (E\).  The nonzero designated relative component therefore contradicts exceptional support.

## 5. Primary sources actually checked

Fresh full statement/proof reads in this audit:

- Stacks **0AH2**, Lemma 15.51.14: regularity of completion of a G-ring; opened reference `turn355795768view0`.
- Stacks **07GC**, Theorem 16.12.1: Popescu; `turn355795768view1`.
- Stacks **0B8W**, Lemma 32.10.3(2): descent of an invertible sheaf; `turn355795768view2`.
- Stacks **0H74**, Lemma 15.13.3: smooth lifting over a henselian pair, including a prescribed reduction modulo the square of the maximal ideal; `turn355795768view3`.
- Stacks **0885**, Lemma 30.24.3: projective formal existence; `turn987817111view0`.
- Stacks **0C6R**, Lemma 37.4.1: the square-zero Picard sequence; `turn987817111view1`.

The exact Rost, Kerz, Braunling, Jiang, cubic-surface and projective-bundle inputs were already read in this audit window and are recorded in the degree-two/all-degree divisibility, lattice, bj and bk reviews.  I independently derived the Euler/conormal computation here.  No source theorem identifying a formal Picard functor with an actual family was imported.

## 6. Scope and computation

No new computation was needed or run for this auxiliary re-proof.  The existing finite Smith tables are illustrative certificates, not substitutes for the all-(m,s\) elementary argument.  The receipt certifies the entire exceptional-image proposition under PB.1–PB.2 and the nonzero-cup hypothesis; it does not establish the separate existence of an ordinary fixed-product family or the principal target needed in a combined theorem.
