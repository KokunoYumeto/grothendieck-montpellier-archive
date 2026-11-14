import sys
sys.path.insert(0,'edition/scripts')
from audit_late_helpers import complete
R=[
(r'\mspage{11}',r'\mspage{\hand{11}}','The upper11 is handwritten in pencil.'),
(r'\mspage{184}',r'\mspage{\hand{184}}','The lower184 is handwritten in pencil.'),
('de k (vu',r'de k $\over{(}{\unsure{(|t}}$vu','The opening parenthesis has a dark pen retouch and a cross-stroke, giving a t-like outline. Its intended resulting glyph remains uncertain.'),
("n'est pas",r"n'est $\overset{\hand{\unsure{\wedge}}}{\mathrm{p}}$as",'The typed p remains readable, with a small pen loop/caret above its head. The uncertain mark is retained without changing the letter or assigning it a correction function.'),
('dans le cas',r'dans le ca\unsure{s|z|x}','The final cell of cas has overlapping s/z/x strokes and remains uncertain.'),
('localement',r'l\unsure{o|c}\unsure{c|o}alement','The o and c cells overlap with competing c/o forms; both altered cells are marked.'),
(r'\xout{surjectif}',r'\deleted{\xout{surjectif}}','Surjectif is legible beneath typed cancellation and a continuous additional pen stroke.'),
(r'\to',r'\hand{\to}','All three S-prime to S arrows are handwritten.'),
(r'a^{1/2}',r'a^{1\hand{/}2}','The slash between the typed raised1 and2 is pen, with a thick rounded upper end.'),
(r'\inserted{schéma en}',r'\inserted[typed]{schéma en}','Schéma en is typed interlinearly and attached after le by a pen curve.'),
(r'\inserted{$\simeq \underline{O}(n)_S/\underline{SO}(n)_S$} \hand{(}des racines carrées\hand{)}',r'\inserted[typed]{$\hand{\simeq}\underline{O}(n)_S\hand{/}\underline{SO}(n)_S$} des racines carrées'+'\n% NOTE: The apparent parentheses around des racines carrées belong to one continuous curved insertion leader for the formula above; no separate closing parenthesis occurs after carrées.\n','The O(n), SO(n), their subscripts and underlines are typed; the isomorphism sign and slash are pen. The long continuous insertion curve begins before des and ends above the start of carrées. It supplies no separate pair of literal parentheses around those words.'),
(r'\xout{,xxxxxxxx}',r'\xout{\deleted{\unsure{,}} tel que}','Tel que is readable beneath typed cancellation. The initial punctuation is obscured by an extra pen cross and remains tentatively a comma; the live following comma is separate.'),
(r'en\over{v}{vi}sagé',r'en\over{\unsure{vi|vr}}{\unsure{vi}}sagé','Two adjacent cells are retouched, with a high pen dot above the second. The older vi/vr and resulting vi are both qualified; the draft one-character v-to-vi account does not capture the visible two-cell overlap.'),
('supposer ',r'suppose$\overset{\hand{\unsure{/}}}{\mathrm{r}}$ ','The final typed r is legible and has an additional ascending oblique pen stroke above/right of it. The stroke is retained with uncertain function, without changing the word.')
]
D={
9:'The initial gén and the later surjectif are legible under cancellation. Surjectif also has a separate long pen strike. Both altered o/c cells of localement remain uncertain.',
11:'Schéma en is typed, with a pen leader after le. Mu is handwritten, while the lower2 and following baseline S are typed and retain their distinct positions. The added quotient formula is typed apart from its pen isomorphism sign and slash. Its long insertion curve is not transcribed as a pair of literal parentheses around des racines carrées. The cancelled tel que is recovered; its initial punctuation remains obscured by a pen cross. The short dash before le chan- is pen.',
14:'The two retouched cells in envisagé and the extra dot are retained as an uncertain old vi/vr and uncertain new vi; no single-cell expansion is asserted.'
}
N=[
'Both upper11 and lower184 are handwritten pencil folios. The complete lower scan is blank apart from the archive number and paper/scan marks.',
'The opening parenthesis is pen-retouched into a t-like outline and remains uncertain. A small loop/caret above typed p is retained separately. The final s/z/x cell of cas remains unresolved.',
'Gén is readable under typed x marks. Surjectif is legible under both typed and pen cancellation. The o/c pair in localement consists of overlapping type forms and is explicitly qualified.',
'Schéma en and the letters/indices of the quotient formula are typed; mu, the isomorphism sign, slash and insertion leaders are pen. The apparent parentheses form one continuous leader rather than a separate pair around des racines carrées. The cancelled tel que is recovered with uncertain initial punctuation and its extra pen cross; the following live comma and pen dash remain.',
'The two cells after en are retouched, and an added pen dot sits above the second. Both the older vi/vr and the resulting vi remain uncertain.',
'The typed final r of supposer has an added upward oblique pen stroke. Its shape and uncertain function are retained without changing the underlying r.',
'No long handwriting occurs. Both full scan parts, all blank margins, the entire lower half, and every short addition/formula mark were inspected.'
]
extra=[
dict(line=11,before=r'\mu_2 S',image=r'\mu_2 S',decision='retained',reason='The2 is lower beside mu, while S is a separate baseline character; it is not normalized into a two-part subscript.',category='literal-formula'),
dict(line=7,before='standart',image='standart',decision='retained',reason='The final letter is visibly t.',category='literal-spelling'),
dict(line=11,before='le ... groupes',image='le ... groupes',decision='retained',reason='The typed le and plural groupes remain as written around the typed schéma en insertion.',category='literal-wording')
]
print(len(complete('ega25_25_184',R,D,N,extra)['decisions']))
