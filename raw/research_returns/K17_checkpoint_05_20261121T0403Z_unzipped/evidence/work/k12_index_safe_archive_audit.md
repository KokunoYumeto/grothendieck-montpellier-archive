# Independent audit: index-safe K12 and repaired double-building criteria

Date: 2026-11-21 UTC. Reviewer: GPT-6 Astra Pro, `/root/archive_kummer`; reasoning effort not exposed.

**Verdict: PASS as the stated conditional implications.** Read the whole current `work/k12_index_safe_section.tex`, repaired `work/k12_double_building_section.tex`, bibliography addition, and `work/dekm_source_index_review.md`. No endpoint vanishing, no double-building hypothesis, and no K12 vanishing is promoted to an unconditional conclusion.

Reviewed hashes:

- Index-safe TeX: `a3c3f6c411a9d15f8c16cf406db48b060e5196c61eb26158ba8a300ef032cbaa`.
- Repaired DB TeX: `c94bea55653ab068d5e8d42b9d7c720da9a47048bd7a4fffdf9a24ec5286da5f`.

## 1. The endpoint distinction is necessary

The dimension equalities are d=r−1 and q=d−N+1=r−N. A cone rank twelve record at N=8 reaches Steinberg degree four; cone rank eleven at N=9,10 reaches degrees two and one. The announced DEKM endpoints are one step larger. The new statement distinguishes the announced theorem from the documented enumeration mechanism and retains H5(GL8;St8⊗R)=0 as an explicit hypothesis. It does not assert that this announced vanishing is false.

My earlier DB audit has been amended explicitly: the original proof also used the announced rank-nine degree-three endpoint from Table5. The repaired proof below removes that dependency without adding a double-building hypothesis. The earlier audit was relative to the stated source theorem, not an independent verification of the questioned endpoint data.

## 2. The repaired DB proof

For N=9, the existing H̃10 hypothesis gives exactness at S2, in addition to the existing exactness at S−1,S0,S1. Use S3 in degree three and append ker(S3→S2) in degree four. This is an exact R-free resolution and provides the same decomposition spectral sequence on total degree three. Its proper factors have rank at most eight, so the questioned rank-nine datum is not used.

All relevant factor homology groups through degree three are zero except (rank,degree)=(1,0),(3,3),(4,3), each a copy of R. Thus all-rank-one factors on p+q=3 would have p=3 and five factors, hence rank five. One degree-three factor would have p=0 and two factors, with rank at most five. Neither sums to nine. There are no Tor terms because the factor modules involved are free. This proves H3(GL9;St9⊗R)=0 from the original H̃10 hypothesis alone.

For H4(GL9), exactness through S3 and the resolution starting at S4 give the original diagonal argument using only ranks≤8 through degree four. For H3(GL10), exactness through S2 gives the resolution starting at S3; rank-nine factors now use the vanishing just derived. The original three building hypotheses therefore still imply the two rank-nine/rank-ten groups. The appended kernel always lies in column d+1 and cannot contribute to total degree d. Incoming or outgoing differentials cannot create an E-infinity term on a diagonal already zero at E1.

The final K12 implication now explicitly adds the rank-eight degree-five hypothesis. This exactly repairs the source endpoint dependency.

## 3. The three-rank K12 criterion

With R=Z[1/13!], Quillen's rank spectral sequence has E1_(a,b)=H_b(GL_a;St_a⊗R). The three hypotheses remove (a,b)=(8,5),(9,4),(10,3) from total degree thirteen. The independent low-rank calculation leaves precisely E1_(7,6)=R among ranks two through seven; ranks at most four have no projective degree-twelve cells. Rank zero has no positive-degree contribution, and localized positive-degree homology of GL1=C2 vanishes. MPP Corollary E removes (11,2), and the localized degree-one and degree-zero theorems remove (12,1),(13,0).

Rationally BQ is the infinite-loop-space delooping of connective K(Z). Its rational homotopy generators in this range have degrees one, six and ten. The degree-one generator is exterior and the even generators are polynomial. The only total-degree-thirteen monomial is the degree-one generator times the square of the degree-six generator. Hence rational H13(BQ) has rank one.

Only one first-page term on this diagonal can survive. An incoming differential with nonzero image in its current rank-one free submodule would have rank-one image, destroying the only rational contribution on the diagonal. Therefore all incoming images into it are zero. Outgoing differentials replace it only by a submodule. The eventual term is consequently torsion-free; no extension with another diagonal piece is possible. Thus H13(BQ;R) is torsion-free.

Apply the general stable Hurewicz bound to E=ΣK(Z), which is zero-connected, with i=13 and b=1. The kernel is annihilated by the product of exponents of the first twelve positive stable stems. Their prime divisors are at most (12+3)/2, hence at most seven; they are units in R. The stable Hurewicz map is therefore injective after localization. The ordinary map from π13(BQ)=K12(Z), followed by homology suspension, is the stable map, so its kernel is also zero after localization. A finite group cannot inject nontrivially into the torsion-free H13(BQ;R). This kills K12⊗R. The established 2-primary result and regularity of 3,5,7,11,13 remove all inverted-primary parts. This proves the exact conditional statement.

## 4. Primary source checks actually made

- Freshly opened the EVGS published author copy <https://www.ihes.fr/~soule/documents/YAIMA4438.pdf>. Read the projective convention and stabilizer chain discussion, §§2.2–3.2, pp590–591, and §3.4's Steinberg context. Read Theorem4.3, p597, directly: projective H12 is R at rank seven and zero at ranks five and six. Read Theorem8.1, p604, directly for the degree-three rank-three/rank-four classes. Retrieval references: `turn934851807view0`, `turn709734044view0`, `turn709734044view1`. The source's large chain computations were not rerun.
- Read the entire local author note `work/references/KupersK8short.txt`, dated21October2019, including the rank spectral sequence, the identity BQ≃Ω^(infinity−1)K(Z), Lemmas2.1–2.2 and the complete localized modification argument on pp2–3. This confirms that the degree-one input is localized integral, not merely rational.
- Freshly read MPP Corollary E and surrounding Remark1.18 in `work/steinberg_integral_mpp_2025.txt`, printed p7. It includes H2(GL_n;St_n⊗F)=0 for n≥8 over every commutative ring F. The complete Theorem23.3 and Lemma23.5 proofs and TheoremD' exactness convention were already read for the earlier DB audit.
- Freshly read Arlettaz's construction of the stable Whitehead sequence, pp38–39, Definition6.5, the complete argument proving Theorem6.6 on p40, and the stable/ordinary Hurewicz comparison on pp41–42 in `work/arlettaz_topological_viewpoint_2000.txt`. The general theorem applies to the suspended connective spectrum directly; no unjustified simply-connected BQ assumption is made.

The DEKM endpoint review's search for an erratum or replacement theorem was read, but its searches were not independently repeated here. This audit verifies the conditional proofs and their exact dependencies, not an absence theorem about the literature.
