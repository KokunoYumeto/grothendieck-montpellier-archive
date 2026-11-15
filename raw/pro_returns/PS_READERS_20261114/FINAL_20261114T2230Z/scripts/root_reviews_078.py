from review_root import review
from pathlib import Path
import json

k='ps_134-2_078'
cue=r'\margin{\hand{\tikz[x=1cm,y=1cm]{\draw[->] (.8,-.3)--(.15,-.3) .. controls (-.4,-.3) and (-.2,.25) .. (.15,.25)--(.65,.25);\draw (.05,.22)--(.05,2.6) .. controls (.05,3.05) and (.55,3.05) .. (.65,2.85);}}}'
oldcomment='% NOTE: a large handwritten bracket in the left margin, with an arrow pointing right at its top, encloses the lines from "Chapter I" down to the note "These letters are reproduced ..."'
review(k,changes=[
(r'\mspage{62}',r'\mspage{\hand{62}}','Both live folio digits are written in pen; the rounded2 has the same freehand shape as the new12 below.'),
(r'\uline{to Chapter I}',r'\uline{to Chapter} I','The first heading underline stops after Chapter, before the separate Roman I.'),
(oldcomment,cue,'The long marginal arrow and curved enclosure are visible source marks, not merely a transcription comment. They direct the paragraph now numbered1 before the paragraph now numbered2; the annotated master applies that transposition.'),
(r'\deleted{Chapter I}',r'\deleted{\uline{Chapter I}}','The cancelled typed heading has an underline as well as the diagonal cancellation.'),
('I little suspected that the former friend',r'I little suspected \over{th}{th}at the former friend','The first two letters of this that are visibly retraced in pen over their typed forms.'),
(r'\unsure{that} was to be expected',r'\over{tha}{tha}t was to be expected','The word is clearly that. Its first three letters have pen retracing over the typed letters; the final t remains plain type.'),
(r'\over{\illegible{1}}{12}',r'\deleted{\unsure{12}}\hand{12}','The old section number is crossed out, and the new12 is written beside it rather than directly on it. The old reading12 remains tentative under the cancellation.'),
(r'\deleted{\illegible{1}}. Compare',r'\deleted{goes}. Compare','The cancelled word has a looped descending g, round o, open e and final s; goes is legible beneath the diagonal strokes.'),
(r'(1\over{\illegible{1}}{7})',r'(1\over{\unsure{6|7}}{7})','The old digit has visible parts consistent with6 or7, without a secure distinction; the pen7 is clear.'),
(r'\hand{$\frac{\unsure{i}}{2}$}',r'$\overset{i}{\underset{\hand{\ell}}{*}}$','The image shows a typed i above a star and a separate looped handwritten ell below it. There is no fraction bar; an independent visual reading confirms the lower ell rather than2.'),
(r'\over{\illegible{1}}{\unsure{1}}',r'$\over{1}{\unsure{\ell}}$','The old glyph is a clear typed1. The new oblique pen stroke plausibly gives ell, but its shape is not secure enough to remove the doubt.'),
(r'\margin{78}',r'\margin{\hand{78}}','The lower-left78 is pencil archive foliation.')
],doubts={'unsure':[
(r'\unsure{1}','doubt retained','The earlier digit beneath the new2 is largely covered;1 remains tentative.'),
(r'\unsure{ask}','doubt retained','The typewriter overstrikes obscure the middle of this word; the outer a and tall final stroke do not settle ask independently.'),
(r'\unsure{intensely}','doubt retained','The interlinear typed word is heavily crossed out; its suggested full spelling remains uncertain.'),
(r'\over{tha}{tha}t','doubt resolved','The live word that is clear, including the retraced first three letters and plain final t.'),
(r'\unsure{2}','doubt retained','The former digit under the new1 is too heavily overprinted for a secure reading.'),
(r'\unsure{-}','doubt retained','The small retouched mark after fami reaches the cropped page edge; its exact identity is not settled.'),
('i','doubt resolved','The upper glyph has a typewritten stem, serifs and a separate dot: it is i, above the star rather than a fraction numerator.'),
(r'\unsure{\ell}','doubt retained','The live pen stroke over typed1 suggests ell but has no independently clear loop at this resolution.')
],'illegible':[
(r'\illegible{1}','illegibility retained','The overtyped word at the right edge after of is both blackened and clipped by the supplied scan edge.'),
(r'\unsure{12}','illegibility partly resolved','Parts of both old digits can now be described as tentative12, but the cancellation still prevents certainty.'),
('goes','illegibility resolved','All four letter shapes are visible beneath the diagonal cancellation.'),
(r'\unsure{6|7}','illegibility partly resolved','The old digit’s top and lower curved part narrow the reading to6 or7; the new7 does not settle the old form.'),
('1','illegibility resolved','The underlying typewritten1 has a visible top flag, vertical stem and broad base.')
]},notes=[
'The new labels2 and1 are clear. Their old typed labels remain doubtful. A long pen arrow enclosing the These letters paragraph directs it upward, and an explicit master variant applies that move in the corrected forms.',
'The crossed interlinear word remains tentatively intensely; the later typed insertion sincerely is live and distinct.',
'The final that is clear with pen retracing on tha. The earlier that after suspected likewise has retraced th; both are now marked.',
'The word after was remains tentatively ask. The right-edge overtyped word after of remains illegible and partially clipped.',
'The mark after fami remains doubtful at the cropped right edge; the handwritten exclamation after geometry is clear.',
'The old section number is tentatively12, crossed before a separately written12. The cancelled word after functor is goes. The new7 in note17 is clear over a doubtful6/7.',
'The supposed fraction is a star with typed upper i and handwritten lower ell, independently confirmed. The later order symbol retains the typed1 under a doubtful pen ell.',
'The lower-left78 is pencil archive foliation.'
],summary='Both halves and thirteen enlarged details inspected, including every original doubt and illegible mark. Restored the marginal transposition graphic, heading underline extent and pen retracing in that. Resolved cancelled goes and the old typed1 in note10; replaced the false fraction with the visible indexed star, independently checked. Preserved uncertainties in old note labels, typewriter cancellations, clipped hyphen, old section/note digits and the new order symbol. The corrected forms put the note now numbered1 before note2 by an explicit master variant.',differences={
1257:(r'$B_G$','the typescript reads as our transcription','The B is the ordinary typewriter capital with a subscript G, not the witness’s blackboard-style B macro.'),
1258:('for the discrete group G.','the typescript reads as our transcription','The final period is clearly typed and retained.'),
1260:('Buffalo in1973.','the typescript reads as our transcription','The typed sentence ends with a period, omitted by the witness.')
})

project=Path(__file__).resolve().parents[1]
page=(project/'checked_pages'/f'{k}.tex').read_text()
start=page.index(r'(\over{\unsure{1}}{2})');second=page.index(r'(\over{\unsure{2}}{1})');end=page.index('\n\n',second)
block=page[start:end];first=page[start:second].strip();last=page[second:end].strip()
p=project/'records/MASTER_VARIANTS_134_2.json';a=json.loads(p.read_text());a=[x for x in a if x['source_id']!='MOVE:078:1']
a.append(dict(key=k,before=block,after=last+'\n\n'+first,kind='authorial transposition with corrections',reason='The long marginal arrow moves the paragraph renumbered1 above the paragraph renumbered2. This single compound variant applies that move and the visible corrections within both paragraphs; the diplomatic reading preserves their source order and all underlying layers.',source_id='MOVE:078:1'));p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
p=project/'guide_sections/134_2_appendix.tex';s=p.read_text()
if '\\subsection*{Notes 1--11:' not in s:
 s+=r'''
\subsection*{Notes 1--11: Retrospective qualifications of the Quillen letter}
Cote 134-2, site78 (folio62), opens the notes to ChapterI and the appendix. A long pen arrow and the renumbering move the notice about reproducing the Breen letters before the account of the unanswered Quillen letter; the diplomatic form retains the physical order and the corrected forms apply the move. Note3 points toward tame topology in the Esquisse, while notes4--5 qualify the earlier judgment of the Bangor group's relation to geometry. Note6 restricts the earlier assertion to strict associativity. Note7 calls the claim about existence and uniqueness of the functor rash and points to section12 and note17; its cancelled final word is goes. Note8 gives torsors and the classifying topos as another example, with an ordinary typed B rather than the witness's blackboard-style symbol. Note9 recalls the Buffalo seminar. The initial transcription of note10 as a fraction was materially wrong: the scan has a star with typed upper i and a looped handwritten lower ell. The witness instead gives a lower2, while its following order is ell. In the source the latter position contains a clear typed1 with a tall pen correction plausibly read as ell; that live reading remains doubtful, so the readers do not settle it by appeal to the intended composition order. Note11 explicitly withdraws an earlier belief and refers to section11. These retrospective statements should be read with the earlier tentative construction of successive layers of structure, not as part of its original uninterrupted argument.
'''
 p.write_text(s)
