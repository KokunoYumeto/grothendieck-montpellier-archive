# Independent complete audit of the charged oscillator comparison

Statement **A-061**, reviewing T-052,
work/theta/oscillator_charge_report.md, all OC.1–OC.31
and every endpoint and group convention.
Checked 21 November 2026 by GPT-6 Astra Pro,
run /root/archive_audit; effort setting not exposed.

**Complete proof PASS.** The charge space, frame quotient,
harmonic kernel and balanced Schur space are related by the
specified maps. Metaplectic shifts are retained, and the finite
permutation action is explicitly untwisted. An independent
argument below proves the irreducibility and direct sum in OC.31.

## 1. Parameters and first-row endpoints

For \(e=0\), summation gives
\[
N=(m-1)\lambda_2+\lambda_1-mn,\qquad
N-mk=\lambda_1-\lambda_2.
\]
For \(e>0\), \(n_0=\lambda_2,k=0\), and
\(\lambda_1^0=\lambda_2+N\ge\lambda_2\).
Thus the shifted shape is a partition of \(mn_0\), and all
degrees are nonnegative. In both cases
\(b=N-mk=\lambda_1^0-\lambda_2\).

The first-row map is literal multiplication by \(u^e\), where
\(u=\prod_i x_i\), in the balanced flag algebra. Products of
height-at-least-two minors have degree at most \(\lambda_2\)
in every block. Each first coordinate therefore has excess
degree at least \(e\), proving divisibility by \(u^e\) and
the polynomial inverse. The product \(u\) is fixed by column
permutations, so it introduces no sign. The pure row, the empty
partition at \(n=0\), and \(m=3,r=1\) are included.

## 2. Operators, adjoints and real dual pair

The Weyl relations give exactly
\[
[C_a,R_b]=\sum_iX_{bi}\partial_{X_{ai}}
+\delta_{ab}(N_Y+m)=A_{ba}-\delta_{ab}A_{00}.
\]
Together with the compact brackets this verifies every block
of the matrix-unit relation. The two terms of \(G_{ij}\)
are the standard and dual \(\mathfrak{gl}_m\) actions.
Their commutators with \(R_a\) cancel literally, as do
their derivative commutators with \(C_a\). The common center
has exactly the scalar \(m(r-1)/2\), and every \(A\)
preserves each individual charge.

The factorial monomial form gives \(R_a^\dagger=C_a\)
and all adjoints in OC.11. In \(\mathfrak u(r,1)\),
the two mixed matrix coefficients are complex conjugates,
while the represented operators are negative adjoints.
This gives the asserted skew-adjoint real action. The compact
real form follows from \(B_{ij}^\dagger=B_{ji}\).

A real-linear commutant of \(U(r,1)\) commutes with its
scalar \(i\), hence is complex-linear. The phases, positive
unitaries and a mixed boost span the matrix units on
\(H=\mathbf C^{r,1}\), so its complex commutant on
\(H\otimes W\) is \(1\otimes\operatorname{End}W\).
Preserving the imaginary Hermitian form and complex linearity
recovers its real part, giving exactly \(U(m)\). The reverse
centralizer is obtained by the same calculation.

The positive compatible complex structure is \(i\) on the
positive part and \(-i\) on the negative part. The latter
turns its creation representation into \(W^*\), giving
\(F\otimes W\oplus W^*\). Its determinant is
\[
(\det a)^m z^{-m}(\det g)^{r-1}.
\]
The vacuum square and its half derivatives therefore give
every shift in OC.7, including the negative-block sign.

The source cover convention was checked in A-059, and this
report retains it. Removing the compact vacuum character gives
the ordinary polynomial \(GL(W)\) action. For even \(r\),
tensoring by its inverse on the pullback cover cancels the
central kernel and descends to literal permutation matrices.
For odd \(r\), the integral determinant character gives the
stated section and sign. No fractional sign character of
\(S_m\) is asserted.

## 3. Charge, quotient and harmonic projection

A block-homogeneous monomial of degree \(d_i\ge k\) has
forced \(Y_i\)-exponent \(d_i-k\). Hence OC.14 is a
bijection, with inverse erasing \(Y\), and commutes with
row changes and column permutations. Raising the block degree
by one raises its \(Y_i\)-exponent by one, proving exactly
\(\Phi_k(Z_{ai}f)=X_{ai}Y_i\Phi_k(f)\). Thus diagonal
multiplication is transported to the \(R_a\)'s.

The all-degree T-049 quotient theorem applies at
\(\dim F=m-2\). Its substitution
\(Z_{ai}\mapsto\ell_i\otimes f_a\) identifies the actual
product/intersection ideal in OC.16. This proves OC.17
with its maps and degree shifts.

On the finite charge-degree space, the denominator's
orthogonal complement is exactly the common lowering kernel.
The operator \(T=\sum_aR_aC_a\) is positive semidefinite;
its kernel is that common kernel and its range is the
denominator. It commutes with the ordinary row action:
the terms in \([A_{bc},\sum_aR_aC_a]\) cancel. It also
commutes with column permutations. Thus the polynomial
projector is equivariant even though the full \(GL(F)\)
action is not unitary for the chosen form.

For \(\det(t-T)=t^s q(t)\), \(q(0)\ne0\),
diagonalizability proves that \(q(T)/q(0)\) is identity
on the zero eigenspace and zero elsewhere. Its coefficients
are rational. Harmonic inclusion followed by the quotient is
its inverse comparison. Invertible, zero and zero-dimensional
operators give exactly the stated endpoints.

The rightmost derivative in
\((N_i-k+1)\partial_{Z_{ai}}\) acts first; the resulting
coefficient is \(d_i-k\). It vanishes at the truncation
boundary. The transported norm
\(\prod_i u_i!(d_i-k)!\) independently verifies its adjoint
against diagonal multiplication.

## 4. Harmonic irreducibles and all dual maps

Cauchy extraction gives a row type \(S_\alpha F\) and the
mixed tensor \(S_\alpha W\otimes\operatorname{Sym}^bW^*\).
The row contraction equations are exactly the traceless
conditions after Young projection. The primary §5.2 and
Appendix A derivation identifies their kernel as the rational
irreducible of highest weight \((\alpha,0,-b)\).
At \(b>0\), \(\ell(\alpha)+1\le m-1<m\), strictly
inside the source's tensor range. The equality sentence
refuted in A-059 is not used. At \(b=0\), this is Cauchy.

The vector \(Y_m^b\prod_j\Delta_j^{\alpha_j-\alpha_{j+1}}\)
is nonzero, has the two required highest weights and is
harmonic: its \(Y\)-derivative uses a column absent from
its \(X\)'s. Both compact raising actions kill the initial
minors. This fixes the actual normalized summand map in
OC.20. Taking its literal equal-weight space gives OC.22.

The identity
\(\gamma=\lambda_2\mathbf1-\operatorname{reverse}(\lambda^0)\)
holds coordinate by coordinate. Exterior-column multiplication
in the \(m\)-by-\(H\) rectangle gives the nonzero perfect
pairing to \((\det W)^H\). Twisting the complementary
factor by \((\det W)^{-b}\) gives OC.24. Its charge is
\(k-\lambda_2=-n_0\), yielding OC.26 with exactly
\(\operatorname{sgn}^{\lambda_2}\).

The remaining dual is handled by the displayed Gram map.
The rational Young image and its balanced subspace have
positive definite tensor forms over the reals, hence
nondegenerate rational restrictions. Permutation matrices
preserve the forms and commute with the tensor-position Young
idempotent. The map to the dual is therefore a rational
\(S_m\)-intertwiner. Composing it with the first-row map,
determinant pairing and harmonic embedding proves OC.4.

## 5. One-column module and an independent proof of OC.31

The one-column homogenization gives the four operators OC.29
literally. Its lowest positive compact type is
\(\operatorname{Sym}^kF\) with the half vacuum twist, and
its negative compact weight is \(-1/2\).
A submodule has a least nonzero homogeneous degree, since
a polynomial in the degree operator isolates components.
At degree above \(k\), a derivative is nonzero with
coefficient \(d-k\), contradicting least degree.
The complete compact type at degree \(k\) is consequently
present, and coordinate multiplication generates every higher
degree. This proves irreducibility, including \(k=0\).

Tensoring the literal one-column operators gives the complete
multi-column operators and summed shifts. The permutation
action is ordinary tensor-factor permutation, so OC.30 is
an actual intertwiner on a common cover.

An independent algebraic proof of the full decomposition is
as follows. At each finite bidegree the Fischer decomposition is
\[
\mathcal P_{N,b}=\mathcal H_{N,b}
\oplus\left(\sum_aR_a\mathcal P_{N-1,b-1}\right).
\]
The internal sum in parentheses need not be direct. Iteration
shows that every polynomial is generated from harmonics by
raising operators. These commute with \(GL(W)\), so this
is true in each compact isotypic multiplicity space.
OC.20 assigns a compact weight
\(\gamma=(\alpha,0,-b)\) exactly one harmonic degree
and one irreducible lowest row type \(S_\alpha F\).

The energy operator
\[
\sum_aA_{aa}-A_{00}=N_X+N_Y+m(r+1)/2
\]
belongs to the noncompact algebra. Any nonzero submodule of
this multiplicity space has a least homogeneous degree,
after polynomial isolation. Every lowering operator kills
that degree, or gives a lower degree in the same submodule.
It therefore meets the unique harmonic lowest type. Compact
irreducibility supplies that whole type, and raising generation
supplies the whole multiplicity module. Thus each such module
is irreducible. The distinct compact weights and finite-degree
decompositions give the complete algebraic direct sum.

Taking the equal-charge weight and then the finite Specht
Hom space gives precisely OC.31. Both operations commute
with the algebraic direct sum and the noncompact action.
The primary general discussion §5, (5.1)–(5.6), printed
pp.26–27, was also read and agrees. This argument proves the
step directly from the report's finite harmonic decomposition;
it was sent to the author, who is adding it.

## 6. Endpoints and verification scope

At \(b=0\), charge forces every block degree to be \(k\),
so there are no lowering or quotient relations. The complementary
plethysm follows from the same exterior pairing.
At \(k=0\), the diagonal polynomial quotient is the stable
frame algebra. The empty partition gives its single constant
vector. Every asserted endpoint and its comparison with the
previous positive formulas checks.

The author's 1895 commutator checks, 42 nullspace cases,
663 coefficient and trace comparisons and six rational-projector
checks belong to the author's separate receipt. They were not
rerun by this whole-proof event and are not counted as new
independent computations here.

