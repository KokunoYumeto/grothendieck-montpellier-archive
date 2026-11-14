import sys
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT

key='ps_134-3_057';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'\phi',r'\hand{\phi}').replace(r'\hat{}',r'^{\hand{\wedge}}')
 if new!=line:edits.append([line,new,'The phi symbols and raised presheaf carets on this line are handwritten; the typed words and base letters are retained.'])
edits += [
 [r'in $\hand{A}^{\hand{\wedge}}$',r'\over{o}{i}\over{n}{n} $\hand{A}^{\hand{\wedge}}$','The end of the line shows typed on corrected by a pen i and reinforced n before the handwritten A and caret.'],
 [r'\hand{I} \times \hand{\alpha}(C)',r'\over{I}{I}\,\underset{\illegible{1}}{\over{x}{x}}\,\hand{\alpha}(C)','I and the product x are pen retracings of typed characters. A separate small mark remains below the x; retain its actual position as unreadable rather than silently discard it or assign a mathematical index.']
]
save_review({
 'key':key,'edits':edits,
 'diffs':{
  2480:[r'$A_{/C}$\hand{\unsure{,}}(NB','The small mark is a dark left-pointing wedge/curved stroke before the opening parenthesis. Its punctuation value remains uncertain; retain the doubtful comma.'],
  2482:['thus we get the functor','The article is visibly the, not a.'],
  2487:[r'$n\hand{\to}\hand{\Delta}_n$','The source arrow has no vertical tail bar; retain the plain arrow rather than the witness mapsto.'],
  2491:['is obtained by associating to','The typed word clearly ends associating, as the source sentence requires; the witness’s associated is not adopted.']
 },
 'unsure':[[r'\unsure{,}','The enlarged mark resembles an angle or heavy comma. The image does not decide between punctuation and a small correction stroke.']],
 'illegible':[],
 'notes':[
  'The small pre-parenthesis mark was enlarged and remains doubtful; it is not silently replaced by a conventional comma.',
  'The listed words have legible final type readings despite double impressions. The source spellings would’nt and standart and the final comma before Now remain unchanged.',
  'Both I and x are pen-retraced type. A separate lower mark is preserved as an unreadable mark beneath the product symbol, without supplying an inferred index.',
  'The a is handwritten and the thick mapsto is handwritten over a crowded earlier impression. No independent old letter can be read safely; the mapping and final symbol are retained.'
 ],
 'evidence':'Both full scan halves read, followed by enlarged comma, I-x, a-mapsto, in-A and standart details. The comparison functor evaluates p at the chosen final element e_a; the slice argument reduces asphericity to targets C having final elements, and the alpha-image of their interval homotopy finishes the proof. The source uses a plain n-to-Delta_n arrow and literally says associating and it’s facettes. All phi symbols and presheaf carets are pen additions. The crowded product expression retains its unresolved lower mark; the punctuation before NB is still doubtful.'
})

key='ps_134-3_058';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'A\^{}',r'$A^{\hand{\wedge}}$').replace(r'A\hat{}',r'A^{\hand{\wedge}}')
 if new!=line:edits.append([line,new,'The A carets are handwritten raised wedges; repair the free/empty accent while retaining the deleted or live status of the surrounding text.'])
edits += [
 [r'\varinjlim_{b \text{ in } A_{/a_u}}',r'\underset{b \text{ in } A_{/a_u}}{\underset{\hand{\longrightarrow}}{\mathrm{lim}}}','The word lim is typed, with a separate handwritten rightward arrow below; retain that mixed provenance in the direct-limit notation.'],
 [r' I \times F',r' I\mathrm{x}F','The product character in the deleted homotopy display is a typed lowercase x, not a multiplication glyph.'],
 [r'\unsure{(\alpha(\Delta_1))}',r'\unsure{(\hand{\alpha}(\hand{\Delta}_1))}','The cancelled Greek letters are handwritten. The old expression remains uncertain because dense cancellation crosses the parentheses and letters.'],
 [r'\unsure{\alpha(\Delta_1)}',r'\unsure{\hand{\alpha}(\hand{\Delta}_1)}','The second cancelled expression also has pen Greek letters and a typed index; retain the uncertain reading.'],
 [r'\hand{\unsure{\longmapsto|\to}}',r'\hand{\longmapsto}','The enlarged arrow has a definite vertical tail bar. The page uses mapsto in this position, even though the usual arrow is intended.'],
 [r'\inserted{above,}',r'\inserted[typed]{above}','above is typed; the apparent comma is the raised right end of its placement curve.'],
 [r'\inserted{\unsure{empty or,}}',r'\inserted{empty or}','The handwriting clearly reads empty or, with no independent comma; its placement curve ends in an upturned hook.'],
 [r'\over{\unsure{p}}{\S}.\over{\unsure{5}}{3}6',r'\over{p}{\S}.\over{5}{3}6','The old p loop and 5 outline are visible under the handwritten section sign and 3, giving the corrected reference §.36.'],
 [r'bec\over{o}{a}me\unsure{s}',r'bec\over{o}{a}mes','The final typed s is intact, not cancelled. The resulting literal becames is retained as an authorial grammatical slip.']
]
save_review({
 'key':key,'edits':edits,
 'diffs':{
  2495:[r'\margin{*}','The first-line margin has a large pencil star.'],
  2496:[r'follows:\hand{..} \hand{(42).}','The continuation dots, parenthesized 42 and final period are visibly handwritten after follows.'],
  2497:[r'\margin{\unsure{cor. inst ci-dessous}}','Rotated and enlarged the pencil note: Cor. and the ci- continuation can be recognized, but the abbreviation and final directional word remain too faint for a secure reading.'],
  2498:[r'\deleted{Corollary ... of course).}','Long oblique pencil strokes cancel the entire corollary and its proof through the final of course line. The new dated section below is not included in the cancellation.'],
  2500:[r'$C_u\hand{\cap}C_o$','The actual sign is a small rounded intersection cap with two legs, not a composition circle.'],
  2501:[r'$F\hand{\longmapsto}e$','The vertical stroke at the left end is clear in the enlargement. Retain the source mapsto despite the witness’s ordinary arrow.','correct transcription'],
  2503:[r'\inserted[typed]{above}','The word is typed and the curve’s upturned endpoint is not a comma.','correct transcription'],
  2504:[r'$a_u$ is \inserted{empty or} in A','The handwritten second word is or; the witness omits it. No independent comma follows the insertion.','correct transcription'],
  2505:['first thing','The source has no preceding the.'],
  2507:[r'\over{p}{\S}.\over{5}{3}6','The pen changes the old page reference p.56 to §.36; the old letters/numerals remain visible.'],
  2510:['when defining test categories','The source clearly types defining, not defined.'],
  2514:[r'bec\over{o}{a}mes','The o-to-a change is visible but the final s is not struck, leaving the literal becames. Preserve this apparent authorial slip rather than silently conjugating it.','correct transcription']
 },
 'unsure':[
  [r'\unsure{cor. inst ci-dessous}','The rotated faint marginal abbreviation and directional phrase cannot be settled; retain doubt.'],
  [r'\unsure{(\hand{\alpha}(\hand{\Delta}_1))}','The old parenthesis/Greek-letter cluster is heavily crossed. Its outline is compatible with the transcription, but not clear enough to remove doubt.'],
  [r'\unsure{\hand{\alpha}(\hand{\Delta}_1)}','The second small cancelled formula is similarly obscured; preserve it as a tentative reading.'],
  [r'\longmapsto','The arrow has a clear upright tail bar.'],
  ['empty or','The cursive r is visible, while the supposed comma belongs to the placement line.'],
  ['p','The old loop/descender of p is visible under the section sign.'],
  ['5','The old 5 outline survives at the right of the replacement 3.'],
  ['s','The final s is typed and uncancelled.']
 ],'illegible':[],
 'notes':[
  'Rotated the margin note and retained its uncertainty; no conjectural expansion has entered the source.',
  'Both old formula clusters are visibly cancelled and still uncertain. Their Greek characters are pen additions and are now marked accordingly.',
  'The insertion reads empty or without a punctuation comma, and the earlier insertion above is typed.',
  'The final s is not struck. The source’s resulting becames is retained and recorded explicitly.',
  'The right edge visibly cuts through the final t-like letter of repet; the next line begins tition). Preserve the clipped source without supplying a guessed hyphen or normalized repetition.',
  'The first F-to-e arrow has a tail bar, while the later one on the following line is an ordinary arrow. Both are retained distinctly.'
 ],
 'evidence':'Both complete halves opened and inspected, with nine enlarged details including the rotated margin. The entire corollary and proof are cancelled by long diagonal strokes, ending before 21.3 and section 37. Its set operation is intersection and the first F-to-e sign is literally mapsto. The above insertion is typed; empty or is handwritten and lacks an independent comma. The new section changes p.56 to §.36, speaks of defining test categories, and leaves a typed final s after the o-to-a correction in becames. The margin, two inner deleted formula readings and the clipped word ending retain their limitations.'
})
