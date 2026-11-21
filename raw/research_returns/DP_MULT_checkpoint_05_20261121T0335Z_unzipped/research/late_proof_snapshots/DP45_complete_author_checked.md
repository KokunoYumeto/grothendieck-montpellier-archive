# DP45: actual cyclic CM display and sharp slopes for the genus-three Jacobian

Author/checker: `/root/archive_binomial`, **GPT-6 Astra Pro**, inherited model; runtime reasoning effort **not exposed**. Date: **2026-11-21 UTC**. The root reserved finding **DP45**. This supplies the concrete geometric normal-form input left conditional in DP40. It does not edit the main paper or compute a global theta cost.

## 1. Statement

Let p be a prime with \(p\equiv3\) or \(5\pmod7\), put

\[
R=W(\mathbb F_{p^6}),\qquad C:y^2=x^7-1,
\qquad J=\operatorname{Jac}(C).
\]

Take the good integral model over R and the **covariant** Jacobian action a induced by \(\sigma(x,y)=(\zeta_7x,y)\), so

\[
a[P-\infty]=[\sigma(P)-\infty].
\]

Then \(G=J[p^\infty]\) is connected, of height six and dimension three, and its formal group is the actual completion \(\widehat J\). Its integral display is, after choosing generators of its rank-one CM eigenspaces, exactly a unit-arrow cyclic display of DP40 with

\[
h=6,\qquad A=\{0,1,2\}\subset\mathbb Z/6\mathbb Z.
\tag{J1}
\]

The Frobenius ordering of the embedding characters is

\[
(1,3,2,6,4,5)\quad(p\equiv3\bmod7),
\qquad
(2,3,1,5,4,6)\quad(p\equiv5\bmod7).
\tag{J2}
\]

In the corresponding three primitive integral tangent directions, the sharp directional coefficients are

\[
\boxed{(\gamma_0,\gamma_1,\gamma_2)
=\frac{(p,p^2,p^3)}{(p-1)(p^3+1)}.}
\tag{J3}
\]

The actual Cartier dual has the complementary cyclic type and the same ordered triple on the remaining three positions. For each selected direction and every \(n=(p^6)^r\), the normalized integral Teichmüller coordinate \(X_i\) satisfies

\[
v_p(D_i^nX_i(0))=\gamma_i(n-1).
\tag{J4}
\]

The mixed coefficientwise lower bound of DP40 holds for all integral formal functions. Thus these numbers are actual sharp local slopes for this Jacobian, with no remaining conditional rank-one-display hypothesis.

Their equal-direction mean on J, and on J together with its dual, is

\[
\frac{S_6(A)}6
=c_2\frac{p^2+p+1}{3(p^2-p+1)}<c_2,
\qquad c_2=\frac p{p^2-1}.
\tag{J5}
\]

The largest individual direction is nevertheless greater than \(c_2\), by \(p/(p^3+1)\). These statements do not identify a theta normalization, a harmonic operator, or a global cost with an equally weighted sum.

## 2. Integral curve, CM action, and tangent characters

The geometric construction already checked in DP22 works over every base where 2 and 7 are invertible. Its two charts are

\[
y^2=x^7-1,\qquad v^2=u-u^8,
\qquad u=x^{-1},\quad v=y/x^4.
\]

The relative derivatives verify smoothness on the first chart and at infinity on the second. The model is a projective geometrically connected genus-three curve with an infinity section. The Picard representability, smoothness and properness inputs giving its relative Jacobian were checked with exact FGA locators in `cm_genus3_primary_inputs.md`; their hypotheses are unchanged here because p is neither 2 nor 7. Therefore J is an abelian scheme of relative dimension three over R.

The ring R contains a primitive seventh root, chosen as its prime-to-p Teichmüller lift. The automorphism extends to both charts and fixes infinity. The regular differentials

\[
\omega_i=x^{i-1}dx/y,\qquad i=1,2,3,
\]

are an integral basis and have pullback eigenvalues \(\zeta_7^i\). Their orders at infinity are 4, 2 and 0. By the covariant Abel–Jacobi convention above, the pullback action of a on the cotangent space of J has those same eigenvalues. The differential on the tangent space has the same eigenvalues, since its ordinary transpose on cotangents retains the scalar. Thus

\[
\operatorname{Lie}J=\bigoplus_{b\in\{1,2,3\}}\operatorname{Lie}J_b,
\qquad a|\operatorname{Lie}J_b=\zeta_7^b,
\tag{J6}
\]

with each summand free of rank one over R.

As in DP22, \(\Phi_7(a)=0\): on the characteristic-zero generic fibre its differential is zero, hence the homomorphism is zero, and equality extends over the abelian scheme. This gives the integral cyclotomic action. Since p has order six modulo seven, \(\Phi_7\) is irreducible modulo p and \(E_p=\mathbb Q_p(\zeta_7)\) is the unramified field of degree six. The action on p-power torsion extends to \(\mathbb Z_p[\zeta_7]\), by reduction of its coefficients modulo each \(p^n\), and hence gives a unital \(E_p\)-action in the isogeny category of p-divisible groups.

## 3. Connectedness before introducing a display

Tate's canonical connected–étale sequence is functorial:

\[
0\longrightarrow G^0\longrightarrow G\longrightarrow G^{\mathrm{et}}
\longrightarrow0.
\tag{J7}
\]

The height of G is six and its dimension is three, by the standard abelian-scheme example. The completed cyclotomic action descends to \(G^{\mathrm{et}}\). If that quotient is nonzero, the resulting unital map from the field \(E_p\) into its endomorphism algebra up to isogeny is injective. Its rational étale Tate module is therefore an \(E_p\)-vector space. Consequently its height is a positive multiple of six. Since its height is at most six, it must equal six. Then the connected part has height zero, G is étale, and its dimension is zero, contradicting dimension three.

Thus G is connected. The same argument applies to its Cartier dual: the dual has height six and dimension three by Tate's dimension formula, and the dual cyclotomic endomorphism gives the same unital field action. Hence both G and \(G^D\) are connected. Tate's formal-group equivalence and the abelian-scheme example identify G with the p-divisible group of \(\widehat J\), and give a smooth three-dimensional formal group for \(G^D\).

This argument does not assume a CM Newton-slope formula or the rank-one display that will be proved next. A zero étale quotient is not claimed to carry an injective field action; injectivity is used only after assuming it is nonzero.

Exact primary locators: **Tate 1967 §1.4, p. 160; §2.2, sequence (4), p. 164; §2.1, Example (a), p. 161; §2.2, Proposition 1, p. 162; and §2.3, Proposition 3 and Example (b), p. 166**.

## 4. Integral CM idempotents force rank-one Witt eigenspaces

Work first over \(R_n=R/p^n\). Zink's **Theorem 9, p. 132**, applies to this excellent local p-nilpotent base and supplies the display

\[
\mathcal P_n=(P_n,Q_n,F,V^{-1})
\]

of the connected group \(G_{R_n}\). Its Witt-module rank is six, by **Theorem 5, p. 131**, and its tangent quotient is \(P_n/Q_n=\operatorname{Lie}G_{R_n}\). Full faithfulness transports the order action and all its relations to the display.

Let \(\widehat\zeta=[\zeta_7]\in W(R_n)\), with the bracket denoting the Witt Teichmüller lift of the chosen root in \(R_n\). Because 7 is invertible, the operators

\[
e_b=\frac17\sum_{r=0}^{6}\widehat\zeta^{-br}a^r,
\qquad b=0,1,\ldots,6,
\tag{J8}
\]

are orthogonal idempotents. The relation \(\Phi_7(a)=0\) makes \(e_0=0\), and their remaining sum is the identity. Thus

\[
P_n=\bigoplus_{b=1}^{6}P_{b,n},\qquad P_{b,n}=e_bP_n.
\]

These are finite projective summands over the local ring \(W(R_n)\), hence free. The Witt ring is local because \(R_n\) is local with p nilpotent; equivalently a Witt vector is invertible exactly when its zeroth component is invertible. Denote the free ranks by \(r_b\).

The semilinear Frobenius has the precise orientation

\[
F(P_{b,n})\subset P_{pb,n},
\tag{J9}
\]

where indices are nonzero residues modulo seven. Indeed, a commutes with F, and Witt Frobenius sends \(\widehat\zeta^b\) to \(\widehat\zeta^{pb}\). No inverse embedding occurs in this calculation.

The linearization of F becomes an isomorphism after p is inverted. To see this directly, choose any normal decomposition \(P_n=L\oplus T\). The linearization of \(V^{-1}\oplus F\) on \(L\oplus T\) is an isomorphism, and replacing \(V^{-1}\) by F on L multiplies those columns by p. Therefore F's linearization is invertible over \(W(R_n)[1/p]\).

This ring is nonzero: it maps to \(W(\mathbb F_{p^6})[1/p]\). Restricting the isomorphism to the idempotent summands gives equal free ranks \(r_b=r_{pb}\). Multiplication by p is a single cycle on the six nonzero residues modulo seven, so every \(r_b\) is equal. Their sum is six. Hence

\[
\boxed{\operatorname{rank}_{W(R_n)}P_{b,n}=1\quad(1\le b\le6).}
\tag{J10}
\]

This proves integral rank one without first identifying the Hodge filtration of a dual display or assuming a splitting of a rational isocrystal descends integrally.

## 5. Hodge filtration and unit-arrow normal form

Let \(I_n=\ker(W(R_n)\to R_n)\). The display's exact Hodge sequence is

\[
0\longrightarrow Q_n/I_nP_n\longrightarrow P_n/I_nP_n
\longrightarrow P_n/Q_n=\operatorname{Lie}G_{R_n}
\longrightarrow0.
\tag{J11}
\]

The order action preserves all its terms. On each character b, the middle term has rank one by (J10). The last term has rank one for \(b\in\{1,2,3\}\) and is zero otherwise, by (J6). Therefore

\[
Q_n\cap P_{b,n}=
\begin{cases}
I_nP_{b,n},&b\in\{1,2,3\},\\
P_{b,n},&b\in\{4,5,6\}.
\end{cases}
\tag{J12}
\]

In the first case a surjection between free rank-one \(R_n\)-modules is an isomorphism; in the second case the quotient is zero. These give the equalities themselves, not merely their generic-fibre ranks.

Choose generators of the six free lines in the Frobenius order (J2). Then T is the sum of the first three lines and L the sum of the last three. Frobenius, and \(V^{-1}\) on L, move to the next line by the same character calculation as (J9). The linearized normal-decomposition map is now a monomial matrix. Its invertibility forces every arrow coefficient to be a Witt unit. Thus the display has precisely the form

\[
Ff_i=u_i p^{\epsilon_i}f_{i+1},\qquad
\epsilon_i=0\ (i=0,1,2),\quad
\epsilon_i=1\ (i=3,4,5),
\tag{J13}
\]

with cyclic indices and unit \(u_i\), exactly as required by DP40.

The choices can be made compatibly in n. Display base change identifies the reduction at n+1 with the display at n; its idempotents reduce to the same idempotents. A generator of a free rank-one summand can be lifted to a generator at the next level, since the Witt-ring reduction is surjective and preserves units. Choosing these generators successively gives compatible arrow units. Their inverse limits lie in

\[
\varprojlim_n W(R_n)=W(R).
\]

This yields the integral display over the stated complete base. The associated isomorphisms of formal groups are compatible at all levels and therefore identify the unit-arrow model with \(\widehat J\) itself. No isogeny denominator or nonunit tangent rescaling has been introduced.

## 6. Dual precomposition and the Hodge-sequence orientation

The preceding rank argument does not require a dual-character computation. The proposed Hodge-duality check is now available without circularity, because (J13) and DP40 identify the actual Cartier dual with the complementary reciprocal-unit display.

On the dual Witt module, the endomorphism \(a^D\) acts by precomposition. If \(f_b\) has eigenvalue \(\widehat\zeta^b\), its coordinate covector satisfies

\[
a^D(f_b^*)=f_b^*\circ a=\widehat\zeta^b f_b^*.
\tag{J14}
\]

Thus the scalar is retained by this ordinary dual endomorphism. The dual selected tangent positions are the complementary three positions, so \(\operatorname{Lie}G^D\) has precisely characters \(\{4,5,6\}\) under \(a^D\).

Zink's dual normal submodule in **Definition 19, p. 143**, is the annihilator of \(Q_n/I_nP_n\) modulo \(I_n\). Evaluation consequently gives the perfect pairing

\[
(Q_n/I_nP_n)\times\operatorname{Lie}G^D_{R_n}\longrightarrow R_n,
\]

and hence \(Q_n/I_nP_n\simeq(\operatorname{Lie}G^D_{R_n})^*\). Functoriality reads \(\langle ax,y\rangle=\langle x,a^Dy\rangle\). Again precomposition retains each scalar eigenvalue. Thus the complementary Hodge characters agree exactly with (J11)–(J12).

As an optional independent generic-fibre check, applying **Tate 1967 §4, Corollary 2 following Theorem 3, p. 180**, to the dual group gives the natural exact Hodge–Tate sequence with left term \(\operatorname{Lie}G_C\), middle term \(\operatorname{Hom}_{\mathbb Z_p}(T_pG^D,C)\), and right term \((\operatorname{Lie}G^D_C)^*\) tensored with the Tate line. The middle term has each of the six characters once, since its Tate space is rank one over \(E_p\); removing \(\{1,2,3\}\) gives the same complementary set. This check is not used to prove (J10) or (J13).

## 7. Actual slopes and precise limitation

Apply DP40 to the now established model (J13). Its selected directional numerator sums are

\[
p+p^2+p^3,\qquad p^2+p^3+p^4,\qquad p^3+p^4+p^5,
\]

divided by \(p^6-1\). Cancelling \(p^2+p+1\) gives (J3). In the original character labels their order is

| Prime class | Character of first direction | Second | Third |
|---|---:|---:|---:|
| \(p\equiv3\pmod7\) | 1 | 3 | 2 |
| \(p\equiv5\pmod7\) | 2 | 3 | 1 |

The corresponding slopes are respectively p, \(p^2\), \(p^3\), over the common denominator \((p-1)(p^3+1)\). The dual positions give the same triple. The exact sharp sequences and mixed lower bounds are those already proved for arbitrary unit arrows in DP40, so they apply to the actual integral Jacobian without choosing its arrow units to equal one.

The displayed total and mean are the previously checked (CM11)–(CM14) arithmetic. Because this particular type has three selected and three complementary embeddings, its individual three-direction mean equals the full-pair mean. This equality of means would not hold automatically for an unbalanced type.

The result removes the concrete Jacobian's conditional local-model status at these primes. It does not change its CM type into the source's alternating type, identify a new geometric theta kernel, determine a selected harmonic module, or prove a shorter global lift chain.

## 8. Primary citations and actual check scope

The known geometric inputs are those already precisely checked for DP22: Grothendieck FGA exposé 232, **Theorem 3.1**; exposé 236, **Corollaries 1.7 and 2.3 and Proposition 2.10(ii)**. See `cm_genus3_primary_inputs.md` for the verified pages and hypotheses.

Tate, *p-Divisible Groups* (1967), [primary PDF](https://www.math.purdue.edu/~tongliu/teaching/598/p-divisible.pdf): **§1.4 p. 160; §2.1 Example (a) p. 161; §2.2 Proposition 1 p. 162 and sequence (4) p. 164; §2.3 Proposition 3 and Example (b) p. 166**. The optional orientation check uses **§4, Corollary 2 following Theorem 3, p. 180**. The exact p. 164 and p. 180 original pages were viewed in this check, in addition to reading the cited statement text.

Zink, *The display of a formal p-divisible group*, Astérisque 278 (2002), [primary PDF](https://www.numdam.org/article/AST_2002__278__127_0.pdf): **normal decomposition p. 129; Theorem 5 p. 131; Theorem 9 p. 132; Definition 19/(22) p. 143; Theorem 81/(145)–(156) pp. 204–207; Proposition 121 p. 241 and Theorem 122 p. 247**. The relevant statements and base hypotheses were read; their classical proofs are cited rather than reproved.

The connectedness argument, rank-cycle argument, Hodge component calculation, compatible integral basis construction and embedding orientation were derived and checked in this turn. A complete saved-proof reread, exact hashes and actual event **ABA-CE42** are recorded separately. An independent second-agent review is requested, not presumed completed. No machine formalization is claimed.
