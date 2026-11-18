# K84-05 · Mathematical notes

The letter χ below denotes the first candidate for the recurring handwritten scalar. The notes follow the order of the calculations. Statement identifiers also locate the entries in CHECK_EVENTS.tsv.

## What the pages do

**U1 · A lift and its retraction, 67–68.** A lift $T$ of the scalar χ under an augmentation ψ gives a map from the base ring into the extension. It also gives a map back to the kernel, characterized after inclusion by $x\mapsto\chi x-\psi(x)T$. Starting with the latter map, the author factors the complementary expression through the quotient, then evaluates at a local section of augmentation 1 to recover $\psi(T)=\chi$.

**U2 · A product of two extensions, 68–70.** The diamond in $E_1\otimes E_2$ has $L_1\otimes L_2$ at its top and mixed tensor factors at the sides. The two maps from the mixed factors to $L_1\otimes L_2$ agree on their common part, where they act by χ. Their induced map μ is used to push out an extension. A second diagram arranges the map to the product kernel using $\pi_{E_1}\otimes\pi_{E_2}$.

**U3 · Recovering the product lift, 70–72.** Substitution of $T_1*T_2$ into the projection identity gives $\chi^2 T=\chi(T_1*T_2)$. The author singles out regularity of χ on $L_1\otimes L_2$ before the cancellation leading to $\chi T=T_1*T_2$. The struck trials with $1/\chi$ and the surviving regularity qualification are both visible.

**U4 · Translating the torsor inputs, 72–74.** Multiplication takes $P_1\times P_2$ into the augmentation-one fibre $P$. Translating the inputs produces two terms linear in their increments and a mixed term $\chi u_1\otimes u_2$. The b’s at the foot of 72 appear in $T_i=\chi x_i+b_i$. On 73 the author introduces $b_{T_i,x_i}=\chi x_i-T_i$, and the coefficient for the product point becomes the tensor of these signed coefficients. Scan 74 collects the resulting rules.

**U5 · Trivialisation of the product, 75.** The displayed rule is $\pi_E(x_1*x_2)=\pi_1(x_1)\otimes\pi_2(x_2)$. The first computation restricts one input to the kernel. With both inputs in their torsors the calculation gives $T=\chi(x_1*x_2)-b_1\otimes b_2$ in the convention $b_i=\pi_i(x_i)$. At the foot the author checks $\chi T=T_1*T_2$ by expansion. An oblique NB gives the formula on ordered pairs in the chosen splittings.

**U6 · Biaffine maps and a universal problem, 76–77.** The target is a torsor Π under a module M. A candidate pairing $f$ is accompanied by a bilinear map $\alpha:L_1\times L_2\to M$ that specifies its change on translating either input. The author writes down the simultaneous translation, discusses how much one value determines, and retains $(f,\alpha)$ as data because the bilinear part need not be unique. Scan 77 names the product torsor and its pairing as a solution. It then imposes a compatibility involving the trivialisation of the target.

**U7 · Morphisms, 77–78.** A map of torsors is paired with a map of translation modules. The two lower identities on 77 express compatibility with translation and with π. For extensions carrying distinguished lifts the latter requirement is written $f(T)=T'$.

**U8 · A split torsor, 78–79.** Choosing $x_0$ identifies $P$ with L and gives coordinates $x=\lambda x_0+u$ in E. The single coefficient $b=\pi(x_0)$ determines $T=(-b,\chi)$ and $\pi(u,\lambda)=\lambda b+\chi u$. The end of 78 checks the expression for π. For split inputs the chosen product point is $x_1*x_2$, and its coefficient is $b_1\otimes b_2$.

**U9 · Commutativity and associativity, 79.** The commutativity map swaps the two torsor inputs and the two kernel factors. The associativity map moves the parentheses in the corresponding threefold expressions. For each map the author says that these actions determine it.

**U10 · The unit and an invertibility criterion, 79–80.** The unit presentation starts with a splitting whose b is a basis. With the resulting identification of L and the base ring the sheet gives $\pi(u,\lambda)=\lambda+\chi u$ and $T=(-1,\chi)$, followed by the unit maps on chosen points and on translation modules. A diagonal NB gives a criterion for invertibility under $*$, in terms of an invertible L and the section obtained by restricting T to $V(\chi)$. It also describes a local criterion with b a basis. The equation where this note crosses the horizontal text is uncertain.

**U11 · The involution, 80–81.** After the specialization $\chi=2$, scan 81 defines $\sigma_E(x)=\bar x=T\psi(x)-x$. It preserves ψ, squares to the identity, negates the kernel and induces the identity on the quotient. With 2 invertible the fixed summand $E_0$ splits the extension. The margin identifies its augmentation-one point by $2x_0=T$. In the resulting coordinates the sheet gives $T=(0,2)$ and $\pi(u,\lambda)=(2u,0)$.

## Statements left without proof

- **P1 · 72.** The oblique « NB Si $\{b_1\}$ est une base de $L_1$ » asserts that $x_2\mapsto x_1*x_2$ gives « un iso » of torsors and indicates the associated map $u_2\mapsto-b_1\otimes u_2$. The note supplies no inverse.
- **P2 · 73.** The small « Re NB » says « on vérifie [or vérifierait] aussitôt » that changing the chosen sections leaves the expression unchanged. It specifies the replacements, with a sign warning, without writing out the comparison.
- **P3 · 76–77.** « est une solution du pb universel défini par cette notion », followed by « une solution de [or du] ce problème universel ». The universal factorizations and their uniqueness are not constructed on these sheets.
- **P4 · 79.** The descriptions of commutativity and associativity both end « ce qui suffit à le caractériser ». No separate uniqueness argument follows either description.
- **P5 · 80.** « Les compatibilités entre les contraintes d’unité, d’assoc., de commutativité... » ends without a completed assertion or a diagram. The marginal « est inversible pour * sss » gives criteria and compares some of them, without constructing a product inverse here.
- **P6 · 81.** Under the invertibility hypothesis, the sheet records the identities with $\operatorname{Ker}(1-\sigma)$ and $\operatorname{Im}(1+\sigma)$ and the description of $x_0$. The calculations above establish the action on E, the kernel and the quotient. There is no separate proof of the image description in this extract.

## Questions and conjectures

None explicitly formulated. The « (!) » on 71 flags the fraction involving χ. The « Attention signe ! » on 73 accompanies an actual change of coefficients rather than a stated conjecture.

## Slips

| ID | Scan | Reading retained | Apparent correction and reason | Confidence |
|---|---|---|---|---|
| S1 | 68, top | « section locale x de O » | $x$ should belong to E for $\psi(x)$ to be defined. The letter is rounded and its upper closure is faint. | Low for the proposed slip. The type comparison favours E, but the ink is inconclusive |
| S2 | 68, 73, 74 | In several second-factor formulas an index resembles 1 | $T_2$ in $\psi_2(T_2)$ on 68, $x_2$ in $\pi_{T_2}(x_2)$ on 73, and $\psi_2$ in the second augmentation factor on 74. Compare each with the separately named second object on its sheet. | Low in all three places |
| S3 | 70 | Under the large diagram, $M(=E_1\otimes E_2)$, followed by $M=L_1\otimes L_2$ | The target of the ensuing $\rho$ is $L_1\otimes L_2$. The parenthesis could represent an earlier choice of M. | Medium |
| S4 | 76 | $\alpha(x_1,x_2)$ in the first term on each right-hand side | $f(x_1,x_2)$ has the declared torsor domain and target. The surrounding changes from α to f and from B to α are visible. | Low for a slip in this reworked passage |
| S5 | 80, diagonal NB | $T=2\chi x-b$ | If this recalls the split formula in U8, it would be $T=\chi x_0-b$. The coefficient 2 is visible before χ in the margin. | Low given the intersecting text and the change from $x_0$ to $x$ |

The doubts file locates additional possible index slips, including the first filtration step on 68 and the inner tensor index on 79.

## Pointers

No other cote, work, paper or person is named on these sheets. Internal pointers include « ci-dessus » after μ on 69 and after the variance condition on 76. In the 80 NB the small words after « scindage $x_0$ » may include « cf. »; the destination of that possible reference is unclear.

## Remarks of the model

- **M1 · Model remark, high confidence in the split rank-one calculation, 75 and 79.** Using the coordinate product written in the right margin of 75, interchanging the two sets of coordinates or rebracketing three inputs produces the transformations listed on 79. I checked both coordinates by polynomial expansion with independent variables. This check concerns the split model.
- **M2 · Model remark, high confidence, 81.** The last two boxed formulas are compatible with the overbar rule. In the canonical coordinates the overbar sends $(u,\lambda)$ to $(-u,\lambda)$, and $2x-\psi(x)T$ has coordinates $(2u,0)$.
- **M3 · Model remark, low confidence about the intended scope, 81.** The insertion says « plus gén. si $2\,\mathrm{id}_M$ est inv. ». If M here denotes the kernel L, the fixed-summand description and the formula $E_0=\operatorname{Im}(1+\sigma)$ have different requirements. For $L=0,\ E=\mathbb Z,\ \psi=\mathrm{id},\ T=2$, every element is fixed while the image is $2\mathbb Z$. The issue is how far the inserted qualification was meant to extend.
- **M4 · Model remark, medium confidence, 76–77.** In $\pi_\Pi(f(x_1,x_2))=\pi_1(x_1)\otimes\pi_2(x_2)$, the displayed sides naturally take values in M and $L_1\otimes L_2$, respectively. For the general target of 76 the induced map $L_1\otimes L_2\to M$ would make the comparison meaningful. For the product torsor itself the two targets already coincide.
- **M5 · Model reading question, low confidence, 68, lines 1–5.** The frozen reading is O in « section locale x de O ». A close look at the rounded character also admits a U shape. The maps in the calculation suggest E, but they do not supply the missing strokes. The transcription has been left as hashed.
