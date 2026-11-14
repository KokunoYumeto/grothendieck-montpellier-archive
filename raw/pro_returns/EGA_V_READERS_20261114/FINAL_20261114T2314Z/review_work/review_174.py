import sys
sys.path.insert(0,'edition/scripts')
from audit_late_helpers import complete
R=[
(r'\margin{nouveau EGA V}',r'\margin{\hand{nouveau EGA V}}','The upper note nouveau EGA V is clear cursive handwriting.'),
(r'\mspage{1}',r'\mspage{\hand{1}}','Upper-right authorial folio1 is handwritten.'),
(r'\unsure{une}',r'u\unsure{n|6}e','The central type cell has overlapping n-like and looped6-like strokes; only that cell is doubtful.'),
(r'\xout{\unsure{définit}}',r'\xout{définit}','The complete underlying word définit is readable through its typed x cancellation.'),
(r'\xout{\illegible{3} \unsure{section}}',r'\xout{\unsure{ou} encore comme une section}','Encore comme une section is legible beneath the x overstrikes. The first two-cell group favors ou but remains tentative.'),
(r'\hand{$\vee$}',r'\hand{\vee}','All four dual checks are pen marks above their respective first E symbols; nested math delimiters are removed without changing the layer.'),
(r'\longrightarrow',r'\hand{\longrightarrow}','The E-to-E and determinant arrows are drawn in pen.'),
(r'\in ',r'\hand{\in} ','Membership signs in the discriminant display and proposition are pen.'),
(r'\Gamma',r'\hand{\Gamma}','Both Gamma signs have pen strokes, including the inline Gamma before O_S.'),
(r'\otimes',r'\hand{\otimes}','The tensor exponent in the discriminant display and the rank-expression tensor sign are pen.'),
(r'\hand{$n$}',r'\unsure{n|m}','The exponent over O_S is a blackened n/m overprint; the image does not securely separate a handwriting layer from the type impression.'),
(r'\neq',r'\hand{\neq}','The two not-equal signs are handwritten.'),
("car est 2. D'ailleurs",r"car est 2. D\hand{\raisebox{.7ex}{\unsure{+|t}}}'ailleurs",'A small raised cross/t-like pen mark survives above the apostrophe after D; its function is unresolved and the mark is not omitted.'),
(r'\inserted{\unsure{alg clos}}',r'\inserted{alg clos}','The interlinear handwriting reads alg clos, with a descending g and clear clos, attached by a curved insertion leader.'),
(r'\unsure{ils}',r'i\unsure{l|b}s','Only the central type cell overlaps l and b; the initial i and final s are clear.'),
(r'\hand{$\partial$}',r'\hand{\partial}','All six partial-derivative signs are handwritten; the fraction bars are also pen and represented by the displayed fractions.'),
(r'\hand{$\sum$}',r'\hand{\sum}','The summation sign is handwritten.'),
(r'si car $k = 2$',r'si car $k = \unsure{2}$','The final2 has a blackened lower overstroke;2 remains the visible candidate, with its local damage marked.'),
(r'\margin{174}',r'\margin{\hand{174}}','Lower-left archive folio174 is handwritten.')
]
D={5:'The large brown upper-left strokes allow IV or1/U but their exact form and material origin remain uncertain. Nouveau EGA V and upper1 are clear handwriting.',9:'The n/6-like central overprint of une is localized; the first and last letters are clear.',10:'Définit is legible beneath type x cancellation.',11:'The dual check is pen. The cancelled phrase reads tentative ou then secure encore comme une section; no blank illegible words are needed for the latter.',12:'Both dual checks sit over the first E in their respective expressions, and the arrow is pen.',13:'The check belongs over the first determinant E; the arrow is pen and the second E has no check.',16:'The raised exponent is a blackened n/m-like cell; its underprint and possible pen retouch cannot be separated securely.',22:'The opening parenthesis immediately before D’ailleurs is pen.',23:'The matching closing parenthesis after E is pen.',30:'Alg clos is a clear handwritten insertion with a curved leader. Both partial signs are pen; the final s letters of zéros and communs are type-cancelled.',31:'The central cell of ils/ibs is overprinted l/b; other letters are clear.',33:'The sum and both partial signs are pen; X_i and Q are typed.',34:'The numerator after the handwritten partial shows Q and E shapes in one overprinted cell; the Q/E alternative remains. The denominator partial is pen.',35:'The full clause si E est de rang pair is readable under typed cancellation; the preceding2 has a black lower overstroke.',37:'Archive folio174 is pencil handwriting.'}
N=[
'The large brown strokes remain IV/1-U uncertain and their material role unresolved. The adjacent nouveau EGA V and upper1 are handwriting.',
'The lower folio174 is clear handwriting.',
'Une has a central looped/n-like overprint, recorded locally as n/6 rather than confirming the whole word.',
'All four checks are pen, and each belongs to the E directly underneath. Both arrows are also pen.',
'The underline beneath discriminant de la forme quadratique is a single pen stroke; the words themselves are typed.',
'The raised cross/t-like mark above the apostrophe of the later D’ailleurs is now represented, with its glyph/function left uncertain.',
'Alg clos is clearly legible in pen and retains its abbreviated spelling without a supplied period.',
'The l/b alternatives occupy one central type cell between clear i and s.',
'The last derivative numerator has an E-like vertical/bars and Q-like tail; both alternatives are retained.',
'Every partial sign and the summation sign is pen; the formula indices and numerator letters were checked individually.',
'Both halves, their overlap and all margins were read; no further long handwritten passage is present.'
]
extra=[dict(line=14,before='d(Q) in determinant(E) tensor2',image='d(Q) with the printed exponent tensor2',decision='retained',reason='Every symbol and parenthesis was compared; E in this display has no visible underline unlike earlier E terms.',category='formula-layout'),dict(line=17,before='qui exprime Q',image='qui exprime Q',decision='retained',reason='The letter is visibly Q, not changed to B from the preceding bilinear-form discussion.',category='literal-notation'),dict(line=28,before='untranscribed mark above apostrophe',image='raised cross/t-like mark',decision='corrected',reason='The mark is visible as a small cross with descending stem and is preserved without assigning it a note function.',category='handwriting')]
print(len(complete('ega25_25_174',R,D,N,extra)['decisions']))
