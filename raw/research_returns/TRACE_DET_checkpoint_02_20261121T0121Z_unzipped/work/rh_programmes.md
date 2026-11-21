# RH programmes and the finite-field comparison

Run TRACE_DET, agent `/root/rh_programmes`, GPT-6 Astra Pro, effort not exposed, dated 2026-11-21 Europe/Berlin. These are intermediate research notes for the parent paper. Alpöge's RH and Dirichlet GRH are stipulated theorems, as required by the user. No Lean compilation or proof replay was performed here. Masullo-dependent extensions must retain their conditional label.

## Findings at a glance

| Programme | Theorem under the stipulated result | Separate structural target, or limitation |
|---|---|---|
| Weil | The full Weil quadratic positivity criterion for ζ; the corresponding Dirichlet criteria under Dirichlet GRH. | An arithmetic realization of the form by correspondences, intersection theory, or cohomology does not follow merely from its positivity. |
| Li | Every λ_n is positive, n≥1. For the designated zero-diagonal B, the paired Li coefficients are ordinary S₁ polynomial traces; proof below. | The scalar sequence does not identify Alpöge's determinants or provide a cohomology. A claim that no trace-class expression for Li coefficients exists is too broad. |
| Nyman–Beurling | The indicator of (0,1] belongs to the L²-closure of the integer-dilation fractional-part span, in Báez-Duarte's precise formulation. | No residual open question in that equivalence. Particular rates, algorithms, or arithmetic explanations require their own theorems. |
| de Branges | The shifted ξ family E_ε is Hermite–Biehler for every ε>0, hence gives de Branges spaces and their positive kernels; Suzuki's family criterion is satisfied. | Explicit arithmetic Hamiltonians / integral-kernel realizations require their own constructions. Some older sufficient shifted-inner-product positivity proposals were refuted; they are not restored by RH and are not open. |
| Connes | The ζ-sector of the RH-equivalent global cutoff trace asymptotic is true; Dirichlet sectors follow from Dirichlet GRH. | An independent direct geometric proof is a different objective. The uncut operator has not thereby acquired an ordinary trace. General-number-field Hecke sectors depend on Masullo's draft here. |
| Deninger | The spectral location predicted for the ζ and Dirichlet factors is true. A zero-coded Hilbert model can be written. | The requested functorial dynamical cohomology, cup product, duality, comparison with K-theory, and regularized determinant identification are additional structure, not a formal consequence of RH. |

“Does not follow” here means that the cited equivalence or implication establishes no such construction; it is not a claim of logical independence from RH in a formal system. Likewise “remaining structural target” does not assert that no later paper has made progress on any specially restricted version.

## PRG-WEIL: exact positivity and its sign

Write

\[
\widetilde g(s)=\int_0^\infty g(x)x^{s-1}\,dx,
\quad \overline g^{\sharp}(x)=x^{-1}\overline{g(x^{-1})},
\quad f=g*\overline g^{\sharp},
\]

with multiplicative convolution. Direct substitution gives

\[
\widetilde f(s)=\widetilde g(s)\overline{\widetilde g(1-\overline s)}.
\]

Connes–Consani's normalization of the explicit formula is

\[
\widetilde f(0)-\sum_{\rho}\widetilde f(\rho)+\widetilde f(1)
=\sum_v\mathcal W_v(f).
\]

For smooth compactly supported g with \(\widetilde g(0)=\widetilde g(1)=0\), RH therefore gives

\[
Q(g):=\sum_\rho |\widetilde g(\rho)|^2\geq0,
\qquad \sum_v\mathcal W_v(g*\overline g^\sharp)=-Q(g)\leq0.
\]

The Mellin values decrease rapidly in vertical strips, so these sums converge with multiplicity. This identifies the exact positive quadratic form and the minus sign on the local-distribution side. It is not a statement that every local summand, or a Frobenius/scaling operator, is positive. The two vanishings remove the pole contributions, analogous to the H⁰ and H² terms in the curve trace formula.

**Primary locator.** Connes–Consani, *Weil positivity and trace formula, the archimedean place*, Appendix C, **Proposition C.1**; attached TeX `weil-compo.tex`, label `mainprop`, equation `appendweilnegav`. It allows any additional finite vanishing set F disjoint from the zero set and containing {0,1}. The raw continuous theorem counter of the source must not be used to cite this as “Proposition 46.” Author PDF: <https://alainconnes.org/wp-content/uploads/Selecta.pdf>.

The corresponding Dirichlet explicit-formula positivity follows in the appropriate character sector from stipulated Dirichlet GRH. A literal substitution of ζ's pole/archimedean terms into an arbitrary character is not intended; completed L-factors and principal-character pole terms must be adjusted.

**Attached Connes–Consani theorem is stronger and already unconditional.** Their introduction **Theorem 1**, source label `mainthmintro`, states, for g supported in \([2^{-1/2},2^{1/2}]\) with multiplicative Fourier transform vanishing at i/2 and 0,

\[
W_\infty(g*g^*)\ \geq\operatorname{Tr}\bigl(\vartheta(g)\mathbf S\vartheta(g)^*\bigr)\ \geq0.
\]

Here \(\mathbf S\) projects the even L²-space onto Sonin's space of functions whose function and Fourier transform vanish on [-1,1]; \(\vartheta(\lambda)f(v)=\lambda^{-1/2}f(\lambda^{-1}v)\). The positive compressed trace is additional local operator structure. It is not an equality identifying the designated B. Their **Theorem 6.11**, source label `mainthmfine`, removes the vanishing at 0 at the cost of a correction \(c|\widehat g(0)|^2\), with 13<c<17. These are cited existing results, not re-proved here.

## PRG-LI: precise criterion and new paired trace form

**Known criterion.** X.-J. Li, *The positivity of a sequence of numbers and the Riemann hypothesis*, J. Number Theory **65** (1997), 325–333, **§1, Theorem 1**. Define

\[
\lambda_n=\frac1{(n-1)!}\left.\frac{d^n}{ds^n}
\bigl(s^{n-1}\log\xi(s)\bigr)\right|_{s=1},\qquad n\geq1.
\]

Li's theorem equates RH with nonnegativity of every coefficient. The zero expression uses the standard symmetric limiting sum

\[
\lambda_n=\sum_\rho\left[1-\left(1-\frac1\rho\right)^n\right].
\]

Primary publisher record: <https://www.sciencedirect.com/science/article/pii/S0022314X97921375>. The original article's theorem text was checked in its text reproduction at <https://paperzz.com/doc/7086946/--science-direct>; publisher full-text access returned 403. Bombieri–Lagarias, *Complements to Li's criterion for the Riemann hypothesis*, J. Number Theory **77** (1999), 274–287, **§2, Theorem 1 and its Corollary**, give the general zero-multiset criterion and explicitly recover Li's theorem. Neither full source proof was independently checked in this run.

### PRG-LI-BRIDGE: proof in the designated trace-class space

This independently verifies the parent's new bridge. Assume the parent's construction of the normal diagonal trace-class B with one entry \(\gamma_j^{-2}\) for each pair \(\{\rho_j,1-\rho_j\}\), where \(\rho_j=1/2+i\gamma_j\), and the product/zero-count background established in the parent note. Define

\[
C=B(I+B/4)^{-1},\qquad
x_j=\frac1{\gamma_j^2+1/4}=\frac1{\rho_j(1-\rho_j)}.
\]

The inverse exists: a diagonal entry of \(I+B/4\) could vanish only for \(\gamma_j^2=-1/4\), equivalently a zero at 0 or 1; neither is a zero of ξ. The diagonal entries tend to 1, so their inverses are uniformly bounded. Thus C is trace class and has eigenvalues x_j with algebraic multiplicity.

Put \(a_j=1-1/\rho_j\). The partner \(1-\rho_j\) contributes \(a_j^{-1}\), and direct algebra gives

\[
a_j+a_j^{-1}=2-x_j.
\]

The Chebyshev recurrence consequently yields

\[
a_j^n+a_j^{-n}=2T_n(1-x_j/2),
\quad P_n(x):=2-2T_n(1-x/2).
\]

Because \(P_n(0)=0\), the polynomial \(P_n(C)\) is trace class. Pair grouping respects the usual \(|\Im\rho|\leq T\) cutoff, and the paired terms are absolutely summable: \(P_n(x)=O_n(x)\) as x→0 and \(\sum_j|x_j|<\infty\). Therefore

\[
\boxed{\lambda_n=\operatorname{Tr}P_n(C)
=\operatorname{Tr}\bigl[2I-2T_n(I-C/2)\bigr],\quad n\geq1.}
\]

The expression in brackets is a single polynomial with cancellation of the constant coefficient. It does not mean subtracting two separately defined infinite traces.

Under RH all \(x_j\in(0,4)\). The spectral theorem and \(T_n(y)\in[-1,1]\) for \(y\in[-1,1]\) give \(P_n(C)\geq0\). In fact \(\lambda_n>0\): there are arbitrarily small positive x_j, and \(P_n(x)=n^2x+O_n(x^2)>0\) for sufficiently small positive x. This includes multiplicities and needs no simplicity assumption.

**Effect on intake.** SA23 §4.1(4) remains correct if narrowly read as excluding an S₁ operator with eigenvalues 1/ρ. A conclusion excluding all ordinary trace-class expressions for Li coefficients is refuted by this formula. This bridge concerns the already specified zero-diagonal B; it gives no identification of Alpöge's finite determinants with B.

## PRG-NB: an exact closure statement

Use Báez-Duarte's strengthened version to avoid switching between several Nyman–Beurling normalizations. In \(H=L^2((0,\infty),dx)\), put

\[
\rho_a(x)=\left\{\frac1{ax}\right\},\quad a\geq1,
\qquad \chi=\mathbf1_{(0,1]}.
\]

Then the theorem under stipulated RH is

\[
\boxed{\chi\in\overline{\operatorname{span}\{\rho_a:a\in\mathbb N\}}^{L^2}.}
\]

It is membership of this specific indicator in the closed span, not density of that span in all of L²(0,∞). Equivalently its distance from the increasing finite integer-dilation spans tends to zero. This mathematical assertion has no remaining RH gate. Particular optimized approximants, bounds, or a motivic explanation are different questions; the cited source itself already gives explicit approximants and a rate, so it would be incorrect to imply that the criterion lacks any constructive information.

**Primary locator.** L. Báez-Duarte, *A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis, 2*, arXiv:math/0205003v1 (1 May 2002), **Theorem 1.1**, PDF p.2: <https://arxiv.org/pdf/math/0205003>. The theorem statement and definitions were read; the proof was used as literature, not independently re-proved.

## PRG-DB: the full shifted de Branges family, with the old false conditions excluded

For every ε>0 define

\[
E_\epsilon(z)=\xi(1/2+\epsilon-iz)=\Xi(z+i\epsilon),
\qquad E_\epsilon^\#(z)=\overline{E_\epsilon(\overline z)}=\Xi(z-i\epsilon).
\]

Under RH each E_ε satisfies the Hermite–Biehler inequality

\[
|E_\epsilon(z)|>|E_\epsilon^\#(z)|\qquad(\Im z>0).
\]

Consequently each defines a de Branges Hilbert space \(\mathcal H(E_\epsilon)\) and its positive reproducing kernel. With the usual convention it is

\[
K_\epsilon(w,z)=
\frac{E_\epsilon(z)\overline{E_\epsilon(w)}-
E_\epsilon^\#(z)\overline{E_\epsilon^\#(w)}}
{2\pi i(\overline w-z)}.
\]

This is positivity of the kernel (all finite Gram matrices), not merely positivity of one numerical diagonal entry.

**Exact numbered criterion.** M. Suzuki, *A canonical system of differential equations arising from the Riemann zeta-function*, arXiv:1204.1827v2 (23 September 2016), **§1.4, Proposition 1.2**, for ω₀≥0:

\[
\zeta(s)\ne0\text{ for }\Re s>1/2+\omega_0
\iff \Theta_\omega\text{ is meromorphic inner in }\mathbb C_+
\text{ for every }\omega>\omega_0,
\]

where \(\Theta_\omega(z)=\xi(1/2-\omega-iz)/\xi(1/2+\omega-iz)\), equation (1.7). The corresponding strict modulus inequality is **(1.11)**, equivalent to **(1.3)**. Primary PDF: <https://arxiv.org/pdf/1204.1827>. This is a family criterion. The same paper explicitly notes that shifts ω≥1/2 are already available unconditionally; one such shift does not imply RH.

### Short proof of the shifted-Xi form

The usual paired canonical product under RH is \(\Xi(z)=\Xi(0)\prod_{\gamma>0}(1-z^2/\gamma^2)\), with multiplicities and locally uniform convergence. If z=x+iy, y>0, and ε>0, then for every real zero γ,

\[
|z+i\epsilon-\gamma|^2-|z-i\epsilon-\gamma|^2=4y\epsilon>0.
\]

The same holds for −γ. Thus for every partial paired product the modulus at z+iε exceeds the modulus at z−iε, factor by factor. If the denominator in the limiting ratio vanishes, the numerator is nonzero and the desired strict inequality is immediate. Otherwise the quotient of the paired products converges to the quotient of two nonzero entire values. Every paired factor has ratio >1, and fixing one paired factor bounds all later ratios below a constant >1. Hence the limiting inequality is strict. Also E_ε has no real zeros. This proves the claimed Hermite–Biehler property.

Conversely, suppose every ε>0 has this property. If Xi had a zero z₀ with Im z₀>0, choose 0<ε<Im z₀. Then E_ε(z₀−iε)=0 in the upper half-plane, contradicting the strict inequality. Real-entire conjugation symmetry rules out zeros in the lower half-plane. Thus the entire shifted family is equivalent to RH. This short proof translates the numbered source criterion to the exact Xi convention used by the parent.

**What remains a construction question.** Abstract de Branges reconstruction supplies a canonical system from a de Branges space (Suzuki §1.1, citing de Branges Theorem 41). Its bare existence should therefore not be called a remaining open problem after establishing the family. Suzuki **Theorem 2.3** constructs a specific arithmetic integral-operator Hamiltonian only for ω>1 in that source. **§5** discusses the analytic work needed to extend that explicit construction, including singular kernels and determinant differentiability, even assuming RH. A request for this prescribed arithmetic Hamiltonian or for compatibility with a Grothendieck-style cohomology is genuinely additional data; RH supplies neither its formulas nor its functoriality.

**Historical sufficient positivity is false, not open.** J. B. Conrey and X.-J. Li, *A note on some positivity conditions related to zeta and L-functions*, IMRN (2000), no.18, 929–940; arXiv:math/9812166: <https://arxiv.org/pdf/math/9812166>. Their **Theorems 1 and 2** formulate sufficient Hilbert-space positivity hypotheses; **§3.1**, equations **(3.1)–(3.4)**, show that the proposed ξ choices fail. In particular equation (3.4) records

\[
\Re\frac{\xi(1+282i)}{\xi(2+282i)}<0.
\]

A separate 80-decimal mpmath evaluation in this run returned −0.000131957293372083440713135302288618141549637246917098974942066. That repeat is a numerical check only, not an interval certificate or an independent rigorous proof. The published refutation is the cited result. Do not present those old positivity proposals as either consequences of RH or remaining open conjectures.

## PRG-CONNES: the RH-equivalent global cutoff trace formula is now true in its stated sectors

Primary source: A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Math. (N.S.) **5** (1999), 29–106; author preprint: <https://alainconnes.org/wp-content/uploads/selecta.ps-2.pdf>. Section/statement/equation numbers below are those of this author text.

The source's **§III Theorem 1 and Corollary 2** give spectral realization of critical zeros in its Sobolev-space quotient. The **local §V Theorem 3**, **semilocal §VII Theorem 4**, and the explicit formula **Appendix II Theorem 6** are established results. Do not redescribe these as newly supplied by RH.

The global cutoff statement is **§VIII, equation (16)**:

\[
\operatorname{Tr}(Q_\Lambda U(h))
=2h(1)\log'\Lambda+
\sum_v\int_{k_v^\times}'\frac{h(u^{-1})}{|1-u|}\,d^\times u+o(1),
\]

with the paper's conventions for the local principal values, cutoff Q_Λ, and

\[
2\log'\Lambda=\int_{|\lambda|\in[\Lambda^{-1},\Lambda]}d^\times\lambda.
\]

**§VIII Theorem 5** (author PDF p.42) first states the equivalence of this asymptotic and RH for all Grössencharakter in positive characteristic. Its application to number fields must not silently identify a nonexistent simultaneous exact compact-support cutoff at the real place with the function-field construction. In **§VIII equations (31)–(37)** Connes instead uses prolate spheroidal cutoffs; the space B_Λ is spanned by ψ_n with n≤4Λ², and the robustness condition is equation (36). Immediately after **equation (37)** (author PDF p.47), the source explicitly states that this gives the analogues of Lemma 1, Theorem 5 and Lemma 3. The ζ case uses the even subspace. This is the checked qualification supporting the Q-case.

Accordingly, with these actual cutoffs and test-function hypotheses, the ζ-sector of the global asymptotic follows from stipulated RH. Dirichlet character sectors follow from stipulated Dirichlet GRH, with the usual unitary-character normalization. For a general number field, the analogous conclusion for every Hecke character is conditional on Masullo's asserted theorem in this project. It would be incorrect to leave the truth of the RH-equivalent ζ cutoff asymptotic open once RH is granted.

What RH does not by itself supply is a new direct geometric proof of that trace asymptotic, an identification of its cutoffs with the cotê-1 zero-diagonal B, or an ordinary trace of the uncut scaling representation. The operators, their smoothing by h, and their cutoffs are essential. The positivity relevant to the equivalence is the positive-type Weil distribution / associated quadratic form, with the divergent bulk term subtracted as in the formula. It is not positivity of the infinitesimal scaling generator.

## PRG-DEN: Deninger's structural programme and regularized determinants

Primary source: C. Deninger, *Arithmetic geometry and analysis on foliated spaces* (23 May 2005), **§3**: <https://swc-math.github.io/dls/DLSDeninger.pdf>.

The source defines zeta-regularized determinants in **equation (2)** and proposes for the completed Dedekind zeta function in **equation (3)**

\[
\widehat\zeta_K(s)=\prod_{i=0}^2
\det_\infty\left(\frac{s-\Theta}{2\pi}\mid
H^i_{\rm dyn}(\overline{\operatorname{Spec}\mathfrak o_K},\mathbb R)\right)^{(-1)^{i+1}}.
\]

The displayed overline records the intended archimedean compactification in the source; this is a prospective dynamical space or Grothendieck site attached to the arithmetic scheme, not an already defined ordinary ℓ-adic cohomology of Spec O_K. The source explicitly discusses the expected site and sheaf immediately after (3). The H⁰ and H² terms encode the poles; H¹ should encode the nontrivial zeros with multiplicity.

The classical explicit formula is **Proposition 3.2**, and its distributional form is **equation (5)**. The conjectural cohomological distributional trace is **equation (6)**. For general schemes over Z the prospective compactly supported determinant formula is **equation (7)**, duality is **(8)**, and the proposed comparison with Adams/γ-graded motivic K-groups is **(9)**. These are stronger structural requests than the spectral assertion for degree-one L-functions.

On pp.8–9, after (3), the source assumes a cup product, trace in degree two, a positive Hodge-star pairing, and a derivation Θ commuting with star on H¹. They imply

\[
(f_1,f_2)=(\Theta f_1,f_2)+(f_1,\Theta f_2),
\quad\text{hence}\quad\Theta+\Theta^*=I
\]

in the form sense on the common domain. The source expresses this as \(\Theta=\tfrac12+A\) with A skew-symmetric. In the general weight-i formalism the star-flow compatibility is **equation (11)**; its positive pairing would force the expected real part i/2. This is a geometrically induced adjoint relation, not an ordinary Fredholm-determinant assertion for Θ.

Under stipulated RH one may of course form the tautological model \(\ell^2(Z)\), with \(A e_\rho=\gamma_\rho e_\rho\), \(\gamma_\rho\in\mathbb R\), on domain \(\{v:\sum_\rho\gamma_\rho^2|v_\rho|^2<\infty\}\), and \(\Theta=\tfrac12+iA\). The diagonal operator A is self-adjoint (the resolvents at ±i are bounded diagonal inverses), so this model has \(\Theta+\Theta^*=I\) on its domain and the required zero spectrum. This construction starts from the zeros. It supplies no functorial site, cochain theory, cup product, cycles, duality, compact-support formalism, or K-theory comparison. Nor does it turn a zeta-regularized determinant into an ordinary Fredholm determinant.

The source's **Theorem 3.3** already constructs a dynamical flow-cohomology formalism for schemes over finite fields and explicitly distinguishes the difficulty of extending it to schemes flat over Z. The new ζ/Dirichlet spectral theorem does not establish the general Hasse–Weil purity assertions for all arithmetic schemes, or the missing extension. No EGA/FGA theorem can honestly be cited as a construction of that as-yet unspecified number-field cohomology. SGA5's duality and trace formalism is a precise finite-field comparison, not that construction.

## PRG-FF: the curve analogue, purity, and a complete counterexample to positive Frobenius

Let C/F_q be a smooth proper geometrically connected curve of genus g, and ℓ∤q. Use the Frobenius convention F on \(H^i_{\mathrm{et}}(C_{\overline{\mathbb F}_q},\mathbb Q_\ell)\) for which H⁰ has eigenvalue 1 and H² has eigenvalue q. Put \(V=H^1_{\mathrm{et}}\). Then

\[
N_n:=\#C(\mathbb F_{q^n})=1+q^n-\operatorname{Tr}(F^n\mid V),
\]

\[
Z(C,T)=\frac{P_1(T)}{(1-T)(1-qT)},\qquad
P_1(T)=\det(1-TF\mid V),
\]

\[
-\log P_1(T)=\sum_{n\geq1}\frac{\operatorname{Tr}(F^n\mid V)}nT^n.
\]

These are finite-dimensional versions of trace/determinant identities; every finite-dimensional operator is trace class. The determinant also equals \(\sum_r(-T)^r\operatorname{Tr}(\bigwedge^rF)\), matching λ-operations. The trace formula is alternating across cohomological degrees, and H¹ enters with a minus sign.

Purity gives \(|\alpha|=q^{1/2}\) for each eigenvalue α on V under every complex embedding. On a complex diagonal realization of the semisimplified eigenvalue multiset, \(U=q^{-1/2}F\) is unitary; then

\[
P_1(T)=\det(1-\sqrt q\,T U).
\]

This language does not posit a canonical embedding of the entire ℓ-adic vector space into a complex Hilbert space, or a preferred positive inner product. Nor is numerical scaling by q^−1/2 a canonical half Tate twist in the ordinary ℓ-adic category: the usual Tate twists are integral. Purity is a modulus statement, and it does not make F or U positive self-adjoint.

### Complete explicit example

Take \(E/\mathbb F_3:y^2=x^3-x\). For x=0,1,2, the right side is 0, so there are three affine points and one point at infinity. The projective model is \(Y^2Z-X^3+XZ^2=0\); its X-derivative is Z², nonzero on the affine chart, and at the only infinite point [0:1:0] its Z-derivative is 1. It is smooth, and this smooth Weierstrass cubic has genus one. Hence

\[
\#E(\mathbb F_3)=4,\quad a=3+1-4=0,\quad
P_1(T)=1+3T^2.
\]

The eigenvalues of F are \(i\sqrt3,-i\sqrt3\); normalized U has eigenvalues i,−i, and \(\operatorname{Tr}(U^2)=-2\). Thus

\[
\det(1-wU)=1+w^2,
\]

whose roots are not positive real. For every nonzero scalar c the eigenvalues of cF remain opposite nonzero numbers. They cannot both be nonnegative real, so no scalar rotation or rescaling makes cF positive semidefinite. Similarity preserves the eigenvalues. This is a complete counterexample to the dictionary “purity implies positive Frobenius” and to the proposed repair by a common scalar phase.

The Poincaré pairing on H¹ is alternating and takes values in \(\mathbb Q_\ell(-1)\); F is a q-similitude for it. Mere similitude cannot replace purity either: \(D=\operatorname{diag}(1,q)\) satisfies \(D^{\mathsf T}JD=qJ\) for \(J=\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}\), yet its eigenvalue moduli are 1 and q. Polarization positivity and the unit-circle location of normalized eigenvalues are different notions from positive self-adjointness of Frobenius.

### Exact primary Grothendieck / Deligne locators

1. **SGA5, Exposé III, Corollaire 4.7**, equation **(4.7.1)**, printed p.109, is the Lefschetz–Verdier formula; **Corollaire 4.8**, on the same page, specializes it to the trace of an endomorphism and its fixed locus. Original scan: <https://library.slmath.org/nonmsri/sga/sga/5/SGA5-page-121.png>. It explicitly cites traces of complexes from **SGA6, Exposé I, §8.3**. The underlying compatibility is Exposé III **Théorème 4.4**, not a guessed “Corollary 4.4.”
2. For the precise curve statement, **SGA5, Exposé III B, Corollaire 1.3.1**, printed p.143, gives the alternating ℓ-adic cohomological trace as the sum of fixed-point stalk traces. Its preceding **Corollaire 1.3** treats constructible torsion complexes. The page explicitly states that the hypotheses apply to Frobenius. Original scan: <https://library.slmath.org/nonmsri/sga/sga/5/SGA5-page-155.png>. It points to **SGA5 XV, §2, n°3, Proposition 2**, and **SGA4½, Rapport, 3.2**; only the III B corollary itself was directly read in this run, so the cross-references should not be represented as separately read proofs.
3. Deligne, *La conjecture de Weil I*, Publ. Math. IHES **43** (1974), 273–307: **(1.5.1)** is the point-count trace formula (printed p.275); **(1.5.3)** is the formal determinant logarithm identity (p.275); **(1.5.4)** is the cohomological determinant formula for ζ (p.276); **Théorème (1.6)** gives purity for smooth projective varieties (p.276). Original PDF: <https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf>. These exact printed statements were checked. Their deep proofs were cited, not re-proved.

## Check scope and remaining integration

All new elementary proofs in this note were read from beginning to end and checked: the Li polynomial trace identity; the shifted-Xi Hermite–Biehler translation; the zero-coded adjoint relation with its domain; the F₃ curve counterexample; and the similitude counterexample. No new formal certificate is claimed. Published theorem statements and their hypotheses were checked at the locators above; this is not a full re-verification of their published proofs. The source-check and proof-check events are in `programmes_events.tsv`. Parent may identify PRG-LI-BRIDGE with its B-03, and PRG-FF with its finite-field finding, preserving both independent check events.
