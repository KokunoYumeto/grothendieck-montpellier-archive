import sys
sys.path.insert(0,'edition/scripts')
from audit_late_helpers import complete
R=[
(r'formels,\xout{\illegible{2}}',r'formels,\xout{montrent alors}','Montrent alors is legible beneath the typed x cancellation.'),
(r'\xout{\illegible{1} k(s) \illegible{1} de \illegible{1}}',r'\xout{sss k(s) est de car}','The cancelled line reads sss k(s) est de car; all surviving letters are recoverable through the x row.'),
(r'produi\xout{\unsure{se}}',r'produi\over{\illegible{?}}{se}','The final se is live joined pen writing over an obscured older type group. The lower-case looped e is clear; the old characters and their count cannot be recovered. This is not typed cancellation of se.'),
(r'Utili\xout{\illegible{1}}',r'Utili\xout{\unsure{sa}}','The short cancelled terminal group permits sa, but its second letter is heavily obscured; the group remains tentative.'),
(r"que \xout{\illegible{1}} l'on",r"que \xout{dans (} l'on",'The cancelled text is dans followed by an opening parenthesis; all those shapes are visible.'),
(r'\xout{\unsure{ex}}',r'\deleted{\xout{\unsure{ex}}}','The tentative ex group has both type cancellation and an additional pen stroke; its reading stays uncertain.'),
(r'\xout{\illegible{3}} Comme',r'\deleted{\xout{Il existe un morphisme}} Comme','The cancelled phrase Il existe un morphisme is legible and has both typed x marks and a long pen strike.'),
(r'que \xout{\illegible{1}} si Q',r'que \xout{tout} si Q','Tout is fully readable under the typed x cancellation.'),
('et un morphisme',r'et un m\unsure{o|r}\unsure{r|o}phisme','The second and third cells of morphisme each show o/r overprinting, while the remaining letters are clear.'),
('soit la forme standart.',r'soit la forme sta\unsure{n|d}dart.','The n/d cell before the following clear d is overprinted; it is not silently chosen as n.'),
('Si par exem',r'Si par exe\unsure{m}','Only part of the last m-like cell remains at the clipped right edge; it is retained as uncertain, with no hyphen supplied.'),
(r'\inserted{16.14.} \hand{(}\over{L}{C}',r'\inserted{16.14.} \over{L}{C}','The large curve before Ces is the left end of the insertion leader for16.14, not a separately written opening parenthesis. The C over L remains a genuine pen correction.'),
(r'\inserted{signalés dans 16.13.} \hand{(}à',r'\inserted{signalés dans 16.13.} (à','The wide left curve belongs to the insertion leader; a separate narrower typed opening parenthesis stands immediately before à.'),
(r'lisse)\hand{)}',r'lisse)\hand{,}','After the first closing parenthesis, the separate pen mark lies low and is a comma, not a second full-height parenthesis.'),
(r'\inserted{imparfait}',r'\inserted[typed]{imparfait}','Imparfait is typed above the line and attached by a pen brace-like leader.'),
('hypothèse supplémentaire',r'hypothèse supp\unsure{l|é}ementaire','The l-position contains overlapping l/é strokes and an accent, while the following e is unaccented in its own cell. The overprint and accent placement are retained.'),
(r'\hand{$a \in$}',r'a\hand{\in}','The a has the typed serif form seen in the neighbouring formula; the membership sign alone is clearly pen.'),
('ne peu',r'n\unsure{e|d} pe\unsure{u}','The e of ne is overprinted with a d-like ascender, and the last u is clipped at the edge. Neither is silently completed or normalized.'),
(r'\margin{183}',r'\mspage{\hand{183}}','The bottom-left183 is handwritten archive numbering.')
]
D={
5:'The upper10 is handwriting followed by a separate darker dot; the dot is retained without assigning an unproved pen/type layer.',
7:'The cancelled phrase reads montrent alors.',
8:'EGA is pen with a curved insertion leader. The following1/I type cell is overworked and remains uncertain; no numeral is selected from the chapter sequence.',
9:'The wavy arrow from the pair (E,Q) to P is pen. The word équivalence is typed with a separate underline.',
15:'The membership sign between s and S is handwritten.',
16:'The cancelled sss k(s) est de car is recoverable. The live exactemnt remains exactly as printed.',
18:'The terminal se is live pen replacement, not a deleted type group. Its older substrate remains illegible with unknown character count. The later membership sign is pen.',
20:'The short cancelled terminal group after Utili remains tentatively sa; no missing hyphen is added before the next-line sant.',
21:'The cancellation after que reads dans followed by an opening parenthesis.',
22:'The short ex-like group remains uncertain and has both typed and pen cancellation.',
24:'Il existe un morphisme is legible through both cancellation layers. The live S-prime to S arrow is pen.',
29:'The cancelled word before si Q is tout.',
31:'The S-prime to U arrow is pen. The n/d overprint in standart and the partly clipped m of exem are explicitly retained.',
33:'The S-prime to S arrow is pen; fini is typed with its underline.',
35:'16.14 and signalés dans16.13 are handwritten additions with long curved leaders. The first apparent parenthesis before Ces is part of the16.14 leader; C is penned over L. The separate parenthesis before à is typed, beside the leader for signalés.',
36:'The second low mark after lisse) is a handwritten comma, not a second closing parenthesis. The altered l/é cell in supplémentaire is retained.',
37:'Imparfait is a typed interlinear insertion with a pen leader.',
38:'The a is typed while membership is pen. The e/d overprint in ne and the clipped final u of peu remain qualified.',
41:'The lower183 is handwritten archive numbering.'
}
N=[
'Upper10 is handwriting followed by a separate dark dot; lower183 is handwritten archive numbering.',
'EGA is hand inserted, and the overworked1/I cell after V remains unresolved.',
'The wavy arrow, all three rightward arrows and each membership sign are pen. The a before the final membership sign is typed, not confidently handwritten.',
'The cancelled phrases montrent alors, sss k(s) est de car, dans (, Il existe un morphisme and tout are recovered. Sa and ex remain tentative. The ex and Il-existe groups have additional pen cancellation. The final se of produise is instead live pen replacement over unreadable old type.',
'The16.14 and signalés additions are pen, with curved leaders. The first apparent opening parenthesis is the16.14 leader; the parenthesis before à is separately typed. C is penned over L. The extra low mark after lisse) is a comma. Imparfait is typed interlinearly.',
'Every margin, short insertion, cancellation and formula was inspected; no further long handwritten passage is present.'
]
extra=[
dict(line=7,before='purements',image='purements',decision='retained',reason='The final s of purements is present in the scan; the spelling is not regularized.',category='literal-spelling'),
dict(line=16,before='exactemnt',image='exactemnt',decision='retained',reason='The scan omits the e before m; the written spelling is retained.',category='literal-spelling'),
dict(line=11,before=r'\uline{fibrés principaux}',image='Typed words with pen underline',decision='reviewed',reason='The underline is a separate long stroke below the baseline; the letters remain typed.',category='handwriting-layer'),
dict(line=12,before=r'\uline{homogènes} ... \uline{de groupe}',image='Typed words with separate underlines',decision='reviewed',reason='Both underlines are visible, with gaps separating them from the following formula.',category='handwriting-layer')
]
print(len(complete('ega25_25_183',R,D,N,extra)['decisions']))
