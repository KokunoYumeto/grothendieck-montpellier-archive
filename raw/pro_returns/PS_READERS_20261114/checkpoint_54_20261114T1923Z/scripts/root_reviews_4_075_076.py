from review_root import review
from pathlib import Path

src=(Path(__file__).resolve().parents[2]/'inputs/text/transcription/ps_pages/ps_134-4_075.tex').read_text()
changes=[
 (r'this\xout{wxxx}',r'this\xout{weak}','The lower w, e, a and k remain visible beneath the regularly typed x strikes; the strike characters are not literal word letters.'),
 (r'\over{have}{\unsure{had}}',r'\over{have}{have}','The pen retracing has h, a, v and e; it has no final ascender of d. The earlier had reading is incorrect.'),
 (r'\over{may}{\unsure{may}}',r'\over{may}{may}','The pen m, closed a and long descending y are all readable over the typed may.'),
 (r'\xout{thatxthis}',r'\xout{that this}','The x between the words is one of the cancellation impressions across the interword space.'),
 (r'\hand{(}\inserted[typed]{otherwise}',r'\inserted[typed]{otherwise}','The apparent opening parenthesis is the left end of the curved insertion mark under otherwise; no independent parenthesis is present.'),
 (r'\margin{(horizontal line drawn by hand across the left margin)}',r'\margin{\rule{.9\linewidth}{.35pt}}','Replace the editorial description by the visible horizontal pen rule, preserving its marginal position.'),
 (r'W \subset \mathrm{F\unsure{l}}(M)',r'W \hand{\subset} \mathrm{F}\over{l}{\ell}(M)','The inclusion sign is pen, and the typed l has an added diagonal pen stroke.'),
 (r'\over{\illegible{1}}{b}',r'\over{\unsure{b}}{b}','A b-like old stem and lower bowl are visible under the pen b; narrow the unreadable word to that still-doubtful single letter.'),
 (r'\over{\illegible{1}}{of}',r'\over{of}{of}','Both typed bases o and f remain visible beneath the pen retracing, including the f crossbar and serifs.'),
 (r'\xout{Txextroublexwith}',r'\xout{T\raisebox{-0.3ex}{h}e trouble with}','The base reads The trouble with; x characters are cancellation impressions. The h of The is visibly lowered and is retained in that position.'),
 (r'f \sim g',r'f \hand{\sim} g','The homotopy tilde is a continuous dark pen stroke.')
]
for line in src.splitlines():
 if any(x in line for x in [r'\longrightarrow',r'\to']):
  changes.append((line,line.replace(r'\longrightarrow',r'\hand{\longrightarrow}').replace(r'\to',r'\hand{\to}'),'The arrows have continuous hand-drawn shafts and pen arrowheads.'))
review('ps_134-4_075',owner='134_4_tail',changes=changes,doubts={'unsure':[
 ('have','doubt resolved with corrected reading','The final pen word is have, with separate v and e and no d ascender.'),
 ('may','doubt resolved','The pen m, a and descending y can each be followed.'),
 (r'\over{l}{\ell}','doubt resolved','A diagonal pen stroke crosses a clear typed l.')
 ],'illegible':[
 (r'\unsure{b}','doubt narrowed','The old lower bowl suggests b, but the pen stroke conceals too much to settle it.'),
 ('of','doubt resolved','The typed o and f remain separately visible beneath the pen retracing.')
 ]},notes=[
 'The live word is this. The following cancelled word reads weak beneath x overstrikes, now transcribed as the old text rather than literal x letters.',
 'The pen word is have, not had. The added d, opening parenthesis and closing parenthesis around independently of W are visible and retained.',
 'The pen may is fully readable over the typed may.',
 'The section number consists of a pen 6 and pen 4 over a typed 4; the existing layered encoding is retained.',
 'Fl has a clear typed l crossed by a separate diagonal pen stroke, now resolved.',
 'The old b-like base under b remains doubtful. The typed of under the pen of can be read and is now resolved.',
 'The before On the other hand is struck by regular typewriter x impressions. The small raised regular fragment belongs to its overprint; it does not establish another live character.',
 'The lower-left 75 is handwritten archive foliation.'
 ],summary='Both halves and nine enlarged details inspected. Resolved have (not had), may, Fl and the old of; narrowed the old b to a single-letter doubt. Corrected three cancelled word runs that had mistaken strike characters for literal x letters, removed an insertion-curve fragment misread as a parenthesis, and represented the marginal rule graphically. The final paragraph of section 63 and the opening saturation definitions of section 64 retain all formulas and their provisional qualifications.',differences={
 4513:('M,W','the typescript reads as our transcription','No parentheses surround this pair on the scan.'),
 4516:(r'we \over{have}{have} define\hand{d}','our transcription corrected','The pen retracing reads have, not had; its final v and e are visible. The separate pen d completes defined.'),
 4518:('64.','the typescript reads as our transcription','Only the section number appears here; the witness supplies a descriptive title.'),
 4519:('If f,g are maps and gf exists','the typescript reads as our transcription','The composition in the source hypothesis is gf, as in its following two-out-of-three list; the witness reverses it to fg.')
 })

review('ps_134-4_076',owner='134_4_tail',changes=[
 (r'$\underline{W}$\hand{as}pheric',r'$\underline{W}$\hand{-}\over{as}{as}pheric','A dark pen hyphen precedes the pen as, whose typed as base remains visible.'),
 (r'\mathrm{x}C \longrightarrow C',r'\mathrm{x}C \hand{\longrightarrow} C','The projection arrow has a continuous handwritten shaft and irregular pen head.'),
 (r'L \over{\unsure{3}}{3})',r'L \over{3}{3})','Both old arcs of the typed 3 remain visible beneath the pen 3.'),
 (r'u: $\over{\illegible{1}}{A} \hand{\to} \over{\illegible{1}}{B}$',r'u: $\over{B}{A} \hand{\to} \over[typed]{\unsure{A|B}}{B}$','The old B beneath the pen A retains two right-hand bowls. The final B has regular typed serifs, but its older overlapping letter is uncertain.'),
 (r'\over{\illegible{1}}{A}_{/b}',r'\over{B}{A}_{/\over[typed]{\unsure{a}}{b}}','The second A also covers a typed B with visible right bowls. Its subscript b contains a separate rounded overprint, with a doubtful old a-like base.'),
 (r'\over{\illegible{1}}{so} is \over{\illegible{1}}{f}',r'\over{\unsure{it}}{so} is \over{\unsure{i}}{f}\deleted{\illegible{1}}','The old it-like stem pair under so remains doubtful. The pen f overlays an i-like first cell, while the following old run is separately cancelled by diagonal pen strokes; the draft had hidden that separate cancellation inside the overwrite.'),
 ('These properties',r'T\unsure{\ensuremath{\underset{\hand{\prime}}{\overset{\hand{+\,+}}{\mathrm h}}}}ese properties','Preserve the small paired upper marks and lower hook around h. Their meaning remains uncertain; they are not omitted as a presumed smudge.'),
 (r'\hand{\unsure{(}}including',r'\deleted{\unsure{(}}including','Diagonal pen strokes cross a small parenthesis-like base before including; retain the uncertain base as cancelled rather than a live handwritten parenthesis.'),
 (r'\inserted{the final}',r'\inserted[typed]{the final}','The interlinear the final is regular typing, placed above the cancellation by a pen curve.')
 ],doubts={'unsure':[
 (r'\unsure{m}','doubt retained','The final cancelled old glyph after whom is heavily struck; m remains possible but not certain.'),
 ('3','doubt resolved','The old typed 3 has both right-hand arcs visible beneath the pen retracing.'),
 (r'\unsure{H}','doubt retained','The diagonal cancellation covers the central portion of the old capital; H remains plausible, not settled.'),
 (r'\deleted{\unsure{(}}','doubt retained with final status corrected','The curved old base is uncertain, but the crossing diagonal pen strokes establish a cancellation.')
 ],'illegible':[
 ('B','doubt resolved','Both right-hand bowls of typed B are visible beneath the new A.'),
 (r'\unsure{A|B}','doubt narrowed','The final B is regularly typed, but its older overlapping letter could be A or B.'),
 ('B','doubt resolved','The lower occurrence again exposes the old B bowls under pen A.'),
 (r'\unsure{it}','doubt narrowed','Two old stem-like impressions suggest it; the pen so still prevents certainty.'),
 (r'\over{\unsure{i}}{f}\deleted{\illegible{1}}','doubt retained with layers separated','A doubtful old i-like first glyph is overlaid by f; the remaining old run is independently struck out and unreadable.'),
 (r'\illegible{1}','doubt retained','The typewriter x cancellation beneath the final covers the earlier word too densely to resolve it.')
 ]},notes=[
 'The old glyph after whom is densely struck; its m reading remains uncertain.',
 'A visible pen hyphen precedes as, and the typed as bases remain visible under the handwriting; all three are now represented.',
 'The projection, category, fiber and implication arrows are hand-drawn; the previously unmarked projection arrow is corrected.',
 'The cancelled capital before (Cat)(W) remains a doubtful H.',
 'The old word under so is tentatively it. The pen f overlays an i-like cell and is followed by a separate unreadable cancellation, now represented separately.',
 'The upper paired marks and lower hook sit around h, not T; their graphic is now preserved with an explicit doubt.',
 'The parenthesis-like mark before including is crossed by pen strokes, so it is retained as a doubtful cancellation.',
 'The lower-left 76 is handwritten archive foliation.'
 ],summary='Both halves, ten enlarged details and the complete rotated margin note inspected. The five localizer axioms and implication chain are complete. Resolved the old 3 and two old B letters, restored the pen hyphen and typed bases in aspheric, corrected the typed the-final insertion, and separated the cancelled run after the pen f. The original difficult old letters remain explicit doubts. The margin clearly refers to the proposition on p.167; no wording change is needed there. The L4 subscript retains live b and now records its doubtful old a-like base.',differences={
 4536:(r'\underline{W}=W_{(\mathrm{Cat})}','the typescript reads as our transcription','The parentheses around Cat are explicit in the source subscript.')
 })
