# Fresh independent review of the F28 rectangular hook note

Reviewer: `/root/gct_statements`, GPT-6 Astra Pro; effort inherited/not exposed. Date/time: 2026-11-21 00:08 UTC. Review type: complete direct textual/full-proof review, with independent reconstruction of the hook-multiplicity and effective-orbit obstruction. No formal proof assistant or numerical approximation was used.

Reviewed file: `agent_rectangular_hook_gate.md`.

SHA-256 at review: `74d5fd6685b080bc40b12f54a666c1b64f72eaca7d06499084c310578187e1c8`.

**Outcome: PASS. No mathematical blocker or necessary correction was found in the reviewed note.**

## 1. Primary source match

I read the local primary text `primary_sources/Manivel_0809_3710.txt` directly at Theorem 1 and its immediate introductory conventions. The theorem is exactly the multiplicity-free square of the height-two rectangle, with all-even partitions of length at most four and all-odd partitions of length exactly four. The note's use of `d` in place of the paper's `n` is consistent. The source explicitly explains that transposing both rectangles has the same square decomposition because the two sign twists cancel.

I also read the conclusion of the supplied proof in §3: its four invariant-generator weights on the last factor are `(1111),(2),(22),(222)`, and it translates their nonnegative span into the theorem. I did not independently re-prove the entire invariant-theoretic theorem. The note correctly treats RH1 as a cited established result rather than a newly verified external proof.

The source label and printed-page claim used in the note agree with the local extracted PDF text: Theorem 1 is on printed p.1, and the proof is in §3, printed pp.3–4.

## 2. Parity translation and exact point model

For a partition `nu` padded by zeros to four parts, common even parity is exactly the first source case; common odd parity forces all four entries nonzero and is exactly the second source case. Thus RH2 follows with no extra partitions or missing boundary cases. For length greater than four the coefficient vanishes.

The affine point in RH3 is integral exactly when the three differences `nu_i−nu_4` are even. Dilation by `N` tests the three differences after stretching, so RH4 follows from RH2 applied to the partition `N nu` and the rectangle `(Nd,Nd)`. The implicit input condition remains `|nu|=2d`, as fixed in RH1/RH2. Stretching preserves that condition and preserves positive-part length.

The exact model has fixed dimension three, denominator at most two, and six rational linear inequalities if the three equations are written as pairs of inequalities. Membership/separation at a rational point uses ordinary exact rational comparison with coefficients of polynomial bitlength. This is a valid restricted-family model, not an assertion of general PH1. Choosing the empty polytope for length greater than four is consistent under all positive dilations.

## 3. Independent reconstruction of RH5

For a Young subgroup with `r` nonempty blocks, the natural permutation module restricts as the direct sum of the `r` block permutation modules. Splitting a constant line from each and removing the global constant line gives

`Res U_n = (direct sum_i U_(a_i)) ⊕ 1^(r−1)`.

The exterior algebra of a direct sum is the graded tensor product. In `Lambda^j U_a`, the hook representation `(a−j,1^j)` is trivial only in degree zero and sign only in degree `a−1`, with these two cases coinciding only for `a=1`. Therefore the character prescribed on nonsingleton factors forces total degree

`s=sum_(sign factors)(a_i−1)`.

The residual exterior degree comes solely from the trivial `(r−1)`-space, contributing `binom(r−1,k−s)`. Frobenius reciprocity gives exactly RH5. The report's brief derivation of `Lambda^j U_a` from the oriented-subset induced module and Pieri also checks: the two adjacent hooks and the induction on `j` have the correct shapes, including the endpoints `j=1` and `j=a−1`.

The valid degree interval is indeed contained in `0,...,n−1` because `s≤n−r`. Singleton blocks contribute zero to `s` under either label, so no spurious second choice is introduced. Empty exterior powers have dimension one, as used in the binomial coefficient.

## 4. Effective Young-orbit obstruction

RH1 allows hook degrees exactly `0` and `3` when `n=2d≥4`. Degree zero gives `(n)`; degree three gives `(n−3,1,1,1)`, whose first part is positive and odd. No hook with a trailing one can be all-even, and exactly four odd parts force degree three.

Every proper Young subgroup has at least two nonempty blocks. RH5 then supplies a nonempty interval of at least two consecutive hook degrees in its induced one-dimensional-character module. Since `{0,3}` has no consecutive pair, that orbit module has an irreducible constituent absent from the rectangle square. In a direct sum of actual orbit modules there is no cancellation of irreducible multiplicities. This establishes the obstruction independently of any signed trace argument.

The only remaining Young subgroup is the whole symmetric group, which gives a one-dimensional trivial or sign orbit module. The constituent `(2d−2,2)` is present by RH1 and is neither trivial nor sign for every `d≥2`. This completes the contradiction even in the boundary case `d=2`, where the degree-three hook itself is sign.

Allowing arbitrary scalar phases rather than just signs does not evade this reasoning while stabilizers remain Young: over characteristic zero every one-dimensional character of each `S_a` is trivial or sign, with the singleton factor trivial. The note correctly limits this conclusion to these stabilizers, not arbitrary subgroups.

## 5. Small constructive counter-scope model

The three pairings of four letters form an `S_4` orbit with permutation character `(3,1,3,0,1)` on the five stated conjugacy classes. Adding sign `(1,−1,1,1,−1)` gives `(4,0,4,1,0)`, the square of the character `(2,0,2,−1,0)` of `(2,2)`. Hence RH9 is an actual characteristic-zero representation isomorphism, not just a dimension equality.

The stabilizer has order eight and is `S_2 wr S_2`. The complete list of Young-subgroup orders for `S_4`, from the five partitions of four, is `24,6,4,2,1`; thus the stabilizer is genuinely outside the excluded class. The sign line is a second signed orbit with whole-group stabilizer. The example precisely demonstrates the claimed scope of RH-Y without claiming a designated geometric component basis.

## 6. Check-event wording

Suggested event: `F28-REPORT-INDEPENDENT-74d5fd66`, full direct read and independent proof reconstruction, PASS. External Manivel Theorem 1 was source-matched and cited, not fully re-proved. The hook lemma, parity/point consequences, effective obstruction and small signed model were checked in full. No Lean/kernel check is claimed. A later generated paper statement/proof still needs its own final-text match if it differs from this report.

## 7. Further proposal check: all nontrivial rectangle squares

After the reviewed note, the parent and `/root/rectangular_and_theta` proposed extending the signed-Young-orbit obstruction from height two to every rectangle `(a^b)` with `a,b≥2`. I independently checked that proposal in full; **PASS**, with the separate size-four case retained.

I directly read the supplied IP source `sources/LIT_Ikenmeyer_Panova_rectangular_Kronecker_plethysm/main.tex`, its complete hook generating-function proposition and proof around source lines 1377–1427. The proposition states

`sum_k g((ab−k,1^k),(a^b),(a^b)) t^k = product_(i=2)^min(a,b)(1+t^(2i−1))`.

The source proof uses Littlewood's identity, complementary partitions in a rectangle, self-conjugate partitions and distinct odd parts. The exact displayed statement yields coefficient zero at hook degrees two and four, and coefficient one at degree three, whenever `min(a,b)≥2`. The proposition is the one the other agent identifies as IP Proposition 6.4; the complete algebraic statement, rather than that number alone, was checked directly here.

For area `ab≥6`, hook degree three is internal: it is neither zero nor `ab−1`. Any effective Young orbit contributing the degree-three hook has the consecutive hook interval from RH5. An interval of length at least two containing three also contains two or four, forbidden in the target. Hence the interval must have length one, so the Young subgroup has one block and is the whole symmetric group. Its one-dimensional trivial/sign character contributes only hook degree zero or `ab−1`, again impossible. This proves the obstruction for every such rectangle.

The only rectangle with `a,b≥2` and area below six has area four and shape `(2,2)`. The already reviewed height-two argument excludes it using the extra `(2,2)` constituent, while the degree-three hook itself is sign and alone would not yield the larger-area contradiction.

This is a proposal-level supplement, not yet a hash match to the other agent's forthcoming revised/supplemental file. Its exact source-derived isolated-hook argument and all edge cases were independently checked. The same scope restriction to effective sums and Young stabilizers remains necessary.

## 8. Final standalone generalized-report match

On 2026-11-21 UTC I read the complete standalone generalized report `agent_rectangular_hook_gate_general.md`, SHA-256 `3ab52cad173ae4f9d48513d010652cd7fbb1a7f1f2b51c215b173970257b5e48`. This check covers every section, including IH1–IH5, the size-four edge, and the last section identifying the actual rectangular Schur–Weyl multiplicity module. **PASS; no necessary correction.**

The general isolated-hook lemma is valid for every internal hook degree `1≤k≤N−2`: an interval of at least two consecutive integers containing `k` must contain a neighbor, while a one-block Young orbit supplies only the two endpoint hook degrees. The conversion of a scalar-monomial orbit to `Ind_H chi` uses the label stabilizer, so it does not mistakenly require the chosen vector itself to be fixed. The stated induced-module map has the correct relation for its one-dimensional character. Arbitrary characteristic-zero scalar phases introduce no additional Young-factor characters.

I re-read the full supplied IP proposition and proof at source lines 1377–1427 while matching this version. The theorem's use here is exact: the source height parameter is the smaller side, and transposing both Specht factors cancels the two sign twists. I independently rechecked all low hook degrees and the size-four exception. The proof does not require the stronger and false assertion that the whole hook support is gap-separated.

For the actual-module statement, characteristic-zero Schur–Weyl duality decomposes `U^{tensor N}` into the `GL(U)` Schur modules tensored with Specht modules. With `dim U=b`, the only summand isomorphic to `det^a U` is the rectangle `(a^b)`, with multiplicity module that rectangle's Specht module; the same holds for `V`. The shuffle isomorphism `(U tensor V)^{tensor N}=U^{tensor N} tensor V^{tensor N}` turns the original symmetric-group permutation into the diagonal action. Taking the stated product-group Hom therefore gives exactly the tensor square of the rectangular Specht module. This is an equivariant module identification, not merely equality of dimensions or of one coefficient.

Suggested new check event: `F28-GENERAL-REPORT-INDEPENDENT-3ab52cad`, full direct text match, independent complete proof reconstruction, source match of the supplied IP statement/proof, PASS. This event supersedes only the earlier report's height-two scope; it does not erase that earlier historical check. No formal-kernel check, general geometric nonexistence statement, or automatic check of a separately generated paper version is claimed.

## 9. Generated F28 paper text and the positive height-two model

I subsequently read the full generated F28 in `GCT_NSRH.tex`, from its statement through the final paragraph on the height-two invariant monomial model, and saved that exact excerpt as `audit_snapshots/F28_gct_review.tex`, SHA-256 `95babcb51309f16f4e71e1b1a4eca259e7f6e4119b260f7c170023394ffc3eb9`. **PASS**: the theorem/proof matches the standalone general report, including both neighboring-hook zeros, the characteristic-zero scalar-character classification, the effective-cone qualification, the size-four edge, and the actual Schur–Weyl module.

I also freshly read Manivel's complete §2 setup and §3 proof from the local primary text, including the open-orbit argument and all four boundary-generator descriptions. The generated paper uses exactly the polynomial invariant algebra displayed at the end of §3, with the source's dual-polynomial convention acknowledged. Its generator weights on the last factor are `(1111),(2),(22),(222)`, with degrees `4,2,4,6`, and the determinant exponents on each of the first two factors are `2,1,2,3`. Solving the four triangular weight equations gives precisely the displayed `a_1,...,a_4`; the point coordinates are the displayed unimodular triangular change from `a_2,a_3,a_4`. Thus this is an exact exponent rule for the known family, not a point selected after testing positivity. The support-length and denominator-two stretching edge cases remain correct. The paper properly distinguishes this highest-weight monomial model from a monomial action on the entire rectangular Specht tensor square.

This check includes direct source matching of that established invariant-algebra statement and independent verification of all exponent/point deductions. It does not claim an independent new proof of Brion's invariant-theoretic theorem used by Manivel, and it does not infer a general rectangular formula.
