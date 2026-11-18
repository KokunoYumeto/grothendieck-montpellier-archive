# Mathematical notes · K158-01

Scan numbers refer to the PDF. Line numbers count the manuscript approximately. The statements and quotations in the first five sections belong to the sheets. The final section identifies the model's checks by the same IDs used in CHECK_EVENTS.tsv.

## What the pages do

**A functor built from components (scan 2).** A diagram factors $\pi:B\to\mathrm{Ens}$ through a locally connected topos and $\pi_0$. The sheet gives the Hom formula for $F^I$. A second diagram introduces $P$ and a section $\sigma$. For a subset $E$ of the components of $p(b)$, $P(b,E)$ is denoted by $\widetilde E$. The last calculation indexes a product of summands by $E\times E'$.

**Images, inverse images and products (scan 3).** For a map $u:E\to E'$ the sheet compares $u(F)\subset F'$ with $F\subset u^{-1}(F')$. It expands the product of two coproducts into a coproduct of $z\times z'$ in $Z^\wedge$. Several attempts to relate that formula to the product in the base are crossed out.

**The ordered fibres (scan 4).** The composite $\widetilde\pi:B\to\mathrm{Ens}\to\mathrm{Ord}$ uses $\mathcal P^*$. In $C=\widetilde\pi\backslash B$, an arrow above $u$ is allowed when the image of the source subset lies in the target subset. The sheet calls the projection faithful and describes the category as cofibrée. Its lower diagram factors a cone over $b_\infty=\varprojlim b_i$ using an arrow marked « cocart ».

**The functor to presheaves (scan 5).** With $Z=\pi\backslash B$ coétale over $B$, the sheet sends $(b,E)$ to $\coprod_{z\in E}z$ in $Z^\wedge$ and draws how arrows act. The proposed product over $b\times b'$ has subset $p_1^*(E)\cap p_2^*(E')$.

**A presheaf of components (scan 7).** Assume every 0-connected object of $X^\wedge$ is 1-connected. For $F\in X^\wedge$, passage to its support $U$ makes $F$ epimorphic onto the terminal object of $Y^\wedge$, where $Y=X_{/U}$. The category $\widetilde\Delta$ represents nonempty finite sets by $[0,n]\cap\mathbb Z$. The assignment $\pi_F(I)=\pi_0(F^I)$ is contravariant in $I$.

**Components as objects and arrows (scans 7, 9).** An object $(\widetilde\Delta_n,\alpha)$ gives the component $\alpha\subset F^{n+1}$. A map of the indexing sets induces a map on powers whose restriction sends $\beta$ to $\alpha$. This gives $\varphi:Z\to Y^\wedge$ for $Z=(\widetilde\Delta_{/\pi})^{\mathrm o}$. Its colimit extension is written $\Phi:Z^\wedge\to Y^\wedge$.

**A cancelled approach (scan 8).** The crossed construction starts with $I\mapsto F^I$, passes to a presheaf category and restricts to the support of $F$. Below the cancellation are a map of topoi, an endomorphism-like arrow and an expression involving $f^*$ and exponentiation. The two exponent labels in that expression have different possible readings.

**Transport of connectedness (scans 9–10).** The proposed left exactness of $\Phi$ would give $f:Y^\wedge\to Z^\wedge$. The sheet identifies inverse images of representables with components, extends the 0-connectedness assertion to arbitrary $G$, then invokes the hypothesis on $X^\wedge$. A morphism between the slices over $f^*(G)$ and $G$ is used to conclude that every 0-connected object of $Z^\wedge$ is 1-connected.

**A terminality test and two consequences (scan 11).** The proposed lemma combines that property of $Z^\wedge$ with the condition that $\pi(\widetilde\Delta_0)$ is a singleton. It would force every $\pi(\widetilde\Delta_n)$ to be a singleton. The corollaries concern connectedness of the positive powers of $F$ and local cofilteredness of $X$.

**A candidate for closure under finite limits (scans 12–13).** For arbitrary $A$, set $B=A^{\mathrm o}$ and $Z=(A_{/\pi})^{\mathrm o}$. A nonempty subset $E\subset Z_b$ defines $\widetilde E=\coprod_{a\in E}a$ in $Z^\wedge$. These objects and their induced arrows give the displayed functor $(*)$. Forgetting the order in $\widetilde\pi$ gives the same objects over $B$, with equality in the arrow condition where the ordered construction allows inclusion.

**A revised requirement (scans 13–15).** After asking for full faithfulness and stability of the essential image, the author asks instead for nonempty finite limits in the source and left exactness of $(*)$. Testing the constant singleton functor leads to a condition on $B$ involving binary products and pullbacks or equalizers. Surjectivity of $\pi(u)$ then ensures that inverse images of nonempty subsets stay nonempty. The resulting operation is presented as right adjoint to direct image.

**Limits in a fibration (scans 15–16).** Lemme 1 states that existence of limits of a fixed shape $I$ in the base and fibres gives limits in $C$, preserved by $C\to B$. The following corollary starts with a deleted epimorphism hypothesis and continues across the page turn. Scan 16 also has a cancelled superscript on $\mathcal P$. Both changes affect how the proposed application should be read.

**A group of pairs (scan 18).** The three displayed relations define $\Delta(E)$ by ordered pairs. After suggesting a realization by the words $x^{-1}y$, the author gives the free generators $g_i=[i,i+1]$ for a finite interval, writes $[i,j]$ and $[j,i]$ as words in them, and states a countable analogue.

**A quotient for the fundamental group (scan 18).** For a category with a « plus petit objet » $e$ and a « plus grand objet » $a$, the sheet gives a quotient of $\Delta(\operatorname{Hom}(e,a))$. Each diagram $e\rightrightarrows x\rightrightarrows a$ supplies the relation $[\alpha v,\alpha u]=[\beta v,\beta u]$. The sheet does not specify the sense of « plus petit » and « plus grand » further.

**Working diagrams (scan 19).** Several strings of parallel arrows surround a composition $H_{m,n}\times H_{n,p}\to H_{m,p}$ and equations involving $u,v$ and their primed versions. The last diagram puts a question on $H_x\to[x]$. The sheet supplies no definition of $H_{m,n}$ or $R_x$ that would identify the construction uniquely.

## Statements left without proof

| Scan and lines | Author's words or display | What is left open on these sheets |
|---|---|---|
| 2, 15–17; 3, 8–10; 5, 13–14 | $P(b,E)\times P(b',E')=$ … and $(b,E)\times(b',E')=(b\times b',p_1^*(E)\cap p_2^*(E'))$ | The expansions and candidate product are written down. The universal property of the latter and nonemptiness of the intersection are not checked there. |
| 9, 6–15 | « se prolonge par continuité » and « foncteur commutant aux $\varinjlim$ quelconques » | The extension is asserted. Its left exactness remains a separate question. |
| 10, 1–21 | « Ce morphisme est $W_0$-asphérique », « ce qui implique que », « on en conclut que le but … l'est aussi » | There is an outline via inverse images and slice topoi. The passage to arbitrary 0-connected $G$ calls on a preservation property still under discussion. |
| 11, 3–23 | « Lemme (?) », « Vu ce qui précède, cela implique », « l'on sait déjà que », « et inversement, bien sûr » | Terminality of $\pi$ is conjectured. The two corollaries depend on the preceding argument. Local irreducibility is recalled, and the converse about local cofilteredness is asserted. |
| 13, 17–19 | « il est clair que cette image essentielle contient $Z$ » | No argument is written alongside this claim about $(*)$. |
| 15, 9–15 | « Alors elles existent dans $C$, et $C\longrightarrow B$ commute aux $\varprojlim$ de type $I$. » | Lemme 1 (L15). No compatibility between reindexing and these limits is stated. |
| 15, 16–19; 16, 1–6 | « est aussi fibrée sur $B$ » and « elle est stable par tout type de $\varprojlim$ … » | The corollary continues on a new sheet. Its changes to the hypotheses and the notation are visible. |
| 18, 7–16 | « $\Delta(E)$ est un groupe libre à $n-1$ générateurs » and « Résultat analogue si $E$ est dénombrable » | The words for a pair and its inverse are given explicitly. Freeness and the countable analogue are stated. |
| 18, 17–24 | « Alors $\pi_1(X,e)$ est isomorphe … à un quotient du groupe $\Delta(\operatorname{Hom}(e,a))$ » | The relations are specified. No proof of the resulting presentation occurs here. |

## Questions and conjectures

| Scan and lines | Author's formulation | Object of the question |
|---|---|---|
| 2, 8–10 | « $P$ est $\Phi$-exact à g. ? » | Exactness of the diagrammatic functor. |
| 9, 11–15 | « Je suspecte que ce foncteur est exact à gauche » and « mais pas encore » in the margin | Whether $\Phi$ preserves finite limits and where a connectedness hypothesis on $X$ might enter. The margin wording is partly uncertain. |
| 11, 1–9 | « Mais je conjecture que l'on doit avoir ceci » and « Lemme (?) » | Whether the two hypotheses on $Z^\wedge$ and $\pi(\widetilde\Delta_0)$ force $\pi$ to be terminal. |
| 12, 4–7; 13, 13–21; 14, 1–5 | « J'ai en vue un candidat », « Je voudrais des conditions », « Je m'aperçois qu'il est déraisonnable de s'attendre … » | Which assumptions give the proposed closure property? The full-faithfulness requirement is abandoned at the page turn. |
| 14, 13–20 | « Montrons qu'alors … » and « il faudra faire une hypothèse sur $\pi$ » | Which assumptions on $B$ and $\pi$ give limits in the category of subsets? |
| 18, 4–6 | « Je soupçonne que $\Delta(E)$ est isomorphe au sous-groupe du groupe libre $L(E)$ … » | The putative identification sends $[x,y]$ to $x^{-1}y$. |
| 19, 14–15 | « iso ? » | Whether the final vertical comparison is invertible. |

## Slips

| Scan and lines | Written form | Proposed reading of the intention and reason |
|---|---|---|
| 2, 11–13 | $\mathcal P(\pi_0(p(b))$ | $\mathcal P(\pi_0(p(b)))$. Three left parentheses and two right parentheses occur inside the membership label. High. |
| 3, 14–15 | Both bottom objects of the product diagram read $b$. | The right-hand one may be $b'$, as in the neighbouring calculation. The raised mark on its parent object is doubtful. Low. |
| 5, 5–7 | $(b,E)\to(b',E)$ | Probably $(b,E)\to(b',E')$. The same line has $u_*^{E,E'}$ and the next line ends in $E'$. Medium. |
| 7, 19–22 | « Une flèche … est formé » | « formée » would agree with « flèche ». High. The $f$ named here and $\rho$ in its defining equation may also denote the same arrow. Low for that identification. |
| 14, 2–3 | $\widetilde\pi\backslash E$, with $B$ also possible in the ink | Probably $\widetilde\pi\backslash B$ given the next occurrence. Low. |
| 18, 1–2 | $(x,y)\in E$ | Probably $x,y\in E$ or $(x,y)\in E\times E$. The group construction uses two elements of $E$. This could be shorthand. Medium. |

## Pointers

Scan 11, lines 17–20, refers to an earlier result with « l'on sait déjà que » and gives a condition on $X$ whose label looks like $\mathrm{PS}^*1$ or $\mathrm{P5}^*1$. Its source is unnamed. On scans 13–14, « le foncteur $(*)$ » points to the display on scan 13. No person, paper, other cote or identifiable title is cited on these sheets.

## Remarks of the model

**A15 · Model check, high confidence for the finite case (scans 3, 15).** For the surjection $0,1\mapsto p$, $2\mapsto q$, the direct-image/inverse-image adjunction held for all 21 pairs of nonempty subsets. Each nonempty subset of the target had nonempty preimage. For the constant map with value $p$, the preimage of $\{q\}$ was empty. This isolates the role of the epimorphism condition on scan 15.

**L15 · Model counterexample, high confidence for the literal lemma (scan 15, 9–15).** Take the base $0<1$, with fibres the chain $0<1$ and the powerset of $\{p,q\}$ ordered by inclusion. Reindex a subset to $1$ exactly when it is nonempty. In the associated six-object poset the base and fibres have binary products. The pair over $\{p\}$ and $\{q\}$ has two incomparable maximal lower bounds, $(0,1)$ and $(1,\varnothing)$, so it has no product. The computation also checked the cartesian lift over the base arrow.

**R15b · Model refinement, medium confidence as a reading of the intended hypothesis (scan 15).** A sufficient extra hypothesis is that every reindexing functor preserve limits of shape $I$. This makes the limit of a diagram pulled to the fibre over its base limit compatible with further base change. For the same finite example, changing reindexing to $S\mapsto 1$ exactly when $p\in S$ preserves all 16 ordered binary meets in the upper fibre. All 36 ordered pairs of total objects then have products projecting to the base products. The manuscript gives no such hypothesis.

**R16 · Model check, high confidence for the finite poset, low confidence for its application to the corollary (scans 15–16).** In the poset of nonempty subsets of $\{p,q\}$, $\{p\}$ and $\{q\}$ have no common lower bound. In the full powerset their meet is $\varnothing$. The two conventions therefore give different answers even over a one-object base. The crossed condition on scan 15 and the overwritten superscript on scan 16 leave open which version the author wanted.

**G18 · Model check, high confidence for the stated sample (scan 18, 1–6).** Substitution of the reduced word $x^{-1}y$ for $[x,y]$ satisfied all three written relations on three letters across three diagonal cases, nine reversals and 27 compositions. The sample leaves injectivity and the presentation of $\pi_1$ open.

**E18 · Model boundary check, high confidence for the empty set and medium confidence about the author's intended scope (scan 18, 7–10).** When $E=\varnothing$ the presentation has zero generators, while the expression $n-1$ gives $-1$. The displayed finite-rank statement thus needs $n\geq1$ if the empty set is admitted. No lower bound on $n$ is written there.
