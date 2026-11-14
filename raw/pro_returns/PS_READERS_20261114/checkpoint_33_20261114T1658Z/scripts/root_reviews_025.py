from review_root import review

k='ps_134-2_025'
review(k,changes=[
    (r"\mspage{\unsure{6'11|§11}}",r"\mspage{\unsure{\deleted{\hand{6'}}}\hand{11}}",'The current handwritten folio is clearly 11. The preceding crossed mark plausibly reads 6-prime but its original strokes remain doubtful.'),
    (r'is \unsure{what} we',r'is \hand{what} we','The live word what is clear in pen over faint typed strokes; the full-word reading doubt is resolved and the visible pen layer marked.'),
    (r'\uline{co - $\infty$-groupoid in the category}',r'\uline{co} - $\infty$-\uline{groupoid in the category}','The page has separate underlining below co and below groupoid in the category, with no underline beneath the intervening dash and infinity sign.'),
    (r'$F_*(X)$',r'$F_{\hand{*}}(X)$','The star subscript is handwritten.'),
    (r'\hand{(}Top\hand{)} to \hand{(}Sets\hand{)}',r'\hand{(Top)} to \hand{(Sets)}','The category names as well as their parentheses are penned/retraced in this line.'),
    (r'\deleted{\unsure{the B}}',r'\deleted{\unsure{the D|the B}}','The cancelled capital has a broad right-hand bowl suggesting D, but the strike crosses the position distinguishing D from B; the doubt remains.'),
    (r'\over{\unsure{e}}{c}ells',r'\over[typed]{\unsure{e}}{c}ells','The initial c of cells is a typewriter overprint, with a small displaced typed mark below; the underlying e-like letter remains doubtful.'),
    (r'\unsure{essentially}',r'\over{\unsure{ess}}{ess}entially','The live pen ess and following typed entially are clear. The overwritten type at the beginning remains uncertain; the doubt is confined to that underlying layer.'),
    (r'\over{\unsure{is}}{was}',r'\over[typed]{\unsure{is}}{was}','The live was is typewritten over the earlier letters, not a pen correction; the underlying is remains doubtful.'),
    (r'D_i \rightrightarrows D_{i+1}',r'D_i \hand{\rightrightarrows} D_{i+1}','The displayed pair of arrows is drawn by hand.'),
    (r'\mspage{25}',r'\mspage{\hand{25}}','The bottom-left archive number 25 is handwritten.')
],doubts={'unsure':[
    (r"\unsure{\deleted{\hand{6'}}}\hand{11}",'doubt retained','The current folio 11 is clear; the preceding crossed old numeral is still doubtful.'),
    (r'\unsure{from|frop}','doubt retained','The overprinting obscures the vowel and final stem; from is plausible, but the final descender-like stroke prevents a secure removal of the alternative.'),
    (r'\hand{what}','doubt resolved','The pen w, h, a and t establish the live word what.'),
    (r'\unsure{the D|the B}','doubt retained','The cancelled capital appears D-like, but the horizontal cancellation masks its medial structure.'),
    (r'\over[typed]{\unsure{e}}{c}','doubt retained','The live typed c is clear; its underlying e-like character is not separable from the overprint.'),
    (r'\deleted{\unsure{t}}','doubt retained','The single cancelled character before built is blacked out and remains only tentatively t.'),
    (r'\over{\unsure{ess}}{ess}entially','doubt retained','The remaining uncertainty concerns the old typed beginning, not the live word essentially.'),
    (r'\unsure{+ 23.2. But no longer now -- and I do not really care ! cf. p.10 \S 11}','doubt retained','The wording is substantially recoverable from the full margin and rotated crop, but the crossed hatching leaves the note status and some small strokes uncertain.'),
    (r'\over[typed]{\unsure{is}}{was}','doubt retained','The typed replacement was is clear; the older is-like pair is partly obscured.')
],'illegible':[
    (r'\over{\illegible{1}}{this}','illegible retained','The handwritten this is clear but the faded and overlaid typed word beneath cannot be recovered.'),
    (r'\deleted{\illegible{1}}','illegible retained','The old category designation beneath the inserted C-infinity is fully scribbled out.'),
    (r'\over{\illegible{1}}{c}','illegible retained','The old character at the beginning of the second line of precisely is a solid blot under the correction.')
]},notes=[
    'The current centered folio is handwritten 11; the preceding crossed old numeral, plausibly 6-prime, remains doubtful.',
    'The word after say has multiple typed strokes and a blot. The from/frop doubt is retained.',
    'The cancelled phrase before various appears the D, rather than the initial the B, but the capital is not fully resolved beneath its strike.',
    'The first c of cells is typed over an uncertain e-like character. The blacked single character before built remains doubtful.',
    'The old typed word under the handwritten this remains illegible even in the enlarged crop.',
    'The live pen ess and typed entially are clear; the uncertainty is confined to the old type beneath ess.',
    'Was is a typewriter overprint, with the original is still uncertain. The corrected layer is no longer falsely colored as handwriting.',
    'The dated marginal note retains the wording But no longer now and the reference p.10 section 11. Its pencil hatching does not permit a secure decision about cancellation, so the doubt stays.',
    'The lower-left handwritten 25 is retained and its pen provenance marked.'
],summary='Both scan halves and six enlarged/rotated crops inspected. Resolved current folio 11 and live what; distinguished the typed cells and was overprints, narrowed the essentially doubt, and marked pen category names, star, arrows and archive number. The dated marginal retraction remains marked because its hatching status is unresolved. Section 6 ends before section 7 at the foot.',differences={
    225:('experimenting','the typescript reads as our transcription','The typed word is experimenting, not the witness experiment. The separate earlier from/frop blot remains doubtful.'),
    228:(r'\deleted{\unsure{the D|the B}} various','our transcription corrected','The old phrase is visibly struck and the live word is various. The capital in the cancelled phrase is now recorded as D-like with B retained as an alternative; the witness leaves the as live text.'),
    231:(r'(I believe it is\hand{(!!!)})','the typescript reads as our transcription','The three handwritten exclamation marks in parentheses are visibly added after is and are not included in the witness wording.'),
    232:(r'\margin{\unsure{+ 23.2. But no longer now -- and I do not really care ! cf. p.10 \S 11}}','the typescript reads as our transcription','The witness paraphrases the marginal note as a dated footnote and omits its explicit p.10 reference. The scan wording and unresolved hatching status are preserved.')
})
