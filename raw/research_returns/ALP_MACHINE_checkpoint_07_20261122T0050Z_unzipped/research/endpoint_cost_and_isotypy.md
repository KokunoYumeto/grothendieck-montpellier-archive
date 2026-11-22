# ALP_MACHINE root contribution: actual comparison and endpoint normalization

Author: GPT-6 Astra Pro, `/root`; reasoning effort is not exposed by the runtime. Run: ALP_MACHINE, 21 November 2026. This is an application of accepted DP_MULT results and directly read source definitions. It is not a Lean execution or a reproof of Alpöge's theorem.

## AM-R-001. Comparison of two rebuilt families

Let \(\mathscr D\) and \(\mathscr D'\) be two fully specified families of lengths \(M\) and \(M'<M\). Fix corresponding family members, but do not suppose their endpoints or coefficient fields are equal. Use DP44's scalar definitions on each family, with primes denoting the second family. Thus

\[
 Q_M=\sum_{j=1}^{M}(g_j-e_j)-T_\tau-MH+K_u,
\qquad
 Q'_{M'}=\sum_{j=1}^{M'}(g'_j-e'_j)-T'_\tau-M'H'+K'_{u'}.
\]

Then the exact difference is

\[
\begin{split}
Q'_{M'}-Q_M={}&-\sum_{j=M'+1}^{M}(g_j-e_j-H)\\
&+\sum_{j=1}^{M'}\bigl((g'_j-g_j)-(e'_j-e_j)\bigr)
-M'(H'-H)\\
&-(T'_\tau-T_\tau)+(K'_{u'}-K_u).
\end{split}\tag{R1}
\]

If the compared quantity is \(Q-B\), add \(B_M-B'_{M'}\) to the right side. No sign of \(H\), or equality between the two period normalizations, is assumed.

**Proof.** Subtract the two displayed defining expressions and split the unprimed sum into retained and deleted indices. The unprimed main-term difference is \((M-M')H-M'(H'-H)\). Combining its first term with the deleted sum gives (R1). This short proof gives the changed-family form that DP44 did not write as an equation; the frozen-family formula DP44.3 is carried, not rederived as a new finding.

**Application and limitation.** A proposed calculation of a lift saving must specify every term of (R1). The supplied curve, prime, formal-group slopes and generic rank records do not supply those numbers. `SizeData₂.gain`, `SizeData₂.E`, `SizeData₂.tau`, the weights and level are additional source data tied to a family through the global links. `LinkG_at` includes a coarse upper bound as well as the ramp inequality; that ramp inequality is only a lower certificate and cannot be reversed into a sharp upper bound on true gains. Thus the local slope upper obstructions in DP42/DP51 do not supply the missing upper bound in (R1). This is a scope statement about the available implications, not a theorem that no shorter family exists. In particular, even a negative difference alone is not equivalent to failure of the full global theorem's inequalities.

**Locators.** DP_MULT DP44(d), equations DP44.1–DP44.4; original source `Formalism/LocalRingCardinality/DataParams₂.lean`, `SizeData₂` lines 76–181, `sz` 203–206, `gainD` 212–213, `Ga` 220, `Ee` 222, `logOm` 224, `MAIN` 232–234; `Formalism/SharpRestriction/GlobalTheoremInputs.lean`, `LinkDIV_at` 77–89 and `LinkG_at` 122–136. Source bytes were recovered from the intake-pinned mirror and matched to the intake's original-author archive SHA256 values.

## AM-R-002. The arithmetic and archimedean cost of an endpoint detector

This statement makes quantitative the distinction retained in DP55 between a nonzero complex pairing and an integral, controlled detector. It is an elementary application of the exact source pairing, not a claim that ideal content or dual norms are new general concepts.

Let \(K\) be a number field, \(\mathcal R\) a full projective \(\mathcal O_K\)-lattice in the row coefficient space \(W\), and \(B:V\times W\to K\) the algebraic endpoint pairing, including its stabilizer and coefficient normalization. Let \(0\ne f\in V(K)\), and suppose the functional \(\ell_f=B(f,-)\) is nonzero. Define its nonzero fractional content ideal

\[
 I_f=\ell_f(\mathcal R)\subset K.\tag{R2}
\]

At a finite place \(\mathfrak p\), write \(I_f\mathcal O_{K,\mathfrak p}=\pi_{\mathfrak p}^{s_{\mathfrak p}}\mathcal O_{K,\mathfrak p}\), with the valuation normalized by \(v_{\mathfrak p}(\pi_{\mathfrak p})=1\). Then:

1. There is a detector \(z\in\mathcal R_{\mathfrak p}\) with \(B(f,z)=1\) if and only if \(s_{\mathfrak p}\le0\).
2. The least integer \(d\ge0\) for which such a detector exists in \(\pi_{\mathfrak p}^{-d}\mathcal R_{\mathfrak p}\) is
   \[d_{\min}(f,\mathfrak p)=\max\{0,s_{\mathfrak p}\}.\tag{R3}\]
3. If \(r_1,\ldots,r_N\) is a local lattice basis and \(b_i=B(f,r_i)\), then
   \[s_{\mathfrak p}=\min_i v_{\mathfrak p}(b_i).\tag{R4}\]

For a fixed embedding \(\sigma:K\hookrightarrow\mathbb C\), put a positive Hermitian norm on \(W_\sigma\), and let \(\beta_\sigma(f)=\|\ell_{f,\sigma}\|_*\). Then

\[
 \inf_{B_\sigma(f,z)=1}\|z\|_\sigma=\beta_\sigma(f)^{-1},\tag{R5}
\]

and the infimum is attained. If the norm on rows is transported through DP55's representing map \(J\), then \(\beta_\sigma(f)=\|f\|_{\rm cl,\sigma}\), provided that transported form is a norm; alternatively apply (R5) to the quotient by \(\ker J\).

For \(a\in K^\times\),

\[
 I_{af}=aI_f,\qquad \beta_\sigma(af)=|\sigma(a)|\beta_\sigma(f).\tag{R6}
\]

Consequently the signed normalization balance

\[
 \mathcal B(f)=\frac1{[K:\mathbb Q]}
 \left(\sum_{\mathfrak p}s_{\mathfrak p}\log N\mathfrak p
       -\sum_{\sigma:K\hookrightarrow\mathbb C}\log\beta_\sigma(f)\right)\tag{R7}
\]

is invariant under \(f\mapsto af\). All complex embeddings are counted; this convention automatically counts a conjugate pair twice. It is the negative Arakelov degree of the quotient image line \(I_f\), equipped with the quotient norm \(\|1\|_\sigma=\beta_\sigma(f)^{-1}\).

**Full proof.** Since \(\mathcal R\) is a finite lattice, its image under a nonzero \(K\)-linear map is a nonzero finitely generated \(\mathcal O_K\)-submodule of \(K\), hence a fractional ideal. Localization commutes with its image. The image of \(\pi^{-d}\mathcal R_{\mathfrak p}\) is exactly \(\pi^{s_{\mathfrak p}-d}\mathcal O_{K,\mathfrak p}\); it contains 1 exactly when \(d\ge s_{\mathfrak p}\). This proves (R3), including negative \(s_{\mathfrak p}\), and assertion 1. A basis generates the image ideal, and a finitely generated ideal over a DVR has valuation equal to the least valuation of its generators, proving (R4).

By the finite-dimensional Riesz representation theorem, there is a unique nonzero vector \(y\in W_\sigma\) such that \(\ell_{f,\sigma}(z)=\langle y,z\rangle\), in the convention conjugate-linear in the first argument. Its norm is \(\beta_\sigma(f)\). Cauchy–Schwarz gives \(1\le\beta_\sigma(f)\|z\|\) for every detector. The vector \(z=y/\|y\|^2\) is a detector and attains equality. This proves (R5). DP55's identity \(B(f,z)=\langle Jz,f\rangle_{\rm cl}\), with \(J\) conjugate-linear and onto, gives the stated transported-norm specialization by the same argument; if necessary take its injective quotient first.

Bilinearity gives the ideal equality in (R6), and the definition of operator norm gives the norm equality. The change in the numerator of (R7) is
\[\sum_{\mathfrak p}v_{\mathfrak p}(a)\log N\mathfrak p-\sum_\sigma\log|\sigma(a)|=0\]
by the product formula. Finally, relative to the lattice \(I_f\), the rational section 1 has divisor coefficient \(-s_{\mathfrak p}\); its quotient norm is \(\beta_\sigma(f)^{-1}\). Substituting these two facts into the definition of arithmetic degree gives \(-\mathcal B(f)\). This proves every assertion.

### The exact source coefficient matrix

DP55's source form is the bilinear normalized Fock form

\[
 B_\lambda(x,y)=D_\lambda^{-1}\sum_\alpha x_\alpha y_\alpha\alpha!,
\quad
 D_\lambda=\prod_\tau\sum_\alpha (\operatorname{ext}_{\lambda_\tau})_\alpha^2\alpha! .\tag{R8}
\]

At class \(c\) it is multiplied by \(1/a_c\), where \(a_c\) is the actual finite stabilizer order. Choose bases of the actual invariant coefficient lattices, not a larger unconstrained polynomial module. Write \(G_c\) for their raw Fock matrix and \(f_c\) for the point coordinates. When the row lattice is expressed as the direct sum of these invariant class lattices, (R4) becomes the explicit formula

\[
 s_{\mathfrak p}
 =\min_{c,b}v_{\mathfrak p}\left(
       \frac{(f_c^{\mathsf T}G_c)_b}{a_cD_\lambda}\right).\tag{R9}
\]

If integral coordinates are tied together by an additional lattice inclusion \(C\), replace the row of all displayed coefficients by its product with \(C\). Formula (R9) then applies to generators of that actual image lattice. Thus no arbitrary basis is silently assumed unimodular.

**Proof of the application.** The source period is the finite sum of the classwise forms (R8), weighted by \(a_c^{-1}\). Evaluating it on a basis row supported on one class gives exactly the coefficient inside (R9). Formula (R4) then applies. If rows are restricted to an integral submodule, evaluating on its generators multiplies by its inclusion matrix. This proves the corrected formula for that case too.

**Locators.** DP_MULT DP55, (ED3), (ED7), (ED11), and its explicit statement that the arbitrary detecting row has no proved denominator or norm bound. Directly read original-source declarations: `Formalism/LocalToGlobal/Columns/CoefModB.lean`, `fockB` line 18, `extNormB` 55–56, `pairB` 58–59, `pairBK` 61–62, `PairBDual` 113–119; `Columns/Record.lean`, `perCl` 315–329 and `periodC` 1568–1571; `Columns/TiedPer.lean`, `per_jMCL_eq` 243–244 and `per_jMC_onto` 250–252. Perfectness over the field does not assert that the two chosen integral lattices are mutually dual.

**Consequence for Q3e.** A unit-valued complex period cannot be inserted at zero arithmetic cost merely by rescaling. For a specified algebraic terminal lift vector, the endpoint denominator problem is exactly the content computation (R9), and the archimedean problem is the dual norm (R5). These are computable once the actual kernel/image and lattice matrices are given. This result does not construct that terminal lift vector or identify its lattice, and therefore does not decide the sign in (R1).

## AM-R-003. Powers of the genus-three Jacobian do not repair an elliptic Serre-tensor requirement

Let \(J/\overline{\mathbb Q}\) be the Jacobian of \(y^2=x^7-1\), with its accepted CM type \(\Phi=\{1,2,3\}\) on \(E=\mathbb Q(\zeta_7)\). For every \(N>0\), no nonzero elliptic-power abelian variety is isogenous to an abelian subvariety or quotient of \(J^N\). In particular there is no nonzero isogeny, nor a nonzero homomorphism, in either direction between \(J^N\) and \(C^d\), for any elliptic curve \(C\) and \(d>0\).

This remains true after a finite extension of the base field, after twisting the displayed CM action by automorphisms, and for the geometric product \(J^P\times\bar J^Q\) used by DP65, where \(\bar J\) is the same abelian variety with conjugate \(E\)-action. Consequently an actual Serre tensor of an elliptic curve by a finite projective module cannot become such a geometric power of \(J\) through a field enlargement or an isogeny. This excludes only attempts to retain the source's elliptic `IsTen` requirement. It is not a no-go theorem for a newly defined mixed-type theta correspondence.

**Proof.** The only proper CM subfield of the cyclic degree-six field \(E\) is its imaginary quadratic field \(K=\mathbb Q(\sqrt{-7})\). The two induced types from \(K\) are \(\{1,2,4\}\) and \(\{3,5,6\}\). The actual type \(\{1,2,3\}\) is neither, hence primitive. Milne, *Complex Multiplication* (2020), Proposition 3.13, identifies primitive CM types with simple complex CM abelian varieties up to isogeny. Thus \(J\) is geometrically simple of dimension three.

A nonzero homomorphism \(J\to C\) would have an abelian image of positive dimension, hence image \(C\). Its connected kernel would have dimension two, contradicting simplicity. A nonzero map \(C\to J\) would give a positive-dimensional abelian subvariety of dimension at most one, again a contradiction. Every homomorphism between products is a matrix of homomorphisms between factors, so all maps \(J^N\leftrightarrow C^d\) vanish. By Poincare complete reducibility, a nonzero elliptic isogeny factor of a subvariety or quotient of \(J^N\) would give such a nonzero map, which is impossible.

The argument is over \(\overline{\mathbb Q}\), so a finite base extension changes nothing. Twisting a named endomorphism action does not change the underlying variety. For a finite projective module \(M\) over an order acting on an elliptic curve, \(M\otimes C\) is, after clearing denominators in a module basis, isogenous to an elliptic power. Hence it cannot be isogenous to a nonzero variety in the \(J\)-isotypic category. This proves the statement.

**Locators and scope.** The CM type and the earlier type-package obstruction are carried DP22, DP25, DP49, DP52(d), DP57. The exact old `IsTen` input is `Development/AbelianVarietyTheory/Definitions/CMLattices/IsDiffOf.lean`, lines 73–77, as identified in DP57 §7. The new assertion applies the simple-isogeny-factor invariant to arbitrary powers and field enlargements; it does not reprove the accepted local derivative results. In motives it says that the weight-one simple constituent \(h^1(J)\) cannot be replaced by an elliptic \(h^1\) constituent. Exterior and tensor powers of motives are a different operation; no vanishing of all higher-weight correspondences is claimed.
