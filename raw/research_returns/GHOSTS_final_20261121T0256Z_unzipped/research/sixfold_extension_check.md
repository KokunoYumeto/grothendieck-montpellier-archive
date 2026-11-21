# Independent checks of R22 and R23: lattice scope and degree-preserving contraction

Run GHOSTS-20261121. Date2026-11-21. Checker: GPT-6 Astra Pro, inherited effort not separately observable, `/root/bounded_specialization`. Full source of `work/root_sixfold_extension.md` read. This memo checks R22--R23; it does not independently certify the Prym support/dominance input R20 or the separate constant audit of R21.

## Verdict

R23 passes, including arbitrary effective three-cycles and all multiplicities. R22 is valid after expressly making the fixed rational target lattice monodromy-invariant on a finite etale cover. A fixed rational O_K-action can be made integral by a fixed isogeny, but the change of polarization and its explicit degree cost must be included. The formulas below make both reductions precise.

## X01. Compensation of the rational Hermitian form

Let A be an O_K-integral polarized Weil fourfold of signature(2,2), polarization H, and fixed rational Hermitian determinant class d in Q_{>0}/Nm(K*). Any positive rational representative can be multiplied by a rational square to become a positive integer: if it is a/b, multiply by b². Fix such an integer d. On A'=E² with mixed K action, H'=theta1+d theta2 has Hermitian matrix diag(1,-d), up to the common convention for the alternating-to-Hermitian conversion. Hence det(A')=-d, while the direct sum A x A' has determinant -d², equivalent to -1 modulo norms, and signature(3,3).

This rational Hermitian space is split. A direct argument avoids hiding the classification in a citation: its underlying rational quadratic form has indefinite signature(6,6), so Meyer's theorem supplies a rational isotropic vector. Split a hyperbolic K-plane. The remaining Hermitian rank4 space has signature(2,2); Meyer supplies another hyperbolic plane. The remaining binary Hermitian form has determinant class -1 and signature(1,1). Diagonalize it as (a,b); the determinant condition says -ab is a norm, so -b/a is a norm as well, and an isotropic vector follows. Thus there are three hyperbolic planes. Meyer's theorem and diagonalization are background here; the determinant reduction has been checked.

Consequently choose a fixed K-linear rational isometry F from the homology space of A x A' to the standard principal sixfold lattice's rational Hermitian space. Transport the complex structure by F. Choose m>=1 so that mF sends the source integral lattice Lambda into the standard unimodular lattice Lambda0. Fiberwise this gives an isogeny h:A x A' -> Q satisfying

    h^*theta_Q=m²(H+H').

The target complex structure remains compatible with the standard positive polarization and K action, so Q lies in the relevant principal signature(3,3) domain/component after the separately audited integral component identification.

## X02. The necessary family cover and exact degree factors

A fixed rational isometry need not itself intertwine the original monodromy with automorphisms of Lambda0. This is the only omitted family step in the original R22 sentence. It has a standard finite-cover repair.

In the source rational homology space, set Lambda_Q=(mF)^(-1)Lambda0. It contains Lambda with finite index. Choose n with Lambda_Q contained in (1/n)Lambda. The subgroup Lambda_Q/Lambda is then a subgroup of the finite n-torsion local system. After a finite etale level-n cover trivializing this local system, that subgroup is globally defined. Quotienting the abelian scheme by it gives the target family Q, and h becomes a genuine isogeny of families. Equivalently, take the finite-index subgroup of monodromy stabilizing Lambda_Q. The target principal polarization and K action descend because their lattice forms and O_K-stable target lattice are invariant. If an actual universal line bundle representing the polarization is needed for the Hilbert construction, pass to a further finite level/theta cover; the fiberwise degree constants do not change.

Write h0=H⁴/4!, a positive integer. Since H'^2=2d,

    (H+H')⁶=binom(6,4)H⁴H'^2=720 d h0.

Therefore

    e=deg h=m^12 d h0,
    deg_(H+H')(h^*Z)=(e/m⁶)deg_theta_Q(Z)
                   =m⁶ d h0 deg_theta_Q(Z)              (X02.1)

for any codimension-three cycle Z on Q. The calculation is projection formula applied to h^*theta_Q=m²(H+H'). This is an integer degree factor, even though the intermediate expression e/m⁶ might initially look rational. Isogeny pullback is finite flat and effective with scheme-theoretic multiplicities.

If Gamma is the class constructed in R23, tau=(h^*)^(-1)Gamma can be written explicitly

    tau=(1/e)h_*Gamma.

Since3delta_t Gamma is integral, one may choose

    delta_tau=3delta_t e,
    U_tau=-tau²=t²/e.                                  (X02.2)

Here h_* preserves integral cohomology, and h_*h^*=e. Thus no exterior-matrix denominator computation is necessary for a sufficient bound; it can only improve the conservative value in (X02.2). Both quantities are constant after the family isogeny is fixed and the class is flat. If R21 supplies C6(delta_tau,U_tau), pullback and R23 give the fourfold bound

    C4=m⁶ d h0 C6(3delta_t e,t²/e),

since the factor m⁶ d h0 is at least1 and therefore also bounds the unchanged multiplier. This is conditional only on the independently established R20--R21 sixfold bound and the target component identification; no new dependence on a reduction prime occurs.

## X03. Making a fixed rational O_K-action integral, with its cost

Now suppose the original family only has a rational action eta:K->End^0(A), with a fixed rational K-lattice and polarization H. Work first in homology V and put

    Lambda_sat=O_K Lambda,

where Lambda=H_1(A,Z). This is a finite-index superlattice because the finitely many generators of the rational action have a common denominator. Choose a positive integer M with M Lambda_sat subset Lambda. It is stable under the fixed family monodromy because that monodromy commutes with eta. The inclusion Lambda subset Lambda_sat defines a fixed isogeny

    q:A -> A_sat,
    e0=[Lambda_sat:Lambda].

The target now has an integral O_K-action. If E_H is the original integral alternating polarization form, then M²E_H is integral on Lambda_sat. It defines a compatible polarization H_sat with

    q^*H_sat=M²H.

At the family level the subgroup Lambda_sat/Lambda is a finite locally constant subgroup of A[M], and the quotient is an abelian scheme; a finite etale cover may be taken to fix level data and a line-bundle representative. These operations do not change the constants M,e0. The target class is

    t_sat=(q^*)^(-1)t=(1/e0)q_*t.

Thus delta_sat=delta_t e0 is a sufficient integral denominator, and t_sat²=t²/e0. Apply the integral-action construction to the fixed target polarized lattice. If it produces a bound C_sat, pulling cycles back gives the original class with the same multiplier and with numerator degrees multiplied by e0/M⁴. A sufficient integral final complexity bound is

    max(C_sat, ceil((e0/M⁴) C_sat)).                     (X03.1)

There is no assertion that these lattice saturation and polarization costs are1, or that they are uniform over varying rational orders or unbounded lattice denominators. They are explicit fixed data of the given family. This resolves the rational-action scope of R22 without conflating it with the integral-action case.

## X04. Exact contraction identity and norm

On A'=E² let F1,F2 be coordinate fibers and put D=Gamma_1-F1-F2. It is in the rational Weil plane for the mixed K action. Indeed its Kunneth class is the cross (1,1) part, the sum of the two conjugate K-exterior lines. The intersection calculations are

    D²=-2,
    D.R'D=D.(R')²D=1,

where R' is pullback by diag(omega,bar omega). For example R'Gamma_1 is Gamma_(omega²), their intersection is deg(1-omega²)=3, every graph meets each coordinate fiber in degree1, and (F1+F2)²=2. These formulas include intersection multiplicities.

On the fourfold Weil plane put R_A=[omega]^*, so1+R_A+R_A²=0 and t.R_A t=t.(R_A)²t=-t²/2. Define

    Pi=(1+R_A tensor R'+R_A² tensor(R')²)/3,
    Gamma=-Pi(t tensor D).

The characters on the fourfold K-exterior lines are omega,omega², whereas on the twofold K-exterior lines they are omega²,omega. Hence Pi selects exactly the two equal-embedding exterior lines, which form the sixfold Weil plane. Contraction gives

    p_A*(Gamma.p_A'^*D)
      =-(1/3)(-2t+R_A t+R_A²t)=t.

The projector is self-adjoint for the intersection pairing because it averages a finite group of isometries. Thus

    Gamma²=(t tensor D).Pi(t tensor D)
           =(1/3)(-2t²-t²/2-t²/2)=-t².

This proves -Gamma²=t² and shows that3delta_t Gamma is integral. The required multiplier3 is already included in delta_tau above.

## X05. Effectivity and the no-degree-cost contraction

Write D+=Gamma_1, D-=F1+F2. Let H0=theta1+theta2. The numerical identity

    2H0-Gamma_1=Gamma_-1

shows that2H0-D+ is nef; it is an effective elliptic divisor class on an abelian surface. Since H'=theta1+dtheta2 with d>=1, H'-H0 is nef. Therefore2H'-D+ and H'-D- are nef.

Let X be any effective integral dimension-three cycle on A x A'. For each of the three divisor components involved, choose a general translate in A'. Its pullback to A x A' contains no irreducible component of X unless the resulting intersection is empty; the standard translation incidence argument gives a common nonempty open set of permitted translates. A proper Cartier divisor cut of an effective cycle is effective with its intersection multiplicities. Thus the resulting two-cycles push forward to effective cycles on A, with lower-dimensional images contributing zero. Translation preserves the cohomology classes.

By projection formula and nef intersection inequalities,

    deg_H p_*(X.D+) <=2 H²H'.X,
    deg_H p_*(X.D-) <= H²H'.X.

All mixed intersections of the nef divisors H,H' with X are nonnegative, and3H²H'.X is one term of (H+H')³.X. Consequently the two displayed degrees are at most (2/3)deg_(H+H')X and (1/3)deg_(H+H')X. These inequalities need no smoothness assumption on X and hold for cycles with all multiplicities retained.

If N Gamma=[X+]-[X-] and both numerator degrees are <=C, the signed contraction has positive numerator

    p_*(X+.D+)+p_*(X-.D-)

and negative numerator

    p_*(X+.D-)+p_*(X-.D+).

Both degrees are at most(2/3+1/3)C=C, and its class is Nt. The same N is used. The contraction therefore introduces no extra degree factor and no extra multiplier beyond those already needed to represent Gamma.

## Source level and checks

The translation-and-nef argument is independently rederived above and agrees with the method checked in agent cm_transport's C03. Standard background used: quotient of an abelian scheme by a finite flat subgroup; Riemann forms and polarizations; Meyer's isotropy theorem; finite etale level covers; projection formula; numerical nef intersection positivity. The rational Hermitian determinant computation, finite-cover repair, all degree exponents, sufficient denominators, contraction identity and signed effectivity argument were each read in full and checked here. This memo does not claim new proofs of the background theorems or of Schoen's sixfold Prym dominance.

## Check events

statement_id	date	who_model_effort_run	type	outcome	method_or_locator
R22-X01-X02	2026-11-21	GPT-6 Astra Pro; inherited effort not separately observable; GHOSTS /root/bounded_specialization	independent re-proof	Rational compensation and family isogeny checked after adding finite etale lattice-stabilizer cover; exact factors e=m^12 d h0 and e/m^6 verified; delta_tau=3delta_t e and U_tau=t²/e supplied	work/root_sixfold_extension.md R22; X01-X02 here
R22-X03	2026-11-21	GPT-6 Astra Pro; inherited effort not separately observable; GHOSTS /root/bounded_specialization	independent re-proof	Fixed rational action made integral by lattice saturation; polarization M² and pullback e0/M⁴ explicitly charged; scope limited to fixed lattice family	X03 here
R23-X04-X05	2026-11-21	GPT-6 Astra Pro; inherited effort not separately observable; GHOSTS /root/bounded_specialization	independent re-proof	Character projector, contraction, norm, denominator3, general translated cuts, nef degree bounds and signed sums all checked; no degree cost	work/root_sixfold_extension.md R23; X04-X05 here
