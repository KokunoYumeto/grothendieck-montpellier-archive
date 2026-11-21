# Independent formal-group proof (agent /root/formal_bound)

Run: DP_MULT_20261121. Model: GPT-6 Astra Pro (inherited). Effort setting: not exposed. Written 2026-11-21 Europe/Berlin (2026-11-20 23:53 UTC).

## FBA-1. Exact explicit finite-height bound and universal sharp subsequence

Let k be perfect of characteristic p, R=W(k), K=Frac(R), and let F(X,Y) be a one-dimensional commutative formal group law over R. Write

D=F_Y(T,0)d/dT

for the normalized invariant derivation (D(T)(0)=1). Let the reduction of F have finite height h, q=p^h. Thus if g(T)=[p]_F(T)=pT+sum_{n>=2}a_n T^n, then a_n is in pR for 2<=n<q, and a_q is a unit. For every f in R[[T]] and every integer a>=1,

v_p(D^a f(0)) >= B_h(a):=max{0, v_p(a!)-floor((a-1)/(q-1))}.

There is no unspecified error term. Put s_p(a) for the sum of the base-p digits of a and r_h(a)=(a-1) mod (q-1), 0<=r_h(a)<q-1. Equivalently the nonzero-floor part of the bound is

a[1/(p-1)-1/(q-1)] - s_p(a)/(p-1) + [1+r_h(a)]/(q-1).

For every such F, every r>=0, f(T)=T, and a=q^r, equality holds:

v_p(D^{q^r}T(0)) = (q^r-1)[1/(p-1)-1/(q-1)].

Consequently the linear coefficient c_h=1/(p-1)-1/(p^h-1) is optimal for each individual finite-height formal group (and not merely optimal over the class).

### Full proof

1. **Scaling.** Let pi satisfy pi^{q-1}=p, let K'=K(pi), and R'=R[pi]. Since X^{q-1}-p is Eisenstein (with the evident trivial interpretation when q-1=1), R' is a complete DVR, pi is a uniformizer, and v_p(pi)=1/(q-1). Form

F_pi(X,Y)=pi^{-1}F(pi X,pi Y) in R'[[X,Y]].

Its p-series is

g_pi(X)=pi^{-1}g(pi X)=pX+sum_{n>=2}a_n pi^{n-1}X^n.

Each coefficient belongs to pR': when n<q this follows from a_n in pR; when n>=q it follows from pi^{n-1} in pR'. Hence g_pi(X)=pH(X) for an H(X) in R'[[X]] with H'(0)=1. Modulo pi,

H(X) = X + uX^q (mod pi),

where u is the nonzero reduction of a_q. For n<q, the nonlinear coefficient of H is (a_n/p)pi^{n-1}, divisible by pi; for n>q its valuation in pi is at least n-q>=1. The q coefficient is a_q.

2. **Integral logarithm whenever [p] is coefficientwise p-divisible.** Write H(X)=X+sum_{n>=2}c_n X^n. Define U_0(X)=X and

U_r(X)=p^{-r}g_pi^{circ r}(X).

Inductively U_r lies in R'[[X]]: if g_pi^{circ r}=p^r U_r, then

U_{r+1}=U_r+sum_{n>=2} c_n p^{r(n-1)}U_r^n.

For r>=1 the increment is coefficientwise in p^rR'. Thus U_r converges coefficientwise p-adically to an L_pi(X) in R'[[X]], with L_pi(0)=0, L_pi'(0)=1. The homomorphism identity for [p]^r gives

U_r(F_pi(X,Y)) = p^{-r}F_pi(p^rU_r(X),p^rU_r(Y)).

Every nonlinear term on the right has an extra factor p^{r(i+j-1)}, for i+j>=2. Passing coefficientwise to the limit gives

L_pi(F_pi(X,Y))=L_pi(X)+L_pi(Y).

Therefore L_pi is the normalized formal logarithm of F_pi. Its compositional inverse E_pi belongs to R'[[Z]] by recursive inversion of a series with unit linear coefficient.

3. **Original exponential coefficients.** Let L(T)=pi L_pi(T/pi), which is a normalized formal logarithm of F over K'. Uniqueness, obtained by differentiating the logarithm identity at Y=0, shows L'(T)=1/F_Y(T,0), so L belongs to K[[T]] and is the normalized logarithm over K. Let E(Z)=L^{-1}(Z). Then

E_pi(Z)=pi^{-1}E(pi Z).

Writing E(Z)=sum_{n>=1}e_nZ^n, integrality of E_pi says

v_p(e_n)+(n-1)/(q-1)>=0.

4. **An arbitrary integral function.** For a>=1 and f(T)=sum_{m>=0}f_mT^m, the coefficient of Z^a in f(E(Z)) is a finite sum of terms

f_m e_{n_1}...e_{n_m}, n_i>=1, sum n_i=a, m>=1.

Every such term has valuation at least -(a-m)/(q-1)>=-(a-1)/(q-1). Since the coefficient belongs to K, its valuation is an integer, so

v_p([Z^a]f(E(Z))) >= -floor((a-1)/(q-1)).

The identity D=d/dL gives

D^a f(0)=a![Z^a]f(E(Z)).

This proves the second term in B_h(a). The value D^a f(0) is integral because D preserves R[[T]], proving the extra maximum with zero.

5. **Sharpness.** In step 2, U_1=H, and U_{r+1}-U_r is divisible by p for every r>=1. Therefore

L_pi(X)=X+uX^q (mod pi).

The formal inverse in k[[Z]] is sum_{r>=0}b_r Z^{q^r}, with b_0=1 and

b_r=-u b_{r-1}^q.

Indeed substituting it into X+uX^q yields Z because q is a power of the characteristic. Every b_r is nonzero. Thus the coefficient of Z^{q^r} in E_pi is a unit, i.e.

v_p(e_{q^r})=-(q^r-1)/(q-1).

Legendre's formula gives v_p((q^r)!)=(q^r-1)/(p-1); multiplying the coefficient by (q^r)! proves equality. (At r=0 it says D(T)(0)=1.) This also proves optimality of the slope by letting r tend to infinity.

6. **Exact error expression.** Legendre's formula v_p(a!)=(a-s_p(a))/(p-1) and a-1=(q-1)floor((a-1)/(q-1))+r_h(a) give the displayed expression by algebra. Since s_p(a)<= (p-1)(1+floor(log_p a)), this implies the original O(log a) claim with an explicit error. No deformation normal form has been assumed.

## FBA-2. Infinite-height case

If [p]_F(T) mod p is identically zero (height infinity), then [p]_F(T) belongs to pR[[T]]. Step 2 above works over R itself, without scaling; both L and E are integral. Hence v_p(D^a f(0))>=v_p(a!) for all f in R[[T]]. This is optimal for every a: take f(T)=L(T)^a, which is integral and satisfies f(E(Z))=Z^a.

## FBA-3. Normalization and extension to bounded denominators

If D_c=cD for c in K, then D_c^a=c^aD^a. If f is in p^{-b}R[[T]], then replace f by p^bf. Thus the direct bound is

v_p(D_c^a f(0)) >= a v_p(c)-b+v_p(a!)-floor((a-1)/(q-1)).

When c in R, one may use a v_p(c)-b+B_h(a). If c is not integral, a height-only nonnegative bound need not hold. Bounded denominator b and tangent scaling c are data required when applying the estimate to normalized theta sections.

## FBA-4. Fable's normal-form argument is not justified

The assertion that an arbitrary height-h formal group over W(k) has logarithm T+T^q/p+T^{q^2}/p^2+... in an integral coordinate is not a consequence of height and generally imposes special endomorphisms. The proof FBA-1 replaces this assertion by the scale-and-limit argument, which applies to all deformations. No classification or p-typification theorem is needed for the bound. A simple strict-coordinate version shows the displayed logarithm cannot be literally universal in the supplied coordinate even at h=1: the multiplicative formal group has L(T)=log(1+T), not the displayed p-typical series. A stronger non-isomorphism assertion would require deformation theory and is not used in the proof.

## Genuine check events

- FBA-1: independent re-proof, /root/formal_bound, GPT-6 Astra Pro, effort not exposed, DP_MULT_20261121, 2026-11-21 Europe/Berlin: developed scaling and p-series iteration proof independently of root's coefficient-recursion proof; passed.
- FBA-1: targeted proof check, same metadata, 2026-11-21: reread all six proof steps from hypotheses through exact-sharp subsequence; checked the pi-adic reductions separately for n<q, n=q, n>q, formal coefficientwise limits, and the finite composition sums; passed. No formal verification claimed.
- FBA-2: targeted proof check, same metadata, 2026-11-21: checked no scaling is required, L integral, and witness f=L^a attains the bound; passed.
- FBA-3: targeted proof check, same metadata, 2026-11-21: checked scalar multiplication commutes with D, derivative scaling is c^a, and denominator shift is -b; passed.
- FBA-4: targeted proof check, same metadata, 2026-11-21: only the literal normal-form assertion and its unnecessary role are claimed; no unproved general classification claim is used.
- BKG-Legendre: used and rechecked in this run, same metadata: v_p(a!)=sum_{j>=1}floor(a/p^j)=(a-s_p(a))/(p-1), checked by counting multiples of p^j and summing the digit expansion. This elementary background identity is re-derived only in this specific form.

## Primary-source lead (not yet used as a theorem)

Katz, N. M., “Divisibilities, congruences, and Cartier duality”, Journal of the Faculty of Science, University of Tokyo, Sect. IA Math. 28 (1981), no.3, 667–678 (published 1982). Author's publications index: https://web.math.princeton.edu/~nmk/old/. The exact numbered theorem relevant here must be checked before attributing the explicit bound to Katz. FBA-1 is self-contained and does not require that attribution.

## FBA-5. Coefficientwise operator bound and restricted p-power

For every a>=1,

D^a(R[[T]]) is contained in p^{B_h(a)}R[[T]].

Proof. Apply FBA-1 coefficientwise in T to f(F(T,U)) in R[[T,U]], viewed as a series in U. Invariance gives D_U f(F(T,U))=(Df)(F(T,U)); iteration and U=0 give D_U^a f(F(T,U))|_{U=0}=D^a f(T). Every coefficient in T is divisible by p^{B_h(a)} by FBA-1. At a=p, h>=2 gives B_h(p)=1, hence D^p=0 modulo p. At h=1, FBA-1 sharpness at a=p shows D^p(T)(0) is a unit, hence D^p is nonzero modulo p. The finite-height dichotomy is therefore proved without invoking an external restricted-Lie theorem. Infinite height is covered by FBA-2.

## FBA-6. The bound is not an ordinary divided-power action

For any finite h and r>=1, the value of (D^{q^r}/(q^r)!)(T) at zero has valuation -(q^r-1)/(q-1)<0, by FBA-1. Thus D^a/a! does not preserve R[[T]] in general. The proved structure is an explicit filtration on the invariant differential operators; it is not an ordinary divided-power action on the original integral coordinate ring. The rescaled derivation pi D does have divided powers acting integrally on R'[[T]] because a/(q-1)+v_p(D^a f)-v_p(a!)>=1/(q-1)>0 for a>=1 (using the unrounded bound). This rescaled statement does not identify the original theta sections with crystals; that needs separate data.

## FBA-7. Exact sharpness at every p-power order

Let a=p^j, write j=hr+s with 0<=s<h, and choose f(T)=T^{p^s}. The coefficient of Z^{a} in E_pi(Z)^{p^s} is a unit, because modulo pi it is the p^s-th power of sum b_r Z^{q^r}. Therefore

v_p([Z^a]E(Z)^{p^s})=-(a-p^s)/(q-1).

Since 1<=p^s<q and (a-1) mod(q-1)=p^s-1,

floor((a-1)/(q-1))=(a-p^s)/(q-1).

Hence equality holds in FBA-1 for every order a=p^j, with the displayed f. In particular the bound is sharp at every p-power, even though it need not be optimal at every intermediate a. All arithmetic cases include h=1 (then s=0). This strengthens, but is not needed for, the slope-optimality result.

### Further checks

- FBA-5: targeted whole-proof check, /root/formal_bound, GPT-6 Astra Pro, effort not exposed, DP_MULT_20261121, 2026-11-21 Europe/Berlin: checked all substitutions are valid (T,U)-adically, coefficientwise application to each R[[U]] coefficient, and invariance identity by differentiating associativity. Passed.
- FBA-6: targeted whole-proof check, same metadata/date: checked denominator cancellation and the fractional scale pi^{a}; original divided powers fail already at a=q. Passed.
- FBA-7: targeted whole-proof check, same metadata/date: checked Frobenius powers of inverse series modulo pi, coefficient scaling pi^{a-p^s}, integer floor identity, and nonnegative valuation of D^a f. Passed.

## FBA-8. Stronger floor-sum bound (root's refinement, independently checked)

Define, for finite h,

E_h(n)=sum_{j>=1, h does not divide j} floor(n/p^j)
      =v_p(n!)-sum_{r>=1}floor(n/p^{hr}).

Then for every n>=0,

D^n(R[[T]]) is contained in p^{E_h(n)}R[[T]].

In particular

v_p(D^n f(0)) >= E_h(n)
 =n[1/(p-1)-1/(q-1)] - s_p(n)/(p-1)+s_q(n)/(q-1).

This is a stronger explicit error formula than FBA-1 at general n. For h=2 the exponent is exactly sum_{r>=0}floor(n/p^{2r+1}), which has the linear term n/p+n/p^3+... from Alpöge's step 2. It is an exact exponent in a proved lower bound, not a claim that the valuation equals it for every n and f, nor that the lower bound is optimal at every intermediate n. It is sharp at every n=p^j by FBA-7. For h=1 the exponent is zero. For h=infinity interpret E_infinity(n)=v_p(n!), as proved by FBA-2.

### Full proof

Write n=sum_{j>=0}d_jp^j in base p, 0<=d_j<p. By FBA-5, for each j, D^{p^j} is coefficientwise divisible by p^{B_h(p^j)}. Composition of these integral operators, using D^n=product_j(D^{p^j})^{d_j}, gives a coefficientwise exponent sum_jd_jB_h(p^j). For a p-power the maximum with zero is unnecessary; FBA-7 gives the exact expression

B_h(p^j)=v_p((p^j)!)-floor((p^j-1)/(q-1)).

If j=hr+s with 0<=s<h, then

floor((p^j-1)/(q-1))=(p^j-p^s)/(q-1)=sum_{t=1}^{floor(j/h)}p^{j-ht}.

Consequently

sum_j d_j floor((p^j-1)/(q-1))
 =sum_{t>=1}sum_{j>=ht}d_jp^{j-ht}
 =sum_{t>=1}floor(n/p^{ht}).

Also Legendre's digit formula gives

sum_jd_jv_p((p^j)!)=sum_jd_j(p^j-1)/(p-1)=(n-s_p(n))/(p-1)=v_p(n!).

Subtracting proves the exponent E_h(n). The equivalent floor sum removes exactly the indices divisible by h from Legendre's sum. Finally sum_{r>=1}floor(n/q^r)=(n-s_q(n))/(q-1), proved by the same digit expansion algebra with base q (no primality of q needed). Substitution yields the exact digit-error expression. All sums are finite for fixed n. This completes the proof.

### Check event

FBA-8: independent re-proof and targeted whole-proof check, /root/formal_bound, GPT-6 Astra Pro, effort not exposed, DP_MULT_20261121, 2026-11-21 Europe/Berlin. Root supplied the refinement; agent independently checked operator composition, base-p digit interchange, the residue j modulo h, the Legendre subtraction and base-q digit identity, including h=1 and n=0. Passed. No formal verification or computational certificate claimed.

## FBA-9. Optimal constant-error bound (step2_higher refinement, independently checked)

For finite height h, put q=p^h and c_h=1/(p-1)-1/(q-1). For every n>=0 and f in R[[T]], coefficientwise,

v_p(D^n f) >= max{0, ceil(c_h n-(h-1))}.

Here v_p of a series means the infimum of its coefficient valuations. The real affine inequality v_p(D^n f)>=c_h n-(h-1) has the best possible slope c_h and the best possible intercept h-1 for that slope: slope optimality is FBA-1/FBA-7, and the intercept is attained at n=q-1, f=T^{q-1}, for every normalized F. The stronger floor-sum FBA-8 and this constant-error bound can be combined by taking their maximum; neither is asserted to be the exact minimum valuation at every n.

### Full proof checked independently

The scale proof FBA-1 applies also to logarithm coefficients: if L(T)=T+sum l_nT^n, then v_p(l_n)>=-(n-1)/(q-1). Since l_n lies in K and hence has integral valuation, l_n is integral for 2<=n<q. Thus the strict coordinate change

Z=T+sum_{2<=n<q}l_nT^n

is defined over R and invertible over R. In this coordinate the normalized logarithm has form

L(Z)=Z+bZ^q+O(Z^{q+1}),

with v_p(b)>=-1. The coordinate change is strict, so the invariant derivation remains normalized. It suffices to prove the result in this coordinate, since integral coordinate changes preserve divisibility of power series and invariant differential operators.

For m>=0 let Delta_m be the integral translation operator defined by

f(F(Z,U))=sum_{m>=0}(Delta_m f)(Z)U^m.

Over K, the formal logarithm gives the Taylor identity

sum_m Delta_m U^m = exp(L(U)D).

Indeed F(Z,U)=E(L(Z)+L(U)), and ordinary formal Taylor expansion in the additive coordinate L(Z) gives this identity coefficient by coefficient; each U-coefficient involves only finitely many summands. Since L(U)=U+bU^q+O(U^{q+1}), comparison yields

Delta_m=D^m/m! for m<q,
Delta_q=D^q/q!+bD.

Let B=v_p(q!)-1. Since q=p^h, Legendre's formula gives

B=(q-1)/(p-1)-1=c_h(q-1).

Write q!=p^{B+1}v with v a unit. Rearranging the Delta_q identity gives

D^q=p^B u D+p^{B+1}T,

where u=-pvb lies in R and T=vDelta_q is an integral R-linear operator on R[[Z]]. No commutation property of T is required in what follows.

For 0<=n<q, integrality of Delta_n gives v_p(D^n f)>=v_p(n!). Write n=sum_{j=0}^{h-1}d_jp^j. Then

v_p(n!)-c_h n
 =n/(q-1)-s_p(n)/(p-1)
 =sum_{j=0}^{h-1}d_j[p^j/(q-1)-1/(p-1)].

All bracketed coefficients are nonpositive. Their minimum over 0<=d_j<=p-1 is therefore attained when all d_j=p-1, i.e. n=q-1, where the value is 1-h. This proves the claimed real affine bound for the base cases, including n=0.

Suppose n>=q and all smaller indices satisfy the bound. Multiply the operator identity on the right by D^{n-q}:

D^n=p^B uD^{n-q+1}+p^{B+1}T D^{n-q}.

The first term sends R[[Z]] into series of valuation at least

B+c_h(n-q+1)-(h-1)=c_h n-(h-1).

The second term has valuation at least

B+1+c_h(n-q)-(h-1)=c_h n-(h-1)+(1-c_h),

which is at least the required bound because 0<=c_h<1 for all finite h and all primes p (h=1 gives c_h=0). The nonarchimedean triangle inequality proves the induction step. Valuations are integral, giving the ceiling, and D preserves R[[Z]], giving the maximum with zero.

Finally, for n=q-1 and f(T)=T^{q-1}, the coefficient of derivative order n at zero is D^n f(0)=n!, because D(T)(0)=1 and f vanishes to exactly order n. Hence

v_p(D^{q-1}T^{q-1}(0))=v_p((q-1)!)=c_h(q-1)-(h-1).

Any universally valid inequality with the same slope and an error C<h-1 fails on this f and n for every F. Slope sharpness follows from FBA-1. This proves both asserted optimalities.

### Check event

FBA-9: independent re-proof / targeted whole-proof challenge, /root/formal_bound, GPT-6 Astra Pro, effort not exposed, DP_MULT_20261121, 2026-11-21 Europe/Berlin. The originating idea came from /root/step2_higher; root independently checked it and requested a challenge. This agent checked integral coordinate construction, invariance of normalized D, the exact formal Taylor coefficient at q, valuations of q! and b, the order of operator composition (which removes any need for commutativity of T), the digit maximum h-1, the induction endpoints, h=1, and the universal sharp witness n=q-1. Passed. This is a mathematical reading/re-proof, not a formal certificate.
