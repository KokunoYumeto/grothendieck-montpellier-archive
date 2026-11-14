import json,sys
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT

def commit(c):
 (OUT/'review_notes'/f"{c['key']}.json").write_text(json.dumps(c,ensure_ascii=False,indent=2))
 if c['key']=='ps_134-3_038':
  c['extra_records']=[{'source_id': 'MECH:ps_134-3_038:1', 'before': '\\margin{\\diagram{\\begin{tikzpicture}\\draw (0,0)--(0,1.1);\\draw (.06,0)--(.06,1.1);\\end{tikzpicture}}', 'after': '\\margin{\\diagram{\\begin{tikzpicture}\\draw (0,0)--(0,1.1);\\draw (.06,0)--(.06,1.1);\\end{tikzpicture}}}', 'reason': 'Close both the diagram and margin macros after the TikZ environment; the missing closing brace was identified by the reader build.', 'line': 17}]
 save_review(c)

commit(dict(key='ps_134-3_037',edits=[
 [r'K($\pi$,1)',r'K(\hand{$\pi$},1)','The pi is drawn in heavy pen; K, comma and numeral remain typed.'],
 [r'b\unsure{o}th','both','The circular live o is visible under a small overstrike.'],
 [r'\inserted{closed}',r'\inserted[typed]{closed}','The interlinear word has the same monospaced typewriter forms as the base line; its curved pen stroke places it before model.'],
 [r'\over{\unsure{If}}{I}',r'\over{If}{I}','The typed I and f remain recognizable beneath the pen correction.'],
 [r'natural \xout{\illegible{1}}',r'natural \xout{g\unsure{ene}}','The cancelled fragment begins with a clear g; three following overstruck letters plausibly read ene but remain doubtful.'],
 [r'\unsure{in|fn}','in','The live typed reading is in, with an overprint on i.'],
 [r'can \unsure{be}','can be','The overtyped b and following e are legible as be.'],
 [r'likewise \unsure{by}','likewise by','The live b and y are legible beneath the typewriter correction.'],
 [r'\unsure{it|ft} commutes','it commutes','The corrected first character is i, followed by t.'],
 [r'same symbol \hand{$\hat{\ }$}f :',r'same symbol f :','There is no hat over this inline f: the lower pen caret belongs to the display f on the next line.']
],diffs={
2092:['for a category C','The line after the horns has a single C and no b prefix.'],
2094:['a to c, with b below and b to c','The second hand-drawn horn places b below the a-to-c segment; the existing diagram topology and vertical placement agree.'],
2096:[r'\inserted[typed]{closed}','The upper word is typed, with a handwritten placement curve; it is not cursive.','correct layer attribution'],
2106:['same symbol f :','The proposed inline hat is absent. The visible caret is lower and belongs to the displayed f, as its alignment with the other displayed carets confirms.','correct transcription']
},unsure=[
[r'\unsure{(}','A heavily crossed single mark follows spaces; the underlying opening parenthesis remains possible but cannot be established.'],
['o','The live round o is legible in both.'],
[r'\unsure{ry}','The rightmost letters are clipped and partly retraced at the scan boundary, so the existing completion remains doubtful.'],
['If','Both original typed letters can be distinguished in the enlarged crop.'],
['in','The live reading is in despite the overprint.'],
['be','Both letters of be are visible.'],
['by','The live letters read by.'],
[r"\unsure{X'}",'The dense pen cancellation hides the alleged X-prime; retain the supplied doubtful reading.'],
['it','The live i and t are visible.'],
[r'\unsure{(}','The overwritten initial character of between is not separable from the correcting pen stroke; retain the uncertainty.'],
[r"\unsure{'}",'A small heavy cancellation follows the final C; a prime is plausible but its underlying form is not recoverable.']
],illegible=[
[r'g\unsure{ene}','The first cancelled g is clear; the remaining three letter forms are only tentatively ene.'],
[r'\illegible{1}','A typewriter cancellation immediately after localizing obscures the old character, possibly quotation punctuation.'],
[r'\illegible{1}','The short cancelled group before E,F remains too heavily overprinted for a defensible reading.']
],notes=[
'The vowel in both is a legible o under overtyping; doubt removed.',
'Closed is interlinear typing, with a placing curve rather than deletion of model. The category ending remains doubtful at the cropped edge; no missing hyphen after spe is invented.',
'The underlying If is readable in the crop; the correcting I remains handwritten.',
'In, it, be and by are the visible live readings; the overlapping typed forms do not justify retaining alternative live words.',
'The first g of the cancelled natural-fragment is recovered, its remainder is tentative. The localizing, sheaves and X-prime cancellations remain unresolved.',
'The exclamation marks in f-sub-bang are pen strokes with detached dots, consistently retained as handwriting.',
'The final C has a heavy cancelled small mark, possibly a prime; doubt is retained. The inline f above has no hat.'
],evidence='Both supplied halves inspected, plus enlarged crops of the cancelled parenthesis, edge category ending, If, natural-fragment, localizing, sheaves, X-prime, between and final prime. The upper hand horns have b above in the first and below in the second; Delta is penned beside a typed subscript 2. Pi is handwritten. Closed is typed above model, placed by a curve. The lower discussion keeps the typed x in the fiber product, slashed-o map notation, the apostrophe in one\'s, and the unmatched opening parenthesis in the by (X\'= insertion. In the last two lines the inline f is plain; the three hats belong to the lower display. Clipped or heavily cancelled characters remain explicitly doubtful.'))

commit(dict(key='ps_134-3_038',edits=[
 [r'\mspage{38}',r'\mspage{\hand{38}}','The folio number is handwritten.'],
 [r'crite\unsure{r}',r'crite\xout{r}','The terminal r is visibly crossed with a typewriter x at the right edge.'],
 [r"\[ \hat{C'}_{/a} \hand{\cong} (C'_{/a})^{\wedge} \hand{\to} \hat{C}_{/a} \simeq (C_{/a})^{\wedge} \]",r"\[ \overset{\hand{\wedge}}{C'}_{/a} \hand{\cong} (C'_{/a})^{\hand{\wedge}} \hand{\to} \overset{\hand{\wedge}}{C}_{/a} \hand{\simeq} (C_{/a})^{\hand{\wedge}} \]",'The carets, connecting arrow and both isomorphism signs in this display are penned; the category symbols and slice indices are typed.'],
 [r'\margin{||}',r'\margin{\diagram{\begin{tikzpicture}\draw (0,0)--(0,1.1);\draw (.06,0)--(.06,1.1);\end{tikzpicture}}}','Reconstruct the paired long margin strokes beside the two-line criterion rather than printing two short text bars.'],
 [r'come back to a \xout{\illegible{1}}',r'come back to a \xout{would}','The enlarged cancellation shows the five typed letters would beneath x-overstrikes.'],
 [r'O\unsure{\over{m}{n}}e',r'O\over{n}{n}e','The original type is a one-humped n, with another n drawn immediately below it; the m conjecture is not supported.'],
 [r'the \unsure{c}ategory','the category','The live opening c is visible despite its overprint.'],
 [r'$i_Aj_A(B)_{/b}$ \xout{\illegible{1}}',r'$i_Aj_A(B)_{/b}$ \xout{over}','The four cancelled letters read over, followed by the surviving second over.'],
 [r'\mathrm{Hom}(\underset{\hand{\wedge}}{A}_{/a},B)) \in',r'\mathrm{Hom}(\underset{\hand{\wedge}}{A}_{/a},B)) \hand{\in}','The membership sign at the right of this display is handwritten.'],
 [r'\inserted{aspheric}',r'\inserted[typed]{aspheric}','The replacement aspheric above the cancelled line is typed; its placement arc is penned.'],
 [r'\unsure{\xout{a}|a} sense','a sense','The a is plainly typed and has no cancelling x or pen stroke.'],
 [r'theo\unsure{r}-',r'theo\xout{r}-','The terminal r is crossed with a typewriter x; the next line starts ry.'],
 [r'\over{\illegible{2}}{at least}',r'\over{\unsure{in the base}}{at least}','The old type includes a recognizable final base; the whole likely phrase remains uncertain under the pen replacement.']
],diffs={
2111:[r'(C_{/a})^{\hand{\wedge}}','The complete slice is parenthesized before the caret; the slash-a is a subscript to C.'],
2114:['[small] category B','The interlinear hand addition has square brackets; the curve below is its placement mark.'],
2115:['For a [small] category A','The handwritten brackets are square in this second insertion too.'],
2118:['for any [small] category B','The right-margin small addition is present and bracketed, with a placement curve leading after any.'],
2119:['aspheric for any [small] category B','The same bracketed addition is visibly inserted before category in (ii).'],
2120:[r'is \deleted{an} \inserted[typed]{aspheric} \deleted{\xout{aspheric}} element','The old an and lower aspheric are cancelled; the upper replacement is typed.','retain deletion; correct insertion provenance'],
2121:[r'\inserted[typed]{aspheric}','Its evenly spaced typewriter letters match the surrounding typescript, unlike the placement stroke.','correct layer attribution'],
2126:['insure','The last paragraph distinctly types insure, not ensure.'],
2127:[r'\margin{$\times$}','A light pencil cross stands to the left of that much, using.'],
2128:['two long parallel vertical margin strokes','The mark extends beside both lines of the asphericity criterion; it has been reconstructed graphically.','reconstruct graphic']
},unsure=[
[r'\xout{r}','The enlarged end of line has an x over the terminal r.'],
[r'\unsure{t}','The first next-line letter has overlapping stems and crossbar. It resembles t but may conceal a correction to r; leave the literal doubtful character.'],
[r'\over{n}{n}','The typewriter base reads n, with a pen n immediately below; the proposed m has no second hump.'],
['c','The live open c is legible beneath a small overstrike.'],
['a','No cancellation crosses this a.'],
[r'\xout{r}','The end of theor- is visibly crossed; ry begins the following line.']
],illegible=[
['would','The sequence w-o-u-l-d is visible through the row of cancelling x characters.'],
['over','The cancelled old over is immediately followed by a freshly typed over.'],
[r'\unsure{in the base}','In and final base have partial visible support, but the intervening typing is obscured by at least; the phrase remains doubtful.']
],notes=[
'The right-edge r is machine-cancelled. The initial character of the next line remains doubtful because of overlapping t/r strokes.',
'The underlying letter is a one-humped typed n; the pen n below is retained as a correction/retracing.',
'The live c in category is readable and its doubt removed.',
'The small pen caret really lies below the A in Hom(A/a,B); its position and uncertainty of meaning are preserved, not moved above A by mathematical expectation.',
'The a in at all a sense is unstruck and retained.',
'The old phrase under at least is tentatively in the base; it remains explicitly unsure.',
'Have has a pen v over the old typed d. The terminal r of theor- is machine-cancelled before next-line ry.',
'Carets, arrows, congruence signs and the display membership sign are pen additions. The upper replacement aspheric is typed.'
],evidence='Both halves inspected with enlarged crops of the criterion line ending and continuation, would, One, cancelled over, at least and theor-. The first display places hats after full parenthesized slice categories; its mathematical connectors and hats are penned. The criterion is accompanied by paired vertical strokes. Four [small] insertions are handwritten and square-bracketed. In (i) the n of an is cancelled before weak; in the later prose the old an/aspheric line is cancelled and aspheric retyped above. The unusual caret under A in Hom is visibly below the letter and is retained there. The live a in at all a sense is plain. The source says insure and that B is a test category, both preserved.'))
