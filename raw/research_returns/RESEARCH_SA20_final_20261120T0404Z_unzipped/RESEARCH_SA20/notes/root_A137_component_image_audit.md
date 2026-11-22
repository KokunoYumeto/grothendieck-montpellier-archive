# Root audit of A.137: the complete base-four component-image criterion

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 19 November 2026. We claim no priority.

## Verdict and scope

PASS after reading the complete updated candidate `agents/singularities_duality/logs/A137_base_four_component_image_draft.tex`. The independent audit is `agents/higher_comparison/A137_independent_audit.md`. Both requested explicitness additions are present: independence from an arbitrary lift of an endpoint isotopy, and common-collar normalization of the fixed-endpoint family Q_s.

For a closed compact real PL four-manifold B, let I_B be the subgroup of ordinary TOP concordance components whose top restriction is TOP-isotopic to a PL automorphism. Let J_B be the actual image of pi_0 beta_B in H^2(B;Z/2), with beta_B specified in A.136. The theorem defines a homomorphism lambda_B:I_B→H^2(B;Z/2)/J_B and proves that its kernel is precisely the image of the PL concordance component group. It does not assert surjectivity of lambda_B or evaluate either the endpoint predicate or J_B. The quotient of I_B by the PL image is consequently a finite elementary abelian two-group of order at most 2^b_2. Empty and disconnected bases are covered.

## Relative class and exact zero test

For a bottom-fixed TOP concordance whose top map is literally PL, the common-product-collar normalization from A.136 makes its pushforward PL structure equal to the standard structure near both boundary components. The relative open-five-dimensional structure classification used in A.135 therefore defines its difference class kappa in H^3(B×I,B×boundary I;Z/2). The original Kirby–Siebenmann inputs were already read and visually checked in this run: Essay V relative (1.5), p229; relative classification (3.2), pp240–241; and the universal KS square with chosen-lift interpretation, pp252–253. The entire four-dimensional boundary is prescribed in this application.

The zero test is stronger than an unspecified PL isomorphism. If kappa vanishes, a path of relative structures from the standard structure to F_*alpha lifts through the actual relative automorphism orbit map, beginning at the identity. Its endpoint g satisfies g_*alpha=F_*alpha and is connected to the identity by TOP maps fixed near the boundary. Thus g^{-1}F is PL, and the lifted path gives a TOP isotopy from F to g^{-1}F with both boundary maps fixed. The converse follows by pushing the standard structure along such an isotopy. No four-dimensional smoothing or stable-boundary sufficiency statement is used.

## Additivity

Differences of relative PL lifts give the natural affine cocycle

    kappa(FG)=kappa(F)+F_*kappa(G).

The action is trivial here. Bottom-fixedness implies that the top map a is homotopic to the identity by pr_B F(x,t). The cohomology restriction H^j(B×I)→H^j(B×boundary I) is the injective diagonal. The connecting map identifies the relative H^3 with the cokernel of H^2(B)→H^2(B)⊕H^2(B). Both boundary actions are identity, so naturality gives identity on that cokernel. This proves ordinary additivity of kappa on the group of maps with PL top. The argument also works for a finite disconnected B, because bottom-fixedness preserves its cylinder components.

## Endpoint correction and its exact ambiguity

For a TOP isotopy gamma from f=e(h) to a PL a, the displayed correction

    E_{gamma,s}(x,t)=(gamma_{st} f^{-1}(x),t)

is a continuous bottom-fixed isotopy from the identity, and E_{gamma,1}h has top a. Its slice inverse is explicit. Paths are first made constant near their endpoints; common-collar normalization handles the full families when required.

For another endpoint path eta, cancellation gives h_eta h_gamma^{-1}(x,t)=(eta_t gamma_t^{-1}(x),t). This is exactly the trace of a TOP path from the identity to a PL map. A.136 identifies its kappa class with an element of J_B. Conversely every member of J_B is represented by such a trace, and each trace is in the identity component of the free-top concordance group, through (x,t)↦(delta_{st}(x),t). Thus J_B is the exact ambiguity, not merely a subgroup containing it. It is a subgroup because beta_B is a loop map under the specified based homotopy-type equivalence.

Two arbitrary lifts of one endpoint path beginning at the identity differ by a path fixed at both ends and beginning at the identity. Their final composites with h therefore have the same relative class. This validates the statement's freedom to choose a lift, even though the proof supplies a canonical formula.

## Invariance on genuine ordinary concordance components

For any ordinary TOP path H_s between maps F_0,F_1 with PL top, put a=e(F_0), f_s=e(H_s), T_s(x,t)=(f_{st}a^{-1}(x),t), and Q_s=T_s^{-1}H_s. The top of Q_s is exactly a for every s, while its bottom remains the identity. Common-collar normalization gives a path of relative PL structures, so kappa(Q_s) is constant. The final T_1 is a trace of a path from the identity to the PL map e(F_1)a^{-1}. Additivity shows kappa(F_1)−kappa(F_0) lies in J_B. This proves that the quotient class is invariant on the original ordinary TOP components; no block-concordance substitution occurs.

## Exact kernel and finite quotient

I_B is a subgroup as an inverse image under endpoint evaluation. Representatives of its elements can all be chosen with literally PL top. Their product has PL top, and kappa additivity proves the homomorphism property. A PL concordance has class zero. Conversely a zero quotient class can be cancelled by postcomposing with a trace representing its opposite member of J_B. That correction stays in the same free-top component, and the resulting zero relative class gives a boundary-fixed isotopy to PL by the zero test. The kernel is therefore exactly the PL image.

The first isomorphism theorem embeds I_B/im(pi_0 c_P) into H^2(B;Z/2)/J_B. Finite triangulability of compact B gives finite-dimensional mod-two cohomology. No realization of every cohomology coset is needed or asserted. For H^2(B;Z/2)=0, only the endpoint predicate remains.

## Remaining original task

This is a complete criterion for the image of the PL-to-TOP map on ordinary concordance components in base dimension four. The endpoint-image predicate, the actual stabilization image J_B, the image of lambda_B, and the rest of the whole-space calculation remain unevaluated in general. A.1(b) is not completed. There is no finite counterexample here and no finite computation is represented as a proof of the continuous structure-space assertions. Any qualifying reduction is assessed only at the scheduled hourly review.
