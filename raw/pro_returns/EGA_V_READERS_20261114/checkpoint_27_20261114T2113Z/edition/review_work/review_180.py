import sys
sys.path.insert(0,'edition/scripts')
from audit_late_helpers import complete
R=[
(r'\mspage{7}',r'\mspage{\hand{7}}','The upper-right7 is written in pencil, not typed.'),
(r'\margin{180}',r'\mspage{\hand{180}}','The lower-left180 is a handwritten archive folio.'),
(r'\Longrightarrow',r'\hand{\Longrightarrow}','The implication arrow in the opening continuation is pen.'),
(r'\longrightarrow',r'\hand{\longrightarrow}','The arrow from Gl(E) to Q(E)-star is hand drawn.'),
(r'\rightsquigarrow',r'\hand{\rightsquigarrow}','The mapping arrow from u to u(q_o) is pen.'),
(r'On peut \xout{\illegible{1}} supposer',r'On peut \xout{alors} supposer','Alors is fully legible beneath the typed x cancellation.'),
(r'\unsure{générique|génériaque}',r'génér\unsure{a|i}\unsure{q|i}ue','Two adjacent cells after génér are overprinted: a/i and q/i. The other letters are clear, and no extra cell is supplied.'),
('le morphisme précédent soit plat',r'le morphisme préc\unsure{é|s}dent soit plat','The cell after préc has an e-shaped body with an overlapping upper curved stroke; é/s remains uncertain.'),
(r"\margin{\unsure{dégager un lemme sur les morphismes d'espaces homogènes}}",r"\margin{dégager un lemme sur les \unsure{morphismes} d'espaces \unsure{h}omogènes}",'The oblique marginal note is readable after rotation except the compressed morphismes and edge-clipped initial h of homogènes, which remain qualified.'),
(r'\xout{$u\in Gl(E)(k)$}',r'\xout{$u\unsure{\in}Gl(\underline{E})(k)$}','The cancelled formula clearly has u and Gl with underlined E and (k). The relation between u and Gl is concealed by x fill, so the proposed membership sign remains uncertain.'),
(r'$u\in Gl(\underline{E})(k)$',r'$u\hand{\in}Gl(\underline{E})(k)$','The membership sign in the live repeated formula is pen.'),
(r'il suffit\hand{,}\inserted{pour établir la platitude} de prouver\hand{),} \xout{\illegible{1}}',r'il suffit\hand{$\unsure{\leftarrow}$}\inserted[typed]{pour établir la platitude} de prouver\hand{,} \xout{que les u(}\hand{$\downarrow$}'+'\n% NOTE: The typed insertion has a long pen leader pointing left to the blotted mark after suffit and a downward branch after the cancelled words; the curved ends are part of this leader.','Pour établir la platitude is typed. The heavy mark after suffit lies at the left end of its long insertion leader, with an uncertain arrowhead. A separate downward arrow branches near the right end. The mark after prouver is one pen comma, not a parenthesis plus comma. The cancelled text is legibly que les u(, with no further argument restored.'),
(r'formes quadratiques \xout{\illegible{1}} sur \hand{$\checkmark$}E',r'formes quadratiques \xout{sur E} sur $\overset{\hand{\checkmark}}{E}$','The cancelled phrase is sur E. The pen check-shaped mark lies above the live E, rather than as a separate symbol before it; no meaning is assigned to the mark.'),
(r'non nul, \xout{\illegible{1}} i.e.',r'non nul, \xout{\unsure{et}} i.e.','The small cancelled two-cell group permits et, but the cancellation obscures its final strokes and the reading remains uncertain.'),
(r'\deleted{(}$***)$',r'\unsure{\deleted{(}}$***)$','A short horizontal stroke crosses the opening parenthesis. Its exact layer and cancellation intent are uncertain, so the draft definite deletion is qualified.'),
(r'\hand{\unsure{|}}qui',r'\over{\unsure{q}}{q}ui','The long ink stroke belongs to a handwritten q over the first letter of qui; it is not a separate vertical bar. The old underlying q remains tentative.'),
('prouvera alors 16.11.',r'prouvera \unsure{a|e}\unsure{l|n}ors 16.11.','The first two type cells of alors contain overlapping a/e and l/n forms; neither is a separate pen correction.'),
(r'\overset{\hand{$\sim$}}{d}',r'\overset{\hand{\sim}}{d}','The tilde over d is handwritten and belongs inside the existing math context.'),
(r'\neq',r'\hand{\neq}','Both not-equal signs are handwritten.'),
(r'\xout{\unsure{dim}}',r'\xout{dim}','The cancelled abbreviation dim is readable through the typed cancellation.'),
(r'\xout{\unsure{donc}}',r'\xout{donc}','All four letters of donc are recoverable beneath the x marks.'),
('(i.e. se met sous forme standart',"% NOTE: Small irregular ink specks occur above the end of alors and the following Q on the preceding line; no coherent accent or character can be established.\n(i.e. se met sous forme standart",'The small marks noted above Q also extend over the preceding letters and gap. They are irregular specks without a secure character or accent reading; no mathematical accent is inferred.')
]
D={
11:'The cancelled word after On peut reads alors.',
12:'The right-hand capital is an E/B type overprint and remains uncertain; the first E has lower o.',
16:'The two altered cells of the adjective remain a/i and q/i; the final comma is a separate pen curve.',
18:'The left marginal note is retained with localized doubts in morphismes and the edge-clipped h. The altered cell in précédent is also explicitly uncertain.',
19:'The cancelled formula has an underlined E; its obscured relation stays uncertain. The live membership sign is handwritten.',
20:'The insertion words are typed. The blot after suffit is the left end of a long leader, with a possible left arrowhead; its separate downward branch is retained. The pen comma after prouver is a single mark. Que les u( is readable under cancellation.',
21:'The comma after the parenthesized three-star reference is a long pen curve, distinct from the typed punctuation nearby.',
23:'The cancelled sur E is recovered. The check-shaped pen sign is above the live E. The small cancelled group after non nul stays tentatively et.',
24:'The opening parenthesis has a short cross-stroke with uncertain layer/function. The stroke at qui is a pen q written over its first type cell, not a separate bar. The a/e and l/n overprints in alors remain uncertain.',
28:'The tilde and not-equal sign are pen. The small specks span the end of alors, the gap, and Q without a coherent accent form; their presence is recorded without inventing an accent.',
33:'Dim is legible under typed cancellation.',
34:'Donc is legible under typed cancellation.',
37:'The lower-left180 is a handwritten archive folio, encoded as such.'
}
N=[
'Both upper7 and lower180 are handwritten folios and are now marked accordingly.',
'The crossed word is legibly alors.',
'The second capital has overlapping E/B strokes; the uncertainty is retained without a contextual choice.',
'The altered cells are a/i and q/i, not an extra inserted syllable. The comma at the line end is handwritten.',
'The words pour établir la platitude are typed. Their long pen leader points left to the blot after suffit and has a downward branch near its right end; the single comma after prouver and the separate comma after the three-star reference are both pen. The geometric marks are not converted into a reordered sentence.',
'The check-shaped mark is placed above E. The long stroke at qui belongs to a pen q over the first cell. The short stroke across the opening parenthesis remains uncertain in layer and cancellation status.',
'The tilde is pen. The scattered specks above the end of alors and Q are recorded in a comment, without treating them as an unobserved mathematical accent.',
'The oblique note reads dégager un lemme sur les morphismes d-espaces homogènes, with localized uncertainty in the compressed morphismes and the clipped initial h of homogènes.',
'Both dim and donc are recoverable beneath the typed cancellation.',
'The full marginal note, all short pen additions, every formula sign, and the top/bottom margins were inspected.'
]
print(len(complete('ega25_25_180',R,D,N)['decisions']))
