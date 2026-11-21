# Partial-packet operator limits: whole-proof and independent finite review

Date:2026-11-21. Reader: GPT-6 Astra Pro, AN_GRH `/root/row_audit`. Effort is not exposed.

## Exact source and verdict

**PASS, targeted proof check.** I read the entire source

`work/gt_certificates/positive_rank_theta/PARTIAL_PACKET_OPERATOR_LIMITS.tex`

at SHA256 `b9b420ab17efe79c0e9c50e8b38afdb58b02c0fe8aa9d95fcc61ea94cfe16ecc`.

Every statement and all three proofs were checked. No correction is requested. This is a whole-proof reading plus the separately described finite computations; it is not formal verification or a geometric counterexample.

## Norm bound

The unit hypothesis makes the characteristic-zero cyclotomic integer nonzero. Its norm is the product over all primitive embeddings, including the embeddings at the one selected p-adic place. Summing the displayed valuations therefore gives at least a(phi(n)−|Omega|). The absolute value of the nonzero integer norm is at least the corresponding p-power, while every complex factor is at most the coefficient L1 norm d. Thus d≥p^[a(phi(n)−|Omega|)/phi(n)] follows. The separate exact-isolation statement follows from the irreducibility of Phi_n over Q. No rational conjugacy orbit is silently replaced by a single local orbit.

## Entire binary spectral code

The trace expansion gives the Fourier values a^(2^j) on the negative orbit and b^(2^j) on the positive orbit. The two order-five orbits modulo31 are disjoint. Those values recover a,b, and binary coefficients impose the converse squaring relations, proving equality with the full ten-dimensional spectral subspace.

I authored a separate implementation before reading the producer's implementation. It uses five-component coefficient tuples, ordinary polynomial convolution, and long reduction by z^5=z^2+1. It imports no producer code/data, curve arithmetic, or external algebra package. It checks the31 distinct nonzero powers of z, every field trace, all1024 codewords, their distinctness, rank10, and the Fourier support of all ten generators. The latter and dimension10 prove the asserted whole-subspace calculation.

The exact weight distribution is

    0:1, 10:31, 12:155, 14:310, 16:217, 18:155, 20:155.

The minimum nonzero weight is10, attained by a=b=1. The sum is1024. This is exhaustive finite arithmetic, not a proof-assistant certificate or any curve enumeration.

Independent checker:

- `check_trace31_independent.py`, SHA256 `4db53b12b663a3dcf4772595a9f25228ab339f5d752b6be94d9f6f4a9c0f78e2`.
- `check_trace31_independent.json`, SHA256 `60f99b75689641c936ec4a69368a8ff254b1762fbea775fa0389eaa0151357e3`.

## Exponent-eight module and all integral annihilators

The polynomial identity for f(t)=3t²−2t³ is exact. Starting from an idempotent modulo2, two applications give an idempotent modulo8, still reducing to the same binary projector. Its complement is a direct summand of the free rank31 module over the local ring Z/8, so it is free of rank21 and has the stated generator.

For A=2^b B with B having an odd coefficient, the case b≥3 has norm at least8. For b<3, annihilation of the complement modulo8 implies that the nonzero reduction of B is supported on the good binary packet. Its weight is at least10, giving norm(A)≥2^b·10. This covers all nonzero integral operators, including those with zero reduction modulo2. Scalar8 attains the unrestricted minimum, so that minimum is exactly8. Since31>(d−1)² requires the integer d≤6, no nonzero annihilator passes that comparison.

The source correctly distinguishes this from an exponent-two module, where scalar2 would already annihilate everything and the binary nonzero-reduction bound alone would not suffice. It also correctly identifies the degree of the positive part of A(Q′−P′) with its coefficient L1 norm when the two deck orbits are disjoint and free.

## Producer-code read and unchanged replay

After authoring/running the independent trace enumeration, I read the complete producer `verify_trace31_packet.py`. Its bitwise field arithmetic is different from the independent tuple/convolution arithmetic. Its idempotent computations and Fourier checks agree with the written proof.

An unchanged isolated copy in `producer_replay/` was run and reproduces byte-identical JSON:

- producer script SHA256 `b5278c3827b2dbac5be04e25c374ca4b828b15365223581588a9e8de21ee33b0`;
- producer JSON SHA256 `268ff05cde6a415cf6e6ddcd4554827e9a083365b22a60643ae9f81873ae0699`.

The full1024 tuples (a,b,word,weight) were compared against the independently generated output; every tuple agrees. The producer replay is not counted as a third implementation.

## Scope

The module W is abstract. No Jacobian, geometric cover, or point-section collision realizing W is asserted. The result obstructs an unqualified deduction of a sufficiently small integral annihilator from one missing signed packet. It does not refute the geometric witness requirement, exclude a useful operator for a particular cover, or prove that full primitive-unit packets are necessary for every approach.
