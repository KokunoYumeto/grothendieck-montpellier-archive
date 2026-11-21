# A fixed rational duality and a one-way cross-cycle certificate

## CC-XC15: only one family of cross-cycles remains to be found

Let \(X/\mathbf F_q\) be nonempty, smooth projective, and pure
of dimension \(d\). Fix the concrete rational target
\[
       M=M(X)=(T,e),\qquad T=\bigoplus_\nu h(Y_\nu),
                                                        \tag{CC-XC.D1}
\]
constructed by CC-XC14, where the \(Y_\nu\) are abelian
varieties or finite étale schemes. Put \(r_\nu=\dim Y_\nu\).
All the known abelian-sector inputs and the geometric-Frobenius
conventions of CC-XC11--14 remain in force.
Correspondences involving \(X\) are interpreted in the
homological categories of CC-XC02, with rational cycle
representatives; numerical computations below are confined
to the abelian-sector targets.

**Theorem.** One can effectively construct, using only cycles
between the \(Y_\nu\), a rational isomorphism and its inverse
\[
              \delta_M:M\xrightarrow{\sim}M^\vee(-d).
                                                        \tag{CC-XC.D2}
\]
Choose it once. Let
\(\delta_X:h(X)\xrightarrow{\sim}h(X)^\vee(-d)\)
be the canonical Poincaré-duality isomorphism, and, for
rational cycles
\[
        z_\nu\in\mathrm{CH}^d(X\times Y_\nu)_{\mathbf Q},
        \qquad f=e z:h(X)\longrightarrow M,
                                                        \tag{CC-XC.D3}
\]
form the rational adjoint correspondence
\[
 f^\dagger=
   \delta_X^{-1}\circ f^\vee(-d)\circ\delta_M:
          M\longrightarrow h(X).                       \tag{CC-XC.D4}
\]
The finite rational number
\[
 \mathcal D_X(f)=
   \prod_{i=0}^{2d}
       \det\bigl(f^\dagger f\mid H^i(X_{\bar k},
                                             \mathbf Q_\ell)\bigr)
                                                        \tag{CC-XC.D5}
\]
is computable by intersection numbers and is independent
of \(\ell\ne p\). It is nonzero if and only if \(f\)
is an isomorphism on \(\ell\)-adic cohomology, for one,
and then every, \(\ell\ne p\).

Such an \(f\) exists if and only if the equivalent
abelian-sector membership conditions of CC-XC12 hold.
Consequently, after the terminating construction of
\(M,\delta_M,\delta_M^{-1}\), a one-sided procedure
need enumerate only the forward cycles (CC-XC.D3).
It accepts precisely when \(\mathcal D_X(f)\ne0\).
An accepted \(f\) determines a rational inverse
correspondence valid in every \(\ell\)-adic homological
realization. No separately chosen reverse cross-cycles
on \(Y_\nu\times X\) are required.

Only invertibility of \(\delta_M\) is used. The theorem
does not require it to have any symmetry or positivity
property. For schemes with several dimensions, apply
this statement to the finitely many pure-dimensional
open-and-closed pieces, as in CC-XC14.

### Complete proof

**Existence of the fixed rational duality.** Poincaré
duality for \(X\) gives, in every degree, a
Frobenius-equivariant isomorphism
\[
 H^i(X_{\bar k},\mathbf Q_\ell)
      \simeq
 H^{2d-i}(X_{\bar k},\mathbf Q_\ell)^\vee(-d).
                                                        \tag{CC-XC.D6}
\]
This does not require Frobenius semisimplicity.
On passing to semisimplifications, (CC-XC.D6) shows
that \(R_\ell(M)\) and \(R_\ell(M^\vee(-d))\)
have the same degreewise Frobenius polynomials.
Both are objects of the rational abelian sector.
The rational recognition theorem AQ.16, equivalently
the uniqueness in CC-AG08, therefore gives an actual
rational isomorphism (CC-XC.D2).

Here is a terminating construction of that
isomorphism. Poincaré duality on \(Y_\nu\) identifies
\[
 h(Y_\nu)^\vee(-d)=h(Y_\nu)(r_\nu-d).
 \]
Thus, before applying the two projectors, the forward
and reverse Hom blocks used to find \(\delta_M\) and
its inverse are represented respectively by
\[
 \begin{aligned}
 h(Y_\nu)&\longrightarrow h(Y_\mu)(r_\mu-d):
 &\mathrm{CH}^{r_\nu+r_\mu-d}
                       (Y_\nu\times Y_\mu)_{\mathbf Q},\\
 h(Y_\nu)(r_\nu-d)&\longrightarrow h(Y_\mu):
 &\mathrm{CH}^{d}
                       (Y_\nu\times Y_\mu)_{\mathbf Q}.
 \end{aligned}                                         \tag{CC-XC.D7}
\]
As usual, a codimension outside
\([0,\dim(Y_\nu\times Y_\mu)]\) gives the zero group.
These formulas retain the Tate twists; replacing
the first codimension by a uniform \(d\) would
generally be incorrect.

The finite numerical-basis procedure of CC-XC14
computes every block and its compositions. If a
finite étale factor occurs, its product with an
abelian variety is a finite disjoint union of
abelian varieties over explicit finite extensions
of \(k\), viewed as \(k\)-schemes. A product of two
finite étale schemes decomposes by the finite-field
tensor-product algorithm in the same way, with
zero-dimensional abelian varieties. Cycles on such
a component are the cycles over that component's
constant field. Intersection degrees over \(k\)
are their degrees over the constant field multiplied
by its extension degree. This nonzero rational
factor preserves numerical equivalence and
nondegeneracy of the pairing. Thus the same
known-rank basis search, over those explicit finite
fields and then on their finite direct sum,
computes these blocks as well.

Let \(e'\) be the dual projector \(e^\vee(-d)\)
on \(T^\vee(-d)\). Enumerate rational projected
maps
\[
       u=e' u e:T\longrightarrow T^\vee(-d),\qquad
       v=e v e':T^\vee(-d)\longrightarrow T
 \]
in the computed finite-dimensional numerical
spaces, and test
\[
                        vu=e,\qquad uv=e'.              \tag{CC-XC.D8}
\]
These are decidable finite rational equalities
inside the known abelian sector. Enumerate the
two coefficient tuples jointly, so that no
unsuccessful candidate monopolizes the search.
The rational isomorphism already proved to
exist supplies a pair satisfying (CC-XC.D8);
the search therefore terminates. Rational cycle
representatives of that pair give
\(\delta_M,\delta_M^{-1}\).
Numerical--homological equality on this sector
makes them mutually inverse in every
\(\ell\)-adic realization.

**The determinant test.** Duality of rational
correspondences is given by transposition with
the indicated Tate twists. Thus (CC-XC.D4)
is computable from the forward cycles, the
fixed \(\delta_M\), and the diagonal duality
of \(X\). It is a rational correspondence
from \(M\) to \(h(X)\).

Fix a prime \(\ell\ne p\), and choose bases
of the total cohomology spaces \(V=H^*(X)\)
and \(W=R_\ell(M)\), with the corresponding
dual bases. Let \(A:V\to W\) be the matrix
of \(f\), and let \(B_X,B_M\) be the
invertible matrices of the two dualities,
after choosing a basis of the one-dimensional
Tate twist. Both spaces have the same
dimension by CC-XC11. The total matrix of
\(f^\dagger f\) is
\[
                         B_X^{-1}A^{\mathrm t}B_M A.
                                                        \tag{CC-XC.D9}
\]
Consequently
\[
       \det(f^\dagger f)
           =\det(B_X)^{-1}\det(B_M)\det(A)^2,
                                                        \tag{CC-XC.D10}
\]
and it is nonzero exactly when \(A\) is
invertible. This identity is used on the
total cohomology: duality pairs degree \(i\)
with degree \(2d-i\), so it does not assert
a separate square identity for each
individual degree. Every correspondence
in (CC-XC.D4) respects the cohomological
degree, so the determinant on the left is
the product in (CC-XC.D5).

The endomorphism \(f^\dagger f\) is a
rational algebraic correspondence on the
smooth projective \(X\). CC-XC05 computes
its characteristic polynomial in every
degree by rational Frobenius projectors,
intersection traces and Newton's identities.
Therefore (CC-XC.D5) is a rational,
prime-independent computable number.
If it is nonzero at one prime, it is
nonzero at all; (CC-XC.D9) then shows
that \(f\) is an isomorphism in every
realization.

Cayley--Hamilton, degree by degree and
combined by those rational projectors,
gives a rational correspondence \(u_X\)
acting as \((f^\dagger f)^{-1}\)
in every realization. Hence
\[
                             u_X f^\dagger              \tag{CC-XC.D11}
\]
is a rational inverse of \(f\) in each
homological category. This proves all
assertions about an individual candidate.

Finally, if the membership condition of
CC-XC12 holds, that theorem supplies a
rational forward isomorphism \(f\) to
this fixed target. The fixed-duality
calculation makes its (CC-XC.D5)
nonzero. Conversely any successful
test gives an isomorphism to \(M\)
by (CC-XC.D11), and hence membership.
Enumerating the rational cycles in
(CC-XC.D3), and running the finite
test, therefore halts exactly in the
asserted cases. No conclusion follows
from a search that has not halted.
\(\square\)

The rational verifier is defined through
intersection traces. Its construction
does not require a
\(\mathbf Q\)-valued fibre functor on
the entire rational abelian category.
The arbitrary-variety problem is now
the existence of one family of forward
cross-cycles passing this explicit
quadratic-composition determinant test.
All target, projector, and duality
data are obtained in the terminating
abelian-sector stage.

## Exact dependencies and source locators

This is a complete deduction from
AQ.16 and CC-AG08 (rational recognition),
CC-XC11 (the rational spectral target),
CC-XC12 (rational all-prime
correspondence certificates), CC-XC14
(effective numerical Hom bases on
the abelian sector), and CC-XC05
(intersection-trace verification).
Their primary hypotheses are retained.

For the classical duality and
composition conventions, the
directly inspected primary
locators are Milne (1994), corrected
2019 author version, §1, p. 4
for correspondence composition,
and the proof of Proposition 1.1,
p. 6, for \(h(Y)^\vee=h(Y)(\dim Y)\),
together with the exact
codimension convention in AQ.15.
The computation uses
Poonen--Testa--van Luijk (2015),
Propositions 8.1--8.2, Lemma 8.7,
Theorem 8.15(b), and Remark 8.18,
author pp. 10--14, exactly as scoped
in CC-XC14. No new external
classification theorem is required.

Milne, J. S. (1994). Motives over
finite fields. In U. Jannsen,
S. L. Kleiman, & J.-P. Serre
(Eds.), *Motives* (Proceedings
of Symposia in Pure Mathematics,
Vol. 55, Part 1, pp. 401--459).
American Mathematical Society.
Corrected author version:
https://www.jmilne.org/math/xnotes/Seattle1.pdf

Poonen, B., Testa, D., &
van Luijk, R. (2015). Computing
Néron--Severi groups and cycle
class groups. *Compositio
Mathematica, 151*(4), 713--734.
https://doi.org/10.1112/S0010437X14007878
Author manuscript:
https://math.mit.edu/~poonen/papers/compute_ns.pdf
