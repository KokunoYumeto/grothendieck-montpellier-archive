# A39 independent complete-proof and certificate review

Date: 2026-11-21 UTC. Reviewer: GPT-6 Astra Pro; effort not exposed; /root/effective_galois.

**PASS.** I read the entire written proof, the complete301-line producer and the complete182-line independent verifier. I then reran the independent verifier successfully in an isolated copy at work/effective_galois/A39_review/. The producer was not rerun; no third arithmetic implementation is claimed. The verifier output is byte-identical to the author's output.

## Exact material

- Final TeX SHA256: a083a76b7d7c0cb89bc99f8f15f65169dcae79ac2a89fe7198e5dd35cbfec247.
- Initial whole-read SHA256:7657591197d52d023d2610113208496497b6cc1f956a188bdd0f6372a697dadd. The final version adds the odd-order normal-closure sentence; that delta was separately checked and passed.
- Producer code SHA256:daaf8c6f2423573d0014d044d376ce9fdc0acdd821649c4e8e75b8edb42fab72.
- Certificate data SHA256:916b5a3ca3eda1bfdd1fc430b81a6d9671f92df6f70139ee04e1cfdc88a34e9d.
- Independent verifier code SHA256:7144c3b7bbf0b1f0f13c628d16d8a2c8c6a4eec97e8fa9d3f717bc0877baed06.
- Successful replay JSON SHA256:5c3d7beab4548818e5a2b982681d7a8e121ad0f1cf4102e42e40d1da4107d67b.
- Command: python verify_A39_pointed_certificate.py, working directory /workspace/scratch/63b175cc138c/work/effective_galois/A39_review.

## Whole mathematical proof checks

1. The retained field and h,f,U,V,A,B arrays match exactly the stated A36 curve and RPT.1 polynomials. The norm, branch congruence and gcd condition put all five zeros at each point of D0. The degree-five monic A term has pole order ten at infinity, whereas BY has pole order at most nine. Thus div(F)=5D0-10Ws. The previously checked nonzero exact-five class implies geometric connectedness; the valuations imply etaleness. The split infinity normalization fixes the constant twist, and the unique rational five-torsion subgroup identifies the cover with A36 up to generator. The reflection preserves the equation, is involutive and inverts the deck group. Both specified fixed lifts are rational: at infinity z/X tends to1, while at the finite branch z=92 satisfies z^2=224 and z^5=188.

2. The Artin--Schreier jumps1 and3 give different2P+4Q on the reflection double map. Combining its canonical-divisor formula with K_C~2Ws yields RPT.5. Pullback on geometric degree-zero classes is injective: a function with invariant principal divisor transforms by a constant c satisfying c^2=1; in characteristic two c=1, so the function descends. This proves the theta-characteristic identity for B0 and both formulas RPT.6. No identification of B0 with the Raynaud characteristic is needed for canonical classes.

3. The complete Riemann--Roch space is correctly identified. Its bounding divisor32*pi^*Ws is deck-invariant, so character projection preserves the bound. A coefficient of z^i may have finite poles only of order at most i along D0. Multiplication by U^i clears them; the resulting function belongs to the smooth affine ring k[X,Y] and has unique form A_i+B_iY. The opposite-branch congruence is exactly the missing regularity condition. At infinity z^i/U^i has zero order2i; the pole orders2 and5 of X,Y have opposite parity, preventing leading cancellation. The bounds are therefore deg(A_i)<=16+i and deg(B_i)<=13+i. The remainder condition and division by U^i give the31 displayed basis vectors for each character,155 total. This also agrees with degree160 and genus6 by Riemann--Roch.

4. The local formulas were checked directly. With t=Y/X^3, S=t^2a, the curve equation gives the displayed implicit equation for a; division of F by X^5 gives the Z equation. At Q, Y is a parameter because the X-derivative is u. All four implicit derivatives are units, so residual identities with initial values uniquely certify the series through degree127. A principal32-fold pullback of Z_Rt would be regular at P and vanish to order128 at Q. These are exactly32 coefficients of t^32f and128 coefficients of f, on the complete155-dimensional space. Full rank155 over F256, independently checked as binary rank1240 of the1280-by1240 block matrix, excludes such a function even geometrically.

5. Each summand of the positive function is regular away from the fibre over Ws and has pole order at most two there. The independently verified expansions give exact zeros of order four at P and Q, leading coefficient189. The function is nonzero because its first character component is225z. The remaining four potential poles have degree at most eight, equal to the known zero degree. This proves its exact divisor, so2Z_Rs=0 and kappa_Rs=0. A genus-two point with canonical divisor2R is Weierstrass.

6. Since2 is inert in O5, each nonzero cyclic summand of the finite two-primary O5-module contributes two dimensions to the group killed by two. Geometric rank two permits one summand; its order2^10 gives exponent32. Thus the certificate32Z_Rt!=0 forces a nonzero three-primary canonical component. The correspondence relations give RPT.13 on the three-primary part. The identities (2-T)(T+3)=5 and (1-T)(T+2)=1 make both operators invertible there, proving the same component for both other Ws-fibre images. The three-adic O5 ring is unramified quadratic, and a module of order3^4 has exponent at most nine. A29 therefore supplies a degree-three or degree-nine detector over the same field, with the prescribed image split.

7. Pullback along the degree-two reflection map is geometrically connected by coprimality and remains etale. The composite degree over C is15 or45. A lifted collision pushes to equality at the useful reflection image by A29. Its two possible preimages project to hyperelliptic conjugates on C, which coincide for the source Weierstrass point. The useful lifts Q for Wt and sigma P for Ws therefore exclude every distinct original collision. The final added sentence also checks: the geometric normal closure of a cyclic-m cover above the cyclic-five cover embeds in C_m wr C5, hence has odd order. The composite need not be Galois, but lies in the required pro-odd framework.

## Computational scope and conclusion

The independent verifier imports no producer arithmetic. It uses polynomial-product/long-reduction field multiplication, Newton inverse series, reconstruction from residual identities, and binary block rank. Its replay confirmed every residual, the complete matrix and positive function. I explicitly checked the retained coefficient arrays against the theorem before execution. This is an existing independent-verifier replay plus a complete mathematical check of what the matrix means. It is not a third implementation or formal proof-assistant verification. The final result remains a fixed-example pointed success, not a universal pointing theorem.
