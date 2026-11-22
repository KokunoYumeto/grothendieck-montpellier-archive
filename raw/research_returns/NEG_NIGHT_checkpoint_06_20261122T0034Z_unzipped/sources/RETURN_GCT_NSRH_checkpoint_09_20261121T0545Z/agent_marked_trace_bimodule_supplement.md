# F54 supplement: the marked trace with both actual actions

Author: /root/gct_statements, GPT-6 Astra Pro. Inherited effort is not exposed. Date: 2026-11-21 UTC.

This is a consequence of the complete actual bimodule calculation already proved in F43, not a new irreducibility assumption. It strengthens the marked-X actual-module result when the named ordinary left operators themselves must be Frobenius morphisms.

## 1. Exact actual branch and operators

Keep the actual rank-64 module, its named right P_1,P_2, and the marked central X of F54 Part3. Let b>1. The Delta-eigenspace of X_b is the eight-dimensional branch

\[
M_{2,b}=(W_1^V\otimes W_1^W)\otimes N(D(b)-2).
\tag{B1}
\]

This is precisely the last summand of the complete F43 bimodule decomposition (P10). The two W_1 spaces have dimension two. Their labels are the sl_2 highest weights; as polynomial GL_2 modules they are the degree-three modules with partition (2,1), including the determinant twist. No polynomial degree is being changed.

The F43 formula (P6), derived from the source coproduct and the explicit regular basis, is

\[
E g_-=g_+,\quad E g_+=0,\qquad
F g_+=g_-,\quad F g_-=0.
\tag{B2}
\]

Thus E and F on each W_1 are the two elementary off-diagonal matrix units. Their products are the two diagonal matrix units, so they generate the entire endomorphism algebra M_2(C). The V and W operator pairs commute and act on separate factors. Their joint image on W_1^V tensor W_1^W is therefore M_4(C).

On N(a), the actual right matrices are

\[
P_1=\begin{pmatrix}D&0\\a&0\end{pmatrix},
\qquad
P_2=\begin{pmatrix}0&a\\0&D\end{pmatrix},
\quad a=D-2.
\tag{B3}
\]

At b>1, D>4 and a>0. The regular F21 basis change takes P_1/D to e=diag(1,0) and P_2/D to

\[
f=\begin{pmatrix}1-z_2&1\\z_2(1-z_2)&z_2\end{pmatrix},
\qquad z_2=\frac{4(D-1)}{D^2}.
\]

Here 0<z_2<1. Hence

\[
ef(1-e)=E_{12},\qquad
(1-e)fe=z_2(1-z_2)E_{21}.
\]

Together with e and 1−e these generate all of M_2(C). In particular the full named left/right image on (B1) is

\[
M_4(\mathbb C)\otimes M_2(\mathbb C)=M_8(\mathbb C).
\tag{B4}
\]

All claims use the actual F43 left/right matrices, not a replacement action with the same dimensions.

## 2. Scalar restriction and marked-trace contradiction

Suppose F(v) is an invertible algebraic family on the actual tensor lattice, regular at a chosen place above v=1 and with regular evaluations at b and every sufficiently large b^n. Suppose it commutes with the actual right action, and suppose its base value F_b also commutes with the four named ordinary operators E_V,F_V,E_W,F_W.

The right-action commutation makes (B1) invariant. Equation (B4) then forces

\[
F_b|_{M_{2,b}}=\beta I_8,\qquad \beta\ne0.
\tag{B5}
\]

This conclusion needs no purity or spectral-weight assumption, and no identification of the actual algebra with a full target endomorphism algebra.

If the marked comparison

\[
\operatorname{Tr}(X_{b^n}F_{b^n})
 =\operatorname{Tr}(X_bF_b^n)
\]

held eventually, the algebraic function

\[
g(v)=\operatorname{Tr}_M(X(v)F(v))
\]

would satisfy

\[
g(b^n)=8\Delta(b)\beta^n.
\tag{B6}
\]

The constant 8 Delta(b) is nonzero. By the fully proved single-exponential lemma of F54 Part3,

\[
g(v)^L=(8\Delta(b))^L v^m
\]

for some L>0 and m in Z. In particular g is a unit at every place over v=1.

But the actual regular tensor action has X(1)=0, and F is regular there, so g(1)=0. This is a contradiction.

## 3. Scope and exact remaining alternative

Only the ordinary left commutation at the base is needed; a global left-equivariance hypothesis is sufficient but stronger. The right action and marked central insertion remain exactly those of the actual nonstandard tensor module.

The result applies when the named left raising and lowering operators are morphisms of the same Weil representation, so they commute with its chosen F. It does not apply to a graded or coefficient-twisted interpretation in which these operators are maps from a nontrivial weight-line tensor product and satisfy a covariance law instead. The F48 character construction explicitly distinguishes those two cases.

An unrestricted fractional mixed-weight marked-X construction commuting only with the right algebra can therefore evade this corollary by not commuting with the named ordinary left factors. The result does not forbid such a construction or substitute itself for the missing categorical comparison.

## 4. Source and check scope

The immediate inputs are the complete proved F43 formulas (P6), (P9), and (P10), which were reread in their full report context. Their primary ordinary-action input is GCT IV Section 4.1 equations (28)–(29), printed p22, and the commuting action in Section 6.1, printed p33; the actual nonstandard right conventions are Definition 11.1 equation (93) and Proposition 11.14 equation (110), pp64–65. The F43 calculation already directly checks the regular tensor basis and these ordinary operators.

The new argument (B1)–(B6) is supplied in full above. The check performed is exact matrix-generation and trace reasoning, not a new numerical experiment or proof-kernel verification. Independent whole-proof review is requested before adding this corollary to the final fragment.

