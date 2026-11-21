# Bridges 3, 4, 5 and 7: research and check notes

Owner: `/root/bridges`. Model: GPT-6 Astra Pro. Effort: inherited/undisclosed. Check-record date: 20 November 2026, UTC (clock observation 23:13:36 UTC).

## Main findings and exact scope

- **B3.1:** A sign change makes the Schubert K-product a positive based algebra. On total-degree equality its coefficients equal ordinary LR. This is a deduction from cited statements, not a newly discovered positivity theorem and not a plethysm rule.
- **B3.2:** Actual sign-positive geometric constants have `a_(1),(1)^(2,1)=1` and `a_(2),(2)^(4,2)=0`. The calculation uses Lenart Pieri, as restated in Buch Corollary 4.7, after conjugation. It refutes nonzero-at-scale-one implies nonzero-at-scale-two for K coefficients, hence the full LR dilation equivalence. It does not refute the opposite implication separately. This is an explicit corollary of known formulas, with no priority claim.
- **B4.1:** Matrix Grothendieck objectives and cut norm are positive exactly when the input matrix is nonzero. A polynomial-size efficiently constructible exact zero-preserving realization of a multiplicity by such a norm already puts nonvanishing in P without using SDP rounding. This isolates the difficult part of a proposed norm bridge.
- **B4.2:** A fixed multiplicative approximation guarantee cannot distinguish all consecutive positive integers; its permitted output intervals overlap. This limits what such an estimate alone can certify about strict multiplicity inequalities.
- **B5.1:** Scalar changes leave tensor rank, border rank and full GL orbit unchanged, while scaling nuclear norm. Therefore an unnormalized norm threshold is not an algebraic orbit invariant.
- **B5.2:** Projective norm is monotone under tensor products of contractions and gives a genuine obstruction for that bounded-operator model, including Euclidean limits. This does not cover the full GL orbit.
- **B5.3:** `T_epsilon=(e1⊗e1+epsilon e2⊗e2)⊗e1⊗...` has rank/border rank 2, all positive epsilon lie in one GL orbit, and nuclear/Frobenius ratio `(1+epsilon)/sqrt(1+epsilon^2)` tends to the rank-one value 1. Thus even this normalization has no uniform positive rank gap.
- **B7.1:** For an integral GL representation and integral x,y, every characteristic-zero orbit-closure separation has an integer polynomial witness f which vanishes identically on the integral orbit map, and survives for all primes not dividing f(y). No claim that orbit closures commute with every reduction is needed.
- **B7.2:** In each fixed degree d, construct an integer matrix of the orbit pullback after clearing a common power of det, and an evaluation row. Separation iff appending evaluation increases rank. Two rank-size minors give an explicit integer outside whose prime divisors the criterion agrees with characteristic zero. The expanded matrix generally has too many columns for a polynomial-time flip.
- **B7.3:** G_m scaling on A1, x=2,y=1: no separation over Q, separation modulo 2. Arbitrary finite-characteristic separation need not lift.

The intended ranking within this branch is B7.1/B7.2 (actual geometric transfer), B3.2 (explicit failure of a proposed saturation transport), B5.1--B5.3 and B4.1--B4.2 (precise limits/gates), then B3.1 (dictionary). None settles P vs NP or the GCT positivity hypotheses.

## Primary sources and exact locators

Root must open any child web reference before using its GenUI reference in the final chat. The paper can cite the actual works and URLs below.

| Key | Work and locator | URL | Retrieved refs |
|---|---|---|---|
| `brion2002` | M. Brion, *Positivity in the Grothendieck group of complex flag varieties*, J. Algebra 258 (2002), 137–159. Theorem 1 and Lemma 2; arXiv v1 Theorem 1 on PDF p.2. | https://arxiv.org/pdf/math/0105254 | `turn382071275view0` |
| `buch2002` | A. S. Buch, *A Littlewood–Richardson rule for the K-theory of Grassmannians*, Acta Math. 189 (2002), 37–78. arXiv v2: Corollary 4.7 (Pieri), Theorem 5.4, Corollary 5.5, Example 5.6, Corollary 6.7 (conjugation involution), Introduction (degree-equality LR). | https://arxiv.org/pdf/math/0004137 | `turn382071275view1`, `turn631377434view0`, `turn870257019view3` |
| `kt1999` | A. Knutson and T. Tao, *The honeycomb model of GL_n(C) tensor products I*, JAMS 12 (1999), 1055–1090. Section 6 Theorem 3 and immediately following Corollary (the saturation conjecture), arXiv PDF pp.28–30. The Introduction explains the nonvanishing semigroup via product of invariant sections. | https://arxiv.org/pdf/math/9807160 | `turn870257019view1`, `turn171847896view0` |
| `groth1953` | A. Grothendieck, *Résumé de la théorie métrique des produits tensoriels topologiques*, Bol. Soc. Mat. São Paulo 8 (1953), 1–79. Section 4 no.2 Theorems 1–2 (fundamental theorem); reproduced/typeset PDF below has printed pp.47–48. | https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/AG/AG-22.pdf | `turn268872830view2`, `turn919981465view2` |
| `alon-naor2006` | N. Alon and A. Naor, *Approximating the Cut-Norm via Grothendieck's Inequality*, SIAM J. Comput. 35 (2006), 787–803. Introduction programs (1)–(2), Lemma 2.1, Proposition 2.2, Theorem 4.3. | https://web.math.princeton.edu/~nalon/PDFS/cutnorm3.pdf | `turn268872830view1`, `turn870257019view4`, `turn171847896view1` |
| `rs2009` | P. Raghavendra and D. Steurer, *Towards Computing the Grothendieck Constant*, SODA 2009, 525–534. Theorem 1.1 (UGC optimal hardness). | https://www.dsteurer.org/paper/grothendieck.pdf | `turn382071275view2`, `turn870257019view5` |
| `chtw2010` | R. Cleve, P. Høyer, B. Toner and J. Watrous, *Consequences and Limits of Nonlocal Strategies*, arXiv:quant-ph/0404076v2 (11 Jan. 2010). Theorem 4 (Tsirelson), Proposition 5 and Theorem 7. This primary research article gives the exact vector and bias formulations needed; cites Tsirelson 1987 as [48]. | https://arxiv.org/pdf/quant-ph/0404076 | `turn877000796view0`, `turn586275371view0`, `turn586275371view1` |
| `friedland-lim2018` | S. Friedland and L.-H. Lim, *Nuclear Norm of Higher-Order Tensors*, Math. Comp. 87 (2018), 1255–1281; arXiv:1410.6072v3. Equation (1), Section 2, Theorems 8.1 (real order ≥3) and 8.10 (complex order ≥4), in arXiv v3 numbering. | https://arxiv.org/pdf/1410.6072 | `turn268872830view0`, `turn919981465view1` |
| `sga3-I` | M. Demazure, SGA 3, Exposé I, Section 4.2 (affine group schemes and bialgebras), Section 4.5 (GL_n over Z). | https://webusers.imj-prg.fr/~patrick.polo/SGA3/origExp1.pdf | `turn293863500view0`, `turn713176400view0`, `turn713176400view1` |
| `fga221` | A. Grothendieck, *Techniques de construction et théorèmes d'existence en géométrie algébrique IV: les schémas de Hilbert*, Bourbaki Exposé 221 (May 1961), pp.249–276. Theorems 3.1–3.2; Hilbert special case after Proposition 3.8; Remark 3.9 on Z and vertical components. | https://www.numdam.org/article/SB_1960-1961__6__249_0.pdf | `turn847409731view1`, `turn518081162view2` |

## Source pitfalls actually checked

1. The author-hosted Raghavendra–Steurer PDF has a display in Theorem 1.2 reading an approximation ratio `K_G - eta`, which conflicts with its Theorem 1.1 if interpreted as the standard factor greater than one. I inspected its page 2 screenshot and Section 3.3, whose guarantee is `(1/K_G - O(eta))*SDP`. The deliverable uses only unambiguous Theorem 1.1 and Alon–Naor's rounding theorem; it does not propagate the ambiguous display.
2. The arXiv v2 Buch preprint is 34 pages and has the exact Pieri/Example locators used. The final 42-page published copy has a reported saturation discussion on p.71 (Pak–Robichaux 2026 cites it), but that copy became unavailable to the browser on follow-up requests. No claim relies on that uninspected p.71. Our two coefficients follow directly from the read Corollary 4.7 and Example 5.6.
3. Tsirelson's own 1987 PDF repeatedly timed out; no invented theorem number is supplied. The accurate accessible locator is CHTW Theorem 4, Proposition 5, Theorem 7. It is a primary research paper, not a blog or unsourced survey.
4. Nuclear norm hardness over C is stated only in the order range explicitly read from Friedland–Lim arXiv v3 Theorem 8.10; no extrapolation to all complex 3-tensors is made.
5. The archive files are supplied TeX transcriptions with uncertainty markup, not original scan images. Cote 119 scan 217 and cote 2 scan 17 were read for the limited attribution claims in this branch. No eye-check of an original manuscript image occurred.

## Whole-proof check, after writing

Read the complete `bridges.tex` after drafting, then checked every inference with particular attention to quantifiers, fields and closure notions. Found and corrected one TeX typo in B5.3 (`otimes` missing backslash), changed the stated classical saturation display to the all-positive-N equivalence that B3.2 actually refutes, and replaced a vague matrix-multiplication complexity sentence by the explicit tensor-decomposition identity. No mathematical gap was found in the stated deductions after these corrections.

Specific checks: B3.2 conjugated Pieri: `(4,2)/(2)` is horizontal, four added boxes in two rows, so binomial(1,2)=0. B5.3 the dual functional is complex-bilinear in the first two variables and is bounded by Cauchy–Schwarz; it evaluates to 1+epsilon. B7.1 descent uses flatness of field extension and torsionfreeness of Z[GL]; it never assumes arbitrary reduction commutes with taking an orbit closure. B7.2 denominator clearing works in every characteristic because det is a nonzero polynomial; the row-space/kernel-annihilator equivalence and both minor inequalities were checked. B7.3 gives the required warning about reverse transfer.

This is a targeted full-proof review by the same agent, not an independent re-proof, not Lean certification, and not an assertion that these simple deductions are new to the literature.

## Remaining gates, and approaches tried

- K positivity → plethysm/GCT: tried sign rebasing, associated-graded LR identification, and dilation transport. The first two give B3.1; the third fails by B3.2. Next required step is a specific coefficient-identifying map, with boundary extension control, for the actual GCT representations.
- Grothendieck inequality → multiplicity positivity: tried zero-preserving norm realization and constant-factor recovery. B4.1 reduces the former to explicit construction of the matrix; B4.2 rules out generic exact recovery from the stated guarantee alone. Next required step is a gap-preserving, succinct reduction to a nonzero threshold.
- Projective/nuclear norm → full GL orbit separation: tried absolute and Frobenius-normalized norm thresholds; B5.1/B5.3 disprove invariant/uniform-gap uses. B5.2 identifies the valid contraction model. Next required step is an invariant normalization or quantitative reduction respecting unbounded GL operations.
- Integral foundations → GCT obstruction: proved fixed-witness spread B7.1 and bounded-degree modular criterion B7.2. A reverse transfer without a good-prime certificate fails by B7.3. Next step is a polynomial-size representation of the orbit-pullback matrices and effective sufficient degree bounds uniform in determinant/permanent size; representability of Hilbert/Quot alone supplies neither.
