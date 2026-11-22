# A.163 four-torus checker: independent code and mathematical audit

Completed 20 November 2026, approximately 03:18 UTC, by `/root/higher_comparison2`.

**Verdict: PASS.** The entire program `code/check_A163_four_torus.py` was read before an independent rerun. Program SHA256: `55e1fa4e0cab4fdccf866482c5e984916889ca6cec49e7b3041bd284ab7c104e`.

## Why this is the standard PL four-torus

Each factor is the oriented triangle boundary in R² with successive vertices `(0,0)`, `(1,0)`, `(0,1)`. Thus the geometric product of the four factors is embedded in R⁸ and is the standard PL product of four circles. Its 81 vertices have the grid labels used in the program.

For each product of four oriented edges, the code takes all 24 permutations of coordinate changes. In the unit-cube parameterization, each permutation gives the simplex with successive vertices `0`, `e_a1`, `e_a1+e_a2`, and so on to `(1,1,1,1)`. These are the staircase simplices of the cube. Their interiors partition the cube by the weak order of its four coordinates.

The cyclic orientation of a triangle edge, including its edge from label 2 to label 0, causes no gluing problem. On a product face, the fixed coordinates are discarded and the induced triangulation is precisely the staircase triangulation on the remaining oriented factors. This is independent of which incident product cube supplied that face. Distinct product cells meet in product faces in the embedded R⁸ model. Consequently the entire listed simplicial complex triangulates that geometric product, rather than merely having the homology of a torus.

The universal cover is the product of the four standard covers of a polygonal circle by a polygonal line, hence is PL homeomorphic to R⁴. The product CW structure has one vertex, four one-cells and six two-cells attached by the pairwise commutators. Cells of dimensions three and four do not alter the fundamental group. This proves the stated presentation is Z⁴; the program's exponent-sum check alone is not used as that proof.

## Orientation and chain checks

In the oriented unit cube, the edge-column matrix of a staircase simplex in its path order is obtained from the coordinate permutation matrix by adding preceding columns. Its determinant is therefore the sign of the coordinate permutation. The additional sign of the ordered vertex labels is exactly the conversion from that path order to the ascending-vertex convention used for the simplicial chains. Thus

`sign_of_order(axes) * sign_of_order(ordered)`

is the correct fundamental-chain coefficient. The wraparound edge already has its specified circle orientation in the cube parameterization; it requires no extra ad hoc sign.

The integer boundary matrices use alternating deletion signs in ascending vertex order. The boundary-square checks compute those actual integer composites. Each codimension-one face is incident to two facets, and the program separately verifies that the signed fundamental coefficients cancel there. These calculations are consistent with the geometric product orientation.

The binary rank routine performs exact Gaussian elimination over F₂ using the leading set bit as pivot. The chain dimensions and successive boundary ranks then give the homology dimensions by `dim C_d − rank d_d − rank d_(d+1)`.

## Independent execution and preservation

The original root output was copied to `logs/check_A163_four_torus_root.json`. The program was executed through `runpy` with captured standard output. Its generated JSON was saved at `agents/higher_comparison/logs/check_A163_four_torus_independent.json`; a `finally` block restored the original root output atomically, and byte equality was asserted.

- Checks passed: **24,473**; failed: **0**.
- f-vector: **(81, 1215, 4050, 4860, 1944)**.
- F₂ boundary ranks in degrees one through four: **(80, 1131, 2913, 1943)**.
- F₂ Betti numbers: **(1, 4, 6, 4, 1)**.
- Independent measured runtime: **0.16903232899858267 seconds**.
- Independent output SHA256: `f94a82c08c9942741eed46370a18acf5e1d535eb28355618de2bf8186a4f0eb5`.
- Root output SHA256, before and after: `e4bc32c3daea49f45fe0dd86409fa95ee9c83c8d7136dc3c99e2b749cab1e99a`.

This is a finite base certificate. It supplies no computational verification of assembly, a TOP concordance, an isotopy class, or the comparison theorem.
