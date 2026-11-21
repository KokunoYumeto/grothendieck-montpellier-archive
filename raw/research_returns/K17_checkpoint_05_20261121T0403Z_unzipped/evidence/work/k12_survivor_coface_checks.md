# Exact coface boundary calculation

Author /root/tripod_integral, GPT-6 Astra Pro. Date 2026-11-21 UTC.
Effort not exposed. This is a checked computational deduction with
an explicit mathematical incidence proof, not formal verification.

## Result and scope

For the certified rank-nine survivor tau, adding w=e8+e9 gives a
rank-nine cone eta with thirteen independent minimum rays. Every
facet except tau is killed by an explicit odd integral reflection.
The coface itself preserves orientation; its boundary coefficient
on tau is one. Orthogonal extension gives an analogous coface
whose boundary is the rank-ten survivor sigma. Thus these two
specified cycles are boundaries. No full homology group or K12
vanishing is asserted.

## Discovery and final exact input

The existing twelve facet reflections have a common fixed plane:
w=(0,t,-t,0,0,t,0,s,s). The choice t=0,s=1 suggested a coface
whose other facets would all be killed by the same witnesses.
An exploratory floating LP kept the twelve original minima and
w at norm one, and used integer-vector inequalities to find a
positive candidate. An exact rational reconstruction was then
checked by exhaustive rational enumeration. The initial denominator
3600 candidate required 390 enumeration nodes. The final simplified
matrix has denominator 720 and requires 388 nodes. Only the latter
is used in the final proof and standalone certificate.

The finalized matrix and vectors are literal inputs to
work/k12_survivor_coface_certificate.py. The program uses only
Python's standard library. Its executed output is
work/k12_survivor_coface_certificate.json.

## Complete self-check

I read the whole final standalone program and TeX proof. The exact
LDL algorithm checks its reconstruction identity as well as strict
positivity of all pivots. The short-vector recursion visits every
integer in the exact integer-square-root interval, so its output
is exhaustive without a guessed coordinate box or numerical
tolerance. Exactly twenty-six signed minima occur, all of norm
one, and the quadratic rank is thirteen.

The twelve original reflection rows are hard coded. For every
row, the program checks phi(w)=0, the integral matrix square
g^2=I, every stated action on the remaining original rays and w,
the full vector rank nine and quadratic rank twelve of the facet.
Each action is one transposition of independent rays, hence odd.

The orientation argument for eta is separate from the enumeration:
an eta stabilizer must preserve tau, the unique facet with no odd
integral stabilizer. It fixes the complementary ray w and acts
evenly on tau by the previously certified complete stabilizer
classification. This proves eta is an allowed orientation generator.

## Incidence convention, independently read

Primary author PDF:
https://jamartin.perso.math.cnrs.fr/Publications/DEKM.pdf

Fresh retrieval ref turn804552978view0. Local source
work/k12_source_data/dekm_author_current.pdf/.txt.
I read the complete definitions and formulas in §1.2.1, printed
p.4, equations(1)-(2), and §1.2.2 Proposition1.3 p.5. The
coefficient is the sum of orientation incidences over actual
facets in the target orbit. Here only the one geometric facet
tau can be in its orbit, since every other facet has an odd
stabilizer. Its incidence is +1 with the displayed cone-ray
ordering. Equivariantly, the transfer index is one since the
source stabilizer fixes this facet. Inclusion into the target
stabilizer contributes no factor on H0.

The primary §2.1 p.6 states the minimal-class/cell correspondence;
this verifies that the entire minimum set of the displayed
positive form specifies a cell. None of the disputed endpoint
enumeration or Theorem4.5 homology assertions is used.

## Orthogonal extension

For eta plus the orthogonal rank-one lattice, mixed vectors have
norm at least two. Thus the full minimum set consists exactly of
the thirteen old pairs and the new axis pair. Deleting an
original ray gives its old odd reflection extended by identity.
Deleting the axis has rank nine in ambient rank ten, hence is
relative-boundary zero. Deleting w gives sigma. It is the only
full-rank facet with nonzero orientation coinvariants, so the
same orientation and coefficient-one arguments apply.

Independent whole-proof review was requested from both root and
archive before promotion. Their verdicts are recorded separately.
