# DEG_L / polarization constraints and syzygy candidates

Run `DEG_L_20261121`, author `/root`, GPT-6 Astra Pro, effort not exposed. These statements attack the replacement-object gate after S-09 and S-14. They do not assert that the required weakly equivariant object already exists.

## DER1. A strict polarization-discriminant test for a Hermite–Einstein candidate

Let `(A,H)` be an abelian variety of Weil type of dimension `2n`, `n>=2`, with `theta=c1(H)`. Let `0!=t` be a rational Weil class, so `theta t=0`. Let `E` be a holomorphic vector bundle of positive rank `r`, let `B` be a rational algebraic divisor class, and assume

\[
 w=e^B\operatorname{ch}(E)=P(\theta)+\lambda t,\qquad
 P(x)=r+p_1x+p_2x^2+\cdots,\quad \lambda\ne0.
\]

If `E` admits a Hermite–Einstein metric for the polarization, then necessarily

\[
 p_1^2-2rp_2>0.
\tag{DER1}
\]

In particular a single exponential `P(x)=r e^{ax}` is impossible. More generally any finite sum `P(x)=sum_i r_i e^{a_i x}` with positive rational `r_i` is impossible. These are obstructions to this Hermite–Einstein route, not claims that every semiregular bundle is Hermite–Einstein.

**Proof.** Write `Delta(E)=c1(E)^2-2r ch2(E)=2r c2(E)-(r-1)c1(E)^2`. Multiplication of a Chern character by `e^B` leaves this expression invariant: its first two components become `c1+rB` and `ch2+B c1+rB^2/2`, and the extra terms cancel. If `n=2`, the Weil contribution to `ch2` is `lambda t`, whose product with `theta^{2n-2}` vanishes because `theta t=0`. If `n>2`, there is no Weil contribution to `ch2`. Therefore

\[
 \int_A\Delta(E)\theta^{2n-2}
 =(p_1^2-2rp_2)\int_A\theta^{2n}.
\]

Kobayashi, *Differential Geometry of Complex Vector Bundles*, Theorem 4.4.7, printed p.106 in the 2013 retypesetting of the 1987 book, says that this number is nonnegative and that equality for an Einstein–Hermitian bundle forces projective flatness. The full statement and its curvature proof were read in the official Mathematical Society of Japan PDF. Projective flatness gives `ch(E)=r exp(c1(E)/r)`, by the same book, equation (2.3.3), printed p.41. Thus in the equality case

\[
 w=r\exp(B+c_1(E)/r)
   =r\exp((p_1/r)\theta),
\]

where the second identity follows by comparing degree-two components of `w`. Its Weil component is zero, contradicting `lambda t!=0`. Hence the inequality is strict.

For a sum of exponentials the same coefficient is

\[
 p_1^2-2rp_2
 =-\sum_{i<j}r_i r_j(a_i-a_j)^2\le0.
\]

This contradicts the strict inequality, including the case in which all slopes coincide. QED.

**Exact primary source.** <https://www.mathsoc.jp/assets/pdf/publications/pubmsj/Vol15.pdf>; Theorem4.4.7, PDF page116 / printed p106, and equation2.3.3, PDF page51 / printed p41. This is a cited curvature theorem applied to the particular character, not a new proof of the Kobayashi–Lübke inequality.

## DER2. The globally generated syzygy construction preserves a full trace kernel

Let `A` be an abelian variety of dimension `g>=3`. Let `E` be a globally generated vector bundle with `H^i(A,E)=0` for all `i>0`. Put `V=H^0(A,E)` and let

\[
 0\longrightarrow M_E\longrightarrow V\otimes\mathcal O_A
 \longrightarrow E\longrightarrow0
\tag{DER2a}
\]

be the evaluation sequence. Then the Fourier–Mukai functor with kernel the ideal of the diagonal induces an injection

\[
 \operatorname{Ext}^2_A(E,E)
 \hookrightarrow \operatorname{Ext}^2_A(M_E,M_E).
\tag{DER2b}
\]

Under this injection, the kernel of the full Buchweitz–Flenner semiregularity map goes into the corresponding kernel for `M_E`. Consequently, if `E` is not fully semiregular, neither is `M_E`.

**Proof.** Let `Psi=Phi_{I_Delta}` on `Dperf(A)`. The exact sequence of diagonal kernels induces the functorial distinguished triangle

\[
 \Psi(E)\longrightarrow R\Gamma(A,E)\otimes\mathcal O_A
 \longrightarrow E\xrightarrow{\eta_E}\Psi(E)[1].
\]

The vanishing hypothesis identifies `RΓ(E)` with `V` in degree zero; surjectivity of evaluation identifies `Psi(E)` with the vector bundle `M_E` in degree zero. Serre duality and `K_A=O_A` give

\[
 \operatorname{Ext}^2(E,\mathcal O_A)
 =H^2(E^\vee)
 \simeq H^{g-2}(E)^*=0,
\]

since `g-2>0`. Apply `Hom(E,-)` to the triangle shifted by two. Because `Hom(E,V tensor O_A[2])=0`, composition with `eta_E[2]` injects `Ext²(E,E)` into `Hom(E,Psi(E)[3])`.

If `u:E -> E[2]` has `Psi(u)=0`, naturality of `eta` gives

\[
 \eta_E[2]\circ u=\Psi(u)[1]\circ\eta_E=0.
\]

The preceding injection implies `u=0`. This proves (DER2b).

The full categorical semiregularity morphism is natural for a functor between smooth proper categories: Perry, *The semiregularity theorem for equivariant noncommutative varieties*, arXiv2604.00511v2, Remark2.3, printed p.5. Remark2.5 on that page identifies it with the Buchweitz–Flenner map under HKR. Hence

\[
 \sigma_{M_E}(\Psi(u))=\Psi_*\sigma_E(u).
\]

A nonzero element in `ker sigma_E` therefore has a nonzero image in `ker sigma_{M_E}`. No assertion that `Psi` is an equivalence is used or needed. QED.

**Scope.** This concerns the full object trace map. A map-level obstruction kernel `ker tau_f` cannot be inserted unless its nonzero image in `Ext²(Rf_*O,Rf_*O)` has separately been proved. It also does not rule out unrelated equivariant structures which eliminate the original invariant kernel. For a finite translation action preserving all displayed data, the same argument is equivariant and preserves a kernel already present in the invariant category; no assertion is made for arbitrary tensor actions, which need not commute with the evaluation functor.

## DER3. Opposite exponential coefficients fix the numerical test but not this trace kernel

Suppose an integral `K_0` class with character `N t` has been realized, as in S-16, by a vector bundle `E_0` with

\[
 \operatorname{ch}(E_0)=R e^{a\theta}+N t,
 \qquad R>0,\quad a\in\mathbf Z.
\]

Assume `E_0` has an established nonzero full semiregularity kernel. This hypothesis holds in the precise Q(i) fourfold situation of S-13; it is not asserted for every higher-dimensional Weil family.

For every sufficiently large positive integer `q`, write `b=a+q`, set `E=E_0 tensor H^q`, and let `M=h^0(A,E)`. Then the evaluation kernel is a vector bundle of positive rank `M-R`, with

\[
 \operatorname{ch}(M_E)
 =M-R e^{b\theta}-N t.
\tag{DER3a}
\]

Its polynomial character has strictly positive discriminant coefficient

\[
 p_1^2-2(M-R)p_2=MRb^2>0,
\tag{DER3b}
\]

but `M_E` is not fully semiregular.

**Proof.** Choose `q` so that `E` is globally generated, has no higher cohomology, `b!=0`, and `M>R`. Global generation and higher-cohomology vanishing hold for large twists by Stacks Project, Proposition 28.27.13(7), tag `01Q3`, and Lemma 30.16.1(4), tag `0B5T`, respectively; the Hilbert polynomial has positive leading coefficient, giving `M>R`. Since `theta t=0`, multiplication by `e^{q theta}` fixes `t`, so `ch(E)=R e^{b theta}+Nt`. Taking the character of the evaluation sequence gives (DER3a). Here `p1=-Rb` and `p2=-Rb²/2`; direct substitution gives (DER3b).

Tensoring by a line bundle is an equivalence, so S-10, or Perry Remarks2.3 and2.5 applied in both directions, preserves the nonzero full trace kernel of `E_0`. DER2 then preserves a nonzero kernel in `M_E`. Thus this canonical two-exponential construction passes the necessary numerical inequality while failing the desired trace injectivity. QED.

**Consequences for the next approach.** The polarization polynomial cannot be chosen solely to satisfy a positivity inequality. A successful replacement must change the relevant obstruction representation or its invariant trace kernel. The tensor–determinant construction after a successful deformation is different: it is used to produce effective cycles and does not require the resulting bundle to be semiregular.


## DER4. Adams untwisting removes the virtual-rank condition

Let `A -> S` be a smooth projective family of complex abelian varieties of dimension `2n`, with `S` smooth and irreducible and a relatively very ample line bundle `H`. Let `theta=c1(H)` be the relative polarization class and `0!=t` a global flat Weil class, with `theta t=0`. Suppose a point `0` has an object and actual finite target-group action satisfying Perry Theorem 1.2, with

\[
 e^{B_0}\operatorname{ch}(E_0)=P(\theta_0)+\lambda t_0,
 \qquad \lambda\ne0.
\tag{DER4a}
\]

The complete displayed character is required to remain Hodge. There is **no restriction on the virtual rank of `E_0`**. Then the conclusion can be strengthened from existence of algebraic classes to a concrete construction of a fixed signed-cycle bound, as follows.

After passage to an etale neighborhood `U -> S`, let `mu_M` be the band of a Kummer gerbe used in Perry's proof, enlarged as there if necessary. There is an ordinary integral perfect `K_0` class `xi` on `A_U` whose central-fibre character is

\[
 \operatorname{ch}(\xi_0)=P(M\theta_0)+M^n\lambda t_0.
\tag{DER4b}
\]

Choose a finite bundle presentation and integers `R,m,a,k` by the construction below. Write

\[
 Q(x)=e^{kx}\bigl(P(Mx)+R e^{-mx}+a\bigr),
 \qquad \mu=M^n\lambda,
\]

and define

\[
 C_n=[u^n]\exp\!\left(
 \sum_{j=1}^{n}(-1)^{j-1}(j-1)![x^j]Q(x)u^j\right),
 \qquad \beta=(-1)^{n-1}(n-1)!\mu.
\tag{DER4c}
\]

Let `v=integral_A theta^{2n}`. For an integer `d>=1` clearing the denominators of `C_n` and `beta`, put

\[
 N=|d\beta|,\qquad D=dC_n v.
\tag{DER4d}
\]

The construction gives `C_n>0`, `N` a positive integer, and effective integral cycles of degree at most `D` representing `N t` as their difference on every fibre of `S`. Thus

\[
 c_t(s)\le \max\{1,N,\lceil D\rceil\}\qquad(s\in S(\mathbf C)).
\tag{DER4e}
\]

These numbers are explicit once the successful local deformation and its finite bundle presentation and generation twists are specified. The assertion does not bound those choices in terms of the original 032 level.

**Proof: the gerbe and the Adams operation.** Perry, arXiv2604.00511v2, section6.2, proofs of Theorems1.1 and1.2, printed pp26--27, constructs the deformation using a `mu_M` gerbe `pi:mathcal A -> A_U` whose central class is the reduction of `M B_0` modulo `M`. The integer may be increased by a multiple when extending the group action, as specified in Corollary5.17 and the proof on p27. Replacing the initial integer by this multiple does not change `B_0`. The category of twisted perfect complexes is explicitly the category of weight-one perfect complexes on this gerbe (section3.2, pp7--8). Hence the resulting object `F` is of weight one. Under the central trivialization specified by the algebraic B-field, the gerbe is the gerbe of `M`th roots of a line bundle `L_0` with `c_1(L_0)=M B_0`; its tautological root `T` has `T^M=pi^*L_0`, and

\[
 F_0\simeq \pi^*E_0\otimes T.
\]

The sign is fixed by the convention that the weight-one Chern character under the rational cohomology identification is `exp(B_0) ch(E_0)`, as in Perry Theorem3.2(2), equation(3.3), p9.

For a perfect complex in characteristic zero, each derived exterior power is again perfect. One can form it as the alternating idempotent summand of a derived tensor power; these summands exist in the idempotent-complete perfect category. Exterior powers of a weight-one object have weight equal to their exterior exponent. Newton's recursion

\[
 \psi^j(x)=\lambda^1(x)\psi^{j-1}(x)
 -\lambda^2(x)\psi^{j-2}(x)+\cdots
 +(-1)^{j-2}\lambda^{j-1}(x)\psi^1(x)
 +(-1)^{j-1}j\lambda^j(x)
\tag{DER4f}
\]

therefore writes `psi^M([F])` as an integral finite virtual sum of perfect objects, every term of weight `M`, hence weight zero modulo `M`. A weight-zero perfect complex on a tame `mu_M` gerbe descends uniquely to the base: this is checked etale-locally on the neutral gerbe, where a weight-zero representation is the trivial representation tensored with a complex on the base; the identifications descend. Applying this to each term defines the ordinary integral class `xi` on `A_U`.

The Newton operations are additive and multiplicative on `K_0`, and on a line bundle satisfy `psi^M(L)=L^M`. Their formal source is SGA6, ExposeV, Appendix7.1, equation(7.1.1), printed pp360--361, and Proposition7.5, pp362--364 (SLMath original scan, PDF pages367--371). The weighted homogeneity in (DER4f) is also explicitly noted in7.1. In the present characteristic-zero perfect setting, the exterior-power filtration of a triangle supplies the same lambda identities, so the recursion is compatible with passing to the perfect `K_0` group. On a split bundle with Chern roots `x_i`, the Chern character of its Adams operation is `sum_i exp(Mx_i)`. The splitting principle, and additivity for a difference of bundles, consequently give `ch_j(psi^M x)=M^j ch_j(x)`.

At the central fibre we may compute before descending:

\[
 \psi^M([F_0])
 =\pi^*\psi^M([E_0])\,[T]^M
 =\pi^*\bigl(\psi^M([E_0])\,[L_0]\bigr).
\]

Thus $\xi_0=\psi^M(E_0)\otimes L_0$. Its Chern character is $\exp(MB_0)\operatorname{ch}(\psi^M(E_0))$, which is the degreewise operation multiplying the degree-$2j$ component of $\exp(B_0)\operatorname{ch}(E_0)$ by $M^j$. Applying it to (DER4a) gives (DER4b). All objects and Chern classes are defined over $U$; their fibre classes are flat, so this character formula persists on the connected neighborhood.

**Proof: an ordinary bundle and its effective Chern cycle.** Shrink `U` to a smooth affine neighborhood. The total space `A_U` is smooth and quasi-projective and has the resolution property. Stacks Project Lemma36.37.2, tag0F8F, gives a bounded finite locally free presentation of every perfect object. Grouping its even and odd terms writes `xi=[V^+]-[V^-]` for actual vector bundles. Choose `m` so that `V^- tensor H^m` is globally generated, and a finite surjection `O^R -> V^- tensor H^m`. Its kernel `K` is locally free because its quotient is locally free. Hence

\[
 [V^+\oplus (K\otimes H^{-m})]
 =\xi+R[H^{-m}].
\]

Add `a>=0` trivial line bundles so that the resulting bundle has rank at least `n`, then choose `k` so that its tensor product `V` with `H^k` is globally generated and has no higher fibre cohomology on a neighborhood. The relevant standard facts are Stacks Project Proposition28.27.13(7), tag01Q3, and Lemma30.16.1(4), tag0B5T, together with cohomology and base change; all twists and ranks are finite fixed integers. Since `theta t=0`, the resulting character is

\[
 \operatorname{ch}(V_s)=Q(\theta_s)+\mu t_s.
\]

The identity between total Chern class and Chern character is

\[
 c_u(V_s)=\exp\left(\sum_{j\ge1}(-1)^{j-1}(j-1)!
 \operatorname{ch}_j(V_s)u^j\right).
\]

Only the linear occurrence of `t_s` contributes in codimension `n`; therefore

\[
 c_n(V_s)=C_n\theta_s^n+\beta t_s.
\tag{DER4g}
\]

For a globally generated bundle of rank `q>=n`, the degeneracy cycle of `q-n+1` sufficiently general sections is effective of codimension `n` and represents `c_n(V_s)`; if empty its class is zero. This is Fulton, Intersection Theory, second edition, Theorem14.4, p254, and Examples14.4.2--3, pp255--256. Call that cycle `Z_s`. Its degree is `C_n v`, because `theta_s t_s=0`. Its Weil component is the nonzero class `beta t_s`, so it is not the zero cycle and `C_n>0`. Let `W_s` be an intersection of `n` sufficiently general polarization hyperplanes, representing `theta_s^n`, of degree `v`. Then

\[
 d\beta t_s=\operatorname{cl}(dZ_s)
             -\operatorname{cl}(dC_n W_s),
\]

and both effective cycles have degree `dC_n v`. Reversing signs if `beta<0` gives (DER4d)--(DER4e) on the nonempty etale image of this neighborhood. That image is Zariski open and dense in `S`. Use the fixed-multiplier version of the closed-locus argument in the proof of DIV1: retain this one `N` and degree cutoff `D` in its finite projective parameter spaces, instead of taking the finite union over multipliers. Its closed image contains the dense open set and is all of `S`, preserving these same `N,D`. This completes the proof.

**What was removed.** Tensor--determinant untwisting requires nonzero virtual rank and gives a factor `r^r`. Adams untwisting uses the torsion order of the explicitly constructed gerbe, preserves the first nonzero Weil component even in virtual rank zero, and gives the factor `M^n`. It takes place after deformation; no semiregularity assertion about the new bundle is needed. The remaining hypothesis is existence of the original weakly equivariant semiregular object with its complete Hodge-compatible character.

## Check state

Root read DER1–DER4 in full after writing. The semiregularity agent independently read all four proofs and checked the central gerbe sign, Adams weight/descent and effective Chern cycle. Its requests for the exact bundle-resolution locator and fixed-N specialization argument are incorporated above. Recorded events distinguish these readings from formal verification. No assertion here proves existence of a new semiregular object.
