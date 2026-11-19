# Independent Levi-input audit (F.3.30)

**Verdict.** The exact invariant tangent input has dimension twelve for every
`s = dim(W)/2 >= 3`: the positive multiplicity blocks have dimensions
`3,3,1,0`, and the pure-W block has dimension five. The statement includes
`s=3`; its formal pairing relation causes no loss in these five vectors.
This audit does not evaluate the mixed-normalizer matrix and does not assert
the all-genus single-line q6 conclusion.

## 1. Program and exactness

I read and independently ran `work/calc_levi_single_line_input.py`.
The first run returned exit zero, internal elapsed 2.672488007 seconds.
The accompanying independent specialization certificate reran the exact
input program (internal elapsed 1.749756536 seconds) and completed all its
additional checks in a total of 3.163374777 seconds. Its recorded start time,
input hash, complete output and exit status are in
`work/code_elliptic/check_levi_pure_specialization.json` and `.out`.

The input program represents each inserted symplectic tensor by an oriented
pair of slots. Reversing an edge changes its sign. Its permutation, cyclic
sum and right-nested Dynkin maps therefore act on the actual tensor span.
It explicitly verifies the Dynkin idempotence identity `Dyn_6^2=6 Dyn_6`
and the cyclic identity `S_8^2=8 S_8` before selecting bases. Modular pivots
only select candidate rows: rational row reduction and substitution of every
kernel vector into every original integer row certify the exact rational
rank. The matching rank lower bounds complete the certificates. All
modular products in its int16 elimination are bounded by 10000 before
reduction modulo 101, so this use does not overflow.

In positive block m the program stores `m Psi_m(A)`, rather than
`Psi_m(A)`, since its tensor is `-S_8(b tensor [A,a])`. Its consistency
equation `pi_b T = -m b tensor [A,a]` is exactly the correspondingly
rescaled reconstruction equation. Multiplication by nonzero m does not
change its image or dimension over Q. The parameters and target diagrams
contain at most three W-pairs. The symplectic invariant theorem therefore
gives independent diagrams already at s=3, and the same equations apply
for every larger s. The resulting exact dimensions are:

| m | raw diagrams | Lie parameter dimension | constraint rank | input dimension |
|---:|---:|---:|---:|---:|
| 1 | 15 | 3 | 0 | 3 |
| 2 | 90 | 15 | 12 | 3 |
| 3 | 90 | 16 | 15 | 1 |
| 4 | 20 | 3 | 3 | 0 |

The cyclic reconstruction, suffix Lie condition and consistency equation
give both inclusion directions, as written in LI.2--LI.3. No assertion that
individual multiplicity projections preserve the actual arithmetic image
is used.

## 2. Exact source-to-program map for the pure block

I reopened MSS2015 arXiv v2, `MoritaSakasaiSuzuki2015_v2.pdf/.txt`, printed
p.7 for its map Phi, pp.25--26 for all five 105-coordinate chord vectors
C_i, and pp.26--27 for Proposition 7.2. Page 27 was also visually read.
The source uses

`Phi(C) = sgn(i1,j1,...,i4,j4)` times the inserted oriented omega tensor.

The program's diagram omits that global permutation sign. The independent
certificate parses all 105 entries of each C_i, verifies their count, and
multiplies every chord coordinate by this exact sign. Let B denote the
105-by-5 matrix of the program's five pure columns, and let C denote the
converted five source columns. The complete exact identity is `C=B M`, with

```
M = [ -16/3  -7/3   -1    -2/3   1/3 ]
    [   1     -1    1/3   -1/3   2/3 ]
    [ -13/6   1/3   1/3    5/6  -2/3 ]
    [   5/6  -1/3  -2/3    1/2  -1/2 ]
    [  -2/3   2/3   1/3     0    1/2 ],  det(M)=5.
```

All 525 coefficient identities were checked over Q. Thus the formal
program basis and the five explicit source vectors span exactly the same
formal subspace; no assumption of independence of all 105 pairings at
s=3 is made.

Proposition 7.2 gives the actual five-contraction detector at matching
indices 1,2,3,8,14. Its constant five-column matrix has determinant -2160.
Its five column multipliers are

```
2s(2s+1)(2s+2)(2s+3),
(2s-2)2s(2s+1)(2s+2),  (2s-2)2s(2s+1)(2s+2),
(2s-2)(2s-1)2s(2s+1),
(2s-4)(2s-2)2s(2s+1).
```

Every multiplier is positive for integer s>=3. The full determinant is

`-17694720 s^5 (s-2)(s-1)^4(s+1)^3(2s-1)(2s+1)^5(2s+3)`.

At s=3 it equals -3330064449640857600. After the exact change M, the
detector on the program basis has determinant -666012889928171520.
These determinants were checked symbolically and at s=3 in the independent
certificate. Consequently all five actual specialized program vectors
are independent for every s>=3. Proposition 7.2 also gives that the actual
pure-W invariant derivation space has dimension five, so their
specialization is an isomorphism onto that space.

## 3. Scope

The twelve-dimensional input is now justified, including the smallest
requested complement. The coupled mixed-normalizer equations, their
genus-dependent scalar contractions and their q6 image remain a separate
calculation. I did not duplicate or rely upon that calculation in this audit.
