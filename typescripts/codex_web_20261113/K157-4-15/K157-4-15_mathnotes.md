# Mathematical notes on cote 157-4, scans 228–242

## What the pages do

**U1 · Scan 228.** Grothendieck tests the hypotheses of corollary 7.4 in Cat and in the presheaf category \(A^\wedge\). For subobjects \(A_1,A_2\) of \(B\), the map in question goes from their pushout over \(A_1\cap A_2\) to \(B\). He needs this map to be mono and monos to be stable under cobase change in \(A^\wedge\). He also transfers stability under filtered direct limits from \(W\) to \(W_A\) via \(i_A\).

**U2 · Scans 228–229, lemma 8.1.** An inverse image under a functor commuting with filtered direct limits preserves the accessibility of a part, subject to the listed hypotheses. The refinement fixes a cardinal \(\pi\) for which the part is accessible and the functor carries the \(\pi\)-objects of the source into those of the target. The categories and the parts they contain have similar-looking handwritten names.

**U3 · Scans 229–230, lemma 8.2.** The first display includes monos in \(\mathrm{Cof}_{W_A}\). The second concerns the stability of \(\mathrm{Mon}\cap W_A\) under cobase change. In the pushout square, \(i,i'\) are the horizontal monos and \(\alpha,\beta\) the sloping maps. The stronger last display compares membership in \(W_A\) along each pair. The first double arrow has an uncertain left end.

**U4 · Scan 230, corollary 8.3.** With \(C=\mathrm{Mon}(A^\wedge)\), \(\mathrm{TC}=C\cap W_A\), \(F=(\mathrm{TC})_*\) and \(\mathrm{TF}=C_*\), he obtains two Quillen pairs with functorial factorizations. The criterion for the triple is \(\mathrm{TF}\subset W_A\). The insertion identifies the maps in question by injectivity in the slice over their target. The corollary gives left properness. Full properness remains a question.

**U5 · Scans 231–232, theorem 8.4, part 1°.** Four conditions on \(A\) are stated as equivalent. In a), the maps of injective type belong to \(W_A\). In b), the arrow \(L_A\to e_A\) from the Lawvere object to the final object belongs to \(W_A\) after every base change. He also expresses this by testing \(L_A\times a\). In c), there is a universally \(W_A\)-aspherical interval with two disjoint sections. In d), each slice \(B=A_{/a}\) is a test category for \(W\). The two functors \(i_B,j_B\) detect the indicated weak arrows and give quasi-inverse functors on the displayed homotopy categories. A slanted note proposes a further test d′) in terms of \(j_A\).

**U6 · Scan 233, theorem 8.4, parts 2° and 3°.** Under the equivalent conditions the presheaf category has the stated left-proper closed Quillen triple. The next clause identifies the further condition under which \(A\) itself is a test category, namely that \(A\) be \(W\)-aspherical. The interlinear “et alors seulement” gives the converse.

**U7 · Scans 233–234, corollary 8.5.** The examples comprise ordered and unordered combinatorial simplices and cubes. The other case asks for finite products and an object with two disjoint sections over the final object. A marginal note narrows the products required to \(I\times a\). The next sheet applies c) and uses the final object for asphericity.

**U8 · Scans 234–235, proof of theorem 8.4.** He first writes \(a\Rightarrow b\Rightarrow c\) and appeals to *Pursuing Stacks* for \(c\Rightarrow d\) and \(c\Rightarrow b\). A cancelled attempt at \(d\Rightarrow a\) passes to a slice and a final object. Below the cancellation he changes his plan. Taking the equivalence of b), c), d) as already established, he turns to \(b\Rightarrow a\).

**U9 · Scan 236, lemma 8.6.** For a Quillen precouple and a class \(W\) closed under retracts, he relates \(\mathrm{TF}\subset W\) to factorizations \(f=pi\) with \(i\in C,\ p\in W\). One may test the factorization condition on \(f\in\mathrm{TF}\). The proof identifies \(f\) as a retract of \(p\). Its last written membership statement is recorded under S2.

**U10 · Scans 237–238, factorization of a presheaf map.** In the construction called “mapping-cône”, he takes the product of the interval with \(X\), then forms a pushout using \(\delta_0^X\) and \(f:X\to Y\). The other endpoint supplies \(i_f=f'\delta_1^X\), with \(f=p_f i_f\). He gives the argument for \(p_f\in W_A\) and identifies \(i_f\) as the composite \(X\to Y\amalg X\to Z(f)\) of two monos. An added line declares theorem 8.4 proved.

**U11 · Scans 238–240, lemma 8.7.** The abstract version fixes \(X\) and starts with a factorization of the fold \(X\amalg X\to X\) through \(I_X\). A diagram with two pushout squares constructs the factorization of \(f\). For \(i_f\in C\) he adds the condition \(X\in M_C\), expressed using \(X\to Y\amalg X\), and notes a tacit existence assumption for finite “lim”. The sign beneath the word may be a rightward arrow. The next page identifies \(i_f=j\circ\lambda\) and invokes the two closure properties of \(C\).

**U12 · Scans 240–241, hypotheses actually used.** The comments distinguish \(a\Rightarrow(b\Leftrightarrow c\Leftrightarrow d)\) from the full equivalence, for which he adds closure under retracts. The corollary and the construction of the Quillen triple have separate axiom lists. The latter list retains the clauses annotated “limites”, “carré coc.” and “accessibilité”. The connectivity axiom 5 is struck out of it.

**U13 · Scan 242, section 9.** He restates saturation, its stronger retract form and the final-object axiom. The weak localization axiom tests \(X_{/y}\) for each \(y\in Y\). The strong form tests \(f_{/s}:X_{/s}\to Y_{/s}\) over each \(s\in S\). A bracketed note proposes restricting this last test to split fibrations. The entry on \(W\)-fibrations at the foot is crossed out.

## Statements left without proof

| ID and scan | His words | What is asserted or deferred here |
|---|---|---|
| B1 · 228 | “c’est évidemment vrai dans \(A^\wedge\)”, “dans tout topos, l’étant dans (Ens)” | He takes the subobject assertion in sets as known. For cobase change of monos he contrasts its behaviour in Cat and \(A^\wedge\). |
| B2 · 229 | “Vérification immédiate.” | This follows the cardinal refinement of lemma 8.1. The sufficient cardinal bound also has a reference to 9.14. |
| B3 · 229–230 | “En fait on a mieux”, “Il reste à vérifier (8.24.)” | He refers the stronger pushout statement to an earlier chapter. |
| B4 · 230 | “sont des couples de Quillen”, “Q-engendrées … par des petites parties” | The two pairs and the small generating parts are presented as consequences of 7.4. The direction of the argument for left properness is given by “par 8.2.1.” |
| B5 · 232 | “La condition \(d)\), d’apparence très forte, est équivalente à la condition … \(d')\)” | The margin also says “il suffit \(=\) de l’exiger pour \(C\to e\)” when \(C\) has a final object. The intervening description of the adjoint condition is hard to read. |
| B6 · 233–234 | “universelle”, “il suffit que \(I\to e\) soit …”, “sont traités dans P.S. § 34” | The margin gives a universal characterization of the cube example and weakens the product hypothesis. The four named examples are referred to an earlier treatment. |
| B7 · 234 | “L’objet de Lawvere d’un topos quelconque est un objet injectif” | He uses this fact in \(a\Rightarrow b\). The sheet calls the two successive implications “\(\pm\) tautologiques”. |
| B8 · 234–235 | “Que l’on ait \(c\Longrightarrow d\) (et \(c\Longrightarrow b\)) est établi dans PS”, “prop. 3 page 173” | In the revised proof he takes the earlier equivalence of b), c), d) as available. |
| B9 · 240–241 | “sont valables sous les seules conditions”, “il suffit de”, “il nous faut (presque) tout l’éventail” | These are his conclusions about which numbered hypotheses suffice. The individual axioms from the earlier chapter are not reproduced in these pages. |

## Questions and conjectures

| Scan | His words | Question or qualification |
|---|---|---|
| 228 | “Je doute que c’est vrai dans Cat” | Does the comparison from the pushout of two subobjects to their common ambient object remain mono in Cat? The later “sûrement fausse dans Cat” refers to stability of monos under cobase change. |
| 230 | “Il reste à vérifier (8.24.)” | The verification concerns the stronger statement at the foot of 229. |
| 230 | “Il n’est pas clair qu’elle soit forcément propre”, \(F\subset\mathrm{Fib}_{W}\) “(?)”, “Nous y reviendrons par la suite.” | He defers full properness. |
| 231 | “sauf peut-être celui (4) des fibrations” | The qualification belongs to the original statement of the axioms for 8.4. |
| 235 | “telle quelle je ne vois pas, … comment en déduire \(a)\)” | This concerns the proposed direct route from d). His next sentence changes the proof. |
| 241 | “On devrait … les axiomes”, “Il se pourrait d’ailleurs … que si \(W(5)\) n’est pas satisfait, on ait \(W=\mathrm{Fl}\,\mathrm{Cat}\) tout entier, donc \(W_A=\mathrm{Fl}\,\widehat A\) !” | The margin suggests renumbering. The separate conjecture asks whether failure of connectivity forces every arrow to be weak under the other stated axioms. |
| 242 | “version définitive (?)”, “Sauf erreur, il suffit de l’exiger si \(X,Y\) sont … fibrés scindés sur \(S\)” | The first question accompanies XVII. The second proposes testing strong localization on split fibrations and maps compatible with the splittings, assuming Loc (1,2). |

## Slips

| ID and scan | Frozen wording or formula | Apparent correction and reason |
|---|---|---|
| S1 · 230, opening reference | “(8.24.)” | **High confidence.** The immediately preceding numbered conclusion is (8.2.4). The opening reference on 230 omits the interior stop after 2 and puts one after 4. |
| S2 · 236, end of lemma 8.6 | “on a \(i\in W\)” | **High confidence.** Read \(f\in W\) for the conclusion of this argument. The sentence explicitly identifies \(f\) as the retract of \(p\) and states \(p\in W\). Closure under retracts applies to \(f\). |
| S3 · 237, right of (8.6.1) | \(\mathrm{pr}_1^X:X\times I\to I\) | **High confidence.** The indicated first projection has target \(X\). The same sheet draws it down to \(X\), and 238 identifies the endpoint maps as its sections. The small annotation itself ends in a barred \(I\). |
| S4 · 232, last line | “dans \(W\) respt. dans \(W_A\)” | **Low confidence.** \(W_B\) would agree with the adjacent formula for the adjoint pair indexed by \(B\). An intentional return to \(A\) is possible. The noun immediately before “dans \(W\)” is uncertain. |

## Pointers

| Scans | His words | Referent as identified here |
|---|---|---|
| 228–230 | “cor. 7.4”, “On conclut donc de 7.4.” | The earlier corollary on the preliminary conditions and Quillen pairs. On 229 the first digit in the reference is uncertain. |
| 229 | “cf loc cit. 9.14 p. 153” | The cardinal estimate. This sheet gives no title. |
| 230–231 | “qui a été vu dans …”, “notations de XII” | The numeral after the first phrase has readings XII, XV and XIV. The added pointer to XII on 231 concerns the names of the axioms. |
| 231–234 | “l’élément de Lawvere”, “L’objet de Lawvere d’un topos quelconque” | Lawvere is named in the criterion and its proof. |
| 232, 234–235 | “cf Pursuing Stacks, § 65, notamment pages 172–173”, “P.S. § 34 (p. 47–50)”, “PS p. …–179”, “prop. 3 page 173”, “dans loc cit” | The first and last group of references concern test categories. Section 34 concerns the simplex and cube examples. The starting page before 179 looks like 168 or 468. |
| 230, 233–234, 236 | “couples de Quillen”, “triple de Quillen”, “à la fin du § 4 … Généralités sur les triples de Quillen” | Quillen supplies the terminology. The last phrase identifies the suggested place for the retract lemma. |
| 238, 240 | “cf XII p. 230”, “que j’ai sous les yeux”, “développements de PS” | The first two phrases point to the more complete factorization diagram. Scan 240 specifies the use of PS in relating d) to the other conditions. |
| 242 | “cf XVII version définitive (?)”, “cf XIV” | The upper pointer accompanies the revised axioms. The lower pointer is inside the cancellation of Loc (4). |

## Remarks of the model

- **R1 · Model, high confidence · Scans 237–240.** The two maps whose composite is announced on 238 can be located separately on 239. The underbraced term is the map \(\lambda:X\to Y\amalg X\). The following vertical map is \(j\) in the prose on 240, which then writes \(i_f=j\circ\lambda\).
- **R2 · Model, medium confidence · Scans 235–237.** The page turn preserves two stages of the revision. Scan 235 ends “qui va résulter” after \(b\Rightarrow a\). Scan 237 opens “du lemme 8.6.” Between them, 236 still says “dém de \(d)\Rightarrow a)\)”. The sentence reads continuously across the lemma. The two implication labels give different accounts of the route taken.
- **R3 · Model, low confidence · Scan 239.** The prose calls the object \(C(f)\), while the lower diagram labels it \(Z(f)\), as on 237. The page gives no separate definition relating two objects with these names. The difference may be a change of notation within the draft.
