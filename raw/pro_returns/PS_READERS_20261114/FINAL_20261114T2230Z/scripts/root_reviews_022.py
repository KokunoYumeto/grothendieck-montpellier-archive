from review_root import review

k='ps_134-2_022'
review(k,changes=[
    ('\\mspage{5}\n\\hand{\\unsure{8}}','\\margin{5}\n\\mspage{\\hand{8}}','The 5 is handwritten at the upper left; the central rewritten folio is clearly 8. Both are retained in their respective roles.'),
    (r'\margin{\unsure{(8) torsors under a group}}',r'\margin{\unsure{(8) torsors under group G}}','The enlarged marginal cue has no article a before group and ends with a separate capital-like G. Its call/final glyph and pencil hatching remain uncertain.'),
    (r'in \xout{\illegible{1}} these',r'in \xout{any of} these','The typed cancellation clearly preserves a-n-y and o-f beneath the x overstrikes.'),
    (r'categories \xout{\illegible{2}}',r'categories \xout{and functors}','Enlargement recovers the two cancelled typed words and functors.'),
    (r'\hand{\unsure{,}} endowed',r'\hand{,} endowed','The separate curved pen stroke after N) is a definite comma.')
],doubts={'unsure':[
    ('8','doubt resolved','The centered folio has two joined loops forming a clear 8 despite retracing.'),
    (r'\unsure{n}','doubt retained','The first letter beneath the typed x is not separable enough to establish n.'),
    (r'\unsure{"}','doubt retained','Closing quote strokes are visible, but the adjacent dense handwritten/cancelled mark remains ambiguous; the original uncertainty is retained rather than silently regularizing the cluster.'),
    (r'\unsure{n}','doubt retained','The second x-overstruck letter after give a remains uncertain.'),
    (r'\unsure{(8) torsors under group G}','doubt retained','Rotated enlargement supports torsors under group followed by a capital-like G, without a; the call, last glyph and status of the pencil hatching remain uncertain.'),
    (',','doubt resolved','The final pen comma is distinct and has the usual curved downstroke.')
],'illegible':[
    (r'\illegible{1}','doubt retained','Still is retraced over a typed word; some middle strokes survive but do not establish the complete underlying word.'),
    (r'\illegible{1}','doubt retained','The typed word following cancelled still at the extreme right is covered by dense overstrikes and clipping.'),
    ('any of','doubt resolved','The lower descender of y and the final of are visible beneath the cancelling x strokes.'),
    ('and functors','doubt resolved','The remaining letter stems and bowls establish and functors across the two words.')
]},notes=[
    'The upper-left 5 and lower-left 22 are handwritten. The centered folio is clearly 8; its doubt is resolved and its centered page-number role is recorded.',
    'The two underletters after a remain doubtful beneath typed x strikes; no grammatical reconstruction is substituted.',
    'Of is written above the right edge by pen with a curved placement mark; the existing handwritten insertion is retained.',
    'The dense cluster after n includes quote-like strokes and an obscured neighbouring mark; it remains doubtful.',
    'The pen word Still overlies the typing; the complete old reading remains illegible after enlargement.',
    'Still and the following overtyped cluster are cancelled, and correspondingly is inserted above. The final punctuation near object and the call is congested; no unsupported period is restored.',
    'Rotated enlargement gives the tentative cue (8) torsors under group G. There is no separate a, and the final capital-like glyph plus pencil hatching remain uncertain.',
    'The two lower typed cancellations are now readable as any of and and functors.',
    'The last-line mark after N) is a clear handwritten comma.'
],summary='Both halves and enlarged quote, Still, marginal cue and two cancellation crops reviewed. Restored upper folio roles, resolved 8 and final comma, and recovered any of / and functors under typed strikes. The marginal cue has no article a and a final G-like glyph, still doubtful. Six doubt marks remain.',differences={
    165:('namely from n-ary to','the typescript reads as our transcription','The scan has from n-ary without the article an supplied by the witness.'),
    166:(r'for the functor\hand{s} one allows','the typescript reads as our transcription','A handwritten final s visibly pluralizes functor; the witness leaves it singular.'),
    168:(r'which commute \deleted{to}\inserted{with} these','the typescript reads as our transcription','To is crossed out and with written above it; the witness retains the superseded preposition.'),
    169:(r'structure \deleted{of} \hand{"}category\hand{,"} \hand{"}groupoid\hand{"} or the like','the typescript reads as our transcription','Of is visibly cancelled and quotation marks added by hand around the two names; the witness prints of live and removes those marks.'),
    172:(r'some kind\hand{s} of inverse limits','the typescript reads as our transcription','The handwritten final s after kind is visible on the scan and absent from the witness.'),
    174:(r'\margin{\unsure{(8) torsors under group G}}','our transcription corrected','This page has a short, partly uncertain marginal cue, not the full classifying-topos paragraph printed at the witness footnote. Enlargement removes the false article a and reveals the final capital-like glyph; the long note must be compared separately with the letter notes.'),
    175:(r'\deleted{still \xout{\illegible{1}}} \inserted{correspondingly} more stringent \inserted{exactness} conditions','the typescript reads as our transcription','The author cancels still and its overtyped continuation, adds correspondingly above, and inserts exactness before conditions. The witness does not apply these revisions.')
})
