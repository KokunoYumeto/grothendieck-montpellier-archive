from review_root import review

review('brown_134-2_115',changes=[
 (r'\mspage{\hand{116}}',r'\margin{116}','The pencilled 116 is the archive folio at the lower left, not an original typescript page heading; retain it as a marginal annotation.')
],doubts={},notes=[
 'The light handwritten 116 is visible at the lower left of the otherwise blank lower half; it is retained as an archive marginal number.',
 'The underline under Note is part of the typed heading and is retained.',
 'Both halves were inspected. Apart from the complete six-line note and archive folio, the paper is blank; scattered specks and edge rules are scan or paper marks.'
],summary='Both supplied halves inspected. Brown credits Breen and Loday, dates the translated letter 17–19 July 1975, and thanks Grothendieck for this and the two earlier letters. No words are cancelled or uncertain; archive folio 116 is moved from the manuscript-heading macro to a margin annotation.')

review('brown_134-2_117',changes=[
 (r'\margin{demander réf. : Breen.}',r'\margin{\tikz[baseline=-.4ex]{\draw (0,-.1)--(0,.7);}\quad demander réf. : Breen.}','Restore the vertical pen line grouping both incomplete references with the right-margin request; the words are clearly readable.'),
 (r'\mspage{118}',r'\margin{118}','The lower-left 118 is handwritten archive pagination, not a typed manuscript heading.')
],doubts={'unsure':[(r'\deleted{\unsure{S}}','retain doubt','The typed initial after N. is covered by a dense pen cancellation. The candidate S cannot be securely recovered; Saavedra is clearly inserted before Rivano.') ]},notes=[
 'The handwritten request reads demander réf. : Breen.; a vertical line to its left spans the Begueri and Bester references. The line is restored, and the two light handwritten supplements Memoir SMF and Thesis, U of Michigan are retained.',
 'The acute accent above the typed E of Etat is a separate dark pen stroke; the E-to-É writing-over notation is retained.',
 'The old initial remains doubtful under the ink. Saavedra is clear; the long curved line ends in the gap before Rivano and is an insertion cue, not a literal parenthesis or punctuation after the surname.',
 'The visible notation has a plus followed by a short hyphen before groupoid. A tiny high spur lies above the hyphen; it does not establish a second lexical character or a replacement of the plus. The literal +-groupoid is retained.',
 'The isolated small left-margin dot has no call or textual continuation. The speck under developed is contiguous with typed ink; neither establishes a cancellation, accent, or added letter.',
 'The lower-left 118 is plainly written by hand and is now a marginal archive folio.'
],summary='Both halves and enlarged details inspected. The references, strict associativity and strict zero-object qualification, Brown–Spencer equivalence, and Verdier attribution remain literal. Restored the bracket-like line beside the bibliographical request and handwritten archive folio. The cancelled initial alone remains doubtful.')

review('brown_134-2_118',changes=[
 (r"""\arrow[r, leftrightarrow, "(f)"] \arrow[d, leftrightarrow, "(f)"']""",r"""\arrow[r, leftrightarrow, "(f)",color=blue] \arrow[d, leftrightarrow, "(f)"',color=blue]""",'The diagram arrows have hand-drawn shafts and arrowheads; mark the two arrows leaving poly-T-complexes as handwriting while retaining their typed labels.'),
 (r'\arrow[r, leftrightarrow, "(c)"]',r'\arrow[r, leftrightarrow, "(c)",color=blue]','Mark the hand-drawn horizontal equivalence arrow; its c label remains typed.'),
 (r'\arrow[d, leftrightarrow, "(d)"] \arrow[dl, leftrightarrow, "(a)"]',r'\arrow[d, leftrightarrow, "(d)",color=blue] \arrow[dl, leftrightarrow, "(a)",color=blue]','The vertical and diagonal arrows are drawn by hand; retain both heads and the typed labels d and a.'),
 (r"""\arrow[r, leftrightarrow, "(e)"']""",r"""\arrow[r, leftrightarrow, "(e)"',color=blue]""",'Mark the hand-drawn equivalence arrow labelled e.'),
 (r"""\arrow[r, leftrightarrow, "(d)"']""",r"""\arrow[r, leftrightarrow, "(d)"',color=blue]""",'Mark the hand-drawn lower-right equivalence arrow labelled d.'),
 ("d) R. Brown and P. J. Higgins, 'The equivalence of $\\infty$-groupoids and", "d) R. Brown and P. J. Higgins, 'The equivalence of $\\unsure{\\infty}$-groupoids and",'The symbol in the reference is heavily blotted or overtyped. Infinity is plausible but not visually secure in that occurrence; retain it as an explicit doubt instead of silently using the expected title.'),
 (r'\mspage{\hand{119}}',r'\margin{119}','The handwritten lower-left 119 is archive pagination; the original typed heading -2- is retained separately.')
],doubts={},notes=[
 'The infinity-like sign before -groupoids in reference d is a dense overprint. The image does not identify an older omega or securely settle the final infinity; a doubt mark is added to that occurrence.',
 'The darker groupoids and Esquisses retain clear letters. They are typed overprints or heavy typing, without a separate readable cancelled word or a pen replacement.',
 'The handwritten archive folio 119 is retained in the margin, distinct from the typed -2- at the head.',
 'Small isolated marks above the text and to the left of reference d have no lexical or insertion structure. The seven diagram connections, in contrast, have clearly hand-drawn shafts and arrowheads and are now marked as such.'
],summary='Both scan halves and enlarged diagram/reference crops inspected. The six categories and seven bidirectional equivalences match the diagram; the arrows are handwritten and their labels typed. The restriction on crossed-complex homotopy types is retained literally. Added one visual doubt at the blotted symbol in reference d; no older symbol is invented.')
