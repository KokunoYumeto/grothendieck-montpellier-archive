import sys,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT,OUT
variants=[]
key='ps_134-4_028';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'\subset',r'\hand{\subset}').replace(r'J \to I',r'J \hand{\to} I').replace(r'\sim',r'\hand{\sim}').replace(r'\Longleftrightarrow',r'\hand{\Longleftrightarrow}').replace('Fl(M)',r'F\over{l}{l}(M)')
 if new!=line:edits.append(['\n'+line+'\n','\n'+new+'\n','The inclusion and homotopy signs and the implication arrow are handwritten; Fl has a typed l retraced in pen. The displayed J-to-I arrow is also penned.'])
edits += [
 [r'\inserted{We assume M stable under finite products.}'+'\n'+r'\margin{X} C) \inserted[typed]{\uline{Weak}} \uline{Homotopy intervals}.',r'\margin{X} C) \inserted[typed]{\uline{Weak}} \uline{Homotopy intervals}. \inserted{We assume M stable under finite products.}','The long insertion curve places the handwritten assumption after the heading and before The type, not before C).'],
 [r'\xout{\unsure{sub}}set',r'\xout{sub}set','The surviving s/u and ascender of b identify the cancelled prefix.'],
 [r'\xout{\unsure{Any}} Any',r'$\overset{\hand{\smile}}{\underset{\hand{\frown}}{\text{\deleted{\xout{\unsure{Any}}}}}}$ Any','The old word remains doubtful under both machine and pen cancellation. Small upper and lower curved pen marks are also visibly present and retained graphically.'],
 ['it seems;  the natural',r'it seems;  th\over{e}{e} natural','The e of the is pen-retraced.'],
 [r'is in $\hand{\Sigma}_h$',r'\over[typed]{\illegible{1}}{i}s in $\hand{\Sigma}_h$','The i has overlapping typed impressions over a covered earlier cell.'],
 ['THe assumption',r'\over{T}{T}He assumption','The capital T is pen-retraced, while the following typed capital H remains live.'],
 ['mapping the two',r'mapping the\ensuremath{{}_{\mathrm o}} two','A small typed o is visibly below the e of the. Its function is not inferred, but the source mark is preserved.'],
 [r'\xout{\illegible{1}} \inserted[typed]{given}',r'\xout{\unsure{fixed}} \inserted[typed]{given}','The old word has f/i and a final d-like ascender under the strikes, supporting fixed as a tentative reading.'],
 [r'the \xout{\illegible{1}} equivalence',r'the \xout{\unsure{one}} equivalence','The surviving rounded first/last cells and middle n-like stems support one, without settling the heavily crossed letters.'],
 [r'equivalence relation \xout{\illegible{1}} in',r'equivalence relation \xout{\unsure{given}} in','An initial g descender and the sequence of following cells support given beneath the x row.'],
 [r'homotopy relation \xout{\illegible{1}} (with',r'homotopy relation \xout{\unsure{between arr}} (with','The cancelled span visibly begins between and ends in arr-like stems; the exact fragment remains doubtful.'],
 ['redpect',r're\unsure{\over[typed]{d}{s}}pect','Both a raised d stem and an s-shaped body are present. Preserve the uncertain layer order instead of printing a clean d or s.'],
 [r'the\xout{t} relation',r'th\over{e}{e}\deleted{\xout{t}} relation','The e is pen-retraced and the following t has both machine cancellation and a separate diagonal pen stroke.'],
 ['THe corresponding',r'T\over{H}{h}e corresponding','The capital H is corrected to a lower h by a clear long pen ascender and low shoulder.'],
 [r'homotopism\xout{s}',r'homotopism\unsure{\over{s}{s}}','The final cell is a dense pen-marked glyph with no independently identifiable x or cancellation stroke. Retain a doubtful live s layer; deletion is not established.'],
 [r'Now,  if \xout',r'Now,  i$\overset{\hand{\frown}}{\text{\over{f}{f}}}$ \xout','The f is pen-retraced and has a separate small curved mark above it.'],
 [r'\over{\unsure{\Sigma}}{R}_h',r'\over{\illegible{1}}{R}_h','The pen R covers an older typed angular letter; a Greek Sigma cannot be securely read there.'],
 [r'\inserted{weak} \unsure{h|H}omotopy',r'\inserted[typed]{weak} \over{H}{h}omotopy','Weak is typed interlinearly. The following H is corrected to h by pen, whose long ascender and low shoulder are visible.'],
 [r'\xout{\illegible{1}}may',r'\unsure{\over[typed]{\illegible{1}}{may}}','May occupies the same cells as earlier dark lettering and lower cancellation strokes; it is not a separate following word. Preserve uncertainty about the exact lower layer and typing/pen sequence.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3640:['marginal X','A large pencil X is plainly present to the left of C).'],
 3648:['organigram','The source gives the word organigram, not a numbered figure reference.'],
 3653:['barred Sigma_h','The Sigma has a separate short bar above its upper stroke; retain it.'],
 3655:['weak homotopy intervals','Weak is actually typed above the line and inserted by a pen curve; the H is corrected in pen.'],
 3656:['R_h','The subscript beside R is lowercase h.'],
 3659:['weak homotopy interval structure','The underlined heading at the foot ends in singular structure.']
 },'unsure':[
 ['sub','The s/u and final b ascender remain readable through the machine strikes.'],
 [r'\unsure{Any}','The old cells are obscured by both x impressions and pen strokes; the small curved marks do not settle the letters.'],
 [r'\illegible{1}','The older letter under R is angular and typed but cannot be securely named.'],
 [r'\over{H}{h}','The lower-case h has a long pen ascender and low shoulder over typed H.'],
 [r'\unsure{sub}','The final prefix is genuinely diagonally pen-cancelled, but its old letters remain too covered to resolve fully.']
 ],'illegible':[
 [r'\unsure{fixed}','The first and last typed stems support fixed, with internal uncertainty retained.'],
 [r'\unsure{one}','The rounded cells suggest one; the x row prevents certainty.'],
 [r'\unsure{given}','A g descender and the remaining cells suggest given, with doubt retained.'],
 [r'\unsure{between arr}','Between and arr-like terminal strokes can be followed, but the exact cancelled fragment is uncertain.'],
 [r'\illegible{1}','The earlier lettering under may remains unreadable; the upper and lower layers are no longer falsely separated into successive words.']
 ],'notes':[
 'Weak is typed and underlined. The mark over the initial H belongs to the continuous insertion curve, so no H-to-h correction is asserted in the heading.',
 'The cancelled Any remains doubtful. Both pen cancellation and small upper/lower curves are preserved.',
 'The small typed o below the e of the is restored; it has no assigned mathematical meaning.',
 'The suspect cell contains both a d ascender and s-shaped type. The layer order remains doubtful.',
 'No independent cancellation stroke or x is visible through the final s. Retain a doubtful marked s rather than deleting it.',
 'The older letter under R is unreadable. The H of homotopy is visibly corrected to h by pen; weak is typed above it.',
 'May is a multilayer overprint rather than a new word after an independently deleted old word; the old layer and exact provenance remain doubtful.',
 'The final sub prefix is diagonally pen-cancelled, but its letters retain doubt.',
 'The lower-left 28 is handwritten.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_028:notation','before':'R_h subset bar R_h; R_h satisfies (Sat 3); subset of Int(M) containing R_h','after':'R_h subset bar R_h; R_h satisfies (Sat 3); subset of Int(M) containing R_h','line':40,'decision':'retain author notation','reason':'These R symbols are visibly typed, even though the surrounding construction concerns a set of intervals Sigma_h. The guide flags the change of mathematical level without silently replacing the symbols.'},
 {'source_id':'OBS:ps_134-4_028:duplicate_we','before':'we\nwe','after':'we','line':37,'decision':'master slip variant','reason':'The same live typed word we is duplicated across consecutive physical lines after a cancelled clause. Corrected forms suppress this isolated repetition.'}
 ],'evidence':'Both original halves and twenty enlarged panels inspected. The large marginal X and two weak insertions are visible; both weak words are typed, while the finite-product assumption is penned and placed after the C heading. The old sub prefix resolves, but the old Any remains doubtful under machine and pen cancellation with small upper/lower curves. A typed o below the e of the is restored. Several cancelled words now have explicitly tentative readings fixed, one, given and between arr. The redpect cell has overlapping d/s type and retains layer uncertainty. The final s of homotopism is a dense marked glyph without a secure cancellation, independently confirmed by root. The Sigma bar and the lowercase h subscript are present. The old letter beneath pen R is unreadable; later weak is typed and H is pen-corrected to h. May is a multilayer overprint, not an additional word after an old deletion. The typed formulas retain R where the surrounding discussion concerns intervals, and the repeated we is recorded separately as an isolated typing slip.'})
variants.append({'key':key,'before':'we\nwe','after':'we','kind':'slip corrected','reason':'The same live word is duplicated on consecutive physical lines after a cancelled clause.','source_id':'OBS:ps_134-4_028:duplicate_we'})

key='ps_134-4_029';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line
 for m in ['hookrightarrow','to','subset']:new=new.replace('\\hand{$\\'+m+'$}','\\hand{\\ensuremath{\\'+m+'}}')
 if new!=line:edits.append(['\n'+line+'\n','\n'+new+'\n','Repair nested math delimiters in the scan-confirmed handwritten arrows/inclusion signs; their readings do not change.'])
edits += [
 [r'\hand{$\Sigma_h$}\xout{xxxf}',r'\hand{$\Sigma_h$}\deleted{\xout{\illegible{1}}}\unsure{f}','The replaced span has machine x marks and pen cancellation, but the following typed f has no independent visible strike. Preserve that residual f with uncertainty about its relation to the cancelled span.'],
 [r'The\xout{x}',r'Th\over{e}{e}\deleted{\xout{\illegible{1}}}','The e is pen-retraced; the following old cell is obscured by both pen and machine cancellation.'],
 [r'\xout{xxxxxx} set',r'\xout{\unsure{we get}} set','The surviving w/e and g descender support we get under the x row, but the exact cancelled phrase remains doubtful.'],
 [r'\unsure{in|on}',r'\over[typed]{o}{i}n','The dotted i is typed over a visible rounded o; the live word is in.'],
 [r'au\over{t}{t}omatically',r'au\over{to}{to}matically','Both the tall t and the following rounded o are pen-retraced over their typed letters.'],
 [r'\hand{(}As a type',r'As a type','The apparent opening parenthesis is the left end of the continuous insertion curve beneath the parenthesized addition, not another textual parenthesis.'],
 [r'\xout{xxx}set',r'\xout{sub}set','The cancelled prefix sub is legible beneath the x strikes.'],
 ['These objects will',r'T\over{h}{h}ese objects will','The h has a separate pen retouch at its ascender.'],
 [r'\inserted{just}',r'\inserted[typed]{just}','Just is typed above the line and linked by a pen hook.'],
 [r'\xout{fixxx}',r'\xout{first}','The cancelled first is readable from its f/i/r and final t.'],
 [r'\xout{whichxwill}',r'\xout{which will}','The old phrase has a space between which and will; x is the cancellation character rather than a live letter.'],
 [r'\inserted{(as seen in C)}',r'\inserted[typed]{(as seen in C)}','The parenthetical addition is typed interlinearly and placed by a pen curve.'],
 [r'N\over{\illegible{1}}{o}w',r'N$\overset{\hand{\smile}}{\underset{\hand{\frown}}{\mathrm o}}$w','The o itself is an ordinary typed letter, with separate small curved pen marks above and below. There is no visible overwritten old word or letter at that position.'],
 ['The saturation\n', 'THe saturation\n','The source visibly has a typed capital H; retain its case rather than normalize it.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3662:['in M','The i is a typed correction over o; the live word is in.'],
 3667:['Contractibility structure.','The heading is singular.'],
 3671:['in the organigram','The source gives the word organigram, not a numbered reference.']
 },'unsure':[[r'\over[typed]{o}{i}n','The dotted i and rounded old o are separately visible.']],
 'illegible':[
 [r'\illegible{1}','The old typed word under the large penned that has scattered rounded contours but no secure complete reading.'],
 [r'\illegible{1}','The handwritten the covers an older typed cluster; no full lower word is established.'],
 ['typed o with curved marks above and below','The letter is plainly o, without an overwritten lower letter. The two separate pen curves are retained as graphics.'],
 [r'\illegible{1}','The short handwritten addition above me is heavily scratched out. Its isolated loops cannot be assembled into a secure word.']
 ],'notes':[
 'The initial replaced span has both machine and pen cancellation; a residual f lacks a separate strike and is retained with doubt. The e of The is pen-retraced and its following old cell is unreadable.',
 'The word resolves to in from typed i over the older rounded o.',
 'The word beneath that remains unreadable. Both t and o of automatically are pen-retraced.',
 'The handwritten the covers old typed lettering which cannot be read securely.',
 'The arrows, inclusion signs, Sigmas and deltas are handwritten. Their typed indices remain plain.',
 'The scribble above me is a genuinely cancelled handwritten addition whose text remains unreadable. Now instead has two separate curved marks around an ordinary typed o.',
 'The lower-left 29 is handwritten. Just and as seen in C are typed interlinear insertions.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_029:embedding','before':'r23 from Hom3 into Hom1','after':'r23 from Hom3 into Hom1','line':21,'decision':'retain author notation','reason':'The first index is visibly 23, though the target is Hom1 and the later Hom3-to-Hom2 map is also r23. The guide explains the evident index inconsistency without applying the witness correction.'},
 {'source_id':'OBS:ps_134-4_029:containment','before':'the latter contains barred C_h','after':'the latter contains barred C_h','line':39,'decision':'retain author notation','reason':'The bar above this C is visible. The following displayed condition C_h subset barred C_h shows the intended unresolved containment question, but the typed prose is retained literally.'}
 ],'evidence':'Both original halves and fourteen enlarged panels inspected. The first overwritten span has separate machine and pen cancellation, with a residual f lacking a distinct strike; this is retained doubtfully rather than erased. The next old phrase is tentatively we get. The live preposition resolves to in from i typed over o. Recall, that and the are penned, with the older words under the last two still unreadable. Both t and o of automatically are pen-retraced. The insertion after the D heading is parenthesized, but its long placing curve is not a second textual parenthesis before As. Just and as seen in C are typed above the line. The sub, first and which will cancellations are readable. Now contains an ordinary typed o bracketed by two small pen curves; no hidden old letter is inferred. The cancelled handwritten addition above me remains unreadable. The initial r23-to-Hom1 index and the later barred C in the containment prose are visibly present authorial notational inconsistencies, preserved for explanation in the guide.'})
p=OUT/'records/MASTER_VARIANTS_134_3_4.json';old=json.loads(p.read_text());ids={v['source_id'] for v in variants};p.write_text(json.dumps([v for v in old if v['source_id'] not in ids]+variants,ensure_ascii=False,indent=2)+'\n')
