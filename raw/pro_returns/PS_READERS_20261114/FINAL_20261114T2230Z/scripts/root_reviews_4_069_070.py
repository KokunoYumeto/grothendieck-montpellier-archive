from review_root import review
from pathlib import Path

review('ps_134-4_069',owner='134_4_tail',changes=[
 (r'\unsure{W|A}',r'W','The enlarged subscript has two descending V-shaped strokes and is clearly typed W, not A.'),
 ('b) The functor',r'b) \over{T}{t}he functor','The old capital T remains in gray, while a black pen lowercase t with a curved foot is drawn over it.'),
 (r'\begin{tikzcd}',r'\begin{tikzcd}[every arrow/.append style={draw=blue!65!black}]','All ten arrows in the comparison square are drawn in pen; all category labels remain typed.'),
 (r"$C \to C'$",r"$C \hand{\to} C'$",'The inline map arrow is handwritten.'),
 (r"$A_{/C} \to A_{/C'}$",r"$A_{/C} \hand{\to} A_{/C'}$",'The corresponding category-of-elements arrow is handwritten.'),
 (r'$C \mapsto A_{//C}$',r'$C \hand{\mapsto} A_{//C}$','The first mapsto is drawn in pen.'),
 (r'$C \mapsto AxC$',r'$C \hand{\mapsto} AxC$','The second mapsto is drawn in pen.'),
 (r'(Cat)$\to H_',r'(Cat)$\hand{\to} H_','The localization functor arrow is pen.'),
 (r'xC $\to$ C',r'xC $\hand{\to}$ C','The Delta_1 product projection arrow is pen.')
 ],doubts={'unsure':[
 ('W','doubt resolved','The enlarged printed subscript is unmistakably W, despite its conflict with the earlier definition using A.'),
 (r"\unsure{'}",'doubt retained','The pen mark includes an acute upper part and a long lower curved trace; it does not securely settle to a simple prime alone.'),
 (r'\unsure{twe|two}','doubt retained','The final round letter also contains a horizontal e-like bar; the order of the two typewriter impressions is not established.')
 ]},notes=[
 'The subscript is clearly W. With is legible through the typewriter retouching; no word is supplied or omitted.',
 'The capital typed T is covered by a black pen lowercase t with a curved foot; both layers are now recorded.',
 'The lower-right pen mark after C has a longer curve than a simple prime; its uncertainty remains.',
 'The last letter of twe/two contains overlapping round and barred forms. Its uncertainty remains.',
 'The line-end restric is cut at the edge; the recorded split continuation tive is present below, and no extra letter is invented.',
 'The lower-left 69 is handwritten archive foliation.'
 ],summary='Both halves and four enlarged details inspected. Settled the literal i_W index, preserved the two remaining glyph uncertainties, recorded the T-to-t overwrite and pen arrows. All four bottom-row objects are primed, unlike the supplied witness row. Source references to diagram (12) and saturation condition b) are preserved, although the comparison diagram is (11) and saturation was condition a); the guide records these mathematical reference slips. The three localized isomorphisms include the inverse of the middle comparison arrow.',differences={
 4401:(r'f_i=i_Wi^*','our transcription corrected','The image settles the disputed subscript as W. The witness prints A; the defined construction uses A, but the typescript is not silently repaired.'),
 4403:('the first hand side','the typescript reads as our transcription','The word is first, not left.'),
 4404:(r"A_{/C'}\to A_{//C'}\leftarrow AxC'\to C\hand{\unsure{'}}",'the typescript reads as our transcription','All four lower objects carry prime marks; the final pen mark remains doubtful in exact shape. The witness row omits the primes.'),
 4410:('deduced from it','the typescript reads as our transcription','The singular pronoun it is printed, not them.')
 })

review('ps_134-4_070',owner='134_4_tail',changes=[
 (r'\unsure{Fl|F/}',r'F\over{l}{\ell}','The scan shows a typed F and serifed l with a pen diagonal, matching the repeated Fl treatment on the preceding pages; it is not a bare slash.'),
 (r'\unsure{definitely}',r'definitely','The complete word is readable through the typewriter retouching, including the two dotted i letters.'),
 (r'\uuline{not}',r'\uwave{\uline{not}}','The emphasis beneath not comprises two straight strokes in total and a lower wavy stroke; retain the wavy character rather than three straight underlines.'),
 (r'\unsure{isomorphism\xout{e}}',r'isomorphis\over[typed]{\unsure{p}}{m}e','Enlargement shows a live terminal e before for; it is not cancelled. The preceding m overlays a lower p-like typewriter impression, whose old reading remains doubtful.'),
 (r'\inserted{k}',r'\inserted[typed]{k}','The interlinear k has a regular typewriter stem and arms; its placing slash is pen.'),
 (r'\hand{(}constant \deleted{grou}\unsure{\hand{)}}',r'\hand{(}constant\hand{)} \deleted{grou}','The closing pen parenthesis is visible immediately after constant, at the left edge of the cancelled grou. It is distinct from the horizontal cancellation.')
 ],doubts={'unsure':[
 (r'F\over{l}{\ell}','doubt resolved','A serifed typed l remains visible beneath the diagonal pen stroke.'),
 ('definitely','doubt resolved','The letters can be read independently through the retouching.'),
 (r'\unsure{c}','doubt retained','The line-end old character is covered by a dark x overstrike; c remains a candidate only.'),
 (r'isomorphis\over[typed]{\unsure{p}}{m}e','doubt narrowed and transcription corrected','The final e is live and the final word reads isomorphisme. Only the older p-like impression beneath m remains uncertain.'),
 (r'\hand{)}','doubt resolved','The closing arc is visible before the cancelled grou and is separate from its horizontal stroke.')
 ],'illegible':[
 (r'\illegible{1}','illegibility retained','The pen of covers the old short word; a gray final curve survives but does not recover a secure full word.')
 ]},notes=[
 'The group is F followed by typed l and a pen diagonal, matching adjacent Fl notation. Its layered form is now explicit.',
 'Definitely is readable after enlargement. The line-end cancelled character after equivalen remains doubtful.',
 'The pen of is clear, but the old short word remains unreadable.',
 'The final e is visibly live; the m before it overlays a p-like typed impression. The earlier cancellation of e was unsupported and is removed.',
 'The closing pen parenthesis stands directly after constant at the start of the cancelled grou. The old grou remains cancelled.',
 'The display arrow is clearly drawn in pen, as transcribed.',
 'The lower-left 70 is handwritten archive foliation.'
 ],summary='Both halves and six enlarged details inspected. Resolved Fl, definitely and the closing parenthesis; narrowed the isomorphisme doubt to its overwritten old p-like letter and restored its live final e. The line-end c and old word beneath of remain unresolved. Corrected the typed k insertion and the mixed straight/wavy emphasis of not. The source explains that closure axioms admit all arrows and many coefficient-dependent or truncated notions of weak equivalence; the philosophical continuation is preserved in full.',differences={
 4415:('appears as rather obvious','the typescript reads as our transcription','The word as is fully typed and must not be omitted.'),
 4417:(r'\inserted[typed]{k}','our transcription corrected','The k is a typed interlinear insertion with a pen placement slash.'),
 4418:(r'an isomorphis\over[typed]{\unsure{p}}{m}e','our transcription corrected','The article an is clear, not the witness as; the terminal e is live rather than cancelled, and only the old glyph beneath m remains doubtful.'),
 4420:(r'\hand{(}constant\hand{)} \deleted{grou}','our transcription corrected','The closing parenthesis is settled and placed at its visible position before the cancelled grou.'),
 4428:('strongly personally implied','the typescript reads as our transcription','The final word ends in d, not the witness s.')
 })
