# Mathematical notes on scans 453–467

The source throughout is Alexander Grothendieck’s *Dérivateurs*, cote 157-5, manuscript pp. 365–379 (s.d.). Line numbers refer to the individual frozen TeX files. These notes follow the live layer of the manuscript. Square brackets in French quotations identify uncertain readings or an editorial omission. The page files give the full wording and alterations.

## What the pages do

**U1. Filtering and powers of an endomorphism, scans 453–454.** The opening continues an argument about a subcategory $K'$. Grothendieck reduces the equalization question to the parallel powers $p^r,p^s$ at $e$. Their equalization is expressed by $p^{r+t}=p^{s+t}$. Taking consecutive powers gives eventual stationarity, which need not hold. He therefore constructs $K_0\subset K_1\subset\cdots$, arranging that a parallel pair in one stage can be equalized in the next. The resulting $K_\infty$ is said to be filtered, to contain $K$, and to have cardinal at most $\pi$.

**U2. The endomorphism family and its arrows, scans 454–455, Corollaire 4.13.39.** Under the conditions of 4.13.38, the author takes endomorphisms of $e$ in $J$ that equalize every parallel pair $k\rightrightarrows e$ in $K$. He asserts closure under composition and the existence of a nonempty part with a pairwise equalization property. The proposed arrows $F$ comprise those of $K$ and composites $k\to e\xrightarrow{p}e\to k'$. He claims that these form a filtered subcategory containing $K$. The single- and double-loop subscripts on $\Sigma$ alternate within the statement.

**U3. Choosing the generators, scans 455–456.** Starting with $p_0$, he chooses an endomorphism at each stage to equalize pairs in the monoid generated at earlier stages and the listed pairs ending at $e$. A bound on the collection of pairs and a return arrow $j\to e$ supply the desired endomorphism of $e$. Two elements in the generated family occur together at a finite stage. The following equality gives the filtering condition. Its two handwritten subscripts are independently doubtful (456, line 5).

**U4. Composition and equalization in $K'$, scans 456–457.** Closure for two added arrows is reduced to $p'u'v=p'\mathrm{id}_e=p'$. The middle endomorphism of the shortened composite is $p'p$. For a parallel pair the author reduces to target $e$, composes with $p_0$, then chooses $q$ so that $q(p_0p)=q(p_0p')$, with common value $r$. The conclusion says that $qp_0$ equalizes the two arrows. R1–R2 examine the two calculations.

**U5. Designated cones, scans 458–459, Théorème 4.14.1.** Section 4.14 opens with an essentially small category $C$, two small families of shapes $\Phi,\Psi$, and two families of chosen cones $\Lambda_1,\Lambda_2$. The right cone adds a final vertex and the left cone an initial vertex. A functor in the specified full subcategory sends the first kind of vertex to a colimit and the second to a projective limit of the corresponding restricted diagram. Under the stated stability assumptions, accessibility of the target implies accessibility of this subcategory.

**U6. Preservation of specified limits, scans 459–460, Commentaire and Corollaire 4.14.2.** An empty $\Lambda_2$ or $\Lambda_1$ leaves a single index on Hom. If the chosen cones in $C$ already exhibit the specified colimits or limits, the condition on a functor becomes preservation. In 4.14.2, $C$ and the target admit the indicated colimits of type $\Phi$ and limits of type $\Psi$. The corollary asserts accessibility of the category of functors preserving them when the target is accessible. S2 discusses the target letter in the running definition.

**U7. Accessible functors, scans 460–462, Corollaire 4.14.3.** For accessible $M,N$ satisfying the condition written $L_{\pi_0}$, with $\pi_0$ infinite, the category of $\pi_0$-accessible functors $M\to N$ is asserted to be accessible. The argument chooses a useful cardinal $\pi$, takes $C=M_\pi$, and writes $M$ as $\mathrm{Ind}_\pi(C)$. A small subfamily represents the required diagram shapes up to isomorphism. Restriction to $C$ identifies the required Hom with $\underline{\mathrm{Hom}}_\Phi(C,N)$, to which 4.14.2 applies. The margin qualifies one reference used in this identification.

**U8. Combining preservation and accessibility, scans 462–463, Corollaire 4.14.4.** The functors must be $\pi_0$-accessible and preserve the specified colimits and limits. A further bound on the shapes allows restriction to $C=M_\pi$. In the resulting Hom the upper index remains $\Psi$. The lower index becomes $\Phi'$, adjoining shapes described as « gdes devant $\pi_0$ » of cardinal at most $\pi$. The text again appeals to 4.14.2.

**U9. Larger families of shapes, scans 463–464, Corollaire 4.14.5.** The main list offers $\Phi_1,\Phi_2,\Phi_3,\Phi_2\cup\Phi_3$. The first consists of categories equivalent to small ones. The second restricts this class to filtered categories. The third mentions discrete categories and categories « gdes devant $\pi_0$ » with an uncertain connective. For a small family $\Psi$ and accessible $M,N$ with the stated stability, the conclusion is accessibility of $\underline{\mathrm{Hom}}_\Phi^\Psi(M,N)$. The proof gives three cardinal conditions, including $\pi^{\pi'_0}=\pi$, restricts to $C=M_\pi$, and invokes 4.14.2 with a bounded family $\Phi_\pi$.

**U10. Small-colimit-preserving functors, scan 465, Corollaire 4.14.6.** For accessible $M,N$, with $M$ stable under small colimits, $\underline{\mathrm{Hom}}_!(M,N)$ is asserted to be accessible. If $N$ too is a paratopos, the functor category is a paratopos. The proof specializes 4.14.5, then invokes stability under small colimits and the criterion cited as 4.8.9, page 207. S3 discusses the family index in this specialization.

**U11. Opposite categories, scans 465–466, Corollaire 4.14.7.** The revised opening refers $\Phi,\Psi,M$ to 4.14.5 and takes an accessible $N$. The category asserted to be accessible is $\underline{\mathrm{Hom}}_\Psi^\Phi(M^\circ,N)$. The display identifies it with $\bigl(\underline{\mathrm{Hom}}_\Phi^\Psi(M,N^\circ)\bigr)^\circ$. The proof restricts to $C$ and applies 4.14.2 with $C^\circ,\Psi,\Phi_\pi$. The superseded hypothesis continues across the page turn under a block cancellation.

**U12. The box product, scans 466–467, Corollaire 4.14.8.** For paratoposes $M,N$, the display identifies $M\boxtimes N$ with $\underline{\mathrm{Hom}}^!(M^\circ,N)$ and declares it a paratopos. The author cites 4.14.7 for accessibility, observes stability under small projective limits because $N$ has them, and applies 4.8.9. The subscript in the specialization at the bottom of 466 is cut by the image edge.

**U13. Taking a left adjoint, scan 467, Corollaire 4.14.9.** For paratoposes $M,N$, the category $\underline{\mathrm{Hom}}^!(M,N)$ of functors preserving small projective limits is displayed as equivalent to $\underline{\mathrm{Hom}}_!(N,M)^\circ$. The map sends $f$ to its left adjoint. The accessibility conclusion is explicitly about the category opposite to $\underline{\mathrm{Hom}}^!(M,N)$. The word « opposée » carries three rules.

**U14. Adjoint criterion, scan 467, Lemme 4.14.10.** The lemma, headed « pour mémoire », pairs existence of a left adjoint to $f$ with preservation by $f$ of small projective limits. The parenthetical version pairs a right adjoint with preservation of small inductive limits. The surviving opening names $M$ as « cat.-paratopos » and gives $f:M\to N$. Two canceled groups make the earlier wording of the opening uncertain.

## Statements left without proof

| Statement and place | Grothendieck’s words | Status within these sheets |
|---|---|---|
| U1, scan 453, line 6 | « La condition PS 1′ est évidente, puisque e est un plus petit élément de J » | The reason is named in one clause. The preceding construction begins before this extract. |
| U2, scan 455, line 11 | « Que Σ soit stable par composition est clair. » | The proof proceeds directly to construction of the nonempty family. |
| U5, scans 458–459, conclusion on 459, line 9 | « si [𝒩] est une catégorie accessible, il en est de même de » the indicated Hom | The statement is followed by the Commentaire. These sheets give no proof of the general theorem. The brackets mark the doubtful alphabet of the target. |
| U6, scan 460, line 3 | « Alors, si [𝒩] est accessible, il en est de même de » the indicated Hom | Presented as the preservation case of the preceding theorem. The next paragraph passes to further corollaries. |
| U7, scan 461, line 3 | « Le cas où π₀ est [utile] pour M a déjà été traité. » | The special case is referred elsewhere. The author addresses the general case here. |
| U9, scan 464, lines 3–9 | « π un cardinal ayant les propriétés suivantes » | The three displayed conditions are used as a choice of cardinal. Its existence is not argued on this sheet. |
| U12, scan 467, line 5 | « il est immédiat qu'elle est stable par petites » projective limits, « N l'étant » | Closure under these limits receives this brief justification. |
| U14, scan 467, line 25 | « Lemme 4.14.10 (pour mémoire) » and « il f. et s. que f commute aux petites » limits | The adjoint criterion closes the extract without a proof. |

## Questions and conjectures

- **Scan 453, line 6, U1.** « mais est-elle filtrante ? » asks whether the first enlargement $K'$ is filtered. The answer is conditional on stationarity of the powers. « Ce n'est / pas forcément le cas » crosses onto 454, motivating the successive enlargements.
- **Scan 458, line 12, U5.** « Cette propriété de stabilité n'est pas [néc.] pour la déf. » is followed by « il est [à peu près / toujours] sûr que [le th.] est [valable / applicable] sans faire cette hyp sur N ». The note suggests weakening the target hypothesis. Its last lines about $\Psi$ are especially difficult to separate from the main writing.
- **Scan 461, line 11, U7.** « La référence n'est pas tout à fait [adéquate] » and « [il faudrait / il faut] [préciser] » qualify the use of 4.13.20. The overlap prevents a secure formulation of the further condition.
- **Scan 463, line 13, U9.** « On pourrait […] faire ici un énoncé qui englobe 4.14.4, en rajoutant un d) ». The proposed $\Phi_4$ and its possible unions are revised in the margin. The modal opening distinguishes the proposal from the main statement.

## Slips

| ID and place | As written | Possible correction and grounds |
|---|---|---|
| S1. Scan 455, lines 9 and 17 | $u,v\in\mathrm{Fl}\,J$ in two places | Possibly $\mathrm{Fl}\,K$. The definition on 454 tests pairs in $K$. The case split and the list of outside factors on 456 use $K$ explicitly. The ambient $J$ does occur elsewhere, so the scope of the two occurrences matters. Low confidence. |
| S2. Scan 459, line 11, and scan 460, line 3 | $M$ after $f:C$ and its connecting stroke | The intended target may be the N-shaped letter of the ambient $\underline{\mathrm{Hom}}(C,\mathcal N)$. The same $M$ occurs twice. Its shape is distinct from the hooked target, whose exact alphabet is uncertain. Low confidence. |
| S3. Scan 465, line 7 | $\Phi=\Phi_0$ | Possibly $\Phi=\Phi_1$. The closed subscript on 465 is a 0. Case a) on 463 uses 1 for the family of all categories equivalent to small ones, the case suggested by « petites » colimits on 465. Other occurrences of $\Phi_0$ name small families. A local use of that notation remains possible. Low confidence. |

## Pointers

| Scans | Wording or reference on the sheet | What the author invokes |
|---|---|---|
| 454 | « Sous les conditions de 4.13.38 » | Hypotheses inherited by 4.13.39. |
| 455 | « cf argument plus bas pour [constr. / const.] de $p_i$ » | Later choice of an endomorphism equalizing the listed pairs. |
| 458 | « Cf 4.14.16 » | Later discussion attached to the proposed weakening of stability. |
| 461 | « pour la validité de 4.14.1 et 4.14.2 » | Passage to a small family representing the required shapes up to isomorphism. |
| 461 | « (cf. [4.13.3 / 4.17.3] p. 275) » and « 4.13.20 […] page 341 » | Restriction to $C$ and recognition of the required preservation condition. The second reference carries the oblique qualification. |
| 462–464 | « et le corollaire 4.14.2. [donne] la conclusion voulue », « comme dans [4.14.1 / 4.14.2] », « d'appliquer encore [4.14.2] », « et on applique 4.14.2 » | Applications to the successive Hom categories. The proposed extra case on 463 also names 4.14.4. |
| 465–466 | « le cas particulier de 4.14.5 », « comme dans 4.14.5 », « On procède comme pour 4.14.5 », « et on applique 4.14.2 » | Specialization to small colimits and passage to opposite categories. |
| 465, 467 | « (4.8.9 page 207) », « par 4.8.9 (page 207) » | The paratopos conclusions of 4.14.6 and 4.14.8. |
| 466 | « (cf 4.2 et 4.3) », « en vertu de 4.14.7 » | The box-product display and its accessibility. |
| 467 | « Ceci résulte du » followed by « Lemme 4.14.10 (pour mémoire) » | The adjoint criterion used after 4.14.9. |

## Remarks of the model

- **R1. Model calculation, high confidence.** On 456, lines 8–11, the six arrows give the word $v'p'u'vpu$, reading composition from right to left and taking $v'$ for the final label. Substituting the displayed relation $p'u'v=p'$ from 457, line 5, leaves $v'p'pu$, the three-arrow diagram on 457, line 9. This checks the order of the middle product conditional on that label reading. Its other candidate is $u'$.
- **R2. Model calculation and reading question, scan 457, lines 21–25.** The defining relation gives $q(p_0p)=q(p_0p')=r$. Substitution with the respective final factors $u,u'$ gives $(ru,ru')$. Confidence is high in this substitution and low in identifying it stroke for stroke with the next display. Its second $p_0$ carries a high dab. The frozen candidates are a raised point, a prime, and a plain $p_0$. The unmarked defining relation immediately above supports the last reading for the calculation.
- **R3. Model comparison, high confidence.** The argument order changes from $M,N$ to $N,M$ in the displayed correspondence on 467, lines 10–11. This agrees with the direction of a left adjoint to $f:M\to N$. The superscript circle applies to the Hom on the right. The wording « la catégorie opposée à » on line 21 independently locates the accessibility conclusion.
- **R4. Model reading question, low confidence.** Scan 453, line 6, calls $e$ « un plus petit élément de $J$ ». Scan 454, line 11, has the frozen readings « maximal / minimal » and 456, line 3, has « objet maximal de $J$ ». The extract opens mid-argument and 454 starts a new corollary. The difference alone cannot justify changing « petit » to « grand ».
- **R5. Model reading question, low confidence.** At the foot of 466, line 31, the frozen reading of the subscript after $\Phi=\Phi_{\cdots}$ is $M$, with alternatives 1 and 0. A downward stroke and a shorter upright meet the image edge. The specializations in U9–U10 make the numeral readings relevant, but the lower join needed to identify the character is missing.
