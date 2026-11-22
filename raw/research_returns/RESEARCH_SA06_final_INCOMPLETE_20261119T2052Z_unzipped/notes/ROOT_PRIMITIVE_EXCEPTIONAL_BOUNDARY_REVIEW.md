# Root independent review — the primitive exceptional-boundary lemma

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), RESEARCH_SA06, /root. No priority claim. Full review completed 19 November 2026, approximately 15:19 UTC.

## Material actually read and exact conclusion

Read the complete original `agents/frobenius/C3_primitive_exceptional_boundary_draft.tex`, PB.1–18, in three bounded chunks, then the complete diff to the final `C3_primitive_exceptional_boundary.tex`. The final changes replace Step 3 by an integral primitive quotient, move the already required Picard-thickening and formal-existence citations into Step 4, and record the retained alternate proof. The initial attempt to print the full draft was truncated and was not counted as a reading; the subsequent three chunks cover the full text.

Outcome: PASS for the whole auxiliary proposition under its exact geometric hypotheses, for every m>=0, s>=1, and algebraically closed k of positive characteristic. This is not by itself a construction of a local counterexample. Actual ordinary families, the nonzero cup, the split principal target, and the required geometry remain assertions of the separately audited combined theorem.

## Relative class and whole Chow-kernel reduction

The sheaves used are ordinary Milnor-symbol sheaves. The exact relative sequence and its exponent-p kernel J_n give the unique relative lift in H^n(J_n) of every absolute class reducing to zero: the preceding H^(n−1)(V,K_n^M) is divisible by the previously fully checked Rost-localization argument, while H^n(J_n) is killed by p. This is the correct preceding cohomology degree. The relative conormal dlog map and its product identity were previously rederived including p=2. The product of a nil line bundle and fixed divisors has the stated ordered cup coefficient one, without a factorial.

The integral Chow decomposition of T×C follows by the projective-bundle formula and successive blow-ups of point-products. It retains Pic(C) torsion. Each cubic factor has integral basis 1,H,E_1,...,E_6,z, and every top class is an integral divisor polynomial. The projective-space factor is harmless for m=0 as well as m>0.

The elementary adjoint argument is valid on the full rational Tate lattice: the cubic chain 1,A,3z has squared norms 1,2,4 and lowering coefficients 2,2; primitive divisors carry weight zero and zero raising/lowering operators. On projective space the lowering coefficient is j(m−j+1). Their tensor commutator is weight 2j−2s−m. The norm identity gives injectivity of b in negative weight and of b² in weight at most −2; the endpoint weight −2 follows by applying the weight-zero identity to bv and then adjointness. Degree s−1 has weight −m−2, so both needed maps are injective for all m>=0. Since the integral groups are free, rational injectivity is enough for these specific integer equations; no integral hard Lefschetz assertion is invoked.

Write gamma=alpha+v[o]+eta, with eta in B_(s−1) tensor Pic^0(C). If L·gamma=0, its free equations are b alpha=0 and e alpha+bv=0, where e=deg K_C is a nonzero integer. Thus b²v=0, v=0, and alpha=0. The remaining equation is exactly b eta=0. Smith bases for the injective integral lattice map therefore describe the entire exceptional kernel as sum v_j Q_j with b v_j=d_j w_j and d_j Q_j=0. Nonunit invariant factors, including those divisible by p, are kept.

## Final integral saturation proof

The integral Chow ring is multigraded by the degrees on the projective-space and cubic factors. Only multidegree (0;1,...,1) can reach the specified Kunneth component of the twisted differential cup. Every anticanonical class A_i is primitive because its intersection with a line is one. Hence Lambda_i=Pic(W_i)/Z A_i and their tensor Lambda are finite free abelian groups.

Project the degree-s Chow lattice to that multidegree and then to Lambda. This defines the integral map Psi. A term of b v reaching that component necessarily inserts an A_i in a missing cubic factor; the projective-space term has the wrong degree. Thus Psi(bv)=0. Applying it to the exact Smith equation gives d_j Psi(w_j)=0, hence Psi(w_j)=0 in a free integer group. This occurs before reduction to characteristic p.

The selected coherent cup Phi factors through Psi. For each cubic, the restricted Euler sequence has the isomorphism k^4→H^0(A) on global sections and H^1(O)=0. Therefore H^1(Omega^1_(P3)(1)|W)=0. The ambient cotangent class of O(1) maps to dlog A, so multiplication by any section followed by this class is zero. Thus mu_A=0, and additivity in each integral Picard variable gives the factorization through every Lambda_i. Consequently Phi(w_j)=0 even when p divides d_j. This kills the saturation of the b-image; it does not assert that b is integrally split or that the full exceptional kernel vanishes.

## Retained Witt proof independently checked

The original Step 3 is also valid. A primitive lift of each cubic equation over W(k) is flat; smoothness near the special fibre and properness give a smooth projective lift. H^2(O_W)=0 permits every Picard basis element to lift through successive Witt thickenings, and projective formal existence algebraizes the system. One can choose a basis containing the primitive A and lift it as the hyperplane bundle.

The restricted Euler sequence is acyclic, and the conormal and hypersurface sequences identify H^1(Omega_W(A)) with H^2(O_W(−2A)) and H^3(P3,O(−5)), a free rank-four Witt module. These identifications commute with reduction. The lifted designated cup kills every b-image; its target Hom module has no integer torsion, so it also kills every w_j in the saturation. The final integral quotient proof avoids this lifting machinery. No error or withdrawn mathematical assertion is concealed by that simplification.

## Actual curve-line lifts and the additive vanishing

The factor cohomology gives H^2(V,L^n)=0 for every n>=1, H^1(V,L^n)=0 for n>=2, and H^1(V,L)=H^0(T,L_T) tensor H^1(C,K_C). The square-zero unit sequence lifts each individual curve line bundle through all infinitesimal neighbourhoods. Their ideals are exactly powers of the base maximal ideal by the hypothesis m_R O_Z=I_V. Projective formal existence over the completion gives a line bundle there. The finite presentation of the bundle and its inverse, regularity of the completion map, Popescu, and henselian lifting through a smooth algebra give an actual bundle on Z with its chosen first jet preserved. This only uses a finite list at any one application, not an algebraization of a Picard functor.

The canonical actual extension of K_C is O_Z(−V) tensor q*L_T^(−1). Its restriction is K_C, and this identity does not require a nonexistent projection Z→C. For any Q in Pic^0(C)(k), the product K-tilde·Q-tilde reduces to zero because both reduced factors come from the curve. Its absolute Milnor class therefore has a unique relative lift xi_Q. If the actual lift of Q is changed, the relative differential changes by a' cup dlog K_C. Both cohomological degree-one factors lie on C, so the change lies in the zero group H^2(C,K_C tensor Omega_C^1). The resulting F(Q)=tau_2(xi_Q) is well defined. Tensor products of lifts and uniqueness of relative lifts show that F is additive. Since Pic^0(C)(k) is divisible and the target has exponent p, F=0. This only claims vanishing of the relative differential, not of xi_Q itself.

## Exact exceptional identity and finite-stage comparison

If beta vanishes off V, localization gives beta=i_*gamma. Its zero restriction to V and self-intersection put gamma in the whole kernel just described. All lattice classes are actual divisor polynomials pulled from the smooth cellular T; their identities pull back as Chow-ring identities. The projection formula and O_Z(V)=q*L_T^(−1) tensor K-tilde^(−1) give the literal Chow identity PB.18. The first sum uses the nil bundles Q-tilde_j^(d_j); its projected relative differential vanishes by Phi(w_j)=0. The second sum uses xi_(Q_j) times the actual divisor polynomial v_j; its full relative differential vanishes by F=0 and symbol-product compatibility. Every summand reduces to zero, so uniqueness of relative lifts identifies their sum with the relative lift of the total class.

The finite list of line bundles and rational-equivalence witnesses descends to one pointed etale model. Properness permits a shrink on which the finite-type source is regular and hence smooth over perfect k. The pointed etale base change preserves the residue field and the quotient by m², so the actual E and all chosen jets remain fixed. Integral Milnor–Bloch and ring-product compatibility apply on that smooth model. Restriction to E then gives the desired absolute cup identity; uniqueness supplies the relative one. No comparison theorem on the nonreduced E, unproved cohomology/filtered-colimit interchange, or absolute-differential substitute is used. The projected beta invariant is nonzero by hypothesis, contradicting the computed boundary invariant.

## Exact primary sources freshly opened

The root freshly opened and read Stacks Project Section 30.8, Tag 01XS, Lemmas 30.8.1 and 30.8.2 with their proofs, including the final base-change/multiplication argument. These justify the projective-space cohomology and reduction identifications; the Euler/conormal deductions above were separately rederived. Also freshly opened and read Lemma 37.4.1 (0C6R), Lemma 30.24.3 (0885), Lemma 15.51.14 (0AH2), Theorem 16.12.1 (07GC), Lemma 32.10.3(2) (0B8W), and Lemma 15.13.3 (0H74), matching each hypothesis to the actual construction.

The earlier full root audits of Jiang Theorems 2.4 and 2.8, Stacks 02TX, Rost's localization/projective-bundle formulas, Kerz Theorems 7.1 and 7.5, and Braunling Section 3 diagram (22) remain the exact source record for those reused inputs. They are not claimed to prove this auxiliary proposition verbatim. No new program is asserted to prove this infinite-family lemma; the prior lattice certificates support only their stated finite cases.
