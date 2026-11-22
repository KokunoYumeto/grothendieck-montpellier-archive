# Root audit of A.135: four-dimensional base comparison fibre

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 19 November 2026. No priority is claimed.

## Verdict and precise scope

PASS for every displayed mathematical claim in the complete candidate `agents/singularities_duality/logs/A135_base_four_comparison_fibre_draft.tex`, read in full by the root. Before promotion we requested two wording clarifications: each collar-fixed simplex fixes one common collar; the exact fibre sequence retains connecting maps and extension data. The homotopy type of its last space alone is not a complete calculation of the middle space. The author agreed. Independent audit by the higher-comparison agent also passed.

The base B is a compact closed real PL four-manifold, allowing finite disconnected components and the empty base. PL families are jointly PL and preserve parameter projection. TOP uses the singular complex of the compact-open homeomorphism space. Let A denote base automorphisms, P bottom-fixed cylinder automorphisms with free top, and H automorphisms fixing both ends. F_A,F_P,F_H denote based homotopy fibres of their natural PL-to-TOP maps.

## Direct family checks

1. Top restriction P→A is a Kan fibration. For a horn J⊂Delta, choose a PL retraction r and a jointly PL homotopy d from r to the identity, fixed on J. Convex PL extension of the prescribed prism-boundary data gives d; no homeomorphism property is needed. Pull a given horn family back through r, call it p0, and set delta_t=a_t e(p0_t)^{-1}. Then delta is exactly the identity on J. The collar formula E_t(x,u)=(delta_{d_u(t)}(x),u) is a jointly PL homeomorphism family, with jointly PL inverse, fixes the bottom and J, and has prescribed top delta_t. Thus E_t p0_t is an exact horn lift. The same formulas are continuous in TOP. Surjectivity on vertices of A is not required.

2. In the resulting comparison square, iterated based homotopy fibres commute. This gives F_H→F_P→F_A as a homotopy-fibre sequence, without assuming a surjective strict fibration model for F_P→F_A.

3. The collar embedding sigma_s(t)=min(t+s,(t+delta)/2), for 0≤t≤delta and 0≤s≤delta/2, is strictly increasing from [0,delta] onto [s,delta], starts at the identity, is jointly PL with jointly PL inverse on its image, and satisfies sigma_s(t)≥t. Reflect at the upper end. Conjugating h by the resulting embedding and adjoining identity on the removed collars glues exactly because h fixes the boundary. The full finite-parameter formula remains PL. Every positive s produces a uniform collar, existing fixed collars remain fixed, and identity parameter faces stay exactly the identity. This proves the common-collar subcomplex has the same weak type in both categories. It is not an appeal to the singular complex of a merely pointwise union of subgroups.

## Original-source checks

We opened the original full Kirby–Siebenmann text and read Essay V pp217–218,222–225,229,240–241,251–253. We explicitly viewed the original page images for printed pp229,240,252,253 in this audit turn; p251 was previously image-checked in the A.132 source audit and rechecked in text here.

For M=B×R and closed C=M\(B×(0,1)), the dimension is five and M has no boundary. Extending a collar-fixed cylinder map by identity identifies it with a map fixed near C. Compact support converts the locally finite PL convention to the finite joint convention on the cylinder.

Essay V (1.5), p229, and its relative paragraph identify the automorphism quotient with a union of components of the sliced PL structure space. It contains the whole component of the standard structure. No assertion that all relative PL structures are isomorphic to the standard structure is used. Looping at the standard structure therefore gives F_H≃Omega S_standard.

The relative classification (3.1)–(3.2), pp240–241, applies because m=5. It identifies S with the relative tangent-lift space. Theorem5.5(I), p251, identifies TOP_5/PL_5 and its stabilization with K(Z/2,3). The universal Kirby–Siebenmann square in §5.6, pp252–253, explicitly compares BPL→BTOP with the path fibration over K(Z/2,4). The chosen standard PL lift gives a nullhomotopy, whose subtraction untwists the lift problem. Page253 explicitly states the relative version. Thus S≃Map_*(N/∂N,K(Z/2,3)), pointed by the constant map. This does not assume untwisting merely from the action on π3.

Constant-near-boundary maps and maps constant on the boundary have the same weak type by collar compression; finite parameter faces already constant on a collar can be retained using a smaller common collar. The quotient N/∂N is Sigma(B_+), including disconnected and empty cases. The structure space has one suspension shift and F_H adds one loop, giving

F_H ≃ Omega Map_*(Sigma B_+,K(Z/2,3)) ≃ Map(B,K(Z/2,1)).

The components of this mapping space are H^1(B;Z/2), its fundamental group at the constant map is H^0(B;Z/2), and its higher groups vanish. Consequently F_P→F_A is an isomorphism on πj for j≥3, and the displayed low-degree exact sequence has the correct shifts and pointed-set endpoint.

## Limits retained

This is an exact structural calculation for the fully fixed boundary and an exact fibre sequence for the free top. It is not a proof that F_A or F_P is contractible, a proof of surjectivity on original concordance components, or a calculation of the connecting maps. We do not count it as closure of original A.1(b).

For a closed three-manifold base, the same relative-all-boundary argument would have ambient dimension four and H^4(M,C;Z/2)=H^3(B;Z/2), nonzero on every nonempty closed component. The dimension-four exception on KS p240 therefore does not apply. A separate open-collar route is only a candidate and is not part of A.135.

No finite counterexample or computational topological certificate is asserted, so this proof requires source and family audits, not a fabricated finite test.
