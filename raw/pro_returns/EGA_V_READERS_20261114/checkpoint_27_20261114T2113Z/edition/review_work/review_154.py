import sys
sys.path.insert(0,'edition/scripts')
from audit_late_helpers import complete
k='ega25_25_154'
r=[
(r'\over{\$}{$S$}',r'\over{S}{Y}','The base letter is a typed S overwritten by a forked handwritten Y, as on site153; it is not a dollar sign rewritten S.'),
(r'\over{\$}{S}',r'\over{S}{Y}','Each denominator has the same typed S under a forked handwritten Y.'),
(r'\xout{\unsure{naturel}}',r'\xout{naturel}','The cancelled word naturel is legible beneath the typewriter strokes.'),
(r'\xout{$d^{\infty}$\illegible{1}}',r'\xout{$d^{\infty}$\illegible{1}$E$}','The final typed E survives at the end of the cancelled fragment; the intervening letters remain unreadable.'),
(r'\inserted{$\underline{K}$}',r'\inserted[typed]{$\underline{K}$}','The inserted underlined K is typed, with a pen placement slash.'),
(r'\unsure{d|n}',r'\over{n}{d}','Both letters are handwritten d over typed n; their ascenders and the underlying n are visible.'),
(r'\xout{\unsure{maintenant}}',r'\xout{maintenant}','Maintenant is legible beneath its typewriter cancellation.'),
(r'\underline{\mathrm{Symm}}^{2}',r'\underline{\mathrm{Sym}}\xout{m}^{2}','The extra second m is x-cancelled and lies beyond the underline; it must not remain a live letter.'),
(r'\unsure{-n+m-1}',r'-n+m\over{\unsure{+|-}}{\unsure{-|+}}1','The first -n+m and final1 are clear; the intervening sign has pen overprinting and cannot be uniquely read as minus or plus. Both under- and over-reading remain doubtful.'),
('ordinaires','ordinair'+r'\unsure{es}','The terminal es is overtyped; the candidate letters are retained explicitly rather than presented as clean typing.'),
('homomorphisme envisagé','homomorphisme '+r'en\unsure{v|i}\unsure{i|v}s\unsure{a|g}gé','The doubled-looking v/i and a/g overprints in envisagé are retained at their exact positions.'),
('de modules loc','de '+r'\unsure{m}odules loc','The first letter of modules is obscured by multiple typed impressions; the m reading remains tentative.'),
('vectoriels sur',r'vect\unsure{o|r}\unsure{r|i}\unsure{i|r}\unsure{e|d}ls sur','The internal o/r, r/i, i/r and e/d overprints are visible on enlargement and are not silently normalized.'),
('de Modules\n','de Modu'+r'\unsure{l|b}es'+'\n','The final line has an l/b overprint in Modules; both letterforms are retained.'),
(r'\infty',r'\hand{\infty}','The infinity signs are handwritten.'),
(r'\to',r'\hand{\to}','The short arrows are pen-drawn.'),
(r'\longrightarrow',r'\hand{\longrightarrow}','The two long arrows are pen-drawn.'),
(r'\bigwedge',r'\hand{\bigwedge}','The exterior-product wedge is handwritten.'),
(r'\underline{\Omega}',r'\underline{\hand{\Omega}}','The Omega letters are handwritten.'),
(r'\in ',r'\hand{\in} ','The membership signs are handwritten.'),
(r'\subset',r'\hand{\subset}','The inclusion sign is handwritten.'),
(r'\notin',r'\hand{\notin}','The non-membership sign is handwritten.'),
(r'\Gamma',r'\hand{\Gamma}','The Gamma in the discriminant display is handwritten.')]
d={5:'The upper15 is handwritten.',8:'The typed S is overwritten by a forked Y, not a dollar sign by S.',9:'Naturel is legible beneath its typed cancellation.',10:'The cancelled fragment retains d-infinity and a terminal E, with unreadable material between. Both denominators are S-to-Y overwrites.',13:'Both denominators are S-to-Y overwrites; the arrows are handwritten.',14:'The inserted underlined K is typed with a pen slash.',15:'The denominator is S-to-Y; Omega and the arrow are handwritten. The label is a typed underlined x.',18:'A broad looping pencil bracket emphasizes the following rank explanation.',21:'The denominator is S-to-Y; the wedge, arrow and Omega are handwritten.',25:'Both occurrences have handwritten d over typed n, now recorded explicitly.',26:'The denominator is S-to-Y, while the separate phrase sur S is visibly untouched.',27:'The asterisk is handwritten; maintenant is legible under the typed x cancellation.',32:'The exponent reads -n+m, then an overprinted ambiguous sign, then1. Neither sign reading is imposed from the rank discussion.',35:'The lower154 is handwritten.'}
n=['Every base correction is a typed S overwritten with handwritten Y; the dollar-to-S reading is corrected from the visible forked pen glyph.','Naturel and maintenant are legible under x strokes; the earlier cancelled fragment ends in a visible E but retains its unreadable middle.','Both rank letters are handwritten d over typed n.','The disputed sign between m and1 remains plus/minus uncertain, with its pen-overwrite layer recorded.','All named overprinted words were examined closely; the visibly ambiguous letter positions are now marked, while correspondant remains readable as typed.','The K is a typed insertion with a pen placement stroke; the asterisk and looping marginal bracket are handwritten.','Both folios are handwritten.','Every line, formula, overwrite and margin was inspected in both image parts; the small overprints and cancelled final m were enlarged.']
e=[dict(line=17,before='est de rang m-1 en x',image='est de rang m-1 en x',decision='preserved',reason='There is no comparison sign before m-1 in the parenthetical clause; the following clause repeats exactement de rang m-1. The page’s wording and blank space are retained.',category='mathematical-slip'),dict(line='25–32',before='rank d-(m-1), discriminant exponent -n+m [sign]1',image='rank d-(m-1), discriminant exponent -n+m [sign]1',decision='preserved',reason='The rank letters are changed from n to d by hand, but the discriminant exponent retains a typed n. This incomplete change of parameter is preserved for the guide.',category='notation-discrepancy')]
x=complete(k,r,d,n,e);print(k,len(x['decisions']))
