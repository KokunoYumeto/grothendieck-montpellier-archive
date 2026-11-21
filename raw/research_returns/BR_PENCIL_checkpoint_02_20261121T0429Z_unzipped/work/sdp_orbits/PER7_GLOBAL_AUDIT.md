# Global permanent seven-plane coverage audit

I read the entire `work/root/verify_per7_global.py`, using the independently audited determinant verifier's exact determinant and Koszul-entry routines, and read the complete P-13 and P-16 manuscript proofs. P-15 and P-19 were separately read in full and independently replayed.

The verifier constructs all1152 distinct row/column permutations and transposition actions, computes each listed representative's complete orbit, verifies the declared orbit size, and checks disjointness. It enumerates every one of binomial(36,7)=8347680 coordinate subsets independently and checks that each support of size below14 belongs to the covered set. Thus the1517 listed low-support orbits cover exactly1543608 low-support subsets; the other subsets have ordinary flattening rank at least14 because the matching slices have zero common kernel on their union of variables.

The1517 representatives are1503 A-Koszul cases,3 B-Koszul cases, and11 explicitly mapped prolongation dependencies (P-13 five, P-16 three, P-15 two, P-19 one). The source checks each coefficient as+1, the correct exterior insertion signs, the pure-tensor cost, nonzero modular minors, and disjoint output-weight blocks before summing ranks. It reuses no search code. The reported6041 verified modular minors are consistent with these case types. I inspected the completed PASS report; this event is a whole-code/proof audit, not an additional independent replay of that exhaustive report.

P-13's268 quotient choices split into254 saturation exclusions and14 line blocks. The4275 zero-pattern tests equal9*binomial(7,3)+5*binomial(12,5); the increments5 or8 give ranks79>78 or144>143. P-16's3522 choices split into3424 saturation exclusions,97 line-pair exclusions, and one conditional enlarged-base exclusion. The last bound125+6=131>130 is correctly based on the enlarged U0, not the original U. All permutation and transposition actions preserve the permanent residual tensors up to product isomorphisms; no permanent Borel invariance is assumed.

With these checked dependencies, the global coordinate cover and P-01 prove the characteristic-zero minimum m7=14, using the anchored seven-edge construction for the upper bound. Generalized substitution gives36-7+14=43 for the permanent4 tensor. Propagation gives m8=15 and m9=16 with the matching anchored constructions. The modular/exact-rational proofs do not by themselves extend this43 claim to every positive characteristic.

## Actual replay and final R-10 proof review — 2026-11-21T04:10:42Z

The complete global verifier was subsequently replayed in this agent turn and returned PASS for all6041 minors and all8347680 coordinate subsets. The final actual `work/root/per7_global.tex` was read in full; every step of R-10, including μ8/μ9 propagation and the symmetric border-rank consequence, passed the whole-proof check.
