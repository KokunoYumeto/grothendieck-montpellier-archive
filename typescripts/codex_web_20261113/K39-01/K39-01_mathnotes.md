# Mathematical notes on cote 39

These notes refer to Grothendieck’s undated manuscript (Montpellier archive, cote 39, scans 3–8, 10–17 and 19–20). Line bands refer to the accompanying transcription. Quotation marks identify manuscript wording. Square-bracketed identifiers connect specific observations to the check-event register. The two sequences of axioms have different lettering and different hypotheses on the base.

## What the pages do

**Scans 3–4, choice of series.** Over a field $k$, the author chooses subrings $A_n\subset k[[t_1,\ldots,t_n]]$. He gives the operations on variables explicitly: permutation, passage to a larger set of variables, and identification of two variables. Successive requirements concern the unit, locality and the coordinate $t_1$. He lists the image of the prime ring, the prime subfield, polynomial rings and their localizations as minimal examples under different requirements. The coefficient in one polynomial example raises a question below [R3].

**Scans 3–4, morphisms and inverses.** Coordinates in $A_m$ define an $A$-map with source the formal $m$-disc. Condition e) requires closure under composition. Condition f) asks that the inverse of an invertible formal coordinate change still have $A$-coordinates. The notes compare this with Henselian local rings and name the Henselization of a localized polynomial ring as a minimal example. The last paragraph moves to formal schemes, modules and differential calculus.

**Scan 5, flows.** Over a field of characteristic zero, g) asks that the flow of an $A$-vector field be an $A$-morphism. Condition g′) makes the field depend on time. The triangle places this field over $X$, and the text proposes treating the time parameter as one more spatial coordinate.

**Scan 6, formal groups.** For $k_0=A_0$, the Hausdorff formula gives a law on the completion of a finite-dimensional Lie algebra after extension from $k_0$ to $k$. The author says the law and the homomorphisms induced by Lie homomorphisms respect the $A$-structure. He begins a Pfaff-system argument, strikes it out, and turns to an embedding into a matrix Lie algebra via Ado.

**Scans 7–8, primitives and foliations.** The corollary lists the primitive with zero constant term and the series $\log(1+t_1),\exp t_1,\cos t_1,\sin t_1,\mathrm{tg}\,t_1$. A quotient $X\to B$ of relative dimension $p$ determines its vertical distribution $D$. Condition h) asks that a completely integrable $A$-Pfaff system give an $A$-foliation. A transverse section determines a retraction, and h′) concerns the fibre above zero. The cancelled scan 8 tries two formulations, first a product presentation with $Y,Z$, then a retraction onto $Z$.

**Scans 10–11, change of base assumptions.** The exposition restarts with a commutative ring $k$. Augmentations of coordinate images may be nilpotent. Axioms (a), (b) and (c) govern coordinate maps, substitution and subrings. The minimal system is displayed as $\Lambda[t_1,\ldots,t_n]$, where $\Lambda$ is the image of $\mathbb Z$ in $k$. The smooth formal category has products and transverse fibre products. A completed symmetric algebra on a base-changed finite free module gives the construction $W_{A_*}$. The margins discuss finite projectives and bundles on $X$.

**Scans 12–13, inverses and implicit equations.** The Henselian condition is expressed by invertibility of the augmented Jacobian. Corollary 1 tries to obtain reciprocals using a coordinate change that multiplies the last variable by $f$. Its margin objects to setting that variable equal to 1. Corollary 2 lifts a prescribed simple root of a monic polynomial. Corollary 3 handles a power series with zero augmentation and invertible last partial derivative. The last coordinate of the inverse to $(x,z)\mapsto(x,P(x,z))$, evaluated at $z=0$, gives the desired $F$ [R12, R13].

**Scan 14, subobjects and completion.** An $A_*$-structure on a smooth formal subscheme $Y$ is required to make its inclusion an $A_*$-morphism. A projection onto a model $Y'$ identifies the candidate structure. Diagonals and graphs supply examples and a criterion. For a scheme smooth along a section, the text then asserts functoriality and base-change compatibility of an $A_*$-structure on its completion along that section.

**Scans 13 and 15, differential operators.** A cancelled formula at the foot of scan 13 precedes the fresh statement of d) on scan 15. Stability under elementary differential operators yields $f_p(x)\in A_n$ for the coefficients of $f(x,y)=\sum_p f_p(x)y^p$. The text applies the condition to principal parts, normal neighbourhoods, the universal operator and relative differential operators. Its coefficient-ring corollary gives $A_n\subset k_0[[t_1,\ldots,t_n]]$ [R15].

**Scans 16–17, quotients.** For a formal submersion $p:X\to Y$, a formal section model $Y'$ tests whether the quotient carries its induced $A_*$-structure. The relation is $R=X\widehat\times_Y X$. Condition f), called the integral condition in this sequence, asks that an $A_*$-relation give a quotient structure on $Y=X/R$. The following paragraph interprets this in characteristic zero in terms of integration of a completely integrable Pfaff system.

**Scans 19–20, formal division.** Let $A$ be separated and complete for a linear topology. If $a_0,\ldots,a_{N-1}$ are topologically nilpotent and $a_N$ is a unit, the theorem asserts that each series has a unique expression $QF+\sum_{i<N} b_iZ^i$. It also asserts regularity of $F$. After reduction to a discrete quotient the finitely many lower coefficients generate a nilpotent ideal. An argument invoking Nakayama and a separate polynomial case are cancelled. The surviving argument treats the single map $((b_i),Q)\mapsto\sum b_iZ^i+QF$ with the finite filtration by powers of that ideal [R19, R20].


## Statements left without proof

| Scan and lines | His words | Extent of the argument on these sheets |
|---|---|---|
| 3, 10–26 | « Le plus petit » | Four minimality assertions accompany the prime-ring, prime-field and polynomial examples. The sheet gives formulas. |
| 4, 16–28 | « si f) est satisfait pour un $n$, (f′) est satisfait pour cet $n$ » and « il satisfait = e) et f) » | The first is a dimension-by-dimension assertion. The second concerns the displayed Henselizations. His attempted intervening explanation is struck out. |
| 4, 30–33 and 11, 9–25 | « on définit la catégorie » and « des produits fibrés dans le cas “transversal” » | The constructions of formal schemes, transverse limits, the completed-symmetric-algebra functor and its more general version are announced. |
| 5, 11–20 | « il suffirait de le … demander pour $X$ de la forme $X_n$ » and « la variable temps, devenant variable spatiale » | For the passage from g) to g′) the text indicates a device and gives the flow equation. |
| 6, 11–20 | « Cette dernière est une $A$-loi » and « on est ramené à prouver » | The reduction reaches the formal subgroup associated to a matrix Lie algebra and stops. |
| 7, 1–3 and 18–28 | « stable par primitivation canonique » and « h) implique g), qui équivaut à h) pour $p=1$ » | The corollary and the marginal implication are stated. The retraction formulation and the assertion about the fibre follow. |
| 8, 11–25, cancelled | « On sait qu'il existe alors » and « Conditions équivalentes » | The product and retraction formulations are given in a cancelled draft that ends mid-sentence. |
| 12–13 | « $f^{-1}\in A_n$, cqfd. » and « le couple … est … hensélien » | Corollary 1 has an argument and an objection in the margin. The attempted direct proof of Corollary 2 is cancelled. The proof attached to Corollary 3 survives. |
| 14, 15–27 | « La diagonale de $X\times X$ » and « une construction utilisant e) permet d'y mettre une … structure » | The graph criterion and the construction on a completion, including compatibility with inverse images, are given without working out that construction. |
| 15, 5–25 | « ont … $A_*$ structure canonique et fonctorielle » and « ces derniers stabilisent » | Claims for principal parts, the normal neighbourhoods, composition and the action on $A_*$-functions are listed. |
| 16–17 | « il y a corr. biunivoque » and « la réciproque est vraie » | The first refers to formal quotients and equivalence relations. The second introduces condition f), an additional requirement on the chosen $A_*$. |
| 19, 11–15 | « on est ramené aussitôt au cas où $A$ est discret » | The passage through the discrete quotients is compressed. The finite-filtration argument occupies the following sheet. |

## Questions and conjectures

| Scan and lines | His words | Question |
|---|---|---|
| 4, 3, margin | « Moyennant a) à e) » beside $\mathrm{Hom}_A(X_m,X_n)$ and $\mathrm{Hom}_{A_0\text{-alg}}(A_n,A_m)$ | A possible question about identifying the two Hom sets. Both the connecting sign and the final punctuation carry doubt marks. |
| 4, 16–24, margin | « f') implique-t-il f (moyennant a) à e)) ? il ne semble pas » | Does the Henselian condition on the rings suffice for inverse coordinate changes? |
| 7, 16–20 | « On veut qu'on ait une réciproque » | The desired converse from an integrable $A$-Pfaff system to an $A$-foliation becomes axiom h). |
| 11, 14–18 | « et $=$ projectifs de type fini ? » | Can the finite-free module construction be used for finite projectives? The adjoining margin also proposes projective modules over the ring of $A_*$-functions. |
| 12, 21–24, margin | « $1$ n'est pas nilpotent ! » and « une propriété de divisibilité » | What extra condition validates recovery of the coefficient in Corollary 1? |
| 13, 17–24, margin | « impliquent-ils que $S_n$ soit fid. plat sur $A_n$ … ? » | Faithful flatness under the corresponding hypothesis for $k$ over $k_0$ is left open. |
| 17, 3–11 | « Heuristiquement » and « bien connu » | The paragraph offers an interpretation of f) in terms of leaves and completely integrable Pfaff systems. |

## Slips

| ID, scan and lines | As written | Apparent correction and reason |
|---|---|---|
| S3, 3, 14–17 | $f\in\mathrm{rad}\,S_n$, « $f$ inv. dans $S_n$ », then $1/f\in S_n$ | In this field case, a unit is outside the maximal ideal. In the reformulation c′) the substantive conclusion is $1/f\in A_n$. The oblique leader to « et » stands to the left of $f$, leaving the membership sign intact. Low confidence about the intended wording. |
| S5, 5, 7–10 | « et $X$ un … champ de vecteurs » | The flow formula names its field $\xi$ and its underlying space $X$. The disputed occurrence is drawn with the two crossing strokes of $X$. High confidence. |
| S7, 7, 21–27 | « $\pi\circ i=\mathrm{id}_Y$ » followed by « que $\varphi$ soit compatible avec $D$ » | The compatibility condition appears to concern the same retraction $\pi$. The displayed map letter is overwritten. Low confidence about the attribution of a slip. |
| S10, 10, 14–17 | « les morphismes identiques des $X_n$ sont $\in A_n$ » | The definition puts their coordinate functions in $A_n$. For the maps themselves the intended predicate appears to be “are $A_*$-morphisms.” High confidence. |
| S11, 11, 5–8 | $\mathbb Z[t_1,\ldots,t_n]\hookrightarrow k[[t_1,\ldots,t_n]]$ | Read as a ring map, its kernel contains the characteristic when that characteristic is positive. A plain map from the integer polynomial ring or an inclusion from $\Lambda[t_1,\ldots,t_n]$ fits the displayed image. Medium confidence that the hook was intended as an assertion of injectivity. |
| S12, 12, 21–24 | $g(t_1,\ldots,t_n,1)\in A_n$ | The boxed note objects to this evaluation. The linear coefficient in the last variable gives the desired inverse under the stated differential condition. The objection is explicit and independent of the uncertain exponent in the preceding line. |
| S16, 16, 10–14 | $X'\to Y'$ | The lower edge of the diagram and its composite start at $X$. A distinct prime follows $X$ in the sentence. Read $X\to Y'$ for its indicated map. High confidence. |
| S20, 19, 16–22 and 20, 24–26 | Scan 19 gives $\dot F=\dot U Z^N$. Scan 20 gives $\dot F=\alpha Z^N$ followed by a possible identification with $a_{N+1}$. | In general $\dot U$ is a series with unit constant term $\dot a_N$. The reading of the parenthesis and the attribution of a coefficient slip both have low confidence. See R20. |

## Pointers

| Scan | His words | Referent |
|---|---|---|
| 6, 1–4 and 11–14 | « Par Hausdorff » and « Les formules de Hausdorff » | The formal group law attached to a Lie algebra. |
| 6, 15–20 | « Utilisant le Th. d'Ado » | The passage to a matrix Lie algebra. |
| 6–8 and 17 | « système de Pfaff » and « systèmes de Pfaff » | The name designates the differential systems under discussion. |
| 19, 23–31, cancelled | « on gagne donc par Nakayama » | Generators after reduction modulo the nilpotent ideal. |
| 13, 1–7 and 17, 8–11 | « selon le cor. 1 » and « le morphisme formel plus haut $X\to Y'$ » | Internal pointers to scan 12 and to the triangle on scan 16. |

These sheets give no bibliographic title, external cote or page reference for a work by the author or by another writer.

## Remarks of the model

**R3 · Model remark, low confidence about the intended hypotheses.** On scan 3, lines 23–24, the polynomial example under a), b), d) is written over $\mathbb P$, defined above as the prime field. With just those three requirements in characteristic zero, $\mathbb Z[t_1,\ldots,t_n]$ is already an example and omits $1/2$. The prime-field coefficients would follow from an additional condition on constants. The mathematical distinction is clear. The author may still have been carrying the preceding locality hypothesis.

**R8 · Model remark, low confidence about a slip.** Scan 8, lines 1–4, calls $\exp t_1$ the « série inverse » after $\log(1+t_1)$. The pointed compositional inverse is $\exp(t_1)-1$. Adding the permitted constant 1 still yields the stated inclusion for the exponential. The entire passage is struck.

**R12 · Model remark, high confidence.** Scan 10 imposes nilpotence on constant terms for formal substitution. The polynomial $g(x,y)=f(x)^{-1}y$ can individually be evaluated at $y=1$, but closure of the selected subrings under that evaluation needs justification. Scan 15 supplies coefficient extraction. The coefficient of $y$ in this particular $g$ is exactly $f^{-1}$.

**R13 · Model remark, high confidence for the example.** Scan 13 takes the last inverse coordinate at zero. For $P(t,Z)=Z+Z^2-t$, its value begins $t-t^2+2t^3-5t^4$. Substitution into $P$ gives zero through degree four. This checks the direction of the inverse and the specialization in Corollary 3.

**R15 · Model remark, low confidence about the scope of the margin.** The factorial denominators in the cancelled formula on scan 13 help explain the characteristic-zero remark on scan 15. In a $\mathbb Q$-algebra these factorials are units. For the wider commutative-ring setting of scan 10, characteristic zero alone does not ensure this. In one variable $B=\mathbb Z[t,2u,ut^2]\subset\mathbb Z[u,t]$ is closed under $\partial_t$, while the second divided derivative of $ut^2$ is $u$, absent from $B$. This example concerns the two operator conditions on a subring. The manuscript does not specify here how much of its earlier field framework it is retaining.

**R19 · Model remark, high confidence.** In the discrete stage on scan 19 the ideal generated by finitely many nilpotents is nilpotent. The filtration on scan 20 is therefore finite. At general $A$, uniqueness in the discrete quotients makes the quotients and remainders compatible on reduction. This explains the abbreviated reduction step on scan 19.

**R20 · Model remark, high confidence in the algebraic test, low confidence in the reading of the overwritten line.** Take $A=\mathbb Q$ discrete, $N=2$, $F=Z^2+Z^4$. Here $a_2=1$, $a_3=0$ and $F=Z^2(1+Z^2)$. It cannot equal a scalar multiple of $Z^2$. Multiplication by the unit series $1+Z^2$ gives precisely the invertible factor needed by the associated-graded map. The possible scalar reading concerns this proof line alone.

**Reading questions.** Scan 4, line 3, left margin, has the frozen alternatives $\simeq$ and $\approx$ between the two Hom expressions. In 004-place-01.png the lower stroke has a distinct angular point at its right end. An arrow with an upper tilde, $\xrightarrow{\sim}$, is a further possibility. The ink joins the two strokes at the left. Scan 13, lines 1–3, has the frozen reading « un unique $F$ … telle que ». The two tall l-strokes in *telle* are visible in 013-agreement.png. The low ending of the article in 013-article.png can also be read *une*, and an implicit *série* would account for feminine agreement. This remains a reading question. Scan 14, lines 24–27, has $\mathfrak X$ at « dépend ». The construction suggests $\widehat{\mathfrak X}$, but the nearby insertion already carries a separate small hat, leaving its scope unclear. Scan 20, lines 24–26, retains $a_{N+1}$ after the marked sign. $a_N$ would match the unit coefficient in the hypotheses. The overwritten subscript on the preceding term makes the relation between these two written coefficients difficult to establish.


**Scan 3, lines 27–30.** The frozen main-line labels are $D_n\to D_n$ and $D_m\to D_n$. In 003-end.png the upright passes through the middle of an oval and ends in a separate horizontal foot. A capital $\Phi$ is also possible in these four labels and in the labels below *Specf*. The clearest occurrence is the target of the identity map. The similar capital in the distribution on scan 7 favours the original D reading. The question concerns the letterform independently of the identity of the formal scheme.


**Scan 11, lines 17–24, outer edge.** The frozen text gives a second $\subset$ between the Hom expressions beneath $O_{A_*}(X)\subset O(X)$. The upper inclusion has an open bowl. On the lower baseline in 011-side2.png there is a point after the first closing parenthesis, and there are quote-like strokes higher up. A literal point or a ditto for the upper relation is also possible. The two Hom expressions themselves are legible.


**Scan 14, lines 12–13, the map following *ssi*. Model reading question, low confidence.** The frozen text has $Y'\to X$. The upper and lower pen strokes meet to form a clear point in the earlier $X\to Y'$. At the later occurrence there is a horizontal with a short downward nick at its right end. A plain dash, $Y'\mathbin{-}X$, is another possible rendering. The composite two lines above explains the direction of the map but cannot supply a missing stroke.


**Scan 19, lines 20–22, the second coefficient ring in the quotient comparison. Model reading question, low confidence.** The frozen text distinguishes the first, explicitly doubtful $\dot A_0$ or $A_0$, from the unmarked $A_0$ on the right of $\simeq$. In the latter there is a small dark point just above and to the right of the apex, separated by a much narrower interval than the dot on $F$. It could belong to the entry stroke of the capital or mark $\dot A_0$ there too. The quotient construction cannot distinguish these shapes.

