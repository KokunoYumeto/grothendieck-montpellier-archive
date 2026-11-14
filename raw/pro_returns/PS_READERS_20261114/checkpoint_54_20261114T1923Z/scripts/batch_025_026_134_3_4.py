import json
from review_134_3_4 import save_review, OUT
conf={'key':'ps_134-3_025','edits':[
[r'\xout{\unsure{25}}',r'\xout{25}','The canceled top page number remains readable as 25.'],
[r'\unsure{subcategor}',r'subcategor','The x-struck fragment retains the letters subcategor.'],
[r'\inserted{such}',r'\inserted[typed]{such}','Such is typed above cases.'],
[r'\inserted{intrinsic}',r'\inserted[typed]{intrinsic}','Intrinsic is typewritten above structure.'],
[r'\inserted{full}',r'\inserted[typed]{full}','Full is typewritten above subcategory.'],
[r'\inserted{simultaneous}',r'\inserted[typed]{simultaneous}','Simultaneous is typed in the lower-half interline; the placement curve is handwritten.'],
[r'subtopos of $M^{\wedge}$',r'subtopos of $M^{\hand{\wedge}}$','The first presheaf hat above M is handwritten.'],
[r'of $M^{\wedge}$).',r'of $M^{\hand{\wedge}}$).','The second presheaf hat above M is handwritten.'],
[r'M \simeq \mathrm{Ind}',r'M \hand{\simeq} \mathrm{Ind}','The equivalence sign before Ind is penned.'],
[r'$\underline{B}_{oo}{}^{\wedge}$',r'$\underline{B}_{oo}{}^{\hand{\wedge}}$','The hat above the cellular-core notation is handwritten.'],
[r'$B^{\wedge}$',r'$B^{\hand{\wedge}}$','The bottom-line presheaf hat above B is handwritten.'],
[r'\margin{mainly}',r'\margin{\diagram{\begin{tikzpicture}[baseline=(n.base)]\node[draw,ellipse,inner sep=3pt] (n) {mainly};\end{tikzpicture}}}','The marginal mainly is enclosed by an oval pencil loop.']
],'diffs':{
1853:[r'\inserted[typed]{such}','The inserted such has typewriter glyphs.','correct layer'],
1854:[r'\inserted[typed]{intrinsic}','Intrinsic is typed above the line.','correct layer'],
1855:[r'\inserted[typed]{full}','Full is typed above subcategory.','correct layer'],
1858:[r'\hand{(${}^{22\prime}$).}','Only the call 22 prime is present; the longer retrospective arXiv footnote is not on this page.'],
1861:[r'\inserted[typed]{simultaneous}','The inserted simultaneous is typed, with a pen positioning curve.','correct layer'],
1865:[r'\margin{\diagram{\begin{tikzpicture}[baseline=(n.base)]\node[draw,ellipse,inner sep=3pt] (n) {mainly};\end{tikzpicture}}}','The lower-left margin repeats mainly inside a drawn oval.'],
1866:['important cases','Cases is plural at the lower-right edge, followed by when on the next line.']},
'unsure':[['25','The crossed header digits read 25.'],['subcategor','The letters are recoverable through the typewriter x-overstrikes.'],[r'\unsure{subt}','The final character of the short canceled fragment is too densely overtyped to settle.'],[r'\unsure{givi}','The right-edge canceled fragment is partly cut; retain its tentative reading.'],[r'\unsure{25}','The overwritten section digits are covered by the new 26, so the old 25 remains uncertain.'],[r'\unsure{,}','The former character under the handwritten closing parenthesis remains obscured.'],[r'\unsure{\hand{red}}','The pen completion of ordered runs into the image edge and cannot be completely verified.']],
'illegible':[[r'\illegible{1}','The circular margin sign is heavily hatched; no definite reading survives.'],[r'\illegible{1}','The character after M is covered by a dense pen blot.']],
'notes':['The canceled top page number is 25.','The slight stroke after best is at the crop edge and does not establish a textual character.','The sign in the margin and the deleted character after M remain unread; the new comma is clear.','Small marks above and below n in Ind appear to reinforce the letter; they do not yield an alternative word.','The pen completion red is clipped at the right edge and remains doubtful.','The live section number 26 is clear, while the earlier digits remain doubtful.','The closing parenthesis after instance is a pen correction over an uncertain old character.','The w of were has a small pen reinforcement, with no recoverable different predecessor.','The handwritten call reads 22 prime; there is no corresponding note body on this page.'],
'evidence':'Both halves inspected. The top canceled page number and the crossed fragment subcategor can be read. Such, intrinsic, full and simultaneous are typed interlinear insertions; species and mainly are pen additions. The marginal mainly has a drawn oval, now reconstructed. Presheaf hats and the equivalence sign are handwritten. The page ends section 25 with an admitted lack of an intrinsic characterization and call 22 prime, then opens section 26 on simplex and cube subcategories. The clipped ordered completion, old section number, canceled fragments and two obscured marginal/textual marks remain doubtful.'}
(OUT/'review_notes/ps_134-3_025.json').write_text(json.dumps(conf,ensure_ascii=False,indent=2));save_review(conf)
conf={'key':'ps_134-3_026','edits':[
[r'\inserted{$B =$}',r'\inserted[typed]{$B =$}','The interlinear B and equals sign are typed; the placement bracket is pen.'],
[r'on $\underline{B}_{oo}\hat{}$',r'on $\underline{B}_{oo}\hand{\hat{}}$','The first presheaf hat is handwritten.'],
[r'M \longrightarrow \underline{B}_{oo}\hat{}',r'M \hand{\longrightarrow} \underline{B}_{oo}\hand{\hat{}}','The displayed arrow is retraced pen and the presheaf hat is handwritten.'],
[r'$M_B = B\hat{}$',r'$M_B = B\hand{\hat{}}$','The inline hat defining M_B is handwritten.'],
[r'\longrightarrow (Hot)',r'\hand{\longrightarrow} (Hot)','The arrow in the displayed functor to Hot is handwritten.'],
[r'$\hand{\widehat{B}}$',r'$\overset{\hand{$\wedge$}}{B}$','In the expression Ob B-hat, B is typed and only its hat is in pen.'],
[r'\unsure{because}',r'because','The crossed margin word because is legible through the pencil hatching.'],
[r'\inserted{(3)}',r'\inserted{(23)}','The enlarged endnote call clearly has two digits, 23, not 3.'],
[r'\inserted{extremely}',r'\inserted[typed]{extremely}','Extremely is typewritten above the next line, with a pen placement curve.'],
[r'from B\hand{$\hat{}$} to',r'from B\hand{$\hat{}$}\hand{/}to','The scan includes a diagonal handwritten separation stroke between B-hat and to.']
],'diffs':{
1870:['natural Hot-equivalence class','The body uses the singular class.'],
1871:[r'\uline{class}','The single word class is underlined in pen.'],
1872:[r'\uline{of subcategories} B_{oo} \uline{in} M','There are separate pen underlines beneath of subcategories and in.'],
1873:[r'\inserted[typed]{$B =$}','B = is a typed interlinear insertion with a handwritten placement bracket.','correct layer'],
1877:['(Hot)','The display and body retain parentheses around Hot.'],
1879:[r'\inserted{(23)}; \margin{\deleted{because ...}}','The scan has call 23 and a crossed marginal because with a partly legible equivalence. The arXiv expanded prose is not present, and the original call 3 was a misreading.','correct transcription'],
1880:['identifying (Hot) to a category','The source uses to, not with.'],
1882:[r'\inserted[typed]{extremely}','Extremely is typed above the line.','correct layer']},
'unsure':[[r'\unsure{descripttion|description}','The enlarged middle letters are multiply impressed, with p/t overlaps; retain the alternative rather than impose a clean spelling.'],['because','The diagonal pen letters spell because despite the cancellation lines.'],[r'\unsure{\widehat{B}_{/a} \simeq \widehat{B_{/a}}}','The crossed formula is only partially visible; neither placement of both hats nor the full comparison sign can be verified.']],
'illegible':[],
'notes':['The h in The point is typewriter-overstruck; the live word The remains readable.','Tiny marks near the initial The words do not establish an alternative word; no spurious text is supplied.','The description overstrike remains unresolved after enlargement.','Because is recovered; the crossed formula remains uncertain. The isolated tiny margin mark near cit sooner or later has no readable character.','The enlarged note call is 23, not 3.','The closing parenthesis after Hot is retouched, but no different underlying character can be recovered.'],
'evidence':'Both halves inspected, with enlarged note call, arrow, description and canceled margin note. The call after over a is unequivocally 23. The marginal because is legible, while its crossed presheaf/slice equivalence remains doubtful. B = and extremely are typed interlinear additions. The displayed arrows and hats are pen, with a retraced single arrow in the first display; the final diagonal separator after B-hat is retained. The section formulates localization of the presheaf category as the intrinsic condition sought, while asking whether the cellular examples provide merely sufficient conditions.'}
(OUT/'review_notes/ps_134-3_026.json').write_text(json.dumps(conf,ensure_ascii=False,indent=2));save_review(conf)
