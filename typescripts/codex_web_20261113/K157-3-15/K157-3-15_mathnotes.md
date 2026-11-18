# Mathematical notes on scans 222–236

Scan numbers refer to the archive images. The manuscript numbering runs from 172 to 186. Line ranges follow the comments in the transcription.

## What the pages do

**U1 · Definition and first theorem, 222.** Grothendieck starts with the fundamental group and the components of a loop object. He distinguishes two chain constructions and sets $\pi_n(X,x)=\pi_0(\Omega^n(X,x))$. To define $W_n$, he proposes that isomorphisms on the $\pi_i$ through degree $n$, tested either everywhere or on representatives of the components, are equivalent to a list of cohomological comparisons. The margin questions the reverse implication.

**U2 · Moving the basepoint, 223–226.** A cartesian square exhibits $\Omega(X,x)$ as a fibre. The section selects the empty loop. A functor from $\Pi X$ to a pointed homotopy category would give the required local system. In the slice construction the transition map does not preserve the selected point. The cancelled alternatives on 224–225 try to compare different pointings. The surviving discussion proposes a morphism in the pointed homotopy category and defers the composition checks.

**U3 · Attempted induction, 226–228.** Grothendieck reduces the first theorem to a lemma in degree $n$, assuming the preceding degrees. The square on 227 compares a map of loop groups with the map in degree $i+1$. Those loop groups are based at their units. The passage to other basepoints remains open, and the author abandons this version of the theorem on 228.

**U4 · Corrected formulation and first implication, 228–229.** The new conditions concern connectivity of a homotopy fibre ($a_n$), components and pointed homotopy groups ($b_n$), and comparison of cohomology with locally constant coefficients ($c_n$). In $c_n$ the author specifies sheaves of groups in degree one and abelian sheaves from degree two. The written chain is $a_n\Rightarrow b_n\Rightarrow c_n\Rightarrow a_{n-1}$. Using a fibration replacement, he relates $a_n$ to $b_n$ together with surjectivity in degree $n+1$. The $K(\pi,n+1)$ example belongs to the strictness discussion for this first arrow.

**U5 · The fibre sequence and constant coefficients, 230–232.** To obtain $b_n\Rightarrow c_n$, Grothendieck reduces to degree $n$ and a connected base and total space. He obtains an $(n-1)$-connected fibre and a zero map from its $n$th homotopy group to that of $X$. He writes the Leray sequence and identifies the possible obstruction with a map out of $H^n(X,F_X)$. For constant coefficients he compares it to restriction along the composite $\pi_n(Z,z)\to\pi_n(X,x)\to H_n(X,\mathbb Z)$.

**U6 · Comparison using universal covers, 232–233.** For a nonconstant $F$ he returns to the universal covers of $X$ and $Y$. When $n=2$ the vanishing $H^1$ of the two covers gives the two exact rows on 233. He invokes the five lemma. For general $n$ he does not see how to carry the indicated comparison from $E_2$ to the later terms.

**U7 · A proposed pairing for local coefficients, 233–235.** A based sphere representing a class in $\pi_n(X,x)$ pulls a cohomology class back to the sphere, giving a value in the stalk $G_x$. Grothendieck asks for the resulting pairing to be equivariant and additive. If the map it defines agrees with the edge map after restriction to the fibre, the zero map $\pi_n(Z,x)\to\pi_n(X,x)$ gives the required vanishing. He closes the paragraph with a qualified “qed”.

**U8 · The last implication, 235–236.** Starting from $c_n$, the induction aims to raise the connectivity of $Z$ from $n-2$ to $n-1$. For $n=2$ a quotient argument gives an abelian $\pi_1(Z,x)$. Its vanishing is a further step. The final general sequence links degrees $n-1$ and $n$. The last sentence breaks off at “qu’on a”.

## Statements left without proof

| ID | Scan and lines | Statement and the author’s words |
|---|---|---|
| B1 | 222 L12–17 | The comparison between the two chain constructions is postponed. “Tôt ou tard il faudra donner un énoncé de comparaison…” |
| B2 | 223 L1–5, L13–20 and margin | Change of basepoint as a local system is still to be constructed. “chose que je n’ai pas fait encore”. For its descent to the pointed homotopy category he writes “Mais il faut avoir vérifié que … transforment … en isom.” The axiom cited in the slant is difficult to read. |
| B3 | 225 L17–21 to 226 L1–3 | The proposed pointed morphism is supposed to compose. “Ceci doit suffire pour définir la flèche”, “avec transitivité pour une composition” and “quitte à faire des vérifications circonstanciées par la suite”. |
| B4 | 227 L19–25 to 228 L1–2 | For a morphism of monoids, the comparison must hold at an arbitrary point of the loop object. “On devra sans doute prouver que … ça reste vrai pour les $\pi_i$ en tout point $\xi$”. |
| B5 | 229 L10, insertion above the middle arrow | “si X,Y 1-connexes c’est vraiment prouvé, sinon, il y a des vérifications à faire”. The following parenthetical is uncertain. This is the author’s assessment of $b_n\Rightarrow c_n$. |
| B6 | 230 L4–13 and 235 L14–19 | Earlier low-degree cases are invoked. “tout est OK si $i\in\{0,1\}$” and “même pour $n=1$, où il est prouvé”. Their earlier treatment lies outside these leaves. |
| B7 | 231 L11–21 to 232 L1–9 | The identification with equivariant Hom is introduced by “sauf erreur” and flagged “(À vérifier.)”. Equality of the canonical map and the composite is introduced by “et sûrement”. |
| B8 | 234 L6–23 to 235 L1–13 | The map to the stalk should depend only on pointed homotopy class. “Sûrement l’application … ne dépend que de la classe d’homotopie ponctuée”. The two further requirements are compatibility with the action of $\pi$ and additivity in $\pi_n$. Identification with the edge map starts “Si j’admets ceci …”. The conclusion retains “mais il y a pas mal de travail de vérifications à faire…”. |
| B9 | 235 L20–23 to 236 L10–24 | The last implication requires the vanishing of $\pi_{n-1}(Z)$. For $n=2$ the author writes “Il faut le voir comme un $\pi$-Module, et prouver sa nullité comme tel”. In the general case the next inference begins on the last line of 236. |

## Questions and conjectures

| ID | Scan and lines | Question or conjecture |
|---|---|---|
| Q1 | 222 L21 margin, 227 L5 margin, 228 L7–14 | “Sans doute faux” occurs beside both the first theorem and its lemma. The first margin singles out $b\Rightarrow a$, already at $n=2$. On 228 he writes “je me suis ± convaincu que l’énoncé du th. 1 est faux tel quelle” and then “Voici un énoncé que j’espère vrai”. |
| Q2 | 224 L3–19 and 225 L6 margin | Can the chosen section give a canonical pointed functor “transformant toute flèche en iso ?” A cancelled approach asks “Cela ne permet-il pas de définir la flèche cherchée ?” The later margin observes “le carré n’est pas commutatif”. |
| Q3 | 227 L19–25 | The parenthesis “satisfaisant certaines conditions ?” qualifies the suggested use of a morphism of monoids to move away from the unit. |
| Q4 | 229 L10–12 and left margin | “je présume que chacune de ces implications est stricte”. For $c_n\Rightarrow b_n$, even for simply connected $X,Y$, the margin distinguishes vanishing of a homotopy map from vanishing after composition with a homology map. He adds “Je présume qu’il y a des contre-exemples.” |
| Q5 | 232 L15–19 and 233 L10–22 | “Comment récupérer le cas où $F$ n’est pas constant ?” Of the comparison in higher degrees he writes “ne me semble pas impliquer la relation similaire pour les $E_r$ supérieurs”. He then writes “J’ai envie de trouver une application canonique”. |
| Q6 | 235 L23 to 236 L1–14 | “Le cas $n=2$ demande peut-être une attention particulière”. The question concerns the fundamental group of the fibre at the start of the connectivity induction. |

## Slips

| ID | Scan and lines | Frozen reading, proposed correction and reason | Confidence |
|---|---|---|---|
| S1 | 233 L5–7 | The last lower object reads $H^3(\pi,H^0(\widetilde Y))$. The expected lower object is $H^3(\pi,H^0(\widetilde X))$. The other lower entries use $X$ or its cover. The lower spectral sequence on 232 gives the same assignment. The forked Y is clear. | High |
| S2 | 233 L17–19 | The page reference is marked $\text{187}$ or $\text{181}$. The sequence occurs on manuscript p. 181 and is explicitly cited as p. 181 on both 234 and 235. The intended location is clear. Whether Grothendieck wrote a wrong last digit remains a reading question. | Low |
| S3 | 228 L7–8 | “l’énoncé du th. 1 est faux tel quelle”. The apparent agreement would be “tel quel”. On a separate look at the word endings, the first word ends at l and the second shows two tall strokes followed by a short e. | Medium |

## Pointers

| Scan and lines | Reference as it appears |
|---|---|
| 222 L22–23 | “(cf page 171 ci-dessus)” belongs to the cancelled $f\in W_1$ clause. Manuscript p. 171 precedes this batch. |
| 223 L5 and L17–20 margins, 225 L1–6 | The margins refer to a letter group followed by “2° bis, b)” and to “W(4…)”. The cancelled comparison on 225 refers to another “W… bis”. The exact letters and digits are marked in the transcription. |
| 226 L14–16, 228 L9–14 | The low-degree statement is said to have been “rappelé” previously. The later reference to work done “from scratch” specifies “dans le modélisateur Cat”. No separate text is named. |
| 230 L1–3, 231 L1–10 and L21–26, 232 L9–14 | The first “suite spectrale de Leray” on 230 is crossed out. The sequence is written on 231. On 232 “la suite exacte de Leray (page précédente)” and the labels $(*)$, $(*')$ refer back to it and the two maps on 231. The identification below the brace is credited “par th. de Hurwicz”. |
| 233 L8–19, 234 L20–23, 235 L3–13, 236 L21–23 | “le lemme des 5” is invoked on 233. For the doubtful page reference see S2. On 234–235 “p. 181” or “page 181” is explicit, and “la flèche précédente (page précédente)” on 235 refers to 234. The final brace on 236 again reads “par Hurwicz”. |

## Remarks of the model

**R1 · Model remark, high confidence, 231 L8–10 and 235 L8–13.** In the displayed exact row, once the edge map $\alpha$ vanishes, exactness makes $H^n(Y,F)\to H^n(X,F_X)$ surjective. The initial zero gives injectivity. This checks the last inference conditional on the identification that the author leaves open.

**R2 · Model remark, high confidence, 229 L13–22 and 230 L14–21.** For the chosen fibre in degree $n\geq2$, exactness and $b_n$ make the boundary from $\pi_{n+1}(Y)$ onto $\pi_n(Z)$. Surjectivity of $\pi_{n+1}(X)\to\pi_{n+1}(Y)$ then amounts to vanishing of $\pi_n(Z)$. This checks the extra top-degree condition in the first implication.

**R3 · Model remark, high confidence, 236 L5–14.** The stated surjection from the abelian group $\pi_2(Y,y)$ makes its quotient $\pi_1(Z,x)$ abelian. A quotient of an abelian group can still be nonzero, so the manuscript’s next requirement, proving vanishing under $c_2$, is a genuine additional step.

**R4 · Model remark, low confidence about an intentional change of notation, 230 L4, 231 L8–10 and 235 L8–13.** The parenthesized $\alpha$ on 230 sits beside the comparison between the cohomology groups of $Y$ and $X$. The bare $\alpha$ on 231 sits above the outgoing arrow from the group of $X$. The first shaft has a doubtful head and a coefficient in the later row has been overwritten. The explicit reference to “la suite exacte page 181” on 235 identifies the map called zero there.
