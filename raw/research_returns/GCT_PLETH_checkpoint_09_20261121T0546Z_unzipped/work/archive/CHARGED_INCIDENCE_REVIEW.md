# Independent audit of the charged incidence and Rees algebra

Statement **A-062**, reviewing the entire T-053 report,
work/theta/charged_incidence_rees_report.md, IR.1–IR.14,
including its amended direct diamond proof and explicit
smaller-rank plethysm labels.
Checked 21 November 2026 by GPT-6 Astra Pro,
run /root/archive_audit; effort setting not exposed.

**Complete proof PASS.** The maps preserve the stated gradings
and multiplication, the degeneration is explicitly flat, and
the row-weight polytopes have the asserted bijection. The
permutation obstruction concerns the specified monomial initial
ideals and literal column action, with a complete degree-two proof.

## 1. Rees multiplication and the affine quotient

For block degrees \(d_i\ge k\), the charge homogenization
sends \(f\) to \(f(X)\prod_iY_i^{d_i-k}\).
Since \(R_a\) has charge zero, its contribution in an equal
charge component has a coefficient in the same charge component.
Thus the component quotient is exactly
\(D_k/(L_1,\ldots,L_r)D_k\), not a larger saturation.

The T-049 substitution identifies this quotient with \(J_k\).
For degrees \(k,l\), adding the forced exponents proves
\(\Phi_k(f)\Phi_l(g)=\Phi_{k+l}(fg)\).
This gives the actual Rees algebra isomorphism, including its
unit and the coefficient algebra at degree zero. In particular,
\(\ell_i\otimes f_a\) maps to \([X_{ai}Y_i]\), while
\(t\prod_i(\ell_i\otimes f_{a_i})\) maps to
\(\prod_iX_{a_i i}\). These are the correct generator images.

The substitution and homogenization commute with row changes
and column permutations. They preserve row weight, \(X\)-degree
and charge; \(Y\)-degree is forced to be \(N-mk\).
Adding \(z\) with charge \((-1,\ldots,-1)\) identifies
invariants with the terms \(fz^k\), \(k\ge0\).
The resulting ring inclusion gives the actual affine quotient
morphism. Slot permutations fix \(z\) and normalize the
charge torus, so this map retains their action.

## 2. Complete direct normal forms and flat family

For \(M_a=X_{aa}Y_a\), every other term in \(R_a\)
has zero degree in every diagonal variable \(X_{jj}\).
Replacing \(M_a\) by the negative remainder therefore strictly
decreases the total diagonal-variable degree. Termination holds
without an appeal to an unproved algorithmic criterion.

The leading monomials \(M_a\) are pairwise coprime.
The two reductions from \(qM_aM_b\) both reach
\(qT_aT_b\); repeated occurrences of one rule are identical.
Induction on the decreasing diagonal degree proves uniqueness
of every linear normal form. Such a form kills every multiple
of a relation, and each reduction preserves the ideal residue.
The standard monomials are therefore a basis. Because every
step also lowers the displayed monomial order, the initial ideal
is exactly \((M_1,\ldots,M_r)\).

For a nonzero standard representative modulo the first \(a-1\)
relations, the leading monomial of \(R_af\) is
\(M_a\operatorname{in}(f)\). Its new factors are disjoint
from the previous leading monomials, so it remains indivisible
by them and cannot disappear under reduction. This proves each
required nonzerodivisor step, hence the regular sequence.

The same diamond proof works over \(\mathbf Q[s]\),
with rule \(M_a\mapsto sT_a\); both two-rule paths give
\(s^2T_aT_b\). Thus the standard monomials form a free
\(\mathbf Q[s]\)-basis and the family is flat.
The general-fiber map sends the family diagonal coordinate
to \(sX_{aa}\), fixes the other variables, and carries its
relation to \(sR_a\). The inverse uses \(s^{-1}X_{aa}\).
Both preserve all stated torus gradings. Selecting equal
nonnegative charge pieces is a direct sum of free graded
pieces, hence gives the asserted flat Rees family.

## 3. Literal bounded polytopes and smaller-row transport

A standard monomial has exponents \(u_{ai},v_i\).
Its row weights and charge are precisely
\[
\sum_i u_{ai}=\eta_a,\qquad \sum_a u_{ai}-v_i=k.
\]
It avoids \(X_{aa}Y_a\) exactly when \(u_{aa}=0\) or
\(v_a=0\). The unique tag
\(A=\{a\le r:v_a>0\}\) consequently gives all constraints
in IR.8 and their inverse monomial map. There is no duplicate
at \(u_{aa}=v_a=0\), because that index belongs to the
complementary tag. Row sums bound every \(u\), and the column
equations bound every \(v\), so all these polytopes are bounded.
The impossible total degree and the zero-weight constant
endpoints follow immediately by summing the equations.

When \(r<m-2\), padding the row highest weight by zeros
is an actual inclusion of polynomial spaces. The new zero row
degrees force independence from the new variables; the new
compact raising and lowering equations vanish. Thus the highest
multiplicity spaces are literally identified.

The added inverse labels are correct. With
\(\gamma=(\alpha,0^{m-r-1},-b)\), \(t=\alpha_1\),
\(n=t-k\), and
\(\lambda=t\mathbf1-\operatorname{reverse}\gamma\),
one has \(t\ge N/r\ge k\), \(|\lambda|=m(t-k)\),
and \(\lambda_2=t\). This is a nonnegative partition,
including the stated empty case. The exact T-052 column pairing
and finite Gram dual map give the outer transpose at odd \(t\).
Consequently IR.10 identifies every multiplicity, every Kostka
weight and every Specht dimension in the positive weighted sum.
The whole row-weight count is exactly that sum.

The independent script check_charged_incidence_polytopes.py
enumerates the literal row-composition matrices, forces their
\(Y\)-exponents, and assigns their unique standard tags.
It compares them with the separate exterior-Koszul alternating
sum of raw truncated block counts. All **418** cases pass:
**15042** standard monomial points and **220** forced-empty
cases, in ranks \((r,m)=(1,3),(1,4),(2,4),(2,5),(3,5)\).
This includes smaller-row inclusions and zero weight/charge.
The receipt is CHARGED_INCIDENCE_POLYTOPE_RECEIPT.json.

## 4. Exact finite-group obstruction

The degree-two ideal is the \(r\)-dimensional span of the
\(R_a\)'s. Their supports consist only of \(X_{ai}Y_i\).
For any monomial order, the degree-two initial space has the
same dimension and all its monomials belong to this set.
This remains true for an order that is not degree-compatible:
the ideal is homogeneous, and a degree-two leading monomial
comes from its degree-two homogeneous component. No relation
exists in smaller degree.

The literal column-permutation orbit of \(X_{ai}Y_i\)
has exactly the \(m\) distinct monomials \(X_{aj}Y_j\).
A stable monomial subspace containing one would contain them
all. Since \(1\le r\le m-2\), its dimension \(r\) makes
that impossible. This proves IR.11 for the stated action and
coordinates. It does not assert a failure for other coordinate
systems or other constructions; the original quotient keeps
the exact permutation action supplied by the algebra map.

## 5. Equivariant resolution and geometric transport

The proved regular sequence gives the written Koszul resolution.
The relation span transforms as \(F\), so its exterior factors
are \(\Lambda^jF\), with bidegree shift \((j,j)\).
The actual differential is multiplication by \(R_{a_h}\)
with its exterior deletion sign. The compact \(GL(W)\)
fixes every \(R_a\), and each has charge zero. These facts
prove the full equivariance and the exact charge extraction.

The selected weight and bidegree spaces are exact direct summands
for the rational torus action. Taking their Euler classes gives
IR.14 with the correct row exterior factors and degrees.
The first equality is T-052's actual rational harmonic projector.
Under homogenization, its cyclic tensor trace agrees with the
factored T-049 truncated character.

The free resolution is used on \(\operatorname{Spec}\mathcal P\)
or after exact graded sheafification on
\(\operatorname{Proj}\mathcal P\). The report does not
assert preservation of that resolution by a nonflat pullback
to a different Proj. The Rees comparison is a separate actual
graded algebra isomorphism, hence identifies its own affine
scheme and relative Proj charts. Every geometric base and
every map in this transport is therefore specified.

