# Mathematical notes · K157-5-17

## What the pages do

**Direct factors and cardinal bounds (261).** The page continues an argument already in progress. Lemma 4.7.9.1 gives closure under direct factors for \(\pi>\pi_0\). For an accessible filtration, Corollary 4.7.10 places \(M_\pi\) between \(\mathcal F^\pi\) and \(\mathcal F^{\pi^{\pi_0}}\). The equality case \(\pi=\pi^{\pi_0}\) plays a separate role. The oblique note questions closure at the initial cardinal.

**The comparison functor (261–263).** Section 4.7.11 considers the fully faithful extension of \(\mathcal F^\pi\subset M\) to \(\operatorname{Ind}_{\pi}(\mathcal F^\pi)\). Proposition 4.7.12 identifies essential surjectivity with a condition on every slice \(\mathcal F^\pi_{/F}\): it must be filtering and “grande devant \(\pi\).” The further equality \(\mathcal F^\pi=M_\pi\) is explicitly qualified by \(\pi>\pi_0\).

**Useful, superfluous and regular cardinals (263–264).** Definition 4.7.13 calls a cardinal *utile* when the comparison conditions hold, with the extra equality of the two categories required at \(\pi=\pi_0\). The other cardinals are *superflus*. Regularity for the given filtration requires usefulness and the cardinal estimate referred to as (4.7.7.1). The following paragraph singles out \(\pi^{\pi_0}=\pi\) and observes that usefulness of all the cardinals forces the filtration to be canonical.

**The associated canonical filtration (264–265).** Proposition 4.7.15 passes from the given accessible filtration to \((M_\pi)_{\pi\geq\pi_0}\) and retains usefulness and regularity where the original filtration had them. In 4.7.16 Grothendieck asks what is gained by passing to this filtration. He emphasizes its dependence on the initial cardinal and considers whether a canonical filtration of an ind-category can nevertheless have nonregular or superfluous cardinals.

**Raising the initial cardinal (266–268).** Proposition 4.7.17 restricts the family to \(\pi\geq\pi'_0\), where \(\pi'_0\geq\pi_0\). The restricted family is again an accessible filtration and it inherits canonicity. The same cardinals in this range are useful. For regularity the two cardinal estimates have different thresholds. The addition extending into the left margin gives \(2^\pi\geq\pi'_1\) as a condition for the converse, with the stronger sufficient hypothesis \(\pi\geq\pi'_1\).

**A bound on the new threshold (268).** Corollary 4.7.18 assumes regularity at the original initial cardinal and restricts at \(\pi'_0\geq\pi_1\). Formula (4.7.18.1) bounds \(\pi'_1\) by \(2^{((\pi'_0)^{\pi_0})}\) and then by \(2^{(2^{\pi'_0})}\). An addition supplies the conditions under which the preliminary inequality is automatic. The starred note at left refers to a later result about usefulness of \(\pi_0\).

**Reduced cardinalities and slices (268–270).** Lemma 4.7.19 bounds the reduced cardinal of \(\mathcal F^\pi\) for \(\pi\geq\pi_1\). It also bounds the reduced cardinal of a slice over \(F\in\operatorname{Ob}\mathcal F^{\pi'}\), with \(\pi'>\pi\). The respective right members are \(2^{(\pi^{\pi_0})}\) and \((\pi')^{(\pi^{\pi_0})}\). The proof sets \(C=\mathcal F^{\pi_0}=M_{\pi_0}\), passes to the ind-category description, and estimates \(\operatorname{Hom}(G,F)\), the objects of the slice and its arrows, in that order. The marginal variants are questions.

**Maximality (271).** Section 4.7.20 calls a canonical filtration *maximale*, also *strictement canonique*, if it was not obtained by restriction from a canonical filtration with a smaller initial cardinal. An existence and uniqueness statement closes the paragraph.

**Accessible categories and the meaning of strict generation (271–272).** Proposition 4.8.1 compares a stability and strict-generation condition, an ind-category presentation, and the existence of an accessible cardinal filtration with useful initial cardinal. Condition \(c'\) strengthens the last formulation by requiring regularity and canonicity. The margin gives \(c'\Leftrightarrow c\Leftrightarrow b\Rightarrow a\). Section 4.8.1.1 then turns to strict generation by a full subcategory. It relates a presentation by a canonical colimit to full faithfulness of \(M\to C^\wedge\).

**All arrows versus a chosen family (273–275).** Grothendieck reopens an objection to his earlier proof of \(a\Rightarrow b\). He distinguishes the family of all arrows from the subcategory to an object from the existence of one strictly epimorphic family. He asks what happens on adjoining more arrows, considers a condition on inverse images of sieves, and traces the consequences for enlarging a strictly generating subcategory. The next page records his change of view.

**The general functor (275–276).** Proposition 4.8.2 starts with \(i:C\to M\), constructs the restricted Hom functor \(\varphi:M\to C^\wedge\), and writes the canonical arrow from the colimit over \(C_{/X}\) to \(X\). Here \(a\) is the strict epimorphism condition on the whole family, \(b\) says the comparison arrow is an isomorphism, and \(c\) says \(\varphi\) is fully faithful. The diagram gives \(b\Leftrightarrow c\Rightarrow a\); the text says all three are equivalent if \(i\) is fully faithful. The bracketed NB uses \(b,c\) to define a strictly generating functor and applies the terminology to inclusion of a subcategory, which need not be full. Part 3° opens on the final line.

## Statements left without proof

- **261, direct factors.** “Si \(\pi>\pi_0\), … est stable par facteurs directs.” This is a named lemma used inside the surrounding proof. The preceding closure under certain colimits is mentioned; a separate proof of the lemma does not appear on the sheet.
- **268, starred marginal addition.** “Il suffit pour cela que \(\pi_0\) soit utile … cela implique régulier, cf 4.8.5.” The cited passage falls after this group.
- **271, strict canonicity.** “elle admet même une fcg str. canonique, et cette dernière est de plus unique.” The next sentence is “On va revenir là-dessus dans la section suivante.”
- **271–272, Proposition 4.8.1.** “On a alors le diagramme d’implications” introduces the four-condition diagram. The pages continue by discussing strict generation. They do not give separate proofs of every arrow of that diagram.
- **275–276, Proposition 4.8.2.** “On a alors les implications” and “si on suppose \(i\) pl. fidèle, alors les trois conditions … sont équivalentes.” The statement and terminology are present. A full proof of the general-functor statement does not occur before 3° starts.

## Questions and conjectures

- **261, opening of 4.7.11; 264–265, 4.7.16.** “Il me semble” qualifies first the usefulness of accessible filtrations and later the judgment that the associated canonical filtration is “meilleure.” The oblique note on 261 treats the behavior at \(\pi_0\) separately.
- **265, canonical filtrations on ind-categories.** “Je présume … (sans avoir cependant construit d’exemple)” introduces the possibility of nonregular and even superfluous cardinals for \(M=\operatorname{Ind}_{\pi_0}(C)\), with \(C\) small and Karoubian.
- **268–269, strength of the estimates.** “J’ignore si on peut … dans ces majorations” asks whether \(\pi\) can replace \(\pi^{\pi_0}\). The next page says “Il faudrait quand = s’assurer sur un exemple … dans le cas général.” Both notes concern the possible improvement, and several intervening words are uncertain.
- **273–275, strict epimorphic families.** “Mais peut-être l’annotation résulte-t-elle d’une confusion” concerns \(a\) and \(a'\). On 274 he considers cases where \(a'\) holds without \(a\), and on 275 says “il me faudrait donner un exemple.” He then writes “Finalement, réflexion faite, ces ennuis … disparaissent.” The separation and proposed example belong to this sequence of reconsideration.

## Slips

| Scan | Frozen reading | Apparent correction and reason |
|---|---|---|
| 269, immediately before the pair of estimates | (4.7.9.1) and (4.7.9.2) | **High.** The two estimates under proof bear (4.7.19.1) and (4.7.19.2) on 268. The digit 1 before 9 would restore both references. |
| 269, upper braced display | \(M_{\pi/F}\) followed by \(F'\in\operatorname{Ob}M_{\pi'}\) | **Low.** Using \(F\) for both would agree with the later restatement on this page. A nearby long vertical stroke makes the first reading vulnerable. |
| 269, line after *résulte en effet de* | Possible \(2^{\pi_0}\) on the right | **Low.** The next calculation ends with \(2^\pi\), which suggests π as the exponent. The small stroke read as 0 is uncertain. |
| 275, (4.8.2.1) | A single closing parenthesis after the final \(X\) | **Low.** If the left parenthesis before \(x\) introduces the entire assignment, a second closing parenthesis would complete it. The grouping is more certain at the right than at the left. |

## Pointers

| Scans | Wording or reference as it stands | Use here |
|---|---|---|
| 261–264 | “en vertu de (4.7.9.1)”; “comme (4.7.9.1)”; “cf 4.7.7” | The fixed-point case, the direct-factor argument, and the earlier conditions defining a filtration. |
| 262–263 | “résulte aussitôt de 4.4.” followed by an uncertain digit; “(p. 81)”; “(4.7.7.1)” | Equivalence of the comparison conditions and the earlier cardinal bound. |
| 265 | “au sens de SGA 4” with an uncertain continuation after I; “au sens SGA” | The older sense of *filtration cardinale*. |
| 268 | “cf 4.8.5”; “cf. remarque 4.7.7.2” | Initial usefulness and the automatic threshold, respectively. |
| 269–270 | “(4.7.6.2)”; “la … que celle prouvée dans 4.5.” followed by an uncertain number | The Filt size condition and an earlier proof of a similar estimate. Several further numerals in the oblique comparison on 269 are doubtful. |
| 272–273 | “SGA 4 I 7.2, (i)”; “la démonstration donnée dans loc. cit”; “cf SGA 4 I 10.3” | Strict generation, the author's re-examination of the old implication, and strictly epimorphic families. |
| 275–276 | “(4.8.2.1)” and “4.8.2.2.” | The comparison functor and its canonical colimit arrow are cited on the immediately following page. |

## Remarks of the model

- **R1 · model remark · high confidence (266).** In the displayed sandwich \(\pi\leq\pi^{\pi_0}\leq\pi^{\pi'_0}\), the equality assumed immediately above identifies the two endpoints. The inference to the old fixed-point condition uses just that ordering. I checked this local inference.
- **R2 · model remark · high confidence (266–267).** The direction of the first threshold implication on 267 agrees with the order \(\pi'_1\geq\pi_1\) at the foot of 266. Replacing the threshold by the smaller one is the direction used in the proof. I checked the ordering step, taking the stated comparison of thresholds as a premise.
- **R3 · model remark · high confidence (276).** The unconditional diagram alone permits \(a\) true with \(b,c\) both false. The text’s subsequent full-faithfulness hypothesis is where the reverse implication is asserted. This is a check on the logical content of the diagram; a categorical example realizing that truth assignment is a different question.

Source for all six sections: Grothendieck, A. (s.d.). *Dérivateurs* [Manuscript, cote 157-5, manuscript pp. 177–192, supplied scans 261–276]. Montpellier archive.
