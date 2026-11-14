import sys,re,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT,OUT

key='ps_134-4_022'
save_review({'key':key,'edits':[
 ['namely upon',r'namely \over[typed]{\unsure{w}}{u}\over{p}{p}on','The u overlaps an older w-like typed impression, and p is retraced in pen.'],
 [r'F\!\!/(M)',r'\mathrm F\over{l}{l}(M)','The slanted stroke is a pen retracing of typed l, not a slash after F.'],
 ['a rather loose one,',r'a rather loose one\hand{,}','The final comma is a dense pen mark with a low pointed tail.'],
 [r'interval\xout{x}',r'interval\xout{\illegible{1}}','The cancelled final cell cannot be read beneath its x impression.'],
 [r'\xout{thx}',r'\xout{the}','The underlying t, h and rounded e remain readable.'],
 [r'\unsure{homotopy}',r'homo\over[typed]{y}{t}opy','The old y descends beneath the regular typed t; the full live word is homotopy.'],
 [r'$\delta_o,\delta_1$',r'$\hand{\delta}_o,\hand{\delta}_1$','Both deltas are penned, while the endpoint indices are typed.'],
 [r'\xout{\unsure{$\delta$IxI}}'+'\n'+r'\xout{\unsure{$\delta$IxI}}',r'\xout{\unsure{of I|$\delta$IxI}}'+'\n'+r'\xout{\unsure{of I|$\delta$IxI}}','Both cancelled rows contain regular type impressions. The rounded first cell and tall following cell allow of I as an alternative, but the overlapping strikes do not settle either reading.'],
 [r'\xout{canxbexjoinedxxby}',r'\xout{can be"joined" by}','Can be joined by is legible, and quotation marks visibly surround joined.'],
 [r'\uline{intrin}'+'\n'+r'-\uline{sic',r'\uline{intrin}%'+ '\n'+r'-\uline{sic','Suppress only the spurious TeX word space at this physical line split; preserve the printed hyphen.'],
 [r'\hand{t}he choice',r'\over{t}{t}he choice','The pen t retraces a typed t rather than filling an empty cell.'],
 [r'\over{i}{(}in',r'\over{i}{(}\over[typed]{i}{i}n','The parenthesis covers an old i, while the following i has its own displaced type impression.'],
 [r'\inserted{in} the nicest',r'\inserted[typed]{in} \over{t}{t}\over{h}{h}e nicest','In is typed interlinearly. The following t and h are separately retraced in pen.'],
 ['weak equivalen\n-ce', 'weak equivalen%\n-ce','Remove the extra TeX word space across the physical split, retaining its printed hyphen.'],
 [r'\inserted{W}',r'\inserted[typed]{W}','W is a small typed interlinear capital, with a pen placing stroke.'],
 [r'contractib\hand{le} \deleted{elements}',r'contractib\over{l}{l}\over{e}{e} \xout{elements}','The final l and e are pen retracings over typed letters. Elements is cancelled by a regular machine x row.'],
 [r'Th\hand{u}s',r'Th\over{u}{u}s','The pen u is written over a recognizable typed u.'],
 [r'b\hand{e}t-',r'b\over[typed]{f}{e}t-','The live typed e overlies an older f, whose raised stem and crossbar remain visible.'],
 ['ween the underlying',r'\over{w}{w}\over{e}{e}\over{e}{e}n the underlying','The w and both e letters are retraced in pen over the typed word.'],
 [r'autom\hand{at}i-',r'autom\over{a}{a}\over{t}{t}i-','The a and t are pen retracings over typed letters.'],
 ['the modeli\n-zers','the modeli%\n-zers','Remove the added TeX word space at the physical split without deleting the source hyphen.'],
 [r'get\xout{x}',r'get\xout{\unsure{t}}','The final cancelled cell has a t-like upper stroke but remains partly obscured.'],
 [r'A\^{}',r'$A^{\hand{\wedge}}$','The presheaf caret is penned above A; replace the empty accent command with its actual superscript.']
 ],'diffs':{
 3519:['the way it is handled','The word is way, not the witness was.'],
 3524:['Fl(M) being','There is no comma between the formula and being.'],
 3528:['essentially the points','No that precedes the typed inserted phrase. The separate lower pen stroke crosses the old they.'],
 3529:[r'\delta_o,\delta_1','The first index is the typed round letter o; preserve it.'],
 3531:['two days ago','The plural s is visible.']
 },'unsure':[
 [r'homo\over[typed]{y}{t}opy','The old y descender and the live typed t are distinguishable; the word is recoverable.'],
 [r'\unsure{of I|$\delta$IxI}','The first cancelled row remains unresolved. Its regular type shapes allow a word reading, but the layered strikes prevent certainty.'],
 [r'\unsure{of I|$\delta$IxI}','The second repeated row has the same unresolved structure; repetition does not settle its wording.']
 ],'notes':[
 'Upon is pen writing over typed on, whose lower remnants remain visible; it is not a separate interlinear insertion.',
 'Being is penned over the visible older is. The final comma after one is also penned; no comma occurs after Fl(M).',
 'Both short cancelled rows remain doubtful. The longer cancelled phrase reads can be"joined" by, with its quotation marks preserved.',
 'Homotopy has typed t over y; the descended older stroke resolves the initial whole-word doubt.',
 'The opening parenthesis covers typed i, and the next i is independently repeated in typing.',
 'The corresponding is a pen insertion after the still-live of. Its placing curve does not strike of.',
 'The lower-left 22 is handwritten. In and W are typed insertions; the t/h, l/e, u, w/e/e and a/t pen retracings are distinguished from replaced or newly supplied letters.'
 ],'evidence':'Both original halves and sixteen enlarged panels inspected. Upon and being overwrite on and is. The next upon has a doubtful older type layer under u and pen p. Fl contains a pen-retraced l. The final comma after one is penned. Homotopy resolves to typed t over y; the two short cancelled rows remain doubtful with an alternative word reading, while the longer quoted joined phrase is recovered. The old they has a lower pen cancellation independent of the insertion curve. The inserted in and W are typed. Contractible le, Thus u, ween and automatically at are pen retracings; elements is machine-cancelled. Between has typed e over f. The corresponding leaves of live. Three mid-word physical line splits receive percent continuation only, preserving their literal hyphens.'})

key='ps_134-4_023';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=re.sub(r'\\hand\{\$([^$]+)\$\}',lambda m:r'\hand{\ensuremath{'+m[1]+'}}',line)
 new=new.replace(r'\emptyset_M',r'\hand{\varnothing}_M')
 if r'\ar[' in new:new=new.replace(r'\ar[',r'\ar[color=blue,').replace(r', "\hand{}"','')
 if r'\mathrm{Fl}(M)' in new:new=new.replace(r'\mathrm{Fl}(M)',r'\mathrm F\over{l}{l}(M)')
 if new!=line:edits.append(['\n'+line+'\n','\n'+new+'\n','The diagram arrows and slanted l retracings are handwritten while the objects remain typed. The initial-object circle is penned; nested math delimiters are repaired.'])
edits += [
 ['four basic homotopy notions and',r'four basic homotopy \over[typed]{n}{n}\over[typed]{o}{o}tions and','The initial n and o have displaced repeated type impressions.'],
 ['for the time being any',r'for the t\over[typed]{\unsure{u}}{i}me being any','The i has an older rounded lower type impression, possibly u; its identity remains doubtful.'],
 [r'T\hand{h}e strongest',r'T\unsure{\over[typed]{h}{h}}e strongest','The typed h has a small lower h-like repetition. Its provenance is not secure, so the layered representation remains doubtful rather than asserting new handwriting.'],
 [r'T\hand{h}e most',r'T\unsure{\over[typed]{h}{h}}e most','The second The shows the same lower h-like repetition; its provenance remains doubtful.'],
 [r'M\^{}',r'$M^{\hand{\wedge}}$','The first presheaf mark is a pen caret above M; repair the empty text accent command.'],
 [r'into M\^{}.',r'into $M^{\hand{\wedge}}$.','The second presheaf mark is likewise a penned superscript caret.'],
 [r'technic\hand{\ensuremath{\frown}}al',r'technic\hand{\ensuremath{\smile}}al','The joining mark is a low cup-shaped pen curve, not an upper arch.'],
 ['final objects of',r'final obje\over[typed]{\unsure{f}}{c}ts of','The c has an older tall, f-like typed impression that remains only tentative.'],
 ['I definitely',r'I defini\over[typed]{\unsure{j}}{t}ely','The t has a descended older j-like type stroke; preserve doubt about the older letter.'],
 ['(namely the endpoints',r'(na\over[typed]{m}{m}ely the endpoints','The m has displaced repeated typed stems.'],
 ["We'll denote",r"W\over{e}{e}'ll denote",'The e is pen-retraced over the typed e.'],
 [r'\uline{Int}(M)',r'\uline{I\over[typed]{N}{n}t}(M)','The n in the underlined category name is typed over a capital N.'],
 ["Now here's",r"No\over{w}{w} here's",'The w is written in pen over a visible typewriter w.'],
 [r'\margin{\unsure{$\llcorner$}}',r'\margin{\diagram{\begin{tikzpicture}[x=1em,y=1em]\draw[gray] (0,1.5)--(.05,.4)--(3,.55);\draw[gray] (0,-1)--(-.05,.1)--(3,.3);\end{tikzpicture}}}','Two distinct pencil corner strokes bracket the transition to the diagram; reconstruct both actual shapes.'],
 [r'\begin{tikzcd}[arrows=Rightarrow', '% Hand-drawn arrows are marked blue; typed objects remain plain.\n'+r'\begin{tikzcd}[arrows=Rightarrow','Record the shared color convention for the scan-confirmed handwritten arrows.'],
 [r'\margin{*}',r'\margin{\diagram{\begin{tikzpicture}[x=1em,y=1em]\node at (0,0) {$\ast$};\draw[line width=.6pt](-.2,-1.5)--(.2,-1.7);\end{tikzpicture}}}','The right margin has an asterisk-like pen mark and a separate lower slanted dash; preserve both graphics.']
]
# The repeated M accent needs an occurrence-specific first replacement.
for edit in edits:
 if edit[0]==r'M\^{}':edit[0]=r'introduce M\^{}';edit[1]=r'introduce $M^{\hand{\wedge}}$'
save_review({'key':key,'edits':edits,'diffs':{
 3539:['51. in the left margin','The manuscript has the handwritten section number but no descriptive section title.'],
 3543:['timely here to introduce','The to is present.'],
 3546:['dotted arrows with handwritten asterisk','The asterisk after arrows is present and echoed by the right-margin star-like mark.'],
 3549:['an interval in M','The indefinite article is an, not the witness in.'],
 3553:['2) homotopisms','The top-right diagram label has plural homotopisms.'],
 3556:['Two pencil corner strokes','The left margin contains two distinct bracket-like strokes, not a securely readable mathematical corner symbol.'],
 3548:['relationsships','The extra s is visibly typed. It is retained in the checked diplomatic source; the master receives a separately documented one-off slip correction.']
 },'unsure':[
 [r'\unsure{M}','The old second subscript is crossed by dense pen strokes; M remains tentative.'],
 ['Two pencil bracket strokes','Both long horizontals and their separate vertical ends are visible; they are graphical delimiters rather than uncertain text.']
 ],'notes':[
 'The noted repeated type impressions are recorded individually. The older cells in time, objects and definitely remain doubtful; the category-name n is typed over N. We\'ll and Now instead have pen retracing.',
 'Both The occurrences have a small h-like form below typed h. Their provenance remains doubtful and is encoded as such rather than confidently assigned to pen.',
 'The second e subscript is genuinely crossed out; the older M reading remains doubtful. The first M is a separate pen addition.',
 'Two pencil brackets precede the diagram. The right margin contains a star-like mark and a lower slanted dash, both reconstructed.',
 'The lower-left 23 is handwritten. All six diagram arrows, labels 1/2/3, membership signs and Sigma are penned; typed node text and variables remain plain.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_023:join','before':r'technic\hand{\ensuremath{\smile}}al','after':'technical','line':23,'decision':'master author join applied','reason':'The low pen joining curve explicitly closes the gap inside technical.'},
 {'source_id':'OBS:ps_134-4_023:relationships','before':'relationsships','after':'relationships','line':27,'decision':'master slip variant','reason':'The extra s is a one-off typing repetition; relationships is correctly attested on the already reviewed ps_134-3_036.'}
 ],'evidence':'Both original halves, thirteen enlarged panels and a separate relationships enlargement inspected. The source does type relationsships with two s letters. The h-like lower marks in both The occurrences remain provenance doubts. Other repeated or overwritten type cells are recorded, retaining old-letter doubts in time, objects and definitely. The first M subscript is added in pen and the second is crossed out but still doubtful as M. Two pencil corner strokes delimit the diagram, while its right margin has both a star-like mark and a lower dash. The six drawn arrows preserve the source topology and are marked blue; all typed node text remains plain. The printed an, to and homotopisms and the absent witness section title were checked against every required difference row.'})
p=OUT/'records/MASTER_VARIANTS_134_3_4.json';old=json.loads(p.read_text());vs=[
 {'key':key,'before':r'technic\hand{\ensuremath{\smile}}al','after':'technical','kind':'author join applied','reason':'The visible pen curve joins the two parts of technical.','source_id':'OBS:ps_134-4_023:join'},
 {'key':key,'before':'relationsships','after':'relationships','kind':'slip corrected','reason':'One-off extra s; relationships is correctly attested on reviewed ps_134-3_036.','source_id':'OBS:ps_134-4_023:relationships'}];ids={v['source_id'] for v in vs};p.write_text(json.dumps([v for v in old if v['source_id'] not in ids]+vs,ensure_ascii=False,indent=2)+'\n')
