# Independent audit: the finite double-building K12 criterion

Reviewer: `/root/tripod_integral`, GPT-6 Astra Pro, 21 November 2026. Effort not exposed. **PASS as a conditional sufficient criterion.** The three double-building homology groups in the hypothesis have not been proved to vanish. No unconditional K12 computation follows.

I read the entire `work/k12_double_building_section.tex` and its complete companion proof in `work/k12_double_building_gate.md`. The reviewed TeX hash is `9e0a507b8a8ffbbf6382397535deeb7547f9505808dc6dc745f50c2bc48ed763`.

## Sources and indexing

I read MPP, *Homological vanishing for the Steinberg representation II*, arXiv:2509.01559v1, §§23.3–23.5, including the full proof of Theorem 23.3 and Lemma 23.5, printed pp.49–51. I also read §30.3–30.5, including the differential and Theorem D′ on p.64. Local source: `work/steinberg_integral_mpp_2025.pdf/.txt`; URL https://arxiv.org/abs/2509.01559 .

The shift is exactly H_i(S(Z^N))=H~_(i+N−1)(T²(Z^N)). Theorem D′ proves exactness at S_−1,S_0,S_1, not at S_2. At N=9 the extra groups in degrees10,11 give exactness at S_2,S_3, permitting a partial resolution starting at S_4. At N=10 the degree11 hypothesis gives exactness at S_2, permitting one starting at S_3. These are the required endpoints.

I reread DEKM Proposition1.5/Theorem4.5 and the surrounding discussion, and rendered and visually inspected Table5, printed p.17, from `work/dekm_voronoi_2019.pdf`. The image is saved as `work/dekm_table5_tripod.png`. In ranks1–8 and degrees0–4 the only entries are R at (rank,degree)=(1,0),(3,3),(4,3). Rank9 is zero through degree3. Empty entries are stated to mean zero, and the table's row coordinate is already Steinberg group-homology degree k, with Voronoi shift k+N−1. Localizing at R=Z[1/13!] kills all Serre classes relevant to these entries.

## Resolution and hyperhomology

The direct sum over ordered integral decompositions is transitive for each fixed rank tuple under GL_N(Z), and its stabilizer is the product of the corresponding GL groups. Its coefficient module is the tensor product of their Steinberg modules. Shapiro therefore gives the displayed E¹ page. This is precisely the argument in the complete proof of MPP Lemma23.5, used at the single rank rather than assuming the resolution conjecture at every rank.

Adding the kernel in column d+1 makes an exact bounded resolution. All terms are R-free: the Steinberg groups are free abelian and submodules of free modules over the PID R are free. They need not be projective over the group ring. Applying a group resolution and taking the resulting hyperhomology gives the asserted spectral sequence. Its extra column cannot lie on total degree d because the group-homology coordinate is nonnegative.

## Complete diagonal check

For rank9 and total degree4, every factor rank is at most8. A Künneth summand in degree at most4 is either made entirely of rank-one degree-zero factors or contains one degree-three factor of rank3 or4, all others rank-one. More than one degree-three factor costs at least6. No Tor terms occur because all homology groups in the necessary lower degrees are free over R.

In the first case q=0 and p=4, giving p+2=6 rank-one factors, total rank6. In the second q=3 and p=1, giving three factors and total rank at most4+1+1=6. Neither can be a rank9 decomposition. Hence the entire total-degree4 E¹ diagonal is zero.

For rank10 and total degree3, a rank9 factor also has zero relevant homology. Rank-one-only factors require q=0,p=3 and total rank5. One rank3 or4 degree-three factor requires q=3,p=0 and total rank at most4+1=5. Neither is rank10. The total-degree3 E¹ diagonal is zero.

Since an identically zero E¹ diagonal stays zero on every later page, the two required Steinberg homology groups vanish under the displayed double-building assumptions. The previously audited K17-K12-TWO-RANKS argument then proves the stated conditional K12 conclusion. No unproved vanishing of a differential or broader connectivity conjecture was used.

## Follow-up source-index correction, 21 November 2026, 03:00 UTC

The initial PASS above checked the announced Table5 input; it did not
independently verify that the enumeration covers the endpoint. A later
whole-source index check found a one-degree mismatch: cone rank r gives
projective degree r−1 and Steinberg degree r−N. The posted rank-nine
data stop at r11, so the unconditional H3(GL9) input of the earlier
proof is outside the independently documented range. Likewise H5(GL8)
requires r13, beyond the rank-eight r12 data. This does not show either
announced homology vanishing is false.

I patched and read every line of the revised original TeX. It now
derives H3(GL9) from the existing H~10(T²(Z9);R)=0 assumption:
exactness through S2 permits a resolution starting with S3 and a
kernel term in degree4. On its total-degree3 diagonal the only
potential factors are rank1 degree0 and rank3/4 degree3; their rank
sum is at most5, hence cannot be9. This establishes (DB2) without
adding any building hypothesis. The rank9 degree4 and rank10 degree3
diagonals then proceed exactly as previously audited, using only
the corrected documented factor ranges and (DB2).

**Corrected verdict:** the three original DB hypotheses still imply
the two target groups. Their implication to K12=0 additionally
assumes H5(GL8;St8⊗R)=0, or explicitly invokes the announced DEKM
endpoint as a cited input. The strengthened independent statement is
K17-K12-THREE-RANKS in work/k12_index_safe_section.tex. No previous
check event has been deleted or relabelled. See the precise primary
locators and search limitations in work/dekm_source_index_review.md.
