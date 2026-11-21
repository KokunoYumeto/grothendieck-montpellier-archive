# Independent whole-proof audit: all twenty-six ternary coface fillings

Reviewer: `/root/archive_kummer`, GPT-6 Astra Pro. Date: 2026-11-21 UTC.
Reasoning effort: not exposed. Verdict: **PASS**, for the twenty-six
coefficient-one fillings and the stated restriction on representatives
of rank-ten Steinberg homology. No assertion about the remaining
larger-index cells or K12 follows.

## Complete reading and retained prerequisites

I read the entire final `k12_ternary_coface_section.tex`, every line of
`k12_ternary_coface_certificate.py`, and the entire generated report.
I parsed all twenty-six frozen data records and their complete schemas;
every scalar used in the positive-definiteness, minimum, and matrix
identities is checked by the successful exact replay. I do not claim
to have certified large matrices by visual inspection alone.

I read the complete independent classification audit
`k12_ternary_glue_vandiver_audit.md`, and the statement, exact templates,
ambient-lattice definitions, and beginning of the preceding classification
proof. Its exhaustive twenty-six-orbit coverage and absence of odd
stabilizers in the old cells are retained, independently reviewed inputs.
I did not rerun that separate 65,788-state classification in this audit.
The new coface conclusion needs its orientability assertion, not a new
unstated stabilizer classification.

## Exact replay and actual ambient coordinates

The standalone new certificate was executed and passed every assertion:

| Check | Result |
| --- | --- |
| Records, without duplicates or omissions | 26 |
| Complete signed minimum sets in every coface | 28 vectors, or 14 pairs |
| Quadratic rank in every coface | 14 |
| Exhaustive enumeration nodes | 327 through 477 |
| Old-ray facets with integral odd involutions | 307 |
| Old-ray facets still of deficient vector rank | 31 |
| Unique remaining facet in each coface | Original cell |

There are four records with no relative facet, thirteen with one, and
nine with two. Thus `307+31=13*26`, accounting for every old-ray deletion.
Each new-ray deletion is the original thirteen-ray cell.

I additionally checked the actual lattice change, separately from the
new verifier. For every old template, its integer ambient-basis numerator
D has determinant of absolute value `3^9`, so the basis D/3 has determinant
of absolute value `1/3`. The first ten minimum-generated coordinates
are the identity basis. Every inherited coordinate identity

    D * v_ambient = 3 * v_Lmin

holds for all thirteen old vectors. The new verifier uses precisely
these ambient-coordinate vectors, not their coordinates in the proper
minimum-generated sublattice. All fourteen vectors in every coface
are integral and have coordinate gcd one. Thus the form is enumerated
on the actual ambient lattice, and its reflection matrices act there.

## Positive definiteness and completeness of the minimum enumeration

The program reconstructs a unit-lower-triangular rational LDL transpose
decomposition, checks each diagonal pivot is positive, and checks every
entry of the reconstructed matrix. This certifies positive definiteness.

For the descending search, with the later coordinates fixed, the ith
summand is

    d_i * (z_i + sum_{j>i} L_{j,i} z_j)^2.

Write the rational shift as a/b, with b positive. The condition is
`|b*z_i+a| <= sqrt(remaining*b^2/d_i)`. Its left side is an integer,
so the radius is exactly the integer square root of the floor of the
rational right-side square. The lower bound in the code is
`-floor((radius+a)/b)`, which is the required ceiling of
`(-radius-a)/b`; the upper bound is `floor((radius-a)/b)`.
These formulas also hold for negative shifts. Consequently no norm
at most one vector can be skipped. Each branch is checked exactly,
and at a leaf the quadratic form agrees with the accumulated sum.

The output set is exactly the twenty-eight signed target vectors,
all of norm one. There are no shorter vectors, additional minima,
floating tolerances, or unproved finite-box bounds. The rank of the
fourteen upper-triangle quadratic rows is checked over the rationals.
Thus the cone is simplicial of dimension fourteen and its projective
cell has dimension thirteen.

## Every other facet is zero in the relative chain group

For every nonrelative old-ray deletion j, the data give two distinct
retained indices a,b, a sign epsilon, and a functional phi. The stored
numerator of phi is divisible by three coordinate by coordinate, so
phi itself is integral in the actual ambient basis. With

    d = epsilon*v_b - v_a,
    G = I + d*phi,

the exact check gives `phi(d)=-2`, and hence `G^2=I`; the program
also multiplies out every matrix entry of this identity. Thus G has
an integral inverse and lies in GL10(Z). The exact vector checks give
the stated signed exchange of a and b, fix every other retained old
vector, and fix w. They do not rely on G fixing the discarded ray.

The corresponding facet has thirteen independent quadratic rays.
Exactly two are exchanged and all others are fixed, so its orientation
is reversed. It has zero orientation coinvariant after inverting two.
The verifier checks its vector rank is ten as well.

For every marked coloop deletion, the verifier recomputes the rank of
the twelve retained old vectors together with w. It is exactly nine.
Therefore these facets lie in the relative boundary, even after w
has been added. The check cannot be replaced by merely knowing that
the reflections fix w: adding a new ray could otherwise restore full
rank. Here that possible gap is explicitly closed for every record.

## Actual cofaces, orientability, and incidence one

The complete minima of a positive form define a cell of the Voronoi
fan; this is the minimal-class/cell correspondence. Since the fourteen
quadratic rays are independent, every deletion is an actual facet.
Deleting w leaves the exact original rays in the same ambient lattice,
so this facet is the previously classified cell, not just a rationally
equivalent configuration.

The original facet is full rank and has no odd stabilizer, by the
retained classification. Every other facet is either deficient rank
or has an odd stabilizer. Both properties are invariant under an
integral equivalence. Any stabilizer of the coface must therefore fix
the original facet and its complementary ray. Its restriction on
the original facet is orientation preserving, and the complementary
ray has positive scaling. It follows that the coface itself is
orientation preserving. No uncomputed coface-stabilizer classification
is required.

The boundary coefficient is the sum of signed incidences over actual
facets equivalent to the target. Exactly one facet is equivalent to
the original target, and its simplicial incidence is plus or minus
one. Equivalently the source stabilizer fixes this facet, so its
transfer index is one. Inclusion on degree-zero orientation
coinvariants introduces no target-stabilizer-index multiplier.
Choosing the coface orientation makes the coefficient plus one.
Hence every one of the twenty-six cells is an actual boundary with
unit coefficient.

For these incidence and shift claims I freshly read the complete local
primary passage DEKM sections 1.2.1--1.2.3, printed pp.4--5, including
equations (1)--(4), Propositions 1.3 and 1.5, and the section 2.1
minimal-class dictionary on p.6. I also freshly opened the author PDF:
https://jamartin.perso.math.cnrs.fr/Publications/DEKM.pdf .
The boundary in equation (1) is explicitly over actual facets. The
Steinberg shift gives `12-10+1=3`. Cell stabilizer primes are at most
11 in rank ten, so the retained coefficient ring Z[1/13!] suffices.

## Homology-representative consequence and limits

Every chain is a finite linear combination of orbit generators. The
previous classification removes all orientation generators of maximal
minimum-basis index at most two; the minimum-generated index-three
case is zero or the previously filled sigma; the proper index-three
case is precisely these twenty-six generators. Subtracting their
coefficient-one fillings removes every such low-index term from a
cycle without introducing another nonzero boundary term. The result
remains a cycle, represents the same homology class, and is supported
only at maximal minimum-basis index at least four.

This does not compute the remaining boundary matrix, show that the
larger-index chain group vanishes, prove that its cycles bound, or
prove any new K12 vanishing. The preceding finite classification is
kept as a separate input with its own complete audit.

## Reviewed hashes

* New TeX: `8315d583dc0c610d8e01f3961fadad854632482151d4ad8270796c6eb28b0e1f`.
* New verifier: `767d7bc27ff0ae44d461ef08b2c2b7d51000dfd6ec7e7884741cd14b782e11e7`.
* Frozen coface data: `119691eb6607afd11d8ae3a583b2442702c1595f95cc584b0d22ddce799d9678`.
* Inherited form data: `a4377187a3f9f20bd8366e4e2a6e7a32ed4ec610fa014d7095a4810a360bdbe7`.
* Fresh replay report: `2ba2c3996fcbe65243e54d82ddc379e998b3e11b4eb7936fe0e24ec952f48cdd`.

No mathematical correction to the new coface section was requested.
