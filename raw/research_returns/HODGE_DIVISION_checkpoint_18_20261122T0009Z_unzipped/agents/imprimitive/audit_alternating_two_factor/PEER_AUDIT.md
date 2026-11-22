# Independent whole-proof audit: D-ATT-04–06

**Result: PASS.** Auditor `/root/imprimitive`, GPT-6 Astra Pro, effort inherited/not exposed, run `HODGE_DIVISION`, 2026-11-21.

The complete frozen proof `agents/g34_eightfolds/bireflection/alternating_two_factor_section.tex` was read at SHA-256 `b7a5a8d6e9c887fb0e3cdb4964bd2cda6a927d38d8d314b2c821cb3f4c78bcbf`. Every line of the adjacent author checker `check_alternating_two_factor.py` and its full final output `alternating_two_factor_checked.json` was also read. No author file was edited. The author's execution is attributed to the author; the separate computation below is my own implementation.

## Exact dependencies and source scope

The preceding D-ATT-01–03 proof was independently reviewed in full immediately before this addendum, with its full scalar/normalizer and actual field interface. That report is `audit_alternating_two_tail/PEER_AUDIT.md`, SHA-256 `52e5c87cdd650a5d08573ea365d7c515dae9de0ef3977da06e0f251b69050b37`. I reread the complete UP.3–UP.4 and EX.2–EX.4 derivations in the author's earlier own-directory proofs. The precise hypothetical source is an actual faithful intermediate image with six-dimensional cohomological multiplicity and a connected cover; the review retains this geometric interface rather than introducing arbitrary branch profiles.

The only arithmetic source needed beyond those earlier results is exactly the freshly read Milne conductor/cyclotomic input of the preceding audit: *Class Field Theory* v4.03, ChapterV Example3.2 printedp157, Remark3.8 p158, Examples3.10–3.11 p159, complete passages at `https://www.jmilne.org/math/CourseNotes/CFT.pdf`. References from that actual fresh reading are `turn753288950view0` and `turn988107425view0`–`turn988107425view2`. This is a reuse of that immediately preceding complete source read, not a claim of another retrieval or a re-proof of general class field theory. No new classification theorem is invoked by the addendum.

For completeness, the actual irreducibility of both alternating constituents also has a direct independent check. On `A_n`, for `r+2s≤4` and `n≥6`, the factorial moment `E[(f1)_r(f2)_s]=2^(−s)`: prescribe the ordered fixed points and ordered two-cycles; at least two unspecified letters remain, so exactly half of the completions have either parity. Applying these moments to the two actual character polynomials gives mean zero and squared norm one for each. Thus their actual rational modules are nontrivial irreducible `A_n` modules in the stated range. The finite symbolic supplement verifies these exact moment identities, separate from the already known ordinary-label description.

## D-ATT-04: common index inequality

I checked every case for `A=(n−5)/2`, `B=n/4`. The unordered-pair target-one estimate is exactly UP.3, while the other-scalar constant `(n−4)/2` is at least `B` for `n≥15`. The exterior target-one estimate is stronger by `k/2+n/12`. For other exterior targets, EX.2 suffices when `k≥n/2−2`. Below that threshold, EX.3 gives `(n²−4n+3)/4`, exceeding `A(n/2−2)+B=(n²−8n+20)/4` because `4n−17>0`. The floor is discarded in the valid lower-bound direction. The identity permutation remains excluded, and off-spectrum targets cause no exception.

## D-ATT-05: actual weighted swaps

Conjugating `(X⊗Y)S` by `I⊗Y` in the convention `C^(−1)TC` gives `(XY⊗I)S`. In an eigenbasis of `XY`, constant words have eigenvalues `alpha_i`, while each unordered pair of distinct words gives the two square roots of `alpha_i alpha_j`. For a proposed eigenvalue `zeta`, subtracting the diagonal contributions from the ordered-pair count and adding back the correct constant words gives exactly

`2m_zeta = N_zeta + d_plus − d_minus`.

Each first index admits at most `a−nu(W(h))` second indices. Thus `N_zeta≤a(a−nu(W(h)))`, proving the displayed bound for every scalar, including absent eigenvalues. The identity-product swap has only eigenvalues plus and minus one; its marked scalar outside `mu6` therefore makes its actual fixed space zero. This last use is about the actual scalar of the inertia, not an inferred support bound after arbitrary convolution.

## D-ATT-06: scalar placement and actual quotient cover

The factor permutation is an actual map to `S2`. Transitivity and the product-one relation force a positive even number `P` of swaps. Four swaps and eight other genuine marks exceed the moving-rank budget, so `P=2`. If a scalar mark outside `mu6` occurs at a non-swap, two marked entries can be chosen with a third, distinct swap; their three bounds and the nine remaining marks give the stated strict contradiction. This selection remains valid when there are more than two marked entries. Consequently the two swaps are precisely the outside-`mu6` marks.

For a non-swap with at least one nonidentity factor permutation, twice the larger projective support is at least the sum of the two projective supports. At least one factor contributes the positive `B` term, giving ATT.8. A genuine scalar with both factor permutations identity has full moving rank and satisfies the same inequality. For each swap, ATT.9 follows from the exact weighted-swap estimate when its cycle product is nonidentity; when the cycle product is identity, its actual marked scalar supplies full moving rank and hence still supplies the required `B` term. I checked `B−1≤a` in the full range.

The scalar extraction is an actual homomorphism, and its rational tensor-wreath image has trivial scalar intersection. Faithfulness therefore gives the actual permutation action on two blocks of `n` letters. It is transitive because the normal core contains `A_n×A_n` and the image has a swap. Taking the stabilizer of a letter in the actual connected finite cover yields a connected degree-`2n` quotient cover of the sphere.

A non-swap has permutation index `ind(x)+ind(y)`. A swap has one cycle of twice the length for each cycle of its product, so its index is `n+ind(xy)`. Riemann–Hurwitz on this actual quotient gives total permutation index at least `4n−2`. Removing the two base contributions `n` gives precisely `E≥2n−2`. Scalar branch entries contribute zero index but remain genuine coefficient-variation marks. No abstract tuple or unproved dominance implication is substituted here.

Summing the coefficient support estimates gives

`D ≥ e + a(AE+rB)/2 − a`.

The inequalities `r≥12`, `E≥2n−2` give the polynomial `n²−3n+5`, equal to `2a+5` for UP and `2a+3` for EX. The resulting excesses over `2e` are respectively `3a/2` and `a/2`, both greater than six. This contradicts the actual multiplicity-six Euler identity. Every numerical inequality is universal in `n≥15`, with no extrapolation from the finite scan.

The theorem keeps transitivity on exactly two factors, the non-Eisenstein original field as a subfield of the actual inducing field, and arbitrary compatible phases/outer cosets. The stated failure to extend the identity-cycle-product argument automatically to larger tensor cycles is correct. At `n=100,t=2`, both labels pass the previous finite-range and ALT07 numerical gates, so the new obstruction is a strict reduction without asserting prior existence.

## Independent exact reconstruction

`independent_check.py` imports no author arithmetic. It reuses only the two pure functions from my own preceding signed-pair-orbit implementation, extracting their AST definitions without executing any top-level tests or output code. The retained hash of that own dependency is `1e1c7a9a7878b92d3e1f15eb70202237fa1d6c0aee69978e75070f218fa5d3e2`.

The final exact run passed at **2026-11-21T22:40:28.482124+00:00**, in **2.1944611290018656 seconds**:

- All **11,224** actual signed/unsigned pair-orbit partitions for `15≤n≤26`, checking the new common-index inequality on **777,756** nonidentity spectral entries.
- **112** weighted swaps built explicitly on eigenbasis words, checking **2,272** eigenspace multiplicity identities and rank bounds.
- All **576** pairs `(x,y)∈S4×S4` on the actual eight-letter block action, verifying the doubled cycle-product lengths and indices.
- Eight universal polynomial positivity checks after the shift `n=15+u`, with every coefficient explicitly required to be rational and positive.
- The independent exact alternating character moments establishing norm one and mean zero for the two constituents.

This supplements the universal proof and full geometric argument; it is not a claim of tuple enumeration.

## Honest attempts and result

The first supplementary run passed at22:40:09.769113UTC in2.260124116s, but a subsequent code read caught Python's evaluation of one integer division as floating `1.0` inside one symbolic UP polynomial. Although the constant is exactly representable and no inequality was wrong, that run is not used as the final exact certificate. I retained `first_independent_check.py/.json`, replaced the division by `SymPy Rational(1,2)`, required every shifted coefficient to be rational, and reran the full supplement successfully. There was no mathematical counterexample, author repair, or failed assertion.

**Disposition: whole-proof/source/code audit PASS.** Larger tensor counts and other labels retain their stated gates. No new positive source or cycle is claimed.

Final report written: **2026-11-21T22:41:36.421136+00:00**.
