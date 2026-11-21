# Independent whole-proof review: A27

- Date: 2026-11-21.
- Reviewer: GPT-6 Astra Pro; reasoning effort not exposed; `/root/effective_galois`.
- Source: `work/row_audit/RANK_ONE_AUGMENTATION_OBSTRUCTION.tex`.
- SHA256: `35e6cd0752198cbcd1e93eb634a44167007978c80d2a9568f2e2ba286c97acfd`.
- Scope: complete statement, all four proof steps, finite table, certificate source and output, and the final scope paragraph.
- Outcome: **PASS**. No mathematical gap found. This is not a formal proof-assistant verification.

## Exact conclusion

For the displayed genus-two, 2-rank-one curve over F4, every finite constant extension and every odd prime for which 2 is primitive satisfy |J(F_Q)/rJ(F_Q)| < #C(F_Q). Thus neither sufficient numerical size test of A26 can hold on this curve over any constant extension. This does not show that all actual rational relative-class-number witnesses fail, and it does not exclude geometric theta witnesses or primitive-zero covers. The written statement preserves these distinctions.

## Complete proof checks

### 1. Genus, rank, finite counts and Frobenius polynomial

The Artin–Schreier rational function has precisely the two reduced geometric poles of odd orders 3 and 1, at infinity and zero. The genus is two and the 2-rank is one; each pole has one rational point above it. The two displayed point counts, 6 and 28 over F4 and F16, produce the quartic T^4+T^3+6T^2+4T+16 with the stated signs. Its product decomposition into A(T)=T^2-T+4 and B(T)=T^2+2T+4 is exact.

The two trace recurrences and the formulas |J(F_Q)|=e_m h_m and #C(F_Q)=Q+1-t_m-w_m follow from that quartic, without an elliptic isogeny classification. Both quadratic factors have roots of complex absolute value two. The induction t_m=1 modulo 4 for m>=1 is correct, including its m=1 anchor; hence 4 divides e_m. Positivity of e_m is also ensured by its two Weil roots.

### 2. The rational torsion bound uses no semisimplicity assumption

For r>=5, the resultant of A and B is 36. Their coprimality modulo r splits the full four-dimensional r-torsion representation into two two-dimensional primary blocks. This remains valid at r=5, where A has a repeated root: no diagonalization is required. On the B block, (T-2)B(T)=T^3-8 gives F^3=8 exactly.

A nonzero F^m-fixed vector on the B block therefore forces r-1 to divide 3m for an eligible prime. If the rational torsion rank is at least two and the B block has no fixed vector, the entire two-dimensional A block is fixed. Its determinant is 4^m, so r-1 divides 2m. In either case r<=3m+1. The finite abelian-group identity |G/rG|=|G[r]| and the geometric rank bound at most four are correctly used.

### 3. Every extension degree from ten onward

The anchor 31^4=923521 < 1044481=L_10 is correct. The lower bound L_m grows by a factor greater than four, while (3m+1)^4 grows by a factor smaller than two for m>=10. This proves the uniform strict bound for all subsequent m, not merely sampled exponents.

The prime 3 is separately handled by |G/3G|<=81, so the exceptional resultant prime is never passed through the coprime-block argument. Rank zero gives quotient size one. At rational rank at least two, the block bound and growth inequality finish the proof.

At rational rank one, an eligible odd prime dividing e_m is at most e_m/4 because 4 divides e_m. The displayed strict comparison with the curve lower bound is equivalent to 3(s^2-6s+1)>0, valid for s=sqrt(Q)>=8. If the prime does not divide e_m, it divides h_m. The determinant of 1-F^m on the B block is h_m modulo r, so that block has a fixed vector, and the earlier order bound applies. These cases exhaust all possibilities.

### 4. The nine remaining extension degrees

The table records all eligible prime divisors of the exact Jacobian cardinality, not merely a selected set. For such a prime, r^min(4,v_r(|G_m|)) is a valid upper bound for the quotient size; for a prime not dividing |G_m|, the quotient size is one. Every displayed upper bound is strictly below the corresponding curve count. Thus the finite table completes the all-extension proof.

## Primary inputs independently reopened

1. Pries–Zhu, *The p-rank stratification of Artin–Schreier curves*, Annales de l'Institut Fourier 62 (2012), Lemma 2.6, printed p.712, including the preceding lower-jump setup and its short proof. The cited formula applies over an algebraic closure; the displayed poles and their unique points above them are individually rational here.

   https://www.numdam.org/item/10.5802/aif.2692.pdf

   Web references: `turn111332570view0`, `turn982868494view0`.

2. Milne, *Abelian Varieties*, author version 2 January 2022, Theorem 19.1(a)–(c), printed pp.40–41, and the following proof identifying rational point cardinality with the determinant of 1-F^m.

   https://jmilne.org/math/xnotes/AVs.pdf

   Web reference: `turn982868494view1`.

## Certificate review and execution

I read the entire supplied second implementation `verify_A27_independent.py` and the complete supplied JSON certificate. It uses direct enumeration of affine y-solutions, a quartic companion matrix, exact Bareiss determinants, complete trial division, and direct order iteration. It imports none of the exploratory census implementation. The chosen quartic defining F16 has no linear factor and is not divisible by the sole irreducible quadratic over F2, so it defines the required field; u=z^2+z has u^2+u+1=0. The code counts both ramified points separately.

I copied the checker into `work/effective_galois/A27_certificate_rerun/` and executed that copy. It passed and produced JSON identical to the supplied certificate. Exact execution record:

`work/effective_galois/A27_certificate_rerun/EXECUTION_RECORD.json`.

- Script SHA256: `bb48c6297c8fe5ebeb5c74a3913b8ec9ce110cae4f29c60d24f483c7b20619f1`.
- Output SHA256: `7c3f28efd6ab0b4a000a2b6b43563e0c8762d2a390e1edfc63f30168ad951d16`.
- Executed at 2026-11-21T03:11:27.189960+00:00.

This is an independent execution of the supplied second implementation, not a claim to have authored a third independent implementation. It checks the finite inputs and anchors. The all-extension induction and Frobenius-block proof were checked by mathematical reading, not by the finite computation.

No canonical TeX, final proof source, or build artifact was edited.
