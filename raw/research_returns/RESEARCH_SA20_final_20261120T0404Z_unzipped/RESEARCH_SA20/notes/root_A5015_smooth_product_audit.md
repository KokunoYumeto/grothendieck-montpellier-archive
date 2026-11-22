# Root audit of A5.015: a smooth polynomial product without a Thom stratification

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 19 November 2026. No priority is claimed.

## Verdict and exact scope

PASS for the complete numbered proof in `agents/maximal_locus/part_A5_method.tex`, read in full by the root. This is a counterexample to a proposed necessary Thom-stratification criterion for bundle recognition. It does not decide the original maximal-locus question: this example's bundle locus is its entire base. We assign no qualifying progress-review movement to this method obstruction.

The map over an arbitrary real closed field with any o-minimal expansion is

`f: R^2 × S^2 × R → R^3, (a,b,x,u) ↦ (a,b,u^3-b*x1)`.

Its source is a smooth algebraic five-manifold, and the explicit inverse cube-root change of variables gives a global semialgebraic product with closed fibre S². Closed bounded preimages follow from the displayed uniform bound on u. Ordinary properness is also valid over the reals; the general-field argument uses definable compactness.

## Universal stratification quantifier

The proof does not assume that the exceptional central sphere is already a union of strata. Finiteness and definable dimension force an open patch of that sphere to lie in one source stratum T. Its sphere tangent directions lie in the kernel of the stratum map at the chosen point q. We choose q where the height differential is nonzero.

Along q_t=(a0,t,x0,0), the full differential has the fixed vertical kernel `V={alpha=beta=0, dh(v)=0}`, with the u-direction free. The displayed central tangent vector has positive height differential and therefore lies outside V. O-minimality puts a tail of this curve in one stratum S. Every restricted kernel is contained in V. Its fixed-dimensional Grassmann limit exists over every real closed field: the orthogonal projection matrices are definable and bounded, and their endpoint limits preserve idempotence, symmetry and trace. This avoids an invalid use of sequential compactness in a non-Archimedean field.

If S=T, continuity of the constant-rank kernel bundle gives the contradiction. If S differs from T, the frontier axiom makes the pair incident and Thom a_f requires the excluded central vector to lie in the limiting kernel. Arbitrary finite compatible refinements of both source and target are covered. Thus the proof excludes every such finite ambient C¹ Thom stratification near each stated base point.

## Source and certificate checks

The original Giménez Conejero–Lê–Nuño-Ballesteros article was opened at Definitions 2.1–2.2, DOI `10.1007/s13398-022-01353-y`; the tangent-kernel convention agrees with the proof. The proof of the counterexample itself is supplied in full rather than inferred from that citation.

The root read the entire attached symbolic checker and reran it independently. `logs/root_A5015_smooth_product.json` records 12 PASS checks in 0.047369758001877926 seconds. These check the inverse cube identity, tangent relation, height differential, approach curve, vertical differential, excluded direction, free u-direction and nonzero rank minor. They certify only the finite polynomial algebra; the universal stratification argument is the mathematical proof above. The author's separate timing is preserved in the author's output.

The earlier rational-graph construction remains valid route history. The smooth polynomial construction strengthens that method obstruction, without promoting the original A.5 row to proved or refuted.
