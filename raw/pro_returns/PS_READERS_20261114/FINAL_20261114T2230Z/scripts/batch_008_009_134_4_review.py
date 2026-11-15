import sys,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT,OUT
variants=[]
key='ps_134-4_008';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace('A_{//C}',r'A_{\hand{//}C}').replace('A_{/C}',r'A_{\hand{/}C}').replace(r'A_{/i^{*}(C)}',r'A_{\hand{/}i^{\hand{*}}(C)}')
 if r'\begin{tikzcd}' in line:
  new=new.replace(r'\ar[r]',r'\ar[r,color=blue]').replace(r'\ar[u]',r'\ar[u,color=blue]')
  new='% Hand-drawn arrows are marked blue; typed objects remain plain.\n'+new
 if new!=line:edits.append([line,new,'The category-of-elements slashes and first asterisk are penned; the three diagram arrows are penned while the objects and product x are typed.'])
edits += [
 [r'\mspage{96}',r'\mspage{(96)}','The folio has typed parentheses.'],
 ['key result',r'key \over[typed]{t}{r}esult','The first letter of result is typed over a t-shaped impression.'],
 ['Here one',r'\over[typed]{H}{H}ere one','The initial H has repeated type impressions.'],
 ['careful with',r'careful \over{\unsure{w}}{w}\over{i}{i}th','The w and i are retouched in pen; the older w cell is crowded and remains uncertain.'],
 ['gives rise\nto',r'give\over{s}{s} \over{r}{r}\over{i}{i}se'+'\nto','The final s and the r/i of rise are pen-retraced.'],
 ['functorial for varying',r'functorial f\over[typed]{o}{o}r varying','The o has two offset type impressions.'],
 ['The second is',r'T\over[typed]{H}{h}e second is','The capital H is displaced upward beneath the lowercase h.'],
 [r'\inserted{again}',r'\inserted[typed]{again}','Again is typed above the line. The curve below it places the insertion and does not cancel to.'],
 ['There is',r'T\over[typed]{H}{h}ere is','There has the same upward-displaced H/lowercase h type overlap.'],
 [r'\xout{rather a}\inserted{a}',r'\xout{rather a}\hand{\unsure{a}} \inserted{a}','A separate a-like pen loop lies over the cancelled text; its status is uncertain. The clear replacement a before more is a separate handwritten insertion.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3268:['with fibers which need not be discrete','The source relative pronoun is which.'],
 3276:['may well generalize to more general situations','The source reads more, with o.']
 },'unsure':[[r'\unsure{a}','The single machine-cancelled cell after second is too dense to identify securely.']],
 'notes':[
 'The comma after C is pen-added and the first i* asterisk is handwritten. The category slashes throughout and the diagram arrows also have pen forms.',
 'No hyphen is visible after suitab before the scan edge; none is supplied.',
 'The g is crossed by a machine x and a distinct following hyphen survives.',
 'All three diagram arrows are pen-drawn, with typed objects. They are marked blue without altering topology; the later double arrow is also penned.',
 'Again has typewriter letterforms above the line; its pen placing curve passes over to without deleting it.',
 'The machine-cancelled extra cell after second remains tentatively a.',
 'Here repeats H, result has typed t/r, for repeats o, and The/There have vertically offset H/h impressions. With and gives rise contain pen retracing.',
 'Rather a is machine-cancelled. A separate small a-like pen loop over the cancellation is unresolved; the clear final a with its placing slash is retained as the replacement.',
 'The lower-left 8 is handwritten. The typed folio is (96), including parentheses.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_008:there','before':'that their is a canonical','after':'that there is a canonical','line':9,'decision':'master slip variant','reason':'The source their is is an isolated wrong form in this existential construction; there is occurs on this same leaf. Diplomatic preserves their.'},
 {'source_id':'OBS:ps_134-4_008:identifying','before':'Identifiying a set','after':'Identifying a set','line':24,'decision':'master slip variant','reason':'The extra i is isolated; the correct same word identifying occurs on this leaf before C with the full subcategory.'},
 {'source_id':'OBS:ps_134-4_008:constant','before':'identifying C with the full subcategory of constant functors','after':'Source claim retained; its generality needs a connected nonempty domain.','line':31,'decision':'retain mathematical qualification for guide','reason':'For arbitrary i(a), natural transformations between constant functors can vary by connected component; if i(a) is empty, even the objects collapse. The later contractibility hypothesis supplies the needed condition.'}
 ],'evidence':'Both original halves and eleven enlarged panels inspected. The first i* star, all category slashes and the three diagram arrows are penned. The folio parentheses are restored. The comma after C is pen-added, while the line-end g is machine-cancelled and the hyphen is visible. The extra cell after second remains doubtful. Again is a typed insertion whose curve leaves to live. Type overlaps in Here, result, for and The/There are recorded, and pen retouching in with and gives rise is distinguished. The cancelled rather a has an additional uncertain pen loop, beside a clear replacement a. Literal their and Identifiying are retained diplomatically with explicit same-page slip variants.'})
variants += [{'key':key,'before':'that their is a canonical','after':'that there is a canonical','kind':'slip corrected','reason':'The existential construction and same-page there is settle the isolated wrong form.','source_id':'OBS:ps_134-4_008:there'},{'key':key,'before':'Identifiying a set','after':'Identifying a set','kind':'slip corrected','reason':'The same word identifying is correctly typed later on this page.','source_id':'OBS:ps_134-4_008:identifying'}]

key='ps_134-4_009';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%') or line.startswith(r'\inserted[on'):continue
 new=line.replace(r'\longrightarrow',r'\hand{\longrightarrow}').replace(r'\rightarrow',r'\hand{\rightarrow}').replace(r'A^{\wedge}',r'A^{\hand{\wedge}}').replace('A_{/C}',r'A_{\hand{/}C}').replace('A_{//C}',r'A_{\hand{//}C}')
 if new!=line:edits.append([line,new,'The arrows, carets and category slashes are drawn in pen.'])
edits += [
 [r'\mspage{97}',r'\mspage{(97)}','The typed folio has parentheses.'],
 ['condi-%\n'+r'\inserted[on i: $A\rightarrow$ (Cat)]{and A,}'+'\ntions which', 'condi-%\ntions '+r'\inserted[typed]{on i: $A\hand{\rightarrow}$ (Cat)} \inserted{and A,} which','On i: A (Cat) is typed above the line with a pen arrow, and and A, is handwritten. Their placing curve attaches after the complete word conditions and before which.'],
 [r'\deleted{equivalent}\inserted{isomorphic}',r'\deleted{equivalent} \inserted{isomorphic}','The replacement isomorphic is a separate handwritten word.'],
 ['therefore the functor',r'therefore t$\underset{\hand{\unsure{\scriptscriptstyle z}}}{\mathrm h}$e functor','A small dark zigzag-like pen mark lies below h. The underlying typed h remains visible; the mark is not resolved as an older letter.'],
 [r'\xout{induced a}\inserted[the]{}',r'\xout{\illegible{1}\unsure{induced a}} \inserted[typed]{\unsure{\over[typed]{i}{t}}he}','The cancellation spans more cells than induced a alone. The obscured prefix remains unreadable; induced a is tentative. The replacement the is typed above it, with a crowded first-cell overprint.'],
 [r'\xout{fib}',r'\deleted{fib}','Fib is crossed by two continuous pen strokes, not a regular row of machine x marks.'],
 ['Then u',r'T$\underset{\hand{\unsure{\scriptscriptstyle\times}}}{\mathrm h}$en u','A small crossed pen mark sits at the foot of h; its function is uncertain.'],
 [r'amount\xout{\unsure{s}}',r'amount\unsure{s}','The final cell is cramped at the clipped edge, without a secure independent machine cancellation. Retain the probable s as live but doubtful.'],
 ['objects i(a)',r'object\over[typed]{s}{s} i(a)','The final s has offset repeated type impressions.'],
 ['*9.4. Actually this is done only a lot later, on page 121 and (for the converse) on page 143.','*9.4. Actually, this is done only a lot later, on page 121 and (for the converse) on page 143.','A short comma stroke follows Actually in the handwritten marginal note.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3277:['and A, which will ensure','The inserted and A, is handwritten; the following which is typed and live.'],
 3284:[r'the functor\xout{s}','The final s has a regular typed x cancellation, leaving singular functor.']
 },'unsure':[[r'\unsure{s}','The final cell is overprinted at the clipped edge, but an independent cancellation cannot be established; preserve the probable s live and doubtful.']],
 'notes':[
 'The inserted on i: A (Cat) is typed; its arrow, and A, and placing curve are handwritten. The insertion belongs between conditions and which.',
 'A dark zigzag-like mark is below the typed h of the. Its identity is unresolved and represented with a doubtful graphic.',
 'The cancelled phrase has an unreadable prefix beyond the tentative induced a. The replacement the is typed above the line, with a doubtful i/t-like first-cell overlap.',
 'The end of amounts is clipped and overprinted. The probable s is retained without asserting cancellation.',
 'The final s of objects has repeated type impressions.',
 'Then has a small cross-like mark at the foot of h. It remains a doubtful pen graphic, without deleting the h.',
 'The lower-right 9 is handwritten. The dated 9.4 note has a visible comma after Actually and clearly refers to pages 121 and 143; the inserted o in terminology is penned below the line.'
 ],'extra_records':[{'source_id':'OBS:ps_134-4_009:cartesian','before':'or F and G are fibering and i is cartesian.','after':'Source i retained; the quantified functor is u.','line':39,'decision':'retain mathematical slip for guide','reason':'The proposition quantifies u:F→G and its fibers u_a. The i in condition b has no defined role there; the witness silently substitutes u.'}],
 'evidence':'Both original halves and seven enlarged panels inspected. The mixed typed/handwritten condition insertion is moved to its actual attachment between conditions and which. Equivalent is pen-cancelled in favor of handwritten isomorphic. The cancelled text before the inserted the is longer and less secure than the draft; its unreadable prefix and tentative remaining letters are preserved. The small marks under the and Then remain graphic doubts. Fib is pen-cancelled, while the s of functors is machine-cancelled. The final s of amounts is clipped without secure deletion and remains live but doubtful. The s of objects is retyped. The complete dated marginal note, including the visible comma after Actually, is retained.'})
p=OUT/'records/MASTER_VARIANTS_134_3_4.json';old=json.loads(p.read_text());ids={v['source_id'] for v in variants};p.write_text(json.dumps([v for v in old if v['source_id'] not in ids]+variants,ensure_ascii=False,indent=2)+'\n')
