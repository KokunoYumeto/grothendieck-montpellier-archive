from review_root import review

k='ps_134-2_032'
review(k,changes=[
    (r'\mspage{10}'+'\n\n'+r'\margin{18}',r'\margin{10}'+'\n\n'+r'\mspage{\hand{18}}','The left marginal number is 10; the centered handwritten folio is 18.'),
    (r'\xout{\unsure{11}}11.',r'\deleted{\hand{\unsure{11}}}\hand{11.}','Both the current section number and the cancelled earlier mark are pen writing. The old digits remain partly obscured.'),
    (r'\mathrm{Ob}(\underline{B}_o)',r'\mathrm{Ob}(B_o)','The B in this particular object-set formula has no underline; the C immediately before it does.'),
    (r'\unsure{amounts}',r'amount\hand{s}','The word is amounts; its terminal s is a distinctive pen replacement, with no separable earlier character visible.'),
    (r'\inserted{of $\mathrm{Hom}(D_n,|K|)$}',r' \inserted[typed]{of $\mathrm{Hom}(D_n,|K|)$}','The whole interlinear phrase is typed. A word space separates it from the preceding formula.'),
    (r'\inserted{by}',r'\inserted[typed]{by}','By is typed above the cancelled with.'),
    (r"$D_n \to |K| \to |K'|$",r"$D_n \hand{\to} |K| \hand{\to} |K'|$",'Both arrows in the composition chain are hand-drawn.'),
    (r"$K \to K'$",r"$K \hand{\to} K'$",'The next arrow is handwritten; the lack of geometric-realization bars on these K symbols is retained.'),
    (r"\inserted{an ``allowable''}",r"\inserted[typed]{an ``allowable''}",'The replacement words are typed interlinear text.'),
    (r'\inserted{namely}',r'\inserted[typed]{namely}','Namely is typed, with a pen insertion pointer.'),
    (r'$S_n^{\unsure{*}} \to |K|$',r'$S_n^{\unsure{*}} \hand{\to} |K|$','The arrow is handwritten; the dense superscript remains doubtful.'),
    (r'$D_{n+1} \to |K|$',r'$D_{n+1} \hand{\to} |K|$','The extension arrow is handwritten.'),
    (r"\inserted{on the $D_i$'s}",r" \inserted{on the $D_{\unsure{i|n}}$'s}",'The subscript has a dot or short upper mark but an n-like lower trace. An independent reading confirms that i and n cannot be securely distinguished; the preceding word space is restored.'),
    (r'subsidiary\inserted{after all}',r'subsidiary \inserted{after all}','The inserted phrase is a separate pair of words after subsidiary, not part of that word.'),
    (r'\inserted{undesirable}',r'\inserted[typed]{undesirable}','Undesirable is typed above the line, not handwritten.'),
    (r'$K \mapsto |K|$',r'$K \hand{\mapsto} |K|$','The assignment arrow is penned.')
],doubts={'unsure':[
    (r'\deleted{\hand{\unsure{11}}}','doubt retained','The old pen number is heavily cancelled; the live 11 is clear.'),
    (r'amount\hand{s}','doubt resolved','Amounts is readable, with the final s in pen.'),
    (r'S_n^{\unsure{*}}','doubt retained','The dense superscript could be a star or an overwritten/cancelled mark; its shape and status are not securely separable.'),
    (r'\unsure{A|a}','doubt retained','The overprinted letter has a capital-A-like outer outline and a smaller loop; its exact layer order remains uncertain.'),
    (r'\unsure{this|the}','doubt retained','The final typewriter impressions overlap and do not securely separate this from the.')
],'illegible':[]},notes=[
    'The page has left marginal 10, centered current folio 18, and lower-left archive number 32.',
    'The old number before the live 11. is handwritten and struck by hand; it is not a typewriter cancellation.',
    'Amounts is secure and the final s is handwritten.',
    'The superscript after S_n remains doubtful in both shape and cancellation status; the witness plain S_n does not settle it.',
    'The overprinted word before topological remains this-or-the.',
    'The heavily overprinted A/a remains marked. The surrounding reference must not be silently reassigned from the earlier filler condition to the local closure condition.',
    'The heavy and at the end of the lower paragraph is live typewriter text, not a struck-out word; it is retained.'
],summary='Both halves and seven enlarged details inspected. Corrected the folio placement, pen section numbering, un-underlined B_o, handwritten terminal s, typed interlinear additions, and pen arrows. Preserved the three unresolved overprints/superscript readings and introduced a justified i-or-n subscript doubt after an independent image reading. All required comparison rows and notes were decided.',differences={
    385:(r'\mathrm{Ob}(B_o)','our transcription corrected','The B has no underline in the scanned object-set formula, while the adjacent C does.'),
    386:('every K a subset','the typescript reads as our transcription','The explicit variable K is visibly typed; the witness omits it.'),
    387:(r'\inserted[typed]{of $\mathrm{Hom}(D_n,|K|)$}','our transcription corrected','The added phrase is typed above the line.'),
    388:(r'\xout{with}\inserted[typed]{by}','our transcription corrected','The live by is typed interlinear text.'),
    389:(r"\xout{a}\inserted[typed]{an ``allowable''}",'our transcription corrected','The replacement an allowable is typed, with its quotation marks.'),
    390:(r'\inserted[typed]{namely}','our transcription corrected','Namely is typed above the line.'),
    392:(r'$S_n^{\unsure{*}} \hand{\to} |K|$','the typescript reads as our transcription','A dense superscript mark is present and remains doubtful; it is not silently removed to match the witness.'),
    395:(r"\inserted{on the $D_{\unsure{i|n}}$'s}",'our transcription corrected','The handwritten subscript cannot be certified as the initial i or the witness n. Both remain marked after a second image reading.'),
    398:(r'interpretation\hand{,}','the typescript reads as our transcription','The handwritten comma is present at the right edge.'),
    402:(r'\inserted[typed]{undesirable}','our transcription corrected','The interlinear word is typed.'),
    403:(r'\underline{C}_{n-1}','the typescript reads as our transcription','The source index is clearly n minus 1; the witness prints n plus 1.')
})
