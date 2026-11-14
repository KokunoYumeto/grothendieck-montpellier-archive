from review_root import review
from pathlib import Path
import json

hemi=r'\hand{\ensuremath{\mathord{\begin{tikzpicture}[x=1ex,y=1ex,baseline=-.5ex]\draw (0,0) ellipse (.72 and .95);\draw (0,-.95) .. controls (-.75,-.15) and (-.2,.65) .. (0,.95);\end{tikzpicture}}}}'
fragments=r'F\tikz[baseline=(r.base),x=1pt,y=1pt]{\node[inner sep=0pt,anchor=base] (r) at (0,0) {r};\draw[line width=.25pt] (-2.4,8)--(-2.4,10) (-3.2,8)--(-1.5,8) (1.5,8)--(1.5,10) (.6,8)--(2.5,8);\draw[line width=.25pt] (-2,-2.5)--(-.7,-2.5) (.2,-3) .. controls (.8,-1.5) and (1.6,-1.5) .. (2,-2.5);}ench'
review('ps_134-2_079',changes=[
(r'\mspage{53}',r'\mspage{\hand{63}}','The live first digit is a looped6, not5; both63 digits are pen.'),
(r'n $\geqslant$1',r'n $\hand{\geqslant}$1','Both the thick angled greater-than stroke and the lower oblique equality stroke are handwritten.'),
(r'\hand{\unsure{$\bigcirc$}}',hemi,'The symbol is a closed oval with an inner curved meridian, not an undecorated circle. Its visible geometry agrees with the standard-hemisphere symbol checked at134-3/89.'),
(r'\xout{\unsure{the}}\inserted[typed]{any}',r'\xout{the}\inserted[typed]{any}','The three old letters t,h,e are recoverable beneath the regular typewriter x-overstrikes.'),
('the French\nword','the '+fragments+'\nword','Restore the two small upper typewriter fragments and the two lower fragments around the r of French without assigning them a semantic meaning.'),
(r'(${}^{20}$\xout{\unsure{1}}!)',r'(${}^{20}$\deleted{\unsure{1}}!)','The small old character is cancelled with irregular heavy pen strokes, not a regular typewriter x.'),
(r'the \xout{\unsure{the}} ``primitive',r'the \deleted{\unsure{the}} ``primitive','This cancellation is a set of thick diagonal pen strokes rather than typewriter x-overtyping; its old word remains doubtful.'),
(r'\mspage{79}',r'\margin{\hand{79}}','The rotated lower-left79 is pencil archive foliation.')
],doubts={'unsure':[
(hemi,'doubt resolved','The outer oval and curved inner meridian are both visible; the geometry can be reproduced without guessing an alphabetic symbol.'),
('the','doubt resolved','The old t, h and e can be separated from the regular overtyped x strokes.'),
(r'\unsure{1}','doubt retained','The densely crossed small mark next to20 does not establish a unique old character.'),
(r'\unsure{the}','doubt retained','The diagonal pen cancellation obscures most of the old word, so the remains do not securely settle the.')
],'illegible':[]},notes=[
'The live folio is63, with a looped pen6 and pen3. The interior retracing does not yield an independently secure older digit.',
'The meet sign is handwritten. The overlapping-circle drawing has f in the left part, f-prime in the overlap, and f-double-prime in the right part, as represented in the checked diagram.',
'The postscript comment is handwritten beneath note13. The comparison sign has two visible pen components, now explicitly marked.',
'The hemisphere sign has an inner meridian and is reconstructed geometrically. The overwritten the before typed any is resolved. A closer enlargement and independent review confirm a small pen t over the typed T in The; the large outer curve belongs to In my notes, rather than a literal parenthesis.',
'The tiny fragments above and below r in French are now drawn in place, with no inferred word or punctuation function.',
'The doubtful character beside20 and the doubtful word before primitive remain marked; their cancellations are pen, not typewriter overstrikes.',
'Notes12,13,15,19 and20 are visibly present, including the handwritten qualification beneath13, regardless of the limited comparison excerpt.',
'The lower-left79 is rotated pencil archive foliation.'
],summary='Both halves and enlarged folio, relation sign, cancelled words, retouched T and typewriter fragments inspected. Corrected53 to63, reconstructed the hemisphere symbol and the small French fragments, resolved old the before any, and corrected two cancellation provenances. A closer crop and independent reading confirm the lowercase pen t over T. All substantive qualifications, including the handwritten postscript below13, are retained.',differences={
1262:('fibered products exist','the typescript reads as our transcription','The typed verb is exist, with no final s.'),
1263:(r'in $\underline{C}$\hand{$_{\bullet}$} only','the typescript reads as our transcription','The lower-right bullet is a visible pen addition to the underlined C; the witness omits it.'),
1264:(r'\hand{$_{\bullet}$}','the typescript reads as our transcription','The pen subscript bullet is present and mathematically distinguishes the category used here.'),
1265:('has to be rephrased','the typescript reads as our transcription','The complete typed word be is visible.'),
1266:('it the map from it','the arXiv text corrects','The literal source has it, an isolated t-for-f slip. The conditional if is confirmed by the same ordinary usage elsewhere, including if needed on this page; an explicit master variant records that correction.'),
1267:(r'$\underline{B}_{o}$\hand{$\to$} M thus obtained','the typescript reads as our transcription','The target M is fully visible after the handwritten arrow and is missing from the witness.'),
1268:(r'M\hand{$\to$}(Ho)','the typescript reads as our transcription','The target is literally parenthesized Ho, not the witness Hot notation.'),
1269:('canonically isomorphic','the typescript reads as our transcription','The typed adverb ends in ly.'),
1270:('(and unicity)','the typescript reads as our transcription','The typed word is unicity, not the witness unicicity.'),
1271:('unicity theorems','the typescript reads as our transcription','The typed word is again unicity.'),
1276:('we would call it rather','the typescript reads as our transcription','The modal would is clearly typed, not should.')
})

project=Path(__file__).resolve().parents[1];p=project/'records/MASTER_VARIANTS_134_2.json';a=json.loads(p.read_text());a=[x for x in a if x['source_id']!='DIFF:1266']
a.append(dict(key='ps_134-2_079',before='it the map from it',after='if the map from it',kind='slip corrected',reason='The isolated t-for-f typing slip is settled by the conditional construction and by the ordinary if in if needed on the same page.',source_id='DIFF:1266'));p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
p=project/'guide_sections/134_2_appendix.tex';s=p.read_text()
if '\\subsection*{Notes 12--21:' not in s:
 s+=r'''
\subsection*{Notes 12--21: Products, test functors, and primitive structure}
Cote 134-2, site79 (folio63, initially misread53), collects substantial retractions. Note12 gives an overlapping-circle counterexample; note13 rejects the earlier assertion for positive dimensions and adds that even the postscript to section13 remains inaccurate, referring onward to section18. Note14 confines the required fiber products to the category marked by a lower bullet and requires the relevant functors to preserve those products; the witness omits that bullet, thereby losing a mathematical distinction. Note15 doubts the proposed equivalence even for groupoids or Gr-categories. Notes16--17 revisit fibrancy and the functors into a homotopy model: even if every object is fibrant, a suitable uniqueness statement is needed before the resulting functors to(Ho) can be said to be canonically isomorphic. The discussion links this issue to existence and uniqueness of test functors out of the category of standard hemispheres and to section90, then records the shift toward asphericity and contractibility structures. The hemisphere symbol has a visible curved meridian, and the witness's missing target M changes the displayed functor. Note18 explains gerb as a rendering of gerbe and proposes stack of groupoids or Gr-stack. Note19 explicitly rejects the earlier claim; note20 warns that the suggested construction may give overly large categories; note21 recommends retaining the primitive subcategory as additional structure rather than expecting to recover it from the ambient category alone. These notes qualify the Quillen letter's statements about coherators and their generators. The isolated it for if in note16 is corrected only in the corrected forms and is recorded in the apparatus.
'''
 p.write_text(s)
