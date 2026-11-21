# DET-18: the actual rational character endpoint and an ordinary determinant

Date: 2026-11-21. Author: /root/step1_history_route, GPT-6 Astra Pro; effort setting not exposed.

## Result and scope

The actual finite level endpoint has rational character weights. Its completed weighted logarithmic derivative is exactly a scaled ordinary Fredholm resolvent trace after clearing those denominators. A safe source-explicit multiplier is \(M=2(3o+1)\). The resulting determinant is a normalized product of completed, pole-cleared primitive Dirichlet functions. This is an unconditional analytic construction from the completed zero divisor. The stipulated Dirichlet GRH makes the diagonal operator positive and bounded above by four.

The full integration-ready proof is in **work/paper_weighted_endpoint.tex**. It was read in full after writing, including the central-point calculation, exact completion corrections, and the converse integrality criterion. An independent checker was sent that complete version; their result is separate from this author's proof check.

The construction does not identify an upstream finite period matrix or the historical step-4 operator. It also does not assert that any actual retained zero has a nonintegral weighted multiplicity. The exact condition for an uncleared ordinary determinant is stated below.

All Lean paths in this note are relative to **work/external_lean/lean/src/**. No Lean build, proof-admission audit, or re-audit of the stipulated RH/Dirichlet theorem was performed.

## 1. Exact source interfaces

| Input | Exact locator | What was checked |
|---|---|---|
| Primitive characters and their duals | Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/PrimePairSizeCondition.lean:7–24 | PChar carries prim; its inverse has the same modulus and is primitive. |
| Actual finite set | The same file:39–45 | KEPT contains one, is inverse-closed, and its optional exceptional character is real and odd. |
| Actual weights | Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/ExplicitFormulaErrorOfHostConditions.lean:8–9,32–38 | o is a natural number; Nt erases the modulus-one character; wt is 1 or \(1/(3o+1)\); Gm is Gz plus the weighted real nontrivial sum. |
| Scalar family instantiation | Development/AutomorphicArithmetic/PrimitiveCosets/LevelFamily.lean:9–25,27–52 | Full file read. Zeta has weight one; remaining source weights are retained; the analytic CharFamily and Gm are actually constructed, with equal zero-free predicates. |
| General analytic family scope | Development/AutomorphicArithmetic/DedekindLFunctions/CharFamily.lean:10–32,36 | General CharFamily requires finiteness, positive real weights and an admissibility condition; it does not require primitivity or rationality. DET-18 restricts to the actual Level family. |
| Actual scalar corrections | Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/Analytic.lean:9–24 and Development/AutomorphicArithmetic/DedekindLFunctions/CharFamily.lean:15–22 | Zeta correction is \(-y\log y+(1+\gamma_E)y\); nonprincipal correction is \(yL'(1,\chi)/L(1,\chi)\). |
| Nonprincipal Mellin transform | Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/mellinGchiOfNeOne.lean:116–119 | Entire file read, including the absolute integral summability argument and main proof. Domain is \(\Re s>1\). |
| Zeta Mellin transform | Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/mellinGchiModOne.lean:115–118 | Displayed formula rechecked; the full DET-11 calculation was reread. |
| Logarithmic change of variable | Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/poleData.lean:114–135 | Complete change-of-variable proof read. |
| Character conjugation | Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/GchiConj.lean:10–51 | Full file read; includes the derivative conjugation needed for the correction at one. |
| Actual half-average | Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/poleData.lean:248–261,288–304 | The constructed scalar transform is \(\sum_i\alpha_i(\Phi_{\chi_i}+\Phi_{\chi_i^{-1}})/2\). |
| Actual residue | The same file:344–364 | \(S_\rho=\sum_i\alpha_i(m_i+m_i')/2>0\), and residue \(S_\rho/[\rho(1-\rho)]\). |
| Boundary nonvanishing | Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/CharFamilyLFunctionNeZeroOfOneLeRe.lean:9–20 | Full file read. Source uses nonvanishing for \(\Re s\ge1\); functional-equation reflection excludes completed zeros on the other boundary. |
| Generic Laplace domain | Development/AutomorphicArithmetic/DedekindLFunctions/LandauZeroFreeCriterion.lean:15–23 and LandauTheorems/poleData.lean:91–112,137–144 | Generic PoleData states the transform on \(\Re s>2\). The actual Mellin formulas and direct absolute majorants give \(\Re s>1\). These domains were not conflated. |

Two initial guessed filenames, work/paper.tex and a TotientGaloisClasses/PChar.lean, were absent. The actual definition was located by rg and read in PrimePairSizeCondition.lean. These path misses support no mathematical absence claim.

## 2. Classical completion inputs and independent source check

The completion conventions are those already fixed in **work/paper_masullo_characters.tex**, read in full before this proof:

\[
F_\chi(s)=(q/\pi)^{(s+\kappa_\chi)/2}
\Gamma((s+\kappa_\chi)/2)L(s,\chi),\qquad
\kappa_\chi=(1-\chi(-1))/2
\]

for nontrivial primitive \(\chi\), and

\[
F_\zeta(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)=2\xi(s).
\]

The two principal poles are cancelled without adding zeros. The functional equation is \(F_\chi(s)=\epsilon_\chi F_{\chi^\vee}(1-s)\), with \(\chi^\vee=\chi^{-1}\) and \(\epsilon_\chi\epsilon_{\chi^\vee}=1\). These functions are entire of order one.

The primary background was reopened in this run:

- [DLMF §25.15](https://dlmf.nist.gov/25.15), equations (25.15.5)–(25.15.6), for the primitive functional equation and Gauss-sum convention; (25.15.9) for nonvanishing at one.
- [Kedlaya, Chapter 6](https://kskedlaya.org/ant/chap-funceq2.html), §6.1 and (6.2.2), for the even/odd completed derivation. The completion used here is the DLMF-compatible one already fixed in MAS-11; the isolated typographical normalization issue in Kedlaya's displayed (6.1.4) is not imported.
- [Rajan, Distribution of values of Hecke characters of infinite order](https://www.researchgate.net/publication/266311380_Distribution_of_values_of_Hecke_characters_of_infinite_order), author-uploaded full text, §1, p.282, for the entire-order-one assertion after multiplying by the principal polar factors.

These established functional-equation/order statements are background inputs, not new re-proofs of the classical analytic continuation theorem. Their application and all determinant arguments below were independently calculated.

Nonprincipal \(L(1,\chi)\ne0\), finite nonzero gamma factors there, and the functional equation imply \(F_\chi(0)F_\chi(1)\ne0\). Also \(F_\zeta(0)=F_\zeta(1)=1\). Thus normalization at \(s=0\) is legitimate even for an even nonprincipal character whose uncompleted L-function vanishes there.

## 3. Integer multiplication and symmetry

Set \(d=3o+1\) and \(M=2d\). For each actual nontrivial index, \(b_i=M\alpha_i/2\) is either d or 1. Define

\[
\mathscr P_M(s)=
\left(\frac{F_\zeta(s)}{F_\zeta(0)}\right)^M
\prod_i\left[
\frac{F_{\chi_i}(s)F_{\chi_i^\vee}(s)}
{F_{\chi_i}(0)F_{\chi_i^\vee}(0)}
\right]^{b_i}.
\]

This finite product uses integer powers only. Each pair is invariant under \(s\mapsto1-s\), because the two root numbers multiply to one. Therefore \(\mathscr P_M\) is entire of order at most one, symmetric about \(1/2\), and equal to one at both 0 and 1.

Write

\[
S_\rho=m_\zeta(\rho)+\sum_i\frac{\alpha_i}{2}
[m_{\chi_i}(\rho)+m_{\chi_i^\vee}(\rho)].
\]

Then \(\operatorname{ord}_\rho\mathscr P_M=MS_\rho\). At the central point the partner multiplicities agree, so the paired contribution is even; the zeta contribution is even by its own functional equation. Hence \(MS_{1/2}/2\) is an integer without any hypothesis of central nonvanishing.

This construction works for any positive integer M making all \(M\alpha_i/2\) integral. The displayed \(2d\) is a safe explicit choice, not a claimed minimal multiplier.

## 4. Entire descent, trace class and exact ordinary determinant

Let \(E(z)=\mathscr P_M(1/2+z)\). It is even and entire, so its even power series defines a unique entire \(\mathscr D_M\) by

\[
E(z)=\mathscr D_M(1/4-z^2),\qquad \mathscr D_M(0)=1.
\]

No square-root branch is used. The maximum modulus bound

\[
\max_{|v|\le R}|\mathscr D_M(v)|
\le \max_{|z|\le\sqrt{R+1/4}}|E(z)|
\]

proves that \(\mathscr D_M\) has order at most \(1/2\). Its zeros are \(v_\rho=\rho(1-\rho)\). A noncentral pair \(\{\rho,1-\rho\}\) gives one such zero of multiplicity \(MS_\rho\). The central point gives \(v=1/4\) with multiplicity \(MS_{1/2}/2\).

For any \(1/2<\theta<1\), Jensen's formula gives the counting estimate \(n_{\mathscr D}(R)=O(R^\theta)\). Dyadic summation yields \(\sum_a q_a/|a|<\infty\), where \(q_a\) is the multiplicity of a distinct zero a. The genus-zero Hadamard theorem then gives exactly

\[
\mathscr D_M(v)=\prod_a(1-v/a)^{q_a}.
\]

The order is below one, so no nonconstant exponential factor remains; the value at zero fixes the constant.

Define \(C_{\mathcal L,M}\) to be diagonal in an orthonormal basis, with entry \(a^{-1}\) repeated \(q_a\) times. Then

\[
\|C_{\mathcal L,M}\|_1=\sum_aq_a/|a|<\infty,
\qquad
\det(I-vC_{\mathcal L,M})=\mathscr D_M(v).
\]

In particular,

\[
\det(I-s(1-s)C_{\mathcal L,M})=\mathscr P_M(s).
\]

This is an explicit normal diagonal realization; it does not use the invalid implication from summable eigenvalues of an unspecified nonnormal operator to trace class.

## 5. Resolvent sign and central pole

Define the weighted completed logarithmic derivative

\[
\mathscr L_{\mathcal L}=
\frac{F_\zeta'}{F_\zeta}
+\sum_i\frac{\alpha_i}{2}
\left(\frac{F_{\chi_i}'}{F_{\chi_i}}+
\frac{F_{\chi_i^\vee}'}{F_{\chi_i^\vee}}\right).
\]

By integer differentiation, \(\mathscr L_{\mathcal L}=M^{-1}\mathscr P_M'/\mathscr P_M\). On compact subsets avoiding the determinant zeros, the reciprocal-eigenvalue series for the logarithmic derivative converges absolutely and uniformly; its tail denominators are uniformly bounded away from zero. Therefore the diagonal inverse is bounded and

\[
\mathscr L_{\mathcal L}(s)=\frac{2s-1}{M}
\operatorname{Tr}\!\left(C_{\mathcal L,M}
(I-s(1-s)C_{\mathcal L,M})^{-1}\right).
\]

The sign comes from two negatives: the v-logarithmic derivative of \(\det(I-vC)\) is \(-\operatorname{Tr}(C(I-vC)^{-1})\), and \(v'(s)=1-2s\).

At \(z=s-1/2\), a central block of multiplicity \(q=MS_{1/2}/2\) and eigenvalue 4 contributes \(q/z^2\) to the resolvent trace. Multiplication by \(2z/M\) gives \(S_{1/2}/z\), exactly the logarithmic pole. If there is no central zero both sides vanish at \(s=1/2\). No division by \(2s-1\) is used.

## 6. Exact source transform and all correction terms

Write \(\psi=\Gamma'/\Gamma\) and

\[
a_\zeta(s)=1/s+1/(s-1)-\tfrac12\log\pi+\tfrac12\psi(s/2),
\]
\[
a_\chi(s)=\tfrac12\log(q/\pi)+\tfrac12\psi((s+\kappa_\chi)/2).
\]

The partners have equal conductor and parity, so \(a_{\chi^\vee}=a_\chi\). Define

\[
A_{\mathcal L}=a_\zeta+\sum_i\alpha_i a_{\chi_i},
\quad
b_{\mathcal L}=1+\gamma_E+
\sum_i\frac{\alpha_i}{2}\left(
\frac{L'(1,\chi_i)}{L(1,\chi_i)}+
\frac{L'(1,\chi_i^\vee)}{L(1,\chi_i^\vee)}\right).
\]

The exact source Mellin formulas become

\[
\Phi_\chi(s)=-\frac{L'(s,\chi)/L(s,\chi)}{s(s-1)}
+\frac{L'(1,\chi)/L(1,\chi)}{s-1}
\]

for a nonprincipal character, and

\[
\Phi_\zeta(s)=-\frac{\zeta'(s)/\zeta(s)}{s(s-1)}
-\frac1{(s-1)^2}+\frac{1+\gamma_E}{s-1}.
\]

Conjugation gives \(G_{\chi^\vee}(y)=\overline{G_\chi(y)}\), so the source's real-part sum is the finite partner half-average even when s is complex. Direct integration of the absolute ramp majorant, with \(|\chi(n)|\le1\), gives absolute convergence for \(\Re s>1\); the linear and \(y\log y\) corrections also converge there. The generic PoleData uses the weaker common domain \(\Re s>2\).

For the actual \(G_{\mathcal L}\),

\[
\begin{aligned}
\Phi_{\mathcal L}(s)
&=\int_0^\infty G_{\mathcal L}(e^u)e^{-su}\,du\\
&=\frac{A_{\mathcal L}(s)-\mathscr L_{\mathcal L}(s)}{s(s-1)}
-\frac1{(s-1)^2}+\frac{b_{\mathcal L}}{s-1}.
\end{aligned}
\]

Substituting the resolvent identity proves the exact denominator-cleared operator trace representation. Near a completed zero the correction terms are analytic, and the residue is \(S_\rho/[\rho(1-\rho)]\), exactly as in poleData.lean:344–364. This also holds at the central point.

## 7. Exact criterion for omitting integer multiplication

An ordinary determinant \(D(v)=\det(I-vT)\), \(T\in\mathcal S_1\), can satisfy

\[
\mathscr L_{\mathcal L}(s)=\frac{d}{ds}\log D(s(1-s))
\]

if and only if

\[
S_\rho\in\mathbb Z_{\ge0}\ \ (\rho\ne1/2),\qquad
S_{1/2}/2\in\mathbb Z_{\ge0}.
\]

Necessity follows because determinant zero orders are integers; noncentral pullback preserves the order and central pullback doubles it. For sufficiency divide every zero order of \(\mathscr D_M\) by M. Under exactly these conditions the results are integers, the reciprocal-zero sum still converges, and the resulting diagonal trace-class determinant D satisfies \(D^M=\mathscr D_M\). Differentiation gives the claimed equality.

Equivalently, the normalized local germ \(\mathscr D_M^{1/M}\) at zero has a global entire ordinary determinant realization precisely under these conditions. All possible denominators divide \(2d\), so the least multiplier at the divisor level is the finite least common multiple of the denominators of \(S_\rho\) for noncentral zeros and of \(S_{1/2}/2\). Its value has not been inferred or computed from source positivity.

The actual inverse-closed source array gives a further exact simplification. The exceptional character is real and hence fixed by inversion, so the weights are inverse-invariant. Reindexing gives

\[
S_\rho=m_\zeta(\rho)+\sum_i\alpha_i m_{\chi_i}(\rho).
\]

Thus the source's half-average supplies no separate factor-of-two denominator at noncentral zeros. It still does not show the remaining rational-weight divisibility conditions. No claim is made that these conditions fail for an actual retained zero.

## 8. Positivity, and why trace scaling is not eigenvalue scaling

For \(\rho=\beta+it\) in the open strip,

\[
\rho(1-\rho)=\beta(1-\beta)+t^2+it(1-2\beta)
\]

has positive real part. Under GRH, \(c_\rho=(1/4+t^2)^{-1}\in(0,4]\). Conversely, if \(0\le C_{\mathcal L,M}\le4I\), every reciprocal is real positive. Then either \(\beta=1/2\) or \(t=0\). In the second case \(c_\rho\ge4\), with equality only at \(\beta=1/2\); hence the upper bound forces GRH. Positivity alone would permit a real off-center zero with eigenvalue greater than four. This is a logical qualification, not an assertion of such a zero.

The factor \(1/M\) multiplying the ordinary trace cannot be absorbed by replacing C with C/M. Under GRH the nonzero positive C has \(\operatorname{Tr}(C^2)>0\). The v coefficients in

\[
M^{-1}\operatorname{Tr}(C(I-vC)^{-1}),\qquad
\operatorname{Tr}((C/M)(I-vC/M)^{-1})
\]

are respectively \(\operatorname{Tr}(C^2)/M\) and \(\operatorname{Tr}(C^2)/M^2\). For \(M>1\) they differ. Rescaling eigenvalues moves determinant zeros; scaling the trace changes residue weights.

## Check status

The completed TeX proof was read in full after saving. This author's check passed the source primitivity restriction, source positive rational weights, root-number cancellation, endpoints 0 and 1, half-order at the branch point, no hidden exponential factor, trace-class summability, resolvent sign and domain, every Mellin correction, exact necessity and sufficiency of integrality, and the distinction between positivity and the bound by four. Classical completion/order theorems remain cited background; the new determinant proof and scalar algebra were independently re-proved. The companion event file records these distinct activities.
