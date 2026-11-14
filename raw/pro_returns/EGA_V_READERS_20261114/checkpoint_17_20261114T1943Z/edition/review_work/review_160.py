import sys
sys.path.insert(0,'edition/scripts')
from audit_late_helpers import complete
k='ega25_25_160'
r=[
(r'\inserted{$^{(k)}$}',r'\inserted[typed]{$^{(k)}$}','The raised (k) is typed above the line with a pen leader.'),
(r'\inserted{$H$}',r'\inserted[typed]{$H$}','H is a typed insertion with a pen placement line.'),
(r'\hand{\unsure{$\cap$}}',r'\hand{$\cap$}','The small hand-drawn arch between X and H is legible as the intersection sign.'),
(r'\inserted{non vide}',r'\inserted[typed]{non vide}','Non vide is typed between the lines with a pen placement curve.'),
(r'\check{\underline{E}}',r'\overset{\hand{\scriptscriptstyle\vee}}{\underline{E}}','The dual check over E is handwritten.'),
(r'\over{$=$}{\unsure{$\neq$}}',r'\over{\unsure{$=$}}{$\neq$}\hand{\unsure{(}}','The final not-equal sign is clear; the underlying equal sign is less secure. A separate curved pen mark between the sign and zero remains uncertain and is retained.'),
(r'pour tout \xout{x}',r'pour tout $\unsure{x|s}$','The point letter is a densely overtyped x/s-shaped glyph, not simply a cancelled variable with no surviving letter; its reading remains uncertain.'),
(r'\xout{\illegible{3}}',r'\xout{\unsure{et que au dessus}}','The cancelled line ending permits et que au dessus beneath the x strokes; the phrase is kept tentative without grammatical repair.'),
(r'\xout{\unsure{d\'un corps}}',r'\xout{d\'un corps}','The cancelled continuation d’un corps is legible.'),
(r'\unsure{N}+1',r'\unsure{N|n}+1','The exponent has a superposed upper/lower N/n shape; no r is supplied from the following variable list.'),
(r'\inserted{\unsure{$n$ invers.}}',r'\inserted{\unsure{si} $n>0$\unsure{?}}','The small insertion reads a tentative si followed by n>0 and a final uncertain question-like mark; it does not read invers.'),
(r'\unsure{Car mais on}',r'Car $n=0$: on','The lower handwritten note clearly begins Car n=0: on, with two small punctuation dots after zero.'),
(r'\margin{160}',r'\mspage{\hand{160}}','The lower160 is a handwritten folio.'),
(r'\dfrac{\partial\phi}{\partial X_i}',r'\hand{\dfrac{\partial\phi}{\partial\textcolor{black}{X_i}}}','The differential signs, phi and fraction bar are handwritten; X_i retains the typed layer.'),
(r'\phi',r'\hand{\phi}','The phi signs throughout the page are handwritten.'),
(r'\in ',r'\hand{\in} ','The membership signs in the displayed words are handwritten.'),
(r'\in$',r'\hand{\in}$','The membership sign after the doubtful point letter is handwritten.'),
(r'\in\mathrm',r'\hand{\in}\mathrm','The membership sign before Sym is handwritten.'),
(r'\subset',r'\hand{\subset}','The inclusion sign is handwritten.'),
(r'\geqslant 2',r'\hand{\geqslant} 2','The degree comparison sign is handwritten.'),
(r'\to',r'\hand{\to}','The change-of-base arrow is handwritten.'),
(r'V(\hand{\phi})_s\neq',r'V(\hand{\phi})_s\hand{\neq}','The not-equal sign comparing the fibre and P_s is handwritten.')]
r=[x for x in r if x[0] != r'\xout{\unsure{d\'un corps}}']
r.insert(8,(r"\xout{\unsure{d'un corps}}",r"\xout{d'un corps}",'The cancelled continuation d’un corps is legible.'))
d={5:'The upper3 is handwritten.',8:'The (k) and H insertions are typed with pen leaders; the membership and degree comparison signs are handwritten.',10:'The intersection arch is legible handwriting.',12:'Non vide is a typed insertion with a pen leader.',17:'The final m of Symm is x-cancelled; the dual check is handwritten. The pen alteration at n>0 remains uncertain in its exact >= reading.',21:'The final not-equal sign is clear, with an uncertain underlying equal sign and a separate curved pen mark before zero. Membership and phi are handwritten.',22:'The point letter is a dense x/s overprint; the cancelled line ending has the tentative undertext et que au dessus.',23:'The cancelled d’un corps is readable.',29:'The exponent has N/n overprinting; it is not normalized to the r of the following line.',30:'E forme is visibly cancelled by typewriter strokes.',32:'The insertion allows si n>0 with a doubtful final question mark. The differential signs and fraction bar are handwritten.',35:'The lower note reads Car n=0: on trouve les sections inversibles de underlined O_S !; its opening is now settled. The folio160 is handwritten.'}
n=['Both folios are handwritten and clear.','The arch between X and H is a handwritten intersection sign, now settled.','The final m is x-cancelled. The exact alteration of the inequality after n remains doubtful as recorded.','The final not-equal reading is clear, while the underlying equal sign remains tentative; a separate curved mark before zero is now retained.','The point letter is a dense x/s overprint. The cancellation is tentatively et que au dessus, followed by a legible cancelled d’un corps.','The raised character is an N/n overprint; the following r-indexed variables are left as written.','The insertion reads tentative si, clear n>0 and an uncertain final question-like mark, not n invers.','The handwritten note begins Car n=0: on; its complete continuation is legible.','Background traces were inspected but do not add a separately readable foreground sentence.','The empty separator note has no additional concern; all visible margins were inspected.','Every foreground baseline, formula, cancelled phrase, insertion, overwritten sign and marginal note was inspected in both scans; the small insertion and opening of the lower note were enlarged.']
e=[dict(line='13–14',before='je crois ... mais sans garantie',image='je crois ... mais sans garantie',decision='preserved',reason='The author explicitly qualifies the stated degree; the guide will report this reservation and will not supply or assert a new theorem.',category='authorial-status'),dict(line='29–31',before='E=A^(N+1); X_0,...,X_r',image='E=A^((N|n)+1); X_0,...,X_r',decision='preserved',reason='The rank exponent is overprinted N/n while the variables have a visible r. The edition does not make the letters agree.',category='notation-discrepancy')]
x=complete(k,r,d,n,e);print(k,len(x['decisions']))
