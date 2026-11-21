# Independent whole-proof challenge: DP19, DP20 and DP22

Reviewer: `/root/formal_bound`. Model: GPT-6 Astra Pro, inherited. Effort: not exposed. Run: DP_MULT_20261121. Review date: 2026-11-21. Tool-observed times include 00:29:22 UTC at the first complete read and 00:33:29 UTC after the original Lubin–Tate pages were visually inspected (01:29:22 and 01:33:29 Europe/Berlin). This is an independent mathematical/source review, not a Lean compilation or computational certificate.

Reviewed files: `research/ramified_cm_scope.md` (DP19 and DP20) and `research/cm_genus3_example.md` (DP22). **All three pass the whole-proof challenge. No mathematical correction is required.** A terminology clarification about O-height versus p-height is recorded below.

## FBA-CHECK-DP19: full unramified CM action over a ramified base

### Equivariant coordinate

The averaging formula is integral: q-1 is a unit, every [zeta] is an integral endomorphism, and the linear coefficient is `(q-1)^(-1) sum_zeta zeta^(-1)zeta=1`. Its inverse is therefore integral. Reindexing with theta=zeta*eta gives `x([eta](t))=eta*x(t)` exactly. There is no separability, denominator or descent assumption hidden in this calculation; the fixed integral embedding O->A supplies the Teichmuller roots.

If n is not 1 modulo q-1, a Teichmuller root makes `zeta^(n-1)-1` a unit, since its nonzero reduction lies in the residue field. Thus the support restriction on [p], L and E is exact, even though A is ramified. In particular no nonlinear degree below q can occur. The height assumption makes the degree-q coefficient a unit; the lower bound itself needs only the absence of smaller nonlinear degrees.

### Contraction and the integer floor

The scaled group is integral because every coefficient of total degree d is multiplied by pi^(d-1), with v(pi)>0. Its p-series is p-divisible because its nonlinear degrees are at least q. In the logarithm coefficient induction, `p-p^n=p(1-p^(n-1))` has exactly valuation 1, and all other terms are in pA'. The inverse of an integral normalized series is integral.

The coefficient of E(z)^m can be nonzero only when n-m is divisible by q-1. Hence the contraction inequality

`v([z^n]E(z)^m) >= -(n-m)/(q-1)`

has an **integer right side on its nonzero support**. For m>=1 it is at least `-floor((n-1)/(q-1))`. This is the valid replacement for rounding a fractional value-group element. The finite coefficient sum in f(E) cannot lower that bound. The n=0 case is ordinary integrality.

Translation promotes the evaluation estimate to a coefficientwise p-ideal containment. The p-power estimates can then be composed because every operator involved is A-linear and preserves the indicated p-power lattice. Rechecking the digit interchange gives exactly

`E_h(n)=v_p(n!)-sum_(r>=1)floor(n/q^r)`.

### Affine ceiling

The identity `Delta_q=D^q/q!+bD` is valid because the equivariant logarithm has no nonlinear term below q. Contraction gives pb integral, hence the stated integer-exponent operator recurrence. Every recursively defined b(n) is a nonnegative integer. Numerical induction proves `b(n)>=n*c_h-(h-1)`; taking its integer ceiling is legitimate independently of the value group of A. No step rounds an arbitrary valuation to an integer. The composition order `T D^(n-q)` only requires T to be integral and A-linear, not to commute with D.

The cases h=1 and q=2 are correctly treated as trivial zero-bound cases. The averaging coordinate is strict, so it does not rescale the primitive tangent vector.

**Result:** DP19 is proved as stated over the possibly ramified A. An integral lift of the full unramified O-action is an essential hypothesis; a special-fibre action alone is not being used as a substitute.

## FBA-CHECK-DP20: actual ramified deformation and its exact witnesses

### Existence source checked directly

I opened the primary paper and independently viewed the original printed pp.50–51, including Proposition 1.1 and its proof. Its clause 2 for i=1 gives precisely the whole family

`Gamma(t_1,...,t_(h-1))(X,Y) = X+Y+t_1 C_p(X,Y) mod degree p+1`.

Clause 1 preserves the required special fibre after all parameters reduce to zero. Thus specializing t_1=varpi and all other t_i=0 does give an actual integral formal group, not an arbitrary proposed p-polynomial. The map from the power-series parameter ring converges because varpi is topologically nilpotent and A is complete. The normal form for Phi is stated immediately before Proposition 1.1. The underlying general bud-extension theorem used by Lubin–Tate is cited, not independently reproved in this review.

Primary source: Jonathan Lubin and John Tate, *Formal moduli for one-parameter formal Lie groups*, Bull. Soc. Math. France 94 (1966), pp.49–59, Proposition 1.1, pp.50–51. URL: https://www.numdam.org/item/10.24033/bsmf.1633.pdf . Web retrieval reference `turn765675901view0`; original local renderings are `research/lt1966_p50.png` and `research/lt1966_p51.png` from `research/Lubin_Tate_1966_formal_moduli.pdf`.

### Low-degree coefficient and primitive derivation

For the stated positive primitive cocycle,

`partial_Y C_p(t,0)=t^(p-1)`.

Hence the primitive invariant derivation is exactly `D=(1+varpi*t^(p-1)+O(t^p))*d/dt`. To obtain a constant after p applications to t, the total degrees of the selected vector-field coefficients must sum to p-1. Only one coefficient of degree p-1 can occur, and it must occur in the first application, because taking the constant coefficient first produces a constant killed by the next derivative. Consequently

`D^p t(0)=(p-1)!*varpi`

with no additional terms. This has valuation 1/e, while E_h(p)=1 for every h>=2.

For the p-series, the recurrence on the degree-p coefficient is additive, since substituting an O(t^p) correction into the degree-p cocycle changes degree only from p+1 onward. The exact telescoping sum is

`sum_(j=1)^(p-1) C_p(j,1) = (p^p-p)/p = p^(p-1)-1`.

Thus a=(p^(p-1)-1)*varpi, a unit times varpi; there are no nonlinear terms below p.

### The contraction threshold and exact exponential coefficients

For `beta^(p-1)=p/varpi`, the scaling exponent is

`r=(1-1/e)/(p-1)`.

The condition `e>p` is **exactly equivalent** to r>1/p. For every m>=p+1, the coefficient of the scaled p-series divided by p has valuation at least `(m-1)r-1 >= pr-1>0`. This controls every higher coefficient, including the special-fibre height term; no assumption about those coefficients beyond their integrality is missing.

The degree-p coefficient divided by p is a/varpi, reducing to -1. Consequently the contracted p-series divided by p reduces to `X-X^p` (the memo's more general notation X+cX^p is valid). The integral logarithm functional equation, divided by p, gives the same reduction for the contracted logarithm: all terms of logarithmic degree j>=2 acquire p^(j-1) and vanish in the residue field. Its inverse therefore has nonzero coefficients at every p^s; in the explicit c=-1 case they are all 1.

The relation `E_beta(z)=beta^(-1)E(beta*z)` then gives exactly

`v([z^(p^s)]E(z))=-(p^s-1)r`.

Legendre's formula and `D^n t(0)=n![z^n]E(z)` give

`v(D^(p^s)t(0))=(p^s-1)/(e(p-1))`.

The right side belongs to the value group (it is an integer divided by e), so there is no compatibility problem with the original ramified ring. Its asymptotic coefficient is strictly smaller than c_h for every h>=2 and e>p. The deficit is linear on these witnesses; an O(log n) error cannot repair it. The case p=2 is included: taking e=3 gives r=2/3>1/2 and the same calculation works.

**Result:** DP20 supplies the asserted genuine counterexample and the exact infinite witness sequence. Suggested terminology only: say “Lubin–Tate O-module of O-height 1 (p-height h)” in its final paragraph, rather than leaving “height-one” unqualified.

## FBA-CHECK-DP22: the genus-three CM example

### Geometry and CM action

The second chart is correctly derived from `u=1/x`, `v=y/x^4`: its equation is `v^2=u-u^8`. Each chart is finite flat of degree two over the corresponding affine chart of P^1, and the transition gives a finite hence proper cover. The stated Jacobian-criterion calculations prove smoothness when 2 and 7 are invertible. The branch points are seven simple roots and infinity, so Riemann–Hurwitz gives genus 3. Infinity supplies the section required for the relative Jacobian construction.

The automorphism extends to the second chart by `u -> zeta^(-1)u`, `v -> zeta^(-4)v`; it fixes infinity. The regular forms have eigenvalues zeta, zeta^2 and zeta^3. Their orders at infinity are 4, 2 and 0: ord_v(u)=2, ord_v(x)=-2, ord_v(y)=-7 and ord_v(dx)=-3. The covariant Jacobian convention is explicit and correct. Pullback on cotangents is the transpose of the derivative, so it has the same eigenvalue multiset, not the inverse multiset. The ring-polynomial relation has zero differential in characteristic zero and therefore is the zero abelian endomorphism; its generic equality extends to the abelian scheme. Irreducibility of Phi_7 proves the asserted injection of the maximal order. No claim about the full endomorphism ring is needed.

### Integral factors and their formal realization

The two Frobenius orbits for multiplication by 11=4 modulo 7 are exactly `{1,4,2}` and `{3,5,6}`. Their intersections with `{1,2,3}` have cardinalities 2 and 1. The completion of the maximal order at 11 is the product of two unramified cubic orders. Its idempotents act on the integral p-divisible group and give actual direct factors; no isogeny denominator is being suppressed.

The rank-one rational Tate-module assertion is the standard full-CM assertion used by Tate's decomposition theorem. If a short elementary characteristic-zero justification is desired, use Betti H_1 of dimension 6 with its faithful degree-6 field action, hence rank one over E, followed by the Betti/etale comparison. Faithfulness of an E-action on an arbitrary Q_11-vector space by itself would not be an adequate substitute for that assertion, but the memo does not make that faulty argument.

The factor heights are 3. The local CM slope formula yields respectively 2/3 and 1/3, consistent with the dimension/height convention in which the multiplicative group has slope 1. The one-dimensional factor has connected special fibre, so the connected p-divisible/formal-group correspondence over the complete local base applies. The integral idempotent makes it a direct formal factor of the completed Jacobian. This is a formal subgroup assertion, not an assertion of a global elliptic subvariety. Its Lie lattice is an integral direct summand, so the selected primitive tangent direction has no hidden nonunit scaling.

The usual existence of the relative Jacobian, the connected p-divisible/formal-group correspondence, and Tate's local CM theorem are accepted standard inputs with their hypotheses checked here; they were not independently reproved in full. Tate's §5, pp.106–108, had already been independently visually reread by this reviewer during GTR-10.

### Arithmetic and scope

Recomputing gives `c_3(11)=66/665`, `c_2(11)=11/120`, and ratio `144/133`. The example satisfies the original unramified theorem directly and the full-action refinement DP19. Its odd orbit length and slopes prevent identifying it with the unchanged even alternating/height-two input. It establishes existence of an actual higher-height direction, not shorter global theta chains.

**Result:** DP22 passes, including its integral formal-subgroup and normalization claims.

## Genuine event summary

| Statement | Check type | Outcome |
|---|---|---|
| DP19 | Independent whole-proof challenge and coefficient/ideal re-proof | Passed; ramified value-group rounding is handled by support and integer operator exponents |
| DP20 | Independent whole-proof challenge plus original-primary-source inspection | Passed; actual integral existence, exact p-coefficient, contraction threshold and p-power derivative witnesses verified |
| DP22 | Independent geometric/local-CM whole-proof challenge | Passed; smooth model, covariant type, integral factors, connected formal realization and numerical ratio verified |

All checks above were performed by `/root/formal_bound`, GPT-6 Astra Pro inherited, effort not exposed, on 2026-11-21 in run DP_MULT_20261121. No finite numerical experiment, computer algebra proof, Lean compilation or formal verification is claimed.
