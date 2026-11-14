from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).parent))
import audit_record as ar
from root_review_support import ReviewedPage
k='ega25_25_042';p=ReviewedPage(ar.source_path(k).read_text())
p.change(r'\unsure{\nu}',r'\nu','The opening handwritten nu is legible and agrees with the adjacent pages.','doubt-resolved')
p.change(r'\hand{\unsure{\check{}}}\!P',r'\overset{\hand{\vee}}{P}','The opening check is clear and stands above the typed P.','doubt-resolved;corrected-layer')
p.change(r'\longrightarrow',r'\hand{\longrightarrow}','The opening arrow is penned.','corrected-layer')
p.change(r'\inserted{géom.}',r'\inserted[typed]{géom.}','The letters are typed; the curved insertion bracket is penned.','corrected-layer')
p.change(r'\unsure{\xi|\zeta}',r'\xi','The point symbol has the curled xi form.','doubt-resolved')
p.change(r'\underline{\Omega}',r'\hand{\underline{\Omega}}','The diagram Omegas and underlines are handwritten.','corrected-layer')
p.change(r'\check{P}',r'\overset{\hand{\vee}}{P}','The diagram checks are pen marks above typed P.','corrected-layer')
p.change(r'\unsure{\nu.\mu}',r'\unsure{\nu}.\mu','The black mu is legible; the faint preceding pencil symbol remains uncertain. The small intervening dot remains.','partly-resolved-reading')
p.change(r'\underline{\omega}',r'\hand{\underline{\omega}}','The lower-left omega and underline are handwritten.','corrected-layer')
p.change(r'\over{V}{\nu}',r'\hand{\nu}','The enlargement shows a continuous pen nu without a separately readable underlying typed V.','corrected-layer')
p.change(r'\unsure{f propre}',r'tjrs','The enlarged abbreviation reads t-j-r-s, confirmed independently; it is retained without expansion.','doubt-resolved')
p.change(r'\xout{Saxsaxtaxqusxx$\underline{Y}$xxxxx}',r'\xout{\illegible{1} sorte que $\underline{Y}^{\mathrm{sing}}$}','The words sorte que and the superscript sing are readable under the x impressions; the initial cancelled word remains obscured.','partly-recovered-cancelled-reading')
p.change(r'\xout{xxxxx} Alors',r'\xout{\unsure{Alors}} Alors','The crossed word shows an initial A and following l/r/s traces; Alors remains tentative.','partly-recovered-cancelled-reading')
p.change(r'\margin{42}',r'\margin{\hand{42}}','The lower-left foliation is pencilled.','corrected-layer')
p.note('8','raised supsi','raised supsi','corrected-attachment','The raised typed letters begin immediately above/right of the cancelled Y, with no prose-insertion leader. They belong to its superscript. The baseline cancellation crosses Y, while most raised letters are not directly struck; their deletion status follows attachment to the cancelled expression. An independent visual review agreed.')
p.note('21','blob beside top0','blob beside top0','unresolved-mark','The top0 is readable; a separate dense round/squared ink blot beside it has no secure alphabetic value or editorial function.')
p.note('22-25','diagram layout and arrows','diagram layout and arrows','confirmed','Every node and connector was traced. All connectors are pen-drawn. The lower-middle0 is also penned. The lower-right nu label has a fainter parallel old trace, without a separately readable second letter.')
p.note('23-24','Y1 following differential module','Y1 following differential module','corrected-placement','The unparenthesized Y1 at the lower-middle entry is written at the same subscript level as P/S, as at the upper X/S Y1 entry; it is moved to that level without changing the stated notation.')
p.note('37','corollary number','corollary number','unresolved','The final8 is clear; the overlapping underlying numeral remains unreadable.')
p.note('7-40','remaining text','remaining text','confirmed','Both halves were read in full, retaining quelconqque, symtaxe, the bottom X/Y, exponent-2 and the exact twist factors. The f:X to P insertion and(tjrs lisse sur k) placement brackets were followed.','full-line-check')
s,d=p.finish()
old=r'\xout{yx/x$\underline{Y}$xxxxx} \inserted[typed]{\unsure{supsi}}'
new=r'\xout{yx/x$\underline{Y}^{\unsure{supsi}}$xxxxx}'
assert old in s;s=s.replace(old,new)
d.append(dict(line='8',before=old,image=new,decision='corrected-attachment',reason='The raised typed supsi is positioned as the superscript of cancelled Y. Its inclusion in the cancelled expression is based on that physical attachment; no direct strike through every raised letter is asserted.',category='placement'))
old=r'\hand{\underline{\Omega}}^1_{\overset{\hand{\vee}}{P}/S}\ \underline{Y}^1'
new=r'\hand{\underline{\Omega}}^1_{\overset{\hand{\vee}}{P}/S\,\underline{Y}^1}'
assert old in s;s=s.replace(old,new)
d.append(dict(line='24',before=old,image=new,decision='corrected-diagram-script-level',reason='The Y1 glyph is at the lower script level alongside P/S in the image. No parentheses or change of letters are added.',category='diagram'))
old=r'& & 0 \arrow[u] & &';new=r'& & \hand{0} \arrow[u] & &'
assert old in s;s=s.replace(old,new)
d.append(dict(line='25',before=old,image=new,decision='corrected-layer',reason='The lower-middle zero consists of irregular pen loops, whereas the side zeros are typed.',category='diagram'))
s=s.replace(r'\scanpage{25/42}',r'\scanpage{25/42}'+'\n% NOTE: The raised supsi belongs to the cancelled Y as a superscript; the cancellation crosses the base expression. All diagram arrows are penned. A separate dense blot beside the upper0 has no secure character value.',1)
ar.save(k,s,d,0,'Both halves and enlarged supsi attachment, diagram labels, continuous nu, corollary number, tjrs abbreviation and cancelled words inspected; independent attachment/abbreviation review obtained.')
print('Saved42;',ar.aggregate(),'pages checked.')
