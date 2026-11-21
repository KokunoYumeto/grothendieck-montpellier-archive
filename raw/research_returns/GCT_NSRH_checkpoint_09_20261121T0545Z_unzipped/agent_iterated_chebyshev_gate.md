# F63: an actual iterated three-strand summand obstructs strict effective kernels

Author: /root/gct_statements, GPT-6 Astra Pro. Inherited effort is not exposed. Date: 2026-11-21 UTC.

The strand rank is fixed at r=3. The integer k counts tensor factors in Blasiak's iterated nonstandard coproduct, whose k=2 member is the binary algebra used in F56/F61. Known source formulas are not claimed as new. The deductions here are the two-word strict-effectivity obstruction, its persistence for k>=4, its regular occurrence in the tensor product of two previously positive k=2 modules, an explicit marked projector, and a proof that all unmarked word traces of that whole tensor remain positive.

## 1. Primary source and exact normalization

Primary source: Jonah Blasiak, Nonstandard braid relations and Chebyshev polynomials, arXiv:1010.0421v2, 16 May 2014.

https://arxiv.org/pdf/1010.0421

Local PDF: primary_sources/Blasiak_1010_0421v2.pdf.
SHA256: 1970dbbe63dcf8b4f32b00d6b637b7b9425f743f21f91d7d9565ad10a1a82387.

Local layout text: primary_sources/Blasiak_1010_0421v2.txt.
SHA256: c7a0f02d417f8f7d4f89a9431b58772e4cb58b84ddd9911109395cfa74b054a3.

Rename the source variable u as v and put

\[
\delta=v+v^{-1},\quad D=\delta^2,\quad
\Lambda=\mathbb Z[v,v^{-1}],\quad K=\mathbb Q(v).
\]

These are the actual generator normalizations, without replacing the generators by idempotents. Definition 2.5, printed p. 6, defines

\[
\check H_3^{(k)}\subset H_3^{\otimes k},\qquad
P_i^{(k)}=\delta^k\Delta_i^{(k)}(p_+),\qquad
Q_i^{(k)}=\delta^k-P_i^{(k)}.
\tag{I1}
\]

Here k=1 gives ordinary H_3 and k=2 the binary nonstandard algebra. The parabolic H_2 has the Hopf structure of Proposition 2.3, pp. 4–5. Equations (8)–(11), p. 6, give the actual inclusions

\[
\check\Delta^{(k_l,k_r)}:
\check H_3^{(k_l+k_r)}
\hookrightarrow\check H_3^{(k_l)}\otimes\check H_3^{(k_r)},
\]
\[
P_i^{(k_l+k_r)}
\longmapsto P_i^{(k_l)}\otimes P_i^{(k_r)}
 +Q_i^{(k_l)}\otimes Q_i^{(k_r)}.
\tag{I2}
\]

No full Hopf structure on the three-strand algebra is asserted. The parabolic iteration and restriction map (I2) are what is used.

In §3.1, equation (13), p. 8, X^(k)(c) has LEFT-COLUMN matrices

\[
P_1^{(k)}=\begin{pmatrix}\delta^k&c\\0&0\end{pmatrix},
\qquad
P_2^{(k)}=\begin{pmatrix}0&0\\1&\delta^k\end{pmatrix}.
\tag{I3}
\]

Equation (14), p. 9, makes it absolutely irreducible when c is neither 0 nor delta^(2k). These matrices and the left-column convention were checked visually on original p. 8. Transposition gives the earlier right-row convention, leaving the two-word trace unchanged.

Write

\[
A_j=\delta^jT_j(1/\delta),\qquad
c_{k,j}=\delta^{2(k-j)}A_j^2,\quad 1\le j\le k.
\tag{I4}
\]

Theorem 3.4, p. 12, lists the generic simples: the two scalar modules and X^(k)(c_(k,j)), j=1,...,k. Its equivalent notation is epsilon_+^(k-j) tensor M^(j), with M^(j)=X^(j)(A_j^2). Corollary 3.5, p. 13, proves generic split semisimplicity.

Theorem 3.7, pp. 13–14, equations (27)–(28), gives the presentation

\[
(P_i^{(k)})^2=\delta^kP_i^{(k)},\qquad
P_1^{(k)}F_k(P_2^{(k)}P_1^{(k)})
=P_2^{(k)}F_k(P_1^{(k)}P_2^{(k)}),
\quad
F_k(y)=\prod_{j=1}^k(y-c_{k,j}).
\tag{I5}
\]

The source itself prints the following in equation (24), p. 11:

\[
A_1=1,\quad A_2=2-D,\quad A_3=4-3D,\quad
A_4=D^2-8D+8.
\tag{I6}
\]

We read the entire defining iteration context, the matrix discussion and tensor decomposition, the proofs of Theorems 3.4/3.7, and all of §5. The source is not being interpreted as a statement about strand rank four.

## 2. First individual-simple obstruction and persistence

From (I3),

\[
P_1^{(k)}P_2^{(k)}
=\begin{pmatrix}c&c\delta^k\\0&0\end{pmatrix},
\qquad
\operatorname{Tr}(P_1^{(k)}P_2^{(k)})=c.
\tag{I7}
\]

At k=j=4 put A=A_4. The source already displays A's mixed Laurent expansion. Squaring it gives the invariant word trace

\[
\begin{split}
c_{4,4}=A^2={}&v^8-8v^6+12v^4+8v^2+38\\
&+8v^{-2}+12v^{-4}-8v^{-6}+v^{-8}.
\end{split}
\tag{I8}
\]

A product of matrices over N[v,v^-1], or even Q_nonnegative[v,v^-1], has trace in the same cone. Simultaneous change of basis preserves trace. The negative coefficients in (I8) therefore prove that no basis of this actual generic simple makes both named generators nonnegative Laurent matrices. This is a two-word invariant obstruction, not a failure of one displayed basis or one diagonal rescaling.

It persists for every k>=4. Choose v_0>1 such that

\[
D(v_0)=4+2\sqrt2.
\tag{I9}
\]

This exists because D(v)=v^2+2+v^-2 increases continuously from 4 to infinity for v>1. The right side of (I9) is a root of D^2-8D+8. Thus

\[
c_{k,4}=\delta^{2(k-4)}A^2\ne0
\quad\hbox{as a Laurent polynomial},\qquad
c_{k,4}(v_0)=0.
\tag{I10}
\]

A nonzero nonnegative Laurent polynomial is strictly positive at every positive argument. Hence c_(k,4) is not such a polynomial for any k>=4. Its coefficients are mixed: c_(k,4)(1)=4^(k-1)>0, while its positive zero excludes all coefficients nonnegative. The source includes the j=4 simple for every k>=4.

There is an exact limited minimality statement. For k<=3, set

\[
b_{k,1}=\delta^{k-1},\qquad
b_{k,2}=\delta^{k-2}(D-2),\qquad
b_{k,3}=\delta^{k-3}(3D-4),
\tag{I11}
\]

using only j<=k. These have nonnegative integral Laurent coefficients, because D-2=v^2+v^-2 and 3D-4=3v^2+2+3v^-2. They satisfy b_(k,j)^2=c_(k,j). Conjugating (I3) by diag(b_(k,j),1) gives

\[
P_1^{(k)}=\begin{pmatrix}\delta^k&b_{k,j}\\0&0\end{pmatrix},
\qquad
P_2^{(k)}=\begin{pmatrix}0&0\\b_{k,j}&\delta^k\end{pmatrix}.
\tag{I12}
\]

The scalar simples have values delta^k and 0. Therefore every individual generic simple for k<=3 has a positive Laurent generator model. The first failure of this property is k=4. This does not claim compatible effective coproduct intertwiners for those earlier models or regular simultaneous splittings of all full tensor lattices.

## 3. Actual regular occurrence in two F56 blocks

The j=2,k=2 model of (I12) is F56's N(D-2), with the left-column transpose of its right-row matrices. Put

\[
a=D-2,\quad d=D^2,\quad A=D^2-8D+8,
\]
\[
P_1=\begin{pmatrix}D&a\\0&0\end{pmatrix},\quad
P_2=\begin{pmatrix}0&0\\a&D\end{pmatrix},\quad
Q_i=D I_2-P_i.
\tag{I13}
\]

The actual Delta^(2,2) gives

\[
R_1=P_1\otimes P_1+Q_1\otimes Q_1
=\begin{pmatrix}
d&Da&Da&2a^2\\
0&0&0&-Da\\
0&0&0&-Da\\
0&0&0&d
\end{pmatrix},
\]
\[
R_2=P_2\otimes P_2+Q_2\otimes Q_2
=\begin{pmatrix}
d&0&0&0\\
-Da&0&0&0\\
-Da&0&0&0\\
2a^2&Da&Da&d
\end{pmatrix}.
\tag{I14}
\]

This uses the named source restriction, not an abstract isomorphism of two-idempotent algebras. Let B have columns

\[
u_+=(d,-Da,-Da,d)^{\mathsf T},\quad
u_-=(0,1,-1,0)^{\mathsf T},
\]
\[
b_1=(A,-Da,-Da,d)^{\mathsf T},\qquad
b_2=(d,-Da,-Da,A)^{\mathsf T}.
\tag{I15}
\]

Direct multiplication gives the full action:

\[
\begin{array}{c|rrrr}
 &u_+&u_-&b_1&b_2\\ \hline
R_1&d u_+&0&d b_1&A b_1\\
R_2&d u_+&0&A b_2&d b_2 .
\end{array}
\tag{I16}
\]

For example the first coordinate of R_1 b_2 is d^2-2da^2+2a^2A=A^2, since A=2a^2-d; the remaining coordinates are those of A b_1. The other products use the same identity.

Subtract u_+ from columns b_1,b_2. They become (A-d)e_1 and (A-d)e_4. The middle coordinates of u_+,u_- have determinant 2Da. Since A-d=-8(D-1),

\[
\det B=2Da(A-d)^2=128D(D-2)(D-1)^2.
\tag{I17}
\]

It is a unit in R=Q[v,v^-1]_(v-1), because D,D-2,D-1 specialize to 4,2,3. Thus (I16) proves an actual regular decomposition

\[
N(D-2)\otimes N(D-2)
\simeq\check\epsilon_+\oplus\check\epsilon_-\oplus N(A),
\tag{I18}
\]

with plus value d and two-dimensional matrices

\[
N_1(A)=\begin{pmatrix}d&A\\0&0\end{pmatrix},\qquad
N_2(A)=\begin{pmatrix}0&0\\A&d\end{pmatrix}.
\tag{I19}
\]

The trace invariant is A^2. Over K this is neither 0 nor d^2, so this is the actual generic M^(4) from Theorem 3.4. This checks the particular occurrence supplied abstractly by Proposition 3.1, preserving named matrices and the parameter-local lattice.

The occurrence also belongs to the actual tensor setting already proved in F21/F43. Each binary rank-three module with two two-dimensional ordinary factors has regular N(D-2) summands in the verified basis. Tensor one such summand from each of two binary modules and use (I2); this is exactly (I14). Therefore the tensor cube of four two-dimensional ordinary factors contains the displayed regular summand after the stated finite localization. Alternatively, the ordinary Specht module M^(2,1) occurs in each factor's tensor cube, and source equations (25)–(26), p. 12, put M^(4) in its fourth tensor power.

For general k>=4 append ordinary trivial M^(3) factors. On a trivial factor P_i^(1)=delta and Q_i^(1)=0. Equation (I2) therefore scales the preceding generator by delta. The resulting trace is exactly delta^(2(k-4))A^2. No assertion that M^(2,1) tensor-power k contains the j=4 simple at odd k is needed or made.

## 4. A regular actual projector identifies the extra effectivity requirement

Define on the four-dimensional tensor

\[
E_4=\frac{d(R_1+R_2)-R_1R_2-R_2R_1}{d^2-A^2},
\qquad
d^2-A^2=16(D-1)(D-2)^2.
\tag{I20}
\]

The denominator is a unit in R. On the scalar blocks of (I18) the numerator is zero. On N(A), direct multiplication in (I19) gives numerator (d^2-A^2)I_2. Hence

\[
E_4^2=E_4,\quad [E_4,R_i]=0,\quad
\operatorname{Tr}(E_4)=2,\quad
\operatorname{Tr}(E_4R_1R_2)=A^2.
\tag{I21}
\]

Explicitly it simplifies to

\[
E_4=\frac1{8(D-1)}
\begin{pmatrix}
-A&-Da&-Da&-d\\
Da&d&d&Da\\
Da&d&d&Da\\
-d&-Da&-Da&-A
\end{pmatrix}.
\tag{I22}
\]

This is an actual commuting idempotent, regular at v=1, rather than a generic projector with a forced pole at that specialization.

No simultaneous basis can make R_1,R_2,E_4 all nonnegative Laurent matrices: otherwise their product trace would be nonnegative, contrary to (I8),(I21). Thus extending the effective-kernel route while preserving this regular simple projector as an effective coefficient-kernel operator is impossible. A general linear or derived idempotent is not automatically such an effective kernel operator; its mere existence is not a contradiction.

## 5. All unmarked word traces on the whole tensor are positive

This boundary can be proved for every word. Let w be a nonempty word of length L in R_1,R_2 and let 2s be its number of cyclic changes of label. Then L>=2s.

For the two-dimensional block, factor the rank-one matrices as N_i=u_i r_i with

\[
u_1=(d,0)^{\mathsf T},\quad r_1=(1,A/d),\qquad
u_2=(0,d)^{\mathsf T},\quad r_2=(A/d,1).
\]

Every scalar r_i u_j equals d for equal labels and A for different labels. Taking the trace closes the final scalar product back to the initial label. Consequently

\[
\operatorname{Tr}_{N(A)}(w)=d^{L-2s}A^{2s}.
\tag{I23}
\]

This includes s=0. The plus scalar contributes d^L, and the minus scalar contributes zero, so

\[
\operatorname{Tr}_{N(D-2)^{\otimes2}}(w)
=d^{L-2s}\bigl(d^{2s}+A^{2s}\bigr).
\tag{I24}
\]

Both

\[
U=d+A=2(D-2)^2,\qquad V=d-A=8(D-1)
\tag{I25}
\]

are nonnegative integral Laurent polynomials. For s>=1, the even-binomial identity is

\[
d^{2s}+A^{2s}
=2^{1-2s}
 \sum_{\substack{0\le j\le2s\\ j\ {\rm even}}}
 \binom{2s}{j}U^{2s-j}V^j.
\tag{I26}
\]

The right side has nonnegative rational coefficients. The left side is integral Laurent, so its coefficients are nonnegative integers. The s=0 factor is 2. Multiplying by d^(L-2s) proves positivity for every word.

For example,

\[
d^2+A^2=2v^8+40v^4+64v^2+108
+64v^{-2}+40v^{-4}+2v^{-8}.
\tag{I27}
\]

Thus unmarked scalar word traces do not rule out another P-only positive model of the whole tensor. No such model or coherent iteration is constructed here. The obstruction is on the specified simple or on the simultaneous marked projector; positivity of all whole word traces does not prove the existence of a positive basis.

## 6. Pure-point and iteration scope

Every exponent of c_(k,4) is even and its coefficients are mixed. Under v=q^(n/2), the F57 pure-point criterion rules out a bounded point complex pure of any single weight with these Euler traces. Precisely, a root q^j has even weight 2j and can occur in a pure weight-w complex only in degree 2j-w. Every visible coefficient would therefore have the same sign (-1)^w, contrary to (I10).

The same obstruction holds for v=q^n, where the root weights are again even. An overall parity shift or common Tate twist cannot remove mixed signs. Mixed Tate complexes remain possible. An independently inserted endomorphism trace is outside this conclusion; the marked version requires the extra comparison which makes that effective closed-kernel word the Frobenius trace object.

It follows that F56/F61 cannot extend to a compatible family supplying a strict effective finite graded kernel model on every actual simple of every iterated algebra, together with the stated word-trace comparison. The k=4 simple already excludes this. Whole tensor objects with non-effective simple projectors are not ruled out, as Section 5 demonstrates.

This is the source's tensor-factor iteration k at fixed strand rank r=3. It is not a new increasing-r obstruction for the original binary algebra, and it does not replace constructing the source's all-r family. Its relevance is the concrete additional compatibility demanded by (I2).

## 7. Exact boundary of the published cellular bases

Section 5 begins on printed p. 19. Definition 5.1, p. 20, requires an anti-involution and triangular multiplication with coefficients in R, imposing no nonnegative cone.

For m=3 the two-dimensional labels are j=1,...,k, with sigma_j=delta^k T_j(1/delta). Equation (45), p. 21, defines the cellular basis using factors P_21-sigma_j^2. Proposition 5.3, p. 22, requires the indicated sigma_j to be invertible, as well as the earlier condition on differences for incomparable labels. Equation (48), p. 22, gives the balanced cell matrices with off-diagonal sigma_j. On j=k=4 this is the mixed A_4, and the invariant two-word trace is A_4^2.

The localization may invert sigma_4 and omit the positive zero (I9). The resulting cellular basis is still not a nonnegative Laurent matrix model: any such model in any generic basis would have the impossible trace (I8). Nothing here contradicts cellularity, the specialization analysis of Propositions 5.5/5.8, pp. 23–24, or generic semisimplicity.

No IV/VIII conjecture for these iterated k>=4 bases follows from the word cellular. Their signed/factored conventions, designated bases and original binary all-r problem are distinct. The source's known formulas (I1)–(I6) are inputs; strict-effectivity and pure-trace exclusions are the deductions.

## 8. Separate Grothendieck dictionary

The restriction (I2), regular change (I15) and idempotent (I20) are finite locally free module/action data. EGA I, Theorem 1.3.7, p. 86, Corollary 1.3.8, p. 87, and Theorem 1.4.1, pp. 90–92 give the affine module dictionary. SGA 3, I, 4.7.2–3 and cote 90, scan 17 supply action/coaction language, not a new Hopf structure on the whole nonstandard algebra.

Strict graded coefficients use the effective split-torus character cone N[v,v^-1]. The trace obstruction concerns that cone on the actual module, not the mere existence of a module or cellular basis. SGA 6, V, §§2–3 and cote 133, scan 18 supply representation and lambda/sigma language for coefficient objects, without a lambda-ring assertion for the noncommutative word algebra.

The pure-point corollary uses the specified grading-to-Frobenius comparison and BBD §§5.1.5/5.1.8, pp. 125–127. Bounded mixed complexes remain in the perfect framework of SGA 6, I, Definition 4.7, pp. 121–122, and Example 4.8, p. 122. A regular linear projector does not by these framework identifications become an effective categorical projector; that is exactly the extra comparison tested by (I21).

## 9. Verification record

- Complete primary contexts read: §§2.4, 3.1–3.3 and all of §5 of arXiv:1010.0421v2. The retrieved original PDF and layout text are hashed above.
- Original page images inspected: p. 8 for equation (13) and left-column convention; p. 11 for equation (24); p. 22 for Proposition 5.3 and equation (48). Numbered theorem locators also match the full extracted contexts.
- Reconstructed by hand: trace, positive-zero persistence, k<=3 balanced positive models, the actual four columns and determinant, projector by block actions, all-word trace formula and even-binomial positivity.
- Exact certificate: verify_iterated_chebyshev_gate.py checks expansions, source matrices, actual Delta^(2,2), quadratics, the complete regular block change, projector identities, characteristic polynomial, small-k models and the actual k=4 braid relation. The complete output is saved separately. This is supplemental exact algebra, not a formal proof assistant or the proof of universal positive-zero and all-word claims.
- Fresh independent full-proof/source and script review is requested before integration. No such verdict is claimed here.

