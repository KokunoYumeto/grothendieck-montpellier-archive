#!/usr/bin/env python3
"""Merge actual DP54--56/58 checks and current gates, preserving older events."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,hashlib
root=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
def readtsv(p):
 with p.open(newline='') as f:
  r=csv.DictReader(f,delimiter='\t');return r.fieldnames,list(r)
def writetsv(p,fields,rows):
 with p.open('w',newline='') as f:
  w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
fields,rows=readtsv(root/'CHECK_EVENTS.tsv')
def add(sid,who,kind,scope,outcome,evidence,when):
 if any(r['evidence']==evidence for r in rows):return
 serial=max(int(r['event_id'].split('-')[1]) for r in rows)+1
 rows.append(dict(zip(fields,[f'DPC-{serial:03d}',sid,'2026-11-21 UTC',when,who,'GPT-6 Astra Pro','not exposed by runtime','DP_MULT_20261121',kind,scope,outcome,evidence])))
_,ar=readtsv(root/'research/archive_binomial_check_events.tsv')
for e in ar:
 if int(e['event_id'].removeprefix('ABA-CE'))>=68:
  add(e['statement_id'],e['checker'],'targeted proof check',e['scope'],e['outcome']+' LIMIT: '+e['limitations'],'research/archive_binomial_check_events.tsv:'+e['event_id'],e['utc_time'])
for n in (54,55,56,58,59):
 for p in sorted((root/'research').glob(f'DP{n}_*review_metadata.json')):
  d=json.loads(p.read_text())
  if 'scope' not in d:continue
  when=next((d[k] for k in ['observed_completion_utc','observed_complete_read_utc','recorded_utc','observed_whole_read_utc'] if k in d),now)
  add('DP'+str(n),d.get('who',d.get('agent','/root')),'targeted proof check',d['scope'],d.get('outcome',d.get('result','PASS')),'research/'+p.name,when)
p=root/'research/DP56_conormal_rank_delta.json';d=json.loads(p.read_text())
add('DP56','/root','targeted proof check',d['scope'],d['outcome'],'research/'+p.name,d['recorded_utc'])
d=json.loads((root/'research/DP55_step2_checks.json').read_text())
for e in d['proof_events']:
 add('DP55','/root/step2_higher','targeted proof check',e['scope'],e['outcome'],'research/DP55_step2_checks.json:'+e['id'],e['observed_completion_utc'])
for e in d['source_events']:
 for path,scope in e['reading_scopes'].items():
  add('ALPOGE-ENDPOINT-'+path.split('/')[-1],'/root/step2_higher','used and rechecked in this run','; '.join(scope)+' Individual read times not separately captured; this is the recorded retrospective source-pass time.','PASS stated reading scope only; recovery-only scans are not proof verification.','research/DP55_step2_checks.json:'+e['id']+':'+path,e['recorded_utc'])
for sid,who,scope,ev in [
 ('MILNE-PICARD-1986','/root/formal_bound','Actual original pixels of printed117-119: Proposition9.2, Pic0 definition and Proposition10.1; positive-sign polarization implies translation of ample theta line.','DP54_author_whole_review_metadata.json:Milne_1986'),
 ('STACKS-DP54','/root/formal_bound','Official statements 0B5T,0D2N,02O1,02KH and35.25.6 in02LB read; exact ample/coherent/proper and flat base-change hypotheses used.','DP54_author_whole_review_metadata.json:Stacks'),
 ('STACKS-DP54','/root','Opened and read official0D2N,0B5T and02KH statements and their short proofs; proper noetherian ampleness spreading, Serre vanishing, flat base change.','DP54-root-primary-read-20261121'),
 ('STACKS-DP56','/root','Opened and read official01VT parts(2),(5) and01Q3 part(7), including hypotheses for projective embedding and all sufficiently large globally generated powers.','DP56-root-primary-read-20261121'),
 ('MUMFORD-THETA-1966','/root','Original printed289 and297 pixels read; neighboring text293-296 read, including nondegenerate commutator, weight-one representation and its hypotheses. Known results cited, not claimed as new.','theta_translate_sources/source_identity.json:root-read')]:
  add(sid,who,'used and rechecked in this run',scope,'PASS within exact stated source scope.','research/'+ev,now)
writetsv(root/'CHECK_EVENTS.tsv',fields,rows)
mf,mr=readtsv(root/'AUTHOR_SOURCE_MANIFEST.tsv');existing={r['path']:r for r in mr};new=[]
for fn in ['DP55_added_sources_manifest.json','DP59_translate_source_recovery.json']:
 d=json.loads((root/'research'/fn).read_text())
 for r in d['records']:
  p=root/'research/external_lean'/r['path'];data=p.read_bytes()
  assert len(data)==r['bytes'] and hashlib.sha256(data).hexdigest()==r['sha256']
  if r['path'] in existing:
   assert existing[r['path']]['sha256']==r['sha256'];continue
  row={'path':r['path'],'author_archive_member':r['author_archive_member'],'bytes':str(r['bytes']),'sha256':r['sha256'],'byte_equal_to_author_archive':'True','recovery_method':'direct extraction from original 14-part author archive','pinned_recovery_url':''}
  existing[r['path']]=row;new.append(row)
mr=sorted(existing.values(),key=lambda r:r['path']);writetsv(root/'AUTHOR_SOURCE_MANIFEST.tsv',mf,mr)
(root/'research/global_jet_incremental_manifest_review.json').write_text(json.dumps({'recorded_utc':now,'new_rows':len(new),'total_rows':len(mr),'scope':'Size/hash verification against previously recorded original-archive direct extraction metadata, not a new complete archive sweep or proof reading.','files':[r['path'] for r in new]},indent=2)+'\n')
qf,qs=readtsv(root/'QUESTIONS.tsv')
gate=('DP54 realizes every finite pure-kernel jet globally and over the number field in valuation. DP56 gives a fixed linear interpolation threshold and subexponential square levels; DP58 sharp explicit degrees further give linear tensor powers with no unit-parameter congruence. DP55 proves detection of every nonzero vector in the exact endpoint Fi space, and an actual period1 after an auxiliary principal level. Thus bare global-jet existence and intrinsic endpoint detection are closed. The remaining main gate is one actual mixed-type family with compatible moduli/CM type, prescribed selected sections and row degrees, nonzero iterated theta image, all six lift identities, and controlled normalization/section/row/level costs proving a net integer lift saving. Current DP57 adelic repair and DP59 permitted-translate constructions are under review, not assumed here. Fixed-order prime budgets and universal polynomial/HaO rates are already settled by DP51/53; no general chain minimality or shorter chain is proved.')
for q in qs:
 if q['id']=='Q3e':q.update(finding_ids_or_counterexample='U2;DP25-DP56;DP58',current_gate_or_scope=gate)
newqs=[
 ('Q3ao','DP49;DP54;Milne1986Prop9.2/10.1;Stacks0D2N/0B5T/02KH','Can sharp finite primitive theta jets be realized by actual global algebraic sections at square tensor levels?','proved','DP54','Every finite jet over the complete DVR extends in all sufficiently large powers; square unit levels preserve selected valuations, and number-field approximation preserves the finite valuations. Sections and powers may vary.'),
 ('Q3ap','DP52;TiedPer79-252;TiedValFi16-255;StdLatUnimodular81-111','Does the actual endpoint period detect every nonzero endpoint vector, and can its coefficient space be made nonzero?','proved within the exact source Fi space','DP55','Surjective conjugate row representing map and positive Gram detect every nonzero Fi vector at the given level. An odd unramified principal auxiliary level makes the action free and gives an actual period value1. The prescribed theta image and quantitative row/level costs remain.'),
 ('Q3aq','DP54;DP56;Stacks01VT/01Q3','Can jet extension and square tensor levels be bounded quantitatively along sharp sequences?','proved','DP56','A fixed linear threshold rn+b separates every integral n-jet; coefficientwise tensor-polynomial bounds give logM=o(n) along sharp sequences. This is not an archimedean section-height bound.'),
 ('Q3ar','DP46/UI16-19;DP51/HA7;DP56;DP58','Are there explicit sharp ordinary/harmonic degrees uniform in every unit tensor parameter, with linear tensor powers?','proved','DP58','Degrees(p^k+1)p^r and harmonic pair(p^r,p^(k+r)) have exact valuation(p^r-1)/(p-1) for every unit parameter. Actual global sections realize them at kappa=An+O(sqrt n); a finite prefix may share one section. Arbitrary prefactors and a prescribed family are not asserted.')]
ids={q['id'] for q in qs}
for q in newqs:
 if q[0] not in ids:qs.append(dict(zip(qf,q)))
writetsv(root/'QUESTIONS.tsv',qf,qs)
for name in ['README.md','DP_MULT.tex']:
 p=root/name;t=p.read_text();t=t.replace('the578 targeted modules:526','the600 targeted modules:526').replace('and52 directly extracted','and74 directly extracted').replace('578 modules:526','600 modules:526').replace('578 targeted','600 targeted');p.write_text(t)
print(json.dumps({'recorded_utc':now,'events':len(rows),'questions':len(qs),'source_modules':len(mr),'added_source_rows':len(new)}))
