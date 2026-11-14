import sys
sys.path.insert(0,'edition/scripts')
from audit_late_helpers import complete
k='ega25_25_146'
r=[
(r'\mspage{7}',r'\mspage{\hand{7}}','The upper7 is handwritten.'),
(r'\mspage{146}',r'\mspage{\hand{146}}','The lower146 is handwritten.'),
(r'\det P^{\unsure{\hand{-}}1}',r'\det P^{\hand{\unsure{-|\vee}}1}','The handwritten mark before the typed1 has a descending left stroke and can be a check or a retouched minus; both shapes remain represented.'),
(r'\hand{\omega}_{X/Y}^{\unsure{\hand{-}}1}',r'\hand{\omega}_{X/Y}^{\hand{-1}}','The later inverse exponent is a pen-written -1; both strokes are visible.'),
(r'\begin{tikzcd}\n',r'\begin{tikzcd}\n','placeholder')]
r=r[:-1]+[(r'''\begin{tikzcd}
 & P \arrow[r, hook] & M \\
\det P\otimes\det Q\otimes\det M^{-1}=L \arrow[r, phantom] & L \arrow[u, "a"] \arrow[r, "b"] & Q \arrow[u, hook]
\end{tikzcd}''',r'''\begin{tikzcd}
P \arrow[r, hook, handwritten] & M \\
\det P\otimes\det Q\otimes\det M^{-1}=L \arrow[u, "a", handwritten] \arrow[r, "b", handwritten] & Q \arrow[u, hook, handwritten]
\end{tikzcd}''','The scan has one bottom-left L, with its long equality label to the left, rather than two copies of L. The four arrows are handwritten; a and b and all objects are typed.'),
(r'\unsure{\underline{I}}',r'\hand{\underline{I}}','The two ideal symbols are hand-drawn underlined capitals I; their thick uneven stems and bars match one another.'),
(r'\unsure{clariffer|clarifier}',r'clariffer','The second middle glyph has the upright head and crossbar of f, not a dotted i; the visible spelling clariffer is retained.'),
(r'\inserted{(D)}',r'\inserted[typed]{(D)}','The label (D) is typed above the line; its insertion brace is handwritten.'),
(r'\phi',r'\hand{\phi}','The phi has a free pen stroke and oval and is handwritten, not a typed slashed-o.'),
(r'\longrightarrow',r'\hand{\longrightarrow}','The two arrows in the opening morphism line are handwritten.'),
(r'\underline{O}_{\unsure{X|V}}1',r'\underline{O}_{\unsure{X|V}^{1}}','The overtyped X/V index remains doubtful, but the1 is raised relative to that index.'),
(r'\underline{O}_{V}1',r'\underline{O}_{V^{1}}','Each1 is raised relative to the lowered V in the coefficient index.'),
(r'$X-Y$ et $Y-S$',r'$X\hand{\to}Y$ et $Y\hand{\to}S$','The short connectors are pen arrows, with visible right tips, rather than typed hyphens.'),
(r'\uline{a} ce \hand{---}',r'\uline{a} \uline{ce}','The low pen stroke under ce is an underline at the same level as the neighboring underlines, not a baseline dash after ce.'),
(r'\uline{factorise par la composante $\underline{O}_{V1}$}',r'\uline{factorise par la composante} $\underline{O}_{V^{1}}$','The long underline ends after composante, before the coefficient sheaf; its1 is raised relative to V.')]
d={9:'The dx fragment is x-cancelled; the pen mark in the first inverse exponent remains minus/check uncertain.',28:'Both ideal letters are handwritten underlined I and can be read consistently from their matching forms.',29:'NB en begins the handwritten two-line note.',30:'The full note reads les points notin V(a)=V(b), L est exactement l’intersection de P et Q dans M; every letter and symbol is retained.',32:'The scan reads clariffer, with two f-shaped glyphs, so the spelling is retained without normalization.',33:'Phi is handwritten; the inserted (D) is typed with a hand brace, and dx is typewriter-cancelled.',35:'The first omega and the whole -1 exponent are handwritten; the X/V overtyped coefficient index remains doubtful. The second omega is handwritten and underlined.',36:'All three omegas are handwritten; the coefficient indices visibly raise1 above V.',38:'The underlined Omega is handwritten; the extra x after morphismes is typed cancellation, and the two short arrows are handwritten.',39:'The isomorphism sign and omega are handwritten.',40:'Omega and omega are handwritten. The lxxp fragment is typed cancellation. The first h in homorphisme remains uncertain; the low stroke under ce is an underline, not a textual dash.'}
n=['The two page numbers are handwritten.','The first pen exponent mark remains minus/check uncertain; the later inverse exponent over omega is clearly written -1 by hand.','The long equality is the label of a single L. The duplicated L and phantom connector are removed; all four visible arrows retain their exact directions and hook forms, and are marked handwritten.','The blanks between 0,F′,F,F″,0 and between the two determinant expressions are genuinely empty and are retained.','The matching handwritten ideal symbols read underlined I.','The printed word is clariffer; phi is handwritten rather than a typed slashed-o.','The coefficient index retains its X/V uncertainty; its1 is raised relative to the index letter.','The h remains uncertain; the underlines include ce but stop before the final O_V1. The former baseline dash was the underline beneath ce.','Every omega, Omega and the displayed isomorphism sign is handwritten.','Both scan parts, all typed baselines, the complete handwritten note and all diagram objects/arrows were read.']
e=[dict(line='14–15',before=r"0\quad F'\quad F\quad F''\quad0; det F\quad det F' tensor det F''",image='The spaces for connectors are blank on the scan.',decision='preserved',reason='No arrows or isomorphism sign are supplied in these two lines; the source gaps remain as printed.',category='mathematical-gap'),dict(line=40,before='a ce factorise',image='a ce factorise, with ce underlined',decision='preserved',reason='The page visibly reads ce, and the pen stroke underlines it. No replacement by se is made in the checked transcription.',category='spelling')]
x=complete(k,r,d,n,e);print(k,len(x['decisions']))
