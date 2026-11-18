# Mathematical notes on scans 297–311

Manuscript pp. 247–261. The short identifiers refer to entries in CHECK_EVENTS.tsv where a statement was used or checked. The marginal and interlinear readings are identified as such.

## What the pages do

**Products after localization (297–298).** Over a fixed \(S\), the proposed product sends \((\xi_1,\xi_2)\) to \(\xi_1\times_S\xi_2\). Grothendieck compares the diagonal and product functors, first on the category of fibrations over \(S\), then on its localization. He writes down the two adjunction maps and their components. A slanted note asks for preservation of finite products under change of base.

**The localization lemma (298, L).** If each of two adjoint functors carries the indicated class of arrows into the class on the other side, the induced functors are again adjoint. The corollary applies this to the diagonal and binary product and then to the final object. The assumption on \(W\) is stated for a product of two arrows in \(W\).

**The subcategory of spans (299–300, F).** The first numbered lemma identifies the localization of the full subcategory \(\mathscr F\) of spans with both legs in \(\mathrm{Fib}_W\) with the localized diagram category. Assuming this identification, the span is sent to the square with fourth vertex \(X_1\times_S X_2\). Scan 300 checks that the four-vertex map is a termwise \(W\)-equivalence by separating change of base along \(f_0\) from the comparison over \(S'\).

**The subcategory of squares (301–302, G).** A second lemma proposes the analogous localization equivalence for the subcategory \(\mathscr G\) of squares with the two arrows to \(S\) in \(\mathrm{Fib}_W\). On these representatives, restriction forgets the fourth object and its right adjoint supplies the product. The ordinary adjunction and lemma L are used to obtain the localized adjunction, subject to F and G.

**The theorem and its calculation (303–304).** Restriction along the open immersion of diagram shapes has a right adjoint. Its value is represented by the ordinary product square when either leg is a \(W\)-fibration. In general the text factors one leg, the other leg by symmetry, or both legs. The proof of functoriality refers back to the representatives of lemma 1.

**The other extension (304–305).** With an initial object in \(M\), the note marked “NB” gives a left adjoint to restriction. Its square has that initial object in the vacant corner. The drawing is the clearest indication of how this construction differs from the product-square construction.

**Evaluation at 3 (305–306).** The functor previously constructed is composed with restriction to vertex 3. On the stated representatives it takes a span to \(X_1\times_S X_2\). Cor. 1 identifies the composite \(\varepsilon_3^* i_*\) with the right adjoint to the constant-span functor \(p_\Psi^*\). This gives the proposed interpretation as a \(W\)-homotopy limit.

**A category with a final object (306–307).** The projection of the three-vertex shape is factored through the square shape. The auxiliary lemma identifies the relevant adjoint for a category \(I\) with evaluation at its final object \(e\). The argument compares ordinary diagram categories and then passes to fractions. The two different side-of-adjunction phrases are recorded below.

**The three comparison maps (308–309, C19).** Proposition 19 factors \(p_1,p_2\) and compares \(X_3\) with three products having one or both factors replaced. Membership in \(W\) for the three comparisons is equivalent, and the choice of factorization drops out. The next sheet uses this condition to define a \(W\)-cartesian square.

**Essential image (309).** The first corollary sends the image of such a square into the essential image of the extension functor. It expresses the condition in terms of the canonical map \(Q\longrightarrow i_*i^*Q\). The converse is stated when \(W\) is strongly saturated.

**Pasting (309–310).** Two adjacent squares are numbered 1 and 2, and the exterior square is numbered 3. Given that square 1 is \(W\)-cartesian, square 2 is \(W\)-cartesian precisely when square 3 is. The proof replaces vertices until square 1 can be taken cartesian. In the final diagram the same condition \(\beta\in W\) tests both remaining squares.

**Base change of a \(W\)-arrow (310–311, B).** In the new square the top edge is \(f_2\) and the right edge is \(f_1\). Under the \(W\)-cartesian hypothesis, \(p_1\in W\) implies \(f_1\in W\), and likewise with index 2. The margin gives the more precise test with \(p_i\) fixed in \(W\). The proof takes \(\overline X_1=S\) in this case. The converse implications are expressly disclaimed.

**Dual construction (311).** The final paragraph turns to homotopy amalgamated sums and \(W\)-cocartesian squares using a right factorization axiom. It draws a closed immersion, writes restriction and an adjoint to it, and breaks off mid-sentence after “de”.

## Statements left without proof

| Scan | His words | Status on these sheets |
|---|---|---|
| 297, angled note | “Dire aussi que le foncteur” and “aux produits finis” | Preservation by \(f^*\) is called for in the margin. The intervening verb is doubtful. |
| 299, F | “Nous allons prouver ce lemme plus bas. En l’admettant” | The localization equivalence for spans is assumed. |
| 301–302, G | “Je vais pour le moment admettre ce lemme” and “modulo la dém. des lemmes 1 et 2” | The comparison for squares is assumed alongside F. On 307 he writes “Je le ferai demain.” |
| 304–305 | “on trouve l’existence d’un adjoint à gauche” and “la loi fonctorielle étant” | He gives the value using an initial object and treats the action on morphisms as evident. |
| 309 | “La réciproque est vraie si \(W\) est fortement” | The following word is read *saturée*. The converse of the essential-image criterion has no separate proof here. |
| 311, B | “on ne peut en général affirmer les implications inverses” | No counterexample appears in the manuscript paragraph. |
| 311 | “Tous ces résultats … se dualisent” | The right factorization axiom is cited and the dual construction begun. This group of scans ends before the discussion does. |

## Questions and conjectures

On 301, “J’ai envie de prouver que les foncteurs … sont adjoints” introduces a goal. The adjunction is obtained on 302–303 conditional on F and G. On 305, “On veut interpréter ce foncteur comme une” precedes the left-arrow limit sign. Cor. 1 on 306 addresses that interpretation. The remaining express undertaking on 307 is to prove the two comparison lemmas.

## Slips

| ID | Scan | Reading kept, suggested repair and reason | Confidence |
|---|---|---|---|
| S1 | 297 | The final \(\alpha_0\) points left and \(\beta_0\) appears to point right. The two component maps above suggest the opposite directions. Some ends are thickened. | Low |
| S2 | 299 | The small span is described as “dans \(S\)”. The ambient category \(M(\Psi)\) and the placement of \(S\) at the vertex suggest “dans \(M\)”. | Medium |
| S3 | 299 | The last target is \(\mathrm{Ho}_W(\Psi)\). The preceding display and the added fourth vertex suggest \(\mathrm{Ho}_W(\Psi^{\sim})\). | High |
| S4 | 300 | The edge at the left of the first diamond points from \(S\) toward \(X_1\). As a copy of the span on 299 it would point into \(S\). Several edges have been retraced. | Low |
| S5 | 303, 309 | The extension label has a j-like base. The adjacent prose and the unit suggest \(i_*\). On 303 the letter in the Fib condition also looks like \(f'_1\), where the preceding factorization names \(p'_1\). | Low |
| S6 | 306–307 | The lemma says “un adjoint à gauche” for \(p_*\). “À droite” would agree with the preceding corollary and the role of evaluation in its proof. | High |
| S7 | 308 | The low \(S\) is absent from two products in and below the second fan. Supplying the base makes those products agree with the first fan. This may be an abbreviation. | Medium |
| S8 | 309–310 | The written fibration condition on 309 starts at \(X'_0\), where the triangle suggests \(\overline X'_0\). The reduction on 310 reads \(X_0\) followed by a shaft to \(S\), where the proof is dealing with the vertical \(X'_0\)-to-\(X_0\) map. The transcription retains both discrepancies. | Low |
| S9 | 309–310 | “Corollaire 2” appears a second time. A consecutive count would suggest 3 for the second heading, but the author gives no instruction to change it. | Low |

The article before *flèche* on 300, the form *Cet/Ce* on 304 and the gender ending on *saturée* on 309 are unresolved readings. The footed shape on 301 and 311 is recorded as \(\Phi\) with a \(\Psi\) alternative. Neither the change in shape nor the last doubtful side-of-adjunction word on 311 establishes a change of convention.

**RQ311 · Reading question after the freeze (311, line 19).** The frozen alternatives are *gauche* and *droite*. In an enlarged comparison, the ending resembles the clear *gauche* on 307, while *droite* in the factorization reference higher on 311 has a distinct taller final stroke. This supports the first candidate. The opening descender remains very faint.

## Pointers

| Scan | His words | Where the reference leads |
|---|---|---|
| 302 | “(p. 249)” and “cf lemme p. 248” | Manuscript p. 249 is scan 299, lemma 1 on spans. Manuscript p. 248 is scan 298, the lemma on adjunction and localization. |
| 303, 311 | “(p. 240)” and “cf page 240” | A factorization axiom, first used on the left and later invoked in its right-hand form. That page precedes this group. |
| 304–305 | “du lemme 1 p. 249” and “conformément au lemme 1” | The representatives from scan 299. |
| 307 | “par le lemme page 248” | The adjunction/localization lemma on scan 298. |
| 310 | “la prop. 19 et la définition” | Proposition 19 on scan 308 and the definition at the head of 309. |

## Remarks of the model

**R1 · Model remark · high confidence.** The two composites in the second fan are \(j_2\pi_1\) and \(j_1\pi_2\). Their sources and targets both agree with those of \(\pi_0\). Once the two \(j\)’s lie in \(W\), two-out-of-three makes the membership tests on all three \(\pi\)’s agree. This checks the indexing of that step in C19. It leaves the separate assertion about the \(j\)’s as a hypothesis of the check.

**R2 · Model remark · high confidence for the finite-set example.** The failure of the converse in B already occurs for a pullback of sets with bijections as \(W\). Take both legs to be the inclusion \(\{0\}\hookrightarrow\{0,1\}\). Their pullback is \(\{(0,0)\}\), so its projection to either copy of \(\{0\}\) is bijective. Neither original inclusion is surjective. The example checks the direction of the implication in that specialization.
