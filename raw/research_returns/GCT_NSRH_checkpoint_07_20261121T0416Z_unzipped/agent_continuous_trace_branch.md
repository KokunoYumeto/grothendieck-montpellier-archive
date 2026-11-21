# F55 supplement: a continuous positive-parameter branch

Author: /root, GPT-6 Astra Pro; effort not exposed. Run GCT_NSRH_20261121. Date: 2026-11-21 UTC.

Status: complete new proof below, awaiting an independent whole-proof check. The common-power input is the already checked F54 Part1. The branch-separation argument was independently suggested by /root/grothendieck_dictionary during discussion; the complete statement and proof are recorded here for review.

## Statement

Let b>1. Let f:[1,infinity) -> C be continuous. Suppose there is one monic irreducible polynomial P(v,Y) over C(v), of positive Y-degree, such that P(v,f(v))=0 whenever its rational-function coefficients are defined. Suppose further that, for every sufficiently large integer n,

    f(b^n) = sum_i m_i alpha_i^n,

where each m_i is a positive integer and each alpha_i is nonzero. Repeated roots may be grouped; neither semisimplicity nor a weight condition is assumed.

Then there are rational numbers r_i for which

    alpha_i = b^(r_i),
    f(v) = sum_i m_i v^(r_i)  for every real v>=1,
    f(1) = sum_i m_i > 0.

Every real power here uses the positive real branch. This is a theorem about a specified continuous scalar branch of one algebraic function. It is not a claim that a finite algebraic cover automatically supplies that branch, or that an arbitrarily selected place over v=1 belongs to it.

## Complete proof

By F54 Part1, applied to the eventual algebraic genuine power trace, choose a common positive integer L and integers a_i such that

    alpha_i^L = b^(a_i)

for every i. Put p(t)=sum_i m_i t^(a_i), a nonzero Laurent polynomial with positive integral coefficients after equal exponents are grouped.

For every sufficiently large integer k, the trace identity at n=Lk gives

    f(b^(Lk)) = p(b^k).

The finitely many poles of the coefficients of P do not interfere with all sufficiently large k. Therefore the rational function P(t^L,p(t)) vanishes at infinitely many distinct positive t=b^k and is identically zero. A nonzero rational function has only finitely many zeros, as follows directly from its polynomial numerator.

Set v=t^L. The field extension C(t)/C(v) is cyclic Galois, with automorphisms t -> zeta t for zeta^L=1. Because P is irreducible over C(v) and p(t) is one of its roots, all its roots are among p(zeta t). This assertion follows directly by taking the orbit polynomial of p(t) under that Galois group; its coefficients are fixed by the group, hence lie in C(v), and irreducibility makes P a scalar multiple of its minimal orbit factor. Repetitions among the expressions p(zeta t) are harmless.

Consequently, away from the finite exceptional set of coefficient poles, for every real v>=1 one has

    f(v) in { p(zeta v^(1/L)) : zeta^L=1 }.

The same inclusion holds at every exceptional point by continuity: approach it through nonexceptional values, choose a subsequence with the same root of unity from this finite set, and take the limit. Each of the finitely many displayed functions is continuous on the positive real axis, including v=1.

Write p_0(v)=p(v^(1/L)). For any root of unity zeta,

    |p(zeta v^(1/L))| <= sum_i m_i v^(a_i/L) = p_0(v).

If p(zeta v^(1/L))=p_0(v) at one positive v, equality in the triangle inequality, together with the positive real value of the sum and positive coefficients, forces zeta^(a_i)=1 for every i. Indeed all summands must have the same argument, and their sum is positive real, so each summand has argument zero. This includes negative and zero exponents without change. Therefore that branch is identically p_0 at every positive v. Thus no genuinely different branch in the finite displayed set meets p_0 anywhere on the positive real axis.

Let E={v>=1 : f(v)=p_0(v)}. It is closed by continuity. It is nonempty because it contains every sufficiently large b^(Lk). It is also open in [1,infinity): at any v_0 in E, the finitely many genuinely different branch values have a positive distance from p_0(v_0). Continuity of f and of those branches preserves a smaller positive separation on a neighborhood of v_0. The finite-branch inclusion then forces f to remain p_0 on that neighborhood. Connectedness of [1,infinity) gives E=[1,infinity).

It remains to remove the possible root-of-unity phases of the alpha_i. We have |alpha_i|=b^(a_i/L), and for every sufficiently large n the proved branch identity and the original trace law give

    sum_i m_i alpha_i^n = sum_i m_i |alpha_i|^n > 0.

Again equality in the triangle inequality forces every alpha_i^n to be positive real. Applying this at two consecutive sufficiently large integers n and n+1 makes alpha_i itself positive real. Thus alpha_i=b^(a_i/L). Setting r_i=a_i/L proves every assertion, including f(1)=sum_i m_i.

## Application to the actual marked trace

Use the actual rank-64 tensor module and X from F54 Part3. At b>1, X_b is Delta(b) times the projector onto its rank-eight N(D-2)^4 sector; Delta(b)>0. At the actual collision X(1)=0 as a matrix.

Suppose a finite algebraic matrix family F has a chosen continuous evaluation along v in [1,infinity), is regular at the endpoint v=1 on that same choice, and has invertible base value F_b. Retain the actual right-action commutation assumed in F54; only commutation of F_b with X_b is needed for the following trace calculation. Suppose the marked trace law holds eventually:

    Tr(X(b^n) F(b^n)) = Tr(X_b F_b^n).

The right side divided by Delta(b) is the genuine power trace of the invertible restriction of F_b to that eight-dimensional sector. The scalar branch

    f(v) = Tr(X(v) F(v)) / Delta(b)

is continuous on the chosen positive-parameter branch and satisfies one algebraic equation. It satisfies the irreducible minimal polynomial over C(v) of the trace element in the fixed coefficient field, normalized to be monic. The theorem gives f(1)=8. Actual regularity gives f(1)=0 instead. This contradiction excludes the marked law for arbitrary mixed radii and arbitrary rational or nonrational weights; no full-centralizer hypothesis is used. Rational powers are a conclusion of algebraic retuning, not a prior weight assumption.

The statement presupposes that the chosen continuous scalar evaluation is a branch of one irreducible algebraic function, as in the theorem. A single fixed finite coefficient field and continuous evaluation of its functions supplies exactly that condition. No simultaneous global diagonalization is required.

## Relation to the other-sheet construction

The F55 fractional example uses the arithmetic points t=2^(n/2)>0 on v=t^2 but chooses t=-1 for its regular collision. Its marked-sector trace h and some operator entries have poles at t=+1. The normalized marked scalar g=2(1+t)^2 itself has value8 at t=+1 and value0 at t=-1; the adjusted ordinary total trace 56+g is also regular there. These two endpoint choices cannot be joined by a continuous evaluation over the positive v-axis while retaining the arithmetic branch. The theorem therefore explains the extra compatibility that excludes that example. It does not invalidate the example under its actual one-place assumptions.

The preceding comparison of the example's formulas is to be confirmed against its final independently reviewed report; it is not an input to the theorem or application.

## Grothendieck dictionary for a separate paper part

The coefficient functions live on a finite algebraic cover of the parameter torus. The family, named actions and marked endomorphism are coherent affine module data, translated through EGA I Theorem1.3.7 p86, Corollary1.3.8 p87, and Theorem1.4.1 pp90-92. Representations and specified commuting morphisms use SGA3 I4.7.2-3, with archive cote90 scan17 as the audited affine-action anchor.

After the Kummer base change v=t^L, the genuine trace is an effective sum of torus characters t^(a_i), the positive cone in K0 of finite-dimensional torus representations. Tensor characters and the distinction between effective and virtual classes use SGA6 V sections2-3 and archive cote133 scan18. The positivity used in the separation proof is precisely positivity of actual weight multiplicities, not a positivity theorem for a lambda- or gamma-filtration and not positivity in a conjectural canonical basis.

The choice of a continuous branch over the positive real locus is additional comparison data on the complex points of that finite cover. EGA's module/sheaf equivalence does not supply it. The entire new proof of branch separation and phase removal is given above; it is not attributed to an archival theorem. In the finite-field dictionary, the positive integers are genuine Frobenius multiplicities on the marked subspace. A virtual alternating trace with cancelled coefficients does not satisfy this hypothesis merely by having the same numerical dimension.

## Checks actually performed

Root reconstructed the common-power reduction, orbit-field argument, finite-exception extension, positive-branch separation, open-and-closed continuation, and consecutive-index phase removal in the complete proof above. This is a mathematical proof check, not a numerical or formal certificate. Independent review is requested on this exact report.
