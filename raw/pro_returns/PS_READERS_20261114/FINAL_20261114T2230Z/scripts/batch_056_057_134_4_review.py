import sys,json,re
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT
key='ps_134-4_056';edits=[
 ['58.  Some',r'5\over{\unsure{7}}{8}.  Some','The new 8 is penned over a dark older digit; 7 is plausible but not fully recoverable.'],
 [r'\overline{\hand{\Gamma}}(X) \overset{\text{\unsure{def}}}{=}',r"\overline{\over{\mathrm I}{\Gamma}}(X) \overset{\text{\unsure{\illegible{1}d\over{e}{\'e}f}}}{=}",'The Gamma is constructed from a typed capital I with an added pen top-right bar. The raised label contains an extra marked cell before typed def and a pen mark above e; the first cell and its cancellation status cannot be recovered securely. Keep the whole label doubtful.'],
 [r'\margin{NB d) \unsure{a conséquence de} f)!}',r'\margin{\uline{NB} d) \unsure{a|=} conséquence de f)!}','NB is underlined, and conséquence de resolves in the rotated view. The small mark after d) remains uncertain.'],
 ['Indeed,  let',r'I\over[typed]{n}{n}deed,  let','The n has a second regular typed impression displaced below it.'],
 ['0-conne%\n% NOTE: the right edge of the scan cuts off the end of the line above\nted.',r'0-conne\unsure{c}%'+ '\nted.','The line reaches the clipped edge after conne; the joining c is not visible and remains doubtful. Keep the physical continuation joined.'],
 [r'By assumption\inserted{f)}',r'By assumption \inserted{f)}','Separate the inserted condition label from the preceding word.'],
 [r'\xout{xxy}',r'\xout{\unsure{sa}y}','The lower final y is visible; the first two cancelled cells are compatible with sa but remain uncertain.'],
 [r'\xout{$(s_i,t_i)$ with i \unsure{=} 1,2 Now these sections are homotopic, because}',r'\xout{$(s_{\unsure{i|1}},t_{\unsure{i|1}})$ with i \unsure{=} \unsure{1|0},2\unsure{.} Now these sections are homotopic, because}','The cancelled line is otherwise readable, but its old subscripts, relation, first number and punctuation after 2 are obscured by the regular x row; do not infer them from the rewritten line.'],
 ['The condition f)',r'T\over[typed]{h}{h}e condition f)','The h has a displaced second regular typed impression.'],
 [r'\xout{xxx} the final topos',r'\xout{\illegible{1}} the final topos','The three x impressions are cancellations, not a recoverable old word.'],
 [r'\overline{\hand{\Gamma}}(X) \overset{\hand{\text{def}}}{=}',r'\overline{\over{\mathrm I}{\Gamma}}(X) \overset{\hand{\text{def}}}{=}','The second Gamma likewise has a typed I underneath the hand-drawn upper bar. Its def is independently clear handwriting.']
]
save_review({'key':key,'edits':edits,'diffs':{
 4154:['object X','The typed variable is clearly X, not K.'],
 4155:['Every 0-connected object of M','Object is singular on the page.'],
 4157:[r'NB d) \unsure{a|=} conséquence de f)!','The pencil margin note is present and its consequence-de-f wording is readable; retain the small ambiguous mark.'],
 4158:['Firstly, it is','The source has the full adverb Firstly.'],
 4164:['strictly totally 0-connected','Both defining and repeated occurrences say connected, not disconnected.'],
 4167:['A doubtful raised label including an extra marked cell before def','The scan has additional raised material, unlike the witness omission; the extra first cell cannot safely be removed.']
 },'unsure':[
 [r'\unsure{\illegible{1}d\over{e}{\'e}f}','An extra rounded cell precedes def. Pen marks obscure its identity and status; independent inspection agrees to retain the entire label doubt.'],
 [r'\unsure{a|=} conséquence de','The long words conséquence de are readable; the small sign after d) remains uncertain.'],
 [r'\unsure{=}','The regular strike obscures the relation after i; equality remains only a candidate.']
 ],'notes':[
 'The 8 is a pen replacement over an older digit, tentatively 7, whose full shape remains obscured.',
 'Indeed has repeated typed n impressions and The repeated typed h impressions, displaced downward.',
 'The rotated pencil note reads underlined NB, d), a small uncertain sign, conséquence de f)!. The wording is preserved without converting its assertion into an editorial theorem.',
 'The long cancelled line is readable apart from the old subscripts, relation, first number and punctuation after 2. The short old word before it has a clear y and tentative sa.',
 'Both Gamma signs contain a regular typed I and a pen upper bar. The first raised label has an additional obscured rounded cell before def; the pen mark above e and the first-cell status remain doubtful. The second handwritten def is clear.',
 'The pencil archive folio 56 is visible at lower left.'
 ],'evidence':'Both original halves, nine detail panels, a rotated margin crop, and enlarged raised-label and cancelled-line crops inspected. The date remains typed 5.4. The heading 8 is penned over a doubtful older digit. Both Gamma signs are made from typed capital I with a pen top-right bar, while the first raised definition label includes an extra marked cell that cannot safely be deleted or named; this doubt is independently confirmed. The margin note has underlined NB and readable conséquence de f), with its small separator uncertain. The old cancelled line is preserved with scoped uncertainty in the subscripts, relation, first numeral and punctuation. A clipped c in connected is made doubtful, and the continuation is joined. The sheaf-category replacement is typed above the line, with both older formulations cancelled. The extra old word before the final topos remains illegible. The source X, singular object, Firstly and connected are secure against the witness variants.'})

key='ps_134-4_057';edits=[
 ['is evident indeed',r'is \over{ev}{ev}ident indeed','The initial e and v have dark irregular pen retracings over their typed letters.'],
 ['can be checked using',r'can be check\unsure{\over[typed]{u}{e}}d using','The second e has a raised u-like regular impression over it; preserve the uncertain typed layering.'],
 [r'properties \xout{xx}',r'properties \xout{\illegible{1}}','The x row hides the old short word; the lower letters cannot be read securely.'],
 [r'\xout{littlex,}',r'\xout{little,}','Little and its following comma are recoverable; the extra x is the cancellation impression, not an old textual x.'],
 ['to the ``meaning',r'to t\over{h}{h}e ``meaning','The h is retraced with a tall irregular pen stroke.'],
 [r'been start\xout{t}-%',r'been star\xout{t}-%','The scan has only one cancelled t after star, not a live t plus another cancelled t. Removing the duplicated transcription cell restores the visible star/ting continuation.'],
 [r'class\inserted{es}',r'class\inserted[typed]{es}','The raised es has regular typewriter forms, with only the placing curve handwritten.'],
 [r'\inserted{An} elemen-',r'\inserted[typed]{An} \unsure{\over[typed]{a}{e}}lemen-','An is typed above the line. The first e of elementary has a dense older a-like impression and remains doubtful in its layering.'],
 ['components of the category',r'componen\unsure{\over[typed]{t}{t}}s of the category','The t has displaced repeated impressions; the exact lower layer remains uncertain.'],
 ['generated by the relation',r'generat\over[typed]{\unsure{a|e}}{e}d by the relation','The second-to-last e has a dark older rounded impression, possibly a or repeated e.'],
 ['the usual\none of isomorphy',r'the \unsure{\over[typed]{us}{us}}ual'+'\n'+r'one of isomorp\over[typed]{y}{h}y','The first us of usual has dense regular overlaps, whose order is uncertain. The h of isomorphy overlies a typed y with its descender visible.'],
 ['into category theory',r'in\over{to}{to} category theory','The t and o are pen-retraced over type; the tall stroke belongs to the t, not to a separate boundary mark.']
]
save_review({'key':key,'edits':edits,'diffs':{
 4173:['we need to care only','The source r in care is clear; the witness case is incorrect.'],
 4182:['to another Y','Another is fully typed; no intervening category is present.'],
 4186:['Thus homotopy classes','There is no comma after Thus.'],
 4187:['Topological motivations alone','The plural s is present at the beginning of the continued line.']
 },'illegible':[[r'\illegible{1}','The handwritten precise covers the lower typed word; its complete earlier reading remains unrecoverable.']],
 'notes':[
 'The placing curve for the typed parenthesis geometric bends around the top of the and terminates at its right; no independent cancellation through the is visible.',
 'Evident and the have pen retracings. Checked, components, elementary, generated, usual and isomorphy contain typed overlaps, with uncertainty retained where older letters or order cannot be separated. The old y below the h of isomorphy is clear.',
 'The lower word under precise remains illegible. The live handwritten precise is clear.',
 'The tall mark belongs to the retraced t of into, followed by a small retraced o; it is not an extra textual separator.',
 'A functor which is a is typed above the line with a continuous placing curve leading before weak. An and es are also typed interlinear additions.',
 'The pencil folio 57 is visible at lower left.'
 ],'extra_records':[{'source_id':'OBS:ps_134-4_057:felationship','before':'felationship','after':'relationship','decision':'isolated typing slip corrected only in corrected forms','reason':'The initial letter is plainly typed f. Relationship is correctly typed in reviewed 134-4/023, 026 and 050; this isolated f-for-r slip is recorded as an explicit variant.'}],
 'evidence':'Both original halves and sixteen enlarged detail panels inspected. The first line plainly types felationship, kept diplomatically and corrected separately as an isolated typing slip. The geometric insertion leaves the live. Evident has pen ev retracings, checked a doubtful raised u/e typed layer, and the meaning a pen h retracing. The old short word after properties and the lower word under precise remain unreadable. Little and its comma resolve under cancellation. There is a single cancelled t after star; the initial transcription duplicated it, which incorrectly changed the joined word. Both es and An are typed interlinear additions. Elementary, components, generated and usual retain scoped overlap doubts, while the old y beneath the live h of isomorphy is distinct. Into has pen to retracings. The live care, another, plural motivations and absence of a comma after Thus are secure.'})
v={'key':key,'before':'felationship','after':'relationship','kind':'slip corrected','reason':'Isolated typed f for r; correctly typed relationship occurs in reviewed 134-4/023, 026 and 050.','source_id':'OBS:ps_134-4_057:felationship'}
p=OUT/'records/MASTER_VARIANTS_134_3_4.json';old=json.loads(p.read_text());old=[x for x in old if x['source_id']!=v['source_id']];old.append(v);p.write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
# Mechanical balance check after reconstruction; this does not substitute for visual review.
for k in ['ps_134-4_056','ps_134-4_057']:
 s=(OUT/'checked_pages'/f'{k}.tex').read_text();s=re.sub(r'(?<!\\)%[^\n]*','',s);n=0
 for m in re.finditer(r'(?<!\\)[{}]',s):
  n+=1 if m.group()=='{' else -1
  assert n>=0,(k,m.start())
 assert n==0,(k,n)
