# Exact prefix identity and bounded two-field unit scan

**PASS, bounded scope.** Read the complete `main_gate/bernoulli_prefix_formula.tex` and all 202 lines of `main_gate/explicit_two_unit_certificate.py`. Ran an unchanged frozen copy independently; session 11042 finished with exit 0. Its entire JSON is byte-identical to the saved original, SHA256 `758005cd82f9aceb79027276ae565984249532b6a5f283086407e91e6a8e8f0e`. Starting source, proof, and report hashes equal their current hashes; details are in `two_unit_finite_replay/review_manifest.json`.

## Formula audit

Writing `a=r+ph` in the defining conductor-`fp` sum makes the `r` term vanish because the nontrivial `χ` sums to zero. For `A_j=Σ h χ(h+j)`, cyclic reindexing gives exactly `A_(j+1)−A_j=fχ(j)`, including the wraparound term. Thus `A_j=A_0+fP(j)`. Multiplicativity gives `χ(r+ph)=χ(p)χ(h+[p^−1 r]_f)`. The remaining `A_0` term vanishes because `ψ` is nontrivial. This proves the exact formula, including its sign and normalization, and establishes `p`-integrality before reduction. Reducing the Teichmüller character gives the displayed prefix residue.

The family uses nontrivial exponents `e0=(p−3)/2` and `2e0=p−3`. Their weights are respectively the Legendre symbol times `r^−1`, and `r^−2`; both match the code. The proof's operation-count statement concerns the number of summands, not an assertion of constant-time integer arithmetic.

## Code audit

The sieve enumerates exactly primes `p≡3 mod4` in `[7,20000]`. A separate trial-division enumeration, written during this review, agrees with every saved prime. Squarefree extraction and square-factor assertions produce the intended `m` and fundamental discriminant `−4m`. For odd `a`, the character formula is `(-1)^((a−1)/2)(a/m)` because `m≡1 mod4`; it also handles `m=1` correctly. The exact class-number and splitting checks match the infinite two-unit theorem already reviewed.

The inverse recurrence and half-range square enumeration produce the required weights. The direct reconciliation uses `a^p mod p²`, the unique Teichmüller lift modulo `p²`; dividing the numerator by `p` only after retaining this precision gives the correct residue. The separate rational calculation uses the standard Bernoulli recurrence with `B1=−1/2` and the exact Bernoulli-polynomial distribution formula. Neither check uses floating point or a primality assumption on a composite modulus.

## Completed result and limits

The independently replayed report contains all **1135 primes and 2270 sign-labelled fields**, exactly two rows per prime. Every row has nonzero class-number/B1, first-twist, and third-twist residues. Both failure lists are empty. The complete row hash is `8328795e4544c175eaa37953962b681aee08ecb2b7aa9cf787aea3660994a472`. All 72 direct conductor-sum comparisons and 12 rational Bernoulli-polynomial comparisons pass. The script labels its formula scan PASS even if a third-unit failure were recorded, so the review additionally checks both empty failure lists and every nonzero row explicitly.

Together with the already-reviewed character transport, this proves the three units for these two fields throughout the indicated weight progression, **only for the finite prime range stated**. It gives neither a third-unit theorem for larger primes nor a new general auxiliary-field existence theorem. This is a fresh replay of an audited implementation, not a claim to a wholly different large-scan implementation or a Lean kernel proof.
