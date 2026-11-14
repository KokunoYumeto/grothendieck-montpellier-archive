from review_root import review
k='ps_134-2_053'
circle=r'\tikz[baseline=(x.base)]{\node[draw,circle,inner sep=1pt] (x) {$\mathcal C\mathcal F$};}'
review(k,changes=[
(r'\mspage{38} \mspage{6}',r'\mspage{\hand{38}} \hfill 6','The centered 38 is handwritten; 6 is independently typed at the top right.'),
(r'\xrightarrow{\hand{$\mathcal{F}$}} \text{(n-Cat.',r'\hand{\xrightarrow{\mathcal{F}}} \text{(n-Cat.','The first functor arrow is handwritten along with its F label.'),
(r'\xrightarrow{\hand{$\mathcal{F}$}} \text{(n-cat.',r'\hand{\xrightarrow{\mathcal{F}}} \text{(n-cat.','The second functor arrow is likewise entirely handwritten.'),
(r'e_n^{\hand{$\mathcal{C}_{n+1}$}}',r'e_n^{\hand{$(\mathcal{C}_{n+1})$}}','The exponent in the first cohomology formula has visible parentheses around C_{n+1}; these were omitted.'),
("fallait''",r"fallait\hand{''}",'The closing quotation consists of two pen strokes.'),
('fait sans structure',r'fait san\hand{s} structure','The final s is rewritten in pen.'),
("Il s'impose, pour",r"Il s'impose, \over[typed]{\unsure{b}}{p}our",'The p cell has a second typed impression with an ascender, possibly b; preserve the live p and mark the older reading doubtful.'),
(r'\margin{$\mathcal{C}\mathcal{F}$ (circled)}',r'\margin{\hand{'+circle+r'}}','The margin contains the handwritten CF enclosed in a circle; the word circled is an editorial description and is replaced by the graphic.'),
(r'\mspage{53}',r'\margin{\hand{53}}','The lower-left 53 is pencil archive foliation.')
],doubts={'unsure':[],'illegible':[]},notes=[
'The top folio 38 is pen, the independent top-right 6 is typed, and the bottom-left 53 is pencil archive foliation.',
'The classifying operator has the author’s looped script-C form. It is retained without substituting a modern B notation or silently identifying it with the differently formed fundamental groupoid symbol.',
'The live CF in the formula is reinforced and crowded but legible; the circled marginal repetition clarifies it. No distinct earlier word can be recovered under the reinforcement.',
'The final s of sans is penned. The p of pour has overlapping typed impressions; the possible older b is newly marked doubtful rather than mislabelled as pen.',
'There are four typed dots after strict, all retained.'
],summary='Both halves and enlarged retouched-letter and quotation details inspected. Marked the pen arrows, final s and closing quote, restored the parenthesized exponent and circled marginal CF, and preserved the typed overprint in pour with its uncertain old letter. The four dots, script classifying operator, and the clear n-i index remain literal; the witness n-1 is unsupported.',differences={
847:('(n-Cat. de Picard strictes).','the typescript reads as our transcription','The target has visible surrounding parentheses and a terminal period; the witness removes the parentheses.'),
848:(r'\pi_{n-i}','the typescript reads as our transcription','The subscript is n minus i, with a dotted i, not n minus one.'),
851:('strictes) with no brace','the typescript reads as our transcription','The source closes the target with a parenthesis and contains no additional brace.'),
852:('nécéssairement','the typescript reads as our transcription','The enlarged word has both acute accents, including the extra acute after c; the source spelling is retained.'),
853:(r'\margin{\hand{circled CF}}','our transcription corrected','The handwritten circled repetition is present; the description is now encoded as an actual graphic.')
})
k='ps_134-2_054'
u1=r'\underbrace{\underline{Hom}\, ( e_n^{\hand{\mathcal{D}_{n+1}}}, \ \hand{\mathcal{F}} )}_{\hand{\parallel\ \text{déf}} \atop \hand{\Gamma_{\mathcal{D}_{n+1}}(\mathcal{F})}}'
u2=r'\underbrace{\underline{Hom}\ (e_n^{\hand{\mathcal{C}_{n+1}}} \ , \ f^*_{n+1} \hand{\mathcal{F}} \ )}_{\hand{\parallel\ \text{déf}} \atop \hand{\Gamma_{\mathcal{C}_{n+1}}(\mathcal{F})}}'
spacer=r'\tikz[baseline=(x.base)]{\node[draw,circle,inner sep=1pt] (x) {espacer};\draw[<->] (.6, .5)--(.6,-.5);}'
down=r'\tikz[baseline=-.4ex,x=.5em,y=.5em]{\draw[->] (1,2)--(0,2)--(0,0);}'
loop=r'\tikz[baseline=-.4ex,x=.5em,y=.5em]{\draw (1,1) .. controls (0,1) and (-.1,.8) .. (0,.3) .. controls (.2,0) and (.8,.2) .. (1,0);}'
review(k,changes=[
(u1,r'\hand{'+u1.replace(r'\underbrace{',r'\underbrace{{\normalcolor ',1).replace(r'}_{\hand{\parallel',r'}}_{\hand{\parallel',1)+'}','The left underbrace is drawn in pen; mark its rule without changing the mixed provenance of its contents.'),
(u2,r'\hand{'+u2.replace(r'\underbrace{',r'\underbrace{{\normalcolor ',1).replace(r'}_{\hand{\parallel',r'}}_{\hand{\parallel',1)+'}','The right underbrace is drawn in pen, like the definition signs beneath it.'),
(r'\hfill \mspage{7}',r'\hfill 7','The typed 7 is an independent top-right foliation.'),
(r'f$_n$est',r'f$_n$ est','The scan has a word space between the mathematical symbol and est.'),
(r'$\hand{\varphi \longrightarrow \varphi}\circ f_n$',r'$\hand{\varphi \longrightarrow \varphi\circ} f_n$','The small composition circle is penned with the two phi symbols and arrow.'),
(r'\margin{\unsure{espacer} (circled, with a vertical double arrow)}',r'\margin{\hand{'+spacer+r' \rule{1.5cm}{0.4pt}}}','Espacer is legible inside the oval, crossed by an up/down spacing arrow with an associated horizontal separator. Replace editorial descriptions by the drawn marks.'),
(r'\margin{\unsure{(App.8)|(Arr.8)}} \hand{(} La',r'\margin{\hand{\unsure{(App.8)|(Arr.8)} '+down+r'}} \hand{'+loop+r'} La','The handwritten marginal label remains doubtful in its middle letters. Restore its downward bent arrow and the opening placement curve, which is not an ordinary parenthesis in the text.'),
(r'\unsure{\over{;}{:}|:}',r'\over{\unsure{;}}{:}','The live colon is clear and handwritten; only the alleged older semicolon remains uncertain beneath the dark points.'),
(r"l'algèbre semi-simpliciale.",r"l'\hand{a}lgèbre semi-simpliciale.",'The a is retouched in pen in this occurrence.'),
(r'\mspage{\hand{54}}',r'\margin{\hand{54}}','The lower-left number is pencil archive foliation.')
],doubts={'unsure':[
('espacer','doubt resolved','The letters of the circled spacing instruction are readable.'),
(r'\unsure{(App.8)|(Arr.8)}','doubt retained','The two abbreviated middle letters have open, r-like pen shapes; their exact reading remains uncertain.'),
(r'\over{\unsure{;}}{:}','doubt narrowed','Two pen dots establish the live colon, but the underlying punctuation is not independently visible.')
],'illegible':[]},notes=[
'The circled word is espacer; the opposed vertical arrows and horizontal stroke are restored graphically.',
'The marginal label is handwritten and conventionally suggests App.8, but the r-like middle strokes remain explicitly doubtful.',
'The live colon is penned. The possible earlier semicolon remains uncertain under the ink.',
'The underlines and appended comma-like marks after items a and b are drawn in pen; their literal punctuation is retained.',
'The composition circle is handwritten, as are the adjacent phi symbols and arrow.',
'The lower-left 54 is a pencil archive foliation.'
],summary='Both halves and enlarged marginal instruction, section label, colon and composition-circle details inspected. Resolved espacer and reconstructed its visible geometry, retained the doubtful App.8/Arr.8 label, narrowed the colon doubt, and marked the composition circle and retouched a as handwritten. The source right-hand terminal object has C_{n+1}, not the witness D_{n+1}; both Gamma abbreviations have F as argument. The source’s question about avoiding semi-simplicial algebra remains intact.',differences={
863:(r'\mathcal F:\mathcal D_{n+1}\longrightarrow(n-Cat),','the typescript reads as our transcription','The category has parentheses and the display ends with a comma, as the scan shows.'),
864:(r'e_n^{\mathcal C_{n+1}}','the typescript reads as our transcription','The right-hand exponent is the C symbol of the source groupoid, not D.'),
865:(r'\Gamma_{\mathcal D_{n+1}}(\mathcal F)','the typescript reads as our transcription','F is visibly the argument following Gamma with its D subscript, not part of the subscript.'),
866:(r'\Gamma_{\mathcal C_{n+1}}(\mathcal F)','the typescript reads as our transcription','F is the argument of the second Gamma, not included in the C subscript.'),
867:(r'\parallel\ \text{déf}','the typescript reads as our transcription','Both handwritten definition marks are present below the underbraces and absent from the witness.'),
868:(r'circled handwritten espacer with spacing arrows','our transcription corrected','The word is resolved and its graphics are represented without editorial descriptive prose.'),
869:(r'\margin{\hand{\unsure{(App.8)|(Arr.8)}}}','our transcription corrected','The handwritten abbreviated label remains doubtful; the witness descriptive heading is not on the page.'),
871:('Je ne sais si une théorie des champs et opérations sur iceux pourra s’écrire sans jamais utiliser de l’algèbre semi-simpliciale.','the typescript reads as our transcription','The complete sentence is visibly typed, including underlined sans, and is omitted by the witness.'),
872:(r'\hand{,} after item a','the typescript reads as our transcription','The handwritten punctuation is a comma, not the witness semicolon.'),
873:(r'\hand{,} after item b','the typescript reads as our transcription','The handwritten punctuation is a comma, not a semicolon.'),
874:(r'\over{C}{\v C}echiste','the typescript reads as our transcription','A clear handwritten caron is added above the typed C.')
})
