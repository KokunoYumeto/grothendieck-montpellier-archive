# K17-K12-R8-INDEX5: the remaining rank-eight quotient types

Date: 2026-11-21 UTC. Author: `/root/vandiver_k`, GPT-6 Astra Pro.
Reasoning effort: not exposed. Status: short complete deduction from
the cited Martinet classification; independent review requested.

## Statement

Let L be a rank-eight lattice whose complete minimum cone is simplicial
of dimension thirteen. Then every basis selected from its minimum vectors
has index at most five in L. More precisely, for any such frame
F=sum Z f_i, the quotient L/F has one of the types listed below. Signs,
permutations of the frame, and changes of generators of the quotient are
allowed. Each numerator denotes coefficients on the ordered frame.

| Quotient | Allowed numerator(s), divided by the indicated order |
| --- | --- |
| trivial | no generator |
| C_2 | `(1^m,0^(8-m))/2`, with `5<=m<=8` |
| C_3 | `(1^m,0^(8-m))/3`, with `7<=m<=8` |
| C_4 | `(1^5,2^2,0)/4`, `(1^5,2^3)/4`, `(1^6,2^2)/4`, or `(1^7,2)/4` |
| C_2 times C_2 | `(1,1,1,1,1,0,0,0)/2` and `(0,0,0,1,1,1,1,1)/2` |
| C_5 | `(1^5,2^3)/5` |

This is a necessary list, not a claim that all listed types can occur
with exactly thirteen minimum pairs, and not a classification of the
whole cells. It applies to the actual ambient lattice even when the
minima generate a proper sublattice.

Combined with K17-K12-R8-NONSIMPLICIAL, every potentially contributing
rank-eight projective degree-twelve cell is simplicial, has exactly
thirteen minimum pairs, and satisfies this finite list for every minimum
frame. In particular no potentially contributing cell has maximal
minimum-basis index greater than five.

## Proof from the precise source table

A simplicial thirteen-dimensional cone has exactly thirteen extremal rays.
Distinct minimum pairs give distinct extremal rank-one positive
semidefinite rays, so L has exactly thirteen minimum pairs.

Martinet's Table 11.1 classifies the minimum-frame quotient types through
dimension eight. Section 11 specifies that each listed type has a unique
minimal minimum configuration, and the column s is its number of minimum
pairs. Thus every realization of the type has at least that many pairs.
For a type supported on n<8 frame coordinates, the restricted lattice on
that support already contains its s minimum pairs, while the other 8-n
independent frame vectors supply further pairs. Consequently

    number of minimum pairs in L >= s+(8-n).                 (I5.1)

The complete rank-eight index bound is used with its 2014 completion:
the appendix gives index at most nine except E_8, and original
Theorem 10.1 confines index nine to E_8. The latter lattice has 120 minimum
pairs and cannot occur here. The complete quotient-type classification
has no index seven. The remaining possible orders above five are six
and eight.

For index six, all six primitive rank-eight types in Table 11.1 have

    s = 31, 27, 120, 28, 14, 36.

Index six does not occur below rank eight. Thus every such frame would
force at least fourteen minimum pairs, contradicting the total thirteen.

For index eight, the primitive rank-seven type is E_7, with s=63, and
the six primitive rank-eight types have

    s = 48, 75, 120, 56, 48, 32.

All contradict (I5.1). This proves the index bound five.

For orders at most five, apply (I5.1) to every row of the same complete
table. At order two, support four has s=12, hence at least sixteen pairs
in rank eight; supports five through eight have s=n and remain. At order
three, support six has s=12 and hence at least fourteen pairs; supports
seven and eight remain. At order four, all types except the five stated
rows have s+(8-n)>=16. At order five, the two distributions (4,4) and
(6,2) have s=16, while (5,3) has s=8. Exactly the displayed list remains.
The first cyclic order-four row has primitive support seven; the other
three cyclic rows and the elementary order-four row have support eight.
This proves every claim in the statement.

## Source locators and actual checks

J. Martinet, *Sur l'indice d'un sous-reseau*, Monographies de
L'Enseignement Mathematique 37 (2001), 163--211. In the 51-page author PDF:
section 11 setup pp.45--46, complete Table 11.1 pp.47--48; introductory
classification theorem p.3; rank-eight index-nine case Theorem 10.1
pp.39--40. The full section 11 setup and every row of both parts of
Table 11.1 were read. Section 7's definition of quotient types and
section 8's deformation discussion distinguish quotient types from
complete minimum classes. We rely on the published table's classification
and its explicitly stated minimum-count meaning, rather than claiming
to have rerun its classification.

Primary https://jamartin.perso.math.cnrs.fr/Publications/watsonensmath.pdf .
Local `k12_source_data/martinet_index_2001.pdf/.txt`.

The relevant 2014 errata and entire appendix were read in the preceding
rank-eight proof check. They do not change any of the table rows used
here. Primary https://jamartin.perso.math.cnrs.fr/Publications/erratcompl37.pdf .

No incoming boundary calculation or vanishing of the residual simplicial
chain group is asserted.
