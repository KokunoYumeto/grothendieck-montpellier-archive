# Mathematical notes on scans 85–100

## What the pages do

**End of 4.1 and 4.2, scans 85–86.** The opening finishes an argument relating the factorisation axiom $\mathrm{Cof}_3$ to the earlier condition (4.4), assuming stability of $W$ under direct factors for the converse. Starting with a small $C_0$, the author takes its closure under change of base and transfinite composition, with the option of taking direct factors as well. The remaining issue is stability of $C\cap W$ under change of base. His sufficient condition passes through $C\subset\mathrm{Cof}_W$ and $C\cap W=C\cap W^{\mathrm{univ}}$.

**4.3, scan 86.** To put a structure on $M(I)$, he starts with the discrete category $I_0$ on the objects of $I$. The canonical functor $u_I:I_0\to I$ gives the adjoints $u_!$ and $u^*$ between the product category $M(I_0)$ and $M(I)$.

**Definition 4.4, scan 87.** A special cofibration structure consists of $(M,W,C)$ with conditions on small inductive limits and accessibility, saturation of $W$, stability of $C$ and $\mathrm{TC}=C\cap W$, a small generating part of $C$, and $\mathrm{TF}=C_*\subset W$. The qualifier on saturation is abbreviated and uncertain. A cancelled occurrence of *transfinies* in b) and a separate b′) distinguish the condition on transfinite compositions. This definition is on manuscript page 74.

**4.5 and Lemma 4.5.2, scans 87–90.** For an adjunction $M\rightleftarrows M'$, he defines $W'$ by inverse image under $u^*$ and $C'$ by closing $u_!(C)$ under change of base and transfinite composition. A cocartesian square motivates the hypotheses $u^*u_!(C)\subset C$ and commutation of $u^*$ with small inductive limits. He then controls the images of $C'$ and $\mathrm{TC}'$ and treats the tilded variants when $C=\widetilde C$. The proposed small generating part is $u_!(C_0)$.

**Lemma 4.5.3 and Proposition 4.6, scans 90–92.** The lemma identifies $\mathrm{TF}'$ with the inverse image of $\mathrm{TF}$ under the right adjoint. The proposition collects the hypotheses on $M'$ and the adjunction and gives a special cofibration structure $(M',W',C')$. It also discusses replacing $C'$ by $\widetilde C'$. The text places a direct-factor hypothesis on $C$ near this second assertion. A long marginal note questions the need for it.

**The relations (4.7.1)–(4.7.6), scans 92–94.** The author seeks bounds on $\mathrm{TC}'$ and $\mathrm T\widetilde C'$ in terms of $u_!(\mathrm{TC})$. He proposes $u^*u_!(\mathrm{TC})\subset\mathrm{TC}$ for the first bound. For the other direction he introduces $F=(\mathrm{TC})_*$, $F'=(\mathrm{TC}')_*$ and $F'_{\sim}=(\mathrm T\widetilde C')_*$. He distinguishes $F'_{\sim}=F'$, to which he returns, from the further equality $F'=(u^*)^{-1}(F)$, for which he lacks a proof here.

**Proposition 4.8, scans 94–96.** For $I_0$ he takes the product structure, defined “fibre à fibre.” On $M(I)$ the weak equivalences are detected by restriction, while $C(I)$ is generated from $u_!(C(I_0))$ by change of base and transfinite composition. He identifies $\mathrm{TF}(I)$ by inverse image and gives inclusions for $\mathrm{TC}(I)$ and $F(I)$. The calculation on scan 96 writes $u_!(F_0)(i)$ as a sum over $j$, with copies of $F_0(j)$ indexed by $\operatorname{Hom}_I(i,j)$. The curved arrow from the following equality points back to that sum.

**Section 5 and Proposition 5.1, scans 97–99.** He introduces $\mathrm{TF}=C_*$, $\mathrm{TC}=C\cap W$ and $F=(\mathrm{TC})_*$, then puts $\mathrm T\widetilde C=\widetilde C\cap W$. He asserts that each element of $\mathrm T\widetilde C$ is a direct factor of an element of $\mathrm{TC}$. A marginal definition identifies the small opposing-arrow exponent with taking direct factors. The proposition compares the left Q-closures and the associated right classes. In passing to $(M,W,\widetilde C)$ he invokes direct factors for base change and transfinite composition for b′). The lower margin on scan 97 distinguishes the equalities in (5.6) from the conclusions that require assumptions on $W$.

**Proposition 5.2 and Corollary 5.3, scan 100.** The two formulas are $W=\mathrm{TF}\circ\mathrm{TC}$ and $\mathrm{TF}=F\cap W$. The proof factors a map in $W$ and then uses the return map $r$ in the argument for the second formula. The corollary asks when $(W,C,F)$ gives a Quillen triple. Its criterion is factorisation for $(\mathrm{TC},F)$. It gives stability of $C$ under direct factors as the further closure criterion.

## Statements left without proof

| Scan | His words | Scope on these sheets |
| --- | --- | --- |
| 85–86 | “alors l'axiome de factorisation … est satisfait”; “la stabilité de $W$ … assure alors qu'on a également” | The first argument begins before scan 85. The passage from (4.6) to (4.7) is asserted. |
| 87 | “ce qui implique … l'axiome de factorisation” | The definition refers the reader to the earlier hypotheses and to page 39. |
| 88–90 | “étant Q-close à gauche”; “Par c) plus bas”; “On voit alors que” | The author uses stability properties of the Q-closure and the description by direct factors. For the generating set he gives the closure argument briefly. |
| 91 | “C'est formel”; “de l'adjonction de $u_!,u^*$” | This is the reason given for Lemma 4.5.3. The lifting-square calculation is implicit. |
| 94 | “on montre assez facilement qu'on a”; “cf prop. 5.1 ci-dessous” | The equality $F'_{\sim}=F'$ is deferred to the general cofibration result. |
| 95–96 | “On sait déjà”; “Il est clair aussi”; “un lemme général” | The proof uses colimits and accessibility in $M(I)$. The transition from finite to arbitrary sums receives a marginal request for a general lemma. |
| 97 | “On sait alors … que” | The description of $\widetilde C$ by direct factors of elements of $C$ is accompanied by an earlier reference. |
| 100 | “il f. et il suffit” | Corollary 5.3 follows the proof of Proposition 5.2 without a separate demonstration on this sheet. |

## Questions and conjectures

- **85–86.** “Il me semble que ces conditions, en pratique, ne seront guère jamais vérifiées” qualifies the opening discussion. He calls the base-change requirement “une condition délicate.” On scan 86 he inserts “(je crois)” in the sentence about dispensing with §§ 2, 3 for now.
- **88–89.** “Stabilité de $\mathrm{TC}'$ … par cochgt. de base ?” leads to the cocartesian square. For (4.5.3) he writes “je ne vois aucun moyen — il faut le poser comme hypothèse.”
- **92–93.** “J'aimerais”, “La relation hypothétique” and “la question est donc si on a égalité” introduce the proposed bounds and the comparison with the inverse image of $F$. In the overlapping NB, “L'hypothèse sur $C$ est inutile ici” is legible. Several words in the proposed replacement are doubtful.
- **94–95.** “Mais je ne vois guère comment prouver (sous des hyp. convenables)” refers to the inverse-image equality for $F'$. On the next sheet, “Ces inclusions devraient être des égalités” is followed by his difficulty proving them without stronger hypotheses.
- **96.** The slanted “mérite un lemme général …”, with its first word tentative, accompanies stability under sums.
- **99.** “Je ne vois pas d'autre façon de le voir” introduces the assumption that $W$ itself is stable under transfinite composition. The following comparison calls this “à peine moins exigeant” than stability under the indicated inductive limits.

## Slips

| Scan and approximate line | Frozen reading | Possible intended form and reason |
| --- | --- | --- |
| 85 L16 and 87 L5 | “transfinie,,” and “4.1.,” | A single comma suffices in each place. The first has two comma strokes. In the reference a point is followed by a comma. |
| 88 L7 | A second (4.5.1), with a possible prime | **Low confidence.** An intended second label could be (4.5.1′). The closing strokes also allow deliberate repetition. |
| 94 L2, L24–26 | $(C'\cap W']^{\sim}$, with an uncertain closer; later $M'(I_0)$ | **Low confidence.** A round closer would match the opening curve. $M(I_0)$ would agree with the product just introduced, though the later M has a prime-like stroke. |
| 95 L3, (4.8.1) | The first inner index reads $I$ or $1$, two closing parentheses precede the inclusion, and the right side reads $\mathrm{TC}(I)$ | **Low confidence.** The proposed reading $u^*(u_!(\mathrm{TC}(I_0)))\subset\mathrm{TC}(I_0)$ would match the domain and codomain on scan 96. It supplies a closer and zero subscripts absent from the line as read. |
| 95 L14–17 and 96 L24–25 | Displays (4.8.8), (4.8.9); the later references read approximately (4.6.8.) and (4.8.4) | **Low confidence.** The latter pair may refer back to the equality and inclusions on scan 95. The digits do not decide an intended renumbering. The doubled closing stroke at the final (4.7.4) could also be a retracing. |
| 98, upper triangle and L13–14 | $f\in C\cap W$ and “Comme $f\in C$” | **Low confidence as a slip.** The paragraph starts with $f\in\widetilde C\cap W$. A tilde would align the later membership with this starting point. The visible later C's are plain. The existence of the lift is a separate issue from the retract calculation below. |
| 98 L20–21 and 100 L27–28 | “et et par composition”; “stable par / par facteurs directs” | The apparent intended readings are “et par composition” and “stable par facteurs directs.” Both copies of each short word are visible. The slash here indicates the line ending. |

## Pointers

- **85–87.** “(4.4.)” on scan 85 belongs to the argument already in progress. Scan 86 names “4.1” and “§§ 2,3.” In Definition 4.4, scan 87 gives “$\mathrm{Cof}_0$ de p. 39” and “l'axiome de factorisation $\mathrm{Cof}_3$ de page 39.”
- **92.** “d'énoncés du type 3.7” refers to statements establishing the existence of functors of the indicated type. A separate tiny reference inserted into the slanting NB may refer to 5.7. Its numerals are uncertain.
- **94–95.** “cf prop. 5.1 ci-dessous” and “voir cependant prop. 5.8. ci-dessous” are separate edge notes. “déf. 4.4. page 74” points to scan 87. The product construction is related to “la définition générale donnée au § 2.” Scan 95 invokes “cat. de Quillen spéciales” with a small reference read as § 9 or p. 9.
- **96.** “résulte de 4.6” and “ont été vus dans 4.7.” refer back to the two abstract parts of the construction.
- **97–98.** The heading names Quillen. Beside the direct-factor assertion the inserted reference begins with the ruled Roman numeral XV and reads approximately “4.2. cor. 1 … page 31”. The digit 7 is also possible in place of 2. Scan 98 repeats “déf. 4.4. page 74.”
- **99–100.** Scan 99 recalls “La dernière assertion de 5.1” and (5.7). Scan 100 begins its proposition with “les notations de (5.1)” and ends with a “précouple de Quillen”.

## Remarks of the model

- **R1. My observation, high confidence, scan 98.** Given the three written equations $pi=f$, $gf=i$ and $pg=\mathrm{id}_Y$, the direct-factor assertion holds with the source $X$ fixed. The first two equations make $p$ and $g$ morphisms under $X$, and the third identifies their composite on $Y$. This checks the conclusion conditional on the displayed lift.
- **R2. My observation, high confidence, scan 100.** Here the fixed object is the target $Y$. The equations $pi=f$ and $fr=p$ make $i$ and $r$ morphisms over $Y$. Their composite on $X$ is $ri=\mathrm{id}_X$, which makes $f$ a direct factor of $p$.

