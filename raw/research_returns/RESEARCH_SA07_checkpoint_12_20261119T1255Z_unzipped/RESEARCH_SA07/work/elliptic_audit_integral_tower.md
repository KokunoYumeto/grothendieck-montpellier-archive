# Independent audit of E.2.23: the simultaneous elliptic integral tower

Auditor: elliptic_splitting, OpenAI GPT-6 Astra, 19 November 2026.
Audited file: `work/agent_elliptic_integral_tower.md`, ET-1–ET-3.
Verdict: the stated construction passes, with exactly its stated diagram scope.
It supplies one actual quartic-swapping Galois element and integral transport
on the entire specified elliptic, CM, Artin and geometric-isogeny diagram.
It does not assert the corresponding construction for arbitrary abelian
simple factors or the full pure diagram.

## 1. The primary adelic open-image input

I independently opened the complete sixteen-page author manuscript of
Davide Lombardo, *An explicit open image theorem for products of elliptic
curves*, at
https://web.dm.unipi.it/lombardo/files/ProductsEC.pdf .
The exact source is Theorem 1.1 and Remark 1.2, printed page 1
(web `turn768574560view0`). I also visually inspected the first page
(`turn294363978view0`): the nonisogeny and endomorphism hypotheses are
over the algebraic closure. The theorem is adelic and includes 2. Its
finite-index conclusion applies to the distinct geometric non-CM
isogeny representatives over Q used in ET-1. The single-factor Serre
input is a previously audited dependency rather than a newly opened
source in this audit.

## 2. Actual independently supported subgroups

The image G is compact, so the finite-index theorem makes it open in
the equal-determinant group. Thus its intersection with the determinant-one
product contains a product congruence neighborhood. In particular the
single-factor, single-prime supported matrices used in ET-1 are actual
elements of G. Actual complex conjugation has an involutory component
of determinant -1 in each elliptic factor. For odd primes its two
eigensummands are integral, using (1+C)/2 and (1-C)/2. At 2 they are
rational summands and the chosen eigenbasis has only finitely many
denominators. Increasing root depth therefore places both conjugated
root groups in the actual congruence neighborhood.

Since complex conjugation is central on Qcm, each commutator [g,C]
comes from Gamma_Qcm. In an eigenbasis its upper and lower parameters
are multiplied by 2. At all primes outside the finite exceptional set,
these are the complete root groups. At an exceptional prime their
positive-depth subgroups suffice. I checked the displayed four-root
diagonal identity by multiplication: it gives diag(1+xy,(1+xy)^-1).
Fixing x at the chosen root depth realizes every diagonal at twice
that depth. The Gauss factorization then realizes every sufficiently
deep determinant-one congruence matrix. Conjugating back loses only
the explicitly bounded denominators of the eigenbasis.

The image N of Gamma_Qcm is compact and therefore closed. It contains
the independently supported groups, hence their full infinite product
by closure of finite products. The cyclotomic determinant is trivial
on Gamma_Qcm, so N lies in the determinant-one product and is open
there. No passage from a Lie algebra to an arithmetic group is used.

## 3. The derived subgroup and Fcm

Each extension K^ab Qcm/Qcm is abelian. Their compositum Fcm/Qcm is
therefore abelian, giving the needed inclusion of the closed commutator
subgroup of Gamma_Qcm into Gamma_Fcm. Equality is unnecessary.

For a compact surjection Gamma_Qcm onto N, the image of that closed
commutator subgroup equals the closed commutator subgroup N': finite
commutators map to finite commutators, and compactness makes the image
closed; conversely each commutator in N has lifts. At a full factor
with prime at least 5, conjugation by diag(2,1/2) gives all upper roots
through the unit 3, and all lower roots through the unit -3/4. These
root groups generate SL2. At a remaining prime choose a deep supported
congruence subgroup in N. The commutator with diag(d,d^-1), d=1+l^a,
gives root depth 2a at odd l and 2a+1 at l=2, taking a at least 2 in
the latter case. The same diagonal and Gauss calculation supplies a
supported open subgroup in N'. Closure again gives an open product.
Consequently the actual image of Gamma_Fcm is open in the product.

## 4. Nested selection with previous full Tate matrices fixed

At each finite stage, the subgroup Gamma_Fcm intersect Gamma_P has
closed finite-index image in the open product from the preceding step.
It contains a product congruence subgroup. Intersecting with the kernels
of the first n entire adelic matrix maps still leaves the last supported
congruence factor. Thus the image on factor n+1 of the exact previous
matrix kernel is open. This verifies the needed assertion with all
previous full matrices fixed, rather than only their reductions modulo
one integer.

The allowed next matrices form an open coset in SL2(Zhat). The reduction
maps SL2(Z) onto SL2(Z/m) are surjective by elementary matrices and the
Chinese remainder theorem, so this coset contains an integral matrix.
Its inverse image inside the current compact coset is nonempty, closed
and nested. Compactness supplies a single sigma in every stage and
retains the prescribed nontrivial quartic permutation. The asserted
deterministic ordering is a specification of a choice, not a claimed
algorithm for deciding membership in the adelic cosets.

## 5. Geometric quotient lattices and the full stated diagram

For an actual isogeny q:A0 to B, use q_* to identify the rational Betti
homology spaces. The target integral lattice becomes L_B with
Lambda_A0 contained in L_B contained in (1/m)Lambda_A0. Under the
analytic uniformization, L_B/Lambda_A0 is precisely ker q. The
identification with torsion is compatible with Betti–étale comparison:
the class of a vector in (1/m)Lambda modulo Lambda is the usual
m-torsion point. Since the chosen comparison on A0 completes to the
actual Galois map, it sends this finite kernel to its sigma-conjugate.
It therefore sends L_B onto the conjugate target lattice. This constructs
an actual integral isomorphism on B and its completion is exactly the
Galois map there.

If two isogeny presentations produce maps on B, their completions
coincide. Injectivity of a free integral lattice into its profinite
completion makes the two maps equal. This proves independence of the
presentation, including geometric forms isomorphic to the chosen
representatives. Products use direct sums; all CM factors use the
previously proved canonical s=1 comparison, with the same actual
completed Galois action. Thus the construction is consistent over
arbitrarily many objects, since each object and equation is finite.

For every actual algebraic correspondence, its étale cycle-class
equation is transported by this same sigma. The Betti equation follows
from comparison and faithfulness of completion on the torsion-free
cohomology of abelian varieties. The same reasoning applies to the
specified integral projectors, tensor maps and polarizations. Exterior
powers and inverse duals give all cohomological degrees, with Tate fixed
because sigma fixes the cyclotomic extension. Underlying-Q Artin blocks
are permuted by sigma; the maps on their geometric factors are exactly
the already constructed maps. Hence their descent equations also hold.

The proof therefore passes for all products, geometric isogeny lattices,
CM factors, Artin objects and actual correspondences specified in ET-3.
There is no need, and no justification supplied by this argument, to
identify this diagram with all abelian or all pure objects.
