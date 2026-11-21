# MAS-12 — no selfadjoint similarity for the actual character quotient

## Result

The metric obstruction of MAS-09 extends to every fixed unitary Hecke character in MAS-11, including the central-zero removal and the even exchange summand of the character/partner pair. It also extends to the internal even summand of a globally self-dual character.

**Conditional on the same full spectral-annihilator theorem as MAS-11, the resulting inverse-square operator is not boundedly similar to a selfadjoint operator. No GRH or simplicity hypothesis is needed for this conclusion.** Under GRH its retained nonzero eigenvalues are positive, while the actual operator remains nonselfadjoint and nonpositive. An equivalent Hilbert inner product cannot remove this obstruction.

The complete integration-ready proof is in work/paper_masullo_character_metric.tex. This note explains every part of the transfer, especially the finite central correction and the multiplicity-sensitive gap argument. The result does not assert the absence of noninvertible bounded intertwining maps.

## 1. Setup and the correct projection after central removal

Use MAS-11's fixed unitary character χ, center 1/2, half-width α>1/2 and weight parameter ν>1:

\[
H_\alpha=L^2(\mathbb R,w_\alpha(u)\,du),
\qquad w_\alpha(u)=e^{2\alpha|u|}(1+u^2)^{\nu/2}.
\]

The actual quotient Eχ=Hα/Vχ is isometric to Vχ⊥. This is the unitary radial gauge of the already centered theta quotient, as in MAS-11. Let m be the central zero multiplicity of the pole-cleared completed function 𝓕χ. The continuous dual central jets have Riesz representatives

\[
p_j(u)=\frac{u^j}{w_\alpha(u)},\qquad 0\le j<m.
\]

Write C₀=span{p₀,…,pₘ₋₁}, interpreted as zero if m=0. Let P₀ be the central Riesz spectral projection of the Green operator. MAS-11 proved that its transpose is identity on the full central jet block and zero on each noncentral jet block. Density of the complete jet span implies

\[
\operatorname{Ran}P_0^*=C_0,
\qquad
E_\chi^\circ=(I-P_0)E_\chi=\ker P_0
=C_0^\perp\cap E_\chi.
\tag{1}
\]

The finite-dimensional space in (1) is the range of P₀*, not its kernel. P₀ need not be orthogonal. If Π₀ is the orthogonal projection onto C₀, then

\[
Q=I-\Pi_0
\tag{2}
\]

is the orthogonal projection of Eχ onto Eχ°. Generally Q differs from I−P₀. This distinction determines the actual Riesz representatives after removing the central block.

Restrictions of noncentral jets to Eχ° remain finitely independent. Indeed, if a noncentral jet combination ℓ vanished on ker P₀, then ℓ=ℓ∘P₀; but P₀′ kills every such combination, so ℓ=0. Thus central removal cannot destroy a retained Jordan chain or turn a retained evaluation into zero.

The alternative half-width α=1/2 is allowed under the full boundary nonvanishing input described in MAS-11. The proof below depends only on α>0 once the full retained jets are known to exist continuously.

## 2. The actual Gram matrix

For a retained critical zero ρ=1/2+iγ with γ real and nonzero, define

\[
v_\gamma(u)=\frac{e^{-i\gamma u}}{w_\alpha(u)},
\qquad q_\gamma=Qv_\gamma.
\]

With the conjugate-linear-first inner product, vγ represents the evaluation ℓγ(h)=∫h(u)e^{iγu}du. It belongs to Vχ⊥ because that evaluation annihilates Vχ. Its restriction to Eχ° is represented by qγ. The complete jet multiplier of Rχ is −1/z², so

\[
R_\chi^*q_\gamma=\gamma^{-2}q_\gamma.
\tag{3}
\]

Set

\[
K_\alpha(t)=\int_{\mathbb R}\frac{e^{itu}}{w_\alpha(u)}\,du.
\]

Kα is real, even and continuous, tends to zero as |t|→∞, and Kα(0)>0. Every polynomial times wα⁻¹ is integrable. Therefore every coordinate of Π₀vγ in a fixed orthonormal basis of C₀ tends to zero by Fourier decay, yielding

\[
\|\Pi_0v_\gamma\|\longrightarrow0
\qquad(|\gamma|\to\infty).
\tag{4}
\]

This can also be checked by integration by parts: a polynomial times wα⁻¹ is continuous, piecewise continuously differentiable, with integrable weak derivative and vanishing limits at infinity. Its Fourier transform is consequently O(1/|γ|).

The exact post-removal Gram identities are

\[
\langle q_\gamma,q_\delta\rangle
=K_\alpha(\gamma-\delta)
-\langle\Pi_0v_\gamma,\Pi_0v_\delta\rangle,
\tag{5}
\]

\[
\|q_\gamma\|^2=K_\alpha(0)-\|\Pi_0v_\gamma\|^2.
\tag{6}
\]

Before central removal, Kα(t) is strictly positive for every real t. For an explicit verification, put a=2α and b=ν/2 and combine the Gamma mixture of (1+u²)⁻ᵇ with the Cauchy Fourier formula for exp(−a|u|). The Gaussian integral gives

\[
K_\alpha(t)=\frac{a}{\pi\Gamma(b)}
\int_0^\infty r^{b-1}e^{-r}\sqrt{\frac\pi r}
\int_{\mathbb R}\frac{e^{-(t+y)^2/(4r)}}{a^2+y^2}\,dy\,dr>0.
\]

The formula is the proof of MAS-09 with its exponential parameter changed from 1 to 2α. Its integral rearrangements are justified by the same absolute integrability; here b>1/2 in particular. After a nonzero central removal, however, the correction term in (5) must be retained. Strict positivity for every individual pair is not asserted after projection. The contradiction below uses large nearby ordinates, where that finite correction vanishes.

## 3. Gamma growth supplies the needed density consequence

Let

\[
f_\chi(z)=\frac{\mathcal F_\chi(1/2+z)}{z^m},
\qquad a_\chi=f_\chi(0),
\qquad
\mathcal H_\chi(z)=
\frac{f_\chi(z)f_{\chi^{-1}}(z)}{a_\chi a_{\chi^{-1}}}.
\]

MAS-11 proved the absolutely locally uniformly convergent identity

\[
\mathcal H_\chi(z)
=\prod_{\rho\ne1/2}(1-z^2/z_\rho^2)^{N_\rho},
\qquad z_\rho=\rho-1/2,
\tag{7}
\]

where ρ ranges over distinct completed zeros. Conjugation under the specified completion gives, for real x,

\[
\mathcal H_\chi(x)=\frac{|f_\chi(x)|^2}{|a_\chi|^2}.
\]

This is positive for x>1/2, since the completed zeros lie in the closed critical strip.

For n_F=[F:ℚ], Stirling's formula in [DLMF 5.11.1](https://dlmf.nist.gov/5.11.E1) yields

\[
\log\mathcal H_\chi(x)=n_F x\log x+O_\chi(x)
\qquad(x\to+\infty).
\tag{8}
\]

Each real-place gamma factor contributes (x/2)log x+Oχ(x) to log|Λχ(1/2+x)|, and each complex-place factor contributes x log x+Oχ(x). Since n_F=r₁+2r₂, their sum is (n_F/2)x log x+Oχ(x); the squared modulus doubles it. The conductor contributes a linear term. The finite Euler product tends to 1 along the positive real axis by dominated convergence in its absolutely convergent Dirichlet series. Pole clearing and central removal change the logarithm by Oχ(log x). This proves (8) directly from the normalization already checked in MAS-11.

No separate Hecke zero asymptotic is required. In particular, the argument does not mistake a zero count with unbounded multiplicities for a count of distinct ordinates.

Suppose now that every retained zero is simple and every centered zero lies on the real or imaginary axis. The real-axis zeros are finite: they lie in the compact interval [−1/2,1/2] and the entire completion is not identically zero. Their factors in (7) contribute Oχ(log x) to the logarithm of the absolute value. Thus

\[
\log\mathcal H_\chi(x)=O_\chi(\log x)
+\sum_\gamma\log(1+x^2/\gamma^2),
\tag{9}
\]

where iγ runs over the retained imaginary-axis zeros.

Let N_im(T)=#{γ:0<|γ|≤T}. If N_im(T)=O(T), discreteness around the removed central point permits a constant C with N_im(t)≤Ct for every t>0. Using

\[
\log(1+x^2/\gamma^2)
=\int_{|\gamma|}^{\infty}\frac{2x^2}{t(t^2+x^2)}\,dt
\]

and Tonelli gives

\[
\sum_\gamma\log(1+x^2/\gamma^2)
\le2Cx^2\int_0^\infty\frac{dt}{t^2+x^2}=\pi Cx.
\]

This contradicts (8). Therefore N_im(T) is not O(T). In the present simple-zero case, an eventual positive lower gap on each signed half-line would imply N_im(T)=O(T). Hence there exist distinct same-sign ordinates γj,δj such that both absolute values tend to infinity and |γj−δj|→0. Their squares are distinct. Discreteness prevents infinitely shrinking gaps from remaining in a fixed compact set.

## 4. The three exhaustive cases

### A nonreal eigenvalue

If some centered zero zρ has nonzero real and imaginary parts, the eigenvalue −zρ⁻² is nonreal. This excludes similarity to a selfadjoint operator, since similarity preserves spectrum.

### A retained multiple zero

Otherwise all centered zeros lie on the real or imaginary axis, so the eigenvalues are real. If any noncentral zero has Nρ≥2, the independent first two restricted jets satisfy

\[
R_\chi'\ell_{\rho,0}=F(z_\rho)\ell_{\rho,0},
\quad
R_\chi'\ell_{\rho,1}=F(z_\rho)\ell_{\rho,1}
+F'(z_\rho)\ell_{\rho,0},
\]

with F(z)=−z⁻² and F′(z)=2z⁻³≠0. Thus a genuine Jordan chain survives central removal. The Riesz identification gives a Jordan chain for the adjoint. Selfadjoint operators have no nontrivial chain at a real eigenvalue: if (A−λ)y=x and (A−λ)x=0, then

\[
\|x\|^2=\langle x,(A-\lambda)y\rangle
=\langle(A-\lambda)x,y\rangle=0.
\]

Bounded similarity preserves this obstruction. This step handles all multiplicities before any gap argument is invoked.

### Simple zeros on the axes

The remaining case is exactly the setting of §3. For the nearby imaginary-axis pairs, equations (4)–(6) give

\[
\|q_{\gamma_j}\|,\|q_{\delta_j}\|\to\sqrt{K_\alpha(0)},
\qquad
\langle q_{\gamma_j},q_{\delta_j}\rangle\to K_\alpha(0).
\]

Their normalized vectors aj,bj satisfy ‖aj−bj‖→0 and are eigenvectors of Rχ* for distinct real eigenvalues. If Rχ*=SAS⁻¹ with A selfadjoint and S boundedly invertible, the two vectors S⁻¹aj and S⁻¹bj are orthogonal and each has norm at least 1/‖S‖. Therefore

\[
\|S^{-1}a_j-S^{-1}b_j\|\ge\sqrt2/\|S\|,
\]

while boundedness of S⁻¹ makes the left side tend to zero. This contradiction excludes similarity for the adjoint and hence, by taking adjoints, for Rχ itself.

These cases exhaust every possible zero configuration. Real noncentral exceptional zeros, including a possible real zero away from 1/2, cause no omission: if simple they are finitely many and contribute only the O(log x) term in (9); if multiple the Jordan case applies. Thus GRH is not an input to the no-similarity theorem.

## 5. The paired even space and the self-dual internal even space

For the labeled χ,χ⁻¹ pair, MAS-11 gives the unitary graph map

\[
U:E_\chi^\circ\longrightarrow E_{\chi,\chi^{-1},+}^\circ,
\qquad Ux=(x,Jx)/\sqrt2.
\]

It intertwines the actual operators and their adjoints. Consequently their Gram matrices and the no-similarity conclusion transfer without any change of Hilbert metric. Labeled copies remain necessary if the compact restrictions coincide but the global characters differ.

If χ=χ⁻¹ globally, internal reflection is available. The even central dual space is C₀,+=span{u^{2j}/wα:2j<m}. Let Q+ be the orthogonal projection from the original even quotient onto its central complement. For a positive imaginary ordinate define

\[
c_\gamma(u)=\frac{\cos(\gamma u)}{w_\alpha(u)},
\qquad q_{\gamma,+}=Q_+c_\gamma.
\]

These are adjoint eigenvectors with eigenvalue γ⁻². Before the finite correction,

\[
\langle c_\gamma,c_\delta\rangle
=\tfrac12\bigl(K_\alpha(\gamma-\delta)
+K_\alpha(\gamma+\delta)\bigr).
\]

The correction to each vector tends to zero at large ordinates. In the simple-axis case, self-duality makes the imaginary zeros symmetric, so a positive lower gap among positive ordinates would make the full count O(T), which §3 excluded. For nearby positive pairs tending to infinity, the corrected squared norms and inner products all tend to Kα(0)/2. Normalized vectors coalesce and yield the same similarity contradiction.

The other two cases also persist internally. Each noncentral pair {z,−z} retains the full multiplicity of its eigenvalue, including a nonreal one. At a multiple zero, the even jet pair

\[
\ell_{z,0}+\ell_{-z,0},
\qquad \ell_{z,1}-\ell_{-z,1}
\]

has the nonzero Jordan entry F′(z), since F is even and F′ is odd. Central removal preserves the independence of these jets. This completes the internal-even proof.

## 6. Positivity and comparison with the Bessel realization

Under GRH, every retained eigenvalue −zρ⁻²=γρ⁻² is positive. The no-similarity result nevertheless rules out actual selfadjointness and positivity. If an equivalent Hilbert inner product made the operator selfadjoint, its bounded positive invertible metric operator would have a bounded invertible square root, giving the forbidden similarity. Thus the obstruction applies to every equivalent Hilbert norm.

MAS-11's ordinary determinant identity survives unchanged. A positive diagonal realization or DET-15's positively weighted Bessel projection construction can have the designated determinant without being related to this weighted theta-quotient operator by a boundedly invertible intertwiner. This statement does not rule out noninvertible bounded intertwiners or a different nonequivalent completion.

The positivity comparison uses the relevant zero-location result: the stipulated theorem in the zeta/Dirichlet setting, and GRH as an additional assumption for a general unitary Hecke character. The main MAS-12 no-similarity theorem itself requires no such zero-location assumption.

## 7. Sources and checks

The draft dependence is exactly MAS-11's full spectral-annihilator theorem, Masullo Theorem 10.2.2.1, printed page 446, together with the same actual weighted quotient and Hilbert-dual density. The central Riesz projection, exact full jet multiplier, labeled exchange parity, self-dual internal parity and normalized Hadamard product are the results proved in MAS-11, not new source assumptions.

The only additional external formula used is Stirling's logarithmic gamma expansion, [NIST DLMF §5.11, equation (5.11.1)](https://dlmf.nist.gov/5.11). It was opened and checked in this run; the fixed shifted positive-real arguments stay in its allowed sector. No unverified Hecke zero-count asymptotic is imported. Fourier decay and the actual reciprocal-weight correlation follow from the explicit functions above and the MAS-09 argument.

The complete author proof was reread after correcting the final comparison to “boundedly invertible intertwiner” and making the general Hecke GRH scope explicit. The parent independently read the full proof and reported a pass on the central range, Fourier correction, Stirling coefficient, simple-zero gap argument, axis/Jordan cases and internal even jets. The parent records that independent event separately. No master deliverable was edited by this author.
