from review_root import review

review('brown_134-2_125',changes=[
 (r'C_{n+1} \xrightarrow{F}',r'C_{n+1} \hand{\xrightarrow{\textcolor{black}{F}}}','The displayed arrow is drawn by hand; the F above it remains typed.'),
 (r'C \xrightarrow{F}',r'C \hand{\xrightarrow{\textcolor{black}{F}}}','The second long F-labelled arrow is also hand drawn, independently of the typed label.'),
 (r'\Gamma_{\unsure{x|\times}}',r'\Gamma_{\times}','The enlarged subscript is a plain four-armed cross, matching the cross on site 124 and distinct from the serifed X used in the other formulas.'),
 (r'\mspage{\hand{126}}',r'\margin{126}','The handwritten lower-left 126 is the archive folio, separate from the typed heading - 4 -.')
],doubts={'unsure':[(r'\times','doubt settled','The enlarged crop resolves the shape as a cross; no serifed capital X is visible. The literal mark is retained rather than normalized from context.')]},notes=[
 'The t of strict is heavily typed or overtyped but the word is clear. No different underlying letter can be securely recovered.',
 'The subscript is a plain cross, now settled as times; the other Gamma subscripts are serifed X. This source inconsistency is retained.',
 'The first C in C-double-struck-C-F is plain, while the next is double struck. The existing distinction is correct.',
 'The irregular closing mark at the end of the first line is a typed right square bracket after a full stop, as transcribed.',
 'The handwritten archive folio 126 is now represented as a margin annotation.'
],summary='Both halves and enlarged Gamma detail inspected. The literal phrase one knows it fails is clearly typed even though the French source at site 53 says on a fait ce qu’il fallait; the translation discrepancy is explained in the guide and not silently corrected. The cohomological ranges, mixed C typography, two hand-drawn arrows, and cross-shaped Gamma subscript are preserved. No visual doubts remain.')

review('brown_134-2_126',changes=[
 (r'C_{n+1} \longrightarrow D_{n+1}',r'C_{n+1} \hand{\longrightarrow} D_{n+1}','Mark the hand-drawn long arrow, keeping the typed domain and codomain.'),
 (r'C_n \longrightarrow D_n',r'C_n \hand{\longrightarrow} D_n','The truncation arrow is drawn by hand and is marked accordingly.'),
 (r'((n-1)\text{-Cat})) \longrightarrow \mathit{Hom}',r'((n-1)\text{-Cat})) \hand{\longrightarrow} \mathit{Hom}','The long comparison arrow between Hom expressions is hand drawn.'),
 (r'D_{n+1} \longrightarrow (n\text{-Cat})',r'D_{n+1} \hand{\longrightarrow} (n\text{-Cat})','The long local-system arrow is hand drawn.'),
 (r'\arrow[r] \arrow[d, equal, "\text{def.}"]',r'\arrow[r,color=blue] \arrow[d, equal, "\text{def.}",color=blue]','The diagram arrow and the vertical equality strokes are drawn by hand; the def. label stays typed.'),
 (r'\arrow[d, equal, "\text{def.}"]',r'\arrow[d, equal, "\text{def.}",color=blue]','The second vertical equality likewise has two drawn strokes and a typed definition label.'),
 (r"``\v{C}echist''",r"``$\overset{\hand{\scriptscriptstyle\vee}}{\mathrm C}$echist''",'The first hacek is a dark pen addition above the typed C; mark the accent alone as handwriting.'),
 (r'(b) viewpoint \v{C}echist',r'(b) viewpoint $\overset{\mathrm v}{\mathrm C}$echist','The second accent is a typed lower-case v placed above the C, visibly taller than the first pen accent; preserve that layered typing.'),
 (r'\mspage{\hand{127}}',r'\margin{127}','The handwritten 127 is lower-left archive pagination, distinct from the typed - 5 - heading.')
],doubts={},notes=[
 'The phrase (n+1)-functor is in a raised or heavier typed face. There is no pen insertion cue or recoverable earlier wording; ordinary typed text is retained.',
 'Enlarged crops distinguish a dark hand-added first hacek from a typed v above the second C. Both accents are now represented with their visible provenance.',
 'The r in there sits low but is part of the typed word; no different reading is supported.',
 'The tiny spot between the and coefficients is irregular and has no typewriter punctuation shape; no stop is added to the text.',
 'The Hom labels and the emphasized words are italic typing. The diagram and long formula arrows, by contrast, have drawn shafts and heads; the vertical definition signs have drawn parallel strokes.',
 'The handwritten archive 127 is retained in the margin.'
],summary='Both halves and enlarged accent details inspected. Conditions A′ and B′ remain literal, including the right lower Gamma expression with argument F rather than an explicit pulled-back F. The concluding three-way comparison and signature are complete. Long drawn arrows/equality strokes and the two different accent constructions are distinguished from typing; there are no doubt marks.')
