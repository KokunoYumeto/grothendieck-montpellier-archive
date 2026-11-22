# AM-K021 — the cubic relative period and the exact CM-height boundary

**Status.** New proved reductions and scoped obstructions for question 3. The stipulated Alpöge theorem, its archive, and the earlier accepted DP statements retain their accepted status. This report does not establish the relative arithmetic window, a new RH theorem, or a new automorphic cost bound.

**Dependencies.** AM-K001–AM-K005 in kummer_extension.md and AM-K007–AM-K011 in kummer_cubic_host.md supply the Artin identity, conductor table, completed functional equation, elliptic Hom realization, finite ray character, norm-one splitting twist, and explicit CM supply tower. They are used with those statements' existing proofs and scope. The new result strengthens the earlier observation that coherent splitting phases telescope: even a genuine cubic twist of the actual polarized CM variety leaves the stable geometric letter degrees unchanged. A separate finite-character argument excludes the cubic standard Artin character from every finite linear combination of CM-type height classes.

## 1. The exact source scalar is geometric and quadratic

All paths in this section are relative to work/research/alpoge_source. These are inspected source interfaces, not a claim to have compiled or independently reconstructed their full upstream proofs.

| Source locator | Exact role |
|---|---|
| Formalism/LocalRingCardinality/DataParams₂.lean, lines 65–71 | chiK is the quadratic Dirichlet character modulo D.host.d; dlogL is the real part of its logarithmic derivative. |
| The same file, lines 126–127 | SizeData₂.logDerivativeAtOne is constrained by logDerivative_at_one_eq to equal dlogL D 1. It is not a freely chosen real parameter. |
| The same file, line 224 | logOm is Euler's constant plus log(π / host.v) minus that logarithmic derivative. |
| The same file, lines 232–234 | MAIN contains the term −R.m · aT(t) · logOm for every host type t. |
| Formalism/LocalToGlobal/ProjectiveLattices/RosatiLatticeNorms/LamObj.lean, definitions IsVecLine and LamObjGood | A letter line must carry the actual integral tangent lattice and the norm induced by the polarized complex uniformization. |
| Formalism/LocalToGlobal/ProjectiveLattices/RosatiLatticeNorms/LamPtClauses.lean, lines 53–56 | LamDegSt requires every actual letter to have normalized degree logOm / 2. |
| Formalism/LocalToGlobal/ProjectiveLattices/RosatiLatticeNorms/CmFrameOfEq.lean, lines 45–58 and 78–115 | The degree identity is transported to the frame letters and is a hypothesis of the construction. |
| Formalism/LocalToGlobal/CMDeterminantIdeals/StatementS.lean, lines 63–73 | Step5 consumes those exact letter degrees in its determinant estimate. |

In particular the actual source chain has two separate equalities:
\[
 \log\Omega=
 \gamma+\log(\pi/v)
 -\frac{L'(1,\chi_K)}{L(1,\chi_K)},
 \qquad
 \widehat{\deg}_{\rm norm}(\ell)=\frac12\log\Omega.
 \tag{R1}
\]
The first equality is a prescribed auxiliary quadratic analytic constant. The second is a fact about actual integral metrized lines. Renaming a splitting character does not change either equality.

The source IsVecLine is stronger than a choice of norm on an abstract one-dimensional vector space. At every finite place its fractional ideal is characterized by membership in the tangent lattice of a model. At every complex embedding its squared norm equals π times the polarized Hermitian length of the corresponding tangent vector. Thus an arbitrary metric rescaling chosen to force a desired new value would require a new comparison with those actual geometric conditions.

**Scope.** The original Dirichlet argument can use auxiliary quadratic hosts while proving conclusions for other Dirichlet characters. Consequently (R1) does not imply that every successful relative argument must replace the quadratic logarithmic derivative by the target cubic logarithmic derivative. It proves that this replacement is not an available instantiation of the unchanged record. The task could instead require a new character-weighted arithmetic comparison using the existing auxiliary heights.

## 2. Cubic descent does not create a new stable CM letter degree

Set
\[
 K=\mathbf Q(\zeta),\quad \zeta=\zeta_3,\quad
 \alpha=p^{1/3}>0,\quad M=K(\alpha),
\]
and retain the standing condition p=3 or p≡2 modulo 3. Consider the actual elliptic curves
\[
 A_0:\ y^2=x^3+1,\qquad A_p:\ y^2=x^3+p^2.
\]
Their geometric CM action is (x,y)↦(ζx,y).

### Proposition R2. Stable isometry under the cubic twist

After a finite extension where both curves have good reduction, the polarized CM isomorphism
\[
 g_p:A_p\longrightarrow A_0,\qquad
 (x,y)\longmapsto (x/\alpha^2,y/p)
 \tag{R2}
\]
identifies their integral tangent eigenlines, their polarized archimedean metrics, and their normalized Arakelov degrees. The same holds for each eigenline in the polarized CM products constructed in AM-K010–AM-K011 with the same fixed positive Hermitian form.

**Proof.** The displayed substitution gives
\[
 (y/p)^2=(x/\alpha^2)^3+1
\]
because α³=p. It fixes the origin, commutes with the CM action, and hence preserves the canonical principal elliptic polarization. After a further finite extension both curves have abelian-scheme models. The generic-fibre isomorphism and its inverse extend uniquely between these models, so their maps on integral Lie algebras are inverse integral isomorphisms. At a complex embedding the polarized analytic uniformizations are isomorphic, and the induced Hermitian metric is carried by the same tangent map. The resulting integral metrized lines are isometric.

Normalized Arakelov degree is unchanged by a finite base extension: both finite and infinite contributions multiply by the extension degree before normalization. It therefore gives the same degree for the two stable eigenlines over their original field of definition.

For the products in AM-K010, apply g_p on each elliptic factor. The scalar map commutes with the given matrix action of the larger CM coefficient field and with the fixed Hermitian form. It carries the corresponding polarization and each coefficient-field eigenline to the untwisted one. The preceding argument applies to every such line, not just to the determinant of the whole tangent space. ∎

The coordinate scaling is useful for detecting an incomplete accounting. For the algebraic differential ω=dx/y,
\[
 g_p^*\omega_0=\alpha\,\omega_p,
 \qquad
 \int_{\gamma_p}\omega_p
  =\alpha^{-1}\int_{g_p\gamma_p}\omega_0.
 \tag{R3}
\]
Thus the displayed complex period changes by p^{-1/3}. This is a change of algebraic basis in an isometric stable line. Its finite principal-divisor contribution cancels its archimedean contribution by the product formula. Keeping only the −(log p)/3 in the period would not compute a normalized Arakelov degree.

This assertion concerns stable lines after good reduction and their actual polarized metrics. It does not identify unstable minimal models, remove conductor terms, or set the finite level costs at 2, 3 and p to zero. Those costs remain part of any relative arithmetic adapter.

**Consequence.** In the particular induced CM supply tower already constructed, a norm-one Kummer descent twist can preserve the nontrivial Hom character while leaving every degree used in (R1) unchanged. The nontrivial Galois character is real arithmetic information, but it is not a new stable CM-type height.

## 3. A representation-level obstruction for all CM-type height classes

Write G=Gal(M/Q). With σ(α)=ζα and complex conjugation c fixing α,
\[
 G\simeq S_3,\qquad c\sigma c^{-1}=\sigma^{-1}.
 \tag{R4}
\]
Let ρ be the two-dimensional augmentation representation on the three roots of X³−p. Its character is
\[
\begin{array}{c|ccc}
 \text{cycle type}&1&(12)&(123)\\ \hline
 \chi_\rho&2&0&-1.
\end{array}
\tag{R5}
\]
AM-K001 gives
\[
 L_K(s,\chi)=L_{\mathbf Q}(s,\rho)
            =\zeta_{\mathbf Q(\alpha)}(s)/\zeta_{\mathbf Q}(s).
 \tag{R6}
\]

Let Q^{cm} be the composite of all CM subfields of a fixed algebraic closure. Complex conjugation is central on every finite Galois CM subfield. Such subfields are closed under finite composition and Galois closure. Equivalently Q^{cm} is fixed by the closed subgroup generated by all commutators with complex conjugation (Milne, 2020a, I, Proposition 1.4, Corollary 1.5 and Remark 1.6, p. 10).

### Proposition R7. No cubic component in a finite CM-type height class

Let B/Q be a finite Galois CM field, N=BM, and H=Gal(N/B). Inflate ρ to Gal(N/Q). For every complex class function A inflated from Gal(B/Q),
\[
 \langle A,\chi_\rho\rangle_{\operatorname{Gal}(N/\mathbf Q)}=0.
 \tag{R7}
\]
Consequently no finite complex linear combination of class functions factoring through Q^{cm} equals χρ. In particular no finite combination of CM-type height Artin classes gives the target cubic Artin character.

**Proof.** B∩M is Galois over Q because B and M are Galois. The normal subfields of the S₃ extension M are Q, K and M. The last possibility would imply that complex conjugation is central on Gal(M/Q), because it is central on Gal(B/Q). This contradicts (R4). Hence B∩M is Q or K, and the restriction of H to M is respectively S₃ or its normal subgroup A₃.

The restriction of ρ to A₃ is the sum of its two nontrivial one-dimensional characters. It has no invariant vectors. Thus ρ^H=0. Averaging ρ(h) over h∈H is the zero projector. For each g∈Gal(N/Q),
\[
 \sum_{h\in H}\chi_\rho(gh)
 =\operatorname{Tr}\!\left(\rho(g)\sum_{h\in H}\rho(h)\right)=0.
\]
A is constant on each H-coset. Summing the character inner product by those cosets proves (R7).

Any finite collection of locally constant functions on Gal(Q^{cm}/Q) factors through one finite Galois CM field after enlarging their fields of definition. Their linear span is therefore orthogonal to χρ. Since the latter is an irreducible character with inner product one with itself, it cannot belong to this span. ∎

The standard CM-type class is AΦ^0, the conjugacy average of the convolution Φ*Φ∨ on Gal(Q^{cm}/Q). Its construction is exactly on this quotient (Yang, 2010, §3, equations (3.1)–(3.12); author manuscript pp. 9–10). Proposition R7 concerns that definition and its finite Artin support. It does not require a new case of the Colmez formula.

Thus the obstruction remains even if every relevant CM-type height realization is granted. A finite identity of Artin representations, or an equality of all corresponding Artin Euler factors, cannot turn those CM-type height classes into ρ. Indeed equality of Euler factors at all unramified primes gives equality of characters on a common finite Galois group by Frobenius density, contradicting (R7).

An equivalent short detection is
\[
 [c,\sigma]=c\sigma c^{-1}\sigma^{-1}=\sigma^{-2}=\sigma,
\]
which acts nontrivially under ρ. Every representation factoring through Q^{cm} kills this commutator.

### Limits of the obstruction

1. It is an obstruction to an Artin-character identity, not a proof that an individual real number L′(1,ρ)/L(1,ρ) cannot accidentally equal some CM height expression.
2. It does not exclude infinite approximation schemes or an arithmetic construction with non-CM descent data.
3. It does not exclude a relative comparison in which CM heights remain auxiliary and the cubic character is represented elsewhere.
4. It does not say that the cubic Artin line is absent from all tensor categories generated by CM abelian varieties. AM-K004 explicitly realizes it as a Hom line between two CM elliptic eigensummands. The failure is in the CM-type class function used for the stable height, which forgets this finite descent twist.

For odd prime r the same argument applies to the augmentation representation of C_r⋊(Z/rZ)^×. Complex conjugation acts by inversion on C_r, and [c,σ]=σ^{-2} generates C_r. The augmentation representation has no C_r invariants. The cubic case has the additional explicit ray-character and rank-one lattice constructions used below.

## 4. A concrete relative theta period for the target logarithmic derivative

This section gives an actual function and an exact integral formula. It is independent of any proposed CM-height identification.

The primitive conductor from AM-K003 has the following scalar ideal generator m:
\[
\begin{array}{c|c|c}
 \text{case}&\mathfrak f=m\mathcal O_K&Q=3N\mathfrak f=|D_{\mathbf Q(\alpha)}|\\ \hline
 p\ne3,\ p\equiv8\pmod9&m=p&3p^2\\
 p\ne3,\ p\equiv2,5\pmod9&m=3p&27p^2\\
 p=3&m=9&243.
\end{array}
\tag{R8}
\]
Let Λ=O_K=Z[ζ]⊂C in the fixed complex embedding. Its Euclidean covolume is V=√3/2, and |a+bζ|²=a²−ab+b².

Define the periodic function
\[
 w(a)=
 \begin{cases}
 \chi((a)),&(a,\mathfrak f)=1,\\
 0,&(a,\mathfrak f)\ne1.
 \end{cases}
 \qquad a\in\Lambda.
 \tag{R9}
\]
Here w(0)=0. Because K has class number one, the actual character is already given explicitly by AM-K007 on the finite unit quotient. The definition is independent of an ideal generator, invariant under the six units, and periodic modulo mΛ. As a nontrivial multiplicative character on (O_K/𝔣)^×, extended by zero, it has mean zero.

Set
\[
 \Theta_\chi(t)=\sum_{a\in\Lambda}
                  w(a)e^{-\pi t|a|^2},
 \qquad t>0,
 \tag{R10}
\]
and
\[
 I_\chi(s)=\int_0^\infty\Theta_\chi(t)t^{s-1}\,dt.
 \tag{R11}
\]

### Proposition R12. Convergence and exact Mellin identity

The integral in (R11), and the integrals obtained by inserting any fixed power of log t, converge absolutely locally uniformly in s∈C. Therefore Iχ is entire. Moreover
\[
 I_\chi(s)=6\pi^{-s}\Gamma(s)L_K(s,\chi)
 \tag{R12}
\]
by analytic continuation. The function Θχ is real-valued.

**Proof.** For t bounded below away from zero, (R10) is absolutely and locally uniformly convergent by the positive-definite norm on Λ. Because w(0)=0, it decays exponentially as t→∞.

For the other endpoint, let Λ* be the Euclidean dual lattice, with pairing ⟨z,a⟩=Re(z\bar a). The finite characters of Λ/mΛ are indexed by
\[
 \xi\in m^{-1}\Lambda^*/\Lambda^*.
\]
With
\[
 \widehat w(\xi)=m^{-2}
  \sum_{b\in\Lambda/m\Lambda}
      w(b)e^{-2\pi i\langle\xi,b\rangle},
\]
finite Fourier inversion gives
\[
 w(a)=\sum_\xi\widehat w(\xi)e^{2\pi i\langle\xi,a\rangle}.
\]
Its constant coefficient is zero. Poisson summation for the two-dimensional Gaussian yields
\[
 \Theta_\chi(t)=\frac1{Vt}
   \sum_{\xi\ne0}\widehat w(\xi)
      \sum_{\lambda^*\in\Lambda^*}
       \exp\!\left(-\frac{\pi|\lambda^*-\xi|^2}{t}\right).
 \tag{R13}
\]
Each nonzero coset has positive distance from Λ*. There are finitely many cosets. Hence Θχ(t)=O(t^{-1}e^{-c/t}) for some explicit c>0. These two endpoint bounds remain integrable after multiplication by t^{Re(s)−1}|log t|^j, uniformly on every compact set of s. Differentiation under the integral and entireness follow.

For Re(s)>1, absolute convergence permits termwise integration. The Gaussian integral is Γ(s)(π|a|²)^{-s}. Each nonzero integral ideal of O_K has exactly six generators, all of the same norm and character value. Thus the sum is six times the Hecke ideal series and gives (R12) in this half-plane, then everywhere by continuation.

Finally χ(\bar{\mathfrak a})=\overline{\chi(\mathfrak a)} by AM-K002, while norms and the conductor are invariant under conjugation. The substitution a↦\bar a conjugates the sum without changing it, so Θχ(t) is real. No pointwise positivity is asserted. ∎

### Explicit tail bounds

The preceding proof is effective. Since |ŵ(ξ)|≤1 and Λ*=(2i/√3)Λ, define
\[
 B(a)=\left(1+\frac{2e^{-a}}{1-e^{-3a}}\right)^2-1
 \qquad(a>0).
\]
The elementary inequalities n²≥1+3(n−1) for n≥1 and
a²−ab+b²≥(a²+b²)/2 give
\[
 |\Theta_\chi(t)|\le B(\pi t/2),
 \qquad
 |\Theta_\chi(t)|\le\frac1{Vt}
                    B\!\left(\frac{2\pi}{3m^2t}\right).
 \tag{R14}
\]
For the second bound, the disjoint nonzero dual cosets in (R13) form a subset of m^{-1}Λ*\setminus\{0\}; summing the absolute values over that larger lattice proves the formula. These inequalities give certified truncation of the integral and its logarithmic moments. They are not a useful arithmetic-window estimate by themselves.

### Corollary R15. An exact replacement scalar as a logarithmic heat moment

The denominator Iχ(1) is positive. One has
\[
 \frac{L'_K(1,\chi)}{L_K(1,\chi)}
 =\log\pi+\gamma+
   \frac{\displaystyle\int_0^\infty
                       \Theta_\chi(t)\log t\,dt}
        {\displaystyle\int_0^\infty
                       \Theta_\chi(t)\,dt}.
 \tag{R15}
\]
Consequently, for any v>0, the scalar having the same displayed analytic form as the source scalar is
\[
\begin{aligned}
 \log\Omega_\chi(v)
 &:=\gamma+\log(\pi/v)
        -\frac{L'_K(1,\chi)}{L_K(1,\chi)}\\
 &=-\log v-
   \frac{\displaystyle\int_0^\infty
                       \Theta_\chi(t)\log t\,dt}
        {\displaystyle\int_0^\infty
                       \Theta_\chi(t)\,dt}.
\end{aligned}
\tag{R16}
\]

**Proof.** The quotient in (R6) and the positive residue of the Dedekind zeta function at one give L_K(1,χ)>0. Equation (R12) gives Iχ(1)=6L_K(1,χ)/π>0. Its logarithmic derivative at one, using Γ′(1)/Γ(1)=−γ, is
\[
 I_\chi'(1)/I_\chi(1)
  =-\log\pi-\gamma+L_K'(1,\chi)/L_K(1,\chi).
\]
Rearrangement proves both assertions. ∎

This is a finite ray-character weighted lattice theta function with a completely specified Gaussian and measure. It changes actual summands according to χ; it is not the result of conjugating an unchanged oscillator chain by scalar phases. The Fourier version (R13) also makes it a finite linear combination of shifted dual-lattice heat sums.

The construction supplies a precise relative period to compare against an arithmetic model. It does not supply that comparison. In particular this report does not identify (R16) with any line satisfying the unchanged IsVecLine and LamDegSt conditions in §1. An integral or spectral construction with this logarithmic moment would need its own finite-place lattice, determinant formula, and estimate.

## 5. Why a leading regulator alone does not supply the source scalar

Let F=Q(α) and Q=|D_F|. AM-K003 supplies the exact completion
\[
 \Lambda(s)=Q^{s/2}\Gamma_{\mathbf C}(s)L_K(s,\chi),
 \qquad
 \Gamma_{\mathbf C}(s)=2(2\pi)^{-s}\Gamma(s),
 \qquad
 \Lambda(s)=\Lambda(1-s).
 \tag{R17}
\]
The value Λ(1) is nonzero and finite. Therefore L_K(s,χ) has a simple zero at zero. Write
\[
 L_K(s,\chi)=a s+b s^2+O(s^3),\qquad a\ne0.
 \tag{R18}
\]

### Proposition R19. The required invariant is a next-coefficient ratio

The exact relation is
\[
 \frac{L'_K(1,\chi)}{L_K(1,\chi)}
 =-\log Q+2\log(2\pi)+2\gamma
       -\frac{L_K''(0,\chi)}{2L_K'(0,\chi)}.
 \tag{R19}
\]
If h_F and Reg(F) denote the ordinary class number and regulator, then
\[
 L_K(1,\chi)=\frac{2\pi h_F\operatorname{Reg}(F)}{\sqrt Q},
 \qquad
 L_K'(0,\chi)=h_F\operatorname{Reg}(F).
 \tag{R20}
\]
Moreover, for the Laurent expansion
\[
 \zeta_F(s)=\frac{R_F}{s-1}+C_F+O(s-1),
 \qquad \gamma_F=C_F/R_F,
\]
one has
\[
 L_K'(1,\chi)/L_K(1,\chi)=\gamma_F-\gamma.
 \tag{R21}
\]

**Proof.** The expansion Γ(s)=s^{-1}−γ+O(s) gives
\[
 \frac{\Lambda'(0)}{\Lambda(0)}
   =\tfrac12\log Q-\log(2\pi)-\gamma+b/a.
\]
At one,
\[
 \frac{\Lambda'(1)}{\Lambda(1)}
   =\tfrac12\log Q-\log(2\pi)-\gamma
      +\frac{L_K'(1,\chi)}{L_K(1,\chi)}.
\]
The logarithmic derivative of (R17) makes these two expressions negatives. Since b/a=L_K″(0,χ)/(2L_K′(0,χ)), this proves (R19).

F has signature (1,1) and only two roots of unity. The analytic class number formula therefore gives R_F=2πh_F Reg(F)/√Q. This is L_K(1,χ) by (R6). This specialization uses Milne (2020b), V, Theorem 2.4(a), p. 156. At zero, Λ(0)=2a. At one, Λ(1)=√Q L_K(1,χ)/π. Equality gives the second assertion in (R20).

Finally divide the displayed Laurent expansion of ζ_F by
ζ_Q(s)=(s−1)^{-1}+γ+O(s−1). The constant term of the quotient is R_F, and its linear coefficient is C_F−γR_F. Their quotient is (R21). ∎

Thus an explicit unit or regulator realization of the leading coefficient L_K′(0,χ) is valuable, but it is not the invariant needed in (R1) with χ inserted. Formula (R19) requires the next coefficient relative to the leading one. Equivalently (R21) requires the Euler–Kronecker constant of the non-Galois cubic field, relative to that of Q.

For comparison with the theta construction,
\[
 I_\chi(0)=6h_F\operatorname{Reg}(F),\qquad
 I_\chi(1)=12h_F\operatorname{Reg}(F)/\sqrt Q.
 \tag{R22}
\]
Its logarithmic moment Iχ′(1)/Iχ(1), rather than either displayed value alone, is precisely the new scalar in (R16).

## 6. The actual Artin motive and its ordinary period matrix

There is no need to posit a new variety merely to realize the representation.

Over K, let σ generate Gal(M/K). In the convention where Γσ acts by σ, the projector
\[
 e_\chi=\frac13\sum_{j=0}^2\chi(\sigma)^{-j}\Gamma_{\sigma^j}
 \tag{R23}
\]
on h⁰(Spec M), with coefficients containing μ₃, gives the rank-one χ component. Reversing the cohomological action convention exchanges χ and χ^{-1}, whose L-functions coincide here.

Over Q, let π:Spec F→Spec Q. The degree-three unit and trace maps give the rational projector
\[
 e_\rho=1-\frac13\pi^*\pi_*,
 \qquad
 h^0(\operatorname{Spec}F)=\mathbf1\oplus\mathcal M_\rho.
 \tag{R24}
\]
Indeed π_*π^*=3 on the trivial summand, so eρ²=eρ. Its Betti realization is the trace-zero part of the three-element permutation representation, hence is ρ. Its Artin L-function is exactly (R6).

For an explicit de Rham/Betti comparison, the trace-zero de Rham space is
\[
 \ker(\operatorname{Tr}_{F/\mathbf Q}:F\to\mathbf Q)
   =\mathbf Q\alpha\oplus\mathbf Q\alpha^2.
\]
Evaluating on the three embeddings gives the matrix
\[
 \begin{pmatrix}
  \alpha&\alpha^2\\
  \zeta\alpha&\zeta^2\alpha^2\\
  \zeta^2\alpha&\zeta\alpha^2
 \end{pmatrix}.
 \tag{R25}
\]
Its columns sum to zero, and the first two rows have determinant p(ζ²−ζ)≠0. This is a fully explicit algebraic comparison for the weight-zero Artin motive.

An ordinary Artin comparison matrix such as (R25) has algebraic entries. By itself it does not prescribe the logarithmic heat moment (R16), its integral metric, or its derivative-of-L determinant formula. The leading regulator statement (R20) supplies a different arithmetic object, involving units; (R19) explains exactly why that leading datum alone is still insufficient.

There is also the positive-dimensional realization from AM-K004: an eigensummand of Hom(h¹(A₀),h¹(A_p)) over K carries χ or its inverse. Proposition R2 and (R25) explain how a nontrivial Artin descent can coexist with unchanged stable CM height. These are compatible facts, not contradictory notions of “CM”.

## 7. What this changes in the steps 2–20 audit

The complete original step table remains in kummer_extension.md, §7. The present proof resolves the following narrower questions.

| Part of the attempted transfer | New exact conclusion | Remaining obligation |
|---|---|---|
| CM geometric supply and character descent | The explicit polarized cubic twists and induced CM tower exist; their actual stable tangent letters are isometric to the untwisted ones. | Compute descent-sensitive finite indices and the genuinely character-weighted arithmetic quantity. |
| The height term used in MAIN | The unchanged source record fixes a quadratic dlogL and actual degrees. The cubic S₃ character cannot be obtained by a finite CM-type height Artin-class identity. | A new comparison theorem, or an auxiliary-height argument that inserts the cubic character outside that scalar. |
| Ideal/ray-character analytic side | Θχ and its Mellin transform give the exact cubic L-function, including the wild p=3 case and primitive conductor. | Relate this actual relative period to the chosen arithmetic sections and lattice estimates. |
| Motivic realization | The rank-two Q-Artin projector and rank-one K-projector are explicit; a CM elliptic Hom realization is already available. | A period/metric/determinant construction representing the logarithmic moment, with all finite terms. |
| Leading special values | L(1), L′(0), and the ordinary unit regulator are exactly related. | Control L″(0)/(2L′(0)), or equivalently the relative Euler–Kronecker invariant, in the required arithmetic comparison. |
| Final analytic implication | AM-K005 already supplies the field-independent Landau/window adapter. | Prove its full family of arithmetic window bounds. None follows merely from the formulas above. |

The relative Mellin construction is therefore a concrete alternative target, rather than an unspecified “Hecke analogue of Chowla–Selberg”. Its input is the already explicit ray character, its output is exactly the required logarithmic derivative, and its normalization is fixed in (R10)–(R16). The open part is an arithmetic realization and estimate of this period that meets the actual source hypotheses.

## 8. Sources and verification scope

- Alpöge, L. (2026). Author Lean archive, source locations in §1. The local mirror is the parent-recovered source set. This report inspects the listed definitions and statements; it makes no new whole-archive compilation claim.
- Milne, J. S. (2020a). *Complex multiplication*. I, Proposition 1.4, Corollary 1.5 and Remark 1.6, p. 10. https://www.jmilne.org/math/CourseNotes/CM.pdf. Used only for the maximal CM quotient and central conjugation facts; the obstruction in Proposition R7 is proved here.
- Milne, J. S. (2020b). *Class field theory*. V, §2, especially Theorem 2.4(a)–(b), pp. 155–156. https://www.jmilne.org/math/CourseNotes/CFT.pdf. Used for the Hecke ideal convention, nonvanishing at one and the analytic class number formula.
- Yang, T. (2010). The Chowla–Selberg formula and the Colmez conjecture. *Canadian Journal of Mathematics, 62*(2), 456–472. https://doi.org/10.4153/CJM-2010-028-x. Author manuscript: https://people.math.wisc.edu/~tonghaiyang/Colmez.pdf. §3, equations (3.1)–(3.12), author pp. 9–10, defines the CM-type class functions on the maximal CM quotient. No unproved general Colmez formula is invoked in Proposition R7.
- Internal proved prerequisites: AM-K001–AM-K005 and AM-K007–AM-K011, at the companion paths identified at the beginning. All new analytic identities in §§4–6 are proved above with explicit normalizations.

**Completed author checks.** The saved report was read in full and its arguments reconstructed: stable polarized tangent-line isometry; the common-Galois-group averaging in (R7); conductor and unit factors; both finite Fourier normalizations and Gaussian tail bounds; the Mellin logarithmic derivative; both gamma-factor expansions in (R19); the class-number and regulator constants; and the Artin projectors and trace-zero comparison matrix. The listed source interfaces and the cited primary definitions were inspected directly. No numerical or finite computational certificate was run for this report. The continuation in (R12) follows from its convergence proof, not from numerical agreement. The author check and source-use events are recorded in kummer_extension_CHECK_EVENTS.tsv.
