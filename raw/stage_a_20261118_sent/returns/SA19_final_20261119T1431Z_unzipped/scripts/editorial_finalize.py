"""Apply explicitly reviewed prose corrections; render counts from final registers."""
from pathlib import Path
import json,re
B=Path(__file__).resolve().parents[1]
p=B/'SA19_dossier.md';t=p.read_text()
# APA author-year disambiguation: curve duality alphabetically precedes Neron pairing.
if '2020a and 2020b respectively' in t:
    t=t.replace('Suzuki, 2020a','Suzuki, 2020_TEMP').replace('Suzuki, 2020b','Suzuki, 2020a').replace('Suzuki, 2020_TEMP','Suzuki, 2020b')
    t=t.replace('publication years 2022, 2020a and 2020b respectively','publication years 2022, 2020b and 2020a respectively')
t=t.replace('Grothendieck, 1966','Grothendieck & Dieudonné, 1966')
t=t.replace('Grothendieck, 1968, VI.2.3','Grothendieck, 1968a, VI.2.3').replace('Grothendieck, 1968, Exposés II–V','Grothendieck, 1968a, Exposés II–V')
t=t.replace('- Grothendieck, A. (1966).','- Grothendieck, A., & Dieudonné, J. (1966).').replace('troisième partie (with J. Dieudonné).','troisième partie.')
t=t.replace('- Grothendieck, A. (1968). Le groupe de Brauer.','- Grothendieck, A. (1968b). Le groupe de Brauer.')
t=t.replace('- Grothendieck, A. (1968). *Cohomologie locale','- Grothendieck, A. (1968a). *Cohomologie locale')
t=t.replace("*Annales scientifiques de l'École Normale Supérieure, 2*(1)","*Annales scientifiques de l'École Normale Supérieure* (4th series), *2*(1)")
t=t.replace('multiplication-by-\u200bp','multiplication-by-p')
p.write_text(t)
p=B/'SA19_directions.md';t=p.read_text().replace('Grothendieck, 1968, §8.4–8.5','Grothendieck, 1968b, §8.4–8.5');p.write_text(t)
p=B/'workstreams/codex43/proofs.md';t=p.read_text()
old='Over an algebraically closed field k of characteristicp, a labelled extension of α_p by α_p corresponds by finite Dieudonné theory to a two-dimensional k-vector space with a fixed subobject ke_1 and quotient ke_2. Write Fe_1=Ve_1=0, Fe_2=a e_1, Ve_2=b e_1, with the usual σ/σ^{-1} semilinearity. The relations imply p=FV=VF=0.'
new='Over an algebraically closed field k of characteristic p, begin with the exact Dieudonné-module extension 0→k→M→k→0. The operators F and V map M into the submodule and vanish on that submodule, so FV=VF=0 and hence pM=0. Therefore M is a two-dimensional k-vector space with fixed subobject ke_1 and quotient ke_2. Write Fe_1=Ve_1=0, Fe_2=a e_1 and Ve_2=b e_1, with the usual σ/σ^{-1} semilinearity.'
if old in t:t=t.replace(old,new)
p.write_text(t)
print(json.dumps({'editorial_corrections':['APA year and author disambiguation','C8 order of p-torsion argument','confirmed source-scope clarifications retained'],'dossier_words':len((B/'SA19_dossier.md').read_text().split()),'directions':len(re.findall(r'^### RD-SA19-',(B/'SA19_directions.md').read_text(),re.M))}))
