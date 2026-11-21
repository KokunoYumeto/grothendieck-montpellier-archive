# Final integration scope review

Date: 21 November 2026 (Europe/Berlin). Reviewer: GPT-6 Astra Pro;
reasoning effort not exposed; run `ZETA_TWO/intake_audit`.

## Scope and outcome

Read the whole current `work/core.tex`, the conclusions and hypotheses of
IA02–IA09 in `work/intake_section.tex`, the CM01 assumption/formulation in
`work/masullo_cm.tex`, and the uploaded prompt. This was an independent
integration and convention check, not another proof of the already checked
lemmas. No new literature theorem was used in this review.

One material terminology mismatch was found and has been corrected in the
shared core: comparing a scheme zeta function with a **completed** motivic
function does not leave only a finite product, because completion also adds
archimedean factors. The core now says **canonical finite motivic Euler
product**. Its displayed correction factors already had the right meaning.

One scope clarification was sent for integration: the count definition uses
nonnegative Tate indices, while Artin motives admit every integer Tate twist.
The motive paragraph should explicitly permit every integer index. The shift
identity and proof already establish this case; it is not an additional
analytic hypothesis or proof gap.

## Dependency labels

| Result | Checked scope |
|---|---|
| ZT01, abelian part of ZT03 | Euler factorization is U; shifted Dirichlet divisor RH is A. “Complete” here means every finite prime, including ramified primes. |
| ZT02 and general part of ZT03 | M suffices for all finite-image Artin factors and Dedekind zeta functions. Quotients give meromorphic divisor RH; no Artin holomorphy conclusion is asserted. |
| CM01 and its use in ZT06–ZT07 | M explicitly covers all continuous unitary Hecke characters, including infinite-order ones. Algebraic Hecke characters require unitary normalization; a finite-order-only M would be insufficient. The absolute-Hodge category and the algebraic-projector limitation are explicit. |
| ZT06–ZT07 | General non-CM geometric RH remains B, together with analytic continuation where unavailable. The non-CM gate is preserved by Tate twists and is not characterized by a positive numerical weight. The elliptic noncancellation claim uses A and the specified open strip. |
| IA02–IA04 | A supplies the stated Dirichlet-GRH hypotheses. Exact class-number/count/height identities are U. Conductors, discriminants, strict inequalities, height normalization, and nonmaximal-order corrections are stated. Bounds for hR do not silently become separate h or R bounds. |
| IA05 | A already removes the CM exceptional-zero obstruction by the stated Stark descent. The displayed individual-height conclusion is A for abelian CM and B for general CM when individual Colmez remains an extra premise. M is not represented as proving Colmez. Full CM endomorphisms over K are required. |
| IA06–IA09 | The exact quartic CM height, the cyclotomic class-number calculation, the particular quadratic unit value, and the counterexample family are U. Their proofs do not claim that RH supplies exact special values. I.5’s original refuted status remains intact. |
| Metadata/source gates | U0 records absence of an analytic hypothesis in supplied metadata, not verification of the absent source proof. A.8c’s ring definition and A.69’s DS/RH expansion remain source gates. |

## Finite Euler factors and normalization

The shared convention is geometric Frobenius: Q_l(-1) has eigenvalue p,
weight 2, and L(N(n),s)=L(N,s+n). The global weight-w central line is
Re(s)=(w+1)/2. A removed local factor with eigenvalue of absolute value
p^(v/2) has its divisor on Re(s)=v/2; these are different statements.

ZT04 retains the actual bad fibers and the ratio of canonical local factors.
ZT05 correctly provides nonreal zeros on Re(s)=0 for Spec Z[1/p], while
explicitly preserving the original all-prime F1 hypothesis. ZT06 records
finite factors and outside-strip assumptions rather than applying strip RH
outside its stated range. In ZT07, the deleted elliptic local factors are
invertible in 1/2<Re(s)<3/2; the numerator is invertible there off Re(s)=1
under A. Thus the claimed off-line noncancellation is consistent with all
the finite Euler conventions.

No further material unsupported overclaim or convention mismatch was found
in this scope pass. This review does not certify the proposed RH proofs,
the original literature proofs, or the absent original research returns.
