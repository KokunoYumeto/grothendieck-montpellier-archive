# F51 supplement: several integral weights and the actual collision

Author: /root/gct_statements, GPT-6 Astra Pro; inherited effort not exposed. Date: 21 November 2026 UTC. Parent proposed this extension of the radial separation proof; the author independently checked it in full. It is kept separate from the already reviewed base F51 report until its own fresh review.

## I1. Algebraic power traces with integral spectral weights

Fix b>1 and a finite sequence
\[
u_n=\sum_{j=1}^s c_j\alpha_j^n,\qquad
\alpha_j=b^{w_j}\zeta_j,\qquad
w_j\in\mathbf Z,\quad |\zeta_j|=1,
\tag{I1}
\]
with arbitrary complex coefficients c_j. Let f be one algebraic function over C(v), with primitive irreducible minimal relation P(v,Y) in C[v,Y]. Suppose allowed values of this same algebraic function satisfy
\[
f_{b^n}=u_n
\tag{I2}
\]
for every sufficiently large integer n, with arbitrary allowed sheets at those evaluations.

**Theorem I3.** Then the algebraic function is the Laurent polynomial
\[
f(v)=p(v):=\sum_j c_j v^{w_j}.
\tag{I3}
\]
Consequently the visible finite power sum u_n equals p(b^n) for all integers. For genuine matrix eigenvalues counted with positive multiplicities, every phase zeta_j is one and the coefficient of v^w is exactly the multiplicity of that spectral weight.

**Proof.** Write
\[
P(v,Y)=\sum_{i,k}a_{i,k}v^iY^k.
\]
Expanding P(b^n,u_n) gives a finite power sum. Every root has the form
\[
b^{\,i+w_{j_1}+\cdots+w_{j_k}}
  \zeta_{j_1}\cdots\zeta_{j_k}.
\]
Group terms by the integer
\[
r=i+w_{j_1}+\cdots+w_{j_k}.
\]
For fixed r their coefficient is a finite unit-circle power sum S_r(n). Roots from distinct r have distinct moduli b^r. Finite-power-sum uniqueness therefore implies S_r(n)=0 identically for each r, since the full sum vanishes for all sufficiently large n.

At n=0, all phases disappear. The number S_r(0) is exactly the coefficient of v^r in the Laurent polynomial P(v,p(v)). Hence
\[
P(v,p(v))=0\quad\hbox{in }\mathbf C[v,v^{-1}].
\]
The rational function p(v) is a root of the irreducible minimal polynomial over C(v). Thus that minimal polynomial has degree one and f=p. When some w_j are negative, this conclusion is taken over C(v); no incorrect assertion that P is a constant multiple of Y-p inside C[v,Y] is needed.

The prescribed evaluated values therefore give u_n=p(b^n) eventually, and finite-power-sum uniqueness extends the identity to all n. If the original coefficients are genuine positive multiplicities, any nontrivial phase produces a nonzero coefficient on a root b^w zeta that is absent from the Laurent side. Such a coefficient cannot cancel with another positive multiplicity. Thus every phase is one, with precisely the claimed multiplicities. QED.

For signed virtual coefficients, the theorem still controls the visible grouped power sum, but does not recover eigenvalues cancelled between degrees.

## I4. Full spectral retuning forces a rational characteristic polynomial

Let an invertible finite matrix family F lie over an algebraic extension of C(v). Suppose F_b is regular and invertible and every base eigenvalue has modulus b^w for some integer w, possibly varying among eigenvalues. Let m_w be the multiplicities. Assume full spectral retuning for regular evaluations of the same family:
\[
\operatorname{Spec}F_{b^n}=\operatorname{Spec}(F_b^n)
\tag{I4}
\]
for every sufficiently large n.

Theorem I3 applied to its trace gives
\[
\operatorname{Spec}F_b
 =\{b^w\text{ with multiplicity }m_w\}.
\tag{I5}
\]
For each characteristic-polynomial coefficient a(v), let P_a(v,Y) be its irreducible minimal relation. The spectral identity says that its evaluated values agree with the corresponding Laurent coefficient p_a(v) of
\[
\prod_w(T-v^w)^{m_w}.
\]
Thus P_a(b^n,p_a(b^n))=0 at infinitely many distinct parameters. The rational function P_a(v,p_a(v)) is identically zero. Since p_a is a rational root of the minimal polynomial, that coefficient a itself is p_a. Therefore
\[
\det(TI-F(v))=\prod_w(T-v^w)^{m_w}
\tag{I6}
\]
as an identity of algebraic functions.

This argument allows arbitrary sheets of the same coefficient relation. It needs neither a continuous branch nor a common fixed basis. Trace retuning alone gives (I3) and (I5); (I6) here uses the full spectral assumption.

## I7. Actual collision consequence

If such a family has a regular fixed-rank model at a point above v=1, (I6) gives
\[
\det(TI-F(1))=(T-1)^N.
\]
Thus its full centralizer has local center: the elementary cyclic-module argument of F48 identifies the center of a nilpotent centralizer with k[N_0], a truncated polynomial local algebra.

The actual rank-three collision algebra has center
\[
k\times k\times k[\epsilon]/(\epsilon^2),
\]
with three components. Hence it cannot be the full special Frobenius centralizer. This extends the F48 rational mixed-weight collision obstruction to algebraic matrix entries, arbitrary sheets, and any auxiliary rank, as long as all spectral weights at the base point are integral.

The constant-function single-weight result of base F51 remains stronger in a different direction: it needs only trace retuning, already excludes the actual nonsimple generic full centralizer, and needs no regularity at the collision.

## I8. Precise remaining scope

Under v=Q^{1/2}, the condition |alpha|=b^w with w integral is the usual integral spectral-weight condition. The inverse parameter convention changes the signs of the exponents and leaves the theorem unchanged.

This supplement does not classify unrestricted spectral magnitudes, nonintegral weights, infinite spectra or cancelled virtual eigenvalues. An algebraic Kummer family such as v=t^3 with eigencharacters 1,t,t^2,t^5 has spectral weights 0,1/3,2/3,5/3. It is therefore outside the present integral-weight statement and must not be described as a mixed object with integral Deligne weights. A separate contact-order comparison is needed for that broader algebraic case.

The proof is exact elementary algebra: finite power-sum uniqueness, Laurent polynomial expansion, and irreducibility. No new primary theorem, numerical experiment or formal proof-kernel verification is claimed. The actual collision algebra and the center lemma are previously fully proved F19/F48 inputs.

