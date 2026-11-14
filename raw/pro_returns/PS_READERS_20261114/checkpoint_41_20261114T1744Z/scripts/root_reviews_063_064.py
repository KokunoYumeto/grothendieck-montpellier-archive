from review_root import review
k='ps_134-2_063'
arrow=r'\hand{\tikz[baseline=-.7ex]{\draw[->] (1,0)--(1,.2)--(0,.2)--(0,-.05);}}'
review(k,changes=[
(r'\mspage{-18 -}',r'\mspage{-\hand{4}8 -}','The first digit is a handwritten4, not typed1; the 8 and hyphens are typed.'),
(r"\margin{G'} such",r"\margin{\hand{G'}} such",'The first marginal G-prime is handwritten.'),
(r"\margin{G'} usual",r"\margin{\hand{G'}} usual",'The second marginal G-prime is handwritten.'),
(r'G^{\over{\unsure{/}}{\unsure{\prime}}} = \mathrm{Ext}',r'G^{\over{\unsure{/}}{\prime}} = \mathrm{Ext}','The live slanting prime is visible beside the blackened old exponent and is confirmed by the separate margin G-prime; only the old exponent remains doubtful.'),
(r'G^{\over{\unsure{/}}{\unsure{\prime}}} = \mathcal{E}xt',r'G^{\over{\unsure{/}}{\prime}} = \mathit{Ext}','The second live prime is clear. The following Ext is ordinary italic type, not a calligraphic E followed by upright letters.'),
(r'\mathcal{E}xt^0',r'\mathit{Ext}^0','The exponent-zero Ext is typed italic throughout.'),
(r'\mathbb{R}\mathcal{H}om',r'\mathbb{R}\mathit{Hom}','The operator has a doubled R followed by ordinary italic Hom, not a calligraphic H.'),
(r'\deleted{\unsure{only meets}}',r'\deleted{only meets}','All letters of the two cancelled typed words can be recovered through the hatching.'),
(r'\deleted{taking \unsure{i}}',r'\deleted{taking i}','The small cancelled final character has the dot, stem and foot of typed i.'),
(r'(\mu_{\hand{\unsure{\infty}}})_X',r'(\mu\deleted{\illegible{1}}_{\hand{\infty}})_X','The new subscript infinity is clear. A separate blackened old baseline character after mu was omitted and is now preserved as an illegible cancellation.'),
(r'\hand{$\curvearrowleft$}',arrow,'The arrow over the shift indication is angular, with a horizontal top and downward left arrowhead; replace the generic curved glyph by that geometry.'),
(r'\uline{R\mathcal{H}om}(F, \mu_{\hand{\unsure{\infty}}})',r'\uline{\mathrm{R}\mathit{Hom}}(F, \mu\deleted{\illegible{1}}_{\hand{\infty}})','The underlined operator is upright R followed by italic Hom. The live infinity is clear, and its separate blackened old baseline character is restored as an illegible cancellation.'),
(r'R\mathcal{H}om(F, \mathbb{G}_m)',r'\mathrm{R}\mathit{Hom}(F, \mathbb{G}_m)','The alternative operator has upright R and ordinary italic Hom.'),
(r'\deleted{coefficient}',r'\deleted{coefficients}','The cancelled typed word visibly ends in s; the initial transcription omitted it.'),
(r'\margin{63}',r'\margin{\hand{63}}','The lower-left 63 is pencil archive foliation.')
],doubts={'unsure':[
(r'\unsure{/}','doubt retained','The old exponent is heavily blackened; the slash-like original remains only a tentative reading.'),
(r'\prime','doubt resolved','A separate live prime stroke is visible beside the blackened exponent and the margin repeats G-prime.'),
(r'\unsure{/}','doubt retained','The second old exponent is likewise covered by thick pen strokes.'),
(r'\prime','doubt resolved','The live prime stroke and its separate marginal reminder agree.'),
('only meets','doubt resolved','The typed letters of both words can be followed under the diagonal cancellations.'),
(r'\unsure{on}','doubt retained','The old letters under the pen by overlap too densely to establish on independently.'),
('i','doubt resolved','The final cancelled typed character has a visible dot, stem and foot.'),
(r'\infty','doubt resolved','The handwritten subscript consists of two joined loops; the separate old baseline character remains illegible.'),
(r'\infty','doubt resolved','The second new subscript is equally clear, while its blackened predecessor cannot be read.')
],'illegible':[]},notes=[
'Both live G-primes are resolved from their separate pen strokes and marginal reminders; each blackened old exponent remains doubtful.',
'The Q in the cohomological Serre-duality formula is plain, unlike the doubled Q in nearby formulas; the literal difference is retained.',
'The cancelled typed phrase only meets is now readable through the hatching.',
'The character after taking is a dotted typed i and is cancelled with that word.',
'Both live infinity subscripts are handwritten and legible. Both separate cancelled baseline characters were omitted by the initial transcription and are restored as illegible marks.',
'The shift arrow is a squared, bent arrow pointing down over[2]; its actual geometry is now represented.',
'The lower-left63 is pencil archive foliation.',
'The first folio digit is handwritten4, giving48; it is not1.'
],summary='Both halves and enlarged G exponents, cancelled words, infinity corrections and underlined operator inspected. Corrected folio48, resolved the live primes, only meets, final i and both infinity subscripts, while restoring two unreadable cancelled baseline characters. Both marginal G-primes are marked as handwriting. Typed italic Ext/Hom and the cancelled plural coefficients are restored. The underlying G exponents and old on remain doubtful; the source plain Q is preserved.',differences={
1019:(r"\margin{\hand{G'}} (twice)",'our transcription corrected','Both margin reminders are legible handwriting and are absent from the witness.'),
1020:(r'\mathit{Ext}^1(G,\mathbb{Q}/\mathbb{Z})','our transcription corrected','The scan uses ordinary italic Ext, differing from the upright Ext in the opening equation and the normalized witness.'),
1021:(r'\mathit{Ext}^0(G,\mathbb{Q}/\mathbb{Z})','our transcription corrected','The exponent-zero operator is typed italic; the witness loses that distinction.'),
1028:('squared bent pen arrow from shift to[2]','our transcription corrected','The source has an angular pen arrow, now reconstructed rather than represented by a curved-arrow character.'),
1029:(r'\uline{\mathrm{R}\mathit{Hom}}(F,\mu\deleted{\illegible{1}}_{\hand{\infty}})','our transcription corrected','The underline spans RHom. The clear new infinity and unreadable cancelled old baseline character are now both represented.'),
1031:('it consists certainly','the typescript reads as our transcription','The typed verb ends in s.'),
1033:(r'categor\over{y}{ies}','the typescript reads as our transcription','The pen explicitly changes the ending to plural ies; the witness retains the singular.')
})
k='ps_134-2_064'
review(k,changes=[
(r'\mspage{- \unsure{\hand{4}}9 -}',r'\mspage{- \hand{4}9 -}','The angular first digit is a clear pen4.'),
(r"classfield\deleted{s''\unsure{,}} \inserted{theory''}",r"classfield\deleted{s''} \inserted{theory''},",'The comma is clearly visible below and to the right of the insertion curve and is not crossed out. Place the new theory quotation before this surviving comma.'),
(r"\inserted{theory''}:",r"\inserted{theory''}\hand{:}",'The colon after the arithmetic-classfield replacement is handwritten, with two irregular pen dots.'),
(r'\margin{64}',r'\margin{\hand{64}}','The lower-left64 is pencil archive foliation.')
],doubts={'unsure':[
(r'\hand{4}','doubt resolved','The leading folio digit has the angular crossbar and descending stem of handwritten4.'),
(',','doubt resolved','The enlarged comma is an intact typed glyph and lies outside both the cancellation and the insertion curve.')
],'illegible':[]},notes=[
'The leading4 of49 is clearly handwritten.',
'The typed comma after the old closing quotation remains live; the curve from theory does not cancel it. The old s and quotation are cancelled.',
'The two dots of the colon after arithmetic classfield theory are handwritten and now marked as such.',
'The lower-left64 is pencil archive foliation.'
],summary='Both halves and enlarged geometric-classfield comma and arithmetic-classfield colon inspected. Resolved handwritten4 and the surviving typed comma, placed the inserted theory before that comma, and marked the new colon as pen. The literal lowercase k in both cohomological operators, extra closing parenthesis, H_! without a degree star, and square brackets around Lang’s remark are preserved.',differences={
1042:('in its cohomological form','the typescript reads as our transcription','The typed word in includes n.'),
1043:(r'\Delta_0\mathbb{R}\Gamma_k(J^*)\simeq\mathbb{R}\Gamma_k(\Delta J^*[1])','the typescript reads as our transcription','Both base-field subscripts are lowercase k, not the witness uppercase K.'),
1045:(r'$\mathbb{Q}/\mathbb{Z}$)\hand{)}','the typescript reads as our transcription','The handwritten closing parenthesis is additional to the typed one; the duplicate is literal and is not silently removed.'),
1048:(r'\mathbb{R}\Gamma_k','the typescript reads as our transcription','The subscript is the same lowercase k as the base field and earlier displayed formula.')
})
