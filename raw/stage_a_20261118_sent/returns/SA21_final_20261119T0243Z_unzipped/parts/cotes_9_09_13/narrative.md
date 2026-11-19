# IX, scans 66–104: from failed generator lemmas to correspondences of spatios

This section covers all five folders J156-9-09 through J156-9-13: 39 manuscript scans, every transcription line and every accompanying short note. The counts are 36 claim records (031–066), nine consolidated problems (09–17), sixteen mathematical reading alarms and twenty-one checked internal links. It continues IX01–08 and stops before the mathematical development owned by the reader of IX14–18. The next folder's opening was read solely to check the two outgoing links.

The main objects are the author's **disjoncteurs**, sets with symmetric disjunction in which a self-disjoint point is disjoint from every point, and **spatios**, complete ortholattices. Distributivity, atomicity and orthomodularity are not assumed. The supports are biorthogonally closed subsets. Different points may determine the same support, and several universally disjoint zero points may occur. These conventions matter when comparing modern orthosets with a distinguished unique zero.

## The author's sequence of work

Scans66–70 continue a failed attempt to make a general correspondence commute with support and cosupport. An inclusion assumed on66 is not enough for the claimed reverse implication; on67 the author himself requires equality after taking support and strengthens disjunction preservation to faithfulness. On68 he asks whether these stronger assumptions actually force an isomorphism. They do: his later Proposition2 on81–84 gives precisely the faithful join-dense representation theorem needed. The implication back to his earlier question is made explicit as this run's inference, without inventing a backward citation.

The more durable idea appears on69–70. A raw correspondence α admits a reverse correspondence β when α(x) is disjoint from y exactly when x is disjoint from β(y). The closedness of the perpendicular fibers γ(y) is the exact existence condition; the largest normalized reverse value is γ(y)⊥. At this point no separate preservation of disjunction between two source points is necessary. The page's own margin recognizes this distinction.

Two premature lemmas then obscure the distinction between a raw assignment of generator values and a map on support lattices. Lemma1 on72 treats every assignment E→ΣF as if its join extension automatically preserved all joins. Lemma2 on73 treats a support-level adjoint as if it automatically came from a raw pretranspose. Both literal statements are false. The first fails in a three-point disjoncteur, and the second fails when two indistinguishable source points receive different singleton values in a two-point trivial target. The complete finite checks and their outputs are preserved; these refutations concern the early versions, not the author's final theorem.

On76, dated10 juillet, the author restarts systematically with the axioms of disjoncteurs and spatios. The support construction is classical polarity theory. Deleting the zero points preserves the support ortholattice, provided the formulas keep track of which ambient set is being used. The point-to-support map induces a canonical preorder, which need not be antisymmetric. Every complete ortholattice is recovered from its own underlying disjoncteur because its closed subsets are principal ideals.

The representation theorem on81–84 is valid: an orthogonality-faithful map into a spatios with join-dense image determines an isomorphism of support ortholattices. The ensuing dense-subspace corollaries are also valid in their precise support-lattice formulations. Two formulations require care: the lower-point test must quantify over the chosen subdisjoncteur, and the phrase about density in the canonical point preorder needs an ambient-join convention. Intrinsic suprema in a possibly incomplete point preorder do not automatically express the required support join density. These are explicitly separated as reading/convention issues.

Scans90–97 complete the correspondence theory. Proposition3 includes inserted closure identities, and its deferred proof is supplied after a cancelled circular attempt. Proposition4 then makes the decisive correction: preservation of arbitrary joins by the induced map must be accompanied by equality on each singleton support. On97 the author expressly says that he had to add this condition afterward. With it, his five criteria are equivalent: existence of a pretranspose, commutation with support closure, closed inverse membership fibers, closed perpendicular fibers, and the corrected generator extension condition. This also resolves the earlier closure question indexed as MP-SA21-9-08 in the preceding part. It must not remain listed as awaiting inspection of the continuation.

The corollary on98–99 is therefore sound. Arbitrary-join maps of support lattices, normalized compatible correspondences and relations with closed rows and columns determine one another. The relation is formed by taking the perpendicular of each normalized value; it is not the raw graph of α. Composition closes the setwise composite. The resulting category is equivalent to complete ortholattices with all join maps, and orthogonal transposition is an involutive contravariant equivalence. The earlier composition and generator reminders are discharged here.

## The final questions and their present answers

The heading on100 introduces questions suggested by the set case. They are not solved by the preceding correspondence theorem.

| Question | Present answer | Evidence |
|---|---|---|
| Are closed-fiber relations exactly the supports of the OR product? | No in general; yes if one factor is a trivial disjoncteur. | C058, P8. Four-point paired-orthogonality factors give a three-point diagonal with closed fibers but full product closure. |
| Does the pointwise ordered complete lattice of all correspondences admit an orthocomplement? | No in general, even for finite orthomodular factors. | C060, P9. The six-element four-atom example has234 join maps,40 atoms and16 coatoms. |
| Can singleton-wise formulas for the trivial-source complement be applied to arbitrary subsets? | No; the author's warning is correct. | C061–062, P11; explicit two-point certificate. |
| Does every correspondence factor as a comorphism followed by a morphism? | No for the classes defined on104. | C066, P10; a single four-atom map excludes every possible intermediate complete ortholattice, including infinite ones. |

The span obstruction is symbolic, not an inference from searching finitely many middle objects. A C-preserving join map out of the four-atom lattice into a nontrivial ortholattice reflects zero, so its orthogonal transpose takes the top element to the top. Any proposed span therefore sends top to top, whereas the displayed nonzero join map sends top to an atom. A trivial middle object produces the zero composite. The executed calculation verifies the finite map's join identities; the general exclusion is the separately recorded proof.

## Literature fate and dates

The checked pre-1986 foundation is Birkhoff1948, chapterIV §§5–7, and Shmuely1974, particularly the closed-fiber Galois-map construction and completeness result. The cited chapter is **IV**, not V, in the opened revised1948 edition. Those classical results do not license arbitrary incompatible generator assignments.

Four claim records receive classB for exact later mathematical counterparts. Domenach–Leclerc's arbitrary-closure-space theorem matches the closed-fiber presentation; its author preprint is dated November2000 and the journal issue March2001. Coecke–Moore explicitly develops the canonical complete-ortholattice category and conjugate adjunction; arXiv circulation is3August2000 and book publication2000. Ischi's weak-tensor results distinguish the product closures and exclude the hoped-for orthocomplement in the permitted finite example; the journal issue is December2010, online publication20January2011, and arXiv circulation8September2011. These dates are not collapsed, and a related2003 preprint is not used to backdate an unchecked version of the theorem.

Paseka–Vetterlein provides a modern comparison for join-dense orthoset presentations and adjoints. Its first arXiv date is8January2025 and publisher date27May2025; v3 of28October2025 corrects another proposition, which is not used here. The publisher's2025 date takes precedence over the inconsistent arXiv journal-reference year. None of these later matches establishes direct influence from this manuscript.

For the exact scan104 span classes and the unspecified substitute-point programme, the bounded searches found no matching external resolution. ClassD records that literature result; it does not assert that the false span question is mathematically open. Search logs distinguish query families retained from the earlier batches from the exact requests preserved for the final two follow-ups. zbMATH access to a linked record was blocked; Numdam and later bibliographies supplied backwards references. No exact EGA/SGA or other published Grothendieck endpoint was located for this block, and no context-project connection was manufactured from topical similarity.

## Reading alarms and limits

The highest-impact scan checks are the membership/negation signs in the transpose calculation, injection versus surjection in the dense-subspace criterion, omitted membership in the chosen subdisjoncteur, the canonical-preorder wording, ambient sets after deleting E0, and the cross-coordinate indices of the OR product. A further correction concerns the reference to the condition added afterward. All are alarms raised by mathematics; no ink has been seen and no diplomatic transcription is changed. The notation Cbarβ on74 is not flagged as an erroneous extra complement: barβ there denotes the perpendicular fiber introduced on73.

The accompanying short Codex notes correctly identify the explicitly deferred steps, cancelled attempts and open-question heading. Their absence of a warning on a page is not a proof certificate. They receive no Stage1 verdict rows, in accordance with the task. The manuscript's10 juillet and doubtful11.7 dates lack a year on these leaves; the catalogue's year is not silently attributed to the handwriting.

## Ranked follow-up directions, not developed here

1. **Source-critical reconstruction of the correspondence theorem** (C035–038, C052–056; MP10,12,13): establish a clean edition that preserves the early failures and the later pointwise correction. A few-hour run with scans could decide the key signs and condition labels; no new theorem is required.
2. **Restricted geometric correspondences after the two universal obstructions** (C058,060,063,066; MP14–17): identify the intended geometric factor class and what maps should replace all join maps. The first step is a finite list of actual atelier examples and their support lattices, not another unrestricted factorization claim.
3. **Presentation invariance with redundant points and multiple zeros** (C032,040–051,055; MP11): compare the manuscript's conventions with a specified modern orthoset category. The first step is to write the exact quotient/delete/adjoin-zero functors and determine which map class they preserve.

These directions are ranked proposals for later tasks. This consolidation develops none into a new research project.
