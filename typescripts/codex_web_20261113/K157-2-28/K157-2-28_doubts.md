# Readings, notation and editorial doubts

## Notation table

Locations name a line or a distinctive inscription on the scan. A raised ring is especially difficult to distinguish from a handwritten o. The choices for curved capitals and the local placement of a tilde, bar, prime or low letter were checked again at each occurrence.

| Scan | Line or inscription | Visible strokes | LaTeX reading | Other readings or qualification |
|---|---|---|---|---|
| 428 | first display | doubled ascending left stroke of N; small raised ring | `\mathbb N^{\circ}` | o also possible |
| 428 | first display | underlined t and capital T followed by descending y | `\uline{t}, \uline{\mathrm{Ty}}` | upright/variable y indistinct |
| 428 | choice, displays 2–3 | open triangular letter with small signs below the baseline | `\Delta_+, \Delta_-` | — |
| 428 | lower, after «objet de» | large curved capital with inner stroke | `\mathbb C` | \mathcal C |
| 428 | lower, «si c est de type» | short horizontal cap and bent descender; wave above c | `\tau, \widetilde c` | — |
| 428 | last two lines | small following stroke high on c or w | `c', w'` | — |
| 429 | large diagram, vertical edges | rounded u, narrower v, doubled bowl of w with small prime | `u,v,w'` | — |
| 429 | large diagram, upper and lower braces | wave above c and prime grouped underneath | `\widetilde{c'}, \widetilde c` | — |
| 429 | «Ainsi», first group | bent stem like a brace; following letter with a long curved tail | `\xi_u, \eta_v` | y for the second |
| 429 | «Ainsi», product in third line | circles in first two lines, stars in third | `\circ, *` | — |
| 429 | lower, two opposed functors | closed loop with central stem; shallow fork | `\varphi, \psi` | — |
| 429 | lower, «où» | descending loop followed by a low c | `\rho_c` | — |
| 429 | two functor displays | open C with a single outline, subscript double-stroked N and raised ring | `C_{\mathbb N^\circ}` | superscript o |
| 430 | paragraph «Cela prouve» | curled C with retraced top, alongside plain open C in the paragraph above | `\mathcal C` | \mathbb C |
| 430 | paragraph «Pour la propreté» | three raised letters with two tall second stems | `{}^{\mathrm{opp}}` | — |
| 430 | diagram and «le composé» | straight line across w and prime, distinct from wavy mark on c | `\overline{w'}, \widetilde{c'}` | — |
| 430 | paragraph «On doit» | a raised round mark on the N | `\mathbb N^\circ` | \mathbb N^o |
| 431 | factorization, right annotation | capital H followed by ot and a shortened équiv. | `\text{Hot-équiv.}` | — |
| 431 | central column, «chemins» | spiral at the head of capital C | `\mathcal C_X` | \mathbb C_X |
| 431 | lower square, projections | small pr, numeral at foot, X above; diagonal beta | `\mathrm{pr}_2^X, \mathrm{pr}_1^X, \beta_X` | — |
| 431 | first paragraph after break; «chemins» | paired upper strokes each side | `two grave accents at opening, two apostrophes at closing` | — |
| 431 | upper factorization; diagonal diagram | a straight stroke over X prime or f; i followed by a lowered letter | `\overline{X'},\overline f,i_X,i_f` | — |
| 432 | sole display | beta with two lobes; two bracket-like strokes under parts of the composites | `\beta, \underset{…}{…}` | The undersigned lines have turned-up ends. |
| 432 | display, last equality | small «déf» immediately above the two bars | `\overset{\text{déf}}{=}` | — |
| 432 | «Je rappelle», section labels | dotted i and X or f lower down | `i_f,i_X` | — |
| 432 | «C'est une», projection | small horizontal loop with right spur, subscript X | `\sigma_X` | — |
| 433 | title, below the parenthesis | Roman V and three vertical strokes, between two rules | `\overline{\uline{\mathrm{VIII}}}` | — |
| 433 | line printer showing through, repeated rows | G shaped cells and U shaped cells | `monospaced G and U` | — |
| 434 | heading and first paragraph | numeral 1 attached by hyphen to type, pointed mark on S | `1-type, \hat S` | — |
| 434 | first paragraph and top two displays | small raised loop beside S | `S^\circ` | S^o |
| 434 | centre, fundamental groupoid | two straight uprights joined above; small angled x and low s | `\Pi(X_s)` | — |
| 434 | bottom annotated functor | letter like open G followed by rp, rule underneath the letters; angular HOT | `\uline{\mathrm{Grp}}(S), \mathrm{HOT}(S)` | Hot |
| 434 | last line | single-stroke R, stars below the baseline, undulating upper stroke in equality | `R(gf)_*,\simeq` | — |
| 435 | second display | short upright with separate dot at the foot of f | `f_!` | — |
| 435 | «ayant comme fibres» and slanted margin | oblique separating slash runs down to the right; wavy mark on X | `{}_{s}\backslash X, \widetilde X` | — |
| 435 | «En fait», fibre diagram | s with lowered oval after it; opposed i and j arrows, j with tail | `X_{s_0},i,j` | — |
| 435 | margin, next to i | «déf» over equals; Pi with flat top | `\overset{\text{déf}}{=},\Pi` | — |
| 435 | near bottom «peut lui associer» | raised round mark on T | `T^\circ` | T^o |
| 436 | upper display and middle boxed line | subscript straight stem plus separate point on f | `f_!` | — |
| 436 | boxed line and prose underneath | slash in X/T in the box, lower short separator between X and T in prose | `\Pi(X/T),\Pi(X,T)` | — |
| 436 | last line | a top bar with a downstroke and short right end | `\Pi (left), \Gamma (right)` | \Gamma, \mathscr T (left); \mathscr T, \mathrm I (right) |
| 436 | «trivialement» | loop marked over more than once, followed by a small X | `e_X` | — |
| 437 | top, «où» and boxed formula | capital with vertical stroke, foot curving back and flat top; left copy reinforced | `\Gamma` | \mathscr T at the opening; \Gamma' or C inside the box |
| 437 | theorem, boxed formula | One rule under each Hom and a separate rule under each subscript Grp. Star high, exclamation low. | `\uline{\mathrm{Hom}}_{\uline{\mathrm{Grp}}},f^*,f_!` | — |
| 437 | two adjunction arrows, at right | membership and a capital O followed by b | `\in\mathrm{Ob}` | — |
| 437 | lower right, result of last equality | angled reverse slash following s | `\Pi({}_{s}\backslash G)` | — |
| 438 | first line; under first display | raised pen stroke on f and the larger star in the diagram | `f' or f^*; f^*` | ambiguous in first line |
| 438 | first diagram, lower left | t hangs below a reverse slash, inside the parentheses of Pi | `\Pi({}_{t}\backslash f^*(H))` | — |
| 438 | struck projection | small pr with a low numeral, star at the upper right of f | `\mathrm{pr}_2,f^*` | — |
| 438 | bottom, under Pi | short double vertical and «def» | `vertical equality labelled def` | — |
| 439 | change-of-base square | small curved arrow towards upper left, beside a hooked letter | `\gamma` | r |
| 439 | bottom diagram | upright primes high beside f and S, exclamation below f, star above q | `f'_!,q^*,S'` | — |
| 439 | after «Par adjonction» | isolated two parallel horizontal strokes after «au» | `=` | même (shorthand) |
| 439 | top sentence and after «trouver un» | small T and dash written above with slanting join to baseline | `\inserted{T-}` | — |
| 440 | theorem, beside 1-lisse | hook identical to label of previous square | `\gamma` | r |
| 440 | question on 2-foncteur, display and following Hom | two distinct rules under Grp; one under Hom | `\uuline{\mathrm{Grp}},\uline{\mathrm{Hom}}` | — |
| 440 | rotated left margin, last line | right-angled cap on a vertical stroke, underlined | `\uline{\Gamma}` | \uline{\mathscr T} |
| 440 | paragraph «fourbis» | broad vertical and curved right side, retraced upright in D | `\mathbb D` | \mathrm D |
| 440 | left margin, fidelity index | small dotted upright before fidélité and in the brace condition | `i` | — |
| 441 | definition, line with «triviaux» | lower-case pi, a low 0 and a dotted i, plain intervening dash | `\pi_0(Z)\mathrel{-}\pi_i(Z)` | — |
| 441 | «En fait» | two horizontal ends and doubled diagonal of Z; two distinct left strokes in D | `\mathbb Z,\mathbb D_i` | \mathrm D_i |
| 441 | range after «En fait» | square bracket opening to the right at both ends | `[-1,+\infty[` | — |
| 441 | last theorem | circled 1 and circled 2; low dotted i in derived terminology | `\textcircled{1},\textcircled{2},\mathbb D_i` | — |
| 442 | top, after « si » | underlined Grp, angular G; two peaks in Ob, no second vertical | `\uline{\mathrm{Grp}}` | — |
| 442 | upper, t∈T and restriction | small t below G and S; capital T has a heavy cap | `G_t,\ S_t,\ T` | — |
| 442 | middle, clause 3 | narrow Z with short baseline; prefixes inserted via caret | `Z,\ Z\text{-}` | — |
| 442 | lower, after « le foncteur » | raised star, thin baseline u, no descender | `u^*` | — |
| 434 | arrow between HOT and Grp | Two different pen movements for the variable; the second is nearly vertical. | `\xi\mapsto\Pi(\xi/S)` | \zeta before the arrow; f or a single vertical after the opening parenthesis. |
| 428 | after the two choices | Paired initials in the exponent of the new type | `\text{qq chose}` | Probable shorthand for quelque chose. |
| 433 | reverse, title-line and six records | Fixed-pitch capitals. Offset shadows affect multiple characters together. | `GUTS; 0070 0001 M06` | No separate bold alphabet inferred. |
| 434 | after X → X′ | Hot- immediately precedes a shortened equivalence word | `Hot-équiv` | More than one punctuation form occurs. |
| 434 | bottom, three functor letters | The R of R(gf), the R of Rg and the R of Rf each have a single stem. | `R, R, R` | The heavier nearby HOT heading is separately recorded above. |
| 435 | at s\X and the low t at the foot | Small left-hand letter lowered immediately before a backslash | `{}_{s}\backslash X, {}_{t}\backslash G` | Retain this lower placement on the succeeding sheets. |
| 436 | below the transitivity box | The in-line separator is bent and short, distinct from the long oblique in the box | `\Pi(X,T)` | Compare the slash in the box itself. |
| 437 | right of the two arrow lines | Large H with two separate stems and one crossbar | `H` | No doubled left stroke in the two head letters. |
| 440 | after « i-fidélité », and last lines | A short pair of horizontal strokes stands where the prose can use même. | `=` | Expansion is confined to the editorial apparatus. |
| 441 | at « Si … » and in both alternatives | A dotted short stem, with one shorter horizontal and a 1 | `(i-1)` | The index letter does not descend like j. |
| 442 | after f*(H), before pour tout | Three small successive s-like strokes written together | `sss` | The following criterion gives the expansion si et seulement si. |
| 442 | corollary, “verticale” | Two elevated strokes on each side of the word | <code>``verticale''</code> | Both signs are doubled quotation marks. |

## Individual doubts

Each mark has one row, including repeated places in the six damaged printer records. Confidence describes the first reading. For an illegible passage the number is an estimate of the words or fields. The short phrase in the location column is a search aid. Percentages give the approximate extent of the containing block; the line refers to the individual page file.

| Scan | Location | Reading | Other candidates | Confidence | Context and reason |
|---|---|---|---|---|---|
| 428 | 6–17% from top, TeX l. 6 (mark 1) · `même argument que tantôt,` | `mais` | — | medium | The dark cancellation still leaves the humps of « mais ». The following « je présume » could stand without it. |
| 428 | 6–17% from top, TeX l. 6 (mark 2) · `plication technique. Nous` | 1 unreadable word/field | — | low | One small covered word after « Nous ». The clause already has a finite verb in « avions pris » and supplies no unique restoration. |
| 428 | 19–23% from top, TeX l. 9 (mark 3) · `\[ t}\colon\mathbb{N}^` | `\circ` | `o` | medium | The same round high mark returns with N on 429–430. Its position favours an opposite-category mark. It does not distinguish a circle from the letter o. |
| 428 | 19–23% from top, TeX l. 9 (mark 4) · `ure{\circ\|o}}\longrightarrow` | `\mathrm{Ty}` | `\mathrm{T}y` | medium | The long descender is y, and the term « type » supports Ty. Its italic or upright styling is less clear. |
| 428 | 33–35% from top, TeX l. 18 (mark 5) | `où` | `ou` | medium | The introductory alternative favours « ou » without an accent. A separate pen mark sits above the initial word. |
| 428 | 36–39% from top, TeX l. 21 (mark 6) · `\[ t_n=(\Delta_+\Delta_` | `+` | `-` | low | The signs in the first choice and in the later padding formula favour minus. Here a short stroke crosses the horizontal. |
| 428 | 40–98% from top, TeX l. 24 (mark 7) · `car tous` | `les` | — | medium | The immediately following live « les » suggests an abandoned first copy. The body of the first word is inked in. |
| 428 | 40–98% from top, TeX l. 24 (mark 8) · `leted{les}} les $t_n$ sont` | `à` | `:` | low | The line joins the type to its initial direction. A preposition fits, but the two separate marks could be punctuation. |
| 428 | 40–98% from top, TeX l. 24 (mark 9) · `les}} les $t_n$ sont à\|:` | `direction` | `de variation` | low | The pair « initiale … terminale » supports « direction ». Little more than a rising stem and a run of humps remains. |
| 428 | 40–98% from top, TeX l. 24 (mark 10) · `en $t_n=(\Delta_-\Delta_+)^` | `qq chose` | — | medium | The exponent is a phrase in small, fast letters. The high position and the later choices of exponent favour « qq chose ». |
| 428 | 40–98% from top, TeX l. 24 (mark 11) · `onc pour définir $\widetilde c$ en` | `termes` | `terme` | low | The same phrase a few lines later gives no decisive plural ending. A terminal s would coincide with the long horizontal. |
| 428 | 40–98% from top, TeX l. 24 (mark 12) · `mes\|terme} de $c$, comme objet de $` | `\mathbb{C}` | `\mathcal{C}` | medium | The large C has a second left-hand stroke. The superscript/subscript setting supplies no alphabetic distinction. |
| 428 | 40–98% from top, TeX l. 24 (mark 13) · `_{\mathbb{N}^{\circ}}$,` | `il` | — | low | A doubled « il » before « faudra » is possible. Only the surviving first stroke supports it. |
| 428 | 40–98% from top, TeX l. 24 (mark 14) · `enant $t_{n+1}=(\Delta_+\Delta_-)^` | `2n` | `2m` | medium | n matches the index and the earlier exponent. The second hump at the end could also be m. |
| 428 | 40–98% from top, TeX l. 24 (mark 15) · `Delta_-)^{2n\|2m}})$, et de` | `$=$` | `même` | high | Two straight horizontals are distinct. « de même » is the natural expansion in this sentence. |
| 428 | 40–98% from top, TeX l. 24 (mark 16) · `detilde{c'}$ en terme de $c'$. Les` | `dispositions` | `définitions` | low | Both words have an initial d and a tall internal stem. « pertinentes » does not decide between them in this abandoned construction. |
| 428 | 40–98% from top, TeX l. 24 (mark 17) · `\|définitions} pertinentes` | `sont décrites` | — | low | « est décrit » on the next line supports a discarded form of décrire. The long cancellation obscures its ending. |
| 428 | 40–98% from top, TeX l. 24 (mark 18) · `w')$ à $(\widetilde{c'},\widetilde` | `w'` | `w_*` | low | The neighbouring pair (c′,w′) supports a prime; the ink beside the tilde-bearing w also admits a small low star. |
| 429 | 29–44% from top, TeX l. 24 (mark 1) · `ed} \widetilde c&=\xi_u\circ c\circ` | `\eta` | `y` | medium | The pair ξ_u,η_v recurs in the right column. The curved descender also resembles a roman y. |
| 429 | 29–44% from top, TeX l. 25 (mark 2) · `c\circ\eta\|y}_v\\` | `c'` | — | low | Only a short hooked mark can be distinguished inside the ink above the second line. |
| 429 | 29–44% from top, TeX l. 26 (mark 3) · `\\ \widetilde{w'}&=\lambda(u)*w*\mu` | `w)` | `(v)`, `(w)` | low | The factor below is associated with v; that favours (v). The actual stroke after μ has two humps and no clear opening parenthesis. |
| 429 | 29–44% from top, TeX l. 30 (mark 4) · `ght. &\quad \begin{aligned} &` | `où` | — | medium | The right block introduces the definitions of the factors. « où » fits this position; the accent is very slight. |
| 429 | 29–44% from top, TeX l. 34 (mark 5) · `\}\ \substack{type` | `\tau` | — | low | The adjacent label « type » supports τ, but the marking after that word is scuffed. |
| 429 | 29–44% from top, TeX l. 37 (mark 6) · `aligned} \lambda(u)&\colon` | `\xi_u` | — | low | The target ξ_u gives a candidate for this abandoned start. The overwritten source does not identify every letter. |
| 429 | 29–44% from top, TeX l. 38 (mark 7) · `a_+\Delta_-}\longrightarrow\xi_u\\` | `\lambda` | `\mu` | medium | The first arm matches the λ on the preceding line, while the formula at left favours μ for the v-side. |
| 429 | 49–52% from top, TeX l. 46 (mark 8) · `On trouve ainsi,` | `mutatis mutandis` | — | medium | Two groups with the expected two tall stems follow « ainsi ». They fit « mutatis mutandis », but the middle letters run together. |
| 429 | 54–59% from top, TeX l. 49 (mark 9) · `\[ C_` | `\mathbb{N}` | — | low | There is one clear doubled N immediately to the right of the scribble. The first attempt may have been another N. |
| 429 | 54–59% from top, TeX l. 49 (mark 10) · `ed{\mathbb{N}}}\mathbb{N}^` | `\circ` | `o` | medium | The round mark on the other N's in the two arrows supports a degree-like circle. A small o has the same outline. |
| 429 | 61–64% from top, TeX l. 54 (mark 11) · `et on` | `définit` | — | medium | The leftward ψ that follows is being introduced; « définit » fits. The end of the verb is retraced. |
| 429 | 69–82% from top, TeX l. 61 (mark 12) · `ainsi : à $(c'',w'')$` | `de` | `dans` | low | The next object is the category containing the pair. Either de or dans fits; the word ends in one short drag. |
| 429 | 69–82% from top, TeX l. 61 (mark 13) · `rémités fixes, on associe` | `$w'$` | — | low | A loop and a high mark survive before the live (c′,w′); their positions fit w′. |
| 429 | 84–86% from top, TeX l. 64 (mark 14) · `\[` | `c'` | `d` | medium | The preceding pair asks for c′. At the left edge of the equality the shape can be read as a single d. |
| 429 | 94–98% from top, TeX l. 73 (mark 15) · `est défini de façon` | `similaire` | — | medium | The preceding figure supplies a similar definition. « similaire » fits the visible long ascender and ending. |
| 430 | 7–17% from top, TeX l. 10 (mark 1) · `w[d,"v"] \& \widetilde c\quad` | `type` | — | medium | The annotation associates a t with the upper path. The small word looks like « type » with a heavily retraced opening. |
| 430 | 7–17% from top, TeX l. 11 (mark 2) · `quadtype} }t_{n+1}\\` | `a` | `a'` | low | The object in the next two columns is a. A black spur prevents excluding a prime at the first copy. |
| 430 | 19–44% from top, TeX l. 15 (mark 3) · `ur $\psi\varphi$ de $C_{\mathbb N^` | `\circ` | `o` | medium | The earlier categories on 429 carry the same high ring. Its roundness alone admits o. |
| 430 | 19–44% from top, TeX l. 15 (mark 4) · `)$ est homotope à l'identité. Mais` | `ce` | — | medium | The following « foncteur » supplies the referent. The initial c/e is overwritten. |
| 430 | 19–44% from top, TeX l. 15 (mark 5) · `\Delta_-}\,c'\,b'_{\Delta_+\Delta_` | `+` | `-` | low | The upper path on 429 favours a minus after the second Δ. In this occurrence the bar has a thick upstroke. |
| 430 | 19–44% from top, TeX l. 15 (mark 6) · `line{w'})$, où $\overline{w'}$ est` | `encore` | `le lien` | low | « le composé » in the following line favours « encore ». A separate oblique stroke could start « le lien ». |
| 430 | 66–93% from top, TeX l. 31 (mark 7) · `Cela prouve la lissité de $` | `\mathcal C` | `\mathbb C` | medium | The head curls in on itself above a single outer contour. The doubled body of the first C on 428 and the plain C preceding (c,u,v) here offer two different comparisons. No local word distinguishes the alphabets. |
| 430 | 66–93% from top, TeX l. 31 (mark 8) · `hcal C\|\mathbb C}_{\mathbb N^\circ` | `\mathrel{-}` | `\longrightarrow` | high | A map to X×X fits the prose. The line itself has no clear point. |
| 430 | 66–93% from top, TeX l. 31 (mark 9) · `thrm{opp}}=t}$, et` | `il` | — | low | The syntax supports il before « suffit ». The letter group is struck. |
| 430 | 66–93% from top, TeX l. 31 (mark 10) · `er ce qu'on a déjà prouvé` | `pour` | — | low | « au cas » replaces a possible « pour ». The cross-stroke covers the centre. |
| 430 | 66–93% from top, TeX l. 31 (mark 11) · `r voir que $\mathcal C_{\mathbb N^` | `\circ` | — | low | The earlier N on this page carries a high ring. Here there is scarcely more than a spot. |
| 430 | 94–99% from top, TeX l. 33 (mark 12) · `e le lemme à prouver. Ça doit être` | `essentiellement` | — | medium | The first word on 431, « trivial », completes the sense. The ending of « essentiellement » runs towards the edge. |
| 431 | 3–9% from top, TeX l. 5 (mark 1) · `trivial, et je` | `renonce` | — | medium | « à rédiger une démonstration » fits « renonce ». Several central strokes have coalesced. |
| 431 | 27–33% from top, TeX l. 10 (mark 2) · `\[ X'\overset{i_f` | `\mathrel{-}` | `\longrightarrow` | high | The pair of arrows is a factorization, which favours a forward arrow. This first line ends in a dot-like thickening. |
| 431 | 47–65% from top, TeX l. 17 (mark 3) · `_X\ Hot-équiv.}"]\\` | `X` | — | low | The letter before the curled C_X is crossed over itself. X is only a shape-based possibility. |
| 431 | 47–65% from top, TeX l. 17 (mark 4) · `ot-équiv.}"]\\ X` | `\mathcal C` | `\mathbb C` | medium | The terminal curl resembles the one on 430. Its outer edge is less clearly doubled than the competing letter on 428. The more open copy below lacks that curl. |
| 431 | 73–91% from top, TeX l. 26 (mark 5) · `\& {}\simeq X'\times_X(C_X,\sigma=` | `\mathrm{pr}_1p_X` | `\mathrm{pr}_1\circ p_X` | low | The marginal formula writes an explicit composition circle; the cramped main diagram may instead use juxtaposition. |
| 431 | 94–98% from top, TeX l. 36 (mark 6) · `son image inverse sur $X'\times X$` | `soit` | — | low | This sounds like the introduction of a name for the pullback. The last pen movement in « soit » is small. |
| 431 | 94–98% from top, TeX l. 36 (mark 7) · `part $pr}_2^X\circ f'$ est` | `le` | `la` | low | The next sheet starts with « projection », favouring la. The article at the edge of this sheet is open. |
| 432 | 16–21% from top, TeX l. 9 (mark 1) · `.35pt}{.5ex}}}{f')\circ p_{X,f}} =` | `\bigl((` | `\bigl(` | low | Two curves and an oblique near the second equality overlap. The factorization calls for grouping but cannot settle the number drawn. |
| 432 | 16–21% from top, TeX l. 9 (mark 2) · `.35pt}{.5ex}}}{pr}_2^X(p_X` | `)` | `\}` | low | The same group ends at the vertical projection label. A curled right stroke could be a brace or a parenthesis. |
| 432 | 22–49% from top, TeX l. 13 (mark 3) · `Je rappelle que` | `$q_f$` | — | low | The live section is i_f. In the struck start the first loop looks like q with a lower attachment. |
| 432 | 22–49% from top, TeX l. 13 (mark 4) · `la section $i_X$ de $(C_X,` | `\sigma_X` | — | low | The next line identifies σ_X explicitly. The mark within the parentheses is cancelled. |
| 432 | 22–49% from top, TeX l. 13 (mark 5) · `est aussi une Hot-équivalence, et` | `ladite` | `toute` | low | « toute » would give a statement about any section. The compressed modifier also fits « ladite », referring to this section. |
| 433 | 3–6% from top, TeX l. 5 (mark 1) · `ading orientation //*\quad` | `GUTS` | `GGTS` | medium | The clearer printer rows say GUTS. Part of the corresponding title-line field is covered by dark manuscript ink. |
| 433 | 3–6% from top, TeX l. 5 (mark 2) · `t{//*\quad GUTS\|GGTS}\quad` | `0124` | `0I24` | low | The faint monospaced second character could be the digit 1 or an I. The surrounding print offers no sure distinction. |
| 433 | 3–6% from top, TeX l. 5 (mark 3) · `GGTS}\quad 0124\|0I24}\quad` | `I` | `1` | low | The isolated monospaced upright has no surviving feature to distinguish I from 1. |
| 433 | 10–16% from top, TeX l. 9 (mark 4) · `(intégration des` | `champs` | — | medium | The title on 434 and its body use « champs en groupoïdes ». On the cover the middle letters are faint and connected. |
| 433 | 49–59% from top, TeX l. 35 (mark 5) · `\quad GUTS\quad 0070 0001 M06}\quad` | 3 unreadable words/fields | — | low | Three approximate field-sized groups fade into the background after M06. Other repetitions do not give a secure restoration. |
| 433 | 49–59% from top, TeX l. 35 (mark 6) · `70 0001 M06}\quad\illegible{3}\quad` | `MOR` | `MOB` | low | The far edge cuts the last character; there are traces consistent with both R and B. |
| 433 | 49–59% from top, TeX l. 36 (mark 7) · `\quad GUTS\quad 0070 0001 M06}\quad` | 3 unreadable words/fields | — | low | The second impression has offset shadows after M06. No complete field can be recovered. |
| 433 | 49–59% from top, TeX l. 36 (mark 8) · `70 0001 M06}\quad\illegible{3}\quad` | `MOR` | `MOB` | low | The edge again cuts the last bowl; neither reading is independently supported. |
| 433 | 49–59% from top, TeX l. 37 (mark 9) · `\quad GUTS\quad 0070 0001 M06}\quad` | 3 unreadable words/fields | — | low | The third row has the same clear prefix, followed by indistinguishable type impressions. |
| 433 | 49–59% from top, TeX l. 37 (mark 10) · `70 0001 M06}\quad\illegible{3}\quad` | `MOR` | `MOB` | low | Both final letters fit the upright and partial loop in this row. |
| 433 | 49–59% from top, TeX l. 38 (mark 11) · `\quad GUTS\quad 0070 0001 M06}\quad` | 3 unreadable words/fields | — | low | Only the positions of the fields after M06 survive in row four; their contents cannot be read. |
| 433 | 49–59% from top, TeX l. 38 (mark 12) · `70 0001 M06}\quad\illegible{3}\quad` | `MOR` | `MOB` | low | Neither the visible end nor the repeated rows determine the final letter. |
| 433 | 49–59% from top, TeX l. 39 (mark 13) · `\quad GUTS\quad 0070 0001 M06}\quad` | 3 unreadable words/fields | — | low | Three groups of underlying impressions are estimated in the fifth row. Their letters are too washed out. |
| 433 | 49–59% from top, TeX l. 39 (mark 14) · `70 0001 M06}\quad\illegible{3}\quad` | `MOR` | `MOB` | low | The last partial letter can close like B or break like R. |
| 433 | 49–59% from top, TeX l. 40 (mark 15) · `\quad GUTS\quad 0070 0001 M06}\quad` | 3 unreadable words/fields | — | low | The sixth line fades immediately after the common prefix. The field count is approximate. |
| 433 | 49–59% from top, TeX l. 40 (mark 16) · `70 0001 M06}\quad\illegible{3}\quad` | `MOR` | `MOB` | low | The printer line again runs off the edge; the other ends are clipped at the same position. |
| 434 | 9–22% from top, TeX l. 7 (mark 1) · `tiellement aux contrafoncteurs $S^` | `\circ` | `o` | medium | The small elevated ring belongs to S in the contrafunctor, as on the following display. It could equally be written o. |
| 434 | 9–22% from top, TeX l. 7 (mark 2) · `ntrafoncteurs $S^{\circ\|o` | `\mathrel{-}` | `\longrightarrow` | high | Source and target are given, supporting an arrow. The ink between them is a plain horizontal. |
| 434 | 9–22% from top, TeX l. 7 (mark 3) · `erted{(Dans $(Cat` | `\mathrm{fib}` | — | low | The correction lies between Cat and the slash; the remaining fib below the closing parenthesis supports this reading. |
| 434 | 27–32% from top, TeX l. 11 (mark 4) · `Si` | `$S$` | — | low | An S-like coil follows « Si ». It is heavily covered and no longer part of the sentence. |
| 434 | 44–48% from top, TeX l. 24 (mark 5) · `S^\circ\longrightarrow(Gr` | `p` | `po` | low | The following caption « cat. des groupoïdes » supports Grp, but the pen continues into the cancellation. |
| 434 | 44–48% from top, TeX l. 24 (mark 6) · `w(Gr}p\|po` | `\mathrm{d}` | — | low | A final upright and short loop survive after Grp. The old ending is unclear. |
| 434 | 48–54% from top, TeX l. 28 (mark 7) · `ïde fondamental de $X_s$.` | `Il est` | — | low | These words are at the far right before the new start « Je note ». The cancellation obscures the second word. |
| 434 | 48–54% from top, TeX l. 28 (mark 8) · `deleted{Il est` | `Je` | — | medium | The continuation « note la » supports the inserted subject Je. |
| 434 | 48–54% from top, TeX l. 28 (mark 9) · `rted{Je}} note la` | 1 unreadable word/field | — | low | A single covered word follows « la » before the live « cat. fibrée ». Nothing elsewhere supplies its letters. |
| 434 | 48–54% from top, TeX l. 28 (mark 10) · `$S$ par $\Pi(X/S).}$ Il est` | `vrai` | — | medium | The movement at the right fits « vrai », followed by a restarted, cancelled word at the left. |
| 434 | 48–54% from top, TeX l. 28 (mark 11) · `).}$ Il est vrai` | `vrai` | — | medium | The crossed word at the start of the next line resembles the end of the preceding phrase. |
| 434 | 57–62% from top, TeX l. 34 (mark 12) · `at. fibrées sur $S$} qui` | `induit` | `induise` | low | Both endings are possible under the final stroke. The following « qui » clause does not uniquely determine the mood. |
| 434 | 66–72% from top, TeX l. 40 (mark 13) · `mais non un iso. Il y` | `aura` | `a` | low | The published form of the sentence is irrelevant here. The crossed ending allows either the longer or shorter live verb. |
| 434 | 66–72% from top, TeX l. 40 (mark 14) · `iso. Il y aura\|a` | `it` | `urait` | low | The surviving beginning depends on the preceding doubt; the ending continues under one horizontal stroke. |
| 434 | 66–72% from top, TeX l. 40 (mark 15) · `c du travail à faire pour` | `associer à` | — | low | « un foncteur » in the new version does not require a particular abandoned infinitive. |
| 434 | 72–85% from top, TeX l. 43 (mark 16) · `nt=\&,column sep=12mm] \underbrace` | `\mathrm{HOT}` | `\mathrm{Hot}` | medium | The categorical name is given underneath. The first and last strokes look like capitals; the middle one is retouched. |
| 434 | 72–85% from top, TeX l. 44 (mark 17) · `relatifs sur }S}} \arrow[r,"` | `\xi` | `\zeta` | low | The long descending curl before the mapping arrow allows xi or zeta. Its counterpart in the argument of Π has fewer strokes. |
| 434 | 72–85% from top, TeX l. 44 (mark 18) · `w[r,"{\xi\|\zeta}\mapsto\Pi(` | `\xi` | `f`, `\vert` | low | The position after Π favours a repetition of the first variable. The ink is a nearly straight falling stroke, allowing a long f or a bar as well. |
| 434 | 72–85% from top, TeX l. 45 (mark 19) · `des}\\groupoïdes}\\` | `f` | — | low | The word beneath Grp is « fibrés ». Its opening was begun a second time. |
| 434 | 86–97% from top, TeX l. 49 (mark 20) · `ansitivité en homotopie` | `ou où on voit bien` | `ou ce qui serait bien` | low | Several separated strokes end in « bien ». The comparison with cohomology motivates both candidate phrasings. |
| 434 | 86–97% from top, TeX l. 49 (mark 21) · `en\|ou ce qui serait bien` | 1 unreadable word/field | — | low | There is one densely crossed word in the last line, distinct from the inserted comparison. |
| 434 | 86–97% from top, TeX l. 49 (mark 22) · `\illegible{1` | `analogue à` | — | medium | The formula after the small added words is the comparison, supporting « analogue à ». |
| 435 | 7–10% from top, TeX l. 8 (mark 1) · `\[ f\colon S` | `\mathrel{-}` | `\longrightarrow` | high | The subsequent text calls f a functor from S to T. The drawn segment has a blunt end. |
| 435 | 11–13% from top, TeX l. 11 (mark 2) · `est un foncteur,` | `tout` | — | low | The word after « foncteur » is crossed before « on va ». Its tall first stroke could begin « tout ». |
| 435 | 30–51% from top, TeX l. 23 (mark 3) · `lconque} (pas néc. Cat-fibrée), on` | `peut associer` | `lui associe` | medium | The new construction is being assigned to X. The first word at the beginning of this line resembles « peut ». |
| 435 | 30–51% from top, TeX l. 23 (mark 4) · `ie fibrée $\widetilde X^` | `(S)` | `S` | low | S is certain. A shortened curve on either side of it might be a parenthesis or a pen connection. |
| 435 | 30–51% from top, TeX l. 23 (mark 5) · `ow {}_{s'}\backslash X$).` | `Si $X$ est déjà` | — | low | X and a final tall stroke survive on the cancelled start. « Si X est déjà » anticipates the condition written below. |
| 435 | 46–67% from top, TeX l. 25 (mark 6) · `\margin{Ayant $\widetilde X$, on` | `peut définir` | `définit` | low | The body of the margin note runs into the main cancellation. The ensuing defining equality favours définir. |
| 435 | 50–54% from top, TeX l. 30 (mark 7) · <code>rset{``}s''</code> | `p'` | — | low | A p-like letter below the overwriting belongs to the first occurrence of p(x) in the identity arrow. |
| 435 | 55–63% from top, TeX l. 33 (mark 8) · `-Hot-}équivalence si $X$` | `était` | — | medium | « déjà fibrée » gives a past-condition reading. The middle strokes of the verb are overdrawn. |
| 435 | 55–63% from top, TeX l. 33 (mark 9) · `en chaque fibre c'est un` | `équivalé` | — | low | The crossed word starts équi-; the rest is directly under the horizontal. |
| 435 | 55–63% from top, TeX l. 33 (mark 10) · `est un équivalé` | `homotopisme` | — | medium | The maps i and j and the homotopy labelled below favour « homotopisme ». The final letters are abbreviated. |
| 435 | 64–69% from top, TeX l. 39 (mark 11) · `mathrm{id}$, $ij\xrightarrow[` | `simple` | — | low | There is a much smaller word beneath « homotopie ». Its middle is too dark to distinguish securely. |
| 435 | 79–85% from top, TeX l. 47 (mark 12) · `une catégorie fibrée sur $` | `S` | — | low | The live letter is T; the curve under its cap could be a preceding S. |
| 435 | 79–85% from top, TeX l. 47 (mark 13) · `$S}}T$,` | `p` | — | low | A small isolated crossed loop follows the comma before « mais ». A p is a tentative reading. |
| 435 | 84–88% from top, TeX l. 50 (mark 14) · `mapsto {}_{t}\backslash G\qquad T^` | `\circ` | `o` | medium | The functor proceeds from the opposite of T; the drawn high circle can also be a small o. |
| 435 | 84–88% from top, TeX l. 50 (mark 15) · `kslash G\qquad T^{\circ\|o` | `\mathrel{-}` | `\longrightarrow` | high | The phrase « peut lui associer » favours a functorial arrow. There is only a short vertical at its end. |
| 435 | 88–94% from top, TeX l. 53 (mark 16) · `de prendre les` | `directmt` | `directement` | low | The raised addition clearly starts direct-. Its end could be an abbreviation without all intervening letters. |
| 435 | 95–99% from top, TeX l. 59 (mark 17) · `qui` | `est` | — | low | The preceding start « qui » fits an abandoned « est »; the surviving strokes do not fix the word. |
| 435 | 95–99% from top, TeX l. 59 (mark 18) · `définit} une` | `champ` | — | low | The replacement « catégorie fibrée » follows a crossed group beginning like ch-. Context allows champ. |
| 436 | 4–9% from top, TeX l. 5 (mark 1) · `trouve bien un foncteur (en fait,` | `$=$` | `même` | medium | The two horizontal strokes are legible. The parenthesis intensifies the functor claim, which could motivate « même ». |
| 436 | 20–25% from top, TeX l. 17 (mark 2) · `est un` | `hom` | `lien` | low | The word introduces an arrow of fibred groupoids; hom fits the use, while the visible strokes also look like lien. |
| 436 | 26–29% from top, TeX l. 20 (mark 3) · `\[ f_!(u)\colon f_!(` | `G` | `u` | medium | The domain of u is G, supporting G. The source letter under the bang is very small and compressed. |
| 436 | 26–29% from top, TeX l. 20 (mark 4) · `\[ f_!(u)\colon f_!(G\|u})` | `\mathrel{-}` | `\longrightarrow` | high | A map is named on the left. Between the two objects the manuscript gives a blunt line. |
| 436 | 54–63% from top, TeX l. 31 (mark 5) · `alors une $T$-équivalence` | `can` | — | low | The small isolated word next to the box fits « can » for canonical. Its final letter is unclear. |
| 436 | 58–67% from top, TeX l. 34 (mark 6) · `\bigl(\Pi(X/S)\bigr)\simeq` | `g` | — | low | A dark hook hangs below the live left leg of Π. It may be an earlier g. |
| 436 | 84–88% from top, TeX l. 42 (mark 7) · `\[ \Pi(X/S)=p_!(` | `e` | — | medium | The very next line defines e_X. The e in the displayed equation has been gone over again. |
| 436 | 96–99% from top, TeX l. 48 (mark 8) · `\[ f_` | `*` | — | low | The final line clearly needs a low mark on f. The old mark next to the bang looks like a small star. |
| 436 | 96–99% from top, TeX l. 48 (mark 9) · `f_{*}}!}\bigl(p_!(` | `\Pi` | `\Gamma`, `\mathscr T` | low | This first small sign has a cap and a short right leg. The next sheet calls the object Γ-like; neither comparison identifies this drawing securely. |
| 436 | 96–99% from top, TeX l. 48 (mark 10) · `mma\|\mathscr T})\bigr)\simeq(fp)_!(` | `\Gamma` | `\mathscr T`, `\mathrm{I}` | low | The lower-left foot need not belong to a Greek letter. Compare the two different forms on the following page. |
| 437 | 5–11% from top, TeX l. 5 (mark 1) · `où $` | `\Gamma` | `\mathscr T` | low | The object is named by a one-sided cap over a vertical. Greek Γ and a manuscript T remain possible. |
| 437 | 5–11% from top, TeX l. 5 (mark 2) · `suggère de généraliser la formule` | `cas` | `bis` | low | Two or three humps between « formule » and « en » cannot be securely divided into letters. |
| 437 | 11–16% from top, TeX l. 8 (mark 3) · `\[ (fp)_!(` | `\Gamma` | `\Gamma'`, `C` | low | The character in the left argument is thickened at top and at the foot. The right argument supports Γ without deciding the left. |
| 437 | 24–31% from top, TeX l. 17 (mark 4) · `formel si on établit une propriété` | `de` | `d'` | low | The raised 2- changes the form of the noun. The letters immediately before the insertion are cramped. |
| 437 | 96–99% from top, TeX l. 53 (mark 5) · `OK, C'est fonctoriel en $s$` | `\ldots` | — | low | A stroke and a point follow s. They could mark suspension; no further word is secure. |
| 438 | 4–10% from top, TeX l. 5 (mark 1) · `Pour la flèche $f_! f^` | `\prime` | `*` | medium | The rest of the sheet uses f-star. The first sign is a single high slant and may be a prime as drawn. |
| 438 | 4–10% from top, TeX l. 5 (mark 2) · `w H$ sur $T$, il faut trouver pour` | `tt` | — | medium | The clause quantifies t. The two tall strokes look like an abbreviation, not the written-out tout. |
| 438 | 11–22% from top, TeX l. 9 (mark 3) · `_{t}\backslash f^*(H)) \& \Pi(H_` | `t` | `f` | medium | The upper object is H_t. The lower letter, drawn differently, could also be f. |
| 438 | 29–33% from top, TeX l. 18 (mark 4) · `mais` | `avec` | — | low | The following diagram is recognizable, but this introductory word lies directly on the cancellation stroke. |
| 438 | 46–50% from top, TeX l. 25 (mark 5) | `induisant` | `s'en déduit` | low | The square supplies the arrow. A visible gap also allows « s'en déduit » for the continuous « induisant ». |
| 438 | 46–50% from top, TeX l. 25 (mark 6) · `unsure{induisant\|s'en déduit} $f^*H` | `\mathrel{-}` | `\longrightarrow` | high | A map of the two categories is meant. Its horizontal connector in this occurrence has almost no head. |
| 438 | 50–54% from top, TeX l. 28 (mark 7) · `\[ f^*(H)_t=S_` | `t` | `f` | low | The second factor H_t favours t. The smaller mark on S is crossed. |
| 438 | 68–76% from top, TeX l. 42 (mark 8) · `mais d'autre part, comme` | `$H$` | `tout` | low | The subsequent arrow concerns H over T, favouring H. At this point the thick group also resembles the word « tout ». |
| 438 | 77–81% from top, TeX l. 45 (mark 9) · `\[` | `t` | — | low | A small struck form occurs just before H_t; it could have been an initial t. |
| 438 | 90–98% from top, TeX l. 51 (mark 10) · `placement=\&,row sep=3mm]` | `f_!(f)` | — | low | The identifying line underneath supplies f_!(f*H). The cancelled start on the display is much shorter. |
| 439 | 11–25% from top, TeX l. 13 (mark 1) · `est une` | `$S$` | — | low | The isolated crossed coil comes before « équivalence ». The T inserted into the preceding « foncteur » supplies a competing context. |
| 439 | 11–25% from top, TeX l. 13 (mark 2) · `des sur $T$. Donc on peut` | `l'inverser en` | — | low | The following « trouver un quasi-inverse » fits this abandoned wording. Several middle letters meet the cancellation. |
| 439 | 30–34% from top, TeX l. 22 (mark 3) · `\[ f_!(f^*H)\longrightarrow\Pi(H/T)` | `\mathrel{-}` | `\longrightarrow` | high | The preceding formula supplies the arrow to H. The last line in this composite looks almost blunt. |
| 439 | 39–47% from top, TeX l. 27 (mark 4) · `Ayant les` | `2` | `2\textsuperscript{e}` | medium | The preceding sheet actually exhibits two arrows. There is a small projection to the right of the raised 2. |
| 439 | 48–51% from top, TeX l. 29 (mark 5) | `Questions` | `Question` | low | The heading names a question developed below. A short final stroke could also be a plural s. |
| 439 | 51–63% from top, TeX l. 35 (mark 6) · `o=2-2,shorten <=5mm,shorten >=6mm,"` | `\gamma` | `r` | medium | The inscription by the drawn inner arrow resembles a γ, though the short tail could be roman r. |
| 439 | 64–71% from top, TeX l. 38 (mark 7) · `qu'on ait commutativité` | `ou` | — | medium | This inserted line offers a second sufficient datum, favouring the disjunction ou. |
| 439 | 64–71% from top, TeX l. 38 (mark 8) · `de commutativité $\gamma\colon pf'` | `\mathrel{-}` | `\longrightarrow` | high | The text calls this a flèche. The line between pf′ and fq has only a very small terminal thickening. |
| 439 | 64–71% from top, TeX l. 38 (mark 9) · `rrow}fq$ (pas néc. iso).` | `Par` | — | low | The next word is adjonction. The first group is crossed or overtraced. |
| 439 | 64–71% from top, TeX l. 38 (mark 10) · `ar}} Par adjonction, il revient au` | `$=$` | `même` | high | Two bars are clearly drawn. The phrase « il revient au même » explains this use. |
| 440 | 4–9% from top, TeX l. 5 (mark 1) · `ant doit être vrai, et résulter de` | `mes` | — | low | « mes » is plausible before his familiar « fourbis ». The middle of the handwritten possessive is a horizontal. |
| 440 | 6–12% from top, TeX l. 7 (mark 2) · `Théorème} Si le` | `morphisme` | — | low | The last letters under the strike before « carré » resemble the ending of morphisme. |
| 440 | 6–12% from top, TeX l. 7 (mark 3) · `)$ est cartésien` | `de` | `dans` | low | The note specifies the ambient category. Both « de » and « dans » fit that role. |
| 440 | 13–23% from top, TeX l. 10 (mark 4) · `tabular}{@{}\|p{.93\linewidth}@{}} $` | `\gamma` | `r` | medium | It refers back to the small cell marked on 439. The curve and short stem do not eliminate r. |
| 440 | 13–23% from top, TeX l. 11 (mark 5) · `it 1-lisse, ou $p$ 1-propre, alors` | `le` | `la` | low | The following masculine « foncteur » favours le. The article itself is overwritten. |
| 440 | 13–23% from top, TeX l. 11 (mark 6) · `pre, alors le\|la` | `signe` | — | low | There are several joined letters beneath the line preceding T′. « signe » is tentative. |
| 440 | 13–23% from top, TeX l. 12 (mark 7) · `teur de changement de base est une` | `équivalence` | — | medium | The theorem concerns the strength of the comparison. The beginning of « équivalence » has been written over. |
| 440 | 24–36% from top, TeX l. 15 (mark 8) · `urbis'' généraux seraient` | `serait` | — | low | A crossed ending lies between the first apparent conditional and « en termes ». It resembles an earlier « serait ». |
| 440 | 24–36% from top, TeX l. 15 (mark 9) · `unsure{serait}} en termes` | `termes` | — | low | The preceding line ends in « termes ». The next line may have begun by repeating it. |
| 440 | 24–36% from top, TeX l. 15 (mark 10) · `termes}} d'un dérivateur $` | `\mathbb D` | `\mathrm D` | medium | This D has two visible parallel elements. A one-stroke roman D retraced by the pen is also possible. |
| 440 | 38–49% from top, TeX l. 17 (mark 11) · `d le 2-foncteur associé à` | `$f$` | — | low | A hook is covered before the written f:S→T. The second f is clear. |
| 440 | 49–54% from top, TeX l. 20 (mark 12) · `[ f^*\colonGrp}}(T)` | `\mathrel{-}` | `\longrightarrow` | high | The formula defines a pullback functor. Its drawn horizontal has a nearly square end. |
| 440 | 54–64% from top, TeX l. 23 (mark 13) · `dèle, 1-fidèle, 2-fidèle,` | `i.e.` | — | low | There are a few crossed small letters after « 2-fidèle ». The next sentence begins the explanation. |
| 440 | 54–64% from top, TeX l. 23 (mark 14) · `Cela} Si $G,H$ sont des` | `gr` | `g` | low | The short group immediately before « fibrés » could begin a word for groupoid. There is no independent expansion in the line. |
| 440 | 54–84% from top, TeX l. 25 (mark 15) · `\margin{La` | `$i$-fidélité` | `$i$-infidélité` | medium | The main paragraph distinguishes degrees of fidélité, supporting the first form. The joined initial strokes may be read in-. |
| 440 | 54–84% from top, TeX l. 25 (mark 16) · `idélité} de $f^*$ ($i\in\` | `n` | — | low | The blotted first entry is before a comma and the clear 0,1,2; the clean enumeration below does not restore the deleted entry. |
| 440 | 54–84% from top, TeX l. 25 (mark 17) · `le des foncteurs (obtenus` | `à` | `en` | low | The word between « obtenus » and « en » is crossed. Both a short preposition and a repeated en fit the traces. |
| 440 | 54–84% from top, TeX l. 25 (mark 18) · `à\|en}} en prenant $G=e_T$) $` | `\Gamma` | `\mathscr T` | medium | The underlined sign introduces the sections expression; the only clear mark is a right-angled cap over a stem. |
| 440 | 63–68% from top, TeX l. 29 (mark 19) · `m}}_{Grp}}(T)}(G,H)` | `\mathrel{-}` | `\longrightarrow` | high | The comparison maps Hom categories. The line itself is horizontal, with no unambiguous head. |
| 440 | 68–99% from top, TeX l. 33 (mark 20) · `à $T$-}équiv. près, elle` | `$=$` | `même` | high | Two written bars follow « elle ». The idiom favours reading them as même. |
| 440 | 68–99% from top, TeX l. 33 (mark 21) · `est 3-fidèle. On veut des critères` | `commodes` | — | low | The suggestion of criteria makes « commodes » possible. Several diagonal cancellation lines cut the word. |
| 440 | 68–99% from top, TeX l. 33 (mark 22) · `commodes} pour` | `que ce soit` | — | low | The words at the baseline are crossed again within the cancelled passage. No secure restoration follows from the next page. |
| 441 | 3–22% from top, TeX l. 5 (mark 1) · `i$-asphérique} si $\forall\,` | `t` | `s` | medium | The immediately following S/t favours t. The letter by the quantifier is worked over. |
| 441 | 3–22% from top, TeX l. 5 (mark 2) · `rique} si $\forall\,t\|s}\in` | `T` | `S` | medium | The next theorem uses f:S→T. At the end of this first line a flat cap overlaps a curved lower stroke. |
| 441 | 3–22% from top, TeX l. 5 (mark 3) · `=S/t$ est $i$-asphérique,` | 1 unreadable word/field | — | low | One short crossed group precedes i.e. Its letters are below the cancellation line. |
| 441 | 3–22% from top, TeX l. 5 (mark 4) · `que : les $S/t$ sont non vides. De` | `$=$` | `même` | high | The marks are two bars. The parallel discussion of coasphérique supports the sense « même ». |
| 441 | 22–51% from top, TeX l. 7 (mark 5) · `\longrightarrow T$ dans Cat, $i\in[` | `-0` | `0` | low | A short horizontal and a blotted numeral occupy the beginning of the cancelled interval. The clean final theorem uses 0. |
| 441 | 22–51% from top, TeX l. 7 (mark 6) · `w T$ dans Cat, $i\in[-0\|0},` | `2` | `3` | low | The last digit in the discarded range has been retraced. Both 2 and 3 fit part of the mark. |
| 441 | 22–51% from top, TeX l. 7 (mark 7) · `\|0},2\|3}]=\{0,1,2,` | `3` | — | low | A terminal digit is cancelled after the list 0,1,2. Its right edge looks like 3. |
| 441 | 22–51% from top, TeX l. 7 (mark 8) · `ue et $(i-1)$-propre} ou` | `resp.` | — | low | The adjacent alternatives make « resp. » plausible. The crossing strokes make a fuller reading precarious. |
| 441 | 22–51% from top, TeX l. 7 (mark 9) · `il suffit} $(i-1)$-lisse,` | `ou $(i-1)$-propre` | — | low | The uncancelled reformulation below uses exactly this pair of conditions, but the abandoned line is partly obscured. |
| 441 | 22–51% from top, TeX l. 7 (mark 10) · `cteur $f^*$ précédent est` | `($i$` | — | low | This is beneath the strike just before the degree of fidelity. The left curve need not be a letter. |
| 441 | 22–51% from top, TeX l. 7 (mark 11) · `écédent est ($i$` | `$i$` | — | low | The revised theorem has i-fidèle. The immediate writing was amended even before the whole passage was cancelled. |
| 441 | 22–51% from top, TeX l. 7 (mark 12) · `2-fidèle, et soit $G$ un` | `group` | — | low | A stray cancelled word precedes « fibré en groupoïdes ». Only an initial like group- is discernible. |
| 441 | 22–51% from top, TeX l. 7 (mark 13) · `fibré en groupoïdes} $f^*(H)$, il` | `f.` | `faut` | low | The usual pair « … et s. » suggests the abbreviation f. The long overlying line also allows a fuller word. |
| 441 | 22–51% from top, TeX l. 7 (mark 14) · `et s. que ce soit vrai` | `colocalement` | `localement` | low | This word was added below the broadly cancelled paragraph. Its beginning seems to repeat a loc- group. |
| 441 | 50–74% from top, TeX l. 9 (mark 15) · `thbb Z$, on définit un dérivateur $` | `\mathbb D` | `\mathrm D` | medium | Here D has a clear parallel vertical at its left. A reinforced plain D is the other possibility. |
| 441 | 50–74% from top, TeX l. 9 (mark 16) · `_i$-fibrations et de $\mathbb D_i$-` | `cofibrations` | `fibrations` | low | Both occurrences end in fibrations. The extra joining curve at the start of the second could represent co-. |
| 441 | 50–74% from top, TeX l. 9 (mark 17) · `ations} triviales` | `dont` | — | low | The short word crossed before the parenthetical explanation looks like dont. |
| 441 | 72–80% from top, TeX l. 11 (mark 18) · `Cat})$, $i\in\{0,1,2\}$.` | `a)` | — | low | An enclosed/crossed letter and a possible closing parenthesis are visible before the proviso. |
| 441 | 72–80% from top, TeX l. 11 (mark 19) · `$. a)` | `Si $f$ est` | — | low | The extant « Supposons » replaces an earlier start. The word sequence under it is not certain. |
| 441 | 72–80% from top, TeX l. 11 (mark 20) · `ons l'une des conditions suivantes` | `satisfaite` | `satisfaites` | low | The phrase has singular « l'une » and plural « conditions ». The last stroke does not decide the agreement. |
| 441 | 94–97% from top, TeX l. 20 (mark 21) · `\[ f^*\colonGrp}}(T)` | `\mathrel{-}` | `\longrightarrow` | high | The text identifies this as the inverse-image functor. The horizontal is blunt in the display. |
| 442 | 4–28% from top, TeX l. 4 (mark 1) · `de la forme $f^*(H)$ sss` | `il existe` | `il est` | low | The new « pour tout » supersedes the crossed beginning. There is a tall initial and an indistinct second group. |
| 442 | 4–28% from top, TeX l. 4 (mark 2) · `n $G_t$} de $G_` | `t` | `s` | low | A small letter under the live G has been overwritten. The raised G_t favours t but does not settle the old stroke. |
| 442 | 4–28% from top, TeX l. 4 (mark 3) · `eleted{t\|s}}}$ à $` | `T` | — | low | A flat cap overlays the first live S_t. The earlier t∈T offers a plausible former T. |
| 442 | 4–28% from top, TeX l. 4 (mark 4) · `\|s}}}$ à $T}}S_t$` | `soit` | `est` | low | The form is thickened just before « équivalente ». The clause after sss favours soit. |
| 442 | 4–28% from top, TeX l. 4 (mark 5) · `groupoïdes constant sur $` | `T` | — | low | The same broad cap recurs above the second S_t. It could also be simple reinforcement of S. |
| 442 | 4–28% from top, TeX l. 4 (mark 6) · `que son groupoïde fondamental est` | `équiv.` | `équiv` | low | The word ending follows équiv-, and is abbreviated. It is unclear whether the final point is distinct from the pen-lift. |
| 442 | 28–51% from top, TeX l. 6 (mark 7) · `un groupoïde constant sur $Z$, il` | `faut` | `f.` | low | The « … et s. » formula occurs on 441. Overlapping writing from the margin obscures whether faut is written in full here. |
| 442 | 28–51% from top, TeX l. 6 (mark 8) · `il faut\|f.} et s. que pour` | `tte` | `toute` | medium | The adjacent flèche makes tte a natural contraction. Its internal vowels are not separately formed. |
| 442 | 28–51% from top, TeX l. 6 (mark 9) · `toute} flèche $u$ de $Z$,` | `m.s.` | `m.s` | low | Something short was cancelled after « de Z ». The small marks between strokes are uncertain. |
| 442 | 28–51% from top, TeX l. 6 (mark 10) · `foncteur} morphisme de groupoïdes` | `cor\textsuperscript{t}` | `corr\textsuperscript{t}` | low | A tiny t-like stroke is raised after the group beginning co-. The ending is a contraction. |
| 442 | 38–62% from top, TeX l. 10 (mark 11) · `est essentiellement` | `loc.` | `loco.` | medium | « constant sur Z » favours locally constant. There is a small extra movement after the loc- group. |
| 442 | 51–69% from top, TeX l. 12 (mark 12) · `Corollaire} La condition` | `trad.` | `trad.le` | low | The corollary refers to condition 2°. The strokes following « condition » admit neither a secure expansion nor a certain ending. |
| 442 | 51–69% from top, TeX l. 12 (mark 13) · `dentique, le foncteur $u^*$ induit` | `par` | — | medium | « induit … u » favours par. The p is heavily reinforced. |

## Slips kept as written

| Scan and place | As written | Apparently intended | Grounds and confidence |
|---|---|---|---|
| 435, last line | `sur $S$` | `sur $T$` | The line before the final construction calls the target a category fibred over T, and the construction is indexed by t. The last base letter resembles S. Medium. |
| 436, after the boxed formula | `\Pi(X,T)` | `\Pi(X/T)` | The boxed formula immediately above uses the same X and T with an oblique separator. The prose copy has a comma. High confidence in the difference, medium in calling it a slip. |
| 438, upper left of the square | `H\times_S T` | `H\times_T S` | The opposite corners and arrows label H over T and S mapping to T. The square follows a cancelled introduction. Low. |

The two signs after Δ on 428, λ/μ on 429, and the small final capitals on 436 remain reading questions. They have not been silently regularized.

## Abbreviations

| Written form | Likely expansion or use here | Example scan |
|---|---|---|
| Ty | types (a category name) | 428 |
| qq chose | quelque chose | 428 |
| id | identité | 429 |
| can | canonique | 430 |
| opp | opposé | 430 |
| Hot | homotopie, in compounds designating homotopy equivalence or homotopy types | 431 |
| équiv., équiv | équivalence or équivalent, according to the syntax | 431 |
| Cat, cat. | catégorie(s), or the category of categories | 431 |
| cf, Cf | confer, comparez | 431 |
| pr | projection | 431 |
| cart | cartésien | 431 |
| NB | nota bene | 431 |
| inv. | inverse | 431 |
| i.e., i.e | id est, c’est-à-dire | 431 |
| déf, def | définition, par définition | 432 |
| fib | fibré(e), or fibrées in a category subscript | 434 |
| Grp | groupoïdes here, as the written caption specifies | 434 |
| hom | homotopie in “types d’hom”; homomorphisme or morphisme in an arrow context | 434 |
| iso | isomorphisme or isomorphe | 434 |
| néc. | nécessairement | 435 |
| directmt | directement | 435 |
| tt, tte | tout, toute | 437 |
| Th | théorème | 437 |
| Hom | morphismes (the Hom category) | 437 |
| Ob | objets | 437 |
| OK | okay | 437 |
| resp. | respectivement, conjectural in the cancelled line | 441 |
| pl. | pleinement | 441 |
| f. et s. | faut et suffit | 441 |
| sss | si et seulement si | 442 |
| corᵗ, corrᵗ | correspondant | 442 |
| loc., loco. | localement | 442 |
| trad., trad.le | expansion uncertain in the corollary | 442 |
| = in prose | même, for example in “de =” or “au =” | 428 |

## Legibility

The large diagrams are generally easier to read than the prose that connects them. The fast pen joins endings and sometimes leaves almost identical traces for a prime, a pen-lift, and a partly cancelled subscript. I trust the directions of the main labelled diagrams and the chapter boundary more than the readings of the cropped printer fields on 433, the bottom line of 434, and the abandoned formulation on 441. The notes at the left of 435, 440, and 442 were read in rotated views. Some of their abbreviations remain open. The percentages and the inventory identify where to look for each mark.
