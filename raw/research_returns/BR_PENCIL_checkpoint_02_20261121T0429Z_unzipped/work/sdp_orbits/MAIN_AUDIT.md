# Independent audit of the main pencil argument and j=5 computation

Reviewer: `/root/sdp_orbits`, GPT-6 Astra Pro; inherited effort not separately exposed; run `BR_PENCIL-20261121-R1/sdp_orbits`; date 2026-11-21.

## Files and scope actually checked

Read the whole of `work/pencil/PENCIL_PROOFS.md` (P-01 through P-06), and the whole generating program `work/root/coordinate_koszul.py`. Independently reconstructed and verified every record in `work/root/j5.json` using `audit_main_certificates.py`; its output is `main_certificate_audit.json`. The root's final manuscript was not yet assembled when this audit occurred, so this is not described as a check of a final manuscript.

## Verdict on P-01 through P-06

**PASS, no gap found.**

1. **P-01 (coordinate reduction):** the row weights and the disjoint binary row/column weight ranges give genuinely distinct integral torus characters. This remains true in positive characteristic. Reduced row echelon form supplies distinct leading weights, so normalizing each first-factor basis vector makes every tensor coordinate a polynomial in t with the claimed coordinate-plane special fiber. For t≠0 the transformation is a product of invertible maps. Closedness of the border-rank locus gives `BR(special)<=BR(original)`. Hence the arbitrary-plane minimum is at least the coordinate minimum, and the reverse inequality follows because coordinate planes are included. This establishes the exact minimum, not just a generic bound.
2. **P-02 (adjacent pair):** every identified coordinate pair belongs to different selected subsets, never to the same selected subset. Thus both restrictions remain injective on the selected rows and columns. Images of determinant/permanent basis tensors are the stated adjacent tensors, with only absorbable signs. The same applies after transposition. The construction is valid over every field and does not use polarization division.
3. **P-03 (star):** expansion of the k+1-term curve gives the displayed star plus `δt sum_i a_i⊗e_i⊗e_i`. Its lower flattening has the k+1 independent columns described. Both signs remain valid in characteristic two.
4. **P-04 and P-05 (j=2):** a quadratic minor/permanent slice is a signed matching on four coordinates and is invertible on exactly that support. Intersection of slice kernels is the complement of the support union. Two distinct rectangles overlap in at most two variables, yielding minimum six. The adjacent pair decomposes as two three-term star curves, giving the matching upper six. The two-dimensional Koszul map has matrix `[-Q2|Q1]`, cost one, and rank the support-union size. The row result is the same statement for two edges, giving minimum three. Thus the requested exact polynomial minimum is six and the substitution count is `36-2+6=40`.
5. **P-06 (anchored shapes):** the four-term finite difference cancels degree zero and one exactly. Its degree-two coefficient is `a z+z a+σ(x y+y x)`, and all higher terms have positive t degree after division by t². Grouping by the h+r+s+1 displayed residual vectors gives that many pure tensors, independent of the first-factor coefficient combinations. Every coordinate appears in a slice whose matching matrix has no kernel on its support, so the lower flattening rank is exactly h+r+s+1. No smoothability assumption is hidden in the proof.

## Independent proof of the generalized substitution inequality

This proof checks the parent's intended inequality without relying on a not-yet-written draft. Let T have a flattening image U of dimension q inside `V=H1⊗...⊗Hb`, and let `1<=j<=q`. For a j-plane W⊂V define its inclusion tensor `P_W∈k^j⊗V` using any basis of W. Its border rank is basis-independent. Over any algebraically closed field,

`BR(T) >= q-j+min_{W∈Gr(j,U)} BR(P_W)`.

**Proof.** First define `Z_{j,s}⊂Gr(j,V)` to be the set of W for which `BR(P_W)<=s`. On each standard Grassmannian chart, the canonical basis matrix gives P_W as a regular function of the chart coordinates. The Segre border-rank-at-most-s cone is closed, so its inverse image is closed on that chart. Chart transition changes the chosen basis by GL_j, which preserves border rank. These local closed sets therefore glue to a closed set Z_{j,s}.

Inside the flag variety `{(W,U'):dim W=j, dim U'=q, W⊂U'}`, impose W∈Z_{j,s}. This is closed. Projection to Gr(q,V) is proper, so its image J_{q,j,s} is closed. Its points are precisely q-planes U' containing a j-plane W with `BR(P_W)<=s`.

Let r=BR(T); flattening already gives r>=q. Select q fixed vectors in the flattening domain whose images under T are independent. Independence holds on an open neighborhood O of T. Their image spans define a regular map `f:O→Gr(q,V)` with f(T)=U.

For a rank-at-most-r tensor T'∈O, let S be the span of its residual pure atoms. Choosing a basis among those atoms gives `q<=s'=dim S<=r`, and f(T')⊂S. Let L be the span of any `s'-q+j` basis atoms. The dimension inequality gives `dim(f(T')∩L)>=j`. Choose a j-plane W in that intersection. Expanding its basis in the chosen atoms expresses P_W as a sum of at most `s'-q+j<=r-q+j` pure tensors. Hence f(T')∈J_{q,j,r-q+j}.

The preimage of J under f is closed in O and contains every rank-at-most-r tensor in O. Since T belongs to the closure of the rank-at-most-r locus, it belongs to that closed preimage. Thus U contains a j-plane W with `BR(P_W)<=r-q+j`. Rearrangement gives the inequality. QED.

This proof handles a grouping of several original factors into the flattening domain: each original pure tensor still has a pure residual atom in V. Thus the inequality applies to the `(n-b)|b` catalecticant image while bounding the original ungrouped CP border rank. It also makes the properness/Grassmannian step explicit and checks the subtraction `q-j`, with no off-by-one shift.

## Independent computation audit of j=5

The independent verifier does **not** import the generating implementation. It uses:

* BFS on the seven generators consisting of adjacent row transpositions, adjacent column transpositions, and matrix transposition;
* an independently reconstructed matrix for every slice and exterior-power map;
* direct modular determinants of the listed square pivot submatrices, with an unnormalized-pivot elimination algorithm;
* exact trial division to certify that 1,000,003 is prime.

Results:

| Check | Verified value |
|---|---:|
| Distinct five-subsets covered | 376,992 = C(36,5) |
| Disjoint group orbits | 454 |
| Nonzero pivot minors independently verified | 1,816 |
| Minimum determinant certificate | 11 |
| Minimum permanent certificate | 10 |

Every record's orbit cardinality, support set, matrix shape, pivot-row and pivot-column uniqueness, minor determinant residue, atom cost, ceiling and final lower bound agreed. The union cardinality equals the total number of five-subsets, and the orbits were explicitly checked pairwise disjoint, so coverage is exhaustive. Row/column permutations and transposition send minors/permanents to minors/permanents; possible determinant signs are absorbed by the first factor. Hence quotienting by that group preserves border rank.

For an order-three tensor with first-factor dimension j, a rank-one tensor's p-Koszul map has rank `C(j-1,p)`: the wedge map by a nonzero vector has that rank, while the residual matrix factor has rank one. Therefore each stored nonzero r×r minor certifies `BR>=ceil(r/C(j-1,p))`. Matrix entries are integers. A nonzero determinant modulo the stated prime proves the corresponding integer determinant is nonzero over Q and hence over every characteristic-zero field. It also proves nonvanishing in characteristic 1,000,003. It does **not** by itself establish the same lower bound in every other characteristic. The generating NumPy int64 arithmetic is safe here: all multiplicands are reduced modulo the prime, and products are below approximately 10^12, far below 2^63.

The determinant minimum is attained by `[0,1,2,6,7]`: this is an anchored five-edge shape with h=5,r=2,s=3, whose border rank is 11 by P-06. Together with P-01 and the uniform certificates, this proves the exact minimum 11 in characteristic zero. Substitution gives

`BR(det4)>=36-5+11=42`.

For the permanent, the unique minimum-certificate orbit is `[0,1,3,6,7]`, with support nine, p=1 rank40 and cost4, p=2 rank60 and cost6, both yielding10. A certificate minimum of10 is only a lower bound on the true border-rank minimum; no matching upper10 is established by this computation. The anchored upper11 still applies, so the precise gate is `10<=minimum<=11`, unless another proof resolves it. Do not report an exact permanent minimum10 from these matrix ranks alone.

## Optional permanent-exception structure

Write the 3×3 variables as `(a,b,c;d,e,f;g,h,i)`. The exceptional permanent orbit has quadrics

`ae+bd`, `af+cd`, `bf+ce`, `ah+bg`, `ai+cg`.

They are all bilinear between `{a,b,c}` and the six remaining coordinates, so every slice matrix has rank at most six even though their union support has dimension nine. The four anchored quadrics excluding `bf+ce` have border rank nine by P-06. An upper bound ten would require an additional degeneration beyond the anchored formula; none is claimed here.

## Additional verification of the bounds used for the permanent

The same independently implemented verifier was also executed with arguments `3` and `4`. It checked all 7,140 triples in 21 disjoint orbits and all 58,905 four-subsets in 99 disjoint orbits, including 42 and 198 nonzero minor certificates respectively. The certified minima were 8 for both families at j=3 and 9 for both at j=4. P-06 supplies matching anchored upper witnesses (three edges in a 1×3 star; four edges in a 2×2 grid). Thus the minima are exact in characteristic zero, and substitution gives 41 for each polynomial family from either j=3 or j=4. Outputs: `main_j3_audit.json`, `main_j4_audit.json`.

After drafting, the full generalized-substitution proof in this note was read from start to finish at 2026-11-21T03:11:41Z. All chart, properness, open-neighborhood and atom-span steps were checked; no gap was found. This is a mathematical proof check, not theorem-prover formalization.

## Propagation in the retained dimension (supersedes the j=6 experiment)

For a fixed residual space U, define `m_j(U)=min_{W∈Gr(j,U)} BR(P_W)`. Applying generalized substitution to P_W itself, whose first-factor flattening image is W of dimension j, and retaining k<=j gives

`BR(P_W)>=j-k+min_{L∈Gr(k,W)}BR(P_L)>=j-k+m_k(U)`.

Minimizing over W yields `m_j(U)-j>=m_k(U)-k`. Thus `m_j(U)-j` is nondecreasing. With the now proved `m_5=11`, this gives `m_6>=12`; the complete anchored2×3 grid has h=6,r=2,s=3 and exact border rank12, so `m_6=12` for both polynomial families over every algebraically closed field. This is an independent re-proof of the parent's propagation observation; all factor dimensions and the direction of the nested minimum have been checked.

The exploratory j=6 torus-prolongation files are therefore unnecessary for this result. Their partial reduction is retained only as a record:447 possible supports for a torus-stable2-plane in the extension quotient reduced to15 by maximal-extension tests;12 further supports fail the kernel-support requirement, leaving3 equivalent large-block pairs. No completed theorem or extra bound depends on finishing that approach.
