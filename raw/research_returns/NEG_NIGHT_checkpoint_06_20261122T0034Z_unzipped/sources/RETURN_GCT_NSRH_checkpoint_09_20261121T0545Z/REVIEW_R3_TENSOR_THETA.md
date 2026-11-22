# Fresh review: actual tensor module, étale collision, and coherent deformation

Reviewer: /root/rectangular_and_theta, GPT-6 Astra Pro. Date: 2026-11-21 UTC. This records full proof reading and independent mathematical checks, not a formal-kernel certificate.

## Scope and fixed snapshots

| File | SHA-256 | Lines |
|---|---|---:|
| agent_rank3_tensor_geometry.md | f438d567cefe73141b7d15c96322adc8fb8b3c58280a32459095d7a8681c7da6 | 343 |
| agent_rank3_deformation.md | ed7f422160dbea12bb2e7ef205b194b51ba07769184aa52d052b2b464310009a | 173 |
| finding_F21_F22_F25.tex | 0f7f028df041b91e0fa7e0a00eec10412e4b63795b386c94971574353d2a6f1b | 290 |
| GCT_NSRH.tex at final-text comparison | 168675a390886383f73f88c4b65d17d97e24c349d444c8a50de395bd2424feb8 | 1380 |

The complete mathematical proof texts in both reports and the entire 290-line final-text insertion were read. The main-paper hash identifies the containing snapshot; this event does not claim a fresh review of every other main-paper section. Earlier rank-three algebra checks are separately recorded in REVIEW_R3_THETA.md.

**Verdict: PASS. No mathematical blocker found.** The only source-locator correction requested in the tensor report was already applied: the monomial tensor action is IV §6.1, printed p.33, not §5.1.

## 1. Actual tensor action T1–T8

The normalization \(c_i=T_i+v^{-1}\), \(c_i^2=\delta c_i\), is the consistent earlier IV convention. It avoids the already documented exponent swap in §11.1. Converting the actual source action of \(T_i^{-1}\) using \(T_i=T_i^{-1}+v-v^{-1}\) gives the three cases in T1.

The weight blocks \(111,222\) are scalar trivial modules. On \(112,121,211\), the three-by-three action and the displayed row change \(B_3\) were independently checked by exact symbolic matrix multiplication, with \(v\) formal. Both conjugations and \(\det B_3=(D-1)^2\) agree. The complementary weight block interchanges the two generators, and swapping the two rows of its standard summand conjugates the interchanged pair back to the same \(U\). This proves the integral splitting \(\epsilon^4\oplus U^2\), since the determinants are units in the specified \(R_0\).

For \(U\otimes U\), the actual expression \(c_i\otimes c_i+(c_i-\delta)\otimes(c_i-\delta)\) gives the stated four-by-four matrices. The \(B_4\) determinant and both conjugations were independently checked symbolically: they are \(8(D-1)^2\) and the asserted blocks \(\epsilon_+,\epsilon_-,N(D-2)\). These checks use polynomial/rational-function identities, not values at a few parameters. The separate ordinary-Hecke evaluation determinant \(-\delta(D-1)^3\) was also independently checked; it is not needed to infer any unjustified global projective-module freeness.

The multiplicities follow without a generic-to-integral inference: \(16\) copies of \(\epsilon\otimes\epsilon\), \(16\) mixed copies, and four copies of \(U\otimes U\) give \(20,4,16,4\). Their dimensions sum to \(64\). At \(v=1\), the two rank-two branches coalesce to the standard module, with multiplicity \(20\). All denominators are regular at that point in characteristics different from two and three; the colliding-root difference is never inverted.

## 2. Named branch action and Morita side T9–T10

For \(q=a/D\), the determinant of \(S_a\) is \(q\), which is a unit for both \(a=\delta\) and \(a=D-2\). The two displayed conjugations were independently checked with a formal nonzero \(q\). They give the exact matrices \(e,f\) from the center model evaluated at \(z_i=1-q^2\), so this is action compatibility with named generators rather than a dimension comparison.

For a column bundle \(E=\mathcal O_C^2\), \(\operatorname{Hom}(E,F)\) consists of row vectors, and precomposition gives the right \(M_2(C)\)-action by row multiplication. Thus T10 has the correct side and requires no unstated opposite-algebra change. The two branch quotients jointly have zero annihilator because root evaluation embeds \(C\) in \(R_0^2\). Both scalar summands occur as well, proving faithfulness before specialization. After specialization the common central nilpotent kills both branch modules, exactly as the original ambient action does.

The report correctly calls \(F\) coherent rather than locally free on the collision component. Distinct generic branch ranks \(16\) and \(4\) already preclude a vector bundle there. It also correctly separates this right-module statement from a simultaneous based left-quantum-group identification.

The included DVR lemma was supplied by this reviewer and is a targeted recheck, not a second independent proof event: scale a generic intertwiner to integral entries with one unit, reduce to a nonzero map of simple special fibers, and use its invertible determinant.

## 3. Universal-homeomorphism and nearby-cycle assertions E1–E5

The map \(R[x]/(x(x-t^m))\to R^2\), \(x\mapsto(0,t^m)\), is injective and has exactly the stated congruence image. For \(m\ge n\), \(C_n\) is finite over \(C_m\) because its two \(R\)-generators also generate over the larger coefficient ring \(C_m\). The induced map is the identity on the two generic points; each special fiber has one point with unchanged residue field. Thus it is integral, surjective and radicial, and hence a universal homeomorphism. The argument does not mistake equality of topological spaces alone for universal injectivity: the identical residue fields supply the needed radicial condition.

The normalization and conductor calculation is exact. The difference map gives \(R^2/C_m=R/(t^m)\), of length \(m\). Testing multiplication against \((1,0)\) and \((0,1)\) shows that the conductor is \(t^mR^2\). These coherent quantities genuinely retain the collision order.

The two cited topological-invariance statements were freshly opened by this reviewer: Stacks Theorem 59.45.2, tag 04DZ, and Proposition 59.45.4, tag 03SI. They apply to the verified universal homeomorphism and give the asserted étale-category/topos and cohomology equivalence. The report accurately excludes the coherent structure sheaf from this coefficient-topos comparison.

Over a strict henselian trait the finite algebra in question is local and strictly henselian, while its geometric generic fiber is two split points. Thus the nearby-cycle stalk is \(\mathbf Q_\ell^2\) in degree zero. Constant sections specialize diagonally, so the vanishing-cycle cone has its single cokernel \(\mathbf Q_\ell\) in degree zero. There are no negative or positive extra degrees. The two branches and all maps are defined over the residue base, so inertia and Frobenius are trivial. This establishes the entire specified specialization triangle, rather than merely its Euler characteristic.

The conclusion is appropriately limited to these corresponding constant coefficient objects and their ordinary étale operations. Extra \(m\)-dependent coefficient objects or separately supplied algebra actions are not excluded. All tensor and finite-extension trace assertions then follow directly. Translating one root and dividing by the unit in the root difference identifies the completed actual center with \(C_2\) in the stated good characteristics.

## 4. Full fresh check of the deformation report D1–D5

### Commutants and base change

A \(C\)-map \(L_1\to L_2\) is multiplication by an \(r\in R\) annihilated by \(z_2-z_1=-\Delta\). Since \(R\) is a domain, it is zero; the reverse map is also zero, and each branch endomorphism ring is \(R\). Morita equivalence therefore gives the claimed four matrix factors. The ranks \(400+16+256+16=688\) are correct.

At the special fiber the two branches give the same simple module, so their multiplicity spaces combine to dimension \(20\). The map from the old two factors is literally the block-diagonal embedding \(M_{16}(k)\times M_4(k)\to M_{20}(k)\). Its two omitted blocks have dimensions \(64\) each. Thus it is injective with cokernel dimension \(128\), and the full special commutant has dimension \(400+16+400=816\). The report correctly refuses to describe a free rank-688 algebra itself as acquiring rank 816.

### Crossed and same-branch extensions

In the domain \(R[z]\), cancellation proves
\[
\operatorname{ann}_C(f_1)=f_2C,\qquad
\operatorname{ann}_C(f_2)=f_1C.
\]

This verifies every map and exactness in the full two-periodic resolution. With target \(L_2\), the degree-zero differential is \(-\Delta\) and the next one is zero, giving \(\operatorname{Ext}^1=R/(\Delta)\). With target \(L_1\), the first is zero and the next is \(\Delta\), giving zero in degree one because \(\Delta\) is a nonzerodivisor. The index-exchanged complex gives the reverse crossed group.

Finite additivity and Morita equivalence give \(16\cdot4+4\cdot16=128\) crossed copies. The two other central blocks contribute no higher extensions of free \(R\)-modules. Since \(\Delta\) is a unit times the square of the uniformizer, each crossed quotient has length two, and the total length is \(256\). No unsupported derived-base-change theorem is needed for these conclusions.

As a further consistency check, the same complexes show higher odd Ext groups have \(128\) copies of \(R/(\Delta)\), while positive even Ext groups have \(16^2+4^2=272\) copies. This supplementary observation is not required by the reviewed final text and is not counted as a separate finding here.

### Regular center basis and the trace normalization

The affine change \(y=D^2(z_1-z)\) has invertible linear coefficient, and its two evaluations are \(0,D^2\Delta\). Root evaluation is injective, so \(y^2=(D^2\Delta)y\). The factorization
\[
D^2\Delta=(D-1)(D-4)
=(v-v^{-1})^2(v^2+1+v^{-2})
\]
is exact. Matrix units with coefficients \(1,y\), plus the scalar blocks, give all ten basis elements and constants \(0,1,\lambda\). At specialization \(y\) is a nonzero scalar multiple of the central dual-number parameter, so the four \(yE_{ij}\) span the radical.

With \(Q=v^2\), direct multiplication gives
\[
\lambda=Q^{-2}(Q-1)^2(1+Q+Q^2)
=Q^2-Q-Q^{-1}+Q^{-2}.
\]
For prime-power \(Q\), the unnormalized factor is the point count of \(\mathbb G_m^2\times\mathbf P^2\). A Tate twist \((2)\) multiplies its compact-support alternating trace by \(Q^{-2}\), as asserted. This is a mixed Tate alternating trace, not a single effective pure cohomology group or a categorification of multiplication. The report and final insertion preserve that distinction and the separate consecutive-\(v\) grading warning.

## 5. Final-text comparison and event labels

The whole final insertion faithfully states the checked arguments and restrictions above. Its F21 matches T1–T10, its F22 matches E1–E5, and its F25 matches D1–D5. No formula, side convention, characteristic assumption, or essential scope warning was lost in compression.

Event labels: fresh whole-proof review for the deformation report and final insertion; independent exact symbolic action checks for the tensor matrices performed earlier in this same run and re-used here; independent explicit mathematical reconstruction for the étale collision and periodic Ext complexes; fresh source-statement/application checks for Stacks 04DZ/03SI; targeted recheck for this reviewer's own DVR lemma. No claim is made of re-proving the complete external GCT-IV or étale-invariance theorems.
