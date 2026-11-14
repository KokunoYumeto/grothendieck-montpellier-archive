from review_root import review

k='ps_134-2_021'
review(k,changes=[
    (r'\mspage{\hand{4}}',r'\mspage{\hand{\unsure{7|4}}}','The folio has superposed strokes: an upper 7-like form over a 4-like lower crossbar. No separate prime is visible; the final numeral remains uncertain.'),
    (r'F_{i} \to F_{i+1}',r'F_{i} \hand{\to} F_{i+1}','The degeneration-map arrow is drawn by hand.'),
    (r'\unsure{\hand{)}}',r'\hand{)}','The right parenthesis around i+1 is clearly present and handwritten.'),
    (r'\inserted{the real}',r'\inserted[typed]{the real}','The words the real are typed above the line; the curved placement stroke is handwritten.'),
    (r'\unsure{the|thu}',r'thu','The last typed letter is visibly an open u, not e; the source spelling thu is preserved.'),
    (r'\unsure{\over{w}{W}}',r'\over{w}{W}','The small typed w is retraced and enlarged by hand into a capital W.'),
    (r'\unsure{\hand{!}}',r'\hand{!}','The terminal exclamation mark is a clear handwritten upright stroke and dot.'),
    ('precise definition of\ndescription','precise definition or\ndescription','The final letter of the typed word is r: the scan reads definition or description.'),
    (r'C_{0} \to C_{1} \to C_{2} \to \ldots \to C_{n} \to C_{n+1} \to \ ,',r'C_{0} \hand{\to} C_{1} \hand{\to} C_{2} \hand{\to} \ldots \hand{\to} C_{n} \hand{\to} C_{n+1} \hand{\to} \ ,','All six chain arrows are hand-drawn; the terminal arrow is followed by blank space and a comma, not another ellipsis.'),
    (r'\xout{xxxxxxxxxx}',r'\xout{\unsure{"universal"}}','The cancelled word before category has visible letters matching universal and an opening quotation mark; the obscured ending/closing quote remains doubtful rather than being represented by invented ten x characters.')
],doubts={'unsure':[
    (r'\hand{)}','doubt resolved','Both parentheses around i+1 are visible handwritten curves.'),
    (r'\unsure{x}','doubt retained','The small cancelled character before picture is heavily blacked and cannot be securely recovered.'),
    (r'\unsure{\over{.}{,}}','doubt retained','The final comma is handwritten; whether a typed period lies underneath its head remains uncertain.'),
    (r'\unsure{a}','doubt retained','The blotted character immediately before special is too obscured to recover as a with confidence.'),
    ('thu','doubt resolved','Enlargement shows a rounded open u after th, not the closed cross-stroked e of the neighbouring words.'),
    (r'\over{w}{W}','doubt resolved','The lower typed w is visible beneath the taller pen strokes forming W.'),
    (r'\unsure{throwed}','doubt retained','The cancellation obscures the final typed letters of throwed; the handwritten replacement threw is clear.'),
    (r'\hand{!}','doubt resolved','The exclamation mark at the end of the paragraph is a definite pen stroke with a separate dot.')
],'illegible':[
    (r'\illegible{1}','doubt retained','The overstruck cluster at the cropped right end of cons remains unreadable.'),
    (r'\illegible{1}','doubt retained','The short cancelled cluster before the opening quotation mark of infinity-groupoids is obscured by dense crossing strokes.'),
    (r'\illegible{1}','doubt retained','The single dense typewriter overstrike after chose does not disclose its underlying character.')
]},notes=[
    'The centered folio contains superposed 7-like and 4-like strokes; a 7|4 doubt now replaces the overconfident 4. No independent prime is visible.',
    'Both parentheses around i+1 are handwritten and clear; the uncertainty on the right parenthesis is resolved.',
    'The crossed character stays doubtful. The replacement the real is typed interlinearly. The handwritten comma is clear, but an underlying typed period remains doubtful.',
    'The cancelled character before special and the two cancelled clusters remain doubtful or illegible. The word before structure reads thu with a clear u.',
    'The enlarged W is handwritten over the typed w; the terminal exclamation mark is handwritten and certain.',
    'The lower-left archive number 21 is handwritten and already marked correctly.'
],summary='Both halves and five enlarged crops reviewed. Corrected typed/handwritten provenance of the real, resolved closing parenthesis, thu, W and exclamation; restored definition or description and handwritten arrows. The overwritten folio and the cancelled universal quotation remain explicitly doubtful. Section 4 ends and section 5 begins near the bottom.',differences={
    142:(r'every i-object the \hand{(}i+1\hand{)}-object','our transcription corrected','The scan has singular i-object and two handwritten parentheses around i+1. The witness adds a plural s and drops the parentheses; the right parenthesis doubt is now resolved.'),
    144:(r'2-category\hand{,} say','the typescript reads as our transcription','A handwritten comma is present immediately after 2-category.'),
    153:(r'$\underset{1}{*}$','the typescript reads as our transcription','The 1 is typed directly below the star-like composition mark. The witness uses a side subscript; the mathematical index is the same.'),
    154:('ternary etc structure','the typescript reads as our transcription','There is no full stop after etc in the typed sentence; the witness supplies one.'),
    156:('all these operations','the typescript reads as our transcription','The scan clearly reads these, including its terminal se, rather than the witness the.'),
    158:('','the arXiv text adds','The scan has only the corrected section number 5 before It is about time; Jumping over the abyss is an added descriptive heading.'),
    160:(r'C_{n+1} \hand{\to} \ ,','our transcription corrected','The handwritten terminal arrow is followed by space and the typed comma. The witness inserts an ellipsis not on the page; the arrow provenance is now marked.'),
    161:(r'\margin{$\overset{i}{\underset{1}{*}}$} ... \margin{$\overset{i}{\underset{2}{*}}$}','the typescript reads as our transcription','Both stacked handwritten composition symbols are clearly present in the left margin and omitted by the witness.')
})
