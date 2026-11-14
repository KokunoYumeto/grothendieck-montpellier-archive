import sys
sys.path.insert(0,'edition/scripts')
from audit_late_helpers import complete
R=[
('terminologie reçue  -',r'terminologie re\unsure{ç|q}u\textsubscript{\unsure{,}}e  -','In the first occurrence, the third cell has overlapping ç/q forms and a second low comma-shaped mark is visible beneath/right of u. Its role is unresolved and it is retained rather than normalized away.'),
(r'\unsure{neus|nous}',r'\unsure{n|j}\unsure{o|e}us','The first cell contains n/j overprinting with a descending loop and an upper dot; the second contains o/e overprinting.'),
(r'\xout{xxxxZ}',r'\deleted{\xout{sur Z}}','Sur Z is legible under typed x marks and an additional long oblique pen strike.'),
(r'\unsure{$\Gamma$|T}',r'$\over{T}{\unsure{\Gamma}}$','The old typed T is clear. A long pen top stroke with a downward right tip augments it; the resulting gamma-like reading remains qualified.'),
(r'$Gl(\underline{E})$ \xout{xxx}',r'$Gl(\underline{E})$ \xout{\unsure{qui}}','The cancelled three-cell word after Gl(E) permits qui, with q and u more legible than the final cell; the word remains uncertain.'),
(r"\inserted{$Q,Q'$}",r"\inserted[typed]{$\unsure{Q|u},\unsure{Q|u}'$}",'The interlinear letters, comma and prime are typed. Both letters have a Q-like closed loop and tail with u-like upper serif traces; both readings remain visible rather than being chosen from the later formula.'),
(r'\unsure{sss|ssi}',r'sss','All three characters are s; the final one has no i dot or vertical i stem.'),
(r'\xout{ilsxsontxcongruxxxie}',r'\xout{ils sont congr\unsure{us} \unsure{le|la}}','Ils sont congr is recoverable. The following us and final le/la group are obscured by cancellation and remain qualified; no intervening comma is supplied.'),
(r'v \in',r'v \hand{\in}','The membership sign before O(n)(S-prime) is pen.'),
(r'\inserted{voir en attendant SGAD \uline{IV}}',r'\inserted{\unsure{(}voir en attendant SGAD \uline{IV}\unsure{)}}','The handwriting and underlined IV are clear. Curved ends and a lower joining stroke enclose the note; their reading as literal parentheses remains qualified, and the insertion leader attaches after VI.'),
('les opérations naturelles',r'\over{\unsure{l|i}}{l}es opérations naturelles','The first letter of les is retraced in pen with an oblique upper stroke and lower extension; the old l/i type form remains uncertain.'),
(r'\xout{Gl(E$_0$)xxxxGl}',r'\deleted{\xout{$Gl(\underline{E}_{\hand{\unsure{o|0}}})=Gl$}}','The cancelled formula contains underlined E, a lower pen loop o/0, and a visible equals sign before the second Gl. It carries both typed x cancellation and an oblique pen strike.'),
(r"s'ensuit \xout{xxx}",r"s'ensuit \deleted{\xout{que}}",'The cancelled word reads que, with both the typed x fill and an oblique pen stroke visible.'),
(r'\xout{xxxxxiqxxxxx}',r'\xout{canoniquement}','The complete cancelled word canoniquement is readable beneath the typed x marks.'),
(r'\margin{\hand{182}}',r'\mspage{\hand{182}}','The bottom-left182 is archive numbering, not a prose marginal comment.')
]
D={
5:'The upper9 is handwritten and clear.',
10:'The first two cells are n/j and o/e overprints, now localized rather than choosing a complete normalized word.',
15:'The new6 is thick pen over an older type digit; the old5 candidate remains uncertain.',
16:'The cancelled sur Z is fully legible and has both typed x cancellation and an additional oblique pen line.',
18:'The membership sign after Q is handwritten. The underline beneath gonal absolu is also pen while the letters remain typed.',
19:'A typed T remains under a pen top extension; gamma is the qualified reading of the augmented form.',
20:'The cancelled word after Gl(E) remains tentatively qui. The typed words schéma en groupes have a separate pen underline.',
22:'À n variables is typed above the line and attached by a pen curve; the comma after standart is handwritten.',
23:'The interlinear pair is typed, with Q/u overprinting in each letter. The comma and prime are typed. No substitution by the u,u-prime required by nearby prose is made.',
24:'Sss is visibly three s characters. The cancelled phrase has secure ils sont congr and uncertain us and final le/la.',
25:'Deuxième is fully legible beneath x cancellation; the live membership sign in v belonging to O(n)(S-prime) is pen.',
27:'Voir en attendant SGAD IV is legible pen text, with IV underlined. Its curved enclosure is retained as uncertain parentheses and its leader attaches after VI. The initial l of the following les is pen-retouched over a doubtful l/i cell.',
30:'The crossed formula retains its underlined E, separate lower handwritten o/0 loop, equals sign and final Gl. Both typed and pen cancellation are visible.',
32:'The cancelled word is que and is readable through both cancellation layers.',
34:'Canoniquement is readable through the type x fill.',
37:'The lower182 is handwriting and is treated as archive numbering.'
}
N=[
'Upper9 and lower182 are handwritten folios; the latter is encoded as a page number.',
'The first cell is n/j overprint and the second o/e overprint; neither is silently selected.',
'The new6 is handwriting, while the old digit remains tentatively5.',
'The typed T is clear and has an added pen top/right stroke. Its interpretation as an augmented gamma stays qualified.',
'À n variables is typed with a pen leader and a handwritten comma. The interlinear pair is also typed, but each letter contains Q/u overlapping forms, retained with uncertainty.',
'The abbreviation is clearly sss, with no i in the last cell.',
'The note voir en attendant SGAD IV is fully read and IV is underlined. The curved enclosure ends may function as parentheses and remain qualified; the insertion leader is placed after VI.',
'The underlines beneath groupe ortho-/gonal absolu, schéma en groupes/orthogonal relatif à la forme Q, fibré principal homogène sur, and de groupe are separate pen strokes beneath typed text; no word is reclassified wholly as handwritten.',
'Both full halves and all margins were inspected. The pale background traces do not supply an independently secure additional forward-reading passage on this face.',
'All short handwritten material, enclosure and insertion marks, underlines, folios and every formula index were read; no further long marginal passage is present.'
]
extra=[
dict(line=17,before=r'\uline{groupe ortho-}',image='Typed words with a separate pen underline',decision='reviewed',reason='The line beneath groupe ortho- is a continuous slightly curved pen stroke; the type letters remain black.',category='handwriting-layer'),
dict(line=21,before=r'\uline{orthogonal relatif à la forme Q}',image='Typed phrase with a long separate pen underline',decision='reviewed',reason='The underline changes slope below orthogonal and continues below the rest of the phrase; no cancellation crosses the letters.',category='handwriting-layer'),
dict(line=29,before=r'\uline{fibré principal homogène sur}',image='Typed phrase with a separate pen underline',decision='reviewed',reason='A slightly sagging continuous line runs beneath the whole phrase.',category='handwriting-layer'),
dict(line=29,before=r'\uline{de groupe}',image='Typed words with a separate pen underline',decision='reviewed',reason='The underline ends after groupe and before the displayed O(n) expression.',category='handwriting-layer'),
dict(line=35,before=r'change\_%',image=r'change\_%',decision='retained',reason='The last mark is visibly low like an underscore; it is not normalized to a word hyphen.',category='line-boundary')
]
print(len(complete('ega25_25_182',R,D,N,extra)['decisions']))
