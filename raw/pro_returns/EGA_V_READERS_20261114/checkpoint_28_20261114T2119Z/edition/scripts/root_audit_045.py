from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).parent))
import audit_record as ar
from root_review_support import ReviewedPage
k='ega25_25_045';p=ReviewedPage(ar.source_path(k).read_text())
p.change(r'\unsure{49|41}',r'41','The second digit is a long upright1; the final handwritten foliation reads41.','doubt-resolved')
p.change(r"\unsure{U'} h$^{-1}$",r"\unsure{U'|U} = h$^{-1}$",'An equals sign is visible between the doubtful U/prime and h in the typed cancellation.','corrected-reading')
p.change(r'\xout{xxxxxx} cela',r'\xout{comme} cela','The enlarged cancelled letters before cela read comme.','recovered-reading')
p.change(r'\xout{xxxxxx} En termes',r'\xout{Soit \illegible{1}} En termes','The last cancelled group begins with readable Soit; its following crossed group remains illegible.','recovered-reading;doubt-added')
p.change(r'\longrightarrow',r'\hand{\longrightarrow}','All long arrows are penned.','corrected-layer')
p.change(r'\rightarrow',r'\hand{\rightarrow}','The short arrow is penned.','corrected-layer')
p.change(r'\simeq',r'\hand{\simeq}','The isomorphism sign is penned.','corrected-layer')
p.change(r'\subset',r'\hand{\subset}','Both inclusion signs are handwritten.','corrected-layer')
p.change(r'\overline{Y^1}',r'\overset{\hand{\rule{1.1em}{0.35pt}}}{Y^1}','The bar above the typed Y and exponent1 is added by pen. Its scope remains the entire Y-with-exponent.','corrected-layer')
p.change(r'\over{ant}{\unsure{e}}',r'\over{ant}{e}','A final handwritten e replaces the typed ending ant.','doubt-resolved')
p.change(r'\inserted{\unsure{$Y^{\text{sup sing}}$}}',r'\inserted{\deleted{$\underline{Y}^{\text{sup sing}}$}}','The interlinear Y sup sing is underlined and crossed by a clear pen stroke; it cannot remain live.','corrected-deletion;doubt-resolved')
p.change(r'\inserted{\unsure{contenu dans} $Y^{\text{sing}}$, \unsure{de dim r}}',r'\inserted{\deleted{contenu} fait que $\underline{Y}^{\text{sing}}$, de dim r}','The faint earlier contenu is crossed; the darker replacement reads fait que Y sing, de dim r. The Y is underlined. No missing minus1 is supplied.','corrected-reading;doubt-resolved')
p.change(r"\inserted{\unsure{est défini par l'annulation d'une section} D \unsure{d'un Module inversible}}",r"\inserted{est défini par l'annulation d'une section D d'un Module inversible}",'The long handwritten sentence is legible at enlargement, including capital D and Module.','doubt-resolved')
p.change(r'\unsure{n}alé',r'\over{g}{n}alé','The second character of the transposed pair is a handwritten n over the typed g; the pair reads final gn.','doubt-resolved;corrected-layer')
p.change(r'\margin{\unsure{$\ast$}}',r'\margin{\hand{\unsure{$\cdot$}}}','The left mark is a compact blot with a short tail, without a secure star shape. A doubtful dot records its physical presence and uncertain function.','doubt-refined')
p.change(r'\hand{\unsure{´}}',r'\hand{´}','The small detached mark is a clearly slanted acute-like pen stroke; its grammatical function is not inferred.','doubt-resolved')
p.change(r'\margin{45}',r'\margin{\hand{45}}','The lower foliation is pencilled.','corrected-layer')
p.note('7-18','upper proof','upper proof','confirmed','Every line was read against both halves. All the upper Y exponents are typed1 and are retained; f ermé, the bare product x, all domains and codomains, and the clipped isomor/phisme are preserved.','full-line-check')
p.note('19-25','reference and inequality overwrites','reference and inequality overwrites','doubt-retained','The final references9,8,10 and9 are clear; their older digits remain uncertain. The blackened relation before r-2 has two heavy bars and does not securely settle the final less-than-or-equal reading.')
p.note('22','d overprint','d overprint','doubt-retained','The small overwritten character after d remains doubtful e over u; no grammatical restoration decides it.')
p.note('34-35','deleted handwritten word','deleted handwritten word','unresolved','The horizontal cancellation crosses a compact handwritten phrase. Its internal word boundaries and surviving traces do not give a secure reading.')
p.note('28-39','last paragraph','last paragraph','confirmed','Every line of the remark was compared, including lèensemble, the normal/geometrically normal/unibranch terminology, the handwritten full stop, and the clipped final oscul.','full-line-check')
s,d=p.finish()
old=r'\inserted{\unsure{$\underline{Y}^{\vee}$} \unsure{$r_{\text{sing}} = \rho$} \illegible{1}}'
assert old in s;s=s.replace(old,'')
anchor=r'8.\over{\unsure{7}}{8}.\hand{,} dim'
new=r'8.\over{\unsure{7}}{8}.\hand{,} \inserted{$\underline{Y}^{\text{sup}}\text{sing}=\emptyset$ ou} dim'
assert anchor in s;s=s.replace(anchor,new)
d.append(dict(line='19-21',before=old,image=new,decision='recovered-reading;corrected-placement',reason='The circled note reads Y sup sing equals empty, ou; its hook points immediately before dim, not to the previous proof. The handwritten sing sits on the lower baseline beside the raised sup, and that placement is preserved.',category='insertion-placement'))
old=r"\inserted{est défini par l'annulation d'une section D d'un Module inversible} \deleted{dim} $\underline{Y}^{\text{sing}}$\hand{\unsure{sup sing}} \deleted{= r-1}"
new=r"\deleted{dim} $\underline{Y}^{\over{\text{sing}}{\text{sup sing}}}$ \deleted{= r-1} \inserted{est défini par l'annulation d'une section D d'un Module inversible}"
assert old in s;s=s.replace(old,new)
d.append(dict(line='24',before=old,image=new,decision='corrected-placement;corrected-layer',reason='The long bracket carries the handwritten predicate to the position after the typed Y and its overwritten exponent. Sup sing is written over the typed sing; it is not an independent phrase after the formula. The cancelled dim and equals r-1 remain in the diplomatic branch.',category='insertion-placement'))
s=s.replace(r'\scanpage{25/45}',r'\scanpage{25/45}'+'\n% NOTE: The small left-margin blot has uncertain function. The detached acute-like pen stroke over lesquels is retained without assigning grammatical force. The circled insertion places sing on a lower baseline than sup.\n',1)
ar.save(k,s,d,0,'Both halves fully compared; dense middle paragraph, circled note and hooks enlarged, all overwritten references and crossed groups inspected individually.')
print('Saved45;',ar.aggregate(),'pages checked.')
