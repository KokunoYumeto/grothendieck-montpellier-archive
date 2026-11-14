from review_root import review

k='ps_134-2_020'
review(k,changes=[
    (r'\margin{\unsure{1}}',r'\margin{1}','The isolated upper-left pen numeral is clearly 1.'),
    (r'\mspage{6}',r'\mspage{\hand{6}}','The centered folio 6 is handwritten.'),
    (r'F_i \rightrightarrows F_{i-1}',r'F_i \hand{\rightrightarrows} F_{i-1}','Both parallel source-target arrows are drawn by hand.'),
    (r'inv_i : F_i \to F_i',r'inv_i : F_i \hand{\to} F_i','The inversion-map arrow is handwritten.'),
    (r"f : C \to C'",r"f : C \hand{\to} C'",'The arrow between C and C-prime is drawn by hand.')
],doubts={'unsure':[
    ('1','doubt resolved','The upper-left numeral has a single ascending stem and top hook, with no competing letter.'),
    (r'\unsure{s}','doubt retained','The terminal handwritten stroke after involution is crowded against the cropped right edge; the reading s remains uncertain.'),
    (r'\unsure{that}','doubt retained','The very small inserted word has overlapping upright strokes and loops; enlargement does not securely distinguish all letters of that.'),
    (r'\unsure{yiel}','doubt retained','The typed cluster before the line-end hyphen is overprinted. The intended yiel is plausible, but its full underlying sequence cannot be read confidently.')
],'illegible':[
    (r'\illegible{1}','doubt retained','The typewriter cancellation after supplement shows fragments resembling by th, but the x overstrikes prevent a secure complete reading or word count.')
]},notes=[
    'The centered 6 and lower-left 20 are handwritten. The faint upper-left mark is clearly 1 and its doubt is resolved.',
    'All inversion vee marks in the two expressions are handwritten; the vee on the right of the equality is cancelled by a diagonal pen stroke and remains encoded as deleted.',
    'The small insertion before we will remains doubtful after enlargement; that is retained as the tentative reading.',
    'The final mark after involution is handwritten but clipped and congested; the tentative s remains marked.',
    'The line-end yiel cluster is visibly overprinted; the doubt remains rather than imposing the witness wording.',
    'The membership sign between i and N is drawn by hand; the existing hand macro is retained.',
    'The cancellation after supplement is typed with x characters; traces suggest by th but do not securely restore the whole expression.',
    'Faint diffuse reverse-side text and marginal traces were distinguished from the strong forward-facing pen marks; no additional readable body text was found.'
],summary='Both halves and enlarged insertion/overstrike crops reviewed. Resolved the upper-left 1, marked handwritten folio 6 and three arrow occurrences. Four uncertain readings remain. The author begins section 4 and retracts the treatment of inversions as skeletal structure. The source still says i=1 for the formal maps s_o,t_o from F_0; this index anomaly is preserved.',differences={
    126:(r'\margin{\S 4.}','the typescript reads as our transcription','The scan has a handwritten section sign and 4, without the descriptive heading added by the arXiv edition.'),
    133:(r'And even\hand{,} assuming','the typescript reads as our transcription','A small handwritten comma follows even on the scan; the witness omits it.')
})
