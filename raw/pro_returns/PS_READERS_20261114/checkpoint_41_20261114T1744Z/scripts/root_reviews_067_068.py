from review_root import review
from pathlib import Path
k='ps_134-2_067'
def label(text):
 return r'\hand{\tikz[baseline=(x.base)]{\node (x) {'+text+r'};\draw (.5,.3)--(.5,.65);\draw (.5,.3) .. controls (-1,.6) and (-1,-.65) .. (.5,-.3)--(.5,-.65);\draw (1.65,.45)--(.95,.45) .. controls (.7,.45) and (.7,-.2) .. (.95,-.2)--(1.65,-.2);}}'
esp=r'\hand{\tikz[baseline=(x.base)]{\node[draw,ellipse,inner sep=2pt] (x) {espacer};}}'
review(k,changes=[
(r'\mspage{\unsure{52}}',r'\mspage{-\hand{5}2-}','The live folio52 is clear, with a pen-retraced5 and typed2 between typed hyphens. No separate earlier digit can be securely recovered.'),
(r'\margin{\unsure{(App. 14)|(Apr. 14)}}',r'\margin{'+label(r'\unsure{(App.14)|(Apr.14)}')+'}','Retain the doubtful label and reconstruct its surrounding placement brackets; all are pen.'),
(r'\margin{$\mu_{p^n}$}',r'\margin{\hand{$\mu_{p^n}$}}','The complete coefficient reminder in the left margin is handwritten.'),
(r'\over{\ast}{n}',r'\over{\unsure{\ast}}{n}','The old exponent is blackened rather than securely a visible star; the new pen n is clear.'),
(r"one\hand{\unsure{'}}s",r"one\hand{'}s",'The mark is a distinct curved pen apostrophe, clearly visible in enlargement.'),
(r'\margin{espacer}',r'\margin{'+esp+'}','The handwritten espacer is circled; restore the enclosure.'),
(r'\margin{\unsure{(App. 15)|(Apr. 15)}}',r'\margin{'+label(r'\unsure{(App.15)|(Apr.15)}')+'}','Retain the doubtful label and its surrounding placement brackets at the new section.'),
(r'\margin{67}',r'\margin{\hand{67}}','The lower-left67 is pencil archive foliation.')
],doubts={'unsure':[
(r'-\hand{5}2-','doubt resolved','The live folio52 and its hyphens are clear; no earlier digit is supplied from the retouching alone.'),
(r'\unsure{(App.14)|(Apr.14)}','doubt retained','The two narrow internal pen strokes do not securely distinguish the competing abbreviations; chronology or neighboring labels are not used to remove the doubt.'),
(r"\hand{'}",'doubt resolved','The curved apostrophe above ones is a distinct ink stroke, not a background speck.'),
(r'\unsure{(App.15)|(Apr.15)}','doubt retained','The second abbreviation has similarly compressed internal strokes and remains doubtful.')
],'illegible':[]},notes=[
'The live number52 is clear and flanked by typed hyphens. Its5 is retraced in pen, without an independently recoverable earlier digit.',
'Both labels remain doubtful App./Apr.; their pen placement brackets are now represented.',
'The new n and the marginal mu_{p^n} are clear handwriting; the blackened old exponent is now marked doubtful instead of asserted as a star.',
'The apostrophe in ones is a distinct curved pen mark and is resolved.',
'The superscript i in the final crystalline-cohomology expression is handwritten. The cancellation begins with the final s of parts and continues through of points, leaving singular part.',
'The circled espacer and the lower-left pencil archive67 are both retained with explicit handwriting provenance.'
],summary='Both halves and enlarged section labels, apostrophe and coefficient correction inspected. Resolved the live folio52 and the apostrophe, retained both doubtful appendix abbreviations, and added a doubt to the covered old coefficient exponent. Restored all placement brackets, circled spacing instruction and pen margin coefficient. Preserved the two commas around the cancelled p-adic phrase, the period after groups, the literal(B) reference, H1 in the degree-one sentence, and the slope bound<=1.',differences={
1082:('Weil cohomology','the typescript reads as our transcription','The source spells cohomology in full; the witness omits o.'),
1085:(r'\inserted{and k of char. p}','the typescript reads as our transcription','The pen abbreviation char. is not expanded.'),
1086:(r"one\hand{'}s",'our transcription corrected','The apostrophe is clearly present in the scan; the witness omits it.'),
1094:(r"``of slope $\leq 1$''",'the typescript reads as our transcription','The closing quotation mark is visible after1 and absent from the witness.'),
1095:(r'a correct $H^1$','the typescript reads as our transcription','The exponent is the numeral1, not i; the surrounding sentence also explicitly discusses i=1.'),
1099:('Katz','the typescript reads as our transcription','The final typed letter is z.'),
1101:('doubtful handwritten App./Apr.14 label and placement brackets','our transcription corrected','The label remains uncertain but its pen provenance and graphical brackets are restored; the witness substitutes a heading.'),
1102:('doubtful handwritten App./Apr.15 label and placement brackets','our transcription corrected','The label and its graphics remain at the start of Your question7 rather than becoming an editorial heading.')
})
k='ps_134-2_068'
ring=r'\hand{\tikz{\draw (0,0) circle (.04);\draw (.14,-.35)--(.25,.35);}}'
review(k,changes=[
(r'\over{at}{At}',r'\over{a}{A}t','Only the initial a is overwritten by a pen capital A; the t remains typed.'),
(r'\arrow[dl, leftrightarrow]',r'\arrow[dl, leftrightarrow, color=blue]','The left diagonal correspondence arrow is handwritten.'),
(r'\arrow[dr, leftrightarrow]',r'\arrow[dr, leftrightarrow, color=blue]','The right diagonal correspondence arrow is handwritten.'),
(r'\arrow[rr, leftrightarrow]',r'\arrow[rr, leftrightarrow, color=blue]','The horizontal correspondence arrow is handwritten.'),
(r'\margin{/}',r'\margin{'+ring+'}','The faint pencil mark contains a small ring beside the long slant; preserve the graphic without deciding that the ring is a letter or numeral.'),
(r'\margin{68}',r'\margin{\hand{68}}','The lower-left68 is pencil archive foliation.')
],doubts={'unsure':[
(r'\unsure{,}','doubt retained','The heavy punctuation after X has overlapping upper and lower lobes. A new comma over semicolon remains plausible, but the live shape is not unequivocal.'),
(r'\unsure{F}','doubt retained','The pen E covers the old letter; its remaining strokes do not settle the old F independently.')
],'illegible':[]},notes=[
'The initial5 of53 is handwritten; no independently readable earlier digit is forced from the dark stroke.',
'The heavy punctuation after X remains a doubtful comma over the typed semicolon; the image does not securely remove the uncertainty.',
'The live E is clear; the earlier F-like letter remains doubtful beneath it.',
'The cancellation covers the final d of interpreted. The preceding e is a complete uncancelled typed loop and remains live, giving literal interprete in the corrected form.',
'All three double-headed diagram arrows are pen strokes and are now explicitly colored as handwriting; the objects remain typed.',
'The lower-left68 is pencil archive foliation.'
],summary='Both halves and enlarged punctuation, interpreted ending and pale margin mark inspected. Kept the two original doubts. Corrected the provenance of At so that only A is pen, marked all three diagram arrows as handwriting, and restored the small ring accompanying the marginal slash. The visible partial cancellation leaves interprete, and all lowercase/uppercase Cat distinctions and parentheses are retained.',differences={
1108:('determine each other:','the typescript reads as our transcription','The typed colon precedes the diagram and is omitted by the witness.'),
1109:('semi-simplicial complex','the typescript reads as our transcription','The diagram’s word contains the second i omitted by the witness.'),
1110:('(up to n-equivalence).','the typescript reads as our transcription','A full stop follows the bottom-right diagram label.'),
1112:(r'$G_n\to(n-\mathrm{Cat})$','the typescript reads as our transcription','The target is parenthesized and has capital C.'),
1118:(r'$\mathit{Hom}_n(E_n,(n-\mathrm{cat}))$','the typescript reads as our transcription','The target in this later expression is parenthesized lowercase cat, unlike the earlier Cat and the witness normalized notation.'),
1119:(r'$E_n\to(n\text{-}\mathrm{cat})$','the typescript reads as our transcription','The final line also has lowercase cat in parentheses.'),
1120:('pencil ring and slanting stroke','our transcription corrected','A faint small ring stands beside the slash-like mark; both are retained graphically without assigning the ring a letter value.')
})
p=Path(__file__).resolve().parents[1]/'guide_sections/134_2_appendix.tex';s=p.read_text()
if '\\subsection*{Appendix 14:' not in s:
 s+=r'''
\subsection*{Appendix 14: The scope of flat cohomology (part F)}
Cote 134-2, site 67 (folio 52), revisits the hope that finite and continuous coefficients in fppf cohomology might recover a p-adic Weil cohomology. Serre's degree-one constructions and the generalized-Jacobian complex of part C motivate the hope, although the literal backward reference is to(B). Crystalline cohomology, whose properties Grothendieck attributes here to Berthelot, now provides his comparison standard. He argues that the part obtainable from algebraic-group coefficients stays within Frobenius slopes at most one, explaining the success for degree one and the difficulty already in degree two, then explicitly labels recovery of the entire slope-at-most-one part a conjecture and admits that he has lost contact with the current work. This is a retrospective assessment of a proposed programme, not a proof of a precise comparison theorem. For mathematical interpretation, Frobenius slopes belong to the rationalized crystalline object over a suitable perfect base; torsion in the integral Witt-vector modules is not described by a slope decomposition. The source preserves its stated hypotheses and its closed bound at one, without importing a modern comparison statement. The witness changes the decisive degree-one expression from the visible $H^1$ to $H^i$, drops the closing quotation after the slope bound, expands the pen abbreviation ``char.'', and misspells Katz. The original handwritten superscript i, correction of ``parts of points'' to ``part of slope'', and Frobenius arrow are retained, while the blackened old exponent in the coefficient $\mu_{p^n}$ remains doubtful. This closes the duality and cohomology sequence of parts A--F; Appendix 15 returns to the information retained by a homotopy type and its locally constant higher stacks.
'''
 p.write_text(s)
