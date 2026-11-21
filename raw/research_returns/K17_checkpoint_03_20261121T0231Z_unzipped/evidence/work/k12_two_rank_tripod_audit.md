# Independent audit: the two-rank criterion for K12

Auditor: `/root/tripod_integral`, GPT-6 Astra Pro. Date: 2026-11-21 02:00 UTC. Reasoning-effort setting is not exposed. This is a mathematical whole-proof review relative to the cited theorems, not formal verification and not a claim of novelty.

**Verdict: PASS, with exactly the conditional scope stated.** I read the entire current `work/k12_rank_reduction.tex`, SHA256 `6ca7e9da23e1c8d4086ca7a8afde1af94e3baa4f0b022600fe37585221adbc8b`. The proof establishes the localized degree-two Steinberg vanishing in all ranks at least three and removes rank 11 from the earlier K12 homology gate. It does not establish either of the remaining rank-9 and rank-10 vanishings, and does not establish K12(Z)=0 unconditionally.

## 1. Localized codimension-two result

My earlier complete audit is `work/rank11_localization_audit.md`. I independently read Brück–Miller–Patzt–Sroka–Wilson, arXiv:2204.11967v3, all of §8, pp.56–59, including Proposition 8.5 and Lemmas 8.7 and 8.9 and their proofs. The input is the integral partial resolution; flat localization preserves its exactness. If a prime q divides the order of a finite-order matrix in GL_n(Z), a power of that matrix has exact order q, so its rational characteristic polynomial contains the degree-(q−1) polynomial Phi_q. Thus q≤n+1, and every relevant finite order is a unit in R_n=Z[1/(n+1)!]. Lemma 8.7 applies over this ring.

The proof of Lemma 8.9 supplies an orientation-reversing stabilizer for every relative top simplex, separately for its two types. This proof needs only that 2 is invertible, not that the coefficient ring is Q. The degree-two coinvariant chain module is consequently zero. The partial projective resolution may be extended by choosing free modules onto its successive kernels, proving H2(SL_n;St_n⊗R_n)=0. The index-two Hochschild–Serre sequence gives the identical GL_n vanishing. This applies at n=11 over Z[1/12!], and hence over the larger localization used in the criterion.

## 2. Every term in total degree 13

I read DEKM, arXiv:1910.11598v1, Proposition 1.5, Theorem 4.5, Table 5 on p.17, and §§6.1–6.2 through Remark 6.6 on pp.18–19. I also read the entire local copy of Kupers's 21 October 2019 note, `work/references/KupersK8short.txt`, including Lemmas 2.1–2.2 on p.2 and the complete localization proof on p.3.

With R=Z[1/13!], the first page of the rank spectral sequence is E1_(a,b)=H_b(GL_a(Z);St_a⊗R). On a+b=13, ranks 2 through 8 are zero except for (a,b)=(7,6), which is R. The required rank-8 entry follows from DEKM Theorem 4.5 in Voronoi degree 12. The rank-zero filtration space is a point and GL_1(Z)=C2 has no positive R-homology. The two stated hypotheses eliminate (9,4) and (10,3); the new localized lemma eliminates (11,2). Kupers Lemma 2.2 gives H1(GL_12;St_12⊗Z[1/12!])=0, so eliminates (12,1) after localization. His Lemma 2.1, the Lee–Szczarba coinvariant theorem, eliminates (13,0). Negative homological degrees do not occur. Thus the sole potentially surviving term on this diagonal is one copy of R.

There is no hidden rational-only use of Church–Putman here. Kupers explicitly states the localized theorem and gives the two modifications of the original argument: flat relative chain modules when stabilizer orders are invertible, and the torsionfree coefficient hypothesis in the other lemma. DEKM Remark 6.2 independently records the same localization.

## 3. Differentials and the rational rank

The rational infinite loop space BQ has one rational homotopy generator in degree 1 and generators in degrees 6,10,14,... . Its rational homology is exterior in the degree-one generator and polynomial in the even-degree generators. The only monomial of total degree 13 is the degree-one generator times the square of the degree-six generator. Hence H13(BQ;Q) has rank one.

I checked carefully the integral spectral-sequence step. One must not infer that every integral outgoing differential is zero from rational rank. The current proof makes the correct weaker assertion. Until an incoming nonzero differential occurs, the term at (7,6) is a submodule of R and is torsionfree. Any nonzero incoming image into it would itself have rank one and destroy the sole rational contribution to total degree 13. That contradicts the abutment's rational rank. All incoming images are therefore zero. Outgoing differentials merely replace the term by a submodule, potentially a proper ideal; they preserve torsionfreeness. All other terms on the diagonal remain zero. The spectral sequence is first quadrant, so the filtration is finite in degree 13, and the single nonzero associated-graded term proves H13(BQ;R) torsionfree. This argument does not require a splitting or an integral collapse of the entire spectral sequence.

## 4. Exact Hurewicz bound

I read Arlettaz's primary author review `work/arlettaz_topological_viewpoint_2000.pdf`, including the construction on pp.38–39, Definition 6.5 and Theorem 6.6 with proof on p.40, and the stable/ordinary Hurewicz diagram on pp.41–42. Definition 6.5 sets ebar_i equal to the product of exponents of the first i positive stable stems; its prime divisors are exactly among primes at most (i+3)/2. Theorem 6.6(a) annihilates the stable Hurewicz kernel of a (b−1)-connected spectrum in degree i by ebar_(i−b).

Take the connective spectrum X=Sigma K(Z). It is 0-connected, so b=1, and pi13(X)=K12(Z). The degree-13 kernel is killed by ebar_12, whose prime divisors lie among 2,3,5,7. The ordinary Hurewicz map of BQ=Omega-infinity X followed by homology suspension is the stable Hurewicz map under the natural identification of homotopy groups. Consequently the ordinary kernel is a subgroup of the stable kernel, not conversely. All four primes are inverted in R; flat localization therefore makes the ordinary map K12(Z)⊗R→H13(BQ;R) injective.

This avoids reliance on an OCR-corrupted fraction in DEKM's abbreviated citation of Arlettaz and uses the displayed primary stable theorem directly. No assertion that the stable and ordinary targets coincide is needed.

## 5. Final deduction and exact remaining gate

Finite generation and Borel's rational computation make K12(Z) finite. Its localization injects into the torsionfree R-module just obtained, and is therefore zero. The inverted primes contribute no primary part: the established 2-primary table gives zero in degree 12, and 3,5,7,11,13 are regular odd primes. Hence the two hypotheses imply complete vanishing.

DEKM Proposition 1.5 identifies H_q(GL_n;St_n) with H_(q+n−1)(Vor_GL_n) after inverting finite-stabilizer primes. Our R is more than sufficient in ranks 9 and 10. Both remaining groups correspond to Voronoi degree 12. The prior Remark 6.6 listed ranks 9,10,11; the localized codimension-two result removes precisely rank 11.

## Sources and retrieval details

- Brück–Miller–Patzt–Sroka–Wilson: https://arxiv.org/pdf/2204.11967v3, §8 pp.56–59; local `work/codimension_two_sl_n.pdf/.txt`. Full section read.
- DEKM: https://arxiv.org/pdf/1910.11598v1, Proposition 1.5, Theorem 4.5, Table 5 p.17, §§6.1–6.2 and Remark 6.6 pp.18–19; local `work/dekm_voronoi_2019.pdf/.txt`. All cited arguments read.
- Kupers: https://www.utsc.utoronto.ca/people/kupers/wp-content/uploads/sites/50/2021/01/k8zshorter.pdf, Lemmas 2.1–2.2 pp.2–3. Fresh web retrieval returned 403 (`turn488037659view0`); the existing local author PDF/text was read in full, so no claim of successful fresh web retrieval is made.
- Arlettaz: author review in `work/arlettaz_topological_viewpoint_2000.pdf/.txt`, Definition 6.5 and Theorem 6.6 p.40, comparison pp.41–42; bibliography and source URL are retained in `work/k12_rank_bibliography.tex`.

No new large Voronoi computation was performed or implied. The two still missing vanishing assertions remain explicitly conditional.
