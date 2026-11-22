# Whole-proof peer audit: HD-AT301–03

**PASS.** Reviewer `/root/g34_eightfolds`, GPT-6 Astra Pro, effort inherited/unexposed, HODGE_DIVISION. The complete frozen proof, every author checker line, its complete final output, bibliography and source record were read. The reviewed proof is `research/alternating_two_row_three_tail_section.tex`, SHA **2f78ba157ecd0a5d671b682622ecc812e82086b048b6fb91bf7265fae3396096**. The independent computation completed at **2026-11-21 23:25:06.405546 UTC**. No author mathematical repair was requested.

The theorem concerns the ordinary label `(n−3,3)`, n≥15. It excludes a single factor over every original imaginary quadratic field, and all transitive tensor counts t≥2 when the inducing character field contains a non-Eisenstein imaginary quadratic field. It does not claim the other three-box labels, nontransitive tensor systems, spin modules or a positive supplier construction.

## Source check

I freshly opened and read all three pages of the institutional scan of James–Liebeck, *Representations and Characters of Groups*, second edition, including the entire Proposition 29.12 and entire Theorem 29.13 proof on printed pp.344–345:

<https://www.math.colostate.edu/~hulpke/lectures/m667/JamesLiebeckSnRep.pdf>.

The source explicitly gives the irreducible two-row character as the difference of consecutive subset-permutation characters. Its proof uses the intersection-size orbits on pairs of subsets and induction. This is the only new published character input needed. The precise rational degree and fixed-cycle specialization in the draft agree with it. The rational model, non-self-conjugate restriction to A_n, complete symmetric-group outer action and simple-group faithfulness are the accepted alternating-core interfaces; their hypotheses n≥15 and this long label hold here. No fresh proof of all surrounding symmetric-group representation theory is claimed.

## Uniform character and support inequalities

The character specialization is correct: the fixed three-subsets are counted by `C(f,3)+fu+v`, and fixed two-subsets by `C(f,2)+u`. Their difference gives (AT3.2). For f=0 it is bounded below by −n/2; for f=1 it is nonnegative; for f=2,3,4 the only possible negative initial term is at least −2, and for f≥5 all terms are nonnegative. This establishes the global lower bound, including every power of a permutation.

For f≥2 the available two- and three-cycle letters give the stated upper bound on the positive part. Exact division by n−f gives c_f. Its comparison with c has strictly positive numerator `f²+(n−9)f+5`. The f=0 and f=1 upper bounds separately give c and the stated positive surplus. Identity powers cause no exception because both sides of the defect estimate vanish.

The cyclic average of the moved-letter count is the actual natural index. Hence the character defect gives `a−m_1≥cI`. Since every character value is real and bounded below by −b, the real Fourier formula gives `m_z−m_1≤b` for **every** target root z. The factor multiplying a character value is nonpositive, so the direction of this inequality is correct even at negative character values. This is the necessary all-eigenvalue step; it does not equate the maximal eigenspace with the fixed space.

For large index, the exact equality c−A=n/3 gives the claimed full positive B. For smaller index every power fixes at least n−2I letters. The monotonicity of c_f improves the cyclic average, and after clearing denominators the desired inequality is exactly polynomial (AT3.10). Its second derivative is nonpositive on f≥3; its two endpoint values are strictly positive for n≥15. The extra f=2 endpoint is also positive. Thus the universal lemma is proved for every permutation and target eigenspace; the finite spectrum scan is supplemental.

## One-factor source

The rational Sn image has trivial scalar intersection: a scalar image centralizes its faithful An image, so its permutation centralizes An and is the identity. Consequently scalar extraction and the natural n-letter coordinate are actual homomorphisms. The quotient action is transitive because the image contains An. This is an actual connected quotient cover, so Riemann–Hurwitz supplies total index at least 2n−2.

The intermediate Euler identity excludes base genus at least two, and genus one permits at most six genuine marks, hence period rank at most six. A rank-nine case has a sphere, at least twelve genuine inertia entries and total moving rank 2a+6. A nonidentity scalar moves the full representation and satisfies the same bound with natural index zero. Summing the full positive B over all entries gives the exact excess `n²−8n−1>6`. No equality of original and inducing character fields is required.

## All transitive tensor counts

The rational tensor-wreath normalizer also has trivial scalar intersection, by its faithful conjugation action on the simple core factors. Its scalar coordinate is an actual finite character. If its image were contained in mu_6, its character field could not contain the stated non-Eisenstein quadratic field. Generation and product one therefore force at least two actual scalar marks outside mu_6.

Every power of a rational tensor-wreath operator has trace at least `−(b/a)e`: a negative cycle-trace product contains a factor of absolute value at most b, and each remaining factor has absolute value at most a. Rational cyclotomic multiplicities, with the fourth-root square-trace refinement, yield the stated support at both marked entries. This correctly retains arbitrary scalar phases and a possibly larger inducing field.

The lower support d0/a applies to every genuine entry; the weighted-cycle bound applies when factors move. The elementary inequalities `2d0≤a−1`, `b≤d0` and `d0≥43` hold on the full n≥15 range. If at least three inertia entries move factors, one can choose a moving entry distinct from both scalar marks and retain nine more entries, yielding the strict contradiction (AT3.12). Zero moving entries contradict transitivity; one contradicts product one. Thus precisely two move factors, their permutations are inverse full t-cycles.

The actual nt-letter quotient then gives `H+N≥2n−2`. At each factor-fixing entry the maximum of the active supports is at least their average, preserving **the entire B**, not B/t. An actual scalar entry satisfies the same formula. At a full factor cycle the accepted D-ATT08 lemma gives the exact R_t correction; the identity cycle product is retained through the weaker estimate `ν≥AI`, with zero on both sides. The t=2 error is a, and for t≥3 the proved bound is `2a^(t−2)`, so the uniform correction used in (AT3.15) is valid. Its algebra and final strict inequality check exactly.

These arguments use necessary actual-cover identities. No source-dimension inequality is treated as sufficient for dominance. The example `(97,3)` at n=100 lies beyond the earlier long-row exclusions and is a strict profile-level improvement, without asserting an actual source at that profile.

## Independent computation and honest failed attempts

Own files are `audit_three_row_tail.py`, `audit_three_row_tail.json`, and `audit_three_row_tail_attempts.json`. No author checker, exported spectra or fixed-point/divisor inversion routine is imported. The author code was read before this program was written. The independent program constructs the **actual permutations on all two- and three-subsets**, follows their cycles, and subtracts their cyclotomic multiplicities. It does so for every conjugacy class n=15 through 26.

The successful run checked **11,224 classes**, **23,636,509 actual subset points**, **3,508,661 actual subset orbits**, and **86,216 exact cyclotomic entries**. All target-eigenspace and negative-character inequalities pass; the least support margin is 12. Separate symbolic calculations check the universal defect, concavity, endpoint and source identities. The successful run completed at **23:25:06.405546 UTC**, elapsed **10.785513520 seconds**.

Two earlier auditor implementation failures are retained honestly. First, a symbolic normalization assertion mistakenly compared a polynomial with twice itself after all finite assertions had passed; the factor was corrected. Second, a structural equality compared an unsimplified SymPy derivative with its expanded form; it was changed to exact expansion of the difference. Neither failure exposed an author proof defect. The final program and output bind to the frozen proof hash above. The independent code has been read in full after those repairs.

The cyclic-average method is the root's derivation. The weighted-cycle and preceding two-tail source framework were previously authored by this reviewer and independently checked by others. This audit claims a new complete check and distinct finite reconstruction, not independent origin of every shared ingredient. No TeX compilation is claimed.
