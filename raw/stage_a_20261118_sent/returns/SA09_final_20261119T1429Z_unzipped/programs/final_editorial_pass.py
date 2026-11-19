#!/usr/bin/env python3
"""Apply individually reviewed editorial corrections to root deliverables.

This script does not read or modify source transcriptions or assign verdicts.
"""
from pathlib import Path
import json,re

R=Path(__file__).resolve().parents[1]
p=R/'SA09_dossier.md'
s=p.read_text()
changes={
 'The eighteenth-transport programme':'The eighteen-transport programme',
 'The rational function written on scan19 has the same eight distinguished points as the diagram on78.':'The seven marked finite points on scan78 match the finite part of the eight-point special-fibre set of the rational function written on scan19; infinity is implicit in the later projective-line diagram.',
 'Exact modern topological statements and the source\'s broader deferred groupoid comparison are distinguished in CL-SA09-138M-019–022.':'Quintas (1965, Theorem (c), (h), and equation (2.2)) supplies an exact pre-manuscript homotopy-group result; Yagasaki (2000, Theorem 1.1 and Lemma 2.1(i)) supplies the stronger contractibility statements in the specified setting. These and the source\'s broader deferred groupoid comparison are distinguished in CL-SA09-138M-019–022.',
 'Higher-rank rational radical groups have the exact intrinsic quadratic-entanglement index 2^r after the correct saturation.':'For a rank-r rational multiplicative group Γ, put Γ_∞={x : x^n∈Γ for some n≥1} and Γ_0=Γ_∞∩Q^×. The exact quadratic-entanglement index 2^r applies in the intrinsic ambient group A=Aut_{Γ_0}(Γ_∞). It does not automatically apply in coordinates chosen from unsaturated generators.',
 'the separate lead table preserves reports whose intended endpoint was not established.':'the separate lead table preserves the original project leads with their updated verification status, including leads whose selected endpoints were subsequently read. `SA09_project_links.tsv` separately collects the checked project correspondences; no project report is silently promoted into an established result.',
 '- Bühler, T. (2009). Exact categories. arXiv:0811.1480. Publication chronology and opened version are recorded under `Buhler2009`.':'- Bühler, T. (2009). *Exact categories* (Version 2) [Preprint]. arXiv. https://arxiv.org/abs/0811.1480 . First posted 10 November 2008; opened version dated 22 April 2009. See `Buhler2009` for verification scope.',
}
applied=[]
for old,new in changes.items():
 if old in s:s=s.replace(old,new);applied.append(old[:90])
 elif new not in s:raise ValueError('Expected editorial passage not found: '+old)

anchor='- Roby, N. (1963).'
if '- Quintas, L. V.' not in s:
 pos=s.index(anchor)
 s=s[:pos]+'- Quintas, L. V. (1965). The homotopy groups of the space of homeomorphisms of a multiply punctured surface. *Illinois Journal of Mathematics, 9*(4), 721–725. The full primary scan and exact locators are recorded under `M-Quintas1965`.\n'+s[pos:]
anchor='\nAll formulas, source distinctions'
if '- Yagasaki, T.' not in s:
 pos=s.index(anchor)
 s=s[:pos]+'\n- Yagasaki, T. (2000). *Homotopy types of homeomorphism groups of noncompact 2-manifolds* [Preprint]. https://arxiv.org/abs/math/0010223 . First posted 24 October 2000; exact theorem scopes are recorded under `M-Yagasaki2000`.\n'+s[pos:]

# Readability repairs are confined to this authored English overview. They do
# not alter the quoted diplomatic text or the mathematical data ledgers.
words=['Cote','cote','scan','scans','class','Class','June','January','November','December','September','March','April','August','May','July','October','February','Theorem','Lemma','Example','Mathematics','Actions','by','at','on','in','from','over','through','under','type','types','degree','degrees','conductor','modulo','still','are','gives','the','every','original','received','circulated','revision','preprint','released','dated','publication','pages']
for word in words:
 s=re.sub(r'\b'+word+r'(?=\d)',word+' ',s)
s=re.sub(r'(?<=\d)(?=(?:January|February|March|April|May|June|July|August|September|October|November|December)\b)', ' ',s)
s=re.sub(r'(?<=[,;])(?=\d{4}\b)', ' ',s)
s=re.sub(r'\b(SGA|EGA)(?=\d)',r'\1 ',s)
s=s.replace('ClassC','Class C').replace('classC','class C').replace('classF','class F').replace('ClassF','Class F').replace('classD','class D').replace('ClassD','Class D')
s=s.replace('monoid{','monoid {').replace('group{','group {').replace('of{','of {').replace('class[','class [')
p.write_text(s)

p=R/'project_link_decisions.json'
rules=json.loads(p.read_text())
updates={
 'LM4 C.12,D.12,F.7; LM4_SUCCESSOR B.38,B.39; EXIT_TOWER B.27': 'The source and original note were read. These targets were initially absent from the supplied packet. Selected LM4 C.12/D.12/F.7 and successor B.38/B.39 statements were subsequently retrieved and read; exact checked correspondences are in root_verified_links.tsv and project_endpoint_audit_root.md. EXIT_TOWER B.27 remains unlocated. This mixed original lead is retained as provenance, not as a claim that every named target was checked.',
 'LM7_PUSH E.58,E.65,E.3; EXIT_TOWER E.49; LM6 A.22': 'The source and original note were read. LM7_PUSH E.58/E.65/E.3, the relevant referee scopes and LM6 A.22 were subsequently retrieved and read; see workers/cote138_early/verified_project_links.tsv. EXIT_TOWER E.49 remains unlocated. The mixed original lead preserves its earlier provenance and does not certify any external proof.',
 'MPL_147_003-047 N075; WG2 §1.7 #10 and §Summary #1; INTAKE 20261114 §11.2; WG H5': 'The source and original note were read. Cote145 scans11/24 were subsequently retrieved and checked as a separate correspondence, recorded in workers/cote138_early/additional_folder_links.tsv. Cote147 N075 and the separately named WG2, INTAKE and WG endpoints remain unlocated; no checked-both-ends claim is made for those targets.',
}
for r in rules:
 if r['to'] in updates:r['current_evidence']=updates[r['to']]
p.write_text(json.dumps(rules,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'reviewed_text_corrections':applied,'updated_mixed_project_leads':len(updates),'source_files_modified':0},ensure_ascii=False,indent=2))
