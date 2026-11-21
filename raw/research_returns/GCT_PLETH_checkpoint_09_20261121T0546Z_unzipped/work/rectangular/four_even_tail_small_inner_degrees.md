# The remaining inner degrees of the higher-row width-four block

## R-042. Exact cubic extension, canonical scalar, and quadratic endpoint

Let \(m\ge2\), \(a\ge m+1\), \(\dim V\ge m+1\), and
\[
\lambda=(3a-2m-2,4,2^{m-1}).
\]
Require \(\lambda_1\ge4\); among these parameters this excludes
only \((a,m)=(3,2)\). Then
\[
\boxed{
a_{a,3}^{\lambda}=\min(2,\max(0,a-m-1)),\qquad
\operatorname{mult}_{\lambda}\operatorname{im}h_{3,a}
=\begin{cases}1,&m=2,\\0,&m\ge3.\end{cases}}
\tag{QD.1}
\]
The proof specifies the whole polynomial-extension subspace and
the exact nonzero scalar in the three-row case. Together with
R-041, this determines the actual rank for every inner degree
at least three on the same tail family.

For the quadratic inner degree, the valid partitions of this form
have \(a\ge m+3\). They satisfy
\[
\boxed{
a_{a,2}^{(2a-2m-2,4,2^{m-1})}=1,\qquad
\operatorname{mult}_{(2a-2m-2,4,2^{m-1})}\operatorname{im}h_{2,a}=0.}
\tag{QD.2}
\]
The quadratic statement is the explicit principal-minor realization
of the established even-partition decomposition; its maps and
uniqueness are proved in §4. No historical novelty claim is made.

## 1. The exact degree-four row coefficient

Use R-041's three centered polynomials \(P_1,P_2,P_3\).
They span the entire relevant invariant space, of dimension
\(r_a=\min(3,a-m)\), by its explicit invariant restriction map.
Every polynomial has row degree at most four.
Write
\[
\begin{aligned}
\beta_1&=(a-1)/a^2,\\
\beta_2&=(a^2-3a+m+2)/a^3,\\
\beta_3&=-(m-1)(2a-m-2)/(2a^3).
\end{aligned}
\tag{QD.3}
\]
These are the second column of the exact matrix \(\mathcal C_{a,m}\).

For a fixed row \(r\), replace \(w_r\) by \(tv\) and take
the coefficient of \(t^4\). The three coefficients are exactly
\[
[t^4]P_j(w_1,\ldots,tv,\ldots,w_a)
=\beta_j\,W_r(v;w_{i\ne r}),
\tag{QD.4}
\]
where
\[
W_r=v_1^2\sum_{\substack{|I|=m+1\\r\in I}}
\left([t]\det R_I(w_r=tv)\right)^2.
\]
Here \(R\) is the affine row matrix \((1,w_i)\) of R-041.

To verify (QD.4), use the raw row weights before QE.10.
For \(I\ni r\), the leading quadratic coefficients of the
weights of \(A,B,C'\) are, respectively,
\[
\frac{a-1}{a}v_1^2,\qquad
\left(1-\frac2a+\frac{m+1}{a^2}\right)v_1^2,\qquad
\left(-\frac m a+\frac{m(m+1)}{2a^2}\right)v_1^2.
\]
The determinant square contributes its leading quadratic coefficient.
For \(I\not\ni r\), its determinant is independent of \(w_r\),
so its total row degree is at most two and cannot contribute.
Return to \(P_1,P_2,P_3\) by QE.5:
\(P_1=A/a\), \(P_2=(B-P_1)/a\), \(P_3=(C'+P_1)/a\).
The resulting three factors are exactly (QD.3).

The common polynomial \(W_r\) is nonzero. Take \(v=e_1\),
and among the other rows use \(0,e_2,\ldots,e_m\);
there are enough rows because \(a\ge m+1\).
The determinant of that affine subset has nonzero linear coefficient
in \(t\). On real inputs all summands in \(W_r\) are squares,
so their sum is positive for this specialization.
Thus (QD.4) gives a nonzero linear functional on the actual
invariant span. Any linear relation among the \(P_j\)'s also
annihilates \(\beta\), by (QD.4), so it is well defined on that span.

## 2. The full cubic extension and its actual basis

A separately homogeneous polynomial of slot degree three
dehomogenizes to a polynomial of degree at most three in every
row. Conversely, multiplying such a dehomogenization by
\((\prod_i x_i)^3\) is its exact polynomial homogenization.
Since the present row degrees are at most four, (QD.4) proves
that the extension space is precisely the kernel of \(\beta\).

Because \(\beta_1\ne0\), that kernel is spanned by
\[
Q_2=\beta_1P_2-\beta_2P_1,\qquad
Q_3=\beta_1P_3-\beta_3P_1.
\tag{QD.5}
\]
Each has degree at most three in every row, by the literal
degree-four cancellation in (QD.4).
For \(a\ge m+3\), the \(P_j\)'s are independent, so
\(Q_2,Q_3\) are independent.
For \(a=m+2\), QE.14 gives \(Q_3=-Q_2\), with
\(Q_2\ne0\) because \(P_1,P_2\) are independent.
For \(a=m+1\), QE.13 gives both \(Q_j=0\).
The kernel dimension is therefore \(r_a-1\), exactly the
target multiplicity in (QD.1).

The actual highest polynomials are
\[
\widehat Q_{j;a,3,m}
=\left(\prod_i x_i\right)^3Q_j(y_i/x_i).
\tag{QD.6}
\]
Translation invariance and the lower highest-weight equations
are inherited from \(P_j\); separate homogeneity proves injectivity
of the inverse evaluation \(x_i=1\).
This identifies the entire finite-degree multiplicity space,
including its one-dimensional and zero-dimensional endpoints.

## 3. The exact cubic canonical maps

For \(m=2\), the independent-row coefficient rows in QE.10,
after applying the combinations (QD.5), are
\[
\begin{array}{c|ccc}
&Q&R&T\\ \hline
Q_2&-(a-3)^2/a^3&0&-2(a-3)/a^4\\
Q_3&(a-3)/a^3&0&(a-3)(a-2)/a^4.
\end{array}
\tag{QD.7}
\]
The common factor is \((a)_3=a(a-1)(a-2)\).
These entries are direct substitution into QE.11.
Their zero middle column agrees with the pointwise extension proof;
it removes all dependence on fourth moments before the split-form
evaluation is taken.

For three centered split factors in dimension two, the second and
third moments are \(-S_3/6\) and \(C_3/3\).
The exact three-row relations QE.13 give
\(P_{3;3}=-P_{1;3}/6\).
Consequently the formal quantities in (QD.7) are
\[
Q=-P_{1;3}/216,\qquad T=-P_{1;3}/54.
\tag{QD.8}
\]
No fourth moment is needed. One may extend the degree-three row
functional arbitrarily to degree four when deriving QE.10:
the middle column in (QD.7) cancels that extension identically.

The normalized canonical identities are therefore
\[
\boxed{
h_{a,3}\widehat Q_{2;a,3,2}
=\frac{(a-3)(a-2)(a-1)(a^2-3a+8)}
{216a^3}\widehat P_{1;3,a,2},}
\tag{QD.9}
\]
and
\[
h_{a,3}\widehat Q_{3;a,3,2}
=-\frac{(a-3)(a-2)(a-1)(5a-8)}
{216a^3}\widehat P_{1;3,a,2}.
\tag{QD.10}
\]
Their derivation is the actual scalar-one split-form pairing
SR.5–SR.6, followed by dense first-coordinate extension.
The target generator is nonzero by the centered simplex.
For every \(a\ge4\), the coefficient in (QD.9) is nonzero:
all linear factors are positive and \(a^2-3a+8>0\).
The target of this multiplicity map is the whole line
\((S_{(4,2)}\mathfrak h_3)^{S_3}\), whose dimension is one
by R-041. Thus this actual map has rank one.
Its scalar reciprocal gives an explicit preimage of that
line, and scalar-one transposition gives rank one for \(h_{3,a}\).

For \(m\ge3\), the partition has \(m+1\ge4\) rows.
The source of \(h_{3,a}\) is a submodule of
\((\operatorname{Sym}^aV)^{\otimes3}\).
The three horizontal-strip Pieri inclusions have at most
three rows, so its \(\lambda\)-multiplicity is zero.
This proves the remaining actual zero ranks in (QD.1).
It is also visible in the moment map: the three-row covariance
and third tensors have a common row span of dimension at most two,
so all \(P_j\) of \(m\)-dimensional determinant type vanish.

## 4. The quadratic endpoint by actual symmetric-matrix maps

Let \(r=m+1\) and let \(Z\) be a generic symmetric \(r\)-by-\(r\)
matrix. Its entry \(Z_{ij}\) is evaluation on the normalized
symmetric tensor \(e_i\odot e_j\); a pure square therefore
has matrix entries \(v_i v_j\), including the off-diagonal
entries with this convention. Write \(\Delta_i\) for its leading principal minor.
For \(a\ge m+3\), the polynomial
\[
\Delta_1^{\,a-m-3}\Delta_2\Delta_{m+1}
\tag{QD.11}
\]
has degree \(a\) in the symmetric-matrix entries and weight
\((2a-2m-2,4,2^{m-1})\).
It is a nonzero highest vector in
\(\operatorname{Sym}^a(\operatorname{Sym}^2V)\).
Indeed lower unitriangular congruence preserves every leading
principal minor; these are precisely the raising invariances
in the coordinate convention used above. Diagonal congruence
gives their weights \((2^i)\).

The uniqueness can be checked by an actual dense chart.
On the open set where all \(\Delta_i\ne0\), Gaussian elimination
gives the unique factorization \(Z=L\operatorname{diag}(d_i)L^t\),
where \(L\) is lower unitriangular and
\(d_i=\Delta_i/\Delta_{i-1}\), with \(\Delta_0=1\).
These formulas and elementary elimination construct both rational
maps and their inverses on the open set.
A highest polynomial is constant on the unitriangular factor;
its fixed diagonal weight forces its restriction to be a scalar
multiple of
\(\prod_i d_i^{\lambda_i/2}\).
For the stated weight this is exactly (QD.11).
A polynomial vanishing on this dense open set is zero.
Hence its highest multiplicity is exactly one.

For the explicit slot dictionary, polarize a degree-\(a\)
matrix polynomial \(F\) by
\[
(v_1,\ldots,v_a)\longmapsto
\frac1{a!}[t_1\cdots t_a]\,
F\!\left(\sum_{i=1}^a t_i v_i v_i^t\right).
\tag{QD.12}
\]
This is symmetric and quadratic in each vector slot.
It is the normalized outer polarization followed by evaluation
on pure squares. Pure squares span the symmetric matrices;
multilinearity therefore makes this restriction injective.
The construction is the actual Cauchy/Young inclusion of the
symmetric-matrix module in the separate-slot model.
It proves the stated multiplicity in that model as well.

Finally, \(\operatorname{Sym}^2\operatorname{Sym}^aV\)
is contained in the twofold tensor product of the row-\(a\)
representation. Pieri gives at most two rows, whereas the
partition in (QD.2) has \(m+1\ge3\) rows.
Its source multiplicity is zero, and its target multiplicity
one was just proved. This proves (QD.2).

The rational homogenization, polarization, column and Gram maps
have the same fixed multiplicity maps in all declared ranks.
Their coordinate pullback is R-037 EP.3–EP.5, and their
frame-torsor and representation-\(K_0\) transport uses the
primary SGA/EGA/cote locators in R-036 §5.

## 5. Executed checks

The script verify_four_even_tail_degree_three.py expands
the determinant-square row pairings directly. It uses two
different arbitrary fourth-moment extensions of each actual
degree-three split form. The two \(Q_j\) evaluations agree
between those extensions and equal (QD.9)–(QD.10), with zero
higher-row images. Nonunit first coordinates are retained.

Its ranges are \(m=2,3,4\), \(\max(4,m+1)\le a\le8\),
with two independent configurations and both \(Q_j\)'s.
All 56 literal generator pairings and both arbitrary-extension
comparisons pass. The receipt is FOUR_EVEN_TAIL_CUBIC_SCALAR_CHECK.tsv.
It separately computes target and source plethysms by literal
cycle-index expansion and Murnaghan–Nakayama for
\(4\le a\le9\), \(2\le m\le a-1\).
All 27 target and 27 source coefficients agree.
The second receipt is FOUR_EVEN_TAIL_CUBIC_MN_CHECK.tsv.
The polynomial coefficient argument and exact scalar above
prove the unbounded extension and rank laws.

