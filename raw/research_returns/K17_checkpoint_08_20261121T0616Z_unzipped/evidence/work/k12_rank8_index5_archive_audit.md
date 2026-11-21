# Independent audit: rank-eight index-five restriction and proper-glue exclusion

Reviewer: `/root/archive_kummer`, GPT-6 Astra Pro. Date: 2026-11-21 UTC.
Reasoning effort: not exposed. Verdict: **PASS** for both stated deductions,
with the direct signed-coordinate source locator added as explained below.

## Files and actual source reading

I read the entire `k12_rank8_index5_reduction.md` and its TeX, the entire
`k12_rank8_glue5_proof.md`, and the complete new typeset glue-five proof.
I freshly read Martinet's complete section 11 setup and both parts of
Table 11.1, author PDF pp.45--48; Definition 7.4 and its surrounding
discussion, pp.25--26; the full Proposition 8.1 proof, p.27; the opening
order-five distribution calculation in section 9, p.31; and Proposition
9.1 with its full proof, p.33. I also freshly read the corresponding
2014 complement for cyclic quotient counts on pp.4--5. The earlier
rank-eight audit retains its full checks of the rank bound, Theorem
10.1, and the 2014 completion. No published exhaustive classification
is claimed recomputed here.

Primary author sources:

* https://jamartin.perso.math.cnrs.fr/Publications/watsonensmath.pdf
* https://jamartin.perso.math.cnrs.fr/Publications/erratcompl37.pdf

## Every table count and surviving type

A simplicial cone of dimension thirteen has thirteen rays. Distinct
minimum pairs give distinct extremal rank-one rays, so there are exactly
thirteen minimum pairs. Section 11 explicitly says that each listed
type has a unique inclusion-minimal minimum configuration; its column
s counts the minimum pairs. Thus s is a lower bound for every realization.

If the primitive support has dimension n less than eight, the sublattice
on that support has its forced s pairs and the remaining independent
frame vectors give eight minus n additional pairs. This lower bound does
not assume the actual ambient lattice is an orthogonal sum. Its restricted
quadratic form has the same normalized minimum one, so the table applies.

I compared every row in both parts of the table. The exclusions and
remaining list are exactly as stated:

* Order six first occurs in dimension eight, with s values
  31, 27, 120, 28, 14, 36. All exceed thirteen.
* Order eight has its dimension-seven E7 row with s=63, and the six
  dimension-eight rows with s=48, 75, 120, 56, 48, 32. All are excluded.
* The completed general index bound and the E8-only order-nine case
  remove the other orders above five; E8 has 120 pairs. The complete
  quotient table has no order seven.
* At order two, primitive support four forces 12+4=16 pairs; support
  five through eight remains.
* At order three, support six forces 12+2=14 pairs; support seven and
  eight remains.
* At cyclic order four, the support-seven (5,2) row and the three
  support-eight (5,3), (6,2), (7,1) rows remain. Every other cyclic
  row forces at least sixteen after padding.
* For the elementary order-four quotient, only the two displayed
  weight-five numerator rows with overlap two remain. The other
  dimension-six, seven and eight rows force at least sixteen pairs.
* At order five, (4,4) and (6,2) have s=16, and only (5,3) remains.

Thus every minimum-basis index is at most five, and the complete necessary
list in the TeX is correct. Neither actual occurrence at thirteen pairs
nor a classification of the full remaining cells is inferred.

## Signed-frame precision at order five

Definition 7.4 is phrased using monomial-code changes with arbitrary unit
entries. This should not be silently interpreted as only signs and
permutations of an actual minimum frame when the denominator is five.
For the precise signed numerator needed here, I used the direct
section 9 calculation instead. It normalizes actual coefficients to
absolute values one or two, allows changing the single quotient
generator, and obtains exactly the distributions (6,2), (5,3), (4,4).
Proposition 9.1 then proves the first and last force sixteen pairs.
The 2014 complement confirms those minima counts.

Accordingly I added a short source-precision paragraph to
`k12_rank8_index5_section.tex`, and used these exact direct locators in
`k12_rank8_glue5_section.tex`. The mathematical necessary list is unchanged.
No correction to the old source's wording or convention is asserted.

## The entire proper index-five contradiction

Assuming [L:L0]=5, every independent minimum frame has index five in L
and hence is a basis of L0. In one such basis the 8-by-13 matrix contains
the identity and every maximal minor is zero or plus/minus one. Padding
a smaller nonzero minor by complementary identity columns proves total
unimodularity. It also proves equality of the rational and binary column
matroids, which is the exact hypothesis needed below. Distinct minimum
pairs give no loops or parallel elements in either matroid.

For one fixed generator of the quotient L/L0, its eight coordinates in
every minimum basis are nonzero and have nonsquare product modulo five.
The normal form has product 2 cubed. Signs are squares modulo five, and
rescaling that fixed generator by c changes the product by c to the
eighth power, also a square. Thus this assertion remains valid while
comparing different bases; there is no untracked choice of generator.

The exact one-column basis exchange formula is correct. Writing the
nonzero column support as S and r_j=a_j/v_j, nonvanishing in every
exchanged basis makes the r_j pairwise distinct in F5 nonzero, so
the support has at most four elements. Cancelling the unchanged
coordinates and the square sign factors gives precisely equation G5.3.

The full subset check needs only two orbits in size two and one orbit
in size three. The representatives {1,4}, {1,2}, {1,2,3}, pivoted at one,
give old/new products 4/3, 2/1, 1/2 respectively, with opposite quadratic
characters. Scaling a subset multiplies both products by the same
power, so this checks every subset, not only the displayed examples.
Support zero is impossible; support one would duplicate a minimum pair.
Thus every fundamental circuit has size five. Every circuit is
fundamental for some basis, by extending it with one element removed.

In a binary matroid the symmetric difference of two circuits is a cycle.
If two distinct five-element circuits intersect, it is nonempty, even,
and has at most eight elements. Decomposing any binary cycle into
disjoint circuits is justified by repeatedly deleting a minimal nonempty
cycle support. When all circuits have five elements, a positive even
cycle must have at least two circuits and at least ten elements.
This contradiction makes all circuits pairwise disjoint.

Their characteristic vectors are then independent and, by that same
decomposition, span the kernel. Nullity five would require five disjoint
five-element circuits, at least twenty-five columns, instead of thirteen.
The contradiction rules out proper minimum-generated index five.
No regular-matroid classification or omitted circuit hypothesis is used.

## Scope and hashes

The new exclusion leaves minimum-generated cells with maximal basis
index five, and proper glue of other orders. It proves no vanishing of
the remaining chains, their homology, or K12.

* Index-five MD: `742e388474b9251614eb49ffed90e57fa33f83185b6c98b4974021067dd04faf`.
* Index-five TeX, with direct source clarification:
  `9347f2671b0f9c5ac7e03a6f519cd88d9aa5bfae0b5245469c72943b6470c2c5`.
* Glue-five MD: `58c3458653ee69128e77109e52981c6bf278f3ce078cda66c9866195b8c3962f`.
* Full new glue-five TeX:
  `2f85e6586b79071fead3a6445a4e9ee6dca722e9eb5777583124ccbcf1888c28`.

The complete audit note and typeset proof were read back after saving.
