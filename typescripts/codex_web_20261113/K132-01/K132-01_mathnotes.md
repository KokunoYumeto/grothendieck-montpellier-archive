# Mathematical notes · Montpellier, cote 132

Scan numbers refer to the archive PDF. The identifiers are shared with CHECK_EVENTS.tsv. Quotations are from the handwritten pages. The coiled letter for the discrete quotient on 017–018 has two possible readings; below it is called the discrete quotient.

## What the pages do

**FP1 · Comparison of fibre products (002–003).** Given $X\to S\leftarrow Y$ with the first map a Serre fibration, the notes compare the fundamental groupoid of $Z=X\times_S Y$ with the 2-product of the fundamental groupoids. After choosing base points, an object of the latter is an element $\sigma$ of $\Sigma=\pi_1(S)$. Its isomorphism class is a double coset in $H\backslash\Sigma/G$, and its automorphisms are the stabilizer of $\sigma$. The two fibre sequences on 003 yield the same description of $\pi_0(Z)$. A path construction in the last paragraph describes how changing the choices changes the representative.

**FP2 · Kernel of the comparison (004).** The two exact-sequence diagrams compare the ordinary fibre with a groupoid denoted $\Phi$. At the identity representative, the kernel on fundamental groups is expressed as $\operatorname{Coker}(\pi_2(X)\times\pi_2(Y)\to\pi_2(S))$. The sheet reads off a surjectivity criterion for the map on fundamental groups to be an isomorphism. It then considers vanishing of the higher homotopy groups when $X,Y,S$ are “1-tronqués”.

**EN1 · Objects and morphisms of a groupoid construction (006).** A functor $D\to C$ comes with specialness and orientation data. The page draws maps between such functors and maps between the maps. For connected nonempty $C$ it uses a group $G$, an index set $I$ and maps $\mathbb Z\to G$. An object of the resulting Hom is given by $u,v,\alpha$ satisfying a conjugacy condition on the distinguished elements. A morphism has components $\lambda$ and $\mu$, with equations boxed at the foot of the sheet.

**EN2 · Components and loops of End (007–008).** The calculation of $\pi_0$ identifies pairs consisting of a permutation of $I$ and an exterior automorphism carrying each distinguished element to its required conjugacy class. The next calculation takes automorphisms of the identity. It gives trivial $\pi_1$ in the general case. For the sphere with two holes the answer is $G$, isomorphic to $\mathbb Z$ noncanonically. For the sphere with one hole the displayed isomorphism with $\mathbb Z$ is canonical.

**FIX1 · Fixing the source (008–009).** With $D$ fixed, objects become pairs $(v,\alpha)$, and a morphism is specified by $\mu$. The sequence labelled “Teichmüller spécial” and “Teichmüller à trous” is used to compute the kernel of the forgetful map $\psi$. The answers recorded are $\mathbb Z^I$ in the general case, $\mathbb Z$ for the cylinder, and $TS=0$ in the one-hole case. The final line gives $\pi_1(\mathrm{End}_{D\ \mathrm{fixé}})=1$.

**T1 · Data attached to tubes and complexes (011–012).** The entries on 011 combine a circularised combinatorial 1-complex with groupoids $\Pi_d$ and $\Pi_b$. The co-circuits and the components of $\Pi_b$ enter three summands defining $D,C,\varphi$. A second target and “foncteur bordant” appear below the rule. Scan 012 starts a related description with $K_1,\Pi_b$ and a Hom which is a product involving $\mathrm{Cat}(\mathrm{Isom}(\cdot,\cdot))$ and $\underline{\mathrm{Equ}}$. The index of the second factor is obscured.

**EX1 · Components after pulling back an extension (014–016).** The pullback along $u:H'\to H$ gives a comparison $c:\pi_0G'\to\pi_0G\times_{\pi_0H}\pi_0H'$. The author asks what additional data determine $\pi_0G'$. He reduces to a discrete kernel by dividing by $N^0$. With $\varphi:\pi_1H\to N$, the displayed kernel of $c$ is $\pi_1H/(\ker\varphi+\operatorname{Im}\pi_1(u))$. The paragraph calls this a quotient of $\operatorname{Coker}\pi_1u$.

**EX2 · Connected base (016).** In case β) the connected-base extension is described via a homomorphism from $\pi_1H$ to the centre of $N$. To obtain the extension over $H'$, the page first pulls back the covering group $\widetilde H$ and then takes the image under the indicated map to $N$.

**TR1 · Two compatible trivialisations (017–018).** An extension of $H$ by $N$ is pulled back to $\widetilde H$. The added lines impose invariance on a splitting, and the later paragraph asks for strict trivialisations over both $\pi$ and $\widetilde H_0$. If $\pi\subset\widetilde H_0$, the top of 018 expresses the remaining datum as a homomorphism $\pi\to\mathfrak z(N)$. The sloping note discusses equivariance. The cancelled working below juxtaposes extension groups, Hom, quotient diagrams and degree-two cohomology.

## Statements left without proof

| ID | Scan | Wording and scope |
|---|---|---|
| P1 | 007 | “son centralisateur est le groupe engendré par $h_j$”. This is used to obtain the integers $\lambda_i$; the one-hole sphere is discussed separately. |
| P2 | 007 | “en fait leurs images dans $G_{\rm ab}$ sont distinctes !” This is given as a reason that the permutation is determined by the exterior automorphism. |
| P3 | 008 | “le groupe $G$ est libre à … $\geq2$ générateurs, donc son centre est nul”. The rank symbol is marked as doubtful. Freeness is invoked in the case other than the one- and two-hole spheres. |
| P4 | 009 | “On trouve d'autre part, trivialement,” followed by the fixed-source $\pi_1=1$. The page ends at the displayed answer. |
| P5 | 014 | “Il est facile de voir sur des exemples que cet hom (qui est tjrs surjectif) n'est pas néc. bijectif.” No example is displayed there. The kernel computation follows on 016. |
| P6 | 016 | “l'ext. $G$ est caractérisée, à isom unique près, par un hom”. The universal-group construction follows; uniqueness is stated. |
| P7 | 017 | “si $\widetilde H_0$ est connexe et simplement connexe, il existe pour $G$ donné une unique telle trivialisation…” The NB invokes this assertion without a proof. |

## Questions and conjectures

- **Q1 (003).** “donner une description symétrique en $X,Y$ …” is a marginal request attached to the path and double-coset description.
- **Q2 (006–008).** A question mark above the Hom equality on 006 introduces the explicit data. The analogous questions are $\pi_0(\underline{\mathrm{End}})\overset{?}{=}$ on 007 and $\pi_1(\underline{\mathrm{End}})\overset{?}{=}\mathrm{Aut}(\cdots)=\ ?$ on 008. The calculations follow each question.
- **Q3 (014–015).** “Notre propos est de préciser des données algébriques simples” on 014 becomes “déterminer … l'extension” on 015. The words at the start of 016 complete the object of that verb.
- **Q4 (018).** A mark beside the capital in the right-hand cancelled ladder can be read “G?”. Both readings are recorded. The sheet gives no verbal conjecture there.

## Slips

| ID | Scan | Reading kept, possible correction and reason | Confidence |
|---|---|---|---|
| S1 | 002 | After $(g,h)\in G\times H$ the written action uses $(h,g)\cdot\sigma$. With the factors ordered as just declared, its argument would be $(g,h)$. | High |
| S2 | 004, 006 | The set of pairs at $\sigma=1$ on 004 lacks a visible closing brace. The parenthesis starting $(i\in I$ on 006 lacks a visible close. Both would normally close at the end of the expression. | Medium |
| S3 | 007 | The last NB begins with $\sigma$, and the concluding subgroup has $\widetilde u$ followed by a condition on $\widetilde v$. The preceding pair suggests $u$ for the permutation and $\widetilde v$ for the exterior class. | Medium |
| S4 | 008 | The last comparison ends in $\operatorname{int}(\mu_0)\operatorname{int}\alpha_1(i)\,v_1(h_i)$. The earlier object identity suggests $h_i$ as the final argument. The aligned expression above includes a doubtful peripheral symbol. | Low |
| S5 | 011 | The arrow at (c′) bears $\varphi_c$ while the decomposition uses $\varphi_d$. The latter matches $\Pi_d$; the former could instead refer to item (c). | Low |
| S6 | 012 | “boucles isolés” would take “isolées” under usual agreement. | Medium |
| S7 | 014 | The two final arrows point towards the primed groups. Functoriality for the stated $u:H'\to H$ gives arrows towards the unprimed groups. The writing around the first H and the ending of “induit” are doubtful. | Low |
| S8 | 015 | Both quotient squares have H and H′ as their left entries. N⁰ is introduced as a subgroup of G and G′. Replacing the H’s by G’s would give the quotients from the preceding paragraph. | Medium |
| S9 | 015 | After “Supposons connus … $\pi_iH'$” the sheet writes $\pi_iG$. The primed version $\pi_iG'$ fits the preceding sentence and the $\pi_1G'$ immediately following. | High |
| S10 | 016 | The line begins “Cel” without a visible final a. “Cela” would complete the word before the crossed verb. | Medium |

## Pointers

- **002–003.** “fibration de Serre” names the fibration used twice in the comparison.
- **008–009.** The interlinear identification “i.e. le cylindre” on 008 explains the special case taken up on 009. Under $TS$ and $T$ on 009 appear “Teichmüller spécial” and “Teichmüller à trous”.
- **014–017.** The local references (E), (E′), (S), (S′) point to the displayed extension and component rows. The reference “cf ci-dessous pour déf. de $\widetilde G$” on 017 points to the pullback on the same sheet.
- **017–018.** “un splittage … du diagramme” at the end of 017 continues into the first diagram on 018. No other cote, dated paper or bibliographic title is cited in these pages.

## Remarks of the model

- **M1 · Model remark, high confidence (002).** With the two group maps in their written order, fixing $\sigma$ in the displayed action yields precisely the stated condition on morphisms from $\sigma$ to itself. This checks the stabilizer wording independently of the order slip in S1.
- **M2 · Model remark, high confidence (009).** In the cylinder calculation the two coordinates change by $+\mu$ and $-\mu$. Their sum is invariant, and the handwritten “opération somme” singles out that same sum. This concerns the kernel computed on 009. The marginal “pas canoniquement” on 008 refers to a different identification, between $G$ and $\mathbb Z$.
- **M3 · Model remark, high confidence (016).** The two appearances of the kernel description use the same subgroups as the quotient of images immediately above. When $\pi_1u$ is surjective the displayed denominator is all of $\pi_1H$, so the displayed obstruction vanishes.
- **M4 · Model remark, low confidence (018).** The bottom Ext–Hom and $H^2$ expressions may have been attempts to recast the strict-trivialisation problem in terms of extension classes. Long diagonal strokes pass through them and several labels are overwritten. Their status as assertions is unclear.
- **RQ1 · Reading question (006, fragment line 37; 008, line 45).** The frozen transcription uses $h_i$ for the peripheral family; $\ell_i$ is a possible reading of the tall loop. The small second stroke is clearest in some occurrences and disappears into the return in others. This affects the name of the family throughout these calculations.

- **RQ2 · Reading question (011, fragment line 3; 012, line 2).** The frozen heading begins “Catégorie ou” before the doubtful word. At enlargement the first small sign on 012 looks like two joined humps followed by a short detached horizontal. A symbol such as $\infty$ followed by a hyphen is another possible reading of “ou” at this place. The rotated heading on 011 gives a similarly compact sign. Confidence is low.
