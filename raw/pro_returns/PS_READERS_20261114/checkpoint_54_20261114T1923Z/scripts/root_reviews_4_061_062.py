from review_root import review

review('ps_134-4_061',owner='134_4_tail',changes=[
 (r'\over{h}{H}',r'\over[typed]{h}{H}','Enlargement shows regular typewriter serifs and a capital H crossbar over the lowercase h, matching the same overprint on site 41. It is not a freehand capital.'),
 (r'h$_{\unsure{\mathrm{M}}}$',r'h$_{\mathrm{M}}$','The subscript has the two verticals and middle diagonals of a typed capital M. The handwritten for belongs to the following insertion, not to this index.')
],doubts={'unsure':[
 (r'\unsure{\mathrm{l}}','doubt retained','The second character of Fl has an additional diagonal overstrike; its exact final glyph and layer remain uncertain.'),
 (r'\unsure{cf. lemme}','doubt retained','The marginal cf. and initial le are readable, but the remaining abbreviated/wavy strokes do not settle the full word independently.'),
 (r'\unsure{l}','doubt retained','The same diagonal-overstruck second character occurs in the proposition; retain the uncertain l rather than silently regularizing it.'),
 (r'\mathrm{M}','doubt resolved','The enlarged subscript is clearly typed M, not the witness calligraphic A.')
 ]},notes=[
 'The capital H is a regular serifed typewriter overprint on h, also attested at site 41. Its layer is corrected to typed; its capitalization is preserved.',
 'All listed retouched words are readable as transcribed. The visible corrections in checked, all, totally, supposed, over, natural, Then and aspheric are typewriter overprints.',
 'Both Fl groups contain the same additional diagonal stroke on their second character. The doubtful reading remains in both places.',
 'The dark small mark adjacent to the opening parenthesis before page 142 coincides with that parenthesis; no distinct readable inserted character is established.',
 'The subscript is clearly M. The handwritten for sits above any in the following Moreover insertion and is retained there.',
 'The vertical reference ends clearly p.268. Its first abbreviated words remain marked cf. lemme.',
 'The lower-left 61 is separate handwritten archive foliation and remains a marginal number.'
 ],summary='Both halves, the complete long handwritten addition and six enlarged details inspected. Resolved the canonical homotopy subscript as typed M, corrected the H-over-h layer to typewriter, and retained three uncertainties in Fl and the marginal reference. The deleted except Delta_o only is visibly cancelled. The complete generating-interval assertion, its inter and in A deletions, the added for, and all margin marks are preserved. The source distinction between strict total asphericity and modelizing is maintained.',differences={
 4248:('and there are maps of the latter','the typescript reads as our transcription','The word are is fully typed and is omitted by the witness.'),
 4250:(r'\Delta_{\mathrm{o}}','the typescript reads as our transcription','The rounded character sits below the handwritten Delta, not in superscript position.'),
 4252:(r'\deleted{except \hand{$\Delta$}$_{\mathrm{o}}$ only}','the typescript reads as our transcription','A continuous pen deletion cancels the whole exception; the witness prints it as live text.'),
 4253:(r'\margin{X}','the typescript reads as our transcription','The left-margin X is clear and is absent from the witness.'),
 4257:('intervals which are aspheric','the typescript reads as our transcription','The typed relative pronoun is which.'),
 4259:('goes through smoothly indeed, if','the typescript reads as our transcription','No comma is visible between smoothly and indeed; the witness supplies one.'),
 4260:(r'h$_{\mathrm{M}}$','our transcription corrected','The uncertain index is settled by enlargement as typed M; the witness substitutes calligraphic A.'),
 4262:(r'\margin{\unsure{cf. lemme} p.268}','the typescript reads as our transcription','The marginal reference is visible and retained with its unresolved abbreviation; the witness omits it.')
 })

review('ps_134-4_062',owner='134_4_tail',changes=[
 (r'\unsure{A} one)',r'A one)','Enlargement clearly shows a typed capital A below the overtyped and. Its function is unexplained, but its letter and typed provenance are visible.'),
 (r'(Cat)\unsure{,} say.',r'(Cat)\xout{,} say.','The comma position is covered by a regular typewriter x overstrike. The doubtful comma is retained as cancelled punctuation.'),
 (r'\uline{contrac}',r'\uwave{contrac}','The faint pencil underline beneath contrac is a wavy stroke, visible on enlargement, rather than a straight rule.')
 ],doubts={'unsure':[
 (r'\unsure{they|thay}','doubt retained','The middle letter has superimposed vertical and curved typewriter strokes. The final state of they/thay cannot be securely separated.'),
 ('A','doubt resolved','A regular capital A is visible below the cancelled and; its semantic purpose is not used to change its reading.'),
 (r'\unsure{course|dourse}','doubt retained','The initial letter contains overlapping c/d forms including an ascender; the final intended typewriter state remains uncertain.'),
 (r'\xout{,}','doubt resolved','A regular x visibly cancels the comma position after (Cat).')
 ]},notes=[
 'The original er is overwritten by the pen ending ing; its long descending g is unmistakable.',
 'The a has irregular heavy pen cancellation, unlike the regular x overstrikes elsewhere on the line.',
 'Both middle-letter they/thay and initial-letter course/dourse overprints remain uncertain after enlargement; no lexical inference removes their marks.',
 'The detached character is a regular typed capital A, now settled without an interpretation of its role.',
 'The comma position after (Cat) is visibly cancelled by a typewriter x, now encoded as a strike-out.',
 'The small rounded indices e_0, Delta_0 and pi_0 are in subscript positions; no raised exponent or capital O is substituted.',
 'The lower-left 62 is archive foliation, separate from the typed author page 150.'
 ],summary='Both halves and five enlarged details plus the faint contractor underline inspected. Resolved the detached typed A and cancelled comma; retained the two typewriter-overprint doubts. The faint underline is specifically wavy. The text visibly has h_M, the pen modelizing replacement, two margin crosses and the added star. The axiomatic list a–d is complete, including saturation, 0-admissibility, Delta_1 relative asphericity and final-object asphericity.',differences={
 4264:(r'need not be \deleted{a} modeliz\over{er}{ing}','the typescript reads as our transcription','The pen cancels a and overwrites er by ing; the witness leaves a modelizer.'),
 4266:(r'h_W=h_M','the typescript reads as our transcription','The second subscript is clearly typed M, matching page 149; the witness changes it to calligraphic A.'),
 4267:(r'\margin{x} ... \margin{X}','the typescript reads as our transcription','Both marginal crosses are visible.'),
 4268:(r'\uwave{contrac}tor','our transcription corrected','The underline is a faint wavy pencil stroke under contrac, not absent and not straight.'),
 4269:(r'(up to equivalence)\hand{(*)}.For','the typescript reads as our transcription','The handwritten parenthesized star is clearly present.'),
 4274:(r'aspheric \xout{and} A one)','our transcription corrected','The detached capital A is legible below the cancelled and; it remains in the text without a speculative interpretation.')
 })
