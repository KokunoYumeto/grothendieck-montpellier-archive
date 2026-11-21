# Independent whole-proof audit of R-11

Reviewer: `/root/sdp_orbits`, GPT-6 Astra Pro; inherited effort is not separately exposed. Run: `BR_PENCIL-20261121-R1/sdp_orbits`.

## Outcome

**PASS in characteristic zero.** I read the whole actual `work/root/uniform7.tex`, all of `work/root/verify_uniform7.py`, and both imported helper routines `detmod` and `koszul_minor` in `work/root/verify_det7_global.py`. I then actually ran `python work/root/verify_uniform7.py`. The replay passed in 12.173 seconds, verifying 34 support graphs, 1,027 support-exact seven-subset orbits, 18,501 support-exact subsets, and 4,996 nonzero modular minors. For each family, 1,019 orbits use first-factor Koszul minors and eight use support-factor Koszul minors.

The verifier source at this replay has SHA256 `a460ccf256b539ed43931b897872719998b9a89ba008f5cb39457dc361d96ee9`.

The already separately audited size-four dependencies R-08 and R-10, together with P-01, R-01, R-07 and the anchored upper construction P-06, imply exactly the stated conclusion:

\[
\mu_7(U_{n,2})=14,\qquad \mu_8(U_{n,2})=15,\qquad
\mu_9(U_{n,2})=16
\]

for both polynomial families and every \(n\ge4\) in characteristic zero. Hence the degree-two residual method gives full-tensor border-rank lower bound \(\binom n2^2+7\). The statement appropriately does not claim this is the strongest known bound for general \(n\).

## Complete support-graph reduction

A coordinate residual is specified by seven distinct rectangles. Its matrix-entry support gives a bipartite graph. The support flattening has rank exactly the number of used variables: for each used variable, choose an occurrence in one rectangle. The corresponding row indexed by that rectangle and the opposite variable has exactly one nonzero entry, equal to \(\pm1\), and different variables choose different rows. Thus fourteen or more edges immediately suffice.

If the support has at most thirteen edges, every appearing vertex has degree at least two because each used edge belongs to a selected rectangle. Both part sizes are therefore at most six. Graphs with at most four vertices in each part reduce by split coordinate inclusion/projection to the already proved size-four case. Transposition moves every remaining graph to part sizes \(r\ge c\), with \(r\in\{5,6\}\) and \(2\le c\le r\).

The enumerator lists every nondecreasing multiset of \(r\) row-neighbour masks. The row-mask upper-degree bound \(13-2(r-1)\) loses no graph, since every other row has degree at least two. Column degrees, total edge count, existence of seven rectangles, and membership of every edge in some rectangle are necessary conditions. Canonicalization by every column permutation, together with sorting the row masks, identifies precisely row/column relabellings. The enumerator can retain superfluous graphs that have no support-exact seven-subset, which would only make the cover larger.

The verified table matches the manuscript exactly:

| Part sizes | Graphs | Seven-subset orbits |
|---|---:|---:|
| (5,2) | 1 | 4 |
| (5,3) | 6 | 853 |
| (5,4) | 19 | 116 |
| (5,5) | 1 | 6 |
| (6,2) | 1 | 20 |
| (6,3) | 5 | 27 |
| (6,4) | 1 | 1 |
| Total | 34 | 1,027 |

There are no retained (6,5) or (6,6) graphs. Square graphs need not be further identified by transposition; any resulting extra representatives are harmless.

## Automorphisms and exhaustive subset coverage

For each graph, the verifier enumerates every row and column permutation. Its condition `rows[rho[i]] == moved[i]` is exactly preservation of the graph under \((i,j)\mapsto(\rho(i),\gamma(j))\). It then records the induced permutation of the complete rectangle list. Passing to a set of induced permutations correctly removes any kernel in the action.

For each listed seven-subset, the verifier checks that its edge union is the whole graph, reconstructs its complete orbit, checks its recorded orbit size, and checks disjointness from all previously listed orbits. A separate full loop over all seven-subsets checks membership for every subset whose union is the graph. Consequently there is no assumption that a selected subset is generic, Borel fixed, or stable under any larger group. Determinant signs introduced by row/column relabelling are absorbed by the corresponding first-factor basis changes.

## Koszul matrices and arithmetic

The tensor reconstruction gives the four ordered coefficients of each rectangle, with sign -1 for its crossed determinant terms and +1 for permanent terms. The imported entry routine computes exterior insertion signs directly from ordered index subsets.

For an A-Koszul map the exterior factor has dimension seven, and the pure-tensor cost is \(\binom6p\). For a support-factor map the exterior factor has dimension \(m\), and the cost is \(\binom{m-1}p\). Every certified rank exceeds thirteen times the appropriate cost, so the ceiling bound is at least fourteen. Dimensions and all row/column ranges are checked. Distinct indices in each minor and the recorded nonzero residue are checked.

For support-factor maps the numerical weights obey the coefficient identity `vw[u] + vw[v] == aw[h]` for every nonzero tensor entry. Hence every nonzero matrix entry joins equal numerical weights. Distinct listed weights, together with disjoint rows and columns, give genuinely independent matrix blocks whose ranks add. This rank-additivity argument does not require numerical weights to be an injective encoding of every possible torus character; equality for every nonzero entry is already sufficient.

Seven exceptional orbits have thirteen variables and exterior degree one. Their ranks are 159 or 160 for determinants and 158 or 160 for permanents, all exceeding \(13\cdot12=156\). The final orbit has twelve variables and exterior degree three; its certified ranks 2,150 and 2,147 both exceed \(13\cdot165=2,145\).

The largest individual minor has order 261. All entries initially lie in \(\{0,1,-1\}\). Modular elimination reduces each entry modulo 1,000,003 at each step; its vectorized products are bounded by \((1,000,002)^2<2^{40}\), and subtraction stays far below signed 64-bit overflow. Determinant accumulation and modular inversion use Python integers. Primality is verified by trial division. Therefore the computation is exact. A nonzero residue proves a nonzero integer minor and consequently the stated rank in characteristic zero; no unproved positive-characteristic extension is being inferred.

## Propagation and upper bounds

The seven-, eight- and nine-edge anchored curves use at most four rows and four columns and give ranks 14, 15 and 16. They embed in every larger matrix size. R-07 propagates the uniform seventh lower bound as \(\mu_j\ge j+7\), giving equality at eight and nine. Finally R-01 uses image dimension \(q=\binom n2^2\), so \(q-7+14=q+7\). All dimensions and offsets agree with the manuscript.

No mathematical gap or material limitation beyond the explicitly stated characteristic-zero scope was found.
