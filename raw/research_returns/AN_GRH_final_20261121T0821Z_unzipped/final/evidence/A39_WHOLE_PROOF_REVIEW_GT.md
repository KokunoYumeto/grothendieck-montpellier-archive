# Independent whole-proof and certificate review of A39

Date: 2026-11-21. Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.

**PASS.** I read the complete A39 statement and all four proof steps at source SHA256 `7657591197d52d023d2610113208496497b6cc1f956a188bdd0f6372a697dadd`. I then read the final normal-closure scope addition at SHA256 `a083a76b7d7c0cb89bc99f8f15f65169dcae79ac2a89fe7198e5dd35cbfec247`. The latter was a targeted delta review, not a second claimed whole-proof read. Source: `work/row_audit/A39_POINTED_QUINTIC_TRANSFER.tex`.

## Complete mathematical checks

1. The norm and opposite-branch unit conditions assign all five zeros of F to the degree-two divisor represented by (U,V0). The monic leading A term gives the exact pole order ten at Ws. Exact order five of the divisor class, already certified in A36, gives a connected etale Kummer cover. The leading unit specifies a split rational point. Both chosen points P and Q are fixed by the stated reflection; its norm identity and the value 92 verify the second point.
2. The jumps one and three give different `2P+4Q`. Pullback of the base canonical divisor, with the four nonfixed points above Ws and the ramified point Q counted with their correct multiplicities, gives `K_E ~ 2(A_s-R_t)`. The argument proving injectivity of reflection pullback on geometric Pic0 is valid in characteristic two: the invariant principal function has scalar eigenvalue with square one, hence eigenvalue one. No inversion of multiplication by two in Pic0 is used.
3. The five-character decomposition and finite-pole restrictions give all of L(32*pi*Ws). At infinity, X and Y have pole orders two and five; the parity distinction prevents cancellation. Clearing U^i removes all finite denominator possibilities and the opposite-branch congruence is precisely the remaining regularity condition. Each displayed character basis has 31 functions, giving 155 in total (also equal to the nonspecial Riemann--Roch dimension 160-6+1).
4. The P uniformizer `t=Y/X^3` and Q uniformizer `t=Y` satisfy the displayed implicit equations with unit derivatives. Direct substitution gives the exact exponents in both local expansions. The 32 P constraints and 128 Q constraints describe exactly the possible function with the proposed principal divisor; a full-rank 160-by-155 matrix therefore excludes it.
5. The positive Rs certificate has at most a double pole at each of the five points over Ws, no finite poles, and certified zeros of order four at P and Q. It is nonzero because its first deck-character component is nonzero. Equality of total degrees forces its entire divisor, proving kappa_Rs=0 and the Weierstrass assertion.
6. The ordinary O5 action forces the rational two-primary group of order 2^10 to be a single cyclic module over the unramified quadratic 2-adic ring, hence exponent 32. Thus the negative RR result gives a nonzero three-primary canonical part at Rt. The identities on the other two fibre images, including `(T+3)(2-T)=5` and `(T+2)(1-T)=1`, prove that both have nonzero three-primary parts too.
7. The O5 module structure at three bounds the rational three-primary exponent by nine. Therefore A29 supplies degree three or nine. Pullback along the degree-two reflection map remains connected by coprimality; the pointed lift is rational. The final argument correctly allows an arbitrary lift above a source Weierstrass point: either reflection-fibre possibility still lies above that same source point. Thus degree fifteen or forty-five genuinely suffices for each of the two stated source points.
8. The final added scope sentence is correct: the composite need not be Galois; its geometric normal closure is an imprimitive subgroup of the wreath product `C_m^5 semidirect C_5`, with m=3 or9, and has odd order. This supplies the precise pro-odd cover scope.

## Independent finite checker: complete read and isolated rerun

I read every line of `work/row_audit/verify_A39_pointed_certificate.py`, SHA256 `7144c3b7bbf0b1f0f13c628d16d8a2c8c6a4eec97e8fa9d3f717bc0877baed06`. This verifier imports no producer arithmetic. Its field multiplication uses polynomial products and long reduction; its inverse series use Newton inversion; its rank check expands the entire matrix into binary multiplication blocks.

I copied the verifier and its retained producer JSON into `A39_review_rerun/` and executed the unchanged verifier there. The complete matrix was reconstructed, all local residuals were checked to precision 128, the norm/opposite-branch identities passed, and the positive function passed. Binary rank was 1240 for the 1280-by-1240 binary matrix, equivalent to rank 155 over F256.

The output was byte-identical to the author's retained verifier JSON:

- Producer data SHA256: `916b5a3ca3eda1bfdd1fc430b81a6d9671f92df6f70139ee04e1cfdc88a34e9d`.
- Verification JSON SHA256: `5c3d7beab4548818e5a2b982681d7a8e121ad0f1cf4102e42e40d1da4107d67b`.

This is an independent mathematical review plus a full read and rerun of the separately authored arithmetic verifier. It is not a third independently authored RR implementation or a formal proof-assistant check. The earlier A36 group order and exact five-torsion input were already independently reviewed and rerun in their own check events.
