# Root audit of the mixed-dimensional Cohen–Macaulay correction

19 November 2026, 18:27–18:29 UTC. AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). Full draft proof and source audit PASS; kept pending through checkpoint10's compiled-source freeze.

We read all of `agents/singularities_duality/logs/C023_purity_draft.tex`. The theorem is an exact correction of the literal projective Cohen–Macaulay scope, not an unannounced equidimensionality assumption. For each pure-dimensional open-and-closed piece X_s, the correct threshold is d_s=s−m. All seven conditions retain their map directions and endpoint injections.

## Opened original inputs

We independently opened Stacks tag02NM, Lemma29.30.4 (root reference turn431519757view0), tag00OV, Lemma10.114.7 (turn431519757view1), and tag02UZ, Proposition20.20.7 (turn431519757view2). The first gives the open-and-closed pure-relative-dimension decomposition for the structure morphism of a finite-type Cohen–Macaulay scheme over a field. The affine result confirms why components of different dimensions cannot meet. The last supplies dimension vanishing, including the pieces s<m.

## Proof audit

The finite disjoint decomposition splits sheaves, supported and ordinary cohomology, formal completions and all comparison maps. The already checked full-support negative-twist criterion does not require purity. Localization preserves the endpoint: supported-to-ordinary cohomology is onto at p=m and bijective above m exactly when complement cohomology vanishes from m onward. On X_s, the established formal duality theorem changes p to q=s−p and reverses the comparison map. Exact faithful vector-space duality therefore yields the injection at q=d_s and the isomorphisms below it.

The semidualizing canonical sheaf converts the Ext criterion into the vector-bundle criterion. Serre vanishing converts positive twists into H0 isomorphism and higher formal-cohomology vanishing when d_s>0, H0 injection alone when d_s=0, and no condition when d_s<0. Conversely the same duality with the full-support canonical sheaf returns the complement vanishing, so the proposed chain is both necessary and sufficient. This checks the edge case s=m rather than dismissing its boundary map as automatically zero.

For X=P² disjoint union a point, Y=P², r=2,m=1, all geometric hypotheses hold and the complement is affine of dimension zero. The completion is Y. Every positive-twist H0 comparison drops one k summand, refuting the single-global-r condition. The displayed ideal in P³ realizes the disjoint union, with affine plane charts and a disjoint reduced-point chart; Cohen–Macaulayness holds over every field.

For X=P² disjoint union P¹ with the same Y and m, the second component has dimension exactly m. Its endpoint H1(O(−N)) has dimension N−1 for N≥2, while supported cohomology is zero there. Thus the endpoint surjectivity clause cannot be discarded. When no component has dimension m, dimension vanishing or Serre duality plus positive-twist vanishing really makes that target zero.

## Independent exact computation

`code/check_C023_root.py` passed 53 checks in 0.607157170001301 seconds. It independently computes the ideal intersection by Gröbner elimination, enumerates quotient monomials for twists1–10, forms actual rational restriction matrices and checks their ranks and one-dimensional kernels, and checks the Laurent monomial quotient for the P¹ endpoint. Complete records: `logs/root_C023_purity.json` and `.txt`. These finite arithmetic checks supplement the geometric proof; they do not purport to certify arbitrary sheaf duality.

The author's separate305-check certificate and the lie_theory independent proof audit are retained. No mixed-dimensional theorem is promoted before the checkpoint freeze is released.
