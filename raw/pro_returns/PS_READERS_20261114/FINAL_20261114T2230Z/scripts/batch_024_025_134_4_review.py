import sys,re,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT,OUT
variants=[]
key='ps_134-4_024';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'F\!\not{l}(M)',r'\mathrm F\over{l}{l}(M)').replace(r'\subset',r'\hand{\subset}').replace(r'\longrightarrow',r'\hand{\longrightarrow}')
 if new!=line:edits.append(['\n'+line+'\n','\n'+new+'\n','Fl contains a typed l retraced in pen, not a negated l. The inclusion signs and displayed quotient arrow are penned.'])
edits += [
 ['The relevant',r'T\over{H}{h}e relevant','The lowercase h is written in pen over a visible typed H.'],
 ['a) The relation',r'a) \over[typed]{T}{T}he relation','The capital T has a displaced repeated type impression.'],
 [r'\unsure{equivalehce|equivalence}','equivalehce','The tall ascender makes the anomalous letter h visible; preserve that typed source spelling.'],
 [r'\xout{\unsure{in M}}',r'\xout{on M}','The first old letter has a closed rounded o, followed by n and M under the machine strikes.'],
 [r'\inserted{between f and g}',r'\inserted[typed]{between f and g}','The inserted words and variables are typed above the line with a pen placing curve.'],
 [r'\overline{R}_h',r'\overset{\hand{\rule{0.65em}{0.4pt}}}{R}_h','The saturation bar is penned above typed R.'],
 ['between the set of homo-',r'between \over[typed]{t}{t}he set of homo-','The first t has repeated displaced type impressions.'],
 ['considering a homotopy relation in M,',r'considering a homotopy relation in $\underset{\hand{\unsure{\cdot}}}{M}$,','The small dot is below M, not above it. Retain it as a doubtful graphic rather than treating it as established mathematical notation.'],
 [r'\xout{xxx} become',r'\deleted{\xout{\unsure{are}}} become','The old word is plausibly are beneath both machine x strikes and a continuous pen cancellation; retain the uncertainty of its letters.'],
 [r'M_{\hand{h}}',r'M_{\over{\illegible{1}}{h}}','The pen h covers an older typed subscript whose exact letter is obscured.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3557:['R_h subset Fl(M)xFl(M)','The first display has no final comma; its product sign is a typed x.'],
 3558:['have same source','No the precedes same source.'],
 3559:['and same target','No the precedes same target.'],
 3560:['Thus the data','There is no comma after Thus.'],
 3563:['saturated i.e. a homotopy','No commas are supplied around i.e.'],
 3564:['quotient sets of the sets Hom(X,Y)','Both relevant occurrences are plural sets.'],
 3565:['having same objects as M, and','No the occurs before same objects.'],
 3566:['having same objects as M.','The second occurrence likewise lacks the article.']
 },'unsure':[
 ['equivalehce','The taller stem clearly identifies typed h, rather than n.'],
 ['on M','The first old cell has a closed o bowl, not a dotted i.']
 ],'notes':[
 'Every Fl has a slanted pen retracing over typed l; it is encoded as a layered letter rather than mathematical negation.',
 'The source indeed types equivalehce with h. Its one-off master correction is separately documented using equivalence on the same page.',
 'The cancelled words resolve to on M from their surviving rounded o and n/M contours.',
 'The final h is handwritten over an obscured old typed subscript; that lower layer remains unreadable.',
 'The lower-left 24 is handwritten. Between f and g is typed interlinearly; from M is penned.',
 'The small dot near the inline M is below its baseline. Its function and intentionality remain doubtful, so it is retained graphically.',
 'The final inclusion sign is penned, as is the first inclusion sign and the bar above the saturated relation.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_024:equivalence','before':'equivalehce','after':'equivalence','line':17,'decision':'master slip variant','reason':'The isolated h for n is settled by the correctly typed equivalence in the preceding line on the same page.'},
 {'source_id':'OBS:ps_134-4_024:of','before':'or arrows of M','after':'of arrows of M','line':10,'decision':'master slip variant','reason':'The definition is a relation in the set of arrows. The isolated r for f is settled by the many correctly typed of phrases on this page.'}
 ],'evidence':'Both original halves and nine enlarged panels inspected. The anomalous equivalehce is a clear typed h, and the cancelled preposition is on M rather than in M. Between f and g is typed interlinearly. The relevant has pen h over H, the item-a T and later t have repeated typing, and all Fl forms have pen-retraced l. The first and last inclusion signs, the quotient arrow and the saturation bar are penned. A small mark lies below inline M and remains a doubtful graphic. The last old subscript is unreadable under pen h; the cancelled are is tentative beneath both machine and pen strikes. All eight required addition/wording rows were checked against the absence of their proposed added articles, punctuation or singularization.'})
variants += [
 {'key':key,'before':'equivalehce','after':'equivalence','kind':'slip corrected','reason':'One-off h for n; equivalence is correctly typed in the preceding line.','source_id':'OBS:ps_134-4_024:equivalence'},
 {'key':key,'before':'or arrows of M','after':'of arrows of M','kind':'slip corrected','reason':'One-off r for f in the definition of the set of arrows; of is correctly attested on the same page.','source_id':'OBS:ps_134-4_024:of'}]

key='ps_134-4_025';edits=[
 [r'se $\hand{\Sigma}_h$ contains',r'se $\over{\illegible{1}}{\Sigma}_{\hand{h}}$ contains','The third Sigma is penned over an obscured typed placeholder, and its h is itself penned.'],
 [r'\inserted{pure}',r'\inserted[typed]{pure}','Pure is typed above the line and placed by a pen hook.'],
 ['The two prescriptions',r'T\over[typed]{H}{h}e two prescriptions','The h is typed beneath the residual upper bars of an older H.'],
 ['which can\n',r'which \over[typed]{i}{c}\over[typed]{a}{a}n'+'\n','The c is typed over dotted i, and the following a has a repeated type impression.'],
 [r'This implies \inserted{too}',r'This implie\over{s}{s} \inserted[typed]{too}','The final s is pen-retraced. Too is typed interlinearly and its curve places it before that.'],
 [r"\inserted{(and that $f\sim f', g\sim g'$ implies $f\times g\sim f'\times g'$.}",r"\inserted{and that $f\sim f', g\sim g'$ implies $f\times g\sim f'\times g'$.}",'The apparent opening parenthesis is the beginning of a continuous placing curve beneath the whole addition, not independent textual punctuation.'],
 [r'\deleted{and th\unsure{at}}',r'\deleted{and} \unsure{that}','Only and has an independent horizontal pen cancellation. The following th is visible under the placing curve and its ending is obscured; retain the whole proposed that with doubt instead of asserting its deletion.'],
 [r'commute\unsure{s}',r'commutes','Despite right-edge clipping, both the upper and lower curves of the final s are visible.'],
 [r'\mathrm{Fl}(M)',r'\mathrm F\over{l}{l}(M)','The displayed l is penned over a typed l.'],
 ['subset of Fl(M)',r'subset of F\over{l}{l}(M)','The inline l has the same pen retracing.'],
 ['The natural',r'T\unsure{\over[typed]{H}{h}}e natural','The typed h has separate fragments above and below it. Retain doubt about the exact older layer and its order rather than ignore the marks.'],
 [r'\hand{M\to}',r'\hand{M}\over{M}{\to}','The new M is handwritten to the left. The pen arrow runs over a clearly visible older typed M, which must remain in the diplomatic layer.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3583:['our organigram','The manuscript gives the word organigram rather than an explicit numbered cross-reference.'],
 3584:[r'\deleted{\illegible{1}}','The old mark before We\'ll is genuinely pen-cancelled, but its proposed 4A or A-like reading cannot be securely separated.'],
 3591:['commutes to finite products','The final s can be read despite clipping; the witness drops it.']
 },'unsure':[
 [r'\unsure{that}','The th is visible, but the final cells are obscured by the addition. Their cancellation is not independently established.'],
 ['s','The surviving upper and lower arcs identify the final s even at the cut edge.']
 ],'illegible':[
 [r'\illegible{1}','The lattice-like pen cancellation covers the old mark; the suggested 4A cannot be securely read.'],
 [r'\illegible{1}','The first formula scribble remains covered by dense pen hatching.'],
 [r'\illegible{1}','The second scribble has a few surviving letter-like shapes but no secure complete reading.']
 ],'notes':[
 'Homoto and pic, and ca and se, join without inventing an unseen hyphen. The final s in commutes is clipped but legible from its surviving arcs.',
 'Only and has a separate horizontal cancellation. The following that remains doubtful rather than automatically deleted. The handwritten g forms have lower loops and are retained as g. The initial parenthesis-like curve is part of the insertion hook.',
 'Both scribbles in the localisation display remain unreadable. The typed M beneath the new arrow is separately preserved.',
 'Both Fl occurrences have a typed l retraced in pen.',
 'The lower-left 25 is handwritten. Pure and too are typed interlinear additions; the third Sigma overwrites an old typed placeholder and has a penned h.',
 'The mark before We\'ll is heavily pen-cancelled. No secure 4A reading is supplied.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_025:two','before':'twp  among','after':'two  among','line':19,'decision':'master slip variant','reason':'The scan really has a descender on p. This one-off wrong keystroke is corrected using the word two at the beginning of the same sentence.'}
 ],'evidence':'Both original halves and eleven enlarged panels inspected. The third Sigma has a covered typed placeholder and a pen h. Pure and too are typed additions. Twp really has a p descender and remains literal in the checked source. The mark before We\'ll stays unreadable. The c of can is typed over dotted i, and a is retyped. The final s in implies is pen-retraced. The long addition begins with a continuous placing curve, not an independent textual parenthesis; and is clearly struck, while the following that retains doubt about its ending and cancellation status. The final s of commutes is legible at the clipped edge. Both localisation scribbles remain unreadable, but the typed M under the new pen arrow is visible and restored to the layered encoding.'})
variants.append({'key':key,'before':'twp  among','after':'two  among','kind':'slip corrected','reason':'One-off p for o, with two correctly typed at the beginning of the same sentence.','source_id':'OBS:ps_134-4_025:two'})
p=OUT/'records/MASTER_VARIANTS_134_3_4.json';old=json.loads(p.read_text());ids={v['source_id'] for v in variants};p.write_text(json.dumps([v for v in old if v['source_id'] not in ids]+variants,ensure_ascii=False,indent=2)+'\n')
