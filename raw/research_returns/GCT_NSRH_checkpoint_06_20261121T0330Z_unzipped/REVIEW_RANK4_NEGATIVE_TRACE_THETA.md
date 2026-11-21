# F57 — independent whole-proof and primary-source review

Reviewer: /root/rectangular_and_theta, GPT-6 Astra Pro. Reasoning-effort setting is not exposed. Review completed 2026-11-21 at approximately 03:25 UTC.

**Verdict: PASS.** No mathematical correction is required. This is an independent reconstruction and a complete text review, supported by exact symbolic arithmetic and a visual inspection of the primary source. It is not a proof-assistant certification. The source's generic representation classification is used as a cited theorem; this review does not reprove that classification.

## 1. Exact versions and scope

The complete report reviewed is:

- agent_rank4_negative_trace.md — SHA256 d22b8faf7f5616686c736e26bd28b320766ad7b823574e0a4693cf0a2d465778.

The exact certificate was read completely and rerun successfully:

- verify_rank4_negative_trace.py — SHA256 38675f81b97955ca9d1d7f7bfe80eb342aceb8194d2ded23749765355c370d9c.
- verify_rank4_negative_trace_output.txt — SHA256 265731353041b3579a9456f0407ae9574df8ce182b47ba7fa8d14e0c46a411d8.

The complete initial report was reconstructed before its final precision deltas. The final text was subsequently read in full. The deltas comprise the accurate finite-search stopping counts, the source exponent-convention warning, and the parity/Tate-shift consequence. Each delta is checked below.

The review covers every mathematical paragraph in sections 1–7, including the matrix transcription, all multiplication formulas, the actual module identification, tensor occurrence, each obstruction and its limitations, and the stated finite-search evidence. It does not yet certify a generated LaTeX fragment; that requires a separate final-text match.

## 2. Primary-source inspection

Primary source: Blasiak–Mulmuley–Sohoni, GCT IV, arXiv:cs/0703110 v4, 6 June 2013.

The reviewer downloaded and inspected the actual PDF:

- primary_sources/GCT_IV_cs_0703110v4.pdf — SHA256 cc28f69ca06c0c5e43c30b2cf801a1134712a596c87e74bff2ade1c49fb41638.
- Original URL: https://arxiv.org/pdf/cs/0703110.
- The file has 145 pages.
- The actual rendered image of printed page 135 was inspected at primary_sources/IV_page135_figures21_22.png. This was a local PDF rendering and an actual image inspection, not reliance on a search-result caption or OCR alone.

The supplied TeX is sources/LIT_Mulmuley_GCT_IV_nonstandard_quantum_group_Kronecker/Apr13KroneckerGCT4.tex. The reviewer read the complete relevant contexts, including the Figure 22 source, the dual definitions and propositions, the rank-four generic classification, the ordinary/nonstandard tensor comparison, the two-row quotient, and the rank-four basis example.

The important matched locators are:

| Mathematical input | Primary locator | Review result |
|---|---|---|
| Q_i=D−P_i | §11.1, p.59 | Confirmed. |
| Θ(P_i)=Q_i | Proposition 11.6, p.60 | Confirmed with the ordinary-factor twist interpretation. |
| The # contragredient | §11.4, pp.62–63 | Confirmed that it uses Θ^op, not the plain vector-space dual action. |
| Specht # dual conjugates the partition | Proposition 11.11, p.63 | Confirmed. |
| Tensor # conjugates one factor | Proposition 11.12, p.63, (101), (105), (108) | Confirmed, including the diamond self-duality needed for the optional twist formulation. |
| Trace-free symmetric direct summand | §11.4, (98)–(100), p.63 | Confirmed. The generic-field restriction avoids an unproved integral direct-sum assertion. |
| Nine generic full-algebra simples | §11.8, p.67 | Confirmed that both five-dimensional modules occur and are distinct. |
| Actual tensor action by restriction | Theorem 12.1, p.68, and §12.2 | Confirmed, with the source's X/X* convention warning retained. |
| Omission from the two-row quotient | Theorem 13.4, pp.74–75, (124) | Confirmed: the extra five-dimensional # dual is absent. |
| Actual five-dimensional graph | Figure 22, p.135; TeX lines 8146–8179 | Every descent label and directed edge was checked against the rendered figure. |
| Already constructed rank-four tensor basis | Introduction §1.5, p.13; Example 19.3, pp.133–135 | Confirmed. The report does not call this construction unknown. |
| Signed/factored coefficient scope | Remark 11.19, p.67; Theorem 17.7 and Example 17.8, pp.121–122 | Confirmed, including the existing divided-power coefficient v^10−v^4−v^−4+v^−10. |
| Remaining algebra-basis problem | §19.1, p.136 | Confirmed that the separate rank-four Temperley–Lieb algebra basis problem is not conflated with Example 19.3. |

The preliminary exponent inconsistency between §3.1 and §11.1 is genuinely irrelevant to the new calculation once the explicit Figure 22 action and P+Q=D are fixed. The independently verified relation Q_i²=DQ_i checks the convention actually used. This editorial normalization issue is not presented as a failure of the source's mathematics.

## 3. Independent reconstruction of the exact trace

The reviewer first transcribed the Figure 22 matrices directly from the image, using the state order (v_2,v_13,v_1,v_22,v_3) and the right-row convention. The diagonal D entries are exactly at the displayed descents {2},{1,3},{1},{2},{3}. All off-diagonal entries, including both c=D−4 arrows, the −a arrow, and the −2 arrow, match the source.

Before reading the author's complete multiplication proof, the reviewer entered the three matrices independently into an exact SymPy computation. That computation produced the same polynomial

\[
-D^9+20D^8-163D^7+734D^6-2048D^5+
3712D^4-4352D^3+3072D^2-1024D.
\]

It also produced the exact specialization

\[
-\frac{99834597608550400}{387420489}
\]

at v=3. These are exact rational/polynomial calculations, not floating-point tests.

The subsequent written-proof check reconstructed the rank-one compression:

\[
Q_1Q_3=
(-2\delta a,D^2,-\delta D,-\delta a,-\delta D)^t
(0,1,0,0,0).
\]

Rotating the eleven-letter word at its adjacent Q_1Q_3 yields precisely the nine-factor A displayed in the report. Multiplication of its second row gives the claimed r_1 and r_4, and the scalar contraction is −δa(2r_1+r_4). Its factored and expanded expressions agree. The five full-product diagonal entries also agree; only the first and fourth are nonzero. The final exact script explicitly asserts all five entries, rather than merely printing them.

The complete Laurent expansion was checked. In particular the coefficient of each of v^18 and v^−18 is −1, since −D^9 supplies these extreme terms and all other terms have Laurent degree at most 16. There is also a positive constant coefficient 668. Thus the polynomial has both signs; no overall sign change makes it effective.

The quadratic, far-commutation, and adjacent degree-five relations are checked as consistency tests only. The report correctly obtains the module identification from the source and does not misrepresent these necessary relations as a full presentation of the rank-four algebra.

## 4. Dual action and occurrence in the actual tensor power

For the right-row matrices, the Θ^op contragredient has P_i matrix Q_i^t. Consequently the reversed P-word 23232312121 has matrix equal to the transpose of the original Q-word matrix. The stated word reversal is exactly correct. Trace is unchanged.

The source decomposition gives

\[
N=S'\check M_{(3,1)}
\subset S^2M_{(3,1)}
\subset M_{(3,1)}\otimes M_{(3,1)}
\]

as a generic direct summand. Applying # and the cited tensor-dual identities puts N# into the restriction of M_(2,1,1)⊗M_(3,1). This is an actual restricted ordinary Hecke module. Ordinary quantum Schur–Weyl duality therefore puts it in the nonstandard tensor power once the two dimensions are at least 3 and 2, respectively.

For the concrete dimensions (3,2), the ordinary highest-weight factors have dimensions 3 and 3. The relevant Specht tensor product has dimension 9 and contains the five-dimensional N# with multiplicity exactly one: existence is proved by the summand argument, and two copies would already require dimension 10. Hence the ordinary isotypic component has nine copies. The report only needs existence, so even this count is not an essential input to the obstruction.

The source's X/X* convention is handled correctly: a consistent transpose changes word order but leaves an appropriate trace with the same polynomial. No claim that the v=3 specialization remains irreducible is made or needed.

## 5. Each obstruction and its boundary

### Effective matrices and kernels

An entrywise nonnegative Laurent matrix product has an entrywise nonnegative Laurent trace. Since trace is invariant under simultaneous similarity, the negative coefficient excludes every basis with effective P_i matrices on this specified N# module. Extending the coefficient field does not change this argument.

The same reasoning applies to finite graded-vector-space matrix kernels whose split Grothendieck action is this module. It applies to a larger tensor representation only when an effective projector onto the specified summand is additionally retained. That condition is correctly stated as extra data: an abstract direct summand of a positive matrix representation need not have an effective projector in the chosen positive basis.

The negative numerical trace at v=3 also excludes a simultaneous entrywise nonnegative real basis for the displayed specialized module. It is unnecessary to know whether that specialization is simple.

### Genuine finite power traces, signs, and twists

After v=q^(n/2), the Laurent expression is a finite power sum in pairwise distinct positive roots q^(e/2). The extreme root q^9 has coefficient −1. A genuine finite-dimensional invertible endomorphism has a power trace with nonnegative integral multiplicities after equal eigenvalues are grouped. Jordan blocks do not change that statement.

Subtracting the two expressions and applying finite Vandermonde independence proves the contradiction, even if equality is assumed only for all sufficiently large n. The proof works equally with inverse grading. It does not require weights, semisimplicity, purity, or a geometric realization theorem.

The final parity paragraph is correct: p has a negative extreme coefficient, and −p has a negative constant coefficient. Neither can be a genuine finite power trace. A common Tate twist rescales all roots by the same nonzero scalar and preserves their distinctness and signed coefficients. It cannot repair the obstruction.

These conclusions do not exclude a virtual/alternating trace over several degrees, an inserted-operator trace, or a geometric interpretation without the stated parameter-to-grading comparison.

### Two-row and canonical-basis scope

The obstruction is to a P-word on the extra full-algebra N# block. The source's two-row quotient omits this block. On N itself, the computed negative word uses Q generators, and Q=D−P involves subtraction. Thus no conclusion about P-only positivity of the two-row tensor power follows.

The result does not contradict the source's signed/factored positivity, Example 19.3, or the source's compatibility formulation of a canonical tensor basis. It excludes the stronger strict effective-kernel proposal on the specified actual simple.

## 6. Finite evidence and review honesty

The exploratory helper was read, including the necessary-relation tests and the word-generation/search limits. Its logs support the precise corrected record:

- The no-adjacent-repeat enumeration through length 9 contains 1533 words per system.
- Each of 6P, 6Q and 5P completed 200 seeded tests with seed 562104 and length at most 30.
- The 5Q seeded search stopped at its thirteenth test.
- The short search tested 3069 words through length 10 and then 32 additional length-11 words before its first recorded negative example.

These observations are not used as proofs of positivity or global minimality. The Figure 21 four-edge cycle has a negative product for real v>1, which obstructs diagonal rescaling of that displayed basis only. The report correctly separates it from the basis-independent five-dimensional trace obstruction.

The complete final text is mathematically sound. The classification and source constructions remain cited inputs; the trace identity and its scoped consequences are independently checked deductions. No novelty claim about the earlier divided-power counterexample or the source's rank-four construction is supported or made.

## 7. Check-event summary

1. **Source verification:** original PDF and supplied TeX contexts read; actual Figure 22 rendered and visually transcribed; exact numbered locators matched.
2. **Independent exact reconstruction:** the matrices and negative trace were independently computed before the author's product proof was read.
3. **Whole-proof check:** every report section read; product compression, contragredient, tensor occurrence, all obstructions and their limits reconstructed.
4. **Certificate rerun:** final exact script read and rerun successfully, including every diagonal entry and the explicit dual word.
5. **Final deltas:** accurate search counts, the normalization warning, and the parity/Tate-shift extension all checked.
6. **Result:** PASS for report d22b8faf… and certificate 38675f81…. Final generated-fragment matching remains a separate event.

## 8. Complete final-fragment match

At approximately 03:29 UTC on 2026-11-21, the reviewer read the entire generated fragment finding_F57.tex, SHA256 c37c7ffa6a62016df69f3d24cbd9c7052d06c2587564985d9493d8a392d4af7a, and matched every formula and proof to the reviewed report. **Final-text PASS.**

The fragment retains the full source matrix transcription, rank-one and diagonal product certificates, Θ^op word reversal, actual tensor occurrence, generic/full-algebra versus two-row distinction, effective-projector premise, and the finite ordinary-trace/parity/Tate-twist scope.

The only mathematical addition is the explicit bounded two-parity Tate witness. This was checked directly: the positive multiplicities are (657,476,297,176,67,36,4,2), whose sum is 1715, giving dim E_+=668+2·1715=4098. The two odd lines Q_l(-9) and Q_l(9) have Euler contribution −q^(9n)−q^(−9n), and every positive even line supplies exactly the corresponding term of the Laurent expansion. Thus E_+ ⊕ E_-[-1] realizes the scalar sequence for all extension degrees. The fragment correctly makes no claim of original-action coherence or relation maps for this scalar witness.

The separate dictionary correctly distinguishes the effective torus-character cone from the noncommutative word algebra and a virtual bounded coefficient complex from an effective object. The previously audited EGA/SGA framework locators are retained as background; this final-match event does not claim a new inspection of every archive leaf.

No correction is required.


