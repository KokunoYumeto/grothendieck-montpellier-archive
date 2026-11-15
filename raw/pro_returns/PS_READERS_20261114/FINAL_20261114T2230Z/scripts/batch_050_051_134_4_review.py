import sys,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT,OUT
key='ps_134-4_050';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text()
join=r'\diagram{\begin{tikzpicture}[baseline=0ex,x=1em,y=1ex]\draw[color=blue,line width=.65pt] (0,-.25)--(.65,.15);\end{tikzpicture}}'
slash=r'\diagram{\begin{tikzpicture}[baseline=0ex,x=1em,y=1ex]\draw[color=blue,line width=.4pt] (0,-2.5)--(.6,3);\end{tikzpicture}}'
edits=[
 [r'canonic\hand{\unsure{-}}al','canonic'+join+'al','The mark is a short sloping pen connector below the adjoining c and a, not an ordinary textual hyphen. Reconstruct its graphic.'],
 [r'\hand{\unsure{``}}',r'\hand{``}','Two separate sloping pen strokes give an unambiguous opening quotation mark.'],
 [r'\hand{\unsure{\'\'}}',r'\hand{\'\'}','The two closing pen strokes are clear.'],
 [r'\xout{contractibility}\inserted[typed]{homotopy}',r'\xout{contractibility} \inserted[typed]{homotopy}','The interlinear homotopy is typed, with a separate word boundary from the cancelled word in the linearized diplomatic text.'],
 [r'la\hand{\unsure{t}}ter',r'la\hand{t}\over{t}{t}er','There are two clear pen t stems: an added first t and a retracing of the typed second t. The resulting word is latter.'],
 [r'tr\over{\unsure{x}}{\unsure{h}}ough',r'tr\over{\unsure{x}}{h}ough','The live third character is h. Its old cell remains hidden, and the manuscript order tr-h-ough is retained.'],
 [r'any\over{\unsure{h}}{\unsure{y}}how',r'an\over[typed]{\unsure{h}}{y}how','The y occupies one cell over an h-like lower impression. There is no separate preceding y; the live word is anyhow and the new y is regular typing.'],
 [r'investigati\hand{on}',r'investigati\over{\unsure{on}}{on}','The final on is penned over visible lower typed remnants, not simply added; their exact old letters remain doubtful.'],
 [r'(page 42)\over{,}{.}\xout{\unsure{x}}',r'(page 42)\unsure{\over{,}{.}}\xout{\illegible{1}}','The punctuation retains a comma tail beneath a heavy dot-like head, so the layer interpretation is doubtful. The following cancelled cell is unreadable, not a secure old x.'],
 [r'$A\hand{^\wedge}$\hand{/}being',r'$A^{\hand{\wedge}}$'+slash+'being','The hat is penned. The following long slanted stroke is a graphic extending down toward the next line, not a textual slash; reconstruct it.'],
 [r'homot\hand{o}py',r'homot\over{o}{o}py','The second o is pen-retraced over the visible typed round letter.'],
 [r'There \over{\unsure{is}}{ar}e',r'T\over[typed]{h}{H}ere \over[typed]{\unsure{is}}{ar}e','There has a regular capital-H overprint on h. The ar is also typed over a doubtful lower is-like pair, not handwritten.']
]
edits=[[(v.replace("\\'","'") if isinstance(v,str) else v) for v in e] for e in edits]
for line in src.splitlines():
 if r'$A\to ' in line:
  edits.append([line,line.replace(r'\to',r'\hand{\to}').replace(r'B^\wedge',r'B^{\hand{\wedge}}'),'The arrow and, where present, the B-hat are drawn in pen; the surrounding symbols remain typed.'])
save_review({'key':key,'edits':edits,'diffs':{
 4055:[r'W_(Cat)','Both parentheses enclosing Cat in the subscript are plainly typed.'],
 4056:['W_(Cat) namely','No comma appears before namely.'],
 4059:['nicely, it could','The typed comma after nicely is visible.'],
 4061:['d)However there is','There is no comma after However.'],
 4064:['latter approach','Two pen t stems are present, one added and the other retracing typed t.'],
 4075:['test categories, and never','The comma after categories is present.'],
 4077:['for the time being all these','No comma follows being.']
 },'unsure':[
 ['short graphic connector','The pen stroke joins the separated parts below baseline; it is clear as a graphic rather than a textual hyphen.'],
 ['opening quotation mark','Two distinct pen strokes resolve the opening quote.'],
 ['closing quotation mark','Two distinct pen strokes resolve the closing quote.'],
 [r'\unsure{W}','The lower cell is mostly covered by pen w; capital W remains a candidate.'],
 ['t','The added t has a clear stem and crossbar; the following typed t is also retraced.'],
 [r'\unsure{x}','The older third cell in trhough remains obscured beneath the live h.'],
 ['h','The live third letter has an h stem and shoulder, without resolving the source letter order.'],
 [r'\unsure{h}','The lower cell under y is h-like but cannot be completely separated from the new type.'],
 ['y','The live y is a regular typed glyph sharing the same cell with the lower layer.'],
 [r'\unsure{f}','The lower f-like character is covered by the thick pen f, so the old reading remains doubtful.'],
 [r'\illegible{1}','The crossed old character after the punctuation cannot be recovered as an independent x.'],
 [r'\unsure{a}','The new capital A conceals most of the old small cell; a remains tentative.'],
 [r'\unsure{is}','The two old cells remain only an is-like candidate beneath regular typed ar.']
 ],'illegible':[[r'\illegible{1}','The cancelled line clearly begins But we could get; its final old word remains too crossed to settle.']],
 'notes':[
 'The connector is a short low pen stroke joining the c and a positions; it is reconstructed graphically, and the joined word is applied only by a separate corrected-form variant.',
 'But we could get is legible beneath the machine row. The final word is still too crossed for a settled reading.',
 'Both quotation marks are clearly handwritten, and homotopy is clearly typed interlinearly above cancelled contractibility.',
 'The live h in trhough resolves but its old cell remains doubtful. Anyhow has a same-cell typed y over an h-like lower layer; the extra y in the initial transcription was spurious.',
 'The long slanted stroke after A-hat runs toward the next line and is preserved as a graphic, not a textual slash. There has a separate typed H over h.',
 'The second o in homotopy is penned over the typed o, now represented as a retracing.',
 'The pencil folio 50 is present at lower left.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_050:canonical_join','before':'canonic'+join+'al','after':'canonical','line':20,'decision':'master author instruction','reason':'The short low pen connector joins the two parts of canonical; retain the graphic diplomatically and apply the word join in corrected forms.'}
 ],'evidence':'Both original halves and twelve enlarged panels inspected. The three prose arrows and two B-hats are penned. The low connector in canonical is graphic. Both handwritten quotes resolve, and the second t in latter is additionally pen-retraced. The h of trhough resolves while its old layer remains doubtful; no speculative transposition is made. Anyhow contains a same-cell typed y over a doubtful h-like lower cell, not an extra y. Investigation has penned on over doubtful older remnants; for and Among retain uncertain lower cells. The punctuation after p. 42 retains a doubtful comma/dot layering and an unreadable cancelled following cell. The A-hat separator is a long graphic stroke, and There has typed H over h. The ar of are is typed over doubtful is-like impressions. The second o of homotopy is pen-retraced. The final word in the cancelled But we could get line remains illegible.'})
p=OUT/'records/MASTER_VARIANTS_134_3_4.json';old=json.loads(p.read_text());v={'key':key,'before':'canonic'+join+'al','after':'canonical','kind':'author word join','reason':'The low pen connector joins the two separated typed parts of canonical.','source_id':'OBS:ps_134-4_050:canonical_join'};p.write_text(json.dumps([x for x in old if x['source_id']!=v['source_id']]+[v],ensure_ascii=False,indent=2)+'\n')

key='ps_134-4_051';edits=[
 [r'an\xout{xxx}',r'an\xout{\illegible{1}}','The cancelled short run after an has no secure lower reading.'],
 [r'three,\xout{xxx}',r'three,\xout{\illegible{1}}','The three crossed cells after the comma cannot be read securely.'],
 [r'\xout{\unsure{pro}}',r'\xout{pro}','The lower p, r and o can be separated beneath the x row.'],
 [r'homotopy structure\xout{s}',r'homotopy structure\deleted{\unsure{s}}','The terminal cell is crossed by dense irregular pen strokes. A lower s is plausible, but a separate machine-x layer is not secure.'],
 ['following two',r'fo\over[typed]{\unsure{h|d}}{l}lowing two','The first l is typed over a lower rounded h/d-like letter; the live l is clear and the older letter remains doubtful.'],
 [r'conditions\xout{x}',r'conditions\xout{\illegible{1}}','The extra cancelled cell after conditions has no recoverable lower character.'],
 [r'maps \xout{xx} f,g',r'maps \xout{to} f,g','The old two cells resolve as t and o through the machine crosses.'],
 [r"(i')  \xout{f}For",r"(i')  \over{f}{F}or",'The capital F is penned over the same typed f cell, not preceded by a separate cancelled f.'],
 ['for any section',r'for any sec\over{t}{t}ion','The t, not the c, is retraced in pen with a tall stem over its typed letter.'],
 [r'\xout{wxx}',r'\xout{w\illegible{1}}','Only the initial w can be read securely in the cancelled final run.']
]
save_review({'key':key,'edits':edits,'diffs':{
 4082:['was introduce','No to is typed between was and introduce.'],
 4083:["or the equivalent condition e')",'The word condition is explicitly present before the reference.']
 },'unsure':[
 [r'\unsure{6}','The lower digit is largely hidden by the long pen 7; its tentative 6 reading remains uncertain.'],
 ['pro','The p-r-o letter bodies are visible beneath regular crosses.']
 ],'notes':[
 'The pen 7 is secure, but the earlier digit remains too obscured to settle beyond the existing 6 candidate.',
 'Following has a typed l over a rounded h/d-like lower letter; the lower reading remains doubtful.',
 'Pro and the two old letters to resolve. The old runs after an and three, the extra conditions cell and the final w-run remain wholly or partly unreadable. The structure ending is pen-cancelled with a tentative s. The t before f and th before h remain readable. The apparent initial f before For is instead the lower letter in a same-cell pen F correction.',
 'The pen stroke belongs to t in section, with a tall retraced stem, not to c and not a mere typing blemish.',
 'The pencil folio 51 is visible at lower left.'
 ],'evidence':'Both original halves and eleven detail panels inspected. The live section number 57 overlays an uncertain earlier 6. All displayed and prose pi, delta, Sigma, tilde, membership and arrow signs are handwritten as encoded. Pro and to resolve under machine cancellation; other short old runs remain lacunose. The first l of following is typed over an h/d-like lower cell, which remains doubtful. The terminal cell of structure is pen-cancelled and only tentatively s. For begins with a pen capital F over the same typed f cell, correcting the initial false duplication. The t of section is pen-retraced. The wording was introduce and equivalent condition e-prime is preserved against the witness additions/omissions. The final cancelled run retains only its legible w.'})
