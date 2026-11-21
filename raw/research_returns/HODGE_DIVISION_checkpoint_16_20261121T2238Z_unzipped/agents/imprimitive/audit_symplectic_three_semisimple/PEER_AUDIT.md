# Independent whole-proof audit: D-HOS20–22

**Result: PASS.** No mathematical repair is required.

Auditor: `/root/imprimitive`, GPT-6 Astra Pro; reasoning effort inherited and
not exposed; run `HODGE_DIVISION`. Actual completion record:
**2026-11-21 21:56:35 UTC**. The independent exact computation completed at
21:56:06.566428 UTC in **0.219303451 seconds**.

## Frozen objects and scope

I read the complete 284-line proof
`agents/g34_eightfolds/bireflection/higher_odd_symplectic_three_semisimple_section.tex`,
SHA-256
`700d6e80b8e7d7183dfd698627b36b116bf0b8a7235b9e8fccc2c17ff294bf6b`.
I also read the complete author checker and its retained result:

- `check_higher_symplectic_three_semisimple.py`, SHA-256
  `56a45fad9189d4ba1760099097907c979eb91f02e65655b161389f7e4f0d10d7`;
- its JSON, SHA-256
  `c2ac05a6eccaed8d06d1234d9ffc849a8949c84814a2719481964b98ba7ba9b5`.

This is a whole mathematical proof and code audit, together with a new
independent finite reconstruction. It is not a claim that finite examples
prove the universal statements. I did not rerun or import the author's
checker. The independent program is `independent_check.py`, with its actual
output in `independent_check.json`.

## D-HOS20: fixed symmetric forms

I checked the passage from a fixed degenerate form to its nondegenerate
quotient, including stability of the radical and absence of eigenvalues
1 and −1 on the quotient. Over an algebraic closure, invariant symmetric
forms pair inverse eigenspaces; nondegeneracy forces equal multiplicities
within each pair. Thus the quotient rank is even. Rank two is excluded by
the exact binary orthogonal orders 4 and 8, since the acting element has
prime order at least five.

For a quotient of rank (r), the fixed-form space has dimension

\[
\sum_jm_j^2\le(\sum_jm_j)^2=r^2/4.
\]

This dimension is unchanged by extension of the coefficient field, because
the defining equations are linear over the original field. I independently
checked the lower bound (3^{r(r-1)/2}) for each nondegenerate form type:
the upper unitriangular matrices give distinct matrices (L^tDL). The
quotient of two such matrices is an upper unitriangular isometry of a
diagonal form, and the first-column orthogonality induction forces it to
be the identity. This remains valid in characteristic three.

For each stable radical, the resulting fraction is at most

\[
3^{r^2/4-r(r-1)/2}=3^{-r(r-2)/4}\le1/9.
\]

Each radical has the same number of quotient forms of the specified type.
Unstable radicals give no fixed forms, so the bound passes to the entire
general-linear orbit. No unproved orbit enumeration is used.

## D-HOS21: semisimple support

I checked the stable isotropic-pair argument, including the precise
restriction-estimate exponent. If (L,L') have dimension (N\ge4), their
embedded symplectic group has natural dimension (2N\ge8). The published
restriction estimate gives (b/a<3^{8/3-N}<1/4) unless it is the full
group, when (b=0). Opposite Siegel radicals are conjugate and generate
that subgroup, so their invariant-space intersection gives

\[
\dim V^U<5a/8.
\]

The full general-linear Levi makes the multiplicities constant on every
nonzero weight orbit. At most one ninth of each such orbit is fixed; every
remaining orbit under the prime-order element has the full prime length.
An eigenvector is determined by one weight component, even when the
intertwiner has scalar phases. Consequently the exact support is greater
than

\[
(4/5)(8/9)(3/8)a=4a/15.
\]

I independently reconstructed the exhaustive primary-space dichotomy.
For odd multiplicative order of 3 modulo the prime, no nontrivial primary
factor is self-reciprocal, and choosing one side of every reciprocal pair
gives opposite stable Lagrangians. For even order (2d), one has

\[
3^d=-1\pmod\ell,\qquad d\ge2.
\]

Each primary factor is self-reciprocal. Trace duality supplies the stated
skew-Hermitian pairing (K); multiplication by an anti-fixed nonzero
scalar makes it Hermitian. I checked the adjoint and trace identities, and
that an isotropic Hermitian line is isotropic for the original alternating
form. Multiplicity at least two supplies a Hermitian hyperbolic plane,
hence the required opposite isotropic pair of dimension (2d\ge4).

If all primary multiplicities equal one, a commuting map preserves each
polynomial kernel and is scalar over its primary extension field. Its
isometry condition is exactly the norm-one equation. Thus the centralizer
in the full symplectic group, including its scalar center, is

\[
(3^d+1)^k\le10^{n/2},\qquad n=dk.
\]

The inequality starts at equality when (d=2) and improves at each step.
Column orthogonality and the previously proved degree bound then give

\[
|\chi(h)|/a\le10^{n/4}/3^{n-1}\le10/27,
\qquad \nu(h)/a\ge17/54>4/15.
\]

The support estimate uses the largest eigenspace and the triangle
inequality; it does not assume that the largest eigenvalue is 1. All
primary cases are covered.

## D-HOS22: actual normalizers and source exclusion

I checked reduction to a noncentral prime-order power modulo the scalar
center, with the central sign adjustment for odd primes. The existing
order-three, involution, and square-minus-identity estimates combine with
D-HOS21 to give (2a/9) in even half-rank and (19a/104) in odd half-rank.

For a nonselfdual factor, the only compatible factor normalizers are
scalar times inner: the unique nontrivial diagonal outer action is class
inverting. This is the exact previously reviewed D-HOS15 interface, rather
than an assumption about all automorphisms fixing the module. Convolution
retains an active factor's support fraction, while a genuine factor
permutation has the stronger quarter bound. A nonidentity scalar has full
actual moving rank.

I checked the geometric Euler and dimension arguments on the actual
induced variation. Genus at least two is impossible; genus one has at most
six genuine marked points and period rank at most six. Rank nine therefore
requires genus zero, at least twelve genuine inertias, and moving sum

\[
D=2e+6.
\]

The two exact degree ceilings are (e\le9) and (e\le156/5), contradicted
by (e\ge27) and (e\ge81), respectively. Different factor ranks,
represented central quotients, compatible permutations, and larger
inducing character fields are allowed. No selfdual structure is silently
imposed in this part of the proof. In a transitive core the factor modules
are either all selfdual or all nonselfdual; the former case is the already
reviewed D-HOS12. The claimed higher characteristic-three closure follows
in the stated main-source scope. Small ranks remain in their separate
earlier results.

## Published inputs actually read

The following complete invoked primary passages were read in this run
during the immediately preceding HOS17–19 audit and were reused here with
their precise scopes. No new proof of a published classification result
is claimed.

1. Larsen–Shalev–Tiep, *The Waring problem for finite simple groups*,
   Annals of Mathematics 174 (2011), 1885–1950,
   DOI `10.4007/annals.2011.174.3.10`.
   [Published full text](https://annals.math.princeton.edu/wp-content/uploads/annals-v174-n3-p10-p.pdf).
   Proposition 4.2.3 and its complete proof, printed pp. 1909–1912,
   including the symplectic step and the final summation; Lemma 4.3.1 and
   its column-orthogonality proof, printed p. 1912. The restriction
   exponent is the natural dimension divided by two, so it becomes (N)
   for the embedded group on (L\oplus L'). The result is used in its
   ordinary simply connected-group scope. Local PDF SHA-256:
   `dbcfed29aab0f3cc01b6e1ab1de97d0e0901bcc8aeeb20a37f2d8a94ac41e99e`.
2. D. E. Taylor, *The Geometry of the Classical Groups*,
   [author full text](https://www.maths.usyd.edu.au/u/don/papers/gcg.pdf).
   The complete invoked Hermitian norm/Witt discussion on printed
   pp. 115–118, especially Lemma 10.2 and Corollary 10.3 on pp. 116–117;
   the binary orthogonal descriptions and orders on pp. 138–141,
   especially Theorem 11.4 and its proof on pp. 139–140. Local PDF SHA-256:
   `825201a4831659f957bf30156f04e85ab3746c01d942c670284071c68b41e30e`.

The earlier HOS degree, opposite-radical, phase, automorphism, and
geometric-factorization interfaces have their existing whole-proof check
records. Their precise hypotheses were checked again at each use here.

## Independent exact reconstruction

The new program imports no author code. It uses Python 3.12.14,
NumPy 2.3.5, SymPy 1.14.0, and python-flint 0.9.0.

- It recovers the ranks and discriminant types of all **59,049** symmetric
  four-dimensional forms from exact integer quadratic Gauss sums, without
  congruence elimination. The order-five element fixes eight nonzero
  forms, all rank four and discriminant 2. Their exact fraction is
  (8/16848=1/2106).
- It independently checks both **729-element** unitriangular families.
- It derives the primary polynomials by exact cyclotomic factoring. A
  different **order-eleven** example has paired degree-five primaries,
  no invariant symmetric form on one primary, and a five-dimensional
  fixed-form space on the paired ten-dimensional symplectic space.
- It constructs the multiplicity-two order-five stable isotropic pair.
- It enumerates all **6,561** polynomial commuting matrices for an
  irreducible order-41 companion on eight dimensions. Exactly **82**
  preserve the independently solved alternating form, agreeing with the
  norm-one centralizer and the universal bound.
- It checks every stated support constant and both source-degree
  contradictions using exact rational arithmetic.

The initial execution stopped at a SymPy factor-list sorting API error:
`TypeError: nmods cannot be ordered`. No mathematical assertion failed.
Only factor extraction was changed to exact FLINT polynomial factoring,
with the same deterministic integer coefficient selection, and the whole
program was rerun successfully. This attempt is retained in `ATTEMPTS.md`
and the output JSON. The universal theorem rests on the separately
audited proof, not these finite witnesses.
