# A.5 maximal-locus research, 19 November 2026

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), inherited effort configuration, agent `/root/maximal_locus`. No priority claim.

## Current scope

We read the live A5.008, A5.012–A5.014 statements and the existing proper/open conic and weighted-function Thom-route notes. The remaining original scope is unchanged: target dimension at least three and fibre dimension at least two. The recursion is separately refuted; dense open existence and rare complement are already proved.

## 19:00–19:08 UTC: product-bundle necessity test

Root proposed testing whether every actual semialgebraic product bundle admits some finite compatible ambient Thom stratification, even though properness/openness/constant fibre dimension do not suffice. We constructed and proved a counterexample in `product_without_thom.tex`. It is the graph of a continuous rational bump of height at most |b|/2 centered at z=a/b. The centre can approach any point of the special interval as the two base coordinates approach zero. Its fibre tangent at the moving centre is always diagonal, while the special fibre tangent is horizontal. Finiteness of a proposed stratification leaves an interval in one stratum and yields an unavoidable Thom violation.

The map is an exact globally trivial product over R² with compact interval fibre. It is definably proper over every real closed field, not just proper over R. The proof allows arbitrary finite compatible refinements of the target, and does not assume the central fibre is already a stratum. It therefore answers the stronger necessity question negatively. It **does not** reduce the original A.5 gate: its maximal product locus is the whole base. It is retained solely as a failed-route certificate.

The exact SymPy certificate checks ten identities and rank assertions, all passing in **0.10073910000210162 seconds**. The nonexistence of every possible finite stratification is proved mathematically, not asserted to have been exhaustively computed.

### Literature searches

We searched both engines for:

- `semialgebraic proper mapping "bifurcation set" "semialgebraic"`;
- `"local triviality" "locus" "definable" proper map`;
- `"topological triviality" "smallest" "semi-algebraic" map`;
- `"bifurcation" "maximal" "Hardt"`;
- `"semialgebraic" "local triviality locus"`;
- `"definable" "triviality locus"`;
- `"semialgebraic" "bifurcation set is semialgebraic" homeomorphism`;
- `"semialgebraic" "uniform" "small homeomorphisms"`;
- `"topologically trivial" "no Thom" stratification`;
- `"Thom" "trivial bundle" semialgebraic`;
- `"Thom stratification" "homeomorphism" "not"`.

The results mainly give sufficient generalized-critical-value loci or smooth/diffeomorphic triviality questions. They are not proofs of the exact definable-homeomorphism locus in the present scope. We did not identify the displayed rational product example in these searches; this is not a priority claim.

The original article R. Giménez Conejero, Dũng Tráng Lê and J. J. Nuño-Ballesteros, *Thom condition and monodromy*, DOI 10.1007/s13398-022-01353-y, was opened to check Definitions 2.1–2.2 (stratified submersion and the tangent-kernel condition for every incident pair). Its source is <https://link.springer.com/article/10.1007/s13398-022-01353-y>, root-readable retrieval references `turn112171504view0`, `turn460848472view0`, `turn460848472view1`. The paragraph immediately after Definition 2.2 records the familiar blowdown obstruction, not an attribution for our graph construction. The ambient map in our example is itself a linear projection, so it satisfies the ambient smoothness premise of the opened definition; the graph source is the stratified subset.

## Other route considered but not established

Circle dynamics supplies semialgebraic or restricted-analytic one-parameter families with complicated topological conjugacy relations, so a hypothetical encoding into a proper-map germ could threaten definability. We did not obtain such an encoding. Mapping tori retain isotopy rather than conjugacy, and introducing intrinsically marked rays tends either to change nearby fibre type or to require a non-Hausdorff orbit quotient. A local bundle point must have a whole neighbourhood of constant fibre type; no counterexample follows merely from a nondefinable conjugacy relation. This route is retained as an explicit failed attempt, not as evidence of falsity.

## 19:09–19:22 UTC freeze: read-only extensions and source checks

During the checkpoint freeze we observed that the product obstruction works with sphere fibres: replace the interval coordinate by the first coordinate of a point on S² and add one passive base coordinate. This gives a proper globally trivial product over R³ with closed S² fibres and a topological 5-manifold source. The central vertical plane has zero graph coordinate; along the moving-centre curve the vertical plane is the graph of the nonzero height differential. Their incompatibility persists in every finite source stratification, by choosing a full-dimensional central-fibre piece in one source stratum. No file in RESEARCH_SA20 was changed during the freeze.

We also read the original Dyer–Hamstrom, *Completely regular mappings*, Fund. Math. 45 (1958), printed pp. 114–116, from the existing OCR in `source_external/lie_theory/dyer_hamstrom_ocr/full.txt`, checking Definition 5 and Theorems 6–7 in the original-source OCR. The public original PDF is <https://matwbn.icm.edu.pl/ksiazki/fm/fm45/fm45110.pdf>. Their 0-regularity criterion and low-dimensional cell/sphere theorems suggest a possible surface-fibre extension of A5.014. They do not by themselves supply definable local trivializations over arbitrary real closed fields. A classical fine finite mesh need not exist at infinitesimal scale: an infinitesimal-radius ball cover of [0,1] over a non-Archimedean field has no ordinary finite subcover. Nor does a continuous-selection theorem automatically produce a definable family of homeomorphisms. We retain the route as unproved, and apply no unqualified general bundle theorem from the original paper.

## After freeze release: closed sphere product obstruction

We added the full closed-S²-fibre/base-R³ proof to `product_without_thom.tex`, including arbitrary finite target/source refinements and the Grassmannian limit argument over every real closed field. The height differential is nonzero away from the two poles, so a finite partition always leaves a central full-dimensional regular piece in a source stratum. We added two exact algebra checks for the sphere tangent vector and its nonzero height derivative. All **12** checks passed in **0.09074219700414687 seconds**. Root audit remains pending. This remains a failed-method result; it does not count as movement of the original A.5 gate.

## 19:33–19:37 UTC: simpler smooth polynomial product; A5.015

Root independently audited the interval and sphere graph proofs as PASS, with a separate 12-check runtime of 0.09250224501010962 seconds. While examining whether nonsmoothness of the graph source was essential, we found the simpler polynomial map `f(a,b,x,u)=(a,b,u³-bx1)` on `R²×S²×R`. The source is smooth algebraic and the cube-root formula gives an exact global product. The approaching vertical kernel is `ker(dh)⊕R∂u`, which cannot contain the central sphere tangent plane. The same finite-stratification argument applies. Root authorized promotion as A5.015, using this stronger example as the primary complete proof and retaining the graph construction as route history.

We wrote `part_A5_method.tex`, `results.csv`, `report.md`, and the source bibliography entry. The new exact checker `check_smooth_product_without_thom.py` records **12 PASS in 0.04600877300254069 seconds**. Root subsequently read the full new written proof and checker and recorded PASS. The status remains method-only with no original-row movement credit.

We reread Koike–Shiota §5 through original-article OCR and independently noticed the same rotation/sign caveat already recorded in the earlier lie_theory source audit; this is not a new source finding. We reopened Valette's original introduction and Theorem 2, likewise confirming the earlier sufficient-locus-only conclusion. A new direct fetch of Coste's author page returned HTTP 503, and searching its indexed public contents did not locate the corrected 2013 Coste–Reguiat chapter. We claim no new source closure from those repetitions.

## 19:42–19:49 UTC: coherent approximation route and original cell-like theorem

We wrote the direct mapping-cylinder criterion in `mapping_cylinder_recognition.tex`. Root read the complete proof and recorded PASS as an internal route lemma. It proves an exact equivalence for that special class between local product charts and a jointly definable continuous family of approximating homeomorphisms. It expressly does not replace a coherent family by separately existing approximants. This is not a general reduction of A.5 and receives no original-row movement credit.

The higher_comparison agent confirmed that the full Gauld 1976 deformation proof was already audited: its endpoint uses infinite concatenation/limits, and its PL-preserving slice statement does not furnish the required jointly finite-PL or jointly semialgebraic operator. We did not repeat that proof audit.

We obtained and opened the original L. C. Siebenmann, *Approximating cellular maps by homeomorphisms*, Topology 11 (1972), 271–294, DOI 10.1016/0040-9383(72)90014-6, at <https://webhomes.maths.ed.ac.uk/~v1ranick/papers/siebappr.pdf>. The full 2,831,867-byte original PDF is in `source_external/maximal_locus/siebenmann1972_approx.pdf`. Printed pp. 271–272 were visually read from rendered page images; pp. 273–274 were read in OCR of that original. Web refs: `turn276300783view0`, `turn447335663view0`–`turn447335663view2` (PDF/screenshot retrieval); the local rendered originals supply the legible page checks.

Approximation Theorem A, p. 271, is a TOP approximation statement with the listed dimension/boundary hypotheses. Its Complement, p. 272, supplies a continuous one-parameter family ending at the CE map, constructed by joining a convergent sequence of homeomorphisms using local contractibility. The following paragraph promises a nearly canonical version depending continuously on the original map elsewhere. On p. 273, the author notes that when source and target are PL manifolds of dimension at most three, the approximant can be PL, with a relative version where the map was already a PL embedding near a closed subset. These are exact source statements; neither the displayed Complement nor that low-dimensional remark asserts a jointly semialgebraic family over arbitrary real closed fields. We therefore do not infer the needed A.5 recognition theorem.

We also opened the primary article Lerario–Rizzi–Tiberio, *Quantitative approximate definable choices*, Math. Ann. 392 (2025), 1289–1319, DOI 10.1007/s00208-025-03128-3, Theorems A–B in the introduction. They bound the complexity of approximate set selections in Hausdorff distance, not homeomorphism graphs or their joint continuous selection. This does not supply the missing approximation operator. Source: <https://link.springer.com/article/10.1007/s00208-025-03128-3>, ref `turn227177659view0`. No main result is cited to either new source.
