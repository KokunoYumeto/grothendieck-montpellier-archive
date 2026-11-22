# AM-K022 — selected Schur jets in the actual permitted half-orbit

Author: GPT-6 Astra Pro, ALP_MACHINE /root/kummer_extension, 21 November 2026 UTC. Inherited reasoning effort is not separately exposed.

This result gives an explicit arithmetic level and a single permitted finite Schwartz vector detecting any prescribed nonzero homogeneous Schur polynomial. It applies to the ordinary product of Jacobians on the common E′ host, including the actual first even-rank edge of AM-DO-025. It does not identify the second iterated image or compute its class-mass content.

The permitted half-orbit basis is **carried DP59**, not a new representation theorem. The new conclusions are the numerical interpolation threshold, its product specialization, the factorial-exact highest-symbol detection, the norm-one individual-translate conclusion, and the equality of all finite determinantal ideals after passing from jets to the permitted section basis.

## 1. Fixed geometry and the permitted lattice

Work at 11 over an unramified complete DVR R large enough to contain the CM eigenvalues and the finite torsion and symmetric lifts in DP59. Normalize v₁₁(11)=1. Set
\[
 J=\operatorname{Jac}(y^2=x^7-1),\qquad
 L=L_{2\infty},\qquad s=s_q,
\]
where the actual q-normalized section is primitive at 11 by ALP-LIFT-08. Its reduced germ is σq by AM-K018. For an integer N≥1 write
\[
 X=J^N,\qquad \mathcal L=L^{\boxtimes N},\qquad
 s_X=s^{\boxtimes N}.
 \tag{J1}
\]
For the common host E′=Q(ζ₂₈), the positive Hom variety on an edge U(a)→U(b) is X=A^{ab}=J^{2ab}, with A=J², so N=2ab. Its holomorphic dimension is 6ab. The actual E′ eigenbasis differs from the two ordinary J bases by a matrix invertible at 11 (AM-DO-022). It may therefore be used for the integral tangent coordinates below.

Let
\[
 \delta^2=-7,\qquad
 \alpha=(1+2\delta)^e,\qquad M=29^e,\qquad
 \alpha\bar\alpha=M,\qquad \kappa=M^2.
 \tag{J2}
\]
The ideals (α) and (\bar α) are coprime. On each J factor take the exact DP59 orbit
\[
 s_{t'}=U_{t'}[M]^*s,\qquad t'\in J[\alpha^2],
\]
with the canonical odd-order symmetric theta lift. Choose one representative of J[α²]/J[α]. DP59(a) gives an integral basis of
\[
 W_M=[\alpha]^*H^0(J,L^M)
       \subset H^0(J,L^{M^2}),
 \qquad \operatorname{rank}_R W_M=M^3.
 \tag{J3}
\]
The orbit is smaller than the full level-M² section module.

On X take the tensor basis
\[
 \mathcal S_{\mathbf t'}
   =\boxtimes_{\ell=1}^{N}s_{t'_\ell},
 \qquad
 \mathcal W_{M,N}=W_M^{\otimes N}
   =[\alpha]^*H^0(X,\mathcal L^M).
 \tag{J4}
\]
Its rank is M^{3N}. Its actual rescaled Heisenberg parameters are
\[
 \mathbf x=M\mathbf t'\in X[\alpha]\subset X[M].
 \tag{J5}
\]
Thus all vectors used here belong to the allowed half-orbit. The construction never replaces it by the full level-M² theta group.

## 2. An explicit integral interpolation threshold

### Proposition J6

For every integer D≥0 and every M≥3D+2, restriction is surjective:
\[
 H^0(J,L^M)\longrightarrow
 H^0\!\left(J,\ L^M\otimes\mathcal O_J/I_0^{D+1}\right).
 \tag{J6}
\]
The analogous assertion holds on X=J^N with its product line, with the same bound M≥3D+2, independent of N.

**Known geometric input.** On an abelian variety over a field, the third power of an ample line is very ample. Milne, *Abelian Varieties*, I, §6, “Ample divisors,” printed p. 30 (PDF page 36 of AVc.pdf), states this in the chapter's arbitrary-characteristic setting. The higher-cohomology vanishing and integral H⁰ base change used below are the classical input already read and applied in DP59 §5, equations (TS11); its primary locator is Mumford (1966), §1(II), printed p. 289. No characteristic-zero vanishing theorem is substituted for the special-fibre assertion.

**Proof.** The special-fibre line L³ is very ample. Choose a section \(\bar h_0\) nonzero at zero, and sections \(\bar h_1,\bar h_2,\bar h_3\) vanishing there whose ratios \(\bar h_i/\bar h_0\) have linearly independent differentials. These choices exist because a very ample system has a surjective evaluation map and separates tangent vectors. They can be made over the residue field: these are surjective maps of finite-dimensional vector spaces, and an invertible minor can be chosen over that field.

Integral H⁰ base change lifts these sections to sections h_i of L³ over R. Normalize h₀(0)=1 in a rigidified fibre. Subtract h_i(0)h₀ from h_i for i>0. The ratios
\[
 t_i=h_i/h_0,\qquad 1\le i\le3,
\]
are integral formal parameters at zero because their cotangent determinant is a unit. Integral linear combinations make their first differentials any specified integral basis, including the dual of the actual CM tangent basis. Only unit inverses are used.

For each integer m≥2 there is a section of L^m whose value at zero is a unit. Here is the required special-fibre fact. The square L² is generated at every geometric point: choose a translate of a nonzero divisor of L so that neither it nor its opposite translate contains that point; the theorem of the square identifies their product line with L². The forbidden translation sets are two proper closed subsets. Their complement is nonempty over an algebraic closure. Evaluation surjectivity then descends to the residue field. L³ is generated because it is very ample. Every m≥2 is a sum of copies of 2 and 3, so products give the assertion for all m. Integral H⁰ base change lifts a section nonzero at zero to one with unit value over R.

Take m=M−3D≥2 and such a section η_m of L^m. The section η_mh₀^D trivializes L^M along the D-th infinitesimal neighbourhood of zero. An arbitrary target jet in this frame is
\[
 Q(t)=\sum_{|\beta|\le D}q_\beta t^\beta,\qquad q_\beta\in R.
\]
The global section
\[
 \eta_m\sum_{|\beta|\le D}
       q_\beta h_0^{D-|\beta|}
                h_1^{\beta_1}h_2^{\beta_2}h_3^{\beta_3}
 \tag{J7}
\]
has exactly this jet. This proves (J6).

For the product, tensor the single-factor restriction maps through order D. A monomial of total degree at most D in all 3N parameters has degree at most D in each three-variable block. Products of the single-factor interpolating sections therefore span every such monomial. After multiplication by the product local frame unit, they span arbitrary total D-jets. The image is contained in H⁰(X,ℒ^M) by the usual product-section map. This proves the product assertion without a dimension-dependent change of M. ∎

This is the numerical specialization r=3, b=2 of the integral homogenization in accepted DP56(a), not a new claim that an arbitrary ample line on an arbitrary proper variety has that threshold.

### Corollary J8. The same bound for the allowed half-orbit

For M=29^e≥3D+2,
\[
 \mathcal W_{M,N}\longrightarrow
 H^0\!\left(X,\mathcal L^{M^2}
                    \otimes\mathcal O_X/I_0^{D+1}\right)
 \quad\text{is surjective over }R.
 \tag{J8}
\]

**Proof.** The étale isogeny [α] has degree prime to 11, hence induces an integral formal isomorphism at zero. The rigidified equality [α]*ℒ^M≃ℒ^{M²} is part of the DP59 biextension construction. Its comparison in integral local frames is multiplication by an integral unit. Pulling (J6) back along this formal isomorphism proves (J8). The tensor orbit basis in (J4) is the carried DP59 basis on each factor, so the surjection is from exactly the permitted lattice. ∎

One explicit choice is
\[
 e(D)=\max\!\left(1,\left\lceil\log_{29}(3D+2)\right\rceil\right),
 \qquad M(D)=29^{e(D)},
 \qquad
 3D+2\le M(D)<29(3D+2).
 \tag{J9}
\]
In particular κ=M²<29²(3D+2)². The threshold is for **ordinary algebraic jets modulo I₀^{D+1}**, not for divided powers or derivative values normalized to one.

## 3. Highest-symbol detection and its exact factorial

Use any actual integral invariant tangent basis \(D_1,\ldots,D_{3N}\), and choose formal parameters t_i with \(D_it_j(0)=\delta_{ij}\). In the characteristic-zero logarithmic coordinates u_i dual to these derivations, \(t_i(u)=u_i+O(u^2)\).

For a section S of ℒ^{M²}, let F_S(u) be its actual Chern/source reduced germ in the common normalization of AM-K018. In an integral algebraic frame normalized at zero it has the form
\[
 F_S(u)=f_S(t(u))\,G_M(u),\qquad G_M(0)=1.
 \tag{J10}
\]
The gauge G_M is a characteristic-zero series; this argument does not require it to be an integral ordinary power series. The equality uses the fixed source gauge, not a section-dependent gauge.

Let
\[
 P(Z)=\sum_{|\beta|=D}c_\beta Z^\beta
          \in R[Z_1,\ldots,Z_{3N}]
\]
be nonzero and homogeneous, and define the normalized functional
\[
 \ell_{P,M}(S)=
       M^{-D}\,[P(\partial_u)F_S(u)]_{u=0}.
 \tag{J11}
\]

### Proposition J12

For every \(\beta\in\operatorname{supp}P\), the image ideal of ℓP,M on the permitted lattice contains \(c_\beta\beta!\):
\[
 c_\beta\beta!\in\ell_{P,M}(\mathcal W_{M,N}),
 \qquad
 \beta!=\prod_i\beta_i!,
 \qquad M\ge3D+2.
 \tag{J12}
\]
Consequently at least one individual allowed tuple \(\mathbf t'\) satisfies
\[
 \ell_{P,M}(\mathcal S_{\mathbf t'})\ne0,\qquad
 v_{11}\!\left(\ell_{P,M}(\mathcal S_{\mathbf t'})\right)
 \le \min_{\beta\in\operatorname{supp}P}
                     v_{11}(c_\beta\beta!).
 \tag{J13}
\]

**Proof.** By (J8), choose S with algebraic jet
\[
 f_S(t)\equiv M^D t^\beta\pmod{(t)^{D+1}}.
 \tag{J14}
\]
The scalar M^D is a unit at 11. There are no terms below degree D. Substituting \(t(u)=u+O(u^2)\) and multiplying by \(G_M(u)=1+O(u)\) therefore gives
\[
 F_S(u)\equiv M^D u^\beta\pmod{(u)^{D+1}}.
 \tag{J15}
\]
All higher coefficients of the possibly nonintegral gauge are irrelevant to this equality. The homogeneous differential polynomial kills every degree-D monomial except the one matching its exponent:
\[
 M^{-D}P(\partial_u)M^D u^\beta\big|_0
        =c_\beta\prod_i\beta_i!.
 \tag{J16}
\]
This proves (J12).

Expand S in the integral basis (J4):
\[
 S=\sum_{\mathbf t'}a_{\mathbf t'}\mathcal S_{\mathbf t'},
 \qquad a_{\mathbf t'}\in R.
 \tag{J17}
\]
If all basis values had valuation greater than \(v_{11}(c_\beta\beta!)\), their integral linear combination could not equal the nonzero value in (J16). Choose β minimizing that valuation. At least one basis value obeys (J13). The tuple and its canonical theta lifts are global algebraic objects by DP59(c). The conclusion does not require the coefficients in (J17) themselves to be global algebraic numbers. ∎

The factorial in (J16) is essential. Interpolating the ordinary coefficient of t^β to one produces derivative β!, not derivative one. An assertion of a unit derivative at arbitrary degree would divide by β! and would not be an integral interpolation statement.

The argument neither bounds nor uses the archimedean size of the coefficients in (J17). It uses them only in the local nonarchimedean valuation inequality to select one actual basis vector.

## 4. The exact selected Schur polynomial

On the even-rank edge U(a)→U(b), b>a, let \(\nu_\tau\) be the actual nonnegative source partitions identified in AM-DO-025:
\[
 \nu_{\tau,i}
   =(\lambda_{\mathrm{True},\tau})_i
                        +e_\tau-b/2,\qquad 1\le i\le a.
 \tag{J18}
\]
There are six holomorphic labels τ on the E′ host. Put ντ,a+1=0 and write \(Z_\tau=(Z_{\tau,i,j})\) as an a-by-b matrix. Take the standard primitive highest bideterminant
\[
 P_\nu(Z)=
 \prod_\tau\prod_{k=1}^{a}
       \det(Z_{\tau,\{1,\ldots,k\},\{1,\ldots,k\}})
                     ^{\nu_{\tau,k}-\nu_{\tau,k+1}}.
 \tag{J19}
\]
Its homogeneous degree is exactly
\[
 D=\sum_\tau|\nu_\tau|.
 \tag{J20}
\]
It is the highest vector in the actual Cauchy summand of AM-DO-025. This polynomial already lies in the selected Schur space; applying a rational Schur projector to it is unnecessary.

The diagonal monomial of Pν has coefficient exactly one:
\[
 \prod_{\tau,i}Z_{\tau,i,i}^{\nu_{\tau,i}}.
 \tag{J21}
\]
Indeed every determinant must contribute its diagonal term to produce a monomial containing no off-diagonal variable. The exponent of its i-th diagonal variable is
\(\sum_{k\ge i}(\nu_{\tau,k}-\nu_{\tau,k+1})=\nu_{\tau,i}\).
This also proves that Pν is primitive in the polynomial coefficient lattice. It does not assert that every alternative Weyl or normalized Fock lattice has that same basis; their comparison is separate.

Applying (J13) with this diagonal monomial gives a single permitted tuple with
\[
 a_{\nu,\mathbf t'}
 :=M^{-D}[P_\nu(\partial)F_{\mathcal S_{\mathbf t'}}]_0
 \ne0,
\qquad
 v_{11}(a_{\nu,\mathbf t'})
 \le
 \sum_{\tau,i}v_{11}(\nu_{\tau,i}!).
 \tag{J22}
\]
Equivalently,
\[
 v_{11}(a_{\nu,\mathbf t'})
 \le
 \frac{D-\sum_{\tau,i}s_{11}(\nu_{\tau,i})}{10}.
 \tag{J23}
\]
This is an explicit upper bound for **one selected kernel coefficient on the allowed family**. It is not a sharp derivative slope and not a bound for an arbitrary later theta-image vector.

It works for every actual ν₀ satisfying the source recurrence and gap conditions. No fixed-tail or single-row restriction is imposed. Therefore it supplies the nonzero selected first-edge kernel needed for the parent's class-supported compact extraction on U(N₀)→U(N₁).

## 5. The individual Schwartz vector has no translation-combination norm cost

Let \(\phi_{0,f}\) be the actual finite vacuum on X=A^{ab}, normalized to finite L² norm one as in AM-DO-022. For the tuple selected in (J22), use
\[
 \phi_{\mathbf x,f}=W_{\mathbf x}\phi_{0,f},
 \qquad \mathbf x=M\mathbf t'\in X[\alpha].
 \tag{J24}
\]
Every local Heisenberg translation is unitary for the fixed self-dual Schrödinger measure. The exact symmetric lift differs only by its fixed finite-order unit scalar. Hence
\[
                 \|\phi_{\mathbf x,f}\|_2^2=1.
 \tag{J25}
\]
In its permitted-orbit expansion this chosen vector has one coefficient equal to one and all others zero. Its coefficient maximum is one at every finite and complex embedding. Thus selecting this vector introduces no coefficient height or sum-of-orbit norm cost.

The level-normalized identity of ALP-LIFT-10 and AM-R-010 is
\[
 M^{-D}P(\partial_u)
 U_{\mathbf t'}^{M^2H}\bigl(\sigma_q^{\boxtimes N}(Mu)\bigr)\big|_0
 =
 P(\partial_v)
 U_{\mathbf x}^{H}\sigma_q^{\boxtimes N}(v)\big|_0,
 \tag{J26}
\]
with the specified canonical finite-order scalar retained. Accordingly AM-DO-026's actual kernel has the nonzero identity coefficient
\[
           \vartheta_{r_{P_\nu}\phi_{\mathbf x,f}}(1,1)
                  =C^{2ab}a_{\nu,\mathbf t'}.
 \tag{J27}
\]
Here \(C=\theta[0;0](0;\tau)c\), with the fixed algebraic scalar \(c\) of AM-R-006, is the one common period for the \(\sigma_q\) seed in AM-DO-022, §5. It is not a coefficient chosen for this tuple. The archimedean norm remains precisely the norm of the creation vector \(r_{P_\nu}\phi_{0,\infty}\); (J25) removes no Fock or period factor.

This statement supplies the finite vector and its norm. The source automorphic input, its stabilizer mass, its compact Schur-orthogonality factor, and its normalization are constructed separately in the parent's AM-R-012. None of those factors is set equal to one here.

## 6. Exact finite saturation reduction for every chosen polynomial family

The same interpolation gives a useful matrix statement that does not rely on a leading-symbol approximation.

Choose finitely many homogeneous polynomials P₁,…,P_q of degree at most D in a specified integral selected lattice, and include their individual source factors M^{-deg Pj}. Choose an ordinary algebraic monomial basis of the total D-jet module in the fixed integral theta frame. Let
\[
 J_D:R^{\,M^{3N}}\longrightarrow R^{\,\binom{3N+D}{3N}}
 \tag{J28}
\]
be the matrix of the actual permitted section basis's ordinary jets. Let B be the q-by-\(\binom{3N+D}{3N}\) matrix of the corresponding normalized Chern/source derivative functionals on these jets. Its entries lie in Frac(R); no integral reduced frame is assumed. Let A be the q-by-M^{3N} matrix of their actual allowed-tuple values. Then
\[
                       A=BJ_D.
 \tag{J29}
\]

### Proposition J30. No extra finite-translation determinantal loss

For M≥3D+2, the map J_D is split surjective over R. For every k≥1 the fractional ideals generated by the k-by-k minors satisfy
\[
                     I_k(A)=I_k(B).
 \tag{J30}
\]
Equivalently, after adding zero columns, A and B have the same nonzero Smith factors over the DVR.

**Proof.** Surjectivity is (J8). The jet module is finite free, so choose an R-linear right inverse C with J_DC=1. Thus B=AC. Cauchy–Binet applied to A=BJ_D gives \(I_k(A)\subset I_k(B)\), since J_D is integral. Applied to B=AC it gives the reverse inclusion, since C is integral. For fractional matrices first multiply by one common denominator; both k-minor ideals scale by its k-th power, so cancellation recovers (J30). Alternatively split the free domain of J_D as its kernel plus a copy of its target; in adapted integral bases J_D is \((1\ 0)\), and A is \((B\ 0)\). ∎

This equality is about the actual allowed half-orbit, not a larger arbitrary Schwartz space. It quantifies the absence of additional saturation loss in passing from the finite jet module to these section generators. The integral right inverse may have large archimedean entries, but no norm estimate for it is used in (J22) or (J25).

For the second automorphic lift, its class integral and the restriction to the already produced first image impose additional linear maps on this kernel data. Those maps can change the Smith factors, can cause cancellation, and can annihilate a vector. Proposition J30 does not assert that independently chosen jets at the identity can be prescribed at every class representative. The remaining second-stage problem is precisely the content of that **restricted class matrix**, with the source's actual selected coefficient lattice and compact contraction factors included.

The full differential-module obstruction AM-K019 is consistent with (J30). Here the degree-D jet module is finite, the level grows with D, and only the specified evaluated functionals are retained. No fixed-rank D-stable lattice, bounded saturation at all degrees, or iteration of a mod-11 coefficient congruence is asserted.

## 7. Sources and checks

- DP_MULT DP56(a), research/quantitative_theta_jet_levels_DP56.md, §§1–3: integral homogenization and its precise ordinary-jet convention. Carried; the explicit choice r=3,b=2 is justified in Proposition J6.
- DP_MULT DP59(a)–(c), research/theta_translate_span_DP59.md, §§3–8: actual rigidified pullback, exact permitted half-orbit, integral basis, unramified normalization, and global algebraicity. Carried, not rederived.
- Milne, J. S. (2008). *Abelian varieties* (Version 2.0), I, §6, subsection “Ample divisors,” printed p. 30, paragraph immediately before Example 6.5. https://www.jmilne.org/math/CourseNotes/AVc.pdf. The precise used fact is that the third power of every ample line on an abelian variety is very ample; the chapter is over an arbitrary base field.
- Mumford, D. (1966). On the equations defining abelian varieties. I. *Inventiones Mathematicae, 1*, 287–354. §1(II), p. 289, as already audited in DP59 for the cohomology/base-change input. https://pazuki.perso.math.cnrs.fr/index_fichiers/Mumford66.pdf.
- AM-DO-022 and AM-DO-025–026: actual E′ product polarization, unitary finite Heisenberg action, selected partitions, and all-polynomial kernel identity.
- AM-K018 and ALP-LIFT-08: exact source gauge on ordinary J products and primitive actual principal section at 11.
- ALP-LIFT-10 and AM-R-010: exact permitted parameter \(\mathbf x=M\mathbf t'\), retained symmetric lift scalar, and level-normalized derivative identity.

The result does not assume or bound an interpolating section's global coefficient height. The chosen individual allowed translate has coefficient vector a standard basis vector, so its finite Schwartz norm and translation-coefficient bound are exact.
