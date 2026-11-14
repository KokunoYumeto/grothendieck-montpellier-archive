import sys
sys.path.insert(0,'edition/scripts')
from audit_late_helpers import complete
R=[
(r'\xout{xxxxx}',r'\xout{comme}','Five underlying letters read comme beneath the typed x cancellation.'),
(r'\emptyset',r'\hand{\unsure{\phi|\emptyset}}','Each visible symbol is a slashed loop with freehand stroke shape. Its identification as phi or empty set is left uncertain at every occurrence; no distinction is inferred from function or empty-set context.'),
(r'\longrightarrow',r'\hand{\longrightarrow}','The long arrows in the functor and immersion/ramification expressions are visibly drawn in pen.'),
(r'\neq',r'\hand{\neq}','Both horizontal strokes and oblique stroke of the inequality sign are handwritten.'),
(r'\to',r'\hand{\to}','The short arrows following T, the tensor product, and X are drawn in pen.'),
(r'\xout{xxx\unsure{F(T)}xxxxxxxxxxxx}',r'\xout{\illegible{1} F(T) \unsure{=} ensemble}','F(T) and ensemble are legible beneath the type cancellation; the preceding group cannot be securely read, and the apparent equals sign remains tentative.'),
(r'corresponde\xout{xxx}',r'corresponde\xout{\unsure{nt}}','Two crossed type cells follow corresponde; n and t are plausible underlying forms but remain uncertain.'),
('une fomme',r'une fo\unsure{r|m}me','The third cell has overlapping r/m shapes rather than a secure clean m.'),
(r'\xout{xx}',r'\xout{d\unsure{i|f}}','The first crossed character is d; the second has an obscured upper stroke, allowing i or f.'),
(r'\xout{xxxxxx}',r'\xout{comme}','The cancelled word after the V expression has the visible letters comme; trailing cancellation fill is not literal text.'),
(r'\unsure{points}',r'p\unsure{o|p}in\unsure{t|s}','The word occupies five type cells: the second oval has a low/descending stroke and the last cell overlaps t and s. The ordinary spelling is not supplied as a certain reading.'),
(r'x \in V^o',r'x \hand{\in} V^o','The membership sign before V^o is written in pen.'),
(r'\unsure{singulier|siggulier}',r'si\unsure{n|g}gulier','The overlap is confined to the third cell; the remaining letters gulier are readable.'),
(r'\otimes',r'\hand{\otimes}','The circle-and-cross tensor sign is handwritten between the separately underlined E and O.'),
(r'\xout{xxxdxxxxxxxxaxixx}',r'\xout{\illegible{2} est claire}','The right portion est claire is readable under x strikes. The preceding cells remain illegible; the repeated live est claire is preserved.'),
(r'\inserted{$V^o$}',r'\inserted[typed]{$V^o$}\hand{,}','The interlinear V^o has typewriter letter forms; the dark comma beside it and curved insertion leader are pen. The leader inserts the addition before the existing V^1.'),
('sont lisses',r's\unsure{o|e}nt lisses','The vowel in sont/sent is overprinted; the remaining s, n, t are visible.'),
(r'\xout{xixxxxixxxdødixxxxxixx}',r'\xout{fixer la \unsure{d|c}odimension}','The crossed phrase reads fixer la followed by an overlapping initial d/c and odimension; the tall stroke favors a literal d, so codimension is not silently restored.'),
(r'caractérisation de $V^2$',r'caractérisation de $V^{\over{\unsure{2|1}}{2}}$','The superscript is retraced in pen as 2; the underlying typed digit is obscured and may be 2 or 1.')
]
D={
5:'Upper-right pencil folio 5 is clear.',
7:'The typed cancellation covers comme; recovered letters replace the x placeholders.',
9:'All slashed-loop symbols retain a phi/empty-set alternative with their pen layer. The cancelled F(T) and ensemble are secure, initial group and equals remain uncertain; the functor arrow is pen.',
12:'Two cancelled cells after corresponde allow nt; the form word has r/m overprint. Neither is normalized from context.',
15:'The short cancelled group is d plus i/f; the later cancelled word is comme.',
16:'Five occupied cells show p, uncertain o/p, i, n, and overprinted t/s; uncertainty is localized.',
19:'The third cell of singulier/siggulier remains n/g. The separate c) is handwritten above the type baseline before de.',
27:'Typed x cancellation leaves est claire readable at the right, preceding group unresolved.',
30:'Interlinear V^o is typed, with a pen comma and curved leader before V^1; the double quotation marks around bonne are handwritten. Slashed-loop glyph remains phi/empty-set uncertain.',
31:'Cancelled fixer la is legible; the initial letter of the following odimension is d/c uncertain. The final live V superscript is pen 2 over an uncertain typed 2/1.',
36:'Y- and its caret are handwritten before morphisme. The X-to-Z arrow is pen; no additional word is supplied.',
37:'Lower-left archive folio 170 is clear in pencil.'
}
N=[
'The symbols are visually the same slashed-loop shape, now marked with pen layer and phi/empty-set uncertainty at all four occurrences. Their roles do not decide their transcription.',
'Cancelled F(T) and ensemble are legible; preceding group and the apparent equals sign retain uncertainty.',
'Two cancelled cells after corresponde tentatively read nt; the r/m overprint in forme/fomme is localized rather than normalized.',
'The parenthetical word has five cells with o/p and t/s alternatives; singulier has only a third-cell n/g overlap.',
'c) is a clear pen addition above the baseline.',
'The interval between underlined E and J is blank in the scan: no arrow is supplied.',
'V^o is an interlinear typed addition, followed by a pen comma and supported by a pen insertion curve.',
'Both pairs of quotation strokes around bonne are pen.',
'First long cancellation retains only the secure tail est claire; the second reads fixer la plus d/c-odimension.',
'Y- is handwritten with a caret immediately before morphisme.',
'Both handwritten folios 5 and 170 are secure.',
'Both complete halves and all margins were read; there is no additional long marginal prose.'
]
extra=[dict(line=20,before='dédigne',image='dédigne',decision='retained',reason='The fourth letter is visibly d; the literal typed spelling is retained.',category='literal-spelling'),dict(line=21,before='poihts',image='poihts',decision='retained',reason='The fourth type letter has the tall stem and shoulder of h; this also occurs on line 24.',category='literal-spelling'),dict(line=24,before='poihts',image='poihts',decision='retained',reason='The second occurrence likewise visibly has h, not a supplied n.',category='literal-spelling'),dict(line=28,before=r'u:$\underline{E}$ \quad $\underline{J}$',image='E then blank then J',decision='retained',reason='The space between E and J contains no drawn or typed connector.',category='formula-layout')]
print(len(complete('ega25_25_170',R,D,N,extra)['decisions']))
