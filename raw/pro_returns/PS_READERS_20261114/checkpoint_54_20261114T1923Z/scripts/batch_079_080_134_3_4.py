import sys,re
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT
key='ps_134-3_079';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'A\hat{}',r'A^{\hand{\wedge}}').replace(r'\longrightarrow',r'\hand{\longrightarrow}')
 if new!=line:edits.append([line,new,'The presheaf carets and the four displayed single arrows are pen additions.'])
edits += [
 [r'f\unsure{or}m',r'f\over{\unsure{ro}}{or}m','The visible or is penned over two typed cells, plausibly old ro; retain uncertainty on their former order.'],
 [r'\unsure{spheri}','spheri','The final pen letters s-p-h-e-r-i are distinguishable above and across the earlier type.'],
 [r'\deleted{\unsure{some}}',r'\unsure{some}','The crowded some-like group has uncertain reading and cancellation status; preserve the whole proposed deleted layer as doubtful.'],
 [r'(\deleted{as}\inserted',r'(\deleted{as} \inserted','Keep the inserted replacement phrase separate from the cancelled word.'],
 [r'\text{weak test categories}',r'\text{weak test categor\over[typed]{y}{i}es}','The first trilogy i is typed over a y whose descender is still visible.'],
 [r'\text{test categories}',r'\text{test categor\over[typed]{\unsure{m}}{i}es}','The middle trilogy i overlays a wider m-like typed impression, not a handwritten addition.'],
 [r'\inserted{Weak}',r'\inserted[typed]{\uline{Weak}}','Weak is typed interlinearly and underlined in pen.'],
 [r'\inserted{small}',r'\inserted[typed]{small}','Small has monospaced typewriter forms; only its placing stroke is pen.'],
 [r'\hand{F} \hand{\longmapsto}',r'\over{F}{F} \hand{\longmapsto}','The displayed F is penned over a typed capital F, rather than written into an empty space.'],
 [r'i_A^{\hand{*}}',r'i_A^{\over[typed]{*}{*}}','The star has two displaced typewriter impressions with flat terminal bars.'],
 [r'\hand{j}_A(C)',r'\over{j}{j}_A(C)','The hand retraces the j over the remaining typed stem and foot.'],
 ['(i) The functors',r'(i) T\over[typed]{h}{h}e functors','The h has displaced typed remnants above and below its main impression.'],
 [r'\unsure{in}',r'\over[typed]{o}{i}n','The lower rounded o and upper dotted i are visible in the first cell of in.'],
 [r'\unsure{(Cat}',r'(Cat','The struck opening parenthesis and Cat letters are legible.'],
 [r'\margin{\unsure{(i}}',r'\margin{\textcolor{black}{\unsure{(i}}}','The incomplete bottom fragment has a typed serif i and a left parenthesis crossed by pen. Its cancellation extent remains doubtful; it is not wholly handwritten.']
]
save_review({'key':key,'edits':edits,'diffs':{
 2889:[r'I \inserted{then} finally called','Then is a live hand insertion before finally, absent from the witness.'],
 2894:[r'\inserted[typed]{\uline{Weak}} \uline{\over{T}{t}est categories}','Weak is typewritten above the line and underlined; the T-to-t correction is pen.','correct provenance'],
 2895:[r'\inserted[typed]{small}','The added small is typed, with a pen placement curve.','correct provenance'],
 2897:['functorial in C resp. in F','The source has functorial without the additional ly.'],
 2898:[r'Pr\over{\illegible{1}}{es}umably the following','No comma follows Presumably. The pen es covers an earlier layer that cannot be separated securely.'],
 2901:[r'\margin{\textcolor{black}{\unsure{(i}}}','The small bottom fragment is typed (i with an overlapping pen mark; its intended cancellation or continuation is uncertain.','correct provenance; retain doubt']
 },'unsure':[
 [r'\unsure{t}','The dark pen d covers the earlier narrow type cell, preventing a secure identification.'],
 [r'\over{\unsure{ro}}{or}','The live or is clear, but the two covered typed cells may have been transposed ro.'],
 [r'\unsure{cycli}','The old internal letters of acyclicity are too heavily covered to settle independently.'],
 ['spheri','The final six handwritten letters are legible.'],
 [r'\unsure{it}','The two-letter group remains very heavily inked; it is not securely readable enough to remove the doubt.'],
 [r'\unsure{some}','The some-like group and its cancellation status both remain doubtful under the crowded handwriting.'],
 [r'\unsure{ies}','The final handwritten y is clear, but the covered earlier ending remains uncertain.'],
 [r'\over[typed]{o}{i}n','The typed o bowl and dotted i can be distinguished.'],
 ['(Cat','The crossed fragment is legible.'],
 [r'\textcolor{black}{\unsure{(i}}','The typed incomplete fragment is visible, but the pen mark does not settle its intended disposition.']
 ],'illegible':[[r'\illegible{1}','The original layer under the pen es in Presumably is not independently recoverable.']],
 'notes':[
 'The last standard letter is a pen d over a covered typed letter; the proposed old t remains doubtful.',
 'The visible final or is penned. The lower typed order ro is plausible but uncertain, so the layered correction remains qualified.',
 'The pen replacement spheri is readable; the lower cycli remains uncertain.',
 'It and the some-like group remain uncertain, including the latter cancellation status. Be, a, the final y and the closing parenthesis are clear.',
 'The first two trilogy i characters are typed corrections: one over y and one over a wider m-like letter. Neither is a separate handwritten i.',
 'F and j are pen retracings over type, and the mapsto arrows are entirely pen. The star instead has repeated typed impressions.',
 'The final in is typed i over o followed by n, and the cancelled (Cat is legible. The plural s remains pen-deleted.',
 'The displaced h marks around The are typed impressions and have been recorded.',
 'The bottom fragment is typed (i with a pen mark crossing its left side. It remains doubtful and is not expanded into a completed numeral.'
 ],'evidence':'Both original halves and thirteen enlarged detail crops inspected. The date 26.3 and new section 44 introduce the explicit weak/test/strict trilogy. The final standard d and the old letters in asphericity remain partly covered; final spheri is clear. The form correction is pen or over a doubtful earlier ro. The heavily corrected parenthesis retains uncertainty on it, some and the old plural ending. Weak and small are typed interlinear additions; Weak has a pen underline. The two first category-i corrections and the displayed star are typed overprints, while F and j are pen retracings over type. All displayed arrows and carets are penned. The cancelled (Cat is recoverable, and in has typed i over o. The incomplete lower-left (i is typed with a doubtful pen cancellation.'})

key='ps_134-3_080';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'A\hat{}',r'A^{\hand{\wedge}}').replace(r'\longrightarrow',r'\hand{\longrightarrow}').replace(r'\mapsto',r'\hand{\mapsto}').replace(r'\to',r'\hand{\to}')
 new=re.sub(r'\\ar\[([^\]]*)\]',lambda m:r'\ar['+m.group(1)+',color=blue]',new)
 if new!=line:edits.append([line,new,'The arrows and presheaf carets are penned. Hand-drawn diagram arrows are blue while their typed objects remain plain.'])
circle=lambda s:r'\begin{tikzpicture}[baseline=(n.base)]\node[inner sep=0pt] (n) {'+s+r'};\draw[color=blue,line width=.5pt] (n.center) ellipse [x radius='+('1.05em' if s=='iii' else '.58em')+r',y radius=.78em];\end{tikzpicture}'
edits += [
 [r'\margin{\textcircled{}}(iii)',circle('iii'),'The pen oval surrounds the typed iii itself. Replace the editorial empty margin circle by the actual combined mark.'],
 [r'\margin{\textcircled{}}(v)',circle('v'),'The pen oval surrounds the typed v itself; no independent empty circle occurs in the margin.'],
 [r'equivalences\inserted{(5)}',r'equivalences \inserted[typed]{(5)}','The interlinear (5) is typed and has a pen insertion curve; separate it from the preceding word.'],
 [r'\hand{likewise deduced from (4).}',r'\hand{likewise deduced from }\inserted{(4).}','The (4). is a separate pen insertion above from. The extra left curve is its placing mark, not another textual parenthesis.'],
 [r'$W_A^{-1}',r'$W_A^{\hand{-1}}','The first raised minus-one is penned above the localized category.'],
 ['is aspheric.','is a'+r'\over{\unsure{s}}{s}'+'pheric.','The s has a heavy pen retracing over a partly obscured typed letter.'],
 [r'\xout{quasi}\inserted[typed]{weak}equivalence,',r'\xout{quasi} \inserted[typed]{weak} equivalence,','Restore the word boundaries around the interlinear replacement weak.'],
 [r'\xout{quasi}\inserted[typed]{weak}equivalence in',r'\xout{quasi} \inserted[typed]{weak} equivalence in','The replacement weak is a separate word before equivalence.'],
 [r'\xout{quasi}\inserted[typed]{weak}equivalence.',r'\xout{quasi} \inserted[typed]{weak} equivalence.','The replacement weak is a separate word before equivalence.'],
 [r'transforms \xout{quasi}\inserted[typed]{weak}equivalences into \xout{quasi}\inserted[typed]{weak}equivalences',r'transforms \xout{quasi} \inserted[typed]{weak} equivalences into \xout{quasi} \inserted[typed]{weak} equivalences','Both replacement instances are separate words and require explicit boundary spaces.'],
 ['nition (more',r'n\over[typed]{\illegible{1}}{i}tion (more','The i is overtyped on a rounded older character that cannot be identified securely.'],
 ['(vii) The functor',r'(vii) T\over{h}{h}e functor','The h has a small pen retracing below the typed h.'],
 [r'type $C \hand{\to} e$',r'type $C \hand{\to} \over[typed]{e}{e}$','The target e has two heavy but distinguishable type impressions.'],
 [r'\diagram{\begin{tikzcd}[row sep=small, arrows=Rightarrow]',r'% Hand-drawn arrows are marked blue; typed objects remain plain.'+'\n'+r'\diagram{\begin{tikzcd}[row sep=small, arrows=Rightarrow]','The implication diagram consists of typed labels joined by handwritten double arrows.'],
 [r'\xout{\unsure{,}}',r'\xout{\unsure{;}}','The tall crossed punctuation has an upper component as well as a lower one, suggesting a semicolon rather than a comma; keep the reading uncertain.'],
 [r'\inserted{[3.30]}',r'\inserted{[\unsure{\S}.30]}','The brackets are square and 30 is clear. The leading section-like pen glyph remains uncertain rather than being silently identified by the witness.'],
 ['saying that (3)',r'\over[typed]{d}{s}\over[typed]{a}{a}ying that (3)','The s is typed over d, and the following a is overtyped by a displaced a.'],
 ['The only'+ '\n'+ 'equivalence',r'T\over{h}{h}e only'+'\n'+'equivalence','The h in The only is a long pen retracing over the typed h.'],
 [r'conditions\hand{.}',r'conditions\unsure{\over{,}{.}}','The reinforced punctuation still has a comma-like lower tail; retain uncertainty on the proposed comma-to-period correction.'],
 ['But it is so',r'B\over{u}{u}t it is so','The u has a pen retracing extending below its typed baseline.']
]
save_review({'key':key,'edits':edits,'diffs':{
 2902:[r'equivalences \inserted[typed]{(5)}, being','The scan has the inserted equation number alone, without in. It is typed interlinearly.'],
 2905:['is a weak equivalence.','The source ends equivalence without a plural s.'],
 2911:['(C in (Cat) as in (v)','The source visibly has as in.'],
 2913:[r'\inserted{[\unsure{\S}.30]}','The two brackets are square and the number 30 is legible. The leading glyph is section-like but remains doubtful on shape alone.','retain uncertainty']
 },'unsure':[[r'\unsure{;}','The crossed punctuation is too dark to settle; its height suggests a semicolon, not just a comma.']],
 'notes':[
 'Every implication-diagram arrow and all four square arrows are penned, as are the inline implication signs. Their provenance is now represented without colouring the typed objects.',
 'The insertion has square brackets and a clear 30. The leading section-like glyph remains doubtful.',
 'The pen ovals enclose the iii and v labels themselves. Both empty-circle margin placeholders have been replaced by graphic reconstructions.',
 'The equation reference (4). is inserted above from; the left sweep belongs to its placement curve. Do not duplicate it as another parenthesis.',
 'Overprinting or retracing has been recorded at the s of aspheric, the i in nition, the e target and the initial sa of saying. The older character in nition remains unreadable.',
 'The crossed sign after (v) has semicolon-like height, but its exact underlying punctuation remains doubtful.',
 'The mark after conditions is reinforced and still comma-shaped below; preserve uncertainty on the proposed full-stop correction.',
 'The h in item vii, the h in The only and the u in But have pen retracing strokes extending below the type line.',
 'Less is not deleted. The pen curve places the typed interlinear slightly before it.'
 ],'extra_records':[{'source_id':'OBS:ps_134-3_080:1','before':r'j_Ai_A(C) = A_{/j_A(C)}','after':r'j_Ai_A(C) = A_{/j_A(C)}','decision':'retain apparent authorial composition slip','reason':'The typescript visibly puts j_A before i_A here, although C is a category and the right side, together with the preceding counit, requires i_A j_A(C). Preserve the written order and flag it in the guide.','line':11}],
 'evidence':'Both original halves and thirteen enlarged details inspected. The two Roman labels are individually encircled, not accompanied by empty margin circles. The (5) insertion is typed; (4). is a separate handwritten insertion above from. All implication and square arrows are drawn in pen. Five weak replacements need visible word spacing. The lower reference has square brackets and number 30, with its leading section-like glyph retained as doubtful. The condition (v) literally has j_A i_A(C), an apparent composition-order slip preserved in source. The typed interlinear slightly does not delete less. The overprinted punctuation after (v), the older letter in nition, and the final comma/period correction remain uncertain. The final hand deletion runs from under through say, followed by live But it is so.'})
