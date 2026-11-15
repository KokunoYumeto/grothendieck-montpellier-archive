# J156-9-06 — readings and doubts

## Notation table

These are readings of the supplied images, not statements of mathematical convention. For a recurring ambiguous form, the first candidate is used after its first marked occurrence on each page. A clearly present or absent accent is preserved independently at each occurrence.

| Image location | Form | LaTeX reading and alternatives | Visible evidence |
|---|---|---|---|
| 42, lines 1, 6–8 | Inf / Sup | ` \mathrm{Inf}, \mathrm{Sup} ` | Capital I has a long upper/lower horizontal stroke; S is looped. The parenthetic anti-Inf/Sup is unresolved. |
| 42, lines 2–4 | empty set; complement | ` \varnothing; C ` | Empty set is a long slash through a small oval, not a Greek phi in this context; C is a tall open loop. |
| 42, lines 7, 11 | support lattice index | ` \Sigma_\mu; candidates M, U ` | Second reading: the left descending lead favours lowercase mu; M and U remain possible. First occurrence marked; both occurrences harmonized. |
| 42, lines 10–17 | separation relation | ` \mathrel{\|\circ\|} ` | Two vertical bars with a small open circle between them; do not replace by perpendicular. |
| 42, lines 12–17 | set letters and primes | ` S,S',x,x' ` | Plain capitals/lowercase with short separate prime strokes. |
| 42, bottom paragraph | magasin letter | ` \mathcal A; candidate A ` | Open curved A with a sweeping left lead; initially marked where its alphabet is less clear. |
| 42, bottom paragraph | figure family | ` \mathscr F; candidates \mathcal F, \mathbb F ` | Ornate reinforced F with parallel stem strokes; script favoured by its lower hook, double-struck not excluded. Following low mark on 42 is a comma, not an index. Rechecked against 44. |
| 42 bottom; 46 margin; 47 tuples; 49 | triangle relation | ` \trianglelefteq ` | Left-pointing triangle with a lower parallel stroke; confirmed by comparing directly with later pages. |
| 42, bottom paragraph | quotation marks | ``` ``figures'' ``` | Paired short upper strokes; reproduced as double backticks and apostrophes. |
| 43, opening and middle displays | constructible supports | ` \Sigma\mathrm{cons}_{\mathcal A}; candidate \Sigma_{\mathrm{cons}_{\mathcal A}} ` | cons is smaller than Sigma but sits close to its baseline; A is distinctly lower. Layout is marked at first use. |
| 43, end of first paragraph | decorated containment | ` \overset{\circ}{\ll}; candidate \overset{\circ}{\Subset} ` | Two nested left-opening curved strokes with a small loop above; second reading harmonized with 44–49, without reducing to a single subset. |
| 43, middle display and following line | open support | ` X^{\circ}, \mathrm{supp}^{\circ}X, \mathrm{supp}^{\circ}(X) ` | Open high circle, not a star or prime. The annotation below X has two vertical strokes. |
| 43, final two lines | Art / Aut | ` Art; candidate Aut ` | The abbreviated/technical word has a reduced middle letter. First occurrence is marked; the second uses the first candidate under the recurring-glyph rule. |
| 44, first two lines and line 5 | double left relation | ` \overset{\circ}{\ll}; candidate \overset{\circ}{\Subset}; \ll ` | The inserted parenthesis has a plain double left angle. Main sign has a small circle above. Compared with 43 during the audit. |
| 44, first display and lower paragraph | deployment | ` \mathrm{Dep}(X); candidate \mathrm{D\acute{e}p}(X) ` | Capital D followed by small e and descending p, not D subscript v; an accent is not secure. |
| 44, first display and lower paragraph | tilded X | ` \widetilde X ` | Broad tilde separate above X; not a hat or circle. |
| 44, lower paragraph | map without visible head | ` \widetilde X\mathbin{-}\mathrm{Dep}(X) ` | A horizontal stroke is visible, no arrowhead; do not supply one. |
| 45, display phi and corrected equality | phi | ` \varphi; candidate \phi ` | Loop is left of the long descending stem. First occurrence marked. |
| 45, middle paragraph and display psi | psi | ` \psi; candidate \tau ` | A curved crossbar with two upturns and long stem. The prose form is especially flattened. |
| 45, deployment map and following formulas | accented deployment | ` \mathrm{D\acute{e}p} ` | A separate short acute stroke above e is visible here; not silently back-projected to 44. |
| 45, inequality and parenthesis | order convention | ` \leq; \subset ` | Two lower strokes in the order sign; text explicitly calls it the subset relation in Sigma. |
| 46, condition label and definition | refinement label | ` Raff ` | R followed by a and two tall descending f stems; label is underlined. |
| 46, slanted margin first line | triangular relation | ` \trianglelefteq ` | After rotating the note, a left-pointing triangle with a lower parallel stroke is visible. Rechecked against the triangle on 42. |
| 46, prose after map psi | iff abbreviation | ` sss; candidate ssi ` | Three small strokes, last letter/dot not securely distinguishable. |
| 47, triangle in prose and both structure tuples | triangular relation | ` \trianglelefteq ` | Left-pointing triangular outline with one lower line, repeated clearly. |
| 47, bottom target and insertion | ordered elementary figures | ` \mathrm{Fig\acute{e}l}^{\mathrm{ord}}(\Sigma); inline candidate \mathrm{Figel}\,\mathrm{ord}(\Sigma) ` | Acute visible in the large target; ord added above. Smaller insertion has a flatter spelling/placement. |
| 47, margin | axiom label | ` At 4 ` | Two joined letters before 4; expansion not supplied in the transcription. |
| 48, opening and conditions a/b | figure support letter | ` \Phi; candidate \varphi ` | Large double oval with long central/downward stroke and baseline foot. Capital Phi favoured; first occurrence marked. |
| 49, first display | left arrow beside triangle | ` \trianglelefteq\!\leftarrow ` | Both the underlined triangle and a short arrow pointing left are clearly present; no mathematical simplification made. |
| 49, At 2 b diagram | vertical triangle relation | ` \trianglelefteq rotated 90 degrees ` | The triangle points down, with its parallel lower stroke rotated to the right; reproduced with a rotated tikz-cd phantom label. |
| 49, At 3 two-line statement | ditto line | ` \rule{7cm}{0.3pt} ` | A horizontal repeat stroke after -T replaces repeated words in the manuscript; the stroke is reproduced, not expanded. |
| 45, final display | unaccented deployment | ` \mathrm{Dep}(Y) ` | Independent enlargement shows no separate acute stroke here; central occurrences remain accented Dép. |
| 48, final display | mixed accent in deployment | ` \mathrm{D\acute{e}p}(X)\ll\mathrm{Dep}(Y) ` | Small separate stroke is present over the first e; absent over the second. Neither is normalized to the other. |

## Doubts

There is one row below for every final `\unsure` mark. Locations refer approximately to manuscript lines or blocks; the final number gives the line in that page’s `.tex` file. Alternatives are transcribed literally. “None used” means no surrounding-text preference was used to choose the first candidate; the accompanying explanation records the visual evidence. The one possible insertion-leader reading is explained in words because it would remove a punctuation mark rather than replace it with another glyph.

| ID / scan | Approximate manuscript location; TeX line | First reading | Every alternative | Confidence | Context and evidence |
|---|---|---|---|---|---|
| U42-01 / 42 | 2; 6 | ` \mathcal A ` | ` A ` | medium | None used. A sweeping initial stroke favours the calligraphic form. |
| U42-02 / 42 | 4; 6 | ` \mathrm{cosupp}^{\circ} ` | None proposed | medium | None used. The middle is compressed; the tall p-like downstrokes support this abbreviation. |
| U42-03 / 42 | 7,11; 6 | ` \mu ` | ` M `; ` U ` | low | None used. The left lead descends below the rounded glyph; context is not used to choose. |
| U42-04 / 42 | 7; 6 | ` \mathrm{Inf} ` | ` \mathrm{Sup} ` | low | None used. The top/bottom stroke favours Inf, while the rounded lower part permits Sup. |
| U42-05 / 42 | 10, deleted; 6 | ` se donne par ` | None proposed | low | None used. Fragments survive the strike. |
| U42-06 / 42 | 12, annotation; 8 | ` \mathrm{Not} ` | ` \mathrm{def} ` | low | None used. Rotated crop has an angular initial N and a possible final t; still unresolved. |
| U42-07 / 42 | margin heading; 22 | ` quasi-radicié ` | ` quasi-radicoïde ` | low | None used. The ending is highly compressed; no contextual choice. |
| U42-08 / 42 | margin before 1°; 26 | ` Alors que ` | None proposed | low | None used. The second word is compressed. |
| U42-09 / 42 | margin item 3, deleted; 28 | ` \forall x\in\Sigma ` | None proposed | low | None used. Overlapping strokes obscure the formula. |
| U42-10 / 42 | margin end; 29 | ` Description ` | ` Dans l'option ` | low | None used. The descender and following tion-like strokes also allow Description. |
| U42-11 / 42 | margin reference; 30 | ` \mathrm{Figel}\,\mathrm{ord} ` | ` \mathrm{Figbord} ` | low | None used. The middle loop resembles the Figél notation on 47, but this crop remains doubtful. |
| U42-12 / 42 | bottom line 1; 32 | ` abstrait ` | ` étalon ` | medium | None used. Fresh crop shows an ab-like pair and a final tall t; favors abstrait. |
| U42-13 / 42 | bottom line 2; 32 | ` \mathscr F ` | ` \mathcal F `; ` \mathbb F ` | medium | None used. An ornate lower hook favours script; close parallel stem strokes also allow a double-struck interpretation. No contextual alphabet was imposed. |
| U43-01 / 43 | opening and middle display; 6 | ` \Sigma\mathrm{cons}_{\mathcal A} ` | ` \Sigma_{\mathrm{cons}_{\mathcal A}} ` | medium | None used. The smaller word cons appears nearly on the Sigma baseline; exact nesting remains uncertain. |
| U43-02 / 43 | first prose line, deleted; 8 | ` en ` | None proposed | low | None used. A short scribbled form before en général; only the outline survives. |
| U43-03 / 43 | end first paragraph; 8 | ` \overset{\circ}{\ll} ` | ` \overset{\circ}{\Subset} ` | medium | None used. Two visible angle-like strokes; agrees with the recurring form on later crops. |
| U43-04 / 43 | deleted middle line; 10 | ` resté ` | None proposed | low | None used. The end is crossed through; final accent may be visible. |
| U43-05 / 43 | final paragraph; 14 | ` la ` | ` l' ` | low | None used. The loop after de could be an article or a contracted article; grammar is not used to resolve it. |
| U43-06 / 43 | last two lines; 14 | ` Art ` | ` Aut ` | low | None used. The page gives no expansion; the first candidate follows the visible narrow middle stroke. |
| U44-01 / 44 | 1–2; 5 | ` \overset{\circ}{\ll} ` | ` \overset{\circ}{\Subset} ` | medium | The inserted (ou ll) supports the double-angle reading; the principal strokes remain rounded.  |
| U44-02 / 44 | 8, deleted; 5 | ` X\leftarrow ` | None proposed | low | None used. Crossing and arrowlike horizontal stroke above considérons. |
| U44-03 / 44 | first display; 7 | ` \mathrm{Dep} ` | ` \mathrm{D\acute{e}p} ` | medium | None used. No accent can be separated confidently from the upper stroke. |
| U44-04 / 44 | first display, deleted; 7 | ` X ` | None proposed | low | None used. Small crossed glyph immediately inside the set brace. |
| U44-05 / 44 | first display; 7 | ` \Sigma\mathrm{cons} ` | ` \Sigma_{\mathrm{cons}} ` | medium | None used. Small cons remains near the capital baseline, as on 43. |
| U44-06 / 44 | below display; 9 | ` déployement ` | None proposed | medium | None used. The visible spelling appears to have y before e; retained rather than normalized. |
| U44-07 / 44 | middle paragraph; 11 | ` H\subset ` | ` \forall ` | low | None used. Initial tall glyph and following small c-shaped mark are unresolved. |
| U44-08 / 44 | middle paragraph, family capital; 11 | ` \mathscr F ` | ` \mathcal F `; ` \mathbb F ` | medium | None used. The ornamental F has the same hooked and reinforced stem features as on 42; first occurrence on this page marked. |
| U44-09 / 44 | lower paragraph; 13 | ` mutuellement ` | None proposed | medium | None used. Visible m-u-t pattern; mathematically surprising alongside a largest element, not corrected. |
| U44-10 / 44 | last paragraph; 13 | ` cela aussi ` | None proposed | medium | None used. The letters after cela are compressed; no mathematical expansion supplied. |
| U45-01 / 45 | map phi; 11 | ` \varphi ` | ` \phi ` | medium | None used. The loop is off-centre; no mathematical convention used to choose. |
| U45-02 / 45 | corrected display; 15 | ` \overset{\circ}{\ll} ` | ` \overset{\circ}{\Subset} ` | medium | None used. Rounded left-angle strokes; same ambiguity as 44. |
| U45-03 / 45 | middle paragraph; 17 | ` déployements ` | None proposed | medium | None used. Apparent y spelling again; no modernization. |
| U45-04 / 45 | middle paragraph; 17 | ` \psi ` | ` \tau ` | medium | None used. The display has two curved branches; prose resembles a tau. |
| U45-05 / 45 | deleted phrase above last display; 27 | ` peut avoir ` | ` pour avoir ` | low | None used. The strike passes through all letter bodies. |
| U46-01 / 46 | line 3 insertion; 7 | ` déployements ` | None proposed | medium | None used. Compressed word but y-like descending stroke is visible. |
| U46-02 / 46 | first display, deleted; 9 | ` X ` | None proposed | low | None used. A heavily crossed capital; X is the best stroke-based reading. |
| U46-03 / 46 | Raff and map; 14 | ` \mathrm{Dep} ` | ` \mathrm{D\acute{e}p} ` | medium | None used. Accent not distinct in upper formulas, visible in bottom definition. |
| U46-04 / 46 | annotation above Raff; 14 | ` not ` | ` tel ` | low | A notation abbreviation fits the following equality; the compressed ink does not decide not versus tel. Initial short stem and rounded middle favour not; context permits a notation abbreviation, but tel remains possible from the ink. |
| U46-05 / 46 | annotation and map; 14 | ` \psi ` | ` \tau ` | medium | None used. Same recurring curved crossbar glyph as on 45. |
| U46-06 / 46 | after est croissante; 25 | ` \overset{\circ}{\ll} ` | ` \overset{\circ}{\Subset} ` | medium | None used. Same double-angle ambiguity. |
| U46-07 / 46 | same line; 25 | ` sss ` | ` ssi ` | low | None used. Last short stroke and any dot are unresolved. |
| U46-08 / 46 | above last display, deleted; 27 | ` X^{\circ}\ll ` | None proposed | low | None used. The visible diagonal X strokes and double-angle survive. |
| U46-09 / 46 | NB parenthesis; 29 | ` il est ` | None proposed | medium | None used. Small compressed introductory strokes. |
| U46-10 / 46 | slanted margin end; 33 | ` ordonnée ` | None proposed | low | None used. Word to the right of partie is reduced and partly crowded by the body text. |
| U46-11 / 46 | definition, deleted; 35 | ` magasin ` | None proposed | low | None used. Underlying word crossed out below atelier; final loop resembles -sin. |
| U47-01 / 47 | line 2, deleted; 7 | ` signi ` | None proposed | medium | None used. Only the initial signi-like sequence was written/cancelled. |
| U47-02 / 47 | line 4; 7 | ` primitive ` | None proposed | medium | None used. Middle is highly compressed; first and last strokes fit the reading. |
| U47-03 / 47 | line 4; 7 | ` \overset{\circ}{\ll} ` | ` \overset{\circ}{\Subset} ` | medium | None used. Recurring relation ambiguity. |
| U47-04 / 47 | end of first paragraph; 7 | ` .\,-- ` | ` \dots ` | low | None used. Two distinct dark marks are visible before the closing parenthesis; the horizontal mark may join two ellipsis dots. A separate full stop follows the parenthesis. |
| U47-05 / 47 | before first tuple, deleted; 11 | ` \mathcal A ` | None proposed | low | None used. Overwritten script capital. |
| U47-06 / 47 | below first tuple; 13 | ` sous ` | None proposed | medium | None used. Four compressed strokes before quelles. |
| U47-07 / 47 | margin; 21 | ` At 4 ` | None proposed | medium | None used. First two letters joined, terminal 4 clear. |
| U47-08 / 47 | margin; 21 | ` rappeler ` | None proposed | low | None used. Letters slope into the main text; proposed reading remains doubtful. |
| U47-09 / 47 | margin; 21 | ` condition ` | None proposed | low | None used. Letters slope into the main text; proposed reading remains doubtful. |
| U47-10 / 47 | bottom map; 23 | ` \mathrm{Dep} ` | ` \mathrm{D\acute{e}p} ` | medium | None used. No separate acute evident in the smaller word. |
| U47-11 / 47 | bottom insertion; 25 | ` \mathrm{Figel}\,\mathrm{ord} ` | ` \mathrm{Fig\acute{e}l}^{\mathrm{ord}} ` | medium | None used. Small compressed lettering does not decide accent/placement. |
| U47-12 / 47 | bottom insertion before de Sigma; 25 | ` ens. ord ` | ` ens. sép ` | low | None used. Last loop and long descender can support either abbreviated ending. |
| U48-01 / 48 | top right, deleted; 5 | ` d'ordre ` | None proposed | low | None used. Middle is crossed out; initial d and final re-like strokes remain. |
| U48-02 / 48 | top insertion placement; 5 | ` ( ` | Curve belongs to the insertion leader, rather than a literal parenthesis | low | None used. The curve continues into the leader; literal parenthesis is retained with a doubt mark. No closing parenthesis is supplied. |
| U48-03 / 48 | top insertion, deleted; 5 | ` ordonné ` | None proposed | low | None used. Heavy double scribble; shape and ending support the proposal only weakly. |
| U48-04 / 48 | before S in Phi, deleted; 5 | ` \forall x\in A\in ` | None proposed | low | None used. Multiple overlaid symbols; all retained as a doubtful formula. |
| U48-05 / 48 | top formulas; 5 | ` \Phi ` | ` \varphi ` | medium | None used. Capital-sized double oval and lower stem favour Phi. |
| U48-06 / 48 | middle display; 16 | ` \overset{\circ}{\ll} ` | ` \overset{\circ}{\Subset} ` | medium | None used. Recurring double-angle form. |
| U48-07 / 48 | condition ii and lower formulas; 24 | ` \mathrm{Dep} ` | ` \mathrm{D\acute{e}p} ` | medium | None used. Upper display shows an accent, smaller later instances do not clearly do so. |
| U48-08 / 48 | lower prose; 26 | ` déduite ` | ` décrite ` | low | None used. Compressed middle; no silent correction to the most usual expression. |
| U48-09 / 48 | lower target; 26 | ` \mathrm{Figel}\,\mathrm{ord} ` | ` \mathrm{Fig\acute{e}l}\,\mathrm{ord} `; ` \mathrm{Fig\acute{e}l}^{\mathrm{ord}} ` | medium | None used. The initial F is heavily retraced; no independent acute stroke is secure. The abbreviation is on one line in this instance. |
| U48-10 / 48 | bottom deleted fragment; 28 | ` De ` | None proposed | low | None used. Capital D and small following stroke survive. |
| U49-01 / 49 | first display; 6 | ` \mathrm{Dep} ` | ` \mathrm{D\acute{e}p} ` | medium | None used. No distinct acute on the first abbreviation; next display has one. |
| U49-02 / 49 | first display; 6 | ` \overset{\circ}{\ll} ` | ` \overset{\circ}{\Subset} ` | medium | None used. Same recurring relation; plain double-angle also occurs on adjacent pages. |
| U49-03 / 49 | insertion under Phi; 12 | ` \psi ` | ` \tau ` | medium | None used. Crossbar/stem glyph as on 45–46. |
| U49-04 / 49 | first display; 14 | ` \Phi ` | ` \varphi ` | medium | None used. Capital-shaped oval with baseline foot. |
| U49-05 / 49 | display left, deleted; 20 | ` \mathrm{De} ` | None proposed | low | None used. Short fragment rather than complete word. |
| U49-06 / 49 | after X circle ll Y prime; 22 | ` oK ` | ` OK `; ` ok ` | medium | None used. The first oval is lower-case sized while the K is tall. Abbreviation capitalization is not silently normalized. |
| U49-07 / 49 | At 2 a); 24 | ` a) ` | ` (ii) ` | low | The preceding numbered condition on scan 48 may favour (ii); the visible small loop favours a). Visible loop and closing parenthesis; context may favour (ii), the preceding numbered condition. |
| U49-08 / 49 | At 3 deleted phrase; 33 | ` transpose par des ` | None proposed | low | None used. All words intersected by a long cancellation stroke. |

## Slips and anomalies retained

These are possible slips or literal anomalies, not corrections to the author. Doubtful forms remain marked in the transcription.

| Scan | Approximate location | As written / retained | Apparently intended | Reason |
|---|---|---|---|---|
| 43 | last paragraph | la Art ouvert associée | uncertain | The apparent agreement and technical term are retained without correction; the noun itself is doubtful. |
| 44 | below first display | déployement | déploiement | Apparent y spelling retained with a doubt mark. |
| 44 | lower paragraph | largest element X circle and mutually disjoint elements | no correction proposed | The conjunction appears surprising; transcription follows the page. |
| 45 | middle paragraph | déployements | déploiements | Visible y-like descending stroke preserved. |
| 48 | top insertion | Possible opening parenthesis before d’ensemble; no closing parenthesis | Possibly only the insertion leader; no closing mark supplied | A closing parenthesis is not visible; retained literally. |
| 49 | At 4, deleted | Evident. | Évident. | No initial acute is visible; not added. |

## Abbreviations

Proposed expansions appear only in this list, never in the transcription.

| Scan(s) | Form | Proposed expansion |
|---|---|---|
| 42 | Inf; Sup | Infimum / supremum (possibly plural in the prose). |
| 42 | cosupp° | Tentatively cosupport with a raised open circle; the abbreviation itself remains doubtful. |
| 42 | p.ex | par exemple |
| 42 | grd | grand |
| 42, 45 | Not; def | Notation; définition, respectively. The tiny label on 42 is uncertain between the two. |
| 43 | supp° | Support with a raised open circle. |
| 43–44 | cons | constructible(s) |
| 43 | Art / Aut | Unresolved technical abbreviation; no secure expansion can be read from these pages. |
| 44–49 | Dep / Dép | déployement(s), using the spelling seen on the pages; modern déploiement is not substituted in the text. |
| 44, 47 | ens; ens. | ensemble(s), or ensembliste(s) in the short insertion. |
| 44 | tjrs | toujours |
| 44–46, 48 | i.e. | id est |
| 46 | néc. | nécessairement |
| 46 | not / tel | Possibly noté / notation; tel is the competing word reading, not an abbreviation. |
| 46 | sss / ssi | si et seulement si; the same page subsequently spells this phrase out. |
| 46 | NB | nota bene |
| 46 | Raff | raffinement (the condition’s label) |
| 42, 47–48 | Figel / Figél; ord | figures élémentaires; ordonné(es). Spelling and placement vary or are uncertain. |
| 47 | sép (alternative) | séparé(es), if this alternative is the intended short word. |
| 47–49 | At | A label for atelier axioms; the prose calls At 3 an axiome. |
| 49 | oK / OK / ok | okay / agreement; capitalization is uncertain. |

## Legibility and limits

The main lines and most formulas are legible, but the rapid hand often reduces word middles to strokes. The least reliable material is the slanted heading and final reference on scan 42, the Art/Aut phrase on scan 43, the H/quantifier-like sequence on scan 44, the small annotation and crowded margin of scan 46, the shortened insertions on scan 47, and the heavily cancelled upper text on scan 48. The tiny reference after At 2 a) on scan 49 is also unresolved. No physically unreadable word was replaced by an illegible macro: tentative readings were possible, and are explicitly marked. A zero illegible count does not mean these doubtful readings are secure. Both readings were performed from the supplied images without OCR, a PDF text layer, external text, or parallel readers. The balance check is a syntax check only; the LaTeX has not been compiled.

Final uncertainty marks: 75.
