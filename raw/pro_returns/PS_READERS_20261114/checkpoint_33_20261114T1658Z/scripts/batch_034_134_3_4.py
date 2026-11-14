import sys,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT,TEXT,occurrences
key='ps_134-3_034';s=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();u=occurrences(s,'unsure');ill=occurrences(s,'illegible');edits=[]
def e(a,b,r):edits.append([a,b,r])
for no in [6,10,14,18,19,21,27,31,35,38]:
 a=s.splitlines()[no-1];b=a.replace(r'\longrightarrow',r'\hand{\longrightarrow}').replace(r'\to',r'\hand{\to}').replace(r'\hat{}',r'\hand{\hat{}}')
 e(a,b,'The arrows and presheaf hats in this line are handwritten strokes above or between typed letters; formulas retain their source direction and punctuation.')
for word in ['model preserving','point',r'$M=$','cannot','any','right']:
 e('\\inserted{'+word+'}','\\inserted[typed]{'+word+'}','The interlinear '+word+' is typewritten, distinguished from its pen placement stroke.')
e(u[1][0],'ting','The old ending under the pen s and cancellation reads ting; the final g and intervening strokes remain visible.')
e(u[2][0],'and more','The machine-cancelled letters clearly read and more in the enlarged crop.')
e(r'in (\xout{xx})',r'in (**)','The two characters are typed asterisks naming the earlier formula; they are not a typewriter strikeout.')
e('automatic, whenever','automatic\\unsure{,} whenever','Heavy pen ink overlaps the comma after automatic; retain the punctuation with doubt about whether it was canceled.')
e(r'\margin{with a}',r'\margin{\diagram{\begin{tikzpicture}[baseline=(n.base)]\node[draw,ellipse,inner sep=3pt] (n) {with a};\end{tikzpicture}}}','With a is enclosed by an oval in the left margin; reconstruct that enclosure.')
e(r'``saturated\'\''.replace("\\'","'"),r'\uline{``saturated\'\'}'.replace("\\'","'"),'The scan underlines the quoted saturated, omitted from the supplied markup.')
a=s.splitlines()[46];b=a.replace(r'\ar[',r'\ar[color=blue, ')
e(a,'% Hand-drawn arrows are marked blue; typed objects remain plain.\n'+b,'Both adjunction arrows are hand drawn between typed M and M prime; the i and j labels are handwritten.')
conf=dict(key=key,edits=edits,diffs={
2032:['which allow to construct','The typed phrase contains no us after allow.'],
2033:[r'just as good \inserted{one} as the other\deleted{s}','One is handwritten above the line and the terminal s of others is struck.'],
2039:[r'\inserted[typed]{model preserving}','Model preserving is typed above embeddings.','correct provenance'],
2041:[r'Another\inserted[typed]{point}','The relocated point is typed above Another; its old occurrence is cancelled.','correct provenance'],
2044:['semi-simplicial structures or simplicial structures','The connecting word is or, with a rounded o; the witness of is not the source.'],
2049:['A somewhat ambitious question','No more is typed or inserted here.'],
2050:[r'\inserted[typed]{$M=$}','M equals is typewritten in the interlinear space.','correct provenance'],
2051:[r'\inserted[typed]{cannot}','Cannot is typed over the cancelled group.','correct provenance'],
2052:[r'\inserted[typed]{any}','Any is typed above the beginning of the following line.','correct provenance'],
2054:[r'$M/_{b}$','The slash of the second induced-topos expression remains on the main line with b lowered; do not silently regularize its placement.'],
2056:[r'\inserted[typed]{right}','Right is typed above adjoint.','correct provenance'],
2057:[r'(cf. \deleted{\illegible{1}} \inserted{section 28)}','The new handwritten reference clearly says section28; the older crossed reference remains unread.'],
2058:[r'\inserted{whenever} this functor admit\over{ting}{s}','The ending ting is readable beneath the correction to s.','correct transcription'],
2061:[r'\deleted{with two} \inserted{with a} \uline{``saturated\'\'} \deleted{sets}'.replace("\\'","'"),'With two and sets are canceled, with a is inserted and also circled in the margin, and saturated is underlined.','correct transcription']},
unsure=[[u[0][0],'The first word above is recognizable, but diagonal strikes prevent a secure recovery of the remainder of the old reference.'],['ting','The ending reads ting under the handwritten s and subsequent strokes.'],['and more','Every letter remains legible under the typewriter x row.']],
illegible=[[ill[0][0],'The old item before A-hat is densely scribbled out; no secure formula can be recovered.'],[ill[1][0],'The canceled reference begins with a p-like form but its numbers are too obscured to settle; retain the illegibility.']],
notes=['The scribbled group before A-hat was enlarged; no reliable reading is available.','The typed period and handwritten call31 followed by a dot remain as given; the scan shows the call adjacent to that earlier period.','The o in Pro(Hot) is overtyped but its live reading is clear.','The reference after i_A is (**), two typewritten asterisks, now corrected from xout markup.','The heavy pen mark overlaps the comma after automatic; uncertainty is now marked rather than deciding deletion.','The gap within set-theoretical is closed by a pen joining mark; the supplied joined word gives the live reading.','The old ending ting and handwritten replacement s are resolved on the enlargement.','The small isolated left-margin marks provide no readable words; the separately circled with a is reconstructed.'],
evidence='Both halves inspected, including enlarged upper canceled item, old section reference, p-reference, admits ending and and more. The arrows and hats are hand additions. Typed insertions are model preserving, point, M=, cannot, any and right; one, namely, general, whenever and with a are handwritten. The old admits ending ting and cancelled and more resolve; the two other crossed references/items remain uncertain or illegible. The formula call is typed (**), not cancelled xx. The source says allow to construct, structures or simplicial structures, and somewhat ambitious without the witness additions. The second slice slash stays at baseline before the lowered b. A comma after automatic has uncertain cancellation. The quoted saturated has a manuscript underline, and the margin with a is enclosed in an oval. Both adjunction arrows are drawn by hand.')
(OUT/'review_notes'/f'{key}.json').write_text(json.dumps(conf,ensure_ascii=False,indent=2));save_review(conf)
