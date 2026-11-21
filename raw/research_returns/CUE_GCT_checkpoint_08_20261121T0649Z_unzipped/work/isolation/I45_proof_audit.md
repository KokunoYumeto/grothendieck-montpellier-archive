# I-45 author proof audit before checkpoint08

Actual complete reread/rederivation recorded 2026-11-21T06:46:25.725988+00:00.
Author/check identity: GPT-6 Astra Pro; effort not exposed; agent=/root/isolation; run=CUE-GCT-20261121-I.
Standalone SHA256: `5f9b71217c165bd391e110fa647a8e165c1698a89723068f6ad1e942746e0626`.
Author outcome: **PASS**; independent whole-proof reviews are requested and pending. This file is separate from the frozen integrated manuscript/registers.

## Exact checks completed

- The coefficient of epsilon squared in the actual scalar identity at alpha+epsilon*(r1+s h(u)) is the multilinear quadratic Taylor term with coefficient H_ij, without a factorial. Its coefficients lie in the fixed center field K and do not involve the fresh selector u. Therefore its residue equations are valid even in characteristic two.
- I recomputed 1/(a_j−a_i)=h_i h_j/(h_i−h_j); using H1=0 gives the exact h-coordinate Cauchy residue, with no sign or integer division ambiguity.
- For the first nonzero row i, every earlier column is zero. All indices from i through the next reset t lie in the same permitted block. The first nonzero sigma_k has the three moment relation, and its own row gives sum rho_j v_j=rho_k v_k before k. At least three nonzero rho positions precede k; at least four if rho_k=0.
- For each such preceding position the residue is exactly S(h_j)=0. The rational function S has distinct nonzero residues, hence a nonzero numerator; its three vanishing moments bound its numerator degree by the support size minus four. Counting those roots gives support>=|J|+4 and distance>=2|J|+3.
- Outside characteristic two, every zero-sigma row between k and the next nonzero sigma_ell gives rho_j*(-sigma_k v_k)=0. Thus no hidden intermediate rho terms remain in the next-row equation. The two independent Vandermonde columns force rho_ell=0 and then rho_k=0, establishing the stated11-distance lower bound without an adjacency assumption.
- The normalized-word Hessian equals the original scalar Hessian because the cut gauges are held constant in the residual variables. Original gradient identities supply the parameter kernels before normalization. The extra Taylor equation therefore legitimately combines with the reset form, including endpoint shears.
- In the two-remaining-anchor determinant, square coefficients still force disjoint P and Q types. Endpoint row sums give each nonempty prefix-P and suffix-Q zero sum. Choosing a P before a Q when B is nonzero forces two P on each side of that Q and two Q on each side of that P, by the already derived three-neighbor rule. Thus at least eight internal coordinates are necessary. B=0 is a literal product of nonzero linear forms and survives the map.
- Rank preservation therefore extends through seven-core runs. At weights8/9, longer runs have either a weight-zero end or a determinant weight1/2 at the start, which cannot be a three-step chain. The existing canonical-anchor or affine-compound argument handles them; all rank statements remain valid in characteristic two. The scalar characteristic-two conclusion stops at weight7.
- The degree induction for n<=15/allchar or n<=17/nonchar2 uses the arbitrary-n cubic theorem, leading translation coefficients that retain width, weight n−2d in the lower half, reversal in the upper half, and lowest-component inheritance for arbitrary inputs. The existing five-parameter interpolation bound is unchanged.

No finite computation is necessary or claimed. The proof uses only the already audited I40–I44, P19 and their registered background; the new residue/count deductions are written completely in the standalone. Integrated status remains pending both independent whole-proof reviews and checkpoint release.
