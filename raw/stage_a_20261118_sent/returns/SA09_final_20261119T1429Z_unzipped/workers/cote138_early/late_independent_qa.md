# Independent review of four late-packet claims

Reviewer: cote138_early worker, 19 November 2026. This review reads the other worker's proofs and the original transcription; it does not edit the late worker's files. The outcome is a mathematical check by direct reasoning, not a new machine certificate.

## Sources actually read

- `workers/cote138_late/proofs.md`, particularly §§4–5, 8–9; the four corresponding objects in that worker's `claims.json`.
- `SA09_texts/pro/MPL_138_090-133_transcription.tex`, original lines 217–334, 1205–1290 and 1583–1660. These include the actual cell-pinning definition, the partly deleted representability draft, the damaged face condition and the proposed postcomposition criterion.
- SGA 1, Exposé XIII, Corollaries 2.8–2.9, construction 2.10 and Lemma 2.11, recomposed pp. 288–290 / original pp. 389–392, independently opened at <https://arxiv.org/pdf/math/0206203>. The adjacent Corollary 2.12 statement was also read. Retrieval references: `turn215208280view0`, `turn541837494view0`, `turn541837494view1`.

## CL-SA09-138L-020: the cell-pinned elliptic twists

**Verdict: sound.** The two smooth connected covers

\[
E_d:dy^2=x^3-x,\qquad f_d=x^2,\qquad d=1,2,
\]

have degree four and passport \((4)\mid(2,2)\mid(4)\). The two white points are \((1,0)\) and \((-1,0)\); the unique black point and pole are rational as well. Thus the manuscript's individual cell labels can all be imposed over \(\mathbb Q\), with no missing point-of-definition hypothesis. The involution \(y\mapsto-y\) preserves those labels and exhibits exactly why cell pinning does not kill all automorphisms.

The map \((x,y)\mapsto(x,y/\sqrt2)\) gives a label-preserving isomorphism after the finite étale extension \(\mathbb Q(\sqrt2)/\mathbb Q\). A putative isomorphism over \(\mathbb Q\) commuting with \(x^2\) must send the target coordinate \(x\) to \(x\) or \(-x\). The two individually labelled white points exclude the second option. The quadratic function-field extensions over \(\mathbb Q(x)\) are then isomorphic only if \(1/2\) is a square in \(\mathbb Q(x)\), which it is not. Consequently distinct rational isomorphism classes become equal over an étale cover. This violates even the separatedness condition for a presheaf to be an étale sheaf, hence excludes representability of the raw isomorphism-class functor. It does not exclude the finite scheme attached to geometric classes.

## CL-SA09-138L-021: the geometric-class scheme

**Verdict: sound for precisely the corrected geometric-class formulation.** Fixed-degree covers have finitely many geometric monodromy descriptions; fixed cell labels add only finitely many choices. At a prime \(p>\delta\), every geometric monodromy group embeds in \(S_\delta\), whose order is prime to \(p\). The marked base \((\mathbb P^1;0,1,\infty)\) has a smooth proper model with disjoint boundary sections over \(\mathbb Z_p\). These are the required good-reduction hypotheses; one cannot replace them by tameness of an arbitrary family alone.

SGA 1 XIII Corollary 2.9 gives locally constant constructible nonabelian cohomology for finite groups of invertible order in this smooth proper normal-crossing-boundary setting. Construction 2.10 provides the specialization comparison, and Lemma 2.11 preserves peripheral inertia. This yields unramified variation of the finite geometric cover-class and cell-label data. The associated finite étale \(\mathbb Q\)-scheme therefore extends over \(\mathbb Z[1/\delta!]\). Rational twists, such as those in claim 020, concern the raw objects and do not contradict this class-scheme statement.

**Suggested editorial refinement:** proof §5 cites Corollaries 2.9 and 2.12. For the specialization and preservation-of-peripheral-data step, cite Corollary 2.9, construction 2.10 and Lemma 2.11. Corollary 2.12 is principally the prime-to-characteristic presentation theorem. No change to the corrected conclusion is required.

## CL-SA09-138L-060: one branch point per face

**Verdict: sound under the stated finite cellular-graph and universal-cover hypotheses.** Over a disc with zero branch values, every connected component is a trivial disc cover. Over a disc with one branch value, its punctured-disc monodromy is cyclic and transitive on each connected component; filling the branch point gives a disc. Since the source surface is connected, the inverse graph is connected: attaching discs along connected boundaries cannot join distinct graph components.

If a face contains two branch values, the double cover of the sphere branched exactly at those two values restricts to an annulus over that face. To make the Euler-characteristic and boundary language entirely literal, take a compact subdisc containing both branch points. Its connected double cover has Euler characteristic zero and two boundary components, since its boundary monodromy is the product of the two transpositions. Its interior is an open annulus. The third allowed branch value does not matter, because the chosen cover is unramified there. All these degree-two covers also satisfy the manuscript's weaker white-index-at-most-two convention.

**Suggested editorial refinement:** call the inverse image of the open face an *open annulus with two ends*, or insert the compact-subdisc step before speaking of boundary components. This is a precision improvement, not a gap in the criterion. The damaged negation in the transcription remains unresolved.

## CL-SA09-138L-076: universal strict-clean postcomposition

**Verdict: sound for nonconstant holomorphic \(\varphi:\mathbb P^1\to\mathbb P^1\), strict cleanness meaning index exactly two everywhere over one, and a universal quantifier over strict-clean Belyi maps.** Multiplication of local indices proves sufficiency of the four stated conditions.

For necessity, surjectivity of every nonconstant inner map forces every critical value of \(\varphi\) to lie in \(B=\{0,1,\infty\}\). The single family

\[
f_n(z)=4z^n(1-z^n),\qquad n\ge3,
\]

is strict-clean: the roots of \(z^n=1/2\) have index two above one. It has index \(n\) at zero and \(2n\) at infinity. Thus \(\varphi(0)\) and \(\varphi(\infty)\) must lie in \(B\), and neither can equal one. Every strict-clean inner map has index two above its old value one, so \(\varphi(1)\in B\); if it equals one, \(e_\varphi(1)=1\). Every other point of \(\varphi^{-1}(1)\) lies outside \(B\), where the inner map is unramified, forcing its outer index to be exactly two.

**Suggested editorial refinements:** state explicitly why \(\varphi(1)\in B\) is necessary, and replace the unspecified “source/target dual variants” by the displayed family, which already gives unbounded indices at both endpoints. The manuscript's index-at-most-two condition belongs to its folded-edge convention and must remain distinct from this strict-clean reconstruction.

## Overall finding

No substantive mathematical correction is required for these four repaired claims. The recommended changes improve exact citation, topological terminology and the explicit necessity argument. They do not broaden the manuscript's claims or resolve uncertain ink.
