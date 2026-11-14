import sys,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT,TEXT,occurrences
key='ps_134-3_029';s=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();u=occurrences(s,'unsure');ill=occurrences(s,'illegible');edits=[]
def e(a,b,r):edits.append([a,b,r])
e(r'\mspage{29}',r'\mspage{\hand{29}}','The page number is pencil handwriting.')
e(r'2\over{\unsure{4}}{7}.',r'\hand{2}\over{\unsure{4}}{7}.','The leading 2 of the renumbered section is also handwritten; the old figure under 7 stays uncertain.')
for no in [7,8,13,16,18,19,23,43]:
 a=s.splitlines()[no-1];b=a.replace(r'\to',r'\hand{\to}').replace(r'\mapsto',r'\hand{\mapsto}')
 e(a,b,'The scan has handwritten arrows on this line between typed formula letters; the bars of the realization were already marked as pen.')
for word in ['a','localization','(or topologic)','left','between']:
 e('\\inserted{'+word+'}','\\inserted[typed]{'+word+'}','The interlinear '+word+' has typewriter letterforms and spacing; the associated insertion stroke is pen.')
# Labels are typewriter asterisks, not handwritten replacements of x.
e(r'(\over{x}{$*$}) \qquad',r'(*) \qquad','The displayed label uses a typed asterisk; no pen replacement of x is distinguishable.')
e(r'(\over{x}{$*$}), namely',r'(*), namely','The repeated label is a typed asterisk in parentheses.')
e(r'(\over{xx}{$**$}) \qquad',r'(**) \qquad','Both asterisks in the second label are typed; the source falsely made them handwritten over xx.')
e(r'$\underline{B}_{\infty}$',r'$\underline{B}_{\mathrm{oo}}$','The subscript is two separately typed round o forms, consistent with the literal notation on p21; it is not a joined infinity glyph.')
e(r'an $\infty$-graph',r'an $\mathrm{oo}$-graph','The typescript writes two adjacent round o forms in the graph designation; preserve that printing.')
# A typed x crosses out the first quote, rather than a new quotation mark added by hand.
e(r'``primitive\hand{\'\'}'.replace("\\'","'"),r'``primitive\xout{\'\'}'.replace("\\'","'"),'The upper-right mark after primitive is an x cancellation at the earlier closing quotation; the live closing quote follows structure on the next line.')
conf=dict(key=key,edits=edits,diffs={
1930:['is that a suitable','The typed verb reads is, whereas the witness it is an error; the inserted a is typed.'],
1931:[r'\inserted[typed]{a}','The interlinear a is a typewriter character above the placement stroke.','correct provenance'],
1932:[r'\inserted[typed]{localization}','Localization is a typewritten interlinear addition.','correct provenance'],
1935:[r'\inserted[typed]{(or topologic)}','The insertion reads topologic, without al; its letters are typewritten rather than cursive.','correct provenance'],
1936:[r'\hand{$^{(28)}$}','Only the penned call28 appears after functor; no text of the long witness note is on this page.'],
1938:[r'\inserted[typed]{left}','Left is typed over the line, with a pen insertion curve.','correct provenance'],
1940:[r'the \hand{``}\uline{test topologies}\hand{\'\'}'.replace("\\'","'"),'Both handwritten quotation marks and the underline are visible; preserve them.'],
1942:[r'\deleted{of} \inserted[typed]{between}','Of is crossed out and between is typed immediately above it.','correct provenance']},
unsure=[[u[0][0],'The tiny word at the extreme upper-right edge resembles on or or; its final stroke is insufficiently clear.'],[u[1][0],'Heavy pen retouching of 27 covers the earlier second digit; the possible4 remains doubtful.'],[u[2][0],'The enlarged word shows an overtyped t/h at the disputed position; the visible trace does not settle the two supplied readings.']],
illegible=[[ill[0][0],'The cancelled four-letter group after B_oo has a visible b-like upright but overlapping x strokes prevent a secure whole-word recovery.'],[ill[1][0],'Pen of overlaps an earlier typed group; the old letters cannot be confidently separated from the new ones.']],
notes=['The clipped upper-right note remains or/on uncertain.','The renumbered 27 is handwriting; its underfigure remains doubtful.','The strengthened/strenghhened overstrike was enlarged and remains ambiguous.','The cancelled word after B_oo was enlarged; x strokes prevent secure recovery.','The overwritten group beneath of was enlarged; retain illegibility for the old text.','All arrows in the page formulas are visibly hand drawn and now marked; realization bars were already correctly marked.'],
evidence='Both complete halves inspected, with enlarged crops of the section number, strength-word overstrike, cancelled group after B_oo and old letters beneath of. The page number is pencil; section27 is written over an uncertain older digit. The top edge note remains or/on doubtful. Main prose clearly says is that and topologic; a, localization, (or topologic), left and between are typed interlinear additions, whereas may and now are cursive. All formula arrows are handwritten; display labels are typed asterisks rather than hand substitutions. The primitive closing quotation on the upper line is x-cancelled, leaving the live quote after structure. Two round typed o characters are preserved in the core subscript and oo-graph notation. The call28 is present without the witness footnote. The two old crossed/overwritten words remain illegible.')
(OUT/'review_notes'/f'{key}.json').write_text(json.dumps(conf,ensure_ascii=False,indent=2));save_review(conf)
