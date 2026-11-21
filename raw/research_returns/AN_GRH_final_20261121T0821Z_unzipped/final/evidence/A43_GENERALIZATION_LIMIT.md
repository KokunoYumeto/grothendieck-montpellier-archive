# Exact scope of the A43 Frobenius construction

Recorded: 2026-11-21T05:37:52.046546+00:00.
Checker: GPT-6 Astra Pro; effort not exposed; /root/effective_galois.

## Setting

Let E be an ordinary genus-two curve over a finite field F_q of characteristic two. Assume the integral Rosati-symmetric endomorphism T is defined over F_q and satisfies T^2+T-1=0. Write pi for q-power Frobenius on J_E and V=pi^dagger for its adjoint. Then pi V=q, and T, pi and V commute because T is defined over the field. The scalar q in these formulas means multiplication by the integer q, not its reduction modulo the characteristic. The identities take place in the characteristic-zero, torsion-free endomorphism ring. Put s=pi+V and u=T-pi.

No claim is made that arbitrary ordinary real-multiplication targets satisfy the additional Frobenius relation used in A43.

## Complete algebra calculation

First,

    u^dagger u = (T-V)(T-pi)
               = T^2 - T(pi+V) + q
               = 1 + q - T(1+s).

Since T(T+1)=1, this yields the exact equivalence

    u^dagger u = 1  if and only if  s = q(T+1)-1.             (GL.1)

Thus the polarized-unit condition is an additional equation involving Frobenius. The RM relation T^2+T=1 alone does not supply this equation.

Independently of that extra condition,

    u^2+u+1 = T^2+T+1 + pi^2 -(2T+1)pi
             = 2-q + (s-2T-1)pi.                           (GL.2)

The second equality uses pi^2-s pi+q=0, which follows directly from s=pi+V and pi V=q. If the equivalent conditions (GL.1) hold, substitute s=q(T+1)-1 into (GL.2) to obtain

    u^2+u+1 = (q-2)((T+1)pi-1).                            (GL.3)

For q=2, the additional condition is exactly s=2T+1, and (GL.3) gives the cyclotomic identity used in A43. Together with u^dagger u=1, this gives the integral polarized automorphism of order three in that proof.

For q different from2, the simultaneous identities u^dagger u=1 and u^2+u+1=0 are impossible in this setting. Indeed the additive group End(J_E) is torsion-free, so (GL.3) would give (T+1)pi=1 and hence pi=T. But T is an automorphism, whereas q-power Frobenius on an abelian surface has degree q^2>1. This contradiction only concerns this exact choice u=T-pi and these two identities. It does not exclude different correspondences, other automorphisms, or a construction based on a different Frobenius or field of definition.

## Geometric consequence and precise limitation

In A43 the extra q=2 relation is verified for the particular A13 Jacobian. The resulting curve automorphism rho preserves its Raynaud theta characteristic. Its differential equals dT. This makes the normalized critical locus split into the two explicit graphs Q=rho(P) and Q=iota rho(P), and the exact Frobenius formulas on those graphs provide the forced tangency of length two. The subsequent branch count then proves that the source of that inverse family has rank one.

For a general ordinary O5 target, an equality between tangent directions defines a fibre product of canonical double maps. Such an equality alone does not provide a curve automorphism lifting the projective tangent action, does not split that fibre product into the two graphs used in A43, and does not establish the required Frobenius formula on a component. The present calculation supplies no replacement for those geometric assertions. It makes no claim that the critical locus is irreducible, that the inverse source is generically ordinary, or that the special graph mechanism can never occur for other data.

Consequently this note is a checked limitation of the attempted extension of the A43 mechanism. It is not a reduction of the universal ordinary Rosati-O5 point-section problem, a uniform theta-incidence theorem, or a revival of the stopped effective-Galois stream. The confirmed A43 example and its exact both-Weierstrass conclusion remain valid.

## Actual check performed

The complete algebra above was expanded and checked manually. A separate symbolic reduction was executed for the norm identity, the unconditional cyclotomic identity, and the conditional cyclotomic identity, using the displayed polynomial relations in commuting variables. All three remainders were zero. The exact execution record is `A43_review/generalization_algebra_check.json`, SHA256 `7cedfda92cc99f312f74bfb21a59fd35c60487a46f03b4a7fe172e8d19d4e65b`. This is an algebra check only, not formal proof-assistant verification or a new geometric theorem. The finite-field degree and torsion-free endomorphism facts are the same standard inputs already used in the checked preceding construction.
