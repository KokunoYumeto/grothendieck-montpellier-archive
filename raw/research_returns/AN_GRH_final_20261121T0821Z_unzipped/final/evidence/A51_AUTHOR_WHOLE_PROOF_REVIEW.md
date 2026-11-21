# A51 author whole-proof and known-input review

Date: 2026-11-21. Author/reader: GPT-6 Astra Pro, AN_GRH `/root/row_audit`. Effort is not exposed.

## Exact source and outcome

**PASS, targeted proof check.** The complete seven-part proof was read at source SHA256 `1fea58c0efdc3308983cdf82526b028bdddde4946df24d1044eda0e654d16852`. Four displays were then split across lines without changing their mathematics. That narrow final delta was checked. The final source is

`work/row_audit/A51_NORM_COMPATIBILITY_AND_TOWERS.tex`

SHA256 `ba76d8eba6a85ec3f81441dcf719d6565debcc38332507c3acedd1898d4a9fd2`.

New bibliography entries are in `work/row_audit/A51_BIB.tex`, SHA256 `30613a652ad51eba1e3bb166164873b79b714ea5727168096b01a4b4a3acb25a`.

This is an author whole-proof reading plus a checked layout-only delta. It is not an independent re-proof, proof-assistant verification, numerical certificate, PDF build, or universal witness-gate improvement. The frozen final paper was not modified.

## Checked mathematical content

1. The actual norm map has the p-primary section d^{-1}h*. Its direct-sum decomposition gives the exact lcm order formula. It does not assert arbitrary realization of the new summand by two points.
2. A rational principal divisor descends its function by the scalar Hilbert90 argument. Exact p-power order excludes an inseparable function. The norm formula uses residue degree one at the specified points. The explicit norm-one rational-function example has simple zero/pole; its ramification and common image are identified, so it is not misrepresented as an allowed pointed-cover counterexample.
3. The whole two fibres are rational only under the constant-deck hypothesis. Counting the zero, pole and q−1 remaining rational fibres proves the displayed lower bound, with the ceiling. No infinite fixed-field tower is asserted.
4. Coprime Galois degrees imply the common fibre product is geometrically connected. The integral trace times the actual primitive projector vanishes, so both proper-quotient norms kill the faithful p-primary component. The remaining constraint of representation by compatible point differences is retained explicitly.
5. The quotient is assumed to exist. Its multiplier is a Weil eigenvalue, hence not a root of unity. The odd-ell binomial valuation calculation proves the exact formula for the minimal deck constantization degree.
6. A45 supplies the already-proved unrestricted integral descent. Freeness of the full product algebra over the invariant product of DVRs gives exact cardinality, rational generator-rank, and exponent identities. The prime-power genus difference gives the actual primitive dimension; the p-rank bound then gives the displayed uniform rational generator bound. The O_r/p^e example is explicitly abstract and has arbitrary exponent while satisfying the same semilinear identities.
7. The direct-sum example is also explicitly abstract. Its action is continuous, and the unit test for Z^{ell^m}−1 proves the exact finite invariant groups for every open subgroup. The proof claims no Jacobian or compatible point-divisor realization.

The final paragraph records only the limit of these deductions. It does not turn a bounded source search into a nonexistence theorem or state that a different compatibility argument is impossible.

## Known inputs directly checked for this conversion

- Recovered A1 A.31, complete statement/proof, retained paper lines1653–1700. Only the covering implication, independent uniqueness and compatibility are used; its concluding appeal to A1 is not reused as a new proof.
- Stacks Project Theorem59.24.1, Tag03P8, complete statement and displayed proof. Applied over a field to the scalar descent cocycle. Primary URL: https://stacks.math.columbia.edu/tag/03P8 ; retrieval `turn571368987view1`.
- Stacks Project Lemma42.18.1, Tag02RT, complete statement and displayed proof. Its divisor-of-norm formula has exactly the proper finite integral curve hypotheses needed here. Primary URL: https://stacks.math.columbia.edu/tag/02RT ; retrieval `turn283920481view0` and the complete section proof in `turn571368987view0`. Its referenced valuation lemma is a cited known input, not independently reproved here.
- Milne, *Jacobian Varieties*, Proposition9.1, exact statement and displayed proof, with the prime-to-characteristic Lemmas9.2–9.3. Primary URL: https://www.jmilne.org/math/xnotes/JVs.pdf ; retrieval `turn283920481view2`. The map defined over k gives the required equivariance.
- Milne, *Abelian Varieties*, Remark15.3 on the Tate-module identification; Theorem19.1 and its displayed proof through Lemmas19.2–19.3; and the numerical p-rank inequality r≤g in Remark8.5. Only that inequality is used from the latter remark. Primary URL: https://www.jmilne.org/math/xnotes/AVs.pdf ; retrievals `turn841374131view1`, `turn571368987view3`, and `turn841374131view0`.
- The already-whole-checked A45 integral descent SD.3–SD.10 was reread as retained in `work/row_audit/NONCONSTANT_PRIMITIVE_DESCENT.tex`; its long proof is cited rather than duplicated. Stacks Proposition35.3.9, Tag023N, complete statement and displayed proof were directly reopened/read. Primary URL: https://stacks.math.columbia.edu/tag/023N ; retrieval `turn502049562view1`. No restriction p not dividing the semilinear action order is introduced.

The primary-source reading above is exact passage reading, not a claim to have reread entire books or papers. No new GRH assumption occurs in A51.

## Static source check

The source has seventeen paired display blocks and tags NC.1–NC.17, one complete proof environment, and no new macros. The four longest displays were split before sending the final hash. This is a static source check only; the final PDF remains under its existing build freeze.
