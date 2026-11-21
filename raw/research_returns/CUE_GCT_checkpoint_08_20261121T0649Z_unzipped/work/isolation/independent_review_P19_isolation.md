# Independent full proof review: P-19

- Reviewer: GPT-6 Astra Pro; effort not exposed; agent=/root/isolation; run=CUE-GCT-20261121-I.
- Actual completed reading/check recorded: 2026-11-21T06:18:11.308460+00:00.
- Exact reviewed file: `work/purity/P19_all_cubic_balanced.tex`.
- SHA256: `4bb5f2f9588840bf41986b657ba3493ebd92cda0f01bea09f52ba896b1535cee`.
- Outcome: **PASS**. This records a full reading and mathematical rederivation, not a numerical execution or a claim of historical novelty.

## Scope checked

The theorem concerns every homogeneous multilinear cubic with a width-at-most-three ROABP in some order, arbitrary distinct evaluation nodes, and the balanced rational two-pair substitution. The argument is valid in every characteristic and every number of variables. It does not identify that rational family with an unweighted ordinary centered SV generator and does not settle unrestricted degrees or growing width.

## Whole-proof checks

1. I reread all of the exact P-18 fragment, including its minimal-essential-variable reduction. Its adjacent exterior-degree contraction equations justify only the stated block-truncation specializations, which is sufficient to make every prefix occupy at most two adjacent coefficient degrees. This yields the three ordered support-position intervals and at most one shared variable at each interface. P-19 invokes that reduction with its minimality hypothesis intact.
2. For two exclusive middle variables j<k, essentiality makes both partial derivatives nonzero. The ordering guarantees that their other variables belong to two disjoint extreme sets entirely before j and after k. Thus each partial has the displayed bilinear coefficient matrix. Pole extraction places it in the prime one-pair ideal; rank one would produce two nonzero linear factors, contrary to the absence of linear equations. No division by an integer is used.
3. At the cut immediately after j, the rows X_i X_j and columns X_l give the first partial's matrix literally inside the left-degree-two block. The rows X_i and columns X_k X_l give the second partial's matrix literally inside the left-degree-one block. The homogeneous coefficient matrix is block diagonal after grouping complementary degrees, so the two ranks add to at least four. Other monomials or shared boundary variables cannot cancel these fixed entries.
4. Hence at most one middle position is exclusive, and the two possible singleton overlaps imply that the full middle interval has at most three nodes. Every support triple meets that interval.
5. The cited HMM cubic characterization places the Vandermonde-rescaled nonzero coefficient tensor W in the exterior cube of the three-row Vandermonde kernel. Deleting at most three columns is injective on that kernel, since every at-most-three-column Vandermonde matrix has full column rank over every field with distinct nodes. Exterior powers preserve injective linear maps over a field. All surviving exterior coefficients are zero because every original triple meets the deleted set, contradicting injectivity.
6. I-40's denominator-cleared selector degree bounds and total amplitude degree three give exactly 20(n+1)^2 points. The stated working-field lower bound supplies n+1 selector values outside the n nodes and four amplitude nodes. Multilinear reversal preserves coefficient-cut ranks and the balanced family, giving the degree-n−3 formal result. Lowest-homogeneous-component inheritance then justifies the stated remaining degree interval [4,n−4], without a general higher-degree claim.

## Sources/dependencies

This review uses the already independently read HMM primary exterior characterization (Definition 9.5, printed p.55; Theorem 9.13, printed pp.61–62), the P-17/P-18 pole and prime-ideal statements, and the fully reread P-18 interval reduction. No additional primary source was claimed to have been opened in this check. No mathematical repair was requested.
