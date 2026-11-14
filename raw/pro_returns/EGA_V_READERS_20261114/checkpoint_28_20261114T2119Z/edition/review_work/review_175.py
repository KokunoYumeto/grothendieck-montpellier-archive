import sys
sys.path.insert(0,'edition/scripts')
from audit_late_helpers import complete
R=[
(r'\subset',r'\hand{\subset}','The inclusion sign before the first dual E is pen.'),
(r'\neq',r'\hand{\neq}','Both not-equal signs are drawn in pen.'),
(r'Q\in',r'Q\hand{\in}','The membership sign in the otherwise typed interlinear Q-in-Sym expression is filled in by hand.'),
(r"x'\in",r"x'\hand{\in}",'The membership sign in x-prime belonging to V(Q) is handwritten.'),
(r'\xout{\unsure{tel que Q(x}}',r'\xout{tel que Q(x\unsure{)}}','The letters tel que Q(x are legible under type x strikes; a final closing parenthesis is possible beneath the last cancelled cell and remains uncertain.'),
(r"\xout{\unsure{x' soit un point lisse de}}",r"\xout{x' soit un point lisse de}",'The whole cancelled phrase is legible, including the initial prime.'),
(r'\xout{\illegible{1}}',r'\xout{relative}','The crossed word after dim is relative, with all eight letters recoverable.'),
(r'\longrightarrow',r'\hand{\longrightarrow}','The homomorphism arrow is pen and has the dual check only over its source E.'),
('associée à Q/',r'associée à Q\hand{/}.','A long oblique pen stroke follows Q, and the separate lower-right period remains visible. Both marks are preserved without assigning the slash a grammatical role.'),
(r'\xout{\unsure{traiter le cas}}',r'\xout{traiter le cas}','The complete cancelled phrase traiter le cas is readable through the typed x marks.'),
(r'\xout{\unsure{Alors}}',r'\xout{auquel}','The cancelled letters are a-u-q-u-e-l, including the descending q. The draft Alors is unsupported.'),
(r'\xout{\illegible{2}}',r'\xout{et ci dessous}','The small cancelled line below est dégénérée reads et ci dessous; no secure hyphen is supplied through the cancellation fill.'),
(r'n>0',r'n\hand{>}0','The greater-than sign is handwritten.'),
(r'\xout{\unsure{$(X_1X_2+X$}}',r'\xout{\unsure{$(X_1^{2}X_2+X$}}','A raised2 is visibly present above the cancelled formula as well as lower1/2-like digits. Its attachment and the obscured sequence remain uncertain, so the whole candidate formula stays qualified.'),
(r'\xout{\unsure{M}}Q(X_{\xout{\unsure{2}}1}',r'\unsure{Q|M}(X_{\unsure{1|n}}','The initial Q/M and first lower digit/letter each occupy a single overprinted type cell. They are not separate cancelled characters followed by new characters.'),
(r'\sum_i',r'\hand{\sum_i}','Both the first summation sign and its small lower i are drawn in pen.'),
(r'\hand{\sum_{i<j}}',r'\hand{\sum}_{i\hand{<}j}','The second sum and comparison sign are pen; the lower i and j retain typewriter stems and serifs.'),
(r'\unsure{indétermihées|indéterminées}',r'indétermihées','The tall stem and shoulder in the disputed cell are a clean typed h; the literal spelling is retained.')
]
D={5:'Upper-right2 and its following dot are handwriting.',7:'Both partial signs are pen, while Q and X_i are typed. The full fraction and closing parenthesis were checked.',8:'Both dual checks are pen; the inclusion sign is also pen, and the quotient denominator N is unchanged.',14:'16.3 is typed interlinearly, with a pen leader. Q and Sym^2(E) are also typed, with only the membership sign hand filled. The second leader places that expression before the existing x.',15:'The dual check is pen. Cancelled tel que Q(x is readable, with only its possible final closing parenthesis uncertain.',16:'The entire cancelled x-prime/point-lisse phrase is readable beneath the x marks.',17:'The cancelled word after dim reads relative; the live rank E-1 and Q-not-equal0 remain literal.',18:'The dual check and arrow are handwritten; the target E has no dual check.',20:'Cancelled traiter le cas is fully legible.',23:'The cancelled word is auquel, followed by the live cas. Dans ce is a typed interlinear insertion with a pen curve.',24:'The dual check over E is pen. The small cancelled extra line is read separately as et ci dessous.',26:'The omitted two-word block is recovered as the three groups et ci dessous under type x cancellation.',33:'The cancelled formula retains its visible raised2 and lower digits with uncertainty over their attachment and remaining sequence.',35:'Q/M and1/n occupy single overprinted cells. The first sum and lower i are pen; the second sum and less-than sign are pen with typed i,j.',36:'Indétermihées visibly contains h and is retained literally.',39:'The lower archive175 is handwriting.'}
N=[
'Both complete halves, their overlap and all margins were read. Pale reverse traces do not supply additional forward-reading body text on this face.',
'Upper2. and lower175 are clearly handwritten folios.',
'Both partial signs and the fraction bar are pen; Q, X and the lower i are typed.',
'Every dual check is pen and is attached to its own E; in the arrow expression only the source E has a check.',
'16.3, the Q/Sym expression and Dans ce are typed interlinear additions with pen leaders. The membership sign inside the Q/Sym expression is handwritten.',
'Tel que Q(x is secure with its last possible parenthesis uncertain; the longer point-lisse phrase, relative, traiter le cas, auquel and et ci dessous are recovered. The cancelled formula in b retains uncertain attachment of its extra visible raised2.',
'A pen slash follows Q and a separate period survives beside its lower end; both are represented.',
'The initial Q/M and lower1/n are same-cell type overprints. Both sums are pen, but the second lower i,j are typed and only their comparison is pen.',
'The disputed letter is visibly a clean h in indétermihées, retained without spelling correction.',
'No further long marginal handwriting is present; all short insertions and pen marks were inspected.'
]
extra=[dict(line=15,before='Q(x,x)',image='Q(x,x)',decision='retained',reason='The scan prints both x arguments and their comma; this is not rewritten as Q(x).',category='literal-formula'),dict(line=17,before='rang E - 1',image='rang E - 1',decision='retained',reason='The digit is1 in the scan; no mathematical dimension adjustment is made.',category='literal-formula'),dict(line=27,before='standart',image='standart',decision='retained',reason='The final letter is t in both occurrences of this word.',category='literal-spelling')]
print(len(complete('ega25_25_175',R,D,N,extra)['decisions']))
