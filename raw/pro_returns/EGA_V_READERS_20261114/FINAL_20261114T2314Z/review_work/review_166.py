import sys
sys.path.insert(0,'edition/scripts')
from audit_late_helpers import complete
k='ega25_25_166'
r=[
(r'\margin{//}',r'\margin{\unsure{//}}','The upper-left brown oblique traces are visible, but their ink-versus-material origin is uncertain; they are not confidently classified as a textual double slash.'),
(r'\hand{nouveau EGA V}',r'\hand{nouveau EGA $\overline{\underline{\mathrm{V}}}$}','The handwritten V has both an upper and lower horizontal bar.'),
(r'\mspage{1}',r'\mspage{\hand{1}}','The upper-right1 is handwritten.'),
(r'\margin{(}',r'\margin{\unsure{(}}','The long brown curved trace follows the left edge and hooks near the title; its bracket-like appearance is retained with uncertainty about its origin.'),
(r'ab\unsure{us}if',r'ab\unsure{u|e}\unsure{s|u}\unsure{i|f}f','The two middle cells are overprinted, and the following i position also has an f-like stem and crossbar. Each ambiguous cell is retained.'),
('et celle à laquelle',r'et \over{\unsure{t|c}ell}{cell}e à laquelle','The first four letters of celle have pen retouching, including loops above both l letters; the first underlying letter has t/c-like traces.'),
('on applique le lemme',r'on app\unsure{l|D}ique le lemme','The l cell in applique has a large rounded D-like typed overprint, retained locally.'),
('satisfait V(a)',r'satis\over{f}{f}ait V(a)','A high curved pen f retraces the typed f in satisfait.'),
(r'libres\inserted{sur',r'libres \inserted{sur','The handwritten sur V1 is inserted as a separate phrase after libres; the word boundary is visible.'),
(r'\inserted{$\mu$:} $P',r'\inserted{$\unsure{\mu|u}$:} $P','The first raised handwritten label has a u-like bowl without a secure mu descender; its mu/u reading remains uncertain. It is placed before P.'),
(r'\inserted{pré}',r'\inserted[typed]{pré}','Pré is typed above schéma and placed with a handwritten leader.'),
(r' & & 0 & &',r' & & \hand{0} & &','The top endpoint zero is drawn by hand, like the lower vertical endpoint.'),
(r'\underline{\Omega}',r'\hand{\underline{\Omega}}','Every Omega and its underline are drawn by hand in the diagram and inline formulas.'),
(r'\otimes',r'\hand{\otimes}','All tensor signs are hand-drawn circles and crosses.'),
(r'\arrow[u]',r'\arrow[u,handwritten]','All vertical arrows have pen-drawn shafts and heads.'),
(r'\arrow[r]',r'\arrow[r,handwritten]','All horizontal diagram arrows are drawn by hand, including the faint-headed central-right arrow.'),
(r'\arrow[ur, ',r'\arrow[ur,handwritten, ','Both rising diagonal arrows are handwritten; their directions and labels are preserved.'),
(r'\rightarrow',r'\hand{\rightarrow}','Each short arrow outside the diagram is drawn by hand.'),
(r'\longrightarrow',r'\hand{\longrightarrow}','Each long arrow outside the diagram is drawn by hand.'),
(r'\subset',r'\hand{\subset}','Both inclusion signs in the displayed chain are handwritten.'),
(r'\simeq',r'\hand{\simeq}','Both isomorphism signs are handwritten.'),
(r'\margin{166}',r'\mspage{\hand{166}}','The lower166 is a handwritten archive folio, not running marginal text.')]
d={5:'Nouveau EGA V is handwritten and the V has top and bottom bars; the upper folio1 is handwritten. The brown double-slash-like edge traces remain uncertain in their material origin.',7:'The long brown curve beside the heading has a bracket-like hook but follows the sheet edge; its textual function remains uncertain.',12:'The quotes around i.e. are handwritten. Abusif has three overprinted cells, including the i/f position, each now explicit.',21:'The rising arrow and its mu label are hand-drawn; all adjacent Omega/tensor glyphs and horizontal/vertical arrows are also handwritten.',22:'The lower rising arrow and wr-like isomorphism label are handwritten; its endpoint and central column agree with the source layout.',23:'The bottom0 and its upward arrow are hand-drawn.',27:'Sur V1 is a handwritten insertion after libres. The l cell in applique is overtyped with a D-like trace. The M formula has handwritten Omega and tensor sign.',30:'The initial a is cancelled with typed x strokes. The first handwritten label is raised above P and remains mu/u-like; the second mu-colon is placed before N by a pen caret and is clear. Both maps and all their indices were checked.',31:'Pré is typed above schéma. The mu before strictement is clear handwriting.',32:'The less-than sign is handwritten; the f in satisfait is retouched by a pen f.',33:'The first digit of15 is rewritten as a hand1 over a still obscured1-like typed cell; the underlying digit remains tentative.',34:'Two close vertical pen strokes stand beside the chain and exact sequence, stopping before the isomorphism paragraph.',42:'The lower166 is handwritten foliation.'}
n=['The quotes are handwritten. Abusif has overprints in the u, s and i positions; all three remain uncertain, including the previously omitted i/f ambiguity.','Both vertical endpoint zeros, all diagram arrows, all Omega/tensor signs, and both diagonal labels are handwritten; the horizontal zeros retain their typed appearance. The row and column geometry was checked object by object.','The page15 reference has a pen1 over an obscured1-like typed cell, which remains tentative.','The first raised label before P is mu/u-like and remains uncertain; the second clear mu-colon sits above a caret immediately before N. Each placement is retained separately.','The double margin stroke spans the displayed chain and exact sequence, stopping above d’autre part.','Both1 and166 are handwritten folios, now encoded as such.','The pale reverse-looking background was inspected without identifying another foreground text line.','','There is no long handwritten passage. Both complete images, all text baselines, every diagram object/arrow/label, all indices, short insertions, cancellations and margin traces were inspected.']
x=complete(k,r,d,n);print(k,len(x['decisions']))
