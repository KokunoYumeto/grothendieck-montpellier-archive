# F60 — independent complete proof and source-applicability review

Reviewer: /root/rectangular_and_theta, GPT-6 Astra Pro; reasoning-effort setting not exposed. Date: 2026-11-21 UTC.

**Final verdict: PASS.** The entire report agent_bounded_kernel_character_gate.md was read and independently reconstructed. The final reviewed SHA256 is b3016fa590e96d69d3f2ba3c737cebf0ff3668236b65db47bb3ad81ccb331592.

The initial whole-read version was 600d76672aba7f13c0af4b3bb97db7b5fdd7fe27853a4166b20a309a0f1bba35. One scope correction was requested: the optional same-module conclusion must retain semisimplicity. The final version explicitly supplies that hypothesis and states that without semisimplicity only the character conclusion is asserted. That exact delta was checked. No mathematical blocker remains.

## 1. Finite-algebra trace rigidity

I independently rederived the lemma without semisimplicity.

For each a in a finite-dimensional F-algebra, a satisfies a nonzero polynomial over the constant field F. Under the representation into matrices over F[z,z^-1], the same polynomial annihilates its image. Over a finite constant splitting extension E/F, every generic eigenvalue is a root in E, regardless of Jordan blocks. The trace is thus a sum of finitely many fixed constants with integer algebraic multiplicities.

Its simultaneous membership in F[z,z^-1] forces every nonconstant Laurent coefficient to vanish: the powers of the indeterminate z are linearly independent over E. The remaining constant lies in F and equals the value at z=-1. No field-continuity assumption, semisimple-module assumption, or choice of a continuously varying eigenvalue branch is being used.

The optional semisimple strengthening is also correct. Each constant central idempotent has integer trace equal to rank, and this trace is constant by the same lemma. Matrix units identify the diagonal pieces inside a simple matrix factor, so these ranks determine the simple multiplicities. This applies only after the explicitly assumed splitting of a semisimple algebra.

The qualifier matters: the dual-number algebra can act by ε↦[[0,z+1],[0,0]], giving a split module at z=-1 and a nonsplit module at z=1 while every character remains constant. The final report correctly excludes this example from its same-module claim.

## 2. Bounded graded kernels and Künneth

The finite cohomology character h_C(v,z) has genuinely nonnegative integer coefficients, with all sums finite because the complex is bounded and each term is finite-dimensional internally graded. The internal and cohomological gradings are independent; z=-1 takes the Euler character and z=1 forgets cohomological degree.

The supplied splitting proof is sufficient. Graded complements split a bounded complex into its cohomology and contractible pairs. Tensoring over a field preserves the contracting homotopy and yields the finite Künneth decomposition, with both degrees adding. Thus the matrix-convolution identity h_(K⋆L)=h_K h_L is an equality of full cohomology-character matrices, not just Euler classes.

An ordinary isomorphism of complexes preserves this full character. A distinguished triangle generally does not, which is the essential scope distinction in the hypothesis.

## 3. Exact relations and the finite-algebra application

Condition K6 is correctly stated as factorization of the full cohomology matrices through the actual finite-dimensional algebra. The sufficient lift condition is also correct: clear rational denominators (including scalar denominators), expand Laurent coefficients, and move negative terms to the opposite side. Finite positive multiplicities and internal shifts in cohomological degree zero then represent the coefficient terms. An ordinary isomorphism implies the corresponding equality of full cohomology matrices. Enough such relations give the claimed algebra factorization.

This is not implied by a mere equality in the triangulated Grothendieck group. Nor is it implied by lifting only the quadratic and adjacent degree-five relations. The report retains both boundaries.

For every word, trace rigidity identifies the trace of the cohomology-character matrix with the specified Euler-module trace. At z=1 this is a nonnegative Laurent polynomial. The stronger observation is valid too: since the full closed-word trace character is nonnegative and independent of z, all its nonzero cohomological-degree coefficients vanish.

The actual F57 N# word has negative Laurent coefficients, so the contradiction is exact. The finding is stated for the specified five-state Euler module; it does not turn an arbitrary positive representation of a larger tensor module into an effective projector onto that summand.

## 4. Primary-source checks

I reopened and read the supplied TeX and primary PDF-text contexts of:

- IV Proposition11.8, printed p61: generic semisimplicity over Q(v), and existence of a finite splitting extension. The report does not silently assert splitting over Q(v) itself.
- IV §11.8, printed p67: dimension114, the actual rank-four module list, and the explicit warning that the quadratic and adjacent nonstandard braid relations do not generate the full rank-four relation ideal.

The exact source proof and page breaks were inspected. The trace-rigidity argument needs only finite dimensionality; the source's semisimplicity is used only for the optional module-isomorphism interpretation.

The negative word identity and exact v=3 value are from F57, for which this reviewer independently transcribed the primary Figure22, reconstructed the matrices and word trace, reran the exact certificate, and matched the complete final fragment. F60 does not introduce a new unverified computation.

The EGA/SGA dictionary locators are the already audited project framework. This review does not claim a fresh inspection of every archive leaf.

## 5. The one-word rank-one relation

I independently reconstructed the additional K9 argument.

The original Q-word contains the rank-one matrix Q_1Q_3, so the full word has rank at most one. Its nonzero trace polynomial gives rank exactly one over Q(v). The dual transpose/reversed P-word retains that rank and trace. Every rank-one matrix W=ab^t satisfies W²=(b^ta)W=Tr(W)W. Thus the displayed relation is an actual annihilator relation on N#, not a relation automatically valid in the entire algebra.

For a kernel lift, an ordinary isomorphism

\[
K_W\star K_W\oplus E_-\otimes K_W
\simeq E_+\otimes K_W
\]

with the stated degree-zero coefficient objects gives C²=pC for the full cohomology matrix C. At v=3,z=1, the resulting matrix M is entrywise nonnegative while p(3)<0. Entrywise comparison of M²=p(3)M forces every entry of M to be zero. Positivity at (3,1) reflects zero for a finite Laurent polynomial with nonnegative coefficients, so every cohomology entry vanishes. The Euler trace would be zero, contradicting p.

No spectral theorem, purity, semisimplicity, full relation presentation, or cohomological concentration theorem is needed for this second gate. It requires exactly the displayed ordinary-isomorphism lift of the actual module-annihilator relation. The report explicitly says that a general algebra action does not automatically supply such a lift for every relation of its Euler module.

## 6. Scope and result

The following are correctly left outside the finding:

- triangle-only relations and coefficient objects with additional cohomological degrees;
- unbounded complexes;
- geometric convolution without the specified matrix-cohomology character comparison;
- larger modules without the required effective summand comparison;
- the ordinary Soergel category, whose tensor product is not silently replaced by tensor product over a field.

The two proofs are complete, complementary, and independent of finite-field weight assertions. The constant-character theorem removes the proposed bounded-complex repair under the full finite-algebra relation hypothesis. The rank-one test removes one explicitly specified ordinary-isomorphism repair using a single actual module relation.

Final report b3016fa… is PASS. The forthcoming generated fragment requires a separate full final-text match.

## 7. Complete generated-fragment match

The entire finding_F60.tex was subsequently read at SHA256 30461c370c3282c33033e0304d7f5e139d79425a9d738fae154aaa7adfc42c6f. **Final-text PASS.**

All proofs and scope conditions match the corrected reviewed report. The fragment explicitly distinguishes the polynomial p(D) from its Laurent substitution π(v)=p((v+v^-1)²), eliminating the report's harmless overloaded notation. The optional same-module assertion retains semisimplicity; the main character lemma does not require it. The Künneth splitting proof, complete relation-factorization premise, rank-one one-word relation, positive evaluation argument, and separate dictionary are all preserved.

No further correction is required.


