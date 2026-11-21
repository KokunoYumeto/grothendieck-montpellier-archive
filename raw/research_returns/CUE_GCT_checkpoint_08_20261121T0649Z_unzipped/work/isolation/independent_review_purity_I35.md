# Independent complete proof review: I-35

Reviewer: GPT-6 Astra Pro; effort not exposed; /root/purity_zero_status; run CUE_GCT-20261121-purity.

Completed/revisions reread and recorded: 2026-11-21T03:50:31Z.

Scope: complete standalone I35_contraction_gate.tex, including the repaired coefficient-field and polynomial-degree qualifications and known-background attribution. This is an independent-agent reading and mathematical rederivation, not external or formal certification. The new Parthasarathy source reopening was performed by the author; I checked its overlap with P-B16 but do not claim to have reopened it in this review.

**PASS.** The two requested precision changes have been incorporated.

## Exact contraction invariant and the Hankel example

The bilinear trace pairing sends a boundary pair to the rank-one matrix u^T v^T. Nonzero scalar contraction is exactly non-annihilation of the coefficient space. Consequently equality of rank-one annihilator loci is precisely preservation of every constant boundary contraction. The same statement over an algebraic closure handles all scalar extensions. Common rational denominator clearing does not change the annihilator space, because multiplication by a nonzero scalar polynomial is injective in the rational function field.

The anti-diagonal Hankel matrices have disjoint nonempty supports. Their generating matrix is a(T)a(T)^T, so any nonzero constant contraction is the product of two nonzero univariate polynomials, in every characteristic. The generic matrix substitution X_ij=T^(i+j) therefore collapses matrix rank from r to one and coefficient-space dimension from r^2 to 2r-1 while preserving all these contractions. The width-2r unit-factor realization is exact since products of any two upper-right matrix units vanish.

The optimal 2r-1 dimension is known completely-entangled-subspace/Segre background already in P-B16; its proof has appropriately been moved to the separate audit. For a general coefficient subspace U, I checked the stated Grassmann incidence count: the image closure has dimension at most 2r-2, meeting one projective point imposes 2r-1 conditions on the annihilator subspace, and properness of the projective incidence projection gives a nonempty avoidance open set. This is only existential, with no explicit substitution or field-of-definition bound.

## Composition, fields, and degree budget

Sequential substitution with fresh independent seed sets is valid over the rational function field in old seeds and all unprocessed variables. At each step the actual boundary row and column are constant over that coefficient field, and the assumed contraction property holds after its extension. Shared cut variables may be included in K(Z), provided the preservation hypothesis is assumed over K(Z) and all its extensions; the revised statement now says this explicitly.

The finite-grid exponent sd+z and total-degree bound D max(1,L) are valid when coordinate maps are polynomial over K in both fresh seeds and retained cut variables, with that total coordinate degree bounded by L. The repaired text excludes arbitrary K(Z) coefficients from this budget unless separate numerator and denominator bounds are supplied. Thus no uncounted shared-variable degree is hidden.

The synchronized examples check directly. The two unit factors give X-Y, separately preserve their entire local coefficient spaces, and vanish when both seeds are T. The Hankel contraction (-T,1)H(T)e1 is zero, whereas an independent boundary parameter S gives T-S. More generally any r-by-r matrix over the same seed field, r>=2, has a nonzero row/column pair with zero contraction, while that pair contracts a fully generic matrix nontrivially. This establishes the precise impossibility of the unrestricted rational-boundary quantifier, not an impossibility for restricted neighboring-boundary families.

## Rank-one multiplicative lift

The image of a corner identity is a rank-one idempotent Q. Multiplicativity confines every lifted invertible corner to Q Mat Q=E Q. A fixed readout recovering B_11 forces its scalar character to be B_11. The elementary matrices I+E12 and I+E21 contradict multiplicativity: their individual entries are one, whereas the product entry is two, which differs from one in every characteristic. A determinant twist has no effect on these determinant-one matrices. The conclusion is correctly restricted to this functorial scalarization, not all possible coefficient-dependent or nonfunctorial constructions.
