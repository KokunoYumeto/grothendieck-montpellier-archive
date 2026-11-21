# Independent full review of F44

Reviewer: /root/gct_statements, GPT-6 Astra Pro; inherited effort not exposed. Date: 21 November 2026 UTC.

Reviewed in full: agent_relative_auslander_repair.md, SHA-256 5169cb379db254cf70303d6cc3e81d459f2a541ce34da9b9bbefdcd0d8a7cf64.

**Result: PASS. No mathematical blocker.** Verification types: full proof reading and independent reconstruction of all algebraic maps, exactness arguments, action comparisons, Ext groups and Frobenius assertions. The previously checked F19/F21 presentation and F40 motivic source application are stated inputs. No formal proof kernel, new numerical experiment, or newly executed symbolic script is claimed.

## 1. Actual algebra and relative diagonal

The map a sends 1 to x-Delta and b evaluates at zero, so ba=-Delta e2 and ab is multiplication by x-Delta on C. Writing a C element as u+vx gives ann(x)=R(x-Delta) directly. Thus the four Hom spaces have ranks 2,1,1,1 and the displayed five basis elements give the actual End algebra. The corner coordinate x=c+Delta and the actual source coordinate z=z2-c are correct. They implement x=z1-z, so L1 retains multiplicity16 and L2 multiplicity4. The sign of c at the closed fiber differs from the earlier F40 choice; the report states this and transports the named generators explicitly.

I checked the complete relative diagonal resolution. Both terms of d1 land in the appropriate vertex summands, and d1d2 vanishes because the central scalar -Delta cancels between the two tensor factors. The eight d1-image vectors in (R6) are correct, including all four added Delta terms. Their indicated pivot minor has unit determinant: the new entries occur above the relevant diagonal blocks and do not change the product 1,-1,-1,1,1,1,1,1. Hence their span has a free complement of rank five. The induced surjection from that free quotient to Gamma is an isomorphism, proving exactness at Q0 without an unproved rank or fiber argument.

The a-component of d2 maps the basis e2,a to b,c, so it has a coordinate left inverse and a free complement. The quotient Q1/im(d2) is free rank eight; its surjection to the already established free rank-eight image of d1 is an isomorphism. Thus the entire finite relative bimodule resolution is exact over the base ring. Each summand is a finite projective enveloping-algebra module. Relative properness follows from the free rank-five underlying R-module.

The global-dimension bound over a DVR is also valid for arbitrary modules. The bounded diagonal resolution is split exact as a resolution of the left-projective module Gamma by left-projective modules. Tensoring with any right N remains exact. Its terms are sums of Ne_i tensor_R e_jGamma; each has projective dimension at most one over Gamma because every R-module has projective dimension at most one and e_jGamma is R-free. A length-two resolution by such terms gives projective dimension at most three. No sharpness claim is made.

## 2. Exact actual tensor-lattice lift

The map a:P2 to P1 remains injective with image Ra+Rc, so S is R-free rank one and perfect of projective dimension at most one. The corners are P2e1=Rb=L1 because bx=bc+Delta b=0, and Se1=L2 because c acts by zero and x acts by Delta. This identifies the two branches through the collision rather than only generically.

Under matrix Morita equivalence, the row P2 module has R-rank four and the row S module rank two. Therefore the stated lift has rank24+16*4+4*2=96. Its corner has rank24+16*2+4*2=64 and the actual prescribed multiplicities. Evaluation at f identifies Hom(fLambda,Mtilde) with Mtilde f; for right modules, precomposition by left multiplication gives the original right corner action, with no opposite-algebra reversal. This recovers the actual specified algebra and tensor lattice. The distinction from F40's different rank104 projective lift is correct.

## 3. Derived Hom, relative exceptional pair, and the corner

Applying Hom(-,P2) to the two-term resolution gives Rb to Re2 by multiplication by -Delta. Over the stated domain its kernel is zero and its cokernel is R/Delta. Thus Ext1(S,P2)=R/Delta, in the stated orientation. Hom(P2,S)=0 and all its higher Ext vanish by projectivity; both self-Ext groups vanish. Matrix Morita equivalence introduces no extra factor of two. Exactly4*16 oriented pairs contribute, giving (R/Delta)^64, length64m when ord(Delta)=m. The original corner had both orientations, so its Ext1 multiplicity128 is deliberately not claimed preserved.

The two self-Hom complexes of S,P2 equal R and the reverse Hom vanishes. The resolution recovers P1, so the relative exceptional pair generates. Perfect Gamma objects have perfect R-Hom complexes because Gamma is R-proper; the stated adjoints of the single-object functors therefore exist. This verifies the relative semiorthogonal decomposition. Its finite-field fibers give the already checked two-point/four-point motive calculation; no finite-field claim about an arbitrary fraction field is made.

The perfect corner functor is fully faithful by its unit. For nonunit Delta, the alternating x,x-Delta resolution of L1 gives Tor_(2j+1)(L1,L1)=R/Delta for every j>=0, so L1 is not perfect. The same representing-object argument as F40 excludes a right adjoint on perfect categories. When Delta is inverted, ba=-Delta e2 makes e1 full, and the corner is a Morita equivalence. These assertions are correctly separated.

## 4. Frobenius lift and the two unit conditions

In characteristic p>3, fixing the vertices and sending a to a, b to Delta^(p-1)b preserves ba=-Delta e2 after Frobenius on R. Hence it is a ring endomorphism. It is not elementwise noncommutative pth power: it fixes the nonzero square-zero arrow a.

Since c^2=-Delta c and p is odd, c^p=Delta^(p-1)c. Also x^p=Delta^(p-1)x. Thus the corner map is precisely scheme Frobenius, including z=z2-c. The entrywise extension to the matrix algebra is a genuine ring map.

The fixed vertex projectives have unit extension-of-scalars pullback structures. The differential in S's projective resolution is a and stays a under this lift, proving unit derived pullback for S with no extra cohomology. All objects in the stated lift therefore have unit pullback structures over the larger algebra.

This does not give unit R-linearization. On the P2 basis(e2,b), the associated semilinear map has linearization diag(1,Delta^(p-1)). There are32 copies of b in the16 row P2 copies, giving exactly Delta^(32(p-1)) on the rank96 lift and on its rank64 recovered corner. A different pullback isomorphism composes with an automorphism whose underlying R-determinant is a unit, so it cannot remove this defect.

For every semilinear ring map fixing the vertices, the rank-one arrow spaces force a to ua and b to vb. The relation and nonzerodivisor Delta give uv=Delta^(p-1), and this condition is conversely sufficient. Pulling back S replaces its resolution map by ua; it remains injective and its cokernel as an R-module is R plus two copies of R/u. Thus S has unit algebra pullback exactly when u is a unit. P2 always has unit algebra pullback, but its underlying R-linearization is diag(1,v) up to units and is invertible exactly when v is a unit. At nonunit Delta these cannot both hold. The argument for the direct sum Mtilde correctly uses actual torsion when u is nonunit and determinant defect when u is a unit.

## 5. Scope clarification recommended

The report's no-go is already correctly scoped to this fixed-vertex family of lifts and this chosen relative smooth model. For reader clarity I recommended an additional sentence: F36 independently constructs an R-unit semilinear structure on the original corner module for its intrinsic center Frobenius. F44 shows that such a base-unit structure cannot be induced from unit pullback structures on this chosen larger lift. It does not negate the F36 construction. This is a clarification of scope, not a mathematical correction.

As an optional separate deduction, the faithful corner projective itself has underlying semilinear matrix diag(1,u,uv) on each P1 copy, hence determinant u*Delta^(p-1). The four P1 entries in fLambda contribute u^4 Delta^(4(p-1)). This is also nonunit through collision. It reinforces the distinction between an algebra-level pullback isomorphism and a unit structure after forgetting to R; it was not needed in the reviewed proof.

## 6. Final assessment

All elementary claims (R1)--(R21) pass independent reconstruction. The result strictly improves the special-fiber repair: it retains the actual relative algebra and module, records collision order in an actual coherent Ext group, and supplies an explicit noncommutative Frobenius lift with a precise additional comparison obstruction. The report does not equate that Frobenius with cyclotomic TP, preserve both original Ext orientations, or infer a canonical basis or main path-sign comparison.

A generated final fragment and any added scope sentence should receive a separate text match with its own hash.

## 7. Complete final-fragment match

I subsequently read the entire generated finding_F44.tex directly, SHA-256 31135b18f70fe3ee598be5c4fa33397a3fc584797e5ce043ccb891415522ac70. **Final-text match: PASS.** Every relative diagonal, actual action, Ext, exceptional-pair, nonadmissibility and Frobenius argument is retained. The theorem and concluding scope paragraph now explicitly preserve the independent F36 R-unit structure while restricting the new no-go to unit structures induced through this chosen smooth lift. This is the recommended clarification and resolves the possible apparent contradiction. The separate dictionary uses previously verified Stacks/SGA/archive framework inputs; those locators were not re-audited in this final mathematical match. No stronger mathematical claim or blocker was introduced.
