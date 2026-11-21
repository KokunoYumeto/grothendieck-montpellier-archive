# Verified references for the Galois task

Date: 2026-11-21. Researcher: GPT-6 Astra Pro child `/root/effective_galois`; effort metadata is not exposed by the runtime.

## Bach–Sorenson (primary)

Eric Bach and Jonathan Sorenson, **Explicit bounds for primes in residue classes**, Mathematics of Computation 65, no.216 (1996), 1717–1735, DOI 10.1090/S0025-5718-96-00763-6.

- Theorem 5.1, p.1729: arbitrary Galois E/K; E not Q; degree-one unramified prime with specified conjugacy class and norm at most `(4 log |d_E| + 2.5 [E:Q] + 5)^2`.
- Last paragraph §2, p.1720: the analytic premise concerns **zeta functions of E and Q**, zero-free to the right of 1/2. Artin holomorphy is absent.
- Theorem 3.2 and Corollary 3.3, p.1721: cyclic reduction and extension from abelian to arbitrary Galois groups.
- Primary author-uploaded PDF successfully opened: https://www.researchgate.net/profile/Jonathan-Sorenson-2/publication/220576951_Explicit_bounds_for_primes_in_residue_classes/links/55100ea70cf2ac2905afbceb/Explicit-bounds-for-primes-in-residue-classes.pdf
- Retrieval reference: `turn613335859view0`; §2 hypothesis at lines216–219, PDF page3. Root must reopen before final chat citation.
- Publisher URL (403 in direct browser retrieval): https://www.ams.org/mcom/1996-65-216/S0025-5718-96-00763-6/S0025-5718-96-00763-6.pdf

## Mayle–Wang (primary)

Jacob Mayle and Tian Wang, **On the effective version of Serre's open image theorem**, Bulletin of the London Mathematical Society 56 (2024), 1399–1416, DOI10.1112/blms.13002.

Full primary text: https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.13002

- Theorem1: `c(E) <= 964 log rad(2N_E)+5760`, E/Q non-CM.
- Theorem2: non-CM E1,E2/Q not Q-isogenous have a good prime of unequal traces at most `(482 log rad(2N1N2)+2880)^2`.
- Theorem5 cites Bach–Sorenson Theorem5.1.
- Corollary6 requires **squarefree positive m** and uses K(sqrt m) to avoid primes dividing m. Secondary quotations sometimes omit “squarefree”; retain it.
- Lemma7 (citing Serre1981 Proposition6): for nontrivial Galois K/Q, `log d_K <= (n-1) log rad(d_K)+n log n`.
- Proposition12: finite deviation-algebra quotient for two Z_l representations, order at most `l^(2r^2)-1`. Our findingG03 states/proves the coefficient-DVR version and explicit uniform ramification bound.
- The introduction names Dedekind-zeta GRH; §3 plus the proof of Theorem2 confirm precisely which analytic result is used.
- Retrieval references: `turn346444527view1`, `turn431575504view1` (Cor6), `turn431575504view2` (Thms1,2), `turn431575504view4` (Lemma7). Root must reopen.

## Serre (original)

Jean-Pierre Serre, **Quelques applications du théorème de densité de Chebotarev**, Publications Mathématiques de l'IHÉS54 (1981), 123–201. Proposition6 supplies the discriminant estimate; Théorèmes21 and22 are the earlier conditional isogeny and open-image bounds. Original paper's detailed proof was not independently rechecked in this child run; the exact proposition locator and inequality were verified through Mayle–Wang's primary statement/proof. No unknown absolute constant is silently made numerical.

## Lombardo (published primary, unconditional)

Davide Lombardo, **Bounds for Serre's open image theorem for elliptic curves over number fields**, Algebra & Number Theory 9, no.10 (2015),2347–2395, DOI10.2140/ant.2015.9.2347.

Primary publisher PDF: https://msp.org/ant/2015/9-10/ant-v9-n10-p06-p.pdf

- Corollary9.3, p2393, also stated in the introduction on p2348: for a number field K and an elliptic curve with geometric endomorphism ring Z, adelic index is less than `exp(10^21483) d^(2.4*10^10) max{1,h_F(E),log d}^(4.8*10^10)`, with d=[K:Q] and h_F the stable Faltings height used in the paper.
- The exact exponent `21483` and the outer exponential were visually checked on publisher p2393, retained as `lombardo_cor93.png`. Local primary PDF and extracted text are retained as `lombardo2015.pdf` and `.txt`.
- This corollary is unconditional. Theorem9.1 is the finer adelic-index statement, deduced using the isogeny bounds recorded in Theorem2.1 and Proposition2.6. The cited statement and hypotheses were rechecked; the entire 49-page theorem proof was not independently repeated.
- The smaller constants in Remark9.4 use the then-unpublished isogeny input of Remarks2.3 and2.7. They are not substituted into the deliverable.
- Useful web references for root reopening: `turn528945879view0` (primary PDF and Theorem2.1), `turn575869752view1` (Cor9.3 at p2393); publisher full-issue parsing `turn984378988search24` also explicitly preserves the exponent `10^{21483}`.

### Actual LM8 application

The model in `recovered/LM8_PUSH_cp17_text/sections/A_nonstable_D3_fixed.tex` is `F_a: y²=x³−3x+a`, a=±6, defined over Q. The proof invokes its representation after restricting to a chosen number field L. Thus there is no missing descent-to-Q hypothesis. Its non-CM certification in `sections/A_prol_normalizers.tex`, A.14, uses ordinary Frobenius discriminants −19 and −35 at 5 and11. These point counts and the model discriminant −2^9*3^3 were directly rechecked. New G06 supplies the Mayle–Wang threshold `964 log6+5760` over Q under M, the restricted mod-ell index bound `[L:Q]`, and an unconditional adelic index bound from Lombardo plus restriction. It does not claim full GL2 image after restriction to L.

## SGA1 (primary)

Grothendieck et al., **Revêtements étales et groupe fondamental (SGA1)**, LNM224 (1971); recomposed edition arXiv:math/0206203v2.

Primary PDF: https://arxiv.org/pdf/math/0206203

- Exp.V, Théorème4.1, recomposed p.104/PDF p.120: abstract Galois-category equivalence.
- Exp.V §7: application to fundamental group of a connected scheme (recomposed pp.115–116).
- Exp.V Propositions8.1–8.2, recomposed p.117/PDF p.133: absolute Galois group of a field, and generic-point description of pi1 of a normal connected locally noetherian scheme as extensions unramified over it.
- Retrieval reference `turn914446209view0` and `turn846709145view0` (exact Prop8.1–8.2 text).

## Further improvement inspected but not needed

Imin Chen and Joshua Swidinsky, **Improved bounds for Serre's open image theorem**, arXiv:2501.00202, inspected HTML dated24August2026. Theorem1.7 improves coefficient constants to446,2254; Theorems1.3,1.5 give other bounds with extra hypotheses. **Do not automatically substitute these in the final package**: the clean published Mayle–Wang bounds suffice, and this child did not audit the computational refinements. The inspected HTML's Cor2.6 drops “squarefree” from Mayle–WangCor6, so it is unsuitable as an unchecked replacement citation. No claim is made here that all its conclusions fail; only its stated citation hypothesis is not copied without checking.

## Source completeness

The original attachment has summaries, bridge keyword contexts, and an intake; it does not itself include the complete papers and row registers identified in those summaries. During this run the parent recovered the complete A1, successor, and LM8 papers. The source-coverage paragraph in effective_galois.tex has been updated accordingly. In the actual LM8 A.32 proof, qualitative Serre open image is used only for Zariski density of a commutator image, with no effective index requested. LM8 D.25 uses Faltings's rational-point finiteness theorem, not Faltings–Serre trace comparison. The row auditor supplies the exact finite splitting fields for the qualitative Chebotarev rows; our G01/G02 and arbitrary-base paragraph give their conditional explicit bounds after those fields are fixed. B.27 in ANABELIAN_A1 and its successor concerns exact least cyclic-cover prime degree191 over a finite field and must not be classified as a number-field Chebotarev least prime.

## Additional primary sources checked for the A1 follow-up audit

Mohamed Saïdi and Akio Tamagawa, **A Prime-to-p Version of Grothendieck's Anabelian Conjecture for Hyperbolic Curves over Finite Fields of Characteristic p>0**, Publ. RIMS45 (2009),135–186, DOI10.2977/PRIMS/1234361157. Primary PDF: https://www.kurims.kyoto-u.ac.jp/~prims/pdf/45-1/45-1-5.pdf . The setting, Remark1.2, Definitions1.3/1.5/1.10, Lemma1.7, and Proposition1.8(vi) were read directly and their hypotheses matched. Useful retrieved references: turn751469338view0, turn751469338view1, turn751469338view2. Detailed scope is recorded in A1_cuspidal_criterion_audit.md.

Brian Conrad, **Chow's K/k-image and K/k-trace, and the Lang–Néron theorem**, L'Enseignement Mathématique(2)52 (2006),37–108. Theorem2.1, p3 in the primary author PDF: https://math.stanford.edu/~conrad/papers/Kktrace.pdf . Retrieved reference turn858315769view0, lines142–143. The finitely generated regular-extension hypothesis was checked; the proof of the cited theorem was not independently repeated.
