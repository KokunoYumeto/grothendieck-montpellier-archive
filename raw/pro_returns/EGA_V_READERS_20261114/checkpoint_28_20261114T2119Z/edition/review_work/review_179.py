import sys
sys.path.insert(0,'edition/scripts')
from audit_late_helpers import complete
R=[
(r'=\xout{W}',r'=W','The first W has its ordinary typed strokes and adjacent opening parenthesis; no separate cancellation x is visible over it.'),
(r'\rightsquigarrow',r'\hand{\rightsquigarrow}','All three wavy mapping arrows on this page are handwritten.'),
(r'\longrightarrow',r'\hand{\longrightarrow}','The long arrows in the two upper displays are pen.'),
(r'\rightarrow',r'\hand{\rightarrow}','Both further rightward arrows are hand drawn.'),
(r'\underline{Isom}(\underline{Q}(\underline{E}_o),',r'\underline{\unsure{I|O}som}(\underline{Q}(\underline{E}_o),','The first character of the target Isom in the upper display is overprinted with an enclosing loop; I/O remains uncertain in that single cell.'),
(r'la section $q_o$',r'la section $\unsure{q|Q}_o$','The first q in the body has a larger upper loop from an overlapping Q-like type impression; the other q occurrences are not changed.'),
(r'\xout{\unsure{sur E}}',r'\xout{sur E}','All letters of sur E are legible under the typed x strikes.'),
(r'\xout{z}comme',r'\unsure{c|x}omme','The beginning of comme is one c/x overprinted cell, not a separate cancelled z followed by another c.'),
(r'\xout{type}\inserted{prés}',r'\xout{type}\inserted[typed]{prés}','The replacement prés is typed above the cancelled type; its typewriter serifs and spacing are clear.'),
(r'Introduisons',r'Introduiso\unsure{n|j}s','The penultimate cell contains an n and a descending dotted j overprint; the draft silently selected n.'),
(r'\xout{$\underline{Q}$x}',r'\xout{$\underline{Q}$(x}','The cancelled group includes an opening parenthesis after the underlined Q, followed by cancellation x fill; no further letter is recovered.'),
(r'_{\tilde{d}}',r'_{\overset{\hand{\sim}}{d}}','The tilde above the lower d in the localization subscript is hand drawn.'),
(r'\unsure{corrigé|modrigé}',r'\unsure{m|c}o\unsure{d|r}rigé','The overprinting affects the first and third cells. The visible competing forms are m/c and d/r; the other letters are secure.'),
(r"s'ensui\deleted{t}\inserted{vra}",r"s'ensui\deleted{t}\inserted[typed]{vra}",'The old final t is pen-struck. Vra is typewritten above it with a pen leader, not handwritten text.'),
(r'\inserted{\unsure{le}}',r'\inserted{le}','The small handwritten le is legible above the insertion leader between par and changement.'),
(r'\hand{\unsure{$\hat{}$}}',r'\tikz[baseline=-0.5ex,x=1em,y=1em]{\draw[handwritten,->] (0,0) .. controls (.6,0) and (.6,.5) .. (.6,.9);}','The mark after Q(E)-star is a curved upward pen arrow: its shaft starts beside/below the star and curls rightward to a small upward arrowhead. No textual target is inferred.'),
('sectio[n]','sectio\n% NOTE: The word is clipped after sectio at the right edge; no final n is visible.','The bracketed n was a completion beyond the supplied right edge. Only sectio is visible.'),
('trivialement des définitions,',r'\margin{\unsure{\illegible{?}}}'+'\n% NOTE: Faint bluish oblique marginal traces; no secure word or word count, and their status as front writing or show-through is unresolved.\ntrivialement des définitions,','The pale left marginal writing has been inspected natively and with color-channel contrast. No word is secure, and its orientation/material role cannot be established. The uncertain unreadable block is retained instead of omitted as presumed reverse show-through.')
]
D={
5:'The upper6 is handwritten and clear.',
7:'The typed W is present without a secure cancellation mark; its following parenthesis overlaps its edge.',
14:'Sur E is fully readable under typed x cancellation.',
17:'The first c of comme shares a cell with x-like overprinting. Type is x-cancelled and prés is typed interlinearly above it.',
18:'The n/j overprint in Introduisons remains explicit. The cancelled underlined Q is followed by a visible opening parenthesis and cancellation fill.',
21:'The extra x between n and t in représentant is cancelled, and the whole word formes is legible beneath typed x marks. The S-prime mapping arrow is pen.',
24:'The word has overprinted m/c and d/r cells, not one securely readable normalized adjective.',
30:'The cancelled Lemme is legible under typed x cancellation. Proposition and its underline remain live.',
33:'The terminal t of s-ensuit is pen-struck; vra above it is typed. The inserted si is pen. The rightmost word ends visibly at sectio; the missing final character is not supplied.',
34:'The mark immediately after Q(E)-star is a curved upward arrow with a distinct head and no securely identified target. The handwritten le is legible above its insertion leader.',
36:'The lower179 is handwritten.'
}
N=[
'Upper6 and lower179 are both clear handwriting.',
'The faint bluish left-margin traces were inspected in the native crop and a color-channel contrast view. No secure word or count is readable, and show-through is not established; an uncertain illegible marginal block with unknown count is retained.',
'Sur E is fully readable beneath the type x cancellation.',
'The cancelled group contains an underlined Q and an opening parenthesis before the final x fill.',
'The n/j overprint is now represented explicitly inside Introduisons.',
'The first and third cells remain m/c and d/r uncertain; the shared o-r-i-g-é sequence is preserved.',
'The mark has a curved shaft and an upward arrowhead. Its form is represented geometrically, without inventing its destination or function.',
'Only sectio is visible before the right edge. The draft bracketed n is removed and the clipping is recorded.',
'The pen insertion le is readable; its leader enters between par and changement.',
'The old t is struck in pen and the replacement vra is typed interlinearly, with its pen leader retained in the layer account.',
'There is no securely readable long marginal passage; the faint possible marginal writing is retained as unresolved rather than dismissed. Every short handwritten formula sign and insertion was checked.'
]
extra=[dict(line=19,before=r'\underline{Q}(\underline{E})_{\tilde d}',image=r'\underline{Q}(\underline{E})_{\overset{\hand{\sim}}{d}}',decision='reviewed',reason='The lower d and the star are typed; only the tilde is pen. The localization notation is not changed.',category='handwriting-layer')]
print(len(complete('ega25_25_179',R,D,N,extra)['decisions']))
