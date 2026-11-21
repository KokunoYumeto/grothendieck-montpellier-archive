# Independent whole-proof review of I-21 and source-scope record

Reviewer: GPT-6 Astra Pro, `/root/purity_zero_status`; effort not exposed. Run CUE_GCT-20261121-purity.

Read `work/isolation/I21_width3.tex` completely. The standalone original-coordinate width-three theorem passes. The critical profile-{0,2,3} concentration was also independently derived in `independent_width3_profile_purity.md`, with an exact sharpness example checked separately. This record does not certify the source preprint's general-width, affine-orbit, or later-section statements.

## Source read and provenance actually inspected

Read Liu (2026), printed pp. 5–7, Theorem 3.2 and Lemmas 3.3–3.6 in full, and the interpolation-pair part of §3.4 on pp. 9–10. The direct specialized proof does not use Lemma 3.5's Hasse-order estimate or the shared-prime generator. Source: https://hexagonmath.org/pdf/2611.00634v1 , web refs turn877817596view0 and turn754880818view0.

The host record https://hexagonmath.org/2611.00634v1 was opened independently, ref turn830526403view0. It gives November 19, 2026, version1, CC BY4.0, and explicitly labels the text primarily AI-generated with no parts marked human-understood. The acknowledgment/provenance describes OpenAI-assisted formulation, proof development/review, drafting, and finite checks. The repository policy https://hexagonmath.org/about , ref turn643684521view1, states that dissemination is not a correctness or novelty judgment. The identifier is Hexagon, not arXiv.

## Critical proof and attempted failure points

The compatible cut complements in the rank-two case exist: each suffix followed by projection along the final complementary line has rank two, so its kernel is a one-dimensional complement respected by the transitions. The stable-projection suffix argument uses an invertible top-left block over a nilpotent local algebra and a genuine row-module graph identity. It produces a coefficient-span containment, and the separate constant-lift restart supplies the support-cost control. This distinction was checked explicitly to avoid transporting generic rank or saturation incorrectly.

Kernel bases at each restart may be linear combinations of retained coefficient rows, but this preserves the span filtration by maximum support. Subsequent disjoint-variable multiplication then expresses their images as linear combinations of actual coefficient rows of the stated larger support. The initial passive-only segment costs zero in ordinary support because its sole starting row is assigned the kernel cost one. The sharp four-factor example attains the two projection growth/reset cycles and confirms that reducing the profile bound below four is impossible.

## Rank tests and simultaneous preservation

For a rank-r target interval, all its prefixes after the first rank-r prefix have rank r. The shortest rank-r suffix exists; appending the next factor has rank at most r from that suffix and at least r because the full target factors through it. Minimality makes the test interior have rank greater than r. Once the prefix is preserved, the specialized suffix has rank exactly r because it contains the prefix row space and cannot exceed its generic rank. Equality of those two row spaces is the correct induction input.

For r=2, second compounds have width three and the higher-rank chunk is invertible at the center on every subinterval. For r=1, the chunk has preserved rank profile {2,3}. Extracting the prescribed endpoint powers from a lowest-degree monomial cannot create a lower-degree surviving chunk term: that would contradict its original minimal degree. Hence the support bounds four and six apply to every needed lowest component.

Fresh SV pairs are independent of the previous parameter field. Setting their selectors to coordinate nodes detects any nonzero polynomial with a low-support coefficient over that field. Homogeneity in the new amplitudes separates the lowest component from all higher ones. Each selected minor is nonzero in the common parameter ring, so the product of the finitely many selected minors is nonzero. Setting the new amplitudes to zero retains all earlier minors. These facts justify simultaneous preservation; no different numerical parameter choice is made for different hidden intervals.

The common center t works for original coordinates in every characteristic: each nonzero univariate determinant remains nonzero at a transcendental t. The construction uses no unknown order. Appending constant boundary matrices makes preservation of the full rank-one word exactly the required scalar nonvanishing.

## Sampling and endpoints

The final pullback has t-degree at most D, each selector degree at most (n−1)D, and total amplitude degree at most D. The first grids preserve some nonzero amplitude polynomial. The Newton simplex matrix is triangular under an order refining total degree and has nonzero diagonal for arbitrary distinct field nodes, in every characteristic. This yields the exact stated count. At n=1 the selector polynomials are constant and the selector grid has size one, as required. The extension-field query requirement is explicitly retained; the proof does not assume an unauthorized base-field simulation.
