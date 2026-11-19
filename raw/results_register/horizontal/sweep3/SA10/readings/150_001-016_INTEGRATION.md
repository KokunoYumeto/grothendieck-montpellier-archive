# Cote 150, scans 1-16: integration into SA10

Claude Opus 5.5 at effort max, reader for a6d42bf6fe2b0d8a8 (Claude Opus 5.5 at effort max), horizontal sweep 3, 19 Nov 2026. The full reading is `150_001-016.md`.

## STUDY

Cote 150 opens "Espaces stratifiés et voisinages coniques (ou : déploiement des espaces stratifiés)" (déc. 81): fourteen written pages (006, 011 blank) in three movements.

**1. The deployment (002, 007, 008).** A stratified space over a finite ordered set I is replaced by its deployed strata Σ_i (manifolds with boundary), tubes of raccord Σ_ij and junctions Σ_ijk: one space Σ_d for every flag d of I, contravariant in d. Initial segments give fibrations, cofinal segments bordant inclusions. Two cartesian squares govern the triple pieces: concatenation Σ_ijk = Σ_ij ×_{Σ_j} Σ_jk, and the corner Σ_ijk = Σ_ik ∩ Σ_jk in Σ_k. On 008 three strata become correspondences, and condition a) says exactly that Σ_0 ⨿ Σ_1 ⨿ Σ_2 is an ordered space over [2], the first form of the "Cat-objet" of 042. Slips: 002 l.41 (target Σ_k for Σ_i), 008 l.4, 35, 46.

**2. Stratifications as maps to an ordered set (003-005).** Esp(I), with the up-sets open (@809), is adjoint to the specialization preorder, and a stratification is φ: X → Esp(I). The stratifying partitions with I ordered are exactly the locally finite families of closed sets with 1° (increasing, covering), 2° X_i ∩ X_j = ⋃_{k≤i,j} X_k, 3° X_i^* ≠ ∅ and 4° X_j nowhere dense in X_i. All of it is re-proved here. False on 005: "3° bis with 1° and 2° gives fidelity" (I = {a<b}, X_a = X_b = X). It needs 4° or 3°; the same example refutes 151/57 (4) (SA10-S3-K1). For finite I the quotient condition reduces to a clean form c′), automatic under 4°. M̄_{g,n}, stratified by stable graph type, is strict: 2° is EXIT_TOWER A.3, 4° the irreducibility of closed strata.

**3. Conical neighbourhoods (012-016).** The absolute conical neighbourhood is the mapping cylinder C(f) of f: Ṫ → Y, with the action of the monoid [0,1]; then thickenings, collars, conical subspaces. Three statements need a hypothesis he does not state, that T̊ be open in X (with T̄ closed):
- (8) of 013 for λ near 1;
- "X^* fermé" in (11) of 015;
- the Proposition's c ⇒ b, and Corollary 2 of 015.

One counterexample, a segment with a spur at a frontier point, refutes all three; with the hypothesis, radial reparametrization and the pasting lemma prove them. His repair is the germ definition (015 margin, 022).

**Connections.**
- 002 and 007 supply the corner stones that the successor-pair theorem of 151/69 lacks: 𝒱_ijk and the deployment over all flags (H1, P1).
- The deployed strata pass the (0,4) test that EXIT_TOWER A.11 fails for ordinary strata; 008 takes the whole fibre product, A.13's replacement.
- 004's 1°-2° are 151/45-52 a)-d); 2° is 156-4's frontier condition (SA21-13); Esp(I) is 156-8's Alexandrov topology.

**State.** 33 check events; 18 corrections (9 slips, 1 precision, 4 readings, 4 refuted and refined); 31 open readings. Ready for an edition with the marks kept, and for translation once the four reading corrections are in and strict|pur (016 l.27) is decided.

## HUNCHES

**H150a-1. The deployment over all flags, with its triple pieces, is the gluing datum that 151/69 lacks. This sharpens H1.**
- Grounds:
  - 002 gives Σ_d for every flag, with the two cartesian squares;
  - 007 names 𝒱_ijk;
  - 008 shows that three strata already need the whole fibre product Σ_012 and the transversalities d) and e).
- The successor-pair theorem of 151/69 glues from pairs alone; the corner stones it lacks are 002's upper square.
- Literature: the unzipping of conically smooth stratified spaces, in D. Ayala, J. Francis, H. L. Tanaka, "Local structures on stratified spaces", Adv. Math. 307 (2017) (locator to be checked).

**H150a-2. The order on Σ_* of 008 is the strict shadow of the exit-path ∞-category. This sharpens H2.**
- Grounds:
  - 008's margin says that a) is an ordered space over [2];
  - with the fibrations of b) and the bordant inclusions, the points of the Σ_i are objects and the points of the Σ_d are chains of exit paths;
  - EXIT_TOWER A.11's W_r is the coherent, Segal-type version of the same presentation.
- Literature: J. Lurie, Higher Algebra, Appendix A, the exit-path ∞-category of a conically stratified space (Theorem A.9.3; locator to be checked).

**H150a-3. "T̊ open in X" belongs among the axioms of a conical neighbourhood, and the germ definition is his own repair.**
- Grounds:
  - the counterexample of SA10-R150a-25 and SA10-R150a-27 needs only a spur at a frontier point of T̄;
  - every statement of 013-015 that fails comes back under this one hypothesis;
  - at the level of germs, (8) holds for small λ when T̄ is closed and Ṫ compact (SA10-K150a-14). So the passage to germs on 015's margin and on 022 removes the failure.
- It bears on H150b-4 of the reading 150_017-030 (the neighbourhood-germ classification).

**H150a-4. The condition c′) of 005 says that the order of I is the adjacency order of the strata, read on closed down-sets. His question on 004 l.64-68 asks for a least moderate stratification.**
- c′) states: the frontier X_j^• of a stratum lies in no union X_{J_0} of a closed J_0 smaller than j̄ ∖ {j}. So each maximal lower index is reached by the frontier.
  - Under 4° it holds, so M̄_{g,n} satisfies it.
  - With the frontier condition it makes the order exactly "X_i^* meets the closure of X_j^*".
- On 004 l.64-68 he asks whether a partition into locally closed moderate parts has a least moderate stratification refining it. The reading majorent|engendre at l.67-68 is still open.
- In o-minimal geometry every definable partition has a refining stratification with the frontier condition: L. van den Dries, Tame topology and o-minimal structures, LMS Lecture Note Series 248, Cambridge University Press, 1998 (locator to be checked). A least one is the open point.
- It belongs to the tame line (SA10-19, SA21-12, 156-3).

## PACKAGES

None new.
- P1 (the gluing theorem for tubes, corrected) and P150b-1 (the deployment of a conically stratified space) gain material:
  - 002, 007 and 008: the deployment over flags, 𝒱_ijk, and the three-strata correspondences with their slips corrected (SA10-K150a-01, SA10-K150a-09, SA10-K150a-12, SA10-K150a-13);
  - 012-016, for the conical-neighbourhood part, with the hypothesis "T̊ open in X" (SA10-K150a-14, SA10-K150a-16, SA10-K150a-17).
- P2 gains the strictness of the M̄_{g,n} stratification in the sense of 004 (SA10-R150a-12).
