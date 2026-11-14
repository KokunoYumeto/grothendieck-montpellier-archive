# Notation

| Scan and position | Mark or letters | Ink on the crop | LaTeX or reading |
| --- | --- | --- | --- |
| 2, heading and items 1–11 | List numbers | Bare number and right parenthesis at 1, 5, 6. Single enclosures around 2–4 and 7–11. | Literal `1)`, etc.; `\textcircled` for single enclosures. The small second mark beneath 10 shares its circle. |
| 2, N.B., after « cohomologique » | Crossed, looped character | Two short strokes above a closed descender. Candidates ζ, ξ, §, g. A separate dot follows. | `\unsure{$\zeta$\|$\xi$\|§\|$g$}.` |
| 2, item 1 | fppf | First and last letters have cross strokes; the two middle letters have descenders. | `\mathrm{fppf}` |
| 2, item 1, interline | Reference star | Several small intersecting strokes within their own circle below the first f of « formalisme ». | `\textcircled{\scriptsize $*$}` |
| 2, item 2 | Repetition stroke | Long continuous horizontal stroke before the colon, with no letters above or below it. | `\rule[.45ex]{3.9em}{.45pt}` |
| 2, item 3 | p | Descending stem and small upper bowl before a hyphen. | `$p$-primaire` |
| 2, item 4 | RR | Two plain capitals, no stops between them. | `RR` |
| 2, items 4–5 | χ or x | Cross with elongated lower-left stroke, very long at 5. | `\unsure{\chi\|x}` at first occurrence; `\chi` at 5. |
| 2, items 4 and 6 | coeff. | Two tall f strokes and one period. | `coeff.` |
| 2, item 5 | V.A. | Capitals separated and followed by dots. | `V.A.` |
| 2, items 6 and 8 | Paired double quotes | Two raised strokes at each end of « continus » and « cristaux ». | Two backticks, two apostrophes. |
| 2, item 7 | Z | Two parallel obliques join the two horizontals. | `\mathbb{Z}` |
| 2, item 10 | Cross below 10 | Two small intersecting strokes; the heavy centre can suggest an asterisk. | `\unsure{\times\|*}` inside the same circle. |
| 2, item 10 | pbs, SGA 6 | The b of pbs has a heavy downstroke; three faint ordinary capitals in the citation. | `pbs`, `SGA 6` |
| 2, N.B., items 10–11 | Short forms | N.B. has dots; th. and val. end with stops. The faint Cf at 10 has no clear stop. | `N.B.`, `th.`, `Cf`, `val.` |
| 3, items 12–19 | List numbers and lower cross | Circled 13, 15, 16, 18, 19; a small cross touches the bottom of 19. At 12, 14 and 17 the number has a closing parenthesis. | Single enclosures, same cross candidates as at 2/10. |
| 3, right of 12, 14, 16, 18 | Right-edge marks | Two short parallel lines at 12; long bent checks or square-ended strokes at 14, 16, 18. | Individual TikZ paths. |
| 3, item 15, line 2 | π and small mark | Horizontal roof and two legs; a point or short stem at the return of the second leg. Candidates i, filled point, small dot. | `\pi_{\unsure{i\|\bullet\|\cdot}}` |
| 3, item 15, final lines | Theorem abbreviations | T and h are followed by s, with a high tick in the first occurrence. The second has no distinct tick. | `\unsure{Th's\|Thés}`, `\unsure{Ths\|Thés}` |
| 3, after item 15 | Quotation marks | Raised pairs around « vrai » over a pointer ending before « groupe ». | Paired backticks and apostrophes inside `\inserted`. |
| 3, item 17, line 3 | Pic, X, S | Single underline under Pic alone; X, slash and S are lower and to the right. X, 1 and S on the continuation are at line height. | `\underline{\mathrm{Pic}}_{X/S}`; `X`, `1`, `S` |
| 3, item 19 | dim. | A dot follows on the first line, before « quelconque » on the next. | `dim.` |
| 3, item 13 | noeth | Tall t and h at the end, with no terminal point. | `\unsure{noeth}` |
| 4, 20–24 | Number enclosures and crosses | 20, 21, 24 have single circles; 22, 23 have a closing parenthesis. Small x below 23 and touching the circle at 24. | Same cross candidates as 2/10 and 3/19. |
| 4, 21, first line | Cohomology | Ordinary single-stroke H and F on both sides. Left star has six rays. On the right a smaller cross runs into the opening parenthesis. Rounded, closed subscripts lie below X and F. | `H^{*}(X,F)\to H^{\unsure{*\|x}}(X_0,F_0)` |
| 4, 21, lines 3–5 | Affine and closed-subset notation | Two equals signs. The first spectrum word has more letters after p. The second is shorter. A slash precedes the hooked ideal letter. The inclusion opens to the right and has no lower bar. | `X=\operatorname{Spec} A`, `X_0=\unsure{\operatorname{Spe}\|\operatorname{Spec}\|\operatorname{Sp}} A/\unsure{I\|J}`, `I`-adique, `X_0\subset X` |
| 4, 22, line 2 | Compound sign | Small upright cross above a horizontal stroke. | `\pm` |
| 4, memo entries 1, 2, 5, 6 | List mark | Two crossing diagonals enclosed in an oval. No number in these ovals. | `\otimes` |
| 4, memo diagram | Brace, two arrows, equals | One heavy closing brace on the left group. The arrows each have two shafts and a right head. Two parallel horizontals between locale and bidualité. | `\right\}`, TikZ-CD `Rightarrow` and `=` |
| 4, 23, third and fourth lines | f, X, Y | Lowercase f, colon, X with a small rising and falling terminal stroke, right arrow, single-stroke Y. Y repeats after que. | `f:\unsure{X'\|X}\to Y`; `Y` |
| 4, 24, bottom lines | k, τ, dimensions and equals | Lowercase k; short horizontal with a single bent leg at τ, then a separate hyphen. Digits 3, 1, 0, 4, 2. | `k`, `\unsure{\tau\|t}`, `3`, `1`, `0`, `4`, `2`, `=` |
| 4, 21, memo and 24 | Short forms | isom and dim without stops at 21; top without a stop in the memo. Stops occur at num. and équiv. in 24; the same endings at the extreme foot are compressed. | `isom`, `dim`, `top`, `num.`, `équiv.`, `hom` |
| 4, item 21, above X | coh. or ch. | The small o touches the preceding c and h. The stop is separate. | `\unsure{coh.\|ch.} étale` |
| 4, memo, left of brace | Possible high question mark | The hook above li of régulier has a separate dot-like stroke. | `\overset` over li, with `\unsure{?}` |
| 4, end of memo | SGA, final digit | Three ordinary capitals. The last digit has the spur and foot of 1 in item 21. | `SGA \unsure{1961\|1962}` |
| 4, margin beside 24 | Raised ordinal | A little closed oval follows the upper right of 1. | `1\textsuperscript{o}` |
| 5, item 25 | Number and cross | Circled 25 with small crossing strokes at its foot. | Circled TikZ node with `\unsure{\times\|*}`. |
| 5, item 25, all five lines | Zero | Small ovals in the equivalences and in 0-cycle(s), with a short hyphen in the two compounds. | `$0$`, `$0$-cycle`, `$0$-cycles`. |
| 5, item 25, line 2 | Quotation marks | Two opening and two closing high strokes around pb du carré, inside round brackets. | Paired TeX double quotes. |
| 5, items 25 and 27 | Short forms | alg., rat., alb., équiv (also with a terminal stroke), pb, cf, dim followed by a low short stroke. | Preserve each shortening, `dim\unsure{,\|.}`. |
| 5, item 28, line 2 | Z | Two diagonals inside Z, both joining the bars. | `\mathbb{Z}`. |
| 5, item 25, lines 1–3 | Accent on contraction | The first mark falls right, the next is almost upright. The third falls right again. Stops differ among the three. | `\unsure{èquiv\|équiv}`, `équiv.`, `èquiv.` |
| 5, items 26–28 | Numbering | 26 and 27 stand bare. 28 is circled, with no mark at the bottom. | `26`, `27`, circled `28` |

## Doubtful readings

Locations count physical manuscript lines within an item. Marginal and interlinear lines are identified separately. A dash in the alternatives column marks a single tentative reading. The text carries a recurring symbol doubt at its first occurrence on each scan. The explanations identify the repeats.

### Scan 2

| Scan | Item and approximate line | First reading | Other readings | Confidence | Surrounding text and stroke evidence |
| --- | --- | --- | --- | --- | --- |
| 2 | under title, cancelled line | `Collection` | — | low | Two ascending loops, a crossbar and a dot survive the zigzag. The title gives no independent reading of the word. |
| 2 | under title, cancelled line | `1964` | — | low | The upright and angled remnants resemble the date immediately above. The final digits share strokes with the cancellation. |
| 2 | N.B., line 2, after cohomologique | `$\zeta$` | `$\xi$`, `§`, `$g$` | low | The head has a zigzag and the foot a closed loop. Its grammatical role is unclear. The dot after it is separate. |
| 2 | N.B., line 3 | `relèvent` | `relévent` | medium | The first small mark above the inner e has little directional extent. The following de la théorie favours relèvent. |
| 2 | N.B., line 4 | `rattachent` | — | medium | The middle after ra is a sequence of contacts. The following à la th. de Néron supports rattachent. |
| 2 | N.B., line 5 | `représentabilité` | — | medium | Only some interior strokes separate in the long word. The phrase yoga de …, de foncteurs supports représentabilité. |
| 2 | N.B., line 5, before foncteurs | `de` | `des` | medium | The last graphic movement might be a terminal s. The earlier de and the parallel list favour de. |
| 2 | item 1, after formalisme | `général` | `general` | medium | The tips of the two accents touch the crowded upper note. The word after formalisme favours général. |
| 2 | item 1, bracketed addition | `coh-mologie` | `coho-mologie`, `cohomologie` | low | After coh there is a distinct horizontal trace and a low series of humps. Cohomologies earlier on the line supports cohomologie, but the trace has been kept. |
| 2 | item 3, last name | `Chafarévitch` | `Chafovévitch` | medium | Ch is tall and f descends. The neighbouring vowel and following arm run together. The second occurrence in item 5 favours Chafarévitch. |
| 2 | item 4, line 2, first word | `Relation` | `Relations` | medium | An unmodulated terminal stroke can be the end of n or the start of an s. The following avec accommodates either reading. |
| 2 | item 4, line 2, before d'Artin | `représentation` | `représentations` | medium | The ending flattens at the pen lift. The separate word supérieures favours représentations. |
| 2 | item 4, bracketed line, and item 5 | `\chi` | `x` | medium | The long leftward-descending foot is stronger in item 5. Both follow du. The notation in these two lines favours χ. |
| 2 | item 4, after closing bracket | `.` | — | low | A small isolated point below the tip may be terminal punctuation. Omitting it is also possible. |
| 2 | item 5, parenthetic name | `chafarévitch` | — | medium | The acute is visible, the compressed middle vowel less so. The longer spelling in item 3 supports the reading here. The initial is lowercase. |
| 2 | item 7, line 2 | `satisfaisant` | `satisfaisants` | high | The lifted final stroke after t need not be a letter. The plural théorèmes permits the second ending. |
| 2 | item 8, first word | `Formalisme` | `Formalismes` | medium | The final e has a short return. It could form a terminal s. Item 1 has the singular form. |
| 2 | item 8, end of line after connexion | `..` | — | low | Two points stand close to the right edge, separated from the final letter. The phrase continues with intégrable. Their status as two punctuation marks is uncertain. |
| 2 | item 10, under the number | `\times` | `*` | medium | Two obliques meet at a dark contact. The other marked numbers in the list support the same small cross without settling its number of rays. |
| 2 | item 10, first line | `pbs` | — | high | The b has a dense downstroke. The final s is small. The following connexes supports a plural shortening. |
| 2 | item 10, after Modules | `analytique` | `analytiques` | medium | A grey speck is separate from the dark ending. The adjacent algébrique is singular and favours analytique. |
| 2 | item 10, faint reference | `Cf` | `cf` | medium | The tip of the opening bracket overlaps the first letter. The citation SGA 6 supports the abbreviation but gives no case evidence. |

### Scan 3

| Scan | Item and approximate line | First reading | Other readings | Confidence | Surrounding text and stroke evidence |
| --- | --- | --- | --- | --- | --- |
| 3 | item 12, pale left note, line 1 | `commencé` | — | medium | The two central humps blend. The final acute and the following par Raynaud support commencé. |
| 3 | item 13, first word | `Théorémes` | `Théorèmes` | medium | Both upper strokes rise to the right. The second is almost horizontal. The word recurs in the similar phrase at 2/7, where the second mark is much flatter. Ordinary French favours Théorèmes. |
| 3 | item 13, line 1, after Théorémes | `assymptotiques` | `asymptotiques` | medium | Two linked s-shaped marks precede the descending y. They can also form the entry and exit of one s. The phrase supplies no count of the s strokes. |
| 3 | item 13, line 1, right edge | `foncteurs` | — | medium | The tall f, t crossbar and last curved pen stroke survive. The middle and final letters are run together. The following de Greenberg and the clearer foncteurs in item 14 favour foncteurs. |
| 3 | item 13, line 3, before complet | `noeth` | — | high | The last two tall strokes look like t and h. There is no stop, and the writer continues with complet ou hensélien. Anneau local supports the shortened adjective. |
| 3 | item 15, margin, second line | `Mazur` | — | medium | The two small letters between M and the final r share their strokes. The following hyphen and Artin identify a sequence of names without determining the first one. |
| 3 | item 15, margin, after Quillen | `en` | — | medium | The pale first word of the last line is almost a horizontal. Its position before train favours en. |
| 3 | item 15, first word | `Théorie` | `Théories` | medium | The final dark junction can end e or continue into s. Other entries begin Théorie de, including item 16. |
| 3 | item 15, first letter of type, under the t | `g` | — | low | A small upper compartment and a closed descender survive under the final upright. The surrounding text supports type as the live word and gives no earlier letter. |
| 3 | item 15, line 2, subscript to π | `i` | `\bullet`, `\cdot` | low | There is a point above a little terminal stroke adjoining the second leg. Reading the lower piece as the body of i gives an index. A point alone accounts for the other readings. There is no independent descender for j. |
| 3 | item 15, line 2 to line 3, cancelled | `coefficients` | — | medium | The tall double f and dot survive at the right edge. c, a dotted stroke and the t/s ending remain on the following line. The two positions and à support the joined reading. |
| 3 | item 15, line 3, before infinitésimaux | `noveaux` | `noyaux`, `nouveaux` | low | An oval o is followed by two small separate marks and a long run to a detached x. There is no clear descender for y. The nearby phrase à … infinitésimaux favours noyaux, while the individual strokes favour noveaux. |
| 3 | item 15, first small addition, before d' | `Th's` | `Thés` | low | A high, nearly vertical tick falls between h and s. It could be a contraction apostrophe or an accent over a contracted vowel. The following de and the repeated shorter Ths favour a theorem abbreviation. |
| 3 | item 15, first small addition, name | `Hurwisz` | `Hurwicz` | medium | A dot sits over i, followed by an s-shaped stroke and a descending z. The first may instead be c. The page offers no other spelling of this name. |
| 3 | item 15, interline, before de comparaison | `Ths` | `Thés` | medium | The h and s meet and there is no separate accent of the size seen in the first abbreviation. The similar preceding abbreviation supports both. |
| 3 | item 15, interline, word crossed after de | `spécialisation` | — | low | The crossed band preserves sp, two high marks, an ascending loop and a t. The clearly written spécialisation in item 16 supports the reading. |
| 3 | item 16, left note after Artin | `situation` | — | medium | Its end meets the circle around 16. The following peu engageante and the opening sit… support situation. |
| 3 | item 17, bracketed left note | `résolu` | — | medium | The last u is a single low tail. Par Raynaud favours a past participle. A separate e cannot be established from the ending. |
| 3 | item 17, line 3, between dim and relative | `de` | `rel` | low | A loop crossed by the long cancelling stroke could be d or the end of rel. The ensuing relative favours an abandoned start of that word. |
| 3 | item 18, line 1, after du | `passage` | — | medium | The inner letters share one low stretch ending in a descender. The following au quotient favours passage. |
| 3 | item 18, cancelled continuation, first word | `Construction` | `Constructions` | medium | Two long horizontal strokes pass through the ending. Either number fits the following adjective. |
| 3 | item 18, cancelled continuation, second word | `générale` | `générales` | medium | The two accents and the ascending l remain. The last short stroke can be the terminal e or an s. The preceding noun has the same ambiguity. |
| 3 | item 18, cancelled last line | `modules` | `variables` | low | Most of the baseline lies under the strike. A short rising stroke in the middle and the tall loop near the end favour modules. The phrase corps de modules favours that reading. |
| 3 | item 19, foot of numbered circle | `\times` | `*` | medium | The intersecting strokes touch the rim and the lower part of 9. The same position in 2/10 supports a cross. |
| 3 | item 19, line 1, after d' | `amplitude` | `amplitudes` | medium | The final e is unusually dark and has a small return. It can contain a terminal s. The singular Théorie d'amplitude favours amplitude weakly. |

### Scan 4

| Scan | Item and approximate line | First reading | Other readings | Confidence | Surrounding text and stroke evidence |
| --- | --- | --- | --- | --- | --- |
| 4 | item 21, high mark on right H | `*` | `x` | medium | Two crossing strokes partly meet the following round bracket. The star on the left H has three distinct axes and favours the star on the right. |
| 4 | item 21, interline over the final X | `coh.` | `ch.` | medium | A tiny round contact could supply the o before h. The following étale and the longer phrase on the next lines favour coh. |
| 4 | item 21, line 3, after second equals sign | `\operatorname{Spe}` | `\operatorname{Spec}`, `\operatorname{Sp}` | low | S and the descending p are clear. What follows is a short flat wave. The first expression on the line has a longer and more legible Spec, favouring the full reading by parallelism. |
| 4 | item 21, line 3, after slash and before -adique | `I` | `J` | medium | The upright after the slash descends to a left hook. The similar letter in the compound has a top and lower bar. The two places favour the same capital, without deciding I/J. |
| 4 | item 22, left margin | `Saavedra` | — | medium | The end of the pale name reaches the item number. S-aa and the tall d are distinguishable. The note travail … en train identifies a name without settling its last letters. |
| 4 | item 22, line 2, after en termes de | `représentation` | `représentations` | medium | The final wave can end n or include s. The adjacent linéaires favours représentations. |
| 4 | item 22, line 3, after et de | `représentation` | `représentations` | medium | The end is a similar flat wave. The first occurrence after termes de suggests a parallel plural. There is no separately traceable final s. |
| 4 | item 22, parenthetic addition, after à | `le` | `la` | medium | The final letter is a small open loop like e. The following théorie favours la. The two short words are left as they appear. |
| 4 | heading above the brace | `memoire` | `mémoire` | high | There is a dot above i. The e after m has no clearly separate acute. The ordinary phrase favours mémoire. |
| 4 | memo diagram, first entry at left | `Résolution` | `Résoluton` | medium | The middle of the word joins t to the final rounded strokes. Singularités and the clearly separate first letters favour Résolution. |
| 4 | memo diagram, third entry at left, above li of régulier | `?` | — | low | An elevated right-curving hook with a dot-like stroke stands above the l/i junction. It may belong to the letter formation. A question mark attached to régulier is the other reading. |
| 4 | memo diagram, lower right, first word | `th` | `ths` | medium | A crossed t and tall h are visible, with a small terminal return. The following de finitude favours the theorem abbreviation and leaves its number open. |
| 4 | memo, line below brace | `morphismes` | — | medium | The middle is a short series of overlapping strokes. The clearer singular morphisme in the diagram and the plural affines favour morphismes. |
| 4 | memo, circled-cross entry before de finitude | `Théorème` | `Théorèmes` | medium | The last undulation is flat. It can conceal an s. The surrounding words accommodate either number. |
| 4 | memo, after Théories and before type, cancelled | `rig` | `rigide` | low | A dot and a descending stroke protrude from the hatched band. The later rigide suggests the longer candidate. Only part of its body survives. |
| 4 | memo, Questions dans SGA, final digit | `1961` | `1962` | high | The straight stem, high left spur and bilateral foot match 1 in the circle at item 21. The 2 beside it has a curved top and sloping body. The heavy foot of the date still allows 2. |
| 4 | item 23, below number, repeated at 24 | `\times` | `*` | medium | The first sign is a two-stroke x. The analogous sign at 24 intersects the rim. Other numbered crosses support the same convention. |
| 4 | item 23, first cancelled word | `qq` | `qcq` | low | A descender and two short arches remain under three long horizontals. There is little room for the full word quelconques. The neighbouring adjective does not decide the abbreviation. |
| 4 | item 23, between rationnelle and cycles | `des` | `de` | medium | A d and its following stroke are clear. The terminal flick may contain s. Both de cycles and des cycles fit the phrase. |
| 4 | item 23, just after des/de, before cycles | `,` | — | low | A little downturned ink point sits below and to the right of the last letter. Its separation supports a comma. It could also be an incidental mark. |
| 4 | item 23, domain after f and colon | `X'` | `X` | medium | The right arm of X has a separate-looking upper hooked tip. The other X's in item 21 have shorter arms. The sentence says nothing else about a prime. |
| 4 | item 24, line 2, between corps and clos | `algébriqmt` | `algébriquemt`, `algébriquement` | low | From the q descender to the rising terminal t there is a single low wave and little room for several separately formed vowels. The phrase corps … clos favours the full word. A contraction accounts for the visible length. |
| 4 | item 24, line 2, after the shortened adverb | `clos` | `clés` | medium | The first tall stroke is followed by a tightly closed middle loop. The point below belongs to the following line or its punctuation. Corps … favours clos. |
| 4 | item 24, after est-il | `\tau` | `t` | high | The short roof has one bent, open foot. The page's ordinary t's have a tall vertical. A separate horizontal hyphen follows. |
| 4 | item 24, at the extreme foot, after the two question marks | `,` | `'` | low | A small rising and then falling hook is higher than both question points. Its shape permits a comma or an apostrophe. The question gives no preference. |

### Scan 5

| Scan | Item and approximate line | First reading | Other readings | Confidence | Surrounding text and stroke evidence |
| --- | --- | --- | --- | --- | --- |
| 5 | item 25, lower rim of numbered circle | `\times` | `*` | medium | Two short arms join at the rim. The analogous signs under 10, 19, 23 and 24 favour a cross. |
| 5 | item 25, line 1, after alg., recurring after alb. in line 3 | `èquiv` | `équiv` | medium | The initial accent is tilted down towards the right, especially after alg. The near-vertical mark after rat. points the other way. The expanded equivalent later on the page favours the conventional acute only as a lexical reading. |
| 5 | item 25, line 4, before à 0 | `èquivalent` | `équivalent` | medium | The upper right end of the small stroke comes down close to e, resembling the stroke on à in this line. The neighbouring uses of the same root favour équivalent as a word. |
| 5 | item 25, line 4, after Question de l' | `équivalence` | `èquivalence` | medium | The mark is almost a dot with a slight upward tilt. It differs from the clearer right-falling mark on the preceding equivalent. The wording favours équivalence. |
| 5 | item 26, after Rosenlicht | `relative` | `reletive` | medium | There is a small bare hump after l. The following t starts immediately. The phrase sur base quelconque supports relative. |
| 5 | item 27, first word | `Adèles` | `Adéles` | medium | The mark over the first e is very short and nearly upright. Its thicker upper left edge suggests a grave. No other occurrence settles its direction. |
| 5 | item 27, after dim | `,` | `.` | high | The tiny low mark tilts and extends below the writing line. The use of dim as a shortening favours a full stop. The same page has a longer comma after locales. |
| 5 | item 28, second line, before de type fini | `prèschémas` | `préschémas` | medium | The first accent slopes down to the right. The second is almost vertical, with a slight rise. The separate schémas in item 27 supports the second accented vowel. The usual form of the compound would favour préschémas. |

## Slips and unusual forms retained

The middle column gives the manuscript reading. The next column gives a possible intended or more usual form. Parenthetic question marks here indicate editorial uncertainty.

| Scan and location | As written | Apparent intention or ordinary form | Evidence |
| --- | --- | --- | --- |
| 2, N.B., after cohomologique | A looped sign followed by a dot | Undetermined | Its upper turns meet the closed lower loop. It was left in place. |
| 2, item 1, small bracketed addition | coh-mologie (?) | cohomologie | A short horizontal interrupts the word. The main entry has cohomologies in full. |
| 2, items 3 and 5 | Ogg-Chafarévitch / Ogg-chafarévitch (?) | The same name in the two entries | Both follow « de Ogg- ». The c has different height in the two occurrences. |
| 2, item 6 | coeff. discrets étales | coefficients discrets étales | The writer puts both plural endings on the page. |
| 2, item 7 | théorèmes de dualité globale satisfaisant (?) | satisfaisants (?) | A small finishing stroke follows t. The plural at the beginning of the phrase supplies the alternative. |
| 2, item 10 | Modules | modules | The M is as tall as the other capitals. |
| 3, item 13 | Théorémes (?) assymptotiques (?) | Théorèmes asymptotiques | The two upper marks and the separate low curves before y account for the retained spelling. |
| 3, item 14 | champs champs | champs | One occurrence ends the line, the other starts the next line. Both are live. |
| 3, item 15 | noveaux (?) | noyaux (?) or nouveaux (?) | The manuscript supplies neither a distinct y-descender nor a neatly closed second vowel. |
| 3, item 16, margin | de Artin | d'Artin | The little e is written separately and survives. |
| 4, item 22 | des catégorielles abéliennes | des catégories abéliennes (?) | Two tall strokes intervene before the end of the first word. |
| 4, item 22, addition | à le théorie (?) | à la théorie | The terminal loop resembles e. |
| 4, heading in the middle | Pour memoire (?) | Pour mémoire | There is no distinct short stroke over the first e. |
| 4, memo, diagram | la top étale | la topologie étale | « top » has no full stop. The contraction is retained. |
| 4, items 21 and 24 | Spe (?) and algébriqmt (?) | Spec and algébriquement (?) | Later letters reduce to a short wave in each. |
| 5, item 25 | èquiv, èquiv., èquivalent (?) | équiv, équiv., équivalent | The marks over the initial e slope in the same direction as the mark on the nearby à. |
| 5, item 27 | dim, (?) | dim. | The abbreviation ends in a small low stroke. |
| 5, item 28 | prèschémas (?) | préschémas | The directions of the first and second marks differ. |

## Abbreviations

Expansions are editorial. The table also covers contractions whose letters or stops remain in doubt. Locations refer to the numbered manuscript items.

| Written form | Likely expansion or meaning | Location |
| --- | --- | --- |
| N.B. | nota bene | 2, heading |
| th. | théorie | 2, N.B., « de Néron » and « du topos » |
| fppf | fidèlement plat de présentation finie | 2, item 1 |
| RR | Riemann–Roch | 2, item 4, compare the full name in item 10 |
| coeff. | coefficients | 2, items 4 and 6 |
| V.A. | variétés abéliennes | 2, item 5 |
| pbs / pb | problèmes / problème | 2, item 10 and 5, item 25 |
| Cf / cf | confer, compare | 2, item 10 and 5, margin to item 25 |
| SGA | Séminaire de géométrie algébrique | 2, item 10 and 4, memo |
| val. | valuation | 2, item 11 |
| noeth | noethérien | 3, item 13, after « anneau local » |
| Th's / Thés / Ths | théorème(s) | 3, item 15 |
| Pic | Picard | 3, item 17, underlined with X/S below |
| dim / dim. / dim, | dimension | 3, items 17 and 19, 4, items 21 and 24, and 5, item 27 |
| coh. / ch. | cohomologie | 4, interline at item 21 |
| isom | isomorphisme | 4, item 21 |
| Spec / Spe / Sp | spectre | 4, item 21 |
| top | topologie | 4, memo, « pour la top étale » |
| th / ths | théorème(s) | 4, memo, « de finitude » |
| etc | et cetera | 4, memo, written twice |
| qq / qcq | quelconques (?) | 4, item 23, cancelled before « réguliers » |
| algébriqmt / algébriquemt | algébriquement | 4, item 24 |
| num. / num | numériquement or numérique according to its place | 4, item 24 |
| équiv. / équiv / èquiv. / èquiv | équivalent(s) or équivalence according to its place | 4, item 24 and 5, item 25 |
| hom | homologique | 4, item 24, small addition |
| alg. | algébriquement | 5, item 25 |
| rat. | rationnellement | 5, item 25 |
| alb. | au sens d'Albanese (?) | 5, item 25 |
| 1° | first question | 4, note beside item 24 |

## Legibility

The principal entries and their numbering are generally legible. The bracketed line under the first title, the sign after « cohomologique », the indexed π and the word before « infinitésimaux » have the weakest readings. The cancellations in items 15 and 18 admit partial letter-by-letter readings. In the heavily blacked-out word before « type » on scan 4, only a dot and a descender are clear. Its proposed readings remain low-confidence. The small upper-right writing on scan 2 and the bottom two lines on scan 4 leave several endings and stops unresolved.

The two sets of parallel strokes in the upper-left corners have been reproduced without assigning them an origin. The lighter slanted notes differ in ink and ductus from the numbered entries. Their author is left open. The archive corner numbers are recorded in comments. No manuscript page number was identified on these four sheets.
