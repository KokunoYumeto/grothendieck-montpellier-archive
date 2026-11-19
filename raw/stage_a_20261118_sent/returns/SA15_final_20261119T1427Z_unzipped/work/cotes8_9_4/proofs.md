# Independent mathematical checks

Reader: GPT-6 Astra Pro; effort setting not exposed. Run SA15-20261119/cotes8_9_4, 19 November 2026. The following arguments are this run's checks, not reconstructed missing manuscript text. They change no diplomatic reading.

## 1. Constant 5-torsion does not determine potentially-good inertia

This checks the two questions in cote 9:13–14 (Pro lines473–487). Let F/Q5 be the unramified extension of degree 4, choose t with t^8=5, and put K=F(t). Thus K is complete discretely valued, has ramification index8 and residue field F625. Set

E_b:y²=x³+5⁴, and E_g:y²=x³−x.

Both are elliptic curves over K. We show that their finite étale K-group schemes E_b[5] and E_g[5] are both constant of rank25, while their finite potentially-good inertia representations differ. In particular K contains μ5. The trace assertion below concerns ℓ-adic inertia for ℓ≠5, or the finite Weil–Deligne/potentially-crystalline monodromy. It is not an assertion about the full raw5-adic Tate module.

### The bad curve has constant 5-torsion

For y²=x³+B the division-polynomial recurrence gives

ψ5=5x¹²+380Bx⁹−240B²x⁶−1600B³x³−256B⁴.

The saved script derives this identity from ψ5=ψ4ψ2³−ψ3³, rather than taking the displayed polynomial as input. For B=5⁴, substitute x=t¹⁰X and divide by t¹²⁸. The resulting integral polynomial is

P(X)=X¹²+76t²X⁹−48t⁴X⁶−64t¹⁴X³−256.

Its reduction is X¹²−1. The residue field F25⊂F625 contains all12 roots, and all are simple. For each root X0, X0³ has a square root in F25: X0 has order dividing12, so X0³ has order dividing4, and F25* has order24. Each has exactly two nonzero square roots. The script enumerates all12 x-values and 24 pairs in F25=F5[a]/(a²−2), checking both derivatives.

Hensel's lemma lifts each X0 uniquely to a root X of P in O_K. After y=t¹⁵Y the curve equation becomes Y²=X³+t². The derivative2Y is a unit at each of the two residual choices, so Hensel again lifts both. The resulting24 distinct points are precisely the nonzero5-torsion points, since their x-coordinates are the roots of ψ5 in characteristic 0. Thus E_b[5] is constant. Nondegeneracy of the Weil pairing now implies μ5⊂K.

### Bad reduction and the finite inertia character

The displayed equation has Δ_b=−432·5⁸. With v_K(t)=1, v_K(Δ_b)=64≡4 (mod12). Discriminant valuations of isomorphic Weierstrass equations differ by a multiple of12. Good reduction would provide a unit-discriminant equation, which is impossible. Thus E_b has bad reduction over K.

Let a³=5. The extension L=K(a) has degree3 because v_K(5)=8 is not divisible by3. It is tame and cyclic, since K contains μ3. With u=a², the substitutions x=u²X,y=u³Y give Y²=X³+1, a smooth elliptic curve in characteristic5. The generator a↦ζ3a acts on its special fiber by an order 3 automorphism (X,Y)↦(ζ3X,Y), up to replacing the generator by its inverse. On an ℓ-adic Tate module, ℓ≠5, its two eigenvalues are ζ3 and ζ3⁻¹, hence its trace is −1. The special fiber is supersingular, as the coefficient of x⁴ in (x³+1)² is0 modulo5.

### A good curve with the same5-torsion module

The curve E_g has good ordinary reduction at5: #E_g(F5)=8, so its Frobenius trace is−2 and its Hasse invariant is nonzero. It has complex multiplication by i, already defined over Q5 since −1 is a square there. The automorphism is (x,y)↦(−x,iy). On E_g[5] its minimal polynomial divides T²+1=(T−2)(T−3); the two eigenspaces are distinct Galois-stable lines. Exactly one is the étale line of the ordinary5-divisible group. Its unramified character has Frobenius value3 modulo5, or its inverse under the opposite Frobenius convention, and therefore order4. The degree 4 unramified extension F kills that character.

The determinant of E_g[5] is the mod5 cyclotomic character, by the Weil pairing. Since μ5⊂K, this determinant is trivial on G_K. The second eigencharacter is therefore also trivial. Consequently E_g[5]≅(Z/5)²≅E_b[5] over K. Good reduction makes the ℓ≠5 inertia representation of E_g trivial, with trace 2. In the common finite good-reduction inertia quotient of order 3 the two traces are2 and−1.

All hypotheses of the stated two-curve question are satisfied: perfect residue field, complete DVR, μ5⊂K, both curves potentially good, equal mod5 modules, and a p-regular inertia element. The bad curve additionally has supersingular potential reduction. This is an independent counterexample in this run. It does not identify the example communicated by Tate, nor determine the leader of the marginal annotation.

Certificate: `code/check_elliptic_inertia_counterexample.py`, `outputs/elliptic_inertia_counterexample.json`.

## 2. The additional torsion term in cote 4:11

Use the manuscript's hypotheses for its amended exact sequence and put i=n−1. Let A=H^i_cris(X/W), T=A_tor, A_f=A/T, and C=H^(i+1)_cris(X/W)[p]. Write st for the bijective Frobenius summand after reduction to k. It is an exact functor over a perfect field.

Derived crystalline base change gives

0→A/pA→H^i_dR(X/k)→C→0.

Since A_f is W-free, tensoring0→T→A→A_f→0 with k gives

0→T/pT→A/pA→A_f/pA_f→0.

Apply st, and use the stable augmentation H^i_dR,st≅H^i(O_X)_st. If

b=dim(T/pT)_st, c=dim C_st, and k0=dim ker v,

then the difference between the two sides of the inequality at Pro line1256 is **b+c**. In contrast the amended sequence at lines1105–1108 gives

dim kerφ=c−k0.

Therefore equality in line1256 means b=c=0; bijectivity ofφ means c=k0. The two conditions coincide under the sufficient additional hypotheses b=0 and ker v=0. Neither b nor k0 may be dropped solely from the displayed sequences. Even when v is injective, preceding-degree stable torsion b remains. The linear-algebra pattern b=1,c=0,k0=0 has bijectiveφ and strict inequality. This is an algebraic countermodel to the asserted implication, **not a claimed geometric counterexample**.

For the author's surface example, H¹_cris is torsion-free, so b=0, and v is injective. The dimension objection does not refute that example. A product construction in higher dimension would require a separate verification of the needed geometric inputs and ample-section hypotheses; it is not used as evidence here.

Certificate: `code/check_calculations.py`, section `torsion_criterion` in its JSON output.

## 3. Other checks, with their logical scope

The same calculation script verifies an integral S3 representation generated by S=[[0,1],[1,0]] and R=[[0,−1],[1,−1]]. Reduction identifies its six matrices with GL2(F2); reducing modulo4 therefore gives a section GL2(F2)→GL2(Z/4). This refutes the universal rank≥2 nonlifting prediction on cote 8:81. It does not by itself classify every exceptional pair.

For the truncated Dieudonné coefficient pairing the script fixes k=Fp and the ring with FV=p,F^(n+1)=V^(n+1)=0. The coefficient of 1 pairing into Z/p^(n+1) is perfect in the tested small instances; replacing the target by Z/p^n makes it degenerate. This diagnoses the importance of the index convention but cannot select the manuscript's ink. The V-dual formula using F instead of V fails already for F=J3,V=0 over Fp, because the resulting proposed dual F,V violate FV=0. The appropriate semilinear twist is still required in the corrected general formula.

The lines span(1,0) and span(1,ε) over Fp[ε]/ε² become equal under Frobenius but are unequal before it. Thus cote 9:17 correctly rejects descent of equality along a nonflat Frobenius. Faithfully flat Frobenius on the smooth universal deformation space gives the later descent step.

For E/F5:y²=x³−x, the enumerated point count8 and Hasse coefficient3 show ordinary reduction but E[5](F5)=0. Hence the literal perfect-field rational-point formula cannot identify a rank-one tangent space; geometric points with descent are necessary.

The canceled universal degree-square claim fails for Frobenius on an ordinary elliptic curve (degree p), and the unrestricted positive-determinant assertion fails for−1 (degree 1, rank-one étale determinant −1). Neither counterexample affects the live positive Rosati-symmetric restriction. The canceled ring identity also fails since1/2∈Z3∩Q but1/2∉Z; interpolation at rational integers gives rational coefficients, which is all the live step needs.

For every p, every r≥2 and every t∈Fp, the block matrix diag([[t−(r−2),−1],[1,0]],I_(r−2)) has determinant1 and trace t. Thus all residues occur as traces even in SL_r(Fp). The script exhaustively checks small fields and ranks; the displayed formula proves the general case. Turning this into every-open point-count congruences still requires a suitable geometric monodromy and Frobenius-distribution statement.

Finally, a finite-dimensional semilinear module over a perfect field decomposes into its eventually stable image and its eventual kernel. The latter is nilpotent and the former has bijective Frobenius. Functoriality of this decomposition, or applying a sufficiently high Frobenius power to an exact sequence, proves exactness of the stable-part functor. It does not imply that the associated Fp Galois representation is semisimple.

## 4. Two further exact checks from the final reread

The margin at cote 9:13,line476 predicts Zp-valued traces conditionally onμp⊂K. This condition is unnecessary for the trace already defined on the Dieudonné module. Write its semilinear Frobenius asAσ and an inertia automorphism asB. Inertia acts trivially on the residue field and commutes with Frobenius, soBA=Aσ(B). After inverting p,A is invertible, givingtr(B)=σ(tr(B)). The trace was integral, andW(k)^σ=W(Fp)=Zp. The same conclusion holds additively for virtual classes whenever theK₀ construction is defined. This does not recover the trace from generic mod-p torsion.

For the coefficient functional in cote 9:5, write a Dieudonné element in normal formz=a0+Σ_(i≥1)a_iF^i+Σ_(j≥1)b_jV^j. Onlyb1 contributes toφ(Fz), givingpσ(b1), whereasφ(zF)=pb1. Likewiseφ(zV)=pa1 andφ(Vz)=pσ⁻¹(a1). This proves the two twisted identities. Left/rightW-linearity follows because multiplying a nonconstant normal monomial by a coefficient does not change its F/V exponent. Quotient maps preserving these normal-form coefficients give compatibility whenever the truncations are consistently indexed. FinallyF^iV^i=p^i, so its coefficient is notzero unlessp^i vanishes in the target. The separate script tests the genuinely nontrivial Frobenius involution onW2(F9), including every coefficient and all coefficient-pair products.

For the Serre-surface implication used inC070, assume precisely the source’s smooth projective free Z/p quotientS of a smooth connected complete intersection Y of dimension2 over an algebraically closed field. The π₁ Lefschetz theorem givesπ₁(Y)=1, henceπ₁(S)=Z/p and H¹_et(S,Fp)=Fp. Finite étale pullback is injective on rational crystalline cohomology because its trace composite is multiplication byp. The complete intersection hasH¹_cris(Y)[1/p]=0, soH¹_cris(S)[1/p]=0. Universal coefficients in degree0 showH¹_cris(S)[p]=0, sinceH⁰_cris(S)/p→H⁰_dR(S) is the identityk→k. ThusH¹_cris(S)=0. The degree 1 universal-coefficient sequence and stable augmentation identifyH²_cris(S)[p]_st with H¹(O_S)_st, whose dimension is1 by Artin–Schreier. This checks the cohomological implication, conditional on the stated Serre construction and the admitted integral section hypotheses; it does not verify a new geometric construction.
