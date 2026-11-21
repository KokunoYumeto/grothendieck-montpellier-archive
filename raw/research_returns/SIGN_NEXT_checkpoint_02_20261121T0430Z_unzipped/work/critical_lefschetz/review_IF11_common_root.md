# Independent review: IF-11 and the common root addition to IF-09

Reviewer: GPT-6 Astra Pro, effort not exposed, /root/critical_lefschetz.
Date: 2026-11-21. This review records complete human proof reads and independent mathematical derivations; no Lean compilation is claimed.

## Common Lefschetz action for the fixed coordinate-exponential chain

**Verdict: approved.** I read the complete new paragraph beginning “A compatible common Lefschetz action on this fixed family,” its proof and scope qualifications, together with the preceding fixed exponential-chain proof and following same-fixed-L obstruction. Checked kernel_intertwiner.tex SHA256: 3ceb6ea17a76f4174d0f0b2c7d539cc4d087f42f7c35a66bdec794b452fbec52.

For a fixed simple root inside the original eight rows, a full determinant vector is killed by both root operators, while each rectangular coordinate inclusion is the identity on the root's two coordinates. Hence both determinant insertion and inclusion commute with both root operators on the whole cyclic coefficient module. Their ambient maps send orthonormal tensor-basis vectors to distinct orthonormal tensor-basis vectors, so the earlier isometry and primitive-image claims apply to these whole modules, not just a root string.

The particle-hole embedding proved in IF-04 identifies this fixed root pair with the exterior Lefschetz raising and lowering on a primitive sublattice. If its ambient number of symplectic pairs is \(N_j\), adjoining one singleton \(e\) in each extra pair is an integral isometry, a coordinate direct-summand embedding, and a vector killed by both local raising and lowering. Tensoring these singletons therefore embeds every stage in one common \(V_N\), preserving both operators. Saturation composes: a primitive cyclic sublattice in its tensor ambient remains primitive in the padded exterior lattice. The common degree formula is \(N-h\), since the unpadded formula is \(N_j-h\) and padding adds \(N-N_j\). Thus the transported arrows have degree zero, as claimed.

The maximum \((r_j-1)q_j\) is \(39\cdot143=5577\) per embedding and \(44616\) for eight factors. Tensor-product exterior identification preserves the integral norm, primitivity, and diagonal root pair. The matrix identities \(E_i'B=BE_i\), \(F_i'B=BF_i\) are exactly the added equivariance conditions for arbitrary blocks; characteristic-zero equality then gives equality for divided powers, whose integrality is already established. The explicit qualification about invariant and level subspaces prevents a false extension to unspecified global forms. No equivariant extension to the whole exterior lattice or algebraicity of these particular particle-hole subspaces is asserted. These scope distinctions are correct.

## IF-11: the inhabited actual theta-jet specialization

**Verdict: mathematical proof approved.** I read the entire initial contribution, the complete revised contribution with corrected field-adjunction attribution and locators, and the primary source proofs described below. The complete reread version had SHA256 cfb501fc60af314bfdf5e22b2e7368284306bd873e072db98dd7cde246037873; the final sentence-only precision revision has SHA256 fc6bcaddf4bc576fd308d831886d3ab69f8054f221023ff2b4d5e169b6d313da. The final sentence-level precision has now been applied and reread: the field extension retains the preliminary rank and weight data, and the subsequent ambient replacement retains the resulting base B. No outstanding correction remains.

The selected witness is genuinely the one produced by ExistsHypJetsAll, not an arbitrary witness of its unrefined existential statement. ExistsHarishChandraWeights chooses distinguished word zero; ExistsNatBoundPre uses the all-true Boolean word, rank Rt 0, and parameters \(\Delta=1,h=18,u_F=24,u_L=-1,b_1=1\). ExistsHypJetsAll then restricts to this word and adjoins finitely many algebraic coefficients. The subsequent JetEx replacement retains its base and weights, but changes the ambient normalization and the two index exponents. The contribution and SF-Q6-02 both state the normalization change correctly.

Independent calculation gives
\[
 \lambda_0=(21,20,17,14,11,8,5,3),\quad
 (s_0,s_1,s_2)=(3,-15,-43),\quad
 (n_0,n_1)=(10,20).
\]
Subtracting the actual \(8j\) stage shift is necessary. The resulting polynomial partitions and kernel partitions in IF-11c,d agree exactly with this calculation. Their polynomial degrees are \(75,155,635\); determinant insertions contribute \(80,480\). The kernel moments therefore have multidegrees \(155,635\) per embedding and total degrees \(1240,5080\). The per-embedding CM characters are the true weight sums \(99,-205,-1085\), with eightfold sums \(792,-1640,-8680\). All displayed root gaps and second-descendant invariants agree with IF-04.

The algebraicity input has the exact scope needed by the finite operator. JetsIn asserts the field-valued normalized ordinary derivatives in the prescribed multidegrees. Every monomial coefficient in the tensor product of exterior-power matrices has precisely these degrees, so no all-degree rationality theorem is needed. The factors \(\chi_F^{-1}\) and \(c_D^\beta\), and the absence of division by \(\beta!\), agree with jetNum and jetC. The complete jetsAll_of_colIn proof ties these degree-restricted jets to the assembled kernel. The finite-generating-set wrapper and actual BaseExt.exists_base field adjunction are now attributed separately.

The flag-polynomial test follows directly by applying the target highest functional to the exterior tensor of the source highest vector. Its column-height exponents are \(1,3,3,3,3,3,2,10\) at the first step, and these together with a height-24 exponent 20 at the second. Hence
\[
 P_1=\Delta_1\Delta_2^3\Delta_3^3\Delta_4^3
       \Delta_5^3\Delta_6^3\Delta_7^2\Delta_8^{10},
 \qquad P_2=P_1\Delta_{24}^{20}.
\]
Taking the product over embeddings gives the stated highest-to-highest coefficient \(J(P_j^{\mathrm{tot}})\). For coordinate exponential moments this is one. The contribution correctly makes no nonvanishing assertion for the actual analytic moments, and keeps the full frame-conjugation/scalar factors outside this single standard-frame entry.

I independently recomputed the Weyl dimension from the exact rational product, using Python Fraction arithmetic separately from the author's prime-exponent script:
\[
 \operatorname{rank}T_{\alpha_0}(8)
 =7\,451\,882\,343\,628\,800
 =2^{28}\cdot3\cdot5^2\cdot7\cdot11^2\cdot19\cdot23.
\]
Thus it cannot equal \(4^n\), and neither can its eighth power. This is a whole-coefficient-module obstruction, not a claim about dimensions of unspecified invariant-form subspaces. The common-root exponential construction fits into \(V_{39\cdot48}=V_{1872}\) per embedding and \(V_{14976}\) after all eight factors.

### Source check scope

Complete source files read: ExistsHypJetsAll, ExistsNatBoundPre, ExistsHarishChandraWeights, HarishChandraParameterFormula, JetsInIffStepField, DegreeEqTotDeg, ExistsColInJetsIn, and JetsAllOfColIn. Relevant HostFam and ThDistC derivative definitions, plus previously reviewed weight and determinant-shift definitions, were checked. I used the imported normalized-vacuum algebraicity and theta/lattice-reduction theorems as supplied results; I did not independently re-prove every deeper import.

The final scope is accurate: this is an inhabited actual theta-jet family on which IF-08 and the normalized geometric coefficient realization IF-10 apply. It does not provide a nonzero composed global period, a full SizeData₂ instance, a positive full sg, or preservation of an automorphic motive or L-function. SF-Q6-02 proves that the selected small-weight witness cannot itself carry SizeData₂.
