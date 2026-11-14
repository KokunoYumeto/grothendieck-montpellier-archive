import re,sys
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT
key='ps_134-3_065';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=re.sub(r'\\hand\{\$([^$]+)\$\}',r'\\hand{\\ensuremath{\1}}',line)
 new=new.replace(r'^\wedge',r'^{\hand{\wedge}}')
 if new!=line:edits.append([line,new,'All raised presheaf carets on this line are pen; preserve the typed A and repair nested math delimiters with ensuremath.'])
edits += [
 [r'\mspage{65}',r'\mspage{\hand{65}}','The folio is handwritten.'],
 ['test c ategory','test category','The scan has normal typewriter spacing inside category; the extra transcription space is unsupported.'],
 [r'a)\quad The category',r'a)\quad T\over[typed]{\unsure{h}}{h}e category','Displaced type impressions remain above and below h; the earlier h-like impression is uncertain and is now retained as a doubtful typed overprint.'],
 [r'\xout{\unsure{in}}',r'\xout{in}','The two cancelled insertion letters are recognizably dotted i and n.'],
 [r'\inserted[typed]{in(Cat)',r'\inserted[typed]{\over{in}{in}(Cat)','The insertion is typed, but its initial in is reinforced with irregular thick pen strokes over the original letters.'],
 [r'\inserted{can.}',r'\inserted[typed]{can.}','The interlinear can. has the same typewriter letterforms as the body.'],
 [r'\inserted{full}',r'\inserted[typed]{full}','The interlinear full is typed above a pen placement curve.'],
 [r'\inserted{the}',r'\inserted[typed]{the}','The replacement the above cancelled a is typed.'],
 [r'$i^*$ too,',r'$i^*$ t\over{\unsure{t}}{o}o,','The first o is a heavy pen oval over an old upright, t-like type impression; preserve uncertainty about the earlier letter.'],
 [r'A$_{/a}$\unsure{,}',r'A$_{/a}$\hand{,}','The right-edge enlargement shows the complete comma, including its descending curve.'],
 [r'types\xout{xx} of given',r'types\xout{xx} \over{of}{of} given','The visible of is pen retracing over typed of; both layers remain readable.'],
 [r'The most com\xout{\unsure{mx}}-',r'T\unsure{\over{h}{h}}e most co\over{m}{m}\xout{\unsure{m}}-','The last The has a strongly displaced h-like correction whose layer remains doubtful. At the right edge the word occupies co, a pen-retraced m, and one cancelled type cell before the hyphen; the original mx counted the cancellation stroke as another letter. The cancelled letter remains tentative.']
]
save_review({'key':key,'edits':edits,'diffs':{
 2645:[r'\xout{the}\inserted[typed]{can.}','The added can. is typed, rather than handwritten.','correct transcription'],
 2651:[r'\inserted[typed]{full}','The added full is typed above a hand insertion curve.','correct transcription'],
 2652:['final object,','The scan clearly has singular object followed by a comma.'],
 2653:[r'\inserted[typed]{the}\deleted{a}','The replacement the has typewriter letterforms; a is cancelled by pen.','correct transcription'],
 2656:['compute with,','The typed comma after with is visible at the right end of the line.']
 },'unsure':[['in','The i dot and n arch survive their machine cancellation.'],[r'\hand{,}','The entire pen comma is visible just inside the right edge.'],[r'\unsure{m}','There is one cancelled type cell after the retraced m, not two; its underlying letter remains m-like and uncertain.']],
 'illegible':[],
 'notes':[
 'The two The occurrences retain visible displaced corrections; the earlier impression of the first and the layer of the second remain doubtful rather than being silently flattened.',
 'The first o of too is a pen oval over an upright t-like earlier impression; the tentative old t is retained.',
 'The cancelled letters in the typed insertion read in.',
 'The initial in is retraced by hand over typed letters within an otherwise typed insertion.',
 'No hyphen is supplied at the clipped end of equivalent; the following line starts ly as in the transcription.',
 'The comma after A/a is now clear in the enlargement.',
 'Gives is a typewriter insertion; the existing typed option is confirmed.',
 'The of after the cancelled cells is traced in pen over typed of.',
 'Most asterisks have the repeated-bar typewriter shape. The star in the condition i-star(Delta_1) is a separate hand star; arrows, carets and Delta are pen.'
 ],'evidence':'Both complete halves and eight local enlargements inspected. Corollary 2’s localization statement and the singular final object are confirmed; analoguous and both occurrences of it\'s remain. Typed insertions include W(resp., the surrounding in(Cat) phrase, can., full, the and gives. The first in and the later of have pen retracing. The ordinary canonical functor is literally labelled i_A on this page. The right-edge comma after A/a is clear; the end of equivalent remains clipped without an invented hyphen. The two The corrections and the old letter under the first o of too remain doubtful. The closing commonly split has a retraced m and only one cancelled type cell.'})
# The single handwritten star differs from the repeated-bar typed stars.
import json
from pathlib import Path
q=Path('PS_READERS_WORK/review_notes/ps_134-3_065.json');c=json.loads(q.read_text());c['edits'].append([r'moreover $i^*$',r'moreover $i^{\hand{*}}$','This star has separate irregular pen rays, unlike the repeated horizontal bars of the typed stars elsewhere on the page.']);save_review(c)

key='ps_134-3_066';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for lineno,line in enumerate(src.splitlines(),1):
 if line.startswith('%'):continue
 new=line.replace(r'\hat{}',r'^{\hand{\wedge}}')
 for macro in ('longrightarrow','to','mapsto','rightrightarrows'):
  new=re.sub(r'\\'+macro+r'(?![A-Za-z])',r'\\hand{\\'+macro+'}',new)
 new=new.replace(r'i_!',r'i_{\hand{!}}')
 if lineno in (8,23,26,28):new=new.replace(r'i^{*}',r'i^{\hand{*}}',1)
 if new!=line:edits.append([line,new,'The arrows, raised carets and exclamation subscripts are handwritten. Where marked here, the star also has separate pen rays; the other typewriter stars remain plain.'])
up=r'\margin{\diagram{\begin{tikzpicture}\draw[->] (.6,0)--(.2,0) .. controls (0,0) and (0,.2) .. (0,.4)--(0,1.2);\end{tikzpicture}}}'
down=r'\margin{\diagram{\begin{tikzpicture}\draw[->] (.6,1.2)--(.2,1.2) .. controls (0,1.2) and (0,1) .. (0,.8)--(0,0);\end{tikzpicture}}}'
edits += [
 [r'e_{\unsure{A^{\hand{\wedge}}}}',r'e_{A^{\hand{\wedge}}}','The subscript A and its separate raised pen caret are clear in the enlarged first line.'],
 [r'\inserted{in (Cat)}',r'\inserted[typed]{in (Cat)}','The interlinear in (Cat) is typed; its curved placement line is pen.'],
 [r'\margin{\unsure{$\updownarrow$}}the one',up+'the one','The margin contains an upward bent arrow with a short lower horizontal tail, not a bidirectional arrow glyph.'],
 [r'\margin{\unsure{$\updownarrow$}}39.',down+'39.','The second mark is a separate downward bent arrow, with its horizontal tail above section 39.'],
 [r'aspher\deleted{\unsure{r}}ic',r'aspher\deleted{r}ic','The cancelled extra letter retains the typed r stem and upper shoulder.'],
 [r'\unsure{topos}',r'to\over{po}{po}s','The word is clearly topos, with p and o reinforced in pen; preserve the retracing over their typed forms.']
]
save_review({'key':key,'edits':edits,'diffs':{
 2661:[r'\xout{xxmdx}\inserted{[deleted]}','The hand replacement says deleted in square brackets over the machine cancellation.'],
 2663:[r'\hand{*}; \margin{cf def. p. 59}','The asterisk and the definition reference to p.59 are both present in the left margin/call arrangement.'],
 2666:[r'\inserted[typed]{in (Cat)}','The insertion is typed above a pen placement curve.','correct transcription'],
 2667:['this map','The source types this, including its initial t.'],
 2668:[r'\deleted{(\unsure{p. 60}}','The old reference is vigorously cancelled. Its tentative reading remains unresolved under the thick pen strokes.'],
 2669:[r'\inserted{(section 37)}','The replacement section number is clearly 37, with handwritten parentheses.'],
 2674:['39.','The source supplies only section number 39 and its opening sentence; the descriptive title belongs to the witness.'],
 2675:[r'\inserted{[if $A\neq\emptyset$],}','The handwritten nonemptiness condition has square brackets; its endpoint comma/placement stroke is retained as transcribed.'],
 2676:[up+' ; '+down,'Two distinct bent arrows point respectively upward and downward beside the paragraph end and the start of section 39. Neither is a bidirectional glyph.','correct transcription']
 },'unsure':[[r'A^{\hand{\wedge}}','The typed A and small raised pen caret are distinct.'],[r'\unsure{p. 38.}','The old page reference remains too heavily struck to settle its digits.'],[r'\unsure{;}','The old punctuation after I is dense with crossing strokes; the tentative semicolon cannot be confirmed.'],[r'\unsure{p. 60}','The cancelled reference remains dense and cannot be securely recovered.'],[up,'The mark is an upward bent arrow, reconstructed from its visible path.'],['r','The typed extra r is legible beneath its cancellation.'],[down,'The mark is a downward bent arrow, distinct from the upper one.'],[r'to\over{po}{po}s','The complete word topos is readable; its po has pen retracing.']],
 'illegible':[],
 'notes':[
 'The first final-object subscript is A with a pen caret. The word of has pen retracing over the typed of, as transcribed.',
 'Both old page references remain uncertain; the new references end of section 36 and section 37 are clear.',
 'The old punctuation after the parallel arrows is still obscured; retain the tentative semicolon.',
 'Topos is settled, with po retraced by hand. The extra r in aspherric is also settled and remains cancelled.',
 'Two separate opposite bent arrows were reconstructed graphically; no transposition instruction is inferred from them.',
 'The Greek letters, membership/braces, arrows, carets and exclamation subscripts are hand. Stars are distinguished individually from their typed repeated-bar counterparts.'
 ],'evidence':'Both full halves and nine local enlargements inspected. Corollary 3 asks for an endpoint-preserving map from i_!(I) to Delta_1; its adjunction argument and the literal this map are clear. The inserted in (Cat) is typed. The revised references point to sections 36 and 37, while the old cancelled page numbers remain doubtful. The first final-object subscript is settled as A-hat. The two margin marks are opposing bent arrows, not updownarrow characters, and are retained graphically without an inferred reordering. The final r cancellation and the word topos are recovered. Section 39’s nonempty qualification is handwritten; its source opening has no descriptive heading.'})
