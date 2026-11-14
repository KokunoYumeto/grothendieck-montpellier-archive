from review_root import review
from pathlib import Path
import json
up=r'\tikz[baseline=-.4ex,x=.5em,y=.5em]{\draw[->] (1,0)--(0,0)--(0,2);}'
down=r'\tikz[baseline=-.4ex,x=.5em,y=.5em]{\draw[->] (1,2)--(0,2)--(0,0);}'
loop=r'\tikz[baseline=-.4ex,x=.5em,y=.5em]{\draw (1,1) .. controls (0,1) and (-.1,.8) .. (0,.3) .. controls (.2,0) and (.8,.2) .. (1,0);}'
k='ps_134-2_051'
review(k,changes=[
(r'\mspage{\hand{36}} \mspage{4}',r'\mspage{\hand{36}} \hfill 4','The handwritten central folio and typed top-right 4 are separate.'),
(r'\unsure{la}',r'l\over[typed]{\unsure{e}}{a}','The live a is clear; a lower typed impression, possibly e, remains doubtful in the same cell.'),
(r'\margin{[bracket from this line to the next]}',r'\margin{\hand{'+up+r'}}','Replace the transcription’s descriptive placeholder with the actual upward bent arrow beside the two lines.'),
(r'\margin{espace} \margin{[bracket and arrow downward]}\hand{(App.7)}',r'\margin{\hand{espace '+down+r'}} \margin{\hand{(App.7) '+loop+r'}}','Espace and App.7 are handwritten marginal annotations. Restore the downward bent arrow and the curved placement bracket instead of printing editorial descriptions as source prose.'),
(r'\xrightarrow{\hand{$\mathcal{F}$}}',r'\hand{\xrightarrow{\mathcal{F}}}','The arrow as well as its F label is drawn in pen.'),
(r'\margin{51}',r'\margin{\hand{51}}','The archive number is in pencil.')
],doubts={'unsure':[
(r'l\over[typed]{\unsure{e}}{a}','doubt narrowed','The live reading is la; only the older same-cell typewriter impression under a remains uncertain.'),
(r'\xout{\unsure{s}}','doubt retained','The typewriter x covers the original final letter after champ too heavily to recover it securely.')
],'illegible':[]},notes=[
'The closing quote after à is penned. La has a live typed a over a doubtful older e-like impression; the uncertainty is now confined to the older layer.',
'The final character after champ is crossed out with a typewriter x; the old s reading remains doubtful.',
'The faint curved smudge after le does not establish a recoverable letter or an identifiable cancellation; no lexical content is supplied from it.',
'The marginal espace, opposed bent arrows and App.7 placement curve are restored as handwriting and graphics; descriptive transcription placeholders are removed.',
'The top central 36 is handwritten, the upper-right 4 is typed, and the lower-left 51 is pencil archive foliation.'
],summary='Both halves and enlarged la, terminal-x and smudge details inspected. Recovered the live la while retaining its doubtful old letter; retained the unreadable cancelled s. Replaced editorial bracket descriptions by the actual marginal arrows and placement curve and marked their handwritten labels. The restriction is to T_1 intersection T_2, not the witness union. The extra opening parenthesis in the target category, the literal isomorphisme unique and all cohomological indices remain.',differences={
814:(r'T_1\cap T_2','the typescript reads as our transcription','The handwritten symbol is an intersection arch; the witness union changes the common restriction space.'),
816:(r'\margin{\hand{espace}} with opposed bent arrows','our transcription corrected','The marginal word is handwritten and belongs to the visible separation instruction.'),
817:(r'\margin{\hand{(App.7)}} with placement curve','our transcription corrected','The handwritten label is marginal; the witness replaces it by an editorial descriptive title.'),
818:('no descriptive heading','the typescript reads as our transcription','The scan has only App.7 as a label, not the supplied descriptive heading.'),
821:(r'\mathcal C_n\longrightarrow((n-1)\text{-Cat})','the typescript reads as our transcription','The source has the extra opening parenthesis shown in the transcription; it is not silently balanced.'),
824:(r'isomorphisme\hand{/}unique','the typescript reads as our transcription','The slash is a pen spacing cue, preserved diplomatically and applied as a space in the corrected forms.')
})
p=Path(__file__).resolve().parents[1]/'records/MASTER_VARIANTS_134_2.json';v=json.loads(p.read_text());v=[x for x in v if x.get('source_id')!='SPACE:051:1'];v.append(dict(key=k,before=r'isomorphisme\hand{/}unique',after='isomorphisme unique',kind='author spacing cue',reason='Apply the pen separator as a space between isomorphisme and unique.',source_id='SPACE:051:1'));p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')

k='ps_134-2_052'
review(k,changes=[
(r'\mspage{\hand{37}} \mspage{5}',r'\mspage{\hand{37}} \hfill 5','The handwritten central folio and independent typed upper-right number are distinguished.'),
(r'\boxed{H^{i}(X , \hand{\mathcal{F}} ) = \hand{\pi}_{N-i}\hand{\Gamma}_{X}\hand{\mathcal{C}}^{N-n} \hand{\mathcal{F}} ) \qquad \text{si} \quad N \hand{\geq} i,n}',r'\hand{\boxed{\normalcolor H^{i}(X , \hand{\mathcal{F}} ) = \hand{\pi}_{N-i}\hand{\Gamma}_{X}\hand{(}\hand{\mathcal{C}}^{N-n} \hand{\mathcal{F}} ) \qquad \text{si} \quad N \hand{\geq} i,n}}','The scan has a clear opening parenthesis between Gamma_X and the classifying operator, omitted in the initial transcription. The surrounding rectangle is drawn in pen; mark its rule separately while preserving the mixed typed and handwritten contents.'),
(r'group\hand{\unsure{\"o}}ides',r'group\unsure{\over{o}{ó}}ides','The mark above the typed o is a single faint diagonal, not two diaeresis dots. Retain its uncertain status as a possible added acute rather than assert an umlaut.'),
(r'\hand{\unsure{$_4$|,}}',r'\hand{$_4$}','The enlarged mark has the angular form of a small handwritten 4, not a comma.'),
(r'comme le montrent les',r'comme le mont\unsure{\over[typed]{n}{r}}ent les','The r cell has a visible same-cell typewriter overprint; a possible older n remains doubtful.'),
(r'\deleted{(}le',r'\deleted{\unsure{(}}le','The zigzag cancellation hides most of the old opening character; its parenthesis reading remains tentative.'),
(r"classifiant''\deleted{)}",r"classifiant''\deleted{\unsure{)}}",'The old closing character is covered by a dense zigzag cancellation, so the inferred parenthesis needs a doubt mark.'),
(r'pour \over{\illegible{1}}{i} $\leq$ n+1',r'pour \over{\illegible{1}}{i} $\hand{\leq}$ n+1','The lower inequality is drawn in pen with the same irregular strokes as the other handwritten inequalities.'),
(r'lence\deleted{s} près',r'lence\deleted{\unsure{s}} près','The dark final cancellation leaves insufficient separate detail to establish s securely.'),
(r'\mspage{\hand{52}}',r'\margin{\hand{52}}','The lower-left 52 is a pencil archive foliation, not the centered source folio.')
],doubts={'unsure':[
(r'\unsure{\over{o}{ó}}','doubt narrowed','A single diagonal mark lies over the typed o; its interpretation as an added acute remains uncertain, but a diaeresis is not visible.'),
(r'\hand{$_4$}','doubt resolved','The enlarged angular sign is legible as a small handwritten 4.')
],'illegible':[
(r'\illegible{1}','illegibility retained','The old terminal letter is covered by the handwritten s.'),
(r'\illegible{1}','illegibility retained','The original letter before the replacement H is densely cancelled; visible serifs do not settle its identity.'),
(r'\illegible{1}','illegibility retained','The older typed impressions beneath the pen il cannot be separately recovered.'),
(r'\illegible{1}','illegibility retained','The live i overlies a circular old impression, whose identity remains uncertain.')
]},notes=[
'All the listed inequalities, including the lower one before n+1, are handwritten.',
'The old character before the new H remains illegible under the crossing strokes.',
'The faint mark over o is diagonal, not a pair of dots; the possible acute is retained as doubtful.',
'The small sign after the bracketed remark is a handwritten 4, now resolved.',
'The two dense cancellations are present, but the older parenthesis readings are not fully visible; new doubts retain that uncertainty.',
'The r cell of montrent has a typed overprint; the suspected underlying n is now marked doubtful.',
'The lower-left 52 is pencil archive foliation and is placed in the margin.',
'The rectangle is hand-drawn. Its contents mix typed and penned symbols, and the missing opening parenthesis in the initial transcription is restored from the scan.'
],summary='Both halves and enlarged boxed parenthesis, overwritten letters, accent, terminal sign and cancellation details inspected. Restored the visible opening parenthesis in the boxed formula and marked the pen frame, resolved the small 4, narrowed the possible accent, and added doubts where old letters or parentheses are actually covered. The literal (n-1)-groupoides in the comparison remains, despite the displayed construction having higher dimension. No mathematical index or classifying symbol is normalized.',differences={
831:(r'\Gamma_X(\mathcal C^{N-n}\mathcal F)','our transcription corrected','The supposedly missing opening parenthesis is visible in the scan; restoring it corrects our transcription rather than emending the author.'),
835:(r'1\leq i\leq n+1 .]\hand{$_4$}','our transcription corrected','The small handwritten 4 after the bracket is resolved; it is absent from the witness.'),
840:(r'\deleted{\unsure{(}}le (n+1) champ classifiant\deleted{\unsure{)}}','our transcription corrected','The source has no inserted hyphen after (n+1); the two cancelled old punctuation signs remain doubtful.'),
844:(r'\mspage{\hand{37}}; typed upper-right 5','our transcription corrected','Both visible top numbers are retained with their distinct positioning.')
})
