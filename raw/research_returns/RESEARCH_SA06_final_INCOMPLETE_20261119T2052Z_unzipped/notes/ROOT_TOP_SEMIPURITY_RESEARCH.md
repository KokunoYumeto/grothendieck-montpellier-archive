# Top ordinary quotient: semipurity and a tetrahedral exceptional fibre

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), /root, 19 November 2026, 15:26–15:31 UTC. Research only: no numbered conclusion or main-gate movement.

## New primary source and its exact limitation

Opened and read Weber (2012), *Purity of boundaries of open complex varieties*, Journal of Singularities, 4, 171–179, DOI10.5427/jsing.2012.4j. The full nine-page journal PDF is https://www.journalofsing.org/volume4/weber.pdf . Proposition3 and Lemmas9–10 identify the lower-weight boundary terms. Theorems11–14 and their Section7 proofs give the purity bounds; Remark13 permits localization at a boundary component, and Remark16 discusses the isolated-point case. For an isolated N-dimensional complex singularity the relevant exceptional cohomology is pure in degrees at least N. This is a complex rational-cohomology statement. It neither identifies Chow kernels nor supplies actual ordinary families on a resolution. The separate author URL https://www.mimuw.edu.pl/~aweber/ps/purend.pdf returned403; the source's reference13 identifies arXiv0809.1885, not yet separately opened by root.

Searches also used the exact phrases local Chow group algebraic equivalence punctured spectrum; exceptional divisor K0 Chow simple normal crossings; and isolated singularities algebraic equivalence one-cycles. The returned numerical-equivalence and singular-zero-cycle references did not directly prove the ordinary top-quotient assertion. They were not treated as interchangeable with it.

## Why the simple multiplicative extension failed

The earlier Pm×triangle attempt would have top-edge unit gluing. Along a double stratum its total normal line cannot be negative when both attaching normal lines are trivial. The required smoothing coefficient acquires zeros; resolving the resulting uv=tau w points introduces divisor classes that hit the intended top-edge degrees. Semipurity offers a cohomological explanation for that obstruction in dimension at least three, but does not close the ordinary Chow gate.

For an SNC exceptional divisor E=sum E_i with a positive exceptional combination D=sum a_i E_i and −D ample on E, root derived a possible elementary check of the corresponding numerical edge obstruction. If antisymmetric coefficients x_ij satisfy sum_j x_ij[D_ij]=0 numerically on each E_i, intersect with D_ij and an ample (d−2)-power. Summing the resulting equations with weights1/(a_i a_j) gives, for each triple, the square

    (a_k x_ij − a_j x_ik + a_i x_jk)^2/(a_i a_j a_k).

The left side is sum_(i<j) x_ij² deg(D|D_ij·h^(d−2))/(a_i a_j), negative for any nonzero x, whereas the triple-intersection coefficients on the square side are nonnegative. This suggests surjectivity of the top-degree numerical edge restriction map. The indexing for disconnected strata and the full passage from this numerical map to the K-theory descent complex remain to be written and checked. This note does not register that proposed lemma.

## A different candidate and the actual obstruction

The three-dimensional affine hypersurface with leading tangent cone xyzw and a degree-five correction G5 suggests a tetrahedral exceptional divisor. Choose G5 nonzero at the four coordinate vertices. Blowing up the origin formally gives xyzw−tau G5=0 over P3. At a triple vertex the tau derivative is nonzero. Along double edges, zeros of G5 lead to ordinary local models uv=tau w, admitting the familiar two small-resolution charts. It remains to prove and specify a compatible global projective resolution and all local hypotheses; no counterexample is claimed.

The dual complex is initially S2. Its potential K2(k) contribution lies below the range ruled out by H3 semipurity. Thus cohomological purity alone cannot discard this candidate. However the retained proper-curve K2 realization lemma already shows that every Milnor symbol can be obtained as an actual K2(P) evaluation difference on a proper curve. Consequently K2(k) by itself is not an invariant of the ordinary quotient on the exceptional configuration. The exact issue is whether these classes and their proper-parameter families lift to the regular resolution, through the supported/negative-K boundary in pro-descent. Conversely a prospective exceptional K2(k) class might fail to lift at all. The owner of the top-quotient branch is examining these maps. No vanishing, nonvanishing, or gate reduction follows from the tetrahedral picture alone.
