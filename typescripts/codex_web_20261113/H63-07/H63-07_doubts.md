# Readings and doubts · H63-07

## Notation

| Scan and position | Reading from the strokes | LaTeX |
| --- | --- | --- |
| 57, opening and references | Straight strokes under words and operands; wavy strokes under parenthesized references. The pen-only wrapper on an underline command applies to the stroke; its following argument keeps its own provenance. | `\handwritten{\uline}{...}, \handwritten{\underline}{...}, \handwritten{\uwave}{...}` |
| 57, title and byline | Individually struck roman capitals including the H of HECKE and the O of OPERATORS. | `literal upper case` |
| 57, “-adic” line | The looped, descending hand-drawn letter has a marginal spelling-out, “German ‘pee’”. The roman-type p in p(n) has a different outline. | `\mathfrak{p}; p(n)` |
| 57, subgroup | Tall right-angled capital and lowered ring. | `\Gamma_{0}` |
| 57, prose and margin | Pairs of typewritten quotation marks and single pen quotes. | `two opening and two closing quote characters; single quotes for ‘pee’` |
| 57, four displays | Three independent horizontal strokes, round parentheses, baseline mod and a number. | `\equiv, (\mathrm{mod}\ 5)` |
| 57, functions paragraph | Typed dotted abbreviation, comma immediately following. | `i.e.,` |
| 58, transformation | A very short horizontal mark with a thickened right end after z. | `\unsure{\rightarrow\|-}` |
| 58, opening and M1/M2 | Greek capital gamma in pen. Typed F, V, D, I, B, H, C and FS show single type faces. | `\Gamma, F,V,D,I,B,H,C, \mathrm{FS}` |
| 58, exponential | A handwritten pi with two legs; local-variable base is x and the exponent contains a dotted baseline i. | `e^{2\pi iz}` |
| 58, M1 | Membership has a middle stroke, opens to the right. | `\in` |
| 58, vector spaces | A raised heavy cross and a raised closed round zero over separately underlined C. | `C^{+}, C^{0}` |
| 58, Fourier expansion | Large pen sigma, top infinity, bottom n=N. Small sideways two-loop end sign recurs in z=i∞ and N>-∞. | `\sum_{n=N}^{\infty}, \infty` |
| 58, above the last paragraph | Two capital type letters, inside parentheses. | `(FS)` |
| 58, two margins | Looped deletion sign; leader to the struck punctuation or word. The sign and its leader are drawn in TikZ. | `marginal pen path` |
| 59, opening and H1–H4 | The operator has a typed capital T with lowered p (m later); separate F, G and C have the single type face. The first F is redrawn. In the heading Theorem the T has ordinary typewriter serifs. | `T_p,T_m,F,G,C` |
| 59, first two displays | Pen lambda parameter, pointed entry and two sloping legs; underlined. Shallow looped p in limit and denominator. Pen braces in Fourier formula. | `\lambda, p, \sum, \Bigl\{...\Bigr\}` |
| 59, after second display | Closed loop with oblique right stroke; “alpha” is in the margin. | `\alpha` |
| 59, scalar product | Two integral signs above one D; an overbar spans G(z). Loop-and-tail eta and three-turn xi occur with underlines, one dot over i in z. | `\iint_D,\overline{G(z)},\eta^{-k-2},d\xi\,d\eta,\xi+i\eta` |
| 59, theorem | Lowered i has a dot and ends on the line; n is raised on x. Separate asterisk at the right of eigenforms and against its note. | `F_i(z), x^n, *` |
| 59, headings H1–H4 | Each H has ordinary typed serifs; fine missing segments in the strike also occur in surrounding text. | `(H1), (H2), (H3), (H4)` |
| 59, final label | A dark point and faint lateral traces after H3. The reference printed on scan 64 reads (H3*). | `(H3\unsure{*\|$\cdot$})` |
| 60, nullity line | Two right-slanting limbs over a sloping lower bar. | `\geqslant` |
| 60, Hauptmodul | Typed descender and separate dot on the baseline j. No subscript on j. | `j(z)` |
| 60, product quotient | A complete numerator in braces, raised 3, a diagonal slash, x followed by capital product with limits r=1 and infinity. Sigma has a horizontal right stroke and a small lowered 3. | `\sigma_3(n), \prod_{r=1}^{\infty}, \Bigm/` |
| 60, quotient ring | Each of the two Zs has one diagonal between two short horizontal caps. Solid pen underline below the expression; alpha above q also has its own sloping underline. | `Z/q^{\alpha}Z` |
| 60, last line | Very faint type body resembles a; surrounding exponents have a right stroke characteristic of alpha. | `\unsure{a\|\alpha}` |
| 60, ring and following α | The small Greek bowl, diagonal, and base match the type of α on 59 and 63. The separate thick underline is in pen. | `\alpha,\handwritten{\underline}{\alpha}` |
| 60, below “pole gives” | A faint slant with a small upturned loop, between two typed lines. | `\tikz ... \draw` |
| 61, first line and after congruence pair | Less-than wedge with a nearly sloping lower bar; reverse direction at 37. | `\leqslant, \geqslant` |
| 61, improved modulus and (3) | Oval with crossbar theta; small two-bowled beta; slopes directly beneath Greek letters are underlines. There are two separate verticals between q^β and c(q^α). | `\theta,\beta,\alpha,\parallel` |
| 61, second conjecture | Two underlined λ in the displayed combination. The second is barred. The conjugates line below has separate bars over λ and a(n). | `\lambda a(n)+\bar{\lambda}\overline{a(n)}; \bar{\lambda},\overline{a(n)}` |
| 61, margins | Four crossing lines at the end of each conjecture, matching the symbol after (1) on 59. | `\#` |
| 61, last two lines | First tiny bar has a thickened right end like 58. | `\unsure{\rightarrow\|-}` |
| 61, Conjecture 2, first display | An isolated short rule directly above the second λ is separated from the continuous underline on “positive integers”. Another rule is under λ. Both copies of the conjugate in the following line have bars. | `\underline{\bar{\lambda}},\overline{a(n)}` |
| 62, section title | A single ordinary type face on the initial T; the following gamma and small round subscript are drawn. The text has separated ruled words. | `\handwritten{\Gamma}_{\handwritten{0}}` |
| 62, operator definition | Pen capital sigma with upper q−1 and lower λ=0; second sigma has just n below. Upright handwritten F takes a parenthesized fraction. | `\sum_{\lambda=0}^{q-1}F\left(\frac{z+\lambda}{q}\right),\ \sum_n` |
| 62, H1q to H4q | Open single-face C with a raised round 0. H in each tag has two uprights and one crossbar; in H2q the T and descending p have been redrawn, with faint type beneath. | `C^0,T_p,U_q` |
| 62, Theorem 2 | The top of the heading T is single; two occurrences of F with a low dotted i, without a lower hook. | `F_i(z)` |
| 62, final relations | A slant crosses two horizontals between p and q; two slants and two crossbars at the right of the second line. | `\ne,\ \handwritten{\#}` |
| 62, last paragraph | Raised minus k, diagonal slash and 2, then minus 1 on the same upper level. | `q^{-k/2\,-1}` |
| 63, conjecture heading | Single impression in initial C. Typed lowercase α and β have uniform bowls; straight pen strokes below them are distinct from the bowls. The drawn Γ has two limbs. | `\alpha,\beta,\Gamma_0` |
| 63, first display and (i)–(iv) | The congruence sign has three parallel strokes. Each right-hand modulus is in round parentheses, with upright mod before q and a raised α. | `\equiv,\ (\mathrm{mod}\ q^{\alpha})` |
| 63, fourth display | The pen k has one high shaft and a bowed cross limb. The following plus sign is also penned. The final typed argument is z. Low comma immediately follows αβ. | `\handwritten{k+}k_{\alpha\beta,}F_\alpha(z)` |
| 63, last line and opening | Left point above a separate slant for the upper bound 23; reverse point in the lower bound on α. | `\leqslant,\geqslant` |
| 64, hypothesis references | H is typed with ordinary serifs, followed by 3, optional q and an asterisk level with the upper part of 3. | `(H3q*), (H3*)` |
| 64, References | The initial R has one bowl and a diagonal leg. The straight line under the heading differs from the waves under volume numbers. | `\uline{References}, \uwave{126}` |
| 64, items 5 and 6 | Open handwritten curved cap with one stem inside the parentheses after a baseline j; separate stroke below. | `j(\underline{\tau})` |
| 64, item 8 | The two f strokes have loops above and below the line; the m has two arches. They are lowercase corrections inside the titles. | `\handwritten{m}, \handwritten{f}` |
| 64, references | Hyphens in printed and handwritten page spans, including 136-148 in pen. | `14-32,\ 136-148` |

## Doubtful readings

| Scan | Line or location | Reading | Other candidates | Confidence | Ink and contextual preference |
| --- | --- | --- | --- | --- | --- |
| 57 | body 3, discovery | underlying i, visible e in indespensably | one surviving i in the composite | medium | A dot survives above an e-shaped bowl. “indispensably” fits the sentence, but the final type impression is uncertain. |
| 57 | body 3, redrawn letter after d | e | i | medium | The bowl and top stroke support e. The dot is compatible with an earlier i. The intended spelling would favour i. |
| 58 | first display, after z | right arrow | short dash | medium | “transformations” supports an arrow. The small thick end has very little spread. |
| 58 | The last two | circled aure | circled aare | low | The middle impression is overwritten. The circled margin spelling supplies are. |
| 58 | after (FS) | short hyphen | stray extension of the closing parenthesis | low | The wording proceeds directly to “of a modular form”. A horizontal mark protrudes right. |
| 58 | end of local variable line | three vertical dots | colon and one extra speck | medium | Two strong dots suit a colon introducing a formula. A third smaller dot is visible above. |
| 58 | after and we call | one obliterated group | no secure underlying letters | low | Several diagonal strokes cross a small area between call and a(n). |
| 58 | exponential, immediately before (\|x\| | dot | isolated copy mark | low | A distinct small spot sits at mid-height with no clear typographic function. |
| 58 | left margin before pi | dot | copy spot | low | The dot stands apart from the word in the margin and has the same density as nearby pen marks. |
| 59 | running head | atkin page 3 | unresolved clipped upper parts | medium | Lower outlines and sequence from page 2 support the reading. |
| 59 | opening F(z) | E under pen F | original F under pen F | low | Top stroke is conspicuous but the old lower bar merges with the newer shaft. |
| 59 | right of integral | gsi | ksi | medium | The first handwritten loop descends like g. The integral contains ξ. |
| 59 | right of eigenforms | cover | no second distinct word resolved | medium | A small cluster follows c and precedes the last r-like stroke. |
| 59 | left margin near group | multiplicative | multipl(ic)atif / multiplicatif | low | Initial rising verticals, longer middle group and a tall final stroke. The nearby formula uses the word “multiplicative”. |
| 59 | same note, final word | group | grup | low | The word is compressed. The typed word being cancelled is group. |
| 59 | last label | H3* | H3 with a small dot | medium | Only a dark centre and smaller side traces survive. Scan 64 explicitly refers to (H3*) in §2. |
| 59 | last line | for C⁰ | of C⁰ | low | Only parts of the type survive before C. The word follows “some basis”. |
| 59 | last line | has distinct | no rival full phrase resolved | medium | Broken verticals and arcs survive and eigenvalues is legible. |
| 59 | second operator display after plus | small dot | copy speck | low | There is a low spot before p. The same term in (1) has no spot. |
| 60 | after However | cancelled comma | unresolved small type impression | low | Dark overstrike covers a low mark. Commas appear after (H4) and essential. |
| 60 | At this point we | one cancelled word | no secure letters | low | Two heavy horizontal strokes leave isolated flecks. |
| 60 | penultimate line, after otherwise | period | reproduction speck | medium | Small distinct dot between otherwise and for. The prose would ordinarily continue directly. |
| 60 | last line, fixed | plain a | α | medium | The body is very pale. The preceding “for all” and the earlier q^α favour α. |
| 61 | repeated transformation at foot | right arrow | dash | medium | The end thickens. Same construction on 58. |
| 62 | between We then have and H1q | Theorem | no other continuous reading | medium | Seven type spaces carry crosses, with a capital-like initial and two curved strokes near the end. The word also appears further down. |
| 62 | Theorem 2, after typica | cancelled l | cancelled o | low | Two arcs survive between a and the clear final l. The word typical favours a repeated l. |
| 62 | last paragraph after state | a form | form | medium | The spacing accommodates a type before form. The letters of form remain visible under x. The insertion supplies an extension. |
| 62 | H2q, below pen Tp | printed T followed by s | printed T followed by p | low | A serifed upper T remains around the pen shaft and the next character has an upper curve. Context favours the lower p in the corrected operator. |
| 63 | item (iv), below display | covered is | no other full word recoverable | low | Pen are lies across older type. The old singular constant suggests is. |
| 63 | last paragraph, multiplicative | old p | i | low | The pen p covers a short serif and apparent shaft. Its older lower portion merges with the pen. |
| 63 | last two lines, before true | t | i | low | There is a short dark cross stroke at the middle of the deleted letter. The following t is clear. |
| 64 | reference 5, old numeral at left | 1 | no other secure digit | low | A vertical survives between deletion lines. The replacement gives a new range. |
| 64 | reference 5, old range between first and last trace | one erased group | unreadable | low | Three continuous dark rules obscure internal strokes. No contextual preference. |
| 64 | reference 5, old numeral at right | 5 | 3 | low | A curved end shows over the rules. New range above does not identify the original last digit. |
| 64 | left of reference 5 | Fin | Fiu | low | A faint high staff and two arms begin the note, followed by two very pale small shapes. No contextual preference. |
| 64 | reference 8, before odular | M | m | low | The dark handwritten m dominates the top of the earlier impression. Lowercase remains plausible. |
| 64 | reference 8, before unctions | F | f | low | The handwritten f covers the earlier stem. The corrected title favours a lowercase f in the new text. |
| 64 | reference 8, before orms | F | f | low | The second looped f has the same correction in the title, with the original impression obscured. |
| 64 | reference 9, page span start | 305 | 395 | medium | The middle oval has a broken lower contour. The end of the span favours 305. |
| 64 | reference 9, page span end | 308 | 300 | medium | The final oval is pinched at midheight but has lost most of its left half. No contextual preference. |
| 64 | institutional line, first word | The | no second whole-word reading | low | The type is exceptionally pale. A mark at the last letter and the spacing support this reading. |
| 64 | institutional line, second word | Atlas | no second whole-word reading | low | Only some upright and lower strokes survive. Computer Laboratory supplies context. |
| 64 | institutional line, third word | Computer | no second whole-word reading | medium | A curved initial and traces of a descender remain with the right number of spaces before Laboratory. |
| 64 | institutional line, first place name | Chilton | Chillton | medium | The first letters run together. The spacing favours a single l. |
| 64 | last punctuation | colon | period | low | Two vertically separated dark spots persist in both views. Their position in an address would favour a full stop. |
| 64 | last reference number, under 9 | 8 | 0 | low | A lighter lower loop shows below the upper bowl. The preceding entry is visibly numbered 8. The order supports the live 9. |

## Slips kept as written

| Scan | Line or location | As written | Apparently intended | Grounds |
| --- | --- | --- | --- | --- |
| 57 | body 1 | aulthor, l struck | author | one diagonal pen stroke cancels the l |
| 57 | body 3 | indespensably (overtyped letter) | indispensably | visible e-shaped impression under a dot |
| 58 | after regular,and | cusp-,forms | cusp-forms | both the hyphen and the comma are visible |
| 58 | The last two | circled aure/aare | are | left-margin correction gives the word |
| 58 | before z=i∞ | cupsp, first p struck | cusp | the surplus p is crossed |
| 59 | right of integral | gsi (uncertain) | xi | the marginal spelling accompanies the written ξ, then eta |
| 59 | left of final paragraph | group, struck | see the pencilled replacement | diagonal line through the typed word |
| 60 | penultimate line | otherwise.for | otherwise for | there is a small dot in the word space |
| 61 | after something like | conjecture with c covered | Conjecture | pen capital C sits over lower-case c |
| 61 | last paragraph | Hwever | However | handwritten o inserted |
| 61 | last paragraph | sp ecial | special | there is a full type space in the word |
| 62 | Theorem 2 | typica plus a covered letter plus l | typical | the pen marks interrupt the word |
| 62 | after state | a form, covered | an extension | the new words appear directly above it |
| 63 | item (iv) | Fα(z) after F(x) | no change proposed | the closing argument has a straight z profile |
| 63 | where k and kαβ | is constant with pen corrections | are constants | the pen replaces the verb and adds a final s |
| 63 | last two lines | extra letter before true | true | diagonal stroke cancels the first small type impression |
| 64 | reference 5 | crossed page range | 136-148 | the replacement is directly above it |
| 64 | reference 8 | initials within Modular Functions and Forms overwritten | modular functions and forms | three pen letters remain visible over the type |

## Abbreviations

| Form on the sheet | Probable meaning |
| --- | --- |
| i.e. | id est, that is |
| Cap. | capital |
| mod | modulo |
| Im | imaginary part |
| FS | Fourier series |
| Math. | mathematical or mathematics, in abbreviated journal names |
| J. | journal, in journal titles |
| IBM | International Business Machines |
| Trans. | Transactions |
| Amer. | American |
| Soc. | Society |
| Proc. | Proceedings |
| Phil. | Philosophical |

## Legibility

Most type impressions and inserted Greek letters can be followed across their lines. The top of scan 59 clips the running head, and the type near the foot fades almost away. Its final label, the pencil beside the struck word at the left and characters covered by repeated strikes of x are among the least secure readings. The original page span under the replacement in reference 5 on scan 64 and the beginning of the institutional line at its foot are also badly impaired. Underlinings sometimes touch character strokes or the rule of a fraction. The inventory assigns the handwriting to an unknown hand where the sheets give no signature for the marks.
