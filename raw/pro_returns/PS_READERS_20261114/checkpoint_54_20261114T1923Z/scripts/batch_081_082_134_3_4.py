import sys,re
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT
key='ps_134-3_081';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'A\hand{$\hat{}$}',r'$A^{\hand{\wedge}}$ ').replace(r'A\^{}',r'$A^{\hand{\wedge}}$')
 if new!=line:edits.append([line,new,'Replace empty hat accents by the raised pen carets actually drawn on A; preserve the following word boundary.'])
edits += [
 [r'insp\xout{i}iring',r'insp\xout{\unsure{i}}iring','The crossed cell before iring is not cleanly separable; retain the earlier proposed i as doubtful.'],
 [r"assumption'',\xout{xx}",r"assumption'',\xout{th}",'The two cancelled letters are t and h, still readable under their x strikes.'],
 [r'\inserted{in (5)}',r'\inserted[typed]{in (5)}','In (5) is typed above the line; the placing curve is pen.'],
 [r'\xout{noxxthxx}',r'\xout{\unsure{nothing}}','The lower typed word retains no and th, but its remaining cells are obscured; nothing is retained as a doubtful partial recovery.'],
 [r'aspheric,\xout{xxxxxxx}',r'aspheric,\xout{\illegible{7}}','The cancellation contains earlier letter remnants, not seven literal x characters; they cannot be securely recovered.'],
 [r'\inserted{\unsure{(98)}}',r'\inserted{\over{\unsure{(*)}}{(48)}}','The final pen call is (48). Its covered earlier asterisk-like call remains uncertain.'],
 [r'\inserted{\unsure{(99)}}',r' \inserted{\over{\unsure{(**)}}{(49)}}','The final pen call reads (49); the older double-asterisk call is too covered to settle. Keep a space after plus.'],
 [r'\hand{(98)}',r'\hand{(48)}','The first margin numeral is 48, with an open angular 4, not 98.'],
 [r'\hand{(99)}',r'\hand{(49)}','The second margin numeral is 49, again beginning with the same open 4.'],
 [r'did\unsure{nt|n\'t}',r"didn\hand{'}t",'The apostrophe is a clear curved pen stroke above the n; the underlying typing has none.'],
 [r'\deleted{\unsure{(***)}}',r'\deleted{(***)}','The final call 50 is clear, and three old stars survive within the heavily crossed preceding call.'],
 [r'\deleted{\illegible{3}}',r'\deleted{cf p.\unsure{88 remark 3.}}','The lower cancelled marginal reference begins cf p.; the continuation plausibly reads 88 remark 3., with uncertainty retained on the covered details.'],
 [r'\xout{xxxxxxxx}',r'\xout{using \unsure{$i_A$}}','Using is legible beneath the x row. The final overprinted symbol has a lower A and is plausibly i_A, but its upper letter remains doubtful.'],
 [r'\inserted{\deleted{\unsure{Weak}}}',r'\inserted{\deleted{\uline{Weak}}}','The crossed insertion before Test reads Weak and retains its pen underline.'],
 [r'\uline{Test categories}\inserted',r'\uline{Test categories} \inserted','The inserted heading continuation consists of separate words and requires a boundary space.'],
 [r'T\unsure{\over{h}{h}}en',r'T\over[typed]{h}{h}en','The tall h has displaced typewriter impressions; its letter and typed provenance are clear.']
]
# The marginal calls are additionally enclosed by later pencil ovals. Broad
# pencil hatching also crosses both notes; preserve the notes under doubt.
for n in (48,49):
 line=next(l for l in src.splitlines() if l.startswith(r'\margin{\hand{('+str(n+50)+')}'))
 current=line.replace(str(n+50),str(n))
 content=current[len(r'\margin{'):-1]
 call=r'\hand{('+str(n)+')}'
 oval=r'\begin{tikzpicture}[baseline=(n.base)]\node[inner sep=0pt] (n) {('+str(n)+r')};\draw[color=blue,line width=.35pt] (n.center) ellipse [x radius=1.35em,y radius=.95em];\end{tikzpicture}'
 content=content.replace(call,oval)
 edits.append([current,r'\margin{\unsure{'+content+'}}','The margin label is enclosed in a pencil oval. Several broad parallel pencil strokes cross the note; their cancellation function is uncertain, so retain its complete text under doubt.'])
# Apostrophe-bearing source is represented without an accidental raw-string escape.
edits=[[a.replace("\\'","'"),b.replace("\\'","'"),c] for a,b,c in edits]
save_review({'key':key,'edits':edits,'diffs':{
 2921:[r"(48) * 27.3. But this is true for any equivalence of categories -- I'm really being very dull!",'The note is legible, dated 27.3 and called 48. Pencil hatching crosses it, so its cancellation status remains uncertain.'],
 2923:['(49) ** The "plus" is unnecessary visibly, see note above.','The note reads this and is called 49. Its full content is retained under uncertainty because of the broad pencil strokes.'],
 2924:['attractive in this condition','The typed demonstrative is this, not the.'],
 2929:['In fact','The rotated margin begins In fact with a clear n.'],
 2930:['whereas','Whereas is typed in full before (iii).']
 },'unsure':[
 [r'\over{\unsure{(*)}}{(48)}','The final 48 is readable; the old asterisk call remains doubtful.'],
 [r'\over{\unsure{(**)}}{(49)}','The final 49 is readable; the earlier call remains partly covered.'],
 [r"n\hand{'}t",'The apostrophe is handwritten over the typing, which reads didnt.'],
 ['(***)','Three earlier asterisks are visible in the crossed call before 50.'],
 [r'\unsure{not $i_A$}','The added not-i_A phrase is crowded against other letters; the proposed reading remains uncertain.'],
 [r'\uline{Weak}','The heavily inked insertion is nevertheless readable as Weak, with its underline.'],
 [r'\over[typed]{h}{h}','The layered h is typed overprinting and can be identified.']
 ],'illegible':[
 [r'\illegible{1}','The first heavily blackened word after the star in the rotated lower note cannot be recovered securely.'],
 [r'cf p.\unsure{88 remark 3.}','The reference prefix cf p. is legible; the remaining page and remark details stay qualified.']
 ],'notes':[
 'The cancelled cell in inspiring remains doubtful; the next crossed pair reads th. The final autoequivalen cancellation is clipped at the right border.',
 'The final call numbers are 48 and 49, matching their visible margin labels. Earlier star calls remain uncertain under the ink.',
 'The new call is (50), preceded by a pen-cancelled (***) call.',
 'Both original halves, rotated margin crops and an enlarged lower-note detail were used. The lower note reads In fact and the main model-preserving assertion. Not i_A and the first crossed word remain doubtful; a later cancelled cf p. reference is partly recovered.',
 'The heading insertion is the underlined word Weak, cancelled by pen.',
 'The final two conditions are enclosed together and crossed diagonally throughout. Both remain fully cancelled.'
 ],'evidence':'Both original halves, eight detail crops, two rotated margin crops and a further enlargement of the lower note inspected. The final calls are 48, 49 and 50. Notes 48 and 49 are legible, but broad parallel pencil hatching crosses both and their oval call labels, so the text is retained under uncertainty rather than deleted. The dated 27.3 note observes that any equivalence preserves a final object; the second removes the extra plus. In (5) is a typed insertion. Didnt receives a pen apostrophe, whereas dont remains without one. The old using phrase is partly recovered, and Weak in heading b is securely readable and cancelled. The lower model-preserving note retains uncertainty on not i_A, its first blackened word, and the exact cancelled cf p. reference. The final boxed i/ii block is wholly cancelled.'})

key='ps_134-3_082';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'^\wedge',r'^{\hand{\wedge}}').replace(r')\hat{}',r')^{\hand{\wedge}}').replace(r'\emptyset',r'\hand{\emptyset}')
 new=re.sub(r'\\arrow\[([^\]]*)\]',lambda m:r'\arrow['+m.group(1)+',color=blue]',new)
 if new!=line:edits.append([line,new,'The presheaf carets, empty-set signs and diagram arrows are penned; typed diagram labels remain plain.'])
edits += [
 [r'T\xout{H}here',r'T\over[typed]{H}{h}ere','The capital H and lower h occupy one overprinted type cell. It is not a separate deleted letter followed by a new cell.'],
 [r'\xout{ix} I',r'\xout{in} I','The cancelled first word reads in beneath the x strikes.'],
 [r'\xout{xxx}',r'\xout{\illegible{3}}','The old three-cell group after the first endpoint has residual letter curves, but is not recoverable securely as a word.'],
 [r'over \unsure{e}',r'over \over{e}{e}','The e is reinforced in pen over type, not cancelled.'],
 [r'e_o,e_{\hand{1}}',r'e_o,\over[typed]{e}{e}_{\over[typed]{1}{1}}','The second e and its index 1 are vertically doubled typewriter impressions, not a handwritten index.'],
 [r'\unsure{in}',r'\over[typed]{o}{i}\over[typed]{n}{n}\hand{\unsure{,}}','The first cell has typed i over o and the n is repeated. A separate small pen comma-like blot follows; its identity remains doubtful.'],
 [r'\xout{\illegible{1}}',r'\xout{where the}','The lower-left cancelled words read where the, with their ascenders and word space visible.'],
 [r'\hand{i}_A j_A(C)',r'\over{i}{i}_A j_A(C)','The first i is a pen retracing over a visible typed i.'],
 [r'\unsure{even}',r'\over{\unsure{even}}{even}','The final even is clear, but several pen retracings cover parts of the lower typed word. Retain uncertainty on that lower layer.'],
 [r'\hand{)}\uline{aspheric}',r'\hand{)} \uline{aspheric}','Keep the visible separation after the added parenthesis.'],
 [r'\diagram{\begin{tikzcd}',r'% Hand-drawn arrows are marked blue; typed objects remain plain.'+'\n'+r'\diagram{\begin{tikzcd}','The implication arrows are hand drawn.'],
 [r'\unsure{\xout{,}}',r'\deleted{\unsure{,}}','The small dark cancellation is made with pen strokes, not typewriter x impressions. The underlying comma remains uncertain.'],
 [r'\unsure{two}',r'\over{\unsure{o}}{t}\over[typed]{w}{w}o','The final t is penned over a rounded older mark; the w has repeated typed impressions. The old first letter remains doubtful.'],
 [r'O\xout{N}ne',r'O\over[typed]{N}{n}e','The capital N and lower n occupy the same type cell, as in There above.'],
 [r'\hand{,}with C',r'\hand{,} with C','The word with is visibly separated after the added comma.']
]
save_review({'key':key,'edits':edits,'diffs':{
 2933:[r'over \over{e}{e}','The word is over, and the e is retraced rather than struck out.'],
 2938:[r'A^{\hand{\wedge}} \hand{\approx}','The sign consists of two wavy strokes, with no straight baseline.'],
 2939:[r"\hand{``}homotopy interval\hand{''}",'Both opening and closing quotation marks are handwritten and retained.'],
 2942:[r'\deleted{with} \inserted{to}','With is struck in pen and to is inserted above it.'],
 2946:['to see that','The source reads to at the right edge before the next-line see that.']
 },'unsure':[
 [r'\unsure{es}','The terminal cells are crowded against the clipped right border; retain the existing uncertainty.'],
 [r'\over{e}{e}','The final e is visible in pen over its typed form.'],
 [r'\over[typed]{o}{i}\over[typed]{n}{n}\hand{\unsure{,}}','The final in is readable, while the separate trailing pen blot remains doubtful.'],
 [r'\over{\unsure{even}}{even}','The pen word reads even; its covered lower layer remains uncertain.'],
 [r'\deleted{\unsure{,}}','The cancellation is pen, and its underlying punctuation is still uncertain.'],
 [r'\over{\unsure{o}}{t}\over[typed]{w}{w}o','The final word is two; the earlier rounded first character remains doubtful.']
 ],'illegible':[['where the','The lower-left x row leaves the letters and space legible.']],
 'notes':[
 'The final es of categories remains partly clipped and overprinted at the right edge.',
 'There contains a typed H-to-h overprint in one cell; the endpoint e is pen-retraced, not deleted.',
 'The final in is typed i over o followed by a repeated n; a small doubtful pen comma-like mark follows.',
 'The cancelled lower-left words are where the.',
 'The mark to the right of the diagram is a pen cancellation above a separate typed comma. Its underlying punctuation remains doubtful.',
 'The final word is two, with a pen t over an uncertain rounded old character and a repeated typed w.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-3_082:1','before':'if A  has a final element','after':'if A  has a final element','decision':'retain apparent authorial hypothesis slip','reason':'After replacing A by A/F with F aspheric, the resulting category is known to be aspheric, not to have a final object. The displayed proof reduction states the stronger final-object condition; preserve it and explain the missing generality in the guide.','line':43},
 {'source_id':'OBS:ps_134-3_082:2','before':r'in same \S.31','after':r'in same \S.31','decision':'retain apparent authorial cross-reference slip','reason':'The handwritten final digit is 1, while the preceding reference is section 37. The literal same section 31 is preserved; section 37 contains the key result being invoked.','line':50}
 ],'evidence':'Both original halves and thirteen enlarged details inspected. There and One have uppercase-to-lowercase overprints in the same cell, not extra cancelled characters. The endpoint e is penned over type; the second e and its index 1 are doubled typing. The lower-left cancelled words read where the. Every presheaf caret, empty-set symbol and implication arrow is penned. The final even and two are readable but their covered layers remain partly doubtful. The diagram has a pen cancellation above its typed comma. The final handwritten reference visibly reads in same section 31, in contrast to the preceding section 37. The proof also literally changes the needed asphericity conclusion into A having a final element; both apparent source slips are preserved and separately recorded.'})
