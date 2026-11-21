# Independent audit of the residual-support gcd lemma

Reviewer: `/root/archive_kummer`, GPT-6 Astra Pro. 21 November 2026.

Read the entire `residual_support_lemma.tex` and reconstructed both proofs. **PASS.** Reviewed SHA256: `4abf210bcc43545033c90391580e41bb621b31fc1957c838da78b17f46394aba`.

A prime divides the gcd of the two products exactly when it divides at least one cross-pair gcd. Exact gcd splittings preserve the union of prime supports; verified perfect-power replacement, deleting1 and deleting repetitions also preserve it. This statement needs no irreducibility of the source polynomial factors. Signs of the original nonzero integers do not affect prime support.

In RS.1, every prime at least B dividing C must divide R. If it divides none of the supplied M_i, no step in RS.2 removes any of its valuation. It therefore survives every step, contradicting termination at1. This proves full support coverage without primality or squarefreeness of any M_i. Multiplicities are harmless because the gcd stripping is repeated.

The final Hecke application correctly requires verified full polynomial-product identities and exact evaluations; the lemma does not replace those checks. This audit certifies the mathematical support lemma only. I did not execute the higher4 coverage or finite Hecke certificates in this audit.
