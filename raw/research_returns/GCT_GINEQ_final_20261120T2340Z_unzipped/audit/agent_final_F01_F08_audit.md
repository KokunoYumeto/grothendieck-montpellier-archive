# Whole-proof audit of final draft F-01--F-08

Reviewer: `/root/tensor_norms`, GPT-6 Astra Pro (inherited); effort not exposed. Run `GCT_GINEQ/tensor_norms`. Timestamp: 2026-11-20T23:32Z. The actual statements, complete proofs, relevant conventions, and intervening consequences in `deliverable/GCT_GINEQ.tex` were read. This is not an audit based merely on intermediate notes. No formal theorem prover was used.

## Result

All eight mathematical proofs pass. F-07's current statement needs `B>0` explicitly, since B=0 otherwise satisfies the coefficient bound but makes its denominator undefined. Adding `delta>=0` is also appropriate. This was reported to root immediately. The F-07 check below is therefore conditional on that small statement correction; no unqualified final-statement PASS is claimed for the uncorrected snapshot.

## Detailed checks

### F-01

Read and checked the support reduction, both norm equalities under support projection, orthonormal expansion, Cauchy--Schwarz, spectral test vector, and minimization over the omitted factor. The mode-minor argument works for complex border rank and real Euclidean border rank. The final ceiling does not exceed the integer maximum mode rank. The special use of a real nuclear norm to bound complex border rank of a real tensor is justified here by the support bound and field-independent matrix ranks, not by false real/complex nuclear equality. **PASS.**

### F-02

Checked the integer positive simple-tensor cost, minor extension to the border locus, all three singular-value inequalities, directions of certified lower nuclear/upper operator estimates, and integer ceilings. The preconditioning saturation is valid: scale the nonzero left singular directions by inverse singular values and leave the complement fixed. This is an invertible map, preserves the rank cost on every pure tensor, and makes all three matrix ratios equal rank. The block-PSD witnesses have correct dimensions, complex adjoints and dual pairings. **PASS.**

### F-03

Reconstructed the singular spectra for all five target families. Matrix multiplication rows have pairwise disjoint supports of size n. Row tensor blocks have dimensions k! by (n-k)! and constant/sign-factorized entries. Polynomial tensor blocks have dimensions (k!)^2 by ((n-k)!)^2 and coefficients of magnitude 1/n!, yielding singular value 1/binom(n,k) with binom(n,k)^2 blocks. Determinant shuffle/matching signs factor and do not change singular values. All bounds follow by CP minors, and symmetric border-rank consequences use only CP<=symmetric. **PASS.**

### F-04

Checked full symmetric spectral maxima, complex Hadamard/CLL use, coefficientwise sign averages, every n!, n^n and n^(n/2) normalization, and equality via duality with Hilbert norm one. Global sign redundancies preserve each weighted power in both parity cases and reduce the term counts by factors two/four exactly. The decompositions are real with scalar coefficients, so their nuclear upper bounds apply over both fields. **PASS.**

### F-05

Checked the grouped matrix-unit identification of matrix multiplication tensors and rank submultiplicativity without assuming general injective/nuclear norm multiplicativity. All three ratios equal n^3, so powers give 8^k versus 7^k. Recomputed every determinant/permanent ratio and its quotient by the stated decomposition upper bound. The recurrence for A_n has the correct factor1/2 and the uniform lower ratio9/8. Derksen's source locator is now correctly unnumbered. The ordinary rank bounds imply the stated border-rank failures. **PASS.**

### F-06

Read and checked the entire slice-pencil proof that W has rank three over both fields. A rank-two decomposition would give two independent rank-one slice directions, but det[[y,x],[x,0]]=-x^2 has only one. The two factors of T_t remain independent for nonzero t, giving exact rank two; its limit and nonzero mode minor give border rank exactly two. Recomputed the Frobenius norm/difference, strict spectral bound61/50 at t=1/100, and rational ratio7500/3721>2. The distinct real/complex nuclear norms and order of a,b,c are correctly retained. **PASS.**

### F-07

The proof is valid for U,B>0 and delta>=0. Triangle inequality and Cauchy--Schwarz give the stated clipped numerator. Bounded total term norms yield individually bounded pure tensors; that bounded cone section is compact in both fields (complex phases are absorbed in a unit factor). Padding by zeros and simultaneous subsequence extraction gives a forbidden rank-r limit. The convex hull of the unrestricted rank-one cone is indeed the whole tensor space. **Proof PASS; statement requires explicit B>0 before final adoption.**

### F-08

Checked the complete support-restricted SVD argument and its complex conventions. A flattened pure tensor preserves product norm, giving the first nuclear inequality; grouping test vectors gives the first spectral one. Each reshaped right singular vector has matrix nuclear norm at most sqrt(min(q2,q3)) times its Hilbert norm. Expansion gives the upper nuclear bound, and matrix operator/nuclear duality on a contraction gives the upper spectral bound. Both source counterexamples use e tensor I_m and I_m correctly; the repaired denominators are nuclear and Frobenius respectively. This is an independent valid proof of the final comparison despite the cited source defects. **PASS.**

## Snapshot hashes and completed check events

Each hash covers the text from the indicated finding's beginning to the next finding's beginning, hence includes its full proof and intervening discussion. All events are completed **targeted proof checks** by the reviewer specified above, at 2026-11-20T23:32Z.

| ID | SHA-256 of audited section | Outcome |
|---|---|---|
| F-01-finaldraft | a71221ab7af7d18248a03bb1cee83fe550248f49047d6ab207c7f859f4863847 | PASS |
| F-02-finaldraft | 26dbb54064c2cf28f7061b29c842d3759a8f5d0d549ead72f017cf0563af21b4 | PASS |
| F-03-finaldraft | bba12b6eef6b6f1cd477791826fbb719e9cdd385b4c556f80f2341220965f688 | PASS |
| F-04-finaldraft | 1bdbc10536e9c769bf7d4b2035e43d8046bad26f1af7b2b593409368875a4ea9 | PASS |
| F-05-finaldraft | 18224c7ee86f47e3ed5ffe25fcd13efc07d53be1ecee66e60eeb2f24b3edcc4c | PASS |
| F-06-finaldraft | 431fd99b77bac03bac5965586a2765080ec7b71508a905e11ee0e834ed9c50c2 | PASS |
| F-07-finaldraft | e2bff2aa75d4f58c1c4d1f4388e5da5d14efbf5a3d8d48ddb8864381459a4b6e | Proof PASS; explicit B>0 statement correction requested |
| F-08-finaldraft | 29b0b5214df49ae1621c879156e957786773796e4498fc6077b3d19cb3009daa | PASS |

No main TeX or other root deliverable was edited in this audit.

## F-07 correction verified in the actual draft

At 2026-11-20T23:35:03Z I observed `B>0` and `delta>=0` in the actual F-07 statement and reread its complete statement/proof. **F-07 now passes without a pending qualification.** Hash of the same finding-to-next-finding section is `106d91fbba100c705eabd2f0830084c67baaa0c2db1889a2e293fad86de86dde`; hash of just its finding and complete proof is `614a5fb2ab28e0b0ee5b4adfa73964c6a1822e2fea5db86a9dbe1d07fb2d46bd`. Actual event: targeted proof check, same model/effort/run as above. The earlier event remains as the truthful record of the uncorrected snapshot and the correction request.
