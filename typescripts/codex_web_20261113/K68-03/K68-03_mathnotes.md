# Mathematical notes on cote 68, scans 33–34 and 36–44

## What the pages do

**33 · Winning and losing positions.** The player-to-move map partitions the positions into two fibres. Intersecting those fibres with $G$ and $P$ recovers each player's winning positions. Away from $C_0$, a position is winning when some reply is losing, and losing when every reply is winning. The page writes these tests again as set equalities.

**34 · A criterion for identifying the two sets.** Four conditions on $\widetilde G,\widetilde P$ control replies and membership on $C_0$. If play cannot continue indefinitely, the proposed sets are contained in the winning and losing sets. Complementarity and disjoint terminal outcomes give equality. A corollary recasts the conditions as a test.

**36 · Exponential and logarithm.** For a unital associative $\mathbb Q$-algebra $A$, Th 1 gives inverse maps between $N(A)$ and $1+N(A)$, records their identities on commuting elements, and restricts the bijection to a suitable subspace $L$. The remark transports multiplication on $1+L$ to $L$ when $L$ is closed under products. The addition law in the commutative case is interlined.

**36 · Reduction examples.** Example 1 applies the remark to $JA$ for a nil ideal $J$ of the base. The NB identifies $JA$ and $1+JA$ through the fibres at zero and one of reduction. Example 2 takes endomorphisms of $M$ carrying $M$ into $JM$, now with $J$ nilpotent. Exponentiation identifies these with endomorphisms acting as the identity on $M/JM$.

**37 · Formal and ordinary one-parameter groups.** Over a commutative $\mathbb Q$-algebra, the formal additive group takes $K'$ to its nilpotent elements. Each $x\in U$ gives $\bar e_x(\lambda)=\exp(\lambda x)$ in the units of $U$. Nilpotent $x$ also gives $e_x$ on the ordinary additive group. The two resulting correspondences are labelled $(*)$ and $(**)$.

**38 · The proof of Th. 2.** Comparing coefficients proves injectivity. The group law for a formal series gives $na_n=a_1a_{n-1}$, hence $a_n=a_1^n/n!$. For the ordinary additive group the polynomial has finitely many coefficients, so $a_1$ is nilpotent. This proof concerns the units functor of the algebra $U$.

**39 · The automorphism functor of a module.** The page applies the construction to $K'\mapsto\operatorname{Aut}_{K'}(M_{K'})$, with endomorphisms as coefficients. It states two bijections for a $K$-module $M$, points out the finite projective case, and invokes a polynomial description of natural maps in the ordinary case. The last assertion needs attention for an arbitrary module.

**40 · Intertwining two actions.** Comparing the coefficients in the action on $f\colon M\to N$ reduces equivariance to $vf=fu$. For nilpotent $u,v$, a second proposition relates formal equivariance, ordinary equivariance, this commutation identity, and intertwining $\exp(u)$ with $\exp(v)$.

**41–42 · Recovering infinitesimal commutation.** Write $\delta=vf-fu$ and expand the difference of the exponential operators using $\delta_n=v^nf-fu^n$. The proof expresses $\delta$ as $\rho\delta$ with $\rho$ nilpotent. Iteration on 42 then gives $\delta=0$.

**42–43 · Tensor products and algebras.** The tensor action comes from $u\otimes\mathrm{id}+\mathrm{id}\otimes v$. The manuscript extends the formula to finite tensor products and identifies the derivation condition for an action by algebra automorphisms. The first line of 43 gives the single-exponential criterion when $u$ is nilpotent.

**43 · Internal Hom and module-valued functors.** The induced infinitesimal action is $f\mapsto vf-fu$. The page pauses over when the internal Hom has the required module-functor form, then defines exponentials for a functor $\mathcal M$ with $K'$-module values and compatible transition maps. A nilpotent natural endomorphism supplies the ordinary action.

**44 · A formal action and an open question.** Item b) defines the formal exponential for an arbitrary natural endomorphism. The NB asks if the two displayed maps are bijections. A separate line names the symmetric, tensor and exterior algebra extensions.

**44 · Globalisation.** A locally nilpotent derivation of the structure sheaf is exponentiated. The text discusses its action on the reduction, the associated scheme automorphism and its behaviour over $S$. Two identities for the named automorphisms close the sheet.

## Statements left without proof

| Scan | His words | What is left on these leaves |
|---|---|---|
| 34 | “si dans $C$ il n'existe pas de partie infinie, on a” and “il f et s.” | The proposition and its corollary are stated. These leaves give no argument ruling out a counterexample by following successive moves. |
| 36 | “$\exp$ est bijective”, “alors $x+y\in N(A)$”, “par 3°”, “satisfait les conditions de la Remarque” | Th 1 and the subgroup and reduction examples give conclusions or refer back to the theorem. The nilpotence assertions in the examples receive no separate verification. |
| 37 | “Si $x,y$ commutent”, “si $U$ est comm., alors ce sont des isom. de groupes” | The compatibility with products and the additional assertion for commutative $U$ are recorded briefly. The bijectivity itself has a proof on 38. |
| 39 | “On trouve encore que $(*)$ et $(**)$ sont des bij.”, “On utilise le fait que tt morphisme de foncteurs”, “nuls sauf un nb fini.” | The ordinary bijection (P39.2) uses a single finite bound on all coefficients (P39.1). The paragraph supplies no justification for that bound for general $M$. |
| 42–43 | “Extension”, “Pour que cette opération soit une op. d'… d'algèbre”, “Si $u$ nilpotent, il f. et s. que $\exp u$ soit un autom d'algèbre.” | The finite tensor extension and derivation criteria are stated without a new proof. The shortened word after “d'” on 42 remains doubtful. |
| 43 | “Alors il opère sur”, “Mais en tte rigueur”, “On trouve sur $\mathcal M$ une structure” | The Hom formula and the functor-level construction are stated. The text itself qualifies the use of the Hom formula. |
| 44 | “Extension aux … algèbres”, “Alors $\exp\theta$ est un autom”, “l'identité sur”, “un $S$-autom.” | The named algebra extensions, the reduction assertion and the relative construction are not developed on this sheet. |

## Questions and conjectures

- **36, slanted left margin.** “réciproque? par … d'indéterminées”. The intervening word is tentatively `introduction`. The note stands beside the passage about the group law on $L$. Its exact target within that passage is open.
- **43, after the Hom formula.** “ce qui n'est guère assuré, que si $M$ proj. de t.f.” The word `assuré` is tentative. This qualifies the use of the module-functor description.
- **44, NB and left margin.** “La question se pose encore si … sont des bij.” A separate question mark stands beside the maps from all endomorphisms and from nilpotent endomorphisms. The sheet leaves the question open for $\mathcal M$.

**Reading questions revisited or raised while making these notes**

| ID | Scan and line | Frozen reading | Other reading and reason |
|---|---|---|---|
| Q38.1 | 38, struck formula above the ordinary polynomial | The doubtful crossed expression ends in $\varphi(\lambda))=$ | The blind reading had one closing parenthesis. An oblique stroke through the old formula can account for the apparent second one. This difference was already entered in the blind comparison. See 038-lowerold.jpg. |
| Q42.1 | 42, final word of the corollary | Underlined “dérivation” followed by a full stop | A short comma-like stroke and a lighter, broken stroke stand just to the right of the underline. A comma with stray marks is also possible. The ink is insufficient to identify closing quotation marks. See 042-dérivation-end.jpg. |
| Q43.1 | 43, first line of the Hom paragraph, following $(M,N)$ | “quand” | The word could be the abbreviation “qnd”. Only the initial q and final d have a distinct outline. A long joining stroke takes the place of the internal letters. The crop-only word list also recorded qnd. See 043-quand.jpg. |
| Q43.2 | 43, vertical diagram | A downward arrow from the value at $K'$ to the value at $K''$ | A one-sided head or a plain stroke with a spur are both possible. The only short diagonal meets the vertical above its lowest point. See 043-middlearrow.jpg. |

## Slips

| ID | Scan and text | Proposed reading of the mathematics |
|---|---|---|
| S33.1 | 33, “se réconstituent” | The ordinary spelling is `se reconstituent`. A distinct acute appears above the first syllable. |
| S36.1 | 36, marginal “$\exp 1=0$” | $\log 1=0$ (S36.1R), high confidence. The log series on this sheet has value zero at $1$, and $\exp$ is defined here on nilpotents. |
| S39.1 | 39, $u\longleftarrow e_u$ | The longer arrow on that line has the direction $u\mapsto e_u$. Low confidence that this is a slip. The short arrow may indicate the inverse correspondence. |
| S39.2 | 39, $u_K$ within the exponential | The evaluation at $K'$ suggests $u_{K'}$. Medium confidence. The same row explicitly puts $K'$ on the power in the sum. |
| S39.3 | 39, $\mathbb A\mathrm{ut}_K\,M))$ twice | An opening parenthesis before $M$ would pair the two closures. Medium confidence. |
| S40.1 | 40, the first proposition asks for a $\mathbb G_{aK}$-morphisme | Its stipulated actions are formal, so the group in this clause would be $\overline{\mathbb G}_{aK}$. High confidence. The next corollary treats ordinary parameters under nilpotence. |
| S40.2 | 40, $v\in\mathbb N\operatorname{End}_K(N)$ | The proof calls $v$ nilpotent. $N(\operatorname{End}_K(N))$ would parallel the hypothesis on $u$. Low confidence about the status of the doubled N, which may be shorthand. |
| S41.1 | 41, $c_{ij}$ identified with $1/(i+j)!$ | Moving the other terms to the right gives $-1/(i+j+1)!$ (S41.1R). At degree one the previous line gives $-1/2$. The coefficient in that comparison is clear. Confidence in attributing an error to the retouched general formula is low. |
| S41.2 | 41, “Or soit $U=\operatorname{End}_K(M)$” | The operators in this two-module argument act on $\operatorname{Hom}_K(M,N)$ (S41.2R). High confidence. Left composition by $v$ needs codomain $N$. |
| S41.3 | 41, $ij\geq1$ below the last $\sum$ | $i+j\geq1$ (S41.3R) includes the pure left and right terms. Low confidence for the attribution because the adjacent occurrence of the subscript has two possible readings. |
| S44.1 | 44, $\mathbb E_{\theta+\theta'}=\mathbb E_\theta+\mathbb E_{\theta'}$ | For commuting derivations one expects composition (S44.1R). Addition fails on $1$ already for two identity operators. The first letter on the right has an earlier layer, so confidence in the proposed correction is low. |

## Pointers

| Scan | His words | Destination on these sheets |
|---|---|---|
| 33–34 | “la précédente”, “les conditions 1) à 4) ci-dessus” | The preceding game terminology, then the four conditions in the proposition. The earlier definition referred to on 33 lies before this selection. |
| 36 | “par 3°”, “conditions de la Remarque”, “comme dans Exemple 1” | Part 3 of Th 1, its following remark and the first reduction example. |
| 37 | “cf. Ex. 1”, “Th. 1, 2°” | The nil-ideal example and commuting-exponentials identity on 36. |
| 39 | “comme tantôt”, “le cas précédent 1°” | The units-functor construction and its proof on 37–38. |
| 41 | “On a déjà vu l'équivalence de (1) à (3)” | The intertwining criterion and the four-item proposition on 40. |

No outside publication, archive cote or named person is cited on these leaves.

## Remarks of the model

- **R34.1 · Model, low confidence about the game convention.** On 33 the reply tests explicitly exclude $C_0$. In condition 1 on 34 there is no such restriction on $x$. If $R(x)$ is empty at a terminal winning position, that position cannot meet the existential condition. The earlier definitions needed to decide how the author treats such positions fall outside these leaves.
- **R39.1 · Model, high confidence.** Take $K=\mathbb Q$ and $M=\mathbb Q[t]$. For each $\mathbb Q$-algebra $R$, substitution $p(t)\mapsto p(t+\lambda)$ on $R[t]$ is a natural ordinary additive-group action. Its value on $t^d$ has a $\lambda^d$ term for every $d$. Thus no degree bound works for all of $M$. Its first coefficient $d/dt$ is locally nilpotent on vectors, with no common nilpotence exponent. This gives a counterexample to both the uniform coefficient assertion P39.1 and the surjectivity asserted in P39.2 under the functor definition on 39.
- **P39.1R and P39.2R · Model, high confidence.** For a finitely generated $M$, bounds on the images of finitely many generators give a common bound for a polynomial family. For an arbitrary $M$, a locally nilpotent endomorphism already gives an ordinary action by the exponential evaluated on each vector. Translation is one such action missed by restricting to globally nilpotent endomorphisms.
- **R41.1 · Model, high confidence.** The last inference on 41–42 only needs a polynomial with zero constant term in the two commuting nilpotent operators. If their nilpotence exponents are $p,q$, taking power $p+q-1$ kills every monomial in that polynomial. The numerical coefficient in S41.1 does not enter this inference.
- **R44.1 and R44.2 · Model, high confidence for the examples, medium for the intended scope of “loc nilpotente”.** On the affine coordinate ring $\mathbb Q[t]$, exponentiating $d/dt$ sends $t$ to $t+1$, even though the ring is reduced. On the open where $t$ is invertible, its iterated derivatives on $t^{-1}$ never vanish. The ring example therefore tests a weaker hypothesis than local nilpotence on every germ of the structure sheaf.
- **R44.3 · Model, high confidence under the stated hypothesis.** If the stalks are local $\mathbb Q$-algebras and the derivation is locally nilpotent on every germ, exponentiation does induce the identity on the reduction. The positive-degree coefficients of a polynomial unit vanish modulo the nilradical. Applying this to the exponential of a unit, and using that either $a$ or $1+a$ is a unit in a local ring, gives the required stalkwise conclusion.
