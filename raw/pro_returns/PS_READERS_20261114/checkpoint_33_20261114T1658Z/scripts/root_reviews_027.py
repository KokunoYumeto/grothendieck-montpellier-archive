from review_root import review

k='ps_134-2_027'
oldmargin=r"\margin{\unsure{Salut}? \unsure{Absurde} \diagram{\begin{tikzpicture}\draw (0,0) circle (0.8); \draw (-0.8,0)--(0.8,0); \draw (0,0)--(0.55,0.58); \node at (-0.3,0.35) {$f$}; \node at (0.45,0.15) {$f'$}; \node at (0,-0.4) {$f''$}; \node at (0.95,0.2) {$S'$};\end{tikzpicture}} $f \cap f'' = S_0$}"
newmargin=r"\margin{\unsure{Just|But}, see this \diagram{\begin{tikzpicture}[draw=blue,text=blue]\draw (0,0) circle (0.8); \draw (-0.8,0)--(0.5657,0.5657); \draw (-0.8,0) .. controls (-0.3,-0.55) and (0.6,-0.5) .. (0.5657,0.5657); \node at (-0.25,0.4) {$f$}; \node at (0.03,0.03) {$f'$}; \node at (0.05,-0.55) {$f''$}; \node at (-0.95,-0.05) {$s$}; \node at (0.78,0.65) {$s'$};\end{tikzpicture}} $f \cap f'' = \{s,s'\} = S_0$}"
review(k,changes=[
    (r'\mspage{\deleted{\illegible{1}} 13}',r'\mspage{\deleted{\illegible{1}} \hand{13}}','The live centered folio 13 is handwritten; the preceding cancelled number remains unreadable.'),
    (r"\unsure{$\varinjlim$'s}",r"$\varinjlim$'s",'The handwritten lim has a right-pointing arrow below and an explicit apostrophe-s after it.'),
    (r'X_i \simeq D_{n(i)}',r'X_i \hand{\simeq} D_{n(i)}','The displayed equivalence sign is handwritten; the typed subscript i on X is plainly present.'),
    (r'\margin{(\unsure{12}!)).}',r'\margin{(12!)).}','The raised marginal number 12 is clear; the accompanying exclamation and closing curves are retained.'),
    (r'standar\unsure{t}-%',r'standar\unsure{\over{t}{d}}-%','The last letter has a pen correction over the typed t. The overlaid d-like reading remains marked because the descending stroke is not completely separable.'),
    (oldmargin,newmargin,'The words see this are legible; the first word is uncertain between Just and But, with dense pencil hatching. Two arcs join the same boundary endpoints, making three regions f, f-prime and f-double-prime, not a central triple junction. The endpoint labels s, s-prime and the formula term {s,s-prime} are restored. A second visual reading independently confirmed the topology and formula.'),
    (r'$S_j^{\hand{\varepsilon}} \to X(i-1)$',r'$S_j^{\hand{\varepsilon}} \hand{\to} X(i-1)$','The attachment arrow is handwritten.'),
    (r"\inserted{$\varphi^{\unsure{\varepsilon'}}_{n(i)}$}",r"\inserted{$\varphi^{\unsure{\varepsilon'}}_{n(i')}$}",'The small prime inside the lower parenthesis is visible in the enlarged right-margin insertion.'),
    (r"\margin{$\varphi^{\varepsilon'}_{n(i),j}$}",r"\margin{\textcircled{$\varphi^{\varepsilon'}_{n(i),j}$}}",'The first left-margin formula is enclosed by a pen circle.'),
    (r'$S_j^{\hand{\varepsilon}} \simeq D_j$',r'$S_j^{\hand{\varepsilon}} \hand{\simeq} D_j$','This equivalence sign is drawn by hand.'),
    (r"\margin{$S^{\varepsilon'}_j$}",r"\margin{\textcircled{$S^{\varepsilon'}_j$}}",'The second left-margin formula is also circled.'),
    (r"$X_{i'} \simeq D_{n(i')}$",r"$X_{i'} \hand{\simeq} D_{n(i')}$",'The comparison with the earlier cell has a handwritten equivalence sign.'),
    (r'in terms of fiber',r'in terms\hand{\unsure{$\vert$}} of fiber','The pen stroke after terms is visible and absent from the initial transcription. Its function is uncertain; it is retained as a doubtful vertical mark.'),
    (r'$i \mapsto n(i) : I \to \underline{N}$',r'$i \hand{\mapsto} n(i) : I \hand{\to} \underline{N}$','The mapping and category arrows are drawn by hand.'),
    (r'\inserted{-object of}',r'\inserted[typed]{-object}\inserted{ of}','The interlinear -object is typed; the following of is penned at the insertion point. These two layers must not both be classified as handwriting.'),
    (r'\inserted{P=}',r'\inserted[typed]{P=}','The interlinear P= immediately above the large product sign is typewritten, unlike the handwritten copy in the margin.'),
    (r'\mspage{27}',r'\mspage{\hand{27}}','The lower-left archive number is handwritten.'),
    (r"two signs $\varepsilon,\varepsilon'$)}",r"two signs $\varepsilon,\varepsilon'$.)}", 'A small handwritten period is visible immediately before the closing parenthesis.')
],doubts={'unsure':[
    (r'\unsure{1}','doubt retained','The tiny upper-right mark is very faint and may be a numeral or incidental mark.'),
    (r"$\varinjlim$'s",'doubt resolved','The arrow below lim and the terminal apostrophe-s are clear.'),
    (r'\xout{\unsure{s}}','doubt retained','The final character of subsets is overwritten by an x; the older s remains plausible but not fully separable.'),
    ('12','doubt resolved','The two raised digits of the marginal reference are clear.'),
    (r'\xout{\unsure{s}}','doubt retained','The character after cell is x-struck; its underlying shape is not fully recovered.'),
    (r'\hand{\unsure{ion}}','doubt retained','The pen ending is partly cut off at the right image edge; its final strokes remain uncertain.'),
    (r'\unsure{\over{t}{d}}','doubt retained','There is a clear overprint, but the final pen letter is still marked as d-like rather than assumed from the expected word.'),
    (r'\unsure{Just|But}','doubt retained','The initial marginal word is obscured by pencil hatching. Just and But are plausible; the original Salut is unsupported.'),
    ('see this','doubt resolved','The two separate words above and right of the diagram read see and this, not Absurde.'),
    (r'\unsure{Dells|cells}','doubt retained','The first letter has a D-like dark body with a faint overlaid arc, preventing secure distinction from an overwritten c.'),
    (r'\xout{\unsure{,}}','doubt retained','The x after constructed obscures its underlying punctuation.'),
    (r"\unsure{\varepsilon'}",'doubt retained','The raised sign over the right-hand phi remains cramped and partly occluded; epsilon-prime is plausible.'),
    (r'\hand{\unsure{,}}','doubt retained','The small mark between can and be is visible but cannot confidently be separated from the nearby insertion stroke.')
],'illegible':[
    (r'\deleted{\illegible{1}}','illegible retained','The old centered folio preceding 13 is densely blacked out.'),
    (r'\deleted{\illegible{3}}','illegible retained','The first long handwritten cancellation under the triviality clause remains unreadable beneath the zigzag strike.'),
    (r'\deleted{\illegible{2}}','illegible retained','The following cancelled handwritten words are also inseparable from the long pen strike.')
]},notes=[
    'The old folio before the clear handwritten 13 remains unreadable; the faint upper-right mark is still doubtful, and the lower-left 27 is pen numbering.',
    'The insertion says rather, finite lim apostrophe-s, with the right-pointing limit arrow; the terminal apostrophe-s is clear and retained.',
    'The undercharacters after subset, cell and constructed remain doubtful beneath their x-outs.',
    'The final letter of standart has a pen overprint, now recorded with its d-like replacement still doubtful. Both longer handwritten cancellations remain illegible.',
    'The marginal phrase has see this, preceded by an uncertain Just/But. Its pencil hatching does not securely establish cancellation. The figure has two interior arcs sharing two endpoints, not three central sectors; the endpoint set {s,s-prime} in the intersection formula is restored.',
    'The pen tick after terms is now represented by a doubtful vertical stroke, rather than silently omitted.',
    'The small can/be mark remains doubtful because of the nearby insertion line.',
    'The right-hand phi insertion has n(i-prime) below; its raised epsilon-prime remains doubtful. The two circled left-margin formulas and their pointers are retained at their related lines.'
],summary='Both halves and fourteen enlarged details reviewed; the marginal words and diagram also received an independent second reading. Corrected the counterexample topology and restored its endpoint set, resolved lim apostrophe-s and marginal 12, distinguished typed -object and P= from pen additions, restored the final handwritten period, and marked the unexplained tick after terms. The pen letter at the end of standart, Dells/cells overprint and cancelled passages remain doubtful.',differences={
    247:(r"\inserted{(rather, finite $\varinjlim$'s)}",'our transcription corrected','The scan clearly includes apostrophe-s after the handwritten limit notation; the witness omits that ending.'),
    248:('amalgamated sums','the typescript reads as our transcription','The typed quotation has plural sums, not the witness singular sum.'),
    249:(r'$X_i\hand{\simeq}D_{n(i)}$','the typescript reads as our transcription','The subscript i after X is plainly visible; the witness omits it.'),
    252:(r'\margin{(12!)).}','our transcription corrected','The handwritten marginal reference 12 and following marks are present and the number is now resolved.'),
    253:(newmargin,'our transcription corrected','The scan has an uncertain initial word followed by see this, a three-region picture with two shared endpoints, and f intersection f-double-prime equals {s,s-prime} equals S_0. The witness rewrites this as prose. The initial transcription had the wrong diagram topology and omitted the endpoint set.'),
    254:(r'\deleted{\illegible{3}} / \deleted{\illegible{2}}','the typescript reads as our transcription','Both crossed handwritten passages are visible but remain unreadable; the witness does not retain their cancellation layers.'),
    260:(r'$S_j^{\hand{\varepsilon}}\hand{\to}X(i-1)$','the typescript reads as our transcription','The handwritten signs are epsilon, not the witness xi; the source notation is retained.'),
    262:(r"\margin{\textcircled{$\varphi^{\varepsilon'}_{n(i),j}$}}",'our transcription corrected','The first left-margin correction is circled and contains the additional lower j; the witness has no separate marginal notation.'),
    263:(r"with\inserted{$S^{\varepsilon'}_j$} one",'the typescript reads as our transcription','The inserted cell label has epsilon-prime; the witness substitutes an unprimed xi.'),
    266:(r'$\inserted[typed]{P=}\hand{\prod_{i\in I}}F_{n(i)}$','our transcription corrected','The object letters are F, not the witness D. The interlinear P= is typed and the product is handwritten.'),
    267:(r'\margin{$P=\prod_{i\in I}F_{n(i)}$}','the typescript reads as our transcription','The separate handwritten formula is present at the left margin and is not independently represented in the witness.'),
    269:('can be numbered','the typescript reads as our transcription','The typed participle is numbered, not numbers.'),
    272:(r"g(u_{i'})",'the typescript reads as our transcription','The prime belongs to the subscript i in the scan; the witness moves it outside that subscript.'),
    273:('source or target maps','the typescript reads as our transcription','The typed conjunction is or, not of.'),
    275:(r"$\varepsilon,\varepsilon'$",'the typescript reads as our transcription','Both handwritten letters are epsilon, with a prime on the second; the witness changes them to xi.'),
    276:(r"$\varepsilon,\varepsilon'$.)",'our transcription corrected','The enlargement shows a small handwritten period before the closing parenthesis. The original transcription omitted it; the witness punctuation agrees with the scan.')
})
