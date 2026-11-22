# Conditional common-high point-field lead after B90

Status: exploratory, unpromoted, no finite test executed and no actual pair
constructed. This note is separate from the frozen CP32 canonical inputs.

Assume the remaining p=5, e_K=20 nontrivial-residual-wild branch. Let R/L be
the common first-level division field of degree five. The two high lines
coincide. Restrict for this calculation to B_i=5b_i with 1<=b_i<=19,
5 not dividing either b_i, and b_1<b_2. This restriction is not asserted to
exhaust the remaining branch.

Suppose an actual corresponding primitive25 point above a low residual vector
has common point field E/R of degree25. Then every first-level translation
occurs. Its two formal coordinates have actual normalized data

    A_i=5b_i,
    D_0,i=125b_i,
    D_1,i=15000-625b_i,

with the same high-displacement line H. All displacements are below
v_E(5)=125*480=60000. The degree25 hypothesis must be proved in any
application; the denominator of the point alone gives only degree>=5.

If E/R has one break r, the leading-coefficient map has a two-dimensional
F5-image. A unique first term cannot vanish precisely on H; a tie below
D_0 would vanish on all25 leading coefficients, impossible for the nonzero
degree-five additive polynomial. Thus r=(D_0-A)/5=24b_i for both models,
forcing equality of b_i.

For two breaks t<u, if the last line is not H, B87's exact coefficient lemma
gives the same larger cyclic break (D_0-A)/5=24b_i, again forcing equality.
Thus a different-parameter comparison must have last line H. For one row:

- t<24b_i forces J_i=5b_i+4t and u+4t=15000-630b_i.
- t>24b_i forces J_i=125b_i-t and u-t=15000-750b_i.
- t=24b_i is the boundary at which the leading term already has degree D_0.

Both strict inequalities in the same direction force equality. If
24b_1<t<24b_2, subtracting the two displayed equations gives
t=150b_1-126b_2<24b_1, impossible. The boundary t=24b_2 is also impossible:
the model1 relation gives u=15000-750b_1+24b_2. In model2 the leading
displacement at u is larger than D_1,2 because

    (5b_2+5u)-D_1,2=750(80-5b_1+b_2)>0.

Hence J_2=D_1,2-u=750b_1-649b_2, but matching the earlier displacement
requires J_2>=101b_2, contradicting b_1<b_2.

The sole remaining necessary profile is

    t=24b_1,
    u=15000-630b_2-96b_1,
    upper breaks=(24b_1, 3000-126b_2).

At this profile, the two forced prime exponents are
J_1=630b_2-529b_1 and J_2=5b_2+96b_1. Their residues modulo five equal
b_1, so the prime-exponent condition does not itself contradict this profile.

If a further actual primitive125 point has degree25 over E, its leading
values A_i stay5b_i and its displacements multiply25. The analogous
calculation suggests upper breaks

    (624b_1, 75000-3126b_2),

with lower second break375000-15630b_2-2496b_1. This repetition remains an
outline until its complete field and coefficient proof is written.

What is still missing: unlike B90's exchanged-high-line case, the low point
fields over different low residual vectors have the same two conductors.
The complementary high-point and diagonal conductors in the full second
division field remain undetermined. Neither elementary disjointness nor
the numerical filtration of B90 may be imported without proving the new
actual group intersections. No contradiction or new branch exclusion is
claimed by this note.
