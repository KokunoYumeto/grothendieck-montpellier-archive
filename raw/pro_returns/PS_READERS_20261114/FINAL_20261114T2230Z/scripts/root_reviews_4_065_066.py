from review_root import review

review('ps_134-4_065',owner='134_4_tail',changes=[
 (r'\inserted{weak}',r'\inserted[typed]{weak}','The added weak has regular typewriter glyphs; only its placement stroke is handwritten.'),
 (r'\inserted{ing}',r'\inserted[typed]{ing}','The inserted ending ing is typed above the line and positioned by a pen curve.'),
 (r"\inserted{there is just \uline{one} $\underline{W}'$}",r"\inserted[typed]{there is just \uline{one} $\underline{W}'$}",'The whole added phrase is typed above the cancelled run, including its W prime; the emphasis under one is preserved.'),
 (r'\unsure{to be just $W_{(\mathrm{Cat})}$ and it is}',r'to be just $W_{(\mathrm{Cat})}$ and it is','The cancelled phrase is legible beneath the x impressions and the additional pen line.'),
 (r"\unsure{be and $\underline{W}'$}",r"be and $\underline{W}'$",'The two words and the underlined W prime are visible beneath their regular x strikes.'),
 (r'\begin{tikzcd}',r'\begin{tikzcd}[every arrow/.append style={draw=blue!65!black}]','All three connecting arrows in (11) are handwritten; the typed objects remain black.'),
 (r'$A_{/C} \to A_{//C}$',r'$A_{/C} \hand{\to} A_{//C}$','The inline comparison arrow is drawn in pen.')
 ],doubts={'unsure':[
 (r'to be just $W_{(\mathrm{Cat})}$ and it is','doubt resolved','Every word and the coefficient are legible beneath the cancellation.'),
 (r"be and $\underline{W}'$",'doubt resolved','The cancelled words and W prime can be read independently.'),
 (r'\unsure{and we were a}','doubt retained','The final letter is covered by an x; the proposed full run cannot be settled completely.'),
 (r'\unsure{;}','doubt retained','The terminal pen blot has two merged parts and does not securely distinguish semicolon from other punctuation.')
 ],'illegible':[
 (r'\illegible{1}','illegibility retained','The old item under weak is crossed by heavy pen hatching; no secure letter sequence survives.'),
 (r'\illegible{2}','illegibility retained','The old run contains fragments resembling all and an underlined W, but the full cancelled expression remains unreadable.'),
 (r'\illegible{1}','illegibility retained','The short cancelled continuation after conditions remains covered by regular x strikes.')
 ]},notes=[
 'The j_A arrow is clearly drawn in pen; a separate earlier typed arrow cannot be recovered securely.',
 'The cancelled item under weak remains unreadable. Weak itself is typed, and its insertion layer is corrected.',
 'Both short cancelled runs remain unresolved; the full added there is just one W prime phrase is typed and has its own placement above the first run.',
 'The long cancelled phrases are readable as to be just W(Cat) and it is / be and W prime. Their uncertainty marks are removed while both cancellation layers remain.',
 'The old prime after W is blackened by a pen cancellation rather than replaced by a live star.',
 'The handwritten st replaces the old tter in latter, producing last. The original underlying letters remain visible.',
 'The terminal punctuation after e is handwritten but remains uncertain.',
 'The lower-left 65 is handwritten archive foliation.'
 ],summary='Both halves and nine enlarged details inspected. Corrected three typed insertions misclassified as pen and settled two long cancelled phrases. Five doubts/lacunae remain. All three diagram arrows and the inline comparison arrow are pen. Diagram (11) literally ends in A, although the comparison with C and the stated W1 condition require the projection to C; this mathematical issue is reserved for the guide. The pen last correction is applied in corrected forms, and the source par.57/pages96–98 reference is retained.',differences={
 4313:(r'W_A^{-1}A\hat{}','the typescript reads as our transcription','The first W_A has no underline in the scan; the witness supplies one.'),
 4316:(r'\inserted[typed]{weak}','our transcription corrected','Weak is a typed interlinear insertion with a pen placement curve, not handwriting.'),
 4318:(r'find\inserted[typed]{ing}','our transcription corrected','The interlinear ing is typed, with pen placement.'),
 4321:(r"\inserted[typed]{there is just \uline{one} $\underline{W}'$}",'our transcription corrected','The phrase is typed above the line; the original transcription misclassified its layer.'),
 4322:(r'just \uline{one}','the typescript reads as our transcription','Only one is underlined, not just one as a unit.'),
 4328:(r'la\over{tter}{st}','the typescript reads as our transcription','The visible pen replacement gives last, unlike the witness latter.'),
 4329:('this condition','the typescript reads as our transcription','The source has singular condition across the line break, not conditions.')
 })

review('ps_134-4_066',owner='134_4_tail',changes=[
 (r'\deleted{\unsure{is}}',r'\deleted{\unsure{X|is}}','The remaining regular crossed diagonals beneath the pen scribble suggest a typed X; the formerly proposed is is retained as an alternative because of the cancellation.'),
 (r'XxC $\to$ C',r'XxC $\hand{\to}$ \over{C}{C}','The projection arrow is pen and its terminal typed C is retraced in dark pen.'),
 (r'AxC \to A_{//C}',r'AxC \hand{\to} A_{//C}','The displayed canonical-map arrow is handwritten.'),
 (r'u: F $\to$ G',r'u: F $\hand{\to}$ G','The fibered-functor arrow is drawn in pen.'),
 (r'C \to \underline{Hom}',r'C \hand{\to} \underline{Hom}','The arrow into the internal Hom is pen, while its labels are typed.'),
 (r'A_{/C} \to A_{//C}',r'A_{/C} \hand{\to} A_{//C}','The arrow in (12) is handwritten.'),
 (r'Fl((Cat))',r'F\over{l}{$\ell$}((Cat))','The second character after F has a pen diagonal over its typed l, matching the same Fl treatment on adjacent pages.')
 ],doubts={'unsure':[
 (r'\unsure{X|is}','doubt retained and alternatives revised','Crossed regular strokes suggest X, but the dense pen cancellation does not settle the old item.'),
 (r'\unsure{s}','doubt retained','A tall d-like stroke and a lower curved stroke overlap in consequence; the final letter state remains uncertain.')
 ]},notes=[
 'The cancelled item after element has a typed X-like core; the alternative is remains because the cancellation obscures its full form.',
 'The fourth letter of consequence has overlapping d/s-like strokes; its uncertainty is retained.',
 'All five cancelled runs were read across both halves. Their visible words agree with the supplied text, including the separately overtyped insure and the duplicated ly at the second long cancellation.',
 'The label e is retraced in pen over a dark circular base; e is readable, while a distinct earlier character is not recoverable.',
 'The inserted article a is typed and is placed by a pen caret, as transcribed.',
 'The lower-left 66 is archive foliation and remains marginal.',
 'The right-edge words and impl cancellation are clipped but their recorded visible portions are present; no extra ending is supplied.'
 ],summary='Both halves and enlarged initial cancellation, consequence overprint and crossed W1 line inspected. Retained two doubts, refining one old-letter alternative. Five arrows and the terminal C retracing are now marked pen; the Fl diagonal is retained as an overprint. The source strengthens final-object asphericity to relative asphericity, introduces the fiberwise condition e), then explicitly withdraws the need for 0-admissibility in this particular argument. The source h_(Cat) <= h_W and full double parentheses in Fl((Cat)) are preserved.',differences={
 4334:('a little stronger still','the typescript reads as our transcription','The typed adjective is little, not the witness littler.'),
 4335:('page 151','the typescript reads as our transcription','The page reference is clearly typed 151; the witness changes it to 150.'),
 4343:('insure that','the typescript reads as our transcription','The source uses insure, consistent with its other occurrences; it is not normalized.'),
 4346:(r'F\over{l}{$\ell$}((Cat))','our transcription corrected','Both opening parentheses are printed, balancing the two closing ones. The pen stroke on l is now represented; the witness has a different parenthesis count.')
 })
