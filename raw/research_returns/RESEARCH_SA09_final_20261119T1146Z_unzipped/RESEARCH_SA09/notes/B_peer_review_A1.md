# Independent targeted review of A1.4 and A1.7

Reviewer: GPT-6 Astra (OpenAI; ChatGPT Pro mode), run `/root/b1_b2_b3`; effort inherited and not separately exposed. Date: 2026-11-19. Reviewed the then-current `sections/A1.tex` and exact original `MPL_137_045-086_transcription.tex`, scans 75--86.

## A1.4: arbitrary-module Hom polynomial law

The explicit formula is valid without projectivity or any Hom base-change isomorphism. The tensor-presentation relations are exhaustively of the following kinds: permutation/insertion of zero summands; additivity in the Hom element; additivity in the coefficient; scalar balance. The divided-power sum identity proves the second, the identity mu_(a,b) Delta_(a,b) = binomial(a+b,a) id proves the third, and Gamma^a(lambda f)=lambda^a Gamma^a(f) proves scalar balance. Empty presentations at p=0 give the identity of the unit, and at p>0 give zero. The comparison into Hom maps after polynomial scalar extension is injective because coefficients can be read separately even for an arbitrary source module. Thus the composition verification does not smuggle in Hom base change. No gap found.

## A1.7: bounds, constants, and composition

The finite co-Kleisli construction is valid. Write epsilon_X:B_1X -> X for the projection. The exact counit identities are

- epsilon_(B_mX) D_(1,m) = id_(B_mX), for m>=0;
- B_d(epsilon_X) D_(d,1) = id_(B_dX), for d>=0.

There is no epsilon:B_0X -> X; the pro notation must not be read that way. Both typed counits follow from the stated degree-one maps and the zero-on-positive-degree behavior of G applied to the zero map. The degree bound dm is correct including d=0 or m=0: all composites are constant in those cases. Projection compatibility follows by the weight inequality sum i nu_i <= dm after the discarded components have been killed. Naturality and the three-bound equation give associativity by the standard finite co-Kleisli calculation; no infinite object is needed.

## Gap found in the first strictness proof and exact repair

The first text claimed that substituting universal maps in disjoint variables uses only alpha_(1,p). This is immediately true when their positive degrees are distinct, but repeated inner degrees p instead use alpha_(q,p). A proof that the chosen exponential comparison is recovered was missing at that point.

The robust explicit normalization is an equality of whole maps. For q>=1, p>=0, X=direct_sum_i X_i and u:G^pX -> direct_sum_i G^pX_i the tuple of pure-component projections, require

pr_(1,...,1) G^q(u) alpha_(q,p)^X = pr_(p,...,p)

as maps G^(pq)X -> tensor_i G^pX_i. This is stronger and safer to state than restricting the source to its (p,...,p) summand: the whole-map equation requires zero on every other multidegree, essential over torsion rings where scalar characters need not separate weights. For p=0, u is the diagonal from the unit to q copies of the unit. The equation is then exactly the constant normalization.

This equation is necessary for the chosen strict representability data. Together with the bounded coassociativity/counit diagrams it is sufficient: group inner components by their common degree p, use the equation for each group, and use the exponential comultiplication to separate the distinct groups. This proves both the intended multidegree and the identity representing map, with all unintended source multidegrees zero. Tensor strictness itself uses only alpha_(1,2) and alpha_(n,1), so follows directly. The resulting criterion is exact without claiming that its axioms are minimal. The root incorporated this full-map normalization and an explicit finite multigrading condition on D into the final criterion. We reread the revised A1.7: its grouped repeated-degree proof now proves the identity and the off-diagonal vanishing; all types, degree-zero cases, and bounds are correct. No substantive gap remains in that revised criterion.

## Optional redundancy argument sent to root

A possible stronger result is that the normalization already follows from the bounded diagrams and unit variables. To handle repeated degrees, tensor each universal map e_p(X_i) with enough independent variables in the tensor unit to make the total degrees distinct. Each padded factor can be computed using only alpha_(1,p) and alpha_(r,1); its product with the others uses only alpha_(1,d_i). Substitute the dummy variables to the universal constant 1 one at a time, so each substitution uses alpha_(1,0) rather than an unproved higher constant normalization. Associativity then identifies the canonical resulting whole map with the original repeated-degree composite. This argument was not required for the safe explicit criterion, and no minimality claim depends on it.

## Evidence scope

This was a proof/type audit, not a new finite counterexample or a numerical experiment. No finite evidence was used to justify the all-degree assertions. No external source beyond the manuscript was needed for the elementary audit; the primary references already opened by the root support A1.4's divided-power identities.

## Final revised-version check

The added D target expansion is indexed by inner multidegrees beta with |beta|<=m and outer exponents nu_beta with sum nu_beta<=d. Its weight w_j=sum_beta nu_beta beta_j is the correct one. Necessity follows by first separating the variables in the degree axiom and then applying the linear diagonal, whose represented G-map is Delta. The p=0 and q=0 cases of normalization N use only the specified unit comparisons and are well typed. The final revised theorem passed this independent targeted proof audit.
