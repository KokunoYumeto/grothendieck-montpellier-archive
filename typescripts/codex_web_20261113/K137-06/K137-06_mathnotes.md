# K137-06 · Mathematical notes

Scan numbers are the PDF scan numbers. Line references are to the individual LaTeX page files. The statement IDs identify the corresponding entries in CHECK_EVENTS.tsv.

## What the pages do

**73–74. The De Rham example.** Fixing total degree $n$ gives a resolution which the author calls flasque except at the top vertical degree. He compares its transform with $C^\bullet$ through degree $n$, then states a homotopy comparison with a truncation. He reserves the claim of alternation until a divided-power structure on $F$ is introduced. Scan 74 adds the De Rham–Sullivan case in characteristic zero.

**75–76. Polynomial morphisms and their degrees.** A category $P$ with finite products contains a subcategory $P_1$ on the same objects. The product projections detect degree-one arrows, and $P_1$ is additive. The text equips $P(X,Y)$ with an abelian group structure, distinguishing the two sides of the distributive law for composition. Axiom d) specifies a direct sum decomposition by nonnegative degree and then a multidegree decomposition for several inputs. Scaling each input acts with the corresponding weight.

**76–77. Why the decomposition is given.** A cancelled lemma tries to recover a summand from its integer weights. The sideways example compares two degrees for a group annihilated by $p$. After considering extension to other scalar rings, the author retains the decomposition as “structure supplémentaire”. He records the degrees of a composite in blocks of variables, symmetry under permutation, and the degree-zero condition for constant arrows. The margins add conditions on degree one and a zero input.

**78–79. Representing objects.** The trilinear functor with values $P_{(1,1)}(X,Y;Z)$ gives $X\otimes Y$ when it is representable in $Z$. Representing $P_n(X,-)$ gives $\Gamma^nX$. The candidate unit is $\Gamma^0(0)$. A tensor product is called strict when its universal map still induces the specified bijection after another variable of arbitrary degree is included.

**79–80. Products and divided powers.** A homogeneous summand in several inputs has a candidate representing object $\Gamma^\nu(X_1,\ldots,X_r)$. Composition with the canonical maps from each $X_i$ gives a comparison with the tensor product of the individual powers. Assuming this comparison is invertible gives the displayed sum over $\sum\nu_i=n$. Applying it to $X\times0$ yields the unit calculation.

**81. The comparison maps.** The graded functor $\Gamma^*$ takes sums to tensor products, giving $\Gamma^*(X)$ a commutative graded algebra structure. A slanted note adds the coalgebra and bialgebra structures. Successive universal arrows of degrees $q$ and $p$ give a map $\Gamma^{pq}(X)\to\Gamma^p(\Gamma^q(X))$. The square records compatibility for three degrees.

**82–83. Reconstruction.** In the converse direction the starting data include an additive category with tensor product, the graded functor, comparisons for sums and the maps $\alpha$. The forks distinguish the degree-one identity conditions from the degree-zero conditions. Representing homogeneous arrows as maps out of $\Gamma^nX$ gives their composition. Its associativity is assigned to the square on scan 81. The circled map $\mathbb{1}\to\Gamma^q(\mathbb{1})$ prompts the note about a missing axiom.

**84–85. Equivalence and scalars.** Decomposing the power of a sum recovers the multidegrees. The author calls the resulting notions a strict polynomial category and a $\otimes$-pd-category, and asserts their equivalence. A $k$-linear version requires the multidegree decomposition to respect scalar operations. The examples pass from $k$-modules to sheaves of modules over an algebra in a topos and then to graded modules.

**85–86. Additional structure.** Two questions remain for the abstract category. The first asks for divided-power operations on $\Gamma^*(M)$. The second asks when composition takes values in polynomial applications between the morphism modules. The final lines locate the proposed extra data in the action of $\Gamma^p$ on morphisms.

## Statements left without proof

| Scan | Author’s words | Extent of the argument on the sheets |
|---|---|---|
| 73–74 | “en fait, on a un choix canonique” and “Il y a de $=$ un complexe de De Rham-Sullivan” | A unique morphism is cited for the canonical choice. Scan 74 names the characteristic-zero complex in two lines. |
| 75 | “sont des groupes abéliens”, “Il en résulte aussi que … opère sur $P$” | The author cites the abelian group objects for the first claim. He states the scalar action and writes its formula. |
| 78 | “ils sont can. isom.”, “il … dépend aussi fonctorielt de $X$” | He states the symmetry of the tensor object and functoriality of the power object in $P_1$. |
| 79 | “On sait qu’un objet unité … si elle existe, est unique” and “automatique si $P_1$ est karoubienne” | The first claim presupposes associativity. The second concerns representability of the homogeneous summands already under consideration. |
| 80 | “Il suffirait de l’établir … pour $r=2$ d’abord” | The reduction to two factors is proposed. The displayed decomposition and unit calculation use the stronger comparison hypothesis. |
| 81 | “il s’ensuit que … une structure de $\otimes$-algèbre graduée comm.” | The group object for $\oplus$ is the reason given. The corresponding assertion for the coalgebra is marginal. |
| 83 | “Le diagramme comm. $(*)$ assure l’associativité de la composition” | The defining composite is drawn. The comparison of two triple composites is left to that diagram. |
| 84 | “On vérifie alors les axiomes a) à g)” and “Les deux notions sont donc en …” | The page announces verification and equivalence. It does not work through the axioms individually. The last noun is marked as doubtful. |
| 85–86 | “La catégorie des $k$-modules est une $\otimes$-pd-catégorie”, “Il y a une telle structure canonique dans le cas de l’exemple”, “Ceci aussi est acquis dans l’exemple principal envisagé” | The examples and their extra structures are stated here without constructions. |

## Questions and conjectures

- **73.** “On ne peut affirmer encore … que le complexe de De Rham associé à $F$ est alterné.” The qualification concerns alternation after applying $F$.
- **76–77.** “si on exigeait … pour tt $\mathbb Z$-algèbre $k$” considers a stronger scalar-extension requirement after the uniqueness argument is struck. The live definition takes the decomposition as data.
- **78–79.** Both unit isomorphisms on 78 carry question marks. Scan 79 asks “Il faut examiner pourquoi ce devrait être $\Gamma^0(0)$.”
- **80.** “Il suffirait de l’établir” proposes a binary test for the comparison hypothesis. The marginal request for a simple criterion is difficult to read.
- **83.** “l’avait oublié dans les axiomes préliminaires” and “il ne semble pas … se déduire du …” concern the circled degree-zero condition. No independence argument follows.
- **85.** A marginal “?” accompanies the graded-module example. The later “quand et comment … une structure ‘à p.d.’” asks for maps from an iterated power to a single power satisfying the divided-power axioms.
- **86.** “quand peut-on considérer la composition … comme une application linéaire” asks when linear dependence on the second argument yields a map into polynomial applications in the first. “La construction doit se ramener” introduces the proposed reduction to the $\Gamma^p$.

## Slips

| ID | Scan and source line | Written form and proposed correction | Reason and confidence |
|---|---|---|---|
| S75 | 75, line 52 | $f\circ(n\,\mathrm{id}_Y)$ → $f\circ(n\,\mathrm{id}_X)$ | **High.** The clearly written $Y$ has the wrong object for precomposition with $f:X\to Y$. The next sheet writes $\lambda\,\mathrm{id}_X$. |
| S76a | 76, line 21 | $\lambda_1^{n_1}\lambda_r^{n_r}f$ → $\lambda_1^{n_1}\cdots\lambda_r^{n_r}f$ | **Medium.** There is a space between the two handwritten factors. At three inputs a middle scalar can change the coefficient. The expanded form agrees with the later live formula on scan 85. The author may have abbreviated the intervening product. |
| S76b | 76, line 25, sideways example | $\lambda^p\,\mathrm{id}_{\mathbb Z}$ → $\lambda^p\,\mathrm{id}_P$ | **Low.** The subscript reads as a small doubled Z in the rotated note. The two actions being compared are on the group $P$. The small subscript was originally doubtful. |
| S82 | 82, line 39, lower branch of $(**)$ | Middle term $\Gamma^1\circ\mathrm{id}$ → $\Gamma^q\circ\mathrm{id}$ | **High.** The crop shows a single-stroke exponent. Replacing the right-hand $\Gamma^1$ in $\Gamma^q\circ\Gamma^1$ by the identity leaves $\Gamma^q$ on the left. |

## Pointers

- **73–74.** “complexe de De Rham” and “complexe de De Rham-Sullivan” name the constructions. Neither line supplies a paper title or bibliographic reference.
- **77, 79–80.** “la décomposition $(*)$”, “la définition précédente” and “la condition plus haut” refer back to the multidegree decomposition, strictness and the power comparison in these sheets.
- **82–84.** “la condition d’associativité ci dessus”, “Le diagramme comm. $(*)$”, $(**)$ and $(***)$ connect the reconstruction to the square on scan 81 and the two forks on scan 82. “les axiomes a) à g)” refers back to scans 75–77.
- **86.** “dans le cas de l’exemple” and “dans l’exemple principal envisagé” refer to the module example on scan 85. No other cote or numbered external work is specified.

## Remarks of the model

- **M76 · Model remark, high confidence for the example.** On $\mathbb Z/2\mathbb Z$, multiplication by $\lambda$ and by $\lambda^2$ give the same map for each of the two residues. This small case realizes the degree ambiguity of the sideways note on 76. The general lemma on 76–77 is struck.
- **M81 · Model reading question, low confidence as a claim of error.** On scan 81, line 36, the frozen superscript of the inner $\alpha_{q,r}$ reads $\Gamma^r(X)$, with $X$ as the other candidate. Applying $\Gamma^p$ to the component at $X$ supplies exactly the two objects on the right of the square. The superscript has been retraced, so the type check establishes the expected component only.
- **M82 · Model reading question, low confidence as a claim of error.** On scan 82, line 15, the frozen last argument in $\Gamma^*(X)\otimes\Gamma^*(M)$ reads $M$, alternatively $Y$. The left-hand sum has been rewritten to $X\oplus Y$, and the surrounding sentence names $X,Y$. These favour $Y$ at the right. The letter itself remains doubtful.
- **M83 · Model remark, high confidence.** On scan 83, the source of $f$ is $\Gamma^p X$, while $g$ has source $\Gamma^qY$. Following the three maps through the written composite gives $g\,\Gamma^q(f)\,\alpha^X_{q,p}$. This accounts for the order $q,p$ at the bottom of the diagram.
- **M83b · Model reading question, low confidence.** On scan 83, line 43, the frozen wording was *on l’avait oublié* with the pronoun marked. The pronoun now also carries *je* as an alternative. The pale terminal stroke of *avait* could be an *s*, giving *je l’avais oublié*. It is too faint to assign a grammatical slip.
- **M85 · Model reading question, low confidence about the sign.** The clear comparison on scan 82 goes from a single power to an iterated power. In the question on 85, line 28, the iterated power comes first. The frozen connector reads as a dash, alternatively a rightward arrow. “des hom de degré 1” supports reading this as a question about maps in the reverse direction.
- **M85b · Model reading question, low confidence.** On scan 85, line 18, the frozen words before the disputed final group are *pour les degrés*. A fresh look also permits *pour le degré*. The article ends in a short horizontal stroke and the noun has an accent but no separately identifiable final *s*. The degree $ni$ makes the singular natural.
