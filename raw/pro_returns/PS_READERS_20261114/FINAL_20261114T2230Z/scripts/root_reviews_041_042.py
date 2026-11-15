from review_root import review
from pathlib import Path
import json
k='ps_134-2_041'
review(k,changes=[
(r'\inserted{en cohomologie étale}'+'\n'+r'à coéfficients discrets\hand{(},',r'à coéfficients discrets \inserted{en cohomologie étale},','The insertion curve points after discrets, before the comma. The apparent opening parenthesis is its anchor, not punctuation.'),
(r'profondeur\hand{(}\inserted[typed]{cohomologique}',r'profondeur \inserted[typed]{cohomologique}','The curve before the typed interlinear word is an insertion anchor, not an opening parenthesis. The inserted word has its own boundary.'),
(r'\deleted{\unsure{aussi}}',r'\deleted{en fait}','An enlarged inspection and an independent second reading recover en fait: two short initial letters, then the long f and dotted i. Aussi cannot account for those traces.'),
(r'le\inserted{$\pi_0$ et le}',r'le \inserted{$\pi_0$ et le}','The inserted mathematical phrase is separated from the preceding article.'),
(r'des\inserted{1-}\uline{champs}',r'des \inserted{1-}\uline{champs}','The inserted 1- belongs to champs, with a word space after des.'),
(r'deur $\geq$ i',r'deur $\hand{\geq}$ i','The inequality sign is penned.'),
(r'\over{\unsure{1}}{1}',r'\over{1}{1}','The old typed 1 remains legible inside the retouched pen numeral.'),
(r'formalisme\inserted{cohomologique non commutatif}',r'formalisme \inserted{cohomologique non commutatif}','The three-word insertion begins after a word boundary.'),
(r'fais\unsure{d}eaux',r'faisdeaux','The bold typed letter has a definite ascender and bowl: d. The source spelling is retained diplomatically.'),
(r"f: X$\to$S",r"f: X$\hand{\to}$S",'The arrow after X is drawn in pen.'),
(r"S'$\to$ S",r"S'$\hand{\to}$ S",'The base-change arrow is also drawn in pen.'),
(r'\margin{41}',r'\margin{\hand{41}}','The lower-left archive number is written in pencil.')
],doubts={'unsure':[
(r'\over{\unsure{a}}{e}','doubt retained','The live e is clear but the covered older letter cannot be confidently recovered.'),
(r'\over{\unsure{e}}{a}','doubt retained','The a is clear while the prior letter remains obscured by the heavy correction.'),
('en fait','doubt resolved','The cancelled phrase is en fait, confirmed independently from the enlarged image; its f and dotted i are visible.'),
(r'\over{\unsure{d}}{l}','doubt retained','The penned l is clear but the underlying typed character is covered.'),
(r'\over{\unsure{R}}{R}','doubt retained','The live R is legible; the older character is not independently separable.'),
('1','doubt resolved','The typed 1 is still visible beneath its handwritten reinforcement.'),
(r"\hand{\unsure{''}}",'doubt retained','The paired pen strokes after arrive may be quotation marks or a nonlexical cue; the scan does not settle their function.'),
('d','doubt resolved','The enlarged character is d, giving literal faisdeaux.'),
(r'\unsure{ct}','doubt retained','There are overlapping c/f-like impressions in this cluster; the exact underlying sequence is not settled.')
],'illegible':[]},notes=[
'Projective is legible as such; the locally dark impression does not supply an extra b.',
'The bold end of profondeur remains readable. Cohomologique is typed interlinearly, and its pen insertion hook is not a parenthesis.',
'The t in fait is penned. The cancelled phrase is en fait, confirmed by a second reader; the old letter beneath the following handwritten l remains doubtful.',
'The original typed 1 remains visible under the pen retouch and is resolved.',
'The paired pen marks after arrive remain uncertain in reading and function.',
'The disputed letter is definitely d. The literal faisdeaux is retained diplomatically, with a separately recorded one-off-slip correction supported by faisceaux later on this page.',
'The folio 26 is penned and the lower-left archive number 41 is in pencil; both are marked.'
],summary='Both scan halves and eight enlarged details inspected, with a second reader for the cancelled en fait. Moved en cohomologie étale to its actual anchor after discrets, removed two insertion curves misread as parentheses, restored whole-word insertion spaces and pen arrows, resolved the retouched 1 and literal faisdeaux, and retained six obscured or functional doubts. The source retains the constructibility hypothesis absent from the witness. One-off Raynaus and faisdeaux corrections are explicit master variants, supported by later same-page spellings.',differences={
585:(r'à coéfficients discrets \inserted{en cohomologie étale},','our transcription corrected','The insertion belongs after discrets, where its curved anchor points; it was misplaced before à in the initial transcription.'),
586:('les plus naturelles','the typescript reads as our transcription','The article ends with a clear s.'),
590:('Ray-naus','the typescript reads as our transcription','The source has s. The same name Raynaud appears twice later on this checked page, supporting an explicit one-off s-to-d correction only in corrected forms.'),
596:('au lieu','the typescript reads as our transcription','The last letter is u, not the witness n.'),
597:(r'\deleted{en fait} \over{\unsure{d}}{l}es','our transcription corrected','The cancelled phrase is en fait, not the original tentative aussi; the older letter under l remains doubtful.'),
598:('démontrés','the typescript reads as our transcription','The final accented e is visibly present.'),
600:('profondeur >= i with closing quotation','the typescript reads as our transcription','The source closes its quotation after i; the witness drops the closing mark.'),
605:('les trois théorèmes suivants','the typescript reads as our transcription','The source has suivants without an extra e.'),
606:('pour un morphisme propre','the typescript reads as our transcription','The source article is un.'),
607:('faisdeaux','our transcription corrected','The doubtful letter is resolved as d. A one-off-slip master variant uses c in corrected forms, supported by faisceaux in the next sentence.'),
608:(r'cara\unsure{ct}érisitques','the typescript reads as our transcription','The source spelling has the recorded transposed ending and a dense uncertain interior overprint; the witness wording does not reproduce it.'),
609:('et dans c) une hypothè se de constructtibilité sur ces faisceaux - mais b) et c) ne servent que','the typescript reads as our transcription','The entire constructibility qualification and transition are present. Omitting them changes the stated hypotheses for generic base change.')
})
p=Path(__file__).resolve().parents[1]/'records/MASTER_VARIANTS_134_2.json';v=json.loads(p.read_text())
v=[x for x in v if x.get('source_id') not in ['DIFF:590','DIFF:607','SPACE:042:1','SPACE:042:2','SPACE:042:3','SPACE:042:4']]
v.extend([
dict(key=k,before='Ray-%\nnaus',after='Ray-%\nnaud',kind='slip corrected',reason='One-off final s for d; Raynaud appears twice later on this same checked page.',source_id='DIFF:590'),
dict(key=k,before='faisdeaux',after='faisceaux',kind='slip corrected',reason='One-off d for c; faisceaux is correctly typed in the following constructibility qualification on this checked page.',source_id='DIFF:607')])

k='ps_134-2_042'
review(k,changes=[
(r'\mspage{27}',r'\mspage{\hand{27}}','The centered folio is penned.'),
(r'en cohomologie étale',r'en c\unsure{\over[typed]{b}{o}}homologie étale','The second cell contains superposed b/o forms, including a definite ascender. Preserve the uncertain overtyping instead of printing an unmarked normalized word.'),
(r"contexte ``naturel'' des",r"contexte\hand{|}``naturel''\hand{/}des",'Two pen strokes separate contexte, the quoted naturel, and des. The strokes are preserved diplomatically and their spacing applied by explicit variants.'),
(r'théorèmes\inserted{du type}',r'théorèmes \inserted[typed]{du type}','Du type is typed above the line; a pen curve gives its anchor. The inserted phrase has a word boundary.'),
(r'tout comme \inserted{de}',r'tout comme \inserted[typed]{de}','De is typed interlinearly, with a handwritten insertion hook.'),
("qu'il y aurait",r"qu'il\hand{/}y\hand{/}aurait",'The two pen strokes separate the words. They are not silently dropped; corrected-form spacing is an explicit master variant.'),
(r'\inserted{\unsure{en groupoïdes|ou groupoïdes}}',r'\inserted{en groupoïdes}','The insertion clearly begins en, with a looped e and following n.'),
(r'à n-équivalence près \deleted{\unsure{``est}}',r'à n-équivalence près\unsure{\hand{)}} \deleted{\unsure{``}est}','A parenthesis-like pen curve remains visible at the right boundary but is partly covered by cancellation. The old word est is legible; its preceding quotation remains doubtful.'),
(r'\xout{\unsure{Kx}}',r'\xout{K}','The old typed K is recoverable. The adjacent x is a cancellation impression, not part of the old mathematical symbol.'),
(r'\margin{42}',r'\margin{\hand{42}}','The archive number is in pencil.')
],doubts={'unsure':[
(r'\hand{\unsure{(*)}}','doubt retained','The parenthesized sign is heavily inked and partly cancelled; its star-like center remains uncertain.'),
(r'\unsure{prosé|prose}','doubt retained','The dark upright mark over the last e does not establish whether an accent belongs to the word.'),
('en groupoïdes','doubt resolved','The two initial pen letters are en, not ou.'),
(r'\deleted{\unsure{``}est}','doubt narrowed','Est is recoverable, but the preceding quotation strokes remain covered by the thick cancellation.'),
('K','doubt resolved','The K is legible beneath typed cancellation; the extra x in the tentative reading belongs to the cancelling layer.')
],'illegible':[
(r'\xout{\illegible{1}}','illegible retained','The short word before commutative remains too densely struck to recover securely.'),
(r'\deleted{\illegible{1}}','illegible retained','The earlier insertion before petite is covered by thick pen hatching; no complete word is recoverable.')
]},notes=[
'The second letter of cohomologie contains b/o overtyping; a new explicit doubt records its uncertain layer order.',
'All four separation strokes around naturel and y are now represented diplomatically, with master variants that apply spaces in the corrected forms.',
'Doit is handwritten on the baseline; no independently readable older word can be recovered beneath it.',
'The comma after contexte is blotted by hand and remains a deletion.',
'The heavily inked parenthesized sign after triangulée remains uncertain, rather than being supplied from the witness.',
'The live petite and en groupoïdes are legible. The prior insertion remains illegible; est is recovered under the later cancellation, while its quote strokes and the adjacent closing-parenthesis trace remain doubtful.',
'The author folio 27 is penned and archive number 42 is in pencil.'
],summary='Both scan halves and six enlarged details inspected. Restored four pen spacing cues, corrected typed provenance of du type and de, recorded b/o overtyping in cohomologie, resolved en groupoïdes and cancelled K, and narrowed the old est doubt. A partly covered closing-parenthesis trace is now explicitly doubtful. The source inequality is i >= n+1, opposite to the witness formula. The signature, App.3 call, and remaining illegible cancellations are retained.',differences={
615:('il devient clair','the typescript reads as our transcription','The source e is unaccented.'),
619:(r'\hand{Idem pour variantes analytiques complexes etc.}','the typescript reads as our transcription','Idem is legible and is not an empty placeholder.'),
620:(r"qu'il\hand{/}y\hand{/}aurait",'our transcription corrected','The y is present between two pen spacing strokes; the witness omits it.'),
623:(r'\margin{(24)} toujours','the typescript reads as our transcription','The marginal call 24 is present. The witness incorporates an editorial footnote rather than preserving this marginal marker.'),
624:(r'\hand{\unsure{(*)}}','the typescript reads as our transcription','The heavily marked sign exists on the page and remains doubtful; it is absent from the witness.'),
627:(r'\hand{A Grothendieck}','the typescript reads as our transcription','The signature is clearly present and is omitted by the witness.'),
628:(r'\margin{(App.3)}','the typescript reads as our transcription','The source has the numbered marginal call, not the descriptive witness heading.'),
631:('en groupoïdes','our transcription corrected','The pen insertion reads en, not the witness ou.'),
632:(r'à n-équivalence près\unsure{\hand{)}}','our transcription corrected','A partly covered closing-parenthesis-like trace is visible. Its exact status is uncertain, so the witness unmarked closing parenthesis cannot simply be adopted.'),
634:("qu'un ensemble",'the typescript reads as our transcription','The typed article is un, without e.'),
636:(r'i \hand{$\geq$} n+1','the typescript reads as our transcription','The index i precedes the handwritten greater-than-or-equal sign. The witness reverses the inequality and changes the stated truncation.'),
638:("n+1'').",'the typescript reads as our transcription','The source closes the quoted paraphrase before the parenthesis; the witness omits the closing quotation.')
})
for i,b,a in [(1,r'contexte\hand{|}',r'contexte '),(2,r"naturel''\hand{/}des",r"naturel'' des"),(3,r"qu'il\hand{/}",r"qu'il "),(4,r'y\hand{/}aurait',r'y aurait')]:
 v.append(dict(key=k,before=b,after=a,kind='author spacing cue',reason='Apply the pen separation stroke as a word space while preserving the graphic in the diplomatic form.',source_id=f'SPACE:042:{i}'))
p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
