#!/usr/bin/env python3
from pathlib import Path
import csv,re
ROOT=Path(__file__).resolve().parents[1]
fields=['id','statement','status','where_proved','depends_on','manuscript_pages','notes']
agent_ids=set()
for p in (ROOT/'agents').glob('*/results*.csv'):
 agent_ids.update(r['id'] for r in csv.DictReader(p.open()) if r.get('id'))
deps={
'A.101':'explicit interval interpolation; radial Alexander contraction',
'A.102':'Armstrong1970 Theorem2; joint extended-collar hypothesis',
'A.103':'Igusa2025 Theorem7.1; WeibelIII–V; BurgheleaLashof1974II Theorems6.1–6.2; CourtePorcelli2025 Section6.2; Shiota2010',
'A.104':'A.103; split endpoint restriction',
'A.105':'A.101; strict conical blowup',
'A.106':'A.102; A.103; simplicial torsor quotient',
'A.107':'Brown1962 Lemmas1–4 and Theorem1; finite definable collar construction',
'A.108':'definable triangulation; barycentric coordinates',
'A.109':'A.101; A.105; explicit collar/cone attachments',
'A.110':'A.109; interval fixed-point counterexample',
'A.111':'A.101; A.103; A.105; derived homotopy fibre',
'A.112':'A.102; A.104–A.111',
'A.113':'Shiota2010 Theorem2.1 and Lemma3.3; BurgheleaLashof1974II Theorem6.2',
'A.118':'explicit eight-vertex polygon; exact rectangular triangulation and all-link certificate',
'A.201':'definable scalar triangulation; strict tube; nearest-point PL retraction',
'A.202':'A.201; disk-with-normal-whisker local separation',
'A.203':'A.103; A.111; full retained mapping-cylinder data',
'A.301':'120 optionalM0 and M9',
'A.302':'first-order formula induction; parameters and trace criterion',
'A.303':'semialgebraic smooth locus; finite freezing induction; all closed saturated unions',
'A.304':'A.303; connected components; dimension marking',
'A.305':'field zero loci; existential reciprocal trick; all-arity closure',
'A.306':'A.302; coordinate compression; VandenDriesDensePairs1998 Theorem5',
'A.307':'local-link homology; compact semialgebraic triangulation',
'A.308':'explicit metric Tietze proof; compact closed pushout construction',
'A.309':'dimension drop; affine transport of an unrealized cut',
'A.401':'finite relational category; equality-class proof; unique_existential.py',
'A.402':'A.401; regular-image reconstruction',
'A.701':'cyclic-cover monodromy groupoids',
'A.702':'fixed structural triangles; descent',
'A.703':'invariant-sheaf recognition; simply connected local fibres',
'A.704':'A.701–A.703; stable internal descent'
}
pages={
'101':'119/148–149','102':'119/148','103':'119/148','104':'119/148–150','105':'119/149–150','106':'119/148','107':'119/148','108':'119/149','109':'119/150','110':'119/150','111':'119/149','112':'119/150','113':'119/148; A.1(b)',
'118':'119/149; A.1(d) weaker-family comparison',
'201':'119/151','202':'119/151','203':'119/152',
'301':'120/007,017,021; L2','302':'121/004–024','303':'121/018','304':'121/018','305':'120/021; L2','306':'121/054–073; L2','307':'121/065','308':'121/054–064,070–073','309':'121/006,012,024',
'401':'120/008,018; L3','402':'120/008,018; L3',
'701':'119/145–146','702':'119/145–146','703':'119/145–146','704':'119/145–146'}
notes={
'A.102':'Every finite parameter family has a joint extended collar; no unproved comparison with a weaker pointwise-family model.',
'A.103':'Torus dimension≥6. General Hatcher splitting is not used; Igusa Wh3 term is explicitly killed. Unstable category transfer checked directly in Burghelea–Lashof Theorem6.1, not inferred from stable concordances.',
'A.107':'Original compact scope checked on manuscript image; no definable ODE flow required.',
'A.111':'Specified derived categorical choice model; weaker pointwise/Hausdorff-family comparison remains separate.',
'A.201':'Existence and homotopy class only; A.209 independently refutes full admissible-rigidification essential uniqueness.',
'A.302':'Necessary and sufficient exact completion criterion; does not claim one-space axioms determine coordinates.',
'A.308':'All closed finite-cube compacta and continuous maps satisfy the stated closure/gluing axioms; Cantor countermodel. Does not assert all finite colimits.',
'A.309':'Ordinary topological connectedness forces finite realizations over non-Dedekind-complete fields; definable connectedness is the intended tame convention.'}
records=[]
for p in sorted((ROOT/'parts').glob('*.tex')):
 if p.name.startswith('unchecked'):continue
 for ident,status,title in re.findall(r'\\begin\{saresult\}\{([^}]*)\}\{([^}]*)\}\{([^\n]*)\}',p.read_text()):
  if ident in agent_ids:continue
  num=ident.split('.')[-1]
  records.append(dict(zip(fields,[ident,title,status,str(p.relative_to(ROOT)),deps.get(ident,''),pages.get(num,''),notes.get(ident,'Full proof and exact hypotheses in the indicated paper section; audit events are recorded separately.') ])))
with (ROOT/'notes/root_results.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(sorted(records,key=lambda x:x['id']))
print(f'Wrote {len(records)} explicit root statement records.')
