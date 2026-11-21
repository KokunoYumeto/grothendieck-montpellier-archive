# Asvin 2023: narrow independent scope review and two algebra checks

Date: 2026-11-21. Reader: GPT-6 Astra Pro; effort not exposed; /root/effective_galois.
Primary: Asvin G., On the variation of Frobenius eigenvalues in a skew-abelian Iwasawa tower, Algebra & Number Theory17(12)(2023),2151–2179, DOI10.2140/ant.2023.17.2151.
URL: https://msp.org/ant/2023/17-12/ant-v17-n12-p03-p.pdf .
Retained primary SHA256: 91b3604dd9da26101c4c1546e2acffd868794701810953bdb4774f3ecd7765e4.
Reviewed probe: work/gt_certificates/positive_rank_theta/FOX_FROBENIUS_SINNOTT_PROBE.md, SHA256 9007417edb41c7fe3ca0bfb52417a35ec11bd8c55fbbf1ff5ef9cea4f63bbb98.

## Primary passages actually read

Read Definition8, CaseB (pp2156–2157) and Remark9; complete Lemma17 statement/proof (pp2160–2161); all §3.1 including the finite power-series matrix and equation(6) (pp2166–2167); Definition25 and full statements of Theorems23/26; the first truncation paragraph of §3.3 (p2169). I did not read the complete long proofs of the congruence theorems or audit every earlier geometric premise.

The scope account in the sibling note passes. CaseB has geometrically connected pullbacks of multiplication by ell-powers and nonconstant deck Frobenius. Lemma17 uses coefficients Z_ell[[T_1,...,T_b]], not finite Laurent support. The return operator in equation(6) is the product over the whole growing Frobenius character orbit. The theorem congruences are at the tower prime ell. The truncation uses positive ell-adic valuation of a root of unity minus1 and can depend on the level. At p different from ell, every nontrivial ell-power root remains nontrivial on reduction, so its difference from1 is a p-adic unit. That exact truncation step does not transfer to characteristic-p exponent control. No fixed rational determinant or cross-prime exponent estimate is supplied by the inspected passages.

## Complete checks of the note's elementary algebra sections

Section4 was read and checked in full. The averages defining e_a are compatible under the finite cyclic quotient maps, including the boundary level n=a. They project to conductors at most ell^a. The orthogonal differences give all exact-conductor idempotents, and only finitely many survive at each finite level; hence arbitrary p-adic scalar coefficients define an element of the inverse-limit algebra. Multiplication by1−B is invertible when every exponent is positive. For the semilinear variant, the exponent automorphism fixes each conductor projector. Splitting the prime-to-p roots after an unramified extension turns each conductor into finite permutation orbits. Successive elimination gives the cokernel relation1−c_a^(d_a), and the stated binomial valuation for b_a>=2 holds for every p, including2. Unramified scalar extension preserves the exponents. These are correctly labelled abstract examples, without Weil weights, polarization or geometric realization.

Section5 was also read and checked completely. Normalizing a fixed nonzero rational function over a finite p-adic field gives two nonzero reduced Laurent polynomials after removing monomials. A primitive ell^a root has residue degree ord_(ell^a)(p^s); beyond the fixed polynomial degrees neither reduction vanishes. Thus the valuation stabilizes to the coefficient-content difference. Those residue degrees tend to infinity by the elementary divisibility argument in the text. For an actual fixed integral Laurent matrix with nonzero determinant, nonnegative elementary-divisor valuations then bound its cokernel exponent. The statement remains conditional on an identification with the actual primitive rational group; a level-varying orbit product does not satisfy the fixed-function premise automatically.

The other literature premises (finite profinite presentations, arithmetic Fox derivatives and Sinnott's rational-measure theorem) were not independently source-checked in this review. This is not a whole-note primary-source audit, a complete re-proof of Asvin's congruences, or a new geometric witness result. No computation was performed.
