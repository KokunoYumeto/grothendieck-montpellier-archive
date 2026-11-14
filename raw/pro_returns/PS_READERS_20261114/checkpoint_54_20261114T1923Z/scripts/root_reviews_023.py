from review_root import review

k='ps_134-2_023'
review(k,changes=[
    (r"\mspage{\unsure{5'|9}}",r'\mspage{\hand{9}}','The centered folio is a handwritten 9, with a closed upper loop and descending curved stroke.'),
    (r'\margin{\unsure{\deleted{AB} The ex}}',r'\margin{\deleted{\uline{NB}} The def.}','The rotated marginal note reads NB, underlined and cancelled, followed by The def.; the initial reading AB The ex was incorrect.'),
    (r'\xout{\unsure{certain fiber}}',r'\xout{certain fiber}','The two words certain fiber remain readable under the typed cancelling x characters.'),
    (r's^{i}_{\unsure{\chi|\ell}}',r's^{i}_{\over{1}{\unsure{\ell|\chi}}}','A typed 1 is visible beneath the diagonal pen strokes in the first index; the superposed ell/chi-like reading remains doubtful.'),
    (r't^{i}_{\unsure{\chi|\ell}}',r't^{i}_{\over{1}{\unsure{\ell|\chi}}}','The second index likewise has the serif and stem of typed 1 beneath a handwritten diagonal/looped correction, whose precise letter remains doubtful.'),
    (r'\inserted{\unsure{lim|$\varprojlim$}}',r'\inserted{$\varprojlim$}','The handwritten lim has a definite leftward arrow underneath it.'),
    (r'(s_i,t_i)_{i\in\underline{N}}',r'(s_i,t_i)_{i\hand{\in}\underline{N}}','The membership sign in the indexing condition is drawn by hand.'),
    (r'\xout{\illegible{1}} categories',r'\xout{functors} categories','The cancelled word before categories reads functors beneath the x overstrikes.'),
    (r'\xout{\unsure{the type}}',r'\xout{the type}','The two cancelled words the type are legible.'),
    (r'in\unsure{)} the condition',r'in) the condition','The stray right parenthesis after in is clearly typed and is preserved as typed.'),
    (r'\underset{n}{\underrightarrow{\mathrm{lim}}}',r'\underset{n}{\hand{\underrightarrow{\textcolor{black}{\mathrm{lim}}}}}','The rightward direct-limit arrow is handwritten; lim and n remain typed.'),
    (r'any\xout{\illegible{1}} category',r'any\xout{allowable} category','Enlargement recovers allowable under the typed cancellation.'),
    (r'\underline{C}_\infty \longrightarrow C',r'\underline{C}_\infty \hand{\longrightarrow} C','The displayed functor arrow is drawn by hand.'),
    (r'in C , \xout{\illegible{1}}',r'in C , \xout{such}','The cancelled word following in C is clearly such.'),
    (r"\margin{\deleted{\unsure{I'll drop the qualification ``iterated'' henceforth}}}",r"\margin{\deleted{I'll drop the qualification ``iterated'' henceforth}}",'Rotated enlargement recovers the crossed marginal sentence, including qualification and henceforth.'),
    (r'\unsure{F|C}, plus',r'F, plus','The source letter is a typed F with two horizontal arms, not C. The apparent mathematical slip is preserved.'),
    (r'maps \xout{\illegible{1}}\inserted[typed]{between}',r'maps \xout{from}\inserted[typed]{between}','The typed word under the replacement between reads from.'),
    (r'fiber-products \xout{\illegible{1}}',r'fiber-products \xout{to}','The short cancelled word following fiber-products reads to.'),
    (r'\mspage{23}',r'\mspage{\hand{23}}','The lower-left archive folio 23 is handwritten.')
],doubts={'unsure':[
    ('9','doubt resolved','The head folio is a definite 9, not 5-prime.'),
    (r'\deleted{\uline{NB}} The def.','doubt resolved','The rotated crop makes the cancelled underlined NB and the abbreviation The def. readable.'),
    ('certain fiber','doubt resolved','The two cancelled words are still legible under the x strikes.'),
    (r'\over{1}{\unsure{\ell|\chi}}','doubt retained','The underlying typed 1 is visible, but the diagonal superposed letter is not secure enough to choose ell over chi solely from its shape.'),
    (r'\over{1}{\unsure{\ell|\chi}}','doubt retained','The second subscript repeats the same typed 1 and ambiguous pen correction.'),
    (r'$\varprojlim$','doubt resolved','The hand lim and its leftward lower arrow are distinct.'),
    ('the type','doubt resolved','Both cancelled words are visibly recoverable.'),
    (')','doubt resolved','The narrow curved mark is a typed closing parenthesis; it is not removed as a slip in the checked source.'),
    (r'\unsure{wrote}','doubt retained','The beginning of wrote is densely overprinted; the plausible whole word remains marked.'),
    (r"I'll drop the qualification ``iterated'' henceforth",'doubt resolved','The rotated crossed marginal note is legible, including the line-divided word qualification.'),
    ('F','doubt resolved','Two straight horizontal arms distinguish F from the rounded letter C on the same line.')
],'illegible':[
    ('functors','doubt resolved','The stems and rounded letters identify the cancelled word functors.'),
    (r'\illegible{1}','doubt retained','The very short overstrike after to me does not establish its underlying word.'),
    ('allowable','doubt resolved','The cancelled word has clearly recoverable a-l-l-o-w-a-b-l-e.'),
    ('such','doubt resolved','The four letters such remain clear beneath the strike.'),
    ('from','doubt resolved','The four letters from can be distinguished beneath the interlinear between.'),
    ('to','doubt resolved','The ascender of t and rounded o remain visible under the cancellation.')
]},notes=[
    'The centered folio is handwritten 9; the initial 5-prime reading is rejected.',
    'The diagonal cue reads cancelled underlined NB followed by The def.; both are now recorded.',
    'Each index has an underlying typed 1 with a superposed pen correction. The final ell/chi-shaped letter remains uncertain in both occurrences.',
    'Recovered certain fiber, functors, the type, allowable, such, from and to. The short overstrike after to me remains unreadable.',
    'The stroke by fiber products belongs to the curved placement line for iterated; the words remain live.',
    'The lower marginal sentence is fully legible after rotation and is crossed through; qualification remains there, while the later inline insertion says word.',
    'The right parenthesis in in) the is visibly typed and retained.',
    'The line begins with F, not C; this is preserved and will be noted as an apparent category-letter slip in the guide.',
    'The lower-left 23 is handwritten and now explicitly marked.'
],summary='Both halves and six detailed crops reviewed. Resolved folio 9, the NB/The def. cue, the inverse-limit symbol, six cancelled words, the crossed marginal sentence, the stray typed parenthesis, and the source letter F. Marked typed-1/handwritten-index layering and the hand arrows. Four doubts remain; the apparent F-for-C mathematical slip stays in the source.',differences={
    180:(r'\margin{\deleted{\uline{NB}} The def.}','our transcription corrected','The diagonal note is present and omitted from the witness; rotation corrects AB The ex to the cancelled underlined NB followed by The def.'),
    181:(r's^{i}_{\over{1}{\unsure{\ell|\chi}}}, t^{i}_{\over{1}{\unsure{\ell|\chi}}}','our transcription corrected','The indices show typed 1 beneath pen corrections. Ell is contextually plausible and is the witness reading, but the scanned glyphs remain ambiguous; their layered provenance is restored.'),
    198:(r"the two \inserted{``primitive''} relations I \unsure{wrote} down",'the typescript reads as our transcription','The handwritten quoted word primitive is clearly inserted before relations and omitted by the witness.'),
    199:(r"\inserted{(I'll drop the word ``iterated'' henceforth!)}",'the typescript reads as our transcription','The live interlinear insertion says word. Qualification occurs in the crossed-out marginal version, which the witness appears to have followed.'),
    203:('exist in F,','our transcription corrected','The scan clearly has F. The witness prints C, which fits the surrounding categorical statement; the source F is retained as an apparent mathematical slip.')
})
