from review_root import review

k='ps_134-2_026'
review(k,changes=[
    ('\\mspage{7}\n\\margin{\\deleted{\\illegible{1}} 12}',r'\margin{7}\mspage{\deleted{\illegible{1}} \hand{12}}','The left 7 is a pen margin number; the centered current folio is handwritten 12 after an unreadable cancelled mark.'),
    (r'$S_i = D_{i+1}$',r'$S_i = \dot{D}_{i+1}$','A small dot is clearly printed above D in the first boundary equality; the initial transcription omitted it.'),
    (r'$(\phi_i^+ , \phi_i^-)$',r'$(\hand{\varphi}_i^+ , \hand{\varphi}_i^-)$','The two phi letters of the pair are handwritten with the open-loop varphi form.'),
    (r'\unsure{$\mathring{D}_i$|$D_i$}',r'$\dot{D}_i$','The enlargement shows a small dot above D, substantially smaller than the open-cell rings below; the boundary notation is dotted D.'),
    (r'$\phi_i^+ , \phi_i^-$ to',r'$\hand{\varphi}_i^+ , \hand{\varphi}_i^-$ to','The phi letters in the next occurrence are also written by hand.'),
    (r'S_{i-1} \simeq S_i^+ \cap S_i^-',r'S_{i-1} \hand{\simeq} S_i^+ \hand{\cap} S_i^-','The equivalence and intersection signs are hand-drawn.'),
    (r'\unsure{$\leq$|$<$}',r'$\hand{<}$','The right-hand bound has a clear strict handwritten less-than sign, with no lower equality stroke.'),
    (r'D_j \longrightarrow D_n',r'D_j \hand{\longrightarrow} D_n','The map arrow is handwritten.'),
    (r'\phi_{n,j}^+ , \phi_{n,j}^- : D_j \rightrightarrows D_n',r'\hand{\varphi}_{n,j}^+ , \hand{\varphi}_{n,j}^- : D_j \hand{\rightrightarrows} D_n','The phi letters and parallel arrows are handwritten in the iterated-map display.'),
    (r'\unsure{$\mathring{D}_n$|$D_n$}',r'$\mathring{D}_n$','The larger hollow ring is clearly visible above the open D_n.'),
    (r'\unsure{$\mathring{S}_j^+$|$S_j^+$}',r'$\mathring{S}_j^+$','The positive hemisphere has a clear hollow ring above S.'),
    (r'$\phi_{n,j}^+(D_j)$',r'$\hand{\varphi}_{n,j}^+(\mathring{D}_j)$','The positive map is handwritten and its argument D_j carries a clear hollow ring, omitted in the initial transcription.'),
    (r'\unsure{$\mathring{S}_j^-$|$S_j^-$}',r'$\mathring{S}_j^-$','The negative hemisphere also carries a clear ring above S.'),
    (r'$= \phi_{n,j}^-(D_j)$',r'$= \hand{\varphi}_{n,j}^-(D_j)$','The negative phi is handwritten. No ring is visible above its argument D_j; that asymmetry is retained and noted in the guide.'),
    (r'cell\inserted{in this decomposition}',r'cell \inserted[typed]{in this decomposition}','The interlinear words are typewritten, with a pen insertion curve; their word boundary after cell is retained.'),
    (r'D_n \longrightarrow (D_n , S_j^+) \amalg_{D_j}',r'D_n \hand{\longrightarrow} (D_n , S_j^+) \hand{\amalg}_{D_j}','The arrow and amalgamation sign are handwritten.'),
    (r'condition \unsure{$*$}',r'condition \deleted{\unsure{$*$}}','The mark after condition is crossed by diagonal pen strokes. Its underlying star-like reading remains doubtful, but its cancellation must be represented.'),
    ('\\xout{\\illegible{1}}\ninto demanding',r'\xout{\unsure{to S}}'+'\ninto demanding','The cancellation under the preceding line suggests to S; the reading remains tentative rather than being treated as fully legible.'),
    (r"standar\over{\unsure{t}}{d}''",r"standar\over{t}{d}''",'The typed t and pen d of the first standard correction are distinct in the scan.'),
    (r'\ar[dr, no head]',r'\ar[dr, no head, color=blue]','The right side of the handwritten triangle has no arrowhead; mark its pen provenance in the rendered diagram.'),
    (r'\ar[ur, no head] \ar[rr, no head]',r'\ar[ur, no head, color=blue] \ar[rr, no head, color=blue]','The other two sides are plain pen strokes, not the arrows printed in the comparison witness.'),
    (r'\ar[r, no head, bend left] \ar[r, no head, bend right]',r'\ar[r, no head, bend left, color=blue] \ar[r, no head, bend right, color=blue]','The two semicircles are plain handwritten curves without arrowheads.'),
    (r'\xout{\unsure{enough}} (I expect)',r'\xout{enough} (I expect)','The first cancelled enough is legible beneath the typewriter x strokes.'),
    (r'(I expect) \xout{\unsure{enough}}',r'(I expect) \xout{enough}','The second cancelled enough is likewise legible.'),
    (r'standar\over{\unsure{t}}{d}ness',r'standar\over{t}{d}ness','The second terminal t corrected to pen d is clear.')
],doubts={'unsure':[
    (r'$\dot{D}_i$','doubt resolved','A small dot appears above D_i, distinct in size from the hollow open-cell rings.'),
    (r'$\hand{<}$','doubt resolved','The final bound is a strict handwritten less-than sign.'),
    (r'$\mathring{D}_n$','doubt resolved','The open D_n has a clear hollow ring.'),
    (r'$\mathring{S}_j^+$','doubt resolved','The positive open hemisphere has a clear hollow ring.'),
    (r'$\mathring{S}_j^-$','doubt resolved','The negative open hemisphere has a clear hollow ring.'),
    (r'\deleted{\unsure{$*$}}','doubt retained','Diagonal pen hatching cancels the small sign; its underlying character cannot be resolved securely.'),
    (r'\over{t}{d}','doubt resolved','The first old typed t is visible beneath the pen d.'),
    (r'\xout{enough}','doubt resolved','All six letters of the first enough are recoverable under the x-out.'),
    (r'\xout{enough}','doubt resolved','The second enough repeats the same legible cancelled word.'),
    (r'\over{t}{d}','doubt resolved','The second old typed t remains distinct beneath its pen correction.'),
    (r'\over{\unsure{f}}{f}','doubt retained','The live pen f is clear, but the overlaid earlier letter is not securely distinguishable.')
],'illegible':[
    (r'\deleted{\illegible{1}}','illegible retained','The old numeral before the centered 12 is densely scribbled out.'),
    (r'\xout{\illegible{1}}','illegible retained','The cancelled small expression before the positive phi in the open-cell formula remains unreadable.'),
    (r'\xout{\unsure{to S}}','doubt retained','The cancelled short expression resembles to S but its last character and spacing remain uncertain.'),
    (r'\xout{\illegible{3}}','illegible retained','The long cancellation after the order ell-minus-one operation remains too entangled with x strokes to reconstruct confidently.'),
    (r'\xout{\illegible{1}}','illegible retained','The word below the interlinear typed formulation cannot be securely recovered.')
]},notes=[
    'The left 7, centered 12 and lower-left 26 are handwritten. The old character preceding 12 remains unreadable.',
    'The first equality does have a small dot above D_{i+1}; it is restored. The later boundary D_i also has a small dot.',
    'The open-cell D_n and both S_j symbols have clear hollow rings. A ring is also present on the positive-map argument D_j; no corresponding ring is visible on the negative-map argument.',
    'Both enough cancellations are now resolved. The earlier short cancellation is tentatively to S; the long three-word cancellation, old formulation word and small cancelled expression in the open-cell formula remain marked.',
    'The mark after condition is cancelled by diagonal pen strokes and remains unreadable as an underlying symbol. The live f of for is clear but its typed underletter remains doubtful.',
    'The marginal composition sign with n above and ell below is present as transcribed. The iterated-map arrows, amalgamation sign and diagram edges are handwritten.'
],summary='Both halves and eight detail crops inspected. Restored boundary dots and four open-cell rings, resolved the strict upper bound j<i and both enough cancellations, distinguished the typed interlinear insertion, and retained undeciphered underlayers. The negative open-cell formula has no visible ring on its D_j argument; this source asymmetry is preserved. All diagram edges are undirected pen strokes.',differences={
    238:('hand-drawn triangle and circle with dots, plain lines','the typescript reads as our transcription','Neither the triangular edges nor the two semicircular arcs have arrowheads. The witness adds directed arrows.'),
    244:(r'$(0 \leq j$ $\hand{<}$ $i)$','our transcription corrected','The final inequality is strictly less than, clear in pen. The witness prints less-than-or-equal.'),
    245:(r'$\mathring{D}_n$, $\mathring{S}_j^+=\hand{\varphi}_{n,j}^+(\mathring{D}_j)$, $\mathring{S}_j^-=\hand{\varphi}_{n,j}^-(D_j)$','our transcription corrected','The open-cell rings are visible on D_n, both hemisphere symbols and the first D_j argument; the witness omits them. The second argument lacks a visible ring and is left unchanged.'),
    246:(r'$S_{i-1}=\dot{D}_i$','our transcription corrected','The enlarged image resolves a small boundary dot above D_i, rather than no mark or the larger hollow open-cell ring.')
})
