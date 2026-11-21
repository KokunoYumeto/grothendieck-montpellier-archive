# A44 — complete proof and finite-verifier review

Date: 2026-11-21. Reviewer: GPT-6 Astra Pro, `/root/row_audit`; effort not exposed.

Source: `work/gt_certificates/positive_rank_theta/A44_PRO_TWO_TOWER_OBSTRUCTION.tex`.

First complete version read: SHA256 `d1e97e8250896fbbbf6801cc1caa94e6dee85b0092199ccaad17997f66a71e3e`.

Final version checked: SHA256 `d7ef05d824572383a63e35a89eb8d74f51d2f6a0e28bf2c7d326cabed15fb01a`.

**Result: PASS.** I read the complete statement, every one of the six proof steps, the exact-order-three illustration and its entire divisor argument, and the concluding scope. The final version adds the exact Milne Proposition12.9 citation. This is a separate-reader targeted whole-proof review and a finite-verifier rerun, not an independent re-proof or formal verification.

## Critical mathematical checks

### Fixed nonzero integers

The displayed factorization has the correct coefficients: `a=(1+epsilon*q)s`, `b=epsilon(1+q²+q*s²)` and coefficient of T equal to `-qa`. Squaring the first equality eliminates s without division modulo any odd prime. Over Q, `D_epsilon=0` gives the same factorization because `1+epsilon*q` is nonzero. Its first quadratic would have root product of absolute value one, contradicting the Weil root absolute values. Thus the finite integer whose prime factors are used is nonzero for every surface in the statement.

### All late-appearing prime cases

An eligible prime first appearing at level `2^m`, with `m>=5`, supplies a Frobenius eigenvalue of exact order `2^m`. The argument only requires semisimplicity on the kernel of the separable polynomial `T^(2^m)-1`, not on the full torsion representation. The eigenvalue degree is a power of two at most four. Eligibility excludes primes congruent to one modulo eight; the valuation of `ell^4-1` excludes residues three and five. Degree one is then impossible.

In degree two, the norm of the eigenvalue is epsilon equal to plus or minus one. I checked every possible overlap with the reciprocal pair. An overlap gives either `q=epsilon` or `q=lambda²`, and in the latter case conjugation sends lambda to minus lambda, so `epsilon=-q`. In both cases the prime divides `q²-1`. Without overlap, the four roots exhaust the Frobenius polynomial and yield exactly `D_epsilon=0` modulo the prime.

In degree four, the two-adic valuations of `ell+1` and `ell²+1` give norm minus one. The full degree-four minimal polynomial has constant coefficient `q²`, so the prime divides `q²+1`. These cases exhaust all late-appearing eligible primes; early levels divide the field-degree-sixteen group order.

### Every primary exponent, not just prime torsion

The length of a rational torsion point's Frobenius orbit is a power of two and divides the order of the Frobenius matrix modulo the relevant prime power. The reduction kernel of GL4 at an odd prime is a group of odd prime-power order, so it introduces no further two-part. This proves the displayed single finite-field bound for all primary exponents. Surjectivity of reduction of units shows that a signed-unit-compatible composite order can only use individually eligible primes. The proof therefore establishes the claimed finite group, not merely a finite list of possible primes.

### Infinite odd theta torsion is a separate valid assertion

For each two-adic unit Frobenius root, its residue either never becomes one under repeated squaring or is already one. In the latter case, positive valuations double below one, pass above one, and then increase by one at each squaring. Nonunit roots contribute zero to the point-count valuation. Reciprocal pairing bounds the number of unit roots by two, including multiplicities. This proves the eventual exact affine growth of the valuation and hence the asserted growth of the rational two-primary group.

The varying-field Lang cover has degree d and genus d+1, so its exact Weil lower bound is the one in CT.13. The main term grows exponentially in `2^m` while d grows polynomially in `2^m`; the lower bound tends to infinity. This argument legitimately changes its counting cover at each field and does not import the incompatible fixed-primary degree condition of A42. Combining this unbounded count with the already proved finite eligible-support group gives the stated ineligible-prime conclusion.

### The finite-field illustration and the actual theta translate

The recurrence and point count give `#A(F_(2^16))=65760²=2^10*3²*5²*137²`, and the two fixed D values are -54 and -4. The eligible prime set is therefore exactly `{3,5}`. The identification of the Raynaud characteristic with `W0+W1-Winf` correctly uses all four geometric theta characteristics of an ordinary genus-two curve, the three effective Weierstrass ones, and ordinary non-effectivity.

For each indicated r and a0, the norm identity has a triple zero at r and simple base zeros at zero and one. The conjugate function is nonzero at R. At each ramified Weierstrass point the norm and its unique point above the base zero force vanishing order one. The function has pole order five at infinity. Hence the full divisor formula is correct; division by h² gives `3(R-B)`, and ordinary non-effectivity excludes the zero class. There are four distinct choices, all over F16. No completeness assertion about all eligible theta points is made.

## Code and exact execution

Read the entire verifier `verify_A44_finite.py`, SHA256 `b7b7893de0f79e6388bef93624927eb1252982e917ee015ba2f77c8bf0d61c43`. Copied it unchanged, together with its referenced RR-output JSON, to `work/row_audit/A44_rerun/` and executed it successfully.

The rerun output is byte-identical to the producer's verifier output:

`verify_A44_finite.json`, SHA256 `f62580bade6acd01f20fd3b88119be24dcea3c77dbdfaa4004175485a0344769`.

Executed scope: symbolic factor/elimination identities; all odd residues modulo `2^m` for `5<=m<=16`; the exact resultant and independent quadratic recurrence; factorization and eligible-prime test; the displayed norm and point equations. The verifier **reads but does not recompute** the separate 220-record Riemann–Roch probe. I did not rerun or independently reconstruct that probe. It is not needed for the written exact-order-three proof or the general theorem. This is a rerun of an existing implementation, not a newly authored arithmetic implementation.

## Primary input and review limits

Milne, *Abelian Varieties*: Theorem8.2 with its complete displayed proof and Remark8.4; Proposition12.9 with its complete printed argument (one auxiliary lemma refers to Lang); Theorem19.1 statement and its displayed point-count proof for (a)–(b); Lemma19.2 and its proof. These were reopened and read at https://jmilne.org/math/xnotes/AVs.pdf . The classical Weil absolute-value assertion is used as stated; no new proof of the full Weil theory or all external dependencies is claimed. Poonen Lemma6.2 was read in the preceding A42 review and is only a consistency citation here; A44 proves its own finite-group stabilization. The exact Raynaud sequence and ordinary-origin criterion were reread in Ozman–Pries §§8.1–8.2 during the immediately preceding A43 supplement check.

The result blocks one tower-based supply inference. It neither proves that its finite candidate set is empty for every curve nor settles the universal prescribed-point cover choice or towers of odd auxiliary degree.
