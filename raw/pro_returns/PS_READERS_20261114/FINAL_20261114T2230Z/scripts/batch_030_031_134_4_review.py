import sys,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT,OUT
variants=[]
key='ps_134-4_030';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'\longrightarrow',r'\hand{\longrightarrow}').replace(r'\hookrightarrow',r'\hand{\hookrightarrow}').replace(r'\to ',r'\hand{\to} ')
 if new!=line:edits.append(['\n'+line+'\n','\n'+new+'\n','These displayed and inline arrows are handwritten; their typed source and target symbols are preserved.'])
edits += [
 [r'\unsure{C}_h',r'\over[typed]{\illegible{1}}{C}_h','The live open-right capital C is readable, but its lower overlapping typed cell remains unidentified.'],
 [r'\xout{\unsure{containing R}}',r'\xout{containing R}','The cancelled containing and terminal capital R can be followed under the machine strikes.'],
 ['worth while',r'wor\over[typed]{\illegible{1}}{th} while','The final two letters are machine overprints with visible earlier stems; their complete older sequence is unreadable.'],
 [r'sequqnee\xout{s}',r'sequ\unsure{\over[typed]{q}{e}}nc\over[typed]{e}{e}\xout{\unsure{s}}','The middle cell shows a q descender and e-shaped type body with uncertain layer order. The next disputed letter is c, not e, and the final e has a repeated impression; the cancelled terminal cell remains tentative s.'],
 [r'\xout{For} \uline{Any}',r'\deleted{\xout{For}} \uline{Any}','A separate pen stroke crosses the already machine-cancelled For.'],
 [r'viewed\hand{,} as \inserted{denoting,}',r'viewed as \inserted[typed]{denoting}','Denoting is typed. The apparent commas are continuous ends of the insertion curves, not independent punctuation; as remains live.'],
 [r'\inserted{on M}',r'\inserted[typed]{on M}','On M is typed above the line and placed by a pen hook.'],
 [r'homotop\unsure{y}\xout{sm\illegible{1}} \inserted{structure} \inserted{$W_h$}',r'homotop\unsure{\over[typed]{j}{i}}sm\xout{notion} \inserted[typed]{structure} \inserted[typed]{$\over[typed]{\illegible{1}}{W}_h$}','The sm is visibly live and unstruck. The x cancellation begins in notion; structure is typed above it. The i/j cell remains doubtful. W_h is typed above on, with an obscured repeated old capital under W.'],
 [r'more\xout{ax}'+'\n'+'over',r'more\xout{ax}%'+'\n'+'over','Suppress a TeX word space at the physical line break; after the cancellation the live letters join moreover without an unseen hyphen.'],
 [r'\inserted{precisely}',r'\inserted[typed]{precisely}','Precisely is typed above the line; its pen placing curve does not cancel that.'],
 ['contractible}.',r'contractib\over[typed]{\illegible{1}}{le}}.','The last le has overlapping type impressions with earlier strokes; retain the obscured lower sequence rather than flatten it.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3686:['viewed as denoting','The apparent two commas are insertion-hook ends. The inserted word is typed and the intervening as is live.'],
 3688:['viewed as a','The typed as has a clear s; the witness a a is not the source reading.'],
 3690:['homotop[i/j]sm; cancelled notion; inserted structure','The sm is unstruck. The old notion is machine-cancelled and replaced with typed structure, not a change to homotopy. The i/j type layer remains doubtful.'],
 3693:['f_i:M to M','The two objects are visibly capital M, even though the paragraph discusses an object X. Preserve the author notation.'],
 3694:['id_M','The typed subscript is M, matching the displayed M-to-M source notation.']
 },'unsure':[
 [r'\over[typed]{\illegible{1}}{C}','The upper capital C is clear; its earlier typed cell is not.'],
 ['containing R','The old letters and terminal capital R remain readable beneath the x line.'],
 [r'\unsure{*}','The small mark is a dense star-like pen cluster, but its exact shape and purpose are unresolved.'],
 [r'\unsure{\over[typed]{j}{i}}','A dotted upright and a j-like descender overlap in this cell; no secure cancellation of the following sm exists.']
 ],'illegible':[['notion','The x-struck word following the live sm resolves as notion, with the t ascender and ion ending visible.']],
 'notes':[
 'The live capital C is readable over an unreadable older typed cell. The inclusion sign is penned.',
 'The small mark over sense remains a doubtful star-like ink cluster.',
 'As is live. The two apparent commas are continuous insertion-hook ends, and denoting is typed; independent root inspection agrees.',
 'The live word is homotop[i/j]sm with a doubtful letter layer. The sm is not cancelled; the cancellation starts in notion and the replacement structure is typed. Independent root inspection agrees.',
 'Precisely is typed and its placing curve leaves that live.',
 'The lower-left 30 is handwritten.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_030:object_letters','before':'maps f_i:M to M; id_M','after':'maps f_i:M to M; id_M','line':43,'decision':'retain author notation','reason':'The prose refers to an object X of M, but these formulas visibly use M. The guide flags the object/category-letter inconsistency rather than silently adopting the witness X.'},
 {'source_id':'OBS:ps_134-4_030:moreover','before':'\\uline{which are moeover contractib\\over[typed]{\\illegible{1}}{le}}','after':'\\uline{which are moreover contractib\\over[typed]{\\illegible{1}}{le}}','line':45,'decision':'master slip variant','reason':'The isolated missing r is settled by the correctly spelled moreover in the preceding paragraph of this same page, across a physical line break.'}
 ],'evidence':'Both original halves and twelve enlarged panels inspected. The first C resolves as a live capital over an unreadable older type cell. Containing R is recoverable under x strikes. Worth and the end of contractible show older type impressions, retained as unreadable layers. The sequence word has a q/e overlap, a clear c and a doubled final e; its terminal cancelled cell remains tentative. The star above sense remains uncertain. Denoting and on M are typed insertions; the supposed commas around denoting are placing-hook ends and as is live. The crucial homotopism passage keeps sm unstruck, cancels notion and inserts typed structure and W_h; only the i/j letter layer remains doubtful, independently corroborated by root. Precisely is typed and does not cancel that. The M-to-M and id_M formulas are literal source readings, retained despite their mismatch with the object X discussed in the prose.'})
variants.append({'key':key,'before':'\\uline{which are moeover contractib\\over[typed]{\\illegible{1}}{le}}','after':'\\uline{which are moreover contractib\\over[typed]{\\illegible{1}}{le}}','kind':'slip corrected','reason':'The missing r is isolated; the correctly spelled moreover occurs earlier on the same page.','source_id':'OBS:ps_134-4_030:moreover'})

key='ps_134-4_031';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'\hand{\Sigma}^{\circ}_{h}',r'\hand{\Sigma}^{\hand{\circ}}_{\hand{\unsure{\circ}}h}')
 if new!=line:edits.append(['\n'+line+'\n','\n'+new+'\n','The upper circle is penned. A separate dark lower circular mark sits before h; preserve it doubtfully without asserting its cancellation or chronology.'])
edits += [
 [r'\inserted{formal}',r'\inserted[typed]{formal}','Formal is typed above the line and placed by a pen hook.'],
 [r'first that \xout{xxxx}',r'first that \xout{\unsure{comes}}','The old word reaches the clipped edge; its visible c/o/m/e contours suggest comes, but the final cell is missing.'],
 ['this matter',r'th\over[typed]{\illegible{1}}{i}s matter','The i has a repeated type impression over an obscured older cell.'],
 [r'clear that \xout{xxx}',r'clear that \xout{any}','The old a/n and descending y remain visible beneath the x line.'],
 [r'\inserted{finite}',r'\inserted[typed]{finite}','Finite is typed interlinearly and placed by a pen hook.'],
 [r'products\xout{x}',r'product\unsure{\over[typed]{x}{s}}','The final s/x impressions occupy a single cell after t; there is no separate extra x cell. Retain uncertainty about layer order.'],
 [r'\xout{\unsure{of}}',r'\deleted{of}','The old o/f are legible beneath an oblique pen cancellation.'],
 ['Fl(M)',r'F\over{l}{l}(M)','The l is pen-retraced over typed l, not a slash or negation.'],
 ['filtering',r'filt\over{x}{e}ring','A clear handwritten e replaces a visible typed x.'],
 [r'out \xout{xxxx} it seems',r'out \xout{that} it seems','The cancelled that is legible beneath the x row.'],
 [r'\inserted{(This implies we assume M stable under finite products)}',r'\margin{(This implies we assume M stable under finite products.)}','This is a vertical handwritten marginal note, linked to the sentence by matching marks. The final period before the closing parenthesis is visible in the rotated detail.'],
 [r'\hand{\Sigma}_{\unsure{h|H}}',r'\hand{\Sigma}_{\unsure{\over{h}{h}}}','The subscript has a pen h-like retracing over a typed h-like cell; the exact layers remain doubtful rather than a clean choice of case.'],
 [r'dealt with \xout{xxx} so far',r'dealt with \xout{\unsure{can}} so far','The surviving rounded c/a and final n-like strokes support can under the x row, with doubt retained.'],
 ["``characteristic''",r"``characteristic\xout{g}''",'The live c is followed by a separate cancelled g, whose descender remains visible.'],
 [r'\uline{weak homotopy interval}',r'\uline{\over{w}{w}eak homotopy interval}','The initial w of the typed insertion is retraced in pen; the long underline belongs to the insertion and does not delete now would seem the.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3718:[r'Sigma with doubtful retraced h subscript','The subscript has a long pen ascender, lower loop and residual typed strokes. Retain the layered uncertainty; do not print the witness capital H as settled.'],
 3721:[r'four upper circles, each with a doubtful lower circular mark','The superscripts are small penned circles. Each has a separate lower ink/circular mark near h; its cancellation is not secure.']
 },'unsure':[
 ['of','The old o and f are readable beneath the oblique pen strike.'],
 [r'\unsure{\over{h}{h}}','Both a typed h-like form and a pen h-like form are visible, but the overlapping lower loop keeps the exact layers uncertain.'],
 [r'\unsure{\xout{,}}','The small mark has an x-shaped body and a dark descending stroke. A cancelled comma is possible but not certain.']
 ],'notes':[
 'The lower-left 31 is handwritten.',
 'The old word of is legible beneath an oblique pen cancellation.',
 'The Fl letter l is pen-retraced over a typed l.',
 'The final products cell is a single overlapping s/x cell with uncertain layer order; filtering has pen e over x; characteristic has a distinct cancelled extra g after its live c.',
 'The long line is continuous with the underline of the raised typed insertion. The lower words now would seem the have no independent cancellation and remain live.',
 'The small mark after chain remains a doubtful cancelled comma/ink mark; its shape is not sufficiently secure to remove the doubt.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_031:structure','before':'structu-%\nte','after':'structu-%\nre','line':19,'decision':'master slip variant','reason':'The isolated t for r in the split word is settled by correctly typed structure repeatedly on this same page.'},
 {'source_id':'OBS:ps_134-4_031:generating','before':r'\uline{generat} -%'+'\n'+r'\uline{ting}','after':r'\uline{genera} -%'+'\n'+r'\uline{ting}','line':39,'decision':'master slip variant','reason':'The split word contains a duplicated t. Generating is correctly typed in both the heading and the last line on this page.'}
 ],'evidence':'Both original halves, thirteen enlarged panels and a correctly rotated margin detail inspected. Formal and finite are typed insertions. The first cancelled word is tentatively comes at a clipped edge; any, of and that are recoverable, and can remains tentative. The Fl l is pen-retraced. Products has one overlapping s/x terminal cell, not a clean plural followed by an extra cancelled x. Filtering has pen e over typed x, while characteristic retains a live c and a separate machine-cancelled g. The last typed weak-homotopy-interval insertion has a pen-retraced w, and its long underline does not cancel the lower text. The vertical marginal note includes a period before its closing parenthesis and is restored as marginal content. The h subscript remains doubtful. All four upper circles are pen-written; the separate lower circular marks are retained doubtfully, with no unsupported cancellation or relocation chronology, consistent with independent root inspection of the first detail.'})
variants += [
 {'key':key,'before':'structu-%\nte','after':'structu-%\nre','kind':'slip corrected','reason':'Isolated t for r; structure is correctly typed elsewhere on the page.','source_id':'OBS:ps_134-4_031:structure'},
 {'key':key,'before':r'\uline{generat} -%'+'\n'+r'\uline{ting}','after':r'\uline{genera} -%'+'\n'+r'\uline{ting}','kind':'slip corrected','reason':'Isolated duplicated t; generating is correctly typed in the heading and last line.','source_id':'OBS:ps_134-4_031:generating'}]
p=OUT/'records/MASTER_VARIANTS_134_3_4.json';old=json.loads(p.read_text());ids={v['source_id'] for v in variants};p.write_text(json.dumps([v for v in old if v['source_id'] not in ids]+variants,ensure_ascii=False,indent=2)+'\n')
