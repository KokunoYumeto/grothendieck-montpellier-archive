from review_root import review
from pathlib import Path
import json
k='ps_134-2_069'
label=r'\hand{\tikz[baseline=(x.base)]{\node (x) {(App.16)};\draw (.5,.3)--(.5,.65);\draw (.5,.3) .. controls (-1,.6) and (-1,-.65) .. (.5,-.3)--(.5,-.65);\draw (1.65,.45)--(.95,.45) .. controls (.7,.45) and (.7,-.2) .. (.95,-.2)--(1.65,-.2);}}'
review(k,changes=[
(r'\mspage{-54-}',r'\mspage{-\hand{5}4-}','The leading5 is handwritten or pen-retraced;4 and the hyphens are typed. No separate old digit is legible.'),
(r'\margin{(App.\ 16)}',r'\margin{'+label+'}','The App.16 label and its surrounding placement brackets are handwritten.'),
(r'\margin{69}',r'\margin{\hand{69}}','The lower-left69 is pencil archive foliation.')
],doubts={'unsure':[],'illegible':[]},notes=[
'The first5 of54 is handwritten or retouched in pen; the4 and hyphens are typed.',
'The lower-left69 is pencil archive foliation.',
'The separator has a visible dollar sign between two continuous horizontal strokes; the rule-dollar-rule transcription retains its graphic form.'
],summary='Both halves inspected. Marked the pen folio, App16 placement graphic and pencil archive number. The source clearly has famliliar at the top and familiar later in the same paragraph, allowing a recorded one-off correction only in the corrected forms. The finite inverse and arbitrary direct limit arrows, emphasized pro, and quasi-compact hypothesis are confirmed; there exist remains literal.',differences={
1121:('famliliar','the typescript reads as our transcription','The scan shows famliliar; familiar appears correctly later in the same paragraph. A master variant corrects this isolated extra l only in the corrected forms.'),
1125:(r'\uline{\textit{pro}}-n-\textit{groupoid}','the typescript reads as our transcription','Only pro carries the visible underline; the italic groupoid and the roman n remain distinct.'),
1126:('handwritten(App.16) and placement brackets','our transcription corrected','The scan has this margin label and graphic, without the witness added descriptive heading.'),
1128:('quasi-compact and quasi-separated','the typescript reads as our transcription','The printed hypothesis is quasi-compact, not the witness quasi-coherent.')
})
p=Path(__file__).resolve().parents[1]/'records/MASTER_VARIANTS_134_2.json';v=json.loads(p.read_text());v=[x for x in v if x.get('source_id')!='DIFF:1121'];v.append(dict(key=k,before='famliliar',after='familiar',kind='slip corrected',reason='The isolated extra l is a typing slip: the same paragraph later types familiar correctly in the same sense.',source_id='DIFF:1121'));p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
k='ps_134-2_070'
step=r'\hand{\tikz[baseline=-.4ex]{\draw (0,-.1)--(.45,-.1)--(.45,.35)--(1.1,.35);\draw (.51,-.1)--(.51,.31);}}'
review(k,changes=[
(r'\mspage{55}',r'\mspage{-\hand{5}5-}','The scan has typed hyphens, a pen-retraced first5 and a typed second5.'),
(r'\margin{$\_\!\|\!\overline{\ \ }$} \margin{$\_\!\|\!\overline{\ \ }$}',r'\margin{'+step+r'} '+step,'The two pen paragraph cues are double-upright steps. One is in the far margin and the other immediately before By; preserve their distinct positions and geometry.'),
(r'giv\over{en}{ing}',r'giv\over{e}{i}n\hand{g}','Enlargement shows a pen i over typed e, an unchanged typed n, and a new handwritten g after it. The initial transcription wrongly marked n as rewritten.'),
(r'\margin{70}',r'\margin{\hand{70}}','The lower-left70 is pencil archive foliation.')
],doubts={'unsure':[(r'\unsure{one}','doubt retained','The short cancelled handwritten word before the closed one is densely blackened; one remains only a tentative reading.')],'illegible':[]},notes=[
'The folio has hyphens around55; its first digit is retouched in pen, its second is typed.',
'The paragraph cues have two vertical strokes and a horizontal step. The far-left cue is marginal, and the matching cue just before By is placed in the line.',
'The cancelled small handwritten word before the closed one remains doubtful.',
'The marked subscripts1 are indeed handwriting, including those in the inclusions; the1 in F1 should be locally constant is typed and remains plain.',
'The lower-left70 is pencil archive foliation.'
],summary='Both halves and enlarged given-to-giving correction inspected. Restored folio hyphens, the two differently placed step-shaped paragraph cues, and the precise correction e-to-i plus added g around an unchanged typed n. The cancelled one remains doubtful. Confirmed the handwritten subscripts1 and the literal extra superscript star on the second i in the gluing formula; this mathematical issue is reserved for the guide.',differences={
1130:('the given stratification of X','the typescript reads as our transcription','The source has singular stratification.'),
1138:(r'i^*_0\,i^*_{\hand{1}*}(F_{\hand{1}})','the typescript reads as our transcription','The additional star is below the second i beside1; the witness raises it as an exponent of1. The separately printed superscript star is also retained.')
})
p=Path(__file__).resolve().parents[1]/'guide_sections/134_2_appendix.tex';s=p.read_text()
if '\\subsection*{Appendix 15:' not in s:
 s+=r'''
\subsection*{Appendix 15: Homotopy types and higher local systems}
Cote 134-2, sites 67--69 (folios 52--54), distinguishes the homotopical algebra performed inside a rich topos from the much poorer homotopy type obtained by localization. The retained information is expressed through locally constant higher stacks, fundamental higher groupoids, and ``special'' or ``n-galois'' categories, arranged in a triangle of proposed mutual reconstructions. This resumes Appendix 6's higher Galois reconstruction: exact functors should recover the fundamental groupoid from its category of local systems, with finite inverse limits and arbitrary direct limits again explicitly distinguished. The handwritten replacement of ``must'' by ``should'' at site 68 preserves the conjectural status of the comparison. Its dimensions also require care: the definition uses locally constant $(n-1)$-stacks but then writes functors into $(n\text{-}\mathrm{Cat})$, followed by lowercase $(n\text{-}\mathrm{cat})$ in the reconstruction formulas. With the usual meaning of n-Cat these targets are one categorical level higher than the preceding local-system description; already at $n=1$, category-valued systems differ from set-valued systems. The text does not settle that convention here, and the printed indices and capitalization remain unchanged. Site 69 makes the important qualification that a locally homotopically trivial situation can have an ordinary homotopy type, while étale topoi generally require a pro-n-groupoid and an accompanying ind-category of local systems. Its emphatic negative assertion about the étale topos should not be read as excluding every special scheme: the étale topos of an algebraically closed field already gives the elementary constant case. The witness loses the underline emphasizing pro and normalizes the parenthesized Cat/cat distinctions; the visible final d alone is cancelled in interpreted, leaving the literal interprete. The isolated typed famliliar is corrected with apparatus because familiar occurs correctly later in the same paragraph. Appendix 16 then addresses the dissatisfaction motivating this section by retaining stratified constructible data instead of only locally constant data.
'''
 p.write_text(s)
