# Mathematical notes on scans 309–324

Alexander Grothendieck, *Les Dérivateurs*, cote 157-5, manuscript pp. 225–240, undated. Scan numbers below refer to the supplied images. The expression $i'\backslash I$ denotes the manuscript's category of pairs $(i,u'\colon i'\to f(i))$. The author writes “grde devant $\pi$” and uses cofinality of the diagonals $I\to I^A$ for $\operatorname{card}A\leq\pi$.

## What the pages do

**M01 · Scan 309.** The second part of a proposition introduces conditions on a functor $f\colon I\to I'$ and an infinite cardinal $\pi$. The circled $\mathrm F3_\pi$ asks for a single $j$ and arrows $v,w_\alpha$ with $f(v)u'_\alpha=f(w_\alpha)$ for a family of cardinality at most $\pi$. The implication diagram includes cancelled branches. An insertion adds the case of ordered $I$ beside that of faithful $f$.

**M02 · Scans 309–311.** For the particular functor of manuscript p. 223, Grothendieck reduces the desired cofinality and largeness assertion to $\mathrm F1$ and $\mathrm F3_\pi$. He spells them out in components indexed by $j\in\operatorname{Ob}J$. In the second construction the composites through $G(j)$ and $H(j)$ must come from the displayed $w_\alpha\colon F_\alpha\to H$. He underlines the word “foncteur” immediately above that display.

**M03 · Scans 311–312.** Corollary 4.9.6.5 gives cofinality of a product of cofinal functors whose source categories are filtered. Its displayed identification expresses the comma category of a tuple $i'=(i'_\alpha)$ as the product of the component comma categories. The sentence concluding that the product is filtered and hence $0$-connected crosses the page break.

**M04 · Scan 312.** Corollary 4.9.6.6 applies the preceding result to the diagonals $I_\alpha\to I_\alpha^B$. Their product is the diagonal for $\prod I_\alpha$. This gives closure of the property “grde devant $\pi$” under products.

**M05 · Scans 312–313.** Part 1 of the proof of 4.9.6.3 starts with $a\Rightarrow b$. To show that $i'\backslash I$ is filtered, he constructs a common upper object, then equalises a pair of arrows on the right. The sideways “Court-circuit” on scan 312 proposes using connectedness and local filteredness of the coétale category over $I$.

**M06 · Scans 313–316.** In $b'\Rightarrow a$, filteredness of the comma categories first yields cofinality. A square in $I$ is completed provisionally up to equality after applying $f$. The remaining parallel arrows are dealt with by right equalisation. The proof temporarily assumes $\mathrm F3$ on scan 315 and recovers it on scan 316 by taking a common upper object of two objects in $f(i_0)\backslash I$. The conclusion is $a\Leftrightarrow b\Leftrightarrow b'$.

**M07 · Scans 316–318.** For $a\Rightarrow c$, condition $\mathrm F2$ makes two candidate arrows agree after a further map. For the return implication under faithfulness, two successive applications of $\mathrm F3$ supply a common upper object in the comma category. Faithfulness is invoked explicitly at the step from $f(wu_1)=f(wu_2)$ to $wu_1=wu_2$.

**M08 · Scans 318–319.** Without the faithfulness hypothesis, Grothendieck introduces the circled $b''$. The comma categories satisfy $\mathrm{PF}1'$ and $f$ is cofinal. He displays $(a\Leftrightarrow b\Leftrightarrow b')\Rightarrow(b''\Leftrightarrow c)$. The two postcomposites have “$=$ image dans $I'$”. He also identifies the ordered case, in which the condition on parallel arrows of $I$ holds automatically.

**M09 · Scan 320.** The identity functor on a category with objects $\mathbb N$ tests the $\mathrm{PF}2$ hypothesis on $I'$. There are two signs for each strictly increasing pair and composition multiplies signs. Grothendieck describes the categories $i\backslash I$ as ordered and filtered, while the category $I$ itself fails the parallel-arrow condition.

**M10 · Scan 320.** Observation 3 takes $I'=e$. In this case $b''$ amounts to pseudofilteredness of $I$. The example shows what can fail in the implication from $c$ to $a$ when $f$ need not be faithful.

**M11 · Scan 321.** Part 2 starts with $a_\pi\Rightarrow b_\pi$. The square of $f$, $f^A$ and the two diagonals transfers the cofinality condition to $I'$. The other assertion about $i'\backslash I$ is referred to Lemma 4.9.6.9.1.

**M12 · Scans 321–323.** Lemma 4.9.6.9.1 says that a $0$-connected category coétale over a filtered category, or one “grde devant $\pi$”, has the corresponding property. For the cardinal case the projection identifies the categories under corresponding objects. An equalising arrow in the base lifts along the coétale functor, whose faithfulness is used on scan 323.

**M13 · Scans 321–322.** Corollary 4.9.6.9.2 supplies the criterion used in the lemma. It combines $0$-connectedness, bounded right equalisation, and a common extension for a bounded family of arrows with fixed source. In the converse direction Grothendieck chooses one $x_0$, joins it and each $x_\alpha$ to a $y_\alpha$, and applies the fixed-source condition.

**M14 · Scan 323.** The cancelled Corollary 4.9.6.9.3 proposes testing largeness by $0$-connectedness of $I$ and largeness of every $i\backslash I$. Its crossed argument reaches “reste à vérifier $\mathrm{PF}_\pi2$ pour $I$”. The oblique “Faux déjà dans le cas filtrant sans plus” refers back to p. 236. The ordinary implication tested there (M14F) asserts that connectedness of the base and filteredness of every undercategory imply filteredness of the base.

**M15 · Scans 323–324.** For $b_\pi\Rightarrow a_\pi$ the author refers the two remaining conditions to the argument on manuscript pp. 231–232, “mutatis mutandis”. For $a_\pi\Rightarrow c_\pi$ he chooses separate lifts $v_\alpha^0,w_\alpha^0$ and maps $\lambda_\alpha$ with common composite $\lambda_\alpha v_\alpha^0=\lambda$. The sheet ends as he states the next obligation concerning $\mathrm{PF}1'_\pi$ in the comma categories.

## Statements left without proof

| ID | Scan | Words on the sheet | Status here |
|---|---|---|---|
| U01 | 309 | “La condition $\mathrm F3_\pi$ est … satisfaite si $f$ est pleinement fidèle.” | The margin states this directly. The adverb in the transcription is doubtful. |
| U02 | 309–311 | “On voudrait établir que $I$ l'est et que $f$ est cofinal” and “Pour prouver 4.9.3, nous sommes donc ramenés à prouver…” | The specialised $\mathrm F1$ and $\mathrm F3_\pi$ verifications for the functor of p. 223 are formulated here. |
| U03 | 310 | “en fait, il suffit de vérifier $\mathrm F3$ (cf plus bas 4.9.7.1)” | The margin refers the reduction to a singleton to a later location. |
| U04 | 311–312 | “leur produit est filtrant (cf. 4.9.6.2)” and “On sait déjà que a) implique que $I'$ est filtrante” | These are inputs to the product argument and to Part 1 respectively. The latter carries an SGA reference. |
| U05 | 321 | “Le cas filtrant est déjà connu (cf II, …).” | The ordinary filtered case of the coétale lemma is taken from an earlier discussion. |
| U06 | 324 | “s'applique mutatis mutandis” and “Il faut prouver que si $c_\pi$ est satisfait…” | The bounded reverse implication invokes the earlier proof. The final assertion about the comma categories is stated at the lower edge of the last supplied sheet. |

## Questions and conjectures

- **Scans 309–311.** “On voudrait établir” introduces the goal for the functor of p. 223. Scan 311 identifies the two verifications still needed there (U02).
- **Scans 312–313.** “On aurait fini si on savait que” isolates an equality between two composites. The next page applies $\mathrm F2$ and changes their common target.
- **Scans 315–316.** “Admettons pour un instant la condition $\mathrm F3$” is a provisional assumption. Scan 316 explicitly returns to it with “il reste à prouver que $b')$ implique la condition $\mathrm F3$”.
- **Scans 317–318.** The marks “$v_1?$” and “$v_2?$” belong to the proposed lifts in the sketch. The prose obtains the lifts successively.
- **Scans 323–324.** The author rejects the crossed corollary with “Faux déjà…”. The live question at the end of the sequence is the verification quoted in U06. No separate conjecture is labelled on these sheets.

## Slips

Suggested forms are editorial. Low confidence applies to every suggestion resting on a doubtful, cancelled or overwritten reading. The local evidence for each entry is also recorded in the doubts register.

| ID | Scan | Frozen reading | Suggested form and reason | Confidence |
|---|---:|---|---|---|
| S01 | 309 | $f(i'_\alpha)$, with unprimed $i$ also possible | $f(i_\alpha)$ agrees with the family and with the sketch. | Low |
| S02 | 310 | First live $\underline{\mathrm{Hom}}(C,J)$ | $\underline{\mathrm{Hom}}(J,C)$ fits the explicit $F\colon J\to C$ and the later order on the same sheet. | Medium |
| S03 | 313 | $f(w')$ in the diagram and $f(w')v'$ | $f(w)$ and $f(w)v'$. Both the upper arrow and the prose name $w$. | Medium |
| S04 | 313 | $f(ww_1)v'$ beneath the right bracket | Possibly $f(ww_2)v'$, from the preceding pair $w_1,w_2$. The surrounding labels also vary. | Low |
| S05 | 314 | $e_1u_1$ or $v_1u_1$ in the last equality | $v_1u_1$ agrees with the product immediately above. The lower initial has a closed loop. | Low |
| S06 | 315 | $f(w)v'=f(w)$, with $v$ possible at the first $w$ | $f(v)v'=f(w)$ has the sources of the two chosen arrows. | Low |
| S07 | 315 | $\zeta_1=(i_0,v')$, possibly $i_1$ | $(i_1,v')$ is the target of the displayed parallel pair. | Low |
| S08 | 316 | $\mathrm{id}_{j_0}$ or $\mathrm{id}_{i_0}$ | $\mathrm{id}_{f(i_0)}$ is the identity of the object named in the preceding pair. | Low |
| S09 | 316 | $f(w)=f(w)u'$, possibly $f(v)u'$ on the right | $f(v)u'$ repeats the term in the preceding equality. | Low |
| S10 | 317 | $\bar v=\alpha w$, possibly $\alpha v$ | $\bar v=\alpha v$ agrees with the neighbouring underbrace. | Low |
| S11 | 317 | “b) implique”, also possibly “c) implique” | The implication immediately above starts at $c$. | Low |
| S12 | 319 | The five-condition list ends $c')$ | $b'')$ would recover the condition circled at the top and paired with $c$ in the display. | Medium |
| S13 | 321 | 4.9.8.5 or 4.9.6.5 | 4.9.6.5 is the product corollary on scan 311. | Low |
| S14 | 323 | $g(vu_\alpha)=g(wu_\beta)$, possibly $v$ on the right | $g(vu_\beta)$ uses the lift in $J$. The author has just put $g(v)=w$ in $I$. | Low |
| S15 | 324 | $\mathrm{FB}_\pi$, also possibly $\mathrm F3_\pi$ | $\mathrm F3_\pi$ fits the bounded lifting assertion being constructed. | Low |
| S16 | 324 | $f(v_\alpha)u'_\alpha=f(w_\alpha)$ | With the names introduced on the preceding line, the two lifts carry superscript $0$. | Medium |
| S17 | 324 | $f(w_\alpha)u'_\alpha$ within the bracket, possibly $f(v_\alpha)u'_\alpha$ | $f(v_\alpha^0)u'_\alpha$ agrees with the short equation and the chosen lifts. | Low |
| S18 | 324 | $h$ in the existence sentence and $j$ in the conclusion | A uniform target $h$ or $j$ would type the final arrows. The overwritten sketch leaves the intended letter open. | Low |

## Pointers

| Scan | Wording or reference | Location indicated |
|---:|---|---|
| 309–310 | “(p. 223)” and “du cas p. 223” | The functor to which 4.9.6.4 is applied. |
| 309 | Slanted note ending “page 227” | The section number beside it is read doubtfully as 4.9.6.7. Manuscript p. 227 is scan 311. The live 4.9.6.7 heading is on scan 312. |
| 310–311 | “cf plus bas 4.9.7.1” and “sous l'une des deux conditions a) ou b) de 4.9.3” | The later singleton reduction and the two hypotheses of the original target. |
| 311–312 | “(de 4.9.6.3)”, “(cf. 4.9.6.2)”, “par le cor. 4.9.6.5” | The proposition, the filtered-product result, and its use for diagonals. |
| 312 | “SGA 4 I 8.1.3. b” | The cited assertion that $I'$ is filtered under condition $a$. |
| 321–322 | “cf II, …” and “(cf page 81)” | The known filtered case of the coétale lemma and the earlier cardinal criterion. |
| 323–324 | “page 236”, “pages 231-232”, “cf 4.9.6.9.2” | The sign example (scan 320), the earlier equalisation argument (scans 315–316), and the common-extension criterion (scans 321–322). |

## Remarks of the model

**R01 · Model, high confidence · Scan 320.** For the two arrows with signs $+1,-1$, postcomposition by $+1$ gives $(+1,-1)$ and postcomposition by $-1$ gives $(-1,+1)$. Both pairs have distinct entries. The undercategories are filtered, yet right equalisation is a separate requirement on the base. The calculation uses the manuscript's explicit words “multiplication des signes”.

**R02 · Model, high confidence · Scans 320, 323.** The page-236 example distinguishes ordinary filteredness from the cardinal-bounded issue in the cancelled corollary. In $i\backslash I$, take one arrow to each successive natural number beyond $i$. This countable family has no common upper target in $\mathbb N$. The marginal qualifier “dans le cas filtrant sans plus” therefore matters when citing this particular example.

**R03 · Model, low confidence about the intended notation · Scan 321, approximately lines 6–13.** The frozen lower diagonal is $\delta_{A'}$. A possible intended notation is $\delta'_A$. The square uses the same exponent $A$ on both sides, while the tick in the diagram and prose is visibly beside the lowered $A$. This is a reading question about the placement of that tick.

