"""Explicit final wording corrections, not automatic verdict generation."""
from pathlib import Path
import json
B=Path(__file__).resolve().parents[1]
items=json.loads((B/'items.json').read_text())
claims=json.loads((B/'claims.json').read_text())
new560='Let P be a nonzero squarefree element of Z[T] defining a genuine quadratic extension of Q(T). Then B=Z[T,S]/(S²−P) is a hypersurface and satisfies S2. If all its height-one local rings are normal, Serre’s criterion makes B normal everywhere; no finite exceptional nonnormal set remains.'
new561='Let P=εqQ be a nonzero squarefree element of Z[T], where ε∈{±1}, q is its positive squarefree content and Q is primitive with positive leading coefficient. Assume P defines a genuine quadratic extension of Q(T). The normalization over Z[T] is generically étale over every rational prime if and only if q=1 and P≡r² modulo 4 for some r∈Z[T]. In that case write P=r²+4h. The full normalization is Z[T,u]/(u²−ru−h), with u=(S+r)/2; it is finite étale over D(P).'
for i in items:
    if i['id']=='SA16-583':i['statement']=new560
    if i['id']=='SA16-585':i['statement']=new561
for c in claims:
    if c['id']=='C-SA16-560':c['statement']=new560
    if c['id']=='C-SA16-561':
        c['statement']=new561
        c['present_status']='True for the stated squarefree radicand and its normalization. Both directions at generic points of integer fibres are proved in proof_notes.md. The original S²=P order itself is never étale in characteristic two.'
    if c['id']=='C-SA16-558':c['statement']='A[[T]]/(T²+2αT+b) is the T-adic completion of B. If b≠0 in the DVR square-residue case, (T) is maximal-ideal-primary, so this is also the local completion even when A is not complete. When b=0 the two topologies need not agree; A=Z_(2), a=α=1 is a split counterexample to an unrestricted interpretation as maximal-ideal completion.'
    if c['id']=='C-SA16-526':c['fate']='Trace-zero normalization requires 3 to be invertible, exactly as stated. LG-ALG.'
    if c['id']=='C-SA16-536':c['fate']='The canonical ratio construction proves the asserted principal-parts sequence comparison. LG-LINEAR.'
for name,obj in [('items',items),('claims',claims)]:
    (B/(name+'.json')).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
old='Grothendieck manuscript modernization: public preprint 2611.00125v2'
new='Énoncés des notes de travail de Grothendieck démontrés en Lean 4, et questions ouvertes'
for name in ['references.bib','literature_notes.md','source_metadata.json']:
    p=B/name;p.write_text(p.read_text().replace(old,new))
p=B/'proof_notes.md';s=p.read_text()
s=s.replace('Now let `P=εqQ` be squarefree and primitive in the sense specified in the item, defining a genuine quadratic field over Q(T).',
    'Now let `P=εqQ` be a nonzero squarefree element of Z[T], with ε a sign, q its positive squarefree content, and Q primitive with positive leading coefficient. Assume it defines a genuine quadratic field over Q(T).')
p.write_text(s)
print('Clarified content q versus primitive factor Q in the global quadratic statement; no mathematical verdict changed.')
print('Corrected Hua title from the opened first page; corrected a project-note heading range.')
