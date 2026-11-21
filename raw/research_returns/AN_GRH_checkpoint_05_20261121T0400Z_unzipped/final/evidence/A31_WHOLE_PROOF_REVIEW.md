# Independent whole-proof review: A31 exact-order-seven theta witness

Date: 2026-11-21.
Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.

Source reviewed: `work/row_audit/A31_A27_THETA_SEVEN.tex`.
Final SHA256: `825ba2c25144253ccfc144710b8ca9f50de4f79bf978df896efe2c5c915d1b29`.

## Outcome

PASS. The entire proof was read at the initial complete source hash, followed by a narrow check of the added all-six-original-points scope statement at the final hash above. The full verifier and its certificate were read, and an unchanged copy of the verifier was rerun in this reviewer's work directory. It passed and reproduced the retained JSON byte for byte. The explicit curve, function and change of variables were discovered by root; this audit independently checks their arithmetic and geometric deductions.

## Isomorphism and norm

The coordinate change was checked by hand independently of the code. With Z=Y+u^2, the new equation becomes Z^2+X^2 Z=X^5+X^4+uX^3+uX. Dividing byX^4 gives (Z/X^2)^2+Z/X^2=X+1+u/X+u/X^3. Substitution X=u/t and Z/X^2=y+u, using u^2+u=1 and u^3=1, recovers exactly the original A27 equation. The inverse formulas therefore hold in the function fields and extend to the smooth proper curves. The original point (t,y)=(u,u^2) maps to (X,Y)=(1,u), while the original simple-pole point t=0 maps to the unique point W at infinity.

The norm was also expanded by hand. In F4[X], X^2+X^3(X+u)+(X^2+u^2)f(X) has coefficient1 in every degree0 through7, hence equals(X+1)^7. The two point values are0 andu^2. The affine curve is smooth: a singular point would have X=0 from the Y derivative, but the X derivative there is u, nonzero. The norm therefore places all finite zeros at the one unramified point R aboveX=1, with multiplicity7. At W, the original-coordinate valuations give ord(X)=-2 and ord(Y)=-5. The termXY is the unique pole term of order7 in F. Thus div(F)=7(R-W), and the nonzero degree-one difference has exact order7.

## Exact differential and twist

For X nonzero finite, the X-map is etale and dX/X^2 is nonvanishing. Differentiating the plane equation gives X^2 dY=f'(X)dX, so atX=0 the same differential is dY/f'(X); it is regular and nonvanishing because f'(0)=u and Y is a local parameter. Its divisor is supported only at infinity and has degree2, hence equals2W. It is exact, d(1/X).

The line of locally exact differentials lives on C^(1), not on an implicitly identified F4-model. In characteristic two an exact local differential with zero order2 gives a zero of order1 in that line on the Frobenius twist. Therefore B_C=O_(C^(1))(W^(1)), and the theta point is M^(1)=[R^(1)-W^(1)], with R^(1)=(1,u^2) on the coefficient-squared model. Its order remains7. A11 applies literally to this class. Its normalization recovers M from F_C^*(M^(1))=M^2, so there is no mismatch between the norm-defined cyclic torsion class and the theta class.

The signed doubling group modulo7 is all six units, with the two doubling orbits {1,2,4} and {3,5,6}. A11 therefore makes the whole new factor of the prime-degree cover have geometric2-rank zero. Finite constant extensions can define all deck transformations and rationalize a chosen fibre without destroying that property. The pointed separation conclusion is consequently valid for any prescribed point after the required extension.

## Detector scope and the final delta

For the explicit R, kappa_R=-2[R-W] has exact order7 and cannot satisfy A29 since ord_7(2)=3 is odd. More strongly, the already checked A27 group order #J(F4)=28 implies that every one of the original six rational points has canonical odd-primary support contained in{7}. The fixed canonical classes keep that support after every constant extension. The all-six-points addendum is therefore correct. The geometric7 witness nevertheless becomes split at any prescribed one after a finite extension. This does not contradict A27: its numerical obstruction concerns primes for which2 is primitive, and7 does not qualify. Nor does failure of either sufficient detector assert failure of every actual cover.

## Exact arithmetic reproduction

Read verifier: `work/row_audit/verify_A31_norm7.py`, SHA256 `4df13e682a8f6382dd69351b4d33876d33c58a5935426916ca7c7d87f3597c98`.
Rerun location: `work/gt_certificates/positive_rank_theta/A31_review_rerun/`.
Author and rerun JSON SHA256: `34e62e0db020835988dd8a1335c263e99f0ebb1db414f8e228995156f345f5a7`.

The code implements F4 operations, polynomial and Laurent products directly and imports no Jacobian package or earlier theta/Mumford implementation. It checks the norm, both substitutions, point values, affine smoothness condition and signed unit orbit. The pole/divisor, differential, exact-order and cover conclusions were checked in the written proof, not inferred from the arithmetic output alone. No formal proof-assistant claim is made.
