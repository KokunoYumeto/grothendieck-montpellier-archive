# Mathematical notes · cote 157-2, scans 147–162

Scan numbers refer to the supplied images. Grothendieck’s own pages are 92–107. The numbered entries identify the statements discussed in the check record.

## What the pages do

**U1 · Scans 147–148.** The corollary concerns two arrows $u_1,u_2:C\to C'$ between objects fibrant over $S$. If they agree after precomposition with $i:X\to C$, under the stated cofibration and weak-equivalence conditions, they agree in the localization of $\underline{\mathrm{Fib}}\,S$. The weak-equivalence condition is inserted; the prime on its $i$ is doubtful. The proof factors the diagonal of $C'$, lifts through the fibration $\delta'$, and compares the two projections after precomposing with $i'$. Scan 148 checks that the intermediate object is fibrant, so this comparison takes place in the indicated category.

**U2 · Scans 148–149.** For a full subcategory $\mathcal F$ between $\underline{\mathrm{Fib}}\,S$ and $\mathcal M_{/S}$, the inclusion gives $\delta$ on the localizations at $W_S$. The replacement construction gives $\gamma$ in the other direction. On each side the comparison at $X$ is $i_X:X\to C(X)$. Grothendieck explicitly flags naturality for each composite.

**U3 · Scans 149–150.** A class $\mathcal L$ of changes of base tests the arrows in $W_S^{\mathcal L}$. An arrow passes the test when its pullback by every $S'\to S$ in $\mathcal L$ belongs to $W$. The text assumes isomorphisms and closure under composition. It also considers local isomorphisms and local co-isomorphisms in $\mathrm{Cat}$, with alternatives in the margin. Testing at $\mathrm{id}_S$ gives $W_S^{\mathcal L}\subset W_S$ and a localization functor $\rho$ from the finer localization to the coarser one. Hypothesis 1 requires equality of the two classes on fibrant objects over $S$.

**U4 · Scans 150–152.** A Quillen-type sufficient condition for Hypothesis 1 is that pulling an arrow in $W$ back along a fibration preserves $W$, in addition to the factorization already available. To handle an arbitrary change of base $g$, he factors it into a weak equivalence followed by a fibration. The two cases are treated on scan 151; the last comparison of the pulled-back horizontal arrows is on 152.

**U5 · Scans 152–154.** The inclusion of fibrant objects gives $i_0$ into the finer localization. Composing $i_0$ with the inverse of the equivalence to the coarser localization gives $i$ with $\rho i\simeq\mathrm{id}$. Grothendieck seeks the adjunction $\rho\dashv i$. Its proposed unit is induced by $X\to C(X)$ in the finer category. The proposed counit uses the inverse of that arrow in the coarser one. He reduces the remaining comparison to $C(i_X)=i_{C(X)}$ in the finer localization.

**U6 · Scans 154–155.** In $\mathrm{Cat}$ he recalls a path-composition arrow $c:C(C(X))\to C(X)$ that equalized the two maps. In the Quillen case he instead puts $u=i_X$ in the square defining $C(u)$. The two composites with $i_X$ agree. The corollary of manuscript page 92 gives equality in localized $\underline{\mathrm{Fib}}\,S$; Hypothesis 1 on page 95 carries it into the finer localization.

**U7 · Scans 156–159.** A functor $\mathrm{Ch}$ on $\mathcal M$ now supplies a factorization of each diagonal by $\alpha_X$ and $p_X$. The two projections of $p_X$ give source $\sigma_X$ and target $\beta_X$. For $f_X:X\to S$, pull back $\sigma_S$ along $f_X$ to form $C(X)$. Its map to $S$ uses the *target* on $\mathrm{Ch}(S)$, while its section over $X$ comes from $\alpha_S$. Under Hypotheses 2–4 and the preceding stability assumptions, $X\to C(X)\to S$ is functorial, with first leg in $W$ and second leg in $\mathrm{Fib}$. Hypothesis 1 then reduces the remaining equality to one in $(\underline{\mathrm{Fib}}\,S)W_S^{-1}$, whose formulation is independent of $\mathcal L$.

**U8 · Scans 159–160.** Writing $X(T)=\mathrm{Hom}_{\mathcal M}(T,X)$, Grothendieck describes $\mathrm{Ch}(X)(T)$ as paths in $X(T)$. A point of $C(X)$ is a pair $(x,c)$ with $c$ starting at $f_X(x)$. A point of $C(C(X))$ adds a path $c'$ starting at $\beta(c)$. The two displayed maps insert a constant path, respectively before and after $c$. The order in which the preceding sentence names those maps raises the question in R1.

**U9 · Scans 161–162.** Composition is introduced as a map from the fibre product of paths with matching endpoints. The composite must retain the source of the first path and the target of the second. With bilateral units, $(x,c,c')\mapsto(x,c'\circ c)$ defines $\gamma_X:C(C(X))\to C(X)$ and gives the identity after either insertion. Grothendieck places $\gamma_X$ in $W_S$, inverts it in the localization, and concludes $i_{C(X)}=C(i_X)$. The extract ends with his announcement of a new summary.

## Statements left without proof

| Entry | Scan | Manuscript words and scope |
|---|---|---|
| P1 | 148 | “La transitivité pour $\gamma(u)$ est claire”, followed by the identity assertion. He does not expand the functor laws here. Later, “j'ai oublié de vérifier que $\gamma$ transforme $W_S$ … $W_S$, mais c'est tautologique” dismisses the omitted check. The connecting preposition is unclear. |
| P2 | 149 | “Il faut vérifier que c'est fonctoriel en $X$” and “À vérifier la fonctorialité.” The two objectwise isomorphisms are written down. The respective naturality checks are left open here. |
| P3 | 153–154 | “Mais c'est contenu dans la construction de $C$ comme foncteur” refers naturality to an earlier construction. “Pour prouver l'adjonction … on est ramené à prouver” gives the equality of the two arrows as the remaining task. The extract does not separately set out both triangle identities. |
| P4 | 160–162 | “On suppose donc” leads to composition, and “En supposant donné … supplément de structure” introduces the final calculation. Existence of such a composition with units for an arbitrary $\mathrm{Ch}$ remains an assumption. |

## Questions and conjectures

| Scan | Manuscript words | Question or expectation |
|---|---|---|
| 149 | “ça doit donner le [sign for *même*] résultat”; “Il n'y en … peut-être pas besoin.” | The first marginal note suggests smooth morphisms as an alternative test. The third refers back to a rewritten assumption on $\mathcal L$; its exact attachment is less certain. |
| 150, 152–153 | “Je voudrais définir un foncteur en sens inverse”; “On s'attend que $i$ soit pl fidèle”; “que $\rho$ et $i$ soient adjoints”. | He constructs the reverse functor and then asks for the stronger right-adjoint property. |
| 154 | “Ça avait l'air très délicat”; “Je renonce pour le moment à axiomatiser les propriétés du foncteur” | He recalls the difficulty of constructing composable paths in $\mathrm{Cat}$ and postpones a general axiomatization at this point. |
| 159–160 | “Peut-être y a-t-il moyen …”; “un langage géométrique, pour s'y reconnaître”; “mais en a-t-on le droit ?” | The verb before “un langage géométrique” has two readings. The later question asks whether one may already compose paths with constant paths. |
| 161–162 | “La pensée naturelle, c'est qu'avec cette composition …”; “on n'a sans doute pas besoin de tout” | He considers a category internal to $\mathcal M$ and asks how much of that structure the comparison needs. He retains bilateral units for the calculation. |

## Slips

| Entry | Scan and position | Frozen reading | Suggested reading and grounds |
|---|---|---|---|
| S1 | 147, final comparison | $p_2$ or $\mathrm{pr}_2$ | Possibly $\mathrm{pr}_2$. The same projection is named on the diagram and again on 148. The r at the end of 147 is doubtful. **Low.** |
| S2 | 151, label beside the factorization | $g\in\mathrm{Fib}$ or $\bar g\in\mathrm{Fib}$ | Probably $\bar g\in\mathrm{Fib}$. The second leg carries a bar; the composite bears plain $g$. The disputed bar might already be present. **Low.** |
| S3 | 158, opening display | $\mathrm{pr}_1\pi'$ | Possibly $\mathrm{pr}_1p'$. The right-hand vertical leg with the required domain and codomain was labelled $p'$ on 156. A change of letter on 158 is also possible. **Medium.** |
| S4 | 158, first paragraph | “est dans $i_X$” | Probably “est dans $W$”. The insertion has already identified the section as $i_X$, and the next display explicitly says $i_X\in W$. The anomalous predicate itself is legible. **High.** |
| S5 | 160, upper path diagram and following identity | $1_x$ | Possibly $1_{f(x)}$. The adjacent tuple places the unit at $f(x)$ and $c$ starts there. The shorter notation may be deliberate, and the 1 in the tuple is retraced. **Low.** |
| S6 | 161, paragraph below the triangle | $X(T),\mathrm{Ch}(T)$ | Possibly $X(T),\mathrm{Ch}(X)(T)$. Scan 159 explicitly names the latter as the set of paths. The shorter expression could be shorthand with $X$ fixed. **Medium.** |

## Pointers

| Scan | Manuscript words | Reference |
|---|---|---|
| 149–150 | “dans le cas de $\mathcal M=\mathrm{Cat}$”; “Dans le contexte de Quillen”; “la structure de Quillen soit ‘propre’” | The category example and Quillen's setting. No particular publication is named on these sheets. |
| 152 | “Revenons … l'hyp. p. 95”; “dans les deux cas envisagés” | Hypothesis 1 on scan 150 and the preceding fibrant-category equivalence. |
| 153–155 | “dans le ‘cas Quillen’”; “J'y étais arrivé dans $\mathrm{Cat}$”; “je devrais y revenir tantôt” | Earlier work with paths in $\mathrm{Cat}$, followed by a planned return to their axioms. The struck parenthesis on 153 also contains a doubtful personal qualification about the $\mathrm{Cat}$ case. |
| 155 | “Le Cor. page 92”; “par hypothèse (p. 95)” | Manuscript pages 92 and 95 are scans 147 and 150. |
| 157–158 | “par Hyp.”; “(Hyp 1)” | The numeral on 157 looks like 3, with 4 an alternative. The cited condition is $S\to e$ in $\mathrm{Fib}$. The clear reference on 158 returns to Hypothesis 1. |
| 160, 162 | “Les ‘calculs’ … il y a deux (?) jours”; “Je vais à nouveau résumer ce que j'ai dégagé.” | A retrospective reference without a calendar date, and a prospective summary beyond this extract. |

## Remarks of the model

**R1 · Model remark · Low confidence · Scan 160, the two rows after “respectivement”.** Applying the component $i_{C(X)}$ to $(x,c)$ would append the unit at its target $\beta(c)$. Applying $C$ to $i_X$ would prepend the unit at $f(x)$. The names before “respectivement” appear in the reverse order to these rows. There is overwritten ink before the second name. The potential transposition does not affect the displayed common composite on 162.

**R2 · Model remark · High confidence · Scans 161–162.** The displayed calculation uses only one binary composition for each inserted unit. Each side reduces by a unit law. No expression in this calculation involves three paths whose parentheses would have to be changed. The endpoint conditions still matter for defining the map over $S$.

**R3 · Model reading question · Low confidence as a proposed change · Scan 153, approximately lines 14–17.** The frozen naturality sentence reads $(\mathcal M_{/S})(W_S)^{-1}$. The table above places the proposed unit in $(\mathcal M_{/S})(W_S^{\mathcal L})^{-1}$, which suggests asking whether the finer localization was intended in the sentence as well. The following displayed codomain again has $W_S$ without $\mathcal L$. The local wording supports the frozen reading and leaves the scope of that naturality argument open.
