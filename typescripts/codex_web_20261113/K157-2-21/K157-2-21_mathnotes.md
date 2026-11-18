# K157-2-21 · Mathematical notes

## What the pages do

**U1 · The fundamental groupoid (323–324).** A constant path of type $\tau$ comes from the one-object type by $p_\tau^*$. The category of path classes is named the *groupoïde fondamental* $\Pi(X)$. The proposed functor from $X$ fixes objects. To see why a single arrow $u:a\to b$ has an inverse there, the author writes the forward and backward paths defined by the same $u$. Two diagrams relate their round trips to the identities at the endpoints.

**U2 · Reversal of an arbitrary path (325–326).** Reversing a type word reverses its order and exchanges its two generators. An example tracks the individual arrows $u_1,\ldots,u_5$ and then $u_5,\ldots,u_1$. Formula $(*)$ gives the order of the two factors in the reverse of a composite. The slanted note on 325 uses this to dispense with the proposed induction.

**U3 · Paths with restricted backward arrows (326–328).** A class $\Sigma$ of arrows is specified. A path and its reverse are both $\Sigma$-paths precisely when all its arrows lie in $\Sigma$; the writer calls such a path strict. The inverse-image functors for changes of type lead to two conditions on $\Sigma$, containment of identities and closure under composition. The resulting full categories of paths form a fibered subcategory. Their connected components supply the morphism sets of $\Pi_\Sigma(X)$. Reversal need not preserve an unrestricted $\Sigma$-path.

**U4 · When the specified arrows are already invertible (329–332).** The functor $k:X\to\Pi_\Sigma(X)$ takes an arrow to the class of its one-step path. If the arrows of $\Sigma$ are already invertible in $X$, the proposed inverse on a morphism set evaluates a path by replacing its backward arrows with their inverses and composing in $X$. One verification compares a reversed one-step path with the forward path of its inverse. A second identifies a forward path with the one-step path of its composite.

**U5 · Functoriality (332–334).** For $f:X\to X'$ with $f(\Sigma)\subset\Sigma'$, the maps on categories of paths induce maps on their connected components. Compatibility with composition and with the empty path gives a functor between the two categories of path classes. The uniqueness argument uses the one-step classes and the inverses of the classes coming from $\Sigma$.

**U6 · Universal property (334–335).** For a functor taking the arrows of $\Sigma$ to invertible arrows, take $\Sigma'$ to be the invertible arrows of $X'$. In the square on 335 the lower horizontal map $k'$ is then an isomorphism. The dashed diagonal gives the factorization through $\Pi_\Sigma(X)$, and the text concludes with its uniqueness.

**U7 · Components and homotopy of objects (335–336).** The discussion turns from classes of paths to a path as a homotopy between its endpoints. Two homotopic objects represent the same element of $\pi_0(X)$. A path of either one-step type is called *simple*. The author asks for a short representative between given endpoints.

**U8 · Useful length and homotopies of functors (336–337).** The reduced type retains one step for each run of equal signs. Its length is the number $r$ of runs; the original length counts all their steps. The closing paragraph places a homotopy between functors $X\to Y$ in the category $\underline{\mathrm{Hom}}(X,Y)$ or in a subcategory specified by the context.

## Statements left without proof

- **P1 · 328, lines 6–8.** « Il est évident que cette sous-catégorie est stable par l’opération de composition des chemins ». The text goes on to explain the obstruction to reversal. It gives no separate proof of closure under composition at this point.
- **P2 · 331, lines 14–23.** For the general $\Sigma$-path argument the writer invokes what was « prouvé … dans le cas de $\Pi(X)$ ». The applicability of that earlier argument to the reversed one-step path is asserted in the terms quoted in Q1.
- **P3 · 336–337, especially 337, lines 1–4.** Replacing the type by its reduced type, « on trouve une homotopie … dont la longueur est égale à la “longueur utile” ». The resulting type and length are displayed. The construction of each compressed step is left implicit here.

## Questions and conjectures

**Q1 · 331, lines 14–23.** « L’argument doit marcher, du moment qu’il a un sens ». The stated condition is that $\mathrm{ch}(u)^\circ$ should be a $\Sigma$-chemin, expressed in the text as $u\in\Sigma$. This is the author’s explicit qualification of a proof step. These leaves carry no separately formulated conjecture.

## Slips

| ID and place | Written form | Possible correction and reason |
| --- | --- | --- |
| S1 · 326, last line / 327, first line | « les flèches rétrogrades sont dans $X$ » | The apparent defining condition is « dans $\Sigma$ ». The next sentence tests both directions by membership in $\Sigma$. Confidence medium for the intended substitution. |
| S2 · 329, line 23 | « inverse de $\beta$ » | « inverse de $\alpha$ ». The map being defined is $\beta$, with domain and codomain reversed from those of $\alpha$. Confidence high. |
| S3 · 331, line 5 | « de $b$ vers » | The absent endpoint would be $a$, as shown in both paths immediately below. Confidence high. |
| S4 · 333, lines 8–11 | « quand ces inverses sont inversibles » | Probably « quand ces flèches sont inversibles ». The following example takes inverses of $k_X(u)$ for $u\in\Sigma$. Confidence medium for this wording. |
| S5 · 334, line 2 | Target $\mathrm{Hom}_\Sigma(f(a),f(b))$ | A target subscript $\Sigma'$ would match $\Pi_{\Sigma'}(X')$ in the preceding square. Confidence medium. |
| S6 · 337, lines 6 and 8 | Last sign $(-1)^r\varepsilon$ in the reduced row | If the brace counts $r$ signs beginning with $\varepsilon$, the last is $(-1)^{r-1}\varepsilon$. With one block, the displayed end would otherwise be $-\varepsilon$. Confidence low as a manuscript slip because the parallel upper line is doubtful and partly overwritten. |

## Pointers

- **325, left margin → 326, line 5.** « la formule $(*)$ page suivante » points to $(\gamma'\gamma)^\circ=\gamma^\circ\gamma'^\circ$. A possible dot between the primed and unprimed factors in the manuscript is marked in the transcription.
- **331–332 → 330.** « La formule (2) signifie que » introduces the second verification. The earlier numbered formula identifies the forward path with the path of the composite.
- **334, left margin; 335, lines 11–15 → earlier discussion.** « C’est inutile » and « ci-dessous » accompany the uniqueness discussion. On 335 « comme on a vu tantôt » refers back to the invertible-arrow case treated on 329–332.

No other cote, external paper or person is named as a reference on these leaves.

## Remarks of the model

- **R1 · 325, lines 18–23. Model observation, low confidence for the disputed last sign.** Taking the arrow directions in the first diagram gives $+,-,+,+,-$. Reversing the order and changing signs gives $+,-,-,+,-$, in agreement with the written second type. This favours a minus in the ink blot at the end of the first type.
- **R2 · 330, line 20; 332, lines 4–6. Model observation, medium confidence.** Scan 330 starts the displayed factorization with $c_n$. On 332 the starred string starts with $c_1$, while the string of homotopy classes on the next display starts with $\mathrm{hot}(c_n)$. Path traversal and categorical composition can account for opposite listing orders. The leaves give no explicit new convention at this point.
- **R3 · 324, lower diagram. Model reading question, low confidence for any proposed correction.** The detached bottom object reads $a$ in both diagrams. The lower caption has $1_b$, which prompts the alternative $b$ for a reader following the argument. The detached letter itself looks like the $a$ in the upper diagram.
