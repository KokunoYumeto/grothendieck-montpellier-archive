# The charged incidence algebra and the actual frame Rees algebra

## T-053. Multiplication, a quadratic degeneration, and its exact finite-group obstruction

Let \(m\ge3\), \(1\le r\le m-2\), \(F=\mathbf Q^r\),
and \(E=\mathfrak h_m\). Retain T-049's frame ideals
\(I_i=(\ell_i\otimes F)\) and
\(J_k=\bigcap_i I_i^k=(J_1)^k\subset
S=\operatorname{Sym}(E\otimes F)\). Define
\[
\mathcal P=\mathbf Q[X_{ai},Y_i],\qquad
R_a=\sum_{i=1}^m X_{ai}Y_i,\qquad
\mathcal B=\mathcal P/(R_1,\ldots,R_r).
\tag{IR.1}
\]
Give \(X_{ai}\) column charge \(e_i\), \(Y_i\) column
charge \(-e_i\), and give \(X_{ai}\) row weight
\(\varepsilon_a\), \(Y_i\) row weight zero. The relations
have charge zero and row weights \(\varepsilon_a\).
There is an actual \(GL(F)\times S_m\)-equivariant graded
algebra isomorphism
\[
\boxed{\mathcal R(J_1)=\bigoplus_{k\ge0}J_kt^k
\simeq\bigoplus_{k\ge0}\mathcal B_{(k^m)}.}
\tag{IR.2}
\]
The degree \(k\) on the right is the equal nonnegative charge;
polynomial degree in \(S\) corresponds to \(X\)-degree.
Every row-weight component has the explicit positive count in
(IR.8), using at most \(2^r\) bounded integer polytopes of
\(rm+m\) variables. These count the entire indicated torus
weight space. The highest-type and Specht projectors that give
individual plethysms remain the explicit ones of T-052.

In the displayed coordinates, no monomial initial ideal of
\((R_1,\ldots,R_r)\) is preserved by the literal column
permutation action of \(S_m\). The proof in §4 is a
degree-two orbit calculation for this specified action.

## 1. The algebra map and every grading

In \(\mathbf Q[Z_{ai}]\), put
\(D_k=\bigotimes_i\operatorname{Sym}^{\ge k}F\) and
\(L_a=\sum_i Z_{ai}\). On a polynomial with block degrees
\(d_i\ge k\), use the charge map of T-052,
\[
\Phi_k(f)=f(X)\prod_iY_i^{d_i-k}.
\tag{IR.3}
\]
It is linear on the direct sum of block-homogeneous pieces.
Since each \(R_a\) has charge zero,
\[
\mathcal B_{(k^m)}
=\mathcal P_{(k^m)}/\sum_aR_a\mathcal P_{(k^m)}.
\]
The equations \(\Phi_k(L_af)=R_a\Phi_k(f)\) therefore
give the component isomorphism
\(D_k/LD_k\simeq\mathcal B_{(k^m)}\).
T-049 identifies its left side with \(J_k\) by literal
substitution \(Z_{ai}\mapsto\ell_i\otimes f_a\).

For \(f\in D_k\) and \(g\in D_l\), first take them
block-homogeneous with degrees \(d_i\), \(d'_i\).
Then \(fg\in D_{k+l}\) and
\[
\Phi_k(f)\Phi_l(g)
=f(X)g(X)\prod_iY_i^{d_i+d'_i-k-l}
=\Phi_{k+l}(fg).
\tag{IR.4}
\]
Bilinearity proves the same identity for all \(f,g\).
The multiplication in \(D_k/LD_k\) maps to multiplication
of their substituted polynomials in \(J_k\). Hence (IR.4)
proves multiplication compatibility across every pair of degrees,
and proves (IR.2), including its unit at \(k=0\).

In particular the degree-zero coefficient algebra map sends
\(\ell_i\otimes f_a\) to \([X_{ai}Y_i]\); the relations
\(\sum_i\ell_i=0\) map to \(R_a=0\). A generating
degree-one element of the Rees algebra has the concrete image
\[
t\prod_{i=1}^m(\ell_i\otimes f_{a_i})
\longmapsto\prod_{i=1}^m X_{a_i i}.
\]
These formulas specify the algebra map on generators; their
well-definedness and bijectivity are exactly (IR.3)–(IR.4) and
the proved component quotient.

The maps preserve row weights, \(X\)-degree and slot
permutations. At equal charge \(k\), the \(Y\)-degree
is forced to be \(N-mk\) for \(X\)-degree \(N\).
The full \(GL(F)\) action is also preserved: the \(R_a\)'s
transform as \(F\), and both homogenization and substitution
commute with row changes of basis. Thus the torus gradings and
the larger equivariance have distinct, specified roles in (IR.2).

For a scheme description, let \(T=(\mathbf G_m)^m\) act
with the stated charges, and introduce a variable \(z\) of
charge \((-1,\ldots,-1)\). Then
\[
\mathcal R(J_1)\simeq(\mathcal B[z])^T,
\qquad f\in\mathcal B_{(k^m)}\longmapsto fz^k.
\tag{IR.5}
\]
Indeed an invariant polynomial has exactly these charge-homogeneous
terms, with \(k\ge0\) because its \(z\)-exponent is
nonnegative. Formula (IR.4) makes this identification an algebra
map. The inclusion of invariant rings defines the actual affine
quotient morphism from the incidence scheme \(XY=0\), with
this extra affine coordinate, to \(\operatorname{Spec}\mathcal R(J_1)\).
Slot permutations fix \(z\) and normalize \(T\), so this
morphism retains their action. T-049's explicit Rees charts and
relative Proj construction therefore apply to this same algebra.

## 2. A complete quadratic Gröbner calculation

Use a graded monomial order: compare total degree first, then
the weight assigning one to \(X_{aa}\), \(1\le a\le r\),
and zero to every other variable, then a fixed lexicographic
order. It gives
\[
\operatorname{in}(R_a)=X_{aa}Y_a,
\qquad
\operatorname{in}(R_1,\ldots,R_r)
=(X_{11}Y_1,\ldots,X_{rr}Y_r).
\tag{IR.6}
\]
Here is a direct normal-form proof of the second equality.
Write \(M_a=X_{aa}Y_a\) and
\(T_a=-\sum_{i\ne a}X_{ai}Y_i\), and replace every
factor \(M_a\) by \(T_a\). Each replacement strictly
decreases the total degree in the diagonal variables
\(X_{11},\ldots,X_{rr}\), since no \(T_a\) contains
any of these variables. Thus rewriting terminates. The leading
monomials are pairwise coprime. If two different rules apply to
a monomial \(qM_aM_b\), applying them in either order gives
\(qT_aT_b\). The case of two occurrences of the same rule
has the identical replacement. Induction on diagonal-variable
degree therefore proves that every sequence of reductions has
the same linear normal form: after either first rule, apply the
other, and use the induction hypothesis for every lower-degree
term. This argument extends linearly to polynomials.

The normal form kills every multiple of \(M_a-T_a=R_a\),
and every reduction preserves its residue modulo the relation
ideal. Hence the standard monomials give a basis of the quotient.
Moreover every rewriting step lowers the chosen monomial order.
A relation with a standard leading monomial could not reduce to
zero, since lower monomials never create that leading monomial.
This proves (IR.6), including the asserted Gröbner-basis property.
Every reduction preserves row weight, column charge and the two
degrees in \(X\) and \(Y\).

This also proves that \(R_1,\ldots,R_r\) is a regular
sequence, without a dimension inference. Suppose \(f\) is a
nonzero standard representative modulo the first \(a-1\)
relations. The leading monomial of \(R_af\) is
\(M_a\operatorname{in}(f)\). Since \(M_a\) uses no
variable in the previous leading monomials, that product is not
divisible by any of them. Thus \(R_af\) is nonzero modulo
the preceding relations. This is the required injectivity at
each step.

The degeneration itself is explicit. Set
\[
\mathscr B=\mathbf Q[s,X,Y]\big/
\left(X_{aa}Y_a+s\sum_{i\ne a}X_{ai}Y_i:1\le a\le r\right).
\tag{IR.7}
\]
The same proof works over \(\mathbf Q[s]\), replacing
\(M_a\) by \(sT_a\): the two possible reductions of
\(M_aM_b\) both give \(s^2T_aT_b\), and termination
uses the same diagonal-variable degree. The standard monomials
therefore form a free \(\mathbf Q[s]\)-basis. In particular
this is a flat family. Its fiber at \(s=0\) is the monomial
quotient in (IR.6), and its fiber at \(s=1\) is \(\mathcal B\).
Over \(s\ne0\), the map from (IR.7) to
\(\mathcal B[s,s^{-1}]\) sends its \(X_{aa}\) to
\(sX_{aa}\), and fixes all other \(X\)'s and \(Y\)'s;
the inverse sends the original \(X_{aa}\) to
\(s^{-1}X_{aa}\). It sends each relation to \(sR_a\).
These are the exact general-fiber isomorphisms.

Every row-weight and charge piece is free with its indicated
standard basis. Selecting the equal nonnegative charge pieces
therefore gives a flat algebra family whose general fiber is
the Rees algebra in (IR.2). These maps retain the stated torus
gradings; their behavior under the full permutation action is
settled separately in §4.

## 3. The literal bounded polytopes

Fix \(k\ge0\) and a row weight
\(\eta=(\eta_1,\ldots,\eta_r)\in\mathbf Z_{\ge0}^r\).
For each \(A\subseteq\{1,\ldots,r\}\), use integer
variables \(u_{ai}\) and \(v_i\), with constraints
\[
\begin{gathered}
u_{ai}\ge0,\quad v_i\ge0,\qquad
\sum_i u_{ai}=\eta_a,\qquad
\sum_a u_{ai}-v_i=k,\\
a\in A:\quad u_{aa}=0,\ v_a\ge1,\qquad
a\notin A:\quad v_a=0.
\end{gathered}
\tag{IR.8}
\]
Call this rational polytope \(\mathscr P_{A}(\eta,k)\).
It is bounded: each \(u_{ai}\le\eta_a\), and the column
equations give \(0\le v_i\le|\eta|\). Its point
\((u,v)\) gives the monomial \(X^uY^v\). The row and
charge equations give exactly the required weight, and the last
conditions guarantee that no \(X_{aa}Y_a\) divides it.
Conversely every standard monomial has the unique tag
\(A=\{a\le r:v_a>0\}\), and gives exactly one point of
(IR.8). Thus there is a proved bijection and
\[
\boxed{\dim(\mathcal B_{(k^m)})_\eta
=\dim(J_k)_\eta
=\sum_{A\subseteq[r]}
\#\bigl(\mathscr P_A(\eta,k)\cap\mathbf Z^{rm+m}\bigr).}
\tag{IR.9}
\]
If \(|\eta|<mk\), summing the column equations forces
\(\sum_i v_i<0\), so every polytope is empty. The zero
weight at \(k=0\) has its single point in the empty tag.

This also identifies precisely which representation-theoretic
sum the count evaluates. Put \(N=|\eta|\), \(b=N-mk\).
When \(b<0\), all the spaces and counts are zero by the
summed charge equation. For \(b\ge0\),
write \(K_{\alpha,k}\) for T-052's ordinary multiplicity
space for the current row dimension. When \(r<m-2\), pad
\(\alpha\) by zeros and add zero-degree \(X\) rows.
Inclusion of polynomials independent of those rows identifies
the highest multiplicity spaces literally: the new lowering
and compact raising equations vanish, and their zero row weights
force every polynomial in the enlarged space to be independent
of those rows. Thus this is the space of T-052 with the padded
partition. The actual \(GL(F)\times S_m\) decomposition gives
\[
\dim(J_k)_\eta
=\sum_{\substack{\alpha\vdash N\\\ell(\alpha)\le r}}
\dim(S_\alpha F)_\eta\;\dim K_{\alpha,k}
=\sum_{\alpha,\tau}
K_{\alpha,\eta}\,\dim[\tau]\,
\dim\operatorname{Hom}_{S_m}([\tau],K_{\alpha,k}).
\tag{IR.10}
\]
To specify every last factor, set
\[
\gamma=(\alpha_1,\ldots,\alpha_r,0^{m-r-1},-b),
\quad t=\alpha_1,\quad n=t-k,\quad
\lambda=t\mathbf1-\operatorname{reverse}(\gamma).
\]
For a nonzero component, \(N\ge mk\), whence
\(t\ge N/r\ge k\). Thus \(n\ge0\), and
\(\lambda\) is a partition of \(mn\), with
\(\lambda_2=t\). The zero partition has \(t=k=n=0\).
The actual zero-row inclusion just given, followed by T-052's
column pairing and rational balanced dual map, yields
\[
\dim\operatorname{Hom}_{S_m}([\tau],K_{\alpha,k})
=p_{\tau^{(t)},(t-k)}^\lambda,
\qquad
\tau^{(t)}=\begin{cases}\tau&t\text{ even},\\
\tau'&t\text{ odd},\end{cases}
\]
where \(\tau'\) is the conjugate partition. The finite twist
is exactly \(\operatorname{sgn}^t\).
Equation (IR.10) therefore specifies both positive weights and
every plethysm label in the sum. The individual factors are
obtained by the highest-type and Specht maps in T-052;
(IR.9) counts their displayed weighted sum.

## 4. The narrowly stated permutation obstruction

Let \(\prec\) be any monomial order in the fixed coordinates
of (IR.1), and set \(I=(R_1,\ldots,R_r)\). Its degree-two
space is exactly the \(r\)-dimensional span of the \(R_a\)'s.
Consequently \(\operatorname{in}_\prec(I)_2\) is an
\(r\)-dimensional monomial space. Every one of its monomials
is \(X_{ai}Y_i\) for some \(a,i\): these are all the
monomials that occur in the degree-two relations. There are no
relations in smaller degree.

The column-permutation orbit of any such monomial is
\(\{X_{aj}Y_j:1\le j\le m\}\), a set of exactly
\(m\) distinct monomials. A permutation-stable monomial
space containing one must contain all of them. This would force
\(r\ge m\), contrary to \(r\le m-2\). Hence
\[
\boxed{\operatorname{in}_\prec(I)
\text{ is not stable under the literal }S_m
\text{ column action for any such monomial order}.}
\tag{IR.11}
\]
This disproves the particular proposal that standard monomials
from a monomial degeneration in these coordinates inherit that
same slot-permutation action. It makes no claim about a change
of coordinates, other equivariant filtrations, or the already
proved positive formulas. The original quotient and the Rees
algebra retain their actual \(S_m\) actions through (IR.2).

## 5. Exact resolution and Grothendieck transport

The regular sequence proved in §2 gives the actual finite
\(GL(F)\times GL(W)\)-equivariant free resolution
\[
0\longrightarrow\mathcal P\otimes\Lambda^rF
\longrightarrow\cdots\longrightarrow
\mathcal P\otimes F\longrightarrow\mathcal P
\longrightarrow\mathcal B\longrightarrow0,
\tag{IR.12}
\]
where the \(j\)-th term is shifted by \((j,j)\) in
\((X,Y)\)-degree. The differential is
\[
f\otimes(f_{a_1}\wedge\cdots\wedge f_{a_j})
\longmapsto\sum_{h=1}^j(-1)^{h-1}R_{a_h}f
\otimes f_{a_1}\wedge\cdots\widehat{f_{a_h}}
\cdots\wedge f_{a_j}.
\tag{IR.13}
\]
Its charge is zero, \(GL(W)\) fixes each \(R_a\), and
\(GL(F)\) acts on their span as \(F\). These facts prove
equivariance of every differential. Selecting a torus weight is
exact because a rational torus representation is the direct sum
of its weight spaces. Thus each finite bidegree and equal-charge
piece gives, in the representation Grothendieck group of
\(GL(F)\times S_m\),
\[
[(J_k)_N]=[\mathcal H^{[k]}_{N,b}]
=\sum_{j=0}^r(-1)^j
[\Lambda^jF\otimes\mathcal P^{[k]}_{N-j,b-j}].
\tag{IR.14}
\]
The first equality is the actual rational projection of T-052,
and the second is the Euler relation of (IR.12), rather than
an equality inferred from dimension. Under (IR.3), the cyclic
trace of its tensor factors is T-049's factored character.

On \(\operatorname{Spec}\mathcal P\), (IR.12) is a finite
equivariant vector-bundle resolution of the coherent module
defined by the closed incidence immersion. The action is given
by the polynomial coactions specified in (IR.1). Sheafifying
the graded resolution on \(\operatorname{Proj}\mathcal P\)
uses the exact graded sheafification map; T-049 §7 records its
verified EGA and SGA locators. The Rees identification (IR.2)
is a separate algebra isomorphism, so it also induces literal
isomorphisms on its affine scheme and relative Proj charts.
This states the base of each resolution and each geometric map.

## 6. Proof status

The full argument above proves every multiplication and grading,
the specified quadratic Gröbner basis, the flat-family maps,
the standard-monomial/polytope bijection, the degree-two
permutation obstruction and the exact equivariant resolution.
The standalone `charged_incidence_polytopes.py` exports all
integer matrices in (IR.8), and optionally enumerates their
standard monomials. Its reproduction script
`check_charged_incidence.py` passed 151 row-weight/charge cases,
with 4653 literal standard witnesses and unique membership in
the complete tagged constraint systems. The counts matched the
alternating Koszul formula in every case and 104 independently
constructed lowering-matrix nullities. Six exact symbolic
Gröbner calculations checked both the original and parameter
families in three ranks. The receipt is
`CHARGED_INCIDENCE_RECEIPT.json`.

The root and archive agents read the whole proof and passed its
algebra, flat family, polytopes and obstruction. The archive
agent also completed its review of every added lower-rank label
and the direct diamond proof, recorded as A-062. Its separate
literal row-composition/polytope enumeration matched the
exterior-Koszul truncated counts in 418 cases, with 15042
standard monomial points and 220 forced-empty endpoints, in
ranks \((r,m)=(1,3),(1,4),(2,4),(2,5),(3,5)\).
The independent receipt is
`work/archive/CHARGED_INCIDENCE_POLYTOPE_RECEIPT.json`.
Those executed comparisons are distinguished from the complete
mathematical readings.
