# Independent whole-proof review: F59 altered scalar coefficient

Reviewer: /root/rectangular_and_theta  
Date: 2026-11-21 UTC

## Verdict and exact target

**PASS. No mathematical correction required.**

Report: agent_soergel_scalar_complex_gate.md  
SHA256 f0805ab3ae6735815c3acd08b4b42272e6d53a1308cdabb0d2016734278ceafb

I read the entire 243-line report and independently reconstructed every argument, including the canonical Kunneth step SC11. No computation is needed for the proof, and no generic internal grading is silently retained.

## 1. Exact premise

C is a bounded complex of finite internally graded scalar k-spaces. Its differentials are scalar; this excludes arbitrary unit-bimodule complexes with nonconstant polynomial differentials. The comparison is an actual derived isomorphism, with any stronger homotopy realization covered by implication. The conclusion does not claim an unconditional no-go for all nonflat cohomology.

The actual Euler class sends, under ordinary ungraded graph localization, to 2(e+tau). Its scalar coefficient has Euler dimension four. These are precisely the two Euler values needed later.

## 2. Generic positive cohomology and the subgroup argument

The localized graph category is semisimple after forgetting internal shifts. Its actual cohomology multiplicities are Laurent polynomials f_g(u) with nonnegative integer coefficients. Kunneth gives F^2=dF.

Augmentation a of F satisfies a^2=da. It is nonzero, as seen at u=-1, so a=d in the integral Laurent domain. For every positive real u, division by d(u)>0 gives an idempotent probability measure. Its support is independent of u because every nonzero nonnegative Laurent polynomial is positive on that axis.

I checked the complete finite-group argument. Positivity makes support squared equal support; a finite nonempty subsemigroup in a group is a subgroup. At a maximal coefficient, the convolution equality is a weighted average with strictly positive weights. Equality forces every term to have that same maximum, hence the measure is uniform on the subgroup.

The resulting coefficient equalities hold for every positive real u and therefore as Laurent polynomial identities. Euler evaluation at -1 gives 4/|S|=2 at the identity, hence |S|=2 and the other element is tau. Thus F=d(e+tau)/2 and the ungraded cohomological coefficients of d are even.

The warning after SC-A is essential and correct: a homogeneous degree-two unit after generic localization identifies even internal shifts. The above statement is not a two-variable coefficientwise parity result. The report explicitly avoids the tempting but invalid immediate contradiction from the v^2 and v^-2 coefficients.

## 3. Global cohomology flatness and graph splitting

Finite graded flat cohomology modules over the noetherian polynomial ring are finite graded projective. A homogeneous residue basis gives a graded-free surjection; projectivity splits it, and graded Nakayama kills the complementary kernel. Thus they are graded free.

The actual generic support e,tau yields yU=xV and U^2=x^2 I for the right actions of the two independent anti-invariant root coordinates. Left freeness extends these identities globally. Coprimality gives U=xZ, V=yZ, Z^2=I. Fixed coordinates act by the left scalar. The idempotents (I±Z)/2 split each cohomology module into genuine graded free graph summands, and therefore also prove right freeness.

This is the point at which the full global internal grading is recovered. The multiplicities a(v,u),b(v,u) record actual globally free cohomology graph summands. They are not localized shift multiplicities. The tau term b is nonzero, because its Euler multiplicity is two.

## 4. Canonical Kunneth SC11

SC11 is valid with the stated one-sided splitting argument.

A bounded complex of finite right-free modules whose cohomology is right-projective splits, as a right-module complex, into its cohomology and contractible pairs. One can prove this by starting from the top degree: the top cohomology quotient splits, its boundaries become projective, and induction splits the next cycles and boundaries.

Tensoring this right-module homotopy decomposition with the second complex computes the underlying tensor cohomology. Right flatness of each cohomology summand then identifies it with the direct sum of H^i(X) tensor_A H^j(X).

The map that is proved bijective is the canonical cross-product map on cycle classes, rather than a noncanonical asserted bimodule splitting. That cross-product map is intrinsically bimodule-linear and internally graded. Its bijectivity as an underlying map therefore proves the claimed graded bimodule isomorphism. No one-sided contracting homotopy is treated as a bimodule map.

The scalar Kunneth statement for C is immediate over k. Comparing the two graph multiplicities gives a^2+b^2=da and 2ab=db. Maps between the distinct graph types vanish because their scalar is annihilated by 2x in the polynomial domain. Since b is nonzero, d=2a in the two-variable Laurent domain. Euler specialization u=-1 gives delta^2=2a(v,-1), impossible because the two outer coefficients of delta^2 are odd. The right side may have signed coefficients after Euler specialization, but they are still even integers; no effectivity assumption after Euler specialization is needed.

## 5. Both concrete candidates

For the coupled Rouquier lift, the derived object is a degree-zero bifree module. Its square is degree zero. Nonzero scalar cohomology in any other degree on the right would remain nonzero after tensoring with that module, so C must be degree zero. Its Euler class then fixes the original scalar coefficient. The identity-graph square coefficient v^4+6+v^-4 differs from 2v^2+4+2v^-2, as stated.

For the unit-dot cone, the generic cohomological character is
(1+z^2)e+(1+z)(s_1+s_2)+2tau.
I independently expanded it from the two summands of the cone. Its three character values on the Klein four group are z^2+2z+5, z^2-1, and (z-1)^2. All are nonzero and distinct in the Laurent domain. The relation f^2=df would make each equal d, an immediate contradiction. This calculation has no hidden internal grading.

## 6. Central finite-Frobenius fiber and exact residual case

For an originally homotopy-level relation, the central quotient preserves the actual relation, as in the already checked strongest F59 proof. The report does not casually assert that an arbitrary quotient functor preserves all derived isomorphisms.

The reduced complex is derived-nonzero by its Euler k-dimension. Local nonvanishing of top-module tensor products gives top degree 2r on its square. Scalar Kunneth gives a+r on the other side, so r=a. The exact Frobenius dual reverses both complexes and gives the corresponding equality of bottom degrees.

Thus the altered coefficient aligns the extremes; it does not force them to zero. The old minimal-complex argument cannot be reused without concentrated projective fiber cohomology. The report correctly isolates nonflat cohomology as the remaining necessary condition and does not claim a construction or complete exclusion of that remaining case.

## 7. Source and dictionary scope

The ordinary Hecke/localized graph background is the same original source whose full contexts were read in the F59 core review. The new subgroup argument and Kunneth proof are fully included; neither is attributed as a new archival theorem.

The separate dictionary distinguishes scalar perfect coefficient complexes, effective cohomology multiplicities, global graded free summands, and virtual Euler classes. It does not assert a lambda-ring structure on the noncommutative Hecke algebra or confuse the finite Frobenius algebra with an arithmetic Frobenius operator.

Final fragment review remains separate if a LaTeX continuation is generated.

## 8. Complete final-fragment match

I read all 312 lines of finding_F59_scalar_complex.tex and matched the complete arguments and separate dictionary against the checked report.

Fragment SHA256:
d2582ec9bd1d71877eb2bb0546abc380a71e257aa686e125164556ec6eb68fa7

**Final-fragment PASS.** The positive generic-measure proof, explicit localization grading warning, global graph splitting, canonical bimodule-linear Kunneth map, Euler parity contradiction and both concrete candidate tests are retained. The finite quotient paragraph explicitly requires the homotopy isomorphism for that termwise quotient argument and does not claim that ordinary quotient preserves arbitrary derived isomorphisms. Its residual-case and dictionary scope match the report. No new mathematical issue was introduced.


