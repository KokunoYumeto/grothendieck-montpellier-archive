from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).parent))
import audit_record as ar
from root_review_support import ReviewedPage
k='ega25_25_049';p=ReviewedPage(ar.source_path(k).read_text())
p.change(r'\mspage{45}',r'\mspage{\hand{45}}','The upper45 is penned.','corrected-layer')
p.change(r'\mspage{49}',r'\margin{\hand{49}}','The lower49 is pencil archive foliation.','corrected-layer')
p.change(r'\xout{xxxbiex}',r'\xout{ou bien}','The cancelled words read ou bien.','recovered-reading')
p.change(r'\xout{xxxbien}',r'\xout{ou bien}','The second cancelled pair also reads ou bien.','recovered-reading')
p.change(r'\deleted{$X_i$}',r'\deleted{$X_{\unsure{i|a}}$}','The small index has overlapping i/a-like outlines; its typed/pen layering is not securely distinguishable.','doubt-added')
p.change(r'si\unsure{.}',r'si,','The detached mark after si has a clear comma tail.','doubt-resolved')
p.change(r'\inserted{géom}',r'\inserted[typed]{géom}','The interlinear géom has typewriter serifs and spacing.','corrected-layer')
p.change(r'\zeta',r'\xi','All repeated handwritten index/point letters have the curled xi form.','corrected-reading')
p.change(r'\check{P}',r'\overset{\hand{\vee}}{P}','P is typed and only its check is handwritten.','corrected-layer')
p.change(r'\xout{soit}',r'\deleted{soit}','The cancellation of soit in b is a continuous pen strike, not typewriter crosses.','corrected-layer')
p.change(r'\unsure{\hand{,}}',r'\unsure{,|x}','The small sign following2 is heavily overprinted and x-like; neither its character nor its physical layer is settled.','doubt-refined;layer-unsettled')
p.change(r'X \geqslant',r'X \hand{\geqslant}','The inequalities in the first paragraph are penned.','corrected-layer')
p.change(r'dim$\geqslant$',r'dim$\hand{\geqslant}$','The first and later codimension/dimension bounds have handwritten inequality signs.','corrected-layer')
p.change(r'codimension $\geqslant$',r'codimension $\hand{\geqslant}$','This inequality sign is penned.','corrected-layer')
p.change(r'resp\unsure{:}',r'resp:','The image has two clear vertically separated dots.','doubt-resolved')
p.change('exceptionnel de codimension',r'exceptionnel de codim\unsure{e|m}nsion','The second middle type position has competing e/m outlines; the overprint is retained.','doubt-added')
p.change(r'\hand{donc}',r'\over{\unsure{il}}{donc}','The penned donc overlaps surviving typed i/l-like stems. The older reading remains doubtful.','corrected-layer;doubt-added')
p.change(r'\over{o}{où}',r'\over{ou}{où}','Both o and u are typed under the correction, with ink on o and the added grave accent over u. The earlier source omitted u from the underlayer.','corrected-layer')
p.note('7','Xi replacement','Xi replacement','confirmed','The inserted Xi points after composante irréductible; the old X after dimension1 is separately struck, with its small index unresolved.')
p.note('12-18','inequalities and typography','inequalities and typography','confirmed','Every inequality was checked against the scan. The handwritten hyphen, singular point in point lisses, feminine normale, and clipped complé continuation remain.')
p.note('22-25','cancelled note and raised sup sing','cancelled note and raised sup sing','confirmed','The full typewriter-cancelled note was enlarged. Its first lines are readable; the raised sup sing belongs to the final g formula. Prime marks occur above both component letters in the second line.')
p.note('27-41','remark in full','remark in full','confirmed','Both halves were read completely, including receuillir, the internal3.4/5.12 references, the underlined fermé, the claims about codimension, and the author’s final reservation about Rk. No missing hypotheses are supplied.','full-line-check')
p.note('41','des conditions','des conditions','confirmed','The final-line words have a faint displaced type shadow but remain readable as des conditions; the doubled outlines are recorded without inventing a second word.')
s,d=p.finish()
old="\\inserted[typed]{et soit}\n"
assert old in s;s=s.replace(old,'',1)
anchor=r'formée de points lisses de X \xout{ou bien}'
new=r'formée de points lisses de X \inserted[typed]{et soit} \xout{ou bien}'
assert anchor in s;s=s.replace(anchor,new)
d.append(dict(line='8-9',before=old+' before formée',image=new,decision='corrected-placement',reason='The typed interlinear et soit stands directly above the second ou bien and belongs after lisses de X.',category='insertion-placement'))
old="\\xout{(J'aixoubliéxxdaxavantxa)xetxb)xxd'indiquerxl'hypothèse}\n\\xout{suivante,xtoujoursxvérifiéexenxcarx0xxpourxtoutexcompxirrxX$_i$xdexX$_i$,}\n\\xout{xxxxsupxsingx}\n\\xout{\\unsure{g(X$_i$}xxxxxxxxxx)}"
new="\\xout{(J'ai oublié da avant a) et b) d'indiquer l'hypothèse}\n\\xout{suivante, toujours vérifiée en car 0 pour toute comp irr $X'_i$ de $X'_i$,}\n\\xout{$g(\\underline{\\unsure{X|Y}}_i^{\\mathrm{sup\\ sing}})$}"
assert old in s;s=s.replace(old,new)
d.append(dict(line='21-24',before=old,image=new,decision='recovered-reading;corrected-formula-placement',reason='The visible type letters are recovered from the overstrikes, including the literal da and both primes. Sup sing is raised above the last g-formula argument and is joined to it. That underlined argument retains X/Y uncertainty; no mathematical correction is inferred.',category='cancelled-reading'))
s=s.replace(r'\scanpage{25/49}',r'\scanpage{25/49}'+'\n% NOTE: The small mark after dimension at most2 has unsettled character and layer. The first cancelled component index retains i/a uncertainty. The final des conditions has a faint displaced type shadow.\n',1)
ar.save(k,s,d,0,'Both full halves inspected; every cancelled word and the complete crossed note enlarged, typed et soit relocated, dot/comma/colon and all inequalities checked.')
print('Saved49;',ar.aggregate(),'pages checked.')
