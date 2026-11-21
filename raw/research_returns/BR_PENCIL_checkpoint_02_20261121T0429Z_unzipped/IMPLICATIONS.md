# Implications of BR_PENCIL

Dated research state, 21 November 2026. This text describes the checked findings through R-11, including the complete characteristic-zero seven-plane proofs and the exact row cubic pencil calculation. Finding IDs refer to the paper; the published-source locators are reproduced below so that the implications remain understandable outside the paper.

## 1. What changes in the determinant and permanent calculation

The checked characteristic-zero bound is

\[
\underline R_{\mathrm{CP}}(S_{\det,4})\geq43,
\qquad
\underline R_{\mathrm{CP}}(S_{\mathrm{per},4})\geq43.
\]

Here the tensors are the coefficient tensors of the degree-four polynomials in sixteen matrix-entry variables. They are different from the four-factor row tensors in \((k^4)^{\otimes4}\). R-08 and R-10 prove the displayed inequalities in characteristic zero. R-05 separately proves the bound forty-two over every algebraically closed field for the explicit integral coefficient-tensor model of FL-01. In characteristic zero, this is the usual polynomial tensor up to a nonzero scalar. Because the CP atom variety contains the symmetric atom variety, these CP lower bounds also lower-bound symmetric border rank in characteristic zero.

The requested two-dimensional residual calculation is exact: P-04 gives minimum three in the two row families and minimum six in the two polynomial families. With flattening-image dimensions six and thirty-six at \(n=4,b=2\), substitution gives seven and forty respectively. Continuing the same question to larger retained subspaces gives the following exact polynomial minima; the residual tensor has a new first factor of dimension \(j\), while its two matrix-entry factors remain separate.

| Retained dimension \(j\) | Exact residual minimum | Resulting bound at \(n=4\) | Finding |
|---:|---:|---:|---|
| 2 | 6 | 40 | P-04 |
| 3 | 8 | 41 | R-02 |
| 4 | 9 | 41 | R-03 |
| 5 | 11 | 42 | R-05 |
| 6 | 12 | 42 | R-07 |
| 7 | 14 | 43, characteristic zero | R-08; R-10 |
| 8 | 15 | 43, characteristic zero | R-09; R-10 |
| 9 | 16 | 43, characteristic zero | R-09; R-10 |

The improvements come from evaluated residual minima, with explicit lower certificates and matching upper degenerations. The general multidimensional substitution principle is already present in Landsberg–Michałek, arXiv:1608.07486v1, Proposition 2.3, p. 3. R-01 supplies the short proper-incidence proof in the arbitrary residual-order, all-algebraically-closed-field form required here. It does not claim to originate multidimensional substitution.

P-01 turns the Grassmannian minimum into a finite coordinate minimum by an explicit torus degeneration. The Koszul costs are proved from the rank of the wedge map on a pure tensor, and the relevant determinants are recorded as integers. The exceptional permanent five-plane needs the additional limiting-span/prolongation obstruction R-04; direct Koszul ranks alone leave that case at ten. The permanent certificates use unit minors. The determinant certificates use units times powers of two, and characteristic two is covered by equality of the determinant and permanent coefficient tensors. This combination proves the all-characteristic assertion without assuming that a characteristic-zero secant ideal commutes with reduction modulo every prime.

The characteristic-zero seventh minimum requires more than the earlier Koszul tests. The determinant proof covers all 25 Borel ideals; the permanent proof checks all 8,347,680 coordinate seven-subsets through 1,517 low-support symmetry orbits, with ordinary support flattenings covering the rest. The global certificates verify 2,997 and 6,041 nonzero modular minors respectively. Named prolongation proofs settle the remaining cases, including the exact parameter arrangements in P-15 and the higher bidegree obstruction in P-19. These counts describe a reproducible finite proof, not a random or numerical search. The characteristic-zero scope of these additional arguments is retained.

R-06 shows that the minima for \(j=3,4,5\) hold for every \(n\geq4\), and R-07 propagates the sixth minimum. In particular, the degree-two residual calculation yields

\[
\underline R_{\mathrm{CP}}(S_{\det,n}),\,
\underline R_{\mathrm{CP}}(S_{\mathrm{per},n})
\geq \binom n2^2+6\qquad(n\geq4).
\]

R-11 strengthens the displayed constant six to seven in characteristic zero, for every \(n\geq4\). Its proof covers all thirty-four extra small-support graph types and all 1,027 required seven-subset orbits, with 4,996 further exact modular minors. The constant six remains the separately proved all-field consequence.

This is the consequence of this particular residual slice; it is not asserted to be the strongest available general-\(n\) lower bound. For the row permanent, P-20 proves the exact minimum \(j+1\) for every allowed \(1\leq j\leq\binom n2\), in every characteristic. The row determinant has this value in the star range \(1\leq j\leq n-1\). Increasing \(j\) in these ranges does not improve the resulting \(\binom n2+1\) bound. For arbitrary \(b>2\), P-02 gives an exact reduction of the two-dimensional minimum to one adjacent-pair tensor. P-11 evaluates the row cubic seed: permanent six in every characteristic; determinant eight outside characteristic two and six in characteristic two. P-18 gives integral upper curves and exact lower certificates for the polynomial cubic seed: permanent between twenty-one and twenty-four in every characteristic, determinant between twenty-one and twenty-seven outside characteristic three, with the permanent interval also applying in characteristic two. The exact polynomial cubic values remain open. The upper bounds prove that this particular cubic two-plane substitution cannot improve forty-three: its output is at most forty-one for the determinant and thirty-eight for the permanent. A 63-by-63 Jacobian minor of determinant minus sixteen proves the auxiliary nine-labelled-square dominance used for the determinant upper bound in every odd characteristic; characteristic two follows from the permanent curve.

P-17 reduces the determinant ten-plane question to thirty-five Borel ideals after six Koszul and eighteen Borel-flag exclusions. P-20 gives a permanent ten-plane of border rank at most eighteen, so its uniform minimum is now between seventeen and eighteen. These are current gates for a possible bound forty-four; no global forty-four conclusion is asserted.

## 2. What the literature comparison supports

The verified comparisons are Landsberg–Teitler's polynomial border lower bound thirty-six, versus Waring-rank lower bounds forty-three for \(\det_4\) and forty for \(\mathrm{per}_4\) (arXiv:0901.0487v3, Corollary 1.4, p. 2, and §9, pp. 13–14, Table 3), and Farnsworth's symmetric border lower bound thirty-eight for \(\det_4\) (arXiv:1505.05079v2, Theorem 1.6, p. 2). A Waring-rank lower bound cannot be substituted for a border-rank lower bound, and a symmetric border lower bound alone does not imply the same CP bound.

Conner–Harper–Landsberg prove polynomial \(\det_3\) CP border rank seventeen (Forum of Mathematics, Pi 11 (2023), e17, Theorem 1.2, §1.2). Conner–Huang–Landsberg prove polynomial \(\mathrm{per}_3\) CP border rank sixteen (arXiv:2009.11391v1, Theorem 1.1 and following identification, p. 3; proof in §5). Their border-apolarity methods are directly relevant to the present limiting-span obstruction, although these size-three values do not themselves evaluate the size-four residual minima.

The current row-tensor results were checked separately: Han–Ju–Kim's row determinant value twelve, Han–Ju–Kim's row permanent value eight at size four, Han–Song's ordinary row permanent rank sixteen at size five, and Han's symmetric border rank \(2^{n-1}\) for the squarefree monomial/row permanent. Their ambient definitions prevent them from being mistaken for small bounds on the \(n^2\)-variable polynomial tensors. Han–Song, arXiv:2608.09708v2, Proposition 4.1, p. 10, explicitly includes the row permanent border lower bound \(\binom{n}{\lfloor n/2\rfloor}+1\); this familiar plus-one phenomenon is not assigned historical novelty here.

The audit also checked the 2026 simultaneous border-apolarity theorem, work beyond weak border apolarity, and nonlinear Kronecker–Koszul methods. It found no competing published polynomial size-four border lower bound at least thirty-nine among the primary sources inspected. This scoped outcome is not a proof of exhaustive priority. FL-06 records a separate literal error in a survey display and provides its complete degree-two counterexample; that correction does not establish a new general rank theorem.

## 3. Consequences for geometric complexity theory and P versus NP

Forty-three is a finite-dimensional lower bound for explicit degree-four tensors. It is not a superpolynomial circuit lower bound, a determinantal-complexity separation, or a proof separating \(\mathsf P\) from \(\mathsf{NP}\). The uniform degree-two-residual consequence is polynomial in \(n\), and no reduction from a Boolean complexity separation is supplied. Nor does the argument prove that a padded permanent lies outside the relevant determinant orbit closure used in an asymptotic GCT formulation.

What the work supplies is a concrete algebraic certificate strategy: retain several dimensions of a flattening image, exploit group actions to reduce the corresponding Grassmannian problem, and exclude low secant membership through determinantal and prolongation conditions. The method keeps the actual maps, subspaces, and incidence data. It does not infer rank from dimensions or representation classes alone. This gives an exact test case for comparing GCT-style symmetry methods with border apolarity, without asserting that it overcomes the barriers discussed in predecessor GCT_GINEQ.

The calculation does not turn generic projector optimization into an efficient algorithm. A finite SDP or a finite Koszul matrix can have dimension that grows rapidly in the succinct tensor parameter. The exact small certificate and the proved hierarchy error are useful mathematical results, not by themselves complexity-theoretic algorithm bounds.

## 4. The field convention is part of the result

FL-01–FL-04 prove predecessor F-23 over every algebraically closed field using the properness mechanism of F-18 and the integral complementary-minor calculation of F-22. Ordered tensor coefficients are units, so the residual image bases survive every scalar extension. Coordinate projections isolate a chosen nonzero residual coefficient, giving the exact one-dimensional residual minimum and the recursion without norms or factorial denominators.

In characteristic dividing \(n!\), the invariant tensor/divided-power model is essential. Its ordinary symmetric quotient is \(n!\det_n\) or \(n!\mathrm{per}_n\), hence zero, although the tensor itself is nonzero. Moreover, FL-05 proves that the ordinary polynomials \(\det_n\) and \(\mathrm{per}_n\) have infinite border rank relative to the ordinary-power map \(\ell\mapsto\ell^n\) when the characteristic is \(p\leq n\): every such power has zero squarefree degree-\(n\) coefficients. The complete Veronese in divided powers has a different, meaningful finite problem. The all-field theorem must retain this distinction.

## 5. What the SDP and orbit questions establish

S-01 gives an explicit residual image outside the four families, of concise format \(2\times2\times3\), with \(\alpha(U)=3/4\). A rational Gram certificate proves exactness of the first PPT level, and product extensions prove zero error at every higher PPT Bose-symmetric level. S-02 proves the general projector-objective estimate

\[
0\leq\beta_k(U)-\alpha(U)\leq\frac{d-1}{k+d-1},
\qquad d=\dim B,
\]

from the stated Bose-symmetric-extension convention and Navascués–Owari–Plenio's separable perturbation (arXiv:0906.2731v1, Definition 1, p. 2; Theorem 2, equation (7), p. 3). This completes the requested example, while the generic computational problem of predecessor Q-30 remains distinct.

O-01 shows that the proposed product-GL orbit maximum of alpha is absent for a product-free subspace: the supremum is always one for every nonzero subspace, and it is attained exactly when the subspace contains a nonzero product tensor. O-02 identifies the actual Plücker norm-minimization condition as scalar projector marginals. It proves the minimal-vector criterion directly, and does not claim that every orbit attains such a minimum. These results sharpen predecessor F-19's warning that a Hermitian metric is extra data. They do not identify Kempf–Ness capacity with the orbit-alpha supremum. The balanced example has alpha \(2/3\), but its status as the orbit infimum is not asserted.

## 6. Exact transfer to Grothendieck's frameworks

The paper's separate dictionary gives a finding-by-finding transfer. The operative published locators are the following; PDF leaves are one-based counts in the linked facsimiles.

| Framework | Exact locator | What carries the proof |
|---|---|---|
| EGA properness | EGA II, Definition 5.4.1 and Proposition 5.4.2(i)–(iv), printed p. 100, PDF leaf 97; Theorem 5.5.3(i), p. 104, leaf 101 | Grassmann and flag incidences have closed proper images; the substitution and limiting-span arguments work in every algebraically closed fiber. |
| SGA 3 module/group schemes | Exposé I, §§4.5–4.6, including Definition 4.6.1, printed p. 29, PDF leaf 42 | Free tensor representations, split diagonal tori, root subgroups and their integral actions. |
| SGA 6 exterior powers and representation rings | Exposé V, Definition 2.1, Examples 2.2(b), Lemma 2.2.1, pp. 314–316, leaves 321–323; representation-ring example p. 317, leaf 324 | Koszul source and target bundles, exterior operations, and the representation-ring language. |
| SGA 6 gamma filtration | Exposé V, Proposition 3.2(ii), p. 325, leaf 332; §3.10, equation (3.10.1), p. 331, leaf 338 | The precise relation of lambda/gamma operations and filtration, without claiming that these classes determine a morphism's rank. |
| FGA parameter spaces | Bourbaki exposé 221, Theorems 3.1–3.2, pp. 259–260, leaves 12–13; Hilbert specialization after Proposition 3.8 and Remarks 3.9, pp. 265–266, leaves 18–19 | Hilbert/Quot parameter spaces for limiting configurations; the actual limiting span is retained when necessary. |
| EGA images | EGA I, §9.5, Propositions 9.5.1 and 9.5.4, Corollary 9.5.2, Definition 9.5.3, pp. 176–177; predecessor records leaves 175–176 | Image/closure language for explicit integral secant curves; no unjustified arbitrary-base-change claim. |

Primary facsimiles: [EGA II](https://www.numdam.org/article/PMIHES_1961__8__5_0.pdf), [FGA exposé 221](https://www.numdam.org/article/SB_1960-1961__6__249_0.pdf), [SGA 3 I](https://library.slmath.org/nonmsri/sga/sga/pdf/sga3-1.pdf), [SGA 6](https://library.slmath.org/nonmsri/sga/sga/pdf/sga6.pdf), and [EGA I](https://www.numdam.org/article/PMIHES_1960__4__5_0.pdf). The EGA II, FGA, SGA 3 and SGA 6 leaves listed above were newly rendered and viewed in this run. The EGA I locator retains the predecessor's verification provenance.

For the analytic parts, the predecessor's inspected USP *Résumé* facsimile places §1 no. 1, Definition 1 and Theorem 1 at p. 8, leaf 8, and Theorem 2 with its duality corollary at p. 8′, leaf 9; §4 no. 2, Theorems 1–2 at pp. 59–60, leaves 60–61; Corollary 1 after Theorem 3, inequality (8), at p. 61, leaf 62; and the §4 no. 3 proof opening at p. 62, leaf 63. These are analytic foundations, not a source for the norm-free border-rank theorem. Their inherited provenance is recorded rather than relabeled as a new source check.

No new étale sheaf, weight theorem, purity statement or motive is constructed. SGA 4, Exposé VII, §1.2, and Weil II, Definition 1.2.2, p. 153 (predecessor IAS PDF leaf 17), supply terminology only. Predecessor F-20 explains why source/target \(K_0\) classes do not determine the rank of a specific map; F-21 explains why a constant weight-zero stalk or an absolute point motive does not retain the embedding-sensitive tensor rank. These limitations do not exclude future embedding-sensitive sheaves or relative motives. No SGA 5 rank theorem is asserted.

The [CSG published-works catalogue](https://csg.igrothendieck.org/published-works/) identifies the published *Résumé* as CSG17 and the Hilbert-schemes exposé as CSG44. These are published-work identifiers, not unpublished-manuscript archive cotes. The [Montpellier archive](https://grothendieck.umontpellier.fr/archives-grothendieck/) was consulted; no unpublished-manuscript cote and scan establishing the modern findings was established. The archive entry for those claims is therefore **not established**, with the exact published foundations given above. The package does not fabricate a cote, a scan, or a theorem linking a categorical name to a tensor-rank conclusion.
