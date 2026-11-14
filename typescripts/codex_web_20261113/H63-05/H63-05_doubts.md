# H63-05 · Readings and doubts

## Notation table

Positions refer to lines of the original sheets, identified by their opening words or formula numbers. The same symbol was checked again wherever its position, lettering or ink changed.

| Scan and place inspected | What is visible | LaTeX reading |
|---|---|---|
| 041, top right and title; 042–048, top | Lower-case running name “atkin”, page digit alongside. It is partly covered on 043. A replacement number follows the crossed digit on 046 and 047. The separate lower-left pencil series is 40 through 47. | `\mspage{1}` through `\mspage{8}`; lower numbers only in archive-number comments |
| 041, title, byline, affiliation | Typewriter caps have small gaps and heavier blobs on individual strokes. The baseline star on ATKIN corresponds to the baseline star before “Research”. The pencil date has parentheses. | `CONGRUENCES FOR MODULAR FORMS`; `A.O.L.ATKIN*`; `\handwritten{(1968)}` |
| 041 “logical”; 044 “Ramanujan-type”, “accident”; 046 “accident”; 048 “accidents”, “13”, “the same again” | Pairs of upright quote strokes. The single strokes in “computer's”, “hours'”, “O'Brien” and “Glaisher's” are distinguished. | Two opening backticks and two closing apostrophes; a single apostrophe where it is single on the page |
| 041 “a priori”; 042 subsection heading; 043 “idea”; 044 “Congruences for”; 045 “identical”; 046 “not”; 047 “Let”/“Then if”; 048 “The cases”/“general” | Single irregular underlines. The two halves of “a priori” span a line end. Several adjacent words have separate strokes. Where an additional line crosses letters it is also recorded as a deletion. | `\uline{...}`; separate macros where the strokes are separate |
| 042 “theory§provided” and section heading; 043 “proprty”; 047 “comgruence” and “show … by”; 048 left margin | Paragraph correction signs have an accompanying slash, loop or caret. The § after “theory” has two connected curves. The loops in the margins can resemble § or δ. | `\S`, `\inserted`, `\margin`; doubtful marginal loops have the local readings listed below |
| 042 (2.2), first and third lines; 043 (2.4) and transformation; 044 first note; 045 opening and unnumbered series | The cap of τ has a shallow wave. In the independent samples on 043 and 045 the descending stroke begins distinctly below the cap. In the occurrences on 042 and 044 the two strokes nearly or actually meet. The same written letter is used in an argument and as a coefficient name. | `\tau`; the long-stemmed η of `\eta(\tau)` on 042 has a different outline |
| 042 (2.2), first and third lines; 044 first note | π has a horizontal top. The following i has a dot; it precedes τ in the pen exponent. The upright I of Im has single stems and top/bottom bars. | `2\pi i\tau`, `\pi i\tau/12`, `\mathrm{Im}` |
| 042 (2.1), pen sentence; 043 (2.3), two lines; 043 (2.5), two lines | a, b, c, d, e occupy superscript positions. In (2.3) only the right-hand 7 has Greek β. The definition encloses a round pair and a literal slash in square brackets. The final powers in (2.5) continue on the next line. | `5^{a}7^{b}11^{c}`, `5^{a}7^{\beta}11^{c}`, `\beta=[(b+2)/2]`, `2^{3a+8}3^{2b+3}`, `5^{c+1}7^{d}11^{e}` |
| 042 (2.2); 043 series, footnote and transformation; 045 series and recurrence | f has a cross stroke and a low loop. j has a dot and a descender. The 24 on f precedes (x). In the divisor sum, σ has a low 3, while the final d has a raised 3. The divider between d and n is vertical. | `f(x)`, `j(\tau)`, `f^{24}(x)`, `\sigma_{3}(n)`, `\sum_{d\mid n}d^{3}` |
| 042 “coefficient c(n)”; 043 (2.4); 044 (3.1); 046 (3.7); 047 (3.11) | The handwritten coefficient has one open curve, sometimes higher than the neighbouring n. The short and tall specimens share this shape. The typewriter c in the adjacent prose has a short body. | First handwritten occurrence on the four affected sheets `\unsure{c\|C}`, with the alternatives separated by a literal vertical bar in the TeX files. Other occurrences use c. |
| 042 (2.2); 043 (2.4); 045 unnumbered series; 048 top | Bounds above and below Σ or the product sign are vertically aligned. The lower summation bounds on 042, 043, 045 differ. No arrow replaces a bar or vertical bound. | `\sum_{n=0}^{\infty}`, `\sum_{n=-1}^{\infty}`, `\sum_{n=1}^{\infty}`, `\prod_{i=1}^{\alpha}` |
| 042 (2.1), (2.2); 043 (2.4), transformation; 044 (3.2); 045 (3.5); 046 after “since”; 047 ratio in (3.9) | Leader dots before some labels; three visible continuation dots in the product expansion; a long slash on the line in (2.4); stacked numerator/denominator in the transformation. n/p has an ordinary inline slash. | `\ldots`, `\big/`, `\frac{a\tau+b}{c\tau+d}`, `t(n/p)`, `\tau(n/p)` |
| 043 (2.5), right edge/next line | Small left-pointing angle with a weak curved tail; matching right-pointing angle at the resumption. | `<` or `\hookleftarrow`; `>` or `\hookrightarrow`. Both are marked at their respective positions. |
| 042 (2.1); 043 (2.3); 044 (3.1)–(3.4); 045 (3.5); 046 (3.7) and bounds; 047 (3.8)–(3.11); 048 opening and final line | Congruence has three horizontal strokes. Equality has two. In 047 (3.10) the lowest of the three is a hand stroke below a typed equals. The direction of each inequality is retained. The slash of ≠ rises to the right. | `\equiv`, `=`, `<`, `>`, `\leq`, `\geq`, `\ne`; the mixed (3.10) sign is overlaid in place |
| 044, computed “accident” and (3.3); 046 in the two coefficient products; 047 first and last lines | Low multiplicative point, sometimes very small or hollow. It is distinct in position from the decimal point in “1.4” on 046. | `\mathbin{.}` or the decimal point in `1.4` |
| 044 (3.2); 045 (3.5) and discussion; 047 “natural power” and (3.9) | Two upper digit strokes on p in the earlier recurrence. In the later recurrence the exponent has a short minus before one digit. The argument below remains n/p. | `p^{11}`; `p^{-1}` |
| 046 (3.7), product after “of the form”, and underlined coefficients | k has lower α; the 13’s in the result have lifted α+1 or α. Both handwritten i’s are dotted, the second below a b that is itself in the exponent. Each of the two subsequent typed i’s is below its coefficient. Tiny round n-subscript in the accident line permits 0 or o. | `k_{\alpha}`, `13^{\alpha+1}`, `a_i\mathbin{.}13^{b_i}`, `a_i`, `b_i`, first `n_{\unsure{0\|o}}` |
| 046 “output of the form” and “since 40960/…” | Three cells in one row, with broad blank spacing. Comparison after the division has a single hump above a straight lower line. The undulating line after b(7)= reaches into the blank right area. | `\begin{array}{ccc}` inside `\diagram`; `\bumpeq`; an inline TikZ drawing inside `\figure` |
| 047 “there exists some” and (3.11); 048 opening product | θ has an oval and a crossing stroke. α has an open, slanting tail. The capital P in (3.11) has one high bowl and long shaft. On 048 a typed upright P precedes a product of lower-case p’s. The two lower i’s on p and θ have separate dots, as does the i under the product. | `\theta`, `\alpha`, `P`, `\mathrm{P}`, `p_i^{\theta_i}`. No j appears in these positions. |
| 043–048, handwritten references; compare 046 “Newman's”, “at this stage proved”, “still obtained”; 047 “agrees with” and final label | Some internal points are round; two show a distinct lower hook on 046. In the last label on 047 the ink falls in two separated low positions. | Literal full stop or comma, or marked alternatives at the local read; (3,7) after “still obtained” |
| 041 title; 042 section 2 and names; 043 author names; 044 section 3 and F; 045 names; 046 note/table; 047 M/R/P; 048 section 4, ATKIN and P | Each capital was inspected locally. No offset second stem could be isolated in the headings or mathematical names. Superposed distinct glyphs in “values”, “in future” and altered subsection digits have separate readings. No independent script-capital or blackboard-alphabet example could be identified. | Ordinary capitals; earlier and later layers kept with `\deleted` and handwritten markup where appropriate |

## Doubtful readings

The line locators are the nearest words or display labels. “Extraneous ink” means a spot is visible but could have arisen in typing or copying. For those spots the mark transcribes its apparent punctuation value. Confidence concerns the first reading.

| Scan | Approximate line or position | First reading | Other reading(s) allowed by the ink | Confidence | Evidence from surrounding text |
|---|---|---|---|---|---|
| 041 | Upper right, beside “atkin 1” | One unreadable inscription, traced in TikZ | Interlocking strokes could be initials or a nonverbal flourish; no secure letters | low | The author’s name is typed independently in the centre and gives no secure expansion of this mark. |
| 041 | “certainly the …cases” | Low point | Extraneous ink | low | Continuous prose favours “the cases”; the point is visibly separate from c. |
| 042 | Right of “modular theory”, above “(comma)” | § crossed by a short diagonal | δ-like loop with diagonal | medium | The corresponding in-text § and the explicit comma beside the sign favour a proofreader’s matching cue. |
| 043 | Running head, at the tab | Weak a, a covered word-part, then n | The presumed a could be the edge of the tab | low | The other heads read “atkin”. The missing letters are covered. The last n and the numeral 3 survive. |
| 043 | “the modular nature o…” | Old n under the new f | Old f | low | The phrase supports the surviving “of”; it cannot establish the earlier letter. |
| 043 | (2.4), first series coefficient | c | C | medium | The preceding typed “properties of c(n)” favours lower case. |
| 043 | (2.5), after 3 raised to 2b+3 | Left-pointing angle | Curved left-return arrow | medium | Its partner on the next line suggests a continuation cue. The faint tail is fragmented. |
| 043 | (2.5), before 5 raised to c+1 | Right-pointing angle | Rightward return arrow | medium | The pair brackets the same line break; no continuous connecting shaft survives. |
| 044 | “the latter an example” | Point after example | Extraneous ink | low | “example of the most difficult type of case” continues across the line break. |
| 044 | (3.1), initial coefficient | c | C | medium | Repeated typed c(n) and the coefficient at the right favour c. |
| 045 | “his own table of …alues”, earlier layer | e | c | low | A curved bowl shows under the correcting strokes. “values” identifies the final reading only. |
| 045 | Same cell, replacement | v | V | medium | Its size is intermediate; the lower-case word in mid-sentence favours v. |
| 046 | First digit, heading “3.2.” | Old 2 | Old 3 | low | Final 3 is clear. The matching note repeats the two layers. |
| 046 | First digit, “§3.2” in footnote | Old 2 | Old 3 | low | The printed stem and baseline are partly masked by the new 3. |
| 046 | “Newman's (3,1)” | Comma | Full stop | medium | The corresponding equation on 044 bears (3.1). The present mark has a short lower hook. |
| 046 | (3.7), “not … by 13” | diisible | divisible | low | Two narrow dotted forms precede s, with no separate v leg. The wording “by 13” favours “divisible”. |
| 046 | (3.7), initial coefficient | c | C | medium | The same function is repeatedly typed with lower-case c below. |
| 046 | “our subsequent proof of (3.7)”, earlier digit | 2 | 6 | low | A loop and lower extension remain behind the replacement 3. The reference identifies its final digit. |
| 046 | “one of us used …some” | High apostrophe-like tick | Extraneous ink | low | The phrase reads continuously without a quotation around “some”. |
| 046 | “accident of the form”, low circle on n, twice | 0 | o | medium | The same subscript recurs; the first impression is a closed oval with no distinguishing serif. Context does not choose a shape. |
| 047 | (3.9), numerator closing parenthesis | Earlier horizontal dash | Earlier equals | low | A transverse bar survives inside the thick parenthesis; the upper edge is broken. |
| 047 | (3.9), denominator closing parenthesis | Earlier horizontal dash | Earlier equals | low | A short bar survives through the lower part of the parenthesis. |
| 047 | (3.9), after the modulus | Slashed 8 | Slashed β | medium | The corresponding right-margin 8 favours the first reading. |
| 047 | “agrees with (3,2)” | Comma | Full stop | medium | The earlier reference in this paragraph and the equation on 044 have a stop; this mark tails to the right. |
| 047 | To the right of the label (3.10) | Faint full stop | Extraneous ink | low | There are two tiny dark fragments after the closing parenthesis. |
| 047 | Before “n future”, earlier letter | m | n | low | The surviving i gives “in future”, but masks the number of stems in the first impression. |
| 047 | “we have for …ny” | a | Unreadable beginning of the letter | medium | The surviving trace is at the foot of a letter; “any” fits the two following letters and the phrase. |
| 047 | (3.11), first letter | c | C | medium | The typed c(13.p raised to θ) directly above favours c. |
| 047 | Last equation label, between 3 and 11 | Two low points | One broken or smeared point | low | Nearby labels favour a single separator; the two marks remain distinct on this sheet. |
| 048 | Immediately after crossed “for” | Faint full stop | Extraneous ink | low | The following clause begins “but without it”; the point sits to the right of the ruled word. |
| 048 | Left beside “for all”; again beside “obtaining” | δ-like deletion sign and oblique stroke | §-like sign and stroke | medium | Crossed words at both levels suggest matching cancellation cues. Beside “for all” the strokes overlap; beside “obtaining” they stand apart. |
| 048 | At end of the crossed “for all” | α retained outside the cancelled words | Deletion intended to include α | medium | The strike reaches the left tip of α; its body lies beyond both rules. Sentence sense favours extending the deletion. |
| 048 | Section number 4, earlier layer | 1 | 4 | low | The visible replacement is 4; the projecting stroke at the top could also be a retracing of 4. |
| 048 | Before “R-results”, heavily crossed group | p) | p with a terminal crossing stroke | low | “with a view to obtaining” continues directly into “R-results”. It does not recover the cancelled group. |
| 048 | After final q>13 | Comma | Full stop | medium | The mark slopes upward right; the sentence ending favours a full stop. |

## Slips and unfinished entries kept as written

| Scan | Line or position | As written | Apparently intended | Basis |
|---|---|---|---|---|
| 041 | “Science … Council” | Reserach | Research | The r follows the e in “Reserach”; the affiliation above spells “Research”. |
| 042 | Heading 2 | Slashed C in Congruences | Possibly lower-case c | A diagonal crosses only C, with a matching margin slash; no second c is legible. |
| 042 | At the η line in (2.2) | Typed “we have” struck through | “we have” on the next line | It is written again by hand to the left of the sum. |
| 042 | At the exception footnote | Cancelled “as his proofs” | Continue after the note | “as his proofs of some particular cases show.” reappears below the rule. |
| 043 | “of such a …” | proprty | property | A separately underlined e is supplied from the left margin between the second p and r. |
| 043 | “can often … important clues” | provied | provide | The transpose mark steps between e and d. |
| 044 | “with similar …” | porperties | properties | A transpose mark joins o and r. |
| 045 | “Now … the identical relation” | staisfies | satisfies | The step mark joins t and a. |
| 045 | “table of …alues” | Curved earlier letter, overwritten with v/V | values | The pen correction and the unchanged ending give this word. |
| 045 | Last reference | RANKIN(196  ) | Year with its final digit unspecified | Space remains before the parenthesis; the page supplies no fourth digit. |
| 046 | Heading and first note | Overwritten digit in 3.2 | 3.2 | The same visible correction appears in heading and note. |
| 046 | (3.7), condition on k | diisible (doubtful) | divisible | The word is followed on the next line by “by 13”. |
| 046 | After “still obtained” | (3,7) | (3.7) | Most references to the displayed result use a full stop; this pen separator has a comma hook. |
| 046–047 | End of sheet 6, start of sheet 7 | b(7)= followed on the next sheet by =b(11)=1 | A relation carried across the break | There is an equals sign on each page and a drawn continuation stroke beside the first one. |
| 047 | “This … I tested” | conjecutre | conjecture | The step transposes u and t. |
| 047 | “We shall … future” | i over an earlier m/n | in future | The n after the overwritten cell survives. |
| 047 | “multiplicative … properties” | comgruence, m slashed | congruence | The corresponding margin supplies n. |
| 048 | “becomes unnecessary” | Crossed “for” | Remove “for” | The next line continues “but without it”. |
| 048 | “is proved” | Crossed “for all”, α still visible | Possibly remove the whole addition | The strokes end against α; the left margin carries a matching pen mark. |

## Abbreviations

| Form on sheet | Scan and use | Probable sense |
|---|---|---|
| A.O.L. | 041, author line | The author’s three initials. The pages give the surname ATKIN and do not spell out these names. |
| ICT | 041, “ICT Atlas 1 computer” | Name or initials attached to the Atlas 1 computer. The words behind the initials are not supplied here. |
| Dr. | 041–042, before J.Howlett and R.F.Churchhouse | Doctor |
| Mr. | 042, before E.B.Fossey | Mister |
| J., R.F., E.B. | 041–042, acknowledgements | Personal initials. The pages supply the surnames, without full given names. |
| Hartran(Fortran) | 042, first paragraph | Names of the programming system/language given together on the sheet; no expansion supplied. |
| mod | 042–048, in congruences | Modulo |
| Im | 042, first line of (2.2) | Imaginary part |
| § | 044 and 046, numerical references | Section; the similar sign by “theory” on 042 has a correction function. |
| i.e. | 045, after “multiplicative” | That is |
| M-, M-result(s) | 047–048 | Multiplicative, from the definition on 047 |
| R-, R-result(s) | 047–048 | Ramified, from the definition on 047 |

## Legibility

Most of the typewriting and the complete displayed lines remain legible. The difficulties cluster in overwritten cells, punctuation at the foot of a typed or penned glyph, the tiny round subscripts on 046, and the handwritten cancellations. The top-right inscription on 041 and the material hidden by the tab on 043 are the two physically unreadable portions. The hand that filled the mathematical blanks and the hands that made the pencil and proof marks cannot be identified from these sheets. The inventory uses “unknown” for those elements.