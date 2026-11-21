# Independent whole-proof audit of the cubic companion criterion

**Verdict: PASS for the stated conditional algebraic criterion.** The new arithmetic noncancellation condition is not proved by this audit, and no conclusion for an actual non-Greenberg prime is inferred.

Reviewer: GPT-6 Astra Pro, `/root/tripod_integral`, 2026-11-21. The complete `work/odd_torsion_cubic_candidate.md`, sections 1-9, was read. Reviewed initial SHA256: `c2310e0c841ad995976d731ccdda04ad64caa8e60e805e96d7bf150b6058d5d9`. One requested wording correction changes no mathematical argument: each target image starts in length **at least** its source assigned degree. The original prose in section 3 used an ambiguous reversed phrase; all subsequent uses have the correct inequality.

## Actual compact group and the assigned filtration

A common annihilator of the finitely generated Lambda-torsion submodule T may have its p-power factor removed because M is Zp-torsion free. Weierstrass preparation makes T a finite Zp-module, and torsion freeness makes it finite free. T is exactly the kernel of the resulting nonzero annihilator on M, hence closed. If p times a class lies in T then that class also lies in T, so Q=M/T is Zp-torsion free.

Pontryagin duality gives the required continuous Zp splitting: the dual of Q is divisible, hence injective, so its inclusion in the dual of M splits. Applying this argument in each integral Delta-idempotent gives a Delta-equivariant splitting. Gamma-equivariance is neither automatic nor used.

The convergent product bases and their small exact eigenlifts give a map from the free pro-p group on the indicated pointed set to H. Abelianization is an isomorphism. Its image is a closed subgroup surjecting on the Frattini quotient and is therefore the whole group. Projectivity of the free target gives a section. The section is itself Frattini-surjective in the source, so is surjective. This proves an actual isomorphism, not faithfulness merely for a subgroup of finite abelian index.

The weights 1, 2 and 3 define an injective weighted Magnus expansion. A nonidentity element survives a finite quotient that kills a tail of the convergent basis; the finite-rank Magnus expansion then detects it at a finite degree. The Gamma-action preserves this filtration. For a torsion-odd lift its abelian class has no degree-one component; its possible degree-two leading part is even under complex conjugation, whereas the exact odd eigencondition makes that leading part odd. Since p is odd it vanishes. This parity argument is applied only after lower degree terms vanish; it does not incorrectly assert that every degree-two coefficient of an arbitrary odd generator is zero.

## Rational coordinates, resonances and companions

The removal of the finitely many singleton weights satisfying q_o(u^m)=0 is legitimate: quotienting the target by those free generators is equivariant, preserves freeness on the others and preserves density in each remaining finite weight quotient. The linear target maps then kill all torsion. Even lifts begin in target length two and odd torsion lifts in length three.

Finite generation over Lambda implies that an R-coordinate isomorphism and its inverse have a common p-power denominator on the integral lattices. Completed tensor powers at a fixed degree remain torsion free and the induced changes have a bounded denominator. The proof consistently uses bounded-denominator rings, not the larger formal series ring Qp[[T]].

The companion polynomials have integral coefficients because Gamma acts on a finite integral lattice. Their roots reduce to one: the image of the pro-p group in the finite reduction is a p-group, hence its eigenvalues in characteristic p are one. The cyclic orbit classes give a rational basis. Their leading expressions differ from an invertible linear change by terms in lower assigned generators. Successively changing the even and then odd variables is therefore a homogeneous triangular automorphism, with a bounded denominator in every fixed degree.

The even companion error has zero abelian class and assigned degree two consisting only of free-odd quadratic words. The odd companion error has no linear odd-torsion term and has only XXX, XY and YX terms in degree three. Evaluating Y introduces adjacent-pair denominators but no full triple denominator. Thus the displayed equations q_e B_e=C_e and q_o B_o=C_o are exact leading-length equations. Constant partial fractions give the same numerator divided by every required root power, including repeated roots.

## Convergence and the analytic identity

Killing longer tails of an actual convergent free basis tends uniformly to the identity in every finite quotient of H. Continuous maps from H into a finite arithmetic-weight unipotent quotient have compact image. Consequently the coefficient functions used in substitution are bounded; locally constant approximation justifies the completed tensor evaluations. Bounded rational coordinate changes preserve this conclusion degree by degree.

Discarding a sufficiently large ordinary initial range of test weights avoids every possible integer resonance for singleton, pair and triple sums. The remaining residue-class tails still contain infinite sequences accumulating at an interior point of the open p-adic unit disk, independently in every variable. After clearing the finitely many pair and triple factors, successive one-variable identity theorems yield a genuine identity of bounded power series. No inference from boundary accumulation or a merely formal Fourier sequence is used.

## Nested divisors and coefficient separation

For a selected disjoint block, replace its last coordinate by its product minus the chosen root. Because that root is congruent to one, this is an automorphism of the complete integral power-series ring, and hence preserves the bounded-denominator ring. The induced map into the power-series ring over the fraction field of the base coordinates is injective.

After the selected product equations are imposed, a coordinate monomial is constant precisely when its exponent vector is a linear combination of the disjoint block indicators. An interval of length two or three can be such a union only if it is a single selected block: two selected blocks have total length at least four. Every other interval denominator therefore has nonzero constant in the base fraction field and is a unit in the transverse power-series ring. A distinct root on the same interval is also a unit there. In particular, internal pair denominators of a selected triple do not acquire transverse poles at selected external pairs.

Extraction first at all selected triple poles forces each selected triple to occur as an outer triple denominator. A pair denominator cannot provide one. Maximal triple count then excludes every additional triple. Only after this step are the external selected pair poles extracted. Internal pairs now lie in already fixed triple blocks and are disjoint from the external pair blocks, so cannot provide their poles. Maximal pair count fixes the rest of the tiling.

For the fixed tiling and root labels, a contribution to the selected negative coefficient requires componentwise domination of the selected pole-order vector. Pareto maximality excludes strict domination. Incomparable vectors are insufficient in at least one coordinate. Wrong Delta labels vanish on the chosen residue grid. The coefficient left is the nonzero singleton function times the restrictions of the selected numerators. They lie in independent sets of base coordinates, so remain nonzero in the common fraction field. Pair-NV and Triple-NV therefore give the contradiction. This includes multiple roots and does not use a false simple-pole residue argument.

## Scope and source comparison

The degree-three extension has kernel L3(Q) plus [Q,Tplus] as a vector space; its Gamma-action may mix these summands through the quadratic companion. That qualification is essential and present. Changing the odd lift changes the numerator by q_o times a function with only proper pair denominators, which vanishes on every triple root divisor. Changing a cyclic generator by an invertible polynomial modulo q_o scales its restriction by a nonzero root value. The condition measures the stated class-three extension, not an unspecified ordinary triple Massey product.

I freshly read the complete proof of Wake-Wang-Erickson Proposition 2.2.6 and the preceding involution/twist definitions in `work/wake_wang_erickson_ordinary.txt`, printed pages 3-4. The source is https://arxiv.org/pdf/1510.01661v4; a fresh web request was disabled (`turn335988106view0`), so that request is not recorded as a successful retrieval. The already archived complete primary text was used.

The proof states Ext1 of the twisted, inverted p-ramified module equals the corresponding even unramified component, and Ext2 is zero. Its local-unit exact sequence supplies rank one independently of the vanishing assumption. After inverting p, elementary-divisor duality over R gives the same torsion factors on the two sides. The source's inversion followed by twist sends a Gamma eigenvalue alpha to u/alpha. The candidate keeps the exceptional characters separate and correctly refrains from obtaining pair nonvanishing from a characteristic ideal alone.

The conditional algebraic theorem is therefore checked. Its cyclicity hypotheses, Pair-NV outside the earlier Greenberg setting, and especially actual arithmetic Triple-NV remain explicit additional gates. The example showing freedom to alter a degree-three companion is only a formal compatibility observation about lower data. No arithmetic counterexample or unconditional faithfulness assertion follows from it.

## Final TeX and all odd-character extension

The complete final `work/odd_torsion_cubic_section.tex` was then read in full, SHA256 `f6e6ccff6c6d17c62f6e0700959e504466033620d7413bc31a314e2f615463b0`. It incorporates the correct target-length wording and allows one cyclic torsion module in each of several odd characters. This extension also passes: the sum of the three target residue characters uniquely determines the companion's odd character, so two differently colored cyclic modules sharing a root cannot contribute to the same chosen residue grid. The same finite resonance deletion, triangular coordinate change and pole extraction apply to the finite union of their roots. The text correctly retains the one-cyclic-module-per-character assumption; it does not separate several indistinguishable same-character summands.

The formal lower-data paragraph is also more precise: changing the companion by a matching element of L3(Q) preserves even the ordinary class-two quotient. The arithmetic paragraph now explicitly limits the quoted source application to p at least five, with smaller primes handled separately. No further correction is requested. **Final TeX verdict: PASS for K17-CUBIC-ODD with all its stated hypotheses.**
