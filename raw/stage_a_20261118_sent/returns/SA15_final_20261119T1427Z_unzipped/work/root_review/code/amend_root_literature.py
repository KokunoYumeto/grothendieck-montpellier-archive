"""Late primary-source scope corrections, after opening André and Voisin."""
from pathlib import Path
import json,csv
from datetime import datetime,timezone
O=Path(__file__).resolve().parents[1]
def r(n):return json.loads((O/n).read_text())
cs=r('claims_c8.json');ps=r('problems_c8.json')
for c in cs:
 if c['id']=='P78-C055':
  c['fate']=c['present_status']=('Full faithfulness alone is insufficient: the earlier notes’ Borel example is independently re-proved here. Deligne–Milne Prop2.21 gives the subobject criterion. André2023 Lem1.5 supplies the alternative extra hypothesis of observability; Th2.1 proves observability for geometric ℓ-adic cohomology of smooth projective varieties over finitely generated fields (ℓ distinct from field characteristic). This does not identify the draft’s unspecified local p-adic functor.')
  c['refs'].append('Andre2023')
 if c['id']=='P78-C062':
  c['refs'].append('Voisin2025')
  c['fate']=c['present_status']=c['fate']+' Voisin2025 §3 Conj3.1 and §4.2 Conj4.6 give precise rational and generalized formulations; the latter asks for supported Hodge substructures, not arbitrary rational classes of a given Hodge coniveau.'
 if c['id']=='P78-C063':
  c['refs']+=['Andre2023','Broe2026']
  c['fate']=c['present_status']='Tate1966 proves the finite-field abelian homomorphism theorem and divisor consequences. André2023 Conj0.1 distinguishes cycle surjectivity and semisimplicity; Th2.1 and Cor2.4 give observability and a conditional implication, not the general conjecture. Searches through19November2026 found recent Broe2026/Li2026 low-dimensional preprint leads, but repeated primary opens failed; neither is used as an established theorem. No opened source settles the manuscript’s general agenda.'
for p in ps:
 if p['id']=='P78-P016':
  p['refs'].append('Andre2023');p['state_of_art']+=' André2023 Lem1.5 and Th2.1 provide observability as the missing extra condition in a precise geometric ℓ-adic setting.'
  p['worth']='Worth identifying the actual category and whether geometric observability applies; the formal full-faithfulness implication alone is already refuted.'
 if p['id']=='P78-P019':p['refs'].append('Voisin2025');p['state_of_art']+=' Voisin2025 §4.2 Conj4.6 states the corrected supported-Hodge-substructure version precisely.'
 if p['id']=='P78-P020':
  p['refs']+=['Andre2023','Broe2026'];p['state_of_art']='Tate1966 gives the finite-field abelian homomorphism theorem and divisors. André2023 Conj0.1 separates cycles and semisimplicity; Th2.1 and Cor2.4 give precise partial implications. Recent2026 low-dimensional preprint leads were searched but could not be opened; they are explicitly unverified and not counted as established results.'
for name,data in [('claims_c8.json',cs),('problems_c8.json',ps)]: (O/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
ev=r('reference_evidence.json')
extra=[
 dict(key='Andre2023',authors='Yves André',title='On the observability of Galois representations and the Tate conjecture',year='2023',url='https://arxiv.org/pdf/2303.06549',verified=True,access_level='primary theorem and targeted proof check',checked_locator_and_scope='Conj0.1; Lem1.5 and Rem1.6 (full faithfulness, observability and Borel); Th2.1 geometric ℓ-adic observability; Cor2.4 char0 all powers Tate implies semisimplicity. Lem1.5 proof read, general geometry theorem used with its exact hypotheses.',date_evidence='arXiv first12March2023; later publication date not asserted.'),
 dict(key='Voisin2025',authors='Claire Voisin',title='Hodge and generalized Hodge conjectures, coniveau and algebraic cycles',year='2025',url='https://webusers.imj-prg.fr/~claire.voisin/Articlesweb/JOMP_V01N01P02Paper.pdf',verified=True,access_level='primary author exposition, exact conjectures',checked_locator_and_scope='§3 Conj3.1 rational Hodge; §4.2 Conj4.6 generalized Hodge for Hodge substructures; distinction from the false naïve coniveau formulation.',date_evidence='Journal of Open Mathematical Problems1(1)(2025),16–51; received9Jan, revised4Jun, accepted13July2025; DOI10.56994/JOMP.001.001.002.'),
 dict(key='Broe2026',authors='Matt Broe',title='The Tate conjecture for abelian fourfolds over finite fields',year='2026',url='https://arxiv.org/abs/2608.28651',verified=False,access_level='unverified',checked_locator_and_scope='Search record only. arXiv abs/pdf both DisabledError; purported author research page unavailable. Not cited as a checked theorem.',date_evidence='Search metadata19August2026; primary date/status unverified.')
]
now=datetime.now(timezone.utc).isoformat()
for x in ev:
 if x['key']=='Liu2025':x['authors']='Haohao Liu'
 if x['key']=='Hua2026':x.update(authors='Michel Hua',title='Énoncés des notes de travail de Grothendieck démontrés en Lean4, et questions ouvertes, version2')
for x in extra:x.update(accessed='2026-11-19',reviewer='root');ev.append(x)
(O/'reference_evidence.json').write_text(json.dumps(ev,ensure_ascii=False,indent=2)+'\n')
bb=[]
for x in ev:
 fields={'author':x['authors'],'title':x['title'],'year':x['year'],'note':'verified' if x['verified'] else 'unverified'}
 if x['url']:fields['url']=x['url']
 bb.append('@misc{'+x['key']+',\n'+',\n'.join('  '+k+' = {'+v+'}' for k,v in fields.items())+'\n}\n')
(O/'references.bib').write_text('\n'.join(bb))
with (O/'reference_check_events.tsv').open('a') as f:
 w=csv.writer(f,delimiter='\t')
 for x in extra:w.writerow([x['key'],now,'GPT-6 Astra Pro; effort not exposed; SA15-20261119/root','targeted proof check' if x['key']=='Andre2023' else 'used and rechecked in this run' if x['verified'] else 'carried as background without fault found',x['access_level']+': '+x['checked_locator_and_scope']])
print(json.dumps({'references_added':[x['key'] for x in extra],'claims_updated':['P78-C055','P78-C062','P78-C063']}))
