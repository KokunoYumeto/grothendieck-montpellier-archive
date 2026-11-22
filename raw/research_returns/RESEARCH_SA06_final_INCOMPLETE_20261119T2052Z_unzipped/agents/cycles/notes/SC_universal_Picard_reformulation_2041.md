# Universal Picard form of the fixed-presentation tensor condition

**Proved reformulation of SC for fixed supporting curves. Unregistered auxiliary; no new main movement. The actual HK support-node comparison remains unfinished.**

Author: GPT-6 Astra Pro (OpenAI), `/root/cycles_continuation`, RESEARCH_SA06; reasoning effort not separately exposed.

## UP.1. Universal data

Fix the HK supporting curves A_i in the components, and let B be the product of their Jacobians. Write b in B(k) for the chosen tuple of degree-zero line bundles representing the component cycles. Each marked evaluation comes from an actual normalized Poincare line bundle N_q^univ in Pic0(B), and the vectors w_q in the finite-dimensional rational space W are those of SC.1, including their incidence signs and canonical supported lifts.

Choose a rational basis w_1,...,w_r of W and write w_q=sum_j c_jq w_j. Define

    ell_j=sum_q c_jq [N_q^univ] in Pic0(B)_Q.

After one common multiplier these are represented by actual line bundles. For any pointed smooth proper curve f:(A,a0)→(B,0), the SC tensor is

    Omega_f=sum_j w_j tensor f*ell_j.

Consequently Omega_f=0 if and only if f*ell_j=0 in Pic0(A)_Q for every j. The construction is independent of the basis of W. This is a statement about the abstract Picard tensor, not its exterior-product image in a cycle group.

## UP.2. The maximal compatible abelian subvariety

There is a unique largest abelian subvariety H⊂B with

    ell_j|H=0 in Pic0(H)_Q for every j.                  (UP.1)

To prove this, if H1 and H2 satisfy (UP.1), the addition map H1×H2→H1+H2 pulls a Pic0 line bundle back to the exterior tensor product of its two restrictions. This follows from translation invariance and seesaw. Hence every ell_j pulls back to zero rationally.

Pullback of Picard groups along a surjective morphism of projective varieties is rationally injective in the case at hand. Indeed choose a proper generically finite multisection of its source by sufficiently ample hyperplane sections, of degree d over the smooth target. Restricting a trivial pulled-back line bundle to that multisection and applying divisor push-pull gives d c1(L)=0 in CH^1(target)=Pic(target). The same argument applies after clearing denominators. Thus ell_j restricts to zero rationally on H1+H2. Taking a compatible H of maximal possible dimension and adding any other compatible abelian subvariety proves existence, maximality and uniqueness. No infinite algebraic union is used.

The condition means torsion for actual line-bundle representatives. It is not literal triviality before denominator clearing.

## UP.3. Curve criterion

Let f:(A,a0)→(B,0) be a pointed smooth connected proper curve. The pointed map factors through the Abel–Jacobi morphism A→Jac(A) and a homomorphism Phi:Jac(A)→B. Let H_f be the image abelian subvariety. Pullback Pic0(Jac(A))→Pic0(A) is the usual Jacobian duality isomorphism. Pullback along the surjective map Jac(A)→H_f is rationally injective by the multisection argument above. It follows that

    Omega_f=0  if and only if  H_f⊂H.                  (UP.2)

In particular the existence of a curve of this type through the literal points0 and b with Omega_f=0 is equivalent to b∈H(k). For sufficiency, if H has dimension one use H; if it has larger dimension take sufficiently ample smooth geometrically connected complete intersections through0 and b, with independent prescribed jets. The existing VE Bertini argument supplies such a curve. If b=0 a constant map from a smooth proper curve suffices.

Allowing one common multiplier of the original endpoint data, the exact criterion becomes

    b tensor1 ∈ image(H(k)_Q→B(k)_Q).                  (UP.3)

Indeed this says precisely that some positive multiple of b lies in H(k): take the quotient abelian variety B/H and use exactness of tensoring the groups of algebraically closed-field points with Q. One then applies the literal criterion to that multiple. Conversely a curve through0 and mb with zero tensor places mb in H(k), proving (UP.3).

All actual line-bundle powers, principal-divisor torsion multipliers and normalized rational sections needed after this choice are handled by SC.3. Thus this formulation does not replace an actual family by a fractional Picard point.

## UP.4. Exact remaining scope

For fixed supporting curves this describes which endpoint tuples can satisfy the displayed Omega condition after an appropriate proper parameter choice. Component Albanese-kernel membership instead constrains the image of b under B→product_i Alb(E_i). No inclusion of the connected kernel of that map in H has been proved. There is also no proof that changing supporting curves or changing b by the kernel of its pushforward to CH0(E_i) always yields (UP.3).

Most importantly, even when this criterion gives Omega_f=0, the complete comparison with every actual supported HK node class remains unfinished, exactly as in SC.6. Conversely, failure of (UP.3) for one fixed presentation is not nonvanishing of an ordinary class in UK.7. This is a reformulation of a method-specific condition and is not an E-specific counterexample or a new computation of the main quotient.

## Inputs and source scope

The complete argument is given above, using the already audited Poincare/Jacobian duality, translation/seesaw, divisor projection formula and VE smooth-curve construction. Relevant primary sources are Milne, J. S. (1986), *Abelian varieties*, in *Arithmetic Geometry*, 103–150, and the exact Poincare/Albanese and Bertini sources recorded in VE and the preceding SC/SL audits. No fresh full rereading of all those external foundations is claimed in this short reformulation. The rational-injectivity assertion used above is proved by an explicit multisection and divisor push-pull, rather than an unstated injectivity of an abstract tensor into Chow.

Saved: 2026-11-19T20:41:45.239999+00:00
