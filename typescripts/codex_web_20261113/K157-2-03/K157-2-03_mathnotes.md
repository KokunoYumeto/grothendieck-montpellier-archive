# K157-2-03 · Mathematical notes

## What the pages do

**U1 · Scan 35.** Fix two objects $a,b$ of $M$ and a set $\Sigma$ of arrows to invert. When the two endpoint functors are constant at $a,b$, the commuting triangle amounts to a functor into the fibre of $(\sigma_M,\beta_M)$ over $(a,b)$. This gives the boxed identification of categories of chains. The small superscript on the right-hand Hom in the box is uncertain.

**U2 · Scans 35–36.** The Scholie gives a sequential ind-object $K=(K_n)$ for which $\mathrm{Hom}_{\Sigma_X}(a_X,b_X)$ is the direct limit of the sets of components of $\underline{\mathrm{Hom}}(X,K_n)$. On scan 36 each component set is read as $\mathrm{Hom}_{\mathrm{Cat\,hot}}(X,K_n)$. The author concludes that the contravariant functor factors canonically through Cat hot and that its representing ind-object there is determined up to unique isomorphism by $M,\Sigma,a,b$.

**U3 · Scans 37–38.** For $f\colon X\to Y$ the localized categories give a map from the Hom set at $Y$ to the one at $X$. The live corollary says that this map is bijective for a *homotopisme*. The author then asks about weak equivalences, descent to Hot and the possible representing ind-object there. An earlier corollary on scan 37 and an argument about envelopes at the foot of scan 38 are cancelled.

**U4 · Scans 39–41.** Proposition 1 treats a localization $\varphi\colon C\to C'$ with fully faithful right adjoint $\psi$. Write $W$ for the maps inverted by $\varphi$. For $\mathrm{Hom}_C(-,K)$ the author compares testing all of $W$, testing the adjunction units, and testing the unit at $K$. His other criteria are membership of $K$ in the essential image of $\psi$, invertibility of its unit, and the Hom comparison with $C'$. The proof extracts a retraction $p$ of the unit $i$, writes $ip=\psi(q_0)$, and uses the invertibility of this idempotent to conclude that $i$ is invertible. The right margin on scan 39 calls attention to the retraction alone.

**U5 · Scans 41–42.** If $H$ on $C$ factors as $H'\circ\varphi$, the corollary identifies representability of $H$ with representability of $H'$. For representatives $K,K'$ the identifications are $K'\simeq\varphi K$ and $K\simeq\psi K'$. The two directions use the adjunction and the Hom comparison of Proposition 1.

**U6 · Scans 42–44.** The induced functors $\Phi,\Psi$ between the ind-categories are adjoint, and $\Psi$ is fully faithful. Both statements are expressed by taking an inverse limit in the source index and a direct limit in the target index of Hom. Proposition 2 applies the localization criterion to an ind-represented functor. Its proof singles out a gap in a direct application of Proposition 1, since the tests initially range over objects of $C$. For an ind-system the unit is given term by term on the same index set. The author uses this to pass to the required test on ind-objects.

**U7 · Scans 44–46.** Returning to Cat hot and Hot, the author chooses an actual functor $K\to\overline K$ in Cat representing the Thomason–Kan envelope map. For a sequence he chooses transition maps between the envelopes so that the squares commute in Cat. He applies Proposition 2 to the resulting morphism of ind-objects. The functor ind-represented by $K$ takes weak equivalences to bijections exactly when this morphism is invertible in Ind(Cat hot).

**U8 · Scans 46–48.** The explicit path categories $K_n$ have fully faithful transition monomorphisms. Their ordinary direct limit $K_\infty$ is their union as full subcategories. For finite $X$, with both its objects and its arrows finite in number, the page identifies $H(X)$ with $\mathrm{Hom}_{\mathrm{Cat\,hot}}(X,K_\infty)$. The author asks how much these tests determine. He singles out the case where $K_\infty$ is homotopic to a finite category, then considers a sequence of Thomason–Kan categories when $H$ factors through Hot.

**U9 · Scans 49–50.** A strict functor $u_\infty$ sending each $K_n$ into a suitable $K'_{\tau(n)}$ supplies a comparison of the two systems. The author first reasons conditionally on having such a comparison. He reduces existence to realizing the dotted arrow of a square in Cat, then to realizing a retraction strictly. For uniqueness he asks whether homotopy on every $K_n$ implies homotopy of two functors on $K_\infty$.

## Statements left without proof

- **A1 · Scans 35–36.** The Scholie announces «Alors on peut trouver» the ind-object and «un isom can, pour toute catégorie $X$». The page begins in a preceding argument. The whole construction of the stages is outside these sheets.
- **A2 · Scan 39.** The localization Cat hot → Hot is introduced as one «dont on sait qu'il admet un adjoint à droite». Its right adjoint is taken as known.
- **A3 · Scan 45.** One can «choisir» the envelope map as a «cofibration de Thomason». For the sequence, «on peut trouver des» transition maps such that «les carrés … soient commutatifs». The page displays the square and gives no construction of these choices.
- **A4 · Scans 47–48.** With $X$ restricted to finite categories, «cette formule … ne détermine pas» $K_\infty$ in Cat hot up to unique isomorphism. The author singles out the case where it is homotopic to a finite category. No example establishing the claimed limitation is given here.
- **A5 · Scan 48.** Of the suggested direct limit the author writes «Ce sera bien … une catégorie de Thomason-Kan». The closure assertion is left without an argument on this sheet.
- **A6 · Scan 49.** Under the stated stage-preservation and isomorphism hypotheses, «alors $u_\infty$ est forcément un isom. dans Hot». The extension to Cat hot carries the qualification «(sauf erreur)».

## Questions and conjectures

- **Q1 · Scans 37–38.** Does the corollary remain valid «en supposant seulement que $f$ soit une “quasi-isomorphisme” (ou “équivalence faible”)»? If so, is the functor on Hot still ind-representable, and does the image of $K$ represent it? The margin reads «si on a ind-représentabilité comme foncteur sur Hot, cf ci-dessous». The first words of that note are uncertain.
- **Q2 · Scan 44.** «Il n'est pas évident à priori qu'elle passe aux objets quelconques» concerns extension of the unit test. The termwise argument that follows addresses this particular doubt.
- **Q3 · Scan 45.** «et en particulier une imm ouverte ?» asks about an additional property of the chosen cofibration. The point after the abbreviation is uncertain.
- **Q4 · Scans 46–48.** «Je ne sais donner d'interprétation de ce type ni de la catégorie $K_\infty$ elle-même, ni de son image dans Cat hot, ni de son image dans Hot.» Of the finite exceptional case he adds «Je ne me rends pas bien compte si … arrive très souvent».
- **Q5 · Scan 48.** «Il doit être facile … de s'arranger pour que les foncteurs de transition soient des mono et pl. fid.» is an expectation about the choice of sequence. «Cette catégorie est-elle déterminée par le foncteur $H$ … dans Cat hot ?» asks about uniqueness of its limit. The aside «ce qui ne doit pratiquement jamais être le cas» refers specifically to the ind-object being essentially constant.
- **Q6 · Scan 49.** «ce qui n'est pas évident, c'est l'existence d'un hom $u_\infty$ comme dessus», and, if it exists, whether it is unique «(ou du moins canonique ?)» as an arrow of Cat hot.
- **Q7 · Scans 49–50.** Can the arrow given «en pointillés» in Cat hot be made into a functor making the square commute «pour de bon»? In the reduced problem, «on veut la réaliser par une vraie rétraction». A question mark stands in the margin.
- **Q8 · Scan 50.** For two functors whose restrictions to each $K_n$ are homotopic, even «en tant que foncteurs de $K_n$ dans un $K'_N$ convenable», the sheet ends with «sont-ils homotopes ?». The slanted note specifies the Thomason assumptions on the categories and stages.

## Slips

| ID · scan and approximate lines | Frozen reading | Proposed reading and grounds |
|---|---|---|
| S1 · 40, 6–9 | $\mathrm{Hom}_C(\varphi X,K')$ at the upper right of the triangle | $\mathrm{Hom}_{C'}(\varphi X,K')$. Both arguments are objects of $C'$, and the adjunction display immediately above has $C'$. Medium confidence. |
| S2 · 41, 18–19 | «puisque $\varphi(i)$ et $\varphi(i)$ le sont» | The second factor should be $\varphi(p)$. The preceding product explicitly has the two distinct factors $\varphi(i)\varphi(p)$, and the preceding sentence established invertibility of $\varphi(p)$. High confidence. |
| S3 · 42, 19–20 | The arrow labelled $\Psi=\mathrm{Ind}\,\psi$ points from Ind $C$ towards Ind $C'$ | Reverse the upper arrow. In the very next formula $\Psi$ takes $X'$ to the category containing $X$. Medium confidence. |
| S4 · 42, 24–26 | Two occurrences of $X'_j$ inside direct limits indexed by $i'$ | Read $X'_{i'}$ if the indicated limit index is retained. The page introduced $X'=(X'_{i'})_{i'\in I'}$ and supplies no binding for $j$. High confidence. |

**Reading questions.** Each is low confidence as a slip.

- **D1.** On scan 39, margin, lines 21–26, «$\psi\varphi(X)$ sur $X$» could use $K$ in both positions if the note retains the preceding parameter $\mathrm{id}_K$. A change of dummy letter is also possible.
- **D2.** On scan 41, lines 21–24, the subscript of the identity is frozen as $K$ or an unresolved mark. The source of $q$ suggests $\psi(K')$, although the strokes do not establish it.
- **D3.** The closing implication on scan 41, lines 21–24, appears to end in (ii)″ or (ii′). The announced goal on scan 40 favours (ii′).
- **D4.** On scan 43, lines 21–22, $\varphi(K)$ could mean the induced $\Phi(K)$ by abbreviation.
- **D5.** On scan 44, lines 10–12, the frozen $Z_i$ or $Y_i$ follows a pair declared as $(X_i),(Y_i)$.
- **D6.** On scan 47, lines 14–16, the subscript $Y$ on the second endpoint could be $X$, as in the first formula, and the base letter is overwritten.

## Pointers

- **Scans 36–38.** «l'énoncé du Scholie» and «implicite dans le Scholie» refer back to scan 35. The slanted «cf ci-dessous» points forward within the argument.
- **Scans 39, 44–46.** The right adjoint is called «enveloppe de Kan» or «représentant de Kan». The application uses «l'enveloppe de Thomason-Kan» and «cofibration de Thomason».
- **Scans 42–45.** «la prop.» on scan 42 refers to Proposition 1. Scan 44 explicitly invokes «prop. 1», and scan 45 refers to conditions of «la prop 2».
- **Scans 48–50.** «catégories de Thomason-Kan» recurs in the discussion of limits. The strict retraction problem specifies «une catégorie de Thomason» and «une cofibration de Thomason». No title of a paper or reference to a numbered archival cote appears on these sheets.

## Remarks of the model

- **R1 · Model remark, high confidence · scan 41.** The displayed $pi=\mathrm{id}_K$ suffices for the parenthetical $q^2=q$ with $q=ip$. This elementary check uses only the order of the two composites on the sheet.
- **R2 · Model remark, high confidence · scans 46–47.** For a functor from one of the specified finite test categories into the stated union, all its object and arrow images fit into one common stage because there are finitely many images and the stages are nested. This checks the finite-support point in the argument.
- **R3 · Model remark, high confidence · scans 49–50.** The last hypothesis provides a homotopy separately for each source stage, with a suitable target stage allowed to depend on it. The question supplies no compatibility among the chosen homotopies. That is the distinction between the data stated locally and the global conclusion being asked for.
