from review_root import review
k='ps_134-2_036'
review(k,changes=[
(r'\mspage{12}',r'\mspage{\hand{22}}','The centered manuscript folio is handwritten 22; the separate upper-left pencil 12 remains marginal.'),
(r'\hand{(21)}',r'\hand{(\unsure{21|20}!)}','The exclamation mark is secure. The thick second numeral favors 1 but cannot be securely distinguished from 0; a second reader independently retained that uncertainty.'),
(r'\margin{\unsure{Maybe f th} it is safer to give moreover the $\underline{C}_o$ subcategory}',r'\margin{\unsure{Maybe \unsure{f th} it is safer to give moreover the $\underline{C}_o$ subcategory}}','Maybe and the following sentence are readable. The extra cluster after Maybe may be an annotation or reference, rather than letters f th, and remains uncertain. The outer doubt records the uncertain cancellation status of the crossing pencil hatching.'),
(r'coherator, \xout{\illegible{1}}',r'coherator, \xout{acting}','The cancelled word acting is readable beneath its x impressions.'),
(r'from mere irredundancy',r'from \over[typed]{h}{m}ere irredundancy','The first cell contains a typed m over a typed h; the old h ascender remains visible.'),
(r'I would like at least',r'I would like a\over{\illegible{1}}{t} least','The t is retraced in pen over a dense earlier letter that cannot be recovered securely. The a remains a live typed letter.'),
(r'\unsure{a\xout{n}|an} \inserted{later}',r'a\xout{n} \inserted[typed]{later}','The n of an is visibly struck, and later is typed interlinear text whose pen curve locates it before elaboration.'),
(r'\unsure{23.2|25.2}',r'23.2','The second digit has two open curves of 3; the date reads 23.2, without a final full stop.'),
(r"\margin{\unsure{(1')}}",r'\margin{\textcircled{(13!)}}','The marginal call is 13! inside a larger circle.'),
(r"\hand{\unsure{(1')}}",r'\hand{(13!)}','The interlinear pen call also reads 13!, with its first strokes crossing the insertion curve.'),
(r'$\underline{C}_o \to \underline{C}_n$',r'$\underline{C}_o \hand{\to} \underline{C}_n$','The inclusion arrow is hand drawn.'),
(r'$\underline{C}_\infty \to C$',r'$\underline{C}_\infty \hand{\to} C$','The functor arrow is hand drawn.'),
(r'\xout{\illegible{1}} yesterday',r'\xout{next} yesterday','The cancelled word before yesterday reads next.')
],doubts={'unsure':[
(r'\unsure{r}','doubt retained','The right edge clips the end of after; r remains contextually likely but not fully visible.'),
(r'Maybe \unsure{f th}','doubt narrowed','Maybe is legible. The following cluster remains unresolved and may be a reference mark rather than lexical f th; an independent reading agrees.'),
(r'a\xout{n} \inserted[typed]{later}','doubt resolved','The n is visibly cancelled. The typed later is inserted after the surviving a, not before an as in the witness.'),
('23.2','doubt resolved','The date visibly contains 3, not 5.'),
(r'\unsure{\over{-}{:}}','doubt retained','A dash-shaped stroke is visible, but the superposed punctuation cannot be separated securely from the interlinear t in practically; the colon correction remains doubtful.'),
(r'\textcircled{(13!)}','doubt resolved','The marginal digits are 13 followed by an exclamation, all inside a surrounding circle.'),
(r'\hand{(13!)}','doubt resolved','The body call repeats 13! beneath the insertion curve.')
],'illegible':[
(r'\xout{acting}','illegible resolved','All letters of acting are distinguishable under the x impressions.'),
(r'\xout{next}','illegible resolved','The cancelled word next is readable.')
]},notes=[
'The pencil 12 and 36 are marginal numbers. The centered current folio is pen 22.',
'The note clearly begins Maybe, and its following sentence reads it is safer to give moreover the C_o subcategory. The intervening extra cluster remains unresolved. Pencil hatching leaves cancellation status uncertain.',
'The n of an is cancelled. The replacement order is a later elaboration, with later typed above the line and placed by a pen curve.',
'The date reads 23.2, rather than the witness 25.2.',
'The punctuation after products remains doubtful because it overlaps practically below. Both later calls are 13!; the left one is surrounded by an additional circle.',
'Mere begins with typed m over h. In at least the t is penned over unreadable earlier matter. Heuristic, least in the Brown parenthesis, and whose have doubled or displaced typewriter impressions but their live words remain legible; their overlapping impressions do not supply a securely separable additional word or changed letter.',
'The two cancelled words read acting and next.'
],summary='Both halves and enlarged details, including the rotated marginal note, inspected. A second reading confirms the unresolved cluster after Maybe and the uncertain second digit of the body call. Corrected folio 22, date 23.2, both 13! calls, typed later, cancelled n, and recovered acting and next. The clipped final r and overprinted punctuation remain marked. This closes section 13 and the Quillen letter.',differences={
477:(r'\hand{(\unsure{21|20}!)}; Maybe \unsure{f th} it is safer to give moreover the $\underline{C}_o$ subcategory','our transcription corrected','The source note is much shorter than the witness paraphrase. Its first word is secure; the extra cluster and hatching status remain doubtful. The body call has a separate exclamation and uncertain second numeral.'),
482:(r'a\xout{n} \inserted[typed]{later} elaboration','our transcription corrected','The image shows n cancelled and later typed above the line, producing a later elaboration rather than the witness later an elaboration.'),
484:(r'\hand{Alexander}','the typescript reads as our transcription','The handwritten signature is clearly present and omitted by the witness.'),
485:('PS (23.2)','our transcription corrected','The visible second digit is 3. The witness 25.2. changes both the digit and punctuation.'),
488:(r'(by construction \inserted[typed]{practically})','the typescript reads as our transcription','Practically is typed above the line and placed by a curved pen mark. No comma follows construction on the source.'),
489:(r'\margin{\textcircled{(13!)}}; \hand{(13!)}','our transcription corrected','Both calls read 13!; the left one is separately circled. They are absent from the witness.')
})
