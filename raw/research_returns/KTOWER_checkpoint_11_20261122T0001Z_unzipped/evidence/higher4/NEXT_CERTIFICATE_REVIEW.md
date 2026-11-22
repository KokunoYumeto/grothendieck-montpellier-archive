# Independent review of next-weight completion reconciliation

Reviewer: `/root/lean_chain`, GPT-6 Astra Pro; effort not exposed. Date: 2026-11-21 UTC.

## Verdict

**PASS.** I read the complete `next_certificate_audit.py` and `verify_next_classical.py`, the updated source-hash/row-shape assertions, and the complete `replay_native_faddeev.py`. The cyclic module, cyclic full wrapper, integral setup driver, frozen full verifier, native full-row code/wrapper, and native completion collector had already been read in full in the named preceding reviews. I inspected both actual completed initial-field e32 reports and ran the reconciliation afresh. This is a report and integer-arithmetic reconciliation, not a new execution of those large models.

The final reviewed audit source has SHA256 `d92247e43910927808c76e817887d1587d5994b3cfe7acff2fcd703a5b0df594`.

At 18:08:31 UTC the independent execution returned:

* Complete finite certificate gates: e32.
* Pending combined gates: e34 and e36.

The immutable copy is `next_certificate_independent_snapshot.json`, SHA256 `a93a1eb585e618d2c1e1ed727d0d5156e216cbff65da798a2b8bdb0437ad8b37`. The extra exact checks are in `next_review_checks.json`, SHA256 `073227f2d62cbaedcfc42f0e7cb48e9e8b11d18fffa5f448085aae9290ce8a1c`.

## Code semantics checked

The support audit recomputes the full saved characteristic-polynomial evaluations at seven and thirteen, checks their nonzero values, multiplies the full unitary and classical comparisons, and computes the exact gcd. It independently proves each small prime by trial division. Repeated exact gcd division against the residual moduli removes the entire remaining support. Bounded integer factors need not be prime: every prime divisor of a positive integer below the cutoff is itself below the cutoff. No large-modulus primality or squarefreeness assumption enters.

Completion is determined from final JSON reports, never progress logs. Initial-field reports without the final implementation metadata are ignored; an incomplete JSON write is not accepted. Every accepted report must have the full PASS status, current data and neighbor hashes, correct degree and all three dimensions, every-neighbor and whole-characteristic-polynomial flags, both extra-point flags, and the expected comparison gcd. Cyclic reports must contain both prime certificates with full dimension and nonzero Krylov determinants. The checked wrapper sources ensure the exact Horner identity and full model checks precede their published reports.

The explicit native Faddeev substitution clears rational denominators exactly, performs the standard integer recursion, checks every trace division, scales coefficient k by the kth denominator power, and checks the final matrix is zero. It replaces only the prior characteristic-polynomial function. The e32 native and cyclic reports use identical data and have identical full numerical model results. The already reviewed cyclic route alone suffices for the arithmetic proof; the native report is an additional completed exact verification.

The alternate-field collector verifies every saved source/input hash, all thirteen frames, the full-kernel flag, full integer-model verification, all identifying rows, source/target/kernel dimensions, comparison point, denominator and Schur-pivot gcds, canonical determinant residues, norm-unit conditions, and the identity det(A0) times det(D) equals det(S). Its positive result requires an actual completed native report. Missing reports are explicitly pending. A malformed report fails the audit rather than yielding a positive conclusion.

The classical replay wrapper freshly executes the previously audited full initial-field model at both seven and thirteen, and the complete alternate-field model at each residual modulus. It compares entire numerical objects, dropping only elapsed time, and requires unit conclusions with no unresolved pivot obstruction. It records nine replays: one initial-field degree object and two alternate-field objects in each of the three weights. This is a fresh same-code replay, not an independent new mathematical construction.

I requested two small provenance assertions in the reconciliation wrapper: current per-row classical source hashes and exactly one field-minus-three plus two field-minus-seven rows per weight. The parent added them; I reread the changes and reran the final code. Both checks also passed independently against the current report before relying on them.

## Actual e32 evidence and arithmetic proof

The complete initial-field cyclic report has SHA256 `eb4777af4d01ebed96d13bae591c84281aba671bf76979f107fba260b7c008cb`. The integer-Faddeev report has SHA256 `d5273d5fbd09856ab0b98fc013dcfeeb0dbe6ddcace991d41156591b6ce728a0`. Both reconcile to the full data hash `992b4de93f23ef658081a0b13ff57d948b9bc340697ae12616d1c34569db435a`, with dimensions 1355,1200,155. The completed native alternate-field reports have all 1365 rows and the hashes and residues displayed in `next_vanishing_section.tex`. The full alternate classical dimension is 125; its two unit residues are also displayed there.

In addition to the audit's repeated support divisions, I directly checked the identity

`gcd(C7,C13) = 2^667 * 3^798 * 5^22 * 11^11 * 19^4 * 23 * 97^4 * 36293 * 38177 * M1 * M2^3`.

This establishes the exact support statement without factoring either large residual integer.

I wrote and then read the entire `next_vanishing_section.tex`. KT-K64-VANISH follows by the same carried prime-by-prime argument as the preceding degrees: small primes are independently excluded by the stipulated carried results; for every remaining prime, GD and the closed OneChar comparison force initial support; complete alternate unitary and classical units kill that support; VK-PT then gives zero K-primary part. Every remaining prime exceeds 65, so the source's displayed inequality and denominator conditions hold. Finiteness concludes the proof.

KT-COMPONENT-EXTENSION-16 adds only the positive representative 16 to the already proved interval. The safe interval is therefore [-16,16]. The full-domain index formula gives the Soulé character in weight 33, since 2·33−2=64. No additional negative Bernoulli component or deeper-filtration Soulé image is asserted. The conditional e34/e36 paragraph asserts no new K68 or K72 vanishing.

No new Lean kernel build is claimed. The arithmetic proof retains the exact stipulated archive convention and previously accepted arithmetic inputs. Later report completions must be checked separately and must not be retroactively attributed to the frozen 18:08 snapshot.
