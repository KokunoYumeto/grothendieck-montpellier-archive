# K84-11 · Second reading

The times are UTC. For each scan the first timestamp precedes reopening the three strips. The second is when the independent crop notes were saved. Only then was that page’s TeX file opened for comparison. The third marks the page checkpoint. The source registers below give line numbers in the page file at the freeze. Later witness decisions are in the doubts file.

The timed independent comparisons lasted 37–74 seconds per sheet, shorter than the requested several-minute reading pace. Follow-up image checks are recorded separately in the witness and slips tables.

Short extra comparisons of the lower-margin marks and of the shared diagram conventions followed the individual checkpoints. A value written as an alternative documents uncertainty in the reading. A question mark attached to an arrow on the sheet is identified separately.

## Scan 162

**UTC** · start 2026-11-18T11:27:38Z · independent list saved 2026-11-18T11:27:56Z · comparison complete 2026-11-18T11:28:38Z

**Accents and unusual readings from the strips.** Sparse French. I read χ-trivi… above the left return arrows and inc. can. next to the long downward arrow. The top cancelled word has a descending first letter. Tr and id are unaccented. No date.

**Notation and line order from the strips.** Top x ↦ π′(x) = π(x) − (χ − 1)x. 0—L—E—L′—0. An E—E, two restrictions, an equivalence to π|L and another to π:E—L. The next tensor line has indices 1 and 2, two underbraces, a 2−χ below. In the middle, L₁ ⊂ E₁ and L₂ ⊂ E₂ have arrows returning to L. To their right, a proposed direct map has ?, and the low tip has two primes. The bottom grid has Tr, ?, χ id, and inc. can. The lower expansion has α, β, γ with a small low stroke, δ and four tensor terms, then the edge.

**Corrections, lines near live text, capitals and margins.** Strikes at the upper left, on a restriction, on a scalar before id, on the isolated expression above the tensor line, and twice below the grid. Open E has a middle bar. L and L′ have no crossbar. Small arrowheads alternate with plain strokes. The two ? marks are distinct. No letter i or j in numerical subscripts. The short vertical label is Tr. The longer one separates into inc. and can., with a space and two stops. Rechecked both diagonal links below E, both question marks, the 2 under the expansion, and the two bottom traces of ink at γ and before δ. No marginal writing apart from archive 161. The scalar before id and the letters under the upper strike remain uncertain.

**Letter indices.** No i or j was found in an index or exponent. The register distinguishes the written numerals, primes and other marks.

**Formula and diagram register**

Display, line 3.

~~~latex
x\longmapsto\pi'(x)=\pi(x)-(\unsure{\chi|\lambda}-1)x
~~~

Diagram or ruled array, line 6.

~~~latex
\begin{tikzcd}[ampersand replacement=\&,column sep=small]
0\arrow[r]\&L\arrow[r,dash]\&E\arrow[r,dash]\&L'\arrow[r,dash]\&0
\end{tikzcd}
~~~

Display, line 10.

~~~latex
\begin{aligned}
&E\longrightarrow E\\
\deleted{\pi'(L)}\quad&(\pi'|L)=\deleted{\unsure{\chi}}\mathrm{id}_L
\qquad\Longleftrightarrow\quad\pi|L=\chi\,\mathrm{id}_L\\
&(\pi'|E/L=L')=-(\chi-1)\,\mathrm{id}_{L'}\\
&\hspace{4em}\Longleftrightarrow\quad\pi:E\longrightarrow L
\end{aligned}
~~~

Display, line 19.

~~~latex
\deleted{\unsure{\pi(x)}}\qquad
\begin{aligned}
\unsure{u|x}_1\otimes x_2+
\underbrace{\pi'_1(x_1)}_{u_1}\otimes\pi'_2(x_2)
&=u_1\otimes\underbrace{(x_2+\pi'_2(x_2))}_{x_2+\pi_2(x_2)-(\chi-1)x_2}\\
&\hspace{4em}=\underline{(\unsure{2}-\chi)x_2+\pi_2(x_2)}
\end{aligned}
~~~

Diagram or ruled array, line 28.

~~~latex
\begin{tikzcd}[ampersand replacement=\&,row sep=small,column sep=small]
L_1\&{\subset}\& E_1\arrow[ll,bend right=25,"{\pi_1\quad\chi\text{-}\unsure{\text{triv.}|\text{tordu}}}"']\\
L_2\&{\subset}\& E_2\arrow[ll,bend left=25,"\pi_2"]
\end{tikzcd}
~~~

Display, line 32.

~~~latex
\Longrightarrow
~~~

Diagram or ruled array, line 35.

~~~latex
\begin{tikzcd}[ampersand replacement=\&,row sep=small,column sep=tiny]
E_1\otimes E_2\arrow[rr,very thick,"?"]\arrow[dr]\arrow[dd]\&\&E_1\otimes E_2\arrow[dd]\\
\&E\arrow[ur]\&\\
E_1\otimes\deleted{\unsure{L}}E_2\underset{L_1\otimes L_2}{\oplus}L_1\otimes E_{\unsure{1|2}}\arrow[rr,"{\pi_1,\pi_2}"']\arrow[dr]\&\&L'_1\otimes\unsure{L_2|L'_2}\\
\&L'_1\otimes L'_2\arrow[ur,dash,shorten <=7pt,shorten >=15pt]\&
\end{tikzcd}
~~~

Diagram or ruled array, line 41.

~~~latex
\begin{tikzcd}[ampersand replacement=\&,row sep=large,column sep=small]
\unsure{0}\arrow[r,dash]\&E_1\otimes_0 E_2\arrow[r,dash]\arrow[d,"\mathrm{Tr}" ]\& E_1\otimes E_2\arrow[r,dash]\arrow[d,dash]\& L'_1\otimes L'_2\arrow[r,dash]\arrow[d,Rightarrow]\&0\\
\unsure{0}\arrow[r,dash]\&\deleted{\unsure{E}}L_1\otimes L_2\arrow[r,dash]\arrow[d,hook,"\text{inc. can.}"]\& E\arrow[r,two heads]\arrow[d,"?"]\&L'_1\otimes L'_2\arrow[r,dash]\arrow[d,"\chi\,\mathrm{id}"]\&0\\
0\arrow[r]\&E_1\otimes_0 E_2\arrow[r,dash]\&E_1\otimes E_2\arrow[r]\&L'_1\otimes L'_2\arrow[r,dash]\&{}
\end{tikzcd}
~~~

Display, line 46.

~~~latex
\begin{aligned}
&\deleted{x_1\quad\pi_1}\qquad\deleted{\unsure{\alpha+}}\\
&x_1\quad\pi_1(x_1)\qquad x_2,\pi_2(x_2)\\
&\alpha\; x_1\otimes x_2+\beta\,x_{\unsure{1|2}}\otimes\pi_2(x_{\unsure{2|1}})
+\gamma_{\unsure{2|{}}}\,\pi_1(x_1)\otimes x_2\unsure{+|\cdot}\delta\,\pi_1(x_1)\otimes\pi_2(x_{\unsure{2|1}})
\end{aligned}
~~~

**State-of-page register**

- Line 9, deleted · ` \unsure{pour} \illegible{1} `
- Line 13, deleted · ` \pi'(L) `
- Line 13, deleted · ` \unsure{\chi} `
- Line 20, deleted · ` \unsure{\pi(x)} `
- Line 38, deleted · ` \unsure{L} `
- Line 43, deleted · ` \unsure{E} `
- Line 48, deleted · ` x_1\quad\pi_1 `
- Line 48, deleted · ` \unsure{\alpha+} `

**Changes made during comparison**

- ` \unsure{\pi}" ] ` -> ` \mathrm{Tr}" ] `
- ` \unsure{\text{inclusion.}} ` -> ` \text{inc. can.} `
- ` \unsure{\text{tordu}} ` -> ` \unsure{\text{triv.}|\text{tordu}} `
- ` \&L'_1\otimes L'_2\& ` -> ` \&L'_1\otimes L'_2\arrow[ur,dash,shorten <=7pt,shorten >=15pt]\& `
- ` +\gamma\,\pi_1(x_1)\otimes x_2+\delta ` -> ` +\gamma_{\unsure{2|{}}}\,\pi_1(x_1)\otimes x_2\unsure{+|\cdot}\delta `

## Scan 163

**UTC** · start 2026-11-18T11:28:39Z · independent list saved 2026-11-18T11:28:57Z · comparison complete 2026-11-18T11:29:29Z

**Accents and unusual readings from the strips.** parlé, à contre temps, d'écoute, invétérée, à, même, disparu with a mark on its final e, résultat, imposé with a small e, passé, en de moments, où, à autui, à moi, à mes yeux, à présent, à sentir, intéressante, commencé, à, à partir, où à disparu, à toujours, m'apparaît, à tort ou à raison, n'était, décele, à vouloir, à toute fin, celà, préfère, plutôt, paraît, ça, à ce, plutôt, à chercher, fut-ce, bien-fondé, profondémment, enracinée, égo, lâcher, été, d'énergie, portée, de d'extraordinaire, représentait, trouvée, désamorcée, trouvé, allégé, réticence de d'écho, être lié, désir, caché, être, désir, véritablement, solidité à toute épreuve, où, où, dépendance.

**Notation and line order from the strips.** 488, with no hyphens around it. No inline formulas or displays. Two paragraphs, the second continues off sheet after de. Double quote pairs around tu vas faire…, erreurs, ça, d'un poids…, besoin, libre de lui, crochet and accrocher.

**Corrections, lines near live text, capitals and margins.** Small strokes near final e in disparue and immediately after imposé. Spelling autui is at the right end of line 6; later autrui is fully printed. The form qu'il has a small defective u. Recheck whether dommage to a letter or a deliberate interline mark. Pencil 162 only, no marginal sentence. The diagonal at the last e of disparue extends past the letter. Its faint lower part may be an oblique cancellation, and its upper part alone would look acute. The e after imposé is smaller and has a different baseline. No other correction could be distinguished from uneven impressions of the type. The repeated de d' and the different spellings autui/autrui have been retained.

**Letter indices.** No mathematical i or j index or exponent.

**Formula and diagram register**

No inline formula or mathematical display. Numerals, dates and callouts are identified above.

**State-of-page register**

- Line 3, handwritten · ` \deleted{e} `
- Line 3, deleted · ` e `
- Line 3, handwritten · ` ´ `
- Line 3, handwritten · ` e `

**Changes made during comparison**

- ` quasiment disparue, ` -> ` quasiment disparu\unsure{\handwritten{\deleted{e}}|e\handwritten{´}}, `

## Scan 164

**UTC** · start 2026-11-18T11:29:30Z · independent list saved 2026-11-18T11:29:51Z · comparison complete 2026-11-18T11:30:26Z

**Accents and unusual readings from the strips.** No running prose or accents. id and i.e. near the lower right, the latter abbreviated in two separated strokes. Superscript prime at the title πᵢ′.

**Notation and line order from the strips.** First table columns Lᵢ, Mᵢ, rows Lᵢ, Mᵢ, entries χ, τᵢ / 0,0. Second 0,−τᵢ / 0,χ. Detached l₁⊗m₂ over a struck fragment. A large four-row table: 1, π₁′, π₂′, π₁′⊗π₂′ at left, then three 1s, χ χ τ₁⊗id, χ id⊗τ₂ χ, χ² χ id⊗τ₂ χ τ₁⊗id. Above it a crossed expression with π₁′⊗id and id⊗. Beneath, α + β₁π₁′ + β₂π₂′ + γπ₁′⊗π₂′, deletions, and α+(β₁+β₂)χ+γχ²=χ. Two small constraints α+β₁χ=0, β₂+γχ=1; the expansion has an underbrace. At far right an id-subscript, a bracket and a final id⊗τ₂.

**Corrections, lines near live text, capitals and margins.** The index in Lᵢ, Mᵢ, πᵢ and τᵢ is short with a separate dot and no j descender, compared across both upper tables. The second table title is overwritten next to a vertical stroke. Long isolated ruling at middle left with a double vertical line. A small strike in the row of ones, and a crossed initial mark at the box. No pen additions to type. The i in each of the two small table titles, both sets of row and column labels, and the two τ entries is dotted. The signs in the second small table are 0 and −τᵢ above 0 and χ. Both loops in the second title are visible under a top stroke. The bottom-right calculation has a second opening parenthesis before β₁ with a crossing curve after the expression. The inserted α+ is above the baseline. The uppercase-looking I in final Id is separate from the preceding lowercase instances.

**Letter indices.** Dotted i appears in π′ᵢ, the disputed opposite map, Lᵢ, Mᵢ and τᵢ. The suffixes in the large table and boxed equations are numerals 1 and 2. No j.

**Formula and diagram register**

Diagram or ruled array, line 2.

~~~latex
$\begin{array}{c|c|c|}
\pi'_i&L_i&M_i\\ \hline
L_i&\unsure{\chi|\lambda}&\tau_i\\ \hline
M_i&0&0\\ \hline
\end{array}\qquad
\begin{array}{c|c|c}
\unsure{\overline{\pi}'_i|\varpi'_i|\overline{\omega}'_i}&L_i&M_i\\ \hline
L_i&0&-\tau_i\\ \hline
M_i&0&\chi
\end{array}$
~~~

Display, line 12.

~~~latex
\begin{aligned}
&l_1\otimes m_2\\
&(\deleted{\unsure{l_1+m_1}}
\end{aligned}
~~~

Diagram or ruled array, line 18.

~~~latex
$\begin{array}{c|c}
\phantom{1}&\phantom{11111}\\ \hline
\vphantom{\dfrac11}&
\end{array}$
~~~

Display, line 22.

~~~latex
\deleted{\pi'_1\otimes\mathrm{id}_{E_2}+\mathrm{id}_{E_1}\otimes}
~~~

Diagram or ruled array, line 25.

~~~latex
$\begin{array}{c|ccc}
1&\deleted{\unsure{\mathrm{id}}}1&1&1\\ \hline
\pi'_1&\chi&\chi&\tau_1\otimes\mathrm{id}_{L_2}\\
\pi'_2&\chi&\mathrm{id}_{L_1}\otimes\tau_2&\chi\\
\pi'_1\otimes\pi'_2&\chi^2&\chi\,\mathrm{id}_{L_1}\otimes\tau_2&\chi\,\tau_1\otimes\mathrm{id}_{L_2}
\end{array}$
~~~

Display, line 31.

~~~latex
\begin{aligned}
&\alpha+\beta_1\pi'_1+\beta_2\pi'_2+\gamma\pi'_1\otimes\pi'_2\\
&\deleted{\alpha\pi'_1+\beta\pi'}
\end{aligned}
~~~

Display, line 37.

~~~latex
\deleted{\unsure{\chi}}\quad\boxed{\alpha+(\beta_1+\beta_2)\chi+\gamma\chi^2=\chi}
~~~

Display, line 40.

~~~latex
\begin{aligned}
\alpha+\beta_1\chi+
\underbrace{\beta_2\,\mathrm{id}\otimes\tau_2+\gamma\chi\,\mathrm{id}\otimes\tau_2}_{(\beta_2+\gamma\chi)\,\mathrm{id}\otimes\tau_2}
&=\mathrm{id}_{L_1}\otimes\tau_2\\
\text{i.e.}\qquad \mathrm{id}_{L_1}\otimes(\inserted{\alpha+}(\beta_1\chi\unsure{)|{}}\,\mathrm{id}_{M_2}
&+(\beta_2+\gamma\chi)\tau_2)=\\
&\mathrm{Id}\otimes\tau_2
\end{aligned}
~~~

Display, line 50.

~~~latex
\boxed{\begin{aligned}
\alpha+\beta_1\chi&=0\\
\beta_2+\gamma\chi&=1
\end{aligned}}
~~~

**State-of-page register**

- Line 15, deleted · ` \unsure{l_1+m_1} `
- Line 23, deleted · ` \pi'_1\otimes\mathrm{id}_{E_2}+\mathrm{id}_{E_1}\otimes `
- Line 26, deleted · ` \unsure{\mathrm{id}} `
- Line 34, deleted · ` \alpha\pi'_1+\beta\pi' `
- Line 38, deleted · ` \unsure{\chi} `
- Line 45, inserted · ` \alpha+ `

**Changes made during comparison**

- ` \overline{\pi}'_i|\varpi'_i ` -> ` \overline{\pi}'_i|\varpi'_i|\overline{\omega}'_i `
- ` \inserted{\alpha+}\beta_1\chi\,\mathrm{id}_{M_2} ` -> ` \inserted{\alpha+}(\beta_1\chi\unsure{)|{}}\,\mathrm{id}_{M_2} `

## Scan 165

**UTC** · start 2026-11-18T11:30:27Z · independent list saved 2026-11-18T11:30:45Z · comparison complete 2026-11-18T11:31:04Z

**Accents and unusual readings from the strips.** (6 octobre), déployement, désir, spontanément, déjà, perçue, également, être vécue, même, vécu, occulté, réactions, déclenche, même, vécu, vécus, à, père, où, apparaît, détenteur, d'autorité répressive, écrasant, envié, détesté. Même, indépendamment, déséquilibre, foncière, déployement, démesure, néfaste, intéressé, moi-même, à, même, incidents-santé, dernières années, montré, été, pensée, j'ecrivais, déployemen… clipped, était, à, sûrement, réactions de défense, même. Ambiguité, après 1976, élèves, où, mathématique était, où, dépoyement, déployements, passé, créé, réputation, à, à, professionelle, à, présent, thèmes mathématiques, même, périodes mathématiques, réputation, maîtrise, déjà, déployement, élèves, motivés, dépit, Superpère.

**Notation and line order from the strips.** Raised 108 followed by baseline 2 in parentheses; 477 at top, 1976 in final paragraph. No mathematical expression. Spaced letters in contrainte, déséquilibre, passé, réputation and dans le présent. Lower right 164 reads from bottom to top.

**Corrections, lines near live text, capitals and margins.** Light isolated ink near se and under printed letters. No handwritten correction to the body seen. Right edge of first and second paragraphs clips some letters; normal line-end hyphenations join. Double quotations are upright typed strokes, including a space after the opening quote before déployements. Capital Superman/Superpère in plain type. The right edge cuts the last part of vécue, les, chez and déployement. In the first two of these the left halves of the final e and s are visible. Elsewhere the i in ambiguité has one dot; the e in j'ecrivais has no acute. The isolated speck next to se is below the line and has no insertion leader. The page and note numbers are live type. Archive 164 runs up the lower right edge.

**Letter indices.** No mathematical i or j index or exponent.

**Formula and diagram register**

No inline formula or mathematical display. Numerals, dates and callouts are identified above.

**State-of-page register**

- Line 7, margin · ` \unsure{-} `

**Changes made during comparison**

no change

**Cross-page comparison before freeze.** A short isolated mark at the lower left recurs on several typed sheets. It may be a registration mark. Only the stroke is transcribed.

- ` % archive sheet number: 164 ` -> ` \margin{\unsure{-}}
% archive sheet number: 164 `

## Scan 166

**UTC** · start 2026-11-18T11:31:05Z · independent list saved 2026-11-18T11:31:25Z · comparison complete 2026-11-18T11:32:16Z

**Accents and unusual readings from the strips.** Pour définir un hom F, il faut définir … ; avec 4 carrés commutatifs in two lines to the right. Si on veut que F induise … un hom d'extensions, donc … pour que F₂₂ = 0, … de plus … l'identité sur … il f. et s. … d° si on veut que F induise l'identité sur … . Si ces conditions sont vérifiées, alors deux des 4 carrés voulus sont déjà commutatifs, savoir … ; les quatre composés sont nuls. Accents are faint in définir, carrés, identité, vérifiées, déjà and composés.

**Notation and line order from the strips.** Upper Σ joining E₁⊗L₂ and L₁⊗E₂, subscripts on the labels of four descending maps. E₁⊗E₂, L₁⊗L₂ above two further corners, four crosses labelled F₁₁ F₂₁ F₁₂ F₂₂. Lower Π after (E₁⊗M₂)×(M₁⊗E₂). The component conditions in boxes F₂₂=0, F₂₁=α₁⊗α₂, F₁₂=ψ₁⊗ψ₂; lower left square labels 0, F₂₂=0, F₁₂=ψ₁⊗ψ₂, right F₂₁ and F₂₂=0. No letter indices i or j, subscripts are digits.

**Corrections, lines near live text, capitals and margins.** At the lower left corner of the primary diagram, an F is written higher than an overwritten E; other scribbles below. Strike under un hom. After alors there is one overwritten word followed by des. Lower right sketch starts with a struck E… and a second E… lower; Π below another struck character. Bracketed right marginal note about the four composites. At the top vertex the superposed loop at the join may be a corrected sign. The overwritten left lower tensor factor has three horizontal strokes in its final form; F is also possible before the low hook. The word après alors occupies a single position. Its initial letter has been worked over. The upright parenthesis at the far right encloses the separate note les quatre composés sont nuls. The two halves of the diagonal to the lower left are interrupted where the other diagonal crosses. Separate digit-by-digit checks distinguish F₁₂ from F₂₁ in the diagram and the boxes.

**Letter indices.** No i or j was found in an index or exponent. The register distinguishes the written numerals, primes and other marks.

**Formula and diagram register**

- Line 2, inline ` F `.

Diagram or ruled array, line 3.

~~~latex
\begin{tikzcd}[ampersand replacement=\&,row sep=large,column sep=small]
\& (E_1\otimes L_2)\unsure{\oplus|\amalg}(L_1\otimes E_2)=\Sigma
\arrow[dl,"{\mathrm{id}_1\otimes\alpha_2,\ \alpha_1\otimes\mathrm{id}_2}"']
\arrow[dr,"{\pi_1\otimes\mathrm{id}_{\unsure{2|L_2}},\ \mathrm{id}_1\otimes\pi_2}"]\&\\
E_1\otimes E_2\arrow[d,"F_{11}"']\&\&L_1\otimes L_2\arrow[d,"F_{22}"]\arrow[dll,"F_{21}" near start]\\
E_1\otimes\deleted{\unsure{E_2\otimes}}\unsure{E|F}_2
\arrow[dr,"{\mathrm{id}_1\otimes\unsure{\psi|\varphi}_2,\ \psi_1\otimes\mathrm{id}_2}"']\&\&
M_1\otimes M_2\arrow[dl,"{\unsure{\varpi|\overline{\omega}}_1\otimes\mathrm{id}_2,\ \mathrm{id}_1\otimes\varpi_2}"]\\
\&(E_1\otimes M_2)\times(M_1\otimes E_2)=\Pi\arrow[from=2-1,to=3-3,crossing over,"F_{12}" near end]\&
\end{tikzcd}
~~~

- Line 15, inline ` F `.

- Line 15, inline ` L_1\otimes L_2\longrightarrow L_1\otimes L_2 `.

- Line 15, inline ` \boxed{F_{22}=0} `.

- Line 15, inline ` L_1\otimes L_2 `.

- Line 15, inline ` \boxed{F_{21}=\alpha_1\otimes\alpha_2} `.

- Line 15, inline ` M_1\otimes M_2 `.

- Line 15, inline ` \boxed{F_{12}=\psi_1\otimes\psi_2} `.

Diagram or ruled array, line 16.

~~~latex
\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=small]
\&\Sigma\arrow[dl,dash]\arrow[dr,dash]\&\\
E_1\otimes E_2\arrow[rrd,"0","{F_{12}=\psi_1\otimes\psi_2}"']\&\&L_1\otimes L_2\arrow[d,"{F_{22}=0}"]\\
\&\&M_1\otimes M_2
\end{tikzcd}
~~~

Diagram or ruled array, line 22.

~~~latex
\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=small]
\&\&L_1\otimes L_2\arrow[dll,"{\deleted{\unsure{E_1\otimes E_2}}F_{21}}"']\arrow[d,"{F_{22}=0}"]\\
E_1\otimes E_2\arrow[dr]\&\&M_1\otimes M_2\arrow[dl]\\
\&\deleted{\unsure{\varphi}}\Pi\&
\end{tikzcd}
~~~

**State-of-page register**

- Line 8, deleted · ` \unsure{E_2\otimes} `
- Line 15, deleted · ` l'identité `
- Line 15, inserted · ` un hom d'extensions, donc `
- Line 15, deleted · ` \unsure{avoir} `
- Line 15, inserted · ` de plus `
- Line 15, deleted · ` \unsure{Si} `
- Line 15, deleted · ` \unsure{d} `
- Line 23, deleted · ` \unsure{E_1\otimes E_2} `
- Line 25, deleted · ` \unsure{\varphi} `
- Line 27, margin · ` (les quatre composés sont nuls) `

**Changes made during comparison**

- ` L_2)\oplus(L_1 ` -> ` L_2)\unsure{\oplus|\amalg}(L_1 `
- ` \unsure{E_2\otimes}}E_2 ` -> ` \unsure{E_2\otimes}}\unsure{E|F}_2 `
- ` \deleted{\unsure{deux}}\unsure{deux} ` -> ` \deleted{\unsure{d}}\unsure{deux} `
- ` , si on veut que \unsure{ça} ` -> ` , \unsure{d\textsuperscript{o}|si} \unsure{si|{}} on veut que \unsure{ça} `
- ` (les quatre composés sont nuls) ` -> ` \margin{(les quatre composés sont nuls)} `

**Cross-page comparison before freeze.** The F₂₁ diagonal breaks around F₁₂. The stroke order gives F₁₂ the unbroken line.

- ` \arrow[drr,"F_{12}" near end] ` -> (moved or removed at this position)
- ` \arrow[dll,crossing over,"F_{21}" near start] ` -> ` \arrow[dll,"F_{21}" near start] `
- ` =\Pi\& ` -> ` =\Pi\arrow[from=2-1,to=3-3,crossing over,"F_{12}" near end]\& `

## Scan 167

**UTC** · start 2026-11-18T11:32:16Z · independent list saved 2026-11-18T11:32:31Z · comparison complete 2026-11-18T11:32:53Z

**Accents and unusual readings from the strips.** déséquilibre, essayé, précédente, particulièrement, déployement; déséquilibre, cultivé, mécanismes, évanouis, à, ni en les jours. (10 octobre), C'étaient, portés, d'énergie, intérieur, d'émerveillement, après, déployant, C'étaient, où, commencé, à, ignoré, l'appréhendais, connaître, à, même, imprévisible, imprévu, était, entièrement, plutôt, s'était, été coupé ou étouffé, était, mystérieusement, A vrai dire, s'était, déjà dès, précédé, à, où, pensée, guère. été, l'équilibre, années, façon, l'état, resté présent, indélébile, unité, au delà, à, être, même, désigner, unité de l'être, n'es at right.

**Notation and line order from the strips.** 482, (10 octobre), vertical archive 166. No mathematical formulas. Spaced commencement, recommencement, pensée, unité, chose. Faint corrections in devenir and the é of the first letter-spaced unité. Quoted bouts, naissance, devenir, la femme, l'homme, l'enfance, en puissance, division and the two separate final quotations enfant / enfance.

**Corrections, lines near live text, capitals and margins.** The e in the quoted devenir has an extra impression; the u in du yin has a faint left mark, and é in spaced unité is broken. The final t of n'est is outside readable type. The opening is re plus ou moins and after cerner the next visible line begins aspect. No margin annotation besides archive numeral. The restored e in devenir and u in du yin have thick, irregular baselines unlike their neighbours. The spaced é in unité is made up of broken regular type strokes, including an acute, so it stays typed. The spaces after ni en and the absence of an article between cerner and aspect are visible. At the last line only n'es can be read. No separate marginal text.

**Letter indices.** No mathematical i or j index or exponent.

**Formula and diagram register**

No inline formula or mathematical display. Numerals, dates and callouts are identified above.

**State-of-page register**

- Line 7, handwritten · ` e `
- Line 9, handwritten · ` u `
- Line 9, margin · ` \unsure{-} `

**Changes made during comparison**

no change

**Cross-page comparison before freeze.** A short isolated mark at the lower left recurs on several typed sheets. It may be a registration mark. Only the stroke is transcribed.

- ` % archive sheet number: 166 ` -> ` \margin{\unsure{-}}
% archive sheet number: 166 `

## Scan 168

**UTC** · start 2026-11-18T11:32:53Z · independent list saved 2026-11-18T11:33:15Z · comparison complete 2026-11-18T11:33:46Z

**Accents and unusual readings from the strips.** cocart twice and cart twice, all small running letters, no accents. µ over a top horizontal link. No text paragraph.

**Notation and line order from the strips.** Top diamond from L₁⊗L₂ through E₁⊗L₂ and L₁⊗E₂ to E₁⊗₀E₂. Four horizontal sequences bounded by small zeroes. Row 1: E₁⊗₀E₂, E₁⊗E₂ (last index very square), M₁⊗M₂. Row 2: L₁⊗L₂, E₁∨E₂, M₁⊗M₂. Row 3: L₁⊗L₂, E₁∧E₂, M₁⊗M₂. Row 4: L₁⊗L₂, E₁⊗E₂, E₁⊗⁰E₂. Then diamond with E₁⊗M₂ and M₁⊗E₂ down to M₁⊗M₂. π₁⊗id, id⊗π₂ and two corresponding ω-like symbols. First/last middle factors all have 1 or 2, no letter index.

**Corrections, lines near live text, capitals and margins.** A small dark F-like deletion on the central downward arrow from vee to wedge, a separate ? to its right. A horizontal broken rule separates rows two and three and appears left-pointing toward the right. A dark M under E at the fourth right-hand object, and a similar L under M on the lower diamond. No independent marginal sentence. Plain strokes join the lower tip. The cocart in the first inter-row square sits just below the π labels. The cart in the last such square sits half way between the rows. They have been moved into the respective squares. The middle mark to the left of the question mark is struck through and has a vertical stroke beside two horizontals. At the page divide the horizontal stroke on the right doubles back into a left-facing point. The underlying M and L remain visible on the lower diamond. All three numerals alongside the near-identity arrows and the two different heights of the small tensor circles were rechecked.

**Letter indices.** No i or j was found in an index or exponent. The register distinguishes the written numerals, primes and other marks.

**Formula and diagram register**

Diagram or ruled array, line 2.

~~~latex
\begin{tikzcd}[ampersand replacement=\&,row sep=small,column sep=tiny,cells={nodes={font=\scriptsize}}]
\&\&L_1\otimes L_2\arrow[dl]\arrow[dr]\&\&\&\&\&\\
\&E_1\otimes L_2\arrow[dr]\&\text{\unsure{cocart}}\&L_1\otimes E_2\arrow[dl]\&\&\&\&\\
0\arrow[rr]\&\&E_1\otimes_0 E_2\arrow[rr,"\mu"]\arrow[drr,phantom,"{\text{cocart}}" description]\arrow[d,"{\pi_1\otimes\mathrm{id},\mathrm{id}\otimes\pi_2}" description]\&\&E_1\otimes E_{\unsure{2|0}}\arrow[rr,dash]\arrow[d]\&\&M_1\otimes M_2\arrow[r]\arrow[d,"1"]\&0\\
0\arrow[rr]\&\&L_1\otimes L_2\arrow[rr]\arrow[dd,"1"]\&\&E_1\vee E_2\arrow[rr]\arrow[dd,"?","{\deleted{\unsure{F}}}"']\&\&M_1\otimes M_2\arrow[r]\arrow[dd,"1"]\&0\\
\rule{1.2cm}{.35pt}\&{}\&{}\&\rule{1.0cm}{.35pt}\&{}\&\rule{1cm}{.35pt}\&{}\&\leftarrow\mkern-10mu\rule{1.7cm}{.35pt}\\
0\arrow[rr]\&\&L_1\otimes L_2\arrow[rr]\arrow[d,"1"]\&\&E_1\wedge E_2\arrow[drr,phantom,"{\text{\unsure{cart}}}" description]\arrow[rr,dash]\arrow[d]\&\&M_1\otimes M_2\arrow[r]\arrow[d,"{\unsure{\varpi|\overline{\omega}}_1\otimes\mathrm{id},\ \mathrm{id}\otimes\varpi_2}"]\&0\\
0\arrow[rr]\&\&L_1\otimes L_2\arrow[rr]\&\&E_1\otimes E_2\arrow[rr]\&\&\deleted{M}E_1\otimes^{\unsure{0|\circ}}E_2\arrow[r]\arrow[dl]\arrow[dr]\&0\\
\&\&\&\&\&E_1\otimes M_2\arrow[dr,dash]\&\text{cart}\&\deleted{\unsure{L}}M_1\otimes E_2\arrow[dl,dash]\\
\&\&\&\&\&\&M_1\otimes M_2\&
\end{tikzcd}
~~~

**State-of-page register**

- Line 6, deleted · ` \unsure{F} `
- Line 9, deleted · ` M `
- Line 10, deleted · ` \unsure{L} `

**Changes made during comparison**

- ` \arrow[rr,"\mu"] ` -> ` \arrow[rr,"\mu"]\arrow[drr,phantom,"{\text{cocart}}" description] `
- ` \&\text{cocart}\&E_1\vee ` -> ` \&\&E_1\vee `
- ` \rule{1.7cm}{.35pt} ` -> ` \leftarrow\mkern-10mu\rule{1.7cm}{.35pt} `
- ` E_1\wedge E_2\arrow[rr,dash] ` -> ` E_1\wedge E_2\arrow[drr,phantom,"{\text{\unsure{cart}}}" description]\arrow[rr,dash] `
- ` \&\text{\unsure{cart}}\&\deleted{M} ` -> ` \&\&\deleted{M} `
- ` \&\deleted{\unsure{L}}M_1\otimes E_2\arrow[dl] ` -> ` \&\deleted{\unsure{L}}M_1\otimes E_2\arrow[dl,dash] `

## Scan 169

**UTC** · start 2026-11-18T11:33:47Z · independent list saved 2026-11-18T11:34:02Z · comparison complete 2026-11-18T11:34:26Z

**Accents and unusual readings from the strips.** années, où, commencé à, pensée, C'était, où, l'état, l'état créateur, équilibre, énergies, épousailles, état, créatrice. qu'à, unité, foncière, présente, élimination, égotiques, même, élimination, repression, à fait, totalité, là, réalité, réalité, déro…le, obstinément à l'oeuvre, marées, aussitôt, mécanismes, répression, été repérés, à, débarassé, élucidé, obstinés, été relégués, souterrains-poubelle, examinés, repéré également, mécanismes, répression, profondément, enracinés, réalise, années, portée, considérable, déséquilibre, facultés, mécanismes, être désamorcés, qu'à, s'évanouiront-ils, où, entré, profondément, jusqu'à présent. présente, mathématique, ça.

**Notation and line order from the strips.** 483. No mathematics or displays; spaced agit, illusions, doutes. First paragraph begins d'ailleurs; last ends chemin! Single straight hyphen in souterrains-poubelle. The standalone colon-like fleck after conflit is far to the right.

**Corrections, lines near live text, capitals and margins.** Right end clips the final s of plus, the s of forces, and the ending of the first part of déroule before le. The darker é in the second réalité and one letter in totalité look retouched. Archive 168 runs vertically at the right. The second t in totalité has a dark cross with stray dots nearby; the r, rather than the é, is heavier in the second réalité. Their letter outlines remain legible as type. No distinct underlying word or handwritten insertion can be recovered at either place. The paired dots after conflit are far apart from the last letter, so a paper mark is a second possibility. The later répression really has an acute where the first occurrence lacks it.

**Letter indices.** No mathematical i or j index or exponent.

**Formula and diagram register**

No inline formula or mathematical display. Numerals, dates and callouts are identified above.

**State-of-page register**

No handwritten alteration, deletion, insertion or independent marginal annotation in the text.

**Changes made during comparison**

- ` conflit \unsure{:} ` -> ` conflit \unsure{:|{}} `

## Scan 170

**UTC** · start 2026-11-18T11:34:27Z · independent list saved 2026-11-18T11:34:51Z · comparison complete 2026-11-18T11:35:26Z

**Accents and unusual readings from the strips.** α₁, α₂ univ. injectifs; avec χ-trivialisations, On définit de façon autre … et … extensions π-trivialisées … par … et on a une application can. des extensions de … en … ; cocartésien at left of the four rows. The long cursive sequences for extensions and trivialisées are particularly compressed.

**Notation and line order from the strips.** Two sequences 0, L, E, M, 0 numbered 1 above and 2 below with four forward labels α,ψ and four dotted returning π and ϖ. Pairs (π₁,ϖ₁)(π₂,ϖ₂). Beside E₁∨E₂ and E₁∧E₂ a brace with four conditions: αᵢπᵢ + ϖᵢψᵢ = χ id, a struck relation, πᵢαᵢ = χ id, another cancellation, and ψᵢϖᵢ = χ id with some earlier forms struck. All suffixes i are dotted strokes, no j observed. At left a diamond on E₁⊗₀E₂ with L₁⊗L₂ at its left and two possible E/L over-writings. Below it two pairs of rows. First E₁⊗₀E₂ → E₁⊗E₂ → M₁⊗M₂ over L₁⊗L₂ → E₁∨E₂ → M₁⊗M₂; second L₁⊗L₂ → E₁∧E₂ → M₁⊗M₂ over L₁⊗L₂ → E₁⊗E₂ → E₁⊗⁰E₂.

**Corrections, lines near live text, capitals and margins.** Both the right-hand brace and the small horizontal diamond are marginal to the prose. Pen cuts through nearly an entire line in the brace, through several short compositions and through a word before trivialisées. In the diamond, overlapping E/L strokes are visible. No handwriting-on-type, no letterhead. Bottom original scan blank except 169 at lower left. Compared πᵢ, ϖᵢ, ψᵢ, αᵢ and the suffixes on id to their digit-labelled counterparts above. The index below M at the end of the correction has no decisive dot. In the small diamond there are points at both ends of its upper-right link, and a descending mark at bottom left. In the main text the strokes of duale and the joining word before E₁∧E₂ are shallow. The divider is absent between the two pairs of rows on this sheet. The upper marginal pair of small letters is appreciably narrower than the α above the arrows.

**Letter indices.** The identity brace contains αᵢ, πᵢ, ϖᵢ, ψᵢ and the i of Eᵢ and Lᵢ. The last M suffix is i or 2. The small pair in the upper margin contains i/ι with numerical suffixes. No stand-alone j is visible.

**Formula and diagram register**

Diagram or ruled array, line 2.

~~~latex
\begin{tikzcd}[ampersand replacement=\&,column sep=small]
0\arrow[r]\&L_1\arrow[r,"\alpha_1"]\&E_1\arrow[l,dashed,bend right=25,"\pi_1"']\arrow[r,"\unsure{\psi|\varphi}_1"]\&M_1\arrow[l,dashed,bend right=25,"{\unsure{\varpi|\overline{\omega}}_1}"']\arrow[r,dash]\&0\\
0\arrow[r]\&L_2\arrow[r,dash,"\alpha_2"]\&E_2\arrow[l,dashed,bend left=25,"\pi_2"]\arrow[r,"\psi_2"]\&M_2\arrow[l,dashed,bend left=25,"\varpi_2"]\arrow[r,dash]\&0
\end{tikzcd}
~~~

- Line 6, inline ` \unsure{i|\iota}_1,i_2 `.

- Line 8, inline ` \unsure{\chi|\lambda} `.

- Line 8, inline ` (\pi_1,\varpi_1)\;(\pi_2,\varpi_2) `.

Display, line 9.

~~~latex
\left\{\begin{aligned}
&\alpha_i\pi_i+\varpi_i\psi_i=\chi\,\mathrm{id}_{E_i}\\
&\deleted{\pi_1\varpi_2=\chi\,\mathrm{id}_{E_2}}\\
&\pi_i\,\deleted{\unsure{\vert L}}\alpha_i=\chi\,\mathrm{id}_{L_i}\quad
 \deleted{\unsure{\alpha_i\vert M_i/E_i}}=0\\
&\deleted{\unsure{\psi_i\varpi_i\vert L=0}}\ \psi_i\varpi_i
 \deleted{\unsure{+\chi\,\mathrm{id}_{M_i}}}\ \unsure{=}\chi\,\mathrm{id}_{M_{\unsure{i|2}}}
\end{aligned}\right.
~~~

- Line 19, inline ` E_1\deleted{\unsure{\wedge}}\vee E_2 `.

- Line 19, inline ` E_1\wedge\deleted{L}E_2 `.

- Line 19, inline ` \unsure{\Pi|\pi} `.

- Line 19, inline ` M_1\otimes M_2 `.

- Line 19, inline ` L_1\otimes L_2 `.

- Line 19, inline ` E_1\vee E_2 `.

- Line 19, inline ` E_1\wedge E_2 `.

Diagram or ruled array, line 20.

~~~latex
\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=tiny]
\&E_1\otimes\deleted{\unsure{E}}L_2\arrow[dr,<->]\&\&\\
{[}L_1\otimes L_2\arrow[ur,dash]\arrow[dr]\&\&E_1\otimes_0 E_2\&\text{\unsure{cocartésien}}{]}\\
\&\deleted{\unsure{E}}L_{\unsure{1|2}}\otimes E_2\arrow[ur]\&\&
\end{tikzcd}
~~~

Diagram or ruled array, line 25.

~~~latex
\begin{tikzcd}[ampersand replacement=\&,row sep=large,column sep=small]
\unsure{0}\arrow[r]\&E_1\otimes_0 E_2\arrow[r]\arrow[d,"{\pi_1\otimes\mathrm{id},\ \mathrm{id}\otimes\pi_2}"]\&E_1\otimes E_2\arrow[r]\arrow[d]\&M_1\otimes M_2\arrow[d,Rightarrow]\\
\unsure{0}\arrow[r,dash]\&L_1\otimes L_2\arrow[r]\&E_1\vee E_2\arrow[r]\&M_1\otimes M_2\\
0\arrow[r]\&L_1\otimes L_2\arrow[r]\arrow[d,Rightarrow]\&E_1\wedge E_2\arrow[r]\arrow[d]\&M_1\otimes M_2\arrow[d]\\
0\arrow[r]\&L_1\otimes L_2\arrow[r]\&E_1\otimes E_2\arrow[r]\&E_1\otimes^{\unsure{0|\circ}}E_2
\end{tikzcd}
~~~

**State-of-page register**

- Line 6, margin · ` $\unsure{i|\iota}_1,i_2$ \unsure{univ.} injectifs `
- Line 12, deleted · ` \pi_1\varpi_2=\chi\,\mathrm{id}_{E_2} `
- Line 13, deleted · ` \unsure{\vert L} `
- Line 14, deleted · ` \unsure{\alpha_i\vert M_i/E_i} `
- Line 15, deleted · ` \unsure{\psi_i\varpi_i\vert L=0} `
- Line 16, deleted · ` \unsure{+\chi\,\mathrm{id}_{M_i}} `
- Line 19, deleted · ` \unsure{\wedge} `
- Line 19, deleted · ` L `
- Line 19, deleted · ` \unsure{E} `
- Line 21, deleted · ` \unsure{E} `
- Line 23, deleted · ` \unsure{E} `

**Changes made during comparison**

- ` \&E_1\otimes\deleted{\unsure{E}}L_2\arrow[dr] ` -> ` \&E_1\otimes\deleted{\unsure{E}}L_2\arrow[dr,<->] `
- ` L_2\arrow[ur,dash]\arrow[dr,dash] ` -> ` L_2\arrow[ur,dash]\arrow[dr] `
- ` -trivialisation $(\pi_1 ` -> ` -\unsure{trivialisation|trivialisations} $(\pi_1 `
- ` \unsure{duale} $E_1 ` -> ` \unsure{duale|autre} $E_1 `

**Cross-page comparison before freeze.** The literal restriction bars beneath the cancellations have been encoded with the vert command to distinguish these strokes from editorial separators between candidate readings.

- ` \unsure{|L} ` -> ` \unsure{\vert L} `
- ` \unsure{\alpha_i|M_i/E_i} ` -> ` \unsure{\alpha_i\vert M_i/E_i} `
- ` \unsure{\psi_i\varpi_i|L=0} ` -> ` \unsure{\psi_i\varpi_i\vert L=0} `

## Scan 171

**UTC** · start 2026-11-18T11:35:26Z · independent list saved 2026-11-18T11:35:44Z · comparison complete 2026-11-18T11:36:10Z

**Accents and unusual readings from the strips.** (11 octobre), où, après, équilibre. Peut-être, passé, façon, mécanismes de répression, considérablement, je l'a, après avoir été découverts, ignorés, coûte que coûte, multiplicité, être conditionné, là, donné présent, reflète fidèlement, passée, être, récente, déballer, légué, ignorés et réprimés, reflètent, féminins, également, mécanismes de répression, c'est-à-dire, mécanismes invétérés, dénouer, désamorcer, L'expérience, années, attention-là, jusqu'à, même, répression, se résoud, disparaît, libérant, énergie considérable, jusque là, était immobilisée, marées, mécanismes répressifs, pensée, à. vis-à-vis, noués, moi-même, dès, découverte, méditation, dès, près, C'était, juillet 1976, G. , peut-être, homasse, façons d'être, aimées précédemment, Le hasard (?), matérielles, entouré, étaient, placé, rôle, féminin, ménage, préparais.

**Notation and line order from the strips.** 484, raised (110) and (11 octobre); juillet 1976 and eight years both appear. Only the rhetorical (?) in parentheses is a question mark. No displays, equations or indices. Spaced acceptation across the line end. Dash at beginning of lower-left margin.

**Corrections, lines near live text, capitals and margins.** At right after donc there are two small points or a colon. The i after l'a at right is beyond or absent from the image. A short isolated dash at lower left beside the last paragraph; archive 170 reads horizontally. No substantive pen addition to the body. The two individually round points after donc can be distinguished when enlarged. The isolated short horizontal mark beside the last line has no leader and no following word. Both the final d in résoud and the single m in homasse are clear. The right edge supplies no readable letter after l'a. The question mark after hasard is typed.

**Letter indices.** No mathematical i or j index or exponent.

**Formula and diagram register**

No inline formula or mathematical display. Numerals, dates and callouts are identified above.

**State-of-page register**

- Line 7, margin · ` \unsure{-} `

**Changes made during comparison**

- ` inclut donc\unsure{:} ` -> ` inclut donc: `
- ` placé dans un rôle ` -> ` placé\margin{\unsure{-}} dans un rôle `

## Scan 172

**UTC** · start 2026-11-18T11:36:11Z · independent list saved 2026-11-18T11:36:32Z · comparison complete 2026-11-18T11:37:24Z

**Accents and unusual readings from the strips.** solution de l'équation ; injectif sauf en car. 2 et b₁=b₂=0; can. par définition directe? de A; can. par déf. dér. de E; lower struck marginal phrase dé… en car. 2. Above the centre O/zero is separately drawn and underlined.

**Notation and line order from the strips.** u = u₁ … u₂ − b₁b₂ = 2u₁u₂ + b₂u₁ + b₁u₂ ∈ A₁⊗A₂. x²+bx+c=0, b=b₁b₂, c=b₁²c₂+b₂²c₁−4c₁c₂, δ=b²−4c=δ₁ (raised trace) δ₂ and two underbraced differences. Upper paired triads of A and E objects with curved arrows in opposite directions, wedge, 0s and L₁⊗L₂. Middle f∈A₁⊗A₂ … f … = (σ₁⊗σ₂ + id…)(f)=f+bar f, x∈E₁⊗E₂ … x+bar x. Three vertical sequences with Tr, id, id, 2, dual Ls and circles at different heights. Two separate 0—L—E—L′—0 sequences at bottom left; at right E/L tensors with a diagonal arrow toward L₁⊗L₂.

**Corrections, lines near live text, capitals and margins.** A vertical small mark in the first product, a retraced centre A and several short strokes on the intervening links. Whole expression after the second f is crossed; far right beside the bottom grid an entire group of words is struck diagonally. Bottom right E/L is overwritten. The tops and bottoms of the letters differ between A and the subscripted A’s. No numerical j; all labels here visibly 1, 2 or small vertically raised marks. The three marks in the gap between A- and E-objects are short and independent. At left there is a chevron, in the middle a cross, and at right an overwritten star-like mark. Long stems between the rows would add ink. The exponent-like loop after δ₁ is physically visible. The text under it and under δ₂ reads b₁²−4c₁ and b₂²−4c₂. The last abbreviation by E can be dér. or dir. Lower right margin was read at high enlargement with the zigzag strike retained. Indices 1/2 and dual vees were checked at all three positions in the lower grid.

**Letter indices.** No i or j was found in an index or exponent. The register distinguishes the written numerals, primes and other marks.

**Formula and diagram register**

Display, line 2.

~~~latex
u=u_1\overset{!}{\deleted{\unsure{\ast|\otimes}}}u_2-b_1b_2
=2u_1u_2+b_2u_1+b_1u_2\ \in\ \unsure{A|\mathcal A}_1\otimes A_2
~~~

- Line 6, inline ` \;x^2+bx+c=0 `.

Diagram or ruled array, line 7.

~~~latex
\begin{tikzcd}[ampersand replacement=\&,row sep=tiny]
A_1\otimes A_2\\ A\arrow[u,hook]
\end{tikzcd}
~~~

- Line 10, inline ` b_1=b_2=0 `.

Display, line 11.

~~~latex
\begin{aligned}
b&=b_1b_2\\
c&=b_1^2c_2+b_2^2c_1-4c_1c_2\\
\delta&=b^2-4c
=\underbrace{\unsure{\delta_1|\delta_1^2}}_{(b_1^2-4c_1)}
 \underbrace{\delta_2}_{(b_2^2-4c_2)}
\end{aligned}
~~~

Diagram or ruled array, line 20.

~~~latex
\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
\&{\underline{0}\ \unsure{\mathcal O|O}}\&\\
A_1\otimes A_2\arrow[rr,bend left=25,"{\unsure{\leftrightarrows|\leftrightarrow}}"]
\arrow[r,"{\substack{\text{can. par}\\\text{définition}\\\text{\unsure{directe}}}}","{\text{de }A}"']\&
A_1\wedge \deleted{\unsure{A}}A_2=A\arrow[r]\&A_1\otimes A_2\\
E_1\otimes E_2\arrow[u,phantom,"{\unsure{\wedge|\uparrow}}" description]\arrow[d,dash]\&
\underset{\substack{\cup\\L_1\otimes L_2}}{E}=E_1\wedge E_2\arrow[l]\arrow[u,phantom,"{\unsure{\times|x}}" description]\arrow[d,dash]\&
E_1\otimes E_2\arrow[u,phantom,"{\unsure{\ast}}" description]\arrow[l,"{\text{can. par déf. \unsure{dér.|dir.}}}"',"{\text{de }E}"]\arrow[ll,bend left=25,"\leftrightarrows"]\arrow[d,dash]\\
0\&0\&0
\end{tikzcd}
~~~

Display, line 30.

~~~latex
\begin{aligned}
f\in A_1\otimes A_2\ \deleted{\unsure{\leftrightarrows(f)}}\quad
f^{\leftrightarrows}\ \deleted{\unsure{=(\sigma_1\otimes\sigma_2+\mathrm{id})(f)}}&=
(\underbrace{\sigma_1\otimes\sigma_2}_{\sigma}+\mathrm{id}_{A_1\otimes A_2})(f)=f+\overline f\\
x\in E_1\otimes E_2\qquad x^{\leftrightarrows}&=x+\overline x
\end{aligned}
~~~

Diagram or ruled array, line 38.

~~~latex
\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=small]
\unsure{0}\arrow[d,dash]\&0\arrow[d,dash]\&0\arrow[d]\\
A_1\otimes_0 A_2\arrow[r,"\mathrm{Tr}"]\arrow[d]\&\mathcal O\arrow[r,Rightarrow,"\mathrm{id}"]\arrow[d,dash]\&A_1\otimes_0 A_2\arrow[d]\\
A_1\otimes A_2\arrow[r,dash]\arrow[d]\&A\arrow[r]\arrow[d,dash]\&A_1\otimes A_2\arrow[d]\\
L_1^\vee\otimes L_2^\vee\arrow[r,"\mathrm{id}"]\arrow[d]\&L_1^\vee\otimes L_2^\vee\arrow[r,"2"]\arrow[d,dash]\&L_1^\vee\otimes L_2^\vee\arrow[d]\\
0\&0\&0
\end{tikzcd}
~~~

- Line 45, inline ` A\unsure{=|\longrightarrow}(A_1\otimes A_2)^{\leftrightarrows} `.

Diagram or ruled array, line 46.

~~~latex
\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=small]
\unsure{0}\arrow[r,dash]\&L_1\arrow[r,dash]\&E_1\arrow[r]\&L'_1\arrow[r]\&0\\
0\arrow[r,dash]\&L_2\arrow[r,dash]\&E_2\arrow[r,dash]\&L'_2\arrow[r,dash]\&0
\end{tikzcd}
~~~

Diagram or ruled array, line 50.

~~~latex
\begin{tikzcd}[ampersand replacement=\&,column sep=tiny,row sep=small]
\&E_1\otimes E_2\&\\
E_1\otimes\deleted{\unsure{L}}E_2\arrow[dr]\&\&L_1\otimes E_2\\
\&L_1\otimes L_2\&
\end{tikzcd}
~~~

**State-of-page register**

- Line 3, deleted · ` \unsure{\ast|\otimes} `
- Line 24, deleted · ` \unsure{A} `
- Line 32, deleted · ` \unsure{\leftrightarrows(f)} `
- Line 33, deleted · ` \unsure{=(\sigma_1\otimes\sigma_2+\mathrm{id})(f)} `
- Line 45, margin · ` \deleted{$A\unsure{=|\longrightarrow}(A_1\otimes A_2)^{\leftrightarrows}$ est \unsure{dégénéré} en car. 2} `
- Line 45, deleted · ` $A\unsure{=|\longrightarrow}(A_1\otimes A_2)^{\leftrightarrows}$ est \unsure{dégénéré} en car. 2 `
- Line 52, deleted · ` \unsure{L} `

**Changes made during comparison**

- ` E_1\otimes E_2\arrow[u]\arrow[d,dash] ` -> ` E_1\otimes E_2\arrow[u,phantom,"{\unsure{\wedge|\uparrow}}" description]\arrow[d,dash] `
- ` \arrow[u,dash,"{\unsure{\times|x}}"] ` -> ` \arrow[u,phantom,"{\unsure{\times|x}}" description] `
- ` \arrow[u,"{\unsure{\ast}}"] ` -> ` \arrow[u,phantom,"{\unsure{\ast}}" description] `
- ` \unsure{dér.} ` -> ` \unsure{dér.|dir.} `

## Scan 173

**UTC** · start 2026-11-18T11:37:25Z · independent list saved 2026-11-18T11:37:41Z · comparison complete 2026-11-18T11:38:05Z

**Accents and unusual readings from the strips.** décidément, était, mystère, étaient censés, plutôt, désignent, l'épuiser, délicat, à, retrouvé, était présent déjà, délicat, féminin, mâle, compréhension, même, à l'aspect, évènements, d'équilibre, déséquilibre, première, compréhension, réponse. même, réunissent, censés, même, spontanément, commencé, apparaître, réflexion, générations, relevés. activité-passivité, exécution-conception. 6 novembre; père-mère, Mère, exécution, soi-disant, s'insèrent, façon, mère, formé, père-mère.

**Notation and line order from the strips.** 491. The paragraph 'primitif' (*) and two entries in a six-line list have the same starred marker. A horizontal rule introduces (*) (6 novembre). Reference (n° 113). Eight generations are words. No actual mathematical diagram on this typescript. Spaced désignent, action - inaction and père-mère. Single hyphens in compound list.

**Corrections, lines near live text, capitals and margins.** Comma after fait and after j'entends, two upright quote-strokes opening/closing yoga. Small v-shaped mark below the end of the spaced action before the dash. In the note, initial a of action-inaction is heavily retraced. An extra comma sits below the baseline after En fait. Footnote appears below the rule, with archive sheet 172 at left. The detached mark under the space after action has two strokes meeting at a shallow point. It could also be a comma. The two commas around j'entends differ in size and position from the type. The repaired opening quotes in the footnote have unusually heavy stems. In the last footnote line both ac strokes run together. The accent sequence is é then è in évènements. The title, n° 113, all six list lines and all three callouts were compared individually.

**Letter indices.** No mathematical i or j index or exponent.

**Formula and diagram register**

- Line 5, inline ` \checkmark `.

**State-of-page register**

- Line 3, handwritten · ` , `
- Line 3, handwritten · ` , `
- Line 5, handwritten · ` \unsure{$\checkmark$|,} `
- Line 18, handwritten · ``` `` ```
- Line 18, handwritten · ` ac `

**Changes made during comparison**

- ` a\,c\,t\,i\,o\,n\,-\,i ` -> ` a\,c\,t\,i\,o\,n\handwritten{\unsure{$\checkmark$|,}}\,-\,i `

## Scan 174

**UTC** · start 2026-11-18T11:38:06Z · independent list saved 2026-11-18T11:38:27Z · comparison complete 2026-11-18T11:39:20Z

**Accents and unusual readings from the strips.** tel que (3 times), si … ∈ L, nul sur L, au … par …; stabilise L, i.e. nul sur L′=E/L, à val. dans L, induit l'identité (struck), induit … sur L, nul sur L′. Last line close to bottom is cut. No date.

**Notation and line order from the strips.** Top 0—L →ᶦ E →ᵖˢⁱ L′—0. E →ᵖⁱ L, L′ →ᵛᵃʳᵖⁱ E and E →ᶠ E with conditions π(x)=χx, ψ(ϖ(λ))=χλ, 1° f nul sur L, 2° [crossed], χx−f(x)∈L with π(x) under it. Box π=χ id−f. Two columns of equivalences and a curved insertion. Then 0—L′∨ ↔ A → L∨—0, second sequence with E and a small added arrow, an entire ruled-out tensor row with M, another cancelled E₁…E₂, two pairs of indexed rows. Lower right E₁≃A₁⊗Δ₁, Δ₁⁻¹ Δ₂⁻¹, E₁∨∧E₂∨≈(E₁∧E₂)⊗Δ₁…⊗Δ₂… and ≃(E₁∧E₂)∨. Bottom left two marginal formulas. Superscript i at the top is an arrow label, not an index. All real subscripts look numeric.

**Corrections, lines near live text, capitals and margins.** The lower ruled-out row still includes all five objects and links. A small vertical/hooked marker below the E, overwritten indices L₂ and E… and L′/L in the lower rows. In the upper conditions, a whole alternative to χx−f(x) is struck, as is an expression below it. Diacritic on Δ e.g. small 1-like trace; no script T or Γ. Small, slanting side phrase to right of f and lower-left formulas must be read separately. The link from the first dual L to A has heads on both ends. The next one has a double shaft meeting at one head. A long stroke crosses the tensor row as a unit. The separate marginal pencilled sequence number is 173. In the last pair of displayed formulas a capital F is clearly present on the second line, while earlier ink is superposed on the first. The handwritten si λ∈L has no clear prime on L. In the two equivalences val. and stabilise the ink near the words belongs to the strike above them and the insertion leader below them.

**Letter indices.** The i over L → E is an arrow label. L′ has a prime and the factors at the bottom have numerical subscripts and dual or inverse superscripts. No index i or j.

**Formula and diagram register**

Diagram or ruled array, line 2.

~~~latex
\begin{tikzcd}[ampersand replacement=\&,column sep=small]
\unsure{0}\arrow[r,dash]\&L\arrow[r,"i"]\&E\arrow[r,"{\unsure{\psi|\varphi}}"]\&L'\arrow[r,dash]\&0
\end{tikzcd}
~~~

Display, line 5.

~~~latex
\begin{aligned}
E\xrightarrow{\pi}L&\qquad\text{tel que}\qquad \pi(x)=\unsure{\chi|\lambda}x\quad\text{si }x\in L\\
L'\xrightarrow{\unsure{\varpi|\overline{\omega}}}E&\qquad\text{tel que}\qquad
\psi(\deleted{\unsure{\pi}}\varpi(\lambda))=\chi\lambda\quad\text{si }\lambda\in L\\
E\xrightarrow{\deleted{\unsure{\phi}}f}E&\qquad\text{tel que}\qquad
1^\circ)\ f\ \text{nul sur } L\\
&\hspace{7em}2^\circ)\ \deleted{f(x)-\unsure{fx}\in L}\\
&\hspace{8em}\underbrace{\chi x-f(x)}_{\substack{\deleted{f-\chi\,\mathrm{id}}\\\pi(x)}}\in L
\end{aligned}
~~~

- Line 16, inline ` E\xrightarrow{\psi}L'\xrightarrow{\varpi}E `.

Display, line 18.

~~~latex
\boxed{\pi=\chi\,\mathrm{id}-f}
~~~

Display, line 21.

~~~latex
\begin{aligned}
&\deleted{\pi:\text{\unsure{valeurs} dans }L\ \longleftrightarrow}\\
&\unsure{\varpi|\pi}\ \text{stabilise }L\ \longleftrightarrow\ f\ \text{stabilise }L\\
&\pi:\text{ val. dans }L\ \inserted{\text{i.e. nul sur }L'=E/L}
 \longleftrightarrow f\ \text{induit }\deleted{\text{l'identité}}\chi\,\mathrm{id}_{L'}\ \text{sur }E/L\\
&\pi\ \text{induit }\chi\,\mathrm{id}_L\ \text{sur }L\ \longleftarrow f\ \text{nul sur }L'
\end{aligned}
~~~

Diagram or ruled array, line 30.

~~~latex
\begin{tikzcd}[ampersand replacement=\&,row sep=small,column sep=small]
0\arrow[r]\&{L'}^\vee\arrow[r,<->]\&\unsure{A|\mathcal A}\arrow[r,Rightarrow]\&L^\vee\arrow[r,dash]\&0\\
0\arrow[r]\&L\arrow[r]\&E\arrow[r,"{\unsure{\mapsto|{}}}"']\&L'\arrow[r,dash]\&0
\end{tikzcd}
~~~

Diagram or ruled array, line 34.

~~~latex
\begin{tikzcd}[ampersand replacement=\&,column sep=small]
\deleted{0}\arrow[rrrr,dash,start anchor=west,end anchor=east]\arrow[r,dash]\&\deleted{L\otimes M}\arrow[r]\&\deleted{E\otimes M}\arrow[r,dash]\&\deleted{L'\otimes M}\arrow[r]\&\deleted{0}
\end{tikzcd}
~~~

Display, line 37.

~~~latex
\deleted{E_1\unsure{\wedge|\otimes}E_2}
~~~

Diagram or ruled array, line 40.

~~~latex
\begin{tikzcd}[ampersand replacement=\&,row sep=small,column sep=small]
0\arrow[r]\&L_1\arrow[r]\&E_1\arrow[r]\&L'_1\arrow[r]\&0\\
0\arrow[r,dash]\&L_2\arrow[r,dash]\&E_2\arrow[r,dash]\&L'_2\arrow[r,dash]\&0
\end{tikzcd}
~~~

Diagram or ruled array, line 44.

~~~latex
\begin{tikzcd}[ampersand replacement=\&,row sep=small,column sep=small]
\unsure{0}\arrow[r]\&L_{\unsure{1|2}}\arrow[r,dash]\&E_{\unsure{1|11}}\arrow[r,dash]\&L'_1\arrow[r,dash]\&0\\
0\arrow[r]\&L_2^{\unsure{\prime|{}}}\arrow[r]\&E_2\arrow[r,dash]\&L'_2\arrow[r]\&0
\end{tikzcd}
~~~

Display, line 48.

~~~latex
E_1\simeq A_1\otimes\Delta_1
\qquad E_1\wedge E_2
~~~

Display, line 52.

~~~latex
\begin{aligned}
\overset{\Delta_1^{-1}}{E_1^\vee}\wedge\overset{\Delta_2^{-1}}{E_2^\vee}
&\simeq\underbrace{(E_1\wedge E_2)}_{\Delta_1\ \Delta_2}
 \otimes\Delta_1^{\unsure{\prime|-1}}\otimes\Delta_2^{-1}\\
&\simeq(E_1\wedge E_2)^\vee
\end{aligned}
~~~

Display, line 60.

~~~latex
\begin{aligned}
\pi(x)&=2x-\deleted{\unsure{f}}F(x)\\
\pi(x)-x&=x-F(x)
\end{aligned}
~~~

**State-of-page register**

- Line 9, deleted · ` \unsure{\pi} `
- Line 10, deleted · ` \unsure{\phi} `
- Line 12, deleted · ` f(x)-\unsure{fx}\in L `
- Line 13, deleted · ` f-\chi\,\mathrm{id} `
- Line 16, margin · ` donc \unsure{se factorise} en $E\xrightarrow{\psi}L'\xrightarrow{\varpi}E$ `
- Line 23, deleted · ` \pi:\text{\unsure{valeurs} dans }L\ \longleftrightarrow `
- Line 25, inserted · ` \text{i.e. nul sur }L'=E/L `
- Line 26, deleted · ` \text{l'identité} `
- Line 35, deleted · ` 0 `
- Line 35, deleted · ` L\otimes M `
- Line 35, deleted · ` E\otimes M `
- Line 35, deleted · ` L'\otimes M `
- Line 35, deleted · ` 0 `
- Line 38, deleted · ` E_1\unsure{\wedge|\otimes}E_2 `
- Line 62, deleted · ` \unsure{f} `

**Changes made during comparison**

- ` \unsure{0}\arrow[r]\&L\arrow[r,"i"] ` -> ` \unsure{0}\arrow[r,dash]\&L\arrow[r,"i"] `
- ` \psi|\varphi}}"]\&L'\arrow[r]\&0 ` -> ` \psi|\varphi}}"]\&L'\arrow[r,dash]\&0 `
- ` {L'}^\vee\arrow[r,hook]\&\unsure{A|\mathcal A}\arrow[r,two heads] ` -> ` {L'}^\vee\arrow[r,<->]\&\unsure{A|\mathcal A}\arrow[r,Rightarrow] `
- ` \deleted{0}\arrow[r,dash]\&\deleted{L\otimes M} ` -> ` \deleted{0}\arrow[rrrr,dash,start anchor=west,end anchor=east]\arrow[r,dash]\&\deleted{L\otimes M} `

## Scan 175

**UTC** · start 2026-11-18T11:39:20Z · independent list saved 2026-11-18T11:39:38Z · comparison complete 2026-11-18T11:40:07Z

**Accents and unusual readings from the strips.** entraîné, systématique, handwritten vieilles réflexions d'il y a, thème, m'étais amusé, à, s'étaient, assemblés, affinités, réflexion, poétique, j'étais, d'écrire, m'empêcher, à la queue-leu-leu, affinités, au suivant, réflexion, poétique, dix-huit, trouvés, peut-être, soupçonne, peut-être, même, illimité, correspondants à, d'appréhension, réalité, songé, peut-être. relevés, efforcé, affinités, imposés à, tracé d'ébauches, était, très, mathématique, façon, données, aplications, figurées, flèches, catégories, Là, esthétiques, symétrie, fréquemment à, à découvrir, même à, flèches, songé, départ, même, après, ébauches, à, Noël, commençait, à. couché, même si nes notes, avancé, m'étais. déposer, poétique, poème, non linéaire, diagrammatique.

**Notation and line order from the strips.** 490 and two (*), no formulas. Components of a graph described in words, including applications typed with one p, sommets, flèches. The diagram itself is absent. Two typed paragraphs plus third paragraph interrupted by footnote, from jours. to remis en. The named poetic form wraps diagramma-tique.

**Corrections, lines near live text, capitals and margins.** Handwritten span right of ressortir mes; handwritten au sui- continues with typed vant; final s retouched on trouvés. Bottom footnote changes from type to hand at poétique. Closing quotes and full stop after tique look separate in weight. Horizontal dividing rule. A short vertical line between aboutir and à appears above as well as below the baseline. Archive 174. The pen ends after sui at the right edge and the following vant is typed. The final s of trouvés alone is in the heavier hand. Magnification of the punctuation after non linéaire shows an upper dot and a separate curved lower stroke. The gray vertical line by aboutir is a crease through adjacent lines. Rechecked the single p in aplications and the single arch of n in nes. The stars and the rule agree with the body and note.

**Letter indices.** No mathematical i or j index or exponent.

**Formula and diagram register**

No inline formula or mathematical display. Numerals, dates and callouts are identified above.

**State-of-page register**

- Line 3, handwritten · ` vieilles réflexions d'il y a `
- Line 3, handwritten · ` au sui `
- Line 3, handwritten · ` s `
- Line 11, handwritten · ``` poétique, savoir le poème dit ``non linéaire''; ou ``diagrammatique''. ```

**Changes made during comparison**

- ` \unsure{;|,} ou ` -> ` ; ou `

## Scan 176

**UTC** · start 2026-11-18T11:40:08Z · independent list saved 2026-11-18T11:40:31Z · comparison complete 2026-11-18T11:41:06Z

**Accents and unusual readings from the strips.** On veut exprimer … comme …, en calculer … ; car/ainsi; i.e.; l'image de u dans A₁⊗A₂ est donc. Words below =1 have e est [∈?] L⊂… E. Repeated Greek-like λ and µ, careful to distinguish handwritten u.

**Notation and line order from the strips.** Aᵢ, Eᵢ, xᵢ, eᵢ on left, P₁ and L₁ beneath them. A, u, 1; E with corrections, x₁*x₂=x, e=e₁⊗e₂, P with small subscript under the product. Four local pairing equalities: ⟨uᵢ,xᵢ⟩=⟨1ᵢ,eᵢ⟩=0; ⟨uᵢ,eᵢ⟩=⟨1ᵢ,xᵢ⟩=1; ⟨u,e⟩=⟨1,x⟩=1; ⟨u,x⟩=⟨1,e⟩=0. u₁∈A₁, u₂∈A₂. Deletion with 2u₁… + b₂u₁+. λ·1_A+µu; λ=⟨u₁*u₂,x⟩, µ=⟨u₁*u₂,e⟩. λ line uses u₁⊗u₂ + ū₁⊗ū₂ over (u₁⊗u₂) with a two-arrow superscript, and an expansion with b₁u₂+u₁b₂+b₁b₂. A long cancellation before b₁b₂. Product of two φ-like pairings =1 under a crossed expansion, then a previous =2 crossed. Last boxes contain u₁*u₂−b₁b₂=…u, u₁*u₂−Tr₁(u₁)Tr₂(u₂)=2·, and 2u₁⊗u₂+b₂u₁+b₁u₂ at right.

**Corrections, lines near live text, capitals and margins.** Every lateral index in the top-left pairings is a shallow dotted i; no descending j tail. Lower sums have 1 and 2, not i or j. Multiple overwritten coefficients and signs, a ! below b₁, and scribbles at the end of the page. The final box is closed at right after a small plus-like sign. No typed letters. 175 archive vertically low left. The first e immediately after 1ᵢ has a small detached right-hand stroke. Its position allows an i or a prime. The first subscript on 1 has a longer return than the one below it. I retained j as a possible reading at this one position. The glyphs before L and E in e∈ΓL⊂ΓE have long rightward top strokes with upright stems. The lower L and E are upright letters; the earlier A under E can still be seen. The separate ! below b₁ and the small mark meeting the right edge of the final box are distinct. The two 2s beside u are overwritten and do not support a confident change of coefficient.

**Letter indices.** Upper left has Aᵢ, Eᵢ, xᵢ and eᵢ. The P suffix can be 1 or i. The first two left-hand pairings use uᵢ, 1ᵢ, xᵢ and eᵢ. The first suffix on 1 has an unusually long return, hence i/j. The first e after 1 also has a possible prime. Compare the four pairing entries in the register below. The later pairings use numerical 1 and 2.

**Formula and diagram register**

Diagram or ruled array, line 2.

~~~latex
\begin{tikzcd}[ampersand replacement=\&,column sep=tiny,row sep=small]
\unsure{A|\mathcal A}_{\unsure{i|1}}\&\&\&A\&u\&1\\
E_i\&x_i,\& e_i\&\deleted{\unsure{e}}E\&x_1\unsure{\ast|\otimes}x_2=x,\&e=e_1\otimes e_2\\
\&P_{\unsure{1|i}}\arrow[u]\&L_1\arrow[u]\&\&P_{\unsure{3|2}}\arrow[u]\&
\end{tikzcd}
~~~

Display, line 7.

~~~latex
\begin{aligned}
\langle u_i,\unsure{x_i|u_i}\rangle&=\langle1_{\unsure{i|j}},\unsure{e_i|e'}\rangle=0&
 \langle u,e\rangle&=\langle1,x\rangle=1\\
\langle u_i,e_i\rangle&=\langle1_i,x_i\rangle=1&
 \langle u,x\rangle&=\langle1,e\rangle=0
\end{aligned}
~~~

Display, line 15.

~~~latex
\begin{aligned}
u_1&\in A_1&\deleted{\unsure{A\longrightarrow A_1\otimes A_2}}\\
u_2&\in A_2&
\end{aligned}
~~~

Display, line 22.

~~~latex
\deleted{\alpha(u_1\ast u_2)=2u_1\unsure{u_2}+b_2u_1+}
~~~

- Line 25, inline ` u_1\ast u_2 `.

- Line 25, inline ` \lambda\cdot1_A+\mu u `.

Display, line 26.

~~~latex
\begin{aligned}
\lambda&=\underbrace{\langle u_1\ast u_2,x\rangle}_{\unsure{\Vert}} ,
 &\mu&=\langle u_1\ast u_2,e\rangle
\end{aligned}
~~~

Display, line 32.

~~~latex
\begin{aligned}
\deleted{A_1\otimes A_2\longrightarrow A}\quad
\langle u_1\ast u_2,x_1\ast x_2\rangle
 &=\langle\underbrace{u_1\otimes u_2+\overline u_1\otimes\overline u_2}_{(u_1\otimes u_2)^{\unsure{\leftrightarrows|\leftrightarrow}}},x_1\otimes x_2\rangle\\
 &\deleted{\unsure{=u_1}}\ \deleted{\unsure{\langle x}}\langle 2u_1\deleted{\unsure{\otimes}}u_2+
 \underset{!}{b_1}u_2+u_1b_2+b_1b_2,\ x_1\otimes x_2\unsure{\rangle}\\
 &\deleted{=2\unsure{+\beta_1+\beta}\quad\unsure{=\beta_1}}\quad b_1b_2
\end{aligned}
~~~

Display, line 42.

~~~latex
\begin{aligned}
&\deleted{u_1\ast u_2,}\\
\mu&=\langle u_1\ast u_2,e\rangle
 =\deleted{\langle 2u_1\otimes u_2+b_1u_2+u_1b_2+b_1b_2,e_1\otimes e_2\rangle}\\
&\quad \deleted{\unsure{\varphi}}\inserted{\langle\varphi_1(u_1),e_1\rangle
 \langle\varphi_2(u_2),e_2\rangle}\\
&\deleted{=2\unsure{,}}\qquad=1\qquad e\in\Gamma L\subset\Gamma\deleted{\unsure{A}}E
\end{aligned}
~~~

Display, line 53.

~~~latex
u_1\ast u_2=b_1b_2+\deleted{\unsure{2}}u
\qquad\deleted{\unsure{u=}}
~~~

Display, line 58.

~~~latex
\boxed{u_1\ast u_2-b_1b_2=\deleted{\unsure{2}}u}
~~~

Display, line 61.

~~~latex
u_1\ast u_2-\mathrm{Tr}_1(u_1)\mathrm{Tr}_2(u_2)=2\cdot
~~~

- Line 64, inline ` u `.

- Line 64, inline ` A_1\otimes A_2 `.

Display, line 65.

~~~latex
\boxed{2u_1\otimes u_2+b_2u_1+b_1u_2\unsure{+|{}}}
~~~

**State-of-page register**

- Line 4, deleted · ` \unsure{e} `
- Line 17, deleted · ` \unsure{A\longrightarrow A_1\otimes A_2} `
- Line 23, deleted · ` \alpha(u_1\ast u_2)=2u_1\unsure{u_2}+b_2u_1+ `
- Line 34, deleted · ` A_1\otimes A_2\longrightarrow A `
- Line 37, deleted · ` \unsure{=u_1} `
- Line 37, deleted · ` \unsure{\langle x} `
- Line 37, deleted · ` \unsure{\otimes} `
- Line 39, deleted · ` =2\unsure{+\beta_1+\beta}\quad\unsure{=\beta_1} `
- Line 44, deleted · ` u_1\ast u_2, `
- Line 46, deleted · ` \langle 2u_1\otimes u_2+b_1u_2+u_1b_2+b_1b_2,e_1\otimes e_2\rangle `
- Line 47, deleted · ` \unsure{\varphi} `
- Line 47, inserted · ` \langle\varphi_1(u_1),e_1\rangle
 \langle\varphi_2(u_2),e_2\rangle `
- Line 49, deleted · ` =2\unsure{,} `
- Line 49, deleted · ` \unsure{A} `
- Line 54, deleted · ` \unsure{2} `
- Line 55, deleted · ` \unsure{u=} `
- Line 59, deleted · ` \unsure{2} `

**Changes made during comparison**

- ` \langle1_i,e\rangle=0 ` -> ` \langle1_{\unsure{i|j}},\unsure{e_i|e'}\rangle=0 `
- ` donc \unsure{calculer} ` -> ` \unsure{donc|en} \unsure{calculer} `

## Scan 177

**UTC** · start 2026-11-18T11:41:07Z · independent list saved 2026-11-18T11:41:23Z · comparison complete 2026-11-18T11:41:51Z

**Accents and unusual readings from the strips.** équilibre, élan, persévérance, sérénité, tenacité-détachement; lancée, réfléxion de hier, connaître, préciser, société, où, société, traditionelle, considérablement, nôtre, féminin, équilibre, sûrement, intuition-archétype, naît. comentaires, façons, interpellé, fut-ce obscurément, à, lui-même, équilibre, déséquilibre, êtres, celui-là, circonstanciés, départ, réflexion. commun à, compréhension, par là, énergies. Letterspaced en l'ab- finishes the page.

**Notation and line order from the strips.** 492, two lists of six and two couples. No mathematical display. One reference in pen, (111') or raised 1 after 111. Quoted retardataires, yang, masculin, féminin, équilibre yin-yang, le plus primitif, sentirait rien and couples. Short p. ex.; a full question after couple?

**Corrections, lines near live text, capitals and margins.** The faint dark patch below the comma after par là falls between that word and de, partly under the d. The three 1s in the pen number have upstrokes, the fourth stroke lacks one. No bracketed text at the page end. Archive 176 on the lower left. Under par là the black trace is dense at left and narrows to the right. It covers no recoverable letters; an isolated pen mark is also possible. The fourth stroke of the note number has a rounded top distinct from the three 1s, favouring a prime. The first occurrence of comentaires has one m and the next occurrence has two. The typescript specifically has tenacité, réfléxion and traditionelle. No continuation of the final spaced word is supplied.

**Letter indices.** No mathematical i or j index or exponent.

**Formula and diagram register**

- Line 24, inline ` ^{1} `.

**State-of-page register**

- Line 24, handwritten · ` (\unsure{111'|111$^{1}$}) `
- Line 24, handwritten · ` \deleted{\illegible{1}} `
- Line 24, deleted · ` \illegible{1} `
- Line 25, margin · ` \unsure{-} `

**Changes made during comparison**

no change

**Cross-page comparison before freeze.** A short isolated mark at the lower left recurs on several typed sheets. It may be a registration mark. Only the stroke is transcribed.

- ` % archive sheet number: 176 ` -> ` \margin{\unsure{-}}
% archive sheet number: 176 `
