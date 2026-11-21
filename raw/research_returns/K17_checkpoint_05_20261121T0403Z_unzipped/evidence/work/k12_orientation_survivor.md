# K17: an explicit cell surviving orientation pruning

Date: 2026-11-21 UTC. Author: /root/vandiver_k, GPT-6 Astra Pro.
Reasoning effort not exposed. Status: exact certificate executed and
whole argument read; independent audit requested. This is a statement
about a Voronoi chain generator, not about its homology class or K12.

## Result

There exists a rank-ten well-rounded integral lattice configuration
with thirteen minimal-vector pairs, perfection rank thirteen, maximal
minimum-basis index three, and no orientation-reversing cell stabilizer.
Thus the rank-ten projective degree-twelve chain group has a surviving
orientation generator. The assertion that every remaining target cell
can be removed by an orientation-reversing stabilizer is false.

Nothing here says that the generator is a cycle, that it survives a
boundary, or that the target homology or K12 is nonzero.

## 1. The explicit rank-nine lattice

Take L=Z^9 and Q=G/36, with

    G =
    [ 36,  7,  7,  2,  7,   0,  -9,   0,  -9 ]
    [  7, 36,  7,  0,  0, -11,   0, -11,   4 ]
    [  7,  7, 36,  4, -7,   0,   0,  -7,  -4 ]
    [  2,  0,  4, 36,  0,   0, -12,   0,  -6 ]
    [  7,  0, -7,  0, 36,   0,   0, -11,  -7 ]
    [  0,-11,  0,  0,  0,  36,   4,  -7, -15 ]
    [ -9,  0,  0,-12,  0,   4,  36,  -7, -15 ]
    [  0,-11, -7,  0,-11,  -7,  -7,  36, -11 ]
    [ -9,  4, -4, -6, -7, -15, -15, -11,  36 ].

The complete minimum set, of norm one, consists of the pairs of the
nine standard basis vectors and the following three vectors:

    a = (-1,-1, 0,-1,-1,-2,-2,-2,-3),
    b = (-1, 0,-1,-1,-1,-1,-2,-2,-3),
    c = ( 0,-1,-1,-1,-2,-2,-2,-3,-3).

Let V=[I_9 a b c]. The exact certificate checks every asserted norm,
positive definiteness, and completeness of this list; its arithmetic
is detailed below. Exact elimination gives rank twelve for the twelve
quadratic forms p(v_i), so the projective cell has dimension eleven.

## 2. Full stabilizer parity by the relation lattice

The rows of B_0=[-a^t;-b^t;-c^t | I_3] are an integral basis for ker V.
After a unimodular row change and column reordering, its signed column
configuration is the following set, with one vector from each pair:

    e_1, 2e_1, 3e_1;
    t e_1+e_2       for t=0,-1,-2;
    t e_1+e_3       for t=0,-1;
    t e_1+e_2+e_3   for t=0,-1,-2,-3.

This equivalence and the original-to-target column order are checked
integrally and recorded in `k12_trimodular_exact_certificate.json`.
All three-by-three minors have absolute value at most three, some
have value three, and a unit minor occurs. Complementary minors then
show that the maximal minimum-basis index of V is exactly three.

Every integral lattice automorphism preserving the cell permutes its
minimal vectors up to sign: each vector is primitive, so an integral
automorphism cannot rescale its primitive ray by any other factor.
It therefore preserves the full integral relation lattice, and induces
an element U of GL_3(Z) preserving the signed column configuration B.
Conversely any such signed-column symmetry preserves the relation
lattice and descends to an automorphism of the quotient Z^12/row(B).

Here all columns are distinct up to sign, so a given U determines the
signed permutation uniquely. We can classify all U without relying on
the exhaustive program. The pair ±3e_1 is the only column pair whose
content is three, so U(e_1)=±e_1. Multiplying U by -I if necessary,
assume U(e_1)=e_1. Modulo Ze_1 the three nonzero signed ray classes
have multiplicities three, two, and four. These multiplicities are
different, so the induced automorphism fixes each quotient ray.
Fixing the rays e_2, e_3, and e_2+e_3 forces the quotient action to be
epsilon I, with epsilon in {+1,-1}. Thus

    U = [ 1, x, y ]
        [ 0, eps,0 ]
        [ 0, 0,eps ].

If epsilon=+1, preserving the finite fiber intervals forces x=y=0.
If epsilon=-1, the first two intervals force x=2 and y=1; the third
interval is then preserved because x+y=3. Consequently the entire
group is {I,-I,J,-J}, where

    J = [ 1, 2, 1 ]
        [ 0,-1, 0 ]
        [ 0, 0,-1 ].

The pair permutation of -I is trivial. J fixes the three e_1-axis
pairs and reverses the respective fiber intervals of sizes three,
two, and four. It therefore induces one, one, and two transpositions,
respectively: four in total, an even permutation. All cell stabilizer
elements are thus orientation preserving on the independent
twelve-dimensional quadratic span and on its projectivization.

## 3. Rank ten and degree twelve

Now form L'=L orthogonal-sum Z with quadratic form Q'=Q orthogonal-sum
[1]. Its norm-one vectors are exactly (v,0) for the twenty-four minima
of L and ±e_10: any vector having both components nonzero has norm
at least two. There are thirteen pairs and thirteen independent
quadratic rays. The corresponding projective cell has degree twelve.

Its relation matrix is B with one additional zero column. A signed
permutation preserving its relation lattice must fix this unique zero
column. On the other twelve columns it induces one of the four
symmetries just classified. A possible sign on the final vector does
not change its quadratic ray. All ray permutations are therefore
even. The maximal minimum-basis index remains three, since a full
basis must include e_10 and the other nine-vector determinant is a
minimum-basis determinant of L.

The resulting cell supplies an orientation-preserving orbit in the
degree-twelve relative Voronoi chain group. In particular, over
R=Z[1/13!] it is not removed by orientation coinvariants. This is
only a chain-level obstruction to the strategy of making the entire
target chain group zero.

## 4. Exact computational certificate and its proof of exhaustiveness

The preferred standalone executable certificate is
`k12_survivor_certificate.py`, with full exact output in the same
basename `.json`. It uses only hard-coded integer inputs and Python's
standard library. The earlier combined discovery-template certificate,
`k12_trimodular_exact_certificate.py`, additionally verifies the first
template's exclusion identity.
The proposed rational matrix was discovered by a floating-point LP,
but no numerical tolerance is used in the final certificate.

The certificate constructs Q with rational arithmetic and checks
Q=L D L^t, where L is unit lower triangular and D has diagonal

    1,
    1247/1296,
    725/774,
    12863/13050,
    337943/373027,
    14603131/16221264,
    1271478295/1577138148,
    263690369113/411958967580,
    120536209775/3164284429356.

All are positive. For each integer vector z, its norm is

    sum_i D_i (z_i + sum_{j>i} L_{ji} z_j)^2.

The enumeration descends from i=9 to i=1. Given the later coordinates
and the accumulated nonnegative partial sum, let R be the remaining
norm budget and write the rational shift as a/b with b>0. The next
coordinate must satisfy

    (b z_i+a)^2 <= (R/D_i)b^2.

Since the left side is an integer square, the exact permitted interval
uses M=floor(sqrt(floor((R/D_i)b^2))) and

    ceil((-M-a)/b) <= z_i <= floor((M-a)/b).

The program obtains M by integer square root. Every possible integer
coordinate in that interval is visited, and there is no other branch
with norm at most one. The complete search uses 326 nodes and returns
exactly the twenty-four listed signed minima. It also checks their
norms directly and the quadratic rank by rational elimination.
This supplies an exhaustive short-vector certificate, not a search
over a guessed coordinate box.

The separate `k12_trimodular_extremal_check.py` also enumerates all
integral symmetries of the signed relation-column set by considering
every ordered image of a fixed unimodular column basis among the
twenty-four signed columns. It returns exactly the four matrices
classified by the elementary argument above. That exhaustive check
is corroboration; the interval-fiber argument is the mathematical
proof of the stabilizer description.

## 5. Provenance and another excluded template

The construction was found among the three extremal polytopes for
h(3,3)=25 in Averkov--Schymura, *On the maximal number of columns
of a Delta-modular integer matrix: bounds and computations*,
Mathematical Programming 206 (2024), 61--89, section 5.2 and
Tables 1 and 3, p.85. The authors' exact data are at

https://github.com/mschymura/delta-classification

and the archived input is
`k12_source_data/delta_dim_3_delta_3_extremal.txt`.
The explicit surviving-cell proof needs no assertion that this
classification is exhaustive: its lattice, minimum enumeration,
and stabilizer have all been checked directly.

The first of those three templates does not define the asserted
complete minimum set. Its dual configuration satisfies an exact
identity between six proposed minimum quadratic forms and six
different integer-vector quadratic forms, all with coefficient one.
Those outside vectors and the identity are recorded and verified in
`k12_trimodular_exact_certificate.py/.json`. At least one outside
vector must then have norm at most the proposed minimum. This is a
separate exclusion and does not exclude the second template above.

The third template has an explicit odd ray symmetry, recorded in
`k12_trimodular_extremal_check.json`. Thus extending the index-two
orientation proof by the same argument meets a real surviving
configuration at index three. No conclusion about K12 follows.
