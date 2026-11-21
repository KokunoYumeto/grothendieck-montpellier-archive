# The full complementary Chow group: a rigorous further reduction

Run `JAC1964-20261121`. Author/checker: `/root/arithmetic_sign`, GPT-6 Astra Pro; effort setting not exposed. Date: 2026-11-21 UTC. The positive Fermat height and the positive CM orbit below are established inputs from AR-13 and programme JAC-P11. This section does not identify a Selmer rank with a Chow rank.

## 1. Setup and the positive subspace already obtained

Let \(J\) be the Fermat-quartic Jacobian and use the normalized real Beilinson--Bloch pairing \(h_F\) of AR-1--AR-13. After a finite number-field extension containing the required correspondences, programme JAC-P13 identifies the complementary motive exactly as
\[
N=h^3(J)^G,\qquad G=\mu_4^2,
\quad V_F=\operatorname{CH}^2(N_F)
       =\operatorname{CH}^2_{(1)}(J_F)_{\mathbf Q}^{G}.
\tag{AR15.1}
\]
The projector is self-transpose. Its Betti realization has only types \((3,0)\) and \((0,3)\), each once. Every class in \(V_F\) is homologically trivial.

JAC-P11 and JAC-P13 give an actual rational correspondence \(T\) on this whole Chow group with
\[
T^2=-1,
\qquad h_F(Tz,Tw)=h_F(z,w).
\]
Thus \(V_F\) is a \(\mathbf Q(i)\)-module. The complex-valued Hermitian form, linear in its first variable, is
\[
\mathscr H_F(z,w)=h_F(z,w)+i h_F(z,Tw).
\]
For the hyperflex-normalized Fourier--Ceresa class \(\eta\),
\[
U_F=\mathbf Q\eta\oplus\mathbf Q T\eta,
\qquad h_F(r\eta+sT\eta,r\eta+sT\eta)
  =(r^2+s^2)h_F(\eta,\eta)>
  \frac{r^2+s^2}{100}\quad\bigl((r,s)\ne(0,0)\bigr).
\tag{AR15.2}
\]
The two classes are independent even modulo algebraic equivalence. They form one positive \(\mathbf Q(i)\)-line. The following reduction concerns all of \(V_F\), without assuming that this line generates it.

## 2. An unconditional radical and an exact Griffiths-quotient reduction

**Theorem AR-15 (algebraically trivial complementary cycles have zero height against the whole complement).** In the general setup of AR-2, let \(A/F\) have dimension \(2m-1\), and let \(N\subset h^{2m-1}(A)\) be its self-transpose complementary Chow summand. Assume that \(H(N)\) has no nonzero sub-Hodge structure of types \((m,m-1),(m-1,m)\). Put
\[
V_F=\operatorname{CH}^m(N_F),\qquad
\mathcal A_F=V_F\cap\operatorname{CH}^m(A_F)_{\rm alg}.
\]
Here algebraic triviality may be interpreted geometrically. Then
\[
(-1)^m h_F(a,y)=0
\qquad(a\in\mathcal A_F,\;y\in V_F).
\tag{AR15.3}
\]
Consequently the signed height descends to
\[
\operatorname{Griff}^m(N_F):=V_F/\mathcal A_F.
\tag{AR15.4}
\]
Semipositivity on \(V_F\) is equivalent to semipositivity on this quotient. Strict positivity on \(V_F\) is equivalent to **both** \(\mathcal A_F=0\) and strict positivity on the quotient.

*Proof.* It is enough to work after a finite extension of \(F\): normalized heights are unchanged, and restriction on rational Chow groups is injective by the restriction--corestriction identity. Every algebraically trivial class is a finite sum of classes
\[
\Gamma_{0*}D,
\qquad D\in\operatorname{Pic}^0(C)(F)_{\mathbf Q},
\quad\Gamma_0\in\operatorname{CH}^m(C\times A)_{\mathbf Q},
\]
where \(C\) is a smooth projective geometrically connected curve. A finite field extension suffices to define the finitely many curves, correspondences, and divisors occurring in such an expression. Apply the projector \(\pi_N\) and put \(\Gamma=\pi_N\circ\Gamma_0\). Since \(a\in V_F\), these projected expressions still sum to \(a\).

Fix \(y\in V_F\). Its ordinary cycle class is zero because it belongs to the odd-degree Chow--Künneth component. By codimension bookkeeping,
\[
{}^t\Gamma_*y\in\operatorname{CH}^1(C)_{\rm hom,\mathbf Q}
                   =\operatorname{Pic}^0(C)(F)_{\mathbf Q}.
\]
After a complex embedding, the cohomological map of \({}^t\Gamma\) factors through
\[
H(N)(m-1)\longrightarrow H^1(C).
\]
This morphism is zero. Indeed its transpose is a morphism from \(H^1(C)\) into \(H(N)(m-1)\), whose image would have only types \((1,0),(0,1)\); the defining hypothesis on \(N\) excludes such an image. Equivalently use duality and semisimplicity of polarizable Hodge structures. Self-transposition of \(\pi_N\) is what places the transposed correspondence on the same summand.

Functoriality of the complex Abel--Jacobi map therefore gives
\[
\operatorname{AJ}_C({}^t\Gamma_*y)=0.
\]
For divisors on a curve, Abel's theorem identifies this map with the injective identification of degree-zero divisor classes with their Picard class. Hence \({}^t\Gamma_*y=0\) in \(\operatorname{CH}^1(C_{\mathbf C})_{\mathbf Q}\). This detects zero already over the number field: the map on Picard points is injective after field extension, or one can spread the trivialization to a finite extension and apply the norm. The projection formula for the arithmetic height gives
\[
h_F(\Gamma_*D,y)=h_F(D,{}^t\Gamma_*y)=0.
\]
Sum over the finitely many expressions for \(a\). This proves (AR15.3). A bilinear form whose radical contains \(\mathcal A_F\) descends to \(V_F/\mathcal A_F\), and the stated positivity equivalences follow directly. \(\square\)

The background functoriality is recorded explicitly in Achter--Casalaina-Martin--Vial, *Decomposition of the diagonal, intermediate Jacobians, and universal codimension-2 cycles in positive characteristic*, Astérisque 455 (2025), §3.2.4, equation (3.5), pp.17--18. The arithmetic projection formula is AR-B1. No injectivity of a higher Abel--Jacobi map is used: the only injectivity is the classical divisor statement on the auxiliary curve.

For the Fermat motive, AR-15 yields a precise possible zero-direction mechanism. **Any nonzero class of \(\mathcal A_F\) would have zero height and would disprove strict positivity on the full rational Chow group.** No such nonzero class has been produced here. Its vanishing is not supplied by the positive value of \(h_F(\eta,\eta)\). The positive plane (AR15.2) injects into \(\operatorname{Griff}^2(N_F)\), so it survives this further reduction.

## 3. What would make a Selmer-rank bound sufficient

Let \(p\) be a rational prime, put
\[
W_p=H^3_{\rm et}(N_{\overline F},\mathbf Q_p)(2),
\qquad S_p(F)=H^1_f(F,W_p),
\]
and let
\[
\alpha_{p,F}:V_F\otimes_{\mathbf Q}\mathbf Q_p
             \longrightarrow S_p(F)
\tag{AR16.1}
\]
be the scalar-extended étale Abel--Jacobi map. Its finite local conditions are valid for the present potentially good-reduction setting. A primary locator is Nekovář, *p-adic Abel-Jacobi maps and p-adic heights*, Proposition 2.5, Theorem 3.1(i), and §4.1; CM abelian varieties acquire good reduction locally after finite extension. Neither existence of this map nor those local conditions assert injectivity.

**Proposition AR-16 (a sufficient finite-rank criterion, with its missing hypothesis exposed).** Fix a number field \(F\) over which \(N,T,\eta\) are defined. If
\[
\dim_{\mathbf Q_p}S_p(F)\le2
\quad\hbox{and}\quad
\ker\alpha_{p,F}=0,
\tag{AR16.2}
\]
then
\[
V_F=U_F.
\tag{AR16.3}
\]
In particular the full complementary height over this \(F\) is strictly positive, and the complete primitive height is strictly positive after adjoining the orthogonal Picard block of AR-2.

*Proof.* Extension of scalars preserves linear independence of rational vectors. The injective map (AR16.1) and the dimension bound in (AR16.2) imply \(\dim_{\mathbf Q}V_F\le2\), even if finite-dimensionality had not previously been known. Equation (AR15.2) already provides two independent vectors in \(V_F\). They therefore form a basis. Their height matrix is \(h_F(\eta,\eta)I_2\), which is strictly positive by AR-13. Orthogonality to the Picard block completes the assertion. \(\square\)

The scalar extension in (AR16.1) is essential. An injective merely \(\mathbf Q\)-linear map \(V_F\to S_p(F)\) does not bound \(\dim_{\mathbf Q}V_F\) by \(\dim_{\mathbf Q_p}S_p(F)\): for \(a\in\mathbf Q_p\setminus\mathbf Q\), the map \((r,s)\mapsto r+as\) injects \(\mathbf Q^2\) into a one-dimensional \(\mathbf Q_p\)-space. After scalar extension this map has a nonzero kernel. Thus even an injectivity claim must be read with its precise coefficients.

A weaker exact criterion is sometimes useful. If a **rational** subspace \(R_F\subset\operatorname{rad}(h_F|_{V_F})\) is proved to satisfy
\[
V_F=U_F+R_F,
\tag{AR16.4}
\]
then the sum is direct, the height is semipositive, and it is strictly positive exactly when \(R_F=0\). This follows because a positive subspace meets the radical trivially. A Selmer-rank bound alone proves neither the rational decomposition (AR16.4) nor inclusion of an Abel--Jacobi kernel in the radical of the **real** pairing.

All these statements are over the **specified field \(F\)**. A rank-one theorem over \(\mathbf Q\) cannot simply be applied after adjoining \(i\), nor after adjoining fields of definition of arbitrary cycles. Over \(\mathbf Q(i)\), the rank-two Galois representation splits into two conjugate characters. Its Selmer group is the direct sum of their Selmer groups, because the Bloch--Kato local conditions respect direct sums. Conjugation identifies the dimensions of the two character factors. A rank-one bound for each character therefore gives a dimension-two bound over \(\mathbf Q(i)\), before any further extension. It gives no uniform dimension-two bound over every finite extension or over the direct limit defining \(V_{\overline{\mathbf Q}}\).

## 4. Exact current scope of the relevant CM theorems

**Audit AR-17.** The following are primary-source scope checks. The initially open Katz calculation and conductor-specific rank implication are now supplied by AR-19 and H9-T15. They give the character Selmer rank one, hence rank two for the full Fermat representation over \(K_0=\mathbf Q(i)\). Scalar-extended Chow Abel--Jacobi injectivity in (AR16.2), and the alternative rational decomposition (AR16.4), remain unproved.

### 4.1 The relevant character really is a cubic power, at the excluded central boundary

Write \(K_0=\mathbf Q(i)\), \(\mathfrak q=(1+i)\), and use BDP's characters \(\psi,\psi'\) of \(E:y^2=x^3-x\), \(E':y^2=x^3+x\). BDP §5.2, author pp.24--25, gives \(\psi'=\psi\mu\), with \(\mu^2=1\) and conductor \(\mathfrak q^4\). Therefore our motive's character satisfies the exact identity
\[
\chi=\psi^2\psi'=\psi^3\mu=(\psi')^3.
\tag{AR17.1}
\]
Its conductor is \(\mathfrak q^4\), its theta series has weight four and level 64, and AR-11 proves its simple central zero at \(s=2\).

Jonathan Dee, *Selmer groups of Hecke characters and Chow groups of self products of CM elliptic curves*, arXiv:math/9901155, Theorem 5.1.2, p.28, treats representations
\[
V_{j,k}=V_1(E')^{\otimes(j+k)}(-j)
\quad\text{with}\quad j\ge0,\quad k>j+1.
\]
The desired central representation is \(V_{1,2}\): the rational Tate module is \(H^1(E')(1)\), so its cube twisted by \(-1\) has the required twist \((2)\). But \(2>1+1\) is false. The theorem's noncentral critical-value range therefore excludes our case exactly at its boundary. Theorem 1.0.1's nonvanishing at \(s=k\) is likewise not a theorem about the cubic central value at \(s=2\).

Dee's Theorems 1.0.2 and 5.1.5, pp.3 and 29, prove a statement about
\[
\operatorname{Im}(\mathrm{cl})\cap
F^2H^{2i}(X,\mathbf Q_p(i)).
\]
They do not prove injectivity of \(\mathrm{cl}\). There is a particularly direct check for our summand: the projector of \(N\) kills every geometric cohomology group except \(H^3\). In the projected Hochschild--Serre spectral sequence, the only term contributing to total degree four is \(H^1(F,H^3(N)(2))\). Hence
\[
F^2H^4(N,\mathbf Q_p(2))=0
\]
already. A theorem saying that the image has zero intersection with this zero subspace imposes no condition on the kernel in (AR16.1). This is the precise reason the title's reference to Chow groups does not solve the present Chow-rank problem.

### 4.2 Castella's standing conductor hypothesis and a separate proof-level route

Castella, *Tamagawa number conjecture for CM modular forms and Rankin--Selberg convolutions*, author manuscript dated 14 February 2025, starts §5, printed p.21, with the standing hypothesis
\[
(\mathrm{div}):\qquad p\nmid\mathfrak c,\qquad
\mathfrak d_{K_0}\Vert\mathfrak c.
\]
Although Theorem 5.2.1, pp.23--24, does not repeat its second clause in the displayed statement, that omission does not remove the section's standing restriction. The theorem gives, within its stated scope,
\[
\mathcal L_v(\lambda\mathbf N^{-r})(0)\ne0
\quad\Longrightarrow\quad
\dim_\Phi H^1_f(K_0,V_\lambda(r))=1
\tag{AR17.2}
\]
for the specified self-dual character of infinity type \((1-2r,0)\). Theorem C, p.4, and Theorem 5.3.1, p.24, likewise impose exact divisibility by the different.

For the Fermat character take \(r=2\), \(p=5\), \(K_0=\mathbf Q(i)\), and the same ideal-valued character \(\lambda=\chi\), written in Castella's opposite infinity-type convention. The prime splits, is greater than three, is prime to the class number and conductor, and the central character is the required quadratic character. However,
\[
\mathfrak d_{K_0}=\mathfrak q^2,\qquad
\mathfrak c_\chi=\mathfrak q^4,
\]
so the standing exact-conductor condition fails. We therefore do **not** cite Theorem 5.2.1 as a theorem that directly covers this character.

There is a more precise proof-level route. Theorem 4.2.1, printed p.16, constructs twisted elliptic units and their Coleman-map reciprocity law for any self-dual character with the specified prime-to-\(p\) conductor; Theorem 4.3.1, p.17, also permits arbitrary prime-to-\(p\) conductor. The proof of Theorem 5.2.1 uses that reciprocity law, Lemma 3.4.2's local conditions, central vanishing, an elliptic-unit Euler-system bound, and global duality. The independent deduction H9-T15 now checks those ingredients separately and proves the rank-one implication at the actual conductor \(\mathfrak q^4\). It uses Rubin's full twisted elliptic-unit Euler system and strict-dual Selmer bound, with the bad prime above 2 retained in the excluded-prime ideal, followed by the explicit Poitou--Tate dimension formula. This is a reconstructed proof, not a claim that §5 silently withdrew its standing hypothesis.

The analytic premise required by that route was the single **Katz** value
\[
\mathcal L_v(\chi\mathbf N^{-2})(0)\ne0.
\tag{AR-KATZ}
\]
AR-19 now proves (AR-KATZ) directly, by an integral Katz-measure congruence at 5 and an exact fourth-order theta coefficient. It does not use the complex derivative to infer p-adic nonvanishing. AR-11's positive **complex** derivative is not this premise. Remark 5.2.2, p.23, explains why the known weight-two implication from a simple complex zero does not yet carry over to higher weights: it requires both an Abel--Jacobi injectivity statement and nonzero localization. Remark 1.2.1, p.4, retains the higher-weight implication as an expectation. Remark 1.2.2 and its footnote 2, p.4, retain injectivity of the \(p\)-adic Abel--Jacobi map and nondegeneracy of the height as additional inputs to the proposed full motivic consequence.

### 4.3 The BDP calculation does not yet identify the required Katz value at the ramified prime

BDP, *p-adic L-functions and the coniveau filtration on Chow groups*, Proposition 5.2.1, author pp.26--27, proves a nonzero local Abel--Jacobi evaluation for a generalized Heegner-type cycle associated with the Fermat example; the displayed congruence (5.2.3) can be checked with \(k=2,p=5\). This is considerably more arithmetic information than ordinary Betti nonvanishing.

However, their Rankin--Katz factorization Proposition 3.3.1, p.13, is stated with the conductor of the theta character cyclic and of norm prime to the discriminant. In the Fermat construction the theta character is \(\psi^2\), of conductor \(\mathfrak q^2\), at the ramified prime 2. Their Proposition 3.2.1 also assumes odd discriminant and an odd auxiliary conductor. Section 5.2, p.27, explicitly notes that its general exact local formula does not cover this even-discriminant/even-conductor situation, and leaves the local 2-factor for that comparison uncomputed.

Consequently we have not equated the nonzero BDP evaluation with (AR-KATZ), and that exact ramified local comparison remains open. AR-19 bypasses it: its direct integral-measure calculation proves the Katz value is nonzero without the Rankin factorization. Combined with H9-T15 this establishes the stated Selmer-rank result. It does not establish scalar-extended injectivity in (AR16.1).

### 4.4 The generalized Rubin formula retains both the nonvanishing premise and incompatible hypotheses

Longo--Vigni--Wang, *A generalized Rubin formula for Hecke characters*, arXiv:2501.03673v1, Assumption 1.1 and Theorem A, p.2, requires odd imaginary-quadratic discriminant, exact divisibility of the conductor by the different, and a nonzero Katz value. It gives a rank-one Selmer space and a formula for its logarithm. Both the odd-discriminant and exact-conductor hypotheses fail for the present \(\mathbf Q(i)\) character. The introduction, pp.3--4, also explains the additional conjectural steps needed to replace the Katz premise by a nonzero complex derivative. This theorem does not establish (AR-KATZ), (AR16.2), or a real-height factorization for the Fermat Chow group.

### 4.5 A proved p-adic height factorization cannot be substituted for the real one

Nekovář, *p-adic Abel-Jacobi maps and p-adic heights*, Corollary 4.3 and Remark 4.4(2), printed p.7, distinguish these statements explicitly. His constructed \(p\)-adic heights factor through \(p\)-adic Abel--Jacobi maps, with choices of a \(p\)-adic logarithm and Hodge-filtration splittings. The remark separately asks whether the real height factors through the complex Abel--Jacobi map in higher codimension. No result used here identifies these two height pairings or transfers a radical statement from one to the other. AR-15 obtains its restricted real radical by a separate curve-correspondence proof.

The fact that the complex intermediate Jacobian of our rank-two Hodge structure is a one-dimensional complex torus gives no remedy. The Hodge structure \(H(N)(1)\) has types \((2,-1),(-1,2)\), whereas \(H^1\) of an elliptic curve has types \((1,0),(0,1)\). A correspondence inducing an isomorphism between them is excluded by these types. Even a one-dimensional complex torus has point groups of unbounded rational rank; its complex dimension does not bound a Chow group's rational dimension. It supplies neither a number-field Abel--Jacobi morphism to an elliptic curve nor an arithmetic Néron--Tate comparison for \(V_F\).

### 4.6 Infinite-rank results require their own motive-transfer argument

Lilienfeldt, *Heegner cycles in Griffiths groups of Kuga--Sato varieties*, arXiv:2107.06731v3, Theorem 1.4, p.4, proves infinite rank over \(K^{\rm ab}\) for the subgroup generated by Heegner cycles on the stated Kuga--Sato variety. Its Remark 1.6, on the same page, explicitly labels injectivity of the étale Abel--Jacobi map for number-field cycles as conjectural. Remark 4.4, p.13, gives the formula on a fixed newform's intermediate-Jacobian component.

The theorem as stated does not assert infinite rank for our particular \(N\). Passing from an infinite-rank subgroup on the entire Kuga--Sato variety to a specified \(f\)-component requires checking that projection in the proof, and then transporting it to \(N\) requires an actual algebraic correspondence. Equality of compatible Galois realizations or of \(L\)-functions alone is insufficient. The distinction is visible in Longo--Vigni--Wang §2.4 and Proposition 2.7, pp.6 and 12: their motive comparisons there are in the category of absolute Hodge cycles. The existence of separate Chow realizations does not, by itself, turn the comparison into an isomorphism of Chow motives. We therefore assert neither a finite-rank generation theorem nor an infinite-rank counterexample for \(V_{\overline{\mathbf Q}}\) from these sources.

## 5. Current exact remaining requirements

The established result is strict positivity on the orthogonal Picard block together with the positive \(\mathbf Q(i)\)-line generated by \(\eta\). The full Fermat complement has now been reduced further to its Griffiths quotient, with its algebraically trivial subgroup proved to lie in the height radical.

AR-19 and H9-T15 now give the character Selmer rank one over \(K_0=\mathbf Q(i)\), hence dimension two for the full rank-two representation there. Over this specified field, the remaining hypothesis of the finite-rank criterion is scalar-extended injectivity (AR16.1). For a further field extension its Selmer dimension must be established separately; no uniform rank bound is asserted. Thus proving the analytic input has not identified a Selmer dimension with a Chow dimension. A different route could prove the real-height inequality directly on the entire Griffiths quotient, together with \(\mathcal A_F=0\). A rational generation theorem modulo a proved real-height radical would yield semipositivity as in (AR16.4), but strict positivity would still require that radical to vanish.

No negative-height class or nonzero zero-height class in \(V_F\) has been established here. No general higher Abel--Jacobi kernel has been declared zero or placed in the real-height radical. These are the precise limits of the deductions, rather than counterexamples to the expected arithmetic positivity theorem.

## Primary locators

- Castella: https://web.math.ucsb.edu/~castella/Katz.pdf ; local `CastellaKatz.pdf/.txt`.
- Dee: https://arxiv.org/pdf/math/9901155 ; local `Dee1999.pdf/.txt`.
- BDP: https://sites.lsa.umich.edu/kartikp/wp-content/uploads/sites/1326/2024/07/BDP5-hl.pdf ; local `BDP2017.pdf/.txt`.
- Longo--Vigni--Wang: https://arxiv.org/pdf/2501.03673 ; local `LongoVigniWang2025.pdf/.txt`.
- Nekovář: https://webusers.imj-prg.fr/~jan.nekovar/pu/banff.pdf ; primary indexed text read directly, §§2.1--2.5, 3.1--3.2, and 4.1--4.4. Direct PDF transfer returned HTTP 403; no local PDF is claimed.
- Lilienfeldt: https://arxiv.org/pdf/2107.06731 ; local `LilienfeldtHeegner2024.pdf/.txt` (v3, 5 August 2022; published in *Mathematical Research Letters* 31(2), 2024).
- Achter--Casalaina-Martin--Vial: the primary Astérisque 455 (2025) volume, local `work/references/ACMV2025.pdf/.txt`, §3.2.4, equation (3.5), pp.17--18.
