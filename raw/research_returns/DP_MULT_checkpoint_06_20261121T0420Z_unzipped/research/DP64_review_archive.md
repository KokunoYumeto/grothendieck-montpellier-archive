# DP64 independent complete proof challenge

Checker `/root/archive_binomial`, GPT-6 Astra Pro; effort not exposed. All seven sections read at observed04:10:49 and again04:12:10 UTC on2026-11-21. Challenge closed04:12:21. **PASS**. Whole memo SHA256 `e16eec33f63010fa0aa532d7657fb2860d3c61ddacf50ece97c5e967fe7f6e22`. Snapshot and metadata are in `late_proof_snapshots/DP64_complete_archive_checked.md` and `DP64_archive_review_metadata.json`.

A subfield of a cyclotomic field is Galois and abelian, so its embedding set is a torsor under its Galois group. Restriction from the full cyclotomic Galois group is surjective with equal fibres. For every fixed selected embedding exactly half of residue classes send it outside the type. This proves the first-coefficient average independently of geometric display identification.

The class errors are uniform over directions and types because class coefficients are binary. Summing their absolute errors over the fixed finite class set gives one common constant. A fixed finite exceptional set only changes that constant. The higher slope tail is bounded by `1/(p(p-1))`, whose logarithmically weighted prime sum converges. Multiplying by the fixed nonnegative orders gives the stated linear budget and O(N) error.

The floor formula correctly saturates: orders0 and1 contribute zero, and for n at least2 the first-power cutoff is `min(X,n)`. The floor discrepancy is at most one per prime, giving ordinary theta at the cutoff, hence O(n). The entire higher-power contribution is nonnegative and O(n) by the convergent tail. This proves uniformity in n and X, including both sides of the saturation threshold. Same-order-multiset comparison and differing subfields of the fixed cyclotomic field follow.

For positive orders totalling N, the log-cutoff difference is between zero and `log(N/n_i)`. The weighted difference is at most `N log d` by entropy when at most d directions are used. N=0 is separate and N=1 is harmless. Thus fixed-total redistribution changes the certificate by O(N) for fixed d; no growing-conductor or growing-d uniformity is asserted. The mod7 example is correct: class1 preserves type123 and each other class moves at least one element outside, so the adaptive maximum has mean5/6. That is only a finite calculation, not a free global realization of varying local choices.

I visually reread Rudnick, *Primes in Arithmetic Progressions: Fixed Modulus*, Section2, printedp2, equation(1), from the saved original page. It states the weighted prime sum in each reduced class with O(1) error for fixed modulus, beside quantitative fixed-modulus PNT; ordinary theta O(Y) is a consequence. Primary URL: https://www.math.tau.ac.il/~rudnick/courses/sieves2015/fixed%20progressions.pdf . No RH assumption is used.

The proof compares explicitly defined bare directional lower certificates. It proves no upper bound on a selected theta value, no implementation of adaptive choices, no identification of derivative order with automorphic cost, and no exclusion of an O(N) improvement after leading cancellation. Integral geometric cyclic models and fixed primitive directions remain hypotheses for a geometric application. These limits are preserved. No mathematical correction was required.

## Whole intended paper preservation

At04:18:47 I read the entire integrated theorem/proof and both following scope paragraphs, comparing to the whole checked memo. PASS. FragmentSHA256 `eef3230c514be5ca77864a0717cf6c09d229dc6b63b3198c13657700564e7faa`; complete proofSHA256 `7110b4569d32c956fa79b12ee98b6634f3eb0b6de2fc870f574edc4a449e0aa5`; exact main count 1. All analytic, floor, entropy and adaptive-choice limits are preserved.
