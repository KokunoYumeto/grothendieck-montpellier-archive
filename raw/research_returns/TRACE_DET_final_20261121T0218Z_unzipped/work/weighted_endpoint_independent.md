# DET-18 independent check: rational character endpoint and ordinary determinant

Date: 2026-11-21. Checker: GPT-6 Astra Pro; effort not exposed; TRACE_DET_20261121 /root/masullo_spectral_bridge.

## Verdict and version

PASS. I independently read the complete work/paper_weighted_endpoint.tex and the complete work/weighted_endpoint_determinant.md, and checked the exact local source definitions and scalar-transform exports listed below. No mathematical correction is required.

Checked TeX SHA256: 0614f7cf226d3bd84288a1b8158e4032a0b029cc48ab6a14937fce658f07c307.

The result provides an unconditional diagonal trace-class realization of the denominator-cleared completed finite-character product, with the actual scalar endpoint given by a scaled ordinary resolvent trace plus explicit completion and polar terms. For this designated diagonal realization, GRH for the retained family is equivalent to \(0\le C\le4I\). The ordinary determinant without integer multiplication exists exactly under the stated weighted-divisor integrality conditions, including the central half-order condition.

This is a source-text and mathematical proof review. It is not a Lean build, an admission audit, or a re-verification of the stipulated RH/Dirichlet theorem. The classical completion, functional-equation and entire-order facts are retained background, already fixed in MAS-11. This new determinant construction does not depend on Masullo's spectral theorem.

## 1. Exact source scope checked

All Lean paths below are relative to work/external_lean/lean/src/.

I read the complete Development/AutomorphicArithmetic/PrimitiveCosets/LevelFamily.lean. Its private weight assigns coefficient one to the modulus-one character and the actual level weight to each remaining primitive character. Its admissibility proof uses primitivity to show that a principal primitive character has modulus one. The file constructs an actual analytic CharFamily and proves equality with the level scalar, rather than merely postulating a correspondence.

I checked Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/PrimePairSizeCondition.lean:

- PChar carries the primitive-character hypothesis, lines 7–11.
- Its inverse has the same modulus and remains primitive, lines 21–24.
- KSet contains the trivial character, is inverse-closed, and has a real odd optional exceptional character, lines 39–45.

I checked ExplicitFormulaErrorOfHostConditions.lean in that directory, including Level, Nt, wt and Gm. The integer o is nonnegative, \(d=3o+1\ge1\), and each nontrivial weight is either 1 or \(d^{-1}\). Nt erases the single primitive modulus-one character. The scalar is exactly zeta's scalar plus the weighted real parts of the nontrivial character scalars.

I also read the complete Development/AutomorphicArithmetic/DedekindLFunctions/CharFamily.lean and the relevant PoleData interface. A general CharFamily has arbitrary positive real weights and need not contain primitive characters. The proof correctly confines denominator clearing to the actual rational primitive Level family. It does not overgeneralize to that larger interface.

## 2. Completions, partners and endpoints

The completion conventions agree with the explicit customary Dirichlet convention already stated in work/paper_masullo_characters.tex:

\[
F_\chi(s)=(q/\pi)^{(s+\kappa_\chi)/2}
\Gamma((s+\kappa_\chi)/2)L(s,\chi),
\qquad
F_\zeta(s)=2\xi(s).
\]

The nonprincipal primitive completion is entire of order one; the principal factor \(s(s-1)\) removes the two simple poles without adding zeros. The cited classical inputs are DLMF 25.15.5–6, the stated Kedlaya functional equation and the entire-order statement retained in MAS-11. I checked their use against the already established MAS-11 conventions; this independent check does not claim a fresh re-proof of analytic continuation.

The functional equation is

\[
F_\chi(s)=\epsilon_\chi F_{\chi^\vee}(1-s).
\]

Applying the equation again gives
\(F_\chi(s)=\epsilon_\chi\epsilon_{\chi^\vee}F_\chi(s)\).
Since the entire function is not identically zero,
\(\epsilon_\chi\epsilon_{\chi^\vee}=1\). Thus the product
\(F_\chi(s)F_{\chi^\vee}(s)\) is exactly invariant under \(s\mapsto1-s\), with no residual phase. No assumption that an individual nonselfdual completion is even is made.

The nonvanishing statement in
Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/CharFamilyLFunctionNeZeroOfOneLeRe.lean was read in full. It gives the source's nonvanishing on \(\Re s\ge1\) for the admissible family. At 1, a nonprincipal completion has finite nonzero conductor and gamma factors and \(L(1,\chi)\ne0\); hence \(F_\chi(1)\ne0\). The functional equation gives \(F_\chi(0)\ne0\). This remains valid for even nonprincipal characters whose uncompleted L-function vanishes at 0: its gamma pole is cancelled in the completion. For zeta, \(F_\zeta(0)=F_\zeta(1)=1\).

Reflection gives nonvanishing of the completed functions on the other boundary as well. Thus their zeros lie in the open strip, and the denominator \(v_\rho=\rho(1-\rho)\) is never zero. The normalization at 0 is legitimate.

## 3. Integer multiplication and weighted multiplicities

For the actual weights \(\alpha_i\in\{1,d^{-1}\}\), the proposed choice

\[
M=2d=2(3o+1),\qquad b_i=M\alpha_i/2\in\{d,1\}
\]

is sufficient. It is not asserted to be minimal.

Every exponent in

\[
\mathscr P_M(s)=
\left(\frac{F_\zeta(s)}{F_\zeta(0)}\right)^M
\prod_i
\left(
\frac{F_{\chi_i}(s)F_{\chi_i^\vee}(s)}
{F_{\chi_i}(0)F_{\chi_i^\vee}(0)}
\right)^{b_i}
\]

is an integer. Each factor is entire. Partner root-number cancellation and zeta symmetry imply

\[
\mathscr P_M(s)=\mathscr P_M(1-s),\qquad
\mathscr P_M(0)=\mathscr P_M(1)=1.
\]

It has order at most one.

For each distinct zero \(\rho\) of the retained union,

\[
S_\rho=m_\zeta(\rho)
+\sum_i\frac{\alpha_i}{2}
\left(m_{\chi_i}(\rho)+m_{\chi_i^\vee}(\rho)\right)
\]

is positive, and the product's order at \(\rho\) is exactly \(MS_\rho\). Coincident zeros of different characters are added rather than identified without multiplicity. The symmetry gives \(S_\rho=S_{1-\rho}\).

The functional equation gives equal central orders for a character and its partner. Thus every paired factor has even central order. Zeta's own symmetry gives even central order. Consequently \(MS_{1/2}\) is even. The proof does not assume that the characters have no central zeros.

## 4. Entire descent and central branching

With \(E(z)=\mathscr P_M(1/2+z)\), evenness gives a unique entire function \(\mathscr D_M\) such that

\[
E(z)=\mathscr D_M(1/4-z^2).
\]

The proof correctly avoids selecting a branch of the square root. For every \(|v|\le R\), a preimage satisfies
\(|z|\le\sqrt{R+1/4}\), so the displayed maximum-modulus estimate implies that \(\mathscr D_M\) has order at most \(1/2\). Its normalization is \(\mathscr D_M(0)=1\).

The quadratic map has precisely two preimages away from its central branch point. A noncentral pair \(\{\rho,1-\rho\}\) contributes one zero \(v_\rho\) of order \(MS_\rho\); it does not contribute twice that order.

At the central point,

\[
v=s(1-s)=1/4-(s-1/2)^2.
\]

Pullback doubles the order. Therefore the determinant's zero at \(v=1/4\) has order

\[
q_{1/4}=MS_{1/2}/2,
\]

which is an integer by the preceding paragraph. This is the required central half-multiplicity. No central block is removed in this construction.

## 5. Trace class and the ordinary determinant

For an entire function of order at most \(1/2\), the proof chooses
\(1/2<\theta<1\). The maximum-modulus bound and Jensen's formula give
\(n(R)=O_\theta(R^\theta)\), with multiplicities. Dyadic summation then gives

\[
\sum_a\frac{q_a}{|a|}<\infty.
\]

There is no zero at 0, so the finitely many small zeros cause no difficulty.

The order is strictly below one, so genus-zero Hadamard factorization gives

\[
\mathscr D_M(v)=\prod_a(1-v/a)^{q_a},
\]

without a nonconstant exponential. The value at 0 fixes the constant to one.

The operator is explicitly diagonal in an orthonormal basis, with entry \(a^{-1}\) repeated \(q_a\) times. Its singular-value sum is the displayed absolutely convergent sum, which proves trace class directly. No nonnormal trace-ideal inference is used.

The ordinary determinant is exactly \(\mathscr D_M\), and therefore

\[
\det(I-s(1-s)C_{\mathcal L,M})=\mathscr P_M(s).
\]

All of this is independent of GRH.

## 6. Resolvent derivative and the central pole

The product exponents give \(\mathscr P_M'/\mathscr P_M=M\mathscr L_{\mathcal L}\). Absolute local uniform convergence of the reciprocal-eigenvalue series away from determinant zeros gives

\[
\frac{\mathscr D_M'(v)}{\mathscr D_M(v)}
=-\operatorname{Tr}(C_{\mathcal L,M}(I-vC_{\mathcal L,M})^{-1}).
\]

The inverse is bounded by the same diagonal tail argument. Since \(v'(s)=1-2s\), the sign in the final identity is correctly positive:

\[
\mathscr L_{\mathcal L}(s)
=\frac{2s-1}{M}
\operatorname{Tr}(C_{\mathcal L,M}
(I-s(1-s)C_{\mathcal L,M})^{-1}).
\]

For \(z=s-1/2\), a central coordinate has eigenvalue 4 and contributes

\[
\frac4{1-4(1/4-z^2)}=\frac1{z^2}.
\]

A block of size \(q=MS_{1/2}/2\) contributes \(q/z^2\). Multiplying by \(2z/M\) gives \(S_{1/2}/z\), precisely the weighted logarithmic derivative's pole. If there is no central zero, the inverse is bounded there and both sides vanish. No division by \(2s-1\) occurs.

## 7. Exact Mellin and completion corrections

I read the complete nonprincipal Mellin source proof
LandauTheorems/mellinGchiOfNeOne.lean, including the absolute-integrability and summability argument and the main theorem at lines 116–119. I checked the zeta theorem at mellinGchiModOne.lean:115–118 and the complete logarithmic change of variables at poleData.lean:114–135.

For a nonprincipal character the source is exactly

\[
\Phi_\chi(s)=
-\frac{L'(s,\chi)/L(s,\chi)}{s(s-1)}
+\frac{L'(1,\chi)/L(1,\chi)}{s-1}.
\]

Its second term has a plus sign, matching the source's linear correction
\(yL'(1,\chi)/L(1,\chi)\).

For zeta, the displayed source expression is algebraically

\[
\Phi_\zeta(s)=
-\frac{\zeta'(s)/\zeta(s)}{s(s-1)}
-\frac1{(s-1)^2}
+\frac{1+\gamma_E}{s-1}.
\]

The gamma and conductor logarithmic derivatives are

\[
a_\zeta(s)=\frac1s+\frac1{s-1}
-\frac12\log\pi+\frac12\psi(s/2),
\qquad
a_\chi(s)=\frac12\log(q/\pi)
+\frac12\psi((s+\kappa_\chi)/2).
\]

Partners have the same conductor and parity, so their completion terms agree. This explains the coefficient \(\alpha_i\), rather than \(\alpha_i/2\), in the sum defining \(A_{\mathcal L}\).

I read the complete GchiConj.lean. Its derivative-conjugation lemma also verifies the constant at 1. Thus the source real-part function is the half-sum of the two partner functions before transformation. This remains a half-sum at the same complex variable s after transformation; it is not an incorrect real part of a holomorphic transform.

These calculations give exactly

\[
\Phi_{\mathcal L}(s)
=\frac{A_{\mathcal L}(s)-\mathscr L_{\mathcal L}(s)}{s(s-1)}
-\frac1{(s-1)^2}+\frac{b_{\mathcal L}}{s-1},
\]

with the displayed real constant \(b_{\mathcal L}\). All correction terms and signs agree.

Absolute convergence holds on \(\Re s>1\): direct integration of each absolute ramp term gives the convergent von Mangoldt Dirichlet series divided by \(\sigma(\sigma-1)\); the linear and \(y\log y\) corrections also converge there. The generic PoleData interface only asserts its identity on \(\Re s>2\), which is a smaller domain. The paper distinguishes these statements.

I also read poleData.lean:248–390. Its transform is the exact partner half-average and its residue is \(S_\rho/[\rho(1-\rho)]\). In the open strip the completion correction terms are analytic, so the paper's formula has precisely this residue, including at the center.

## 8. Exact unscaled determinant criterion

Necessity is correct: an ordinary entire determinant has integer zero orders. Pullback under \(s(1-s)\) preserves each noncentral order and doubles the central one. Equality of meromorphic logarithmic derivatives therefore requires

\[
S_\rho\in\mathbb Z_{\ge0}\quad(\rho\ne1/2),\qquad
S_{1/2}/2\in\mathbb Z_{\ge0}.
\]

The central condition cannot be replaced merely by integrality of \(S_{1/2}\).

For sufficiency, divide every multiplicity in \(\mathscr D_M\) by M. These exact conditions make the resulting multiplicities nonnegative integers; their reciprocal-zero sum remains finite. The resulting diagonal ordinary determinant D satisfies \(D^M=\mathscr D_M\) by the convergent products. Logarithmic differentiation after pullback gives the requested unscaled derivative.

Thus no hidden exponential ambiguity remains in the sufficiency argument. The equivalent normalized germ statement is valid because its value at 0 fixes the root. The least divisor-level multiplier is the stated least common multiple of denominators. Every denominator divides the fixed integer \(2d\), including the central half-order denominator, so that least common multiple is finite. Its actual value is not asserted.

The paper correctly does not assert that an actual zero has a fractional weighted multiplicity. Rationality of the source coefficients alone does not determine divisibility of the weighted zero orders.

## 9. Actual inverse closure and positivity

The source's real exceptional character is fixed by inversion. All other characters have the same weight \(d^{-1}\). Since the finite set is inverse-closed and inversion fixes the erased trivial character, it permutes the nontrivial set and preserves its weights. Reindexing therefore gives

\[
S_\rho=m_\zeta(\rho)+\sum_i\alpha_i m_{\chi_i}(\rho).
\]

This proves the stated noncentral denominator simplification. The proof does not mistake the original general half-average for an extra denominator that must persist in this particular family, nor claim a minimal value for M.

For \(\rho=\beta+it\) in the open strip,

\[
\rho(1-\rho)=\beta(1-\beta)+t^2+it(1-2\beta).
\]

Its real part is positive. Under GRH its reciprocal belongs to \((0,4]\), including 4 for a central zero.

Conversely, the bound \(0\le C_{\mathcal L,M}\le4I\) makes every retained reciprocal real and positive. Hence either \(\beta=1/2\) or \(t=0\). A real off-center zero would give
\((\beta(1-\beta))^{-1}>4\), violating the bound. Positive weights ensure that no retained zero is cancelled from the operator. This proves the equivalence with GRH for the retained family.

Positivity without the upper bound would not suffice: it logically permits such a real off-center zero. The paper states that qualification without claiming an example exists.

## 10. Trace scaling, eigenvalue scaling and scope

Under stipulated GRH, C is nonzero positive and \(\operatorname{Tr}(C^2)>0\). The coefficient of v in the scaled resolvent trace is
\(\operatorname{Tr}(C^2)/M\); replacing C by C/M instead gives
\(\operatorname{Tr}(C^2)/M^2\). These differ when \(M>1\). Thus scaling the trace does not absorb the multiplicity multiplier by scaling eigenvalues.

All requested checks pass. The construction represents the actual scalar endpoint after explicit completion and polar corrections, but its diagonal operator is constructed from the completed zero divisor. It does not identify an upstream period matrix, the historical step-4 operator, or a zero-independent arithmetic Hilbert realization.

