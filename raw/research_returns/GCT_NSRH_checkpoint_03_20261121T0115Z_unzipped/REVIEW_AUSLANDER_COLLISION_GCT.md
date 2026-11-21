# Independent review of F40: the smooth proper corner repair

Reviewer: `/root/gct_statements`, GPT-6 Astra Pro. Inherited reasoning effort is not exposed. Review completed 21 November 2026 UTC.

**Result: PASS. No mathematical correction or blocker identified.**

Reviewed in full: `agent_auslander_collision_repair.md`, SHA-256 `19f0651145b186b428521f0cb04fc5a844484c881578691b1ff4d97bd4984cd1`. This is a fresh proof review of the complete report, not a review of excerpts or search results. Verification types were full mathematical reading, independent reconstruction of all elementary maps and arguments, and direct local primary-source reading for the stated motivic and TP inputs. No formal proof-kernel verification is claimed.

## 1. Elementary algebra, projective resolutions, and smoothness

I reconstructed the multiplication with composition convention (right factor first). For the right projectives, the bases are indeed P1 = e1 Gamma = <e1,a,c> and P2 = e2 Gamma = <e2,b>. Left multiplication by a embeds P2 into P1 with image <a,c>; left multiplication by b maps P1 to P2 with image <b> and kernel <a,c>. Thus both displayed simple resolutions are exact with the stated orientations. Applying Hom into S2 makes the degree-two term k and the intervening term zero, establishing global dimension at least two. The radical-filtration argument applies even to arbitrary right modules: each quotient is a direct sum of the two simples, and direct sums of the finite projective resolutions remain projective resolutions. It gives the asserted upper bound.

I also independently checked the diagonal resolution rather than inferring smoothness from global dimension. In Q1, the a summand is Gamma e1 tensor e2 Gamma and the b summand is Gamma e2 tensor e1 Gamma. The two terms of d1 land in the appropriate vertex summands. In d2, xb tensor y lands in the a summand and x tensor ay in the b summand. Their middle d1 terms cancel, and the outer terms vanish by ba = 0. The dimensions are 4, 12, 13, 5. All eight displayed d1-image vectors are in the image; their indicated pivot coordinates prove independence over every field. Since multiplication is surjective, rank d1 is exactly eight. Right multiplication by b maps the basis (e2,a) of Gamma e2 to the independent basis vectors (b,c) of Gamma e1, so the a projection of d2 is injective. Dimension then gives exactness at Q1. This proves a finite projective bimodule resolution over any field, with no separability or characteristic assumption hidden in the proof.

## 2. Corner and actual module recovery

The dimensions check: dim Gamma = 5, dim Lambda = 2 + 4*5 = 22, and dim f Lambda f = 2 + 4*2 = 10. The isomorphism e1 Gamma e1 = k[c]/(c^2) sends the actual nonzero collision nilpotent to c = ab. Thus the corner does not remove the radical. The characteristic restriction greater than three belongs to the previously established nonstandard special-fiber presentation, not to the elementary Auslander argument.

For right modules, left multiplication identifies End_Lambda(f Lambda) with f Lambda f, without an opposite-algebra correction. Under evaluation at f, Hom_Lambda(f Lambda, Mtilde) is Mtilde f. Its right corner action is precomposition: composing first with left multiplication by a and then by b corresponds to multiplication by ab. This agrees with the actual right tensor-module convention.

The projective Q is one matrix row with entries in P2, so it has dimension four. Restricting by I2 tensor e1 leaves a row with entries in kb, and right multiplication by c kills it because bc = bab = 0. Hence Qf is exactly the two-dimensional standard row module for M2(k[epsilon]/epsilon^2), with epsilon acting by zero. The dimensions of Mtilde and its corner are respectively 20+4+20*4 = 104 and 20+4+20*2 = 64. The specified scalar blocks and the named normalized matrices with z = 3/4+c preserve the actual specialized action. The report correctly says that End(P) retains the nilpotent faithfully while the original tensor module already kills it.

## 3. Fully faithful corner embedding and nonadmissibility

The extension functor sends the perfect generator B to the right projective e1 Gamma, so it is defined on perfect complexes even though e1 Gamma is not perfect as a left B-module. Its ambient derived right adjoint is exact corner restriction, and the unit is the identity after multiplying on the right by e1. This proves full faithfulness.

Corner restriction of P2 is k over B. The displayed infinite epsilon resolution is exact; tensoring with k gives a copy of k in every Tor degree, so this object is not perfect. If a right adjoint on perfect categories existed, its value at P2 would represent Hom(-,k) on Perf(B). Evaluation on all shifts of B gives one nonzero cohomology module, and naturality for End(B) fixes the usual B-action. The representing object would therefore be k, a contradiction. The same component proves the actual product/matrix corner is not right-admissible. This argument does not confuse the projective upstairs object Mtilde with the nonperfect downstairs M1, and does not assert preservation of M1's higher self-Ext.

## 4. Exceptional pair, motives, and Frobenius

The pair <S1,P2> is exceptional with the stated order: RHom(P2,S1)=0, since P2 is projective and S1 e2=0. The resolution of S1 gives its scalar endomorphism ring and vanishing positive self-Ext; P2 has these properties directly. The resolution triangle recovers P1, giving full generation. Properness provides finite derived Hom complexes and hence both adjoints for each exceptional summand. Thus the asserted semiorthogonal decomposition into two point categories is justified.

For the external implication I read the full relevant context in the local primary source `primary_sources/Tabuada_Weil_1808_00950v7.txt`, corresponding to the inspected PDF:

- Theorem 2.12 and its hypotheses, printed page 8.
- Section 6.1 through 6.2, including the distinction between p-semilinear cyclotomic Frobenius and its K-linear q-Frobenius iterate; equation (6.9), printed page 16.
- Section 7, equations (7.1)--(7.4), printed page 17.
- Example 12.3 and its surrounding additivity discussion, printed page 24.
- The complete supplied proof of Theorem 2.12, including equation (12.6), printed page 26.

Example 12.3 supplies additivity of the noncommutative Chow motive for the explicitly proved semiorthogonal decomposition. The enriched functor (6.9) is a functor with Frobenius, so the resulting four point summands give the actual Frobenius identity on TP0, not merely a four-dimensional vector space with unknown Jordan form. For the point, (7.1)--(7.4) give TP0 = K with F0 = 1 and TP1 = 0. Matrix Morita equivalence and the two additional scalar factors yield four point summands for Lambda. This independently verifies the application and its conventions. The general theorems' foundational proofs are cited inputs and were not re-proved in this review.

## 5. Scope checked

The report states the correct, strictly useful repair: the actual special-fiber algebra and its actual specialized tensor module occur as End and Hom of projectives in an explicit smooth proper category. It does not claim a relative deformation model, an admissible embedding of the singular category, recovery of collision order, a canonical basis, a positive multiplication categorification, or a comparison from category-wide TP to each named action. In particular, purity of the four point TP spectrum does not imply the required nonstandard coefficient realization. No overstatement of that kind was found.

The report is therefore ready for integration at the reviewed hash. A later generated fragment should receive a separate final-text match check.

## 6. Generated final-fragment match

I subsequently read `finding_F40.tex` in its entirety, SHA-256 `462a3816d4532d9e376e018bcf789b093748c590dec880171f7ac1f4b15c5e29`. **Final-text match: PASS.** The fragment retains every elementary proof, both exact action comparisons, the non-right-admissibility argument, the exceptional decomposition, and the precise cited Frobenius enrichment. Its renaming of the projectives to mathsf P_i avoids conflict with the nonstandard generators. The separate Grothendieck dictionary paragraph and the scope paragraphs preserve the report's limitations. No extra mathematical assertion requiring a new proof was introduced.
