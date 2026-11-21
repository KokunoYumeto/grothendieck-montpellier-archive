# Mathematical notes on §4.15

Grothendieck, A. (n.d.). *Dérivateurs [chapitres XVII à XIX, dont sommaires de chacun des chapitres]* [Manuscript notes, cote 157-5, scans 513–527]. Montpellier archive. Scan numbers below refer to the supplied images. A B-number locates the physical block in the transcription.

## What the pages do

**Proposition 4.15.1, scan 513.** For a functor $f:E\to C$ with $C$ small, Grothendieck spells out $H'$ in the written order 1, 3, 2. The fibres $E_s$ are accessible. For each $\lambda:s\to t$ and fixed $x_0$ over $s$, $\mathrm{Hom}_\lambda(x_0,-)$ is accessible. In the first argument there is a bound $\pi_\lambda$ uniform in $x_1$ over $t$, with a corresponding $L_{\pi_\lambda}$ condition on $E_s$. He asserts accessibility of the fibre inclusions. When every idempotent in $C$ is an identity, he also asserts accessibility of $E$ and of the projection.

**Corollary 4.15.2, scans 513–515.** The cancelled opening and first sheet numbered 426 precede a second 426 with parts a)–d). Part a) bounds a single inclusion. Part b) gives a bound on the total category and projection. Part c) chooses $\pi_0$ “utile pour” every fibre and $\pi_1$ bounding $\pi_0$, the size of $C$, the $\pi_\lambda$ and the reduced sizes of the $E_{s\pi_0}$. It also requires $\pi_1$-accessibility of the second-argument functors for these smaller source objects. For $\pi^{\pi_0}=\pi\geq\pi_1$ he states an Ind-equivalence. Part d) gives $E(\pi)=E_\pi$, where $E(\pi)$ collects the $E_{s\pi}$ over all fibres.

**Proof of a) and b), scans 516–518.** The Hom sets comparing a fibre colimit with a colimit in $E$ lie over $\mathrm{Hom}_C(s,t)$. Grothendieck tests the comparison on the part over each $\lambda$. For b), lemma 4.15.3 supplies a cofinal subsystem whose base objects coincide and whose transitions are identities. This lets him construct the colimit in a single fibre and identify its image under $f$.

**Proof of c) and d), scans 518–521.** To treat $H_\lambda(x)$, he presents $x$ as a filtered colimit of $x_j$ in $E_{s\pi_0}$ with $\mathrm{card}\,J\leq\pi$, then uses an inverse limit of Hom functors. The resulting inclusion yields the fully faithful $\mathrm{Ind}_\pi(E(\pi))\to E$ of scan 520. Presentations inside each fibre give essential surjectivity. For d), he expresses an object of $E_\pi$ as the image of a projector. Its image in the base is the identity, and closure of $E_{s\pi}$ under direct factors puts the object in $E(\pi)$.

**Base-change corollary, scans 521–522.** The heading reads 4.15.[4/9/3]. The three conditions require accessibility of the total category and projection after every base change by a small category without nonidentity projectors, the same test on $\Delta^1$, and $H'$, respectively. His circular argument uses base-change stability, then invokes 4.15.1.

**Remark 4.15.5, scans 522–523.** A fully faithful functor satisfies $H$, he says. A small category nevertheless embeds fully faithfully in its Karoubi envelope even when it is itself not Karoubian. His example has one object, with arrows $\mathrm{id}_0$ and $p$, where $p^2=p\ne\mathrm{id}_0$. The envelope $P$ has the displayed relations $\rho\sigma=\mathrm{id}_1$ and $\sigma\rho=p$. He uses this example to ask for stronger base-change tests.

**Proposition 4.15.6 and attempted construction, scans 524–527.** He proposes that $E$ and $f$ are accessible when $f$ is fibrant or cofibrant over an essentially small Karoubian base, with accessible fibres and accessible change-of-base or cobase-change functors. He passes to a small equivalent base, chooses cardinal bounds and describes reconstruction by fibrewise Ind-completions. In the cofibrant case he forms $x=\varinjlim_I\beta_{i*}(x_i)$ in $E_s$. He compares Hom sets over each $\lambda$ using accessibility of $\lambda_*$. The fibrant discussion ends with a difficulty about transition maps.

## Statements left without proof

- **517, B02–B07.** “Nous prouvons plus bas le” introduces lemma 4.15.3. Of 4.8.13 the body says “que je n'ai tjrs pas prouvé !” The margin adds “Mais c'est à présent établi” with a difficult qualification. The rigid case is called “immédiate, cf plus bas”.
- **520 B01 and B09, 521 B09.** The inverse-limit accessibility step is referred to “cf SGA 4 I 9.8”. The assertion about images of projectors is introduced with “on sait” and an incomplete reference. For the base-change corollary, $b\Rightarrow c$ is “l'étant presque”, followed by 4.14.24.
- **524 B07, 526 B03, 527 B06–B08.** “On a déjà vu” introduces the implication to $H'$. The essential constancy assertion on 526 refers to “(4.8.13)”. On 527 the cofibrant colimit is asserted with “On vérifie facilement”. The last margin says “J'ai vérifié” a narrower fibrant assertion ending “alors $E$ est Kar.” The abbreviated predicate remains doubtful.

## Questions and conjectures

- **523 B05–B09.** He asks for “des conditions néc. et suff.” for all small Karoubian base changes. For the proposed tests $\Delta^1,P$ he adds “Mais je doute qu'il en soit ainsi.” Beside two larger diagrams, each described as having three objects and five nonidentity arrows, he writes “devrait marcher”.
- **524 B01–B04, 526 B05, 527 B07.** Beside the proposition stand “faux ?” and “Le cas fibrant n'est pas prouvé, peut-être faux. -- et de = pour le cas cofibrant !” The proposed receiving object on 526 carries a question mark. On 527 he writes “je ne vois comment faire pour construire une limite”, then “Il faudrait prendre $C=P$ pour essayer de comprendre” and “je ne vais pas insister.”

## Slips

Confidence concerns the proposed correction. The French and formulas in the page files retain the written forms.

| Scan and place | Written form and possible correction | Reason and confidence |
|---|---|---|
| 513 B11 | $p:E\to C$ for $f:E\to C$ | The proposition introduced $f$. The preceding $p$ was a projector. High. |
| 515 B03 | $\lambda:s\to t$ followed by “de source $t$”. The gloss would read “de source $s$” | The crossed $t$ is at the target of the displayed arrow. High. |
| 516 B06 | $\mathrm{Hom}_C(x,y)$ for $\mathrm{Hom}_C(s,t)$ | Two occurrences immediately above have $s=f(x)$ and $t=f(y)$. High. |
| 515 B04 and 516 B08 | “$\pi$-accessible” on 515 may need $\pi_1$. The lower index on 516 reads 0 or 1 | The bound discussed is $\pi_1$ and 515 B09 restates it. Medium for 515, low for 516. |
| 515 B16 | $\mathrm{Ind}_\pi(E_{s\pi})$ may mean $\mathrm{Ind}_\pi(E(\pi))$ | Compare 520 B05. The target on 515 also bears a cancellation. Low. |
| 519 B11–B14 | $H_\lambda(x_0)$ may mean $H_\lambda(x)$. The preceding “$\pi_0$-accessible” also poses a question | The presented object is $x$, whereas $x_0$ was the variable of the preceding functor. Medium. The inequality just given omits $\pi_0$ and leaves the intended bound open. |
| 520 B02 and B06 | First $E_{s\pi}\subset E(\pi)$ may mean $E_{s\pi}\subset E_\pi$. “utile pour $\pi$” may mean “utile pour $E_s$” | The next display gives the union's inclusion in $E_\pi$. The presentation following “utile” takes place in $E_s$. Medium for both. The argument of $f$ in B06 could be $s$ or $x$. The following line favours $x$. Low. |
| 525 B04 and B08 | The upper target of $\lambda_*$ is $E_{s\pi_1}$ and the lower target is $E_{t\pi_1}$. The upper target may need $t$ | The lower line repeats the transport. The upper box contains overwritten ink. Low. |
| 526 B07 | The first $\beta_{i*}$ and the inner $\beta_{ji*}$ both have an argument whose subscript reads $j$ or $i$. The two sources suggest $x_i$ | Compare the adjacent triangle and the preceding $\beta_{i*}(x_i)$. The two doubtful strokes differ in depth. Low. |

Further reading questions concern the cancelled base letter $S/C$ (514 B02), the outer family index $j/i$ and the base letter $E/C$ (517 B02, B07), and $\mathrm{card}\,E/C$ (518 B04). Each has low confidence. In 516 B08 the frozen “quel que soit la flèche” might have a reduced feminine ending. A further look shows a short terminal upstroke like the second *quel* on that line. Its shape leaves the agreement unresolved.

## Pointers

513 B02 and 521 B05 give “$H$ (p. 409)”. 515–516 cite 4.15.1 and 4.15.2. On 517 the references include “Cf démonstration page 452”, “4.8.13 (pages 212–216)” and a difficult marginal “4.15.6 a) 1°”. On 520 the citations are “cf SGA 4 I 9.8” and an unfinished “par 4.8. …”. On 521 the earlier argument is “de 4.14.24”. On 523 an insertion says “plus fortes que 4.15.4”. The slanted reference reads 4.15.[7/3], p. [443/445/435]. The bottom of 524 has “4.15.[2/1] a)”. The opening “AQT/SQT” of 525 has no secure expansion here. On 526 “(4.8.13)” is interlined. Scan 527 returns to $P$ from 523.

## Remarks of the model

- **Model observation, high confidence.** The two sheets numbered 426 show how part b) changed. On the cancelled sheet “sans projecteurs” is an insertion. On the next sheet it still appears as an insertion, while the new marginal note assigns only $H1$ and $H2$ to a) and b) (514 B04 and 515 B02–B04).
- **Model observation, high confidence.** The author distinguishes two senses of constancy by giving the transition maps explicitly. On 517 he asks that they all equal $\mathrm{id}_s$. On 527 he can arrange a common $s$ but says the maps are neither identities nor even isomorphisms. This identifies the specific obstacle he records in the fibrant case (517 B05, 518 B01, 527 B07).
- **Model observation, low confidence about the intended numeral.** The later wording “plus fortes que 4.15.4” helps identify which corollary the author meant at 521. The overwritten digit there still supports more than one reading. The numerical sequence and the comparison of the physical 4s are distinct pieces of evidence (521 B03, B09 and 523 B05).
