# Independent review of NC03–NC04

Reviewer: /root/noncm_gate, GPT-6 Astra Pro, effort level not exposed.

Date: 2026-11-21T04:28:26+01:00

Reviewed file: ZETA_NEXT_work/cm/findings.tex.

SHA-256 of reviewed file: e2e51b9640108f26ae5ee5d6c7bf1bc6703dea8f35c435a5b67a5db68addb21c

## Conclusion and scope

**PASS: no mathematical gap found in NC03 or NC04, in their stated scope.** I read both complete theorem statements and proofs, including the definitions of their constants, and independently reconstructed the ideal-class count, the descent and endomorphism arguments, and every exponent and inequality below. This is an independent review by a different agent from the author, logged as a **targeted proof check**. It is not a claim to have independently reproved the cited literature.

NC01 and NC02 were accepted as named inputs, as requested. I checked their precise forms where substituted but did not re-audit their analytic proofs. This review inherits their explicitly stated dependence on the supplied Alpöge theorem. It introduces no Masullo hypothesis and no general individual Colmez conjecture.

No changes were made to cm/findings.tex. Two possible clarifications are recorded at the end; neither changes a bound or repairs a mathematical gap.

## Primary statements inspected

All the following were read from the primary PDFs or their extracted text in cm/sources.

| Source | Exact part inspected | Point verified |
|---|---|---|
| Tsimerman, The André–Oort conjecture for \(\mathcal A_g\), Ann. Math. 187 (2018) | §2.2 and argument preceding Proposition 2.2, printed p. 382 | \(|S(E,\Phi)|=h_E\); primitive types have endomorphism ring \(\mathcal O_E\); isogenies from a fixed object correspond to integral ideals, with degree equal to ideal norm. |
| Same | Lemma 4.1 and its entire short proof, printed p. 384 | A field defining the variety and all its endomorphisms and polarizations exists with relative degree at most \(2\cdot3^{4g^2}\). |
| Gaudron–Rémond, Polarisations et isogénies, Duke Math. J. 163 (2014) | Constants, printed p. 2058; pair-of-isogenies convention, p. 2059; Theorem 1.4, p. 2060 | \(\alpha=2^{10}g^3\), \(B=(14g)^{64g^2}\), height exponent \(2\), and a bound in each direction using the first input's height. The field-degree parameter is that of a field defining both varieties. |
| Same | Supplied primary-page image gr-constants.png | Visually checked the exponents and original Faltings-height normalization. |
| Rémond, Variétés abéliennes et ordres maximaux | Opening convention and Theorems 1.1–1.2, author preprint pp. 1–2 | All morphisms and varieties are over the same fixed field. Maximal-order replacement needs no field extension. A subvariety of a variety with maximal endomorphism order is a direct factor and has maximal endomorphism order. |
| Same | Proposition 3.1 and proof of Theorem 1.2, preprint pp. 6–7 | The direct-factor statement gives actual integral idempotents. |
| Same | Paragraph preceding Lemma 7.5, preprint pp. 17–18 | A CM variety attached to a degree-\(2r\) field is simple exactly when its type is primitive; then its rational endomorphism algebra is that field. |
| Gaudron–Rémond, Théorème des périodes et degrés minimaux d’isogénies | §2.3, printed pp. 351–352 | Height normalizations and additivity of stable Faltings height on actual products. |

Files inspected: tsimerman-2018.txt, gaudron-remond-polarisations.txt, remond-2017-maximal-orders.txt, gaudron-remond-2014.txt, and gr-constants.png. Literature statements were checked for applicability; the long GR and Rémond proofs were not independently re-proved.

## NC03 reconstruction

### Field of definition and ideal classes

Geometric simplicity and the full endomorphism field imply a primitive CM type \(\Phi\). Since every element of \(\mathcal O_E\) acts over \(K\), the common ideal kernel \(A[I]\) is a finite subgroup scheme over \(K\). Its quotient, the quotient isogeny and the induced \(\mathcal O_E\)-action are over \(K\). Individual points of \(A[I]\) need not be \(K\)-rational. No additional reflex-field or ray-class-field extension is required for this construction.

Tsimerman §2.2 gives \(h_E\) isomorphism classes of CM pairs and says every one arises from an integral ideal.

### Automatic \(E\)-linearity

Fix one \(E\)-linear isogeny \(f_0:A\to A_I\). Its rational inverse gives
\[
\operatorname{Hom}^0(A,A_I)=f_0\operatorname{End}^0(A)=f_0E.
\]
For \(f=f_0t\), commutativity of \(E\) implies
\[
fe=f_0te=f_0et=e_I f.
\]
Thus every actual isogeny supplied by GR respects the fixed actions. There is no unproved assumption that GR preserves CM structures. This argument would fail with a noncommutative endomorphism algebra or imprimitive type; neither occurs here.

It also prevents losing ideal classes on forgetting the action: any isomorphism between the underlying varieties for these transported actions is automatically \(E\)-linear.

### Correct direction of counting

GR applies over the given \(K\), because both varieties and a quotient isogeny already exist there. Its first input is the fixed \(A\), whose height is bounded by NC02 independently of the target.

Choose one isogeny of degree at most
\[
N=(B_gk\max\{H_g(D),\log k,1\}^2)^{\alpha_g}
\]
to each of the \(h_E\) target classes. The ideal–isogeny bijection attaches distinct integral ideals to distinct target classes. Thus there are at least \(h_E\) ideals of norm at most \(N\). For \(N\ge1\),
\[
h_E\le\#\{I:N(I)\le N\}
\le N^2\zeta_E(2)
\le N^2\zeta(2)^{2g}
<2^{2g}N^2.
\]
The rational-prime Euler-factor comparison is valid also at ramified primes and for nonnormal fields. This establishes the required upper bound on \(h_E\), which is then combined with its named NC01 lower bound.

### Constants and powers

The case \(k>D\) implies \(k\ge\ell_gD^{\eta_g}\) since \(\ell_g\le1\), \(D\ge3\), and \(0<\eta_g<1\).

If \(k\le D\), positivity and \(D\ge3\) give
\[
\max\{a_g\log D+b_g,\log k,1\}\le U_g\log D.
\]
Combining NC01 and the count yields
\[
c_gD^{1/4}(\log D)^{-g}
<2^{2g}(B_gkU_g^2(\log D)^2)^{2\alpha_g}.
\]
Taking positive roots and dividing positive factors gives exactly
\[
k>
\frac{c_g^{1/(2\alpha_g)}}{2^{g/\alpha_g}B_gU_g^2}
\frac{D^{1/(8\alpha_g)}}{(\log D)^{2+g/(2\alpha_g)}}.
\]
Hence \(f_g\) and \(q_g\) are correct.

Maximizing \(t^{q_g}e^{-\eta_gt}\) proves
\[
t^{-q_g}\ge(e\eta_g/q_g)^{q_g}e^{-\eta_gt}.
\]
Since \(1/(8\alpha_g)=2\eta_g\), this leaves the positive discriminant exponent \(\eta_g\). Taking the minimum with 1 in the definition of \(\ell_g\) also handles \(k>D\). Finally \(16\alpha_g=16384g^3\), as stated.

### Field of moduli

Tsimerman Lemma 4.1 gives \(s_g=2\cdot3^{4g^2}\) and a field defining \(A\), every endomorphism and every polarization. The polarized field of moduli contains the unpolarized one. One may take the compositum of the lemma's defining field with the polarized field; the relative degree over the latter is still at most \(s_g\).

Thus \(k\le s_g[\mathbf Q(A):\mathbf Q]\), giving the claimed lower bound. A second factor \(s_g\) is unnecessary: the present proof constructs all target quotients over a single field \(K\), whereas Tsimerman's pairwise proof uses a different comparison field.

## NC04 reconstruction

### Same-field maximal-order replacement

Choose \(K\) with \(k\le s_gd\), defining \(A\) and all its geometric endomorphisms. Rémond's explicit same-field convention and Theorem 1.1 provide \(B/K\) and a \(K\)-isogeny, with maximal endomorphism order.

Conjugation through the isogeny transports all geometric rational endomorphisms over \(K\). Integral ones are also defined over \(K\), by descent for morphisms. Consequently the maximal order over \(K\) is the full geometric endomorphism ring.

The initial maximal-order isogeny needs no degree estimate. It is used for existence only. GR later produces a controlled isogeny using the height of \(B\). Therefore no conductor-dependent extension or unbounded height of \(A\) is being hidden in this step.

### Simple factors, repetitions and geometric simplicity

Rémond Theorem 1.2 gives an actual product over \(K\) of \(K\)-simple factors \(B_j\), each with maximal endomorphism ring. A geometric endomorphism of \(B_j\), composed with its inclusion and projection, is an endomorphism of \(B\); thus it is defined over \(K\).

If \(B_j\) were geometrically nonsimple, Theorem 1.2 over \(\overline{\mathbf Q}\) would give a nontrivial integral idempotent. It would be \(K\)-defined and yield a proper \(K\)-factor, a contradiction. Thus geometric simplicity is established.

Each factor is CM since \(B\) is isogenous to \(A\). For a geometrically simple CM factor, the rational endomorphism algebra is a CM field \(E_j\) of degree \(2r_j\), with primitive type. Maximality gives the full ring \(\mathcal O_{E_j}\), so NC03 applies over the same \(K\).

The proof allows isogenous but nonisomorphic factors. It counts every factor in the height sum; it does not claim that the actual product must consist of powers of fixed representatives. This distinction matters for maximal orders and is respected here.

### Simple discriminants and height

From NC03,
\[
D_{E_j}\le \ell_{r_j}^{-16\alpha_{r_j}}k^{16\alpha_{r_j}}
\le M_gk^{\beta_g}.
\]
This uses \(k\ge1\), increasing \(\alpha_r\), and the exact maximum defining \(M_g\). Also \(M_g\ge1\) since \(\ell_r\le1\).

Height additivity holds for the actual product. There are at most \(g\) factors, including repetitions, so NC02 yields
\[
h_F(B)\le C_0+C_1\log k,
\quad C_0=g(A_g^*\log M_g+C_g^*),\quad C_1=gA_g^*\beta_g.
\]
The definition \(V_g=1+C_0+C_1\) then implies
\[
\max\{h_F(B),\log k,1\}
\le V_g(1+\log k)\le V_gk.
\]
The last inequality is correctly directed for \(k\ge1\).

Use \(B\) as the first input of GR. Its theorem bounds both directions, so it supplies \(\varphi:B\to A\) with
\[
N=\deg\varphi\le(B_gV_g^2)^{\alpha_g}k^{3\alpha_g}.
\]
The exponent \(3\alpha_g\) consists of one field-degree power and two from the squared height bound.

### Nonmaximal centre and index

Let \(F=Z(\operatorname{End}^0(B))\) and let \(\mathcal O\) be its full ring of integers. Maximality forces the endomorphism order to contain all central algebraic integers: adjoining a missing one would give a larger order. Conversely every central integral endomorphism belongs to \(\mathcal O\). Hence \(Z(\operatorname{End}(B))=\mathcal O\). Transporting centres by \(\varphi\) gives \(R_x\subset\mathcal O\).

The finite kernel of \(\varphi\) is killed by its order \(N\). Thus \([N]_B\) factors through \(\varphi\), giving an actual \(\psi:A\to B\) with \(\psi\varphi=[N]_B\). For \(u\in\mathcal O\),
\[
\varphi u\psi=N\varphi u\varphi^{-1}
\]
is an integral central endomorphism of \(A\). Therefore
\[
N\mathcal O\subset R_x\subset\mathcal O,\qquad
[\mathcal O:R_x]\le N^{\operatorname{rank}\mathcal O}\le N^{2g}.
\]
The scalar is correctly the degree \(N\), with no unsupported square root or conductor estimate.

Repeated simple factors cause no loss: the centre has a field factor for each simple isogeny component, whereas dimension \(g\) counts these components with their multiplicities. Therefore its rank is at most \(2g\).

### Final discriminant and orbit

There are at most \(g\) field components in the centre, each occurring among the \(E_j\), so
\[
|\operatorname{disc}\mathcal O|\le M_g^gk^{g\beta_g}.
\]
The index–discriminant formula gives
\[
\begin{aligned}
|\operatorname{disc}R_x|
&\le M_g^gk^{g\beta_g}N^{4g}\\
&\le M_g^g(B_gV_g^2)^{4g\alpha_g}
  k^{g\beta_g+12g\alpha_g}\\
&=T_gk^{28g\alpha_g}.
\end{aligned}
\]
Thus \(P_g=28g\alpha_g=28672g^4\). Substituting \(k\le s_gd\) and solving
\[
|\operatorname{disc}R_x|\le T_g(s_gd)^{P_g}
\]
gives exactly the stated lower bound for \(d\). The coarse-moduli orbit has size \([\mathbf Q(x):\mathbf Q]\) in characteristic zero.

## Nonblocking wording clarifications

1. “Distinct simple CM-field factors” means one factor per simple isogeny component of the rational endomorphism algebra. Isomorphic abstract fields in different nonisogenous components must still be counted separately. For example, \(E\times E\) has discriminant \(D_E^2\). The proof's bound by \(g\) components is valid; spelling this out avoids an erroneous interpretation.

2. A brief field-of-moduli parenthesis could say that Tsimerman's extension defines every polarization, or explicitly take the compositum with the polarized field of moduli. The existing source statement already supplies the needed constant.

## Check classification

These are independent-reviewer whole-proof checks, recorded as targeted proof check rather than a claimed new independent re-proof of all literature. The displayed algebra is a symbolic verification for every \(g\ge1\); it is not a sampled numerical test or a formal certificate. NC01 and NC02 remain the named inputs specified by the assignment.
