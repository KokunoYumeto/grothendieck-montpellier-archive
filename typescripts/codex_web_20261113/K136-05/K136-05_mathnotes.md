# K136-05 · Mathematical notes

## What the pages do

**Complexes and homotopy type, scans 17–18.** Grothendieck asks what “linear” algebraic data can be associated with a topological space or a simplicial object. He relates a divided-power de Rham complex to a second bigraded complex, first using multiplication by $dT$, then writing a kernel in bidegree $(p,q)$. He asks how much of the multiplicative structure with divided powers one can recover from such a complex. The integer-coefficient variant and the finiteness proviso are interlinear additions.

**The digit calculation, scans 20–21 (B20).** For $c_{ij}=(i+j)!/(i!j!)$, Lemma 1 gives a product modulo $p$ over the base-$p$ digits of $i,j$. It identifies nonvanishing with addition without a carry in any position. To peel off the lowest digits he writes $i=u+pr$, $j=v+ps$ and compares monomials in a two-variable expansion. He treats $u+v\leq p-1$ and $u+v\geq p$ separately.

**Shifted coefficients, scan 21.** Under $N+1=(N'+1)p$, Corollary 2 compares coefficients indexed by $N+1,p^\varepsilon-1$ and by $N,p^\varepsilon$ with coefficients one digit shorter. Its two cases involve, respectively, divisibility of $N'+1$ and a single digit of $N'$. The proof writes out the expansions for $N,N+1,N',N'+1$.

**A finite family, scans 21–23 (F21).** Lemma 2 uses only $N$ and $N+p^\varepsilon$, with $\varepsilon$ in a finite interval. For a module over the integers localized at $p$, the specified binomial relations imply $x_N=x_{N+1}$. The proof sets $y_\varepsilon=x_{N+p^\varepsilon}-x_N$, weakens the system to vanishing tests indexed by units, and descends from $N$ to $N'$. The sideways example on 21 singles out an $x_4$ which can still vary.

**Theorem 1, scan 23.** For a family in an abelian group and relations $\binom ji(x_j-x_i)=0$ for all $j>i\geq N$, the tail is constant. The proof localizes at each prime and applies the finite lemma to consecutive indices. The preceding induction ends on this sheet with “cqfd. Ouf !”.

**Graded modules of divided powers, scans 23–25 (G24).** For $S=k\{T\}$ the ideal $S^{+(N)}$ is spanned by $T^{(i)}$ with $i\geq N$. The corollary defines a graded functor on $k$-modules and asserts full faithfulness. A compatible family $x_i$ is obtained from a single $x$ by $x_i=xT^{(i)}$. The proof applies the preceding theorem to coefficients $\xi_i$, then to the component maps $u_i$ of a graded morphism. The square on 25 shows these maps commuting with multiplication by a divided power.

**Adjunction and truncation, scan 25.** The first remark constructs a right adjoint $\pi_N$ as a subset of a product of graded components, cut out by the compatibility relations. The displayed unit map restates the preceding bijection. The second remark compares two starting degrees $N\geq N'$ by keeping the components of degree at least $N$.

**Virtual shadows, scan 26.** The category $\mathrm{Omb}(k)$ consists of graded modules over the divided-power polynomial algebra. Grothendieck singles out objects zero in degrees at least $N$, describes the quotient by them using truncation, and gives the corresponding Hom identity. He then calls an object negligible when each of its elements is killed by a sufficiently high divided-power ideal. The phrase “et le localisé est” ends the sheet.

**A theorem on the map out of $M\otimes_k S$, scan 27.** He asserts that the displayed map involving the truncation and $\varphi$ is an isomorphism in nonnegative degrees. He restates the assertion in terms of an essential image, then as an isomorphism to a degree-$i$ Hom group. A corollary asserts that the indicated positive Ext groups vanish.

**Coefficient reformulation and localization, scans 27–29.** Given $0\leq i\leq N$, the theorem specifies a family $(\xi_k)_{k\geq N}$ by the relations labelled (1). Its conclusion (2) expresses each term using a single $\xi$ and $\binom{k}{i}$. Scan 28 reduces existence and uniqueness to localized modules, using an integer linear combination of coefficients equal to 1. Scan 29 exhibits arbitrarily large indices with a unit coefficient and subtracts a candidate solution. It remains to show that the difference family vanishes.

**Comparing indices, scans 30–32.** Lemma 1.1 compares vanishing at two indices when the stated coefficients are units. Two factorial quotients give the comparison; a longer attempted calculation is crossed out on 30. On 31 a digit-by-digit complement leads to a common comparison index $p^{r+1}-1$ on 32. The rotated “Présentation plus simple” on 31 uses $p^r-1$ with its own choice of $r$. The final paragraph on 32 sets up one more shift by $l$ and stops at “on veut”.

## Statements left without proof

| Scan | His words | What remains in these sheets |
|---|---|---|
| 17 | “On peut aussi définir …”; “qui permet de reconstituer …” | He describes what the multiplicative structure should recover, without giving the definition or reconstruction in full. |
| 25 | “Le foncteur … admet un adjoint à droite” | The remark supplies the adjoint and its Hom formula. A separate verification of naturality is not given here. |
| 26 | “C’est une sous-catégorie épaisse”; “la catégorie quotient est can. équivalente”; “C’est encore une sous-catégorie épaisse” | The thickness and quotient assertions are stated alongside the descriptions of the objects and functors. |
| 27 | “Cor” followed by the vanishing of positive Ext; “seul le cas $i<N$ est non trivial” | The Ext assertion has no separate proof in this extract. |
| 32 | “il suffit de prouver qu’il existe $l\geq0$ …”; “on veut” | The surviving text does not finish this last step for general $k$. |

## Questions and conjectures

- **Scans 17–18.** “à expliciter…” leaves the structures on $D$ unspecified. “J’ignore si … suffit déjà pour récupérer toute la structure” asks about recovery from the complex. The phrases “sous réserve de conditions de finitude” and “du moins si” qualify the proposed homotopy application.
- **Scan 24.** “Bijectivité ?” is answered in the ensuing paragraph by reducing to a constant family of coefficients.
- **Scan 26.** “[à degrés $\geq0$ ?]” leaves the grading convention open where virtual shadows are introduced.

## Slips

| ID, scan | Written and possible correction | Reason and confidence |
|---|---|---|
| S20, 20 | The last first-index glyph of the no-carry implication looks like $v$; $r$ would repeat (*). | The recurrence uses $c_{r,s}$. **Low** because the ink also admits $r$. |
| S23, 23 | The last tensor is subscripted $S$; $k$ appears intended. | Only a $k$-module structure has been given on $M$. Scan 25 explicitly tensors over $k$ in the same construction at $N=0$. **High** for the discrepancy. |
| S25, 25 | The definition of $\pi_N$ has $x_{j+j}$ where $x_{i+j}$ is expected. | Both lower letters turn down. Formula (*) on 24 and the square on 25 put the product in degree $i+j$. **High**. |
| S28, 28 and 32 | Several coefficients have the form $c_{k,k-i}$ where (2) calls for $c_{i,k-i}$. | At $k=3,i=1$ the two expressions give 10 and 3. The clearly written later occurrences differ from the accompanying binomial. **High** for that arithmetic distinction. **Low** for attributing a particular intention to an overwritten first index. |
| S32, 32 | The “savoir” clause ends with $=0$; a condition of nonvanishing modulo $p$ appears intended. | Both horizontal strokes are visible. The preceding lemma compares indices with unit coefficients. **Low** for the proposed correction because the adjacent index is doubtful. |

## Pointers

- **Scan 17.** “les complexes de De Rham-Sullivan” is the only named mathematical comparison with another construction. No title, date or bibliographic reference accompanies it.
- **Within these pages.** “Il résulte du th.” (24) and “le th. nous permet de conclure” (25) refer back to the rigidity argument. “Le cas $i=0$ a été traité déjà par une démonstration spéciale” (27) points to an earlier argument. The occurrences of “(1)”, “(2)” and “(1.1)” on 28–32 refer to the coefficient theorem and its comparison lemma.

## Remarks of the model

- **R20, scan 20 — high confidence for the finite check.** For $p=2,3,5$ and all $0\leq i,j\leq30$, direct evaluation of the factorial coefficient agrees with the digit product and its no-carry nonvanishing test in all 2,883 cases. This checks the reading of the two assertions on a finite range.
- **R21, scan 21 — high confidence.** In the sideways example with $p=N=e=2$, the coefficients for the pairs $(2,3),(2,4),(2,6),(3,4),(3,6)$ are $3,6,15,4,20$. Only the first and third are odd. This accounts for the author’s $x_2=x_3=x_6$ and leaves $x_4$ free under precisely the relations imposed there.
- **R26, scan 26 L12 — reading question, low confidence.** The frozen first argument on the right of the Hom identity is $\tau_N(\mathcal M)$, with $\mathcal N$ already marked as an alternative. The left-hand source is $\mathcal N$. The functorial reading favours $\mathcal N$; the paired curves in the right-hand capital look like $\mathcal M$.
- **R31, scans 31–32 — high confidence.** The margin chooses $r$ by $p^r>i+j$ and writes $p^r-1$. The main calculation numbers digits from 0 through $r$ and writes $p^{r+1}-1$. These are separate choices of digit length, so the different exponents can coexist.

