# A5.019 reconstruction and fresh author recheck

Author/rechecker: `/root/maximal_locus2`, GPT-6 Astra, OpenAI.
Date: 20 November 2026, after executor recovery and checkpoint 19.
Source: `agents/maximal_locus/part_A5_radial_angular_gate.tex`.
SHA256: `fc5758ef0265ea69427535a9554c69ac252de7a8f6f2250e2a63847aa7963966`.

## Provenance and verdict

The pre-outage A5.019 proof had full root and higher_comparison2 independent mathematical PASS, including the general-target extension and explicit angular-certificate/saturation criterion. Its original four TeX chunks were sent to root. This physical file is a mathematical reconstruction from those retained proof messages, not a byte-identical recovery. The complete reconstruction has now been freshly read and checked by its author. **Fresh author recheck: PASS.** A new independent authored-text audit has been requested; this note does not mislabel the author check as that independent audit.

## Precision edits made during the recheck

- The angular family is explicitly restricted to 0 < t <= t0 <= 1.
- The comparison map T_(w,s) is explicitly typed for 0 < s <= rho(w) < c_*(w).
- The scalar parameters in the angular first-order certificate are explicitly in (0,1].
- For the general-target extension, finite auxiliary map formats are fixed and their coefficient tuples are selected from their first-order validity sets by parameter-preserving definable choice. The choices therefore lie in definable closure of the original named coefficients. No extra unnamed constants silently enter the final complete-theory argument.
- The chart dimension m is explicitly the local target dimension, which need not equal the dimension of the open simplex containing the centre.

## Freshly checked proof chain

1. Properness gives the compact scalar domains. Empty fibres are handled by the open complement of the closed image; dimension-zero regular target points are isolated.
2. Scalar triangulation is certified by one finite graph formula, finite complex, finite ambient dimension, and affine vertex-height data. Every elementary model is o-minimal. Compactness gives a finite scalar-format cover across the fixed complete theory without transferring cell-likeness or assuming effective enumeration.
3. Descending stellar subdivision of every original mixed face has matching combinatorics. Every old zero-positive edge is removed, so each lower height band is exactly the zero/new-vertex subcomplex. The resulting slice maps are PL, while joint coefficient dependence is only rational definable.
4. A genuine local chart implies the finite PL product-pair filter by restriction to a smaller compact band, height-band matching, and relative definable Hauptvermutung. Positive vertices are necessary for a nonempty admissible product with m >= 1. Fibre-manifold filters remain separate finite labelled-pair conditions.
5. On the fixed product pair, a common triangulation makes g = ell_0 P and r = ||v||_infinity PL with identical zero subcomplex. Matching their small stellar bands yields a fixed exact radial product map Psi. Thus G_w has exactly the target radial norm rho(w)||v||, not merely a comparable norm.
6. The angular homeomorphism criterion is necessary and sufficient. Necessity restricts a normalized local chart to each target-radius sphere. Sufficiency uses uniform convergence in the L-coordinate, bounded angular coordinates, and definable compactness to extend to a homeomorphism on a closed central band.
7. The explicit rational R_(w,s) and its stated inverse are valid on every original simplex and match on faces. The retraction Q gives Q R = q. The difference between old q-control and new projection-control is at most d_w(s), tending to zero, in both directions.
8. Moving stellar charts preserve every original target simplex, hence the union S representing the target. They yield finitely many moving target-chart formats, including centres on lower-dimensional simplices inside a higher-dimensional manifold. Compact closed subcubes give compact proper inverse images.
9. The sentinel in e_j excludes empty valid-map sets. The bounded definable scalar function has a limit; its liminf zero gives arbitrarily small valid errors for all sufficiently small radii. Definable choice need not be continuous. Hardt triviality of its compact graph fibres, followed by projection on compact internal intervals, supplies joint evaluation and inverse continuity on a terminal interval.
10. The exact locus equals the union of the individual first-order angular certificates in every model. In a sufficiently saturated model where that locus is definable, saturation yields a finite subcover. Each individual containment in that fixed finite pool is a first-order sentence over the original named coefficients, so completeness transfers it to every model. Definability in one unsaturated model is not used as a substitute.

## Exact scope

The result normalizes a fixed proper map to finitely many fixed product-link angular problems and characterizes all-model definability by a finite pool of those exact certificates. It does **not** prove existence of that pool, does **not** assert uniformity in an external family f_u, and does **not** close original A5 or independently prove the rarity/privileged-recursion assertions.

## Original-source locators

Shiota, arXiv:1002.1508v3: Theorem 2.1, printed p.5 (compatible o-minimal Hauptvermutung), and Theorem 2.2(1), printed p.6 (exact scalar triangulation over an arbitrary o-minimal real closed field). These exact original statements were opened and audited before the outage by root and higher_comparison2. The fresh attempted open of the versioned PDF during this reconstruction returned DisabledError; no new claim is inferred from that failed retrieval.
