import sys
sys.path.insert(0,'edition/scripts')
from audit_late_helpers import complete
k='ega25_25_161'
r=[
(r'\mspage{4}',r'\mspage{\hand{\unsure{4|H}}}','The upper numeral has an H-like crossed-stem shape; 4 and H remain visual candidates without deciding from pagination.'),
(r'v\xout{X}ariable',r'v\unsure{a|X}riable','There is one overprinted a/X cell after v, not an extra cancelled X followed by a clean a.'),
(r'précis\unsure{\xout{x}}ément',r'précis\xout{\unsure{m}}éme\unsure{n|t}t','An extra cancelled letter after précis allows m; near the end the n/t impressions are also overprinted, so neither is normalized.'),
(r'\inserted{qu coh}',r'\inserted[typed]{qu coh}','Qu coh is typed above the line with a pen placement bracket.'),
(r'\xout{dexxxx}',r'\xout{de \unsure{ty}}','The cancelled group preserves de and tentative t/y remnants; no missing continuation such as type is supplied.'),
(r'\hand{\mu}',r'\over{\unsure{u}}{\mu}','Both mu forms have a serifed underglyph tentatively u and a long pen diagonal; the previously omitted underlying layer is retained as uncertain.'),
(r'le noyau \inserted{K}',r'le no\unsure{y|g}\unsure{a|g}u \inserted[typed]{K}','Noyau has two overprinted internal letters. K is a typed insertion above its placement slash, not a handwritten capital.'),
(r'ne\xout{xxx}',r'ne\xout{est}','The cancelled letters after ne read est through the x strokes.'),
(r'\xout{;}',r'\xout{\unsure{;}}','The punctuation beneath the cancellation after the ellipsis is too overtyped to settle confidently as a semicolon.'),
(r'\inserted{de type}',r'\inserted[typed]{de type}','De type is typed above the baseline with a pen leader.'),
(r'\xout{lxxxlxxxxxthéxiexx}',r'\xout{local noethérien}','Local noethérien is readable beneath the typewriter cancellation.'),
('en est ainsi','en '+r'\unsure{est}'+' ainsi','Est has overlapping e/s impressions; it remains an uncertain typed word.'),
(r'\xout{E}Lorsque',r'\unsure{L|E}orsque','The initial letter is an L/E overprint in a single cell, not an extra cancelled E followed by a clean L.'),
(r'n \geqslant 2',r'n \hand{\geqslant} \unsure{2}','The comparison sign is handwritten and the2 is overprinted, so the latter remains tentative.'),
('n un entier','n un ent'+r'\unsure{i|e}\unsure{e|r}'+'r','Two internal cells of entier have overprints; their visible alternative traces are retained.'),
(r'\frac{\partial\phi}{\partial X_i}',r'\hand{\frac{\partial\phi}{\partial\textcolor{black}{X_i}}}','The differential signs, phi and fraction bar are pen-drawn; X_i is typed.'),
(r'\phi',r'\hand{\phi}','All phi signs are handwritten.'),
(r'\to',r'\hand{\to}','The short arrows are pen-drawn.'),
(r'\longrightarrow',r'\hand{\longrightarrow}','The graded-map arrow is pen-drawn.'),
(r'\mspage{161}',r'\mspage{\hand{161}}','The lower161 is handwritten.')]
d={5:'The upper figure has both4-like and H-like strokes and remains uncertain.',7:'The variable word contains one a/X overprint; the extra cancelled letter after précis and later n/t overprint remain doubtful. Pré is typewriter-cancelled.',8:'Le is typewriter-cancelled; the differential fraction is handwritten apart from the typed X_i.',11:'The e in Soient remains overprinted. Qu coh is typed above the line. The cancelled group preserves de and tentative ty remnants.',16:'The mu-shaped symbol has a tentative typed u beneath its pen correction; the long arrow is handwritten.',17:'The second mu has the same layering. K is typed, noyau has internal overprints, and de is crossed only by the insertion leader, not deleted.',19:'The cancelled letters after ne read est.',22:'A dark vertical pencil line emphasizes the paragraph beginning15.1.',24:'The punctuation after the ellipsis is heavily overtyped and remains uncertain.',27:'De type is a typed interlinear insertion.',28:'Local noethérien is legible under x strokes; the later augmentation/augmantation overprint remains uncertain.',30:'The multiplicity n remains overprinted; est and the initial L/E of Lorsque are also explicitly doubtful.',32:'The i is underlined and the extra m is x-cancelled. The short arrow is handwritten.',33:'The multiplicity n and numeral2 remain overprinted; the >= sign is handwritten.',36:'The lower161 is handwritten.'}
n=['The upper4/H shape remains explicitly uncertain; the lower161 is clear handwriting.','The a/X is a single overprinted cell, and précisément has a cancelled extra letter and a later overprinted cell, all now preserved locally.','The e of Soient remains doubtful. Qu coh is typed with a hand leader; de and tentative ty survive in the cancelled group.','Both mu forms have an uncertain typed u under the pen alteration. K is typed; noyau has visible overprints. De is not cancelled: the slash belongs to the insertion leader.','The letters cancelled after ne are readable as est.','The cancelled local noethérien is recovered. Augmentation/augmantation and both multiplicity n readings remain doubtful;2, est, L/E and the two internal cells of entier are also now marked.','The dark vertical marginal stroke is retained. The much fainter reverse-looking traces near the final lines and a) were inspected but not treated as additional front text.','The empty note item adds no concern; all margins were inspected.','Both supplied images and each foreground line, formula, small insertion, cancellation and margin were read; the short overprints and mu/K layers were enlarged.']
x=complete(k,r,d,n);print(k,len(x['decisions']))
