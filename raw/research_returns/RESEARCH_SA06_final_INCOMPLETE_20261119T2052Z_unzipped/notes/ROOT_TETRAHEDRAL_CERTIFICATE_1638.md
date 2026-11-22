# Root inspection of the finite tetrahedral certificate

19 November 2026, 16:33–16:38 UTC. AI-produced by GPT-6 Astra (OpenAI), ChatGPT Pro mode, `/root`; effort setting not separately exposed.

We read the entire source `agents/real_weil/code/check_tetrahedral_spectrum.py` and every field of `agents/real_weil/output/tetrahedral_spectrum_certificate.json` in separate, untruncated tool outputs. An earlier combined output had been truncated and was not counted as a complete inspection. We did not rerun the program.

The retained run began at 2026-11-19T16:26:48.397788+00:00 and reports 15 passes out of 15, with runtime 0.05785261599521618 seconds. Its full scope is finite cochain linear algebra and one symbolic symmetric-matrix identity. It does not certify K-theory descent, comparison with Chow groups, or actual lifting over any parameter scheme.

We checked the two displayed oriented simplex coboundaries, of sizes 6×4 and 4×6. Their product vanishes, and both have rank3. Thus the rank part has cohomology dimensions1,0,1. We checked every column of the 6×34 Picard restriction matrix: four hyperplane columns and five point-exceptional columns for each of six edges. Choosing the first exceptional column on each edge gives exactly −I6, so the Picard restriction is integrally surjective and has rational kernel dimension28. Four component-degree classes then give total degree-zero dimension1+28+4=33. The middle total dimension vanishes, and the component point counts are15,10,5,0.

Finally we inspected the symbolic expansion of x-transpose B x minus the expression obtained from the four row sums and the six terms B_ij(x_i−x_j)². It is identically zero for a generic symmetric4×4 matrix. The separate mathematical proof in TC supplies the positive off-diagonal entries and strictly negative weighted row sums; the program does not establish those geometric hypotheses.

The full proof audits remain `ROOT_TETRAHEDRAL_SPECTRUM_REVIEW.md` and `ROOT_TETRAHEDRAL_RAW_CHOW_REVIEW.md`. This receipt adds an inspection of the retained finite certificate, not a new independent execution, numbered statement, or main-question movement.
