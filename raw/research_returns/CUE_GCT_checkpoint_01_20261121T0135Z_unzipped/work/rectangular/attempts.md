# Rectangular and Haar approach ledger

Run CUE_GCT-20261121, agent `/root/rectangular_bridge`, 2026-11-21.

## A. Direct scalar CUE positivity

The finite moment is a rectangular GL dimension. Treating that dimension
as an individual rectangular Kronecker coefficient fails: R-03 gives
dimension 20 and a relevant coefficient zero. Next construction: retain
all spectral parameters and perform tensor-subgroup restriction (R-01).

## B. Apparent mismatch of rectangle positions

Initially the Bump–Gamburd rectangle occupied the outer Schur label,
while GCT puts two rectangles in the inner labels. Kronecker symmetry
resolves this exactly. R-01 uses `s_(d^n)(X Y)` and projects onto
`s_lambda(X) det(Y)^d`; it reaches every relevant rectangular coefficient.
This is genuine gate movement beyond an analogy of shapes.

## C. Swaps and tableaux

The exact unitary swap formula can be pulled back along the product
alphabet. Weyl coefficient extraction gives a finite alternating
tableau-marginal formula. The individual swap terms have poles and
mixed signs; no termwise positive rule results. Next construction:
orthogonal invariant projectors and their squared entries (R-02),
followed by explicit structured witnesses (R-07).

## D. Rains power splitting

Cycle-index plethysm needs a joint law of powers of one Haar matrix.
Independent Rains marginals give the wrong moment already on U(2):
the true value is 2 and the independent value is zero (R-04).
Next construction: retain the full wreath-product symmetrizer;
it gives an exact sum of squares but still factorial size.

## E. Weingarten and orbit boundary

Connected-stabilizer multiplicities and full determinant-orbit
multiplicities differ (R-03, S4 example); orbit and closure likewise
must be separated. R-05 goes directly to a covariance whose kernel
is the orbit-closure ideal, thereby resolving the boundary distinction
at the level of an exact finite-rank criterion.

## F. Removing signed integration

Gaussian orthogonality converts the covariance to a factorially
weighted coefficient Gram matrix. R-06 gives integral Schur-projector
matrices, explicit entry bounds, and a finite interpolation grid.
These certificates are exact but their displayed sizes are exponential
or factorial. The unresolved task is structural compression or explicit
nonzero-minor control, not nonnegativity of the matrix.

## G. Explicit left-right invariants

Centering the coefficients of a binary determinant pencil gives
highest-weight polynomials Q_j. Their products give a positive basis in
the stable two-row range. Factoring binary forms shows that these
witnesses, and indeed all two-row ambient highest-weight vectors,
survive on the determinant orbit closure (R-07). Thus two-row
multiplicity obstructions are rigorously excluded. The root develops
the next ternary and fixed-variable stages; those are not duplicated here.

## H. Exact ratios rather than an unspecified Molien integral

R-09 projects a two-sided CUE inverse-determinant ratio to obtain the
sum of squares of precisely the GCT rectangular coefficients, with
monotone length cutoffs. In the stable unitary dimension range,
Bump–Gamburd's ratios theorem evaluates the inner integral as one
fourfold tensor Molien denominator. This gives exact identities and
bounds, but not efficient evaluation of the remaining projection.

## I. Arithmetic hypotheses

No R result depends on RH, Dirichlet GRH, or Masullo's claim. Their
truth changes which analytic zero-statistic results are unconditional,
not the Schur-transform identities or rank sizes proved here.
CFKRS's arithmetic moment recipe still requires its own off-diagonal
estimates. No statement that RH logically cannot ever help is claimed;
the missing comparison or compression theorem is simply not supplied.

## Current rectangular gate

For all weights, exact coefficient/minor criteria R-01–R-06 and R-09
are available. In the two-row sector, all determinant-coordinate
multiplicities equal the ambient plethysms, and explicit positive
witnesses are given. General efficient positivity and the actual
determinant/permanent multiplicity separation remain open. Root
findings narrow the shape/padding range further and supersede this
agent's standalone two-row gate.
