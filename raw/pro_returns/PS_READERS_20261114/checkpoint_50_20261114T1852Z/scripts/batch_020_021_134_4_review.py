import sys,re
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT

key='ps_134-4_020';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=re.sub(r'\\hand\{\$([^$]+)\$\}',lambda m:r'\hand{\ensuremath{'+m[1]+'}}',line)
 new=new.replace(r'\to',r'\hand{\to}').replace(r'\emptyset_M',r'\hand{\varnothing}_M')
 if new!=line:edits.append(['\n'+line+'\n','\n'+new+'\n','The arrows and initial-object circle are penned; nested math delimiters in handwritten symbols are repaired mechanically.'])
edits += [
 [r'\xout{kix}',r'\xout{ki\illegible{1}}','The initial k and i remain readable, while the last cancelled cell is clipped and obscured.'],
 [r'look for \deleted{strict} \inserted{contractible}',r'look \over[typed]{\illegible{1}}{f}or \deleted{strict} \inserted{\uline{contractibl\unsure{e}}}','For has an older rounded impression beneath typed f. The first handwritten contractible is underlined and its final e is partly clipped, so that completion remains doubtful.'],
 ["cases I'\nve","cases I'%\nve",'Join the two visible parts of I\'ve mechanically across the scan line break.'],
 [r'\unsure{\hand{s,}|s,}',r'\hand{s,}','The final s and descending comma are unmistakably handwritten, with continuous curved pen strokes.'],
 [r'\xout{whix}',r'\xout{while}','The old while is recoverable beneath the x row.'],
 [r'\xout{xx} \inserted[typed]{when}',r'\xout{\illegible{1}} \inserted[typed]{when}','The two machine-cancelled cells beneath the typed when cannot be independently recovered.'],
 [r'\xout{brxn}',r'\xout{b\unsure{e}tw}','The old b, t and w are visible; the second cell is plausibly e but remains partly covered.'],
 [r'\xout{Jxix}',r'\xout{J i\unsure{s}}','J and i are recoverable; the last rounded cell remains partly hidden by its x strike.'],
 [r'\unsure{\over{t}{T}|\hand{T}}',r'\over{T}{T}','The old full-width capital-T bar and stem remain visible beneath the pen T.'],
 [r'\hand{\ensuremath{\delta_0}} and',r'\hand{\ensuremath{\delta}}$_0$ and','The last endpoint formula has a pen delta and a separate typed subscript.'],
 [r'\hand{\ensuremath{\delta_1}} are',r'\hand{\ensuremath{\delta}}$_1$ are','The second final endpoint likewise separates pen delta from typed subscript.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3494:['an object in M','The preposition is in, not the witness of.'],
 3497:['W-homotopic','A small handwritten W- is placed above the beginning of homotopic and remains part of the word.']
 },'unsure':[
 [r'\hand{s,}','Both strokes are free pen curves, distinct from the typed impression ending before them.'],
 [r'\over{T}{T}','The old capital-T bar extends at full height behind the heavier pen T.']
 ],'notes':[
 'The final s and comma of impressions are handwritten and resolve the initial provenance doubt.',
 'This has a pen capital T over a recognizable typed capital T, not a secure lowercase-t layer.',
 'Cancelled while is recovered; ki has a clipped unreadable ending, betw retains doubt in e, and J is retains doubt in s. The cancelled n homotopy sequence remains readable beneath its x row.',
 'The bottom contractible words show ordinary typed t/i forms on enlargement; no independent h correction can be securely distinguished.',
 'Over e is a typed interlinear insertion. The curve places it after aspheric without deleting that word.',
 'The small W- above homotopic is penned. Its prefix joins directly to the word.',
 'The deltas are penned and the small indices are typed; the final two endpoint names are encoded separately for that reason.',
 'The lower-left 20 is handwritten. The first contractible insertion is underlined and clipped at its last e; its exact edge reading remains doubtful.'
 ],'evidence':'Both original halves and thirteen enlarged panels inspected. The first contractible insertion is underlined and reaches the clipped edge; the final e remains conjectural. For has an unreadable old type impression. The final s and comma of impressions are clearly penned. While is readable under machine strikes, while the old final cells in ki..., betw and J is remain partly uncertain. The capital T of This is a pen retrace over a recognizable capital T. The bottom t/i forms do not establish the supposed h correction. The three strict-to-contractible revisions and the two which-are replacements are retained; the inserted W- is present despite the witness omission. The literal in M and all required difference rows were checked directly.'})

key='ps_134-4_021';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=re.sub(r'\\hand\{\$([^$]+)\$\}',lambda m:r'\hand{\ensuremath{'+m[1]+'}}',line)
 new=new.replace(r'\longrightarrow',r'\hand{\longrightarrow}').replace(r'\longmapsto',r'\hand{\longmapsto}')
 if new!=line:edits.append(['\n'+line+'\n','\n'+new+'\n','The arrows are handwritten. Nested math delimiters in handwritten symbols are repaired mechanically.'])
edits += [
 [r'\xout{inxM}',r'\xout{in M}','The old words in M are legible; the intervening x is the cancellation stroke, not text.'],
 [r'\xout{thisxelemen}',r'\xout{this elemen\unsure{t}}','This elemen is recoverable; the last t is clipped at the right edge and remains conjectural.'],
 [r'\over{\unsure{b}}{p}',r'\over[typed]{\unsure{b}}{p}','The new p has regular typewriter form over a taller, b-like old cell whose exact identity remains doubtful.'],
 [r'\over{\unsure{t}}{r}',r'\over[typed]{t}{r}','The old t stem and crossbar and the later typed r are distinguishable.'],
 [r'T\over{\illegible{1}}{h}en',r'T\over[typed]{H}{h}en','The two upper bars are remnants of a displaced typed H overlaid by typed h, not a separate dagger.'],
 [r'\uline{contract\unsure{ib|b}}',r'\uline{contract\hand{\unsure{ib}}}','The right-edge ending is penned and clipped. A narrow stroke lies beside b, but a separate i is not securely established; retain the whole proposed ib as doubtful.'],
 [r'\xout{\unsure{Thusxinxthisxcasex,xtherexxis}}',r'\xout{Thus in this case, there is}','The old words are recoverable beneath the regular x row; the x marks are not literal letters of the phrase.'],
 [r'\xout{conditionsx}',r'\xout{conditions}','The final x belongs to the cancellation row; the old word is conditions.'],
 [r'T\over{\illegible{1}}{h}e only',r'T\over[typed]{H}{h}e only','This has the same displaced typed H/h pair as Then.'],
 [r'looked \over{\illegible{1}}{up}',r'looked \over[typed]{u}{u}\over{\illegible{1}}{p}','The u consists of repeated typing, whereas the p is penned over an obscured older cell.'],
 [r'\over{v}{c}ategories',r'\over[typed]{v}{c}ategories','The v/c overlap has typewriter serifs and regular impressions.'],
 [r'represent\over{\unsure{g}}{s}s',r'represent\unsure{\over{\illegible{1}s}{s}}','A broad S-like pen loop spans an unreadable older cell and a clear typed s. Its scope over one or both cells is unresolved; no independent cancellation is visible. The entire terminal layered span remains doubtful, as independently confirmed.'],
 ['hence again an intersection',r'hence again an int$\overset{\hand{\unsure{\prime}}}{\mathrm e}$rsection','A short raised pen mark sits above the typed e; retain it as an uncertain graphic instead of discarding it as a stray mark.'],
 ['\n2.4.\n','\n'+r'\hand{2.4.}'+'\n','The date is handwritten.'],
 [r'a\over{\illegible{1}}{b}out',r'a\over[typed]{\unsure{o}}{b}out','The live b is typed; its older layer has a rounded o-like body but is not secure.'],
 [r'\over{a}{o}r',r'\over{\unsure{a}}{o}r','The pen o is clear, but the covered older rounded letter does not securely establish a.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3498:['Then (as already noticed previously','There is no closing parenthesis after noticed; the source closes after comparison lemma.'],
 3503:['there is equivalence','No an occurs before equivalence.'],
 3506:['homotopy intervals','The first display member spells out intervals, unlike the abbreviated witness.'],
 3513:['equivalent to the final one','The article the is plainly present.'],
 3515:['50.','There is no section title on the manuscript, only the number 50 after the handwritten date.'],
 3517:['homotopy intervals','The final noun is plural, with a visible terminal s.']
 },'unsure':[
 [r'\unsure{b}','The older taller type cell is b-like, but the overlapping p obscures its bowl.'],
 ['t','The older stem and crossbar of t remain visible beneath typed r.'],
 [r'\hand{\unsure{ib}}','A narrow pen stroke beside b may supply i, but clipping prevents a secure separation; an independent view agrees.'],
 ['Thus in this case, there is','The underlying phrase can be read through the regular x strikes.'],
 [r'\unsure{\over{\illegible{1}s}{s}}','The large S-like pen loop has no separate cancellation stroke. Whether it replaces one or both typed terminal cells is unresolved.']
 ],'illegible':[
 ['H','The upper horizontal fragments and stems belong to a displaced typed capital H.'],
 ['H','The second H/h overlap has the same form.'],
 [r'\illegible{1}','The old letter beneath the heavy pen o in so remains covered.'],
 [r'u plus \illegible{1}','The repeated u is recognizable, but the old cell under pen p remains obscured.'],
 [r'\illegible{1}','The old cell under the broad handwritten e in equivalent remains covered.'],
 [r'\unsure{o}','The older round type body under b is o-like but not secure.']
 ],'notes':[
 'The clipped contractible ending contains a narrow pen stroke beside b, but no secure independent i. Its proposed ib remains doubtful.',
 'The cancelled phrase reads Thus in this case, there is beneath the x row.',
 'Then and The only both have typed H/h overlaps; the upper fragments are not separate handwritten daggers.',
 'Idempotent has typed p over a doubtful b-like earlier impression.',
 'The small raised mark above e in intersection is retained graphically with explicit doubt.',
 'Homotopy is typed interlinearly and its placing hook leaves interval live.',
 'The lower-left 21 and date 2.4 are handwritten. The terminal represents layers remain wholly doubtful as to the scope of the pen S; no cancellation is inferred.'
 ],'evidence':'Both original halves and fourteen enlarged detail panels inspected. The older text in M and Thus in this case, there is is recoverable beneath x rows; the first-line elemen ending is clipped. The p in idempotent and r in respectively are typed corrections. Both H/h pairs are typed rather than pen corrections. The ending of contractible remains uncertain at the clipped edge. Up separates repeated typed u from pen p over an unreadable old cell. The broad S-like mark at represents spans two terminal cells without a clear cancellation boundary; independent review agrees that its scope must remain doubtful. The small raised mark above intersection e is preserved. The date is handwritten. All six required wording/addition/omission differences were compared directly, including the absent arXiv section title.'})
