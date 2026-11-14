# Notation and doubtful readings

## Notation table

| Scan and location | Strokes in the image | Transcription |
|---|---|---|
| 2, body 1 | Short form with descending p, upright b and a point | `pb.` |
| 2, body 1 | Two upright strokes on both sides of Notice | Two opening grave accents and two closing apostrophes |
| 2, body 2, third line | Upright S and L, 2 written smaller at their lower right | `\mathrm{SL}_{2}` |
| 2, dateline and signature | Point after Nov; short horizontal between initials; point after second initial | `Nov.`, `J-P.` |
| 3, list, upper corners | Small closed ovals around digits, one intersected by an oblique branch | Drawn ellipses and numerals inside the name diagram. Left digit 1 or 2. |
| 3, beside Benjamin, Rim/Swan and Harder | A baseline under Benjamin, thin four-sided outlines around two entries | Underline with `\uline`; outlines with TikZ paths. |
| 3, left side of list | Oblique fork and four open right-facing brackets. The repeated vertical strokes beside Artin are visible. | Undirected paths; endpoints and hooks retained. |
| 4, body, final stroke | Tall separate downstroke returning in a small loop at its foot | `\unsure{f\|b}`. No completion supplied. |
| 4, heading | The printed capital É carries an acute; the surname repeats the form on scan 3 | ÉTUDES; Atiyah. |
| 8, (4.38), (4.41), (4.42), line after (4.43) | Three uprights between a cap and a foot, once primed, once with a crossed superscript | A single inline TikZ sign joins both horizontal strokes to three uprights. The first sign in (4.38) and the first sign in the equality below (4.43) have a separate upper prime. |
| 8, (4.38)–(4.43) | Underlined typewritten Z, A, B; single upright Y, X, H | Underline on the individual letter. The underline under Z is separate from the diagonal of the Z. |
| 8, (4.38) and below | Hooked δ, with 0, 1 or 2 raised ticks; low y beside some δ's; short bar above the left δ in (4.43) | `\delta`, `\delta'`, `\delta''`, `\delta_y`, `\bar{\delta}_y`. |
| 8, (4.39) | Br is darker than the Br of (4.41); offset horizontal foot on B is possible | `\mathbb{B}\mathrm r` or `\mathrm{Br}` here. X is a single typewritten impression. |
| 8, (4.39)–(4.42) | Spearhead at the right. One arrow with a wavy stroke above, one especially short arrow in (4.42) | `\longrightarrow`, `\overset{\sim}{\longrightarrow}`, `\to`. |
| 8, (4.41), last paragraph | Small triangular Δ and upright divider; underlined Pic with upper 0 and lower X_y/y | `\Delta\mid\delta`; `\underline{\mathrm{Pic}}^{0}_{X_y/y}`. |
| 8, middle insertion and lower interline | Upper 3 on H, then upper 1 on H. The m in Gm is small. Upright brackets around 24. | `H^3(k(y),G_{\mathrm m})`, `[24]`, `H^1(k,G)=0`. |
| 10, first line | H with raised 3; distinct rules beneath G (not m), Q and Z. Wavy arc over a horizontal stroke | `H^3(Y,\underline G_{\mathrm m})\simeq\underline{\mathrm Q}/\underline{\mathrm Z}`. |
| 10, i display and Pic lines | Single shallow shoulder and long return stroke. Could be η or a handwritten y. It often carries a separate tilde. | `\eta` or `y`; tilde only at the positions where a wavy stroke is visible. Typed barred y has a straight rule. |
| 10, (4.8) | i has a dot and no descender. The low sign has four strong arms, compatible with × or a compressed star. The next sign has distinct rays and is raised. The single B has a rule below. | `i_{\unsure{\times\|\ast}}(i^*(P))`, `\underline B`. |
| 10, (4.9)–(4.12) | E and F are separate typed forms with individual underlines. P, Ker, Coker, Pic and Br show ordinary typewriter strokes. | `\underline E`, `\underline F`, `P`, `\operatorname{Ker}`, `\operatorname{Coker}`, `\mathrm{Pic}`, `\mathrm{Br}`. |
| 10, below (4.10) | Two quoted marks on each side of faisceaux gratte-ciel | Opening double backticks and closing double apostrophes. |
| 10, lower third | δ with 0/1/2 ticks beside typed y; bar above y in F and E subscripts | `\delta_y,\delta'_y,\delta''_y` and `\bar y`. |
| 14, (4.19), (4.24) | μ has a long left descender; ν or v has a short left leg and a taller curved right leg. The same handwritten form is used down the page. Superscripts are dotted i; lower y has a descender. | `\mu^i_y`, `{\unsure{\nu\|v}}^i_y`, `a^i_y`, `d_y`. |
| 14, cancelled (4.18) | Smaller letters réd to right of y in X; underlined round O; another X nested below O; isolated i below a row of x's after Z = | `X^i_{y\,\mathrm{réd}}`, `\underline O_{X^i_{y\,\mathrm{réd}}}`, possible `\prod_i`. |
| 14, (4.20)–(4.23) | Plain Z for the object and a different impression with a separate rule beneath Z in the sheaves. Stars beside p: low after y, or high above y. | `Z^i_y`, `\underline{\mathrm Z}_{Z_y}`, `p_{y*}`, `p_y^*`. |
| 14, (4.20), (4.23) | Two uprights descending from a single bar with open bottom. No index visible in (4.20); a small dotted i below each sign in (4.23). | `\prod`, `\prod_i`. |
| 14, (4.23) and following line | Q and Z each have their own underline. The upper 2's and 1's are on H. | `H^2`, `H^1`, `\underline{\mathrm Q}/\underline{\mathrm Z}`. |
| 14, (4.20), (4.23), final two lines | Spec, Ker, pgcd and Gal in ordinary type. A long bar across k(y), a caret above the underlined Z | `\operatorname{Spec}`, `\operatorname{Ker}`, `\operatorname{pgcd}`, `\operatorname{Gal}(\overline{k(y)}/k(y))`, handwritten caret over `\underline{\mathrm Z}`.. |
| 19, § (21.6.5) and proof | I and O have separate short rules below their baselines and plain subscripts X, U, X,x or Y(D),x. In the second Idéal de O_U, the O has a doubled contour. | `\underline I_X`, `\underline O_X`, `\underline O_{Y(D),x}`; `\mathbb O` or `O` at the doubled impression. |
| 19, first two Γ occurrences | Single vertical leg and top bar with a short, downward terminal | `\Gamma` inside the t-membership and after *dans*. |
| 19, (21.6.5.1) | Large angular sum, short stroke at upper right, low x ∈ X with raised (1); bar extends across both braces of {x} | `\sum^{\unsure{\prime}}_{x\in X^{(1)}}`, `\overline{\{x\}}`. |
| 19, proposition and proof | Wavy arrow from D to cyc(D), separate from the straight immersion arrow. D has a raised prime in the pair of divisors. Plus above Div and 1 above Z. | `\leadsto`, `\to`, `D'`, `\operatorname{Div}^{+}(X)`, `Z^1(X)`. |
| 19, prose formulas | Curved membership, slashed membership, open inclusion, cap. Solid centred or low dot for the multiplications with t and with the barred singleton. | `\in`, `\notin`, `\subset`, `\cap`, `\mathbin{.}`. |
| 19, heading, proposition and lengths | IV has an ordinary typewritten I and V. The upright word names cyc, codim, dim, long and Div show the same ink gain as the surrounding text. | Roman letters / upright operator names; the weight alone supplies no extra alphabet. |
| 19, after (21.6.5.1) and in the proposition | Both Z's have a high 1; only the first has a separate dark dot near the base of 1 | Upper 1 in both, with a doubtful low point beside the first. |

## Doubtful readings

| Scan | Approximate position | First reading | Other candidates | Confidence | Context and evidence |
|---|---|---|---|---|---|
| 2 | Body 2, first line | papier | — | medium | The ascender and dotted letter fit *papier* for the item by Milnor. The middle is compressed. |
| 2 | Body 2, third line | le fibré | les fibrés | low | Neither word has a separately visible final s. The following *qui sont plats* favours the plural. |
| 2 | Body 2, final line | très | — | medium | A short floating stroke is visible over the end of the word. The last two letters run together before *joli*. |
| 3 | Upper left beside Serre | 1 in a circle | 2 in a circle | low | A branch runs diagonally through the lower part of the numeral. The other circled 1 provides a comparison. |
| 3 | Upper right, struck label | Kleppe | Kleiman | low | An initial with a broad top bar, a loop compatible with l and a long low stroke favour a reading with p. The last letters and even the initial remain insecure. The neighbouring name supplies no completion. |
| 3 | Name 3 | Jouanolou | — | medium | An initial with a long downstroke, intervening shallow joins and a loop in the last group. |
| 3 | Name 4 | Hakim | — | medium | The dotted i is visible. The last group runs into a horizontal tail. |
| 3 | Name immediately below Coates | Jurmila | Jarmila, Jumila | low | A long initial, low undulations and a dotted i lead into a loop and a closed ending. The first vowel is open. |
| 3 | After Hirzebruch | comma | point | low | One thin isolated stroke at baseline, slightly inclined. |
| 4 | End of only body line | f | b | low | The stem ends in a small right-hand loop, with no further letters following it. The wording gives no secure next word. |
| 8 | (4.38), over second three-stemmed sign | crossed prime | star | low | Only a short raised stroke survives among several horizontal and diagonal cancellation strokes. |
| 8 | Before and after first case heading | (4.6); colon | 1 at the second site | low | Parentheses and 4 survive in the first overstrike. An independent (4.6): is clear on the raised line. |
| 8 | After Alors la, end of deletion | automatique. | automatique. La | low | The x's allow *automatiqu* to be read; the last strokes are manually crossed again. The next live word is *plus*. |
| 8 | (4.39), Br | double-impressed B followed by r | ordinary Br | medium | Its foot and the r are darker than in Br(Y); the stems do not give a clear second impression throughout. |
| 8 | (4.40), first cohomology group | X under A | B | low | A lighter crossing survives above and a leftward slash below the new A. A is the clear upper layer. |
| 8 | After (4.13) in (4.7) | et (4.16); sont | — | low | The scratch-out above the line preserves a final parenthesis and several uprights. The plural verb is covered by *est*. |
| 8 | Before on aura | et | — | low | The deleted word occupies two character positions. |
| 8 | After on aura δ = δ′ | crossed = δ″ | — | low | A cap and small right strokes are visible among oblique lines; compare the equality above. |
| 8 | (4.41), first Z | 2 beneath Z | Z | low | Its black face overlaps a curved lower stroke. The matching Z after the triangle has a single typeface outline. |
| 8 | (4.41), divisor | 1 beneath Δ | δ | low | A pale vertical survives in the triangle. The uncrossed divisibility clause gives Δ as the upper reading. |
| 8 | Before D'autre part | compte tenu de | compte tenu du | low | The p descends through the x's, the two t strokes and the d are visible. The last vowel is heavily masked. |
| 8 | End of suivant(e)s | colon | — | low | Near the cropped right edge two small dark spots adjoin the deleted ending. |
| 8 | Left of théorème | x | multiplication cross | low | Two light oblique strokes stand apart in the margin. |
| 8 | connexe | con under con | — | low | A typed rounded letter and a stem show around three darker handwritten letters. |
| 10 | After Soit | i: | — | low | Two typed positions have x's and oblique ink over them; a stem remains in the first. The next line begins i:. |
| 10 | After i: and in the Pic arguments | η | y | medium | The generic-point line favours η. The hand makes an open arch with a long descending return; (4.11) distinguishes an untilded subscript from the tilded divisor. |
| 10 | Start of Pic display, below correction | Pic( | — | medium | The capital, bowls and left parenthesis are visible through x's. |
| 10 | Before Compte tenu | Lorsque | — | medium | A capital L and the descender of q survive. The new sentence starts with a capital. |
| 10 | (4.11), far left | underlined E with low barred y | underlined F with low barred y | low | Typewritten x's and diagonal strokes cross the horizontal bars on the capital. |
| 10 | (4.11), by bar of live F | asterisk | — | low | A small mass of ink with short points has been overwritten immediately to the right of the bar. |
| 10 | (4.12), after barred y | δ with low y | y | low | A rounded upper remnant and a descending stroke remain in a hatched patch. |
| 10 | Inside caractéristique | tc beneath ct | — | low | A stem protrudes above the corrected c and a curve beside the corrected t. |
| 10 | After déjà | sig | — | low | A small dot and the final g descender survive the three overtyped x's. |
| 10 | Above est nul également | également | — | medium | Repeated word partly visible through x's. The new copy below has a clear acute on é. |
| 10 | Right edge, admet un… | e | — | low | A dark curved edge remains after un against the black edge of the sheet. *section* on the next line favours *une*. |
| 10 | (4.8), immediately below the first i | four-armed cross × | star ∗ | medium | The two strongest lines cross obliquely. A weak central thickening also permits a star. The paired raised star has more arms. |
| 10 | (4.11), underneath the handwritten y | y | — | low | Two darker crossing diagonals of a fork remain below the bar. The descending loop belongs to the upper hand. |
| 14 | Left of respectivement | x | multiplication cross | low | Short diagonal strokes, like the marginal mark on 8. |
| 14 | End of first paragraph, parfait | a below f | — | medium | A faint bowl extends to the left of the f. |
| 14 | Cancelled (4.18), after Z = | product with lower i | — | low | The index survives. Several x impressions obscure the baseline sign; the live definition below has a product. |
| 14 | (4.20), subscript of second Z | x beneath y | i | low | Two strokes overlap the printed y. |
| 14 | (4.20), last punctuation | semicolon over comma | period for live mark | low | An upper patch and a lower descending stroke survive. The upper patch carries most of the overwriting. |
| 14 | (4.22), last nested subscript | deleted y | — | medium | A returning curved stroke survives below the hatch, at the next subscript depth. |
| 14 | (4.23), before each Ker | Co | — | low | The same two letter spaces are crossed out on both lines. A short curve survives at the right. |
| 14 | (4.23), lower product | cancelled original arrow tip | — | medium | A horizontal line enters the product frame and ends in a dark reworked tip. A second head is visible to the left. |
| 14 | transition | o under n; i under s | — | low | A bottom loop crosses the n; small typed traces remain beneath the s. |
| 14 | Under et qu'un tel noyau | dont chacun | — | medium | Eleven positions with a gap and a high h are visible among the x's. |
| 14 | Before comma after ν | e | — | low | A small typed outline survives under dark cancellation. |
| 14 | (4.24), end | cancelled semicolon | — | low | A short oblique stroke crosses the punctuation; its low dot remains distinct. |
| 14 | Last word | o under r | — | low | Two overlapping forms occur between t and the undisturbed o of *trouve*. |
| 14 | Second symbol in (4.19), also after degré and in the lower products | ν | v | medium | Two legs meet below the baseline centre of the glyph, the right leg turns outward high up. It is paired with µ. The handwriting permits either alphabet for this shape. |
| 14 | Below the second multiplicité | semicolon-shaped mark | comma-shaped mark | low | A separate dot over a short tail is visible below the later i, just before c. It does not strike through a letter. |
| 14 | Just left and above (4.20) | short sloping dash | waved stroke | low | A fine oblique stroke intersects a heavier short line beside the opening parenthesis. No letters can be separated. |
| 19 | First positive divisor | short prime after D | — | low | A faint high stroke stands immediately to the right of D; the other occurrences in this sentence print D alone. |
| 19 | Raised étant | n underneath the t | — | low | A small arch survives in the touched group. The whole word reads *étant*. |
| 19 | After définit and after car | Cela signifie / cela signifie, then qu at the next start | — | low | Both cancellations span the same number of positions and show the same low loop near the right; the next cancellations each occupy two positions. |
| 19 | Before il y a par hypothèse | que, | — | low | Four covered typed positions, and a short descending stroke near the end. |
| 19 | Left of bracketed passage | devrait; figurer; (sans hyp. noeth.) | passer for figurer | low | Read after rotation. First word ends in *ait*. Next has a long first descender and several collapsed middle strokes; *dans 21.2.* is clear. The last line has a tall th-group before the point. |
| 19 | Before de codimension | est | — | low | Three overtyped positions with oblique cancellation; the middle and last letters are largely covered. |
| 19 | After un seul | préschéma | positif | low | About seven type positions, with a stroke descending near the right. *positif* repeats the preceding description. Neither word can be recovered in full. |
| 19 | Idéal de O_U | double-struck O | plain O | medium | A second vertical is visible inside the loop, unlike the next O_U. The surrounding notation favours ordinary underlined O. |
| 19 | End of régulier | re underneath er | — | low | Dark joining strokes overwrite both last positions; the visible upper reading is *er*. |
| 19 | Beside réf !, after semicolon | two unread words, possible partie, one unread word | — | low | A descender and isolated bowls survive near the middle. Several layers of x's and diagonal ink cover the rest. |
| 19 | Second occurrence of points in Puisque | g under n | — | medium | A small closed loop descends below the baseline under the n. |
| 19 | Top right of sum | prime | — | low | A short sloping stroke and the turned ends of the summation bars are close. |
| 19 | After cyc(D) in proposition | crossed semicolon | — | low | At and just below the closing parenthesis a small second cluster is visible. |
| 19 | After mais puisque | x | — | low | The single crossed position has a short diagonal remnant. |
| 19 | Before aussitôt la proposition | résulte | — | low | A single heavily crossed group shows isolated small openings, with very little surviving letter shape. The following clause favours *résulte*. No second word can be distinguished here. |
| 19 | Below (21.6.5.1), Z¹(X) | small point beside Z below upper 1 | — | low | A separate black dot is visible low between Z and 1. The second Z¹(X), in the proposition, has no such dot. Its status as punctuation is uncertain. |

## Slips and corrected forms kept as written

The middle column gives the source wording or the visible layers. For crossed words, the next column gives the replacement on the sheet when one is legible. Suggested expansions of shortened words are confined to the next section.

| Scan | Approximate line | As written | Apparently intended | Why |
|---|---|---|---|---|
| 2 | Second paragraph, before SL₂ | le fibré … qui sont plats | les fibrés … qui sont plats | The plural verb and adjective suggest the plural noun. The ends of both handwritten words remain doubtful. |
| 8 | First case, before plus grande partie | la [relation (4.13) est automatiqu…] plus grande partie | la plus grande partie | The x's remove a different start to the sentence. The later complete sentence repeats La relation (4.13). |
| 8 | Before l’on a ici nécessairement | que [dans] l’on a | que l’on a | The abandoned preposition is still visible under x's. |
| 8 | Finite-field case, after (4.13) | [et (4.16)] [sont] est | est | A singular verb survives below the crossed raised clause. (4.16) reappears in the handwritten insertion. |
| 8 | Before (4.43) and in its last paragraph | de[s] [la] relation[s] suivante[s]; de[s] [l’]égalité[s]; laissé[e] | de la relation suivante; de l’égalité; laissée | The pen cancels plural endings, supplies articles and adds the final e. The earlier letters remain in the transcription. |
| 10 | After (4.10) | lorsqu’on connait | connaît | The typed i has a dot. No circumflex is visible. |
| 10 | Same paragraph | Leur[s] fibre[s] … les noyaux et conoyau | Leurs fibres … les noyaux et conoyaux; the intended number of the last noun is uncertain | The pen supplies two s's. The second mathematical noun has no x and has no article of its own. |
| 10 | Twice, before the displayed Pic map and after it | au dessus | au-dessus | The source has a space in both places. The hyphen in the nearby sous-groupe is visible. |
| 10 | Lower third | cara[tc]ctéristique | caractéristique | The overwritten two-letter order is doubtful. The dark upper reading is ct. |
| 10 | Before the three indexed δ's | parfait, Désignant par | parfait. Désignant par | The mark after parfait descends like a comma; the next word has a capital D. |
| 10 | Before the last example | est nul également, overtyped above est nul également | est nul également | The repeated lower copy survives. |
| 14 | First line of prose | second multiplicité with a small mark beneath the later i | multiplicité | A separate low dot and tail do not belong to the dotted i above. |
| 14 | Old (4.18) and the sentence immediately after its cancellation | de sorte que l’on a simplement … est le spectre …; la plus petite extension … de k(y) tel que | First wording abandoned; possibly telle que in the surviving sentence | The x run and pen enclosure cover the old wording. The surviving tel is aligned with de k(y) and is retained. |
| 14 | Two successive lines of (4.23) | [Co]Ker … [Co]Ker | Ker in both places | The typescript retains two crossed positions before each Ker. Their earlier letters are uncertain. |
| 14 | After the two-line display | tra[o]n[i]sition | transition | The n shares a rounded lower stroke with a former letter, and the following s has another impression under it. |
| 14 | Last two lines | i.e. son groupe fondamental … isomorphe à … | possibly son groupe fondamental … est isomorphe à … | No verb appears between the group and isomorphe. |
| 19 | First clause | D with a faint high stroke | possibly bare D | The subsequent ideal and closed subscheme in the same sentence have D without a visible prime. |
| 19 | After codim; proof using long | = at the end of one line and = at the beginning of the next; + at the end of one line and + at the beginning of the next | one equality sign or addition sign at the respective line turn | Both marks are present in each case. |
| 19 | End of the long bracketed passage | réguli[re]er | régulier | The last two letters are overwritten; re as the earlier state is uncertain. |
| 19 | After anneau artinien | poi[g]nts | points | A small loop descends under the upper n. |
| 19 | Line below (21.6.5.1) | Z with upper 1 and an additional low spot | Z¹ | The low spot is absent from the second Z¹ in the proposition. |

## Abbreviations and shortened names

| Form | Scan | Probable expansion or meaning |
|---|---|---|
| Nov. | 2 | novembre |
| pb. | 2 | problème |
| J-P. | 2 | Jean-Pierre |
| SL | 2 | special linear; groupe spécial linéaire |
| i.e. | 8, 14 | id est |
| bis | 8 | The Latin numbering suffix indicating the second item with that number. |
| Br | 8, 10 | Brauer; groupe de Brauer |
| Pic | 8, 10 | Picard; the Picard object named or used on the line |
| G with lower m | 8, 10 | groupe multiplicatif |
| Ker | 10, 14 | kernel; noyau |
| Coker | 10 | cokernel; conoyau |
| EGA | 14 | Éléments de géométrie algébrique; IV is the Roman numeral in the citation |
| réd | 14 | réduit; the qualifier occurs inside the crossed-out formula |
| Spec | 14 | spectre |
| pgcd | 14 | plus grand commun diviseur |
| Gal | 14 | Galois; groupe de Galois |
| réf | 19 | référence |
| hyp. | 19 | hypothèse or hypothèses |
| noeth. | 19 | noethérienne or noethériennes in the marginal parenthesis |
| codim, dim | 19 | codimension, dimension |
| cyc | 19 | cycle; the expression associated with D in (21.6.5.1) |
| long | 19 | longueur |
| Div | 19 | diviseurs; the positive superscript appears in the proposition |

## Legibility and attribution

Serre’s letter is legible throughout, with a few very short word endings. The crossed name at the upper right of scan 3 and the unfinished letter on scan 4 admit more than one reading. On the mathematical typescripts, small detached strokes, earlier characters beneath x's, and the verb in the long oblique note on scan 19 are the least secure. In the long crossing after the dimension formula on scan 19, only a possible middle word can be offered. The two surrounding word counts are estimates.

The printed letterheads and typed base text have separate inventory rows from the handwriting. The date and letter on scan 2 are assigned to Serre’s hand. The writer of scans 3 and 4 cannot be identified from a signature there. Scan 19 is classified as reused typed material from its running chapter and page number and its extensive marginal revision. That sheet classification and the assignment of the marginal hand are editorial judgments.
