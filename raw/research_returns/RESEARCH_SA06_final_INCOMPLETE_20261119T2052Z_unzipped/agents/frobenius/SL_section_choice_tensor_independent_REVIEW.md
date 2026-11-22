# Independent review of the displayed section-choice tensor criterion

**Complete mathematical PASS at the fixed-data, displayed-leading-coefficient scope. No main-gate movement and no universal actual-node identification.**

Reviewer: GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode, `/root/frobenius_continuation`; effort not separately exposed.

I read every section SC.1–SC.6, the full proof, the normalization statement and source/limitation ledger in `agents/cycles/notes/SL_section_choice_tensor_criterion_2024.md`. Reviewed SHA256: **97c6ff5c48c4ff1cb7c88238eb0cf340907021c8f19622288f92f13fea2368af**.

The divisor sequence with support avoiding a0,a1 is exact: every line bundle has a rational representative avoiding those two points, and a trivial such divisor is the divisor of a rational function invertible there. Tensoring with Q preserves exactness. Selecting a basis from the given w_q correctly reduces the tensor equation to finitely many rational divisor classes. Clearing denominators and then the finite torsion classes gives one common m, after which the actual functions f_j have the required divisors. Scaling each at a0 preserves the divisor and ensures the normalized value1. All remain nonzero at a1. Subtracting only along the selected basis incidences cancels the entire weighted divisor coefficient at every point. Conversely, taking Picard classes proves necessity. Thus SC.3 is exact with the stated tensor-power allowance; no fractional line bundle is substituted for an actual family.

The h0 observation is also exact: its prescribed zero support is chosen after the n_qx, so changing h0 alone cannot change the displayed coefficient vectors. The norm formula in SC.4 includes the multiplicities of finite pullback. Smoothness of the curves gives finite flatness, including for inseparable maps, and rational norm pull-push proves injection on the tensor. This concerns fixed coefficient space and fixed presentation, exactly as stated.

## Explicit check of SC.5

Retain the support W supplied by HK, which avoids every triple point. Its supported coherent descent is the two-column fibre sequence

    K(E on W) → direct sum_i K(E_i on W_i)
                   → direct sum_e K(C_e on W_e).

For a selected supporting A_i, the perfect class [O_A_i] in its regular component has edge restrictions exactly its transverse point classes, with incidence signs. The vertex supports are empty, so each point class has the canonical coherent map used to define w_q. Their sum is the actual image of [O_A_i] in this supported two-column sequence. Its connecting boundary is zero by exactness. Forgetting support proves sum_(q on A_i) w_q=0 in K_{−1}(E), with precisely those canonical coherent choices. Thus a simultaneous normalization twist by a parameter line M changes Omega by this zero sum tensor [M]. No claim about arbitrary unsupported choices is needed. The same calculation treats the stated component-divisor times parameter-line correction.

The note correctly separates this proved fixed-data criterion from the still-unproved identification of all coherent HK lifts with the displayed SL.3 coefficients. Its final motivic expression is a description of the unresolved route and is not used as a proved orthogonality theorem in SC.1–SC.5. No inference from nonzero Omega to survival of the ordinary main quotient is made. I reuse the prior complete VE/HK/PL support and divisor audits; no fresh external source read beyond those audits is claimed here.

Saved: 2026-11-19T20:26:57.707538+00:00.
