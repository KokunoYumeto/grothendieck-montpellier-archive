from review_root import review

review('brown_134-2_119',changes=[
 (r'from $\sigma\underset{\approx}{\Delta}^{n}$',r'from $\sigma\underset{\unsure{\sim|\hand{\sim}}}{\Delta}^{n}$','There is one continuous wavy stroke, not two, below Delta. Independent inspection agrees. Whether that stroke was typed or penned is not secure; retain both provenance alternatives within a doubt mark.'),
 (r'(i.e. $\sigma\underset{\approx}{\Delta}^{n}$',r'(i.e. $\sigma\underset{\unsure{\sim|\hand{\sim}}}{\Delta}^{n}$','The second under-Delta stroke is likewise a single wave. Its provenance remains uncertain and is marked, without changing the mathematical symbol to a double wave.'),
 (r'complex $\pi\underset{\approx}{\Delta}^{n}$',r'complex $\pi\underset{\unsure{\sim|\hand{\sim}}}{\Delta}^{n}$','The third under-Delta stroke is single; keep the unresolved typed-versus-handwritten provenance explicit.'),
 (r'of $\underset{\sim}{\Delta}^{n}$',r'of $\underset{\unsure{\sim|\hand{\sim}}}{\Delta}^{n}$','The last under-Delta mark is also a single wave. Its form is settled, but its typed-versus-handwritten provenance is not.'),
 (r'$\longrightarrow$ simplicial',r'$\hand{\longrightarrow}$ simplicial','The arrow has a drawn shaft and asymmetric hand-made head, matching the drawn arrows on the preceding page; the adjoining words remain typed.'),
 (r'\mspage{\hand{120}}',r'\margin{120}','The handwritten 120 is the lower-left archive folio, distinct from the original typed heading -3-.')
],doubts={},notes=[
 'The words to G are typed in darker ink or by overtyping; their letters are clear and no earlier alternative text is readable. They remain plain typed words.',
 'Enlarged crops and independent inspection show a single wave in all four occurrences, not a double-wave approximation symbol. Provenance cannot be securely settled, so each has explicit typed/handwritten alternatives under Delta.',
 'The word nerve and the French conference title are in an italic typeface; their existing textit markup is retained.',
 'The small mark at the t of still does not form a separate replacement or a readable cancelled letter. The word still is clear.',
 'The typed -3- remains the manuscript heading; handwritten 120 is retained as archive pagination in the margin.'
],summary='Both halves and all four enlarged under-Delta signs inspected. The single-wave notation is corrected and its uncertain provenance marked rather than guessed. The functor arrow is handwritten; to G is typing. The bibliography retains literal longeur and Astérixes. No inference from the published titles changes those spellings.')

review('brown_134-2_120',changes=[
 (r'\mspage{\hand{121}}',r'\margin{121}','The handwritten lower-left 121 is archive pagination, not a second original page heading.')
],doubts={'unsure':[(r'\unsure{Math,|Math.}','retain doubt','The punctuation after Math has a heavy round body and a small separated lower mark; the enlarged scan does not securely distinguish a comma from a full stop with a speck. Both readings remain marked.')]},notes=[
 'The enlarged punctuation after Math remains ambiguous between a comma and a full stop with a lower speck; the doubt is retained.',
 'U.K. is a clearly handwritten blue addition after the typed Gwynedd.; its existing hand markup is retained.',
 'The full pencilled item reads 11 A van Kampen Theorem for 2-cat-groups has now been proved by Brown and Loday. The expression 2-cat-groups is clear; no insertion cue ties it to an earlier line, so it remains an anchored marginal note below the date.',
 'The lower-left archive folio 121 is handwritten and is retained in the margin.',
 'The typed heading is -4-, unchanged.',
 'Both displayed relations have a tilde above two parallel horizontal strokes; the congruence symbols and the superscripts n and 0 are clear and retained.'
],summary='Both halves and enlarged Math punctuation inspected. The two classifying-space bijections and their too-abelian qualification are retained. The full handwritten item 11 and U.K. addition are legible. One punctuation doubt remains; archive pagination is distinguished from the typed folio.')
