# Mathematical notes · 157-2, scans 307–322

## What the pages do

**U1 · Concatenating intervals and paths, 307–308.** A word in the two oriented interval types gives an interval. To concatenate two words, identify the target endpoint of the first interval with the source endpoint of the second. The first diamond displays this pushout. The transposed diagram describes a path of the resulting type as two paths in the indicated order, with the target of the first equal to the source of the second. The author chooses the order \(c'\circ c\) for writing their composite.

**U2 · Composition on the category of types, 309.** Products of arrows on types satisfy the displayed interchange equality. This gives a bifunctor on the underlined \(\mathrm{Ty}\). Concatenation is strictly associative and has a strict unit, the type corresponding to the point. The page calls this a monoid in the category of small categories.

**U3 · Objects and arrows of the nerve, 310–312.** The nerve components inherit monoid structures. In degree zero the two generators have opposite orientations. In degree one the generators \(f_{\varepsilon,\ell}\) map a signed interval to \(\ell\) copies with that sign. Sources, targets and the empty word are identified. Scan 312 distinguishes the assignment of the map to the point, whose generator index is 0, from the assignment of an identity, whose index is 1.

**U4 · Generators in degree two, 313–315.** For two successive arrows, the first is described by an ordered list of signs and lengths. A weighting on the transitions of its target determines the second. Splitting the weighting along that ordered list gives the triples \((\varepsilon_i,\ell_i,\pi_i)\). Scan 314 expresses the pair as a unique product of the corresponding generators. Scan 315 recovers its three objects and its two arrows by taking the factors in order, a qualification repeated in the right margin.

**U5 · Composition and the two degeneracies, 316–317.** The composition map sends a triple to the arrow indexed by the total weight \(\operatorname{long}(\pi)\). For the case \(g=\mathrm{id}\) the weighting on the interval is constantly 1. For the case \(f=\mathrm{id}\) the interval has length 1 and its weighting is determined by a single integer. The maps on generators are written on opposite sides of the page break.

**U6 · A simplex of arbitrary degree, 317–318.** A chain with a fixed initial sign is described by successive lengths and weightings. The author puts the weightings on a common domain of positive integers, extends them by zero, and bounds each support in terms of the previous total. He names the resulting generators \(F_{\varepsilon,\pi_\bullet}\). The initial support condition and the range of the general formula are discussed under E4 below.

**U7 · What happens at length zero, 318–319.** A vanishing length forces the following lengths and weightings to vanish. The passage gives a geometric reason. Once the chain reaches the unit, a subsequent arrow must be its identity. Some subscripts in the transition from one level to the next are difficult to distinguish.

**U8 · An arbitrary set of signatures, 319–320.** The remark replaces the two signs by an arbitrary set \(\Sigma\). Objects become words in \(\Sigma\), or integer intervals with their transitions labelled in \(\Sigma\). The arrows are increasing morphisms respecting the indicated endpoints. The author singles out the two-sign case for its connection with paths and \(\pi_0\).

**U9 · Paths as generalized arrows, 320–321.** Section 7 introduces the category of paths from \(a\) to \(b\). Inverting the backward arrows of a path, when they are invertible, yields a direct path whose composite is an arrow of \(X\). Taking all paths themselves as arrows gives a category with the same objects as \(X\); its Hom sets are described as prohibitively large.

**U10 · Passing to components, 321–322.** For composable \(u,v\), the one-step path \(c(vu)\) and the two-step path \(c(v)c(u)\) have different types. A canonical arrow between them puts them in the same component of the path category. The author therefore takes \(\pi(a,b)=\pi_0(\underline{\mathrm{Ch}}(a,b))\). Composition of paths induces composition on these sets. The empty path represents the identity and is homotopic to the path consisting of \(\mathrm{id}_x\).

## Statements left without proof

| ID and scan | Author’s words | What is left to the reader or to later work |
| --- | --- | --- |
| S1 · 307 | « où toutes les flèches sont des foncteurs mono et pleinement fidèles » | The four functors in the first square are described this way. Their full faithfulness is not proved separately. |
| S2 · 309 | « On a transitivité de façon évidente » | The displayed interchange law is given immediately. Strict associativity and the strict unit are asserted with a short explanation. |
| S3 · 311 | « les résultats … du par. précédent » | Freeness of the arrow monoid is presented as a reading of the previous determination of its arrows. |
| S4 · 316 | « Il n'existe au plus qu'un seul morphisme » and « Il existe sss » | The existence and uniqueness criterion for a map from a signed generator to an interval is stated in an NB. |
| S5 · 319 | « La fonctorialité de l'opération de composition des intervalles pondérés, pour cette notion de morphisme, est évidente. » | The generalization to arbitrary signatures has no separate functoriality argument here. |
| S6 · 320 | « qu'on explicitera » | The geometric interpretation of a general path is announced for further explanation. |
| S7 · 321 | « les seules flèches inversibles … sont les identités! » | The observation about the category of paths precedes the two-arrow example. |
| S8 · 322 | « Il est immédiat qu'elle est associative (la composition des chemins l'étant), et unitaire. » | The stated reason for associativity is the associativity of paths. The identity representative is then specified. |

## Questions and conjectures

**Q1 · 308.** « Il se pose ici le sempiternel pb si on va noter ce chemin » introduces a question about the order of composition. The same page resolves it with « C'est cette notation que nous allons suivre plus bas. »

**Q2 · 317.** The simplicity of the preceding descriptions « renforce mon sentiment » that the category « est bien “la bonne” ». The next test is « On va déjà voir si elle donne une description sympa des catégories de fractions » and whether this can be done « sans tortillements comme précédemment ». This is an expressed hope about the construction.

## Slips

| ID and scan | Frozen reading | Apparent intended form and reason |
| --- | --- | --- |
| E1 · 313, Hom formula | The left side contains \(\operatorname{Tr}y\) and an uncertain sequence of closing parentheses. | **Low.** The proposed second argument is \(\mathbb N\). Maps to \(\mathbb N\) have just been specified, and that codomain appears in every factor on the right. |
| E2 · 315, formula for length | The lower limit reads \(j\in[1,\ell_i\) with no closing square bracket visible. | **High.** A right bracket after \(\ell_i\) would close the interval specifying the summation indices. |
| E3 · 317, definition under the length | The left side has \(\pi_{i-1}\); the sum beneath it has \(\pi_i(j)\) and a limit with \(\ell_i\). | **Low.** The displayed domain suggests \(\sum_{j\in[1,\ell_{i-1}]}\pi_{i-1}(j)\). An adjoining index is overwritten. |
| E4 · 318, boxed support rule | \(\operatorname{supp}\pi_i\subset[1,\operatorname{long}(\pi_{i-1})]\) is followed by \(i\in[0,r-1]\). | **High on these leaves.** At \(i=0\) the formula refers to \(\pi_{-1}\). **E4a.** Use the separately written initial bound \(\operatorname{supp}\pi_0\subset\{1\}\), then apply the general rule for \(1\le i\le r-1\). |
| E5 · 318, bottom | After \(\ell_i=0\) the index of the weighting in the conclusion resembles \(i-1\) or \(i+1\). | **Low.** The support rule would give \(\pi_i=0\) and hence \(\ell_{i+1}=0\). The tiny sign in the manuscript is inconclusive. |

## Pointers

- **308.** « cf plus bas le formalisme des cat de fractions » anticipates the discussion begun under §7 on 320.
- **311, 314.** « du par. précédent » and « au par. précédent » refer to the earlier determination of the arrows and the earlier definition from a weighting.
- **315.** « la formule (1)(2) (p. 52, 53) » points to the two numbered expressions on scans 313 and 314. Their manuscript page numbers are 52 and 53.
- **317.** « comme précédemment » refers to an earlier treatment of fractions. No title or author is named.
- **320.** The parenthesis beginning « cf § » refers back to the path category. The overwritten numeral admits 4 or 5.
- **322, oblique margin.** « Ce foncteur est déduit des foncteurs » is followed by the product for fixed types and « cf pag » with uncertain figures, read as 7.7, 77 or 47. These pages give no secure destination for that reference.

## Remarks of the model

**R1 · Model remark, high confidence for the three examples, scans 313–316.** The total in the formula for \(\gamma\) can differ from the size of the weighting’s domain. For weights \((3,0,2)\) the domain has three places and the expanded target has five copies. For \((1,1,1)\) the count is three, and for the empty weighting it is zero. These three finite counts were computed in this run.

**R2 · Model remark, high confidence, scans 321–322.** The direction of the canonical arrow matters even though either direction would place its endpoints in the same component. The formula with \(f_{+2}^*\) starts with the two-step path and displays its one-step restriction. The next line explicitly points from the one-step path to the two-step path.

**Reading questions arising after the freeze.** Scan 322, middle assignment of path pairs. The first member is frozen as \(a\) with \(c\) as an alternative. The output \(c'\circ c\) favours \(c\), while the first input has a closed loop. This affects how the letters match across the assignment. The transcription retains the two readings.
