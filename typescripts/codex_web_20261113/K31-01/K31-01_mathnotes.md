# K31-01 · Mathematical notes

Line references are to the corresponding scan, as in the transcription. Quotation marks enclose the manuscript’s words. In quotations, ⟨ ⟩ indicates an insertion and † indicates a doubtful reading. The editorial observations below leave the final LaTeX intact.

## What the pages do

**A field extension of transcendence degree one (52).** Lemme 2 starts with vanishing over finite extensions of a field $k$. It bounds the degrees in which $H^i(K,\Gamma)$ can be nonzero for a finitely generated extension of transcendence degree one. The field diagram and the exact sequence with $G'$, $G$, $G''$ lead to a spectral sequence. The $j>1$ terms vanish by an earlier lemma, and the $i>n$ terms by hypothesis. A corollary states the bound for a function field over an algebraically closed field.

**Restriction of sections to a closed set (55–56).** The initial question asks whether restricting an injective sheaf to $Y$ gives vanishing in positive degrees. The author first tests extension in degree zero. On an irreducible space he prescribes germs with values 0 and 1 at two closed points. Neighbourhoods on which these values are attained must meet. A second example depicts a circle cut by a line at $a,b$ and transfers the two-point problem to that intersection.

**Flasqueness of a restriction (56–57).** Ex 3 considers two irreducible curves meeting at $a$. On $Y-\{a\}$ the indicated section takes values 0 and 1 on the two punctured branches. The attempted extension gives incompatible conditions on intersecting neighbourhoods. A cancelled continuation attempts a decomposition by irreducible components and writes a sequence involving the component restrictions and a sheaf $G$.

**A cohomology class from two intersections (58–59).** Two curves now meet at both $a$ and $b$. The displayed sequence places $F_a\times F_b$ between sections on the components and $H^1(Y,F_Y)$. The author chooses $(0,1)$ and asks whether it can be a difference of sections. Equality of local representatives on overlaps is followed to a claimed contradiction. The lower part of 59 suggests an irreducible $Y$ of dimension 2 inside an $X$ of dimension 3, using a closed $X_1$ and its intersection with $Y$.

**Vanishing on all opens and on covers (60, 62).** The proposition relates vanishing of $H^1(U,F)$, vanishing in all positive degrees, a quotient for a two-open cover, and cohomology for arbitrary open covers. The numbering and the placement of the Noetherian qualification have been revised. The manuscript invokes Leray, then introduces a maximal open on which a cohomology class is zero. Scan 62 returns to the remaining implication. It embeds $F$ in an injective and uses a short resolution, exact as presheaves under the hypothesis, to compute higher cohomology.

**A field-theoretic NB (61).** A separate calculation places $l,k,K,L$ in a condition involving $k\subset l(K^p)$. It compares the $N$ terms with different base fields and writes a map or connecting stroke between two modules of differentials. Below a divider there is a separate boxed inclusion involving $K''_\infty$, $K_\infty$ and $K'_0$. Its link to the calculation above is only briefly indicated.

**Elementary torsion sheaves and a restriction test (65).** The leaf describes sheaves of the written form $i_*(G)_{U,X}$, where $i$ comes from a residue field. The conditions mention an open neighbourhood, étaleness and a unibranch condition. A proposition gives a composition series, and Cor 1 tests $\mathrm{cd}_l(X)\leq n$ by surjectivity in degree $n$ on restriction to $Z$ and vanishing in degree $n+1$. A finite variant follows. A second version with supports is cancelled.

**A dimension bound varying with the point (66).** Cor 2 assigns a closed subset $Y$ the supremum of a strictly increasing function on its points. A bound on $\mathrm{cd}_l(Y)$ is compared with one vanishing test for integral closed subschemes and a finite unibranch variant. The proof is indicated by Noetherian induction. A supported version, headed Cor 2 bis after an earlier Cor 3, is crossed through.

**A local criterion and the support of a sheaf (67–68).** The revised lemma assumes a bound on the $l$-cohomological dimension of each residue field and a strict inequality on proper specializations involving a strictly local ring and its total ring of fractions. The conclusion bounds cohomology by the supremum of the function on the support of $F$. The proof reduces to a generic-point direct image $g_*G$, computes stalks of $R^qg_*G$, and uses a spectral sequence. The square and the diagram of degrees belong to different stages of that argument.

**A finite-type morphism (69).** The NB records $\varphi(x)\leq\varphi(y)+2\deg\mathrm{tr}\,k(x)/k(y)$ for $y=f(x)$. A short crossed beginning follows the inequality.

## Statements left without proof

| Scan and lines | Manuscript words | Extent of the argument here |
| --- | --- | --- |
| 52, L13–16 | « Alors $H^i(K,\Gamma)=0$ pour $i>n$ » | Stated for a function field of transcendence degree $n$ over an algebraically closed field. The preceding lemma proves the one-step estimate; no separate derivation of the corollary is written. |
| 56, L16–20 | « le faisceau induit est tjrs flasque, facile » | A bracketed assertion about the irreducible-curve case. The qualification just before it is faint. |
| 59, L10–18 | « on trouve un exemple avec $Y$ irréd (de dim 2 …) » | He sketches the intersection and the sheaf to take. There is no separate verification of the resulting example. |
| 60, L12–16 | « par suite spectrale de Leray, est bien connu (petit argument de Cartan en une direction) »; « trivial » | He refers to the comparison and lists two implications without developing those arguments here. |
| 65, L8–10 | « a une suite de composition formée de faisceaux de $l$-torsion élémentaires stricts » | The proposition is followed immediately by Cor 1. |
| 65, L11–22 | « Conditions équivalentes »; « sauf que $Y\longrightarrow X$ est fini » | The two tests and finite variant are stated. No proof is written on this leaf. |
| 66, L13 | « Récurrence noethérienne grâce au cor. 1 » | The proof of Cor 2 is given in this one line. |
| 69, L1–4 | « avec la fonction $\varphi$ précédente, on a pour $x\in X$, $y=f(x)$ » | The displayed inequality follows directly in the manuscript. No proof follows it. |

## Questions and conjectures

- **55, L1–5.** « $F$ faisceau injectif sur $X$, est-il vrai que $H^i(Y,F|Y)=0$ pour $i>0$ ». The answer written beside it is « Réponse négative ».
- **58, L10–15.** « la question est de représenter un élément … comme différence $f_1-f_2$ ». For the chosen $(0,1)$ he writes « je dis qu’il ne se représente pas comme diff. ».
- **67, left margin.** « il y a intérêt à inclure le cas $l=0$ » and « Il y a intérêt à prendre† $\varphi(x)={}$dim de … Krull de $\bar{x}$ ». These are proposals. The same note discusses vector spaces over $\mathbb Q$ and condition b).
- No separate conjecture with an explicit conjectural label was identified. The uncertain deleted heading on 54 supplies no statement of a conjecture.

## Slips

| ID | Scan and lines | Written form and possible intended form | Confidence and reason |
| --- | --- | --- | --- |
| S59 | 59, L7–9 | The first displayed equality has $\varphi_{1x}=\varphi'_{2x}$. An intended right-hand $\varphi'_{1x}$ would give the stated contradiction with the second equality. | Low for the proposed correction. The 2 is distinct here, but the parallel earlier index on 58 lies in worked-over ink. See M59. |
| S60a | 60, L6 | « deux ouverts $U,V$ de $F$ » apparently means « de $X$ ». | High. The same proposition calls $F$ a sheaf on the space $X$ and speaks of opens of $X$ immediately above. |
| S60b | 60, L17 | The left side of the inclusion reads $H^1(U\cap V,F)$. The two-open group $H^1((U,V);F)$ from L7 is a candidate. | Low. A worked-over mark precedes $U$. The comparison is offered because L7 defines the two-open quotient and L17 refers to condition (ii). |
| S65 | 65, L4–7 | « $U$ … dans $Y=\overline x$, $U=X-Z$ ». The relative complement suggested by the later phrase « fermé $Z$ de $Y$ » is $Y-Z$. | Medium. The ambient letter in the equality looks like X. The relation to the later corollary motivates the proposed Y. |
| S67 | 67, L3 | $\mathrm{cd}_l(k(x)$ has one visible closing parenthesis. A second one would close the outer argument. | Medium. The displayed handwriting supplies only one closing stroke; the missing one is typographical. |
| S68a | 68, L13–14 | $R^qg_*(F)_x=0$ occurs between formulas with $R^qg_*(G)$. The argument of $g_*$ would ordinarily be $G$ here. | Medium. The same page calls the original sheaf on $X$ a direct image of $G$. |
| S68b | 68, L14–16 | A dash-shaped stroke between $p$ and $q$ gives $p-q$ on the first-candidate reading; $p+q$ would express total degree. | Low. The first sign carries a doubt mark and the later one has essentially the same hand. See M68. |

## Pointers

| Scan | His words or mark | What it refers to on these leaves |
| --- | --- | --- |
| 52, L8–12 | « en vertu du lemme 1 » | Used to remove terms with $j>1$. Lemma 1 is outside this selection. |
| 56–58 | « Exemples 1 et 2 »; « comme dans l’exemple 2 »; « la question du début » | The sequence beginning with the question on 55. Some references lie in cancelled writing. |
| 59, L10–16 | « Utilisant cet exemple »; « la figure … précédente » | The intersecting-curves construction on 58. |
| 60, L12–14 | « suite spectrale de Leray »; « petit argument de Cartan » | The comparison of the two positive-degree criteria. No title or bibliographic citation is supplied. |
| 62, L1 | « Reste … (i) ⇒ (i bis) » | The proposition on scan 60, separated in scan order by the field NB. |
| 66, L13; 67, L23–25 | « grâce au cor. 1 »; « le cor 2 précédent » | The corollaries on 65 and 66, respectively. |
| 68, L12 and L20 | « Condition b »; « par l’hyp. a) » | The two hypotheses on 67, used at different points. |
| 69, L2–3 | « la fonction $\varphi$ précédente » | The point function discussed on 66–68. |

## Remarks of the model

- **M59 · Model, high confidence in the algebraic check.** With $\varphi_2-\varphi_1=0$, $\varphi'_2-\varphi'_1=1$ and $\varphi_2=\varphi'_2$, the offset is $\varphi_1-\varphi'_1=1$. The two equalities actually displayed on 59 admit the values $(\varphi_1,\varphi'_2,\varphi'_1)=(1,1,0)$ taken on their own. The proposed correction to the manuscript is independently rated low in S59.
- **M68 · Model, high confidence in the algebraic check.** The inequalities $p<h-q$ and $p+q<h$ differ by rearrangement. This explains why the addition sign is a meaningful alternative on 68; the identification of the individual pen stroke remains low confidence.
- **Reading question · Model, low confidence (61, whole leaf).** The transcription treats the two long, thin obliques as marks extending across the paper and encodes the unambiguous local strikes separately. Some or all of the leaf may instead have been cancelled by those two lines. Their extent in unwritten space does not settle their editorial status.
- **Reading question · Model, low confidence (67, L8–9; 68, L1–2).** The frozen name was $s$ or $\nu$ in the bound assigned to a sheaf; the final apparatus adds $\varphi$ as another possibility. The small hook before $(F)$ is visibly shorter than the phi on points. All three readings give the same displayed supremum, and these notes do not require a choice.

