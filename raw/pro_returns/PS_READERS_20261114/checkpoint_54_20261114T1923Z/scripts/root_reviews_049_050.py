from review_root import review
from pathlib import Path
import json
hook=r'\tikz[baseline=-.4ex,x=.5em,y=.5em]{\draw (0,0)--(.8,0)--(.8,1)--(1.6,1);\draw (.12,0)--(.92,0)--(.92,1);}'
k='ps_134-2_049'
review(k,changes=[
(r'\hand{$\leq$}',r'\hand{$\unsure{\leq}$}','The upper part of the retraced relation is not secure. Two independent visual readings support keeping a doubtful less-than-or-equal sign rather than resolving it from the later clear inequalities.'),
(r'\mspage{39}',r'\mspage{\hand{34}}','The centered handwritten folio reads 34, not 39; the typed 2 at the right is a separate foliation.'),
(r'\margin{$\ulcorner$ \unsure{(C)} $\llcorner$}',r'\margin{\hand{'+hook+r' \deleted{\unsure{(C)}} '+hook+r'}}','The marginal sign is heavily hatched out between two double step-shaped brackets. Preserve the cancellation and do not treat the bracket strokes as ordinary corner characters.'),
(r'.\hand{$\|$}En',r'.\hand{'+hook+r'}En','The beginning of the marked passage has a double step-shaped bracket, not parallel upright bars.'),
(r'.\hand{$\|$}Dans',r'.\hand{'+hook+r'}Dans','The end of the marked passage has the matching double step-shaped bracket.'),
(r'\unsure{induite|induit}',r'induit\unsure{e}','Induit is clear; only the faint impression after t, possibly a final e, remains uncertain.'),
(r'\unsure{récessairement|nécessairement}','nécessairement','The initial letter has two uprights and an arch: n, not r.'),
(r'($0 \leq i \leq n$)',r'($0 \hand{\leq} i \hand{\leq} n$)','Both inequalities are drawn by hand and point to the left.'),
(r'trivial en dim $\leq$ n,  on',r'trivial en dim $\hand{\leq}$ n,  on','The inequality is handwritten.'),
(r'trivial en dim $\leq$ n, pour',r'trivial en dim $\hand{\leq}$ n, pour','The inequality in the parenthetical hypothesis is handwritten.'),
(r'\mspage{49}',r'\margin{\hand{49}}','The lower-left 49 is a pencil archive foliation, not another centered typescript page number.')
],doubts={'unsure':[
(r'\deleted{\unsure{(C)}}','doubt retained','Heavy pen hatching cancels the marginal sign; (C) remains only a tentative reading.'),
(r'\deleted{\unsure{ceux-ci}}','doubt retained','The pen cancellation obscures several letters of the old phrase; retain the tentative reading rather than infer it from the replacement.'),
(r'induit\unsure{e}','doubt narrowed','Induit is clear, but the weak impression following t may be a final e or a nonletter trace.'),
('nécessairement','doubt resolved','The initial n is legible in the enlarged image.'),
(r'\deleted{\unsure{,}}','doubt retained','The dark cancellation after the new closing parenthesis hides the earlier punctuation.'),
(r'\deleted{\unsure{qui}}','doubt retained','Parts of the old word are visible beneath the cancellation, but not enough to settle all three letters.')
],'illegible':[(r'\illegible{1}','illegibility retained','The small old mark before the new opening parenthesis is entirely covered by pen strokes.')]
},notes=[
'The first inequality is handwritten and heavily retraced; two independent visual readings leave its upper strokes uncertain, so a doubt mark is added. The later dimensional inequalities clearly read less-than-or-equal.',
'The marginal parenthesized sign is heavily cancelled. The two step-shaped margin brackets and matching inline brackets are restored graphically.',
'The old phrase read tentatively as ceux-ci remains uncertain under the cancellation; the live inserted C_n and comma are clear.',
'Induit is secure; a faint possible e after t remains marked separately.',
'The word is necessarily read nécessairement from its visible initial n; the uncertainty is removed.',
'The old mark before the new opening parenthesis remains unreadable beneath the pen cancellation.',
'The old comma after multigaloisien remains doubtful beneath the dense pen mark.',
'The old qui remains doubtful; the inserted lequel is plainly legible.',
'The top handwritten folio is 34, not 39; the top-right 2 is typed; 49 at the foot is a pencil archive foliation.'
],summary='Both halves and enlarged inequality, cancellation, initial-letter and final-letter details inspected. Corrected the handwritten folio to 34, restored the step-shaped double brackets and cancelled status of the marginal sign, resolved nécessairement and narrowed the final-letter doubt in induit. The interval is plainly 0 ≤ i ≤ n, unlike the witness reversal. The abbreviation loc., the live ledit, the limited underlining and all unrecovered old text are preserved.',differences={
767:(r'\hand{$\unsure{\leq}$}','our transcription corrected','The first relation is darkly overwritten; a doubt is required and the later clear inequalities do not settle the obscured strokes.'),
772:(r'cancelled uncertain (C) between double step-shaped brackets; matching inline brackets','our transcription corrected','The geometric marks and hatching are visible; the witness omits them.'),
776:(r'\uline{n-groupoide fondamental de} X','the typescript reads as our transcription','The underline stops after de at the end of the line; X on the next line is not underlined.'),
777:(r'0 \leq i \leq n','the typescript reads as our transcription','Both handwritten inequality signs point left. The witness reverses both and changes the mathematical range.'),
779:(r'\inserted{loc.}','the typescript reads as our transcription','The handwritten insertion is the abbreviation loc.; it is not written out.'),
783:(r'C_1 ) followed by cancelled unreadable mark and new opening parenthesis','the typescript reads as our transcription','The typed closing parenthesis and the new opening parenthesis are visible and should not disappear.'),
784:(r'\deleted{\illegible{1}}\hand{(}','the typescript reads as our transcription','The cancelled old mark remains unrecoverable; the opening parenthesis is handwritten.'),
786:('ledit','the typescript reads as our transcription','The word is typed without an internal space.')
})

k='ps_134-2_050'
review(k,changes=[
(r'\mspage{\hand{35}} \mspage{3}',r'\mspage{\hand{35}} \hfill 3','The handwritten folio is centered; the independent typed 3 is at the right.'),
(r'est la catégorie des',r'est \hand{l}a catégorie des','The l of la is reinforced or rewritten in pen; the a and remaining text are typed.'),
(r'\unsure{générahement|généralement}',r'généra\unsure{\over[typed]{h}{l}}ement','The uncertainty is confined to a typewriter overprint in the l cell; the remaining letters are clear. A possible old h under l remains doubtful.'),
(r'\margin{50}',r'\margin{\hand{50}}','The lower-left archive number is in pencil.')
],doubts={'unsure':[
(r'\deleted{\unsure{s}}','doubt retained','The old final letter after énoncé is covered by a dense pen cancellation.'),
(r'\deleted{\unsure{s}}','doubt retained','Only a weak curved remnant survives after ma; it does not securely establish the old letter.'),
(r'\over{\unsure{d}}{d}','doubt retained','The live d is penned; its underlying typed impression is substantially covered.'),
(r'\over{\unsure{K}}{K}','doubt retained','The live K is penned over the original cell; the underlying letter cannot be read independently.'),
(r'généra\unsure{\over[typed]{h}{l}}ement','doubt narrowed','The overprinted cell shows an l-like tall stroke and a second lower stem; h under l is possible, so the cell remains marked.')
],'illegible':[]},notes=[
'The two top foliations are distinct: handwritten 35 and typed 3. The lower-left 50 is a pencil archive number.',
'The margin reads cela sem- ble sus- pect! with sem- and sus- typed and the other parts handwritten; the note is preserved at its anchor.',
'The acute over the final e is penned; the cancelled following character remains uncertain.',
'The garbling is a typed overprint in the l cell of généralement; uncertainty is narrowed to that cell.',
'The d and K are handwritten over their original typed cells; the older letters remain doubtful.',
'The classifying topos symbol has the distinctive top cross-stroke of script T, consistently different from the open script C used for the groupoid.'
],summary='Both scan halves and enlarged deletion, overprint and pen-letter details inspected. Confirmed the repeated script T symbols against C, arbitrary direct limits and finite inverse limits, n-topos, s’interprète and the mixed typed/handwritten marginal objection. Marked the pen l of la, narrowed the generally overprint, preserved the remaining buried letters, and recorded the pen word-separation cue. The doubled opening parenthesis and all other literal source syntax remain.',differences={
790:(r'\mathcal T_n=(n-\underline{Hom})(\mathcal C_n,((n-1)-Cat))','the typescript reads as our transcription','The left-hand symbol is script T, not C; the distinction is visually clear and mathematically essential.'),
791:(r'\mathcal T_n\longrightarrow((n-1)-Cat)','the typescript reads as our transcription','Both source occurrences in this phrase are T_n, not C_n.'),
792:(r'\varinjlim quelconques; \varprojlim finies','the typescript reads as our transcription','The pen arrows point right under arbitrary limits and left under finite limits; the witness reverses the directions.'),
793:(r'\mathcal T_n serait un n-topos','the typescript reads as our transcription','Both the T symbol and the n prefix are visible.'),
794:('n-topos','the typescript reads as our transcription','The source explicitly retains n-, which the witness omits.'),
797:("s’interprète",'the typescript reads as our transcription','The initial s and apostrophe are plainly typed; the witness d is unsupported.'),
800:(r'classifiant \mathcal T_n','the typescript reads as our transcription','The final classifying object is again T_n, not C_n.'),
804:(r'\margin{\hand{cela} sem- \hand{ble} sus- \hand{pect!}}','the typescript reads as our transcription','The visible mixed handwritten and typed marginal objection is absent from the witness.')
})
p=Path(__file__).resolve().parents[1]/'records/MASTER_VARIANTS_134_2.json';v=json.loads(p.read_text());v=[x for x in v if x.get('source_id')!='SPACE:050:1'];v.append(dict(key=k,before=r'on\hand{/}voudrait',after='on voudrait',kind='author spacing cue',reason='The pen stroke separates on from voudrait; apply the space while preserving the stroke diplomatically.',source_id='SPACE:050:1'));p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
