from review_root import review, macro_occurrences, TEXT

k='ps_134-2_018'
review(k,changes=[
    (r'\mspage{5}',r'\mspage{\hand{5}}','The centered folio5 is written by hand.'),
    (r'\margin{\unsure{3.}} \hand{3.}',r'\hand{\S 3.}','The left mark is a handwritten section sign beside the handwritten3, rather than another numeral3.')
],doubts={'unsure':[(r'\S','doubt resolved','The left mark has the two-loop shape of a section sign, matching the section sign at the start of the letter.'),(r'\unsure{|}','doubt retained','The small stroke after explicit is not secure enough to identify as a separate spacing mark.')],'illegible':[]},notes=[
    'The upper-left3) and centered5 are handwritten; both are preserved, with the centered folio now explicitly marked hand.',
    'The lower-left18 is handwritten and remains a marginal folio.',
    'The small marks around The, One and The other do not establish different words; their typed readings are retained.',
    'Category remains legible despite the overtyped stroke; no different letter is supplied.',
    'The small separator after explicit remains doubtful.',
    'The curve beneath down belongs to the handwritten notation/placement stroke beneath the preceding labelled star; it adds no separate word.',
    'The left mark is a section sign, not a second3; it is now joined with the handwritten section number.',
    'Enlargement shows the terminal period after call(6) is handwritten. The dark beginning of the left parenthesis does not establish a separate additional period.'
],summary='Both halves and enlarged into/call(6) crops reviewed. Restored the handwritten folio and resolved the section sign. Typed comments and with respect to differ from witness contents and with the respect to. Quillen’s is the author’s handwritten replacement of your; one separator doubt remains.',differences={
95:('with respect to','the typescript reads as our transcription','The typed line has with respect to, without the witness extra the.'),
96:('Still some comments','the typescript reads as our transcription','The source letters clearly read comments, whereas the witness reads contents.'),
97:(r'\deleted{your}','the typescript reads as our transcription','A horizontal handwritten stroke cancels your; arXiv prints it as live text.'),
98:(r"\inserted{Quillen's}",'the typescript reads as our transcription','The handwritten replacement above the line reads Quillen’s; the witness retains the cancelled your.'),
107:('','the arXiv text adds','The source has only the handwritten section number before I thought; the descriptive section heading is absent.')
})

k='ps_134-2_019'
review(k,changes=[
    (r"\mspage{5'}",r"\mspage{\hand{5'}}",'The upper folio5-prime is handwritten.'),
    (r'\hand{,} - \hand{Alexander.}',r'\hand{,} \over{-}{-} \hand{Alexander.}','The dash before the handwritten signature has been heavily retraced by pen over a typed dash.'),
    (r'\mspage{19}',r'\mspage{\hand{19}}','The lower-left19 is pencil handwriting.')
],doubts={'unsure':[],'illegible':[]},notes=[
    'The head folio is handwritten5-prime. Its top stroke and lower curve distinguish5 from the arXiv marker3-prime.',
    'Too is legible as typed despite the small dark mark over its vowel; no additional character is inferred.',
    'The dash is a typed stroke heavily retraced by hand; both layers are now encoded.',
    'The remaining upper and lower halves carry only reverse-side show-through; no forward-facing body text is omitted.'
],summary='Both halves viewed, including the largely blank reverse-show-through lower half. Restored handwriting on both folios and the pen retracing of the dash. The page is numbered5-prime, not the witness3-prime. No doubtful reading is needed.',differences={
118:(r'Very cordially yours\hand{,}','the typescript reads as our transcription','A handwritten comma follows yours on the scan and is absent from the witness.'),
119:(r'Very cordially yours\hand{,} \over{-}{-}','our transcription corrected','The visible dash is retraced by hand over typing; the witness omits the dash as well as the comma.'),
120:(r'\hand{Alexander.}','the typescript reads as our transcription','The handwritten signature and terminal period appear clearly on the source page; the witness omits the signature.'),
121:(r"\mspage{\hand{5'}}",'our transcription corrected','The folio is clearly5-prime and handwritten; the arXiv marker labels it3-prime.'),
122:(r'\mspage{\hand{19}}','our transcription corrected','The lower-left pencil folio19 is visible and now marked hand; the witness has no corresponding archive folio.')
})
