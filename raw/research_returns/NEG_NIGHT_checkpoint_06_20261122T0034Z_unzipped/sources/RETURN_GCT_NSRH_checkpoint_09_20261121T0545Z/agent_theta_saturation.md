# A precise obstruction to a homogeneous ordinary-interlacing model

Author/checker: `/root/rectangular_and_theta`, GPT-6 Astra Pro; inherited effort not exposed. Prepared 2026-11-21 Europe/Berlin, around 00:35–00:45 (UTC 2026-11-20). This is a new deduction for the run, not a priority claim. The elementary proof was checked by the author and subsequently received a complete fresh check by `/root/gct_statements`; see `REVIEW_THETA_SATURATION_GCT.md`, outcome PASS. The source formula used below was read in the attached TeX and matched to the numbered primary PDF.

## 1. Precise proposition

Let \(L\) be a lattice, and let \(\mathcal D\subset L\) be a set of admissible integral labels closed under multiplication by positive integers. Fix a nonnegative integer \(s\) and a finite list of constraints indexed by \(e\). For each constraint choose \(i_e,j_e\in\{0,1,\ldots,s\}\), and an integral-valued function \(b_e:\mathcal D\to\mathbf Z\) such that

\[
b_e(Nu)=N b_e(u)\qquad(N\ge1).
\]

Thus an integral linear endpoint map is sufficient. A rational linear endpoint map is also allowed **only when its values on the chosen admissible label lattice are integral**. Put \(x_0=0\) and

\[
P(u)=\{(x_1,\ldots,x_s)\in\mathbf R^s:
x_{i_e}-x_{j_e}\le b_e(u)\text{ for every }e\}.
\]

Assume these sets are bounded when their lattice-point counts are used, and write

\[
h(u)=\#(P(u)\cap\mathbf Z^s).
\]

**Proposition.** For every \(u\in\mathcal D\) and \(N\ge1\),

\[
h(Nu)>0\quad\Longleftrightarrow\quad h(u)>0.
\]

In particular, a uniform exact multiplicity model of this form has saturated support on the specified label lattice in the explicit sense displayed above; this is not VI's residue-wise definition of a strictly saturated quasipolynomial. The conclusion also holds for a fixed finite sum of such counts. Ordinary order/interlacing inequalities, with integral fixed endpoint rows, are a special case: inequalities between internal entries have right side zero, and endpoint bounds are inequalities against the coordinate \(x_0=0\).

### Full proof

The homogeneity assumption gives \(P(Nu)=N P(u)\). If \(x\in P(u)\), set \(y_i=\lfloor x_i\rfloor\) for every \(i\), including \(y_0=0\). An inequality \(x_i-x_j\le b\) with \(b\in\mathbf Z\) implies

\[
\lfloor x_i\rfloor
\le\lfloor x_j+b\rfloor
=\lfloor x_j\rfloor+b.
\]

Consequently \(y\in P(u)\cap\mathbf Z^s\). Thus real feasibility implies integral feasibility. If \(h(Nu)>0\), choose \(z\in P(Nu)\cap\mathbf Z^s\); then \(z/N\in P(u)\), and flooring this vector produces a lattice point of \(P(u)\). Conversely, an integral \(y\in P(u)\) gives \(Ny\in P(Nu)\cap\mathbf Z^s\). For a finite sum, positivity means that at least one summand is positive, and the same summand works in the reverse direction. This proves all assertions. Boundedness is needed for a finite counting function, not for the feasibility argument. ∎

### Scope restrictions that are part of the statement

The dimension and constraint list are fixed along the ray. There are no extra congruences, sum constraints, arbitrary linear inequalities, endpoint-dependent restrictions on the list of admissible cases, or lattice changes. A changing chain length, affine shifts in highest weights, or nonhomogeneous endpoint map is outside the proposition. It is not a theorem that GGP branching or theta lifting always has the displayed form.

Integral endpoint values are essential. The homogeneous family \(P(d)=\{d/2\}\) has rational endpoints and has a lattice point exactly for even \(d\). Equivalently it is cut out by \(2z=d\); the coefficient 2 cannot be treated as an ordinary difference constraint with integral endpoint data. Extra integer-coordinate equations such as \(x+y=1\) combined with \(x=y\) also invalidate coordinatewise flooring.

## 2. Exact Kronecker obstruction already inside two-row rectangles

Let \(u=((1,1),(1,1),(1,1))\). Then

\[
g(u)=0,\qquad g(2u)=g((2,2),(2,2),(2,2))=1.
\]

For the first equality, the Specht module \([(1,1)]\) is the sign character of \(S_2\). Its triple tensor product is sign, so it has no invariant vector. For the second equality, \(S_4\) acts on the three pairings of four letters. The permutation character minus the trivial character is

\[
\chi=(2,0,2,-1,0)
\]

on the cycle types \((1^4),(2,1,1),(2,2),(3,1),(4)\), whose class sizes are \(1,6,3,8,6\). Its character norm is

\[
\frac{1}{24}(4+3\cdot4+8\cdot1)=1,
\]

so it is the two-dimensional irreducible \([(2,2)]\). Directly,

\[
\chi^2=\mathbf1+\operatorname{sgn}+\chi.
\]

Therefore the tensor square contains \([(2,2)]\) exactly once, proving the claimed Kronecker coefficient. Equivalently, the invariant character average is \((8+3\cdot8-8)/24=1\).

**Corollary.** No uniform homogeneous integral difference/order-polytope model as in the proposition can count all two-row rectangular Kronecker coefficients exactly. In particular an endpoint-preserving identification of the whole family with ordinary integral interlacing arrays cannot exist under those hypotheses.

This corollary does not rule out a positive rule, a rational polytope, a polytope in a specified sublattice, or a general functor chain as in F13. It does not contradict revised VI's saturation-index formulation: the distinction is made explicit below. In particular it does not change the status of the known two-row positive crystal rule. The small-height example lies outside IP Theorem 1.10(b)'s large-parameter region; it does not exclude a model restricted only to that asymptotic region.

## 3. The existing crystal formula retains precisely the missing parity data

The attached revised IV contains the needed positive formula explicitly, not merely a conjectural basis. The following locators were checked in the attached file

`sources/LIT_Mulmuley_GCT_IV_nonstandard_quantum_group_Kronecker/Apr13KroneckerGCT4.tex`

and the primary PDF at `https://arxiv.org/pdf/cs/0703110`, whose first page identifies version 4, 6 June 2013.

| Locator | Exact relevant content |
|---|---|
| §2.3, source lines 1534–1536; printed p. 17 | \([n_l,\ldots,n_1]\) denotes the partition with \(n_i\) columns of height \(i\). Thus \((d,d)=[d,0]\), and as a four-row label it is \([0,0,d,0]\). |
| §18.1, equations (163)–(164), printed p. 124; source lines 7452–7466 | A nonnegative sum over invariant-removal indices \(i_1,i_2,i_3\); residual column numbers are \(n_j-2i_j\), while \(\widehat l_2=l_2-i_1-2i_2-3i_3-2n_4\), and similarly for \(m_2\). |
| Theorem 18.2, printed pp. 124–125; source lines 7470–7517 | Each of five types is 0 or 1, determined by a line-segment condition, the congruence \(l_1\equiv m_1\equiv r\pmod 2\), and the stated activation inequalities. |
| §18.3, equation (172), printed p. 128; source lines 7778–7793 | Positive two-row-rectangle formula, rephrasing Brown–van Willigenburg–Zabrocki and reproduced from Theorem 18.2; its indicators require specified quantities to be even and nonnegative. |
| Proposition 18.5, printed p. 128; source lines 7806–7827 | Compact generating-function version for \(\lambda=[d,0]\). |
| Proposition 18.6, equation (180), printed p. 129; source lines 7831–7840 | For \(l_1=m_1=0\), odd \(n_1\) or odd \(n_2\) is among the exact vanishing conditions. |

The full rectangle ray can be evaluated from equation (172) with no additional invariant-theory input. Define, as in that source,

\[
G_{d,\nu}(x)=\sum_{\mu\vdash_2 2d}g_{(d,d),\mu,\nu}x^{m_1},
\qquad \mu=[m_2,m_1].
\]

The source expresses \(G_{d,\nu}(x^{1/2})\) as a sum over \(0\le k\le d\), with \(k=m_1/2\). Its constant term, corresponding to \(\mu=(d,d)\), has only \(k=0\), and then only \(j=0\) in the first inner sum. The second inner sum is empty. Its indicator is

\[
\chi\{n_3,n_2,n_1\text{ are even and nonnegative}\}.
\]

For \(\nu=(d,d)=[0,0,d,0]\), this gives the exact existing-formula consequence

\[
g((d,d),(d,d),(d,d))=
\begin{cases}1,&d\text{ even},\\0,&d\text{ odd}.
\end{cases}
\]

This calculation is also visible in the invariant-removal formula: on the rectangle ray \(n_1=n_3=n_4=l_1=m_1=0\), the only possible surviving term removes all height-two columns in pairs, requiring \(i_2=d/2\) to be integral. Thus a faithful transfer must retain this arithmetic condition or an equivalent representation-theoretic datum. Simply retaining the real line segment loses it.

### Exact rational Ehrhart model on this ray

For the fixed rational polytope \(P=\{1/2\}\subset\mathbf R\),

\[
\#(dP\cap\mathbf Z)=\chi\{d\text{ even}\}
=g((d,d)^3).
\]

Hence this particular ray already has an exact rational Ehrhart model, with constant dimension and denominator two. Its rational feasibility is automatic, while its integral feasibility remembers parity. This is a consequence of the established two-row formula, **not a new consequence of Reynolds/Gram positivity or Alpöge's theta steps**, and it is no model for arbitrary rectangular height, arbitrary two-row triples, or closure multiplicities. It demonstrates why failure of support saturation on the specified label lattice and existence of a rational Ehrhart model are compatible. In fact, VI Definition 1.2.4 (printed p. 14; attached source label `dintrosat`, lines 813–818) calls a quasipolynomial strictly saturated when every nonzero residue polynomial is positive at all positive arguments, allowing identically zero residue polynomials. Here the two residue polynomials are 1 and 0, so its VI saturation index is **zero**. The example does not violate that definition.

The theta gate can now be stated more precisely: in addition to proving the functor and endpoint identification of F13, a proposal must recover the correct weight lattice, congruence conditions and invariant-removal data. It is not enough to show that its real parameters obey ordinary interlacing. The source does not identify its parity data with a specified Alpöge/GGP central character or local sign, so no such further identification is claimed.

## 4. Grothendieck-language restatement

Let \(V,W\) be two-dimensional rational vector spaces and let

\[
\rho:\mathrm{GL}(V)\times\mathrm{GL}(W)\longrightarrow
\mathrm{GL}(V\otimes W)
\]

be the tensor representation, defined already over \(\mathbf Z\). Over \(\mathbf Q\) the representation categories are semisimple. Restriction induces a positive homomorphism of representation Grothendieck rings,

\[
\rho^*:K_0\operatorname{Rep}_{\mathbf Q}(\mathrm{GL}_4)
\longrightarrow K_0\operatorname{Rep}_{\mathbf Q}(\mathrm{GL}_2\times\mathrm{GL}_2).
\]

The coefficient of the actual simple class
\([\det_V^d\boxtimes\det_W^d]\) in
\(\rho^*[S_{(d,d)}(V\otimes W)]\) is \(g((d,d)^3)\). It vanishes at \(d=1\) and equals one at \(d=2\), despite the positivity of every restriction matrix. At \(d=1\), the familiar identity

\[
\bigwedge^2(V\otimes W)
\simeq(\operatorname{Sym}^2V\otimes\bigwedge^2W)
\oplus(\bigwedge^2V\otimes\operatorname{Sym}^2W)
\]

also exhibits the vanishing directly. Thus an effective representation-\(K_0\) map does not make its highest-weight support saturated. The extra conclusion follows only from a specific homogeneous integral difference-array description of its entries. Scaling a highest weight is not, by itself, an exact functor whose existence is supplied by the positive \(K_0\) monoid.

An exact-functor chain with 0/1 branching remains a sufficient path-count framework, as proved in F13. The proposition above says that a chain with the additional pure-interlacing and homogeneous-integral endpoint hypotheses cannot realize this full Kronecker family. A suitable chain retaining congruences or other non-difference constraints is not excluded. No Frobenius, purity, or motive is needed for this obstruction; it is an exact statement in characteristic-zero representation theory and integral convex geometry.

## 5. Proof-check record

- **Author proof check, difference constraints:** checked both implications, the negative-coordinate case via the exact identity \(\lfloor x_j+b\rfloor=\lfloor x_j\rfloor+b\), the anchored coordinate \(x_0=0\), homogeneous scaling, and the boundedness qualification. No total-unimodularity theorem is assumed.
- **Author exact character check:** class sizes and all five character values explicitly used; the \(S_2\) sign computation and \(S_4\) invariant average give 0 and 1. This does not rely on the optional Murnaghan–Nakayama computation.
- **Source applicability check:** read the attached revised IV §18 formula and proof; matched Theorem 18.2, equations (163), (164), (172), Propositions 18.5–18.6 to the primary PDF. No independent re-proof of the full crystal theorem is claimed.
- **Specialization check:** substituted \(n_1=n_3=n_4=m_1=0,n_2=d\) into the constant term of (172); one indicator remains and gives parity. Independently checked consistency at \(d=1,2\) by characters.
- **Scope check:** no claim of universal GGP saturation, VI-strict-saturation failure from the parity example, a new general polytope rule, or PH1 from an abstract functor chain.


**Subsequent independent review:** `/root/gct_statements` read the entire note, independently recomputed the S2/S4 character example, checked the IV constant-term specialization and VI definition directly, and reported PASS in `REVIEW_THETA_SATURATION_GCT.md`. The review did not re-prove the complete cited two-row crystal theorem.
