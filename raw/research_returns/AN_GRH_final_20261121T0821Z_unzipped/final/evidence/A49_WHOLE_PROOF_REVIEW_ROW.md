# A49 entire-proof and finite algebra review

Date: 2026-11-21. Reader: GPT-6 Astra Pro, AN_GRH `/root/row_audit`. Effort is not exposed.

## Version and verdict

**PASS, targeted proof check.** I read the entire source `work/gt_certificates/positive_rank_theta/A49_ODD_QUOTIENT_FOURIER.tex` at SHA256 `f109d30ce9a5c199b6e41d59e53af7cbed2d5cbaa4ac1c7151e39595d82a4e88`.

The sole subsequent source change makes the opening separation conclusion explicitly conditional: “When these equivalent conditions hold”. I requested and read that exact correction. The final checked hash is `5fecbadc1de4120af3591d0f760591a02fd1ccc3d01927fc898e9e922fa24483`. The mathematical proof did not change.

This is a complete separate-reader proof check, not an independent re-proof, computer formalization, or new curve enumeration.

## All proof steps checked

1. For each cyclic quotient of the actual rational Jacobian quotient, the Lang isogeny Φ−1 factors through the indicated constant subgroup. Pullback along the based Abel map is geometrically connected, and its zero fibre makes the cover P-split over the original field. No constant extension is hidden in the argument.
2. The genus-two polynomial is exactly 1+SχT+qχ(κP)T². The point sum has the stated canonical-class symmetry. The actual image of the integral primitive projector has the faithful-character Frobenius factors, so its finite-field order equals their product. Reduction at one fixed prime above p tests the rational integer product; nonzero reduction of every factor is equivalent to its order being prime to p.
3. Unit reduction from modulus n to every divisor m is surjective. Coefficients in Fp propagate vanishing/nonvanishing by the p-power operation. The quotient kills κP, so the hyperelliptic involution gives equality of inverse-character values. The signed generating hypothesis therefore controls every faithful character of the chosen cyclic quotient. No assertion about proper-conductor factors is inserted.
4. Fourier inversion is valid because p does not divide |H|. All nontrivial values vanish exactly for the uniform augmentation component. The converse direction of the stated equivalence also follows directly from a faithful nonzero value. If |H|>N and p does not divide N+1, an empty nonzero coset witnesses nonuniformity: P already occupies the zero coset, so the additional delta at zero does not add an occupied coset.
5. The final use of A46 has its hypotheses: geometrically connected odd cyclic degree prime to p, actual primitive rational p-primary group zero, and a prescribed rational lift over the original field.
6. The original-field seven and nine comparisons use retained actual curves. For the A27 curve, |J(F4)|=28 and N=6 give H=C7; signed powers of two exhaust its units. For the A45 twist, |J(F4)|=18 and a rational order-nine class give H=C9. Its two Weierstrass points have zero odd label; its remaining two points have opposite unit labels modulo nine. The conductor-three factor has order36, while the faithful conductor-nine product is321²=103041. Thus a primitive factor can pass although the full relative class number remains even.

## Sources and retained data actually read

- Recovered A1 `B.2`: complete statement and proof, including Riemann–Roch truncation, character factorization and reduction. Retained file `recovered/ANABELIAN_A1_cp03_text/ANABELIAN_A1/ANABELIAN_A1_paper.tex`.
- Recovered successor final `A.10`, `A.26`, `A.35`: complete statements and proofs, including the prior Fourier/empty-coset argument and canonical symmetry. Retained file `recovered/ANABELIAN_SUCCESSOR_final_text/ANABELIAN_SUCCESSOR_paper.tex`.
- Current A29: complete polynomial derivation and canonical symmetry PC.6–PC.7, read in its wider proof context. These established formulas are credited rather than presented as a new A49 discovery.
- Milne, *Jacobian Varieties*, Proposition9.1, printed p.30, relevant displayed proof and prime-to-characteristic supporting discussion pp.30–31, reopened directly in the primary PDF: https://www.jmilne.org/math/xnotes/JVs.pdf . Its separably closed-field statement applies after geometric base change, yielding the claimed geometric connectedness.
- Current A45 strict39 text ND.12–ND.19 read, including original/twist Frobenius on the order-nine subgroup and the four rational points. The independently retained Cantor JSON `work/row_audit/verify_A45_conductor39_cantor.json` was inspected for the exact generator, full nine-cycle, Frobenius actions and point labels. No new Jacobian arithmetic rerun is counted in this review.
- A27 current statement and RO.3–RO.4 checked for the rational counts and polynomial.

## Exact finite replay

I read the entire small checker `verify_A49_finite_algebra.py`, SHA256 `dec18039d196f659a3b155c4135360523fc3558a3fca09d6e2cf914b5c1f4dbb`.

An unchanged copy was run under `work/row_audit/A49_review/`. It reproduces byte-identical JSON SHA256 `44b2784778c7fd5a175c7fa759d13bb66ea0a6be859ed561ee790e309582a73e`.

The checker verifies the signed orbit modulo7, the full power orbit modulo9, the identity s³−3s+1=0 for s=ζ9+ζ9⁻¹, and the multiplication determinant for7+s. The latter is103041; the proper conductor-three product is36. Its exact integer fraction-free determinant implementation was read. Its scope is finite algebra on retained labels, not point enumeration or an independent new Jacobian implementation.

## Limits preserved

A49 is an exact test for an actual quotient with the displayed hypotheses. It does not supply those hypotheses universally, remove the canonical-kernel requirement, or derive finite-field incidence from Artin density or number-field GRH. The retained examples already have other witnesses in this run. This review does not count them as proof that the universal unresolved existence gate has shrunk.
