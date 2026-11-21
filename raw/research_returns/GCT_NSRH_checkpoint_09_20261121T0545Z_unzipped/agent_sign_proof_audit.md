# Independent audit of MAIN_PROOF_DRAFT.md, F1–F5

Date: 2026-11-21 (Europe/Berlin). Reviewer: `/root/gct_statements`; model GPT-6 Astra Pro; effort inherited/not exposed. Reviewed version: the draft beginning “Main proof draft — GCT_NSRH_20261121_root”, with F3 allowing real a and the original all-embedding duality sentence. Whole proofs F1–F5 were read. These are elementary conditional reductions, not a proof of a pre-existing precisely formulated GCT nonstandard RH.

## Overall outcome

**F1, F2, F3's upper bound and one-embedding equality, F4's upper bound and one-embedding equality, and F5's countermodels pass.** One explicit hypothesis is required for the all-conjugate equality statement in F3/F4: the dualizing scalar c must have the intended absolute value in every complex embedding, which is automatic when w=a+d is an integer and c=q^w is the rational Tate scalar. The current clause merely requiring that c be algebraic is insufficient. A few wording/domain clarifications are listed below.

## F1 — targeted proof check and independent reconstruction

Let K_h(x,y)=psi(h<x,y>). For h nonzero,

\[
(K_hK_h^*)_{x,x'}=\sum_y\psi(h\langle x-x',y\rangle)
=Q^d\delta_{x,x'}.
\]

The second equality uses nondegeneracy in the first slot; for a finite-dimensional square bilinear pairing, nondegeneracy is enough. Hence its operator norm is Q^(d/2). Expand the alternating product with k−1 K factors and k−2 diagonal D factors: its matrix coefficient t^T K D K ... D K t is exactly the path sum. The row functional t^T has norm ||t||2, even for complex t: it is the Hermitian dual of conjugate t. For k=2 the product has no D factor and the same inequality holds. Character orthogonality proves the exact identity. No hidden reality or sign condition was found. **PASS.**

## F2 — independent re-proof by Cesàro orthogonality

This re-proof avoids the draft's generating-series pole argument and confirms its conclusion. Let rho=max_j|alpha_j|>0, put z_j=alpha_j/rho for the indices J with |alpha_j|=rho, and write

\[
p_n/\rho^n=\sum_{j\in J}c_jz_j^n+o(1).
\]

The finite unit-circle numbers z_j are distinct. Therefore

\[
\frac1N\sum_{n=1}^N\left|\sum_{j\in J}c_jz_j^n\right|^2
\longrightarrow\sum_{j\in J}|c_j|^2>0,
\]

because each off-diagonal geometric mean N^−1 sum_(n≤N)(z_j conjugate(z_l))^n tends to 0, while diagonal means are 1. The bounded sequence p_n/rho^n has the same mean-square limit, since its difference from that finite trigonometric sum tends to zero. It follows that |p_n|/rho^n is bounded below by a positive constant along an infinite subsequence. This gives limsup |p_n|^(1/n)≥rho. The triangle inequality gives ≤rho. The draft's independent pole proof is also correct. **PASS.** Explicitly require the proposed comparison radius R>0, and treat the empty spectral set separately as vacuous, as the draft already does.

## F3 — independent reconstruction and one genuine missing hypothesis

First make q a prime power greater than 1, so F_(q^n) exists for every n. Combining the pointwise bound with F1 gives

\[
\|t_n\|_2^2\le B^2Q^{a+d},\qquad
|R_{k,n}|\le (Q-1)B^kQ^{k(a+d)/2+d/2}
\le B^kQ^{k(a+d)/2+d/2+1}.
\]

The exponent d/2+1 is correct; no k-dependent exponential overhead was omitted. Put P_(k,n)=sum_(beta∈B_k) beta^n. The exact identity and S1–S2 give

\[
-\epsilon^kR_{k,n}=P_{k,n}+\sum_{(\alpha_1,\ldots,\alpha_k)\in A^k}(\alpha_1\cdots\alpha_k)^n.
\]

All multiplicities after regrouping coincident roots are **positive integers**. In particular each alpha^k survives; accidental equality with a B_k root only increases its coefficient. Applying F2 for each fixed k yields

\[
|\alpha|\le q^{(a+d)/2+(d/2+1)/k}.
\]

Constants B^k may depend on k without harm, since n→∞ is taken for fixed k. Then take k through the unbounded K. This order of limits is valid. There is no requirement of an estimate uniform in k for the prefactor, only that the exponential overhead divided by k tends to 0. S2 is a strong spectral parity/concentration hypothesis; it is not implied by positivity of numerical values. **Upper-bound proof PASS.**

For one embedding, multiset duality alpha↦c/alpha with c=q^(a+d)>0 gives the reverse bound immediately. **One-embedding equality PASS.**

**Correction required for all embeddings.** If a is an arbitrary real number and c=q^(a+d) is only assumed algebraic, an embedding sigma can have |sigma(c)|≠c. Transporting the duality gives sigma(alpha)↦sigma(c)/sigma(alpha), so the reverse bound is |sigma(alpha)|≥|sigma(c)|/q^((a+d)/2), not necessarily the target q^((a+d)/2). Example of the underlying spectral issue: c=2+sqrt(3), A={sqrt(c)}, and weight w=log_q(c). A is stable under alpha↦c/alpha; all conjugates of alpha have modulus at most sqrt(c), but some have modulus 1/sqrt(c). Thus “all-conjugate upper bounds + this algebraic duality” alone does not give all-conjugate equality. Restrict the purity conclusion to **integer w=a+d and c=q^w**, or explicitly require **|sigma(c)|=q^w for all sigma**. That is the usual Tate situation and is the intended geometric case.

**All-embedding trace-system clarification.** The draft originally allows t_n to have arbitrary complex values, so applying an algebraic embedding to t_n is not intrinsically defined. State instead: for each embedding sigma of the algebraic spectral data into C, a corresponding family t_(n,sigma) satisfies the same hypotheses with spectra sigma(A), sigma(B_k) and a bound B_sigma independent of n,k; B_sigma may depend on sigma. Algebraic-valued trace functions with the specified compatible embeddings are an alternative. This is a formulation repair, not a failure of the spectral argument.

The geometric explanation of parity is correct if the relevant compactly supported cohomology really is concentrated in degree d and kd−1. It correctly says dimension alone does not imply this. For Tate twist (−1), geometric Frobenius eigenvalues are multiplied by Q, as used. Duality of the coefficient system and identification of the relevant cohomologies remain assumptions.

## F4 — targeted proof check

The rearranged positive spectral sum is epsilon^k(E_(k,n)−R_(k,n)). Its exponential growth rate is bounded by

\[
q^{k(a+d)/2+\max(d/2+1,\eta_k)}.
\]

The factors C_k, B^k and n^(A_k) have no effect on the limsup nth root at fixed k. The quotient max(d/2+1,eta_k)/k tends to 0 under eta_k/k→0. Thus the upper bound and, with the corrected duality condition, purity follow. **PASS subject to the same all-embedding scalar correction as F3.**

The concluding phrase “exact removal ... is allowed only with this ... error budget” overstates a sufficient criterion as a general necessity theorem. Suggested wording: “This criterion permits removed background terms when the displayed error bound holds, or when their spectra can be placed explicitly in the positive-sign sum. It does not justify silently discarding uncontrolled boundary terms.” Other unrelated cancellation information might also control larger errors, so “only” should be avoided.

## F5 — whole-proof countermodel check

- **(a) Constant trace:** t_n=1 on F_(q^n) gives M_n=q^n, with alpha=q and a=0,d=1. F1 applies exactly. The claimed sqrt(q) bound fails, so the analytic identity and Parseval bound alone cannot establish it. Actual H_c^2(A1)=Q_l(−1) explains the wrong middle-degree premise. **PASS.**
- **(b) Virtual cancellation:** Q_l(−1) in cohomology degree 0 and another in degree 1 has equal q-eigenvalues, opposite alternating signs, and zero virtual trace for all n. The complex Q_l(−1)⊕Q_l(−1)[−1] uses the usual cohomological shift correctly. Total zeta=1. **PASS.**
- **(c) Upper bound versus purity:** eigenvalue 1 satisfies an upper weight-1 norm estimate and has actual weight 0. **PASS.**
- **(d) Restricted extension degrees:** spectrum {R,−R} has zero traces for all odd n and arbitrarily large roots. **PASS.** Replace the wording “all n ... are necessary” by “F2 as used here assumes all n; arbitrary subsequences are insufficient.” Other sufficiently rich sets of n can also work; a progression needs separate regrouping/noncancellation conditions. No false necessity theorem is needed.
- **(e) Fourier positivity:** normalized 3×3 Fourier kernel has a nonreal diagonal entry, so it is not Hermitian and not positive semidefinite. The 2×2 Walsh matrix has eigenvalues ±1. Thus Parseval/unitarity is not operator positivity. **PASS.**
- **(f) Purity/semisimplicity:** projection Gal(Fbar_q/F_q)=hat Z→Z_l, followed by a unipotent representation, is continuous. Choose the generator sign to make geometric Frobenius act as the displayed matrix; either sign has the same conclusion. Eigenvalues 1 at every extension yield punctual weight 0 and traces 2, while the arithmetic representation is not semisimple. The draft correctly distinguishes this from geometric semisimplicity: over the geometric point the representation is trivial. **PASS.**

## Check-event rows recommended

Use the actual run identifier and this date, model and unexposed effort metadata.

| ID | Type | Outcome |
|---|---|---|
| F1 | independent re-proof | PASS; reconstructed character identity and operator norm estimate in full |
| F2 | independent re-proof | PASS; independent Cesàro proof above; draft pole proof also read |
| F3-upper | independent re-proof | PASS; positive regrouping and two-limit exponent calculation checked |
| F3-purity-one-embedding | targeted proof check | PASS |
| F3-purity-all-embeddings-original | targeted proof check | GAP: algebraic dualizing scalar need not have same absolute value at every embedding; integer Tate weight fixes it |
| F4 | targeted proof check | PASS with F3 scalar correction; sufficient/necessary wording corrected |
| F5a–F5f | targeted proof check | PASS; qualifications in (d),(f) above |

No Lean certificate or computation was used for these checks. The proof-check classifications should not be changed into formal verification.

## Final check of the revised draft

The entire revised F1–F5 draft was re-read after the root corrected the hypotheses. SHA-256 of the reviewed file: `1b952cfcf157965f86bd674eb236a4cce4a948374b2433ac948984f4ca0e9733`. It now assumes a is an integer, q is a prime power >1, explicitly supplies trace functions t_(n,sigma), calls the error budget sufficient, and no longer asserts a universal necessity of all extension degrees. **All F1–F5 proofs pass the targeted full-proof check in this revised form.** The original all-embedding gap above is resolved; retain its history in CHECK_EVENTS rather than treating it as still open. A harmless explicit convention R>0 in F2 is recommended when typesetting. No new change to the mathematics is needed.
