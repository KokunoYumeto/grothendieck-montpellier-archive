from review_root import review
k='ps_134-2_055'
review(k,changes=[
(r'\mspage{\hand{39 bis}} \mspage{8}',r'\mspage{\hand{39 bis}} \hfill 8','The handwritten central folio and independent typed upper-right 8 are distinguished.'),
(r'\mspage{\hand{55}}',r'\margin{\hand{55}}','The lower-left number is pencil archive foliation.')
],doubts={'unsure':[],'illegible':[]},notes=[
'The underline stops under the last letter of commutative; it does not continue beneath the closing parenthesis.',
'The central 39 bis and lower-left 55 are handwritten; the upper-right 8 is typed.',
'The lower half is blank apart from the pencil archive number and nontextual specks; no text is omitted.'
],summary='Both halves inspected, including the otherwise blank lower half. Confirmed the underline endpoint, the literal résoud in both occurrences, the unpunctuated Bien cordialement and the typed signature Alexandre. Corrected only the distinct foliation placement.',differences={
876:('Bien cordialement','the typescript reads as our transcription','The salutation has no comma after it.'),
877:('Alexandre','the typescript reads as our transcription','The typed signature is plainly present and omitted by the witness.')
})
k='ps_134-2_056'
loop=r'\tikz[baseline=-.4ex,x=.5em,y=.5em]{\draw (1,1) .. controls (0,1) and (-.1,.8) .. (0,.3) .. controls (.2,0) and (.8,.2) .. (1,0);}'
review(k,changes=[
(r'\margin{\unsure{41}}',r'\mspage{\hand{4\unsure{0|1}}}','The top-center folio begins with a clear 4. The second character has an oval with a heavy vertical retracing; 0 is the better visible reading but 1 cannot be excluded as the underlying or overwritten digit.'),
(r'\margin{(App.9)}I',r'\margin{\hand{(App.9) '+loop+r'}}I','The marginal appendix label and its curved placement bracket are handwritten.'),
(r'\hand{\unsure{-}}',r'\hand{-}','The small pen mark is a definite horizontal dash.'),
(r'\margin{$\times$}',r'\margin{\hand{$\times$}}','The marginal cross is in pencil.'),
(r'\deleted{of chains}',r'\deleted{\unsure{b|o}f chain\unsure{g|s}}','The deletion leaves an ascender-like mark at the first letter and a covered final letter; the initial transcription silently chose standard spelling where the visible old forms remain doubtful.'),
(r'analogies...\hand{)}',r'analogies...\hand{).}','A separate handwritten period follows the closing parenthesis.'),
(r'\mspage{56}',r'\margin{\hand{56}}','The lower-left 56 is pencil archive foliation.')
],doubts={'unsure':[
(r'\hand{4\unsure{0|1}}','doubt narrowed','The first digit 4 is clear; the second is an oval crossed or retraced vertically and remains doubtful.'),
(r'\hand{-}','doubt resolved','The enlarged mark is a short horizontal pen dash, separate from the typed quotation marks.')
],'illegible':[]},notes=[
'The top folio has a clear 4 and an uncertain second digit, visually more like a retraced 0 than a plain 1. Its centered location is restored.',
'The mark after clear is a legible pen dash and is now resolved.',
'Both the closing parenthesis and the following period are penned; the omitted period is restored.',
'The crossed old phrase has uncertain first and last letters. The ascender-like first mark and the covered terminal mark are retained explicitly rather than silently normalized to of chains.'
],summary='Both halves and enlarged folio, theory correction, dash, old phrase and final punctuation inspected. Resolved the dash, retained the folio uncertainty in its second digit, restored the omitted pen period and placement bracket, marked the pencil cross and archive number, and made the cancelled phrase’s letter uncertainties explicit. The source retains nerve functor, corresponds and an explicit, and its handwritten nose-tip and note25 call are present.',differences={
879:(r'\margin{\hand{(App.9)}} with placement bracket','our transcription corrected','The scan has a handwritten appendix label, not the witness descriptive heading.'),
881:('nerve functor','the typescript reads as our transcription','The source has no of the between nerve and functor.'),
884:(r'clear\hand{-}','our transcription corrected','The pen dash is clear and retained; the witness omits it.'),
885:(r'nose\inserted{-tip}','the typescript reads as our transcription','The insertion -tip is visibly penned and absent from the witness.'),
886:('This functor corresponds','the typescript reads as our transcription','The final s of corresponds is typed and clear.'),
888:('an explicit','the typescript reads as our transcription','The article is an, not the witness a.'),
890:(r'\inserted{(25)}','the typescript reads as our transcription','The page has the handwritten reference number; the witness replaces the call by its typeset note.'),
891:(r'\margin{\hand{$\times$}}','our transcription corrected','The pencil cross is present beside the paragraph ending.')
})
