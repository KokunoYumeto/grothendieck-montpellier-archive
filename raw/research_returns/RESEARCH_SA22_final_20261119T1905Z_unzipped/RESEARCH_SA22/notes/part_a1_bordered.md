# Bordered landing obstruction and exact joint-data repair

## Status

All three claims in `sections/part_a1_bordered.tex` have complete proofs.
The literal external-only admissibility claim is refuted on a four-holed
sphere; the corrected tensor/shadow and full-disc-image statements are proved.

## Primary manuscript reading

Original `sources/cote67.pdf` scans 065, 066, 074, 075, 076, and 021 were
visually opened and checked in this work session. The displayed PDF footer
number is one less than the scan identifier; handwritten/archive foliation
is a further distinct number. The exact definitions agree with the supplied
transcription:

- 065--066: a disc system is admissible if the toric structures induced on
  each boundary by its pointed disc and by the canonical hyperbolic metric
  of the complement coincide.
- 074: cut, then canonically cap *all* resulting holes, including internal
  branch holes and external holes, using the boundary structures of the
  canonical metric of each cut component.
- 075--076: retain an admissible system of discs around the *external marked
  points* on the stable nodal curve, along with nonzero node tensors.
- 021 is the collar-metric question; it does not supply a special alternate
  definition of admissibility on nodal curves.

The ordinary componentwise interpretation on a normalization leaves the
node branches as punctures when only external discs are retained. No claim
is made that the manuscript explicitly resolves this ambiguity. If its word
admissible is redefined to mean extendible by node caps jointly with the
external caps, the target is different and the repaired theorem applies.

## Exact counterexample

Glue two hyperbolic pants with all lengths 2*pi along one boundary. This
is a four-holed sphere with all four external lengths and the separating
seam length 2*pi. On either capped component put the two external centers
at 0 and 1 and the node-cap center at infinity. In the parent paper's
Schwarzian formula the three coefficients are a0=a1=ainfinity=1.

For a unit-disc coordinate u0(z)=c0*z*(1+b0*z+...), and a corresponding
u1 in local coordinate zeta=1-z at 1, both invariants are b0=b1=1/2.
Equality of embedded pointed cap domains forces equality of these b's,
because centered Riemann maps differ only by rotation.

If these external domains alone were admissible with infinity a cusp,
the new coefficients would satisfy a0',a1'>1/2 and ainfinity'=1/2.
The same jets imply

    a0'+a1'-1/2 = a0' = a1'.

Thus a0'=a1'=1/2, which gives both external lengths zero, impossible
for the given nondegenerate external discs. This proof allows the new
lengths to vary; it is stronger than holding the old lengths fixed.
The cusp coefficient follows directly from {log q,q}=1/(2q^2).

`code/part_a1_bordered_checks.py` uses exact Fraction arithmetic, solves
the nonsingular 2x2 system, checks both forced squared lengths are zero,
and writes its output and the three-row result metadata.

## Exact repaired range

Let P be edges disjoint-union actual external legs, with fixed cusp marks
allowed in addition. A coordinate t_e is copied to both node branches;
a coordinate t_l appears once at its external leg. At each vertex use the
full active cap potential S_v and support K_v. Then

    Psi(t) = sum_v S_v(B_v t),     K(p) = sum_v K_v(B_v p).

The combined incidence B is injective, including self-nodes. Therefore
the Hessian of Psi is positive definite. Its edge derivative is log of
the product of the two branch radii, hence log|q_e|; its external derivative
is log r_l. The same recession and finite-boundary coercivity proof from
A2b gives the exact logarithmic range x.p<K(p) for every nonzero p>=0.

Thus normalization, node tensors, and external *shadows* determine the
unique positive t, all full canonical cap systems, and all seam phases.
Equal paired boundary lengths permit unique welding. The image is an
open logconvex subbundle with tangent isomorphism and an equivariant
deformation retraction to the common all-t=1 phase-torus bundle.

If full external domains are retained, first invert their shadows with
the node tensors; then require each external domain to agree exactly
with the reconstructed canonical domain. This supplies a noncircular
necessary-and-sufficient shape condition: the inverse is already uniquely
defined by explicit support inequalities and a strictly convex potential.
The image is the graph of these external shapes. Ordinary admissibility
after discarding node caps is neither imposed nor automatically true.

## Gates and limitations

- The literal external-only interpretation is refuted, not merely shown
  nonsurjective. It is inaccurate to describe that arrow as a globally
  defined map with a proper image without first repairing its target.
- The corrected theorem uses actual toric phases, as in A1-graph-range;
  fully marked real Fenchel--Nielsen twists require the corresponding
  covering on the tensor phase side.
- The exact analytical inputs (A2b-energy, recession, radius image and
  regularity, A4-grafting) are proved/opened elsewhere in this manuscript.
- No new external literature claim is needed for the finite counterexample;
  its formula is derived in A2-schwarzian and its cusp specialization is
  explicitly derived here.
