# Independent verification of the rank-six exterior-cube table

The file `work/theta/EXTERIOR_CUBE_RANK_6.tsv`, with SHA256
`692c5bfa126e15eb26930097ded669c4bfe7cb69f78d19b04b6a4a93d6669f06`,
has been checked by an independently written exhaustive character calculation.
The verifier imports no part of the producer's `few_columns.py`.

The asserted identity is

\[
\prod_{I\subset\{1,\ldots,6\},\ |I|=3}
 (1+t\prod_{i\in I}x_i)
=\sum_{(j,\beta)\text{ in table}}t^j s_\beta(x_1,\ldots,x_6).
\]

There are 156 rows, all coefficients are one, and the right side's dimension
at all \(x_i=1\), summed over all exterior degrees, is \(2^{20}=1048576\).
The verification compares every monomial coefficient in all 21 exterior
degrees, which checks the full character identity and the individual table
dimensions.

## Why the two enumerations are exhaustive

For the left side, index the twenty three-element subsets of a six-element
set. The binary reflected Gray sequence \(g_i=i\mathbin{\mathrm{xor}}(i\!>\!>1)\)
runs through every subset exactly once, and two successive masks differ
in the bit \(i\mathbin{\&}(-i)\). The verifier adds or removes the three
unit coordinate weights of that subset, according to its membership in
the new mask. It records the resulting six-component weight and the number
of chosen subsets. Thus every basis wedge of
\(\bigwedge^j(\bigwedge^3\mathbb C^6)\) contributes exactly once.

For each Schur function on the right side, the verifier directly enumerates
semistandard tableaux of the reported partition, with entries in
\(\{1,\ldots,6\}\). It fills cells in row order and allows every entry
at least its left neighbor and strictly greater than its upper neighbor.
The upper bound is six minus the number of still-unfilled boxes below in
that column. These are necessary bounds for every semistandard filling,
and at a completed filling the row and column conditions are sufficient.
The filling recursion therefore enumerates each tableau exactly once.
The weight character is the Schur character by the tableau formula
(Macdonald, *Symmetric Functions and Hall Polynomials*, Chapter I,
§5, equation (5.12), with empty inner shape).

The program first removes full height-six columns. Such a column is forced
to contain \(1,2,\ldots,6\). Removing \(b\) of them subtracts \(b\) from
each part of the shape and from each weight coordinate. Reinserting these
columns is inverse: entries in row \(i\) of every semistandard tableau
are at least \(i\), so the weak row condition is preserved. This proves
the determinant-twist optimization used in the code.

Every comparison used integer arithmetic. The produced receipts are
`EXTERIOR_CUBE_INDEPENDENT_CHECK.tsv` and
`EXTERIOR_CUBE_INDEPENDENT_CHECK.txt`; the complete executable verifier is
`verify_exterior_cube_independent.py`.

The result is a finite certificate for this complete rank-six table. No
higher-rank assertion is included.
