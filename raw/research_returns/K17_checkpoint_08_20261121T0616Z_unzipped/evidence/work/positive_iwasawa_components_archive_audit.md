# Independent whole-proof audit: positive Iwasawa components

**PASS.** Reviewed the entire `work/positive_iwasawa_components_section.tex`, including both K17-POSITIVE-COMPONENTS and K17-TWO-SIDED-COMPONENT-RANGE, and every line of the 64-line exact certificate.

Reviewer: GPT-6 Astra Pro, run `/root/archive_kummer`, 2026-11-21. Reviewed TeX SHA-256: `3e41379f120417a3c3f0fbbbea5469acd126b1708d37e5157fb5342a37173e91`; certificate SHA-256: `a6ccecb6326a7a520095956d90b242a0b8e4cc3cc5c1630969e36a98ece0e5cd`.

Independently reconstructed all sixteen even Bernoulli numbers B2,...,B32 using the exact Akiyama--Tanigawa triangle, rather than the author's defining recurrence. Compared every numerator and denominator, multiplied every factorization, and independently tested every displayed factor by exhaustive trial division through its integer square root. All checks passed. The largest prime factor is 1001259881, below 2^31. Actual independent replay metadata: `work/bernoulli_positive_components_archive_replay.json`.

For p>2^31, the reparameterization e=p-1-a is even and lies in [2,p-3]. The Bernoulli index in the already fully audited reflector is exactly a, and the even class character -e is a modulo p-1. All denominators are smaller than p and the displayed numerator factors are smaller than p, so the required rational residue is nonzero. The proof does not misuse a fixed-weight Hecke calculation at this large reparameterized e.

For all odd p<2^31, the previously independently sourced Hart--Harvey--Ong Vandiver verification kills every even base class component. This handles numerator divisors, denominator divisors, repeated characters, and trivial characters. There is no prime equal to 2^31. Hence every base component in the claimed positive range vanishes. The now independently audited componentwise control proposition carries that zero separately to every cyclotomic layer and the norm limit, with no character mixing.

The odd p-ramified character is omega^(1-a), as in the exact WWE twist/involution dictionary. The two exceptional characters use the already proved integral Coleman ideals; thus the freeness claim is integral and valid for every residue at p>=5. For k congruent to -j modulo (p-1)/2, the class character -2k is 2j, giving exactly the stated K-primary vanishing by (K2). Combining the negative k residues -16,...,-1 with the earlier 0,...,9 gives the displayed two-sided range. No group-order periodicity or all-character Greenberg assertion is made.

No mathematical correction requested. The positive-component proposition does not use the stipulated Alpoge theorem; the combined two-sided corollary does.
