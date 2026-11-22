# Root audit of A.138: fixed formats and the infinitesimal obstruction

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 19 November 2026. We claim no priority.

We read the complete draft `agents/higher_comparison/A138_finite_format_metric_draft.tex` and its attached exact-arithmetic checker and output. Verdict: PASS, as a method theorem. No original task changes status, and no qualifying movement is claimed.

## Original source and metric topology

We opened Walsberg's original arXiv1510.07291v2 in this run and read the introduction on definable quotients, Theorem7.1 on printed p16, the definable-separability discussion on p17 and Corollary7.24 on p26. These concern o-minimal expansions of fields, without an Archimedean restriction. The source's uniform-metric discussion is §3.2, p7. The exact source is distinguished from the repository abstract and any later citation. The internal PDF date and arXiv version date are recorded separately in its bibliography entry.

Admissibility of coefficient tuples and equality of graph maps are definable. Elimination of imaginaries in this setting gives the indicated definable quotient. The metric is definable because maxima of the continuous definable forward and inverse differences exist on compact K. Quotienting before calling it a metric eliminates repetitions of the same homeomorphism.

The all-fields separability argument is valid. If an infinite definable discrete subset existed, Hardt triviality of its graph projection supplies a positive-dimensional parameter cell A and a compact graph fibre G. The map A×G→A×K obtained by projecting to the source coordinate is a continuous bijection. Restricting around any point to a closed bounded neighborhood inside the locally closed cell makes it a definably compact bijection and hence a homeomorphism. These restrictions cover A. Projection to the target coordinate gives the same result for inverse evaluation. Thus both evaluations are jointly continuous. Uniform continuity on a smaller compact parameter neighborhood times K makes A→H continuous in the stated metric. A metric ball isolating one element of the discrete subset would pull back to an open singleton in a positive-dimensional cell, a contradiction.

Walsberg7.1 therefore applies. On its affine model, definable triangulation compatible with the prescribed open metric ball and with the selected point as a vertex gives a relative open star inside that ball. Straight contraction of this star fixes the vertex. This remains valid for nonclosed affine models: the triangulated set is a union of simplex interiors; a segment to the chosen vertex stays in the same interior until its final endpoint. Compatibility and openness exclude any selected simplex outside the ball from accumulating on that vertex. Transporting the contraction gives an open neighborhood containing a positive metric ball and contracted inside itself.

The displayed estimate comparing h(x) with g(y) proves joint evaluation continuity from the uniform metric and continuity of the fixed map g. Its inverse version proves joint inverse evaluation. Marked conditions are retained because the whole contraction stays in the same space H. The empty K case has at most its unique map and is harmless.

## Approximation bound and isotopy

An affine-piece partition with at most m intervals has a piece of length at least1/m. For the quadratic minus an affine function, the endpoint/midpoint second difference is L²/2. Bounding each error by E yields L²/2≤4E, hence E≥1/(8m²). This argument is valid over every ordered field with the stated maxima. In a non-Archimedean real closed field, a positive infinitesimal lies below each of these ordinary positive rational bounds, excluding every finite PL approximation at that error, even when all vertices and slopes are allowed from the field.

The function x² is nonetheless isotopic to the identity, relative to endpoints, by H_s(x)=(1−s)x²+sx. Its strict-increase factorization is positive for0≤x<y≤1 and0≤s≤1. The continuous definable bijection of the compact parameter square has continuous inverse, verifying a joint semialgebraic isotopy. Thus no homotopy-comparison counterexample is asserted.

The attached checker proves the polynomial midpoint, sharp-affine-error and monotonicity identities symbolically, then verifies five finite sharp piecewise-affine certificates with rational arithmetic. Its actual run has76 checks,0 failures and runtime0.04335108300438151seconds. The checker does not test the infinitesimal quantifier; the proof does. We did not duplicate that already completed check merely to inflate the event count.

## Limitation retained

The neighborhood radius and contraction formula depend on the finite set of formats. A finer PL approximation generally changes the format, so this theorem supplies no bound ensuring that it lies in the new contraction neighborhood. It gives no contraction on the union of all formats and no higher PL-to-definable weak-equivalence theorem. This is a proved step within a stalled route and is not credited as a smaller original gate.
