from review_root import review

k='ps_134-2_030'
review(k,changes=[
    (r'\mspage{9}'+'\n'+r'\margin{\S 16}',r'\margin{9}'+'\n'+r'\mspage{\deleted{\hand{9}} \hand{16}}','The upper-left number is 9. The centered folio has a cancelled pen 9 followed by 16; there is no section sign before 16.'),
    ('to any structure of Mr. X',r'to any \over[typed]{\illegible{1}}{s}tructure of Mr. X','The first letter of structure is a typed overprint. Its prior character cannot be recovered securely.'),
    (r'to a X-structure',r'to a X-s\over[typed]{\illegible{1}}{t}ructure','The t in X-structure has an earlier typed impression underneath it; the prior character is retained as illegible.'),
    (r'\underset{\hand{\infty}}{\simeq}',r'\hand{\underset{\infty}{\simeq}}','Both the comparison sign and its infinity subscript are handwritten.'),
    (r'\inserted{his own} \xout{\illegible{1}}',r'\inserted[typed]{his own} \xout{a different}','His own is typed interlinear text; the cancelled wording underneath reads a different.'),
    (r'\inserted{which} \xout{\illegible{1}}',r'\inserted[typed]{which} \xout{but}','Which is a typed insertion above the cancelled typed but.'),
    (r'\xout{\unsure{his pair of functors}}',r'\xout{his pair of functors}','The whole cancelled phrase is legible beneath the x strokes.'),
    (r"won\hand{\unsure{'}}t",r"won\hand{'}t",'The raised curved apostrophe is a clear pen addition.'),
    (r'\margin{\unsure{ta.}} \hand{10.}',r'\margin{\deleted{10.}} \hand{10.}','The old marginal mark is a cancelled handwritten 10., replaced by another 10. slightly above and to its right.'),
    (r'still\hand{;}',r'still\hand{:}','The handwritten punctuation has two aligned dots and no comma tail: it is a colon.')
],doubts={'unsure':[
    (r'\xout{his pair of functors}','doubt resolved','All words of the cancelled phrase are readable.'),
    (r"\hand{'}",'doubt resolved','The apostrophe is clearly a pen stroke.'),
    (r'\margin{\deleted{10.}}','doubt resolved','The cancelled older section number is 10., not ta.'),
    (r'\margin{\unsure{n}}','doubt retained','The small mark beneath One has the shape n, but its attachment or corrective function is not securely indicated. It remains marked rather than silently applied to the printed word.')
],'illegible':[
    (r'\xout{a different}','illegible resolved','The old phrase beneath his own is legible as a different.'),
    (r'\xout{but}','illegible resolved','The three cancelled letters beneath which read but.'),
    (r'\xout{\illegible{1}}','illegible retained','The dense short cancellation after equivalent remains unreadable; the contextual possibility to is not supplied as certain.')
]},notes=[
    'The extra typed m in associati-m-ng remains cancelled. The first s of structure and t of X-structure are typed overprints whose prior characters remain illegible; their typed provenance is explicit.',
    'The line ending conver is clipped at the right edge. The separate pen dash before sely is retained; no hidden terminal letter is supplied.',
    'The right edge shows mathematicia before the next line an,. The resulting duplicated a is preserved rather than silently normalized.',
    'The cancelled a different, but, and his pair of functors are recovered. The short cancellation after equivalent remains illegible.',
    'The apostrophe in wont is visibly handwritten and its doubt is resolved.',
    'The old marginal 10. is crossed out and rewritten. The small n-like mark below One remains uncertain in function and is retained at its anchor.',
    'The mark above pick is an isolated blot without securely readable lettering; no word is inferred from it.',
    'The pencilled archive number 30 is visible at bottom left and remains in the margin.'
],summary='Both halves and enlarged details inspected. Corrected the misplaced folio, typed provenance of his own and which, the pen equivalence sign and apostrophe, the cancelled section number, and colon after still. Recovered three cancelled phrases, retained the clipped right-edge spellings, and recorded the two typed overprints with unrecoverable old characters.',differences={
    340:(r'\hand{\underset{\infty}{\simeq}}','our transcription corrected','The entire comparison symbol is drawn by hand, not only its infinity subscript.'),
    341:(r'\inserted[typed]{his own} \xout{a different}','our transcription corrected','The live words are typed interlinear and the old phrase can be recovered.'),
    342:('to reconciliate','the typescript reads as our transcription','The source visibly says reconciliate; reconcile is the witness wording.'),
    344:(r'\inserted[typed]{which} \xout{but}','our transcription corrected','Which is typed above the cancelled but.'),
    345:(r"won\hand{'}t",'our transcription corrected','The apostrophe is clear and handwritten.'),
    347:('Here however a fifth','the typescript reads as our transcription','There is no comma after however in the source.'),
    348:("U and U'",'the typescript reads as our transcription','No comma follows U in this phrase.'),
    350:(r'\mspage{\deleted{\hand{9}} \hand{16}}','our transcription corrected','The supposed section sign and 16 margin note are actually the centered page folio, preceded by cancelled 9.'),
    351:('10. Now in the long last','the typescript reads as our transcription','Only the numbered opening is present; the descriptive witness heading is not on the scanned page.'),
    353:(r'\margin{\deleted{10.}}','our transcription corrected','The old mark is a cancelled 10., repeated nearby in the live heading.'),
    356:('Or else and more reasonably','the typescript reads as our transcription','There is no comma after else.'),
    357:(r'Another restriction\hand{,} to avoid','the typescript reads as our transcription','The handwritten comma after restriction is present and omitted from the witness.'),
    358:(r'still\hand{:} \inserted[typed]{thus there would be already \deleted{in}}','our transcription corrected','The handwritten sign is a colon. The interlinear words are typed and the final in is cancelled; the witness substitutes a comma.')
})
