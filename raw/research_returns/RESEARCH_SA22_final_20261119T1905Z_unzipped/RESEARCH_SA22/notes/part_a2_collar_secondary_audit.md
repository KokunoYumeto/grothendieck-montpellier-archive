# Independent audit of the general and fully specified collar proofs

Auditor: GPT-6 Astra, OpenAI, ChatGPT Pro mode, `part_c_algebra` agent. Date:19 November2026. Root owns `sections/part_a2_collar_general.tex`; the A567 researcher owns `sections/part_a567_collar_explicit.tex`. No competing proof edits were made. The exact independent events are in `checks/part_a2_collar_secondary_events.tsv`.

## General collar equation and sign convention

For the retained surface the outward unit normal points into the removed collar. With `k_g=g(nabla_T T,n)`, conformal scaling gives `k_{exp(2u)g}=exp(-u)*(k_g-partial_n u)`, while `K_{exp(2u)g}=exp(-2u)*(-1-Delta_g u)`. Thus curvature-1 and geodesic new boundary give precisely

    Delta_g u=exp(2u)-1,     partial_n u=k_g.

This convention makes a constant positive inward cut r=f>0 have k_g=tanh(f)>0. The sign is therefore consistent with the constant-width monotonicity theorem. The difference of two solutions satisfies `(Delta-c)v=0`, with c>0 and zero Neumann data; integration yields uniqueness. If k_g>=0, a negative minimum of u cannot be interior, and Hopf's lemma makes its outward derivative negative at a boundary minimum, contradicting the boundary condition. If k_g is positive somewhere, u cannot be identically zero; the same principle gives strict positivity throughout. This argument does not assert positivity for sign-changing k_g.

For an inward graph r=epsilon*a(s), the signed curvature variation is epsilon*(a-a''). The pulled-back operator is evaluated at u0=0, so derivatives of the coordinate pullback multiply zero. The first variation therefore solves `(Delta-2)h=0`, `partial_n h=a-a''`, independently of the chosen fixed-domain identification. The Neumann operator is invertible because `integral(|grad h|^2+2h^2)` is coercive; smooth-domain elliptic regularity supplies the Holder-space isomorphism used in the implicit-function theorem. For each fixed smooth a, the resulting C2 expansion is justified.

The high-frequency approximate solution has residual

    R_n=(n+1/n)*exp(-n*r)*(n^2*tanh(r)^2-n*tanh(r)-2)*cos(n*s)

where the cutoff is1. Changing variables t=n*r gives squared L2 norm O(n), since the integral of `(t^2+t+2)^2*exp(-2t)` is23/4. Cutoff terms are supported a fixed positive distance from the original boundary and are exponentially small times a polynomial in n. The even double across the geodesic boundary is smooth because cosh(r) is even. The L2 forcing can be extended evenly even though its derivative need not match; this is enough for the weak H2 solution. The solution is even by uniqueness and has zero Neumann trace. The correction equals v_n-w_n on the original surface.

The integrated Bochner identity on curvature-1 has the **plus** gradient term:

    ||Hess e||_2^2=||Delta e||_2^2+||grad e||_2^2.

Together with `(Delta-2)e=-R`, energy and H2-to-C0 embedding give an O(sqrt(n)) pointwise error, smaller than the negative boundary mode of order n. The proof correctly fixes n large first, then epsilon small. Finally, the retained old area is smaller than2*pi while its newly uniformized geodesic-boundary area is2*pi; therefore u must also be positive somewhere. The general-shape claim is fully supported.

## Fully specified comparison: n=10000, epsilon=10^-14

I independently rederived every continuous estimate and checked the existing symbolic certificate `code/part_a567_collar_explicit.py` against its saved output. This was a proof audit, not a second numerical approximation or a rerun of the same certificate.

### Embedded disjoint collars

With `y=arctan(sinh r)`, the metric is `sec^2(y)*(ds^2+dy^2)`. The closed y-collars of width1/50 lie strictly inside the embedded collars given by the double's collar theorem: `tan(1/50)<=100/4999<2/81<1/sinh(pi)`. The final inequality follows from pi<4 and e<3. The new graph lies within y<1/100 because y<=r<=3*epsilon/2. The three supports are therefore disjoint; at most one cutoff term is nonzero at any point.

### Interior supersolution

The quintic cutoff has derivatives `-30*t^2*(1-t)^2` and `-60*t*(1-t)*(1-2*t)`. Their maximum absolute values are15/8 and10/sqrt(3); dividing by b=1/100 and b^2 gives the stated200 and60000 bounds. The function is C2 across the transition endpoints and vanishes with its first two derivatives at the outer edge.

For `H=2000-sum eta(y_i)*tan(y_i)`, the identity L(tan y)=0 and bounds tan(y)<1/40, sec^2(y)<2 give

    LH<=-4000+60000/40+2*200*2=-1700.

The separated mode `f_n=exp(-n*y)*(n-tan y)` satisfies

    f_n''=(n^2+2*sec^2 y)*f_n,    -f_n'(0)=n^2+1.

Hence the cutoff residual is only `(eta''*f_n+2*eta'*f_n')*cos^2(y)*cos(n*s)`. Its magnitude is bounded by `40600102300*exp(-100)<40600102300/2^100<1`. Therefore `Psi=2H+w/2` has `L Psi<0`. For U=epsilon*Psi, the elementary inequality exp(2U)-1>=2U gives `Delta U<=exp(2U)-1` even where U is negative. No mistaken sign assumption enters this step.

### Exact graph normal and signed curvature

For r=f(s), set p=f', c=cosh(f), q=p/c. The graph velocity is `V=p*partial_r+partial_s`, with squared speed E=p^2+c^2. The outward normal is

    N=(-c*partial_r+(p/c)*partial_s)/sqrt(E).

Using `Gamma^r_ss=-cosh(r)*sinh(r)` and `Gamma^s_rs=tanh(r)`, the normal component of the unnormalized acceleration is

    [-c*f''+sinh(f)*(c^2+2*p^2)]/sqrt(E).

Dividing by E gives exactly

    k_g=[tanh(f)*(1+2*q^2)-f''*sech(f)^2]/(1+q^2)^(3/2).

Thus the curvature formula and its outward sign are independently derived, rather than accepted from the symbolic program.

### Normal and curvature error constants

On the inner collar `F_n(r)=exp(-n*arctan(sinh r))*(n-sinh r)`. The elementary derivative bounds yield `|F_n|<=2n`, `|F_n'|<=2n^2`, and `|F_n''|<=n^3+2n^2+5n+1<=4n^3`. For Psi this implies the stated bounds `|Psi_r|<=2n^2`, `|Psi_s|<=n^2`, `|Psi_rr|<=3n^3`. At the old boundary, `-Psi_r=a-a''+1` exactly.

Writing the normal derivative as `(1+q^2)^(-1/2)*[-Psi_r+(p/c^2)*Psi_s]` gives the independent bound

    |partial_N Psi-(a-a''+1)|
      <=3*n^3*f+n^2*p^2+n^2*|p|
      <=5*epsilon*n^3+(epsilon^2*n^4)/4
      <10*epsilon*n^3.

The three coefficients respectively come from the displacement, the normalization of the normal, and its tangential component. All three are needed.

For curvature, `|tanh(f)-f|<=f^3/3`, `1-sech(f)^2<=f^2`, and `1-(1+x)^(-3/2)<=3*x/2`. The derivative of `(1+2x)*(1+x)^(-3/2)` is `(1/2-x)*(1+x)^(-5/2)`; on[0,1] its absolute value is at most1/2. The proof's looser2*x bound is valid. Using f<=3*epsilon/2, |f'|<=epsilon*n/2, |f''|<=epsilon*n^2/2 produces

    |k_g-epsilon*(a-a'')|
       <=epsilon^3*(9/8+(15/8)*n^2+(3/16)*n^4)
       <=epsilon^3*n^4.

Consequently

    partial_N U-k_g>=epsilon*(1-10*epsilon*n^3-epsilon^2*n^4)>0,
    10*epsilon*n^3+epsilon^2*n^4=1/10+10^-12<1.

The estimates remain valid on the two nonoscillating boundaries, where they are deliberately much looser.

### Comparison direction and the certified point

For W=U-u, subtraction and the positive divided difference of exp(2x) give `(Delta-c0)W<=0` with c0>0. Its outward derivative is positive. A negative interior minimum would have `(Delta-c0)W>0`; a negative boundary minimum would have strictly negative outward derivative by Hopf's lemma. Both are impossible. Therefore u<=U, which is the required **upper** bound.

At s=pi/n, cos(n*s)=-1 and f=epsilon/2. The bounds n*y<=n*epsilon/2<1/10, exp(-n*y)>=9/10, and sinh(f)<1 imply

    Psi<=4000-(9/20)*(n-1)=-9991/20,
    u<=-9991/(2*10^15)<0.

The comparison cutoff is only C2, but C2 is enough for the pointwise equation and the maximum/boundary-point principles. It does not limit the regularity of the actual new boundary: the latter is defined by the analytic function1+(1/2)cos(n*s) in analytic Fermi coordinates. Positive widths and disjoint collars verify the topology and embeddedness. Area again forces u>0 somewhere. This verifies the entire explicit counterexample without an unspecified asymptotic threshold and without a numerical PDE solve.
