import sys,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT,OUT
variants=[]
key='ps_134-4_046';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text()
edits=[
 [r'\xout{\unsure{xxwxxk}}',r'\xout{a weak}','The cancelled a weak resolves through the regular x row.'],
 [r'\xout{\unsure{inxnot}}',r'\xout{\unsure{is|in} not}','Not is clear below the strike; the second letter of the first word remains ambiguous between s and n.'],
 ['55.     Let',r'\hand{55.}     Let','The two fives and point are handwritten.'],
 [r"\xout{(M,h)xxandx(M',h')xxsayx}",r"\xout{(M,h) and (M',h') say}",'The words and, say, both pairs and the primes are visible below machine strikes; x impressions over spaces are not old letters.'],
 ['The assumptions',r'T\unsure{\over[typed]{h}{H}}e assumptions','The h has a displaced lower H-like impression with regular serifs. The typed-layer reading is plausible but its exact form remains doubtful.'],
 ['The natural definition',r'T\unsure{\over[typed]{h}{H}}e natural definition','The h has an added low crossbar and paired descending serifed stems, consistent with a displaced typed H; retain the layer doubt.'],
 ['The existence',r'T\over[typed]{h}{H}e existence','The regular capital H over the lowercase h is unambiguous in the enlarged panel.'],
 [r'\inserted{weak}',r'\inserted[typed]{weak}','Weak is interlinear typing with a pen placement curve, not a pen-written word.'],
 [r'\Sigma^{0}_{\hand{h}_1}',r'\hand{\Sigma}^{0}_{\over{\unsure{h}}{h}_1}','Sigma is penned. The subscript h is penned over a partially obscured typed h-like cell, whose lower reading remains doubtful.'],
 [r'\Sigma^{0}_{h_1}',r'\hand{\Sigma}^{0}_{h_1}','The second Sigma is also penned; its remaining index is typed.'],
 [r'\xout{\illegible{1}}',r'\xout{\unsure{handies}}','The old word now offers a plausible handies reading, with h, a, d, i, e, s fairly visible; the crossed middle cell prevents certainty.']
]
old=src[src.index(r'\diagram{'):src.index(r'\end{tikzcd}')+len(r'\end{tikzcd}')]
new=old.replace(r'\ar[',r'\ar[color=blue, ')
edits.append([old,'% Hand-drawn arrows are marked blue; typed objects remain plain.\n'+new,'All four square arrows are pen-drawn; the objects and u labels remain typed. Preserve topology.'])
save_review({'key':key,'edits':edits,'diffs':{
 3991:['55. with no descriptive title','The section starts with the handwritten number and the running sentence, not the witness title.'],
 3992:['which give rise','Which is clearly typed in the definition.'],
 3998:[r'u(\underline{h})','The final argument is a typed lowercase h with an underline, not I. Preserve this apparent authorial notation slip.']
 },'unsure':[
 ['a weak','The old phrase is fully readable beneath the machine row.'],
 [r'\unsure{is|in} not','Not resolves, but the old first word remains ambiguous in its second cell.']
 ],'illegible':[
 [r'\illegible{1}','The pen c covers most of the lower cell before an; no secure earlier character can be recovered.'],
 [r'\unsure{handies}','The enlarged run permits a tentative handies reading but not a settled whole word.']
 ],'notes':[
 'A weak resolves. The later cancelled phrase resolves only as is/in not, retaining the ambiguous second letter.',
 'Both I-to-e arrows, the u arrow, all four diagram arrows, the displayed tildes and membership signs are drawn by hand. The mixed diagram now records arrow provenance explicitly.',
 'The three specified The patches are retained as typed h/H layers. The existence patch is clear; the two lower displaced impressions remain doubtful. The earlier The trouble is ordinary typing.',
 'The first Sigma is handwritten, and its h is handwritten over a lower typed h-like cell that remains doubtful. The second Sigma is also penned.',
 'The t at the physical respec- line ending is crossed by a typewriter horizontal impression. The existing typewriter-deletion encoding is retained with its physical word-break hyphen.',
 'The folio 46 is in pencil at lower left.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_046:asperic','before':'W-asperic','after':'W-aspheric','line':16,'decision':'master slip variant','reason':'The unique typed omission of h is settled by the correctly typed W-aspheric vocabulary throughout the adjacent reviewed pages, including 134-4/044.'}
 ],'evidence':'Both original halves and nine enlarged detail panels inspected. The old a weak resolves, while is/in not remains partly doubtful. The section number is penned and has no title. The three specified The patches show regular serifed H-like layers over h, two displaced low and kept doubtful. The four commutative-square arrows are handwritten with plain typed objects and labels. Weak is typed interlinearly. The first Sigma and both Sigma glyphs are penned; the first subscript h retains an uncertain lower typed layer. The lower cell under c in can stays unreadable, and the old word before most economic is tentatively handies. The physical respec- ending has a typewriter cancellation of t. The final formula is literally u of underlined h, not the interval I; it is preserved and flagged in the guide.'})
variants.append({'key':key,'before':'W-asperic','after':'W-aspheric','kind':'slip corrected','reason':'Unique omitted h in the established, repeatedly attested W-aspheric terminology.','source_id':'OBS:ps_134-4_046:asperic'})

key='ps_134-4_047';edits=[
 [r'T\hand{h}e case',r'T\over{h}{h}e case','The h is penned over a typed h, with a long new ascender; it is not an isolated inserted character.'],
 [r'commu\unsure{y}ta-',r'comm\unsure{\over[typed]{y}{u}}ta-','The u/y impressions occupy one typed cell. Their layer order is not securely visible; retain the doubtful overprint rather than adding an extra separate y.'],
 [r'\inserted{(generating)}',r'\inserted[typed]{(generating)}','Generating and its actual parentheses are typed interlinearly inside an outer pen placing curve; contractor remains live beneath that curve.'],
 [r'\inserted{(for $h_2$}',r'\inserted[typed]{for $h_2$}','For h_2 is typed above the line. Its apparent opening parenthesis is the left end of the continuous placement curve, not textual punctuation.'],
 ['Fl(M)',r'F\over{l}{\ell}(M)','The l is typed with a slanting pen overstroke, as in neighboring pages.'],
 [r'\inserted{(for strict compatibility, i.e. $W_h \subset W$}',r'\inserted{for strict compatibility, i.e. $W_h \subset W$}','The apparent opening parenthesis belongs to the continuous pen curve placing this inserted phrase; it is not independent punctuation.'],
 [r'to check that \xout{xx} for',r'to check that \xout{\illegible{1}} for','The two old cells under the insertion curve are unrecoverable.'],
 [r'\deleted{(which is}',r'\unsure{(}\deleted{which is}','The pen strike clearly cancels which is, but its contact with the opening parenthesis does not securely establish deletion of that parenthesis. Preserve the doubtful opening, matching the surviving final close without asserting restoration.'],
 ['this condi-tion','this condi-%\ntion','The pen word condition is divided by a physical line ending; record the break rather than an internal spelling hyphen.'],
 [r'\xout{\illegible{2}}',r'\xout{necessary and}','Both old words necessary and are legible through the machine cancellation.'],
 [r'\inserted{supposed}',r'\inserted[typed]{supposed}','Supposed has regular typewriter letters above a pen placing curve.'],
 [r'\xout{that provided we \illegible{1}}',r'\xout{that provided we assume}','Assume is recoverable at the end of the cancelled line.'],
 [r'\xout{\unsure{even} that strengthen the}',r'\xout{even that strengthen the}','The complete old sequence even that strengthen the is legible through its x row.'],
 ['\n4.4.\n','\n'+r'\hand{4.4.}'+'\n','The date is handwritten.'],
 [r'(\xout{xxx} paragraph 48)',r'(\xout{\illegible{1}} paragraph 48)','The old short run before paragraph is crossed by machine type and cannot be recovered.'],
 [r'The \inserted{presumable}',r'T\over{h}{h}e \inserted[typed]{presumable}','Presumable is typed interlinearly, and the h of The is pen-retraced below its typed layer. The placing curve does not cancel factor through.'],
 [r'\deleted{the} \inserted{a}',r'\deleted{\xout{the}} \inserted[typed]{a}','The old the shows machine x impressions and a horizontal pen stroke; the replacement a is typed above it.'],
 ['to correspond to',r'to bor\over{r}{r}espond to','The first cell is a clear typed b, while the second r is pen-retraced. Preserve the scanned borrespond here; record the isolated typing slip separately for corrected forms.'],
 [r'\xout{\unsure{over}}',r'\inserted[typed]{\xout{over}}','Over is a legible raised typed word cancelled by machine strikes.'],
 [r'\xout{xx}aspheri',r'\deleted{\xout{\illegible{1}}}aspheri','The old cells before aspheric are crossed by both machine and pen, with no settled lower reading.'],
 [r'\margin{$e_{A^\wedge}$}',r'\margin{\diagram{\begin{tikzpicture}[baseline=-.4ex,x=1em,y=1ex]\node[color=blue] at (0,0) {$e_{A^\wedge}$};\draw[color=blue,line width=.4pt] (0,0) ellipse (1.2 and 1.8);\end{tikzpicture}}}','The marginal e with A-hat subscript is enclosed by a pencil oval; reconstruct the omitted enclosure.'],
 [r'\inserted{over $e_{A^\wedge}$}',r'\inserted[typed]{over $\hand{e_{A^\wedge}}$}','Over is typed above the line, while the accompanying e-with-A-hat formula is pen-written. The continuous curve leaves under the live.'],
 [r'\xout{xxx} \over{i}{I}n',r'\xout{\illegible{1}} \over[typed]{i}{I}n','The old short run is unreadable. The capital I is a regular serifed type impression over the lower i.'],
 [r'\inserted{homotopy}',r'\inserted[typed]{homotopy}','Homotopy is typed interlinearly and placed after of by a pen curve.']
]
save_review({'key':key,'edits':edits,'diffs':{
 4003:['u(I) will be equally a contractor','The I is a plain typed capital with no underline.'],
 4006:['In the two precedent paragraphs','Two is plainly typed and remains live.'],
 4008:['u or W are compatible','The verb are is clearly typed; it is not normalized to the witness is.'],
 4014:['56., corrected from 55., with no descriptive title','Only the numbered opening follows the date; the long witness title is absent.'],
 4015:[r'condition\unsure{s}','The word reaches the clipped edge; a terminal s-like fragment remains visible but cannot be fully certified.'],
 4018:[r'i^*(Delta)','The handwritten argument is a triangular capital Delta, not an underlined I.'],
 4020:['contractible generating homotopy interval Delta in M','The second handwritten interval symbol is also clearly Delta.']
 },'unsure':[
 [r'\unsure{\over[typed]{y}{u}}','The u and y occupy the same typed cell; their order remains uncertain.'],
 [r'\unsure{structures}','The live pen word is structures, but several old middle letters are hidden, so the lower structures candidate remains doubtful.'],
 [r'\unsure{x}','The small crossed old character after Sigma has x-like lower strokes and an upper pen hook; its original reading is not secure.'],
 ['even','The e-v-e-n letters remain distinguishable under their x impressions.'],
 [r'\unsure{s}','The terminal letter is clipped at the page edge and remains tentative.'],
 ['over','All four letters are readable in the cancelled raised type.']
 ],'illegible':[
 ['necessary and','Both words resolve in the enlarged lower line.'],
 ['assume','The final old word is readable as assume beneath the machine strikes.']
 ],'notes':[
 'The first h is penned over the typed h; both layers are now recorded.',
 'U/y share one typewriter cell and remain doubtful in layer order. Generating and parentheses are typed above contractor; their outer placing curve does not cancel contractor.',
 'The live pen word structures is clear, while the underlying typed middle remains obscured, so its candidate is retained as doubtful.',
 'The small crossed character after the generating-family index remains doubtful; no clean x reading is imposed.',
 'The live replacement begins this condi- at the right, continues tion is also necessary on the next physical line, and precedes the cancelled and conversely phrase. Necessary and resolves in the old typed line. The opening parenthesis has uncertain strike scope and is retained with doubt.',
 'The first cancelled line resolves as that provided we assume; the next resolves as even that strengthen the.',
 'Presumable and homotopy are typed insertions. The curve placing presumable leaves factor through live; the h of The beneath it is pen-retraced.',
 'The weak-homoto word runs to the edge before next-line py, and the terminal s of conditions is clipped and remains doubtful.',
 'Over is typed, the e-with-A-hat formula is penned, and their continuous placing curve does not independently cancel the in under the. The repeated margin formula has a pencil oval.',
 'The lower-left folio 47 is pencil.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_047:borrespond','before':r'bor\over{r}{r}espond','after':r'cor\over{r}{r}espond','line':41,'decision':'master slip variant','reason':'The isolated typed b for c is settled by correctly typed correspond in reviewed 134-4/036, line 40, and 134-4/015. Preserve the independent pen r retracing in both forms.'}
 ],'evidence':'Both original halves, fourteen first detail panels and six extra panels inspected. The first h and the h below presumable are pen-retraced over type. The apparent extra y in commutation is instead a same-cell u/y type overprint whose order remains doubtful. Generating with actual parentheses, for h_2, supposed, presumable, a, homotopy and the two over words are typed insertions; only the first raised over is cancelled. Contractor, factor through, and under the remain live beneath placing curves. The apparent opening parentheses before for h_2 and for strict compatibility are curve ends. In the rewritten strict-compatibility passage the open parenthesis before which is has uncertain strike scope and is retained with doubt; the ending parenthesis remains typed. Necessary and, assume, even and over resolve beneath machine strikes. The final s at the clipped conditions edge and the old structures/isolated x remain doubtful. Delta is clear in both test-functor formulas. Borrespond has a literal typed b and a retraced second r; its isolated slip is handled only by a separate corrected-form variant. The margin formula has an omitted pencil oval, now reconstructed.'})
variants.append({'key':key,'before':r'bor\over{r}{r}espond','after':r'cor\over{r}{r}espond','kind':'slip corrected','reason':'Isolated typed b for c; correspond is correctly typed in reviewed 134-4/036 and 134-4/015.','source_id':'OBS:ps_134-4_047:borrespond'})
p=OUT/'records/MASTER_VARIANTS_134_3_4.json';old=json.loads(p.read_text());ids={v['source_id'] for v in variants};p.write_text(json.dumps([v for v in old if v['source_id'] not in ids]+variants,ensure_ascii=False,indent=2)+'\n')
