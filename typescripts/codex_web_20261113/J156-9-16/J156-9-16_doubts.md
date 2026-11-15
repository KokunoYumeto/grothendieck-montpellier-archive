# Notation table

These are readings of the supplied images, not assertions about the author's intended notation. Locations identify manuscript lines by their words or formulas. Repeated ambiguous glyphs are marked at their first occurrence on each page; clearer or differently drawn occurrences are judged separately. A source line ending is not a TeX line ending.

| Glyph or convention | LaTeX reading / alternatives | Visual evidence and cross-page check |
|---|---|---|
| Ambient ordered set | `\Sigma`, `\Sigma'` | 119 (i), angular capital and separate high prime; rechecked in 120–125. |
| Complement-like operator | `\ell` / `\complement` | 119 (i), 121 stable par Sup, 125 before supp: tall upper loop with lower return. First candidate retained consistently. |
| Enlarged B | `\widehat B` / `\widetilde B` | 119 central display: peaked, slightly wavy upper stroke. Later B occurrences on that page use the first candidate. |
| Power-set capital | `\mathcal P` / `\mathscr P` | 119 consequence: broad loop and long stem, script style not uniquely identifiable. |
| Compared family capitals | `\mathbb G` / `G`; `\mathbb F` / `F` | 119 axiom line: doubled stems checked individually; ordinary single-stroke F and G in the membership clause and subsequent chains. Weight alone is not used to force bold. |
| Class of families | `\mathcal F` / `\mathscr F` | 119 membership and 120 ordered-pair line, hooked script capital F. |
| Subscript of ambient Sigma | `\mathcal A` / `A` | 120 opening, 122 conclusion, 125 final paragraph: curved entry into A, possibly plain cursive. All three first occurrences marked. |
| X and its upper ring | `X^0` / `\mathbb X^0` / `X^\circ` / `\mathbb X^\circ` | 119 B-set: X has retraced strokes and upper open ring. The following membership X is independently ambiguous. The A-set X and 125 X,Y are ordinary single-stroke forms. |
| Sup, Inf; sup, supp | `\operatorname{Sup}`, `\operatorname{Inf}`; `\operatorname{sup}`, `\operatorname{supp}` | 119 and 121 capitals in the order operations; 124 compressed lower-case operation; 125 two visibly descending p stems in supp. Capitalization is not normalized. |
| Axiom label | `Atm. g)` / `Atm. 9)` | 119 and 122 headings, 124 reference: shortened Atm.-like group and a looped descending last sign; never expanded in the transcription. |
| Axiom suffix | 119 `-\gamma\gamma^2` / `-\gamma^2`; 122 `-\gamma^3`; 124 `-\gamma\gamma^3` / `-\gamma^3` | 119 two separated gamma-like strokes; 122 one continuous gamma-like form; 124 two heavy descenders, possibly retraced. Distinct ink is retained rather than forcing a common number of signs. 2 and 3 are upper-right exponents. |
| Figure notation | `\operatorname{Fig\,spat}` / `\operatorname{Fig\,opt}`, with `disc`, `comm`, and inserted `él` as written | 120 middle, 122 lower. The sp-like cluster is compressed. 122's added Fig él spat comm and 123's Fig spat comm have clearer s-p-a-t strokes; these clearer occurrences use spat directly. No hyphens are invented. |
| Spatios term | `spatios` / `specton` | 120 definition and 122 insertion remain reduced; 121 sous-spatios and 124 quoted spatios have clearer endings. The latter are not normalized to another word. |
| Commensurability | `commensurable`, `commensurables`, `comm.`, `commens` | 120 definition through 125: full terms and contractions are preserved separately. 123 final commens remains doubtful. |
| Order and joins/meets | `\ll`, `\leq`, `\subset`, `\vee`, `\wedge`, `\bigcup` | 119–122 chains and set clauses; 123 example and final distributivity clause. Directions checked from chevrons/strokes, not inferred from the argument. |
| Primes, zero, indices | `'`, `''`, `0`, `0_\Sigma`, `i`, `j` | 119–121: single/double upper strokes. 120 F index i/j and 121 final union index j/i remain marked. First union on 121 visibly starts at 1; the later union starts at 0. |
| Triangle relation | `\trianglelefteq` | 123 upper paragraph: closed left-pointing triangle with a separate lower bar. |
| Bar-ring-bar relation | `\mid\circ\mid` / `\mid0\mid` | 123 upper paragraph and 125 primitive relation; first occurrence marked on each. Ring has no feature deciding circle versus zero. |
| Decorated double chevrons | `\overset{\circ}{\ll}` / `\overset{0}{\ll}`; lower `\mathrm{comm}` on later occurrences | 123 first paragraph and transitivity clause; upper ring and lower comm occupy distinct positions. |
| Second support-operation prefix | `\perp` / `\lrcorner`, followed by a dash | 124 lower paragraph: upright with short lower left foot. The prefix is separate from the sup-like letter group. |
| Operation exponent | `0` / `\circ` | 124 co-sup and second operation; 125 supp, open upper ring; first occurrence on each page marked. |
| Phi-like letter | `\Phi` / `\varphi` / `\phi` | 125 upper formula: top oval, central upright, horizontal foot; not equated with another page's letter by convention. |
| Prose shorthand equals | `$=$` | 123 et que =, 123 lui-=, 125 alors =: two literal horizontal strokes, not expanded to même in the transcription. |
| Roman reference numerals | `\uline{$\overline{\mathrm{VIII}}$}` | 124 two CF references: upper and lower horizontal bars both visible. They are not double underlining. |
| Quotation marks | LaTeX double backticks/apostrophes, or single apostrophes where seen | Double quotation marks on 120 diagramme; 121 commensurables/sous-spatios; 122 terms; 123 strate; 124 quoted nouns; 125 ens. constr. and int. disj. Single strokes around intrinsèque on 125. |
| State/layout marks | `\deleted`, `\inserted`, `\margin`, `\uline`, `\figure` with TikZ | Cancellation, addition guides and marginal Déf checked in place. 124 has two nontextual strokes, reproduced in TikZ. No diagram with objects and arrows, typed page, letter, stamp, or image is inserted into the transcription. |

# Doubts

Every `\unsure` occurrence is listed below, including those inside deletions. Alternatives are the remaining candidates after the second reading; abandoned first-pass readings are recorded in the audit. “None separable” means that the proposed reading is uncertain but the ink does not support a distinct alternative. Confidence concerns the reading, not the mathematical proposition. Subsequent unmarked occurrences of a recurring ambiguous glyph inherit the first candidate for that page.

| Scan | Approximate manuscript line / location | Reading | Every remaining alternative | Confidence | Contextual preference and reason |
|---|---|---|---|---|---|
| 119 | s1, (i), after Inf | `\ell` | `\complement` | medium | Complement is favoured by the Boolean-algebra wording; the drawn tall loop is closer to ell. |
| 119 | s1/s2, (ii)a, overwritten variable | `b` | None separable | low | The final a is clear; the underlying loop may be b. No other candidate can be separated from the overtrace. |
| 119 | s1/s2, (ii)a, overwritten set | `B` | None separable | low | Final A is clear; the underlying capital looks B. Context does not establish the deleted letter. |
| 119 | s2, crossed La famille line | `formée` | None separable | low | Formée fits famille, but the crossing obscures medial letters and accent. |
| 119 | s2, crossed b membership | `I` | `B` | low | B is favoured by the next live sentence; the uncancelled remainder is straighter, hence I first. |
| 119 | s2, crossed word after L’ensemble | `formé` | None separable | low | Formé is compatible with the surviving f and m-like strokes; no secure alternative is separable. |
| 119 | s2, next crossed word | `partie` | None separable | low | Partie fits the surviving p and t-like forms; the cancellation leaves the rest uncertain. |
| 119 | s2, set-definition display | `\widehat B` | `\widetilde B` | medium | The stroke peaks like a hat but also undulates. The prose does not distinguish hat from tilde. |
| 119 | s3, cf déf. reference | `110` | `140` | medium | 110 is closer to the central straight stroke. No referenced page is supplied to decide between 110 and 140. |
| 119 | s3, after cancelled est aussi l’ | `iso.` | None separable | medium | Iso. fits the adjacent power-set expression; its tiny reduced letters remain uncertain. |
| 119 | s3, power-set expression | `\mathcal P` | `\mathscr P` | medium | Power-set meaning favours P but does not decide calligraphic versus script alphabet. |
| 119 | s3, admissible-pair correction, deleted | `sont` | None separable | low | Sont is the best residual reading; the correction obscures it. |
| 119 | s3, admissible-pair correction, live | `est` | None separable | medium | Est fits the pair as a single subject; the small replacement is still difficult to separate. |
| 119 | s3, axiom heading | `Atm. g)` | `Atm. 9)` | medium | The loop and descender favour g), but 9) is visually possible; no expansion of Atm. is supplied here. |
| 119 | s3, axiom heading, exponent 2 | `\gamma\gamma^2` | `\gamma^2` | low | Two gamma-like strokes are visible. The later related heading makes a single retraced gamma plausible, but does not erase the extra stroke. |
| 119 | s3, crossed capital after Pour toute | `F` | None separable | low | F is the closest visible remnant; context does not settle the deleted capital. |
| 119 | s3, comparison, left family | `\mathbb G` | `G` | medium | Parallel stems may be deliberate double strokes or retracing. The surrounding sentence does not decide. |
| 119 | s3, comparison, right family | `\mathbb F` | `F` | medium | The F has doubled strokes, independently checked from G. Plain F remains possible. |
| 119 | s3, F then G membership clause | `,` | None separable | low | A faint low mark may be a comma; the exact punctuation is not secure. |
| 119 | s3, family class after membership | `\mathcal F` | `\mathscr F` | medium | Hooked F has a script form; mathcal versus mathscr is not decided by the hand. |
| 119 | s3, first X with upper ring in B-set | `X^0` | `\mathbb X^0`; `X^\circ`; `\mathbb X^\circ` | medium | Ring permits 0 or circle. Retraced X permits ordinary or double-struck form; all four combinations are retained. |
| 119 | s3, membership X in B-set | `X` | `\mathbb X` | medium | This X is checked separately from the preceding X; its extra stroke may be retracing rather than a double-struck alphabet. |
| 120 | s1, cancelled opening, final word | `parties` | `petites`; `finies` | low | Parties is closest to the visible ending. Petites and finies remain possible beneath the crossing; the sentence does not settle deleted wording. |
| 120 | s1, ambient Sigma subscript | `\mathcal A` | `A` | medium | A curved entry suggests script A; a plain handwritten A remains possible. |
| 120 | s1, ordered family class | `\mathcal F` | `\mathscr F` | medium | Same hooked F family as 119; no contextual distinction between mathcal and mathscr. |
| 120 | s1, F-chain second term subscript | `2` | `1` | medium | Ink bends like 2. The sequence 0,...,n favours 1, but this is not substituted for the first visual reading. |
| 120 | s1, cancellation after final F_n | `\ll` | None separable | low | Residual chevrons suggest ll; the cancelled sign is partly obscured. |
| 120 | s2, Fig notation after similaire | `\operatorname{Fig\,spat}` | `\operatorname{Fig\,opt}` | medium | Spat is favoured by the visible p and by spatiales on 122; opt remains a possible reading of the contracted cluster. |
| 120 | s2, cancelled verb before inserted qu’on | `voudrait` | None separable | low | Voudrait is the closest residual outline; the cancellation prevents secure letter-by-letter recovery. |
| 120 | s2, live verb after qu’on | `aimerait` | None separable | medium | Aimerait fits the visible beginning and ending; medial strokes are highly reduced. |
| 120 | s2, structures d’ordre | `superfétatoires` | None separable | medium | Superfétatoires fits the visible long word; several inner letters and accents are compressed. |
| 120 | s2, crossed article before chacun | `les` | None separable | low | Les is the best residual reading; no competing word can be securely distinguished. |
| 120 | s2, chacun des F, subscript | `i` | `j` | medium | The short dotted stroke favours i; a small lower hook also permits j. Generic family context favours i. |
| 120 | s3, definition after un | `spatios` | `specton` | medium | Spatios is favoured by the suffix and its fuller occurrence on 124; specton remains a possible reduced reading here. |
| 120 | s3, cancelled first word after definition comma | `Une` | None separable | low | Une is the best surviving outline; surrounding text does not settle cancelled wording. |
| 120 | s3, next cancelled phrase | `ens. d'` | None separable | low | Ens. d’ fits visible letters and apostrophe, but overtracing obscures the abbreviation. |
| 120 | s3, final cancellation | `les a` | None separable | low | Les a fits the visible article-like strokes and separate a; crossing remains heavy. |
| 121 | s1, after second Sigma prime | `un` | `une` | medium | Un is the shorter visible form; une is possible if the terminal wave is an e. No grammatical correction is imposed. |
| 121 | s1, short cancellation before sous-spatios | `p.` | None separable | low | Only a p-like stroke and dot remain; expansion is not warranted. |
| 121 | s1, stable par Sup | `\ell` | `\complement` | medium | Same looped operator as 119; complement favoured by the Boolean wording, ell by the literal shape. |
| 121 | s2, cancelled On pourrait encore | `l'exp` | None separable | low | L’exp is the visible abbreviated beginning. Completion beyond it would be conjectural. |
| 121 | s3, nonzero condition inside A_i double-prime | `c_i''` | `a_i''` | medium | Open bowl looks c; the preceding set-builder variable favours a. The first reading remains c. |
| 121 | s3, crossed sign before zero subscript Sigma | `\varnothing_\Sigma` | `\varnothing` | low | The empty-set-like loop is visible; a small Sigma may belong to that deletion or to the replacement zero. |
| 121 | s3, cancelled capital before final union | `A` | None separable | low | A is the best residual capital; the crossing obscures the strokes. |
| 121 | s3, summand subscript in final union | `j` | `i` | medium | A downward hook favours j; bound i and neighbouring formulas favour i. The j-like first reading is retained. |
| 122 | s1, first line before disj. | `mut\textsuperscript{t}` | `mut.` | medium | Raised terminal t is the closer visual reading; it may instead be a short terminal mark after mut. |
| 122 | s1, Ceci posé/pose | `posé` | `pose` | medium | Syntax favours posé, but the accent is too faint to establish. |
| 122 | s1, mais je ... désormais | `préfère` | None separable | medium | Préfère fits surviving consonants; accent strokes and medial letters are reduced. |
| 122 | s2, axiom heading | `Atm. g)` | `Atm. 9)` | medium | Same abbreviated Atm. g)/9) group as 119 and 124, independently read; g is favoured by its descending loop. |
| 122 | s2, A-chain after second ll | `,` | None separable | low | Small lower stroke may be a comma; retained in doubt instead of silently omitted. |
| 122 | s3, Fig notation in conclusion | `\operatorname{Fig\,spat\,disc}` | `\operatorname{Fig\,opt\,disc}` | medium | Spat favoured by the lower inserted notation and spelled spatiales; opt is not fully excluded in this compressed occurrence. |
| 122 | s3, Sigma equality, subscript | `\mathcal A` | `A` | medium | Curved A entry suggests mathcal; plain A remains possible, as on 120 and 125. |
| 122 | s3, inserted parenthesis | `spatios` | `specton` | medium | Spatios favoured by its suffix and the fuller 124 occurrence; specton remains a candidate in this reduced insertion. |
| 122 | s3, des fig before spatiales | `éle` | `él\textsuperscript{e}`; `él\textsuperscript{es}` | low | The e-like ending appears near the baseline. A raised e or es abbreviation is also possible; elementary figures are favoured by the inserted él. |
| 122 | s3, last line, les ... | `morphismes` | None separable | medium | Morphismes fits the surviving long-word outline; reduced medial letters prevent certainty. |
| 122 | s3, last word | `attenants` | `attenant` | low | The terminal sweep may or may not be s. Plural morphismes favours attenants, without settling the ink. |
| 123 | s1, first word | `l'atlas` | `disons`; `j'écris` | low | The initial apostrophe-like stroke and following loops permit the listed readings. The preceding unfinished sentence does not securely decide any of them. |
| 123 | s1, Nous y ... | `prendrions` | None separable | medium | Prendrions fits the visible p, r-like strokes and ending; the middle is reduced. |
| 123 | s1, between vertical bars | `\mid\circ\mid` | `\mid0\mid` | medium | A small ring is visible. Relation context suggests a circle, but a written zero is visually indistinguishable. |
| 123 | s1, above double chevrons | `\overset{\circ}{\ll}` | `\overset{0}{\ll}` | medium | Upper ring, no index below at this occurrence. Context suggests circle decoration; 0 remains visually possible. |
| 123 | s2, cancellation after ça ne | `dépend` | None separable | low | Dépend is the best remnant, but heavy crossing obscures the word. |
| 123 | s2, figures ... et C | `R` | `K`; `P` | low | The small capital has an R-like stem and oblique, also compatible with K or P. The supplied pages do not disambiguate the name. |
| 123 | s2, before g <= f <= e | `si` | None separable | medium | A short s-like stroke and point suggest si; the reduced word is not fully secure. |
| 123 | s3, donc ... before three variables | `finalement` | None separable | medium | Finalement fits the remaining outline, but several inner letters are a wave. |
| 123 | s3, before disj et | `mutuellemt` | `mutuellement` | medium | Mutuellemt best matches the contracted ending; full mutuellement remains possible in the compressed strokes. |
| 123 | s3, opening delimiter of second live pair | `(` | `\{` | medium | Left delimiter looks round while the right is curly. Set context favours a curly left brace; asymmetry is retained. |
| 123 | s3, after second live pair | `commens` | None separable | medium | Commens is a plausible visible abbreviation; no expansion is inserted into the text. |
| 124 | s1, axiom reference after validité | `Atm. g)` | `Atm. 9)` | medium | g) is favoured by the descending loop; 9) remains visually possible. Same abbreviated label as the earlier headings. |
| 124 | s1, heavily traced axiom symbol | `\gamma\gamma^3` | `\gamma^3` | low | Two descenders are visible. A single gamma retraced or two gamma-like signs are possible; the related 122 heading favours a single sign. |
| 124 | s1, second CF VIII page reference | `71` | `74` | medium | 71 is the first visual reading; the final mark could be 4. The referenced page is outside this supplied range. |
| 124 | s1, le cas des ... fidèles | `morphismes` | None separable | medium | Morphismes fits visible initial and ending; internal waves remain reduced. |
| 124 | s2/s3, quoted noun after spatios | `espacons` | `espaces` | medium | Espacons best follows the visible c and final rising cluster; espaces remains possible. No normal spelling is imposed on the coined term. |
| 124 | s3, first operation | `\operatorname{co\!-\!sup}^{0}` | `\operatorname{co\!-\!sup}^{\circ}` | medium | Co- and sup-like cursive strokes are visible. The upper open ring permits 0 or circle. The operation is not expanded beyond the written abbreviation. |
| 124 | s3, prefix of second operation | `\perp` | `\lrcorner` | low | A short upright and lower leftward foot precede a dash. Perpendicular and lower-corner signs are the two closest shapes; context does not decide. |
| 124 | s3, parenthesis before disons | `spectralement` | None separable | medium | Spectralement follows the initial spe-like cluster and ending; the long middle wave is not a cancellation but is difficult to parse. |
| 124 | s3, final word | `qu'on` | `qu'en` | medium | The tiny vowel is ambiguous. The next page begins fin de compte, which favours qu’en; qu’on remains the first visual reading. |
| 125 | s1, after ens. constr. and dash | `en ajoutant` | None separable | medium | Ajoutant is favoured by the descending initial consonant and final crossed stroke; reduced middle letters remain uncertain. |
| 125 | s1, before supp | `\ell` | `\complement` | medium | Tall loop matches the earlier ell/complement glyph. Complement is contextually plausible; literal ell remains first. |
| 125 | s1, supp exponent | `0` | `\circ` | medium | Small open upper ring can be zero or circle; no visual basis chooses between them. |
| 125 | s1, after supp exponent | `\Phi` | `\varphi`; `\phi` | low | Upper open oval and horizontal foot favour capital Phi; handwritten varphi or phi remain possible. No external notation is assumed. |
| 125 | s2, cancelled word after Il y a | `donc` | None separable | low | Donc is the closest residual reading; cancellation obscures the middle. |
| 125 | s2, la donnée ... | `primitive` | None separable | medium | Primitive fits visible initial and ending; compressed middle is not fully legible. |
| 125 | s2, relation between X and Y | `\mid\circ\mid` | `\mid0\mid` | medium | Same circle/zero between bars as on 123; circle is contextually favoured but not visually decisive. |
| 125 | s2, comparaison ... strates | `de` | `des` | medium | The visible stroke supports de. Des is favoured by syntax, but a separate terminal s cannot be securely seen. |
| 125 | s3, supports ... à une figure | `subordonnés` | None separable | medium | Subordonnés fits the outline; its reduced internal letters remain doubtful. |
| 125 | s3, ambient Sigma subscript | `\mathcal A` | `A` | medium | Curved left entry suggests script A, as on 120 and 122; plain A remains possible. |
| 125 | s3, final word after On va | `jeter` | `faire` | low | Loop-descending initial followed by e-like loop and t-like upright favours jeter over faire. The continuation is not supplied. |

# Slips and apparent inconsistencies retained

No spelling slip can be confidently diagnosed independently of the handwriting uncertainty. The following visible or potentially inconsistent forms are retained; “apparently intended” is explicitly conjectural, never a correction to the transcription.

| Scan | Line / location | As written or first visual candidate | Apparently intended, if any | Reason for retaining it |
|---|---|---|---|---|
| 120 | First F-chain | `F_0\ll F_2\ll\cdots\ll F_n`, with 2/1 doubt | Perhaps `F_1` | The curved subscript resembles 2; the numerical sequence is not allowed to decide the stroke. |
| 121 | First commensurability union | `A=\bigcup_{1\leq i\leq n}A_i` | Perhaps lower bound 0 | The preceding chain includes A_0, but the lower bound on this line visibly reads 1. |
| 121 | Nonzero condition | `c_i''`, with a_i'' alternative | Perhaps `a_i''` | The set-builder uses a_i, but this occurrence's initial bowl is open. |
| 121 | Last union | `\bigcup_{0\leq i\leq n}A_j''`, with j/i doubt | Perhaps `A_i''` | Bound and summand differ in the first visual reading; the summand has a downward hook. |
| 123 | Second live pair | Opening `(` / `\{`, closing `\}` | Perhaps matched braces | The left delimiter looks rounded; no silent balancing of manuscript delimiters was made. LaTeX grouping itself remains balanced. |
| 119, 124 | Axiom symbols | Two gamma-like strokes / single retraced gamma | Perhaps one gamma as on 122 | The repeated downward strokes remain visible and doubtful. |

# Abbreviations and shorthand

Expansions below are interpretive aids only. None is substituted into the transcription; uncertain expansions are labelled as such.

| Written form | Likely expansion or function | Scans |
|---|---|---|
| alg. | algèbre | 119, 121, 123 |
| op. | opération | 119 |
| t.q. | tel que / tels que | 119, 121 |
| cf | confer / comparez | 119 |
| déf.; Déf | définition | 119 |
| p. | page in references; the deleted p. on 121 has no secure expansion | 119, 121, 124 |
| iso. | isomorphe, probably | 119 |
| sous-ens. | sous-ensemble(s) | 119 |
| Atm. | Axiom-label abbreviation; full expansion not established by these pages | 119, 122, 124 |
| NB | nota bene | 121, 122 |
| ens. | ensemble | 120 (deleted), 125 |
| mut.; mut with raised t; mutuellemt | mutuellement | 121–123 |
| disj; disj. | disjoint(s) | 121–123, 125 |
| i.e. | id est / c'est-à-dire | 122, 123 |
| il f. et s. | il faut et suffit | 122 |
| tt | tout | 122 |
| Fig; fig | figure(s) | 120, 122, 123 |
| él; él.; éle / raised e / raised es | élémentaire(s), probably | 122, 123 |
| spat | spatial(es), supported by spelled spatiales | 120, 122, 123 |
| disc | discret/discrètes, probably; not expanded in these pages | 120, 122 |
| comm; comm.; commens | commensurable(s), supported by the local definitions | 122, 123, 125 |
| p.r. à | par rapport à | 123 |
| CF | Reference siglum; expansion not established by these pages | 124 |
| tjrs | toujours | 124 |
| cor. | corollaire | 124 |
| néc. | nécessairement | 124 |
| sup; supp | support, probably in these operation names; no expansion imposed | 124, 125 |
| constr. | constructible(s) | 125 |
| int. disj. | intérieurement disjoint(s), probably | 125 |
| prose `=` | même, probably in the three prose phrases | 123, 125 |
| `2:2` | deux à deux | 121 |
| l'exp (cancelled) | Beginning of an exp- word, possibly expression/expliciter; no secure completion | 121 |

# Legibility and limits

The page layout and most words are legible, but this is very reduced, widely spaced handwriting. Several word middles collapse into strokes. The least secure material is cancelled or overwritten wording on 119–121, the axiom labels, the transition from the last line of 122 to the first word of 123, small index and alphabet distinctions, the second operation's prefix on 124, and the last word of 125. Alternatives in these places should be reviewed against the images before a critical edition uses the text.

All seven whole-page images and all twenty-one thirds were inspected directly; the thirds were reread for the second audit, with local enlargements where needed. No OCR, external transcription, web source, or mathematical reconstruction was used. No word block was replaced by a description or a gap. Zero illegible macros means that a tentative reading was offered everywhere, not that every stroke is certain. The audit records changes and preserves unresolved alternatives rather than claiming a verified authorial text.
