# Embedded cuts versus geodesic representatives

`sections/part_a1_cut_choice.tex` completely refutes the construction of
pointed-cap antiisomorphisms for arbitrary smooth embedded cut circles,
even when the circles and the boundary maps are analytic. This resolves
the definitional choice mentioned at the start of the parent's A1 section.

Take two pants with one boundary of length 2*pi and two cusps each. Weld
their canonical arclength circles by theta2=-theta1+(1/2)sin(theta1).
The derivative is in [-3/2,-1/2], so the map is an analytic reversing
diffeomorphism. In the canonical cap coordinate its analytic collar
extension is H(w)=w^-1 exp((w-w^-1)/4), locally biholomorphic along the
circle. Thus the welded surface and seam are analytic; cutting recovers
the same conformal pants and their same canonical hyperbolic metrics.

Any antiisomorphism of centered discs is w->c*conjugate(w), so its boundary
derivative is constantly -1. Our angular derivatives at 0 and pi are
-1/2 and -3/2. Consequently the actual seam identification does not
extend to the asserted cap antiisomorphism, and no tensor can be obtained
by that specific construction. This does not rule out inventing a
different tensor assignment; it proves that the text's assignment lacks
the needed hypothesis.

If cut datum means an isotopy class, use the canonical geodesic
representative of the entire surface instead. Both sides inherit the
same metric there and are identified isometrically. The previous exact
range theorems then apply. That interpretation explicitly changes the
embedded seam in this counterexample.

`code/part_a1_cut_checks.py` and its output certify all finite rational
inequalities used in the explicit example. No numerical sampling is used.

Primary text: original cote67 scans074--075 were visually checked.
The new argument depends only on the proved analytic-welding special
case and the Schwarz lemma. No additional external literature is asserted.
