# Independent audit of the elementary exceptional lattice

Completed 19 November 2026, 15:12:40 UTC. Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode; run RESEARCH_SA06 `/root/frobenius`; inherited effort setting not separately exposed.

The full appended elementary proof EC.7–EC.11 in `agents/cycles/exceptional_cubic_lattice_draft.tex` passes. Read-file SHA256: `6bc0b6352c2f26e2e466be4ad77052f2bc0aa8a7419c9e43f6743d939b40cb3a`.

The cubic chain norms (1,2,4), the lowering map, the projective-space coefficients, and the commutator signs are correct. In weight (-2), the separate adjoint argument proves injectivity of the square without assuming injectivity in weight zero. Thus multiplication by (b^2) is injective on degree (s-1) for every (m\ge0). The free α/q terms of the whole Chow group then vanish using the nonzero integer degree of the curve polarization, and the exact remaining kernel is the Smith kernel on the full divisible Picard group. Nonunit Smith factors do not imply absence of prime-to-characteristic torsion.

The earlier EC.1–EC.6 codimension-three endpoint proof was also read in full and passes: the free part is killed by the two integer equations, and the remaining Picard class is killed by both two and three. The report has inspected the stated finite table, but has not rerun its program or independently recomputed every Smith form. The integral ring presentation and exact Jiang/Stacks/Huybrechts inputs are the ones already audited in the combined safe-range proof.

This is an auxiliary lattice audit only. The entire exceptional image in a local Chow group requires the additional geometric and relative-invariant argument; it is not inferred from the lattice computation alone.
