# SF-E823 independent whole-proof audit

Reviewer: /root/imprimitive, GPT-6 Astra Pro, effort inherited/not exposed, HODGE_DIVISION, 2026-11-21. Audit completed and report timestamp corrected at 2026-11-21 18:44:22 UTC. No estimated start/end interval is claimed.

**Outcome: PASS.** Entire proof read at SHA-256 `1beaed063137d36e0e879432c5e39006fd95f32eb9a3eb24ff2b084e44696d4e`, together with its entire author certificate and the preceding unequal-slope compensation note. The new proof is valid for actual global tensor products and does not assert the same result for merely local tensor models or arbitrary gluing.

## Complete mathematical checks

1. The unit-extension input is an actual coherent sheaf, perfect on the smooth fourfold. The global Koszul calculation in the preceding note gives its resolution and full character `2exp(-D)-2exp(-3D)+exp(-4D)=1-2D^3+4D^4`. The same Koszul construction works for any actual divisor D=k theta with the asserted smooth CI; it does not require the special CM point used for the numerical example in that note. I checked the rank, vanishing first/second components, and cubic/quartic moments directly.

2. A vector bundle H is dualizable in the ordinary derived category. Coevaluation/evaluation over H defines a genuine global partial trace from Ext2(H tensor F,H tensor F) to Ext2(F,F); on id_H tensor a it is rank(H) times a. There is no need for separate equivariant structures on either tensor factor. This map is applied after ordinary vanishing, so no equivariance of the partial trace is being assumed.

3. The tensor Atiyah identity is an identity in Ext with differential-form coefficients. The two mixed factors commute in the relevant total degree because the two signs cancel. Taking the partial trace of the divided square gives exactly r A_F^2/2 + c1^B(H) A_F + ch2^B(H) id_F. In particular c1^B(H)=0 kills the entire mixed Ext term, and not merely its total trace. Adding rational B id_H is well-defined in cohomology; no fractional line bundle is postulated.

4. In the convention A=-At_BF, BF's exp(-At) is exp(A). The degree-two characteristic map on bivector plus H2(O) is contraction against A^2/2 plus the scalar class. The conjugation exp(-B) i_pi exp(B) equals the shifted contraction product; its mixed and scalar terms correspond exactly to BA and B^2/2. Thus the displayed general B-shear identity has the right direction and signs. It requires only the linear HKR identification and BF's explicit contraction diagram, not an unjustified claim that every HKR map preserves products.

5. Comparing degrees1/2 in the full normalized character gives c1^B(H)=0 and ch2^B(H)=-rq(theta_plus^2+theta_minus^2)/2. The balanced kernel pi_plus+q eta_plus annihilates the whole character, including its top component. In the partial trace its scalar contribution cancels the contraction of ch2^B(H). This leaves precisely r rho_M0(pi_plus).

6. Supplied S21 applies to the specified effective coherent finite translation/Pic0-tensor action on the product E. Its invariant evaluation lands in Ext2(E,E)^G and its forgetting diagram identifies weak semiregularity with injectivity of the ordinary trace on these invariants. Therefore a class in the full-character cap kernel has zero ordinary evaluation. This uses no action on H or M0. I reread the supplied argument around S21.6--S21.8, treating it honestly as supplied proved input rather than independently reproving the entire equivariant theory.

7. BF's ordinary evaluation/trace identity then contradicts r rho_M0(pi_plus)=0. The Hodge(1,3) component is -12k^3 eta_plus theta_minus, nonzero on the complementary two-plane decomposition. The quartic component cannot cancel it because it has a different Hodge bidegree. No assumption about local obstruction nonvanishing, simplicity, stability, or splitting enters this argument.

## Fresh primary source verification

Buchweitz--Flenner, The global decomposition theorem for Hochschild (co-)homology of singular spaces via the Atiyah--Chern character, Advances in Mathematics217(2008),243--281, DOI10.1016/j.aim.2007.06.013. Freshly downloaded author version arXiv:math/0606730v1, https://arxiv.org/pdf/math/0606730, 34pages, PDF SHA-256 `1e5fad402cbeff79b283659fd2094f3daad9c16cc430044c7dc8652502a316f5`. The manuscript is a version of the published result, not an assertion that arXiv publication alone supplies referee status.

I read the complete invoked statements/proofs: §4.2 authorp22 sign convention and definition; Theorem5.1.3 pp24--25; Proposition5.2.2 pp25--26; Corollary5.2.3 p27; Proposition6.2.1 pp29--30; Proposition6.3.1 and Corollary6.3.2 pp30--31; Theorem6.4.2 and full Proposition6.4.4 argument pp31--33. Their hypotheses cover complex spaces/schemes in characteristic zero and perfect complexes for traces; our smooth complex abelian variety and coherent perfect M0 satisfy these hypotheses. The new tensor partial-trace identity is proved in the manuscript and independently checked here, rather than attributed to an unread citation.

## Independent actual computation

`independent_check.py` and `independent_check.json` implement exterior monomials as sorted tuples, with interleaved holomorphic/antiholomorphic generators. This differs from the author's bit-mask ordering and imports no author code. It checks the complete resolution character, full compensating hull character, both balanced cap kernels, both partial-trace scalar cancellations, both nonzero cubic obstruction classes and their Hodge bidegrees. A distinct exact non-diagonal integral B matrix is used for all256basis elements and both bivectors, totaling512B-shear checks. All passed in0.203seconds.

These finite calculations certify the displayed exterior arithmetic; they do not compute Ext groups or replace the derived argument, the general-B proof, or the finite-action input.

## Minor wording precision sent to author

The sentence 'identity of rational cohomological classes' should read 'complex cohomological identity with rational B': the selected RM-eigenplane bivector and H2(O) class need not themselves be rational. This does not affect the argument or the PASS status. No author's file was silently modified.
