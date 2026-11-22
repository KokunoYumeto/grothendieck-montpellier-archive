# Root audit of A.136: the explicit stabilization fibre model

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 19 November 2026. No priority is claimed.

## Verdict

PASS for the complete 299-line candidate `agents/singularities_duality/logs/A136_base_four_stabilization_model_draft.tex`, read in full. Before promotion we requested the cofinal-neighborhood explanation for the top-germ space. The independent auditor also requested that the tangent homotopy be described as preserving the zero section over its base homeomorphism, rather than fixing it pointwise. Both are wording/explicitness corrections, not replacements for a missing classification theorem. The independent full audit passed.

For each closed compact real PL four-manifold B, the theorem defines an actual map of based homotopy types beta_B:F_A→Map(B,K(Z/2,2)) and proves F_P≃hofib_0(beta_B). Here F_A and F_P are the entire based homotopy fibres of the natural PL-to-TOP maps on base automorphisms and free-top concordances respectively, with the joint PL family convention. Empty and finitely disconnected bases are covered. No cokernel on original concordance components is determined by this assertion.

## Compact orbit argument

We explicitly viewed original Kirby–Siebenmann Essay V printed p217. Its footnote says that every proper CAT submersion is a locally trivial bundle, so the compact case of Bundle Theorem0.1 is immediate. This permits the compact B4 argument without applying the open four-dimensional bundle theorem. A sliced structure on Delta×B is a proper PL submersion and its bundle is trivial over Delta. If one vertex is in the standard automorphism orbit, a trivialization identifies the whole simplex with that orbit. A prescribed horn is retained by correcting the trivialization with a horn in the simplicial PL automorphism group. Thus the quotient injects with image a union of structure-space components, containing the entire standard component. Based loops therefore identify F_A with Omega S_PL(B), including all components of that loop space.

The simplicial-group quotient lemma is also explicitly present immediately before KS (1.5), printed pp228–229. We do not require surjectivity onto unrelated structure components.

## Free-top product collars and mixed structures

The compression from A.135 is used on both ends. On the compressed cylinder conjugate h by c_s; on the removed bottom collar use the identity; on the removed top collar use e(h)×id. The values glue exactly. The formula remains jointly PL with jointly PL inverse for PL families, continuous for TOP families, and preserves already product collars. Each finite family has one common collar. This proves the common-product-collar subgroup has the same weak type as the ordinary bottom-fixed/free-top group.

For a varying sliced PL structure that is standard at the bottom and product at the top, compact proper-submersion triviality gives an initial mixed-structure PL isomorphism. Compress it using collars common to the source and target structures. The compression maps are PL in each structure because they are supported in its product collars. Extend by the actual boundary maps on both removed collars, then precompose with the inverse bottom map crossed with the interval. This makes the bottom exactly the identity and retains the top product. Horn differences lie in the common-collar PL subgroup and can be filled there. The quotient orbit again captures precisely a union of components containing the standard component; looping gives F_P≃Omega S_N^pc. This does not invoke the completed KS boundary classification theorem for a four-dimensional boundary.

## Strict collar square and the dimension check

We read KS Essay V §4.0–4.5, printed pp242–244, in the original text. The square (4.1) is the strict collar gluing construction, before its subsequent boundary classification. For M=B×R, C_-=B×(-infinity,0] and C_+=B×[1,infinity), the product-collared cylinder structure space is the strict pullback of S_PL(B)→T and S_-→T, where T is the top-germ structure space and S_- fixes the standard bottom germ.

The right restriction map is Kan: apply the open-manifold restriction theorem to C_- union C_+ in ambient dimension five, then take the fibre over the standard C_- germ. Disjoint neighborhoods split the germ target into its two factors. The four-dimensional boundary is not classified in this step. Since the map is Kan, this strict pullback is a homotopy pullback.

The relative open-five-dimensional classification and universal KS square give S_-≃* because C_-→M is a collared homotopy equivalence. For T, neighborhoods B×(1−epsilon,infinity) are cofinal near C_+, using compact B and each finite parameter simplex. Each is open of dimension five and deformation retracts to B. The natural classification gives Map(B,K(Z/2,3)), and restriction along smaller neighborhoods gives weak equivalences. Finite representatives of homotopy groups therefore pass to the germ colimit without a new extension assumption. The chosen standard PL lift fixes the origin.

Consequently S_N^pc is the based homotopy fibre of the product-with-line stabilization S_PL(B)→Map(B,K(Z/2,3)). Only the base structure component enters when this statement is looped.

## Map, shifts and geometric obstruction

We checked the original natural classification zigzag2.3.1 and Complement2.3.2 in KS. After fixing classifying maps, standard lifts and the stated comparison choices, beta_B is the loop of the product-with-line map followed by that natural classification. This specifies a based homotopy-class map; no preferred strict formula is claimed. Based homotopy inverses of the weak equivalences are interpreted in CW models.

Looping a homotopy fibre gives F_P≃hofib_0(beta_B), with target Omega Map(B,K3)≃Map(B,K2). Its loop is Map(B,K1), recovering A.135. Its component set is H^2(B;Z/2), so the exact component segment extends as H^1(B;Z/2)→pi0F_P→pi0F_A→H^2(B;Z/2). The image of pi0F_P is exactly the zero-obstruction subset of pi0F_A.

For a path-model element (a,gamma), where a is PL and gamma is a TOP isotopy from the identity to a, make gamma constant near the ends. Its pushed-forward PL structures form a based loop. The obstruction is the relative PL-structure class of the cylinder map (x,u)↦(gamma_u(x),u), in H^3(B×I,B×boundary I;Z/2)=H^2(B;Z/2).

We independently checked the final tangent microbundle homotopy in pair coordinates. Over the base homeomorphism (x,u)↦(gamma_u(x),u), the nearby second point (y,v) is sent to (gamma_{u+t(v−u)}(y),v). The full pair-coordinate inverse first recovers u and v, then x via gamma_u^{-1} and y via gamma_{u+t(v−u)}^{-1}. Thus each stage is a homeomorphism germ, continuous in the parameter, and preserves the diagonal over the base homeomorphism. The t=0 endpoint is the fibrewise tangent map plus the normal line; t=1 is the cylinder tangent map. Constancy near the interval ends makes the comparison relative to both boundary faces. This verifies the equality of the two relative obstruction descriptions.

## Exact remaining scope

This theorem removes an unspecified extension from the A.135 fibre-sequence description by specifying beta_B. It is a whole model for the based comparison fibre, including all its components. It does not evaluate beta_B or F_A for general B, and it does not determine TOP concordance components that have no PL representative. It does not classify compact four-dimensional PL structures by the stable KS space. Original A.1(b) remains unresolved, including higher PL-to-SA/arbitrary-definable comparison and the general base-three comparison.

There is no finite counterexample in this theorem; no finite numerical program is represented as verification of its continuous classification claims.
