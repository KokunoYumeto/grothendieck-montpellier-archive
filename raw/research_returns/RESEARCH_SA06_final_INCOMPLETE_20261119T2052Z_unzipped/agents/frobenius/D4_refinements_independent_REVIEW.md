# Independent review of D.4f–g

Reviewer: GPT-6 Astra (OpenAI, ChatGPT Pro mode), agent /root/frobenius. Date: 19 November 2026.

We independently read research/agents/real_weil/D4_refinements.tex and reopened Milne's primary 2002 article. The two proofs pass under their stated hypotheses, including the explicit requirement that specialization functors be exact, faithful morphisms of Tate categories.

## D.4f: effectivity and the Tate conjecture

The numerical composition–trace pairing between the two rational correspondence spaces is nondegenerate by the definition of numerical equivalence; the customary graded trace sign does not alter nondegeneracy. Rational dual bases therefore give the claimed injection after extension to \(\mathbf Q_\ell\). Pairing a purported linear relation with the realized dual basis recovers each coefficient, since realization preserves composition and trace. Mere faithfulness of an arbitrary rational-linear representation would not by itself prove this scalar-extension assertion; the supplied pairing argument does.

Frobenius is central because it commutes with all correspondences after realization and that realization is faithful. The centre of a finite-dimensional semisimple rational algebra is a product of number fields, so each central element has square-free minimal polynomial. The rational Chinese-remainder projector therefore realizes exactly the Frobenius-fixed subspace. If this projector image is effective, its weight zero forces it to be a summand of degree-zero motives: all other degrees have disjoint Frobenius absolute values, and faithfulness removes the cross maps. Thus it is Artin. Frobenius equal to the identity then makes it a direct sum of unit motives, producing all the fixed classes by algebraic cycles.

In the converse, Tate surjectivity on products gives all Frobenius-equivariant realization maps, while the preceding pairing gives injectivity. A common Frobenius constituent yields a nonzero realization map from a simple motive to the effective Honda–Tate realization constructed in Part B. Fullness makes the rational morphism space nonzero, and semisimplicity splits the simple object off that effective motive. The weight-zero and negative-weight qualifications are necessary and are retained in the referenced D.4b. The all-varieties assertion over the fixed finite field is exactly what is used; no automatic extension from the abelian-type case is asserted.

## D.4g: common polarization from relative generators

Milne (2002), the definition preceding Lemma 1.2 and Lemma 1.2 with its proof, printed pp. 602–603, explicitly describes compatibility classes and restrictions of positive forms to direct summands. Therefore a fixed generator form extends by sums, tensors, duals, and summand restriction to a form on every object of the stipulated generated category. Its specialization is positive and nondegenerate. Exact faithfulness reflects invertibility of the associated map to the dual, and its trace form is positive on the rational endomorphism subspace. This proves the pulled-back form is a Weil form.

The same construction uses exactly the same relative generator forms at every specialization. Each object therefore has a common Weil form lying in every pulled-back positive class. Since a polarization consists of these compatibility classes, all the pullbacks coincide. No independent choice of an involution, fibre identification, or positivity class is smuggled into the generator argument.

Milne's Theorem 3.3 and Corollary 3.4, printed pp. 607–608, supply numerical–homological equivalence and geometric polarization under the CM Hodge hypothesis. The stated 2026 theorem is an explicitly cited input owned by the arithmetic agent; this audit does not independently verify its entire proof. The specialization argument using smooth proper local systems is valid for the specified extending cycles and projectors. Between any two points, an auxiliary prime distinct from both residue characteristics gives a connected open on which vanishing is locally constant. Existence and typing of the category and specialization functors remain hypotheses, as the fragment states.

## Opened primary source

Milne, J. S. (2002). Polarizations and Grothendieck's standard conjectures. *Annals of Mathematics, 155*(2), 599–610. Opened https://www.jmilne.org/math/articles/2002aP.pdf and compared the local published-layout arXiv-v3 text. Checked Remark 1.1, the definition before Lemma 1.2, Lemma 1.2 and its proof, Proposition 1.4, Theorem 2.1, Theorem 3.3, and Corollary 3.4. Printed-page locators above refer to the published-layout text.
