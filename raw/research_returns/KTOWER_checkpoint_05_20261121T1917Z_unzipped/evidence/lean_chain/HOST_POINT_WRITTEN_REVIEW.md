# Additional whole-written-proof review of the actual adjoint host point

The complete `unitary_audit/host_sign_results.tex` was read. No gap was
found in its written mathematical argument. This review does not claim
another complete audit of all newly cited Lean files or of Patrikis's
primary proof; the exact source identifications and the carried local
component theorem remain the separately recorded inputs. The parent
and geometry reviewer had already completed their independent reviews.

The direct obstruction calculation is consistent for split and
unramified quadratic eta. On inertia the Borel and unipotent Lie
modules have even cyclotomic exponents, so their Tate-dual twists
have nonzero odd exponents modulo ell-1. Hence H2 vanishes. The map
from H1 of the Borel Lie module to torus H1 is surjective by H2 of
the unipotent Lie module; restriction to inertia is surjective by
cohomological dimension one of the unramified quotient. Inertia
acts trivially on the torus Lie module, so the correction removes
the actual inertia cocycle, with no hidden coboundary issue. The
resulting framed fixed-inertia family is formally smooth over the
coefficient DVR. Adjoining congruent conjugation variables preserves
its domain property.

The prescribed ordered inertia polynomial kills the upper flag in
three steps. The unramified diagonal specialization makes the
saturating element nonzero. Its nonzero image in the family domain
therefore kills the saturation and then its radical. The family's
prime kernel lies under the base-point kernel; a minimal prime below
it belongs to the prescribed singleton set of base components. This
correctly gives the needed It containment, conditional on the carried
component theorem as explicitly stated.

The global construction correctly obtains a split residual lattice
after a ramified coefficient extension; it does not assume an
original split lattice. Complex conjugation diagonalizes integrally
because two is a unit. One off-diagonal ideal is initially divisible
by the original uniformizer, and square-root scaling makes both
off-diagonal ideals strictly positive. The normalized adjoint basis
and Dc correction give the indicated GG3 residual representation.
The coefficient order O+m(O') has exactly the required residue field
and remains finite, local and complete over O. Ordinary local
conjugation is congruent to one and preserves the polarization.
The normalization and universal-ring steps therefore fit the
explicit predicates assumed in the paper's source audit.

The conclusion is logically compatible with K-primary vanishing:
actual TypeI/TwoPt points need not arise from a nonzero rational
strict Selmer class. The final paragraph appropriately restricts its
claim to sets satisfying CoversPt; it does not identify every
existential witness of OneCharU_s with that particular construction.

A further projector calculation must use the actual nonlinear
involution on matrix coordinates. In a generic adjoint group element,
the two lower simple-root entries are proportional to c*a and c*d;
their literal difference need not vanish. Genuine anti-invariant
functions x-kappa(x) vanish on a kappa-fixed point, but their relation
to the source's weight-minus-one length module requires a separate
argument. The current section correctly leaves that gate open.
