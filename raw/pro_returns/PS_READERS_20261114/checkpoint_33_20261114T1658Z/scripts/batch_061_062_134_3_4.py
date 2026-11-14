import re,sys
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT

key='ps_134-3_061';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=re.sub(r'\\(longrightarrow|longmapsto|mapsto|to)(?![A-Za-z])',r'\\hand{\\\1}',line)
 new=new.replace(r'\hat{}',r'^{\hand{\wedge}}').replace(r'\wedge e_{1}',r'\hand{\cap} e_{1}').replace(r'\emptyset_',r'\hand{\emptyset}_')
 if new!=line:edits.append([line,new,'The plain arrows, raised presheaf carets and set-theoretic glyphs on this line are handwritten. The endpoint intersection is a rounded cap; retain all typed letters and indices.'])
edits += [
 [r'\xrightarrow{\ i^{*}\ }',r'\hand{\xrightarrow{\ \textcolor{black}{i^{*}}\ }}','The first composite arrow is handwritten, while its i-star label is typed.'],
 [r'\xrightarrow{\ i_{A}\ }',r'\hand{\xrightarrow{\ \textcolor{black}{i_{A}}\ }}','The second composite arrow is handwritten, while its i_A label is typed.'],
 [r'e\xout{\unsure{q}}quivalent',r'e\over[typed]{\unsure{q}}{q}uivalent','The doubled q-like impressions occupy the same typewriter position; this is an overprint, not a separately cancelled letter before equivalent. The earlier character remains doubtful.'],
 [r'\inserted{$i_{A}i^{*}$}\unsure{(\deleted{**})}',r'\inserted[typed]{$i_{A}i^{*}$}\unsure{i(**)}','The added functor is typed above the line. A separate small typed i remains to the left of (**); no secure pen cancellation of the marker is visible, so preserve the entire lower residual group with uncertainty rather than assert deletion.'],
 [r'b)  T\over{h}{h}e',r'b)  T\over[typed]{h}{h}e','The h in the final The has doubled serif type impressions; unlike the preceding The in (iii), it is not visibly a pen replacement.'],
 [r'\overset{\text{d\hand{\'e}f}}{=}',r'\overset{\mathrm{d}\overset{\hand{\scriptscriptstyle\prime}}{\mathrm{e}}\mathrm{f}}{=}','Only the accent above the typed e of def is handwritten; preserve the upright typed letters.']
]
save_review({
 'key':key,'edits':edits,
 'diffs':{
  2562:[r'$\delta_1^L,\delta_0^L$','The handwritten first subscript is 1, the second is zero; the surrounding text names unit and zero in that order.'],
  2564:[r'$e_{\hand{1}}$','The pen subscript in the classified subobject is 1, reinforced by the matching margin e_1.'],
  2565:[r'$e^L_{\hand{1}}$','The inverse-image target has pen subscript 1 and a matching margin e_1^L.'],
  2566:[r'\margin{$e_1$} ... \margin{$e^L_1$}','Both handwritten margin formulas are plainly present and retained.'],
  2567:[r'$e_{\hand{0}}\hand{\to}L$','The domain of the restricted map has a handwritten zero subscript.'],
  2568:[r'$e_{\hand{0}}\hand{\to}L$ factors through $e^L_{\hand{0}}$','Both corrected endpoint subscripts are zero.'],
  2581:[r'\inserted[typed]{$i_Ai^*$}\unsure{i(**)}','The interlinear letters and star are typed. The lower i and (**), whose relation to the correction remains uncertain, are retained without an asserted handwritten deletion.','correct transcription']
 },
 'unsure':[
  [r'\unsure{q}','The old impression is q-like but cannot be separated securely from the final typed q; retain doubt while correcting the layer representation.'],
  [r'\unsure{i(**)}','A small residual i and the two-star marker remain below the typed replacement. Their cancellation/retention intent is not securely shown by the ink.'],
  [r'\unsure{:}','The character under the final comma is densely crossed; a colon is plausible but not confirmed.']
 ],'illegible':[],
 'notes':[
  'The delta subscripts are visibly 1 then 0, in agreement with unit then zero.',
  'The final endpoint indices are clear. Some lower typed strokes survive beneath the thick pen replacements, but no complete alternative old numeral is safely recoverable.',
  'The doubled q-like letter is at one typewriter position; it is now encoded as a typed overprint, with its earlier reading still doubtful.',
  'The functor inserted above the marker is typed. The lower marker and stray i are retained with uncertainty because no separate cancellation is securely visible.',
  'The h in (iii) is a pen retracing; the h in b) has displaced serif type impressions and is now marked as a typed overprint.',
  'All diagramless arrows on the page were checked and marked as pen; typed arrow labels in the compositum remain plain.',
  'The old character beneath the comma remains unreadable enough to retain the tentative colon.'
 ],
 'extra_records':[{'source_id':'OBS:ps_134-3_061:1','before':r'subobject $e_{o}\wedge e_{1}$ of $e_{1}$','after':r'subobject $e_{o}\hand{\cap}e_{1}$ of $e_{1}$','decision':'retain apparent authorial slip','reason':'The source really says of e_1, although the restriction just named has domain e_0; its pullback would be a subobject of e_0. Preserve the source index and flag the mismatch in the guide.','line':11}],
 'evidence':'Both complete halves read and eight local details enlarged. Endpoint indices follow the revised unit=1/zero=0 convention and match the two margin formulas. The source still calls e_o cap e_1 a subobject of e_1 after restricting to e_0; that apparent index slip is preserved. The theorem compares the evaluation functor with its localization consequences and separates the stronger b-conditions. All arrows are drawn by hand, their displayed labels mostly typed. The i_A i-star insertion in (ii) is typed, with a lower residual i(**) of uncertain editorial status; the final old punctuation also remains doubtful.'
})

key='ps_134-3_062';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=re.sub(r'\\hand\{\$([^$]+)\$\}',r'\\hand{\\ensuremath{\1}}',line)
 new=new.replace(r'A\^{}',r'$A^{\hand{\wedge}}$').replace(r'A^\wedge',r'A^{\hand{\wedge}}')
 new=new.replace(r'\emptyset',r'\hand{\emptyset}').replace(r'\neq',r'\hand{\neq}')
 if new!=line:edits.append([line,new,'Repair nested math delimiters with ensuremath and mark the scanned presheaf carets, empty-set signs and inequality as handwritten, retaining typed base letters.'])
edits += [
 [r'\mspage{62}',r'\mspage{\hand{62}}','The folio is handwritten.'],
 [r'\hand{\ensuremath{\xrightarrow{\text{can}}}}',r'\hand{\ensuremath{\xrightarrow{\textcolor{black}{\text{can}}}}}','The arrow is handwritten but its can label is typed.'],
 [r'\xout{For any C in (Cat), the functor (xxx) is a weak equivalence}',r'\deleted{\xout{For any C in (Cat), the functor (xxx) is a weak equivalence}}','A continuous pen cancellation runs through the entire already machine-cancelled proposed condition, not only its numeral.'],
 [r'\margin{Look at \unsure{refined} \unsure{on} 63--65 vol.\ 2}',r'\margin{Look at sequel in vol.\ 2 pag \unsure{64--65}}','The rotated margin reads Look at sequel in vol.2 pag; the first page numeral is still uncertain, with 64--65 the best visible reading. Preserve that remaining doubt.'],
 [r'\unsure{\xout{a)}}the',r'\over[typed]{a)}{th}e','The old a) is visible beneath the typed th of the; this is a superposed typed replacement rather than a separate cancelled group.'],
 [r'\unsure{Section (\S40)}',r'Section (\S40)','The left continuation distinctly reads Section followed by the parenthesized section-40 reference; retain the source’s repetition after the earlier section sign.'],
 [r'impl\over{\unsure{y}}{\unsure{ies}}',r'impl\over{y}{ies}','The old y descender and the added dotted i/e/s ending can be distinguished in the enlarged verb.'],
 [r'standar\over{\unsure{t}}{d}',r'standar\over{t}{d}','The old typed t crossbar survives beside the pen d.'],
 [r'we get \inserted{(unique)} a homotopy',r'we get a \inserted{(unique)} homotopy','The placement hook descends between the typed a and homotopy, so (unique) is inserted after a.'],
 [r'\mathrm{x}\, C \rightarrow C',r'\mathrm{x}\, C \hand{\rightarrow} C','The arrow in the categorical homotopy display is handwritten.']
]
save_review({
 'key':key,'edits':edits,
 'diffs':{
  2587:[r'\margin{Look at sequel in vol.\ 2 pag \unsure{64--65}}','Two rotated enlargements settle sequel in and the vol.2 pag wording; the first page numeral remains uncertain.','correct transcription'],
  2589:[r'take \xout{in} C the final category','The source has no to be; in is cancelled before C.'],
  2590:[r'\inserted{lemma (cf.\ below \S\ Section (\S40))}','The inline lemma reference continues into the left margin with Section (§40). Its redundant literal wording is retained rather than normalized to the witness.'],
  2595:[r'\inserted{\deleted{(p.38)}}','The old handwritten page reference is itself struck by a dense pen line.'],
  2596:[r'\inserted{(section 30).}','The replacement says section 30, followed by the closing parenthesis and period.'],
  2597:[r'a \inserted{(unique)} homotopy','The insertion mark locates (unique) after a and before homotopy.','correct transcription'],
  2607:[r'$a\mathrm{x}i^{*}(C)$','The source product character is a typed lowercase x; preserve it rather than normalize its glyph to times.']
 },
 'unsure':[
  ['sequel','The enlarged cursive word clearly contains the descending q and ends el.'],
  ['in','The following two letters are i and n.'],
  [r'\unsure{v}','A v-like remnant remains under the corrected ii, but the old numeral is not fully clear.'],
  ['a)','The old a and curved parenthesis are distinguishable underneath the typed th.'],
  ['Section (§40)','The margin continuation and both numerals are clear.'],
  ['y','The old y descender is visible.'],
  ['ies','The added dotted i, e loop and final s are readable.'],
  ['t','The old t crossbar survives at the left of the replacement d.']
 ],'illegible':[],
 'notes':[
  'The rotated margin reads Look at sequel in vol.2 pag, with the page range tentatively 64--65. The remaining numeral doubt is retained.',
  'The marginal Section (§40) is the continuation of the inserted lemma reference; its words and digits are now settled, without removing the preceding redundant section sign.',
  'The old numeral under the correction to iii remains a doubtful v.',
  'The old a) occupies the same cells as the replacement th of the. It is now represented as typed overprinting.',
  'Upper arrows are handwritten; their can label is typed. The displayed homotopy arrow and the lower empty-set/inequality signs are pen as well.'
 ],
 'evidence':'Both scan halves inspected, eight local crops read, and the volume-2 marginal reference rotated and enlarged separately. The removed original b(ii) has both machine and pen deletion. The live conditions concern asphericity over A times C, representable products and i-star(Delta_1). The margin points to the sequel in volume 2, with uncertain first page numeral. Remark 1 keeps the source unlikely after cancellation of not, and preserves its explicit distinction between weak equivalence and asphericity. The proof inserts (unique) after a, and replaces the p.38 reference by section 30. Remark 2’s endpoint equation uses a handwritten cap and empty-set sign; the final nonemptiness condition uses a pen inequality.'
})
