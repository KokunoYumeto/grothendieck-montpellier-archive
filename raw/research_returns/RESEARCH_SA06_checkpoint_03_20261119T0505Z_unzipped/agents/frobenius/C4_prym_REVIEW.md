# Prym improvement and supplementary independent audits

## 1. Exact new result and limits

The new fragment `C4_prym_addition.tex` proves two numbered statements.

- **C.4m:** Every principally polarized abelian variety of positive
  dimension at most five over an algebraically closed field has
  multiplication by two factoring through a product of Jacobians.
  Characteristic two is included by polarized lifting and specialization
  of an actual integral curve cycle.
- **C.4n:** Every abelian surface satisfies
  `s_J(A) | gcd(2, delta(A))`. Thus an ample line bundle of odd Euler
  characteristic suffices for the exact direct-summand property.
  For Picard rank one and type `(1,d)`, every odd `d` is settled.

This improves the earlier surface bound six to two. In particular,
type `(1,3)` is positive despite the divisor-product index three
computed in C.4l. We have **not** proved the result for every surface
with even delta, and have not found a surface counterexample.
The general threefold bound remains `gcd(120, delta(A))` in this work.
Its possible residual primes are still 2, 3, and 5. We do not claim
that every unhandled case is known to be open in the literature.

## 2. Proof and exact coefficient checks

Beauville's generalized Prym includes a map into the generalized
Jacobian of a nodal curve. Composing with normalization gives a map
`j : B -> product J(C_i)` into an actual product of Jacobians of
smooth curves. Proposition 2.2 identifies the generalized theta as
the pullback of the product theta. Theorem 5.4 gives
`j^* theta_J = 2 Xi` in the Néron–Severi group. Since both
polarizations are principal, the polarized adjoint is an integral
homomorphism and `j^dagger j = [2]` exactly. No finite kernel is
inverted, and no principal polarization on a nonprincipal variety
is silently assumed.

The sum of the images of the normalization curves under `j^dagger`
has cohomology class twice the minimal class. This follows directly
from the associated alternating pairing, or equivalently from
`q lambda_J^-1 qhat = 2 lambda_B^-1`. The proof in the fragment
explains why that pairing determines the full curve cohomology class.

At characteristic two, Oort's valid lifting implication and
Corollary 2.4.2 provide a polarized lift over W(k). A finite base
extension defines the generic integral cycle. Its closures give
an integral special cycle. Fulton's Example 20.3.5 expressly supplies
the commutative diagram with the ell-adic cycle class map for
ell different from two. Numerical equality follows, and Matsusaka
then supplies actual homomorphisms whose composite is `[2]` over k.
No crystalline equivalence or rationally defined retraction is used.

For any fourfold or fivefold X, principalizing ample L and using
the preceding theorem gives `2 chi(L) in I_J(X)`. The ample gcd
lemma gives `s_J(X) | 2 delta(X)`. For the fourfold `A x Adual`,
the Poincaré bundle has Euler characteristic one, hence delta one.
Restriction and projection yield `[2]` on A. The earlier
same-dimensional principalization supplies `[delta(A)]`, and
Bézout gives the final odd-delta criterion.

The fragment includes a finite five-polarization interpolation
formula realizing the gcd construction. It also gives a concrete
alternative: `P tensor H^(72t)` has Euler characteristic congruent
to one modulo three, so a single such principalization and the
existing factorization of six yield a factorization of two.

## 3. Independent review

The cycles agent independently opened Beauville and Oort and checked
both the normalization map and the characteristic-two specialization
argument. Its conclusion was that the proof is sound, including the
finite-kernel issue and use of rational ell-adic equality only to
deduce numerical equality of an already integral cycle.

The script `code/verify_c4_prym_arithmetic.py` checks exact integers
in the finite interpolation formula on a polynomial basis and the
coefficient congruences for the one-polarization construction. This
is an arithmetic certificate only; the geometric existence theorem
comes from the proved construction and the cited primary results.

## 4. Integration instructions and correction to an earlier locator

Insert `C4_prym_addition.tex` after C.4l and before the final
remaining-work paragraph, or put it immediately after the previous
supplement and retain only the new remaining-work paragraph.
The old remaining-work sentence listing types `(1,2)` and `(1,3)`
as unresolved is superseded. A correct replacement is:

> After the Prym improvement in C.4m–n, the untreated surface cases
> in this contribution have even delta, for example Picard-rank-one
> type (1,2). Type (1,3), and all odd types (1,d), are settled
> positively. The analogous general threefold cases at 2, 3, and 5
> remain untreated here.

**Oort–Ueno page correction:** The CWI PDF is the original six-page
preprint with one cover page. Its Theorem 4 is printed on page 2
(PDF page 3), as shown in `output/oort-title-3.png`. It is not the
published pagination 377–381. Our earlier p.381 locator was wrong;
the theorem number and mathematical statement were correct.
`C4_additions.tex` and its local report ledger now use the exact
preprint locator. The parent and cycles agent were notified to
correct their integrated references as well.

The rendered preprint page 3 (`output/oort-4.png`) also expressly
corrects Oort 1971 Theorem 2.4.1: the words "and only if" must be
deleted. Our proof uses only the valid implication from separability
to formal smoothness and the stated lifting corollary. This is now
spelled out in the fragment and bibliography note.

## 5. Other independent audits requested by the parent

### A.1h descent across the finite quadratic field

The parent's determinant descent argument is correct under its
nonemptiness hypothesis: the isomorphism sets before and after
base change to the algebraic closure are torsors under the same
group `Z_p^*`. An equivariant map between nonempty torsors for this
same group is bijective. Naturality under the two field embeddings
then makes the descended determinant rigidification independent of
the choice of embedding. This avoids a finite-field geometric-model
claim. The two `F^2=+p` and `F^2=-p` strata cannot be linked by a
nonzero F-intertwiner: its square relation gives `2p b=0` in a
torsion-free lattice, including at p=2. Thus without compatibility
with geometric base change the strata can carry independent
constants; imposing that compatibility identifies the constants.

### C.2 pencil induction

The lexicographic induction proposed by the parent is sound with
global A-prime available over all algebraically closed extensions,
including the algebraic closure of k(t). The smooth pencil centre
has codimension two. For the exceptional contribution, the fibre
class restricts to `O_{P^1}(1)` on `E=B x P^1`, so the coefficient
of `i_B* beta` is positive one. Weak Lefschetz gives the required
preimage `b0` since `2i-2 < n-2`. The lower-codimension induction
and hard Lefschetz prove its algebraicity from the algebraic class
`L^(k+2) b0`. Finite trace with rational coefficients handles the
generic-fibre descent. No nodal Lefschetz-pencil hypothesis is needed.

### C.2 reduction to critical dimension

The parent's incidence construction is also correct. For
`d=2r+1-n >= 0`, the variety `T=X x P^d` has the critical dimension
`2r+1`. The incidence divisor defined by `sum s_j t_j=0` is smooth
when the common zero locus is a smooth complete intersection:
outside it a fibre derivative is nonzero; on it independence of
the differentials `ds_j` gives a nonzero derivative for every
projective coordinate vector. For d=0 this is just the initial
critical case. On `U=X\Y`, the section s0 trivializes the line
bundle and a triangular projective coordinate change sends the
incidence divisor to the standard hyperplane. Its Gysin image in
the Chow projective-bundle decomposition is exactly divisible by h.
Thus the constant coefficient restricts to zero in CH(U), and
localization puts it in the image of CH(Y). The cohomological
projective-bundle decomposition identifies its class with the
original z. This requires the given hyperplane Y to come from the
very ample embedding in the statement; no extra singular-pencil
assumption enters.

## 6. Opened primary-source ledger

| Key | Exact primary locator | Opened web reference |
|---|---|---|
| frC4Beauville1977 | https://math.univ-cotedazur.fr/~beauvill/pubs/pv.pdf; Proposition 2.2 p.155; Theorem 3.7 p.160; Theorem 5.4 pp.175–176; Theorem 6.5(i) p.178 and Lemma 6.5.2 p.179; characteristic convention p.150 | turn446233183view0; turn284675537view1; turn337819996view0; turn337819996view2 |
| frC4Oort1971 | https://www.numdam.org/item/CM_1971__23_3_265_0.pdf; valid sufficient direction of Theorem 2.4.1 p.286; Corollary 2.4.2 and its proof p.287 | turn385406364view0; turn988083530view0; turn337819996view3 |
| frC4Fulton1998 | https://djvu.online/file/Pl4avuZzLcI6I; Proposition and Corollary 20.3 p.399; Example 20.3.5 p.400, including geometric specialization and ell-adic cycle-class diagram | turn756260425view0; turn115304589view1; turn115304589view2 |
| cyOortUeno1973 | https://ir.cwi.nl/pub/27912/27912.pdf; Theorem4 printed preprint p.2; correction of Oort's iff printed p.3; lifting paragraph printed p.4 | turn446233183view1; local sources/oort_ueno1973.pdf and output/oort-title-3.png, oort-4.png, oort-5.png |
| frC4Mumford1970 | Previously opened primary scan §23, Theorem4 and Corollary1 pp.233–234; see C4_REVIEW.md ledger | turn877907092view0; turn896973874view1; turn896973874view2 |
| cyScaviaSuzuki2025 | Previously opened https://arxiv.org/html/2507.09821v2, Proposition3.4 equations3.1–3.3; see C4_REVIEW.md | turn358199100view1 |

Publisher metadata opened to verify DOIs: Beauville,
https://link.springer.com/article/10.1007/BF01418373,
`turn199065391view0`; Fulton,
https://link.springer.com/book/10.1007/978-1-4612-1700-8,
`turn199065391view1`.

Auxiliary source opened but unnecessary for the final proof:
Mumford, *Prym Varieties I* (1974), §2 equations (2.1)–(2.3),
pp.328–329, and §6 Proposition p.342, at
https://www.dam.brown.edu/people/mumford/alg_geom/papers/1974a--PrymVar-I-NC.pdf,
`turn385406364view1` and `turn988083530view2`.

## 7. Priority and continuing-search status

The result is derived here from classical primary theorems; no
novelty or priority claim is made. Targeted searches for arbitrary
nonprincipal surfaces and direct summands of products of Jacobians
returned the Beckmann–de Gaay Fortman, Voisin, and Scavia–Suzuki
criteria and sources on ramified Prym surfaces, but did not yield
a theorem resolving the remaining even-delta case. This absence
of a search hit is not evidence of an established open problem.

The 2026 matroidal-family obstruction was reopened, including
Theorem1.6 and Definition4.1. Its hypotheses are specific and have
not been verified for the isotypic family `A x Adual`. A possible
rank-of-monodromy limitation is being assessed separately; no
counterexample has been inferred from generic ppav results.
