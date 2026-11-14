from review_root import review

k='ps_134-2_024'
review(k,changes=[
    (r'\mspage{6} \margin{10}',r'\margin{6} \mspage{\hand{10}}','The left 6 and centered 10 are handwritten; their positions identify the centered current folio as 10.'),
    (r'\overset{i}{\underset{\hand{l}}{*}}',r'\overset{i}{\underset{\over{1}{\ell}}{*}}','The lower index of the first composition symbol has a typed 1-shaped base with a diagonal handwritten ell correction.'),
    (r'\underline{C}_{n} \to \underline{C}_{n+1}',r'\underline{C}_{n} \hand{\to} \underline{C}_{n+1}','The arrow of the tower functor is drawn by hand.'),
    (r'\margin{\unsure{NB that $\overset{i}{\underset{\ell}{*}}$ is of order $\ell$ is heuristically clear, but will require a proof none the less}}',r'\margin{\unsure{\uline{NB} that $\overset{i}{\underset{\ell}{*}}$ is of order $\ell$ is heuristically clear, but will require a proof none the less!}}','The enlarged marginal note has an underlined NB and a terminal exclamation mark. The reading/status of the hatched note remains uncertain overall.'),
    (r'standar\unsure{\over{t}{d}} fiber',r'standar\over{t}{d} fiber','The pen d replacing the terminal typed t is clear in the first occurrence.'),
    (r'\unsure{\over{k}{h}}aving',r'\over{k}{h}aving','The pen h is clearly written over the typed k in kaving.'),
    (r'standar\unsure{\over{t}{d}} f\unsure{\over{u}{i}}ber',r'standar\over{t}{d} f\over{\unsure{u}}{i}ber','The second d correction and the pen i are clear; the obscured underlying vowel of fiber remains doubtful.'),
    (r'\inserted{system of}',r'\inserted[typed]{system of}','System of is typed above the line, with a handwritten insertion curve.'),
    (r'X \mapsto F_{i}(X)',r'X \hand{\mapsto} F_{i}(X)','The mapping arrow in the functor display is handwritten.'),
    (r'F_{i}(X) \rightrightarrows F_{i-1}(X)',r'F_{i}(X) \hand{\rightrightarrows} F_{i-1}(X)','The pair of source-target arrows is hand-drawn.'),
    (r'the same \unsure{letters}',r'the same \over{\unsure{f}}{l}etters','The first letter of letters is a handwritten looped l over a typed letter plausibly f; the old letter remains doubtful, while etters is legible.'),
    (r'D_{i-1} \rightrightarrows D_{i}',r'D_{i-1} \hand{\rightrightarrows} D_{i}','The transposed source-target arrows are drawn by hand.'),
    (r'cel\xout{\unsure{lex}}ls',r'cell\unsure{\over{e}{s}}\xout{\illegible{1}}','The crop shows typed cell followed by an overwritten e-like letter and a final x-struck character; it does not show an additional live ls after the strike. The ambiguous replacement is retained as s with a doubt, and the final underletter is illegible.'),
    (r'\hand{$I=$}$D_{1}$',r'\inserted[typed]{$I=$}$D_{1}$','The interlinear I= has the rigid serifed typewriter forms and is typed, not penned; the underlying D_1 remains live.'),
    (r'one point $\rightrightarrows D_{1} = I$',r'one point $\hand{\rightrightarrows} D_{1} = I$','The endpoint pair of arrows is handwritten.')
],doubts={'unsure':[
    (r'\unsure{e}','doubt retained','The terminal e of infinite is at the clipped right edge and is not fully visible.'),
    (r'\unsure{\uline{NB} that $\overset{i}{\underset{\ell}{*}}$ is of order $\ell$ is heuristically clear, but will require a proof none the less!}','doubt retained','Rotation recovers the underlined NB and final exclamation, but the crossing pencil hatching and some small strokes prevent a completely secure reading/status judgment.'),
    (r'\unsure{notion of an}','doubt retained','The cancellation preserves many letters but not enough to resolve the first word securely beneath all x strokes.'),
    (r'\unsure{\hand{$\infty$}}','doubt retained','The infinity sign is clear as a symbol, but its relation to the two overstruck marks above and its typed/pen provenance remain uncertain.'),
    (r'\over{t}{d}','doubt resolved','The terminal typed t and superposed pen d can be distinguished.'),
    (r'\over{k}{h}','doubt resolved','The k arms remain visible beneath the taller pen h.'),
    (r'\over{t}{d}','doubt resolved','The second correction has the same clear d over the typed terminal t.'),
    (r'\over{\unsure{u}}{i}','doubt retained','The final i is clearly penned, while the blacked underlying vowel remains uncertain.'),
    (r'\unsure{though}','doubt retained','Though is plausible below indeed, but the overlaid middle and final strokes remain inseparable.'),
    (r'\unsure{balls}','doubt retained','The old word below cells is heavily blotted; the reading balls cannot be established from all its letters.'),
    (r'\over{\unsure{f}}{l}etters','doubt retained','The live l is handwritten and the remaining etters clear. The typed underletter, plausibly f, is the actual remaining uncertainty.'),
    (r'cell\unsure{\over{e}{s}}\xout{\illegible{1}}','doubt retained','The printed sequence and overlaid pen strokes do not support the original extra live ls. The uncertain e-to-s replacement and unreadable final overstrike are recorded without inventing a suffix.')
],'illegible':[]},notes=[
    'The upper-left 6, centered 10 and lower-left 24 are handwritten. The current centered folio is 10; both upper numbers are retained.',
    'The marginal note has underlined NB and ends less!; its overall reading/cancellation status remains doubtful because the pale zigzag hatching crosses the words.',
    'The first composition symbol has a typed 1-shaped lower index overwritten with a handwritten ell. The tiny extra mark by the upper i does not establish another independent index.',
    'Resolved the d-over-t and h-over-k corrections. The infinity provenance, first cancelled phrase, old vowel in fiber, balls, old first letter of letters, and final cell-word overprint remain marked where uncertain. No changed reading was inferred merely from the expected word.',
    'The tiny marks by to and structures do not securely establish added letters or deletion of the live final s; the typed words are preserved.',
    'The line across on the belongs to the curved insertion mark for the typed interlinear system of; on the remains live.'
],summary='Both halves and six enlarged/rotated crops reviewed. Restored folio positions, pen-arrow provenance, typed system of and I= insertions, and two d corrections plus h over k. Narrowed the letters uncertainty and corrected the unsupported live ls in the cell-word transcription, retaining the unresolved overwrite. Section 5 ends before handwritten section 6; the latter starts the cellular representation argument.',differences={
    206:(r'\hand{(${}^{10}$)} ... \margin{\unsure{\uline{NB} that $\overset{i}{\underset{\ell}{*}}$ is of order $\ell$ is heuristically clear, but will require a proof none the less!}}','our transcription corrected','The marginal composition index is ell, not the witness 2; the underlined NB and terminal exclamation are also on the scan. Some handwriting and the hatching status remain doubtful.'),
    208:(r'standar\over{t}{d} fiber products','our transcription corrected','The author corrects t to d by hand; fiber products remains two words without the witness hyphen. The overprint doubt is resolved.'),
    209:('involved still less lost','the typescript reads as our transcription','There are no commas around still less lost in the typed line; the witness supplies them.'),
    210:(r'\hand{6.}','the typescript reads as our transcription','The handwritten section number 6 is visible at the left of In the outline.'),
    211:('','the arXiv text adds','The descriptive topological-model heading is absent from the scan, which has only the handwritten section number.'),
    218:(r'the same \over{\unsure{f}}{l}etters','our transcription corrected','No comma follows letters on the scan. The word begins with a pen l over an uncertain typed letter, now recorded more precisely.'),
    219:('vou','the typescript reads as our transcription','The printed composition is vou with a small typed o between v and u, not the witness centered dot.'),
    222:(r'unit segment \inserted[typed]{$I=$}$D_{1}$ into','our transcription corrected','The scan retains D_1 and has a typed interlinear I= before it. The witness drops the identification with D_1; the initial claim that I= was handwritten is corrected.')
})
