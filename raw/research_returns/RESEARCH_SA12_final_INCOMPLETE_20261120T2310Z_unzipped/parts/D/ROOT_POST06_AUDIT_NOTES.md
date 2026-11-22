# Root audits of separate post-checkpoint fragments

2026-11-20T04:38:36.971890+00:00

Root read the complete D_finite_exceptional_wild.tex and D_elliptic_surface_boundary.tex, and the complete Part C D_positive_genus_residue.tex. All three arguments pass the targeted audit. They remain separate, unintegrated fragments during the checkpoint06 paper freeze. No change to the compiled checkpoint06 claims is inferred from their existence.

The single-curve calculation includes all additional exceptional curves, preserves the map to the base resolution through every rational (-1)-contraction, uses separable residue degree in Riemann–Hurwitz, and computes the full differential determinant. Its genus-one equality rules out inseparable residue as well as wild ramification index. The global corollary glues local resolutions over disjoint singular neighborhoods, obtains a projective regular proper surface, and uses connected proper-birational pullback plus the projective fixed-boundary theorem. The finite wild-image criterion kills finitely many inertia images by an open normal subgroup and applies the same projective theorem after normalization.

Primary sources independently opened by root on20November2026:

- Stacks0C5P, Lemma54.16.11: regular proper surfaces are projective. Exact statement and proof opened.
- Stacks0C1D, Lemma53.12.2: Riemann–Hurwitz for generically etale maps of smooth proper curves. Exact statement and proof opened.
- Stacks0BUA, Lemma58.13.5: inertia/wild-inertia exact sequence for possibly infinite Galois extensions of a DVR, with arbitrary residue field. Exact statement and proof opened.

No priority is claimed. These are proof checks, not formal stopping reviews.

## Additional root actual-file audits, 2026-11-20 04:57 UTC

The complete files `parts/C/D_rational_tree_Qfactorial.tex`, `parts/B/D_prime_to_p_index_B.tex`, and `parts/D/D_mixed_surface_boundary.tex` were read and pass a targeted proof audit. This records the actual files, not an approval based on agent summaries.

For rational trees, the negative-part argument produces a positive anti-nef exceptional cycle with strictly negative intersection against every component. The degree criterion makes its inverse normal bundle ample, and Serre vanishing makes the Picard transition maps injective and the units transition maps surjective. A single finite nilpotent thickening then bounds the p-power exponent. Compatible trivializations, degree-zero formal functions, properness over a local base, and faithfully flat completion give actual triviality on the resolution. The determinant of the intersection matrix clears every numerical correction. No vanishing of the geometric genus or rational-singularity assertion is assumed.

For the prime-to-characteristic index theorem, the chosen connected component of the canonical torsor is a cyclic Galois cover of degree dividing the given index. Its canonical sheaf is trivial on the punctured surface and hence reflexively trivial on the normal surface. Normal surfaces are Cohen--Macaulay, so this is Gorenstein. Tame discrepancy equality preserves both log canonicity and the existence of a discrepancy-minus-one valuation. The compositum argument transfers all-valuative tameness to every original cover. The SNC persistence proof explicitly includes separability of residues.

For the mixed surface corollary, connectedness of pullback along a proper birational map follows from normality and the unchanged generic field. The finite local groups at log terminal points supply finite wild images; the elliptic and cusp cases supply zero wild images. The finite-exceptional-wild criterion then applies. Regular omitted points impose no extra divisorial condition. The nonnormal variant uses the finite component-normalization descent already proved in the paper.

Root independently opened the complete statements and proofs of Stacks tags 0B5Y (Lemma33.44.15), 0B5U (Lemma30.17.1), 0C6R (Lemma37.4.1), 02OC (Theorem30.20.5), and 02KH (Lemma30.5.2). Root also opened section0EXT on tame extension towers. The Tanaka2014 arXiv source was successfully downloaded and extracted once to `sources/Tanaka2014/tex/source.tex`; its positive-characteristic uses of projectivity for proper Q-factorial surfaces were located. The source acquisition and extraction have complete logged outputs.

The all-log-canonical extension is still being written and audited at this time. These checks do not promote it before its complete argument has been read.


## Root audits of the stronger lc and mixed-boundary arguments: 2026-11-20T05:03:11.650290+00:00

Root read every line of `parts/B/D_all_lc_core_B.tex`, `parts/C/D_surface_mixed_boundary.tex`, and `parts/C/D_fixed_boundary_mixed.tex`. All seven numbered statements in these files pass the actual-file audit. The cycle identity includes internal multiplicity greater than two and all outside neighbors. The quasi-etale source is Q-Gorenstein and lc by the full different inequality; integrality of discrepancies is not used. A nonzero finite-index image in the target cycle's profinite fundamental group forces a cyclic source core. Galois transitivity then forces equality in every different bound, including residue separability.

The global argument retains Q-factorial omitted points and resolves the other singularities. Its projectivity proof explicitly checks both positive intersection with every curve and positive self-intersection. Root independently opened Fujino's author PDF Lemma2.2, printedpp6--7, including the characteristic-zero convention onp5; the short reproduced argument is characteristic-independent, and Tanaka2014 applies that fact in positive characteristic. The fixed-boundary extension lists all new divisors and proves that their centres are isolated points of the original boundary, where the covers are quasi-etale. The precise comparison is a surjective homomorphism from the projective fixed-boundary quotient to the originally requested quotient.

Editorial requests (status heading, Q-factorial wording, and explicit spreading from a local germ) were communicated before integration. No mathematical correction was needed. The original unrestricted D questions have not been marked solved.
