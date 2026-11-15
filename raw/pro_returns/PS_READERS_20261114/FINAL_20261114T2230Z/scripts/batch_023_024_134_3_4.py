import json
from review_134_3_4 import save_review, OUT
conf={'key':'ps_134-3_023','edits':[
[r'\mspage{23}',r'\mspage{\hand{23}}','The page number is handwritten.'],
[r'N:(Cat)\longrightarrow (Ss sets)',r'N:(Cat)\hand{\longrightarrow} (Ss sets)','The arrow in the first display is penned between typed objects.'],
[r'(Preord)\hookrightarrow (Cat) \qquad or \qquad (Ord)\hookrightarrow (Cat)',r'(Preord)\hand{\hookrightarrow} (Cat) \qquad or \qquad (Ord)\hand{\hookrightarrow} (Cat)','Both inclusion arrows are handwritten.'],
[r'\hand{\Delta} \hookrightarrow (Cat)\hookrightarrow \hand{\Delta}^{\wedge}',r'\hand{\Delta} \hand{\hookrightarrow} (Cat)\hand{\hookrightarrow} \hand{\Delta^{\wedge}}','In the simplicial inclusion display the arrows and presheaf hat are handwritten along with the Delta signs.'],
[r'a_o\longrightarrow a_1\longrightarrow \;\ldots\longrightarrow a_n',r'a_o\hand{\longrightarrow} a_1\hand{\longrightarrow} \;\ldots\hand{\longrightarrow} a_n','All three arrows in the simplicial string are penned; the a terms are typed.'],
[r'\hand{\square} \hookrightarrow (Cat)\hookrightarrow \hand{\square}^{\wedge}',r'\hand{\square} \hand{\hookrightarrow} (Cat)\hand{\hookrightarrow} \hand{\square^{\wedge}}','The two cubical inclusion arrows and the hat are handwritten.'],
[r'by $\hand{\square}^{\wedge}$',r'by $\hand{\square^{\wedge}}$','The hat above this inline cubical presheaf sign is drawn by hand.'],
[r'Cub_n(A_i)\longrightarrow \hand{C}ub_n(A)',r'Cub_n(A_i)\hand{\longrightarrow} \hand{C}ub_n(A)','The arrow in the Cub display is handwritten.'],
[r'\hand{\simeq} \hand{\square}^{\wedge}',r'\hand{\simeq} \hand{\square^{\wedge}}','The presheaf hat in the topos equivalence is handwritten.'],
[r'$\hand{\square}^{\wedge}$ instead of $\hand{\Delta}^{\wedge}$',r'$\hand{\square^{\wedge}}$ instead of $\hand{\Delta^{\wedge}}$','Both hats in the concluding topos comparison are hand-drawn.'],
[r'T\hand{h}ese reflections',r'T\over{h}{h}ese reflections','The h is retraced over its typed predecessor rather than inserted into a blank.']
],'diffs':{
1809:[r'\inserted{[presumably]}','Presumably is handwritten inside square brackets, with an insertion line to after which; arXiv parentheses do not match.'],
1810:['the associated homotopy','Associated has its final d in the typed text.'],
1811:[r'\uline{only} N, \uline{not} N\prime, \uline{induces such equivalence}','Three separate underlines emphasize only, not, and induces such equivalence.'],
1820:[r'\over{\xout{here}}{now}','The live pen replacement is now, omitted in the witness.'],
1825:['there are less covering families','The typed interlinear parenthesis says less, not fewer.']},
'unsure':[[r'\unsure{s}','The handwritten d of noted obscures the former terminal letter.'],[r'\unsure{able for}','The enlargement shows overlapping typewriter strokes in suitablefor, including a canceled character after t and doubled f; preserve the uncertain span rather than invent a clean underlying sequence.']],
'illegible':[],
'notes':['The apostrophe in the second Quillen occurrence is a pen reinforcement, as encoded.','The old letter under d remains uncertain.','Left begins with an overtyped l, but the intended live word is readable and no pen replacement is established.','The enlarged suitablefor region remains a composite overstrike; the doubtful span is retained.','The h of These is a pen retouch of typed h, now encoded as over.','Commutative is typed above the preceding line, placed after namely by a long pen curve.','The vertical pen separators in was/of and second/inclusion are visible and retained as source marks.'],
'evidence':'Both halves inspected and the final overtyped suitablefor span enlarged. The opening insists that N alone, not its left adjoint, induces the localization equivalence, with three pen underlines. The lower discussion replaces finer by typed coarser and adds a typed explanatory parenthesis using less. Every displayed arrow and presheaf hat is penned, while the object labels remain typed; those previously unmarked layers were restored. The handwritten now and topology replacements are visible. The underlying letter in noted and the suitablefor overstrike remain unresolved.'}
(OUT/'review_notes/ps_134-3_023.json').write_text(json.dumps(conf,ensure_ascii=False,indent=2));save_review(conf)
conf={'key':'ps_134-3_024','edits':[
[r'\inserted{many}',r'\inserted[typed]{many}','Many is typewritten above the line; its curved placement mark is pen.'],
[r'\margin{[$\uparrow$}',r'\margin{\diagram{\begin{tikzpicture}[x=1cm,y=1cm]\draw[->] (0.35,0)--(0,0)--(0,0.8);\end{tikzpicture}}}','Replace the approximate bracket characters by the actual hooked upward arrow.'],
[r'\margin{[$\downarrow$}',r'\margin{\diagram{\begin{tikzpicture}[x=1cm,y=1cm]\draw[->] (0.35,0.8)--(0,0.8)--(0,0);\end{tikzpicture}}}','Replace the approximate bracket characters by the hooked downward arrow beside section 25.'],
[r'M \to (\mathrm{Hot})',r'M \hand{\to} (\mathrm{Hot})','The arrow in the first display is handwritten.'],
[r'M_T^{\hand{\sim}} \to M_{T\prime}^{\hand{\sim}}',r'M_T^{\hand{\sim}} \hand{\to} M_{T\prime}^{\hand{\sim}}','The morphism arrow between topoi is handwritten.'],
[r'(M_T^{\hand{\sim}})_{/A} \to (M_{T\prime}^{\hand{\sim}})_{/A}',r'(M_T^{\hand{\sim}})_{/A} \hand{\to} (M_{T\prime}^{\hand{\sim}})_{/A}','The induced slice-topos arrow is handwritten.'],
[r'\unsure{*}',r'*','The asterisk in the call before superscript 22 is clear.'],
[r'\inserted{Hot-}',r'\inserted[typed]{Hot-}','Hot- is typewritten above equi-; the pen curve marks insertion without deleting equi-.'],
[r'\unsure{he|be}',r'he','The source types he, with the open shoulder of h; retain the slip rather than normalize to be.'],
[r'\margin{(22) * For a proper map of paracompact spaces, this condition \unsure{means that the fibers are} ``\unsure{aspheric}\'\' \unsure{(``weakly contractible\'\' in the Čech sense)}}',r'PLACEHOLDER','TEMP']
],'diffs':{
1828:['for such topology','There is no article a between such and topology.'],
1829:[r'\inserted[typed]{many}','Many is typed above the line.','correct layer'],
1831:['25.','Only the section number appears; the arXiv title is absent.'],
1845:[r'For a proper map of paracompact spaces, this condition just means that the fibers are ``aspheric\'\' namely ``contractible\'\' (in the Čech sense)','The rotated note includes just and namely, and explicitly qualifies contractibility in the Čech sense; it does not literally say weakly contractible. Pencil shading leaves cancellation status uncertain.','correct transcription'],
1846:['unless we find a still coarser','Still is typed and present.'],
1848:[r'\inserted[typed]{Hot-}','The Hot- prefix is typed; the insertion curve leaves equi- live.','correct layer'],
1849:['he','The typed first letter is h, not b.','settled on image'],
1850:[r'\deleted{this}','The final this is crossed with a pen line; its omission from the live reading must be respected.']},
'unsure':[[r'\unsure{l}','The extra letter in dialectics is obscured by cancellation; retain the tentative l.'],['*','The footnote call begins with a clear asterisk.'],['he','The initial glyph is h in the scan.'],['just means that the fibers are','The rotated margin note reveals the previously omitted just and the whole following phrase.'],['aspheric','The quoted handwritten word is legible.'],[r'namely ``contractible\'\' (in the Čech sense)','The note says namely contractible, with the qualification in the Čech sense; no secure word weakly appears.']],
'illegible':[[r'\illegible{1}','The live 25 is clear but its typed predecessor remains covered.'],[r'\illegible{1}','The left canceled margin call has possible digits 21 but cannot be securely read through the hatching.'],[r'\illegible{1}','The second canceled marginal call is not recoverable.']],
'notes':['The live section number is 25; the earlier typed digits are unreadable.','The two hooked arrows were reconstructed instead of approximate bracket text.','The overstrikes in realizations and irrespective agree with the source; the canceled extra letter in dialectics remains doubtful, and introduce is a typed overstrike with readable live letters.','Both canceled call marks remain unreadable; a possible 21 at left is not promoted to certainty.','The rotated margin note is readable as just means and namely contractible in the Čech sense; broad pencil shading makes its cancellation status uncertain.','The call contains a clear star followed by raised 22.','The pen curve places the typed Hot- before equi- without canceling the latter.','The body types he, a slip retained diplomatically.'],
'evidence':'Both halves inspected and the long diagonal note rotated and enlarged. Section 25 introduces Hot-equivalence and corrects inverse to direct image while moving the prime between the two sheaf topologies. Many and Hot- are typed additions; the three arrows are handwritten. The margin note says the condition just means that the fibers are aspheric, namely contractible in the Čech sense; its pencil shading has uncertain cancellation force. The body clearly types he in the final sentence, and this is deleted at the end. The prior section number and both crossed margin calls remain unread.'}
# Use the exact source forms for apostrophes, avoiding literal backslashes before them.
from pathlib import Path
from review_134_3_4 import TEXT
s=(TEXT/'transcription/ps_pages/ps_134-3_024.tex').read_text()
for e in conf['edits']:
 if 'T\\prime' in e[0]:
  e[0]=e[0].replace('T\\prime',"T'");e[1]=e[1].replace('T\\prime',"T'")
conf['edits'][-1]=[s[s.index(r'\margin{(22)'):].strip(),r'''\margin{\unsure{\diagram{\begin{tikzpicture}[baseline=(n.base)]\node[draw,circle,inner sep=4pt] (n) {(22)};\end{tikzpicture}} * For a proper map of paracompact spaces, this condition just means that the fibers are ``aspheric'' namely ``contractible'' (in the Čech sense)}}''','The rotated note recovers just, means that the fibers are, aspheric, and namely contractible in the Čech sense. Reconstruct its circled call and retain doubt about cancellation under broad pencil shading.']
for v in [conf['diffs'][1845],conf['unsure'][-1]]:v[0]=v[0].replace("\\'","'")
(OUT/'review_notes/ps_134-3_024.json').write_text(json.dumps(conf,ensure_ascii=False,indent=2));save_review(conf)
