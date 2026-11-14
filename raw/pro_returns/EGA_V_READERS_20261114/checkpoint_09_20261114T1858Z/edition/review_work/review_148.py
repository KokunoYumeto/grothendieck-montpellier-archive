import sys
sys.path.insert(0,'edition/scripts')
from audit_late_helpers import complete
k='ega25_25_148'
r=[
(r'\xout{X}$V_y$',r'$\over{X}{V}_y$','The first V is a pen-drawn letter over the typed X; the lowered y is typed. The second cancelled X remains a separate typed cancellation.'),
(r'conditions de déf.1',r'conditio\unsure{n|g}s de déf.1','The penultimate typed letter is an n/g overprint rather than a clean n.'),
(r'\xout{\unsure{de}}',r'\xout{de}','The short cancelled word before x prime is readable as de through the x strokes.'),
(r'ex\xout{c}cellent',r'ex\xout{\unsure{c}}cellent','The x-shaped strike in excellent obscures the proposed extra c; its underletter stays tentative.'),
(r'\xout{bien}',r'\unsure{bien}','Enlargement shows an overprinted live word bien, without typewriter x cancellation across it; its overprinted middle retains doubt.'),
(r'au Chap',r'au \unsure{Chap|Chaap}','The a/h region is overprinted and the apparent extra a is retained as an alternative rather than silently normalized.'),
(r'des points de non lissité',r'\unsure{des|dess} points de non lissité','The last s at the beginning of this line is overprinted; both visible letter-count readings are kept.'),
(r'\over{\unsure{4}}{$\phi$}',r'\over{\unsure{4}}{$\phi$}','The phi is handwritten over a typed glyph that can still be read as4, but that underlying candidate remains uncertain.'),
(r'\phi = xy',r'\phi = \unsure{xy}','The y in xy is heavily overprinted; the visible candidate xy is retained with doubt rather than silently flattened.'),
(r'fonctions coordonnées',r'fonctions co\unsure{or|rr}données','The middle two letters are overtyped and visibly allow or/rr; the source’s normalized spelling is replaced by an explicit local doubt.'),
(r'\phi',r'\hand{\phi}','Every phi in the typescript is handwritten; the already handwritten replacement remains marked.'),
(r'\geqslant',r'\hand{\geqslant}','The inequality sign is drawn by hand.'),
(r'''\begin{tikzcd}
 & & 0 & & \\
 & & \Omega^1_{X/Y}\otimes\underline{O}_{V'} \arrow[u] & & \\
0 \arrow[r] & P^1_{X/Y}(K)^{\vee}\otimes\underline{O}_{V'} \arrow[r] \arrow[ur, "\mu"] & \Omega^1_{X/S}\otimes\underline{O}_{V'} \arrow[r] \arrow[u] & \Omega^1_{V'/S} \arrow[r] & 0 \\
 & K^{-1}\otimes\underline{O}_{V'} \arrow[u] \arrow[r] & \Omega^1_{Y/S}\otimes\underline{O}_{V'} \arrow[u] \arrow[ur, "\nu"'] & & \\
\omega^{\unsure{-2}}_{X/Y}\otimes K^{\unsure{-2n-1}}\otimes\underline{O}_{V'} \arrow[ur] & & 0 \arrow[u] & &
\end{tikzcd}''',r'''% NOTE: The complete diagram, including all objects, labels and arrows, is handwritten. Horizontal endpoint marks are solid dots; the vertical endpoints are open zeros.
\begin{tikzcd}
 & & \hand{0} & & \\
 & & \hand{\Omega^1_{X/Y}\otimes\underline{O}_{V^1}} \arrow[u, handwritten] & & \\
\hand{\bullet} \arrow[r, handwritten] & \hand{P^1_{X/Y}(K)^{\vee}\otimes\underline{O}_{V^1}} \arrow[r, handwritten] \arrow[ur, "\hand{\mu}", handwritten] & \hand{\Omega^1_{X/S}\otimes\underline{O}_{V^1}} \arrow[r, handwritten] \arrow[u, handwritten] & \hand{\Omega^1_{V^1/S}} \arrow[r, handwritten] & \hand{\bullet} \\
 & \hand{K^{-1}\otimes\underline{O}_{V^1}} \arrow[u, handwritten] \arrow[r, handwritten] & \hand{\Omega^1_{Y/S}\otimes\underline{O}_{V^1}} \arrow[u, handwritten] \arrow[ur, "\hand{\nu}"', handwritten] & & \\
\hand{\omega^{-2}_{X/Y}\otimes K^{\unsure{-2n-1|-n-1}}\otimes\underline{O}_{V^1}} \arrow[ur, handwritten] & & \hand{0} \arrow[u, handwritten] & &
\end{tikzcd}''','The entire diagram is pen-written, a layer omitted by the source. Its V indices have raised1 forms matching the Omega exponents, not free primes. The omega exponent is clear -2; the blotted K exponent remains uncertain. Every object, label and arrow direction is retained; the two horizontal endpoints are visibly solid dots and the vertical endpoints open zeros.')]
# Identity reading above is already documented in the per-macro review; do not log it as a change.
r=[x for x in r if x[0]!=x[1]]
d={5:'The upper9 is handwritten.',7:'The first V is handwritten over typed X; the second X is separately cancelled on the typewriter.',10:'The small cancelled word before x prime is legible as de.',12:'The extra c candidate inside excellent remains uncertain under an x stroke. Bien has overprinting but no cancellation and is restored as doubtful live text.',13:'Lorsque is typewriter-cancelled. The overprint in Chap/Chaap remains explicit.',17:'The phi overwrites a tentative typed4; géom. is handwritten above normal. The inequality sign is handwritten.',18:'Nécessairement is typed above the line with a hand bracket. Vérifie is crossed by hand and constate is handwritten above it.',21:'The complete handwritten sentence reads Voici le diagramme analogue à (D), mais pour.',22:'The following handwritten line reads une section varphi d’un Module inversible K; its lowercase and capital forms are retained.',24:'The diagram label (D′) is handwritten in the left margin.',31:'The omega exponent is clearly -2. The K exponent is blotted and remains -2n-1/-n-1 uncertain; the surrounding tensor factors and raised V1 index are legible.',35:'The lower148 is handwritten.'}
n=['The upper9 and lower148 are handwritten.','The first V is a handwritten overwrite of typed X; the second X is a separate typed cancellation.','De is legible beneath its typewriter cancellation.','The typed underglyph remains a tentative4, with a handwritten phi over it.','Nécessairement is typed; constate is handwritten above pen-cancelled vérifie.','The overprints in conditions, excellent, Chap/Chaap, des/dess, xy and co-or/rr-données are now explicitly retained. Enlarging bien showed live overprinting rather than cancellation.','The enlarged omega exponent reads -2. The K exponent remains uncertain; no value is supplied from the surrounding argument. All diagram material is marked handwritten and its actual arrows and endpoint shapes are retained.','The two handwriting lines and the complete diagram were read, in addition to every typed line and margin; small doubtful glyphs were inspected in enlarged crops.']
e=[dict(line='17–19',before='dim_x(X)≥2; dim_x X=1; example phi=xy in the affine plane',image='dim_x(X)≥2; dim_x X=1; example phi=xy in the affine plane',decision='preserved',reason='Both displayed dimension comparisons and the named affine-plane example are visibly written this way. Their apparent mismatch is recorded for the guide without altering a dimension or hypothesis.',category='mathematical-slip')]
x=complete(k,r,d,n,e);print(k,len(x['decisions']))
