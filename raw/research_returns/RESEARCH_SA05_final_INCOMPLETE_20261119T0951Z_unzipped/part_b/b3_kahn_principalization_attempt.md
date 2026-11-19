# A certified principalization obstruction in the affine-surface route

Date: 19 November 2026. Scope: an independently checked failed approach to the remaining B.3 Tate/BSD gate. This does **not** refute Tate, and does not exclude choosing a different successful Nisnevich neighbourhood.

## Source and exact attempted step

Opened Bruno Kahn, *An approach to the Tate conjecture for surfaces over a finite field*, dated 13 May 2025, https://webusers.imj-prg.fr/~bruno.kahn/preprints/Tentative3.pdf. Theorem 1.1, Proposition 2.1, Corollary 3.3, and §§3.2.2–3.2.4 were read in full; web references `turn485153869view1` and `turn343496468view0`.

For an affine open U in a smooth projective surface, with Pic(U)=0, and a smooth irreducible divisor Z, Corollary 3.3 supplies an étale Nisnevich neighbourhood U1→U, isomorphic over Z, such that H¹(U1,Q_l/Z_l)→H¹(Z,Q_l/Z_l) is surjective. The normalization Ubar1 of U in the function field of U1 is finite over U; the inverse image of Z decomposes as Z⊔T. The two proposed additional conditions in §3.2.3 are:

1. H¹(Ubar1,Q_l/Z_l)→H¹(Z,Q_l/Z_l) is surjective.
2. Z has a principal equation f1 on **Ubar1**, with f1=1 on T.

The example below satisfies condition (1), but Z is not even principal on Ubar1. Kahn §3.2.4 anticipated a curve example; the same construction yields an affine surface, including a nonzero geometric residue group at the obstructing prime.

## Explicit example

Let E/F2 have affine equation y²+y=x³+x+1 and origin O at infinity. Its homogeneous gradient ideal is (x²,y²,z²), so E is smooth. Exact counting gives E(F2)={O}, E(F4) of order 5, and E(F16) of order 25. The script proves every nonzero F16-point has order 5.

Let C=E−{O} and U=C×G_m, viewed as an affine open of X=E×P¹. The exact divisor sequence gives Pic(C)=Pic(E)/Z[O]=E(F2)=0. Thus the coordinate ring of C is a Dedekind PID, and adjoining an invertible variable gives a UFD; hence Pic(U)=0. The two factor classes generate NS(X_Fbar), so Frobenius acts trivially on it. This also follows from the projective-bundle formula, since the second factor is P¹.

The closed point z of C cut out by x²+x+1=0 has residue field F16. Indeed its coordinate equations reduce to x=y²+y and y⁴+y+1=0, the latter irreducible over F2. Therefore Z=z×G_m is a smooth irreducible principal divisor of U and Z≅G_m/F16.

Write F16=F2[v]/(v⁴+v+1), and choose P=(v²+v,v). Its Frobenius orbit is P,πP,−P,−πP, of length four. Put

Ubar1=C_F16×G_m,

U1=(E_F16−{O,πP,−P,−πP})×G_m.

The constant extension Ubar1→U is finite étale of degree 4. The open U1 is affine, and U1→U is étale with inverse image of Z exactly P×G_m, mapped isomorphically to Z. Since Ubar1 is normal and finite over U with function field equal to that of U1, it is precisely the normalization demanded in §3.2.2.

Projection Ubar1→G_m/F16 restricts on P×G_m to an isomorphism. Its pullback therefore splits the restriction map

H¹(Ubar1,Q_5/Z_5)→H¹(P×G_m,Q_5/Z_5).

Condition (1) holds. But the Cartier divisor P×G_m represents the pullback of [P−O] in Pic(C_F16)≅E(F16). Projection induces an injection on Picard groups because it has the section t=1. Since [P−O] has order 5, this divisor is nonprincipal. Condition (2) fails before imposing its extra congruence on T.

The geometric residue is nontrivial: H¹(G_m/Fbar,Q_5/Z_5)≅Q_5/Z_5(−1), whose F16-Frobenius invariants have order 5 because v_5(16−1)=1. Thus the example does not merely exploit the constant divisible summand of H¹(Z).

### Essential scope distinction

The selected divisor becomes principal after restricting to U1: the removed point −P has class −[P−O], so its removal kills the class. The failure is on the complete normalization Ubar1, exactly where §3.2.3(2) asks for an equation. No claim is made that every possible U1 fails, or that the desired Gysin vanishing fails. Indeed X=E×P¹ is of abelian type and satisfies Tate.

## Unbounded version on the same fixed surface and prime

The obstruction is not bounded by a fixed power of 5 as the selected neighbourhood varies. The Frobenius relation is π²−2π+2=0, hence π⁴=−4 in End(E). For every r≥1, choose P_r∈E[5^r](Fbar) with [5^{r−1}]P_r=P. Such a point exists because 5 is invertible, and it has exact order 5^r.

Its Frobenius orbit length is d_r=4·5^{r−1}. Indeed an orbit-fixing power must have exponent divisible by 4 after multiplication by 5^{r−1}; then π^{4k}P_r=(−4)^kP_r. The elementary identity v_5((1−5)^k−1)=1+v_5(k) gives the asserted minimum. Let z_r be this degree-d_r closed point of C. Since Pic(C)=0, it is principal. Put Z_r=z_r×G_m, pass to the constant extension F_{2^{d_r}}, and delete all conjugate components except P_r×G_m. This repeats the construction and condition (1) remains split-surjective.

On the full normalization the selected divisor has exact Picard order 5^r. At the same time

v_5(2^{d_r}−1)=v_5(16^{5^{r−1}}−1)=r,

so the geometric residue invariant group has exact order 5^r. Thus a proposed *uniform exponent bound for this principalization construction* is false even on this one fixed surface where Tate is already known. This is a quantified obstruction to that method, not a stronger form of the main conjectural gate.

## Source-proof qualification

The displayed equality in Kahn Proposition 1.3, H¹(G,NS⊗Q_l)=H¹(G,NS)⊗Q_l=0, cannot be used with continuous l-adic cohomology: for G=Zhat and trivial NS=Z, the left group is Q_l. The proposition's conclusion is correct; the divisor-subspace Galois splitting proved in Part B repairs this step. No new result above uses the displayed equality.

## Reproduction and checks

`code/kahn_principalization_counterexample.py` and `output/kahn_principalization_counterexample.txt` contain the complete exact computation: homogeneous smoothness, quartic irreducibility, field arithmetic, all F16-points and their orders, the four-point Frobenius orbit, and the defining equation of z. Runtime: 0.042287 seconds in this run before the additional valuation-family table.

Part D independently checked the elliptic Frobenius relation and the distinction between the normalization and its shrunk open. The scoped counterexample was sent to root; the main B.3 finiteness status is unchanged.
