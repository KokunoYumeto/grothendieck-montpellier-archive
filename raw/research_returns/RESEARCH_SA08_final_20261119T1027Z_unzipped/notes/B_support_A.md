# Independent checks supporting Part A.1

GPT-6 Astra, automorphisms parallel agent, 19 November2026.

## Typed multiplicative comparison for root A-002

Let E^p_n=C^p_norm(Delta[n];Z), viewed as simplicial abelian group by restriction. The augmented complex Z→E^0→E^1→... is exact degreewise; each E^p is extendable and acyclic simplicially. Its normalized complex is a split acyclic complex of free abelian groups, so it admits a simplicial Z-linear contraction. Alexander–Whitney gives natural pairings E^p⊗E^q→E^{p+q}.

For a coefficient resolution K_i=F^i A, form the first-quadrant bicomplex D_i^{p,q}=Gamma_X(K_i^q⊗E^p). Its vertical augmentation is I_i⊗E^p→K_i⊗E^p. This is exact, since E^p is degreewise free; every term is simplicially acyclic, by tensoring with the contraction of E^p. Consequently Gamma_X preserves exactness, and the vertical comparison C^*(X;I_i)→Tot D_i is a quasi-isomorphism. (Gamma_X(I_i⊗E^p)=ordinary p-cochains with coefficients I_i.) The horizontal rows are acyclic resolutions of K_i^q. In total degree i, their higher derived groups vanish whenever q<i, by A-001. Thus the map Gamma_X K_i→Tot D_i induced by Z→E^0 is an isomorphism on H^i. Products K_i⊗K_j→K_{i+j} and AW on E make both comparisons multiplicative. This is an explicit choice-free zigzag adequate to prove the product formula in every degree.

## Arbitrary PD triple via derived tails

Set B=Gamma_Z(T). For any PD triple(S,J,t), B→S sends T^(n) to gamma_n(t). Let Z_B^i=ker(d:A_B^i→A_B^{i+1}). The objectwise relative Poincare contraction is B-linear, so the de Rham sequences are split exact B-modules in every simplicial degree. Hence Z_S^i=S⊗_B Z_B^i and A_S^q=S⊗_B A_B^q.

Normalization preserves tensoring here (it is given by a finite direct-summand projector in each degree). N Z_B^i is a nonnegative projective B-complex with its only homology I_i in degree i; N A_B^q is a nonnegative projective B-complex with its only homology Z=B/B+ in degree q. Therefore N Z_S^i represents S⊗^L_B I_i[i], with homological shifts.

For every X, the strict cochain quotient coker[Hom(X,A_S^{i−1})→Hom(X,Z_S^i)] equals coker[[X,A_S^{i−1}]→[X,Z_S^i]]. The reason is that A_S^{i−1}→Z_S^i is a degreewise-surjective simplicial module map, hence a Kan fibration. A nullhomotopic map X→Z_S^i lifts by homotopy lifting starting at zero; therefore passing to simplicial homotopy classes introduces no additional quotient. [X,V]=Hom_D(Z)(N Z[X],NV), since N Z[X] is a nonnegative free chain complex.

The triangle from 0→Z_S^{i−1}→A_S^{i−1}→Z_S^i→0 then identifies the quotient with the image of
Hom_D(Z)(C_*(X),S⊗^L_B I_i[i]) → Hom_D(Z)(C_*(X),S⊗^L_B I_{i−1}[i]).
The underlying coefficient arrow is I_i→I_{i−1}; identify this in the universal B-case by the connecting map and weight comparison. This gives the proposed complete arbitrary-triple formula rather than a mere bound.

## Nonsplit filtered completion: image of ordinary coefficient tails

Hypotheses: S has a complete separated nonnegative multiplicative divided-power filtration F, t∈F1, and a specified isomorphism gr_F S≅Gamma_k(T) carrying the initial form of t to T. Complete S{U}Λ(dU) in total filtration (coefficient filtration plus polynomial/exterior weight), so the associated graded simplicial DGA is exactly the universal weight model over k. Let Ahat denote that completed DGA.

1. The objectwise PD Poincare contraction h(U^(a)dU)=U^(a+1), tensorized in the U variables, preserves total filtration. Hence F^p Ahat is an exact resolution of the constant simplicial coefficient group F^p S.
2. For q<p, every finite quotient F^p Ahat^q/F^N Ahat^q has a finite filtration whose pieces are universal A_w^q with w≥p>q, all simplicially acyclic. Hence each finite quotient is acyclic. The inverse tower is degreewise surjective, so the inverse-limit/Milnor exact sequence makes F^p Ahat^q acyclic. It is therefore Gamma_X-acyclic for every X.
3. Consequently H^r Gamma_X(F^p Ahat)=H^r(X;F^pS) for r≤p, including r=p by dimension shifting.
4. For i≥1, Ahat and F^{i−1}Ahat agree in exterior degrees i−1,i,i+1, so H^i Gamma_X Ahat=H^i Gamma_X F^{i−1}Ahat.
5. Apply Gamma_X to 0→F^i Ahat→F^{i−1} Ahat→gr^{i−1} Ahat→0. This is termwise exact after Gamma_X: the quotient is zero for q≥i, while for q≤i−1 the kernel F^i Ahat^q is Gamma_X-acyclic. The last term has H^{i−1}=H^{i−1}(X;k) and H^i=0.
6. Its connecting map to H^i(X;F^i S) is the ordinary coefficient connecting map for 0→F^iS→F^{i−1}S→k→0, by naturality of resolution comparison. Thus
H_DR^i(X;Ahat) = image[H^i(X;F^iS)→H^i(X;F^{i−1}S)] for i≥1,
with H_DR^0=H^0(X;S).
7. Products are explicit: choose coefficient lifts alpha∈H^i(X;F^iS), beta∈H^j(X;F^jS); multiply into H^{i+j}(X;F^{i+j}S) and map to F^{i+j−1}S. If a lift changes by a class vanishing in H^i(X;F^{i−1}S), its product vanishes after projection by F^{i−1}S·F^jS⊂F^{i+j−1}S. Therefore the formula is independent of lifts. Multiplicativity follows using the E^p bicomplex comparison above; no scalar splitting of the filtration is used.

This formula contains any coefficient Bockstein obstruction exactly. For the split universal completion it reduces to the product of weightwise cohomologies. Without the gr hypothesis, step2 can fail, so this ordinary-tail formula is not claimed; the derived-tail formula remains available before completion, and completion must retain the relevant derived/inverse-limit data.

## Counterexample when the associated-graded hypothesis is omitted

Take the triple(S,J,t)=(F2,0,0), with trivial scalar filtration F1S=0, and X=Delta[2]/boundary. In cumulative coordinates U,V, the three edges impose U=0, V=0, U=V. The weight2 two-form dU dV vanishes on every edge and is closed. Every weight2 one-form has the unique shape a U dU+b V dU+c U dV+d V dV. Restriction to the three edges gives a=d=0 and b=c. Its derivative is(b+c)dU dV=0. Hence the displayed two-form is not a boundary. Higher or lower weights cannot affect this conclusion since d preserves weight, including after total-weight completion. Thus H_DR^2(X) is nonzero, while the proposed ordinary coefficient-tail image is zero for the trivial filtration. B_finite_checks.py verifies all16 candidates and the2 relative candidates. The derived-tail formula predicts this class: the indecomposable T^(2) survives the map F2 tensor_B I2→F2 tensor_B I1.

## Independent audit of root's strict binomial obstruction A.4

Assume a strict simplicial filtered DGA over Z, with degree-zero algebra Num(Z^(n+1)), its polynomial-degree filtration, a central relative coefficient algebra Num(T) with dT=0, F0 B1=0, and associated graded ΓΦ⊗ΛΨ with its PD differential. Products may be noncommutative. For linear integer-valued polynomials f,g, the commutator [df,g] has filtration≤1 because its filtration2 symbol vanishes in the commutative associated graded. F1 B1=Ψ, and changing f or g by a scalar or an integer multiple of T has no effect, since dT=0 and T is central. Thus b(df,dg)=[df,g] defines a simplicial Z-bilinear map Ψ⊗Ψ→Ψ.

In dimension1 put Ψ1=Ze and b1(e,e)=ce. In dimension2 choose Ψ2=Zu⊕Zv so the three faces are (u,v)↦(e,0),(0,e),(e,e). For b2(u,v), the first two faces force both coefficients to vanish. The third then says ce=0. Thus c=0. This already suffices; no assertion that a nullhomotopic map is zero is being made without examining degrees.

Differentiate 2 binom(f,2)=f²−f. The Leibniz rule yields 2(d binom(f,2)−f df)=b(df,df)−df. The term R=d binom(f,2)−f df belongs to F1 B1: its filtration2 symbol is dγ2(f)−f df=0. For a dimension1 f with df=e, the previous paragraph gives 2R=−e in Ψ1=Z, impossible. Equivalently modulo2 it would force b(e,e)=e, contradicting b1=0.

This validates the obstruction with its strict hypotheses. It does not exclude a filtered E∞ object, a homotopy Leibniz relation, noncentral relative coefficients, a different degree-zero algebra, or a different associated graded. The F1 assertion for R and the relative equation dT=0 are essential hypotheses to state explicitly.
