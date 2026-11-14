import json,sys
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT,TEXT

def commit(c):
 (OUT/'review_notes'/f"{c['key']}.json").write_text(json.dumps(c,ensure_ascii=False,indent=2))
 save_review(c)

def line_edits(key,repls):
 s=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();out=[]
 for n,l in enumerate(s.splitlines(),1):
  after=l
  for a,b in repls:after=after.replace(a,b)
  if after!=l:out.append([l,after,f'At source line {n}, the scan shows the specified mathematical connectors/carets in pen while the accompanying object letters and indices are typed.'])
 return out

key='ps_134-3_039'
edits=line_edits(key,[(r'$a,b \in',r'$a,b \hand{\in}'),(r'\hat{A}',r'\overset{\hand{\wedge}}{A}'),(r'A^\wedge',r'A^{\hand{\wedge}}'),(r'F $\rightrightarrows$ G',r'F $\hand{\rightrightarrows}$ G')])
edits += [
 [r'\margin{\unsure{cf théorème p 46}}',r'\margin{cf théorème p 46}','The slanting top-left marginal reference is legible as cf théorème p 46.'],
 [r'\over{)}{\unsure{)}}',r'\over{)}{)}','The label has a typed closing parenthesis retraced and extended in pen.'],
 [r'\unsure{i.e.} for any','i.e. for any','The note begins i.e., followed by for any, not every.'],
 [r'\unsure{In view of}',r'In view of','The rotated note makes In view of legible.'],
 [r'\unsure{T1 $\to$ T2}',r'\unsure{T1 et T2}','The connector between T1 and T2 is not a clear right-pointing arrow; it resembles the short handwritten conjunction et, retained as a doubtful reading.'],
 [r'\unsure{is} aspheric','is aspheric','The second line clearly starts is aspheric in the rotated crop.'],
 [r'\hand{\emptyset}_{A^\wedge}',r'\emptyset_{A^{\hand{\wedge}}}','The empty-element sign is a thin typed slashed o; the small caret on the subscript A is penned.'],
 [r'\inserted{which}',r'\inserted[typed]{which}','The word which is typed above the line, with a pen insertion curve.'],
 [r'\inserted{h} between',r'\inserted[typed]{h} between','The inserted h has the same typewriter shape as the body h and is placed by a pen curve.'],
]
# The preceding caret substitution has already marked the subscript A.
edits=[([r'\hand{\emptyset}_{A^{\hand{\wedge}}}',r'\emptyset_{A^{\hand{\wedge}}}',x[2]] if x[0]==r'\hand{\emptyset}_{A^\wedge}' else x) for x in edits]
edits += [
 ['\\begin{tikzcd}\n & F \\times I \\ar[dd, dashed, "\\hand{h}"\'] & \\\\\nF \\simeq F \\times e_o \\ar[ur] \\ar[dr, "f_o"\'] & & F \\simeq F \\times e_1 \\ar[ul, bend right] \\ar[dl, "f_1"] \\\\\n & G &',
 '% Hand-drawn arrows are marked blue; typed objects remain plain.\n\\begin{tikzcd}\n & F \\mathrm{x} I \\ar[dd, dashed, color=blue, "\\hand{h}"\'] & \\\\\nF \\hand{\\simeq} F \\mathrm{x} e_o \\ar[ur, hook, color=blue] \\ar[dr, color=blue, "f_o"\'] & & F \\hand{\\simeq} F \\mathrm{x} e_1 \\ar[ul, hook, color=blue] \\ar[dl, color=blue, "f_1"] \\\\\n & G &',
 'Both upper arrows have actual recurved hook tails in the enlarged diagram. All five arrows and both isomorphism signs are penned; products use typed x. Typed object and f labels remain plain.'],
 [r"\unsure{\deleted{''}}",r"\unsure{\xout{''}}",'The quote-like mark after saturation is overstruck by a typewriter x, not plainly deleted by a pen line; the underlying quote reading remains uncertain.'],
 [r'but it is \xout{\illegible{1}}',r'but it is \xout{so}','The final cancelled word is visibly so beneath two x-overstrikes.']
]
commit(dict(key=key,edits=edits,diffs={
2129:['cf théorème p 46','The top-left slanting reference is present and legible, independently of the witness comment.'],
2130:[r'i.e. for any $a\in\mathrm{Ob}\,A$, $A_{/a}\to A$ is aspheric','The handwritten note says any; i.e. is readable and its insertion belongs after the T2 assertion.'],
2131:[r'NB In view of \unsure{T1 et T2}, I aspheric $\Leftrightarrow$ $I\to e$ is aspheric','The two aspheric assertions and the double arrow are legible; the short connector between T1 and T2 remains doubtful.'],
2134:['thus e_o and e_1 are defined','The word are is clearly typed at the end of the upper line.'],
2136:[r'\inserted[typed]{which}','The insertion is typed rather than cursive.','correct layer attribution'],
2137:[r'\margin{\unsure{$\mathcal A$}}','The large black marginal A-like sign is present; heavy retracing prevents secure identification as the script category symbol.'],
2139:[r'\inserted[typed]{h}','The lower interlinear h is typed and placed by a hand curve.','correct layer attribution'],
2142:['two hooked arrows into F x I','The enlarged scan shows clear recurved tails on both inclusions. The initial transcription missed these hooks; the witness happens to retain them.','correct transcription'],
2144:['where we got','The typed line has we got, with no apostrophe or ve.']
},unsure=[
['cf théorème p 46','The top margin reference is legible.'],
[r'\unsure{K}','The small pencil mark to the right of 39 could be a K or a checking sign; do not resolve it.'],
[')','The pen retraces the label-closing parenthesis.'],
['i.e.','The opening abbreviation is legible in the upper-right insertion.'],
['In view of','The rotated marginal line reads In view of.'],
[r'\unsure{T1 et T2}','The connecting strokes are closer to a conjunction than a right arrow, but too slight to settle.'],
['is','The word is begins the final marginal line.'],
[r'\unsure{$\mathcal{A}$}','The A-like marginal sign is heavily retraced and remains doubtful.'],
[r"\unsure{\xout{''}}",'The cancelling stroke is a typewriter x; the underlying closing quote remains uncertain.']
],illegible=[
[r'\illegible{1}','The old symbol before the handwritten A-caret = A-hat is covered by dense pen strokes.'],
['so','The cancelled two-letter word reads so.']
],notes=[
'The margin reads cf théorème p 46; doubt removed.',
'In view of and is aspheric are readable. The connector between T1 and T2 remains doubtful; the double implication between the two assertions is clear.',
'The pencil K-like checking mark remains uncertain.',
'The carets are pen additions, including the small raised carets on A later in the page; the slashed-o empty element is typed.',
'The c in for suitable c is heavily penned/retraced; its source reading c is secure and its handwriting attribution retained.',
'The mark after saturation is a machine overstrike; the old quote reading remains doubtful.',
'The second l in well is drawn/retraced by pen, as the source records.',
'The last cancelled word is so, recovered through the typewriter overstrikes.'
],evidence='Both halves inspected; the marginal NB was rotated and the diagram, quote, old final-object symbol, T2 parenthesis and last cancellation were enlarged. The reference is to théorème p 46. In T2 the insertion says i.e. for any; its definition line has hand membership. The interval condition has a typed slashed-o initial-element sign. Which and h are interlinear typing with hand placement marks. The five arrows in (D) are penned; the two upper ones have unmistakable hook tails, the central h arrow is dashed, and the right descending arrow is retraced. All object strings are typed with literal x products. The marginal A-like sign, pencil K-like check, old final-object symbol and the short T1/T2 connector remain doubtful.'))

key='ps_134-3_040'
import re
s=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for n,l in enumerate(s.splitlines(),1):
 a=re.sub(r'\\(longrightarrow|mapsto|to|in)(?![A-Za-z])',lambda m:r'\hand{'+m[0]+'}',l).replace(r'A\hat{}',r'A^{\hand{\wedge}}')
 if a!=l:edits.append([l,a,f'Source line {n}: arrows, membership/mapsto signs and the small caret specified here are visibly drawn in pen; their typed letters and indices remain plain.'])
edits += [
 [r'\inserted{[small],}',r'\inserted{[small]}','The apparent comma after the square bracket is the curled end of the placement stroke, not separate punctuation.'],
 [r'\inserted{of}',r'\inserted[typed]{of}','The interlinear of is in the typewriter face, with a diagonal pen placement stroke.'],
 [r'\hand{\unsure{$\hat{}$}}',r'\hand{$\hat{}$}','The upper angled caret is clear; the heavy extra mark beneath does not obscure that live hat reading.'],
 [r'\[ h(a)(f,u)',r'\[ \over{h(a)}{h(a)}(f,u)','The displayed h(a) is retraced in thick pen over its typewriter base.']
]
commit(dict(key=key,edits=edits,diffs={
2150:['reduced to check','The scan has the infinitive check, without ing.'],
2154:[r'is a \inserted{[small]} category','The bracketed insertion is present. The stroke taken as a comma is part of the insertion curve, so no comma is transcribed.','correct transcription'],
2156:[r'\inserted[typed]{of}','The insertion is typed rather than handwritten.','correct layer attribution'],
2161:['and f_1:','The hand insertion ends and; no second where is present.'],
2162:['this is functorial','The initial t of this is visible.'],
2164:[r'\xout{(a functor from $A_{/a}$ to B)}','The redundant typed explanation is cancelled by a row of x characters and must remain in the diplomatic layer.'],
2168:[r'arrows x to a in A','The letters in are typed after the arrow expression, rather than a membership symbol.']
},unsure=[
[r'\unsure{0}','The second folio digit is a small dark round blot, plausible as 0 but without a clear open counter. Retain doubt.'],
[r'\hand{$\hat{}$}','The upper caret over A is visibly angled; an extra blot below it is not another readable symbol.']
],illegible=[],notes=[
'The handwritten number begins with a clear 4; the second small dark digit remains doubtful as 0.',
'The retraction overstrike and doubled p/o in compositum are present; the source keeps the machine cancellation history and correct live word.',
'The live caret over A is clear in enlargement; no extra letter is inferred from the lower blot.',
'The small h stroke in Then is an overtyped/retraced part of the word, not an extra content mark.',
'The live final letter in choice of f and u is u under overtyping; its predecessor cannot be securely read, and no alternate letter is supplied.'
],evidence='Both halves inspected, with crops of small, of, the item-a hat, the choice-of-u overstrike and compositum. The first paragraph has pen arrows in every inclusion/retraction expression. The small insertion uses square brackets, and its trailing curve belongs to placement rather than a comma. Of is typed above the line. The (D) call and the G=F/f_0=id_F insertion are penned. The h(a) in the lower display is heavily retraced, while the redundant following explanation is machine-cancelled. The C_u= and C= additions precede typed slice expressions. The lower object x letters are penned, and the prose literally says arrows x to a in A.'))
