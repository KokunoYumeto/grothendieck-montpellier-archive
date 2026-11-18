# Mathematical notes · 157-2, scans 18–33

## What the pages do

**018–019 · Comparing two functors.** Grothendieck reduces the homotopy of $f,g$ to that of $f',g'$ and then to that of $\varphi,\psi$ in a functor category with a prescribed restriction. The lemma on 019 concerns functors $\mathscr L_k\to\mathscr L_l$ preserving source and target. The slanted note says that the functors under consideration are increasing for the numbering of the vertices. It proposes adding the subscript $\mathrm{cr}$ to Hom.

**019–021 · Recording a functor by the arrows it contracts.** The subset $E_\varphi\subset[1,2k]$ records the arrows sent to identities. Collapsing its connected components gives a quotient interval. Its initial direction determines whether it has the required orientation. The list on 021 prescribes the cardinality $2(k-l)$ (statement A21), the parity of interior components and the conditions at the two ends. Uniqueness of the functor uses the lemma about automorphisms of the quotient interval.

**022–023 · Moving a connected subinterval.** Agreement of $E$ and $E'$ on an initial or final segment gives agreement of the functors on the indicated objects. Moving a connected subinterval of even cardinality one place to the left gives a morphism between the two functors. The corollary treats a move to the right. Repeated moves are used to reach $[1,2(k-l)]$ in the equal-parity case and $[1,2(k-l)-1]\cup\{2k\}$ in the opposite-parity case. This is the argument for connectedness.

**023–025 · Composition and identities.** Composition of paths gives a map on connected components. Grothendieck writes strict associativity for three paths of even index and takes the path of index zero at $x$ for $1_x$. He names the resulting category $X_\Sigma$. The proposed functor from $X$ fixes objects and sends an arrow to the path drawn on 025 with three identity labels. The two representatives needed for the identity check already agree at the indicated stage.

**025–028 · Compatibility with composition.** The two candidates for the image of a composite are extended to comparable paths. The triangles on 026–027 reduce their comparison to a homotopy between functors $\mathscr L_4\to\Delta_2$ preserving endpoints. The simplex symbol has a doubled left stroke. Grothendieck introduces generalized intervals of length $n$ specified by $n$ signs, giving $2^n$ choices. He provisionally assumes the particular connectedness statement he needs.

**028–029 · Inverting an arrow.** For $u\in\Sigma$ the reverse step, padded with identities, gives a candidate inverse $c$. Grothendieck draws both composite paths and compares them with constant paths at $x$ and $y$. This time the target of the interval functors is $\Delta_1$. The sheet ends with $\operatorname{Hom}_{X\Sigma^{-1}}(x,y)\simeq\pi_0\underline{\mathrm{Ch}}_\Sigma(X;x,y)$ and the corresponding statement about composition. The preceding argument refers back to the general lemma.

**030–032 · Paths in a category of diagrams.** In §3 the letter $M$ takes over the role of the original category and $X$ indexes diagrams. In $M(X)=\underline{\mathrm{Hom}}(X,M)$ an arrow belongs to $\Sigma_X$ when its value at every $x$ belongs to $\Sigma$. The calculation starts with the constant diagrams $a_X,b_X$. Writing a path at stage $n$ as a functor $\mathscr L_n\times X\to M$ gives a description by functors $X\to\underline{\mathrm{Ch}}(M)$ that factor through a single stage. Scan 032 gives the corresponding $\Sigma$-path formula and presents the system of stages as an ind-object, with a double underline.

**033 · Source and target of a diagram of paths.** Composing the functor associated to a path $c$ with source and target yields the two diagrams $F_0,F_1$. The square compares their evaluation on both sides of the path-category identification. With these endpoints fixed, Grothendieck begins to identify the category of paths with a category of admissible functors. The underlined verb at the lower edge is read «relèvent» or «relient». The complement continues beyond the sheet.

## Statements left without proof

| Scans | His words | What is asserted or deferred |
|---|---|---|
| 019–020 | «NB Elle est non vide» followed by «ssi» (uncertain) and $k\geq l$. «Il est immédiat qu’un foncteur $\varphi$ est surjectif sur les objets et sur les flèches» | The lemma gives the existence condition in parentheses. Surjectivity is used to identify the target with a quotient. |
| 021 | «Lemme (immédiat)» and «est l’identité sur l’objet source (ou sur l’objet but) est l’identité partout» | An automorphism of the path interval fixing the designated end is the identity. |
| 022 | «(immédiat)», «coïncident», «Dualement» | The lemma about equal initial or final segments states where the functors agree. There is no separate demonstration on the sheet. |
| 023 | «il existe un» and «de foncteurs entre $\varphi_E$ et $\varphi_{E'}$» | Lemme 2 asserts existence of the morphism for the local move. The next paragraph obtains the dual case by reversing the move. |
| 027–028 | «On s’attend à ce que l’énoncé suivant soit vrai» and «Je vais admettre provisoirement qu’il en est ainsi, du moins dans le cas particulier» | The generalized-interval lemma is posed as an expectation. The composition argument uses the case $\mathscr L_4,\Delta_2$. |
| 028–029 | «la propriété universelle de ce foncteur est pratiquement» followed by «évidente» or «immédiate». «Cela doit donc résulter du même lemme général.» | The universal property is asserted in this passage. For invertibility he draws both required comparisons and refers their homotopies to the general lemma. |
| 032–033 | «On trouve aussitôt», «se factorise par», «on a commutativité (stricte)» | The pointwise criterion gives the factorization through the category of $\Sigma$-paths. The following sheet states strict commutativity of the displayed source–target square. |

## Questions and conjectures

- **022–023.** «Je ne vais pas expliciter cette relation d’ordre» and «je ne dis pas dans quel sens va la flèche !» delimit what he needs from the order. The direction of the morphism in Lemme 2 is left open.
- **027–028.** «On s’attend à ce que l’énoncé suivant soit vrai». For the category of compatible functors of generalized intervals he writes «elle est 0-connexe (et, je présume, même contractile ?)» under the hypothesis that it is nonempty. The parenthetical question asks for contractibility in addition to connectedness.

## Slips

**022, condition a), TeX L28 · S22-W and S22-C. High confidence.** The sheet reads «card $I$ est pair (i.e. $s-r$ est pair)» for the closed integer interval $I=[r,s]$. The parenthesis should read «$s-r$ est impair». Both endpoints count, so the cardinality is $s-r+1$. For $[2,3]$ the cardinality is two and the difference is one. The two occurrences of «pair» are clear in the manuscript.

**027, TeX L16–17 · Q27, reading question, low confidence.** The line introducing consecutive integers has $i-1,i$ after a cancellation. The next line says the arrow joins $i,i+1$. Matching them would require changing one of the two pairs. The nearby revision leaves the intended choice unsettled.

## Pointers

| Scans | Words | Referent visible in these sheets |
|---|---|---|
| 018–019 | «déjà envisagé ci-dessus», «triangles commutatifs», «dans les six énoncés qui suivent», «ci-contre» | Earlier comparisons of functors and the statements affected by the monotonicity qualification. The numeral following «triangles commutatifs» looks like (3). |
| 021–023 | «Les foncteurs $\varphi,\psi$ de tantôt», «du type explicité dans le lemme 2», «Ce qui précède justifie notre raisonnement» | The original two functors, the local move and its use for composing paths. |
| 026–029 | «(comme tantôt)», «notre lemme d’homotopie de tantôt», «du même lemme général» | The earlier reduction by endpoint functors and the extension to generalized intervals. |
| 031–032 | «du § 2», «au “calcul”», «où le signe ! a le même sens que plus bas» | Application of the preceding section to constant diagrams. The words on 032 are «plus bas». The finite-stage condition is also explained across the break from 031 to 032. |

No person, named publication or other archive cote is cited on these sheets.

## Remarks of the model

- **R21 · Scans 021–022. High confidence for the component count, low confidence for an intended correction.** Each displayed example, $\{1,2,k-1,k\}$ or $\{1,2,i,i+1\}$, is a union of two adjacent pairs. Each can therefore have at most two components for the stated succession relation. This makes «trois dans l’autre» hard to reconcile with the formulas. A specific missing element or intended example cannot be recovered from these sheets.
- **R23 · Scans 021, 023. High confidence for the finite check.** Both proposed normal forms have the cardinality required in A21 for all 45 pairs $0\leq l\leq k\leq8$ tested here. The computation measured cardinalities only.
- **R! · Scans 022, 031–032. High confidence.** The exclamation mark on Hom has two locally explained uses. On 022 the parenthesis reads «compatible aux source et but». At the foot of 031 and top of 032 the full subcategory consists of functors «qui se factorisent par une des sous-catégories pleines» $\underline{\mathrm{Ch}}_n(M)$. The two descriptions occur beside the symbol itself.
