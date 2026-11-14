from review_root import review

k='ps_134-2_033'
review(k,changes=[
    (r'\mspage{\unsure{10.}}'+'\n\n'+r'\margin{\unsure{18|19}}',r'\margin{\unsure{10}}'+'\n\n'+r'\mspage{\hand{\unsure{18|19}}}','The heavily retraced 10 is at the left, whereas the overwritten 18-or-19 is the centered folio. Neither is resolved by numerical sequence.'),
    (r'\deleted{\unsure{11}}\hand{12}.',r'\deleted{\hand{12}}\hand{12.}','The older cancelled pen number reads 12, not 11; the new 12 and its full stop are also handwritten.'),
    (r'\text{(Top)} \longrightarrow (\infty\text{-groupoids})',r'\text{(Top)} \hand{\longrightarrow} (\infty\text{-groupoids})','The fundamental-functor arrow is penned.'),
    (r'D_{\unsure{*|i}}',r'D_i','The handwritten subscript has a distinct dot and short lower stem, identifying i rather than a star.'),
    (r'\inserted{$M$}',r' \inserted[typed]{$M$}','M is typed above the line and is a separate object name after the quoted phrase.'),
    (r'\inserted{stepwise}',r'\inserted[typed]{stepwise}','Stepwise is typed interlinear text.'),
    (r'(\hand{$i\in\underline{N}$}',r'($i\hand{\in}\underline{N}$','The i and underlined N are typed; the membership sign is drawn by hand. No unseen closing parenthesis is supplied at the clipped right edge.'),
    (r'$D_{\unsure{i}} \rightrightarrows D_{\unsure{i+1}}$',r'$D_{i\xout{\illegible{1}}} \hand{\rightrightarrows} D_{\unsure{i+1}}$','The left i is clear, followed by a dense typed cancellation of extra subscript matter. The right i+1 remains overprinted and doubtful; both arrows are hand-drawn.'),
    (r'\over{a}{=}',r'\unsure{\over{a}{=}}','A typed a is clear but the heavy horizontal impressions do not securely establish a separate equals correction. An independent image reading also leaves the correction and its layer order uncertain.'),
    (r'$D_o\amalg_{D_{-1}} D_o = D_o \hand{$\amalg$} D_o$',r'$D_o\hand{\amalg}_{D_{-1}} D_o = D_o \hand{$\amalg$} D_o$','Both coproduct signs are drawn by hand.'),
    (r'$D_o \to S_o$',r'$D_o \hand{\to} S_o$','The arrow is handwritten.'),
    (r'(D_n,\phi_{n-1}^+)\amalg_{D_{n-1}}(D_n,\phi_{n-1}^-)$',r'(D_n,\hand{\phi}_{n-1}^+)\hand{\amalg}_{D_{n-1}}(D_n,\hand{\phi}_{n-1}^-)$','The phi letters and amalgamation sign are penned; the typed disc names and indices remain plain.'),
    (r'S_n \longrightarrow D_{n+1}',r'S_n \hand{\longrightarrow} D_{n+1}','The cofibration arrow is handwritten.'),
    (r'$\phi_n^+ , \phi_n^-$',r'$\hand{\phi}_n^+ , \hand{\phi}_n^-$','The phi letters in this pair are handwritten.'),
    (r'$D_n \rightrightarrows S_n$',r'$D_n \hand{\rightrightarrows} S_n$','The pair of arrows is handwritten.'),
    (r'\underline{C}_o^{\,o} \longrightarrow M \quad , \quad K \longmapsto |K|_M',r'\underline{C}_o^{\,o} \hand{\longrightarrow} M \quad , \quad K \hand{\longmapsto} |K|_M','Both displayed arrows are drawn by hand.'),
    (r'$\underline{C}_\infty^{\,o} \to M$',r'$\underline{C}_\infty^{\,o} \hand{\to} M$','The extension functor arrow is handwritten.'),
    (r'$Z\to X$ and $Z \to Y$',r'$Z\hand{\to} X$ and $Z \hand{\to} Y$','Both maps in the proposed gluing assertion are handwritten.'),
    (r'$X\amalg_Z Y$',r'$X\hand{\amalg}_Z Y$','The pushout sign is handwritten.'),
    (r'M \longrightarrow (\infty\text{-groupoids}) \longrightarrow \text{(Ho)}',r'M \hand{\longrightarrow} (\infty\text{-groupoids}) \hand{\longrightarrow} \text{(Ho)}','Both arrows in the composite functor are handwritten.'),
    (r'\over{i}{\unsure{I}}',r'\over{\unsure{i}}{I}','The live tall pen I is clear. The small underlying typewriter marks are compatible with i but not independently secure, so doubt is transferred to the old layer.')
],doubts={'unsure':[
    (r'\margin{\unsure{10}}','doubt retained','The left number reads approximately 10 but is heavily retraced; no full stop is securely distinguishable.'),
    (r'\mspage{\hand{\unsure{18|19}}}','doubt retained','The second digit has overlapping loops; 18 versus 19 is not settled by its position in the sequence.'),
    (r'\deleted{\hand{12}}','doubt resolved','The old cancelled section number is 12.'),
    ('D_i','doubt resolved','The subscript has the dot and lower stroke of i.'),
    (r'D_{i\xout{\illegible{1}}}','doubt narrowed','The live i is clear; the following cancelled subscript material is unreadable.'),
    (r'D_{\unsure{i+1}}','doubt retained','The right index remains densely overprinted.'),
    (r'\deleted{\unsure{,}}','doubt retained','The small cancelled punctuation after D_n is not securely distinguishable.'),
    (r'\over{\unsure{i}}{I}','doubt resolved','The live pen capital I is secure; the old typed letter is separately retained as uncertain.')
],'illegible':[
    (r'\deleted{\illegible{1}}','illegible retained','The dense pen cancellation beneath the inserted as does not yield a secure earlier word.')
]},notes=[
    'The overwritten centered folio remains 18-or-19; the left 10-like mark is separately marginal. No digit is chosen from sequence alone.',
    'The cancelled old section number reads 12 and the live replacement also reads 12.',
    'The handwritten Hom subscript is i; the dot and lower stroke are visible.',
    'The left i is legible but followed by cancelled extra subscript matter. The right i+1 remains doubtful because its typewriter impressions overlap.',
    'The overprinted letter in the first groupoids is still readable as part of groupoids; no different live letter is supported.',
    'The typed a after S_o is clear. The supposed equals correction cannot be separated securely from its heavy bowl/crossbar impressions, so the correction is now explicitly doubtful after a second reading.',
    'The cancelled mark after D_n remains uncertain punctuation.',
    'The word embodying remains readable through its opening overprint; there is no secure additional word to supply.',
    'The lower-left archive number 33 is clear and retained.'
],summary='Both halves and nine enlarged details inspected. Corrected folio placement and the cancelled section number, resolved the Hom subscript, distinguished typed interlinear M and stepwise, marked pen arrows and symbols, and retained unresolved subscript layers. A second reader confirmed that the supposed equals correction after S_o remains uncertain and that the live final I is secure.',differences={
    408:('D_i','our transcription corrected','The image settles the handwritten subscript as i, agreeing with this witness reading.'),
    410:(r'\inserted[typed]{$M$}','our transcription corrected','The interlinear M is typed, not handwritten.'),
    413:(r'\inserted[typed]{stepwise}','our transcription corrected','Stepwise is typed above the line.'),
    415:('primitive structure','the typescript reads as our transcription','Structure is singular in the typed source.'),
    418:('final object','the typescript reads as our transcription','Object is singular in the source; the witness adds s.'),
    421:(r'\margin{$D_{n+1}$}','the typescript reads as our transcription','The marginal handwritten D with subscript n+1 is present.'),
    423:(r'$\hand{\phi}_n^+ , \hand{\phi}_n^-$','our transcription corrected','The oval-and-stem phi letters are handwritten. Their source forms are retained instead of substituting the witness varphi spelling.'),
    428:(r'\margin{X}','the typescript reads as our transcription','The pencilled X in the left margin is visible.'),
    430:(r"\hand{$\pi$}$_i$'s",'the typescript reads as our transcription','The penned symbol has the curved legs of lower-case pi; the witness capital Pi is not imported.'),
    432:('(Ho)','the typescript reads as our transcription','The typed name is Ho inside parentheses, not the witness Hot notation.'),
    433:(r'\inserted{(18)}','the typescript reads as our transcription','The handwritten call 18 is present after the corrected gerbs phrase.')
})
