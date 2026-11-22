# Independent whole-proof audit: D-HOS11–12

**Verdict: PASS.** Actual completed audit timestamp: **2026-11-21 20:49:41 UTC**. Auditor: `/root/imprimitive`, GPT-6 Astra Pro, effort inherited/not exposed, HODGE_DIVISION. This is a complete independent mathematical proof and source-scope review, followed by separately authored exact finite algebra. The author proof and checker were read before writing the independent checker; this is not a blind audit.

Audited complete proof: `agents/g34_eightfolds/bireflection/higher_odd_symplectic_three_section.tex`, SHA-256 **43d9154af45a2042e1cbbd5a0f536a7f932e0cad351e29e980a1ca5b3d65dae9**. I read every line, the entire author `check_higher_symplectic_three.py` and retained output, and the complete invoked interfaces D-HOS02, D-HOS07–08, and the normalizer/multiplier parts of D-HOS09–10. The q5 proof had already received my complete independent proof/source/code audit in this run.

## Full proof checks

1. **Complete normalizer scope.** For PSp(2n,3), n≥4, the ordinary cover is Sp and the outer quotient is the diagonal C2; there is neither a field automorphism nor a graph automorphism in this range. I freshly reread the complete Li–Xia §2.2.2/Table2.1 on author p14 and the full HHM exceptional-cover paragraph/Table1 p35. The perfectness argument makes the natural GSp lift agree exactly on the represented group, including center-killing representations. It does not leave an uncontrolled scalar character.
2. **Involutions.** The rank-two natural involution scales the line-radical quotient by minus the identity, so the carrier/fixed-space estimate is `(1−3^(−n+1))/4≥13/54`. For a general noncentral involution, putting the radical plane inside the smaller nonzero eigenspace leaves a moving quotient summand of dimension at least4; this gives2/9. The asserted invariant fixed fraction≤1/2 is the actual Q/opposite generation result, not a character-ratio assumption.
3. **Nonzero quadratic case.** The exact transvection commutator has trace2+mu^(−1). For mu1 its square, and for mu−1 its cube, is minus the identity on the natural plane. I checked the rank inequality with a scalar chosen from the largest eigenspace of T: `rank(rho(k)−1)≤2nu(T)`, together with the monotonicity of projective support under taking powers. This gives13/108.
4. **Self-adjoint cases.** Polarization gives h*=h and h²=mu. The square case is a represented involution modulo scalars. In the nonsquare case v,hv form an independent totally isotropic plane and the shear has the two equal coefficients in HOS3.4. Those equal coefficients are essential: they give the anisotropic binary form x1²+x2² over F3. I checked the completion to a natural four-space and availability of a complementary radical plane at n≥4.
5. **Exact carrier phase.** In the declared Weyl convention, multiplication by psi(−c(u1²+u2²)/2) conjugates L_(x,y) exactly to L_(x,y+cx'), including the constant half-pairing term. The eigenvalue multiplicities are1,4,4, so the carrier support is5/9. Tensoring with an arbitrary finite-order multiplicity operator preserves the maximum eigenspace fraction; no scalar third-power assumption on the whole representation is used. Nonzero linear weights have equal multiplicities and fixed fraction<1/9, giving support16/27. Combining these and the full-Q fixed bound gives5/18 before the rank-commutator factor1/2.
6. **Mixed source obstruction.** The factorwise convolution and weighted-cycle quarter estimate cover all normalizers of all indicated central products. The theorem explicitly assumes selfduality for every F3 factor, while F5 factor selfduality is the previously reviewed Vinroot consequence. The invariant bilinear line and nontrivial similitude character therefore exist for the actual inducing image. The original imaginary character field is contained in the inducing character field by the induction formula; equality is not assumed. Two genuine multiplier-nontrivial inertias have half-cost. Actual intermediate-cover factorization gives genus0, at least12 branch points, and total moving rank2e+6. The continuous bound e≤324/11 plus the elementary floor27 leaves27,28,29, each ruled out by exact ceilings. No dominance is inferred from source dimension.

**Scope retained:** the normalizer estimate applies to every ordinary irreducible representation at q3; the geometric exclusion applies only to the stated selfdual q3 factors, possibly mixed with q5 factors. The argument does not exclude nonselfdual q3 cores and does not claim that those are sources.

## Separately authored arithmetic

`independent_check.py` imports no author code, source matrix data, or output selections. It uses python-flint nmod matrices and direct integer Weyl-phase entries, in contrast to the author's custom tuple matrices and symbolic exponent simplification. Actual fresh run **PASS in0.449292201seconds**:

- all48 GSp2(F3) matrices; all576 nonzero vector/parameter commutators,288 for each multiplier;
- all729 self-adjoint natural4D matrices, constructed independently by parametrizing alternating matrices J*h; all72 solutions of h²=−I and all11,520 nonzero-vector/parameter cases;
- **81,648 exact Weyl matrix-entry exponent identities**, covering both central characters, both shear coefficients, all translations and multiplications on function spaces F3² and F3³;
- an independent circular-convolution derivation of the binary multiplicities1,4,4;
- all exact support constants and endpoint costs `(27,60,68),(28,62,68),(29,64,70)`.

These finite computations supplement the universal proof. They are not stated to enumerate arbitrary-rank symplectic groups. No fresh execution of the author's checker is claimed in this audit; its entire code and retained actual output were read.

## Source boundary

The new q3 carrier and commutator arguments are elementary and checked in full. The only classification premises are the already reviewed complete ordinary cover and automorphism statements, freshly reread at the exact Li–Xia/HHM locators above. D-HOS02's degree floor and D-HOS07–08's carrier/opposite-radical inputs are previously complete reviewed proofs, whose relevant full interfaces were reread. The published q5 reality input is carried from the immediately preceding full q5 audit, not represented as a new original-source proof here. No new Weil-character classification or finite character table is a premise.
