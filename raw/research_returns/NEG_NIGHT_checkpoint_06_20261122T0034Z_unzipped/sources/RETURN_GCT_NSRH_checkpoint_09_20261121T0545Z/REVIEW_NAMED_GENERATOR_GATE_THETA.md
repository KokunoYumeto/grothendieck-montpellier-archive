# Independent review: named-generator and source-positivity gate

Reviewer: /root/rectangular_and_theta  
Date: 2026-11-21 UTC

## Verdict and exact targets

**PASS: complete report and complete generated fragment.**

- Report: agent_named_generator_positivity_gate.md  
  SHA256 d1357bcb46a6836ec2c83bc8bf3bf2e11cc728cf849a80fe00e98433e3f85a4d
- Fragment: finding_F57_F58_source_gate.tex  
  SHA256 f4ded9c74a63a1eda1dd0e20cc4011588d93bbd540ee890139afecbf5a3482cc

I read the complete report and complete 205-line final fragment, checked the supplied primary-source contexts listed below, and independently reconstructed the new elementary implications. I checked the two final wording/notation changes and the added nonclosure paragraph. No mathematical blocker remains.

## Primary-source scope

The reviewed claim is correctly limited: IV/VIII do not state unsigned Laurent action coefficients for every named nonstandard generator in every designated cell basis. They do state signed/factored coefficient conditions and cellular specialization conditions.

I independently read the supplied IV TeX contexts for the ordinary upper based module definition (Definition 5.3), the signed swap in Definition 13.2, all of Conjecture 19.1 and its following strengthening discussion, and the relevant Remark 11.19 and Example 19.3 passages. The Figure 21/22 matrices, specialization, actual full-algebra module scope, and primary PDF locators were independently checked in my earlier complete F57/F58 reviews.

I independently read the supplied VII generator/spectral-projector and Kronecker rescaling contexts, and the supplied VIII contexts for the right generators, minimum-degree globalization, Conjectures 3.3, 3.4 and 3.7, the complete left Conjecture 2.7 with its external-basis definition, and the rank-three Figure 2 coefficient and surrounding discussion. The final record does not claim that I recomputed the complete published rank-three multiplication table. Its numbered VIII PDF locators were supplied by the author's separate exact PDF audit; my substantive checks used the original supplied TeX contexts.

The source distinction is essential and correctly retained:
- spectral positivity/negativity labels do not imply an effective canonical cone;
- integral-form membership and ring generation do not imply cone generation;
- the left nonstandard Schur basis is not identified with all named elements of the commuting right algebra;
- the revised IV cellular tensor basis is not automatically VIII's earlier conjectural algebra basis;
- positive vanishing exponents are explicitly allowed to disappear under specialization.

The reported source normalization inconsistency is not propagated: the applications use the independently checked explicit P+Q=D convention and actual contragredient rule.

## Published signed coefficient and nonclosure

The printed coefficient
-(q^2+q+1)(q-1)^2/q^2
is negative for positive q other than 1. The substitution v=q^(1/2) gives exactly
-(v-v^-1)^2(v^2+1+v^-2).
This demonstrates the signed scope without claiming that the negative raw coefficient violates its source conjecture. The fragment correctly avoids an unsupported assertion about inserting zeros between half-parameter parity classes in the source's unimodality convention.

The added nonclosure proof is correct. The sum
1-(v-v^-1)^2=3-v^2-v^-2
has nonzero value at v=1, so any representation as a signed vanishing factor times an effective Laurent polynomial has exponent zero. Both possible overall signs still have mixed coefficients, so neither works. The same reasoning applies to the F57 trace's failure to lie in that class, but that trace is not an individual canonical constant covered by VIII Conjecture 3.4. This prevents a false inference from word traces to a refutation of the source statement.

## Effective algebra-to-cell action implication

The three hypotheses are correctly separated:
1. effective multiplication in the chosen basis;
2. effective expansion of each named generator in that basis;
3. an actual coordinate cellular subquotient.

Under them, a named-generator matrix is a positive Laurent combination of positive multiplication matrices. Restricting to a stable basis-subset span and projecting to another coordinate quotient retains entries and introduces no subtraction. Thus the induced matrices are positive.

The full-algebra application then includes the actual N# summand and invokes F57. An arbitrary basis of N# cannot evade the trace obstruction. A larger representation is not excluded unless projection onto the specified summand is itself effective; that extra premise remains explicit.

The two-row source-cell application instead invokes F58's regular coordinate specialization premise. A nonzero effective Laurent entry cannot vanish at v=1, while the actual designated generic cell has a proper coordinate cellular submodule at specialization. This is an obstruction to the conjunction of strict action effectivity and the source's precise cell compatibility, not to the source conjecture alone.

## Normalization checks

For a rescaling P_i'=epsilon_i h_i P_i with nonzero effective Laurent h_i, the specified word trace is epsilon H p. If epsilon is positive, its leading Laurent coefficient is negative. If epsilon is negative, its value at v=1 is negative. These two cases exhaust the choices, and both exclude a nonnegative Laurent trace. No assertion about arbitrary non-Laurent division is introduced.

The factor v-v^-1 is a nonunit of the local ring at v=1. Inverting it removes that fiber. Diagonal changes by local units preserve the order-two vanishing of the c_0 edge. The final wording correctly says that general basis mixing must be checked against the designated coordinate-submodule premise: a mixing that preserves the premise remains covered by F58.

## Pure-point dependency and nonproper scope

I also read the complete agent_pure_point_complex_trace.md dependency while checking the report's purity corollary. Its criterion is stated for integral Laurent f and gives (-1)^w f(-v) in N[v,v^-1]. The finite Vandermonde argument, unique cohomological degree at a visible weight, and arithmetic coefficient construction establish it. A nonzero f divisible by v-v^-1 has f(-1)=0 and fails the criterion. For rational source coefficients, an actual multiplicity comparison additionally needs integral multiplicities (or an explicitly stated denominator-clearing procedure); the no-go implication for a nonzero vanishing factor is unchanged.

The torus compact-pushforward example is correctly a mixed point object arising from pure coefficients on a nonproper source. It is not a contradiction to the pure-point criterion. The fragment correctly distinguishes raw point Euler traces, pure coefficients on a source, positive graded dimensions, and inserted-operator traces.

## Complete fragment match and final deltas

The fragment retains every intended new argument from the report and a separate Grothendieck dictionary. The dictionary uses the effective torus-character cone and virtual Grothendieck group as framework, without asserting a lambda-ring structure on the noncommutative word algebra.

Final changes checked:
- corrected literal Markdown math delimiters;
- corrected general-basis-mixing scope;
- added the signed/factored class's failure of additive closure;
- retained that the F57 word trace is not an individual canonical constant.

No source conjecture is overclaimed or refuted by substitution of the stronger unsigned package.

