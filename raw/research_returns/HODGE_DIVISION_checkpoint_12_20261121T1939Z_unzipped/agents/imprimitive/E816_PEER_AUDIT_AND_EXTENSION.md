# SF-E816 whole-proof audit and a separate new amplitude extension

Reviewer/author `/root/imprimitive`, GPT-6 Astra Pro, inherited effort not externally exposed, HODGE_DIVISION, 21 November 2026.

## Whole-proof audit of the supplied E816 draft: PASS

The complete `rm_two_cohomology_cone_obstruction_draft.md` was read. Its primitive irrational RM-plane argument forces every unequal rational class difference to have signature(2,2). The common-rank finite-isogeny splitting of stable projectively flat factors is an actual line-bundle construction. Mumford index2 and finite étale trace give cross-Ext concentration in degree2; finite filtrations preserve it in both arguments. Hom/Ext1 vanishing gives canonical actual class summands, and exact translation/tensor functors preserve these summands and their coherent actions.

For the triangle B[1]→E→A→B[2], the three long exact sequences have the claimed indices. In particular Hom(A,-) identifies Ext2 and Ext3(A,E) with those of(A,A); Hom(B[1],-) identifies Ext1 and Ext2(B[1],E) with those of(B,B). The two final connecting maps factor through Ext3(A,B) and Ext4(A,B), hence vanish. This proves the actual equivariant short exact sequence for middle self-Ext, for every gluing class and without a canonical splitting, formality, simplicity or gluability assumption.

The exterior-algebra proof is complete. For balanced v=omega+ wedge omega-, cap2 has rank18 and kernel K+⊕K-, where each primitive hyperplane has dimension5. Bidegree decomposition shows its common annihilator in wedge4 is exactly Cv. If v were a sum of three nonzero pure terms, their three rank6 cap images would have a direct sum of dimension18. Thus every vector in ker cap(v) would kill each term, forcing each pure term into Cv, contradicting the different cap ranks. Two or fewer terms already contradict rank subadditivity. A common divisor shear preserves this argument.

Each actual equivariant class block contributes at least6 invariant self-Ext2 by natural Hochschild evaluation. Disjoint class sets prevent virtual cancellation, so balanced character requires at least4 terms and gives invariant self-Ext2 at least24. Injective invariant degree-two trace gives evaluation surjectivity by the perfect CY4 adjunction, hence exact dimension18. The contradiction is valid without any endomorphism-dimension hypothesis.

Published Mumford and supplied S21 inputs retain their previously recorded source scope. No new numerical calculation or proof-assistant formalization is claimed for this universal argument.

## New author derivation: arbitrary bounded amplitude with globally disjoint class sets

This extension was derived separately during the audit and sent to the parent and sixfolds agent for independent review. It is not labelled an independent re-proof of an existing theorem.

Assume the same stable projectively flat factor and primitive-difference hypotheses, but let E have any finite number of nonzero vector-bundle cohomology sheaves. Suppose the sets of normalized classes in distinct cohomological degrees are pairwise disjoint. Shift E so its highest nonzero cohomology is A=H0(E), and set F=τ≤−1 E. There is an actual equivariant truncation triangle

    F --i--> E --> A --e--> F[1].

Every Postnikov piece of F is H^-k(E)[k], k>=1. Cross-Ext concentration2 gives

    Ext^j_G(A,F)=0 for j>=2,
    Ext^j_G(F,A)=0 for j<=2.

Indeed the first group on a piece is Ext^{j+k}_G(A,H^-k E), whose degree is at least3. The second is Ext^{j-k}_G(H^-k E,A), whose degree is at most1. Finite extension closure preserves both vanishings. This uses no spectral-sequence degeneration assertion.

The triangle now gives Ext^j_G(A,E)≅Ext^j_G(A,A) for j=2,3 and Ext^j_G(F,F)≅Ext^j_G(F,E) for j=1,2. In the final Hom(-,E) sequence, an element represented by i[j]∘a, with a:F→F[j], has connecting image i[j+1]∘a[1]∘e. The middle composite belongs to Ext^{j+1}_G(A,F)=0 for j=1,2. Therefore

    0 → Ext²_G(A,A) → Ext²_G(E,E) → Ext²_G(F,F) → 0.

Induct on the number of nonzero cohomology sheaves, shifting the remaining truncation when necessary. This proves the exact dimension identity

    ext²_G(E,E) = Σ_j ext²_G(H^j(E),H^j(E)).

Each cohomology sheaf splits canonically by its actual normalized classes, and each nonzero block contributes at least6. Global disjointness means every class in the signed character has a nonzero coefficient. The same minimum-four-pure-terms argument gives ext²_G(E,E)>=24, contradicting injective balanced degree-two trace, which forces18.

Thus three or more cohomology sheaves do not evade E816 under global class disjointness. Repeated normalized classes across degrees are not covered by this derivation. No assertion about their connecting maps, existence or semiregularity is inferred.
