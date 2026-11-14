from review_root import review, macro_occurrences, TEXT

def ds(key,name,reasons,resolved=None):
    s=(TEXT/'transcription/ps_pages'/(key+'.tex')).read_text();o=macro_occurrences(s,name);resolved=resolved or {}
    assert len(o)==len(reasons),(key,name,len(o),len(reasons))
    return [(resolved.get(i,x['source']),'doubt resolved' if i in resolved else 'doubt retained',reason) for i,(x,reason) in enumerate(zip(o,reasons),1)]

k='ps_134-2_010'
review(k,changes=[
    (r'\hand{101. Abelian integration $Lf_!^{ab}$ (versus abelian cointegra-%}',r'\hand{101. Abelian integration $Lf_!^{ab}$ (versus abelian cointegra-}%', 'Mechanical: move the closing brace ahead of the comment character without changing printed content.'),
    (r'\hand{106. Review (3): A formulaire for the basic integra-%}',r'\hand{106. Review (3): A formulaire for the basic integra-}%', 'Mechanical: move the closing brace ahead of the comment character without changing printed content.')
],doubts={'unsure':ds(k,'unsure',['The small mark after the first topoi is obscured by the adjacent strike; its punctuation remains uncertain.']),'illegible':[]},notes=[
    'Both halves are entirely handwritten, including the formulas and folio.',
    'The five marked item numbers have visible enclosing circles.',
    'The curved separator places tion Rf_* with item 101 although physically beside item 102. The original line disposition is retained.',
    'The bracket leads from case of down to pseudo-topoi, above the following item. The insertion belongs to item 104.',
    'The horizontal cancellation extends through and abelian topoi, including the final topoi. The preceding punctuation remains doubtful.',
    'The small shape below scheme is the looped extension/retracing of the handwritten initial s, not a separately legible mathematical symbol.',
    'The diagonal marginal heading reads VI and Schematization, with the box/underlines retained.',
    'The lower-left folio is handwritten 10; the nearby diagonal stroke is a separator.'
],summary='Both halves closely read, including all handwriting and displaced continuations. The one punctuation doubt remains. Two comment-hidden braces are repaired; no wording is changed.')

k='ps_134-2_011'
changes=[]
for n in [119,124,131,132]:
    changes.append((r'\hand{\textcircled{\phantom{0}}}'+str(n)+'.',r'\hand{\textcircled{\textcolor{black}{'+str(n)+r'.}}}', 'The circle encloses the typed item number; the empty circle before it was a placement error.'))
changes.extend([
    (r'\arrow[r, leftarrow, shift left,',r'\arrow[r, color=blue, leftarrow, shift left,','The upper left-pointing arrow is handwritten; the objects and label letters are typed.'),
    (r'\arrow[r, shift right,',r'\arrow[r, color=blue, shift right,','The lower right-pointing arrow is handwritten; the objects and label letters are typed.'),
    (r'$^{n}\hand{$\Pi$}. = L\Pi.(S^{n})$',r'$^{n}\hand{\Pi}. = L\Pi.(S^{n})$','Mechanical: remove redundant dollar delimiters nested inside the handwritten symbol in math mode.'),
    (r'127. Schematic homotopy types and Illusie\'s derived category for a \inserted{topos.}',r'127. Schematic homotopy types and Illusie\'s derived category for a \inserted[typed]{topos.}','The word topos is typed above the line; only its curved placement connector is handwritten.'),
    (r'W-\inserted{bundles.}',r'W-\inserted[typed]{bundles.}','The continuation bundles is monospaced typing above the line, with a handwritten connector.'),
    (r'equi\unsure{v}\inserted{valences.}',r'equi\inserted[typed]{valences.}','Enlargement shows typed equi followed by the tip of a handwritten connector, not a typed v; valences is a typed continuation above the line.'),
    (r'\unsure{ff}',r'ff','The enlarged image clearly shows two typed f characters. The diplomatic doubled letter is retained.'),
    (r'\mspage{11}',r'\mspage{\hand{11}}','The bottom-left folio 11 is handwritten.')
])
# The repeated fragments need occurrence-specific surrounding text for the audit.
for before,after in [
    (r'122. Rambling reflections on $L\hand{$\tilde{H}$}.$',r'122. Rambling reflections on $L\hand{\tilde{\textcolor{black}{H}}}.$'),
    (r'the basic ``four functors\'\' $L\hand{$\tilde{H}$}.$',r'the basic ``four functors\'\' $L\hand{\tilde{\textcolor{black}{H}}}.$'),
    (r'126. Dissymetry of $L\hand{$\tilde{H}$}.$',r'126. Dissymetry of $L\hand{\tilde{\textcolor{black}{H}}}.$'),
    (r'\hand{$\tilde{K}$} , \hand{$\tilde{S}$}',r'$\hand{\tilde{\textcolor{black}{K}}}$ , $\hand{\tilde{\textcolor{black}{S}}}$'),
    (r'spherical functor \hand{$\tilde{S}$}',r'spherical functor $\hand{\tilde{\textcolor{black}{S}}}$')
]:
    changes.append((before,after,'The accent is handwritten over a typed letter; keep the letter plain and the accent marked. Nested math delimiters are also repaired where present.'))
# Raw strings containing apostrophes above have no literal backslashes in the source.
changes=[(a.replace("\\'","'"),b.replace("\\'","'"),r) for a,b,r in changes]
review(k,changes=changes,doubts={'unsure':ds(k,'unsure',[
    'The small lowered character after picture remains overworked and its origin unclear.',
    'The vowel in binomial is blotted by overtyping; the proposed o remains marked.',
    'The initial a of analyzers is overtyped; the old strokes cannot be separated confidently.',
    'The letters for are retraced heavily enough that cancellation versus retracing remains uncertain.',
    'The apparent v is the tip of the handwritten connector. The continuation valences above is typed.',
    'The enlargement shows two distinct typed f characters; the doubt is resolved without correcting the doubled letter.'
],{5:'',6:'ff'}),'illegible':[]},notes=[
    'All four circles enclose the item numbers. The encoding is repaired to show typed numbers inside handwritten circles.',
    'The lowered x-like character and the overtyped o remain doubtful.',
    'The curly brace spans the two typed lines; the lambda is handwritten and the a remains overtyped.',
    'The upper arrow points left and the lower arrow right. The arrows and tildes are hand drawn, while LH, K and the objects are typed.',
    'The hand stroke over for remains ambiguous; the discrete set-up is clearly struck and ordinary homotopy types is handwritten.',
    'There are small pen strokes around the h in The; they do not yield a changed word. The first Pi is handwritten.',
    'The closing quotation marks are handwritten. The continuation bundles is typed, as the enlargement confirms.',
    'Enlargement resolves the end as typed equi plus a handwritten connector leading to typed valences above the line; there is no additional typed v.',
    'The scan clearly reads inffinite, with two typed f characters. That spelling is retained in the checked page.',
    'The two commas and separator are handwritten; the printed words remain typed.',
    'The bottom-left folio is handwritten and now marked.'
],summary='Both halves and enlarged right-edge crops reviewed. Repaired typed continuations wrongly marked as handwriting, handwritten circles and arrows, accent provenance, folio and nested math delimiters. Resolved the apparent extra v as a connector and the doubled ff as typed; four other doubts remain.')
