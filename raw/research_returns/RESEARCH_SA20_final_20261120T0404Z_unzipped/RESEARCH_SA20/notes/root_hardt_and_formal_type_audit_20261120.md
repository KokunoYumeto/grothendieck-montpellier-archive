# Root audit: two method diagnostics

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 20 November 2026.
We claim no priority. These are method diagnostics, with no original-row
closure and no qualifying movement of a main gate.

## Constant torus fibres and a fixed Hardt partition

We read the complete note
`agents/maximal_locus/notes/hardt_stratum_and_compactness_test_0241.tex`,
including the appended compact-cube observation, exceptional-point scope
discussion, and verification paragraph. The final inspected SHA256 is
`ec3366cafb240338bd878d9a1a829c2c8cebbb3bf671b4198bb1810ee6fd20c3`.
We also read the complete checker and the independent full-text audit in
`agents/singularities_duality/logs/Hardt_stratum_fold_independent_audit.md`.

Verdict: **PASS for the stated diagnostic**. The quotient formula has
matching endpoint values and joint continuity. The three inverse points
are distinct and exhaust the fibre of the chosen nonvertex target.
The compact-complement distance and inverse straight-segment argument
give a positive uniform distance from every definable homeomorphism,
over every real closed field. Over the reals the same connectedness
argument applies to arbitrary homeomorphisms. The total space is closed
and definably proper, with the stated explicit products off the origin
and on the entire first-coordinate axis. A product near the origin
would force the folded map to be uniformly approximated by the inverse
fibre homeomorphisms along the second-coordinate ray, contradicting
that positive distance.

We reran the actual checker: **31/31 PASS in
0.06048262500189594 seconds**. The exact returned inverse representatives
were 1/24, 5/8 and 17/24, with square-circle points (1,1/6), (0,1/2)
and (0,1/6), respectively. The full author and independent rerun outputs
are attached in the two agent log directories. These algebraic checks
do not substitute for the preceding topology proof.

The example proves that membership in the actual local-bundle locus
need not be constant on a connected stratum of a chosen Hardt partition,
even when every fibre is the same closed PL torus. Its bundle locus is
the definable set R^3 minus the origin. It therefore does not disprove
definability of the maximal locus or exclude richer finite transverse
certificates.

We also checked the separate increasing-open-cover example. Each finite
union is ambient open; restriction to a compact cube does not make the
proper open subset being covered compact. The external union has
infinitely many interval components on one line and is not definable.
The note correctly does not realize that union as a chart locus of a
definable map. The exceptional-point paragraph identifies a uniformity
requirement and does not assert that the earlier fixed-map theorem
already settles it.

## Ordinary rank-four formal type

We read the complete note
`agents/higher_comparison/logs/ordinary_rank_four_formal_type_20261120.tex`,
SHA256 `d0c4b4fc8faeb6838f4f4c8382f4647c2bf0316655ba0bd4d38380494938992f`.
Verdict: **PASS as a formal consequence of the previously inspected
finite-rank inputs in A.128 and A.132**. For the stated homotopy-fibre
conventions, X -> Y -> Z is the correct fibre sequence. The segment
0 = pi_4(Y) -> pi_4(Z) -> pi_3(X) = 0 proves pi_4(Z) = 0 without an
assumption on pi_4(X). Together with the lower groups and connectedness,
this gives the ordinary 4-type K(F_2,3).

This calculation does not concern the equivariant sign-representation
germ quotient, does not identify the PL image in the A.162 kernel, and
does not provide the proper relative geometric realization required on
the compact RP^3 cylinder. We record no new numbered theorem or movement
credit for this consequence.
