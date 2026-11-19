# Mathematical notes on scans 149–164

## What the pages do

**149–150 · Proposition-perplexité 4.3.1.** Given pseudo-toposes \(M,N\) with small strictly generating subcategories \(S,T\), the author considers the inclusion of \(M\boxtimes N\) in presheaves on \(S\times T\). Condition b) asks for representability of evaluation at every pair of objects. Condition b′) asks for the same on \(S,T\). Condition c) asks for a left adjoint; a) says that \(M\boxtimes N\) is a pseudo-topos. The displayed implications are \(b\Rightarrow b'\Leftrightarrow c\Rightarrow a\). The author also identifies the generators obtained by applying the adjoint to pairs \((s,t)\).

**150–151 · Lemma 4.3.2.** To test whether a functor \(\alpha\) into \(X^\wedge\) has a left adjoint, the author tests representability of evaluation at each \(x\) in the small category \(X\). For sufficiency, he writes a presheaf \(F\) as a colimit of objects \(F_i\) of \(X\), and displays the resulting Hom calculation.

**151–152 · Lemma 4.3.3 and conclusion of 4.3.1.** For a fully faithful functor with left adjoint \(\rho\), the lemma computes colimits by applying \(\rho\) to colimits in the larger category. Its added part b) sends a small strictly generating part to one in the smaller category. The proof of b) runs diagonally down the margin of 152. The main text applies the lemma to \(M\boxtimes N\). The last live Hom calculation identifies evaluation at \((s,t)\) by adjunction. A separate, cancelled attempt to obtain \(a\Rightarrow c\) ends at “qui”.

**153–154 · Proposition 4.3.4 and Corollary 4.3.5.** Proposition 4.3.4 characterises a \(U\)-pseudo-topos by a fully faithful embedding into \(S^\wedge\), for \(S\) small, admitting a left adjoint. Corollary 4.3.5 gives the accessible version, with an accessible embedding. The proof on 154 relates accessibility of that functor to accessibility of the objects of \(\rho(S)\), then invokes strict generation.

**154–155 · Theorem 4.3.6.** The conditions concern small colimits and strict generators consisting of accessible objects, accessibility of every object, an accessible fully faithful embedding with a left adjoint, a cardinal filtration, and a presentation by an \(\operatorname{Ind}_{\pi_0}\) category. The author names the first group of conditions “PTA”. A long manuscript arrow moves the filtration clause c) ahead of the Ind clause d). The proof announces \(\mathrm{PTA}\Rightarrow c\Rightarrow d\Rightarrow\mathrm{PTA}\).

**156–157 · Two filtrations.** In (4.3.6.2), \(x\) is written as a colimit over \(S_{/x}\). The first filtration bounds the cardinality of the arrows of \(S_{/x}\). The primed filtration asks for a strict epimorphic family from objects in \(S\) of cardinal at most \(\pi\). The displayed inclusions put the primed term between the unprimed terms at \(\pi\) and \(\pi^{\pi_0}\). For \(\pi=\pi^{\pi_0}\) the two terms coincide. The text questions how much of the earlier stability proof survives under the present hypotheses.

**158–159 · Smallness and stability.** Condition a) is attributed to the presentation by small diagrams in \(S\). For b), the author forms a category \(J\) over the indexing category \(I\). Its fibre over \(i\) is isomorphic to \(S_{/x_i}\). The estimates on fibres and arrows bound the cardinal of \(J\). Giving the colimit a presentation indexed by \(J\) first puts it in the primed filtration. The next argument uses accessibility of the objects of \(S\), with \(I\) large relative to \(\pi_0\), to bound the arrows of \(S_{/x}\).

**160–161 · The filtration and the Ind presentation.** Formula (4.3.6.5) presents an object of the term at \(\pi'\) by objects of the term at \(\pi\), with \(I\) large relative to \(\pi\) and \(\operatorname{Card} I\leq(\pi')^\pi\). The marginal notes question whether the proposed \(I\) has the required largeness. For \(c\Rightarrow d\) the author takes \(\pi_1=2^c\), identifies a filtration term with the \(\pi_1\)-accessible objects, and invokes the equivalence \(\operatorname{Ind}_{\pi_1}(M_{\pi_1})\to M\). For \(d\Rightarrow\mathrm{PTA}\), small colimits are the remaining issue.

**161–162 · Lemma 4.3.7.** Starting with \(M_\pi\) admitting colimits of cardinal at most \(\pi\), the lemma asserts that its \(\operatorname{Ind}_{\pi}\) category has small colimits. It also states a universal property: restriction gives the displayed equivalence between categories of functors preserving the respective colimits. The proof first compares the given colimits with those in the Ind category. The two-row Hom calculation interchanges a colimit over \(J\) and a limit over \(I\). A new argument for representability of small colimits breaks off in cancelled lines.

**163–164 · Section 4.4 and Proposition 4.4.2.** The author returns to the difficulty with Lemma 4.3.7. For an ind-representable \(F\) and a filtered diagram \(i\mapsto x_i\), a map from its colimit to \(F\) gives a factorisation functor \(\varphi_\alpha:I\to C_{/F}\). Proposition 4.4.2 characterises invertibility of \(\alpha\) by cofinality of \(\varphi_\alpha\). The two written conditions express the existence of a map from each test object and eventual equalisation of a parallel pair. F2) continues at the top of scan 164. The converse argument invokes the pointwise filtered-colimit calculation in sets.

**164 · Corollary 4.4.3.** The corollary characterises membership in the essential image of \(\operatorname{Ind}_\pi(C)\) by a cofinal functor \(I\to C_{/F}\) from an ordered category large relative to \(\pi\). The superscript denoting that essential image is hard to read. The final paragraph asks for a condition on \(J=C_{/F}\) ensuring the existence of such a functor \(I\to J\).

## Statements left without proof

| Scan | Author’s words | Status in these sheets |
| --- | --- | --- |
| 155, left margin | “Pour une démonstration complète … cf § 4.6” | The author directs the reader elsewhere for the complete proof of 4.3.6. |
| 156–157 | “C'est prouvé dans loc. cit. 9.13. sous des … hypothèses légèrement différentes”; “dans loc. cit on prouve que” | The earlier result and the cardinal bound for the primed filtration are invoked from that text. The omitted word in the first quotation is a manuscript deletion. |
| 158, left margin | “je ne le prouve que dans ce cas, hélas !” | The closure proof here uses a filtering \(I\) large relative to \(\pi_0\). |
| 160, left margin | “Il n'est pas sûr que \(I\) soit grand devant \(\pi\)” | The proposed indexing category in (4.3.6.5) lacks a settled largeness argument in the generality announced. |
| 161–163 | “est solution d'un problème 2-universel”; “il reste à voir”; “la démonstration du lemme 4.3.7 n'est pas tellement évidente” | The calculation on 162 addresses preservation of existing colimits. These sheets do not finish a proof of the full lemma or its restriction equivalence. |
| 164 | “La vérification est … tautologique” | The author gives the Hom formula and invokes the “calcul” in sets, leaving the details of the two conditions to the reader. The formula and the ± sign are present in the transcription. |

## Questions and conjectures

- **149–150.** The dashed return map in (4.3.1.1) bears a question mark. In the NB the author says “Je ne connais pas d'exemple où … les conditions envisagées ne soient satisfaites, mais doute pourtant à présent que même la plus faible le soit toujours”. He asks in particular whether the product of two pseudo-toposes is always a pseudo-topos.
- **152.** The cancelled words “Reste à prouver \(a\Longrightarrow c\)” introduce a stronger converse. The passage is unfinished.
- **157.** “Les deux filtrations ont l'air \(\pm\) équivalentes.” The author says the earlier demonstration “semble vraiment faire appel de façon essentielle” to universality of strict epimorphic families.
- **160.** “Sauf si on suppose \(\pi^{\pi_0}=\pi\) !” qualifies the assertion that \(I\) is large relative to \(\pi\).
- **163–164.** “Finalement, la démonstration du lemme 4.3.7 n'est pas tellement évidente que je l'anticipais.” On the last sheet the remaining problem is introduced by “nous faut donc donner une condition” on \(J\).

## Slips

| Scan | Frozen reading | Apparent correction and reason |
| --- | --- | --- |
| 149–150 | Two displays labelled (4.3.1.4) | They are different formulas, one computing the presheaf of a pair, the other identifying its image by the adjoint. Separate labels would remove the ambiguity. A specific replacement numeral cannot be recovered. |
| 155 | \(a'\Rightarrow a\Rightarrow b\Rightarrow a\), followed by the assertion of equivalence | An implication back to \(a'\) is needed to establish the three-way equivalence from the chain alone. Which displayed link was intended to do that is uncertain. See remark M1. |
| 156–157 | Both definitions are numbered (4.3.6.3) | A prime distinguishes the filtrations in the text. Distinct display labels would distinguish the references. No replacement number is visible. |
| 161 | The short subscript inside the later \(\operatorname{Ind}_{\pi_1}\) reads \(1\) or \(\pi_1\) | Possibly \(M_{\pi_1}\), as in the preceding formula. Low confidence. The ink does not settle whether a π is present. |
| 162 | “\(\operatorname{Ind}_\pi(M_\pi)\) est stable dans \(M_\pi\) pour ces limites” | The apparent ambient category is \(\operatorname{Ind}(M_\pi)\), where the previous sentence locates those colimits. The original wording is retained. |

## Pointers

| Scan | Reference as it appears | Use on the sheet |
| --- | --- | --- |
| 149 | “comme dans 4.1” | Construction of \(M\boxtimes N\). |
| 150–154 | “du Lemme 4.3.2”; “b) du dit lemme”; “la formule (4.3.1.4)”; “du lemme 4.3.3”; “comme dans 4.3.4. … b)” | Links among the evaluation test, the colimit calculation and the embedding statements. |
| 154 | “Cf SGA 4 I 9.9.” | Accessibility argument after Corollary 4.3.5. |
| 155 | “cf § 4.6” followed by 139–148 | More complete proof. The abbreviation before the page range admits p or pp. |
| 156 | “cf SGA 4 I” followed by a doubtful 7.2 and a subdivision; “SGA 4 I 9.12”; “loc. cit. 9.13.” | Colimit over \(S_{/x}\), the filtration conditions, and an earlier proof with different hypotheses. |
| 157–159 | “dans loc. cit on prouve”; “SGA 4 I 9.13”; “SGA 4 I 9.12”; “condition b) de loc. cit.” | Comparison of the filtrations and stability. Two of the explicit references occur in cancellations. The marginal “explicitée dans” on 159 ends without a destination. |
| 160 | “loc. cit. (p. …–152)”; “loc. cit 9.16”; “en vertu de loc cit. 9.9. (p… 145)” | Construction of the index, accessible objects and their closure. The first page of the range could be 151 or 159. A crossed argument also cites an uncertain “9.6 (iii)”. |
| 161 | “9.18. b)” and “9.18 a)”, both with “(p. 156)” inserted | The Ind equivalence, then accessibility of the named objects. Part of the second reference is overwritten. |
| 162 | “SGA 4 I 9.8”; “SGA 4 I 8.9.5 b…” | Interchange of limits in the central calculation, then representability of colimits in the ordinary Ind category. The closing punctuation of the second citation is unclear. |
| 163–164 | “lemme 4.3.7”; “(4.4.2.1)”; “F1) et F2)” | Return to the unfinished lemma, then the map and the conditions used in the cofinality argument. |

## Remarks of the model

**M1 · Scan 155 · High confidence.** The displayed arrows alone allow \(a\) and \(b\) to hold without \(a'\). This observation concerns the written implication chain. The accessibility argument on 154 gives separate context for the author’s claim of equivalence.

**M2 · Scans 157 and 160 · High confidence with the stated cardinal assumptions.** For infinite \(c\) with \(0<\pi_0\leq c\), the example \(\pi=2^c\) does satisfy \(\pi^{\pi_0}=\pi\). This checks the cardinal example. The existence of the required indexing category in (4.3.6.5) remains a separate issue in the manuscript.

**M3 · Scans 157–159 · High confidence.** The first conclusion on 159, membership in the primed filtration, gives membership in the unprimed one at \(\pi^{\pi_0}\) by the inclusions on 157. At a fixed point of that exponent the two bounds coincide. This accounts for the qualification in the bracket on 159.

## Reading questions

| Scan and line | Frozen reading | Other reading and reason |
| --- | --- | --- |
| 150, 20–21; 151, 4–8 | The test-object letter is ζ or ξ. The adjoint later reads ρ or φ. | The same roles recur in the displayed adjunctions. The role alone cannot choose the form of a handwritten letter. |
| 160, 1–5, left margin | “Démonstration concluante” or “conclut”, followed by “en vérité” or “en réalité” | The endings are reduced even after rotation. The final cardinal equality is much clearer than the qualification that introduces it. |
| 161, 15–19 | \(M=\operatorname{Ind}_\pi C\), with \(M_\pi\) an alternative to \(C\) | \(M_\pi\) would match the hypothesis of this lemma. The visible open stroke looks like C and is not settled by the formula above. |
| 163, 20–21 | ψ, + or r below the canonical arrow | The fork resembles ψ in the earlier diagram. The labels in the next proof give that reading some support. |
| 164, 4–7 and 18–19 | The first limit has a hatched letter before \(\varphi_\alpha\); the raised mark on Ind reads + or a prime. | The crossed letter could be ψ or φ. The prime would match the preceding sheet, while the stroke on this sheet looks crossed. Neither observation supports a change of convention. |
