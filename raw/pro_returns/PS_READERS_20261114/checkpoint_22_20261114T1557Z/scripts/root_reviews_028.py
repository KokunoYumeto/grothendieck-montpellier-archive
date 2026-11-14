from review_root import review

k='ps_134-2_028'
review(k,changes=[
    (r'\mspage{\deleted{8} \hand{14}}',r'\mspage{\deleted{\hand{8}} \hand{14}}','Both the old cancelled 8 and its replacement 14 are pen numbering; the left 8 remains a separate marginal number.'),
    (r'the\unsure{amalgamated|amalgamated}',r'theamalgamated','The two words are typed together without an interword space. The duplicate alternative in the initial doubt does not reflect a word-reading ambiguity.'),
    (r'$X_i \simeq D_{n(i)}$',r'$X_i \hand{\simeq} D_{n(i)}$','The comparison sign is drawn by hand.'),
    (r'f_i : K_i \simeq \underline{J}_{n(i)}',r'f_i : K_i \hand{\simeq} \underline{J}_{n(i)}','The displayed equivalence sign is handwritten.'),
    (r'standar\unsure{\over{t}{d}}ness',r'standar\over{t}{d}ness','The old typed t and pen d are distinguishable in standardness.'),
    (r'standar\unsure{\over{t}{d}} ordered',r'standar\over{t}{d} ordered','The second t-to-d pen correction is clear.'),
    (r'$X\amalg_Z Y$',r'$X\hand{\amalg}_Z Y$','The amalgamation sign is handwritten.'),
    (r'\inserted{however}',r'\inserted[typed]{however}','However is typed above the line, with a handwritten insertion curve.'),
    (r'\xout{\unsure{insist}}',r'\xout{insist}','The cancelled word insist is legible beneath the typewriter x strokes.'),
    (r'\margin{\unsure{(13!)}}',r'\margin{(13!)}','The first marginal reference reads (13!), not B1.'),
    (r'\margin{* This is \unsure{obviously} false, see P.S. p.12}',r'\margin{\unsure{* This is obviously false, see P.S. p.12}}','The word obviously is clear. The broad pencil hatching leaves the status of the note uncertain, so the doubt is retained at the note level rather than attached to that word.'),
    (r'\uline{all categories $\underline{C}_n$}',r'\uwave{all categories $\underline{C}_n$}','The author underlines the phrase with a conspicuously wavering pen stroke, not a straight rule.'),
    (r'\xout{\illegible{1}} \margin{(13!)} are stable',r'\xout{\illegible{1}} \inserted{(13!))} are stable','The second (13!) call is written above the body line, followed by a closing parenthesis for the preceding group; it is not an independent margin note.'),
    (r'$\underline{C}_n\to C$',r'$\underline{C}_n\hand{\to} C$','The first functor arrow is handwritten.'),
    (r'$\underline{C}_\infty\to C$',r'$\underline{C}_\infty\hand{\to} C$','The limiting functor arrow is handwritten.'),
    (r'\inserted{\unsure{for)}}',r'\inserted{for}','The interlinear word is for. The apparent closing parenthesis is the curved insertion mark, not a printed character.'),
    (r'f,g : K \rightrightarrows F_i',r'f,g : K \hand{\rightrightarrows} F_i','The pair of arrows in condition A is hand-drawn.'),
    (r'$h: K\to F_{i+1}$',r'$h: K\hand{\to} F_{i+1}$','The filler arrow is handwritten.')
],doubts={'unsure':[
    (r'\over{\unsure{4}}{8}','doubt retained','The replacement section number is 8; the cancelled earlier digit remains obscured.'),
    ('theamalgamated','doubt resolved','The word letters are clear and the typewriter leaves no separating space after the.'),
    (r'\over{t}{d}','doubt resolved','The first pen d and underlying t are clear.'),
    (r'\over{t}{d}','doubt resolved','The second pen d and underlying t are likewise clear.'),
    (r'\xout{insist}','doubt resolved','The cancelled letters spell insist.'),
    ('(13!)','doubt resolved','The marginal digits are 13 followed by an exclamation mark.'),
    ('obviously','doubt resolved','The enlarged margin clearly reads obviously. A separate note-level doubt records uncertainty about the hatching status.'),
    (r'\inserted{for}','doubt resolved','For is clear; the following curve is its insertion pointer.')
],'illegible':[
    (r'\deleted{\illegible{1}}','illegible retained','The first scribbled old text after the all-categories phrase is not recoverable.'),
    (r'\xout{\illegible{1}}','illegible retained','The underlying typed cancellation immediately after that scribble remains unreadable.'),
    (r'\xout{\illegible{1}}','illegible retained','The crossed word before awkward cannot be securely reconstructed from the remaining letter fragments.'),
    (r'\over{\illegible{1}}{9}','illegible retained','The old section digit under the penned 9 is blacked out.'),
    (r'\xout{\illegible{1}}','illegible retained','The two x impressions before h in B conceal the earlier characters; no word is supplied.')
]},notes=[
    'The centered current folio is handwritten 14; the preceding crossed 8 and separate upper-left 8 are retained, as is the lower-left 28.',
    'The new section numbers 8 and 9 are clear pen additions; their old digits remain doubtful or illegible.',
    'The line has theamalgamated with no interword space, which remains in the diplomatic source.',
    'The epsilon, membership relation and braces are handwritten, whereas the plus/minus-one expression is typed. The existing separation of these layers is retained.',
    'Both d-over-t corrections in standardness and standard are clear and their doubts resolved.',
    'The word obviously and reference (13!) are clear. The broad hatching still makes the note status doubtful. Its exact P.S. p.12 wording is retained.',
    'The word above passing is for; its final curve belongs to the insertion mark.',
    'Insist is recovered. The two dense cancellations after C_n, the word before awkward, and the undercharacters before h remain marked.'
],summary='Both halves and nine enlarged details inspected. Resolved the joined theamalgamated, both d corrections, insist, (13!), obviously and for; preserved the note-status doubt. Corrected the typed provenance of however, restored the second call to its body position and its closing parenthesis, and marked all visible pen arrows. Section 8 ends before the handwritten 9; the retraction of its claimed stability remains explicit.',differences={
    281:(r'$S_j^{\hand{\varepsilon}}$ and $\hand{\varepsilon\in\{}\pm1\hand{\}}$','the typescript reads as our transcription','The source uses handwritten epsilon, not the witness xi.'),
    284:(r'$K_i\hand{\cap}K_{i\prime}$','the typescript reads as our transcription','The handwritten sign is intersection, not an arrow; the statement concerns the common closed subposet.'),
    288:('to exclude final element','the typescript reads as our transcription','There is no the before final element in the typed line.'),
    289:(r'\margin{\unsure{* This is obviously false, see P.S. p.12}}','our transcription corrected','The scan wording says obviously false and points to P.S. p.12; it does not contain the witness expanded discussion of n<=1 and section 18. The word is resolved, but the hatching status remains doubtful.'),
    290:('(13!)','our transcription corrected','The first left-margin reference is visibly (13!).'),
    291:(r'\inserted{(13!))}','our transcription corrected','The second call belongs above the body line at the end of the all-categories parenthesis; the initial transcription incorrectly treated it as a separate margin note.'),
    292:(r'\uwave{all categories $\underline{C}_n$}','our transcription corrected','The full all-categories assertion is present with a wavy underline and asterisk. The witness omits that assertion rather than preserving it with its marginal retraction.'),
    293:(r'between them ...)\hand{(13!)}.','the typescript reads as our transcription','The repeated handwritten call is visible before the final full stop.'),
    296:(r'\inserted{for}','our transcription corrected','The penned word for is clear; the apparent parenthesis was an insertion curve. The witness does not include the word.'),
    297:(r'\deleted{therefore}','the typescript reads as our transcription','Therefore is crossed out in pen but remains live in the witness.'),
    298:(r'\inserted{for this}','the typescript reads as our transcription','For this is the handwritten replacement above the cancelled therefore.'),
    302:(r'with $i\in\underline{N}$, \hand{(}and','the typescript reads as our transcription','The handwritten opening parenthesis before and is visible and absent from the witness.')
})
