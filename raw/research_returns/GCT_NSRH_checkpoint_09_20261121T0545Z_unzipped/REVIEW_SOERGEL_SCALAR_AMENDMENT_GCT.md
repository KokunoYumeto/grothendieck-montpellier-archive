# Independent review: F59 scalar-complex amendment

Reviewer: /root/gct_statements, GPT-6 Astra Pro. Reasoning-effort setting is not exposed. Date: 2026-11-21 UTC.

## Frozen targets and verdict

Full report: agent_soergel_scalar_amendment.md
SHA256 56022996637e174e50382b3d8cf76ea7f4c3a08900783996bd29dab59e350ebf.

Complete generated fragment: finding_F59_scalar_amendment.tex
SHA256 0edcea01cf3a63495928e4a8b218f1fb37a43dc628291d5ccfb1b5be41e909fa.

**PASS.** Both files were read in full and all mathematical arguments reconstructed. No correction requested. The generated fragment matches the report, including the final nonzero-derived U qualification, arithmetic coefficient field, ell not dividing q, and nonunit Koszul example.

Check type: manual whole-proof review, direct report-to-fragment match, and targeted primary BBD context check. No symbolic or formal-proof verification is claimed. No master file was edited.

## Dependency actually checked

The complete agent_soergel_scalar_complex_gate.md was read. In particular SC-A's generic localization reduction, positive idempotent probability measure proof, support independence, evaluation at u=-1, and coefficientwise evenness of cohomological multiplicities were independently reconstructed.

The argument genuinely forgets internal grading at generic localization. It does not falsely infer that all individual internal-degree multiplicities are even. The pure arithmetic amendment restores a degree constraint through an explicit Weil/purity comparison, not through an invalid graded generic character.

The ordinary Soergel localization/source framework is inherited from the separately reviewed F59 core. This review does not claim a new source audit of every primary ordinary-Hecke statement.

## SA-A: arbitrary scalar coefficient cannot repair U tensor T

1. For A=k[x,y,z], tau=(-x,-y,z), the generic invariant extension has degree two. Thus the actual generic T=A tensor_{A^tau} A is the direct sum of the identity and tau graph modules.

2. For nonzero bounded scalar U, its ungraded cohomology polynomial u(t) is nonzero. Generic Kunneth turns the proposed quadratic into
2u(t)^2(e+tau)=d(t)u(t)(e+tau).
Comparing one graph coefficient in the Laurent domain gives d=2u. This also excludes an acyclic proposed C.

3. Let a be the upper cohomological degree of U and r>0 its multiplicity. Then the upper degree of C is a with multiplicity 2r. The ordinary T is in degree zero. Its derived square has no positive cohomology, and its H^0 is T tensor_A T, nonzero generically. Taking degree 2a therefore gives exactly
(T tensor_A T)^{r^2} isomorphic to T^{2r^2}
as actual bimodules, after forgetting internal grading.
Lower Tor groups cannot contribute to this top degree. No flatness is assumed.

4. The actual ordinary left-origin fiber of T is
B=k[x,y]/(x^2,xy,y^2), of dimension three; all fixed z variables die as well. The right invariant-ring action on B factors through augmentation. Hence the left-origin fiber of T tensor_A T is B tensor_k B, of dimension nine.

5. Applying ordinary fiber to the obtained actual module isomorphism forces 9r^2=6r^2. The proof is valid despite nonflatness because an ordinary tensor functor preserves an actual isomorphism. It is not being applied as an exact functor to a derived triangle.

Thus the family U tensor T is excluded for every bounded scalar C, with no Euler premise. The report correctly leaves nonfactorable nonflat complexes outside this family.

## SA-B: the pure scalar coefficient boundary

1. SC-A gives even total cohomological dimensions of C in every degree.

2. A bounded pure point complex of weight w can contain an eigenvalue of point weight m only in degree m-w. This is the precise BBD 5.1.8 smooth/lisse criterion on a point. Jordan blocks leave the ordinary trace multiplicity unchanged.

3. Eventual equality of finite power sums determines the grouped roots by an invertible Vandermonde matrix with an invertible diagonal factor. For the proposed trace the three roots are beta q^s, beta, beta q^{-s}, all distinct for nonzero s. Their grouped Euler multiplicities are epsilon, 2epsilon, epsilon.

4. No additional invisible roots can survive: a pure complex puts each root into only one degree, so opposite-degree cancellation is unavailable.

5. The three point weights t+2s,t,t-2s force three different cohomological degrees. Their actual dimensions are 1,2,1, contradicting SC-A at the two outer degrees. The argument does not require flat cohomology of X.

6. Both F61 candidates have exactly these odd outer dimensions, with s=2 and s=1. Keeping the original formal grading labels is expressly required. A common scalar line or shift does not remove the odd multiplicities, subject to retaining the stated Euler premise.

7. The grading-only variant is also valid: a single affine degree line with nonzero slope prevents cancellation at each formal degree and puts the outer coefficients in distinct degrees. It is explicitly an additional grading-to-degree comparison.

## Scope and remaining example

The nonunit positive-degree Koszul example is correct. In K(f) tensor K(f), replacing one Koszul generator by its difference with the other produces a closed exterior generator, yielding K(f) tensor (k direct sum k(-deg f)[1]). Its generic complex is acyclic and its Euler rank zero. It therefore does not realize the actual nonzero generic support 2(e+tau).

The two exclusions do not prove an unconditional theorem for arbitrary nonfactorable mixed scalar complexes with nonflat cohomology. They do not contradict the different finite-state category used in F61.

The dictionary distinguishes scalar vector-space complexes from polynomial-differential unit-bimodule complexes, keeps ordinary affine fibers separate from derived base-change assertions, and does not attribute a lambda-ring structure to the noncommutative word algebra.

## Primary context

Freshly read original local BBD Section5.1.8, printed pp126–127, including the concluding smooth/lisse clause. It states the degree-shifted point weights used by SA-B. The remaining arithmetic argument is elementary and included in full in the report.

The EGA/SGA framework locators in the fragment are vocabulary anchors for module/sheaf and coefficient operations, not asserted new source proofs of SA-A or SA-B.

