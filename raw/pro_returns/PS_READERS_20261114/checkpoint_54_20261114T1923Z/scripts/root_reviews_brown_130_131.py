from review_root import review
from brown_comparison import record

review('brown_134-2_130',changes=[
 (r'L_1 \xrightarrow{\ d\ } L_0',r'L_1 \mathrel{\overset{d}{\hand{\longrightarrow}}} L_0','The long shaft and head are drawn by hand; the label d and both objects are typed.'),
 (r'L_0 \longrightarrow \mathrm{Aut}',r'L_0 \hand{\longrightarrow} \mathrm{Aut}','The second long arrow is drawn by hand, unlike its surrounding typed symbols.'),
 (r'\theta(d(x_1))',r'\theta(d(x_1)\unsure{)|\hand{)}}','The outer closing parenthesis is visibly thickened. Its character and position are clear, but the image does not distinguish repeated typing from pen retouch; preserve this provenance uncertainty.')
],doubts={},notes=[
 'The lower-left 131 is a handwritten archive folio; its existing margin placement is correct.',
 'An enlarged crop confirms two closing parentheses in the correct order. The second is heavier and irregular; typed-versus-handwritten provenance remains uncertain and is now marked without changing the formula.',
 'The isolated short mark beyond axiom (a) has no attachment, matching footnote, or legible character structure. It is treated as a stray mark, not a mathematical minus or reference.'
],summary='Both halves, enlarged parenthesis detail, and all 12 supplemental witness rows inspected. The crossed-module equations have their literal dot and correctly placed parentheses. The text says or commutative formal groups, not the later and. Both long arrow shafts are handwritten; uncertainty concerns only the retouched closing parenthesis. No later Brown/Conduche note is inserted.')
record('brown_134-2_130',exceptions={51:(r'\theta(d(x_1)\unsure{)|\hand{)}} = \mathrm{int}(x_1)', 'our transcription corrected','Both parentheses are present in the correct positions in the scan. The misplaced parenthesis in the witness is not adopted. Only the outer parenthesis provenance remains doubtful: its heavier outline could be retouched by pen or repeated typing.')})

review('brown_134-2_131',changes=[
 (r'\mspage{\hand{132}}',r'\margin{132}','The handwritten 132 is lower-left archive pagination; the original typed heading is - 4 -.')
],doubts={},notes=[
 'The lower-left handwritten 132 is retained as an archive margin annotation, distinct from the typed page heading.',
 'The sparse marks above chain and the and the short detached dash below chain do not form letters, insertion cues, or cancellation strokes. They are scan/paper marks, not omitted wording.'
],summary='Both halves and all 11 supplemental witness rows inspected. All five short arrows of the noncommutative complex are typed and all indices are clear. The body says connected topological spaces without pointed. The bracketed sentence explicitly says that the biduality and homology commentary is omitted; the lower half is otherwise blank. That omission is part of this copy and is not filled from the revised 1983 version.')
record('brown_134-2_131')
