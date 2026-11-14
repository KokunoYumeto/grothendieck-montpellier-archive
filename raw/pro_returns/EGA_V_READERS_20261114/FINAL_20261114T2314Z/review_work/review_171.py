import sys
sys.path.insert(0,'edition/scripts')
from audit_late_helpers import complete
R=[
(r'\mspage{6}',r'\mspage{\hand{6}}','Upper-right folio 6 is handwritten in pencil.'),
(r'\over{s}{c}',r'\over{\unsure{s|c}}{c}','The c is strongly retraced in pen; the obscured underlying type cell does not securely decide s against c.'),
(r'\xout{\unsure{xxx}}',r'\xout{\deleted{\hand{(\unsure{\nmid|\dagger})}}}','The cancelled left-hand group contains a pen formula label with crossed oblique shaft, between parentheses; typed x marks and further pen cancellation overlap it.'),
(r'\over{D}{\unsure{d}}',r'\over{D}{\unsure{d|D}}','The pen loop encloses/retraces the typed D, with a long lower return; lowercase d versus a retraced capital remains uncertain.'),
(r'\inserted{\unsure{,}}',r'\inserted{ici}','Two dotted i strokes and central c are visible above the insertion curve. This is the word ici, not merely a comma.'),
(r'\rightarrow',r'\hand{\rightarrow}','The arrows in the surjections and in the M display are pen additions.'),
(r'\longrightarrow',r'\hand{\longrightarrow}','The displayed E^o-to-N arrow is drawn in pen.'),
(r'(\unsure{$\nmid$|$\dagger$})',r'\hand{(\unsure{\nmid|\dagger})}','Both occurrences show a pen oblique shaft crossed by a short stroke, with pen parentheses; the label identity remains uncertain.'),
(r'\underline{N}_{\xout{\illegible{1}}}',r'\underline{N}_{\deleted{\illegible{1}^{\unsure{o}}}}','The subscript is blotted/cancelled in pen. A small upper oval may be o, but the base letter is not securely recoverable.'),
(r'sur\over{g}{j}ectif',r'sur\unsure{j|g}\unsure{e|g}ctif','The two type cells after sur overlap j/g and e/g respectively; there is no separable freehand replacement justifying a g-to-j pen correction.'),
(r'\inserted{\unsure{$V^{2}$}}\unsure{p}',r'\inserted{\unsure{$V^{2}$}}p','The pen V and upper 2-like strokes overlap the p, but the typed p itself is readable. The obscured insertion retains its uncertainty.'),
(r'\xout{\unsure{disc}}',r'\xout{\deleted{\unsure{disc}}}','The cancelled word plausibly reads disc; both x overtyping and a broad pen strike obscure its final cell.'),
(r'D \in \Gamma',r'D \hand{\in} \hand{\Gamma}','Membership and Gamma are filled in with pen strokes in the discriminant display.'),
(r'\hand{$\otimes$}',r'\hand{\otimes}','Both tensor glyphs are handwritten. Removing nested math delimiters preserves their glyph and layer.'),
(r'\xout{w}semble-t-il',r'\unsure{s|w}emble-t-il','The s/w shapes occupy the same first type cell; there is no separate cancelled w before the live word.'),
(r'grassma\unsure{nniennes}',r'grassma\unsure{n|m}\unsure{i|n}\unsure{e|i}nnes','The scan has three overlapping cells after grassma before the clear nnes; the draft expands an extra n. The visible alternatives are localized without restoring the ordinary spelling.'),
(r'\margin{171}',r'\margin{\hand{171}}','Lower-left archive folio 171 is pencil handwriting.')
]
D={7:'Pen n replaces an obscured typed cell with a dot above, plausibly i; the under-letter remains uncertain.',8:'The c in ces is pen retraced over an uncertain s/c cell.',10:'The cancelled group contains the same crossed-oblique formula label as below; both type x and pen cancellation are present.',14:'The capital D has an uncertain d/D pen overstroke. The interlinear insertion before à priori reads ici, including both dotted i strokes.',17:'The label is hand drawn, including parentheses; its symbol is kept nmid/dagger uncertain. N has a pen-cancelled unreadable subscript with a possible upper o.',18:'Two consecutive type cells in surjectif show overlaps, without a separable pen g-to-j substitution.',19:'The V^2-like insertion remains uncertain because its upper strokes are blotted; the underlying p of peuvent is readable.',20:'The repeated label has the same pen crossed shaft and parentheses as the display.',22:'The cancelled disc reading remains tentative; a pen strike joins the type x cancellation.',23:'Both tensor glyphs are pen. D, the line-bundle exponent -n+m-1, determinant, and final tensor exponent 2 were individually checked; membership and Gamma are also pen.',32:'The apparent w and s overlap in one cell, so a separate deleted prefix is removed.',33:'Three type-overprint cells after grassma precede clear nnes; their alternatives are retained without spelling restoration.',37:'The archive folio 171 is handwritten.'}
N=[
'The n is pen; its under-letter retains the possible i reading because a dot survives above.',
'The D correction remains d/D uncertain. The mark above à priori reads ici, inserted with a pen curve.',
'Both labels show a pen oblique stroke with short crossbar; nmid/dagger alternatives are retained with the handwritten parentheses.',
'The N subscript remains unreadable under pen cancellation, with only a tentative upper o.',
'The V^2-like pen insertion overlaps the p; the insertion remains uncertain and p is now secure.',
'disc remains a tentative underlying word beneath both type and pen cancellation.',
'Both tensor signs, the membership sign and Gamma in the same formula are pen; all exponents are retained literally.',
'The initial s/w is a same-cell type overprint. The grassma suffix occupies three damaged cells before nnes; no extra ordinary-spelling letter is supplied.',
'Upper 6 and lower 171 are clear handwritten folios.',
'Both halves, including all margins, were inspected; the pale reverse-side traces do not form additional forward-reading writing on this face.',
'All body lines were read; there is no further long marginal prose.'
]
extra=[dict(line=7,before='sur M',image='sur M',decision='retained',reason='The capital is visibly M, and it is retained despite later references to Y.',category='literal-notation'),dict(line=11,before=r'u\,(\underline{N}_{Z^{o}/Z})',image='u followed by parentheses, no star',decision='retained',reason='No inverse-image star is visible after u.',category='formula-layout'),dict(line=12,before='rang n',image='rang n',decision='retained',reason='The displayed source has n here and m in later prose; neither is harmonized.',category='literal-notation'),dict(line=15,before='rant m',image='rant m',decision='retained',reason='The final type cell reads t in rant.',category='literal-spelling')]
print(len(complete('ega25_25_171',R,D,N,extra)['decisions']))
