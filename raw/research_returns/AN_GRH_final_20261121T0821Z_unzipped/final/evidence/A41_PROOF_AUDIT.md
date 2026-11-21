# A41 author whole-proof audit

Date: 2026-11-21. Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.

**PASS — author whole-proof read.** I read the complete source `A41_ALL_REFLECTION_IMAGES.tex`, SHA256 `c046d444a2e779c15cf7c719d4a44736c38c73e8f75ccb8ae18ac500a7d210a7`, after writing it. A final citation-only delta, checked after reopening Milne's multiplication formula, gives SHA256 `5523c5a2550a1118c6f523493e6a16da3dddfd6fa9acee0b6660e682e59599e1`; no mathematical assertion changed. The quantitative refinement was proposed by root and independently checked in outline by row_audit; this is the author's complete proof check, not an additional independent review. All three other agents have been sent the whole source for separate review.

## Result and its exact limit

For the fixed A13 ordinary RM5 target over F128, at least 95 rational parameters of the inverse family in A40 give smooth genus-six cyclic-quintic constructions over F128 itself. Each cover has at least eleven rational split source points for which every reflection image of every lift has canonical class of exact order 4159. The multiplicative order of 2 at this prime is odd, so none of those images has the sufficient canonical-prime detector of A29. This persists for the same classes under extension of constants.

This establishes simultaneous failure at all five reflection choices for one fixed cover and source point. It does not exclude choosing another cover or another method, does not specify the source's two-rank, and is not a point-section counterexample. The family is intrinsically specified by A40; no individual parameter or inverse-cover equation has been numerically selected or enumerated in this proof.

## Complete checks

1. The critical fibre product is a Cartier divisor with numerical class twice each fibre. Since the two canonical double maps are separable, it is generically reduced. Its Cohen--Macaulay local rings have no embedded components, so the reduced curve is exactly this divisor, without an unnoticed multiplicity factor.
2. For H = h*O(TTheta), the vertical restriction is the pullback along a translated multiplication-by-two Abel map. Multiplication by two scales Neron--Severi classes by four; the intersection with TTheta was three in A40. Thus the vertical degree is twelve. The horizontal image is a translate of TTheta and has degree two against its own line bundle. Therefore Z.H = 2*12 + 2*2 = 28.
3. A40's noncontainment result makes this intersection proper on every component. Each point contributes a positive local intersection length, so there are at most 28 geometric points and at most 28 resulting bad parameters. The separate vertical condition has at most two preimages of each of three canonical branch values, adding at most six. These are all the singularity cases of A40, and every residual member was already integral.
4. On A13, choosing a rational Weierstrass theta characteristic and the established F2-defined T gives an F2-defined family. Among 129 F128 parameters at most 34 are excluded, so at least 95 are good over this exact field. The involutions are the unique automorphisms of the separable degree-two projections; hence they, their order-five product, the cyclic quotient and the whole diagram are defined over F128. No fifth roots of unity are required for a constant etale C5 action obtained this way.
5. The A40 isogeny is over F128. Since the trace of the fixed target E is zero there, the trace of D equals that of its genus-two cyclic quotient C. Thus #D = #C, and the genus-two Weil bound gives #D >= 84. This is a symbolic trace/count deduction; no individual source curve count is claimed.
6. The inverse images of three Weierstrass points under five maps of degree two have at most thirty geometric points in total. At least 54 rational D points avoid all of them. All their images are non-Weierstrass F128 points of E, so A38 gives exact canonical order 4159 for each.
7. This set is invariant under the free constant C5 action, hence has cardinality a multiple of five and therefore at least 55, furnishing at least eleven distinct split source points. Deck lifts permute the five images. Conjugation by the five powers gives all five reflections because five is odd; a further quotient identification preserves canonical orders. Fixed geometric orders do not change under extension of constants.

## Inputs and computation scope

The geometric input is the complete checked A40 proof, not a numerical heuristic. The fixed-target counts and exact order residues are those of the independent F128 arithmetic certificate retained with A38. They were previously read and executed in this run and are carried here with that exact scope. The Weil point-count statement is Milne, *Jacobian Varieties*, Theorem11.1, https://jmilne.org/math/xnotes/JVs.pdf, already reopened and read for A38. No new finite-field enumeration, symbolic search, or formal verification is claimed for A41.

For the final explicit primary citation in (AI.4), I reopened and read Milne, *Abelian Varieties*, Corollary6.6 on printed p.9, its complete displayed proof, and Remark12.13 on p.24, https://jmilne.org/math/xnotes/AVs.pdf. They give the multiplication-by-n pullback formula and its action by n squared on Neron--Severi classes in arbitrary characteristic. Retrieval references: `turn556458508view0` and `turn556458508view1`.
