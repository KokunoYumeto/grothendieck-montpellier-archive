# Independent proof audit: whole proper top-family lifting

**Verdict: mathematical PASS for WP.1–WP.8 under the retained C.3bn hypotheses. Auxiliary strengthening; no claim that the remaining component Albanese-kernel quotient vanishes.**

Credit: GPT-6 Astra (OpenAI), ChatGPT Pro mode, RESEARCH_SA06, run `/root/component_families`; effort setting not separately exposed.

## Exact read scope

Freshly read the entire `agents/frobenius/C3_whole_proper_top_family.tex` (SHA256 fe8f965fabc492f1ad3f8e7a3109d8faf854a24b447f17d18c4403a4cdf54c93) and the entire accompanying research/source ledger (SHA256 fcb19e667d8060364c37a7749faf6393ff4d485c346ba1ddbcf43d1ce9969478). Also freshly reread the complete dependency fragments `agents/real_weil/C3_all_dimension_endpoint.tex` (AE.1–AE.14) and `agents/frobenius/C3_fixed_family_negative_K.tex` (FF.1–FF.4), including their displayed proofs and scope restrictions. No fresh complete reopening of all external AE/FF source proofs is claimed in this receipt.

## Reconstructed proof checks

1. For an admissible finite F, the general d-column conormal injection into rank d+1 is full rank over F, by the finite support condition and Nakayama. Together with the finite smooth-stratum first-jet conditions it leaves a regular surface W along the entire closed fibre. The closed nonregular locus has proper image in the local base, so it cannot exist elsewhere. The expected dimension of the closed-fibre intersection makes H Cartier on W; the residual regular-sequence generator makes F Cartier on H.

2. The dimension-one H has H²(H,J^n/J^(n+1))=0 at every stage. Thus the actual line bundle O_H(−F) extends through all thickenings with no tensor power. The AE finite-jet Popescu/henselian descent preserves the specified restriction on H on the fixed W. This gives an integral, actual perfect K0 class j_*(1−[Q]). Since H is Cartier on W, the full square with T is Tor-independent, and its restriction is exactly [O_F].

3. Repeating the AE determinantal construction in total degree d+1 gives admissible finite intersections. The deeper-rank bound is d+1+i_a+2>d+1; all lower-dimensional strata are avoided. The exact perfect tensor resolutions and rational gamma dimension bound therefore generate the entire top tail by these finite perfect classes. No passage through coherent G0 or Cartan injectivity enters.

4. A line-bundle difference on an AE curve C is represented exactly by two finite Cartier zero schemes, after positive twisting. General sections avoid all associated points and the finite bad set and have transverse zeros on the smooth reduction. Their full nonreduced finite schemes are retained. The twisting line bundles are trivial on each Artinian semilocal finite scheme, by the Chinese-remainder/Nakayama argument. The resulting equality is in perfect K0(C), and its pushforwards are the admissible finite corrections just lifted.

5. The AE p-power lift for O_H(−C) gives a times [O_C] plus precisely those line-bundle differences, by successive Cartier sequences on the entire H. Correcting them proves the whole-product equality WP.6. The top-tail correction then proves WP.1 for the prescribed full class, rather than only its endpoints.

6. For d=2, pointwise FF.4 lifts ranks. The same eventual relative-Serre H² vanishing lifts a p-power of any line bundle on T, and a rational multiple of its K0 difference has the required determinant modulo Fγ². WP.1 lifts that remaining filtration term. For d=1, ranks and Fγ¹ suffice. Nilpotent invariance gives WP.7 on E×P. FF.1 identifies its cokernel with K_−1(R×P)_Q, proving WP.8 without treating the product as henselian local.

## Scope retained

The actual local base R, proper curve P and full proper product are essential throughout. The argument does not apply to the nonlocal ring R tensor_k k(u) by merely relabeling it, does not compactify arbitrary affine parameter classes and does not glue independently prescribed component families. It strengthens whole-family lifting in the resolved C.3bn setting; it does not remove the remaining C.3bt quotient. External foundations are reused at the explicit previously audited scopes.

Receipt saved: 2026-11-19T19:46:52.812893+00:00
