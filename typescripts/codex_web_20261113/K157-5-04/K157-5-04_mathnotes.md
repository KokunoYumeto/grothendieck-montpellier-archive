# Mathematical notes on cote 157-5, scans 52–60 and 62–68

## What the pages do

**M1 · Scans 52–53. A category with cofibrations.** Grothendieck starts with an initial object and two classes of arrows in $M$. His four conditions give the two-out-of-three property for $W$ along with the isomorphisms, stability properties for $C$ and $TC=C\cap W$, and a factorization $f=pi$ with $i\in C$ and $p\in W$. He compares these conditions with the dual of Brown’s. He passes to the subcategory of cofibrant objects $M_C$ to discuss localization, including versions with prescribed source or target.

**M2 · Scans 53–54. Homotopy and fractions.** He describes $\mathrm{Ho}_W(M)$ using left fractions in $\pi M_C$. For two arrows with the same endpoints, he first changes the source along a weak equivalence from a cofibrant object. The cylinder diagram then tests whether the two resulting maps extend to a single map from the cylinder. He relates this criterion to exactness of $W$-cocartesian squares.

**M3 · Scans 54–57. Cofibrations of diagrams.** For $M(I^{\circ})=\underline{\mathrm{Hom}}(I,M)$, he uses the two classes from the preceding section. The step-shaped diagram on scan 55 checks composition by factoring the comparison map indexed by $K,J$. The cube on scan 56 checks change of base. Its last face gives a cocartesian square on the maps $u_{K,J}$ and $u'_{K,J}$. He suggests expressing both arguments through the composition of what he calls $C$-squares.

**M4 · Scan 57. The trivial cofibrations.** To obtain the second stability condition, he invokes the identification of $C_{I^{\circ}}\cap W_{I^{\circ}}$ with $(TC)_{I^{\circ}}$. This introduces the alternatives concerning the order on $I$, the noetherian condition on its opens, and transfinite composition.

**M5 · Scans 57–60 and 62. Extending a factorization.** He orders partial factorizations on opens by extension. A totally ordered family gives data on its union. For a maximal partial factorization he adjoins a minimal element of the complement and reduces the extension to a poset with a final object. The two diagrams on scan 60 isolate the component to be supplied there. On scan 62 he forms the pushout $Z'_0$, factors its map to $Y_0$, and takes $i_0=j_0i'_0$. This finishes the construction begun on scan 57.

**M6 · Scan 63. Théorème 3.1.** The theorem packages the preceding verifications. For artinian $I$, it gives the diagram category a structure with cofibrations if $\mathrm{Top}(I)$ is noetherian, or if $C$ and $TC$ admit transfinite composition under the stated colimit hypotheses. The opening insertion says that M is stable under finite “lim”. The mark below the word may be a colimit arrow. In the second case the two smallness qualifications and the colimit arrows are visible.

**M7 · Scans 63–67. Proposition 3.2.** An increasing map $u:I\to I'$ gives an adjoint pair. Part a) considers $u^*$. The live proof uses cofinal maps on opens to identify the vertical arrows of a comparison cube. Part b) considers $u_!$. Inverse images of two opens and compatibility with restriction give a corresponding comparison. He concludes preservation of the indicated cofibrations, trivial cofibrations and cofibrant objects.

**M8 · Scans 67–68. Corollaire 3.3.** The restricted $u_!$ carries weak equivalences of cofibrant diagrams to weak equivalences and yields the functor written $u_!^W$ in (3.3.1). The proof uses the identification of trivial cofibrations and begins a factorization argument for arrows between cofibrant objects. The supplied text ends at “Alors”.

## Statements left without proof

- **U1 · Scans 52–53.** “de plus on … prouve que” the map from $\mathrm{Ho}_W(M_C)$ to $\mathrm{Ho}_W(M)$ “est une équivalence”. These pages also apply Brown’s results to the listed “avatars” with fixed ends. They give no proof here.
- **U2 · Scans 53–54.** “il y a une bonne théorie des carrés $W$-cocartésiens”, “il y a assez de $W$-cofibrations”, and “C’est de ce critère que résulte l’exactitude … des carrés $W$-cocartésiens”. He gives the criterion and asserts its application to exactness. The short insertion after “l’exactitude” on scan 54 reads “à g.”, with “à Q.” and “à D.” also possible. The small loop and its downstroke leave the qualifier open.
- **U3 · Scan 55.** “L’axiome Cof₀ est immédiat, et bien connu pour $I$ une catégorie quelconque.”
- **U4 · Scans 57 and 68.** The equality involving $(TC)_{I^{\circ}}$ is taken from earlier results. Scan 57 says “de façon à pouvoir appliquer le th. 2.1. et son corollaire 2.5.” Scan 68 says “par Th. 2.1. 3° (p. 27)”.
- **U5 · Scans 64–65.** “On applique II 7.4 …”, followed by the assertion that the induced map on slice orders is cofiltrant and the induced map of opens “a fortiori cofinal”. The citation and its page number carry doubts. The comparison argument uses this assertion.
- **U6 · Scans 67–68.** “On procède de = pour $TC_I$” abbreviates the analogous verification. “par la théorie des cat à cofibrations, on trouve que toute flèche … entre objets cofibrants est composée $f=pi$” invokes a factorization in which $p$ is an “inverse à gauche”. The immediate application continues beyond the last supplied sheet.

- **U7 · Scan 68, diagonal NB.** “Cette flèche est définie, = sans supposer I′ ordonné”. The note extends the assertion about weak equivalences to this setting and gives a short page reference whose number is uncertain.

## Questions and conjectures

- **Scan 53.** “ou faut-il dire à gauche ?” questions the terminology “à droite”. His follow-up describes the exactness in question. “Il … faudra revenir dessus de façon plus circonstanciée par la suite” defers a fuller account.
- **Scans 55–57.** “Il y aurait lieu d’introduire la notion de $C$-carré” leads to “il y aurait un lemme commun à dégager”. Both are suggestions for reorganizing the arguments.
- **Scan 57.** “je ne vois pas de façon de le faire, si je ne sais déjà que” introduces the equality needed for Cof₂. “L’axiome de factorisation me paraît … le plus délicat” introduces the subsequent construction, which the author explicitly finishes on scan 62.

## Slips

| ID | Scan and place | Written form | Apparent intention and reason | Confidence |
|---|---|---|---|---|
| S1 | 56, lower face of the cube | $Y'_{J,K}$ | $Y'_{K,J}$ would retain the order in the corresponding unprimed vertex $Y_{K,J}$. The adjacent primed arrow also seems to use that order. | Low for the inference from the overwritten adjacent label |
| S2 | 59, prose immediately before the open-set square | $K=J\cap K$ | $K=J\cap K'$ is the expression actually written inside the adjacent square. | High |
| S3 | 59, immediately below that square | “$(Z\mid K',i\mid K',p\mid K')$ à $K$” | The extension step starts with restrictions to $K$ and extends them to $K'$. The primes in this sentence run in the opposite direction to the inclusions drawn above it. | High |
| S4 | 60, line before the second diagram | “sur $J'$” | “sur $I'$” would match $f'=f\mid I'$ just above and the left-hand indices in the diagram that follows. | High |
| S5 | 62, first hypothesis | $p\in W_{I'^{\circ}}$ | $p'\in W_{I'^{\circ}}$ would match $i'$ in the same clause and the pair at the foot of scan 59. | Medium |
| S6 | 64, live assertion b) | $TC'_{I'^{\circ}}$ | $TC_{I'^{\circ}}$ is the target spelling used later. The extra high mark may be a local way of distinguishing the target. | Low |

## Pointers

- **Scans 52–53.** “Axiomes de K. S. Brown”, “les résultats de Brown”, and the starred “plus précisément, par K.S. Brown”. The marginal qualification concerns $M_C$.
- **Scan 54.** “au sens de Quillen-Brown” and “au sens de Quillen” in the cylinder criterion. Scan 57 names Quillen again in the slanted note, whose last classes are uncertain.
- **Scan 55.** “au § précédent” for the classes on diagrams. **Scan 57.** “Comparer le diagramme similaire p. 32”, “le th. 2.1. et son corollaire 2.5.” **Scan 58.** “par Zorn”.
- **Scan 62.** “par th. 2.1 1° (cor. 2.2)” and “d’après le th. 2.1 2°”. The abbreviation before 2.2 is uncertain.
- **Scan 63.** “cf page 39” and “défini au §2 (cf à ce sujet le th. 2.1)”.
- **Scan 64.** “condition … 1 sur $i'\backslash I$” and “II 7.4 (p. 92)”. Lettering in the condition and the latter page reference should be checked on the cited material.
- **Scans 67–68.** “de Prop. 3.2. et Th. 3.1”, “par Th. 2.1. 3° (p. 27)” and a further “Donc par 3.2”, with an uncertain final digit. The marginal “Cf. … p. 86” is particularly faint.

## Remarks of the model

- **R1 · Model, high confidence for the finite check.** On scan 59 the union $J\cup\{i_0\}=J\cup I_{/i_0}$ and the strict lower set $J\cap I_{/i_0}=I_{<i_0}$ fit together. I tested both equalities for all 8,461 choices of a downward-closed $J$ and a minimal point outside it across the 407 order relations on one to five increasingly labelled points. Both equalities held in every tested case.
- **R2 · Model, high confidence in the identity for the live labels.** On scan 62 the order of the factors in $i_0=j_0i'_0$ agrees with $p'_0=p_0j_0$. Substitution gives $p_0 i_0=p'_0 i'_0$, with both sides going from $X_0$ to $Y_0$.
- **R3 · Model, low confidence.** Scan 58’s opening counted word resembles “triples”. The immediately following display has four entries and the later sentence says “quadruples”. “4-tuples” is a reading question about that word’s initial strokes.
- **R4 · Model, low confidence.** The label left of scan 60’s final diagram looks like “(M”, while scan 62 calls a diagram “(*)”. The discrepancy leaves the intended diagram label open.
- **R5 · Model, low confidence.** At the foot of scan 68, immediately before “d’une flèche de $(TC)_{I^\circ}$”, the transcription gives a cancelled “de la”, with live “donc” as the alternative. The initial d is clear. A dark loop blends into a horizontal stroke through the rest of the word. “Donc” would connect the two descriptions of the arrow. The stroke leaves both the wording and the cancellation in doubt.
