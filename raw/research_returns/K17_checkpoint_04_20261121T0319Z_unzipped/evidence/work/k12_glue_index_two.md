# K17: rank-ten index-two glue and orientation

Date: 2026-11-21 UTC. Author: /root/vandiver_k, GPT-6 Astra Pro.
Reasoning effort not exposed. Status: independently audited restricted
proof; see `k12_glue_index_two_tripod_audit.md`, 2026-11-21.
This is a further cell-pruning result, not a proof
that the rank-ten Voronoi homology target vanishes.

## Statement

Let a rank-ten lattice L have a complete set of minimal-vector pairs
represented by v_1,...,v_s. Suppose that their rank-one quadratic forms
span a space of dimension thirteen and that every independent ten of
the v_i generate a sublattice of index at most two in L. If the minimal
vectors generate a proper sublattice L_0 of L, the associated projective
Voronoi cell has an orientation-reversing element of GL(L).

Together with `k12_bimodular_attempt.md`, this kills every maximal-index-
at-most-two rank-ten target cell having thirteen minimal-vector pairs,
whether or not the minima generate L. The proper-sublattice part of the
present statement itself needs no prior assumption on the number s.
The still-uncovered possibility is a minimum-generated target cell with
more than thirteen minimal-vector pairs, as well as larger maximal
indices. No statement here disposes of all such cells.

## Proof

### 1. The generated lattice and its relation matrix

The index [L:L_0] divides the index of every independent ten-vector
sublattice. It is greater than one and at most two, so it is two.
Consequently every independent ten of the v_i form a basis of L_0.
Choose one such basis. The column matrix is V=[I_10 A], and every
square minor of A is, up to sign, a maximal minor of V; hence V is
totally unimodular.

The simple-TU quadratic-independence lemma proved in
`k12_orientation_attempt.md`, section 3.1, applies: the v_i are nonzero
and no two are equal up to sign, so the v_i v_i^t are linearly
independent. The given quadratic-span dimension therefore implies
s=13. The integral relation lattice of V is the row lattice of

    B=[-A^t I_3].

The matrix B is totally unimodular of rank three. By Heller's bound it
has at most six nonzero signed-column classes. Within each such class
we may change the signs of the v_i so that the corresponding columns
of B are equal. These sign choices do not change any minimal-vector
ray or any quadratic form.

There is also at most one class of zero columns. The six-bound counts
only nonzero classes. Distinct nonzero signed-column classes have
distinct reductions modulo two: TU columns have entries 0,+1,-1;
two columns with the same support but without a common overall sign
would give a 2-by-2 minor of absolute value two. Thus the reductions
of the nonzero classes are distinct nonzero elements of F_2^3.

### 2. The glue class and easy transpositions

Write L=L_0+Z(w/2), with w in L_0 representing the nonzero glue class
in L_0/2L_0. Choose a lift c in F_2^13 of w under V modulo two.
Because V is surjective over Z, its reduction gives the exact sequence

    row(B mod 2) -> F_2^13 -> L_0/2L_0 -> 0.

Any permutation within a signed-column class fixes B, hence preserves
the integral relation lattice and induces an integral automorphism of
L_0 permuting the minimal rays. It extends to an automorphism of L
precisely when it preserves the glue class, equivalently when

    P(c)-c belongs to row(B mod 2).

If any class (including the zero class) has at least three columns,
two corresponding entries of c agree. Transposing this pair fixes c
itself and therefore preserves the glue class. Since the thirteen
quadratic forms are independent, this ray transposition reverses
orientation. The same conclusion holds if a class of size two has
equal c entries.

It remains only to treat the case in which every class has size at
most two and every size-two class has opposite c entries.

### 3. Three transpositions preserve the glue

There are thirteen columns but at most seven classes, counting a
possible zero class. With every class of size at most two, there must
be exactly seven classes: six nonzero classes and the zero class.
Exactly one class is a singleton and the other six are doubled.

Let b be the unique nonzero element of F_2^3 absent among the six
nonzero class reductions. If the singleton class is nonzero, let a be
its reduction. Choose a linear functional lambda on F_2^3 such that

    lambda(b)=1, and lambda(a)=0 if a is present.

Such a functional exists, since distinct nonzero vectors a,b are
linearly independent over F_2. If the singleton is the zero class,
only the first condition is imposed.

Every nonzero linear functional on F_2^3 takes the value one on
exactly four vectors. Removing b leaves exactly three of the six
nonzero class reductions with value one. The singleton class has
value zero, so all three selected classes are doubled. Let P be the
product of the three disjoint transpositions of those pairs.

For each selected pair the two entries of c are opposite, so P(c)-c
has value one at both positions of that pair and zero elsewhere.
This is exactly the vector obtained by applying lambda to the columns
of B modulo two. It lies in row(B mod 2). Thus P preserves the glue
class and its induced automorphism of L_0 extends to GL(L).

On the independent quadratic-ray basis, P is a product of three
disjoint transpositions and has determinant -1. It fixes the positive
radial direction, so it also reverses the orientation of the
projective cell. This completes the proof.

## Background and scope of checking

The only external combinatorial input is Heller's c(1,3)=6 bound,
Theorem 4.2 of I. Heller, *On linear systems with integral valued
solutions*, Pacific Journal of Mathematics 7 (1957), 1351--1364,
proof pp.1358--1360. The simple-TU quadratic-independence lemma is the
previously written and independently audited direct argument in
`k12_orientation_attempt.md`.

The relation-matrix construction, modulo-two exact sequence, index
calculation, glue-preservation criterion, counting argument, and
orientation calculation are all part of the proof above. No
classification of general maximal-index-two minimum-generated
configurations is assumed.
