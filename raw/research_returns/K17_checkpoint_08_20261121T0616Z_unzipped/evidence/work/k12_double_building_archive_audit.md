# Independent audit: the finite double-building gate for K12

21 November 2026 UTC. Reviewer: GPT-6 Astra Pro, `/root/archive_kummer`; effort setting not exposed.

## Verdict

**Endpoint clarification and proof repair, added 2026-11-21:** the original reconstruction below used the announced DEKM Table 5 assertion for H3(GL9;St9). Its underlying enumeration endpoint has the same cone/projective concern as the rank-eight degree-five assertion: projective degree eleven requires cone rank twelve, beyond the rank-nine `n9_rnk11` data. The original audit was relative to the stated Table 5 theorem; it did not independently validate that endpoint computation. The displayed three double-building hypotheses nevertheless prove the two target groups without that rank-nine source assertion. First use H̃10(T²(Z^9);R)=0 and the existing lower exactness to form the rank-nine resolution through S3, appending ker(S3→S2) in degree four. In total degree three its first page uses only ranks at most eight through homological degree three. The only possible nonzero Künneth tensors have all rank-one factors (total rank five), or one rank-three/four degree-three factor and one rank-one factor (total rank at most five). Thus H3(GL9;St9⊗R)=0 follows from the existing hypothesis. Use this derived vanishing in the rank-ten proof below. This repairs the conditional two-group conclusion without adding a hypothesis. The separate H5(GL8;St8) input for the final K12 step remains a source gate. This paragraph supersedes any implication below that only the rank-eight endpoint was relevant to the original use of Table 5.

**PASS as the stated conditional implication.** The entire `work/k12_double_building_gate.md` was read. I independently reconstructed its index shift, partial resolution, hyperhomology spectral sequence, and every possible low-degree Künneth term. I then read the exact primary MPP passages and inspected DEKM Table 5 visually. The three added double-building vanishings remain hypotheses; this audit supplies no proof of them and no unconditional K12 vanishing.

The proof's two finite-rank conclusions are

    H4(GL9(Z);St9 tensor Z[1/13!])=0,
    H3(GL10(Z);St10 tensor Z[1/13!])=0,

conditional on the displayed three reduced homology vanishings. Its final implication for K12 additionally uses the separately checked two-rank reduction with that reduction's stated source inputs. A separate question about the highest rank-eight Voronoi degree in the source data does not enter the present two finite-rank spectral-sequence calculation; it is not silently resolved by this audit.

## Exact reconstruction

Set R=Z[1/13!]. The augmented decomposition complex has

    S_i(Z^N)=direct sum_(V1 direct sum ... direct sum V_(i+2)=Z^N)
                 St(V1) tensor ... tensor St(V_(i+2)),
    S_-1=St_N.

MPP Theorem 23.3 states, in its notation N=n+1,

    H_i(S(Z^(n+1)))=reduced H_(i+n)(T²(Z^(n+1))).

Thus the shift in the candidate is exactly i+N-1. Theorem D' gives exactness through S1 for N>=4. At N=9, the two hypotheses in degrees 10 and 11 give exactness at S2 and S3. At N=10, the hypothesis in degree 11 gives exactness at S2. Flatness of R preserves these statements.

Take d=4 for N=9 and d=3 for N=10. Put S_p in homological degree p for p>=0 and append the kernel of S_d to S_(d-1) in degree d+1. This is a resolution of St_N. Its terms are free over the PID R, since the integral Steinberg modules are free abelian and submodules of free R-modules are free. They need not be projective R[GL_N]-modules; the hyperhomology construction does not require that.

A group projective resolution tensored with this exact complex gives a first-quadrant spectral sequence with

    E1_(p,q)=H_q(GL_N,S_p tensor R)

for p<=d. GL_N acts transitively on ordered decompositions with fixed ranks, and the stabilizer is the direct product of their general linear groups. The coefficient tensor is exactly the corresponding Steinberg tensor. Shapiro therefore gives the candidate's direct-sum formula. The only extra kernel column is p=d+1, so it has no term of total degree d. If every E1 term of total degree d is zero, the same diagonal of E-infinity is zero, regardless of incoming or outgoing differentials, and the abutment in degree d vanishes.

The inspected Table 5 states that in ranks 1 through 8 and degrees 0 through 4, the only nonzero groups after the indicated localization are the degree-zero rank-one copy of R and the degree-three rank-three and rank-four copies of R. Its rank-nine column is zero through degree three. All primes inverted in those entries are among the primes inverted in R. The rank-one assertion also follows directly because GL1(Z) has order two and St1=Z.

Each factor homology module relevant to total degree at most four is zero or free R. Thus no Künneth Tor term can appear; such a term would only use factor degrees no larger than the total degree and would have a free factor. Iteration introduces no additional possibility.

At N=9 every proper factor rank is at most 8. A nonzero tensor in q<=4 would have all factors rank one in degree zero, or exactly one rank-three/rank-four factor in degree three with all other factors rank one. For p+q=4, the first case has p=4, six factors and total rank six; the second has p=1, three factors and total rank at most six. Neither sums to nine.

At N=10 the only additional possible factor rank is nine, whose relevant homology is zero through degree three. For p+q=3, all rank-one factors have p=3 and total rank five. One degree-three factor has p=0 and total rank at most five. Neither sums to ten. This exhausts every case and proves the two asserted conditional vanishings.

## Primary checks actually made

- MPP, `work/steinberg_integral_mpp_2025.pdf` / `.txt`, §23.3 and Theorem 23.3 with complete proof, printed p49; Lemma 23.5 and its complete proof, pp50–51. The normalization of the augmented index and the appended kernel term were read directly, not inferred from Theorem C's global hypothesis.
- MPP Theorem D' was read at its statement in §30 and its repeated statement in §33.2. It asserts exactness of S2 to S1 to S0 to St, hence homology zero through S1. The present audit uses this source theorem; it does not represent a new independent proof of the entire connectivity theorem.
- DEKM current author PDF, `work/k12_source_data/dekm_author_current.pdf` / `.txt`: Proposition 1.5 with its preceding relative-homology normalization, printed p5; Theorem 4.5 and Corollary 5.1, p16; Table 5, p17. The table was visually inspected via `work/qa/dekm_table5_p17.png` and compared with the extracted text. Its caption explicitly says that blank entries are zero and identifies row k with H_k(GL_N;St_N).

The primary rank-eight data-index question noted by the author concerns a possible cone/projective off-by-one at Voronoi degree12, corresponding to Steinberg degree5. The present proof uses rank8 only through Steinberg degree4, corresponding to Voronoi degree11. Accordingly that question does not change the conditional two-group deduction audited here. I make no assertion about whether the source theorem or its external computational data needs correction.
