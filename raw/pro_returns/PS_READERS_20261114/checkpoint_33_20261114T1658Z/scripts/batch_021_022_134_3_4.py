import json
from review_134_3_4 import save_review, occurrences, TEXT, OUT
s=(TEXT/'transcription/ps_pages/ps_134-3_021.tex').read_text()
conf={'key':'ps_134-3_021','edits':[
[r'\mspage{21}',r'\mspage{\hand{21}}','The page number is written in pen.'],
[occurrences(s,'unsure')[1][0],r"``finite''",'The handwritten finite is enclosed by two pairs of quotation strokes.'],
[r'\unsure{of|or}',r'of','The scan types of cubical, with an f-shaped second letter; preserve the source slip.'],
[r'\inserted{natural}',r'\inserted[typed]{natural}','Natural is typed above integers, with a pen placement curve.'],
[r'\unsure{objects|object}',r'objects','The handwritten word ends in a separate s before of B.'],
[r'defin\over{ing}{\unsure{e}}',r'defin\over{ing}{e}','The live replacement e is visible before the crossed ing.'],
[r'bou\unsure{n}ding',r'bounding','The typewriter n is readable in bounding.'],
[r'\deleted{\xout{xxxx}}\inserted{define}',r'\deleted{\xout{form}}\inserted[typed]{define}','The crossed word below define reads form; define itself is typewritten above the line.'],
[r'\xout{xxxxx}\inserted{family}',r'\xout{union}\inserted[typed]{family}','Union remains readable through the x-overstrikes; family above is typed.'],
[r'\inserted{sphere}',r'\inserted[typed]{sphere}','Sphere is typewritten above bounding; the curve marks insertion and does not strike bounding.'],
[r'\[ (\hand{*})',r'\[ (*)','The lower formula label is a typed asterisk; preserve the typed layer.'],
[r'family (\hand{*})',r'family (*)','The repeated formula reference is also typewritten.'],
[r'(\hand{**})',r'(**)','The double-asterisk display label is typed, unlike its arrow.']
],'diffs':{
1756:[r'\inserted{(19)}','The upper-right handwritten call 19 is joined to topology by a placement stroke; no note body is here.'],
1762:['C.W. spaces','The word spaces has a visible terminal s.'],
1764:[r'\inserted{with}','With is penned above the gap between met and so.'],
1765:['components of a','The next line begins of a; the witness or is unsupported.'],
1766:['of cubical','The typewriter letter is f; the source slip is not normalized to or.','settled on image'],
1768:[r'\inserted[typed]{natural}','Natural is typewritten; only its insertion curve is pen.','correct layer'],
1772:[r'\inserted{objects of $\underline{B}$}','The final s of objects is legible in the pen insertion.','settled on image'],
1774:['bounding','The word is bounding, not building.'],
1776:[r'\deleted{\xout{form}}\inserted[typed]{define}','Define is a typed interlinear replacement over the canceled form.','correct layer'],
1780:['is a cell, and the','The conjunction and appears at the right edge after cell.'],
1781:[r'\xout{union}\inserted[typed]{family}','Family is typed above the x-struck union; the following the is canceled.','correct layer'],
1782:[r'\inserted[typed]{sphere}','Sphere is typed above the line, and bounding stays live below it.','correct layer'],
1786:['24.','The source supplies the corrected number 24 without a section title.'],
1789:['this condition','The last paragraph clearly types this condition.']},
'unsure':[[r'\unsure{xxxqui}','The x-overprinted fragment before localization remains partially obscured.'],[r"``finite''",'Both opening and closing quote strokes are visible.'],['of','The second letter has the vertical ascender and crossbar of f.'],['objects','A final s precedes of in the handwritten phrase.'],['e','The live handwritten correction reads e.'],['n','The n of bounding is visible despite light overtyping.'],[r'\unsure{4}','The new date 7 is clear, but the old digit remains partly obscured.']],
'illegible':[],
'notes':['The crossed fragment after a remains doubtful; no speculative expansion supplied.','Finite is quoted and objects has a final s; both are resolved from the scan.','The source types of cubical; preserve the slip.','A small trace below These does not identify a different letter; the raised star after boundary remains in the handwritten layer.','Sphere is typewritten, and its curve places it before bounding without deleting bounding.','The arrows are handwritten, but the lower (*) and (**) labels have the same typewriter face as the body; their stars are corrected to typed.'],
'evidence':'Both halves inspected. The top half contains quoted handwritten finite, with, monomorphic and objects of B; natural, define, family, sphere, topological and and spheres are typed interlinear text. The canceled form and union can be recovered under their replacements. The source typo of cubical is clear, as is bounding. Section 24 begins below the corrected date 7.3., retracting the claim that degree two nerve coverings suffice. Its display labels are typed and its arrows penned. The old date digit and the crossed localization fragment remain uncertain.'}
(OUT/'review_notes/ps_134-3_021.json').write_text(json.dumps(conf,ensure_ascii=False,indent=2))
save_review(conf)
conf={'key':'ps_134-3_022','edits':[
[r"\inserted{(for any $N\in\underline{N}$,}",r'\inserted[typed]{for any $N\hand{\in}\underline{N}$,}','For any N and the terminal comma are typed above the line; the membership sign and placement bracket are pen. The apparent opening parenthesis is the left end of that placement bracket.'],
[r'\deleted{\unsure{true}}',r'\deleted{\unsure{it is|it as}}','Enlargement shows a two-word crossed phrase, beginning it; the second word remains partly obscured. The single-word guess true is unsupported.'],
[r'\inserted{standart ordered}',r'\inserted[typed]{standart ordered}','Standart ordered is typewritten above the line, not handwritten.'],
[r'\hand{\Delta[N]\hookrightarrow}(\mathrm{Cat})\hand{\hookrightarrow\Delta(N)^{\wedge}}',r'\hand{\Delta[}N\hand{]\hookrightarrow}(\mathrm{Cat})\hand{\hookrightarrow\Delta}(N)\hand{^{\wedge}}','In the inclusion display both N letters and the round parentheses of (N) are typed; Delta, square brackets, arrows and hat are penned.'],
[r'\hand{^{\sim}\simeq\Delta}[N]\hand{^{\wedge}}',r'\hand{^{\sim}\simeq\Delta[}N\hand{]^{\wedge}}','The square brackets in the first equivalence are handwritten around typed N.'],
[r'((\mathrm{Cat}),T_{N\,/A})\hand{^{\sim}\simeq}',r'((\mathrm{Cat}),T_N)_{/A}\hand{)^{\sim}\simeq}','The scan puts /A after the closing parenthesis following T_N, then adds a further pen parenthesis before the tilde. Preserve that placement and the unmatched authorial parenthesis rather than putting /A inside the subscript.'],
[r'\unsure{invariants|invariant}',r'invariants','The final s is clearly typed; the nearby curve introduces dimension rather than canceling the s.'],
[r'\inserted{dimension}',r'\inserted[typed]{dimension}','Dimension is typewritten above the canceled degrees.'],
[r'\xout{w}is',r'\xout{wa}is','Enlargement exposes the old a under the overtyped i, as well as the canceled w; retain both superseded typewriter letters.'],
[r'\inserted{left}',r'\inserted[typed]{left}','Left is typewritten at the right interline with a handwritten placement curve.']
],'diffs':{
1791:[r"let's\inserted[typed]{for any $N\hand{\in}\underline{N}$,}denote",'The words and N letters are typed; the apparent initial parenthesis is part of the placement bracket below them.','correct layer'],
1794:['i.e. covering','There is no comma after i.e. in the source.'],
1795:[r'\inserted[typed]{standart ordered}','The two inserted words have typewriter glyphs, with the source spelling standart.','correct layer'],
1797:[r'\Delta(N)^{\wedge}','The second member of the inclusion display uses round parentheses around typed N.'],
1798:['namely any category A','Any is fully typed before category.'],
1799:[r'((\mathrm{Cat}),T_N)_{/A}\hand{)^{\sim}\simeq}(\hand{\Delta}(N)_{/A})\hand{^{\wedge}}','Enlargement places /A outside the pair ending after T_N; a further pen closing parenthesis precedes the tilde. The supplied transcription wrongly put /A in the T subscript.','correct transcription'],
1801:[r'\inserted[typed]{dimension}\xout{degrees}','Dimension is a typed replacement with pen placement curve.','correct layer'],
1802:['invariants','The final s is present and uncanceled.','settled on image'],
1805:[r'\inserted[typed]{left}','Left is typed in the upper-right interline.','correct layer'],
1806:['had same homotopy type','There is no the before same in the source.']},
'unsure':[[r'\unsure{it is|it as}','The canceled phrase begins it, and the second word may be is or as; pen strokes conceal the middle letter.'],['invariants','The s is clear and untouched by the insertion curve.']],
'illegible':[[r'\illegible{1}','The short crossed fragment before simplices remains unread; its mixture of type and pen cancellation does not expose a secure token.']],
'notes':['The live ff is penned over the old terminal s; the i remains typed.','The enlarged cancellation is a short two-word phrase beginning it; retain its uncertainty rather than the original true guess.','The short fragment before simplices remains illegible, with typewriter overstrike and dark pen traces.','The s of invariants is live; dimension is typed above the line.','The formula letters and numerical arguments are typed where visible; Delta signs, comparison signs, hats, tildes, arrows and square brackets are penned. The slice placement was corrected from the enlarged formula.','The lower word exposes an old canceled w and an a beneath i; the live word is is.'],
'evidence':'Both halves inspected, with enlarged canceled phrase, slice equivalence and was/is overtype. The interlinear for any N, standart ordered, dimension and left are typed, whereas not is handwritten and underlined. The slice /A follows the closed site expression, and a further pen closing parenthesis before the tilde is preserved as written. The first inclusion uses Delta[N], while its rightmost object and the slice formula use Delta(N). Invariants is plural. The section distinguishes finite nerve truncations from the full nerve topology and retracts the earlier claim about the left adjoint N prime; a crossed two-word phrase and the short canceled fragment before simplices remain uncertain.'}
(OUT/'review_notes/ps_134-3_022.json').write_text(json.dumps(conf,ensure_ascii=False,indent=2))
save_review(conf)
