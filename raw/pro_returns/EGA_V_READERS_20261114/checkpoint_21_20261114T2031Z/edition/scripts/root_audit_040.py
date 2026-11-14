from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).parent))
import audit_record as ar
from root_review_support import ReviewedPage
k='ega25_25_040';p=ReviewedPage(ar.source_path(k).read_text())
p.change(r'\underline{\Omega}',r'\hand{\underline{\Omega}}','All Omegas and their underlines are penned; the indices remain typed.','corrected-layer')
p.change(r'\hand{\unsure{\check{\mathcal{N}}}}',r'\hand{\check{\underline{\nu}}}','The repeated angular nu, underline and check are legible and match the forms on the adjoining pages.','doubt-resolved')
p.change(r'\hand{\unsure{\mathcal{N}}}',r'\hand{\underline{\nu}}','The unchecked handwritten nu and its underline are legible.','doubt-resolved')
p.change(r'\unsure{\nu|\mu}',r'\mu','The three section symbols have the same mu shape as the cancelled mu passage on39; their strokes are legible in the enlargements.','doubt-resolved')
p.change(r'\inserted{transposée de la}',r'\inserted[typed]{transposée de la}','These words are typewritten above the line; the bracket is penned.','corrected-layer')
p.change(r'\xout{xxxxxxx}',r'\xout{\unsure{relative}}','The crossed seven-letter word has visible r, l, t and v/e outlines supporting relative; the densely overprinted middle remains doubtful.','partly-recovered-cancelled-reading')
p.change(r'\hand{\check{\underline{E}}}',r'\overset{\hand{\vee}}{\underline{E}}','Only the check is penned; the E and underline are typed.','corrected-layer')
p.change(r'\check{P}',r'\overset{\hand{\vee}}{P}','The check above P is penned.','corrected-layer')
p.change(r'\rightarrow',r'\hand{\rightarrow}','Both arrows in the running text are drawn in pen.','corrected-layer')
p.note('5','36 foliation','36 foliation','confirmed','The final6 is visible. Its thickened upper stroke does not securely disclose a prior numeral.')
p.note('8','top first zero','top first zero','doubt-retained','There are two overlapping hollow loops, the second lower and right of the first, with a crossing stroke at their junction. Their operation cannot be settled; the zero doubt remains. An independent inspection agreed.')
p.note('9','top script letter and tensor expression','top script letter and tensor expression','doubt-retained','The initial pen glyph has an upper-left cup, a tall descending right stroke and a lower return; script T remains tentative. The check belongs over P in the index. The typed opening parenthesis, comma and crowded O/Z overprinting remain uncertain rather than being repaired.')
p.note('8-12','diagram arrows and zeros','diagram arrows and zeros','confirmed','All horizontal, vertical and diagonal connectors are pen-drawn. Beta is dashed and alpha solid. The upper and lower zeros of the middle vertical column are handwritten; the other lower/side zeros are typed.')
p.note('17','transposée insertion','transposée insertion','confirmed','The pen bracket joins the typed words before suite analogue; it does not cancel the latter words.')
p.note('25','doit and mécanique','doit and mécanique','confirmed','The typewriter overstrikes leave the final words doit and mécanique legible.')
p.note('9,23-24','X/Y indices','X/Y indices','confirmed','The diagram and both following differential-module formulas visibly have X/Y, not X/S. The notation is retained and discussed in the guide.')
p.note('28-30','checked and unchecked nu','checked and unchecked nu','confirmed','The first submodule line has a checked nu; the next submodule and final projectivization have unchecked nu. No notational repair is imposed.')
p.note('15-34','remaining words and formulas','remaining words and formulas','confirmed','Both halves were compared completely, including the tensor/twist factors, missing close parenthesis in the top entry, final(1), unaccented couté and the unfinished final sentence.','full-line-check')
s,d=p.finish()
a=s.index(r'\diagram{');z=s.index(r'\end{tikzcd}}',a)+len(r'\end{tikzcd}}');old=s[a:z]
new=r'''\diagram{\begin{tikzcd}
 & \unsure{0} & \hand{0} & & \\
 & \hand{\underline{\Omega}}^1_{X/Y} \otimes \underline{O}_Z(1,0) \arrow[u] & \hand{\unsure{\mathcal{T}}}_{\overset{\hand{\vee}}{P}/S}\,\unsure{(\otimes,\underline{O}_Z(0,-1)} \arrow[u] & & \\
0 \arrow[r] & \hand{\underline{\Omega}}^1_{P/S} \otimes \underline{O}_Z(1,0) \arrow[r] \arrow[u] & E\otimes\underline{O}_Z \arrow[r] \arrow[u] & \underline{O}_Z(1,0) \arrow[r] & 0 \\
 & \hand{\check{\underline{\nu}}}_{X/P} \otimes \underline{O}_Z(1,0) \arrow[u] & \underline{O}_Z(0,-1) \arrow[u] \arrow[ul, dashed, "\hand{\beta}"'] \arrow[ur, "\hand{\alpha}"'] & & \\
 & 0 \arrow[u] & \hand{0} \arrow[u] & &
\end{tikzcd}}
% NOTE: All diagram connectors are drawn in pen. The script-letter entry stands directly above E tensor O_Z; its check is above the indexed P. The first top zero has two overlapping loops of unresolved operation. The top tensor expression includes an opening parenthesis and comma, with O/Z overprinting.'''
s=s[:a]+new+s[z:]
d.append(dict(line='7-13',before=old,image=new,decision='corrected-diagram-placement',reason='The scan aligns the script-letter entry and upper0 directly above E tensor O_Z. The draft placed them one column too far right, leaving the E arrow aimed at an empty cell. The corrected matrix follows the actual vertical column and places the check above P; the visible comma after tensor is retained.',category='diagram'))
ar.save(k,s,d,0,'Both complete halves and enlarged zero loops, script entry, foliation, typed insertion, crossed word, mu symbols and prose overstrikes read; every diagram node and connector compared.')
print('Saved40;',ar.aggregate(),'pages checked.')
