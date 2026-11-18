# Mathematical notes on 161-3, scans 004–021

## What the pages do

**U1 · A category of bifaisceaux, 004–005.** The opening display gives several descriptions of Π(E,F). On sites C and D for E and F, its objects are functors on Cᵒ×Dᵒ which are sheaves separately in each variable. The author begins with two presheaf topoi, passes to a sheaf condition in one variable, then takes the intersection of the two resulting subtopoi. This gives the claim that Π(E,F) is a topos.

**U2 · Functoriality and the two projections, 005–006.** For u:E→E′ and v:F→F′ the proposed direct image evaluates a bifaisceau at (u*X′,v*Y′), where both stars are raised. The corresponding inverse-image expression stops at a question mark. Factoring the map allows the author to work with one morphism at a time and to compare sheaves with presheaves. Taking F→P to the point gives the projection to E. The other projection gives the comparison with the 2-product.

**U3 · Universal property, 007–008.** The author reduces to the presheaf case. Maps from X to Ĉ and D̂ are described using the opposite categories of finite-limit-preserving functors into X. A pair of such functors gives one on C×D by taking the product of their values. The inserted warning distinguishes preserving finite limits on the category of pairs from preserving them separately. The two terminal objects enter when extracting the pair of functors again.

**U4 · Families of topoi, 008–009.** The restricted product of the small categories consists of families terminal at almost every index. For subtopoi E′ᵢ⊂Eᵢ the author takes the inverse image of each E′ᵢ under its projection and intersects these subtopoi. The test for a map from X to factor through the intersection is componentwise. This yields the corollary on products of arbitrary families. A separate, cancelled draft below sketches an inverse limit of a fibred topos using successive products indexed by objects, arrows and pairs of arrows.

**U5 · Two topologies on rectangles, 010–012.** The author compares the topos of the topological product with the product of the two topoi. He distinguishes the topology π defined by the separate sheaf conditions from π′ induced by X×Y. To compare them he asks whether a set-theoretic union of rectangles gives the same supremum as subobjects. A quasi-compact neighbourhood provides a finite cover over a fixed y. A second argument takes the largest open U′ for which the inequality holds and enlarges it from a locally closed complement. A diagonal note on 010 gives a related formulation in terms of points.

**U6 · Infinite topological products, 012–015.** The argument passes through finite subproducts Zα and opens pulled back from them. In the compactness step the author fixes a point in a finite stage, covers the complementary factor by finitely many rectangles and then enlarges the point to an open neighbourhood. Next he takes discrete factors and tries to distinguish the two topologies when infinitely many factors are infinite. Scan 015 constructs a family Vz indexed by points and ends in the middle of the question about coverage.

**U7 · Filtered limits of presheaf topoi, 016.** The author asks whether essential transition morphisms suffice to make the limit and its projections essential. For the calculation he assumes site functors with stated adjoints and describes the limit as a presheaf topos on a direct limit of categories. He writes the direct image under a projection as restriction along αᵢ. The proposed inverse image ends at the equals sign.

**U8 · Restriction, extension and their comparison maps, 018–019.** Restriction α composes u with εC. Extension β sends a sheaf F to the colimit of u₀ over C/F. The maps i:βα→id and j:id→αβ are constructed from that colimit, with components at F and at Z, respectively. Applying Hom(−,ξ) turns the test for j to be an isomorphism into an inverse-limit test for a presheaf. A final object in the slice explains the case in which εC is fully faithful. The adjunction is then announced.

**U9 · Extension through sheafification, 020–021.** The same question is taken up after identifying functors on C with colimit-preserving functors on Ĉ. The new α′ composes with sheafification a; β′ restricts along the inclusion j. The calculation transports a colimit across a and identifies the essential image using functors that invert morphisms made invertible by a. The last question asks whether taking covering families to epimorphic families suffices. The marginal answer is « non ».

## Statements left without proof

| ID | Scan and manuscript words | Extent of the claim |
|---|---|---|
| P1 | 008 L3–10, « plus généralement … alors » followed by the equivalence involving the hatted restricted product | The page gives the formula for an arbitrary family. The adjacent verification treats two variables. |
| P2 | 010 left margin, « Analogue pour produit d'une famille quelconque » | The extension of the points argument to an arbitrary family is asserted briefly. |
| P3 | 016 L13–18, « On trouve alors » | Under the extra site hypotheses the limit-topos formula and description of the projections are stated. The leaf has no derivation of the inverse-image formula. |
| P4 | 019 L20–24, « On va prouver que i,j sont des données d'adjonction associées pour les foncteurs α et β » | The components have been constructed; no check of both triangular identities is written here. |
| P5 | 020 L19–24, « et on sait que … commute aux lim », « cf rappel plus bas » | The presheaf extension and its equivalence are used in changing the description of α and β. |

## Questions and conjectures

| ID | Scan | Manuscript words or marks | Status within these leaves |
|---|---|---|---|
| Q1 | 005 L11 | `π(u,v)^*(φ)(X,Y)` with a question mark above `=` | No value is entered. |
| Q2 | 006 L27–28; 007 | « On veut prouver que c'est une … équivalence » | The comparison with the 2-product is argued on 007. |
| Q3 | 010 L14–19 | « voir si ce plongement est une équivalence i.e. π=π′ » | Sufficient conditions and a refinement follow on 010–012. |
| Q4 | 013 L20; 015 L8–9 | « Contr'exemples pour des produits infinis »; « La question est de voir si tous ces » (struck); « ou encore »; marginal « ? » | The proposed discrete example has no completed demonstration here. |
| Q5 | 016 L6–7 | « Il est douteux qu'alors … soit un topos essentiel et ses projections … des morphismes essentiels. » | A computation under a stronger assumption follows. |
| Q6 | 020 L4–5, L19–21 | « commutant aux lim (petites) ? »; « Mais il n'est pas clair que … β(u₀) soit dans Hom′. » | This motivates changing from C to Ĉ. |
| Q7 | 021 L12–20 | « Est-il vrai que dans cette identification, les foncteurs qui commutent aux lim petites se correspondent ? » | The colimit calculation ends with « OK. ». |
| Q8 | 021 L30–33 | « Cela est-il suffisant ? Supposons cette condition remplie, »; « non » | The question is answered in the margin. There is no counterexample on this leaf. |

## Slips

Confidence concerns the proposed correction. The page files preserve the written forms.

| ID | Scan | As written | Proposed reading of the intention and reason | Confidence |
|---|---|---|---|---|
| S1 | 006 L1–5 | F′ as the second argument of Π(id_Ĉ,F′) | v. The factorization on 005 fixes the first variable and applies the morphism v in the second. F′ is its target. | High |
| S2 | 006 L14–19 | « dont l'adjoint à droite est » preceding φ↦v*∘φ (raised star) | « à gauche ». In the Hom calculation v* is on the first argument on the F side; v_* is on the second argument on the F′ side. | High |
| S3 | 008 L7–10 right | Plain φ in the second factor in the last two lines | φ′ would agree with f(x,x′) and with the preceding line. The prime could be too faint to separate from the ink. | Low |
| S4 | 009 L1–8 | « X se factorise par F », then Hom top(X,F) | The map f factors, and the intersection was named E′ on 008. Replacing X by f is strongly indicated. Replacing F by E′ assumes that F was not a temporary new name for the intersection. | High for f; medium for E′ |
| S5 | 010 L7–14 | Top(X×Y) at the start of the account of sheaves for π | The 2-product of Top(X) and Top(Y) would fit the separate sheaf conditions. Later lines put Top(X×Y) on the π′ side and ask when the two agree. | Medium |
| S6 | 013 L7–8, L17–18 | `z∈W` and the last `W×Z′α` | U for W in both places would fit the declared domains: W=U×Z′α while the U_z lie in Zα. The initial z occurs beside an overwrite. | Low |
| S7 | 015 L6–7 | `z′ᵢ=zᵢ` for `i∈I−J(z)` | Fixing i in the stated finite set J(z) gives a usual open cylinder. The complement condition fixes all other coordinates. The surrounding argument is unfinished and contains deletions. | Low |
| S8 | 020 L14–16 | `β:Hom(C,E)→Hom(C,E)` | Hom(C̃,E) for the target. The next display evaluates the resulting functor at F, and β′ below has the sheaf category as its source variable. | High |

## Pointers

| ID | Scan and words | Referent on the supplied leaves |
|---|---|---|
| T1 | 006 L1–2, « dans la dém de prop. 1 »; 007 L1–2, « comme dans la dém. de prop 1 » | The construction starting at the numbered proposition on 004. |
| T2 | 009 L9–10, « Corollaire de a) et b) » | The two parts on 008. |
| T3 | 012 L15–17, « un corollaire immédiat de ce qui précède » | The finite-factor comparison argued just above. |
| T4 | 012 L24–26, « un argument tt analogue » with « à dessus » inserted | The preceding comparison by covers. |
| T5 | 019 L20–24, the words after « qu'on a décrit » | A backward reference is plausible. The candidates include « auparavant », an abbreviated paragraph reference, and « au préal. ». No external reference can be identified from the ink. |
| T6 | 020 L22–24, « cf rappel plus bas » | A promised reminder of the presheaf calculation. |

No person, named publication or other archive cote is explicitly cited.

## Remarks of the model

**R1 · 007–008 · High confidence.** The inserted warning about exactness in a pair of variables explains the appearance of e_C and e_D. Restricting the product formula to (a,e_D) and (e_C,b) recovers the two original values because a finite-limit-preserving functor preserves terminal objects. This checks the direction of the recovery maps used here.

**R2 · 010–012 · High confidence.** The equality of the two rectangle topologies is a stronger conclusion than the inclusion already on 010. The proof needs the passage from a set-theoretic cover to a supremum in the category of sheaves. The separate supremum over y and then over x on 011 addresses precisely that passage.

**R3 · 013–015 · Low confidence.** The discrete example could be testing the failure of the finite-stage cover argument. The section heading and the noncompact factors point that way, but the choice of coordinates in Vz and the unfinished « ou encore » prevent recovering the intended counterexample from these leaves.

**R4 · 018–021 · High confidence.** There are two different tests in the last question. The calculation identifies the functors on Ĉ that invert each map inverted by a. The final paragraph deduces a condition involving epimorphic families in E. The margin says « non » at the attempted converse. The missing argument cannot be inferred from the preceding formal identification alone.
