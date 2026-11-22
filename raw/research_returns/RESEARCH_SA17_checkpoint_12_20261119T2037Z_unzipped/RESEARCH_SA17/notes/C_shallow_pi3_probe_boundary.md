# Boundary of the first-pi Bockstein curvature probe

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), RESEARCH_SA17_FINISH/c1_mixed_s3. Research record,19November2026. This is not a promoted detector theorem and no formal gate movement is claimed.

## The proposed test and its exact finite scope

For a cubic action over A/pi³, A=Z3[zeta3], we considered the first pi-Bockstein on the residue Tate groups and the residual curvature c=(Ttilde³−1)/pi³. The tentative value was the difference, modulo3, between the q-primary composition lengths on the images of the two Bockstein maps, for q other than the zero polynomial z.

`code/C_probe_shallow_pi3_bockstein.py` computes this quantity on all fixed-transposition tangent classes for four rank-six constant baselines. There are6561 classes each for L012,+⊕L012,− and Q,+⊕Q,−, and729 each for L012,+⊕Q,+ and L012,+⊕Q,−, for a total of14,580 parameter combinations. Every candidate value is zero. Final runtime is3.791522seconds. The exact Q(zeta3) coefficient computation, F3 tangent conditions, fixed-inversion assertions, Bockstein square-zero and curvature commutation tests, and image restriction calculations are in the program; output is `logs/C_probe_shallow_pi3_bockstein.json`.

The cubic and transposition relations are first-order identities at the map epsilon→pi². The program verifies their tangent basis conditions, which imply every listed parameter combination is an actual action modulo pi³. It does not claim to have proved additivity of this new expression before using it as a candidate test. Zero values are not class-vanishing evidence.

## Why these values vanish in every full-support multiplicity

There is a direct block explanation which does not depend on the finite search. Use E,F,Y ordering for L012^r⊕Q^s and let C0,D0 be the complementary diagonal projections onto the L012 and Q copies. Thus C0+D0=I and C0D0=D0C0=0. In the integral bases used in the promoted shallow S3 proof,

    T0=I+N+pi*R modulo pi²,
    N=[[0,I,0],[0,0,0],[0,0,0]],
    R=[[0,I,−D0],[0,0,D0],[−C0,C0,0]].

The residue Tate groups are H0=E⊕Y and H1=F⊕Y. With these identifications both first pi-Bockstein matrices are

    beta0=beta1=[[0,D0],[−C0,0]].

Write an arbitrary tangent gauge representative as

    U=[[0,0,0],[0,S,A],[B,0,C]].

For T=T0+pi²U, the residual curvature is the sum of the six products obtained by permuting N,R,U. The constant coefficient terms divisible by3 do not contribute because3 is divisible by pi². Direct multiplication gives

    cbar = [[−A*C0+D0*B, A*C0−D0*B, D0*C+S*D0],
            [0,             −A*C0+D0*B,               0],
            [0,             −C0*S−C*C0,       B*D0−C0*A]].

The image of either beta is the sum of the Y coordinates on L012 copies and the chain coordinates on Q copies. In the image bases supplied by beta, the curvature restrictions are respectively

    c on im(beta0) = [[−A_LL, S_LQ],[0,B_QQ]],
    c on im(beta1) = [[−A_LL,0],[−C_QL,B_QQ]].

They have the same diagonal blocks. A block triangular endomorphism has, for each irreducible q, composition length equal to the sum of the q-primary lengths on its two diagonal factors. Consequently the two image lengths agree for every q. The proposed difference is therefore identically zero for every full-support cubic mixture, even without the S3 constraint. This is a limitation of this test, not a cancellation theorem.

## Relation to the existing modulus-three invariant

The first-Bockstein expression appears to be another description of the already used curvature-cokernel length at modulus3. On a nonzero-curvature primary Smith block, valuations0,1,2,3 of d0 give cokernel lengths0,1,2,3. Their first-Bockstein image differences are0,+1,−1,0 modulo3, respectively. A general naturality/reduction proof was not completed because this observation and the exact block vanishing above remove the hoped-for new detector. No new invariant is promoted from this route.

Independently, the regular_coherent agent proved that the analogous C2 test over a DVR with2 in(pi²) is identically zero in all ranks: the two first-pi Bocksteins agree since their differentials differ by2, and the two curvature operators are equal. Its separate exact certificate is retained in `code/C_finish_ramified_firstpi_curvature_zero.py` and the corresponding log. That result is not being extrapolated from C2 to the cubic calculation; the cubic block argument above is separate.

## Literature check

Searches for Swan rings with nilpotent coefficients and relative stable categories did not supply an applicable cancellation theorem. The opened primary Baland–Stevenson article, *Comparisons between singularity categories and relative stable categories of finite groups*, Journal of Pure and Applied Algebra223(3)(2019),948–964, DOI10.1016/j.jpaa.2018.05.008, treats self-injective zero-dimensional Gorenstein coefficient rings and regular finite-global-dimension coefficient rings in its principal comparison results. The shallow coefficient ring A⋉F3 has an embedded torsion ideal and is not covered by those hypotheses. No K0-excision or nil-invariance conclusion is inferred from the paper. Primary URL: https://doi.org/10.1016/j.jpaa.2018.05.008 ; arXiv record https://arxiv.org/abs/1601.07727 .

The mixed full-support3-torsion bound remains the positive result from this research interval. Its proof and exact identity certificate are separate and make no assertion that the possible3-torsion is nonzero or zero.
