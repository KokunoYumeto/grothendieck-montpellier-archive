# A50: complete independent proof reading

Date: 2026-11-21. Reviewer: GPT-6 Astra Pro; effort not exposed; `/root/effective_galois`.

**Verdict: PASS.** I read the entire final source, including all three proofs, the finite calculation, and the concluding scope qualifications:

`work/gt_certificates/positive_rank_theta/PARTIAL_PACKET_OPERATOR_LIMITS.tex`

SHA256 `e4210912179884aa79bca87a65743b5046b58d0d729aea37371c5a64634666c4`.

This is an independent mathematical reading. The computation described below is an unchanged producer replay, not a new independent implementation or formal verification.

## Norm inequality

The unit assumption excludes the zero cyclotomic algebraic integer. The product of its primitive evaluations is the rational integer norm, so the specified p-adic divisibilities force an absolute lower bound on its nonzero integer magnitude. Every complex conjugate has magnitude at most the integral coefficient l1 norm. Taking the phi(n)-th root gives exactly PP.3. The product includes all embeddings, hence no residue-degree or place factor is missing. Vanishing at one primitive characteristic-zero root forces divisibility by the rational irreducible cyclotomic polynomial and vanishing at every primitive root. The statement is correctly conditional on the displayed divisibility requirements.

## Complete spectral subspace and finite certificate

The signed multiplication-by-two orbits modulo 31 are disjoint and each has length 5. Expanding the trace in PP.6 and using the geometric-series identity gives exactly PP.8, including the two signs. The values at -1 and1 recover a and b. Conversely binary Fourier values obey squaring compatibility, so the two orbits admit precisely two F32 parameters. Thus this is the entire ten-dimensional spectral subspace, not merely a selected code.

I read every line of `verify_trace31_packet.py`. Its bit multiplication implements reduction modulo z^5+z^2+1. The complete 31-element nonzero power orbit proves that the displayed quotient is a field and z has order 31. The script enumerates all 1024 pairs, checks distinct words, exact weights, support of all ten generators, the idempotent and its modulo 8 lift. It retains every word. The resulting distribution sums to 1024 and has minimum nonzero weight 10; a=b=1 attains 10.

An unchanged copy was executed in `work/effective_galois/a50_review_replay/`. It passed and its output JSON is byte-identical to the retained producer output. Script SHA256:

`b5278c3827b2dbac5be04e25c374ca4b828b15365223581588a9e8de21ee33b0`.

Output SHA256:

`268ff05cde6a415cf6e6ddcd4554827e9a083365b22a60643ae9f81873ae0699`.

I did not claim to execute or independently implement the sibling's separate polynomial-vector checker.

## All-annihilator lower bound

The displayed identity for f(t)=3t^2-2t^3 is exact and squares idempotence error, so two iterations suffice modulo 8. The complementary ideal is a projective direct summand of the free Z/8 group ring; since Z/8 is local, it is free, of rank 21 by reduction modulo 2. Its generator is nonzero.

For a nonzero integral annihilator A, take the exact common coefficient power 2^b. If b>=3 its l1 norm is already at least 8. Otherwise division of the coefficientwise congruence modulo 8 yields a nonzero binary reduction in the entire good spectral subspace, so at least 10 coefficients are odd. Its l1 norm is at least 2^b times 10. Scalar 8 attains the unrestricted minimum 8. The threshold 31>(d-1)^2 requires integer d<=6, so every nonzero annihilator fails it.

For two disjoint free deck orbits, the positive divisor degree of A(Q'-P') is exactly the coefficient l1 norm; signs create no cancellation between those distinct orbit points. The exponent-eight example correctly avoids the false inference one would obtain from a binary code alone, since scalar 2 annihilates an exponent-two module.

## Scope

The two assertions establish limits on one proposed integral-operator deduction. They do not realize the finite module as rational Jacobian torsion, construct an actual collision, rule out other operators on a particular curve, or establish failure of geometric supply. The source maintains those distinctions. No change to the installed paper or its build was made for this audit.
