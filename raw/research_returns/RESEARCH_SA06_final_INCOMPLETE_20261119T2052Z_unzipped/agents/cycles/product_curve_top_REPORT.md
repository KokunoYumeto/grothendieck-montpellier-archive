# C.3ar: rational top quotient for complex product-of-curves cones

**Status: proved in the stated restricted scope; not a main-gate reset.**

Let V be a product of smooth projective curves defined over Qbar, basechanged to C, and L an external product of very ample line bundles whose full section ring is normal and generated in degree one. For the strict local cone puncture X and its regular resolution Z, the proof gives B^d(Z)_Q=Q by degree on the exceptional divisor, and B^d(X)_Q=0.

The relative Adams-weight-d group is the direct sum of H^d(V,L^j) tensor Omega_C/Q^(d-1). Actual formal-Pic line bundles, algebraized individually, are multiplied by ordinary point-difference line bundles on the curve factors. High-degree finite maps to P1 make fibre evaluations span each needed H^1(O) tensor db. Every complex coefficient is absorbed into the actual Pic deformation parameter. Thus the argument uses finite sums of actual cycles, without assigning a complex-vector-space structure to Chow groups. Successive leading-degree elimination reaches a finite K0-detecting thickening, where the residual class vanishes.

All three independent proof/source audits passed. The proof does not algebraize arbitrary formal K0 objects, promote a pro-isomorphism to an isomorphism at a fixed level, or claim integral finiteness. The q=0 quintic-cone case is not covered by this Pic-product construction.

## Artifacts

- `product_curve_top_quotient.tex`: full proof.
- `product_curve_top_results.csv`, `product_curve_top_CHECK_EVENTS.tsv`: scoped assertion and actual checks.
- `output/C3ar_check.pdf`, `output/compile_product_curve_top.json`: fresh wrapper and exact diagnostics/runtime.
- `code/fetch_product_curve_sources.py`, `output/fetch_product_curve_sources.json`: primary source files, exact hashes and actual runtime.

No new bibliography key is required: D_Loday1992, D_CortinasHaesemeyerWeibel2009 and D_BlochEsnaultKerz2014 are reused from the independently owned source bibliography.

Registration UTC: 2026-11-19T10:42:50.421284+00:00
