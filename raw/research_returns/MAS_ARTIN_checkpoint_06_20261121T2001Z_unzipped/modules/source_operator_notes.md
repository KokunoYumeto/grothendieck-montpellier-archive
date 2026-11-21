# Source operator audit: complete findings and scope

The complete new proofs are in `source_operator_audit.tex`, MA-LA-008–013. All source copies and rendered pages remain private.

## Source checks actually performed

Read the complete pp. 514–520 local proof and use, rendered pp. 515–516, the S00 definition on p. 259 and proof pp. 260–261, the actual finite tensor statement/proof in Proposition 2.1.4.1 pp. 71–72, and the contrasting multiplicative-Schwartz remark on p. 63. Re-read Proposition 5.3.4.4 pp. 263–264, the global orthogonal projection and condensation on pp. 488–489, the shell overview pp. 491–494, and the relevant complete indentation statement/proof interface pp. 508–513. The full source chain was inspected; the reported failures are not a generic rejection based on missing prose.

## New literal failures

1. LA008: the p. 515 representative has the output factor |x|^(1/2); equations 12.4.1.5/7 omit it. A coordinate pullback can repair this, but changes the diagram.
2. LA009: the raw kernel's input-coinvariant tensor containment fails for a concrete valid compact test and a flat unit-shell input. The raw kernel is equivariant; quotienting output is essential.
3. LA010: the product-norm multiplier does not preserve the additive Schwartz LF space. A Gaussian-times-p-adic-ball input has no uniform local-constancy level after multiplication; an annulus does not fix this mixed-place defect.
4. LA012: the actual bounded raw-cover cutoff/convolution/Fourier composition commutes with a mixing unitary p-dilation. It is noncompact whenever nonzero, with explicit nonzero outer and annular examples. Source p. 515 states quotient nuclearity, so the report does not attribute a separate full-cover trace theorem to it.

## Constructive repairs

LA011 defines the actual flat additive LF subspace explicitly, avoiding a source notation conflict between multiplicative Schwartz and compact-away-zero additive functions. Shell folding is finite on each LF stage and gives a continuous quotient section. Fourier destroys finite valuation support, but its exact section-periodization is a bounded all-pass dilation factor times the even real Fourier transform. This is a unitary involution on ordinary even L2. Multiplicative convolution followed by an annular position cutoff has a compact smooth log-coordinate kernel, so composing it with the unitary quotient Fourier cutoffs gives a genuine nuclear quotient operator. The common rank-one series justifies trace cyclicity on that local quotient.

LA013 computes an actual trace-class one-sided cutoff commutator of the unitary Euler phase. Its trace is the centered local prime sum in both directions, and the phase-c version has c^k and conjugate(c)^k in the two directions. Finite-prime products add traces by bounded cyclicity. This is an operator realization, not a scalar trace definition.

The section B has no bounded extension from the full additive L2 space: N mutually disjoint unit translates have norm sqrt(N), while their folded output has norm N. This does not refute the bounded compressed Fourier map from the chosen quotient section.

## Exact remaining scope

No equality with the global weighted orthogonal Paley-Wiener projection is asserted. Nor is the coupled annular double-cutoff limit replaced by the one-sided commutator. A literal smooth Fourier multiplier cannot itself be an orthogonal projection, but the source never prints that equality; the observation is only a refutation of a possible unstated substitution. The narrow absent statement is a compatible nuclear global/local factorization and matching second cyclic composition, with the limiting remainder and polar terms controlled. WP/EG already compute the actual global completion and cutoff trace independently.

MA-RS-004, separately written in `regularized_smooth.tex`, shows that under the fixed horizontal gap supplied by A for rational zeta the natural regularized Cg Z[J,Mphi] is trace class for every compact smooth test. Thus neither the bare Mobius obstruction nor the raw-cover noncompactness is misrepresented as an impossibility theorem for all smoothed quotient transports.

## Subsequent local closure: MA-LA-014

The coupled annular limit is now proved separately in `local_quotient_limit.tex`, using the correct-order trace-class endpoint operator. It gives A0+B_S when XY tends to infinity and epsilonY tends to zero, and zero for the large-inner-ratio path. Thus the local quotient/prime/coupled-limit construction is closed in the rational trivial sector. The global weighted PW identification remains separate.
