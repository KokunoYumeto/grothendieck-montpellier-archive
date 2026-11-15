from review_root import review

review('brown_134-2_122',changes=[
 (r'\margin{\uline{Stack}}',r'\margin{\uwave{Stack}}','The pencil gloss Stack has a wavy underline, not a straight typed underline.'),
 (r'\mspage{123}',r'\margin{123}','The lower-left 123 is handwritten archive pagination, not a typed manuscript page heading.')
],doubts={},notes=[
 'The faint pencil topoi is clear, beside the typed toposes, with no cancellation or insertion caret. The irregular spot near constructions is a brown paper stain rather than a readable correction.',
 'The marginal Stack is handwritten and has a wavy underline; that underline is now represented as such.',
 'The opening quotation mark touches the preceding the and is malformed or partly filled. The literal close setting already transcribed is retained; no missing word is supplied.',
 'The groupoid letter in C, of X has no visible subscript. The plain C is retained, without supplying the expected 1.',
 'The cohomology arrow bears a clear tilde-over-equals relation above its shaft; the existing xrightarrow label is retained.',
 'The four cited expressions have the italic typewriter face, not handwritten underlining, and remain textit.',
 'The lower-left 123 is handwritten and is moved to the archive margin annotation.'
],summary='Both halves inspected line by line. The topoi and Stack glosses stay marginal; only the wave shape of the latter underline is corrected. Conditions A–C, the unindexed C, the Postnikoff spelling, and SGA3 remain literal. The absent locally-constant qualification in C is a mathematical caution for the guide, not a textual correction.')

review('brown_134-2_123',changes=[
 (r'\margin{\unsure{this} seems \unsure{suspect}}',r'\margin{\textcolor{black}{\unsure{this} seems suspect}}','The marginal words are typed. The clipped first t remains doubtful; the surviving upper and lower curves securely identify the first s of suspect. Keep typed text black within the marginal-note macro.'),
 (r'\underrightarrow{\ell im}',r'\underset{\hand{\longrightarrow}}{\ell im}','The right-pointing arrow under the typed lim is drawn by hand, with a separate shaft and asymmetric head.'),
 (r'\underleftarrow{\ell im}',r'\underset{\hand{\longleftarrow}}{\ell im}','The left-pointing arrow under the second typed lim is likewise handwritten.'),
 (r'\xrightarrow{\ \phi\ }',r'\hand{\xrightarrow{\ \textcolor{black}{\phi}\ }}','The long arrow shaft and head are drawn by hand; the phi label above it remains typed.'),
 (r'\longrightarrow \tau_1',r'\hand{\longrightarrow} \tau_1','The long displayed functor arrow is drawn by hand; the source and target remain typed.'),
 (r'u \longmapsto \phi_0',r'u \hand{\longmapsto} \phi_0','The displayed mapsto bar, shaft, and head are drawn by hand. The low typed 0 after phi is preserved literally.'),
 (r'T \longmapsto \Pi_1',r'T \hand{\longmapsto} \Pi_1','The mapsto arrow in the van Kampen sentence is drawn by hand and is marked independently of the typed symbols.'),
 ('does the job, but',r'does the job\unsure{,|\hand{,}} but','The comma is clear, but its unusually solid ink does not securely identify typing versus a pen addition or retouch; retain provenance alternatives.'),
 (r'\mspage{124}',r'\margin{124}','The lower-left 124 is a handwritten archive folio; the original heading - 2 - remains separate.')
],doubts={'unsure':[
 (r'\unsure{this}','retain doubt','The marginal first letter is substantially clipped; the candidate this remains marked although his is fully legible.'),
 ('suspect','doubt settled','The enlarged crop preserves the right-hand upper and lower curves of the clipped first s and all following letters; suspect is secure.')
]},notes=[
 'The note is typed, not handwritten. Its first t is clipped and doubtful; the partly clipped s of suspect can be identified from its surviving form. Typed color is restored.',
 'Handwritten 124 is retained as the archive marginal number.',
 'Both limit arrows are hand drawn. Their opposite directions are retained while the lim letters remain typed.',
 'The comma after job is visibly dark and full, but no separate underlying character or definite pen stroke can be distinguished. Its punctuation is settled and its provenance explicitly doubtful.'
],summary='Both halves and enlarged margin/comma crops inspected. The classifying-topos proposal, typed skeptical marginal comment, exactness conditions, and proposed 2-universal comparison are retained. Hand-drawn arrows are marked. The displayed phi-subscript-zero is literal; the mathematical role of composition is noted in the guide. Two doubts remain: clipped first letter and comma provenance.')

review('brown_134-2_124',changes=[
 (r'\Gamma_{\unsure{x|\times}}',r'\Gamma_{\times}','The enlarged subscript is a small cross with four plain arms, not the serifed capital X appearing elsewhere in the same paragraph. Retain the literal multiplication-shaped mark rather than supplying X.'),
 (r'\xrightarrow{\ F\ }',r'\hand{\xrightarrow{\ \textcolor{black}{F}\ }}','The long functor arrow is hand drawn; the F above it remains typed.'),
 (r'\mathbb{C}(\Gamma_X F) \longrightarrow',r'\mathbb{C}(\Gamma_X F) \hand{\longrightarrow}','The final displayed comparison arrow has a drawn shaft and head; the adjoining expressions remain typed.'),
 (r'\mspage{\hand{125}}',r'\margin{125}','The handwritten 125 is archive pagination at the lower left, separate from the typed - 3 - heading.')
],doubts={'unsure':[
 (r'\times','doubt settled','The crop clearly shows a plain small cross, unlike the serifed X in the following integration notation.'),
 (r'\unsure{\underline{C}_n|C_n}','retain doubt','A short low dash is visible below C, but the image does not establish whether it is intentional underlining or an incidental mark. The underline alternative stays doubtful.')
]},notes=[
 'The first Gamma subscript is a cross-shaped mark; it is settled as times, while the next paragraph plainly has capital X. The difference is retained.',
 'The words where now and but have heavier or differently spaced typing. No separate pen wording or recoverable earlier word is visible; the words and their order are retained.',
 'There is a short low dash under C. Its status as underlining is not secure, so the existing underlined/ununderlined alternative remains.',
 'The superscript X is heavily typed or overtyped but readable as X; no different underlying character is identifiable.',
 'The small raised o belongs to the following L degree sign; there is no additional o before If.',
 'The archive number 125 is handwritten. Two long displayed arrows also show drawn shafts and heads and are now marked; the short arrows of the cochain complex remain typed.'
],summary='Both halves and enlarged Gamma/C details inspected. Settled the cross-shaped Gamma subscript and retained the possible underline doubt. The displayed condition N≤i,n is unequivocal and conflicts with the following N≥sup(i,n); it remains literal in every reader and is discussed only in the guide. The type n-champ after an N-fold range extension is also preserved.')
