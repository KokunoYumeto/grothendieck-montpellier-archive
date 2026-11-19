# Independent audit of C.3aq

**Verdict:** the entire typed all-positive-characteristic proof passed at **2026-11-19 10:06:45 UTC**. Parent also approved the complete result. This report is reconstructed following the 10:14 UTC scratch reset; it records an audit actually completed before the reset.

Owner: `agents/real_weil/C3_top_all_positive_characteristics_draft.tex`. Scope: an integral surjection from the top ordinary-algebraic-equivalence quotient of a regular punctured strict-local threefold to the additive ground field, in every positive characteristic. This extends the edge-characteristic coverage of C.3an. It does not give rational nonvanishing, a characteristic-zero example, or a general-dimensional statement.

## The relative K₂ map is only a quotient in characteristic two

For a split square-zero extension S=R⊕I, the relative Dennis–Stein presentation gives a natural surjection `K₂(S,I)→I⊗Ω¹_R/Z`. With the positive Steinberg convention it is `⟨m,r⟩↦−m d r̄`, `⟨r,m⟩↦+m d r̄`. All three placements of the infinitesimal entry in relation D3 reduce to the Leibniz rule. D2's correction vanishes because I²=0; D1 gives skew symmetry. Symbols with both entries in I map to zero. No assertion that they themselves vanish in characteristic two is used. No surjectivity of H² is inferred from the sheaf surjection. Actual curves prove surjectivity of the final invariant directly.

The map glues for the conormal line bundle L. Since k is perfect of characteristic p, absolute differentials agree with Ω¹_V/k. The sign is the negative of Weibel's Exercise5.14(a), and it gives `{1+tc,u}↦tc dlog u`. The characteristic-two case does not need van der Kallen's 1/2 hypothesis.

## Uniform geometry

The choices `e=p+1`, `n=p(p+1)`, `d=n−3` give d>0 for every prime. The plane curve `Yⁿ−YWⁿ⁻¹=Zⁿ⁻¹W` is smooth, with one point at infinity and `div(dz)=n(n−3)∞=p·ed∞`. For q=Y/Z and h=W/Z, the exact identity is `z−q⁻ⁿ=qⁿ⁽ⁿ⁻³⁾c`, with `c=q(h/qⁿ)ⁿ⁻²` a uniformizer. Thus the claimed order is accompanied by the required unit differential.

The inseparable curve in the ruled surface is `G∼pS∞−p g*D₁`, where D₁=ed∞ and the infinity section has positive normal bundle O(D₁). The degree-e cyclic cover branched in G+S∞ has inverse-root bundle `O(−S∞+pd g*∞)` and affine equation `Tᵖ⁺¹=sᵖ−z`. Valuation one at the branch proves connectedness even for composite e. Smoothness follows because the two branch components are smooth and disjoint and e is prime to p.

For the reduced section S, `S²=d`. The divisor `D=pS+d g*∞` satisfies `D²=((p+1)²−1)d`, `D·S=(p+1)d`, and `D·F=p`. The fibres are integral cusps with coprime exponents p and p+1; all horizontal curves have positive D-degree. This proves ampleness in every characteristic, including p=2 and p=3.

At base infinity, `s=qᵉᵈs_i+q⁻ᵉ` and `T=qᵖᵈT_i`; at S, with x=1/s_i and w=T_i/s_i, `wᵖ⁺¹=x−cxᵖ⁺¹` and `dT_i=−xᵖ dc/wᵖ`. The section order is p² and the base-infinity order is pd. The intersection calculation shows that `div(dT)=pD` exactly, so with L=pD there is the required nonzero η in Ω¹_V⊗L⁻¹.

## Actual branches and the global quotient

The displayed equations `s=0,T=at,z=−aᵖ⁺¹tᵖ⁺¹,yⁿ−y=zⁿ⁻¹` have derivative −1 in y at the selected point. The proof chooses the unique irreducible component through this smooth point. It never claims irreducibility of the entire displayed polynomial. The finite-normalization and henselian branch argument then produces an actual integral curve on the fixed strict-local resolution.

The rest of the global Chow/K₂ construction is precisely the separately proved integral comparison from C.3an. It uses the quotient map above in place of an isomorphism. The local residue is a, so every element of k occurs. Exceptional pushforwards have zero relative class. Ordinary CH²_alg is divisible by the actual-proper-curve-family argument, and the additive target has exponent p, so the invariant descends. All coefficient, sign, type, and characteristic-two issues in this replacement have been checked.

The owner's original finite certificate was read with its stated scope; the arbitrary-p formulas above, rather than finite testing, are the proof. The owner reconstructs and reruns that certificate with fresh timings after recovery.
