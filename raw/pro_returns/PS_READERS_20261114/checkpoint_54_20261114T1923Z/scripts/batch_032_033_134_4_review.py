import sys,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT,OUT
variants=[]
key='ps_134-4_032';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'\hand{\Sigma}_h^{\circ}',r'\hand{\Sigma}_{\hand{\unsure{\circ}}h}^{\hand{\circ}}').replace(r'R_h \in ',r'R_h \hand{\in} ')
 if new!=line:edits.append(['\n'+line+'\n','\n'+new+'\n','The upper circles and membership sign are penned. Each generator Sigma also has a separate lower circular ink mark, retained doubtfully without asserting a cancellation.'])
edits += [
 [r'\inserted{an}',r'\inserted[typed]{an}','An is typed above the line and placed by a pen curve.'],
 [r'\xout{\unsure{structure on}}',r'\xout{structure on}','The letter sequence, including the separate final on, is readable beneath the x strikes.'],
 [r'\inserted{map} \xout{\unsure{functor}}',r'\inserted[typed]{map} \xout{functor}','Map is typed above the clearly cancelled functor.'],
 [r'\inserted{tied by a}',r'\inserted[typed]{tied by a}','The interlinear phrase is typed; its line and hook are penned.'],
 [r'\xout{\unsure{x}} \inserted{or by a $\check{\underline{I}}$-homotopy.)}',r'\xout{\illegible{1}} \inserted{or by a $\check{\underline{I}}$-homotopy.}','The old terminal cell beneath the x is unreadable. The supposed closing parenthesis is continuous with the placing curve beneath the handwritten continuation, not independent punctuation.'],
 [r'zero\xout{\unsure{x}}',r'zero\xout{\illegible{1}}','An x cancels a cell after zero, but the old letter under it is not securely readable.'],
 [r'\margin{//}',r'\diagram{\begin{tikzpicture}[baseline=-0.4ex,x=1em,y=1ex]\draw (0,0)--(0.7,0)--(0.9,1.7)--(2.1,1.7);\draw (0.6,0)--(0.8,1.7);\end{tikzpicture}}','The mark is a doubled stepped paragraph instruction extending from the preceding underline to above Of course, not a textual pair of slashes.'],
 [r'contra\unsure{d|c}tor','contradtor','The suspect typed letter has a full tall d ascender and closed bowl. Retain the literal d in the diplomatic source.'],
 [r'\inserted{end-point}',r'\inserted[typed]{end-point}','End-point is typed interlinearly.'],
 [r'\xout{\unsure{I get the imp}}',r'\xout{I get the imp}','The capital I, g descender, the and terminal imp fragment are legible under the strikes.'],
 [r'A\^{}',r'$A^{\hand{\wedge}}$','The mark is a handwritten superscript caret over A; replace the empty text accent with the actual mathematical symbol.'],
 [r"\hand{''}$\hand{\Delta}_1$",r"\hand{''} $\hand{\Delta}_1$",'Restore the visible word space between the closing quotation marks and Delta_1.'],
 [r'\unsure{One}',r'$\overset{\hand{\unsure{\scriptscriptstyle\perp\perp}}}{\underset{\hand{\unsure{\scriptscriptstyle,\frown}}}{\text{\over[typed]{\illegible{1}}{O}ne}}}$','One is legible, but O covers an older type cell. The two small upper T-like marks and lower comma/curve are retained as doubtful graphics rather than interpreted as letters.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3722:['two penned upper circles with doubtful lower circular marks','The two superscripts are handwritten circles; the small lower ink marks are independently visible and remain doubtful.'],
 3726:['tied by a; or by a checked-I-homotopy.','The first phrase is typed and the second penned. Both articles are a. The apparent terminal parenthesis belongs to the insertion curve.'],
 3727:['back to the structure of','The typed article the is present.'],
 3732:['if underlined I is','The handwritten insertion names the interval I, not the pronoun it.'],
 3736:['such as (Cat) and various ...','The inner parentheses around Cat are both present, inside the larger parenthesis.']
 },'unsure':[
 ['structure on','The cancelled phrase is recoverable from its stems and the separate on.'],
 [r'\unsure{I satisfies th}','Several old cells near the beginning and ending are obscured by the x row and light marks; retain the tentative fragment.'],
 ['functor','The old f/u/n/c/t/o/r sequence is clear beneath the strikes.'],
 [r'\illegible{1}','The x is a cancellation character, not a secure reading of the former cell.'],
 [r'\illegible{1}','The old cell after zero remains covered by its cancelling x.'],
 [r'\unsure{interactor}','The first pen contractor obscures the old prefix; interactor remains plausible but not secure.'],
 [r'\unsure{interactor}','The second instance preserves more of the ending, but its initial overwritten cells still do not settle the whole word.'],
 ['d','The tall ascender and closed bowl identify a typed d.'],
 ['I get the imp','The fragment and its terminal p descender are recoverable beneath the x line.'],
 ['One with unreadable old O-cell and doubtful upper/lower marks','The current word is clear. The old type cell and the functions of the small surrounding marks remain unresolved.']
 ],'notes':[
 'Both older interactor readings remain tentative beneath the penned replacement contractor.',
 'Structure on, functor and I get the imp resolve. I satisfies th remains tentative; the two small cancelled cells remain unreadable.',
 'One is readable. The older cell under O and the small upper and lower ink marks remain unresolved and are represented with doubt.',
 'The word visibly contains d. Its isolated master correction to contractor uses correctly typed contractor elsewhere on the same page.',
 'The lower-left 32 is handwritten; the large left-margin X is pencil.',
 'The emphasized three-part phrase has a second irregular wavy pen underline, consistent with the existing double-underlining markup.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_032:contractor','before':'contradtor','after':'contractor','line':35,'decision':'master slip variant','reason':'The isolated d for c is settled by the correctly typed contractor in generating contractor on the same page.'},
 {'source_id':'OBS:ps_134-4_032:paragraph','before':r'\diagram{\begin{tikzpicture}[baseline=-0.4ex,x=1em,y=1ex]\draw (0,0)--(0.7,0)--(0.9,1.7)--(2.1,1.7);\draw (0.6,0)--(0.8,1.7);\end{tikzpicture}}','after':r'\par','line':32,'decision':'master author instruction','reason':'The doubled step is an authorial paragraph instruction before Of course; its graphic remains in the diplomatic form.'}
 ],'evidence':'Both original halves, thirteen enlarged panels and a further enlarged One detail inspected. The upper circles and separate lower circular marks continue the preceding page notation. An, map, tied by a and end-point are typed additions; single and if I is are penned. The old structure on, functor and I get the imp fragments resolve, while I satisfies th and the earlier contractor prefixes remain doubtful. The two small x-cancelled cells are unreadable. The last curve after the inserted checked-I homotopy is an insertion hook, not a textual parenthesis. The doubled step before Of course instructs a new paragraph. Contradtor has a definite typed d. The empty A accent is replaced by the visible superscript caret. One has a clear live reading with an obscured older O-cell, two upper T-like marks and lower comma/curve, whose functions remain uncertain. The doubled wavy underline and pencil X are visible.'})
variants += [
 {'key':key,'before':'contradtor','after':'contractor','kind':'slip corrected','reason':'Isolated d for c, settled by correctly typed contractor on the same page.','source_id':'OBS:ps_134-4_032:contractor'},
 {'key':key,'before':r'\diagram{\begin{tikzpicture}[baseline=-0.4ex,x=1em,y=1ex]\draw (0,0)--(0.7,0)--(0.9,1.7)--(2.1,1.7);\draw (0.6,0)--(0.8,1.7);\end{tikzpicture}}','after':r'\par','kind':'author paragraph instruction','reason':'The doubled stepped mark instructs a paragraph before Of course.','source_id':'OBS:ps_134-4_032:paragraph'}]

key='ps_134-4_033';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line
 for m in ['longmapsto','longrightarrow','delta','e']:new=new.replace('\\hand{$\\'+m+'$}','\\hand{\\ensuremath{\\'+m+'}}')
 new=new.replace(r'\hand{$e$}',r'\hand{\ensuremath{e}}').replace(r'\varnothing_{M}',r'\hand{\varnothing}_{M}')
 if new!=line:edits.append(['\n'+line+'\n','\n'+new+'\n','The arrows, deltas, e and empty-object signs are handwritten. Repair nested math delimiters without changing their readings.'])
edits += [
 [r'\unsure{initial|initiah}',r'initia\over[typed]{h}{l}','The final l has a serifed upright over the surviving lower h shoulder.'],
 [r'\unsure{I} forgot',r'\over[typed]{E}{I} forgot','The live capital I is typed over E; the old middle/right bars remain visible.'],
 ['extra condition tha\n','extra condition that\n','The right-edge crop still preserves the stem and crossbar of final t; the letter is recoverable despite partial clipping.'],
 [r'\xout{\unsure{associative (commutative)}}',r'\xout{associative (commutative)}','The full cancelled phrase can be read from the ascenders, parentheses and surviving rounded letters.'],
 ['structure of a contra\n',r'structure of a contra\unsure{c}%'+'\n','A narrow final curved fragment reaches the cut edge. Retain c as tentative and join the following tor without inventing a hyphen.'],
 [r'\inserted{$\underline{L}_{M}$}\deleted{,}',r'\inserted[typed]{$\underline{L}_{M}$},','The inserted L and subscript are typed. The curve near the comma belongs to its insertion hook; the comma has no independent cancellation stroke.'],
 [r'\unsure{of|in}',r'\over[typed]{in}{of}','The live o/f are typed over the dotted i and n of the earlier preposition.'],
 [r'\xout{\unsure{and}}',r'\deleted{\xout{and}}','And is recoverable beneath the machine x row and a separate continuous pen cancellation.'],
 [r'\xout{\unsure{separ}}',r'\deleted{\xout{separ}}','The fragment separ is legible and has both machine strikes and an additional pen stroke.'],
 [r'Law\xout{\unsure{e}}vere',r'Law\unsure{\over{e}{e}}vere','The intervening e-like cell is densely marked in pen, but no separate x or secure cancellation boundary is visible. Retain the doubtful marked cell rather than silently delete it.'],
 ['Composi\n','Composi%\n','Suppress a TeX word space before the next-line hyphen; no source character is added or removed.'],
 [r'\inserted{associative}',r'\inserted[typed]{associative}','Associative is typed above the line. Its placing curve leaves an live.'],
 [r'\xout{\unsure{Homxx$\underline{I}$x}}',r'\xout{\unsure{Hom $\underline{I}=$}}','Hom, an underlined I and a terminal equals-like pair are visible under the machine strikes; the intervening cells and exact former formula remain doubtful.'],
 [r'\hand{\unsure{$_{x}$|,}}',r'\xout{\unsure{,}}','The mark after section is a typewriter x over a possible comma, not a handwritten subscript x. The covered punctuation remains doubtful.'],
 ['suppose the\n',r'suppose \over[typed]{t}{T}he'+'\n','The first letter is a capital T over a smaller typed t. Preserve its visible case and lower layer.'],
 ['The follow-%',r'The follo\unsure{\over{w}{w}}-%','The final w before the hyphen is heavily pen-marked. Its independent cancellation is not secure, so it remains a doubtful live layer.'],
 [r'we\hand{a}k',r'we\over{a}{a}k','The handwritten a retraces a visible typed a; it is not an insertion into a blank.'],
 [r'\mspage{33}',r'\margin{33}','The lower-left 33 is a handwritten archive sheet number. The typescript number is 121 at the head.'],
 [r'\margin{biffé par erreur}',r'\margin{\diagram{\begin{tikzpicture}[x=1cm,y=1cm,baseline]\draw (0,0) ellipse (1.2 and 0.55);\node at (0,0) {\shortstack{biffé par\\erreur}};\draw[->] (1.15,0.1)--(1.6,0.15);\end{tikzpicture}}}','The note is circled and has a right-pointing pen arrow toward the reinstated hypothesis; reconstruct those visible graphics.']
]
stet_before=r'\deleted{of type Hom\hand{$_{3}$}  (a weak homotopy interval structure)}'
stet_after=r'of type Hom\hand{$_{3}$}  (a weak homotopy interval structure)'
save_review({'key':key,'edits':edits,'diffs':{
 3740:['Let X be an object','The object is singular; the witness plural is not on the page.'],
 3743:['section o_X','The section symbol is a small typed o, with no middle bar indicating e.'],
 3756:['of type Hom3 (a weak homotopy interval structure), restored by authorial stet','The pen deletion has dashed restoration marks beneath it and a circled note biffé par erreur with an arrow. The corrected forms must restore the hypothesis; the witness omission loses the later author instruction.']
 },'unsure':[
 [r'initia\over[typed]{h}{l}','The live l and older lower h shoulder can be separated.'],
 [r'\over[typed]{E}{I}','The old E bars and the live serifed I are both visible.'],
 ['associative (commutative)','The entire cancelled phrase is recoverable, including its parentheses.'],
 [r'\unsure{\over{e}{o}}','The two overlapping rounded shapes do not securely establish the old e/new o layers; retain the existing whole-layer doubt.'],
 [r'\over[typed]{in}{of}','The dotted old i and n shoulder are visible beneath the live o/f.'],
 ['and','The surviving n and d contours settle the old word beneath machine and pen strikes.'],
 ['separ','The s/e and p descender, followed by a/r, can be read under the cancellation.'],
 [r'\unsure{\over{e}{e}}','The dark e-like cell has no secure independent cancellation boundary; its live/deleted status remains doubtful.'],
 [r'\unsure{Hom $\underline{I}=$}','Hom and the underlined I/terminal equals-like pair are recoverable, but the complete earlier formula is not.'],
 [r'\unsure{,}','A machine x covers the possible comma; no handwritten subscript is established.']
 ],'notes':[
 'The final letter of initial is l typed over h, with the old lower shoulder still visible.',
 'I is typed over E; of is typed over in. More retains a doubtful rounded-letter overlay, and the extra Lawvere cell remains a doubtful marked e rather than a secure deletion.',
 'The whole cancelled associative (commutative) line resolves from surviving letters and parentheses.',
 'The mark after section is a machine x over uncertain punctuation, tentatively a comma.',
 'Associative is typed. The continuous placing curve leaves an live.',
 'The full Hom3 hypothesis is restored by dashed stet marks and the circled biffé par erreur note with its arrow. The exact full-span master override implements that author instruction.',
 'The lower-left handwritten 33 is corrected to archive-margin metadata; the typed head number is 121.',
 'The clipped final t in that remains readable. The final c before tor is only a narrow edge fragment and remains doubtful. Composi and the next-line hyphen are joined without changing visible characters.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_033:stet','before':stet_before,'after':stet_after,'line':46,'decision':'master author instruction','reason':'The author explicitly labels this deletion biffé par erreur and places dashed restoration marks beneath the phrase. The hypothesis must return in corrected forms, while the diplomatic form retains the visible deletion and note.'},
 {'source_id':'OBS:ps_134-4_033:lawvere_final','before':'final object; unique map of separated intervals to L_M','after':'final object; unique map of separated intervals to L_M','line':18,'decision':'retain author claim','reason':'The source claim is preserved but is too strong under the stated hypotheses: in Set a three-element interval has two endpoint-preserving maps to the two-element Lawvere interval. The guide distinguishes existence from the unsupported uniqueness.'},
 {'source_id':'OBS:ps_134-4_033:law','before':'las,','after':'law,','line':35,'decision':'master slip variant','reason':'The isolated s for w is settled by intersection law and composition law elsewhere in the checked section.'}
 ],'evidence':'Both original halves and seventeen enlarged panels inspected. Initial resolves to l over h, I forgot to I over E, and of to of over in. The cancelled associative (commutative), and and separ readings resolve. More retains its rounded-layer doubt; the dark extra e-like cell in Lawvere has no securely separable cancellation and remains doubtful. The inserted L_M and associative are typed; their curves do not independently cancel the nearby comma or an. The right-edge t of that is readable, while the c before tor remains a tentative edge fragment. The old Hom/I formula and punctuation after section remain doubtful. The final w before follow-wing remains a doubtful pen-marked live cell; weak has a retraced a over typed a. The Hom3 hypothesis has a clear authorial stet: dashed marks beneath the struck phrase, a circled biffé par erreur note and an arrow. Its restoration is recorded as a full-span author instruction. The archive number 33 is corrected from mspage to margin. The printed uniqueness of maps to the Lawvere interval is preserved and flagged as mathematically too strong.'})
variants += [
 {'key':key,'before':stet_before,'after':stet_after,'kind':'author stet restoration','reason':'The author marks the deletion as biffé par erreur and restores it with dashed stet marks.','source_id':'OBS:ps_134-4_033:stet'},
 {'key':key,'before':'las,','after':'law,','kind':'slip corrected','reason':'Isolated s for w, settled by correctly typed law elsewhere in the checked section.','source_id':'OBS:ps_134-4_033:law'}]
p=OUT/'records/MASTER_VARIANTS_134_3_4.json';old=json.loads(p.read_text());ids={v['source_id'] for v in variants};p.write_text(json.dumps([v for v in old if v['source_id'] not in ids]+variants,ensure_ascii=False,indent=2)+'\n')
