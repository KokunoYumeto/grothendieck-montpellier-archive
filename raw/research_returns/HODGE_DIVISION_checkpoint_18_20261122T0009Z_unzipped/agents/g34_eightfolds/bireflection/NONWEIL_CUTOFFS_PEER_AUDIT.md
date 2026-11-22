# Independent whole-proof audit of D-UNW-01–03 and D-LNW-01

**Verdict: PASS, with exactly the stated large-natural-dimension and source hypotheses.**

Reviewer: `/root/g34_eightfolds`, GPT-6 Astra Pro, effort inherited/unexposed, HODGE_DIVISION. Actual clock record: **2026-11-21 20:13:34 UTC**. All complete proof/source/code readings and the independent constant computation below were finished before this timestamp.

The whole final `agents/imprimitive/unitary_nonweil/unitary_nonweil_section.tex` was read, SHA-256 `10addbba497f6f924fb5925732fec27a6ca59308b4abe473220cdf0aac4d76c9`, and the whole `linear_nonweil_section.tex`, SHA-256 `8f66c40c4bb8c1e2f086ec1dcdc991afcfaad418924a4cf3c68f5af884fabea2`. Both complete author constant checkers were read. The three missing display closings in the initial unitary file were repaired by the author; this was a source-integrity correction with no mathematical change. The reviewed final files have balanced display and theorem environments. They have not been compiled.

## 1. The published uniform exponent and its exact domain

I freshly read the full Larsen–Tiep accepted-author Theorem4.4 and its proof on numbered pages19–20, and Theorem5.5 with its full proof on pages25–26. I also read the natural-space/group conventions on page4 and the support definition in the introduction. The theorem includes SL(V), SU(V), and the other stated classical groups; in the unitary case the natural module is over the quadratic field but n is its dimension, exactly as used in the new proof. It is an all-element ordinary-character theorem, not only a semisimple or large-support estimate.

The explicit source constant is 1/(6507 times 2^21 times 10^18), obtained from the stated C and gamma. The displayed constant and the complete final minimum expression on author page26 were visually inspected in the retained rendered page. My independent integer square-root calculation reconstructs this constant and verifies that it exceeds seven times 10^-29. Using the smaller 10^-29 is valid.

The Annals publisher record was independently reopened and confirms the title, authors, volume200 (2024), pages1–70, DOI10.4007/annals.2024.200.1.1, acceptance on12March2024, and online publication on3July2024. The proof actually read is the complete accepted-author PDF, not an unverified claim of reading the journal typesetting. Its retained hash is `70d2546d2a0f01f8e701aa718201216f2b334b6cd074c12b41c2c59e0b7cdd4f`.

## 2. Character levels, special-group restriction, and the unitary endpoint

I freshly read the published GLT2020 Definition2, the full Lemma7.1 proof on pages51–52, Theorem7.3 and proof on page52, the whole unitary dual-pair section8.3 on pages65–67, and the complete Corollary8.6 proof on pages67–68. The publisher PDF was independently reopened; its hash is `0726271e666bd5eb736ff91ea031ef83bb072f2e10f27b664c217d7702926c32`.

The level of an SU character is independent of the GU character chosen above it. At level below n/2, the relevant GU character restricts irreducibly and determinant twists select exactly one true-level representative. Thus the low-level estimate concerns the actual same-degree SU character; no unproved extension to a larger group is assumed. The true-level identification with D_alpha^circle and its exhaustion are justified by the complete section8.3 argument.

The exact equations(8.17)–(8.18), including the square-root tail and the order bound, are correctly transcribed in UNW.5. The even-q range is essential: the proof explicitly obtains positivity, irreducibility, and exhaustion from the inequality j^2+j at most n-1 without assuming q odd. The preceding odd-q-only Corollary8.5 is not used outside its domain. Consequently q=2, j=2 is covered by the exact source estimate. The lower degree constant is 1/[2(q+1)], not 1/(2q)+1 or another parsing of the compact source typography.

## 3. The two quantitative regimes

The coarse degree floors follow from the published inequalities by the valid estimates 2(q+1) at most q^3 and q+1 at most q^2. I checked the exponent decompositions for j at most n/2 and at least n/2, including their overlap. For j greater than 10^30, the minimum of j and n/2 is still at least 10^30. A noncentral natural operator has support at least one. The uniform source theorem therefore gives a ratio at most 2^(-5/2), which is strictly below one quarter.

For two at most j at most 10^30, n at least 10^61 ensures both the source's true-level range and n-j^2 at least eight. The normalizations of all three terms in the exact numerator and denominator are correct. With u=q^(j^2-n), the unitary total error is bounded by 2u+10u^2. Its maximum at u=1/256 is exactly 261/32768, below one hundredth. The resulting relaxed ratio is 26/99, below 4/15. The denominator is positive. The proof uses j at least two in both the q^-j term and the middle-term exponent, so it does not silently apply this bound to Weil level one.

The degree separation also checks: all levels at least two have degree strictly greater than q^n at this range, while level one has degree at most q^n. Level zero is trivial by the published level definition. This separation is sufficient for the later transitivity argument and does not require proving that an arbitrary outer automorphism preserves level.

## 4. The linear companion

I freshly read the entire published general-linear dual-pair section8.1, pages55–61, including the geometric full-rank orbit argument, its multiplicity-one true-level constituent, Lemma8.2 and its proof, and the exact tail estimates(8.9)–(8.11). The linear proof correctly uses this stronger exact display rather than the weaker numerical1.76 corollary. Corollary8.6 supplies the same-degree SL-to-GL extension at low level.

The linear tail is bounded by 3q^(j^2), and the group order by q^(j^2). The normalized total error is at most four times q^(2j^2-n). The common cutoff satisfies n at least 2J^2+9, so this error is at most 1/128. The ratio is exactly 33/127, below 26/99 and 4/15. The high-level estimate and degree separation use weaker common bounds that are indeed implied by the sharper linear degree denominator q-1. The identification of level one with the linear Weil characters is explicitly present on source page61.

## 5. All compatible normalizers and tensor permutations

The full-normalizer commutator argument is sound and has no hidden outer-stabilizer assumption. An irreducible finite core has scalar commutant, so every nonscalar normalizer fails to commute with some core element. The resulting commutator lies in the core image. A nonidentity scalar commutator has full ordinary moving rank. Otherwise the 4/15 character bound and the unitary eigenvalue trace inequality give ordinary moving rank at least 11a/30. The rank commutator estimate is at most twice the projective support of the original normalizer. Hence the stated 11a/60 bound follows, including arbitrary represented central quotients.

Factorwise eigenvalue multiplicities are convolutions, so any nonscalar factor transmits its bound to the tensor product. The weighted factor-permutation argument is also complete: tensor conjugation reduces each cycle to a shift with one diagonalizable return operator; each basis-word orbit contributes at most one dimension to a prescribed eigenspace. At most a constant words and the remaining orbits of length at least two give support at least one quarter on that cycle. This exceeds 11/60. No factor-character field, selfduality, or scalar normalization of an individual outer involution is needed.

## 6. The actual source constraint and exact final scope

The proof uses the previously established actual intermediate-cover VHS/Hurwitz factorization, not an inequality of ambient dimensions as a sufficiency test. Its coefficient multiplicity is six with signature(3,3), and the Euler identity is 6=2e(h-1)+D. Each coefficient-trivial inertia is removed before counting genuine marked points. If h is at least two, e greater than thirty is already impossible; at h=1 the period variation factors through pointed-curve moduli of dimension at most six. Rank nine therefore requires h=0, at least twelve genuine inertia points, and D=2e+6.

Every nonidentity scalar contributes e to D; every nonscalar contributes at least 11e/60. Thus e is at most thirty, contradicting the factor degree lower bound. The mixed-core theorem correctly requires every factor to satisfy the displayed large-rank non-Weil hypotheses. It does not include an arbitrary additional small factor.

In the primitive factorwise tensor-indecomposable case, D-BI19 gives transitive isomorphic simple factors. The complete HHM exceptional multiplier list, freshly reread on numbered page35 together with the ordinary-cover discussion on page4, contains no parameter near the enormous cutoff. Hence all factor characters lift to SU or SL. Transitivity equalizes degrees, and the strict degree separation makes all factors Weil or all non-Weil. The former alternative is removed by the previously proved D-BI24 or D-BI23 in its checked scope. This establishes n<10^61. The additional q at most27 conclusion invokes D-BI20 only with its original nonsplit and primitive-core hypotheses. A finite remaining group list is a reduction, not an executed classification or an existence theorem.

## 7. Independent certificate and source integrity

`audit_nonweil_cutoffs.py` imports no author arithmetic. The actual run passed in **0.12435889100015629 seconds**, producing `audit_nonweil_cutoffs.json`. It independently reconstructs the published minimum constant, both cutoff margins, the high-level exponent, all normalized low-level exponents, monotone error functions, the exact unitary ratio8453/32507, the relaxed26/99 and linear33/127 ratios, the normalizer support11/60, and the total-degree ceiling30. Universal exponent inequalities are checked by symbolic polynomial decompositions and nonnegative translated coefficients, not by enumerating ranks up to10^61. The final proof/source hashes and balanced TeX delimiters are checked. No compilation is claimed.

The primary sources actually reopened/read are:

- Larsen–Tiep, accepted author version https://arxiv.org/pdf/2403.09046, full Theorems4.4/5.5 proofs at numbered19–20 and25–26; independently verified publisher record https://annals.math.princeton.edu/2024/200-1/p01.
- GLT2020, complete published PDF https://www.cambridge.org/core/services/aop-cambridge-core/content/view/77A6CCCB36F94337FD1DAA7F67B40379/S205050861900009Xa.pdf/character_levels_and_character_bounds.pdf, full invoked sections and exact page locators above.
- HHM, retained complete original author text, ordinary-cover discussion p4 and complete exceptional multiplier list p35; its published classification is used, not newly reconstructed.

The cited published character estimates are inputs. This audit does not claim a new proof of every classification or counting theorem used inside those publications. No defect was found in either frozen new proof.
