# Readings and doubts

## Notation table

Manuscript line references below are approximate and start with the first line of the body. Quoted headings and nearby words locate marginal or interlinear writing. The last column gives the LaTeX actually used for the corresponding feature.

| Scans and locations | What the pen does | LaTeX reading |
|---|---|---|
| 42, NB and Lemme A′; 43, Proposition; 44, first implication; 45, Lemme; 46, At Λ3; 48, foot; 49, Lemme 1(a) | Two opposed chevrons cross above and below a small central lozenge. Their arms extend beyond it. | `\mathrel{\rlap{$>$}<}` |
| 42, upper NB and margin; 45, MΛ′4; 46, At Λ2; 48–49, opening lines | Two straight, separated, nearly vertical strokes; in 48–49 the little M or Λ sits centrally below them. | `\parallel`, `\underset{M}{\parallel}`, `\underset{\Lambda}{\parallel}` |
| 42, ruled axiom and lower corollary; 43, MΛ0–3; 46, At Λ1; 48, opening tuple | Single chevron with a lower short stroke, paired chevrons, or a pair with a small open ring above it. The first two signs in the tuple on 48 have M underneath. | `\leq`, `\ll`, `\overset{\circ}{\ll}`, `\underset{M}{\leq}`, `\underset{M}{\ll}` |
| 43, MΛ1; 44, opening parenthesis; 45, lower lemma | Between stacked X and X′, 43 has a heavy V with a stroke on its right. On 44 the right stroke is separate. On 45 two V shapes sit one above the other. | 43 `\unsure{\rotatebox{90}{$\leq$}\|\rotatebox{90}{$\ll$}}`; 44 `\rotatebox{90}{$\leq$}`; 45 `\rotatebox{90}{$\ll$}` |
| 42, first display and closing proof; 43, two unions below MΛ1; 44–46 and 48–49, definitions | Lowercase omb with a small initial loop and tall final b. Capital Omb starts with a much larger round loop. Subscript Λ is present only where drawn. In scan 49 the first P in the second equivalence stands without parentheses. | `\mathrm{omb}_{\Lambda}(X)`, `\mathrm{Omb}(X)`, `\mathrm{omb}_{\Lambda}P` |
| 42, first union and foot; 43, union after MΛ1; 44, lower set definition; 45, NB; 46 and 48, At C and Posons; 49, Lemme 1(a) | A wave over X, Y, L or a primed variable. There are separate waves over the two members of an intersection. In 49(a) a brace reaches beneath both members. | `\widetilde X\cap\widetilde Y`, `\widetilde{X'}`, `\widetilde L`, `\underbrace{\widetilde X\cap\widetilde Y}_{L}` |
| 42, proof; 44–45, empty intersections; 46, At Λ1; 48–49, conclusions | The ring after a parenthesis and above a chevron is small and open. The null-set sign is an oval with a long diagonal. A zero below Z or D has no slash. | `(X)^\circ`, `\overset{\circ}{\ll}`, `\varnothing`, `Z_0`, `D_0` |
| 42, margin and proof; 43, MΛ1, MΛ4; 44, definitions; 45, upper note and four lemma conditions; 46, At Λ3; 48–49, lemmas | One or two short upright strokes to the right of a letter. L or Y may stand lower than a primed base. In the NB on 45 the lower letter is Y. | `X'`, `Y''`, `Z'`, `X'_L`, `X'_Y` |
| 42, Lemme A′ and Lemme B; 43, heading; 44, ML5; 45, MΛ′4/5; 46–48, axiom labels | M has joined rising strokes. Λ is an open triangle. A starts similarly but has a crossbar. In 42 the A′ in the lemma heading has a bar, while the triangle after “par lemme” on the last line has none. L has a foot in the uncertain ML/MΛ occurrence on 44 and the ML5 reference on 48. The first two headings of 43 have a second lower Λ shape. | `M`, `\Lambda`, `A`, `L`, `M\underset{\Lambda}{\Lambda}`, `M\Lambda'`; 44 `\unsure{ML\|M\Lambda}` |
| 42, At in Lemme B; 44–46, At headings; 47, prose beginning Dire que | A and the following low t are joined in At. C and D have single outlines; thickened letters in a revised heading or cell have been checked at that site. A in the prose stands by itself. | `A\!t_M`, `At\,C_{\Lambda}`, `At\,C\Lambda`, `At\,D\Lambda`, `A` |
| 43, Notons and last display; 44, cancelled start of first implication, then live formulas | Looped capital with a second smaller bowl and a leg curving to the right. Calligraphic R is the first reading; script R is also possible. | `\mathcal R` or `\mathscr R`, marked at first occurrence on each page |
| 42, proof; 43–44, R(X,Y) and paragraph on lieux; 48, brace; 49, Terminologie | Angular Z; large crossed X and forked Y in formulas; visibly smaller x,y in the sentence on lieux. On 49 P has an upper bowl, Q has a rounded loop and terminal. On 43 the first variable after MΛ2 could be x or X. | `Z`, `X,Y`, `x,y`, `P,Q`; 43 `\unsure{x\|X}` |
| 42, middle axiom and first union; 43, middle and foot; 44, last set; 46, two criteria; 48, Posons; 49, last line | A wide U-shaped union has its bound underneath. In the set description on 44 a vertical stroke separates the first variable from the conditions. A small “def” is written above an equality or a double arrow. | `\bigcup_{Z\in L}`, `\middle\|`, `\overset{\mathrm{def}}{=}`, `\overset{\mathrm{def}}{\Longleftrightarrow}` |
| 43, system and quantified axioms; 44, lower set; 45, crowded hypotheses; 48–49, membership formulas | Λ ⊂ M has a plain open arc; the sign in Z ∈ Λ has a middle stroke; the existential has two short bars inside an upright and the universal is an inverted open triangle with a crosspiece. | `\subset`, `\in`, `\exists`, `\forall` |
| 45, lower lemma, its additions and proof | The condition labels put i strokes, isolated primes and sometimes a rounded stroke within parentheses. The handwriting makes (ii)/(i0) and several primed labels particularly doubtful. | `(i)`, `(ii)`, `(i0)`, `(i')`, `(ii')`, `(i'')`; alternatives given separately in the register |
| 46, implication diagram; 47, opening list and four-row diagram | Double shafts with directional heads. D has a lowered 0. The star is on the line with C or CΛ. On 47 the left connector in the four-row diagram has rounded ends and is marked separately. | `\arrow[r,Rightarrow]`, `\arrow[d,Rightarrow]`, `\arrow[d,Leftrightarrow]`, `D_0`, `C\Lambda\mathord{*}`; 47 `\Updownarrow` or `\Downarrow` |
| 47–49, numbered cases and parallel relations | Case numbers in 47 and 49 have a raised open circle and a closing parenthesis. In 48–49 the axiom numbers next to Λ occupy the baseline. | `1^{\circ})`, `2^{\circ})`, `M\Lambda4` |
| 42, cancelled NB; 44, after elle-; 45, after au; 46, last line | Two short parallel horizontals appear in prose. The first reading is the drawn sign, with “même” as its possible verbal value. | `\unsure{$=$\|même}` |
| 44, “saturées pour”; 45, lower right “très dense”; 46, “At” and a struck remark | Small paired vertical quotation strokes. “très” has a distinct rule underneath it. | <code>&#96;&#96;…''</code>, `\uline{très}` |
| 42, Cor and Plus gén; 43, réf; 44, tjrs and the raised adjectives; 46–49, headings, margin references and proofs | The writer compresses or stops words. The stop is retained where it has a distinct trace; readings of faint endings are separately marked. | `Cor`, `gén`, `réf`, `tjrs`, `réfl. sym.`, `resp.`, `cf.`, `i.e.` |

## Register of doubtful readings

Each row corresponds to one mark in the transcription. Within a row the first reading follows the ink. An em dash in the alternatives column means that no other reading could be specified. For a single doubtful letter or ending the context column may refer to the whole word.

| ID | Scan | Approximate manuscript line or location | First reading | Other readings allowed by the ink | Confidence | Context and reason |
|---|---:|---|---|---|---|---|
| 42.01 | 42 | 1, between axiome and fait | `ne` | `en` | medium | The hooked beginning gives ne as the first reading. The cancelled sentence continues with que; the construction ne … que also favours ne. |
| 42.02 | 42 | 1, NB, verb after fait | `intervenir` | `intervient` | medium | There is a small upstroke at the end, partly crossed by the long cancellation. The following que and the preceding fait favour the infinitive intervenir. |
| 42.03 | 42 | 2, NB, after et | `$=$` | `même` | medium | Two separate horizontal strokes give the first reading. “et même seulement” accounts for the second reading in the sentence. |
| 42.04 | 42 | 10, after ce qu’il faut | `poser` | `pour` | medium | The downstroke and short terminal allow both. The words about an axiom favour “poser”. |
| 42.05 | 42 | 10, before the final noun | `en` | `au` | low | The connecting stroke has no closed second bowl. “poser … en axiome” favours “en”. |
| 42.06 | 42 | 10, last word | `axiome` | `minimum` | medium | Compare the small repeated strokes in “axiome” in the first line. The numbered statement below favours “axiome”. |
| 42.07 | 42 | 11, overwritten axiom number | `5` | — | low | An upper horizontal and a lower curve survive below the revised 4. The nearby labels provide no independent old number. |
| 42.08 | 42 | 11, end of revised label | `4''` | `4'` | low | Two raised strokes touch the end of the 4. The nearby margin supplies the 4 but does not establish the number of primes. |
| 42.09 | 42 | 13, after Propriété | `restrictive` | — | medium | The first and last groups are clearer than the central connected t strokes. The following “sur les paires” is consistent with “restrictive”. |
| 42.10 | 42 | 13, word under paires | `couples` | — | low | A loop and a long descender remain under the horizontal cancellation. The raised “paires” favours an earlier paired noun. |
| 42.11 | 42 | 15, marginal p.32 reference | `lemme` | — | medium | The reference to a number and page supports the word “lemme”. The middle letters form one long stroke. |
| 42.12 | 42 | 15, letter after Lemme | `B` | — | medium | The capital has two bowls but is inked over. The heading can accommodate B; the page does not recover an older letter. |
| 42.13 | 42 | 17, beneath replacement Cor | `Cor` | — | medium | The overwritten abbreviation has the same width as the legible new heading immediately above it. |
| 42.14 | 42 | 17, after X … Y | `et` | — | low | The small conjunction is compressed into two strokes. It links two written conditions. |
| 42.15 | 42 | 19, between Utilisant and Lemme C′ | `pour conclure donc` | — | low | Several pen strokes run horizontally through this phrase. The following partial condition is compatible with “pour conclure”. |
| 42.16 | 42 | 19–20, end of struck line | `la condition des` | — | low | The upper tips of the letters survive. The later condition heading suggests “condition”; the final word is especially weak. |
| 42.17 | 42 | 20, after X of Soient | `,` | — | low | A short diagonal may belong to the cancellation. The adjacent symbols could take a separator, but context cannot settle it. |
| 42.18 | 42 | 20, second variable after Soient | `Y` | `X'` | low | A dark new downstroke crosses the old pair of arms. Both letters recur in the sentence. |
| 42.19 | 42 | 20, raised insertion after variables | `$(\ll X)$` | — | low | An arrow reaches the overwritten variable. Short angled strokes and the final X survive; the parenthesis is faint. |
| 42.20 | 42 | 20, end of opposed relation | `Y'` | `X'` | low | The prime is visible. The base has crossed strokes like both X and Y, with no conclusive contextual preference. |
| 42.21 | 42 | 20–21, raised Cond. | `Cond. équiv` | — | low | The two short words precede the crossed condition. The longer crossed expression on the next line supports their expansion, but its letters are also crossed. |
| 42.22 | 42 | 20–21, before Z ≪ X | `et` | — | low | The cancellation absorbs the small connective. The condition to the right allows “et”. |
| 42.23 | 42 | 21, line below Lemme C′ | `Conditions équivalentes` | — | medium | The first word has a tall opening loop and a plural-like ending. The preceding raised abbreviated wording supports this reading. |
| 42.24 | 42 | 22, below struck conditions | `(i)` | — | low | A short stroke lies inside two curves. A condition listing is consistent with (i); no dot is secure. |
| 42.25 | 42 | 22, below condition label | `(bis)` | — | low | The curve and final s-like stroke can make “(bis)”. The cancellation prevents a firmer preference. |
| 42.26 | 42 | 24, before i.e. in proof | `et` | — | low | Two small joined strokes remain. The immediate rewrite “i.e.” leaves the former connective open. |
| 43.01 | 43 | 4, before first axiom name | `A` | — | low | A looped crossbar is left of M. The new label supplies no reliable expansion of the earlier one. |
| 43.02 | 43 | 5, left margin beside MΛ1 | `induit` | `indirect` | medium | The word starts in- and ends with a tall t. With “raffinement” either reading forms a phrase. |
| 43.03 | 43 | 5, between stacked X and X′ | `\rotatebox{90}{$\leq$}` | `\rotatebox{90}{$\ll$}` | medium | The V has one distinct stroke on its right. The similar sign on 44 favours rotated ≤; 45 supplies a comparison for rotated ≪. |
| 43.04 | 43 | 6, between ∃ and Y′ | `\mathord{.}` | — | low | A dot lies on the line, below the height of the later prime. The syntax does not require a dot. |
| 43.05 | 43 | 6, struck after Y′ | `\ll` | — | medium | Two inked-over wedge strokes precede “avec”. Plain ≪ occurs later in the same line. |
| 43.06 | 43 | 7, immediately below union | `\varnothing` | — | low | A loop and crossing emerge from heavy ink. The surrounding bounds do not decide the earlier shape. |
| 43.07 | 43 | 7, crossed first bound | `\widetilde Y\cap\widetilde X'` | — | low | The Y-side is better preserved than the second letter. The following, separate union uses the tilded pair and favours this reading. |
| 43.08 | 43 | 8, left of second equals | `\text{et}` | — | low | A tiny crossed mark has a looped first stroke. No preference follows from the equality. |
| 43.09 | 43 | 9, first variable of MΛ2 | `x` | `X` | medium | The cross is conspicuously small. The last X in the same statement is large and favours the uppercase reading in context. |
| 43.10 | 43 | 10, left margin beside MΛ3 | `stricte voisinance` | `stricte minimalité` | low | The opening has the two t strokes of “stricte”. The rest consists largely of short waves; the numbered statement alone does not distinguish the nouns. |
| 43.11 | 43 | 13, old numeral in the MΛ5 heading | `4` | — | low | Beneath the long top bar of the 5, a diagonal, cross-stroke and thickened upright resemble the 4 immediately above. The darker retracing obscures the bottom of the old numeral. |
| 43.12 | 43 | 13–15, first line of long left note | `condition` | — | medium | There is overwriting near the initial c. The next line repeats “la condition”, favouring the reading. |
| 43.13 | 43 | 13–15, long left note, third line | `en apparence` | `apparemment` | medium | A break looks like a space; the following “plus forte” works with either candidate. |
| 43.14 | 43 | 13–15, long left note before plus | `supp.` | — | medium | The end has been run into the edge of the writing field. The opening “où on ne … plus” favours supposer. |
| 43.15 | 43 | 17, before L’axiome | `$M$` | — | low | A pair of joined high strokes is crossed. The neighbouring MΛ label suggests M without deciding the older shape. |
| 43.16 | 43 | 18, Notons … la relation | `\mathcal R` | `\mathscr R` | medium | The swept left loop and diagonal leg recur in R(X,Y) here and on 44. Context identifies the same letter but does not choose a typeface. |
| 43.17 | 43 | 20, before à Λ | `réf` | — | medium | The final downturned stroke resembles f. “sans … à Λ ni à …” favours an abbreviation for référence. |
| 44.01 | 44 | 3, after que cette | `relat` | — | medium | Only a short beginning remains on the line; the repeated live “relation” supports it. |
| 44.02 | 44 | 4, cancelled opening of R(X | `\mathcal R(X` | `\mathscr R(X` | medium | The large left loop repeats the R used twice farther right. Its script style remains open, and the cancelled parenthesis appears unfinished. |
| 44.03 | 44 | 5, beginning of line | `et l'` | — | low | A cancellation cuts the short word and the following upright. The revised opening begins with the article of axiome. |
| 44.04 | 44 | 5, just before axiome | `le'` | `l'` | low | There is a small loop between the upright and the detached stroke. The normal article in the later “l’axiome” favours the second reading. |
| 44.05 | 44 | 5, label before 5 | `ML` | `M\Lambda` | medium | The second character has a foot. The plain L form also occurs on 48, whereas the following clause on this sheet uses Λ. |
| 44.06 | 44 | 5, after est | `de` | — | low | A little loop is struck twice. The surviving continuation gives no definite former word. |
| 44.07 | 44 | 5, after the struck word | `satisfait` | `toujours` | low | The descending stroke could belong to f or j. In the longer reading of the next word, the clause favours “satisfait”. |
| 44.08 | 44 | 5, end of line | `tautologiquement` | `tautologique` | low | The last two letters join into a long return. The following “pour cette condition” works with either wording depending on the previous word. |
| 44.09 | 44 | 9, after the closing double quote | `)` | `,` | low | The extra upright curves below the quote. It might divide the following relative clause as a comma. |
| 44.10 | 44 | 12, elle- followed by two strokes | `$=$` | `même` | medium | The ink shows two strokes. The phrase after “en prenant” favours the word “même” as their value. |
| 44.11 | 44 | 15, after deux | `$L$` | — | medium | There is a tall upright with a bent foot. “des lieux x,y” below is consistent with a short L. |
| 44.12 | 44 | 16, verb before exister | `pourra` | `arrivera` | low | Initial crossing and two waves obscure the body. “pourra exister” reads naturally; the first few strokes also allow arrivera. |
| 44.13 | 44 | 19, parenthesis in At C label | `espac` | `spac`, `espace` | low | The last letter is overwritten. The repeated spac heading on 46 favours “spac”, but the first curl here may be an independent e. |
| 44.14 | 44 | 19, cancelled end of same label | `e` | — | low | A terminal loop is covered by a heavy cross. No reliable original ending is supplied by the other headings. |
| 44.15 | 44 | 23, cancelled definition after posé | `\subset` | `\in` | low | The left edge of the sign is curved. The crossed stroke hides the distinction between a contained-set sign and membership. |
| 44.16 | 44 | 23, immediately after X′L = | `\widetilde X` | — | low | Several repeated diagonal strokes have been obliterated. The live tilded X′ explains the choice of X underneath. |
| 44.17 | 44 | 23, subscript of Omb(L) | `\Lambda` | — | low | The residue is low and triangular. Elsewhere the author uses Λ here, though the finished form here has no readable subscript. |
| 44.18 | 44 | 23–24, right side of set brace | `\text{avec}` | — | low | Only the ends of a short connector survive. The two neighbouring set conditions accommodate “avec”. |
| 44.19 | 44 | 24, beyond set at right edge | `\}` | — | low | A separate closing-shaped stroke remains among the cancellation lines. The ink supports an extra brace; the surrounding prose starts with a parenthesis. |
| 44.20 | 44 | 25, old relation in cancelled corollary | `\parallel` | — | low | Two short, near-parallel strokes precede the overdrawn sign. The nearby surviving parallel relation supports the reading. |
| 45.01 | 45 | 2, after structure d’ | `Atelier` | `Atelies` | low | A tall internal l and a small i-like stroke precede the trailing wave. The paired At labels identify the subject but do not determine the written ending. |
| 45.02 | 45 | 3, after At CΛ | `spac` | — | medium | The parenthesis encloses a short run of letters. The (spac) heading on 46 supports the reading. |
| 45.03 | 45 | 3, to right of the parenthesis | `.` | — | low | There is a small heavy mark before the added At D. It could be the punctuation of the first version. |
| 45.04 | 45 | 3, crossed before Les axiomes | `Cette` | — | low | Initial curve and two tall strokes remain. The next definite article starts the rewritten sentence. |
| 45.05 | 45 | 3, between the two axiom numbers | `:` | `à` | medium | Two separate marks look like a colon. The pair of ordered numbers favours “à” as a possible reading. |
| 45.06 | 45 | 4, after the crossed restent and the word ne | `varieront` | `varient` | low | A dotted i and a tall stroke survive clearly, but the letters between the vowel and the short final stroke have collapsed. The plural subject fits both readings. |
| 45.07 | 45 | 4, after On doit avoir | `$\checkmark$` | — | low | The mark rises again from a short curved stroke. No word or formula nearby fixes its value. |
| 45.08 | 45 | 5, after the parallel bars | `Z'` | — | low | The base letter is written over a fork; the prime is short. The following inequality contains Z′ and favours it here. |
| 45.09 | 45 | 6, small struck start before Z ∥ Z′ | `Si on a` | — | low | The horizontal rules mask both letters and spaces. The rewritten condition immediately starts “Si”. |
| 45.10 | 45 | 8, initial crossed condition | `Y\leq X` | — | low | The lower-order sign lies among long scratch strokes. The short Y ≤ X written below favours this earlier reading. |
| 45.11 | 45 | 8–9, before L = in the scratch | `soit` | — | low | A short rounded s and an upright remain. The defining equation alongside supports the proposed lead-in. |
| 45.12 | 45 | 8–9, after the crossed intersection | `$X$ et` | — | low | There is a dark cross and then a compact connective. The surviving variables around it do not decide its letters. |
| 45.13 | 45 | 10, just before Y′ in the line below Y ≤ X | `\mathord{.}` | — | low | The dot stands apart from the left branch of Y. It has a counterpart before Y′ in scan 43; it may also be an incidental pen touch. |
| 45.14 | 45 | 12–13, crossed intersection after ou encore | `\mathrm{omb}` | — | low | The little letters after the intersection sit behind the horizontal rule. The two adjacent versions contain omb or Omb. |
| 45.15 | 45 | 13, below first surviving capital Omb | `\Lambda` | — | low | The mark is a low triangle partly filled in. Its shape points to Λ; the strokes in the lower lemma offer a different possible index at another occurrence. |
| 45.16 | 45 | 14, between dash and ça revient | `tout` | — | low | The horizontal line crosses a tall t twice. The sentence about the two forms supports “tout”. |
| 45.17 | 45 | 14, after revient au | `$=$` | `même` | medium | Two horizontal strokes appear in the square bracket. The surrounding words favour the value “même”. |
| 45.18 | 45 | 11–14, left margin after définit | `$X'_Y=$` | — | low | The older formula is crossed, with a low Y-like tail. The rewritten formula immediately below supports the proposed left side. |
| 45.19 | 45 | 17, start of lemma’s parenthesis | `uniquement` | — | low | Nearly all letters meet the pen line. The surviving “indépendamment…” is compatible with the proposed discarded adverb. |
| 45.20 | 45 | 19–20, first insertion in Conditions | `(ii')` | `(ii'')` | low | The raised label has two short i strokes and a final elevated mark. Comparison with the four rows favours ii′. |
| 45.21 | 45 | 19–20, second insertion in Conditions | `$(i0)$` | `$(ii)$` | low | The second sign is rounded; the bracketed second condition is the one singled out. The numeral-like form has the better contour here. |
| 45.22 | 45 | 21, label of first condition | `(i)` | — | medium | The small oval opening stroke touches the parenthesis. The further references in the proof favour (i). |
| 45.23 | 45 | 22, left of bracketed condition | `(ii)` | `(i0)` | low | Two small strokes and a rounded terminal run together. The corresponding inserted label looks like (i0). |
| 45.24 | 45 | 23, label of third condition | `(i')` | `(i'')` | low | A diagonal cancellation crosses the short marks. The pair of primed conditions in the heading favours i′. |
| 45.25 | 45 | 23, under large Omb | `M` | `\Lambda` | low | The low strokes form either a pair of joined uprights or a pointed triangle. The smaller omb earlier usually carries Λ; the letter here is thicker. |
| 45.26 | 45 | 24, last condition label | `(ii')` | `(i'')` | medium | The first two small strokes are distinct from the later elevated stroke. The earlier group of labels favours ii′. |
| 45.27 | 45 | 25, underlined start of proof | `Dém` | — | medium | Full-width cancellation obscures the accent. The argument underneath favours the French abbreviated heading. |
| 45.28 | 45 | 25, after the crossed implication | `tautologiquemt` | `tautologique` | low | A tall final stroke runs into the diagonal strike. It may stand for abbreviated “ment”; the next word begins a new implication. |
| 45.29 | 45 | 25, before the live implication | `$(ii')$` | — | medium | The rightmost stroke sits higher than the two at its left. The lower row of the lemma has the same candidate. |
| 45.30 | 45 | 25, just before Supposons | `en` | — | low | A short cancelled mark has two connected downstrokes. The surrounding text gives no dependable former word. |
| 45.31 | 45 | 26, immediately after Supposons | `$(ii')$` | — | medium | The label sits under a diagonal at the left of the line. The preceding implication favours the same (ii′) as its hypothesis. |
| 46.01 | 46 | 1, after Λ ⊂ M | `fermé` | `fermée` | medium | The terminal after the high m is a light taper. The later phrase “partie fermée” on 48 supports the feminine form, but here the ending is compressed. |
| 46.02 | 46 | 2, before pour L | `envisagées` | `analogues` | medium | An evident descender in the middle favours the g of “envisagées”. Both candidates fit “conditions … pour L”. |
| 46.03 | 46 | 6–9, note beside At Λ3 | `réduit` | `ident.`, `évidemt` | low | The turned crop shows an initial wave, a short loop and final tall t. The explicit cross-reference favours a word for reduction or identity. |
| 46.04 | 46 | 7, overwritten first letter before the chevrons | `Z` | — | low | A nearly horizontal trace crosses the new X. The previous reference to existence could accommodate Z. |
| 46.05 | 46 | 7, before L = X ∩ Y | `$X'$` | — | low | The old cross has a short detached high trace. The rewritten line uses X′ shortly afterwards. |
| 46.06 | 46 | 7, near the old X′ | `et` | — | low | The small following curve is covered by a heavy backward stroke. The immediate context leaves the old connective open. |
| 46.07 | 46 | 8, under the parallel strokes | `\Lambda` | — | low | The deleted index is triangular. The same relation bears a clear Λ in other formulas. |
| 46.08 | 46 | 9, after the deleted definitional equals | `\widetilde X` | — | low | There is an upper and two diagonal strokes under the scribble. The live next line has tilded X among its terms. |
| 46.09 | 46 | 17, diagram, immediately to right of C | `*` | `\Lambda` | low | Several crossing strokes could conceal a star or a triangular letter. The final node reads C; the surrounding labels do not recover the old one. |
| 46.10 | 46 | 21, before sigle | `le` | `les` | medium | The last letter may have a further tail. The following singular “sigle” favours “le”. |
| 46.11 | 46 | 23, first (spac) of final paragraph | `spac` | — | medium | The internal p is dark and retraced. The clear paired headings (spac)/(pol) above support this reading. |
| 46.12 | 46 | 24, crossed three-letter label | `CBS` | `CDS` | low | The second capital has a dark bowl. The next wording refers to B or S, favouring CBS but not recovering all strokes. |
| 46.13 | 46 | 24, article in the cancelled parenthesis | `le` | `la` | low | The article has a small upward finish under the line. The shape allows either ending. |
| 46.14 | 46 | 24, after that article | `B` | `S` | low | The initial shape has two bulges, with an upper stroke crossing the cancellation. B is consistent with the previous dark label. |
| 46.15 | 46 | 24, struck quoted expression | `sous-figures` | `bouffe-figures` | low | The second word resembles figures; the crossing covers the beginning. The inserted “bouffe” supports a joke involving figures, without deciding the old first word. |
| 46.16 | 46 | 24, inserted above that quotation | `il bouffe des` | `il bouff. des` | low | Two adjacent long downstrokes fit ff. The last short mark before “des” could be an ending or abbreviation point. |
| 46.17 | 46 | 25, after the last At C | `spac` | — | low | Extra strokes before spac mingle with the letter following the opening parenthesis. The preceding paired labels support spac. |
| 46.18 | 46 | 25, after le in final parenthesis | `$=$` | `même` | medium | Two level strokes are clearly drawn. The words “mais toujours le” favour the value “même”. |
| 47.01 | 47 | 1, after conditions | `de` | — | medium | The little word lies near a thickened stroke. The compound following it can be governed by de. |
| 47.02 | 47 | 2, after compatibilité- | `disjonction` | `des parties` | medium | The small letters form nearly a single run after the dash, which favours “disjonction”. The loop could begin a second word in “des parties”. |
| 47.03 | 47 | 2, crossed after Λ | `peut` | — | low | The first and last strokes of a short word survive. The rewritten sentence later starts “peut être”. |
| 47.04 | 47 | 6–7, between Λ3 and D | `\Updownarrow` | `\Downarrow` | low | The double shaft has a rounded cap at the top and a downturned lower end. The margin’s “équivalences” favours two directions. The neighbouring double-headed arrow is much more explicit. |
| 47.05 | 47 | 9, row d after Λ1 | `''` | — | low | Two short elevated strokes stand apart from the following cell. The diagram supplies no secure meaning for them. |
| 47.06 | 47 | 9, earlier form in second cell | `C\mathord{*}` | — | low | A bowed stroke and a small dark crossing precede the new 2. Neighbouring forms contain C*. |
| 47.07 | 47 | 9, earlier form in third cell | `D_0` | — | low | The earlier large bowl has a low oval at its right. Both the neighbouring D₀ and earlier diagram favour that reading. |
| 47.08 | 47 | 6–8, first right-hand note | `valent` | `valant` | medium | The vowel between l and nt is flattened. The note reads as an independent clause with “valent” or a dependent clause with “valant”. |
| 47.09 | 47 | 9, after figure dans in NB | `chacun` | — | medium | The end merges into the next word. “des quatre” favours the singular chacun in the note’s distribution statement. |
| 47.10 | 47 | 9, lowest line of NB | `syst.` | — | low | The abbreviation has a compact group of tall strokes. The four lettered systems above favour “syst.”. |
| 47.11 | 47 | 18, before devient | `est` | — | low | There is a dark short stroke just before the rewritten verb. Its location favours an earlier copula. |
| 47.12 | 47 | 21–22, end of the insertion M-polyédr | `.` | — | low | A very short terminal stroke is near the hooked lead. It can serve as the abbreviation point. |
| 47.13 | 47 | 22, immediately before D in the sentence ending et à C spac | `:` | `à` | medium | Two tiny detached marks resemble a colon. Nearby instances of à have a lower curve, which is very slight here. Both “satisfait” and “et à C spac” favour à in context. |
| 47.14 | 47 | 22–23, between C spac and C pol | `resp` | — | medium | The middle of the short word and a possible point are weak. The two named conditions favour “resp”. |
| 47.15 | 47 | 25, before il est M-spacieux | `dès` | `ssi`, `si` | low | The tall first stroke resembles d but is crossed by the next curl. The following “et si de plus” also makes a reading with si possible. |
| 48.01 | 48 | number at top centre | `6` | — | low | A curved lower stroke is visible beneath 7. Other overwritten manuscript pagination favours a prior digit. |
| 48.02 | 48 | 2, below double chevron in tuple | `,` | — | low | There is a short inked loop immediately right of the lower M. The live comma already sits separately on the baseline. |
| 48.03 | 48 | 12, crossed after X,Y ≤ Z | `L=\widetilde X\cap` | — | low | L and the crossed X are clearer than the wave overhead. The definition on the next line supports the intersection. |
| 48.04 | 48 | 12, right end of same cancellation | `Y'` | `\widetilde Y` | low | A tiny raised stroke remains past the angle. The repeated definition on the next line favours tilded Y, though the physical trace could be a prime. |
| 48.05 | 48 | 11–12, marginal ML5 | `4` | — | low | A transverse stroke and a second tip are visible underneath the 5. The page reference does not identify its old numeral. |
| 48.06 | 48 | 14, below first capital Omb | `\Lambda` | — | low | Crossed triangular material remains below the baseline. The repeated use of Λ under omb in the preceding line supports it here. |
| 48.07 | 48 | 20, after crossed Comme | `tantôt` | — | low | The long stroke leaves portions of two upright t-like letters. The following rewritten “On pose” does not identify the old word. |
| 48.08 | 48 | 22, below the opposed chevrons at foot | `M` | — | low | A pair of joined strokes is visible through the cancellation. The parallel relation directly below carries M at the corresponding place. |
| 49.01 | 49 | 1, after the comma following symétriques | `.` | — | low | A second isolated dot lies before the chevrons; it could be incidental ink. The clause does not decide. |
| 49.02 | 49 | 5, after Lemme 1 | `Soient` | `Soit` | medium | There is very little ink between i and the terminal t. The pair X,Y favours the plural form. |
| 49.03 | 49 | 10, beginning of the crossed proof | `On a` | — | low | The first large loop and its tail survive the rule. The word after it may have been a detached a. |
| 49.04 | 49 | 10, just after the old X … Y | `trivial sur` | — | low | A tall t and short terminal strokes survive. The next line’s “définition” supports this fragment. |
| 49.05 | 49 | 15, struck before X ∥ Y | `donc par` | — | low | The two groups are separated clearly but their middles lie on the cancellation. The next live condition could have followed “par”. |
| 49.06 | 49 | 18, end of the first low crossed phrase | `donc le` | — | low | Only a low loop and a last upright remain. The following separate definition gives no firm preference. |
| 49.07 | 49 | 18, before L = X̃ ∩ Ỹ | `on` | `a` | low | The small initial loop is open at the right. The raised “Mais comme” makes a verb possible, but the expected words cannot settle the reading. |
| 49.08 | 49 | 18, before donc | `alr` | `alors` | low | Two tall strokes are crossed together. The next surviving word is “donc”, which can replace alors. |
| 49.09 | 49 | 19, struck after ombΛ(L) = ∅ | `elle se réduit à` | `il en résulte` | low | The first group has two upright loops; the last has a tall terminal. The evident new derivation could follow either discarded formulation. |
| 49.10 | 49 | 20, after montre que ça | `signifie` | `signifi:` | medium | The last dot-like mark lies at the outer end of the line. The full verb is favoured by the following X ∥ Y. |
| 49.11 | 49 | 23, immediately after Terminologie | `.` | — | low | The short detached ink could finish the e. The heading does not require punctuation to identify it. |
| 49.12 | 49 | 23, under the corrected verb following Terminologie | `t` | — | low | A crossed t is visible underneath the long final stroke. The position supports an earlier “Soit”. |
| 49.13 | 49 | 23, ending of that corrected verb | `ent` | `t` | medium | The final stroke lengthens the old form. The immediately following P,Q and “deux parties” favour -ent. |
| 49.14 | 49 | 24, first ∀ in the final display, between X and ∈ | `\mathpunct{:}` | — | medium | Two separate dots rise diagonally from the foot of X toward the membership sign. They look like a colon. A parallel expression on the following line has only the variable and membership sign, leaving the function of these marks open. |
| 49.15 | 49 | 26, last line, after et | `item` | `idem` | medium | The middle stem looks crossed rather than looped. Both Latin spellings can introduce the repetition for Q. |

## Slips and discrepancies retained

| Scan and approximate line | As written or read | Apparently intended | Manuscript evidence |
|---|---|---|---|
| 42, final line | par lemme Λ′ | A′, the lemma named higher on the sheet | The upper A′ has a clear horizontal bar. The bottom letter consists only of two diagonal strokes and a prime. |
| 43, l.16, after the last axiom | C'est ces deux derniers axiomes seulement qui font intervenir… | “Ce sont ces deux derniers axiomes…” in regular agreement | The first words are “C'est ces”. The later insertion supplies “deux”. |
| 43, MΛ2, l.9 | The first cross after ∀ is small, with x the first candidate; the last one is X. | Possibly X at both places | The strokes differ in size within the same line. The uncertainty is on the first variable. |
| 44, l.5, after the first implication | le'axiome, or l'axiome; ML5, or MΛ5 | Possibly l'axiome MΛ5 | The article is retouched. A few words later the writer has “Ainsi l'axiome” and a triangular letter in the label. |
| 44, l.9, after “saturées pour ≤” | A comma-like or parenthesis-like stroke after the closing quotes | No secure intended punctuation | The closing quotation marks sit above this stroke. |
| 44, l.23–24, after posé | An opening round parenthesis and a possible additional right brace after the set | Possibly a closing parenthesis after the definition | The right edge and the earlier writing are crossed together; the visible ending is preserved. |
| 45, l.8, cancelled insertion | tels que il existe | Possibly “tels qu'il existe” | Both words are discernible in the insertion. Scan 48 writes the elided form in a closely related line. |
| 46, At CΛ (spac), l.9–10 | définie par L̃ = X̃ ∩ Ỹ). | A closing parenthesis perhaps belonging to a discarded opening | The right parenthesis is distinct. The beginning of the sentence has been rewritten above a cancellation. |
| 47, l.3–5 | (impliquant donc tous les axiomes pertinents … peut être caractérisé | Possibly a closing parenthesis after the intervening list | The left parenthesis is visible before “impliquant”. I did not find its mate at the end of the list. |
| 47, final paragraph | dès / ssi / si il est | A connective agreeing with the later “et si de plus” | The first word remains marked. The letters do not warrant supplying a further “que”. |
| 49, converse of (a), l.17 | A stop after ∅, followed by et prouvons | A continuation after the stop | The punctuation and the lowercase conjunction both remain in the fragment. |
| 49, proof of (b), l.22 | Prouvons b Résulte tautologiquement de MΛ4 | Possibly a break between b and Résulte | There is no secure extra punctuation between the two groups. |
| 49, Terminologie, first row | Two dots between X and ∈ P | Possibly pen touches during the first quantified expression | A low dot and a higher, slightly rightward dot intervene. The membership sign is complete beside them. |

## Abbreviations

These are editorial interpretations of the written forms. A question in the register still applies when an abbreviation occurs in cancelled or reduced handwriting.

| Written form | Possible full form or value | Example |
|---|---|---|
| NB | nota bene | 42, cancelled opening; 45, left margin; 47–48 |
| p. | page | 42, p. 30; 48, p.42 |
| i.e. | id est | 42, ruled axiom; 49, proof |
| def, déf. | définition; par définition in the indicated equality or passage | 42 and 48, above =; 49, converse and last equivalence |
| omb, Omb | ombre; “grande ombre” is the marginal gloss by the capital form | 43, first union; 48, Posons |
| At | atlas or an axiom for an atlas; the sheets use At chiefly as a label | 42, Lemme B; 45–46, headings |
| Cor | corollaire | 42 and 44, lower part |
| gén | généralement | 42, “Plus gén” |
| Cond., équiv | conditions, équivalentes | 42, cancelled lower lemma |
| réf | référence | 43, last paragraph |
| supp. | suppose | 43, long lower-left note |
| relat | relation | 44, crossed opening |
| réfl., sym. | réflexive, symétrique | 44, interlinear addition |
| tjrs | toujours | 44, statement about x,y |
| Dém | démonstration | 45, bottom proof |
| tautologiquemt | tautologiquement | 45, cancelled proof |
| ident., évidemt | identique; évidemment, for the respective doubtful readings | 46, slanted note by At Λ3 |
| spac, espac, pol, polyédr. | spacieux; polyédral, as spelled out in the phrases about an atlas | 44–46, paired headings; 47–48 |
| p. ex | par exemple | 47, above rows a–d |
| syst. | systèmes | 47, right-hand NB |
| resp, resp. | respectivement | 47, C spac and C pol; 48, opening |
| ssi | si et seulement si, for one possible reading of the connective | 47, last paragraph |
| cf. | confer, comparez | 48, “Non, cf. plus bas” |
| alr | alors, for the doubtful short deletion | 49, converse |
| = in running French | même, as in “elle-” and “au” followed by two strokes | 42, 44–46 |
| OK. | okay, a mark of assent | 42, last word |

## Legibility

The equations in the clear rows, the date, and much of the main French text can be followed stroke by stroke. I trust the cancelled lower lemma on 42, the bounds rewritten at the right of 44, the overlapping hypotheses and condition labels on 45, the erased remark at the foot of 46, and the abandoned proof lines on 49 least. Rotation resolves the low note on 48 into “Non, cf. plus bas” with “p.49” below it. The last union of 45 reaches the lower edge after the intersection sign. The fragment stops at the visible ink there.
