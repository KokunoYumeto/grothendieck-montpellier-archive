# Author whole-proof review: special Cohen weight-two bound

Statement: `KT-COHEN-WEIGHT-TWO-BOUND`.

Reviewed file: `cohen_weight_two_bound.tex`, SHA-256
`eada2ea1673de44bb3e18520a6befd4dcc3fdec420f2ce23b25f18faccb4cc50`.

The entire 236-line proof was read after writing. Outcome: **PASS** as a mathematical deduction from the stated carried modular-form inputs. This is not a Lean kernel build and does not prove the missing third auxiliary unit or a new original rational class-group vanishing.

## Exact scope

For every prime p at least 31 congruent to 3 modulo 4, with b=(p+3)/2, the proof supplies an odd negative fundamental discriminant D=-d with 3 <= d <= p-4, p not dividing h(D), and beta_b(chi_D) a p-adic unit. The existing character transport gives the two displayed generalized B1 units and all indices congruent to b. No condition on beta_3 is proved.

## Checks controlling the reduction

The quotient H_b/theta^p has weight two and trivial character: the multiplier exponents are p+4 and p, leaving the fourth power. The theta product has no interior zeros. Its fourth power has nonzero constants at infinity and zero, and expansion 16q+... at the cusp one-half. The formula at zero is -theta(tau/4)^4/4. At one-half, the exact Poisson identity is theta(A tau)/(2 tau+1)^(1/2)=sum over odd a of q^(a^2/4), whose leading term is 2q^(1/4).

The index-one dual theta matrices give the Cohen transform u*2^(-b)*h_1(tau+1/2), with u an eighth root of unity. Thus only coefficients H(b,n) with n<p can contribute negative powers after division by theta^p. All scalar factors are units at odd p. A coefficient extension containing eighth roots is allowed throughout.

The proof uses explicit characteristic-zero principal-part removal, not an assumed special-fiber base-change statement. With G=2E2(2tau)-E2(tau) and Theta=theta^4, the forms W_j=G^(j+1)/Theta^j have their sole pole at one-half, leading term 16^(-j)q^(-j), integral Laurent coefficients there, and integral Fourier coefficients at infinity. If the initial principal part is divisible by p, removing it successively uses only multiples divisible by p and preserves the infinity reduction.

The resulting holomorphic form is subject to the ordinary coefficient-field Sturm bound one. The constant/q coefficient matrix for Theta and G has determinant 16. Their q/q^2 matrix has determinant -384, a unit at p>=31. A unit constant and two following zero coefficients are consequently impossible. The Cohen divisor factor is integral, so a minimal unit index is fundamental. The carried elementary class-number estimate applies since d<p<4p.

## Source scope

The carried complete proof `main_gate/jacobi_two_unit_fields.tex` supplies the full Cohen/Jacobi coefficient formula, integrality even when p divides the discriminant, Kummer transport, and the small-discriminant class-number estimate. Its initial coefficient and integrality portions were reread for this deduction. The theta Poisson normalization is also displayed in the previously whole-reviewed `main_gate/kohnen_theta_discriminator.tex` and was independently derived again using theta3(TS z)=theta4(S z) and the theta2 translation phase; the phases cancel in the stated theta identity.

The exact ordinary Sturm statement was freshly read in Choi--Choie--Kikuta (2013), printed page 129: integral coefficients over a number field, a prime ideal of its ring of integers, and bound k[SL2(Z):Gamma]/12 including the constant. Applying it to locally integral coefficients is legitimate after clearing a bounded denominator prime to the chosen prime ideal. The foundational proof of Sturm's theorem is imported, not newly reconstructed. Eichler--Zagier's full coefficient formula and theta correspondence are carried, already reviewed inputs; no new whole-book claim is made.

Root and geometry communicated agreement with the full argument or its individual reduction steps during drafting. Their final whole-file review records belong to those reviewers and are not represented as author checks here.

The improvement from the prior linear bound to d<=p-4 remains linear. It does not reach the sufficient d^5<=1600p^2 third-unit window.
