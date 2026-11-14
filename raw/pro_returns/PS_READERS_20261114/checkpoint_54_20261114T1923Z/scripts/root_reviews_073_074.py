from review_root import review

review('ps_134-2_073',changes=[
(r'\mspage{58}',r'\mspage{- \hand{5}8 -}','The centered folio includes both hyphens; its first digit is handwritten and its8 is typed.'),
(r'''\Delta \arrow[r, "j"] \arrow[d, "p"']''',r'''\Delta \arrow[r, "j",color=blue] \arrow[d, "p"',color=blue]''','Both arrows in the upper diagram are drawn by hand; the j and p labels remain typed.'),
(r'''\bullet \arrow[r] \arrow[d] & \bullet''',r'''\bullet \arrow[r,color=blue] \arrow[d,color=blue] & \bullet''','The two arrows of the lower shape diagram are hand-drawn.'),
(r"operations\hand{''}",r"operations''",'The closing quotation mark has the regular narrow parallel strokes of the typewritten quotation marks, rather than the larger angled pen strokes of the inserted opening quotation mark.'),
(r'inclusion\hand{s}',r'inclusions','The final s has the same regular typewriter impression and baseline as the preceding letters. The separate pen correction ies over boundary is retained.'),
(r'\margin{73}',r'\margin{\hand{73}}','The lower-left73 is pencil archive foliation.')
],doubts={'unsure':[(r'\unsure{29}','doubt retained','The live call appears to be29, but the second digit is heavily retraced; a secure distinction of its layers is unavailable.')],'illegible':[]},notes=[
'The centered folio is -58- with its5 in pen; no separate old digit can be recovered confidently.',
'The lower-left73 is handwritten archive foliation, now marked as such.',
'The parentheses are handwritten. The call29 remains doubtful because of the dense retracing of its second digit; no hypothetical old number is supplied.',
'The1 of X1 in the top diagram and of F1 in the displayed compatibility map is pen; the intervening X1 in prose has a regular typewritten1.',
'The closing quotation mark after operations is typed; its strokes match the typewritten quotation marks elsewhere on the page.',
'The s of inclusions is typed, while ies over the old y of boundary is a visible pen correction. The witness incorrectly returns both words to the singular.'
],summary='Both halves and enlarged diagram labels, quotation mark, call29 and plural corrections inspected. Restored the folio hyphens and pen5, marked four drawn arrows and archive foliation, and distinguished the typed closing quotation mark and plural s from pen. Retained the retraced call29 as doubtful. The plural spaces and handwritten boundaries are clear; the source excercise is preserved.',differences={
1184:('diagram of spaces','the typescript reads as our transcription','The final s of spaces is fully typed and visible; the witness changes it to singular space.'),
1186:(r'the inclusions of the boundar\over{y}{ies} in','our transcription corrected','The final s of inclusions is typed and the replacement ies of boundaries is pen. Both live words are plural, contrary to the witness singulars.')
})

review('ps_134-2_074',changes=[
(r'gluing(\hand{50})',r'gluing\hand{(30)}','Enlargement shows the two lobes of a handwritten3, followed by0; both enclosing parentheses are pen, not typing.'),
(r'\inserted{may be described\hand{,}}',r'\inserted{may be described}','The supposed comma is part of the continuous placement curve beneath the inserted words, not a separate punctuation mark.'),
(r'\unsure{mutal|natural}',r'mutal','The pen word clearly reads m-u-t-a-l; it has no second u and does not read natural. Preserve the literal handwritten spelling.'),
(r'\inserted{compact,}',r'\inserted{compact}','The hooked stroke after compact continues the insertion curve under the whole word. No independent comma is present.'),
(r'\margin{74}',r'\margin{\hand{74}}','The lower-left74 is pencil archive foliation.')
],doubts={'unsure':[('mutal','doubt resolved','The enlarged handwriting has a clear m, u, crossed t, a and looped l; the alternatives natural and mutual do not fit its visible letters.')],'illegible':[]},notes=[
'The leading5 of59 is handwritten. Its heavy retracing does not establish a separately readable older digit.',
'The call is30, not50, and both parentheses are handwritten; the original note was wrong about their typed provenance.',
'The replacement is the literal handwritten mutal. The scan settles the reading; it is not silently expanded or corrected to mutual.',
'The curved stroke before in terms is continuous with the insertion line under may be described, and is not a comma. The equivalent placement curve under compact is likewise not punctuation.',
'The lower-left74 is pencil archive foliation.'
],summary='Both halves and enlarged call, replacement word and two insertion curves inspected. Corrected call50 to handwritten(30), resolved mutal, and removed two false commas inferred from placement strokes. Confirmed into, made out of, and the baseline hyphens following P_X and P_Y. The four-operation formula retains its literal f/g mixture for discussion in the guide.',differences={
1188:(r'one in\inserted{to} another','the typescript reads as our transcription','The dense small handwritten to is visible above and after in, giving into; it is absent from the witness.'),
1190:('made out of manifolds','the typescript reads as our transcription','The f of of is fully visible in the typed line.'),
1198:('into that expressing','the typescript reads as our transcription','The o of into is fully visible in the typed line.'),
1199:(r'\deleted{some natural}\inserted{mutal}','our transcription corrected','The source cancels some natural and replaces it with the clear literal word mutal. The witness natural fails to apply that replacement.'),
1201:(r'$P_X$- and $P_Y$-','the typescript reads as our transcription','Both hyphens are at the main baseline, outside the subscripts. The witness raises them onto X and Y.')
})
