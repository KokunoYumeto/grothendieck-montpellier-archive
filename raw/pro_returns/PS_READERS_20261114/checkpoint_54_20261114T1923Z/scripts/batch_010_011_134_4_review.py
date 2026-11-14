import sys,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT,OUT
variants=[]
key='ps_134-4_010';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace('A_{/C}',r'A_{\hand{/}C}').replace('A_{//C}',r'A_{\hand{//}C}').replace(r'\varnothing_M',r'\hand{\varnothing}_M')
 if new!=line:edits.append([line,new,'The category slashes and empty-set symbol are handwritten.'])
edits += [
 [r'\unsure{for the}','for the','The letters f-o-r, the space, and t-h-e are legible beneath the typed x strikes.'],
 ['THe\nmost',r'T\over[typed]{H}{h}e'+'\nmost','The capital H and lowercase h are overtyped in one cell.'],
 ['contractible categories',r'contractib\over[typed]{e}{l}\over[typed]{l}{e} categories','The final le is typed over the transposed el; each older bowl or ascender is visible.'],
 [r'\xout{xx}',r'\xout{\unsure{is}}','The two x marks cancel older letter impressions, plausibly is; the old reading remains doubtful rather than treating the cancelling x marks as text.'],
 [r'\illegible{1}','catego','The six cancelled letters c-a-t-e-g-o can be read beneath the machine x row.'],
 [r'\xout{condition}assumption',r'\xout{condition} assumption','The live assumption is a separate replacement word.'],
 ['reduction is from',r'reduction is \over[typed]{f}{f}\over[typed]{\unsure{o}}{r}om','The f is retyped; the r overlaps an older rounded impression, tentatively o.'],
 [r'(\unsure{Cat})',r'(\unsure{\over[typed]{V}{C}}at)','The a and t are clear. The first cell contains a V-like older impression and a rounded C-like correction; that layered reading remains doubtful.'],
 [r'interval\deleted{\unsure{,}}\inserted',r'interval \inserted','The supposed cancelled comma is the downward end of the continuous insertion curve for I=. There is no independently visible punctuation to delete. Independent review agrees.'],
 [r'\hand{$e$}',r'\over{e}{e}','The final-object e is penned over a recognizable typed e.'],
 ['and th%','and the%','The clipped right edge still shows the rounded e after th.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3291:['aspheric morphism of topoi...).','The word ends oi and the closing parenthesis is followed by a separate period.'],
 3294:[r"the $i(a)$\hand{'}s have",'The apostrophe is visibly added in pen before the small s.'],
 3296:['asphericity criteri-on','The source has the words asphericity criterion split across the line, not an external reference label.'],
 3300:[r'\hand{\unsure{Mer.}}','The initial zigzag and following loop support tentative Mer., but the overlapping strokes do not settle it. Independent image review agrees; no weekday inference is used.','retain doubt'],
 3305:['(loc. cit.)','The first consonant is c, not s.'],
 3307:['be a strict initial element','The article a is plainly typed.'],
 3309:["I'll not as-sume it",'The live not is explicit. Its omission would reverse the author\'s decision to defer strictness of the initial object.'],
 3312:[r'\margin{1°}','The lower-left mark is a handwritten 1 with a small raised loop.']
 },'unsure':[
 ['for the','The cancelled words are legible under the machine x row.'],
 [r'\unsure{\over[typed]{V}{C}}at','Only the first cell remains doubtful; the a and t are unambiguous.'],
 [r'\unsure{Mer.}','The initial zigzag and e-like loop support this tentative reading, but the crowded pen strokes preclude resolution.'],
 ['Insertion hook, no separate comma','The stroke is continuous with the curve placing I=; no distinct old comma is visible.']
 ],'illegible':[['catego','All six old letters are distinguishable under the x row.']],
 'notes':[
 'For the is recoverable beneath the typed strikes.',
 'Contractible ends in typed le over el; the old ascender and bowl distinguish both cells.',
 'The cancelled fragment before objects reads catego.',
 'The final s of elements is handwritten, as is the apostrophe attached to i(a).',
 'The first cell of Cat remains a doubtful V/C type overlap; the rest of the name is clear.',
 'Mer. remains a tentative image reading, independently confirmed as appropriately doubtful; no calendar-based substitution is made.',
 'The long curve over interval and its downward end form the insertion hook. There is no secure separate cancelled comma.',
 'No hyphen is visible after contractibi. At the lower right edge the e of the is partially visible and restored; no further text is supplied.'
 ],'extra_records':[{'source_id':'OBS:ps_134-4_010:too','before':'forced too.','after':'forced to.','line':47,'decision':'master slip variant','reason':'The extra o is isolated in this infinitive construction; ordinary to occurs repeatedly on this leaf. Diplomatic preserves too.'}],
 'evidence':'Both original halves and ten enlarged detail panels inspected. The cancelled for the and catego are recovered. Contractible ends in a typed el-to-le correction. The two cancelled cells beneath are remain tentatively is. The first Cat letter has an unresolved V/C-like overlap. The day abbreviation remains doubtful Mer. after an independent visual consultation. The supposed deleted comma after interval is instead the continuous insertion hook for I= and is removed as a misidentified mark. The final-object e is penned over typed e, the initial-object symbol is penned, and the clipped e of the is visible. The decisive not before assume remains live. The handwritten binary-products addition is fully retained.'})
variants.append({'key':key,'before':'forced too.','after':'forced to.','kind':'slip corrected','reason':'The isolated extra o in the infinitive is settled by context and repeated to on this leaf.','source_id':'OBS:ps_134-4_010:too'})

key='ps_134-4_011';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line
 if r'\ar[' in new:
  new=new.replace(r'\ar[',r'\ar[color=blue,')
 if 'X\\rightrightarrows Y' in new:new=new.replace(r'\rightrightarrows',r'\hand{\rightrightarrows}')
 if 'M\\longrightarrow W' in new:new=new.replace(r'\longrightarrow',r'\hand{\longrightarrow}')
 if r'G}\rightarrow' in new:new=new.replace(r'\rightarrow',r'\hand{\rightarrow}')
 if r'$f\rightarrow g$' in new:new=new.replace(r'$f\rightarrow g$',r'$f\hand{\rightarrow} g$')
 if new!=line:edits.append([line,new,'The arrows are drawn in pen. In the diagram the objects remain typed, while arrows and labels are handwritten.'])
edits += [
 [r'\diagram{\begin{tikzcd}',r'% Hand-drawn arrows are marked blue; typed objects remain plain.'+'\n'+r'\diagram{\begin{tikzcd}','Record the mixed provenance of the diagram explicitly.'],
 ['One key notion',r'O\over[typed]{\unsure{N}}{n}e key notion','Small displaced type-like impressions above and below n may be an older capital N; their identity remains doubtful.'],
 [r'F\mathrm{x}I\xrightarrow{h}G',r'F\mathrm{x}I\overset{h}{\hand{\longrightarrow}}G','The inline arrow is handwritten but its raised h is typed. Preserve F and G, not the witness X and Y.'],
 [r'\mathrm{id}_F\times\delta_0',r'\mathrm{id}_F\over{\unsure{\times}}{\times}\delta_0','The first product mark has a thick pen overwrite; the older sign cannot be read securely.'],
 [r'\over{F}{\unsure{F}}',r'\over{F}{F}','The right diagram node has a clearly penned F over a typed F.'],
 [r'\xout{ix}',r'\deleted{\unsure{i}}\xout{\illegible{1}}','The first extra cell after symmetry is pen-blotted and tentatively i; the next bears a machine x but its older letter is unreadable.'],
 [r'\inserted[typed]{an isomorphism,  and g constant  -  then  F} \xout{\unsure{W}-aspheric, then so is g - and conversely} $\hand{\longrightarrow}$ e  and',r'\xout{\unsure{W}-aspheric, then so is g - and conversely} \inserted[typed]{an isomorphism,  and g constant  -  then  F $\hand{\longrightarrow}$ e  and}','The replacement continues at the raised level through the penned arrow and typed e and and; include the whole raised span in the insertion. The older clause remains machine-cancelled.'],
 [r'e^{\hand{\ast}}',r'e^{\hand{\unsure{\ast}}}','The raised dark mark after e is not a securely readable clean star; retain the star interpretation with doubt.'],
 ['namely with',r'namely w\over[typed]{i}{i}\over[typed]{t}{t}h','The i and t have repeated, slightly offset type impressions.'],
 [r'condition\inserted{b)}',r'condition \inserted[typed]{b)}','The interlinear b) is typed, with regular serifed letters and curved parenthesis.'],
 [r'e_0\wedge e_1 = \emptyset',r'e_0\hand{\cap} e_1 = \hand{\varnothing}','The intersection sign is a rounded pen cap, and the empty-set sign is also penned.'],
 ['is atransiti\nve',r'is a\hand{\ensuremath{\backslash}}transiti%'+'\nve','A long oblique pen separator stands between a and t. The line division inside transitive has no hyphen, so the TeX newline must not create an internal word space.'],
 [r've\hand{,}and',r've\hand{,} and','The added comma is followed by the separate word and.'],
 [r'\over{\unsure{g}}{j}ust',r'\over{g}{j}ust','The old typed g loop and descender remain visible beneath the penned j.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3313:[r'F\mathrm{x}I\overset{h}{\hand{\longrightarrow}}G','The inline source uses F and G and a typed x; h is typed and the arrow penned.'],
 3314:['F, FxI, F, G; id_F x delta_0 and id_F x delta_1','All four source objects are typed with F/G. The right F is retraced in pen, and the arrow labels are handwritten.'],
 3317:['is the canonical functor.','A typed full stop ends the sentence.'],
 3319:[r'F\to e and \overset{\hand{\unsure{\hat{\ast}}}}{G}\to e^{\hand{\unsure{\ast}}}','The source uses F and G. Both extra raised marks remain uncertain; neither is silently removed or resolved.'],
 3321:[r'(\underline{I},\delta_0,\delta_1)','The tuple has no added equality or preceding I= on this line.'],
 3326:[r'condition \inserted[typed]{b)} e_0\hand{\cap}e_1=\hand{\varnothing}','The interlinear b) is typed. The intersection and empty-set signs are penned, with a rounded cap rather than angular wedge.','correct provenance and glyph'],
 3327:['g ...). For','The full stop after the closing parenthesis is visible.']
 },'unsure':[
 ['F','The pen correction clearly forms F over typed F.'],
 [r'\unsure{W}','The first old letter beneath the typed x row remains crowded; W is plausible but not fully secure.'],
 [r'\unsure{\hat{\ast}}','The mark above G has an upper angular stroke and lower crossed impressions, with no securely distinguishable letter or correction order.'],
 ['g','The old type g is readable below the pen j.']
 ],'notes':[
 'The replacement an isomorphism, and g constant - then F is typed above the old clause. The following arrow is penned, while e and and are typed at the raised level. The old clause is machine-cancelled, not pen-deleted.',
 'The mark over G remains doubtful, and the separate mark after e is now also explicitly doubtful rather than a secure star.',
 'The right node is pen F over typed F. The first product mark in id_F x delta_0 has a dense overstroke with uncertain older sign. All diagram arrows and labels are handwritten.',
 'After symmetry the first old cell is pen-blotted and tentatively i; the next is machine-cancelled with unreadable old letter. The g beneath just is recoverable.',
 'The lower-left 11 and top folio 99 are handwritten.',
 'The small displaced marks around One are retained as a doubtful older N beneath the live typed n. A separate enlarged panel also establishes the pen word-separation stroke in atransitive.'
 ],'extra_records':[{'source_id':'OBS:ps_134-4_011:separator','before':r'is a\hand{\ensuremath{\backslash}}transiti%'+'\nve','after':'is a transiti%\nve','line':45,'decision':'authorial word separation for master','reason':'The pen stroke explicitly separates the article a from transitive. Diplomatic retains the literal run-together typing and separator.'}],
 'evidence':'Both original halves, eight enlarged panels and a separate atransitive enlargement inspected. The source F/G notation is secure, including the penned correction of the right F. The inline h is typed over a pen arrow. The first diagram product mark has a doubtful older layer. Item c replaces a machine-cancelled clause with raised typing; its two extra raised marks remain unresolved. The small displaced marks around One and the marks after symmetry remain doubtful. The interlinear b) is typed, the intersection symbol is a rounded pen cap, and the g-to-j correction is legible. A long pen stroke explicitly separates a from transitive; the master variant applies that instruction, while the mechanical newline treatment keeps transitive one word.'})
variants.append({'key':key,'before':r'is a\hand{\ensuremath{\backslash}}transiti%'+'\nve','after':'is a transiti%\nve','kind':'authorial word separation','reason':'The pen stroke separates a from transitive.','source_id':'OBS:ps_134-4_011:separator'})
p=OUT/'records/MASTER_VARIANTS_134_3_4.json';old=json.loads(p.read_text());ids={v['source_id'] for v in variants};p.write_text(json.dumps([v for v in old if v['source_id'] not in ids]+variants,ensure_ascii=False,indent=2)+'\n')
