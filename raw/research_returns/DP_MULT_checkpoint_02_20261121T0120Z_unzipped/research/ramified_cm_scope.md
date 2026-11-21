# Ramified base rings: full unramified CM action versus arbitrary deformations

Author/reviewer: `/root/archive_binomial`; GPT-6 Astra Pro, inherited; effort not exposed by the runtime. Date: 2026-11-21 UTC / Europe-Berlin client date. These statements address the root's narrow follow-up about DP7. They do not alter the root paper.

## Answer

**Yes, an integral full action by the ring of integers of an unramified degree-h extension supplies the missing hypothesis and preserves both the exact floor bound and the affine bound over a possibly ramified base.** Teichmuller averaging plus the support of the logarithm/exponential gives a direct proof. It is not necessary to assert, without proof, that the given group is literally the selected universal Lubin--Tate model in its original coordinate.

**No, the height of the special fibre of an arbitrary ramified deformation is not enough.** An actual integral formal group from Lubin--Tate's deformation theorem gives a counterexample. Its derivatives have asymptotic slope 1/(e(p-1)), which can be arbitrarily smaller than the height-h slope c_h, although its special fibre has height h.

## DP19 (agent ABA-R1). Integral unramified action preserves the bounds over a ramified base

Let A=O_L be a complete discrete valuation ring of mixed characteristic (0,p), with valuation v normalized by v(p)=1. Let O be the integers of an unramified extension K_0/Q_p of degree h, and fix an embedding O->A. Put q=p^h. Let F/A be a commutative one-dimensional formal group with an integral O-action satisfying

`[a]'(0)=a` for a in O.

Suppose its special fibre has p-height h. Let D be its invariant derivation normalized to have tangent coefficient 1. Then, for every integral f and n>=0,

`D^n f in p^(E_h(n)) A[[t]]`,

where

`E_h(n)=sum_(j>=1, h does not divide j) floor(n/p^j)`.

The same affine estimate as DP1 also holds:

`D^n f in p^max(0,ceil(n c_h-(h-1))) A[[t]]`,

where `c_h=1/(p-1)-1/(q-1)`.

The h=1 floor and affine bounds are zero, so integrality of D already proves them. In particular q=2 (p=2,h=1) has a trivial Teichmuller group, the average below is simply x=t, and no nontrivial symmetry is needed or claimed. The substantive positive-slope case is h>=2. Strict integral coordinate changes preserve the normalization and all these ideal containments.

### Proof: equivariant coordinate and support

The Teichmuller group mu_(q-1) lies in O. Starting with an integral coordinate t, set

`x(t)=(1/(q-1)) sum_(zeta in mu_(q-1)) zeta^(-1) [zeta](t)`.

This series is integral and has linear coefficient 1, so it is an integral coordinate with integral inverse. Reindexing the finite sum shows

`x([eta](t))=eta x(t)`.

Consequently, in x-coordinates, `[zeta](x)=zeta x`. Commuting [p] with these automorphisms implies that every nonzero coefficient of [p](x) has degree congruent to 1 modulo q-1. Indeed, for a degree outside that congruence class some zeta makes zeta^(n-1)-1 a unit. Thus

`[p](x)=px+a_q x^q+sum_(n>q, n=1 mod(q-1)) a_n x^n`,

with a_q a unit by the special-fibre height. In particular all nonlinear coefficients of degree below q vanish exactly, not merely modulo the maximal ideal.

Let L and E be the normalized logarithm and exponential. Uniqueness of the normalized logarithm gives `L([zeta](x))=zeta L(x)`, so L has the same support restriction. Its compositional inverse E satisfies `E(zeta z)=zeta E(z)` and also has support in degrees 1 modulo q-1.

### Proof: contraction and integer rounding

In a finite extension choose pi with `pi^(q-1)=p`, and let A' be the valuation ring of that extension. Define

`F_pi(X,Y)=pi^(-1) F(pi X,pi Y)`.

It is integral, and every coefficient of its p-series is in pA': the linear term is pX, and each nonlinear degree is at least q. The coefficient comparison in `L_pi([p]_Fpi(X))=p L_pi(X)` shows inductively that L_pi is integral. The coefficient multiplying its degree-m term is `p-p^m`, whose quotient by p is a unit; every other term is divisible by p by induction. The inverse E_pi is therefore integral as well. Here

`E_pi(z)=pi^(-1)E(pi z)`.

It follows that

`v([z^n]E(z)^m) >= -(n-m)/(q-1)`.

The support restriction supplies the point that is missing for a general ramified ring: a nonzero coefficient has `n-m=0 mod(q-1)`. Thus the right side is already an integer. For n>0 and m>=1 it is bounded below by

`-floor((n-1)/(q-1))`.

The invariant derivation becomes d/dz in the logarithmic variable z=L(x), so `D^n f(0)=n![z^n]f(E(z))`. For every f in A[[x]], the coefficient of degree n in f(E(z)) is a finite sum of the terms just estimated. Therefore

`v(D^n f(0)) >= v_p(n!)-floor((n-1)/(q-1))`.

No assertion that the value group of L is Z was used. Translation as in DP3 makes this bound coefficientwise: apply the evaluation estimate in the second variable to each coefficient in the first variable of f(F(t,u)).

Apply the resulting coefficientwise estimates at n=p^j and compose according to the base-p digits of a general n. The same finite identities as in DP3 give

`sum_j d_j v_p((p^j)!)=v_p(n!)`,

`sum_j d_j floor((p^j-1)/(q-1))=sum_(r>=1) floor(n/q^r)`.

Their difference is E_h(n), proving the asserted floor bound over A.

### Proof: affine bound

In the equivariant coordinate L(x)=x+b x^q+O(x^(q+1)), with b in p^(-1)A. The integral translation operators satisfy

`Delta_j=D^j/j!` for j<q, and `Delta_q=D^q/q!+bD`.

Write `B=(q-1)/(p-1)-1`, so `v_p(q!)=B+1`. Exactly as in DP1 one obtains

`D^q=p^B u D+p^(B+1)T`

with u in A and T an integral A-linear operator. For n<q the factorial bound follows from Delta_n. To justify the integer ceiling over a ramified ring explicitly, define integers `b(n)=v_p(n!)` for n<q and `b(n)=B+min(b(n-q+1),1+b(n-q))` for n>=q. The displayed operator identity proves `D^n A[[x]] subset p^b(n) A[[x]]` by induction, without any assumption on the valuation group. The same numerical induction as DP1, using `B=(q-1)c_h` and `c_h<=1`, gives `b(n)>=nc_h-(h-1)`. Since b(n) is an integer and is nonnegative, it is at least `max(0,ceil(nc_h-(h-1)))`. It is this integer operator recurrence, rather than rounding a potentially fractional A-valuation, that proves the affine bound. QED.

### Relation to full CM and to base change

For an integral lifted local CM factor, the action on its one-dimensional Lie algebra determines the embedding O->A used above. If the local CM field is unramified of degree h and the factor has dimension 1 and height h, this is the relevant strict formal O-module situation. The required action must exist on the integral lifted factor; an action or summand only on the special fibre does not supply it. If the CM field itself is ramified, Teichmuller averaging sees its residue degree, not its full degree, and ABA-R1 makes no height-h claim in that case.

For a Lubin--Tate group over O, followed by any integral base change to A, the hypotheses and the bounds hold directly. Alternatively every coefficientwise p-ideal containment over O persists under base change. This establishes the requested base-change statement. No classification assertion identifying every possible factor with a selected base-change model in a chosen coordinate is needed for the proof above.

The averaging coordinate has derivative 1, so it leaves the original normalized tangent vector unchanged. If the chosen tangent direction instead is `D'=uD` for a constant u in L^times, every valuation acquires exactly `n v(u)`. A change between two generators of the same integral tangent lattice has u in A^times and changes no valuation; a nonunit rescaling changes the lattice and must be retained explicitly. These assertions also apply to the counterexample below.

## DP20 (agent ABA-R2). A genuine ramified deformation violating even the proposed asymptotic slope

Fix h>=2. Choose a finite field k and a height-h formal group Phi/k in the normalization `Phi(X,Y)=X+Y modulo total degree p^h`. Such normalization is discussed immediately before Proposition 1.1 of Lubin--Tate 1966. Let e>p and

`A=W(k)[varpi]/(varpi^e-p)`.

This is the ring of integers of a totally ramified extension, with v(varpi)=1/e. For a fully explicit choice of ramification degree take e=p+1.

Lubin--Tate, Proposition 1.1, constructs an integral group law Gamma over `W(k)[[t_1,...,t_(h-1)]]` with special fibre Phi and

`Gamma(t_1,...)(X,Y)=X+Y+t_1 C_p(X,Y) modulo total degree p+1`.

Use the primitive binomial cocycle

`C_p(X,Y)=((X+Y)^p-X^p-Y^p)/p`;

if the opposite sign convention is used, replace t_1 by -t_1. Specialize t_1=varpi and all other parameters to zero. This specialization converges in the complete ring A and gives an actual integral formal group F/A. Its special fibre is still Phi, of height h. It satisfies

`F(X,Y)=X+Y+varpi C_p(X,Y)+O(total degree p+1)`.

### Immediate failure of the integer floor bound

The invariant vector field is

`D=(1+varpi t^(p-1)+O(t^p)) d/dt`.

Applying D p times to t and evaluating at zero gives exactly

`D^p t(0)=(p-1)! varpi`.

Only the degree-(p-1) term can survive those p-1 subsequent derivatives; using a higher coefficient of D cannot decrease degree sufficiently. Consequently `v(D^p t(0))=1/e`, whereas `E_h(p)=1` for every h>=2. The exact floor estimate therefore fails.

### Failure of the height-h asymptotic coefficient

The p-fold group sum has the expansion

`[p]_F(t)=pt+a t^p+O(t^(p+1))`, where `a=(p^(p-1)-1)varpi`.

This follows by telescoping `sum_(j=1)^(p-1) C_p(jt,t)`. In particular v(a)=1/e, and there are no nonlinear terms below degree p.

Choose beta in a finite extension with `beta^(p-1)=p/varpi`, and set

`r=v(beta)=(1-1/e)/(p-1)`.

Since e>p, r>1/p. The contracted p-series `beta^(-1)[p]_F(beta x)` is in pA'[[x]]. Its quotient by p reduces modulo the maximal ideal of A' to

`x+c x^p`, with c nonzero.

Indeed the degree-p coefficient is a/varpi, a unit, while every degree m>=p+1 has valuation at least `(m-1)r-1>0` after division by p. The contracted logarithm and exponential are integral by the same coefficient induction as above. Dividing `L_beta([p]_Fbeta)=p L_beta` by p shows

`L_beta(x) modulo the maximal ideal = x+c x^p`.

The inverse over the residue field is `sum_(s>=0) b_s x^(p^s)`, with b_0=1 and `b_s=-c b_(s-1)^p`. Every b_s is nonzero. Therefore the coefficient of x^(p^s) in E_beta is a unit, and

`v([z^(p^s)]E(z))=-(p^s-1)r`.

It follows exactly that

`v(D^(p^s)t(0))=v_p((p^s)!)-(p^s-1)r=(p^s-1)/(e(p-1))`.

Thus the derivative valuations on these witnesses have asymptotic slope `1/(e(p-1))`. This is strictly smaller than `c_h` for h>=2 and e>p. The difference is linear along n=p^s, so no O(log n) or other sublinear error can rescue the proposed height-only coefficient c_h for this fixed ramified deformation. QED.

One may choose Phi to be the reduction of an unramified Lubin--Tate O-module of O-height one (and p-height h). Its special fibre then has the full O-action. The deformation just constructed cannot carry a compatible integral lift of that full action, since DP19 would contradict the displayed derivatives. Thus even a full unramified action present on the special fibre does not replace the lifted action required by DP19. Likewise a formal summand known only after reduction supplies neither the integral subgroup map nor its normalized tangent lattice.

### Actual integral existence source

Jonathan Lubin and John Tate, *Formal moduli for one-parameter formal Lie groups*, Bulletin de la Societe Mathematique de France 94 (1966), 49--59. **Proposition 1.1, pp.50--51**, supplies precisely the integral group law with the prescribed degree-p deformation coefficient; **Theorem 3.1, p.56**, is the universality statement. Only Proposition 1.1 is needed for the counterexample. The normalization of Phi is discussed immediately before that proposition on p.50.

Primary PDF: https://www.numdam.org/item/10.24033/bsmf.1633.pdf

Inspected web references: `turn517737393view0` for Proposition 1.1 and Theorem 3.1; bibliographic metadata independently in `turn251441319search0`. The source provides a real integral formal group, not merely an arbitrary polynomial proposed as a p-series.

## Check record

The complete proofs above were reread in full on 2026-11-21 from 00:26:17 to 00:27:18 UTC, including the explicit integer affine recurrence added during that read. The checks covered averaging, support-based integer rounding, coefficientwise translation, the affine recurrence, actual integral deformation specialization, the telescoping p-series coefficient and the contracted logarithm/exponential reduction. Lubin--Tate Proposition 1.1 was reopened and its existence statement rechecked. These are author self-checks and a cited-theorem application, not an independent reproof of the Lubin--Tate existence theorem. Events ABA-CE14 and ABA-CE15 record the scope, model and actual check times.
