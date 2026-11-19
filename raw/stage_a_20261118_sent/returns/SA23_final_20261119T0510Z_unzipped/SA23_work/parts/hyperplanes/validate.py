#!/usr/bin/env python3
"""Structural audit and authored computation-to-claim inventory; no verdicts generated."""
import json,csv,re,hashlib,collections
from pathlib import Path
P=Path(__file__).parent
I=json.loads((P/'items.json').read_text());C=json.loads((P/'claims.json').read_text());Q=json.loads((P/'problems.json').read_text());D=json.loads((P/'directions.json').read_text())
ids={x['id']for x in I};cids={x['id']for x in C};qids={x['id']for x in Q}
ED=json.loads((P/'editorial_tasks.json').read_text());eids={x['id']for x in ED}
refs=set(re.findall(r'@\w+\{([^,]+)',(P/'references.bib').read_text()))
errors=[]
required={'items':['id','sources','kind','cote','scans','lines','his_words','statement','reconstruction','check','check_reason'],'claims':['id','items','cote','scans','lines','his_statement','statement','status_on_pages','computation','class','fate','fate_date','present_status','refs','confidence'],'problems':['id','title','occurrences','as_he_states','plausible_today','state_of_art','why_open','worth','refs']}
for typ,records in [('items',I),('claims',C),('problems',Q)]:
 if len({x['id']for x in records})!=len(records):errors.append(typ+' duplicate IDs')
 for x in records:
  for k in required[typ]:
   if k not in x:errors.append(x['id']+' missing '+k)
  for r in x.get('refs',[]):
   if r not in refs:errors.append(x['id']+' unknown reference '+r)
for c in C:
 if c['class']not in 'ABCDEF':errors.append(c['id']+' invalid class')
 for i in c['items']:
  if i not in ids:errors.append(c['id']+' unknown item '+i)
 if c['status_on_pages']=='false as stated'and c['id']+'R'not in cids:errors.append(c['id']+' no refinement')
for d in D:
 for field,valid in [('items',ids),('claims',cids),('problems',qids)]:
  if not d[field]:errors.append(d['id']+' missing '+field)
  for i in d[field]:
   if i not in valid:errors.append(d['id']+' unknown '+i)
 for i in d.get('editorial_tasks',[]):
  if i not in eids:errors.append(d['id']+' unknown editorial task '+i)
out=json.loads((P/'computations_output.json').read_text())
assert out['checks_passed'] is True
# Each mapping below was assigned from individually read claims.
mapping={
 'universal_dimension_identities':[1,5,21,38,39,41,47],
 'generic_combination_zero':[8],
 'blowup_total_transform':[26,48,50],
 'quadric_tangent_section':[23,27],
 'fixed_component_bertini':[28],
 'char2_conic_gradient':[22,29,92],
 'conic_pencil_ramification_numerator':[33,42],
 'conic_pencil_branch_values':[33,42],
 'node_polar_matrix':[78,79,80],
 'cusp_quadratic_polar_matrix':[79],
 'ambient_three_char2_quadric_partials':[78,99,102],
 'ternary_polar_determinant':[100],
 'ternary_half_discriminant':[100],
 'two_odd_ranks_sum':[101],
 'standard_forms':[99,100,102],
 'hilbert_rank_alarm':[86,87,94],
 'schubert_checked_cases':[41],
 'false_range_example':[41],
 'genus_two_no_plane_degree':[53],
 'cofactor_sign_example':[81],
 'line_bundle_determinant_exponents':[83,89],
 'unit_hessian_scaling':[80,83],
 'node_conormal_annihilator':[82],
 'nilpotent_constant_fiber_rank':[90],
 'quadric_hilbert_series_check':[85,86,87,94],
 'veronese_fixed_linear_space':[108]}
inventory=[]
for key,nums in mapping.items():
 if key not in out:errors.append('Missing computation output '+key)
 inventory.append({'output_key':key,'claims':[f'C-SA23-hyp-{n:03}'for n in nums],'program':'parts/hyperplanes/computations.py','output':'parts/hyperplanes/computations_output.json','interpretation':'Exact symbolic identity or explicit example as stated in output; proof_checks.md and claim fields supply the general argument and limitations.'})
unmapped=set(out)-set(mapping)-{'checks_passed','scope'}
if unmapped:errors.append('Unmapped computation results: '+str(sorted(unmapped)))
(P/'computation_inventory.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n')
events=[]
for f in sorted(P.glob('*check_events.tsv')):
 with f.open()as h:events+=list(csv.DictReader(h,delimiter='\t'))
checked={e['statement_id']for e in events}
for sid in ids|cids|qids|eids|refs:
 if sid not in checked:errors.append('No check event '+sid)
readings=list(csv.DictReader((P/'readings.tsv').open(),delimiter='\t'));links=list(csv.DictReader((P/'links.tsv').open(),delimiter='\t'))
source=Path('sources/texts/api/ega_v_cote25_combined.tex')
report={'items':len(I),'claims':len(C),'original_claims':sum(not c['id'].endswith('R')for c in C),'present_run_refinements':sum(c['id'].endswith('R')for c in C),'problems':len(Q),'readings':len(readings),'links':len(links),'directions':len(D),'references':len(refs),'check_events':len(events),'computation_output_blocks':len(mapping),'classes':dict(collections.Counter(c['class']for c in C)),'statuses':dict(collections.Counter(c['status_on_pages']for c in C)),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'source_lines':len(source.read_text().splitlines()),'errors':errors}
(P/'validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
report['editorial_tasks']=len(ED)
(P/'validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
assert not errors,errors
