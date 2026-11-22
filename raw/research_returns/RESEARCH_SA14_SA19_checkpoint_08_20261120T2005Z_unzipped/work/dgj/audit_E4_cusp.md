# Independent targeted audit: BCE's cuspidal cubic quotient

**Verdict: PASS for the stated reduced, geometrically integral family.** This audit does not claim geometrically normal or smooth special fibres.

Let k be algebraically closed of characteristic 2 and R=k[[t]]. Let C/R be the plane cubic

    y^2 z + t x y z + t y z^2 = x^3,

with section infinity=(0:1:0). Its Weierstrass coefficients are a1=a3=t and a2=a4=a6=0. Thus b2=b4=b6=t^2, b8=0, and the discriminant is t^4(1+t^2); the generic j-invariant is t^8/(1+t^2). The generic fibre is therefore smooth and ordinary. The special cubic y^2z=x^3 is integral and cuspidal. Infinity remains smooth since the derivative with respect to z equals 1 there. The morphism g(x:y:z)=(x:y+t x+t z:z) is the Weierstrass inverse, preserves the equation, has square one, and fixes infinity.

Let B be the constant ordinary elliptic curve y^2+xy=x^3+1, with nonzero point P=(0,1) of order 2, and write Y=B/<P>. The constant group Gamma=Z/2 acts on C times B by (g, translation by P). It acts freely because its nontrivial element is fixed-point-free on B after every base change. The quotient X exists as a projective R-scheme and the covering C times B to X is a finite etale torsor. The fibres of X are geometrically integral; its special fibre is C_0 times Y and is nonnormal.

## Why the relative Pic-tau product formula applies

Write G=Pic^0(C/R). For this genus-one curve family, G is a smooth separated group scheme of relative dimension one. Its generic fibre is an elliptic curve and its special fibre is G_a. The degree map on curve Picard groups has torsion-free target Z, so Pic-tau(C/R)=G.

The automorphism induced by g on G is [-1]. It is [-1] on the smooth generic elliptic fibre; equality extends over R because G is flat and the target is separated. In particular its fixed subgroup is exactly G[2], as a group scheme and after arbitrary base change.

The key descent argument from D0 uses a pointed proper family with universally trivial global functions; it does not require C itself to be an abelian scheme. Here H^0(C_T,O)=H^0(T,O) for every T, since C is proper flat with geometrically integral fibres. A class in G[2](T), regarded fppf locally as a line bundle, can be rigidified along infinity. An isomorphism g*L to L is then uniquely normalized to be the identity on that rigidification. Its square is an automorphism of L whose restriction at infinity is one, and hence is one everywhere. This gives a canonical Gamma-linearization. Rigidified descent also glues the local representatives, so this works on arbitrary test schemes, not merely R-points.

Combining this with the Pic-tau product formula for C times B, already proved in BCE's work, gives

    Pic-tau(X/R) = Y^vee times G[2].

The Y^vee factor accounts for the line bundles from the translated B factor, including the character ambiguity in a linearization. The split section of X to Y induced by infinity identifies that factor. Conversely a canonically linearized member of G[2] descends to a numerically trivial line bundle: pullback under the finite covering is numerically trivial, and degrees on curves show that numerical triviality descends under a finite surjection. Thus no step silently replaces Pic-tau by the whole Picard functor.

## The two fibres

Over an algebraic closure of the generic field, G[2] is mu_2 times Z/2 and is not smooth. At the special point, G=G_a and multiplication by 2 is zero, so G[2]=G_a is smooth. Therefore Pic-tau has nonsmooth generic fibre of dimension one and smooth special fibre of dimension two. The set of base points at which the fibre of Pic-tau is smooth is the closed point alone, and is not open.

This is a counterexample for the reading of 57:309(b') asking whether fibrewise smoothness of Pic-tau has open locus, without a normality assumption on the fibres of X. It does not refute the different statement that the smooth locus of the morphism Pic-tau to Spec R is open; the latter is always open, and the morphism here is not flat at the special fibre.

The discriminant, inversion, and cusp computations should be included in BCE's saved finite certificate. No numerical computation is used in this proof audit beyond the displayed exact identities.
