# K157-2-18 · Mathematical notes

## What the pages do

**Opposite intervals and paths (275–276).** Two directed chains illustrate the signed intervals. Two forks, one with arrows out of the middle object and one with arrows into it, illustrate Φ₁ and Ψ₁. The author distinguishes reversing the arrows of a category from reversing the orientation assigned to a fixed underlying interval. In the latter case the category of diagrams is the same up to the indicated canonical comparison, while the meanings of source and target change.

**Evaluating a path at its ends (276–277).** A path consists of an orientation ω and a diagram $c:I\to X$. For a fixed oriented interval the functor to $X\times X$ evaluates $c$ at the two distinguished objects. The page writes this as $c\mapsto c\circ\alpha$, with $\alpha$ defined on the discrete category $\varepsilon=\{0,1\}$.

**Two comparisons for opposite orientations (277–278).** The square on 277 compares the two evaluations over $s(x,y)=(y,x)$. If an automorphism θ of the underlying interval exchanges its endpoints, the triangle on 278 compares the path categories over a single $X\times X$. Grothendieck names the signed chains and the fork examples when discussing which intervals have this symmetry. The longer explanation below the triangle, including two drawings of each fork, has been crossed out.

**A combinatorial type and a law on paths (279).** The type τ is specified by a finite sequence of signs. It determines a standard oriented interval $I_\tau$. A law taking paths of type τ to paths of type τ′ must commute with applying a functor $f:X\to X'$. The four path sets and the two vertical operations $L_X,L_{X'}$ appear in a square.

**Representing the laws (280–282).** On the example $a_0\to a_1\to a_2$, a law can return the composite or return the composite followed by an identity. In general the set of paths of type τ is represented by $I_\tau$. A functor $\varphi:I_{\tau'}\to I_\tau$ acts by $c\mapsto c\circ\varphi$. Thus an operation on path objects also acts on arrows between paths, and the text writes the identity and composition equations for $L$.

**Choice of programme (281–283).** Interval categories are small enough that comparisons of the operations can be made there. At 283 the author lists three possible lines of work. He chooses to construct a path category in which the type can vary, use the composition of paths to test it, and defer the general study of functors between intervals.

**Types, words and realization (283–285).** Section 4 recalls $\underline{\mathrm{Ch}}_\tau(X)=\underline{\mathrm{Hom}}(I_\tau,X)$. Manuscript 25 (scan 285) describes types as words on two generators, groups successive equal directions into powers of lengths $\ell_i$, and relates their number to reduced length. Manuscript 26 (scan 284) realizes a type as an interval in Cat. Whether all functors between the intervals should be arrows between their types is precisely what the annotations qualify.

**The category over the types (284, 286).** Composing the realization with the contravariant assignment $S\mapsto\underline{\mathrm{Hom}}(S,X)$ gives a category over the category of types. Its fibre over τ is the category of paths of type τ. The definition is explicitly provisional.

**Its morphisms and their composition (286–287).** A morphism from $c'$ to $c$ over $\varphi:\tau'\to\tau$ amounts to a transformation $u:c'\to c\circ\varphi$. The framed Hom formula and the triangle express the same description. A second triangle gives the composite transformation $u''=(u*\varphi')\circ u'$.

**Endpoint restriction (287–289).** The attempt to define source and target on all path morphisms leads to two equations: $\varphi(0_{\tau'})=0_\tau$ and $\varphi(1_{\tau'})=1_\tau$. The author restricts the allowed arrows to interval functors respecting these equations. On 289 he distinguishes the larger category Typ and total category CH from Ty and Ch. The displayed fibre product describes restriction along the inclusion of Ty into Typ.

**A further restriction (289–290).** After noting the issue of large $X$ and naming two tests, the author opens section 5 with the square relating Ty, Typ, the category under ε, and Cat. He proposes also requiring morphisms to be increasing for the order in which objects are met along a path. At the foot he retains separate names for morphisms and increasing morphisms.

## Statements left without proof

| Scan | Author’s words | Status on these sheets |
|---:|---|---|
| 275 | «opposées l’une de l’autre, et ne sont pas isomorphes» | The forks are drawn. The nonisomorphism and the following generic assertion about their path categories are stated. |
| 277–278 | «ces catégories n’ont pas d’autre … que l’identité»; «plus généralement … pour les catégories réduites de longueur …» | The first concerns the signed chains and the second extends the symmetry of the forks. The ending of the word for even length is uncertain. No general argument for the extension is given. |
| 280 | «représenté par l’objet $I_\tau$ de $X$»; «… biunivoquement … aux … flèches de Cat» | The argument invokes representability for the correspondence. See S1 and S2 for its source and variance. |
| 281–282 | «au plus une seule flèche allant d’un objet donné vers un autre» | The thinness assertion is the reason he gives for commutativity of diagrams in these categories. |
| 284 | «donne lieu à une catégorie fibrée (et même scindée) sur celle-ci» | He invokes the construction from a contravariant functor. The later sheets describe the total category and its composition. |
| 289 | «dépendent fonctoriellement de $X$, variant dans (Cat)» | The induced functor on total categories is asserted here. |
| 290 | «cette hypothèse qui permet de faire une théorie de structure assez simple» | The structure theory for increasing morphisms is anticipated. Its development lies beyond these sheets. |

## Questions and conjectures

- **283.** «Je préfère attendre pour cela d’avoir besoin de ceci et de cela» postpones the systematic part. Composition will be «un test crucial pour l’utilisabilité des notions obtenues».
- **284–286.** The inserted «(petite ?)» qualifies $X$. «faux» and «Définition un peu cavalière» in the margins question the class of arrows. «Provisoirement — si elle s’avère trop grosse» keeps open the choice of total category.
- **286–287.** «Mais que sont les flèches plus générales ?» is answered by the framed Hom formula. «Mais a-t-on des foncteurs source et but … ?» asks whether this construction also has the desired endpoint functors.
- **288.** The manuscript puts a question mark over the equality with $\sigma(c)$. After imposing the endpoint equations it says «j’ai bon espoir que la catégorie … est “la bonne”». The margin asks for a stronger condition, «qu’ils soient croissants sur les objets».
- **289.** «Deux tests essentiels, pour s’assurer si la notion est bonne». The first involves a symbol read tentatively as $M\Sigma^{-1}$; the second is «La composition des chemins … doit bien marcher». The notation of the first test is left unexpanded.
- **290.** «Je me suis plus ou moins convaincu» introduces the stronger condition. It is a working choice; the closing sentence continues to distinguish «morphismes» and «morphismes croissants».

## Slips

| ID | Scan and place | Frozen reading | Apparent intention and reason | Confidence |
|---|---|---|---|---|
| S1 | 280, just below the brace headed by $X$ | «l’objet $I_\tau$ de $X$» | Read «de Cat» in the mathematical statement. $X$ is the varying input of $\mathrm{Cat}\to(\mathrm{Ens})$, and $I_\tau$ is its representing object. | High |
| S2 | 280, raised insertion above «lois de formation» | «de chemins de type τ … à partir de chemins de type τ′» | Interchange τ and τ′ in this phrase to agree with the actual map: $c$ starts on $I_\tau$ and $c\circ\varphi$ starts on $I_{\tau'}$. The connector is overwritten. | Low |
| S3 | 284, immediately after the realization display | «la catégorie $I_\tau$ … s’identifie à une sous-catégorie pleine de (Cat) (celle des $I_\tau$)» | Ty appears intended as the domain of the realization; its objects are the types. Fullness itself is subsequently qualified by the author. A cancelled word follows the name of the category. | Low |
| S4 | 288, first endpoint comparison | One visible closing parenthesis in $c(\varphi(0_{\tau'})$ before the queried equality | A second closing parenthesis would finish the outer evaluation. This may be an abbreviated pen stroke. | Low |
| S5 | 289, second test | «La composition des chemins) doit bien marcher» | In continuous prose the unmatched closing parenthesis would usually be omitted. It could serve as a separate grouping mark for the tests. | Low |

## Pointers

- **277.** «de l’exemple 4°» refers to the forks on manuscript 16 (scan 275). The oblique note also ends «cf ci-dessous» beside the discussion of θ.
- **281.** «les deux exemples plus haut» refers to the composite and the composite followed by an identity on scan 280.
- **284–285.** «page précédente» on manuscript 26 refers back to manuscript 25. These are scans 284 and 285 in the opposite physical order. The last words after «cf» in the note on 285 are uncertain.
- **288.** «cf page 31» refers to manuscript 31, supplied here as scan 290.
- **290.** «la restriction analogue, dans la définition pré-catégorique des morphismes entre …» refers to an earlier definition involving the triangular symbols. These pages give no work title, cote, author or precise location for it.

## Remarks of the model

**R1. Model remark, high confidence (280–281).** The upward maps in the two drawings account for the identity in the second example. Their lists of vertex images are $(0,2)$ and $(0,2,2)$. The repeated final image contributes the identity of $a_2$; the first edge in either list traverses the edges labelled $u_1$ and $u_2$, in that order.

**R2. Model remark, high confidence (288–290).** The proposed monotonicity condition genuinely removes examples already compatible with both endpoints. For instance, map the vertices of $0\to1\leftarrow2\to3$ to $0,1,0,1$ in $0\to1$. All three arrows have the required images, and first and last vertices go to first and last. Along the sequence of vertices the middle step goes from 1 back to 0. This is a model example, separate from the author’s two drawings.

**R3. Model remark, high confidence (287–288).** The questioned equality can be located at a specific stage of the construction. Evaluating $u:c'\to c\circ\varphi$ at $0_{\tau'}$ ends at $c(\varphi(0_{\tau'}))$. The first endpoint equation identifies this with $c(0_\tau)$; the second equation gives the parallel identification at the other end. This accounts for the two rows in the author’s box.
