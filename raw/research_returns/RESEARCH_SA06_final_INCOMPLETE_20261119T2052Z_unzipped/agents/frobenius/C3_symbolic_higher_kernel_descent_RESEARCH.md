# Higher-kernel correction over k(u) by separable descent

**Auxiliary extension of HG: complete owner reconstruction and independent root/cycles mathematical audits passed; no main-gate movement.** GPT-6 Astra Pro (OpenAI), `/root/frobenius_continuation`, 19 November 2026. This repairs the coefficient-field scope needed before RF. The standard field-K3 input FK retains the exact source-audit qualification in HG.

## HD.1. The issue and the statement

Let k be algebraically closed of characteristic p>0, E/k the exceptional SNC surface of C.3bt, and F=k(u). Write J1(E_F/F) for actual endpoint differences on products with smooth geometrically connected proper F-curves having two F-rational points. Put r=(psi²−4)/4. The extension is

    r² ker(K1(E_F)_Q→direct sum_i K1((E_i)_F)_Q)
                   ⊂ J1(E_F/F).                        (HD.1)

The algebraically closed proof HG cannot be copied verbatim: its regular-curve localization terms over F have closed residue fields finite over F. The following argument reduces this issue using a finite separable extension only. It never asserts properness of Weil restriction for a purely inseparable extension.

## HD.2. Only the separable parts of finitely many fields need splitting

For a fixed kappa and the lift y used in HG, r y has finitely many point-supported edge K2 terms, with finite residue fields L_a/F. Choose a finite Galois extension F'/F containing the normal closures of their maximal separable subextensions. Every residue field of L_a tensor_F F' is then purely inseparable over F'. Since F'/F is separable this tensor algebra is a product of fields; no hidden nilpotent correction is required here.

If L/F' is finite purely inseparable of exponent at most e, Matsumoto's symbol presentation gives a direct rational surjectivity

    K2(F')_Q → K2(L)_Q.                                 (HD.2)

Indeed for a,b∈L*, their p^e powers lie in F' and

    p^(2e){a,b} = {a^(p^e),b^(p^e)}

is the restriction of a symbol from F'. This is an identity of ordinary K2 by Matsumoto and bilinearity. It requires no universal-homeomorphism theorem for arbitrary singular schemes and no inseparable extension of a proper parameter.

After this base change, each edge term is consequently a finite rational sum of constant F'-symbols times the point class. The perfect projection formula gives

    i_{a*} res_{L/F'}{b,c} = {b,c}[O_a]
                          = {b,c}([O_C(a)]−1).

The point may have degree p^e rather than1; its divisor degree is retained. The last equality follows from the Cartier sequence and triviality of a line on Spec L. Thus HG's degree-removal and Picard steps apply over F'. The degree-surjectivity matrix ET.9 is supplied by the original constant k-divisors, so it remains surjective after this base change.

## HD.3. Marked VE over an infinite extension field

The marked VE lemma works over each infinite field F' containing k, for the constant smooth edge curves with their rational basepoints and marks and for F'-defined degree-zero line bundles. Here are the needed geometric details, which should not be replaced by an assertion that all regular curves over an imperfect field are smooth.

The product of the relevant Jacobians is a smooth geometrically integral projective F'-variety with the rational points0 and the line-bundle tuple. Sufficiently ample complete intersections through those points, with prescribed independent first jets, give a smooth geometrically connected proper curve A/F'. The bad loci are proper Zariski closed after base change to an algebraic closure, and the defining conditions are over F'. Since F' is infinite, a nonempty open in the finite-dimensional affine coefficient space has an F'-point. Connectedness is geometric by the same duality/Serre argument as in VE.

Choose normalized rational sections of the marked evaluation line bundles using high twists. Their zeros and poles can be chosen finite etale over F', disjoint from a0,a1: on the smooth curve, first-jet generation makes the nontransverse-zero incidence proper, while two-point evaluation fixes the endpoint values. For a quotient of two such sections, also impose disjoint supports. The relative Picard bundles themselves and their endpoint fibres are the actual ones over F'.

Choose h with its only pole at a0, prescribed value (b−1)²/b at a1 for the required unit b, zeros at all those finite etale supports, and simple zeros there and elsewhere. If b=1 the desired family is zero. In odd characteristic also require transversality over the value−4. These are finitely many jet conditions plus avoidance of a proper bad incidence. If b=−1, the prescribed value at a1 is−4, and one prescribes a nonzero derivative there. One can ensure at least one geometrically simple zero by imposing a zero at a further finite separable point of A. Smooth curves over a field have such points, and the finite jet conditions descend over F'.

The cover (g−1)²=h g is geometrically integral and separable by the simple-zero discriminant/Artin–Schreier argument in VE. It is smooth after normalization: in odd characteristic the only branch values are0 and−4, now simple, and in characteristic two its finite branch zeros are simple. At the pole a0, clearing the denominator shows the two boundary points g=0 and g=infinity are themselves smooth rational points, because the coefficient of g (respectively g^−1) is a unit. Thus the resulting proper curve is smooth over F', not merely regular. A point over a1 with g=b is rational, also in the ramified case. The Dennis–Stein, marked divisor and sheaf-descent proof of VE now applies over F' unchanged. The marked divisor residue fields are retained in the pushforwards, but g=1 at them makes every marked restriction literally zero.

## HD.4. The proper K2 symbol construction over F'

The bq construction also gives actual proper symbol families over F'. For a,b≠1 set c=(a−1)²(b−1)²/(ab)≠0 and consider

    (f−1)²(g−1)² = c f g

in P1×P1. There is no vertical or horizontal component. The unique point over f=0 is (0,1), and it is smooth since the derivative in f there is−c. Over an algebraic closure, every component would dominate the f-line and hence contain that point. Smoothness there forces exactly one component. Thus the curve is geometrically integral.

All four boundary points are smooth by the analogous calculation. In characteristic two the interior derivatives are−c g and−c f, so the interior is smooth. In odd characteristic, an interior singular point must have f=g=−1, and occurs only if c=16. Its quadratic part is a nonzero scalar times x²+y², an ordinary node; the tangent branches split over k⊂F' (and in any event over a separable extension). Its normalization is therefore smooth over F'. If the prescribed point(a,b) is this singular point, the symbol{−1,−1} is2-torsion and hence zero rationally; use the zero family. Otherwise that point lifts to an F'-rational point of the normalization, as does the smooth point(0,1).

The same tame-residue and Dennis–Stein argument as bq gives an actual K2 class on this proper smooth curve with endpoint{a,b} and0. Units equal to1 give zero families separately. Thus the vertex Milnor-symbol correction in HG is available over F'. The field input FK is valid for general fields, and is used with its original explicit source qualification.

## HD.5. Separable norm preserves actual proper relations

Let L/F be finite separable and Q/L a smooth geometrically connected projective curve with L-points q0,q1. The Weil restriction T=Res_{L/F}Q is a smooth projective F-variety, geometrically a product of copies of Q, hence geometrically connected. Its two F-points t0,t1 correspond to q0,q1. Properness here uses that Spec L→Spec F is finite etale; the inseparable assertion would be false and is not used.

For xi∈K1(E_L×Q)_Q, pull back along the universal evaluation T_L→Q and push forward along the actual finite flat map E_L×T_L→E_F×T. This produces gamma∈K1(E_F×T)_Q. Finite flat perfect base change at t0,t1 gives

    gamma_t1−gamma_t0 = Tr_{L/F}(xi_q1−xi_q0).

When the endpoint difference is nonzero the two points are distinct. The same sufficiently ample geometric Bertini/connectedness argument gives a smooth geometrically connected proper F-curve P⊂T through t0,t1. Restriction of gamma to E_F×P realizes the traced endpoint as an actual proper relation over F. If T is already a curve, use T; if the endpoints coincide, the relation is zero. Thus

    Tr_{L/F} J1(E_L/L) ⊂ J1(E_F/F).                     (HD.3)

All pushforwards exist on perfect K-theory because the trace map is finite flat. The pull-push identity on constant classes is multiplication by [L:F], by the projection formula and the rank-[L:F] free module L over F. For this use no general commutation of Adams operations with a nontrivial-normal pushforward is needed: we apply the trace after the endpoint equality, and res commutes with r.

## HD.6. Run HG and descend

Apply the complete HG argument to res kappa over F', using HD.2 for its point-supported edge coefficients, HD.3 for marked VE, and HD.4 for the vertex symbols. This proves

    r² res kappa ∈ J1(E_F'/F').

Trace by HD.3. Since r commutes with restriction and the traced constant class is multiplied by [F':F], this gives [F':F]r² kappa∈J1(E_F/F). Rational division proves HD.1.

The original HK construction for a component tuple defined over k can be made directly over F=k(u): choose its supporting curves and Jacobian base A over k, choose h0 over k with h0(a1)=1 and the required marked simple zeros, and use h=((u−1)²/u)h0. Its two endpoints g=0 and g=u are F-rational. Hence HK supplies delta∈J1(E_F/F) with the desired component endpoint {u}beta. Applying HD.1 to delta−{u}beta exactly as in HG.8 yields

    {u}beta_F ∈ J1(E_F/F).                              (HD.4)

This is the literal exceptional endpoint required before RF. It still does not lift the whole family to the regular target: the surface-supported node vector or the finite-closure trace boundary remains unproved. No main-gate movement is asserted.

## Source and review boundaries

The whole argument reuses the fully audited ET.9, VE, bq, HG coherent diagrams, Matsumoto and perfect pushforward/base-change sources. Stacks Tag05Y8, already freshly read in the parameter-monodromy audit, supplies Weil-restriction representability and compatibility with base change; it does not contain a properness theorem. After finite Galois splitting the restriction is the product of the conjugate proper curves. Properness and smoothness descend fpqc (for properness see Stacks Tag02L1); projectivity is supplied by descent of the symmetric tensor product of conjugate ample line bundles, not by an unrestricted assertion that projectivity descends. The infinite-field first-jet conditions and the bq geometric singularities are proved above; they do not infer smoothness from regularity over an imperfect field. The full foundational field-K3/Adams comparison remains the standard FK input with the source-read scope recorded in HG. The owner reconstructed the full proof; root and cycles subsequently read the entire argument and independently passed its mathematics. The cycles receipt is `agents/cycles/C3_symbolic_higher_kernel_descent_independent_REVIEW.md` (initial completion20:38:55.633094UTC). The final ledger correction above changes source attribution only; this status update records the completed audits. These passes retain the stated FK foundational source qualification and make no main-gate movement claim.
