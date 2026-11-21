#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re
root=Path(__file__).resolve().parents[1];r=root/'research';now=datetime.now(timezone.utc).isoformat()
p=r/'DP61_integrated_fragment.tex';before=p.read_text()
after=re.sub(r'\\texttt\{([^{}]*(?:/|\.lean)[^{}]*)\}',lambda m:'\\path{'+m.group(1)+'}',before)
after=after.replace('\\path{DataParams₂.lean}','\\path{DataParams}\\textsubscript{2}\\path{.lean}')
p.write_text(after)
main=root/'DP_MULT.tex';s=main.read_text()
p=r/'DP59_integrated_fragment.tex';old=p.read_text();new=old.replace(' A=\\operatorname{Jac}(y^2=x^7-1),\\quad g=3,\\quad\n \\delta=1+2(a+a^2+a^4),\\quad \\delta^2=-7,\\quad\n w_0=(1-\\delta)/2,\\quad\n L=(1,w_0)^*\\mathcal P_\\lambda.',' \\begin{gathered}\n A=\\operatorname{Jac}(y^2=x^7-1),\\qquad g=3,\\qquad \\delta^2=-7,\\\\\n \\delta=1+2(a+a^2+a^4),\\qquad w_0=(1-\\delta)/2,\\\\\n L=(1,w_0)^*\\mathcal P_\\lambda.\n \\end{gathered}')
assert old!=new and s.count(old)==1
p.write_text(new);s=s.replace(old,new)
anchor='\\section{Cote 54, Cartier duality, and the crystalline setting}'
scopes={
 61:'Read COMPLETE intended proposition, complete proof and exact-source paragraph in an untruncated output, after the earlier complete memo read. All row formulas, reversal, positivity, sufficient completion, zero evaluation, fixed-window inequalities and qualifications are preserved. Subsequently reviewed only the source-path wrapping and subscript formatting changes; no mathematical change.',
 62:'Read COMPLETE final memo sections1-9 and COMPLETE intended theorem/proof/scope in untruncated outputs. Checked relative finite-flat hypotheses, odd normalization over arbitrary test schemes, overlap independence and nonreduced uniqueness, torsion-point extension, all-prime integral action, canonical metric isometries and Haar norms, tuple-field degrees and exact limits. Subsequently directly opened/read Stacks0BX7 and0BX5 and reviewed the added exact neighborhood-extension and separated gluing paragraph; remaining mathematical content is unchanged.',
 64:'Read COMPLETE intended theorem, full proof and final adaptive-selection calculation, comparing with the previously whole-read memo. Checked every uniformity qualifier, all saturated floor and entropy formulas, zero-order cases, exact analytic locator, mod7 sets and selected-theta/nonabelian limits. Full proof preserved.'
}
for n in (61,62,64):
 fragment=(r/f'DP{n}_integrated_fragment.tex').read_text()
 assert fragment.count('\\begin{proof}')==1 and fragment.count('\\end{proof}')==1
 assert f'\\label{{DP{n}}}' not in s
 s=s.replace(anchor,fragment+'\n\n'+anchor)
 data={'statement':f'DP{n}','recorded_utc':now,'who':'/root','model':'GPT-6 Astra Pro','effort':'not exposed by runtime','type':'targeted proof check','scope':scopes[n],'outcome':'PASS complete intended proof and stated targeted post-read refinements; no Lean execution or machine formalization.','file':f'DP{n}_integrated_fragment.tex','sha256':hashlib.sha256(fragment.encode()).hexdigest()}
 (r/f'DP{n}_root_integrated_review_metadata.json').write_text(json.dumps(data,indent=2)+'\n')
main.write_text(s)
(r/'DP59_display_layout_delta.json').write_text(json.dumps({'recorded_utc':now,'statement':'DP59','who':'/root','scope':'Reflowed only the opening displayed geometric data into three gathered lines, after build reported24.53pt overfull. All symbols and assertions preserved.','old_sha256':hashlib.sha256(old.encode()).hexdigest(),'new_sha256':hashlib.sha256(new.encode()).hexdigest(),'main_count':s.count(new)},indent=2)+'\n')
print(json.dumps({'recorded_utc':now,'integrated':[61,62,64],'counts':{str(n):s.count((r/f'DP{n}_integrated_fragment.tex').read_text()) for n in (61,62,64)},'main_bytes':main.stat().st_size}))
