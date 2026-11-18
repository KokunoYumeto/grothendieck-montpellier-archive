# Mathematical notes on cote 128, scans 002–016

## What the pages do

**U1 · The ideal in tensor powers (002).** Proposition 1 starts with an ideal $I$ of $A$ whose image in the $A$-algebra $B$ is an ideal isomorphic to $I$. A calculation moves a scalar in $I$ through a tensor, reducing to a multiple of the tensor of units. The multiplication map back to $B$ supplies the injectivity argument.

**U2 · Reduction of the complex (003–004).** After a cancelled attempt at a lemma involving two algebras, Corollary 1 compares tensors indexed by a finite set before and after passage to $A_0=A/I$, $B_0=B/IB$. The diagram for a map of index sets makes these sequences into a sequence of simplicial modules. Its first term is constant with value $I$. Corollaries 2 and 3 give a comparison in nonzero degrees, an exact sequence in degree zero, and conditions for injectivity and surjectivity there. The sideways note identifies the cokernels of the two maps from the base rings.

**U3 · Flat coefficients (004–005).** Corollary 4 repeats the comparison with a flat $A$-module $M$. The degree-zero sequence starts with $M\otimes_A I$. Under faithful flatness of $B_0$ over $A_0$, Corollary 5 identifies the degree-zero group with $M$ and sets the nonzero-degree groups equal to zero. The NB singles out $M=A$.

**U4 · Effectivity of a descent datum (005–006).** Proposition 2 starts with a flat $A'$-module $E'$ carrying descent data, with $I$ nilpotent and hypotheses in degrees zero and one. It assumes that the datum on $E'_0$ comes from a flat $A_0$-module. The conclusion gives the module upstairs. The invariants $E$ are flat over $A$, and extending scalars takes $E$ to $E'$.

**U5 · The square-zero calculation (006–007).** For $I^2=0$, the proof computes the subcomplex obtained by multiplying the descent complex by $I$. Its description in terms of $E_0\otimes_{A_0}I$ produces an exact sequence ending in $E\to E_0\to0$. Parts a) and b) identify $E/IE$ with $E_0$ and multiplication on the tensor with $IE$. The author uses these identifications for flatness and then treats the scalar-extension map. The lower square and the longer argument invoking Nakayama belong to an abandoned version.

**U6 · Nilpotent ideals and geometric corollaries (008–010).** Induction reduces the general assertion to lower powers. The intervening lemma says that the ideal-image hypothesis passes to a product of ideals and hence to powers. Corollary 1 applies the argument to effective descent for flat modules. Corollaries 2 and 3 state a form over a prescheme and a base-change assertion with an inserted flatness hypothesis. The next sheet opens with the affine specialization and the phrase « un $A$-préschéma quelconque ».

**U7 · Kernels and ideals (010–011).** Proposition 3 compares the kernels of multiplication from a tensor power to $B$ and to $B_0$. Corollary 1 sends an ideal in the first augmentation ideal to its image downstairs. The reverse assignment intersects the preimage with the upper augmentation ideal. The natural map between the corresponding ideals is said to be bijective. The paragraph below records compatibility with order and with simplicial operations.

**U8 · Equivalence relations and invariants (011–012).** Corollary 2 applies this correspondence to equivalence relations on the two affine schemes. It preserves order and the extreme relations. The bracketed clause compares their rings of invariants $C$ and $C^0$; the displayed criterion passes from a coboundary of an element to the coboundary of its reduction. The last sentence connects effectivity on the two sides.

**U9 · A quotient module of length one (013–014).** Section 2 begins with $A'/A$ isomorphic as an $A$-module to a residue field. Proposition 1 asserts that only the two extreme equivalence relations occur, states exactness and cohomology assertions, and asserts effective descent for flat quasi-coherent modules after base change. The proof cites Section 1 and reduces the equivalence-relation question to an algebra of rank two over a field. It distinguishes the split algebra $k\times k$ and $k[\varepsilon]$ with $\varepsilon^2=0$.

**U10 · A bound from generators of the diagonal ideal (015–016).** Proposition 2 concerns a finite algebra over an Artinian local ring. An equivalence ideal defines $A''$, with $A\to A'\rightrightarrows A''$ exact. The difference $p_2(x')-p_1(x')$ is assumed to generate $\Delta$ whenever $x'$ lies outside $A$. The slanted addition imposes trivial residue extensions. The asserted bound is $\operatorname{length}(A'/A)\leq1$. In the nonradicial case, the proof places $m'$ in $A$, identifies the ideals used for reduction, and carries the generator condition to the reduced algebra. It writes that algebra as a product of $n$ copies of $k$. Taking the specified coordinate vector gives the closing « on trouve $n=2$, O.K. »

## Statements left without proof

| ID | Scan | Words on the sheet | What is left to the reader in this batch |
|---|---|---|---|
| P1 | 007, part b) | « donc grâce à a) et $E_0$ plat sur $A_0$, $E$ est plat sur $A$ » | The flatness criterion used at this step is not spelled out. |
| P2 | 008, lemma | « alors $IJ$ a la $=$ propriété »; « (lemme trivial) » | No separate proof of the product assertion is written. |
| P3 | 009, Corollary 3 | « Sous les conditions précédentes »; « de descente … universelle » | The corollary is stated without a separate argument on this sheet. The word immediately preceding « universelle » is abbreviated and uncertain. |
| P4 | 012, end of c) | « Pour que $J$ soit effectif, il f et s. que $J^0$ le soit … » | The sentence ends with an ellipsis after the comparison of invariants. |
| P5 | 014, proof of (i) | « On peut supposer $k$ alg. clos. » | The passage to an algebraically closed field is inserted without an argument here. |
| P6 | 014, second case | « non réduit, alors $A'\simeq k[\varepsilon]$, avec $\varepsilon^2=0$ » | This sheet identifies the algebra. It gives no further argument counting its equivalence relations before the next proposition. |
| P7 | 015, boxed note | « Sans l’hypothèse ↑, il est vrai que $mA'=m$ » | The margin asserts the ideal equality with the indicated hypothesis removed. |
| P8 | 015, case 1° | « Comme $J$ est nilpotent » | The deduction uses nilpotence here without deriving it on this sheet. |
| P9 | 015–016 | « distinguons deux cas »; « on trouve $n=2$, O.K. » | The supplied pages develop the first case. They end before a second case is treated. |

## Questions and conjectures

None explicitly formulated as questions or conjectures. Scan 012 asks « expliciter plus » by the invariant-ring calculation. Scan 016 asks « dégager un lemme de réduction ». Both are requests for further exposition.

## Slips

| ID | Scan and place | Written form | Likely intended form and reason |
|---|---|---|---|
| S05 | 005, NB, second row | $H^0(B,A)$ | $H^0(B/A)$, medium confidence. The degree-$i$ line immediately above has the slash for the same extension. |
| S06 | 006, parenthesis before the first sequence | $E'_0$ « rel à » $A'_0/A'$ | $A'_0/A_0$, medium confidence. The following complex and a later occurrence after « Grâce » both use $A_0$ as base. |
| S12 | 012, end of the invariants calculation | « donc on écrira aussi $C_0$ aussi » | One « aussi » suffices. Both instances can be read across the line break. |
| S16 | 016, generator sentence | $\delta_0(x'_0)\in A'_0$ | $A''_0$ is the apparent ambient algebra for the generator of $\Delta_0$. Confidence is low because there is a single visible prime, but this stretch also contains a heavy overwrite on the nearby ideal symbol. |

**Reading questions**

| Scan and place | Frozen reading | Other reading and evidence |
|---|---|---|
| 003, last exact sequence | $C(B/A)$ and $C(B_0/A_0)$ | Either initial could be K. Both have a reinforcing stroke absent from the C of $C_I$ in the same line. The opening on 004 uses K. |
| 005, large diagram, reduced E row | Three horizontal strokes without heads from $E''_0$ towards $E'''_0$ | The middle stroke could have a right-pointing head. There is a small wedge at its right end. |
| 008, first bracket of Corollary 1 | $IB=B$, with $I$ as the alternative to the last $B$ | The earlier ideal hypothesis favours $IB=I$. The last stroke joins the closing bracket. |
| 009, Corollary 2, after « affine sur $X$ » | $I\longrightarrow A'$ | A plain horizontal stroke is also possible. At high magnification its right end thickens and turns up slightly. |
| 014, line 2 of the proof | $A_0$ with a raised 2, possibly cancelled | The raised mark has the curled shape of 2 and heavier ink at the top. The following quotient suggests $A_0$ without the exponent. |

## Pointers

| Scan | Manuscript words | Destination within the argument |
|---|---|---|
| 005 | « cf cor. 3 », and « par cor. 3 » in the footnote | The degree-zero and nonzero-degree comparisons just above. |
| 007 | « donc par Nakayama » | A named invocation in the cancelled proof. |
| 010 | « du Cor. 1 de prop. 1 »; « diagramme du serpent »; « comme ds Prop. 1 » | The tensor diagram, the kernel argument and its standing assumptions. |
| 011 | « cf Prop 1, cor 1 »; « par celle du cor. 1 pour $n=2$ » | Simplicial operations and the preceding correspondence of ideals. |
| 014 | « du N° 1, Prop. 1, cor. 5, et prop. 2 … cor. 3 »; « N° 1, Prop 3, cor. 2 » | Section 1 supplies the descent and equivalence-relation comparisons. The first reference carries a small inserted « cor. 1 et ». |
| 015 | « cf prop 1, (i) » | The preceding proposition on the two extreme equivalence relations. |
| 016 | « par N° 1 prop. 3, cor. 2 » | The exact sequence after reduction to the residue field. |

## Remarks of the model

**M14 · Model observation, high confidence.** In the split case on 014, the ordinary two-point calculation gives exactly the diagonal and the full relation. Enumerating subsets of the four ordered pairs with reflexivity, symmetry and transitivity yields those two. This checks the finite-set count only.

**M16 · Model observation, high confidence.** The vector chosen on 016 explains the distinction between two and three factors. On two factors its coordinates differ at every off-diagonal pair. On three factors the difference vanishes at $(2,3)$ and $(3,2)$. This computation concerns the displayed coordinate choice; the reduction to the product algebra belongs to the manuscript’s argument.

**M09 · Model observation, medium confidence.** The inserted « plat » on 009 matters when reading the first paragraph on 010. The latter says « quelconque » of $Y$, without restating a flatness condition there. The precise scope of the passage between those sentences is a reading question about the argument.
