# Exact negative-K obstruction for an actual fixed-parameter family

Research auxiliary, 19 November 2026, `/root/frobenius`. This is unregistered and is not a main-gate movement claim. The full proof is in `C3_fixed_family_negative_K.tex`.

## Result and scope

Let R be a noetherian local k-algebra of characteristic p, with k algebraically closed and equal to its residue field. Let Z be a regular proper modification which is an isomorphism off the closed point, and let E be its reduced exceptional fibre. For a fixed smooth proper k-scheme P, we prove

$$
\operatorname{coker}\bigl(K_0(Z\times P)[1/p]\to K_0(E\times P)[1/p]\bigr)
\simeq K_{-1}(\operatorname{Spec}R\times P)[1/p].
$$

The intended parameter is a smooth proper connected curve. The proof works for the more general smooth proper P stated above. It uses an actual fixed product. It uses no inverse limit, no uniform bound on denominators across all thickenings, and no assertion that compatible virtual classes admit compatible bounded-rank representatives. It keeps the nonlocal term K0(SpecR×P) rather than replacing it with Z.

KST supplies the exact pro-sequence for the base-changed abstract blow-up. GH makes each nilpotent thickening levelwise equivalent after inverting p. Every term is then a constant pro-group, so ordinary exactness follows. The negative groups of the two regular terms vanish. Finally, classes pulled back from P already lift through Z×P.

## Candidate coefficient and exact remaining question

The separate tetrahedral regular resolution has now been proved in `C3_tetrahedral_resolution.tex` (TG.1–TG.5), with full independent root and peer audits. This supersedes the earlier geometry gate recorded here. Its proposed coefficient is a product of a dual-complex class kappa of degree −2 and a field symbol u in K2(k). For a proper-curve representative xi of the difference u−0, the exact family obstruction is xi times the boundary of kappa in K−1(SpecR×P). The fact that the boundary on degree −2 is an isomorphism does not imply injectivity or vanishing after multiplication by xi. No faithfulness statement for this module action has been proved.

We have read the complete current `../real_weil/SEMIPURITY_TOP_RESEARCH.md`, including its conditional coherent vanishing calculation and the newly opened Dayton–Weibel affine tetrahedron result. Neither replaces the actual fixed-product obstruction above. The multiplication map for an actual proper-parameter family remains an outstanding requirement; the separate regular small-resolution geometry is now established.

## Fresh primary-source ledger

1. Kerz, M., Strunk, F., & Tamme, G. (2018). Algebraic K-theory and descent for blow-ups. *Inventiones Mathematicae, 211*(2), 523–577. https://doi.org/10.1007/s00222-017-0752-2 . The full 48-page arXiv v4 author PDF was freshly opened and the complete Theorem A and equivalent sequence (1.6), author pp.2–3, were read at <https://arxiv.org/pdf/1611.08466>. Exact retrievals `turn240243461view0` and `turn867321640view1`. The theorem applies to all noetherian abstract blow-up squares. Existing canonical key: `rootKerzStrunkTamme2018`.
2. Geisser, T., & Hesselholt, L. (2011). On relative and bi-relative algebraic K-theory of rings of finite characteristic. *Journal of the American Mathematical Society, 24*(1), 29–49. https://doi.org/10.1090/S0894-0347-2010-00682-0 . The full primary PDF was freshly opened; Theorem A, printed p.29, and its proof, printed p.39, were read at <https://math.mit.edu/~larsh/papers/025/bounded.pdf>. Exact fresh retrieval `turn181022468view2`. It treats every integer degree in nonconnective K-theory, with p nilpotent in the ring, and states bounded exponent degree by degree. Existing canonical key: `rootGeisserHesselholt2011`.
3. Thomason, R. W., & Trobaugh, T. (1990). Higher algebraic K-theory of schemes and of derived categories. In *The Grothendieck Festschrift, Vol. III* (pp.247–435). Birkhäuser. The full 189-page primary scan was freshly opened at <https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Thomason-Trobaugh.pdf>. We read Theorem8.1 and its full proof, p.367; Proposition6.8(b) and its full proof, pp.362–363; and Section6.5, pp.360–361, for the nonconnective module structure. Exact retrievals `turn879630279view0` and `turn867321640view0`. Existing canonical key: `D_ThomasonTrobaugh1990`.

These three canonical bibliography entries already exist; no duplicate entries are introduced. The categorical constant-pro-group reduction is proved explicitly in the auxiliary, not attributed to a nonexistent numbered lemma. No fresh full proof of KST or GH is claimed.

## Independent check and current assessment

At 15:52 UTC `/root/real_weil` independently confirmed the entire levelwise-localization/constant-pro-group derivation and its exact product obstruction. This receipt concerns the argument as communicated before the final typed file; a full typed-file check is requested separately. The top rational quotient and rational high-range restriction questions remain unresolved in this note.


## Drinfeld pointwise refinement, freshly verified 16:13 UTC

We freshly opened the full primary arXiv v4 (11 October 2004), read Theorem 3.7, Remark (ii), and the complete proof on author p.8, and inspected a screenshot of that page: Vladimir Drinfeld, *Infinite-dimensional vector bundles in algebraic geometry (an introduction)*, <https://arxiv.org/pdf/math/0309155>. Exact retrievals `turn540010757view0`, `turn444353601view0`, and page image `turn322515313view0`. The theorem says that K−1 vanishes Nisnevich-locally; Remark (ii) explicitly gives its equivalent vanishing on commutative henselian local rings. The Calkin-category proof constructs a genuine idempotent after the henselian factorization of a monic polynomial. This is an actual primary proof read, not merely a citation to the preceding Weibel textbook pointer (Chapter III, Example 4.4.3, chapter p.32). New canonical key: `frDrinfeld2004Tate`.

Consequently, for henselian R the point-parameter specialization of FF.1 is surjective. It is also injective: in the same exact sequence, K0(R)→K0(k) is the rank isomorphism Z→Z, and the diagonal graph in K0(Z)⊕Z meets K0(Z)⊕0 trivially. Thus **K0(Z)[1/p]→K0(E)[1/p] is an isomorphism** (new FF.4). This removes the individual coefficient-lifting gate for the strict-local tetrahedral example. It does not remove the proper-family gate: R×P is not henselian local, and its K−1 remains the exact obstruction. We have not proved any ordinary Chow conclusion.

This addition was written before the 16:16 checkpoint freeze. The previous clean combined wrapper build predates FF.4; its successful build record is not claimed to validate the new citation or layout. The addition has been communicated to root and real_weil for independent review.
# Post-checkpoint18 build and endpoint update

The combined FF/TG wrapper was rebuilt after addition of FF.4. The retained builder records start 16:26:34.076963 UTC, finish 16:26:38.218528 UTC, runtime 4.141480605 seconds, five successful command passes, five pages, and 160238 PDF bytes. The log has one underfull box (badness 3039), with no overfull box or undefined-reference warning. Exact output is `output/tetrahedral_auxiliary_build.json`; the earlier build record is retained as history rather than overwritten in prose. This is a build of the auxiliary statements, not a new main-gate certification.

The separate endpoint proof and its independent audit are now retained at `../real_weil/C3_endpoint_family_lifting_draft.tex` and `C3_endpoint_family_lifting_independent_REVIEW.md`. The distinction remains: endpoint equivalence can be obtained without showing that a prescribed whole family class lies in the image in FF.1.



## Dated scope update after C.3bu — 2026-11-19T19:45:30.500069+00:00

The complete whole-proper-family theorem `C3_whole_proper_top_family.tex`, WP.1–WP.8, has passed root and both peer mathematical audits. Under the **additional geometric hypotheses of C.3bn**, for exceptional dimension d≤2 and a **fixed smooth proper curve** P, it proves full rational K0 restriction surjectivity and therefore K_(-1)(Spec R×P)_Q=0 by FF.1. The previous retention of that obstruction is superseded in precisely this scope. The earlier calculations and failed coefficient-faithfulness approach remain as dated research history.

FF's general exact Z[1/p] formula is unchanged. The new conclusion is rational; it does not assert general Z[1/p] vanishing, a higher-dimensional proper-parameter result, an affine-family compactification, or locality after adjoining k(u). In particular, the retained nonzero affine two-dimensional-parameter example remains outside the theorem. The component Albanese-kernel quotient UK.7 is still the main gate, and this auxiliary strengthening is not counted as main movement.
