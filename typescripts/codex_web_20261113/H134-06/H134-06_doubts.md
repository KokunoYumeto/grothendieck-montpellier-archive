# H134-06 · Notation and doubtful readings

## Notation table

Line references count the main lines of handwriting on each sheet. An interlinear sign is assigned to the line where its leader ends. The table gives the first reading and records other shapes where the strokes permit them.

| Sign or group | Scan and approximate line | Strokes on the page | LaTeX in the transcription |
|---|---|---|---|
| X and Y | 178, 2–3. 179, 17 and 22. 180, 5–19. 181, 14. 182, 16–21. 183, 11 and 23. 184, 13, 15 and 21 | X has crossing obliques. Y has two upper branches and a longer lower stroke. X is interlinear after compacts on 179 and after constants on 183. | `X`, `Y` |
| Diagram fork | 178, 11 | One small, separate point at the fork. The upper stroke has a rightward head and the lower stroke has a downward head. Both branches end at their heads. | `\cdot`, `\arrow[r]`, `\arrow[d]` in `tikzcd` |
| Numeral with a slash | 178, 15 | A small raised 1 and a lower 2 with an oblique slash between them precede simpliciaux. | `1/2` |
| Lowercase f and g | 180, 6, 8, 16 and 19. 185, 1–2 | f has a long stem and cross-stroke. The live g has a head and descender. Only the first g in the operation list on 180 is overwritten. On 185 the short g before the colon is more angular. | `f`, `g`. On 180 the first g is preceded by `\deleted{\unsure{f}}`. |
| Connectors | 180, 6 and 19. 182, 20. 185, 2 | The first connector on 180 has a slight upturn at the right. The second connector on 180 and the product connector on 182 also have small rises. The flat stroke on 185 has a blunt right tip. Compare the full heads on 178. | `-` or `\to` on 180 and 182. `-` on 185. |
| Stratification capital | 179, 22 (twice). 180, 17 (twice). 181, 7 and 9. 184, 12 and 16 (three in all) | Large loop and a returning upright. The outer sweep varies, most markedly after strates de on 184. Plain P and a calligraphic P both fit. | `P` or `\mathcal{P}` at the first occurrence on each sheet. The later occurrences use `P`. |
| Subscripted stratification letters | 180, 17 | Small X or Y below the looped capital. Both short hyphens stand level with the following words. | `P_X`- and `P_Y`- |
| Primes and punctuation between objects | 180, 18–19. 185, 2 | Each of X′ and Y′ has one raised stroke. The added pair on 180 has a comma. The two Z's on 185 have respectively one and two high strokes. The punctuation after the source letter g is a colon. | `X'`, `Y'`, `g:Z'-Z''` |
| Operations on 180 | 180, 16 | Both R's have one upright, as does L. A low star follows the first g, a low dotted ! the second. The next two g's have a high star and a high dotted !. | `\mathrm{R}g_*`, `\mathrm{R}g_!`, `\mathrm{L}g^*`, `g^!`, with the first overwrite separately marked |
| Operations on 185 | 185, 1 | Each R has two independently visible uprights. L has one. The low ! precedes the low star on this sheet. The two high marks then occur in the same order as on 180. | `\mathbb{R}g_!` `\mathbb{R}g_*`, `\mathrm{L}g^*`, `g^!` |
| Baseline n and category prefixes | 179, 22. 181, 11. 183, 22–23. 184, 8 and 14 | A small baseline n is separated from champs or catégories by a short stroke. In both occurrences of (n+1) there are two curved parentheses. On 184 the whole new prefix stands above the old one. | `n`, `(n+1)`, followed by a text hyphen when drawn |
| Barred abbreviation | 181, 22 | Two short horizontals between et and des. The lower one has a curved entry. It can represent a compressed m or the second stroke of an equality sign. | `\overline{m}` or `=` |
| Characteristic and inequality | 182, 1–7 | The p has a descender. The k has a tall stem with an angled branch. The numeral is an oval. The point of the comparison sign is on the right. | `p`, `k`, `0`, `p>0` |
| Cohomology letters and arguments | 182, 16–21. 183, 5 | H has two uprights joined across. M has a central dip, N an oblique join. The H on 183 has a short horizontal argument followed by a descending comma and M. | `H^i(X,M)`, `H^j(X,N)`, `H^i(-,M)` |
| Raised i and j | 182, 20–21. 183, 5 | The first exponent in the product is a short dotted i. The second is j with a lower hook. The result has i, a tiny pointed fleck, then j. On 183 there is only a raised dotted i. | `i`, `j`. Between the last pair, `\cdot` or `+`. |
| Product signs | 182, 20–21 | A small free diagonal cross separates the two H's. A cross surrounded by a fine oval separates M and N in the last argument. The first H also has two short partly covered strokes at its left. | `\times`, `\otimes`. In the overwrite, `+` or `=`. |
| Fundamental group and equality | 183, 3–4 | Twice a bar over two descending legs with a short 1 below its right edge. Two horizontal pen strokes precede the second group. The dash after it lies at text height. | `\pi_1`, `=`, `\pi_1`- |
| Tensor with raised L | 183, 13. 184, 24 | A small L with two uprights stands directly over a circled cross on both pages. | `\overset{\mathbb{L}}{\otimes}` |
| R and Hom | 183, 14. 184, 24 | On each sheet a double-stroked R precedes Hom. Only on 184 does a separate straight line run from beneath H to beneath m. | `\mathbb{R}\mathrm{Hom}` on 183, `\mathbb{R}\underline{\mathrm{Hom}}` on 184 |
| Infinity | 184, 2 | Two joined sideways lobes, followed by a separate hyphen before groupoïde. Two points stand over the i in the word. | `\infty`-groupoïde |
| Quotations | 178, 1, 18 and 23. 179, 9. 180, 1–2 and 11. 181, 4, 7, 10 and 22. 182, 1 and 14. 183, 20. 184, 13. 185, 8–9 | Small paired raised strokes open and close the quoted words. The small interlinear fin on 181 has its own pair at each end. | <code>&#96;&#96;…''</code> |
| Brackets, stops and rules | 178, 8. 179, 5 and 14. 182, 7 and 24. 184, 8. 185, 3 and 9 | On 179 the square corners lie over curved brackets. Countable dot strings retain their lengths, with doubtful counts marked. The horizontal dividers on 182 and 185 have different lengths. | `\deleted{(}[` and `\deleted{)}]`, individual dots or `\ldots`, `\rule` |
| Word underlines | 179, 4. 181, 12 and 16. 183, 21. 185, 8 | The straight strokes beneath et, tous, théorèmes de finitude, non abélien and une have identifiable endpoints. | `\uline` around the underlined text |
| Abbreviated words | 178–185, occurrences listed below | A point is present after some abbreviations and absent after others. In particular loc and car vary. | The letters and the observed point are retained. Expansions are listed below. |

## Doubtful readings

A dash in the fourth column means that a single reading could be proposed. Repeated features marked once on a sheet share a row.

| Scan | Line | Reading | Other readings allowed by the ink | Confidence | Context and pen evidence |
|---|---|---|---|---|---|
| 178 | 5 | autrement | — | medium | The parenthesis introduces the difficulty with dualising complexes. Several central strokes fade. |
| 178 | 8 | . . . . . | ellipsis of unspecified length | medium | The five faint deposits before the curved bracket give the first count. The argument does not determine a count. |
| 178 | 8 | apparaitra | apparaîtra / apparaît | medium | Ink continues past the tall stem. The following probablement works with either tense. The mark over the i could be its dot. |
| 178 | 18 | les (underlying) | des / ces | low | The baseline has two superposed loops before fondements. The form beneath is difficult to isolate. |
| 178 | 18 | des (live) | les | medium | The heavier ascender favours d. Both articles fit the phrase. |
| 178 | 21 | d’un (cancelled) | — | low | A rising stroke, an apostrophe and a low trail are visible. |
| 178 | 21 | espace (cancelled) | — | low | The initial loop and descender survive the diagonal cancellation. Line 23 uses the same noun. |
| 178 | 21 | modéré (cancelled) | — | low | Part of the central d and succeeding small strokes can be followed. The phrase on line 23 favours this word. |
| 178 | 21 | compact (cancelled) | — | low | The ending follows the same broad profile as the clearer addition compact below; the cancellation obscures its middle. |
| 178 | 22 | strates | — | medium | The opening str- is clearer than the crowded last letters. The preceding singular stratification supports the plural noun. |
| 178 | 24 | fon (cancelled) | f | low | A tall initial and several very small strokes survive. There is no decisive syntactic clue to the abandoned word. |
| 179 | 1 | morp (cancelled) | morph | low | A low long strike and a p-like descender survive. Flèches follows immediately. |
| 179 | 4 | les (underlying) | des | low | Ink remaining below the upright suggests l. The small loop on its left also allows d. |
| 179 | 4 | des (live) | les | medium | The overdrawn article stands before plural inclusions. Both articles make sense. |
| 179 | 9 | en cellules (cancelled) | en éléments | low | Only some low strokes and one tall stem survive. The preceding cellulaire gives the former some support. |
| 179 | 9 | dont | — | medium | The d and tall final t are visible above the strike. The following strates supplies a plural subject. |
| 179 | 9 | toutes | — | medium | The opening tall stroke and t are visible. The middle disappears along the ruled-out line. |
| 179 | 22 | P | calligraphic P | medium | The same looped capital follows où on the same line, referring back to stratification. |
| 180 | 6 | straight connector in f:X–Y | right arrow | medium | The right end turns upward. A morphism between the lettered spaces and the draft’s arrow favour an arrow. |
| 180 | 13 | à (cancelled) | comma | low | A small loop is traversed by a second stroke, immediately before encore. The later à des fibrations supports an abandoned à. |
| 180 | 16 | f under the first g | — | low | The first g has a tall internal stem and a cross-stroke. Live g is supported by the same descending form on the other three operations. |
| 180 | 17 | P | calligraphic P | medium | The insertion repeats the stratification letter in two forms with subscripts X and Y. |
| 180 | 19 | straight connector in g:X′–Y′ | right arrow | medium | There is a small rise toward the right, without a full head. Induise and the draft favour an arrow. |
| 180 | 19 | comma after f | point | low | The detached low ink mark between f and induise has a short downward tail. Neither punctuation mark is required by the sentence. |
| 180 | 20 | seuls | de tels | medium | There appears to be one group with a high l and terminal s. Bare homotopy types are the subject here. |
| 181 | 7 | P | calligraphic P | medium | The same letter follows the parenthetic condition on the next lines. Its spelling is uniform with scan 179. |
| 181 | 12 | inductive | — | medium | The last letters of the small interlinear word coalesce. Passage à la limite supports the reading. |
| 181 | 20 | ordinaire | — | medium | The middle syllables are compressed and two dots are visible over the first i region. The contrast with fin supports the reading. |
| 181 | 21 | élément | éléments | medium | The t appears to close the word. Les and the plural constituants favour éléments. |
| 181 | 22 | polyédres | polyèdres | medium | The accent appears to rise rightward. The surrounding words identify the noun, but do not establish the accent direction. |
| 181 | 22 | barred m | equals sign | medium | The lower horizontal has a small rising entry and dip. In et … des variétés, même fits the sentence. |
| 182 | 2 | espaces | — | medium | The initial e and the low continuation are clearer than the plural ending. Tels favours the plural noun. |
| 182 | 13 | a) (cancelled) | α) | low | A closing curve remains to the right of two diagonal cancellation strokes. The preceding paragraph mentions several remarks. |
| 182 | 13 | intrigu- | intrigué | medium | The final horizontal stands apart. Été and the absence of a continued syllable on the next line favour an intended é. |
| 182 | 19 | constant (twice) | constants | medium | The two words have nearly identical t-shaped endings, without the curled s visible at the end of tordus. The preceding plural coefficients supports constants. |
| 182 | 20 | straight connector after H^j(X,N) | right arrow | medium | A short rise ends the stroke. The product formula in the draft has a right arrow. |
| 182 | 20 | + (under the first H) | = | low | Two short strokes extend left of the downstroke of H. The upper one crosses the downstroke. The covered sign is only partly visible. |
| 182 | 21 | dot between i and j | plus | low | The mark is a small wedge with no resolved crossbar. The degree expression in the attached formula favours plus. |
| 182 | 24 | ? (underlying) | — | medium | Two similar curves and two displaced lower strokes follow entièrement. The interrogative phrase favours a retraced question mark. |
| 183 | 3 | donc | — | medium | The internal strokes merge at the baseline after π₁. The relation to the coefficient categories favours donc. |
| 183 | 4 | modules | module | medium | The last stroke runs towards the comma. The preceding plural coefficients favours modules. |
| 183 | 4 | constant | constants | medium | The t at the end has a long rightward exit. There is no distinct final curl like the s in the next word. Coeff. and tordus favour a plural ending. |
| 183 | 6 | ab (cancelled) | ab. | low | The end of the short group and its punctuation lie under a continuous horizontal strike. |
| 183 | 6 | foncteur (cancelled) | — | low | A tall f and later short stems survive. The preceding live occurrence suggests a repeated foncteur. |
| 183 | 7 | struc (cancelled) | — | low | Several strokes are superposed before the clearer ending -ture. The repeats support a false start of the same word. |
| 183 | 10 | form- | formée / formés | low | The final pen mark is separate and flat. The context offers several endings after the change to aux complexes. |
| 183 | 12 | triangulé | triangulée | medium | A single small final accent/stroke is visible after the l. The noun structure favours the feminine. |
| 183 | 13 | de (cancelled before multiplicative) | sou / m | low | Short pointed strokes merge with the m at the start of the live word. No abandoned word is certain. |
| 183 | 22 | sans | sa | medium | Sa- survives with a long reduced final rise. The absence of added structure in the translated passage favours sans. |
| 183 | 22 | structures | structure | medium | The last downward curl could be a plural s. The following adjective has a similar final curl. |
| 183 | 22 | dessus | disons | medium | Two low repeated curves follow the d. Placing supplementary structures on the category favours dessus. |
| 183 | 23 | sur X (added) | — | medium | The word is compressed between two baselines and retouched; the two crossed strokes of X are visible. |
| 184 | 1 | réconstituer | reconstituer | medium | A short raised mark occurs after the initial r. The e is reduced. The analogous form on scan 182 also has a raised mark. |
| 184 | 3 | e (under et) | a | low | A closed loop and a low cross-stroke are caught under the beginning of et. The neighbouring words do not identify the abandoned letter. |
| 184 | 10 | cannelés | canelés | medium | The short waves before the ascender of l merge. The adjective describing types is compatible with cannelés. |
| 184 | 11 | des (cancelled) | — | low | The surviving initial loop and low run belong to the overwrite at certains. Its ending is hidden. |
| 184 | 12, 16 | P | calligraphic P | medium | The same closed oval and internal stem recur three times. The one after strates de has the longest return stroke. Stratification identifies the letter but leaves its style open. |
| 184 | 14 | n- (cancelled) | — | low | The flattened baseline prefix has a short rise. The inserted (n+1)- supports a replacement of another category prefix. |
| 184 | 16 | subordonnés | — | medium | The opening su-b and final accented és are visible. The middle is compressed. The phrase qui sont … à P supports the reading. |
| 184 | 17 | topos | topis / topo | low | The final separate curl looks like s. The vowel before it has only a short stroke and a high dot. Its use with de la cat. dérivée scarcely settles the word. |
| 184 | 20 | ss- (added) | — | medium | Two small upright curls and a dash lie above catégorie with a leader to the start of the word. The syntax favours sous-. |
| 184 | 20 | catégori | catégorie | medium | A dot stands over the last visible short upstroke. The final e has little or no trace. The neighbouring unabbreviated catégorie favours the longer form. |
| 185 | 1 | cas | Cas | medium | The initial c is tall and open. The phrase “plus, les / cas échéant” continues across the sheet break and favours lowercase. |
| 185 | 3 | six dots | five dots | medium | The rightmost five places are widely enough spaced to compare. One of the impressions in the close group on the left is weak. |
| 185 | 13 | Bloch | Blod | medium | After Blo a tiny rounded stroke precedes the ascender, whose return joins the end of the word. The attached draft and the hyphenated name favour Bloch. |

## Slips and unfinished constructions kept as written

The middle column gives the visible reading. The proposed sense in the next column is editorial and does not enter the transcription.

| Scan, line | As written | Apparently intended | Basis |
|---|---|---|---|
| 178, 8–9 | apparaitra / apparaîtra / apparaît | apparaîtra is a possible accented future | The ending runs on after the tall stem. The copy does not separate a circumflex from the i-mark. |
| 179, 14 | se réconstitue | se reconstitue | An initial acute is visible. The same marked vowel occurs in the infinitive on 182. |
| 180, 19–20 | f followed by a small comma or point before induise | f induise | The isolated low mark interrupts the subject and verb. |
| 180, 20 | opérations standart | opérations standard | The terminal stroke crosses like a t. The attached English passage has “standard”. |
| 181, 18–21 | des types d'homotopie fin … les types d'homotopie ordinaire … les élément / éléments constituants | fins, ordinaires and éléments would give plural agreement | The nouns have plural articles. No separate plural s can be securely distinguished at the ends of the adjectives or of élément. |
| 181, 22 | polyédres / polyèdres | polyèdres | The little accent over the e rises to the right on the copy. |
| 182, 13 | intrigu- / intrigué | intrigué | After été the final mark on the line is a dash. The next word is par. |
| 182, 19 and 183, 4 | constant / constants … tordus | constants | A long t-stroke ends constant. The adjacent tordus has a separate final curl. The coefficient phrase carries plural agreement. |
| 182, 23 and 184, 1 | réconstituer, with reconstituer also possible on 184 | reconstituer | An acute stands above the first e on 182. The mark in the same position on 184 is faint. |
| 182, 24 to 183, 8 | (disons, … par certaines propriétés formelles. | A closing parenthesis after formelles may have been intended | The opening stroke is clear. The last mark on the later line is a stop. |
| 183, 10–12 | form- / formée / formés … avec sa structure triangulé / triangulée | formée and triangulée are possible agreements | A flat stroke ends form-. The second e of triangulée is indistinct. The superposed additions partly recast the sentence. |
| 183, 17 | ils permettent | A singular main verb or a different subject may have been intended | The earlier subject is singular. Both the written pronoun and permettent have plural endings. The intended referent remains open. |
| 184, 20–21 | catégori / catégorie dérivée | catégorie | The second occurrence ends at a dotted short stroke. The first occurrence of catégorie on the same line has a visible additional loop. |
| 184, 24 to 185, 1 | plus, les / cas échéant, les 4 opérations | Possibly plus, le cas échéant, les 4 opérations | The first les has a visible final stroke at the foot of 184. The second les is written separately on 185. |

## Abbreviations

| Written form | Scan and approximate line | Likely expansion or use |
|---|---|---|
| cat. | 178, 12. 183, 10. 184, 17 | catégorie or catégories, according to the article |
| ens. | 178, 13 | ensembles |
| 1/2 | 178, 15 | semi-, before simpliciaux |
| i.e. | 178, 19. 179, 9. 182, 15 | id est |
| loc. or loc | 179, 2. 180, 9 and 18. 181, 11. 183, 11 and 23. 184, 15, 17 and 22 | localement |
| sing. | 179, 19. 181, 8 | singulières, after strates non |
| resp. | 181, 5 | respectivement |
| alg. | 181, 15 | algébriquement, before clos |
| m with an overbar (possible) | 181, 22 | même, in et … des variétés. An equals sign is also a possible reading. |
| car. or car | 182, 2–7 | caractéristique |
| coeff. | 183, 3 | coefficients |
| ab or ab. (cancelled) | 183, 6 | Possibly abélien. The cancellation leaves too little to establish the expansion. |
| etc | 183, 7 | et cetera |
| coh. | 183, 11 | cohomologie, in faisceaux de coh. |
| ss- (interlinear) | 184, 20 | sous-, before catégorie |
| ch. | 184, 22 | Probably cohomologie, in à ch. loc. constante. The two written letters and their point remain in the text. |

## Comparison with the attached draft

The corresponding passage is in English. Its line numbers refer to the attached LaTeX file. Each manuscript page was written before the comparison. The table records differences in the covered passages, notation, corrections, punctuation and layout.

| Scan | Line | Manuscript reading | Attached draft, source line and English rendering | Pen evidence | Decision |
|---|---|---|---|---|---|
| 178 | 1–8 | 6 opérations habituelles; réunion de strates; long insertion ending opérations | 448: six operations; a subspace which is a union; the known formulae | No extra noun for subspace, and the repeated verification is written interlinearly. | Keep the French wording and attach the insertion before the stop. |
| 178 | 10–11 | Dot at source; right and down arrows; no distinct terminal dots | 449–452: three bullet objects | There is one dot at the fork and there are two arrowheads. | Retain only the visible source dot. |
| 178 | 13–16 | ens. semi-simpliciaux; 1/2 simpliciaux; catégorie homotopique de fractions | 453: semi-simplicial in both places; fractions; an editorial note | The shorthand changes between the two lines. Magnification resolves the ending in fractions. | Retain the change of notation. The footnote has no manuscript counterpart. |
| 178 | 17–24 | en cogitant; cancelled and reinserted wording around espace modéré compact | 455: the compact tame space in continuous English prose | There are two separate addition lines and a zigzag cancellation. | Retain the successive readings and the crossed stem before d’espaces. |
| 179 | 1–5 | à fibres des variétés à bord; des bords | 455: compact manifolds as fibres; the boundary in the singular | The parenthesis ends following à bord; both occurrences of bords outside it have terminal s. | Keep the manuscript wording. |
| 179 | 5–15 | Square brackets over round brackets; i.e. dont toutes les strates fermées; par recollement | 455: round parentheses; the closed strata; footnote after gluing | Curved and angular strokes survive at both ends. Fermées and par recollement are separate additions. | Record the changes of hand position; no gluing footnote on the sheet. |
| 179 | 16–20 | description-dévissage; X; finis de nature précisée | 455: devissage description; finite diagrams of a precise nature | The noun pair has a hyphen; X and finis are additions. | Preserve their positions. |
| 179 | 21–24 | (ou complexes de faisceaux, ou n-champs...); P-constructibles; où P | 455: parenthetic alternatives, P-constructible; P | Both Ps have the same loop; the dots close the handwritten addition. | Mark the visual ambiguity of P once on the sheet. |
| 180 | 2–4 | 6 opérations; ad-hoc | 455: six operations; ad hoc | The numeral and medial hyphen are visible. | Keep their written forms. |
| 180 | 6, 19 | f:X–Y and g:X′–Y′ with doubtful heads | 455: f and g with explicit right arrows | The upper stroke has a short terminal uptick; the lower one rises before the end. | Mark the connector on its own ink in each formula. |
| 180 | 12–15 | morphismes verticaux; variétés à bord sur d’autres | 455: natural morphisms; compact manifolds with boundaries | The line has the letters of verticaux and moves directly from variétés to à bord. | Keep the two manuscript phrases. |
| 180 | 16 | Rg_*, Rg_!, Lg^*, g^! | 455: Rf_*, Rf_!, Lg^*, g^! | The two subscripts are below descending looped gs. The first carries an overwritten stem. R and L each have a single stem. | Keep live g, including the second occurrence. |
| 180 | 17–18 | P_X- et P_Y-constructibles; X′, Y′ | 455: P_{X^-}, P_{Y^-}; X′, Y′ | Baseline hyphens stand after the subscripted signs. The primed pair is written above the main line. | Keep hyphens and additions in their written positions. |
| 180 | 19 | f followed by a comma or point before induise | 455: “such that f induces g” | A separate dark mark lies below the baseline just to the right of f. | Mark the punctuation doubt. |
| 180 | 20–23 | standart entre seuls types [doubt]; y a du travail de fondements sur la planche! | 455: standard operations between the mere homotopy types; work on the foundations | The final letter of standart crosses like a t; de fondements is above the closing sentence. | Retain the spelling, uncertainty and insertion. |
| 181 | 1–9 | Dans l’un et l’autre cas; se définirait; P-types au pluriel | 455: one or other case; is defined; P-homotopy type | The manuscript has l’un et l’autre, the conditional ending -rait and the interlinear prefix P-. | Retain wording, mood and plural. |
| 181 | 10–14 | non des seuls faisceaux ou n-champs loc constants; tous underlined | 457: not only of sheaves or locally constant n-stacks; all of them emphasised | Both fin and n- are interlinear; a separate fine line underlines tous. | Keep the additions and emphasis. |
| 181 | 15–17 | un corps alg. clos disons; les théorèmes de finitude cohomologique ou homotopique | 457: an algebraically closed field k; the strongest cohomological and homotopical finiteness theorem | There is no letter after clos. The phrase on finitude is plural and the conjunction is ou. | Keep the French text and the limits of its underline. |
| 181 | 16–19 | types d’homotopie fin | 457: “a fine homotopy type” | The first noun is plural. The line containing fin ends the word before the comma, with no separate s. | Keep the wording and the singular adjective. |
| 181 | 18–23 | élément(s) constituants; “polyédres / polyèdres finis”; et [barred m / =] | 457: ordinary homotopy types … finite polyhedra emphasised; and even | Only the quoted term is between double quotes. No long underline of the passage. There are two strokes after et. | Retain local doubts and the two-stroke sign. |
| 182 | 1–7 | “complétés profinis” … premiers à p (la car. de k) de tels espaces | 457: completions prime to the characteristic p of k are those of such polyhedra | The parenthesis closes after k; the next noun begins esp-. No verb equivalent to “are those of” appears. | Keep the manuscript construction. |
| 182 | 7–12 | Horizontal rule followed directly by De ces cogitations | 459–462: star break and editorial section heading | The rule and first words of the new paragraph are visible with no intervening heading. | Represent the rule and paragraph. |
| 182 | 13–16 | Cancelled label, intrigu-, la question du type | 464: begins For a long time; questions of the type | There is an abandoned sign before Depuis and a singular la question. | Keep both, with doubt on the final letter of intrigu-. |
| 182 | 19–20 | constant twice, then a short sign under the first H | 464: “constant or twisted constant”, followed by an uncorrected product formula | The endings before ou and before tordus match. The left upright of the first H covers two tiny strokes. | Keep the doubtful endings and the underlying sign. |
| 182 | 20–21 | H^i(X,M) × H^j(X,N) –/→ H^{i ·/+ j}(X,M⊗N) | 464: right arrow and the explicit exponent i+j | The connector has one terminal barb. A tiny fleck separates i and j; both exponent letters can be identified. | Retain the two sign alternatives separately. |
| 182 | 23–24 | réconstituer … entièrement, with a retraced question mark | 464: reconstruct entirely, one question mark | The first vowel bears an acute and the question mark has doubled lines. | Retain the spelling and overwrite. |
| 183 | 1–8 | des catégories; coeff.; constants tordus = π₁-modules; Hⁱ(−,M); formelles. | 464: the category in the singular; explicit bracket around the equality; closes with “?)” | The equality stands on the line with no opening parenthesis; only a full stop follows formelles. | Keep the plural, abbreviation and punctuation. |
| 183 | 9–12 | Two separate additions around complexes abéliens and faisceaux de coh. loc constante sur X | 464: complexes on X, formed from complexes whose cohomology sheaves are locally constant on X | The only X in these manuscript lines is at the end. The additions have separate leaders. | Keep the handwritten construction, including aux. |
| 183 | 13–18 | L above ⊗; double-stroked R in Hom; Je n’ai guère d’idée … en effet | 464: macros for derived tensor and Hom; long footnote on rational homotopy | Hom has no underline here. A short added en effet is the entire interlinear text at récupérer. | The editorial footnote has no place on the sheet. |
| 183 | 20–23 | (n+1)-catégorie (sans / sa structures … dessus / disons!) des n-champs loc. constants sur X pour tout n | 464: without supplementary structure; locally constant n-stacks of constructible sheaves on X | The pen has n-champs, loc. constants and a raised sur X. There are no additional words for constructible sheaves. | Keep the manuscript parenthesis with its uncertainties and its short final line. |
| 184 | 1–8 | ∞-groupoïde, n-catégories . . . .) and a crossed Mais | 464: fundamental ∞-groupoid, n-categories followed by an ellipsis, closing bracket and stop. | The ∞ is on the line. All four dots stand inside the bracket, and Mais carries several crossing strokes. | Keep the stops and cancelled word in their manuscript positions. |
| 184 | 9–16 | types … cannelés / canelés and aux (n+1)-catégories | 466: “the more elaborate homotopy type” and “the (n+1)-category” | The lettering after plus ends in -lés. Plural s is visible after catégories. The prefix replaces an earlier baseline prefix. | Use the manuscript plural and mark the reduced adjective. |
| 184 | 17–22 | le topos / topis / topo de la cat. dérivée loc. constante; ss-catégorie … ch. loc. constante | 466: “the above description of homotopy types” and “locally constant cohomology” | A short, separately ended top- word precedes de la cat. Above the next catégorie is a short addition. The abbreviation before loc. has only c, h and a point. | Keep the short forms and the doubtful ending. |
| 184 | 24 | L over ⊗, double R and underlined Hom plus, les | 466: tensor and Hom macros followed by a comma before “plus” | The underline is directly beneath Hom. The visible comma near plus is on its right, before les. | Preserve the underline and comma placement. |
| 185 | 1–2 | double R in ℝg_! and ℝg_*, no comma between the first two, g:Z′−Z″ | 466: plain roman R and comma between the first two operations, “g: Z′ → Z″” | The two R's each have a second upright. The connector has a blunt end. A comma is visible after the second operation. | Keep the two double strokes, the spacing and the horizontal sign. |
| 185 | 2–9 | des inclusions, “fibre” and “cofibre”, four dots and parenthesis, horizontal divider | 466: “for the induced g”, “fibres” and “cofibres”, then an editorial footnote | The word following des begins in- and has a tall l. The two quoted words each end at e. The long divider is the only material between the paragraphs. | Keep the two singulars, the punctuation and the rule. |
| 185 | 10–16 | cette lettre-fleuve; cette mirifique formule de Bloch / Blod-Quillen | 468: quotes around “lettre-fleuve”; “marvellous formula of Bloch-Quillen” | The manuscript has no quotes around lettre-fleuve. The two parts of the proper name are split at a real hyphen. | Keep the handwritten wording and mark the compressed ch. |
| 185 | 17–19 | Bien cordialement à toi / Alexandre / Grothendieck | 472–475: “Very cordially yours,” and “Alexandre Grothendieck” on one line | There are three distinct baselines. The given name and surname begin at different indentations. | Keep the three lines and their relative placement. |

## Legibility

The wide spacing makes the order of the letter and most interlinear leaders easy to follow. The least secure passage is the cancelled parenthesis over line 21 of scan 178. Each of its four words is individually marked. Other weak places are the sign between the two exponents on scan 182, the crowded correction at the foot of scan 183 and the short word after “Si plus haut le” on scan 184. The line-by-line doubt table records them even where the attached translation would suggest a fluent reading. The final two signature lines are comparatively clear.
