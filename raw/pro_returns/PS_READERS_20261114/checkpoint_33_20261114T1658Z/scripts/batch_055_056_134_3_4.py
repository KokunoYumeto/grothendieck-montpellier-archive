import re,sys
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT

key='ps_134-3_055'
src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text()
edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'\hat{}',r'^{\hand{\wedge}}')
 if new!=line:edits.append([line,new,'The presheaf caret on this line is a handwritten raised wedge; preserve its position and repair the empty accent.'])
edits += [
  [r'\mspage{55}',r'\mspage{\hand{55}}','The folio is handwritten, with its second 5 heavily retraced.'],
  [r'h\over{\unsure{q}}{a}s',r'h\over[typed]{q}{a}s','The old q descender and the serif typed replacement a are both visible in the enlarged first word.'],
  [r'W\over{\unsure{n}}{h}en',r'\over{W}{W}\over{n}{h}en','The old n is readable; the h and the reinforced initial W are handwritten.'],
  [r'\hand{\v{C}}ech',r'$\overset{\hand{\scriptscriptstyle\vee}}{\mathrm{C}}$ech','The C is typed and only the háček is handwritten.'],
  [r'\xout{\unsure{hx}}',r'\xout{\unsure{hx}}\xout{\unsure{a}}','A second small machine-cancelled character sits below the first cancelled h-like fragment before the displayed h_n. It resembles a but remains uncertain.'],
  [r'\hand{(*)}',r'\hand{(41)}','The enlarged body call contains an angular 4 followed by a vertical 1, enclosed in parentheses; it is not an asterisk.'],
  [r'F\over{\unsure{e}}{o}r',r'F\over{e}{o}r','The typed e loop remains visible above the handwritten o.'],
  [r"\inserted{$\Delta'_n =$}",r"\inserted[typed]{$\hand{\Delta}'_n =$}",'The triangle is handwritten, while the inserted prime, n and equals sign are typed above the line.'],
  [r"\hand{\Delta'_n}",r"\hand{\Delta}'_n",'In the later occurrence only the triangle is handwritten; the prime and n are typed.'],
  [r'\xout{\unsure{acyclicity}}',r'\xout{acyclicity}','The cancelled acyclicity is readable under the typed x strokes.'],
  [r'\margin{$\uparrow$}',r'\margin{\diagram{\begin{tikzpicture}[x=1cm,y=1cm]\draw[->] (0.35,0)--(0.1,0) to[out=180,in=270] (0,0.12)--(0,0.9);\end{tikzpicture}}}','The upper margin has a bent arrow with a horizontal foot, rising beside the last two lines of the paragraph; reconstruct the graphic rather than a free upright arrow.'],
  [r'\margin{$\downarrow$}',r'\margin{\diagram{\begin{tikzpicture}[x=1cm,y=1cm]\draw[->] (0.35,0.95)--(0.05,0.95)--(0,0);\end{tikzpicture}}}','The lower margin arrow begins with a short horizontal top and descends beside the opening of section 36. Preserve its bent form without inferring a reordering instruction.']
]
save_review({
 'key':key,'edits':edits,
 'diffs':{
  2443:[r'$\overset{\hand{\scriptscriptstyle\vee}}{\mathrm{C}}$ech','Only the háček is added by hand; the C belongs to the typewritten word.','correct transcription'],
  2450:['T H 1)','The actual spaced condition label is typed T H 1), referring back to the homotopy condition of p.50.'],
  2452:[r'\hand{(41)}','The enlarged call reads 41, not (*); preserve the numbered call without supplying absent note text.','correct transcription'],
  2453:[r'\margin{*} ... \margin{ok if $\exists$ final object}','The left-margin star and pencil note are present. The note says ok if followed by an existence sign and final object.'],
  2454:['(T H 2)','The page has this literal typed label, including the opening parenthesis.'],
  2455:[r'$\hand{\Delta}^{\hand{\wedge}}$\xout{xxx}','A raised caret is visible after the triangle; the category is the presheaf category, unlike the witness’s plain simplex symbol.'],
  2456:[r"\inserted[typed]{$\hand{\Delta}'_n =$}",'The insertion mixes a pen triangle with typed index, prime and equals sign.','correct transcription'],
  2459:['Let U,V two subobjects','No be is typed between U,V and two.'],
  2461:[r'\inserted{[and covering e]}','Both square brackets belong to the handwritten insertion; they are not the witness parentheses.']
 },
 'unsure':[
  ['q','The old descender of q survives under the typed a.'],
  ['n','The typed n can be distinguished beneath the long pen h.'],
  [r'\unsure{hx}','A cancelled h-like form and x are visible, but the x may be only the machine cancelling character. An additional uncertain old a below it is now represented separately.'],
  ['e','The old e bowl is clear beneath the replacement o.'],
  ['acyclicity','The cancelled word is legible letter by letter.']
 ],'illegible':[],
 'notes':[
  'The a in has is a typed replacement over a q, whose descender remains visible.',
  'The small mark above the h of The is a doubled type impression/stray mark; it does not establish an independent quotation mark or word.',
  'The cancelled h-like fragment was enlarged. A further small cancelled character below it resembles a, and has been restored with an explicit doubt.',
  'All listed final readings are legible despite doubled impressions. The inserted final word is literally apshericity; it remains uncorrected.',
  'Both marginal arrows are bent strokes with short horizontal ends. They have been reconstructed as graphics, with no invented textual instruction or reordering.'
 ],
 'evidence':'Both halves opened and read, with enlarged has/When/homotopy/call/For/acyclicity/folio/section details. The folio is handwritten 55. The body call after the last element is (41), while the margin separately has a star and ok if there exists a final object. The proof covers the ordered product by maximal flags and appeals to the displayed Mayer–Vietoris-type lemma. Its final insertion is typed apshericity above cancelled acyclicity. The opposite bent margin arrows remain graphics. The old homotopy fragments retain doubt; author spellings standart and it’s are retained.'
})

key='ps_134-3_056'
src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text()
edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=re.sub(r'\\hand\{\$([^$]+)\$\}',r'\\hand{\\ensuremath{\1}}',line)
 if new!=line:edits.append([line,new,'Mechanical math-mode repair: replace the inner dollar pair in each hand macro by ensuremath, valid both within a formula and in text. Glyphs and handwritten/typed distinction are unchanged.'])
edits += [
 [r'A$^\wedge$',r'$A^{\hand{\wedge}}$','The caret after the A in the opening nerve formula is handwritten; retain the actual A rather than the witness’s simplex symbol.'],
]
# Three occurrences of text-mode A$^wedge$ require distinct contextual changes.
edits.pop()
for line in src.splitlines():
 if line.startswith('%'):continue
 normalized=re.sub(r'\\hand\{\$([^$]+)\$\}',r'\\hand{\\ensuremath{\1}}',line)
 new=normalized.replace(r'A$^\wedge$',r'$A^{\hand{\wedge}}$').replace(r'A^\wedge',r'A^{\hand{\wedge}}').replace(r'$^\wedge$',r'$^{\hand{\wedge}}$')
 if new!=normalized:edits.append([normalized,new,'The presheaf carets on this line are handwritten; encode their raised position while retaining the source’s base letters.'])
edits += [
 [r'\inserted{where}the',r'\inserted{where} the','The handwritten placement stroke puts where after the opening parenthesis and before the; retain a separating word space when the insertion is read continuously.'],
 [r'\hand{\ensuremath{\alpha}}(C) : \hand{\ensuremath{\Delta}}_{n}',r'\hand{\ensuremath{\alpha}}(C) : \over{A}{\Delta}_{n}','The first triangle of the displayed nerve rule is written over a typed A, whose crossbar and serif remain visible.'],
 [r'\hand{\ensuremath{\square}}$^{\hand{\wedge}}$',r'\over{\unsure{\hand{\ensuremath{\widetilde{\Delta}}}}}{\ensuremath{\square}}$^{\hand{\wedge}}$','The square in the beta formula surrounds a surviving triangular form, with a dense wavy cancellation above it. Preserve the earlier possible tilde/triangle as uncertain beneath the replacement.'],
 [r'$A_{/\hand{\ensuremath{\alpha}}(C)}',r'$\over[typed]{\unsure{A}}{A}_{/\hand{\ensuremath{\alpha}}(C)}','The A before the slice subscript is a doubled serif type impression. Its underlying character is not securely distinct; preserve that unresolved old layer without changing the final A.'],
 [r'\deleted{which is}',r'\deleted{\unsure{which is}}','which remains partly visible, but the final word is covered by the heavy pen cancellation; retain the whole proposed old phrase as uncertain.'],
 [r'\hand{\ensuremath{\xrightarrow{\ i_{A}\ }}}',r'\hand{\ensuremath{\xrightarrow{\ \textcolor{black}{i}_{A}\ }}}','The arrow and its subscript A are handwritten, whereas i is typed. Restore the typed label’s plain color.'],
 [r'''a' \ar[rr,"\hand{\ensuremath{\Delta_u}}"] \ar[dr,swap,"p'"] & & a \ar[dl,"p"]''',r'''a' \ar[rr,color=blue,"\hand{\ensuremath{\Delta_u}}"] \ar[dr,color=blue,swap,"p'"] & & a \ar[dl,color=blue,"p"]''','All three arrows in the triangle are drawn by hand; the node strings and p labels are typed. Add only arrow provenance, retaining topology and the source a-prime/a labels.'],
 [r'\diagram{\begin{tikzcd}[row sep=small,column sep=small]',r'% Hand-drawn arrows are marked blue; typed objects remain plain.'+'\n'+r'\diagram{\begin{tikzcd}[row sep=small,column sep=small]','Document the mixed provenance of the reconstructed diagram.']
]
save_review({
 'key':key,'edits':edits,
 'diffs':{
  2466:['has a final element','The opening line clearly says element, not object.'],
  2467:[r'$(\ldots\Delta_m\mathrm{x}\Delta_n)$','The typed closing parenthesis follows the product and precedes the comma and if.'],
  2468:[r'$A^{\hand{\wedge}}$','The image visibly has typed A with a pen caret in this position; it is not a handwritten simplex symbol.'],
  2473:[r"a' \longrightarrow a,\quad\text{label }\Delta_u",'The diagram really has typed a-prime and a as its upper nodes and a handwritten Delta-u label. Preserve that apparent abbreviation/slip instead of replacing the objects by Delta-indexed categories.']
 },'unsure':[],'illegible':[],
 'notes':[
  'The cancellation after ding has (C) followed by one conspicuous x; the original representation is retained.',
  'The square contains a triangular earlier form and has a dense wavy cancellation above it. Both are now preserved as an uncertain old tilde/Delta beneath the square, with the final caret separate.',
  'The first A of the slice expression is a doubled typed impression; its earlier layer is now explicitly uncertain.',
  'The final arrow label has a typed i and handwritten subscript A; the arrow is handwritten. The color encoding now distinguishes them.',
  'The vowel of deduced is overtyped but the final u is readable; no distinct old vowel can safely be recovered.',
  'The old which is was enlarged: which is partly legible, while the final letters remain covered. The cancelled phrase now carries an explicit uncertainty.',
  'where is placed after the opening parenthesis by its insertion stroke. A word space is retained before the following the.'
 ],
 'evidence':'Both complete halves inspected, with enlarged cancellation, cube, A, i_A, which-is and deduced details. The opening source deliberately says final element and A-hat. The nerve display contains a typed A under its first handwritten Delta. All three arrows in the triangular diagram are pen strokes, but its nodes are literally a-prime, a and C, with typed p-prime and p; the arrow label reads Delta-u. The proposition adds that A is aspheric, replaces which is by the latter and strengthens a weak equivalence to aspheric by cancellation and retyping. The final i_A label has a typed i and pen A. Old layers of the cube and doubled A, and the cancelled which-is phrase, remain uncertain.'
})
