# Partial-packet integral operators: author full-proof and computation audit

Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.  
Date: 2026-11-21.  
Source: PARTIAL_PACKET_OPERATOR_LIMITS.tex.  
Final source SHA256: e4210912179884aa79bca87a65743b5046b58d0d729aea37371c5a64634666c4.
Whole-proof-read version SHA256: b9b420ab17efe79c0e9c50e8b38afdb58b02c0fe8aa9d95fcc61ea94cfe16ecc.

## Verdict and scope

PASS. I read the entire source after completion: the norm statement and proof, complete spectral-subspace identification, finite weight calculation, exponent-eight module proof, and final geometric qualification. This is an author whole-proof check. Row_audit independently read the complete source and reported PASS separately. No geometric realization is claimed for the finite module, and no conclusion that actual curves lack separating covers is drawn.

The norm bound concerns integral operators that are units on at least one good primitive character and divisible by p^a on all specified bad characters. The module example concerns all nonzero integral annihilators of one cyclic abstract module generator. These are different statements with their own explicit hypotheses.

## Complete norm argument

The unit assumption ensures the cyclotomic algebraic integer is nonzero, so its norm is a nonzero rational integer. Every primitive embedding occurs in the norm product. At the fixed p-adic embedding, all evaluations are integral and each bad one has the assumed valuation. Thus the integer norm is divisible by p to at least a times the number of bad primitive characters. Every complex conjugate has absolute value at most the coefficient l1 norm. Combining the integer lower bound and archimedean upper bound proves the stated exponent. Since p does not divide n, cyclotomic p-adic valuations are unramified; there is no missing residue-degree factor in the all-embeddings product. Exact integer isolation of only part of a rational cyclotomic block would contradict irreducibility of Phi_n. This argument provides no geometric upper bound on the torsion exponent.

## Complete finite spectral argument

The two signed multiplication-by-two orbits modulo31 are disjoint and each has length5. Expanding the trace gives exactly the displayed DFT values at the ten frequencies, with a and b recovered at frequencies -1 and1. Conversely the binary DFT values satisfy squaring compatibility, so two F32 parameters exhaust the full spectral subspace. The trace family is therefore the whole dimension-ten space, not just a subcode.

The coefficient field used in the checker is verified to be a field by the complete31-element nonzero multiplicative orbit. The complete1024-word enumeration has weight distribution0:1,10:31,12:155,14:310,16:217,18:155,20:155. All words are distinct. The minimum is10, not the preliminary conjectural12. The word a=b=1 is the binary spectral idempotent and has weight10.

## Exponent-eight construction

The polynomial identity for f(t)=3t^2-2t^3 squares idempotence error. Two iterations lift the binary idempotent to an idempotent in (Z/8)[C31]. Its complementary ideal is cyclic with generator1-e and is a direct summand of a free Z/8 module; its reduction has dimension21, giving the asserted rank. The good packet is absent by construction.

For a nonzero integral annihilator A, remove the exact common power of2 in its coefficients. If that power is at least8, the l1 norm is at least8. Otherwise coefficientwise division of the congruence leaves a nonzero binary word supported in the good spectral packet, so at least10 coefficients are odd and the l1 norm is at least10 before restoring the power of2. Thus every annihilator has norm at least8, and scalar8 attains the bound. This excludes the threshold d<=6 corresponding to31>(d-1)^2. At exponent2 the scalar2 would already annihilate the module; the source explicitly prevents confusing the binary code bound with a bound on all integer annihilators in that easier case.

## Execution and independent-output comparison

Executed verify_trace31_packet.py successfully. Final script SHA256:
b5278c3827b2dbac5be04e25c374ca4b828b15365223581588a9e8de21ee33b0.

Final output SHA256:
268ff05cde6a415cf6e6ddcd4554827e9a083365b22a60643ae9f81873ae0699.

The output retains all1024 parameter/word/weight records, all ten generator DFTs, the binary idempotent and its explicit lift modulo8. The integer-annihilator minimum is proved in the written source, not established by enumerating all integer operators; the JSON field explicitly distinguishes this.

I read the complete independently authored coefficient-vector checker in work/row_audit/partial_packet_review/check_trace31_independent.py. It imports no producer code or data and no optional algebra package. I compared every retained parameter/word/weight record against our output; all1024 agree exactly. The comparison is saved as trace31_full_output_comparison.json. I did not rerun the independent checker myself; row_audit executed it and also replayed our checker in a separate directory.

Independent script SHA256: 4db53b12b663a3dcf4772595a9f25228ab339f5d752b6be94d9f6f4a9c0f78e2.  
Independent output SHA256: 60f99b75689641c936ec4a69368a8ff254b1762fbea775fa0389eaa0151357e3.

The source was frozen before the independent full reading. This is a checked algebraic obstruction to one proposed deduction, not a new theorem about all curve covers or evidence that the universal main geometric gate is closed.

## Final label-only delta

At the parent's request the initial paragraph heading “Scope” was replaced by “Finding A50 (integral limits of a partial-packet projector)”. This is the sole change from the entire-proof-read b9b420ab version to the final e4210912 version. The exact one-line change was checked; no mathematical statement, proof or certificate changed.
