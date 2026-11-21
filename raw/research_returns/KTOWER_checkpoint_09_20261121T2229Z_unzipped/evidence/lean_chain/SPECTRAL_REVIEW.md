# Independent reflection and spectral-decomposition review

Date: 2026-11-21 UTC. Reviewer: `/root/lean_chain`, GPT-6 Astra Pro; effort not exposed.

## Verdict

**PASS.** I read the entire 107-line `character_trace13.py`, its entire 137-line `character_trace.py` dependency, and the entire 175-line `check_spectral_split.py`. I read the complete new KT-U3-SECOND13 proof in `unitary_results.tex` and the full spectral factorization corollary KT-E.4–KT-E.5 in `endoscopic_converse.tex`. The latter rests on the global exhaustion proof separately reviewed in `ENDOSCOPIC_CONVERSE_REVIEW.md`.

I freshly executed byte-identical copies of all three programs in this review directory. Both character output JSON files are byte-identical to the author's files. All 30 degree-prime pairs, e=2,4,...,30 and p=7,13, reproduce every polynomial coefficient, comparison value, dimension, and independent trace. The only differences in the spectral report are its new timestamp and the relocated path metadata for the independently generated low-degree inputs. All original input-file hashes were reconciled. Exact hashes and the complete comparison result are in `spectral_replay_reconciliation.json`.

## Reflection proof and normalization

The five vectors have norms 1, 2, 4, 3 and 5. For each, the displayed coefficient `(eta*bar(pi)-pi)/n` is an Eisenstein integer. The rank-one projector expression gives numerator eigenvalues eta*bar(pi), pi and pi, so its Gram matrix is 13 times the identity and its determinant is eta*pi^2*bar(pi). The program checks both identities directly in integer pairs and verifies the nonzero reduction has exactly the prescribed image line.

At pi, the determinant valuation is two and the reduction has rank one, forcing elementary-divisor valuations (0,1,1). Dividing the numerator by pi therefore gives the required minuscule valuations (−1,0,0). At the conjugate prime the unitary relation fixes the conjugate local behavior; away from 13 the matrix preserves the integral lattice. The same center-trivial coefficient and Satake normalization used in the previously reviewed p=7 proof therefore apply.

The six Eisenstein units reduce to the nonzero squares of F_13, while 1−omega reduces to the nonsquare 5. Support-one lines, the two support-two ratio classes, and the two support-three square-class patterns give disjoint orbit sizes 3,18,18,36,108. Their sum is 183, and the program separately constructs every projective line and proves exact set equality. No archived neighbor list is imported.

For a numerator A with A* A=pI, the scaled harmonic character is `Norm(h_d(A))−p Norm(h_(d−1)(A))`. The complete-homogeneous recurrence uses the exact elementary symmetric functions, and averaging `A*gamma` over all 1296 group elements is the invariant-space projector trace. The trace is constant on each group orbit of neighbors, justifying the orbit multiplicities. This checks the mathematical meaning of the computed integers, in addition to their successful execution.

Fresh results include 13^3*T13=54291 on the one-dimensional degree-three module and 13^5*T13=6110859 on the one-dimensional degree-five module. The p=7 replay also returns 7^5*T7=157899. The traces through degree thirty are saved in this directory's `character_trace.json` and `character_trace13.json`.

## Exact polynomial semantics

The program uses descending coefficient lists consistently. Its monic division subtracts each leading multiple and then checks both zero remainder and exact multiplication. Its square-root recurrence determines each new coefficient by the linear term 2*r_i, checks divisibility by two, and finally multiplies the entire proposed root by itself. Thus the check examines every coefficient, not just a trace or a candidate factorization.

The shift routine implements f(X+n) by Horner evaluation. With n=−p^e, roots a_p become a_p+p^e, which is the required normalized endoscopic compact eigenvalue. The CM eigenvalue is pi^(2e)+bar(pi)^(2e); it is removed exactly when 3 divides e. In that case 2e is divisible by six, so its value is unaffected by the choice of unit in the prime generator. The remaining classical polynomial is an exact square because the non-CM forms occur in two-element quadratic-twist pairs and the test primes split.

The shifted square root divides the full compact polynomial exactly. The quotient has the proven stable degree and nonzero comparison value at p^(2e)+p^e+1. Every full compact trace agrees with the independently constructed character average, and all expected pairs are present exactly once in the original report. The e=26,28,30 stable dimensions are 76,96,116 respectively, from full dimensions 84,105,125 and endoscopic dimensions 8,9,9.

## Limits of the check

The characteristic polynomials supplied by the archived harmonic and classical calculations remain input data whose full certificates and coverage proofs are separate. This new calculation does not recompute those full operators. It independently reconstructs the reflection traces and verifies the complete integral polynomial splitting, while the separately reviewed global packet theorem identifies the quotient as the stable spectrum. It does not infer that every stable eigenform is an actual admissible source for the deformation problem, and it supplies no all-weight assertion about residual prime support.

All actual executions and the proof review are recorded separately in `CHECK_EVENTS.tsv`. No Lean kernel build is claimed.
