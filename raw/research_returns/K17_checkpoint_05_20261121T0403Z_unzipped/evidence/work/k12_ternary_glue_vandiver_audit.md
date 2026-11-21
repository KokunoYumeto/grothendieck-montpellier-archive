# Independent whole-proof audit: the twenty-six ternary-glue cycles

Reviewer: `/root/vandiver_k`, GPT-6 Astra Pro. Date: 2026-11-21 UTC.
Reasoning effort: not exposed. Verdict: **PASS**, for the stated restricted
classification and cycle conclusions. No nonboundary conclusion follows.

## Full reading and executed replay

I read the complete `k12_ternary_glue_section.tex` and every line of
`k12_ternary_glue_certificate.py`, reconstructed the proof independently
of its loops, and reran the complete standalone certificate. I inspected
the entire frozen data schema and all twenty-six record identifiers,
dimensions and denominators; every scalar entry used by the proof is
checked in the successful exact replay. I do not claim to have inferred
positive definiteness or minimum completeness by visually inspecting
large integer matrices.

The replay returned:

| Source record | States | Odd | Short support | Remaining states | Orbits |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 63,450 | 21,978 | 24,300 | 17,172 | 20 |
| 2 | 2,310 | 1,410 | 0 | 900 | 6 |
| 3 | 14 | 14 | 0 | 0 | 0 |
| 4 | 14 | 14 | 0 | 0 | 0 |
| 5 | 0 | 0 | 0 | 0 | 0 |
| Total | 65,788 | 23,416 | 24,300 | 18,072 | 26 |

All twenty-six rational forms passed positive-definiteness, complete
minimum-vector enumeration, quadratic rank thirteen, and lattice-index
checks. The parent program's final `nonboundary_claim` remains false.

## Primary coverage

The source classification input is the complete list of five
origin-symmetric determinant-one lattice polytopes in dimension three,
from Averkov--Schymura, Mathematical Programming 206 (2024), section 5.2,
Table 2, printed p.85. I freshly read that table, and had just read the
complete relevant definitions and classification procedure in sections
5.1--5.2 during the preceding trimodular audit. Table 1's Heller value
h(1,2)=7 also supplies the final facet bound.

I read all five archived source records in
`k12_source_data/delta_dim_3_delta_1.txt` and compared them exactly by
Python parsing with the verifier's literal `SOURCE_RECORDS`; they agree.
The determinant and complete lattice-point tests for each model passed.
The published exhaustive coverage itself was not recomputed. The
primary article and author repository were freshly retrieved in the
immediately preceding audit as `turn844349831view0` and
`turn844349831view1`.

## Integral reduction and color classes

The proper minimum-generated lattice index divides the actual maximal
minimum-basis index three and is therefore three. Every independent ten
minima are a basis of that generated lattice. A chosen identity block
then makes both the minimum matrix and its Gale relation matrix totally
unimodular; complementary minors are normalized integrally.

The underlying signed Gale polytope has determinant parameter one.
For each of the five models the complete lattice-point check leaves only
zero and its vertices. Thus the support of the signed classes is exactly
one of the five lists, not an unexamined proper subset of that list.

The saturated presentation identifies glue representatives modulo row
shifts over F_3, with an additional global nonzero scalar. Equal colors
in one normalized nonzero Gale class give an odd transposition preserving
the actual ambient lattice. On the zero class, signs are independent;
three positions force two of the same zero/nonzero type. Their suitable
signed transposition is odd. Thus the mask/zero patterns enumerate every
potentially surviving state, including zero colors and nonzero colors.
A trivial glue class is removed by the support test, as it should be.

## The short-support identity

For any nontrivial glue representative x=sum a_j v_j/3, with a_j in
{0,1,-1}, the vectors x-a_j v_j for nonzero a_j remain outside the
minimum-generated lattice. They are nonzero and cannot be any of the
thirteen prescribed minimum pairs. Consequently each has norm strictly
greater than one. Expanding their norms gives exactly

    sum (Q[x-a_jv_j]-1) = (t-6) Q[x].

Thus t must be at least seven. All twenty-seven row shifts are tested;
global negation preserves support size. This exclusion is algebraic and
does not depend on the later realization search.

## Exhaustiveness of signs, automorphisms and equivalences

The automorphism enumeration chooses the images of a unit three-column
minor among all ordered signed triples of determinant plus/minus one.
Every integral automorphism of the signed Gale set is determined by
such an image, and the remaining column test is exact. This proves
coverage of the finite group used in the loops.

I checked the transpose convention directly. Put P e_j=epsilon_j e_pi(j).
Then B P=U B, so P^t row(B)^t=row(B)^t. Since P is an orthogonal integral
permutation matrix, its inverse is P^t; therefore P also preserves the
same integral relation lattice. The matched-color rule is

    c_pi(j) = epsilon_j c_j - lambda dot b_pi(j).

It gives `(P c-c)_pi(j)=lambda dot b_pi(j)` at each position, exactly
the required row shift. The quotient automorphism therefore preserves
the order-three glue extension. The orientation sign is the sign of
the ray permutation because the thirteen quadratic rays are independent.

Conversely an integral equivalence permutes the primitive minimum
vectors with signs, hence preserves their generated lattice and induces
an integral change of Gale basis. The glue scalar is plus or minus one.
If it is minus one, composition with global negation changes it to plus
one without changing any quadratic-ray permutation. The enumerated
Gale group contains the corresponding negated matrix. Zero-column
signs can then be normalized independently, without affecting the ray
permutation. With two zero columns, their distinct zero/nonzero color
types prevent an interchange. Thus no missing zero sign or scalar
equivalence can merge two reported orbits or add an odd stabilizer.

The orbit loop applies every group element and every row shift, so its
set is a full semidirect-product orbit. Its assertion that the orbit
lies among unprocessed survivors checks compatibility of the exclusions.
The complete remaining-state partition agrees with every stated orbit
and representative. Distinct source polytope classes cannot be
equivalent, since an integral Gale change would identify them.

## Exact ambient forms

For each representative, the expanded colored columns match the
template. The first ten quotient vectors are the identity basis, all
three integral relations vanish, and the maximal relation minors are
zero or plus/minus one. The glue numerator w is reduced to entries
{0,1,-1}; its first nonzero coordinate is normalized to one.

The ambient-basis numerator D is 3I with that coordinate column replaced
by w. Hence det(D/3)=1/3. The old missing basis vector is recovered as
three times the new fractional vector minus the remaining integral
coordinates, so this basis generates precisely the specified ambient
lattice. The identities D W=3 V are checked for all thirteen vectors.
Thus the forms are not inadvertently being tested only on L_0.

The LDL decomposition is reconstructed entry by entry and has positive
rational pivots. The descending enumeration bounds each integer
coordinate using the exact integer floor of a rational square-root
bound; `isqrt(floor(t))=floor(sqrt(t))` for nonnegative rational t.
The lower/upper ceiling formulas are correct even for negative shifts.
Every norm-at-most-one vector is therefore visited. The returned set is
exactly the twenty-six signed prescribed vectors, all of norm one;
there are no additional minima or shorter vectors. The quadratic rank
test and the exhaustive no-odd-stabilizer test pass for every record.

## All facets and the final scope

A full-rank facet contains a minimum basis of L_0, so its twelve vectors
still generate L_0 and its saturated Gale matrix has rank two and is
totally unimodular. Heller's bound permits at most three nonzero signed
classes. Avoiding an odd same-color transposition allows at most three
positions per nonzero class, and the zero class at most two. The maximum
eleven positions is less than twelve. Hence every full-rank facet has
an odd integral stabilizer. Deficient-rank facets lie in the relative
boundary. This proves that all twenty-six cells are cycles, without
computing incoming boundaries.

The earlier minimum-generated classification and its coefficient-one
filling remove the other index-at-most-three contributions. The result
is a precise twenty-six-cycle boundary gate. It does not supply their
fillings, prove their independence or nonzero homology classes, remove
larger-index cells, or prove K_12 vanishing.

## Reviewed hashes

- TeX: `40e0db37faac4716e53083d24f8b95ea15353d8b92b32aafd0e979acff0ee55b`.
- Verifier: `f12b789a02d61fc4be623a11528435e8d80f69e9d1f3ce4ff24ba6da35d59be0`.
- Frozen form data: `a4377187a3f9f20bd8366e4e2a6e7a32ed4ec610fa014d7095a4810a360bdbe7`.
- Five primary records: `2ea61787f76cb353dcdecda1faad3f8dc8ff99679b4d692d17720ee5518a95a8`.
