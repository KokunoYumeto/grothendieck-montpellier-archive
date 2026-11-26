#!/usr/bin/env python3
"""Admit only the whole-reviewed R109 original nonunipotent cut, retaining all four positive completions."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,ast,csv,hashlib,json,re
csv.field_size_limit(20_000_000)
B=Path(__file__).resolve().parents[1];ap=argparse.ArgumentParser();ap.add_argument('spec');args=ap.parse_args();s=json.loads((B/args.spec).read_text());now=datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256((B/p).read_bytes()).hexdigest()
def rd(p):return json.loads((B/p).read_text())
def wr(p,d):(B/p).write_text(json.dumps(d,indent=2)+'\n')
def review_time(v):
 return next((v[k] for k in ['initial_whole_review_completed_utc','completed_utc','review_completed_utc','time_utc','assessment_completed_utc','assessment_utc','whole_assessment_completed_utc'] if v.get(k)),None)
key,fid,src,dst=s['key'],s['finding'],s['source'],s['destination'];ph,sh=s['proof_sha256'],s['script_sha256'];priorp=s['prior'];ep='checks/'+key+'_joint_remainder_error.json';charge=s['charge']
prior_floor=s.get('prior_support_floor',26);new_floor=s.get('new_support_floor',prior_floor);assert isinstance(prior_floor,int) and isinstance(new_floor,int) and new_floor>=prior_floor>=26
assert sha(src)==ph and sha(s['script'])==sh and not(B/dst).exists() and not(B/ep).exists()
prior=rd(priorp);a=prior['all_top_exponents'];u=prior['uniform_exponents'];assert prior['status']=='PASS_EXACT_CANONICAL_ORDERED_TOTALS' and len(a)==s['prior_count'] and len(u)==31 and (prior['all_top_support_floor'],prior['uniform_support_floor'])==(prior_floor,11)
for kind in ['root','peer']:
 x=s[kind];v=rd(x['verification']);assert 'PASS' in v.get('status',v.get('verdict',v.get('outcome',v.get('event',v.get('assessment',''))))) and sha(x['report'])==x['report_sha256'];vt=json.dumps(v);assert ph in vt and sh in vt and x['report_sha256'] in vt and sha(x['replay']) in vt
 assert review_time(v)
 c=rd(x['replay']);cp=Path(c['prior_file']);cp=cp if cp.is_absolute() else B/cp
 assert c['status']==s.get('replay_status','PASS_EXACT_DIAGNOSTICS') and c['proof_sha256']==ph and c['script_sha256']==sh and c['assertions']==s['assertions'] and cp.resolve()==(B/priorp).resolve() and c['prior_sha256']==sha(priorp) and c.get('all_top_exponents',c.get('all_top_exponents_staged'))==a+[charge] and c.get('new_absolute_charge',c.get('new_charge'))==charge and c['uniform_exponents']==u
 assert c['all_top_support_floor']==new_floor and c['uniform_support_floor']==11
assert fid=='AM-R-109' and key=='r109' and charge==3359 and s['prior_count']==156
assert rd('research/run_state.json')['review_count']==48
completion=rd(s['completion']);completion_hash=sha(s['completion']);debit=completion['separate_completion_exponents']
assert s['completion']==s['predecessor_energy_budget']==s['replay_ancestor_budget']=='checks/k131_one_sided_energy_budget.json'
assert completion_hash=='e6ee100945bdff392d6f7d5fa91f2270195b21dd531cee4ee93485f705912bf5'
assert completion['status']=='PASS_EXACT_UPDATED_ONE_SIDED_ENERGY_BUDGET' and debit==[1266,3484,2473,14750]
assert completion['all_top_exponents']==a and completion['uniform_exponents']==u
assert completion['absolute_error_file']==priorp and completion['absolute_error_sha256']==sha(priorp)
assert completion['new_absolute_charge']==235 and completion['new_separate_completion_exponent'] is None
assert completion['actual_signed_support_lower_bound']==s['signed_support_minimum']==30
assert completion['positive_completion_sums']==['P27','P28_rem','P29','Pmix']
assert prior_floor==new_floor==27 and not(B/s['updated_completion_budget']).exists()
for kind in ['root','peer']:
 c=rd(s[kind]['replay']);bp=Path(c['energy_file']);bp=bp if bp.is_absolute() else B/bp
 assert bp.resolve()==(B/s['completion']).resolve() and c['energy_sha256']==completion_hash
 assert c['separate_completion_exponents']==debit and c['positive_completion_sums']==completion['positive_completion_sums']
 assert c['actual_signed_support_lower_bound']==30 and c['row_count']==7
 assert c['uniform_pointwise_p_bound'] is True and c['p_union_charged'] is False
 assert c['fixed_nonunipotent_exhausted_supports']==[30,31] and c['full_support30_exhausted'] is False
 assert c['retained_column_indices']=={'C':'T^(10s)','E':'T^(6s)'} and c['source_fibre_bits']==107
 assert all(__import__('fractions').Fraction(r['complete_exponent']) < -3362 for r in c['complete_rows'])
for es in [a+[charge],u,a+[charge]+debit]:
 m=max(es);assert sum(1<<(m-e) for e in es)<1<<(m-230)
scope=s['scope'];n=len(a)+1
first,rest=(B/src).read_text().split('\n',1);(B/dst).write_text(first+'\n\n**Canonical checked integration — '+now+'.** Complete root and independent proof/script/interface reviews and separate exact replays passed. The actual canonical predecessor has'+str(len(a))+'/31 entries; this integration gives'+str(n)+'/31, complete floors'+str(new_floor)+'/11. Frozen author history is preserved. '+scope+'\n'+rest+'\n\n## Canonical algebraic-geometric context\n\n'+s['geometry']+'\n')
wr(ep,dict(finding=fid,time_utc=now,status='PASS_EXACT_CANONICAL_ORDERED_TOTALS',all_top_exponents=a+[charge],uniform_exponents=u,new_charge=charge,prior_file=priorp,prior_sha256=sha(priorp),all_top_support_floor=new_floor,uniform_support_floor=11,minimum_all_top_non231_exponent=min(e for e in a+[charge] if e!=231)))
wr(s['updated_completion_budget'],dict(finding=fid,time_utc=now,status='PASS_EXACT_UPDATED_ONE_SIDED_ENERGY_BUDGET',absolute_error_file=ep,absolute_error_sha256=sha(ep),all_top_exponents=a+[charge],uniform_exponents=u,absolute_counts=[n,31],absolute_floors=[27,11],new_absolute_charge=charge,new_separate_completion_exponent=None,separate_completion_exponents=debit,positive_completion_sums=completion['positive_completion_sums'],original_completion_file=s['completion'],original_completion_sha256=completion_hash,full_all_top_absolute_sum_plus_completion_below_two_pow_minus230=True,identity=s['energy_identity'],sufficient_signed_gate=s['sufficient_signed_gate'],actual_signed_support_lower_bound=30,predecessor_energy_budget_file=s['predecessor_energy_budget'],predecessor_energy_budget_sha256=completion_hash,signed_gate_status='OPEN',same_actual_remainder=False,newly_removed_actual_subset=True,scope=scope,allocation_history='All four original positive sums and their separate debits are unchanged. R109 removes only the actual surviving intersection with its complete fixed-S nonunipotent C30–34/E30–31 containing sectors, paid by one3359 absolute allowance. Together with accepted R103 this exhausts fixed-S nonunipotent30/31 only; all-II30, mixed30 windows and other structural classes are not claimed exhausted.'))
events=[]
def ev(sf,typ,out,p,detail,date=now,agent='/root'):
 assert date, 'Every event requires its actual date'
 events.append(dict(statement_id=sf,date_utc=date,who_model_effort_run='GPT-6 Astra Pro; inherited effort not externally exposed; ALP_MACHINE '+agent,type=typ,outcome=out,locator=p,detail=detail,sha256=sha(p)))
for kind in ['root','peer']:
 x=s[kind]
 if x['agent'] in s.get('skip_review_events_for_agents',[]):continue
 v=rd(x['verification']);c=rd(x['replay']);vtm=review_time(v);assert vtm;ev(fid,'targeted proof check','PASS_'+kind.upper()+'_WHOLE_PROOF_SCRIPT_AND_INTERFACE',x['report'],s['review_scope'],vtm,x['agent']);ev(fid,'computation or formal certificate','PASS_'+str(s['assertions'])+'_EXACT_CURRENT_PREFIX',x['replay'],'Complete stated arithmetic diagnostics and actual full chronological arrays; no global-arrow enumeration.',c.get('completed_utc',c.get('time_utc',c.get('utc'))),x['agent'])
ev(fid,'used and rechecked in this run','PASS_ROOT_ENTIRE_PEER_REPORT',s['peer']['report'],'Whole peer report and verification read before promotion.')
for x in s['dependencies']:ev(x['finding'],x.get('type','used and rechecked in this run'),'PASS_LITERAL_COMPOSITION_INTERFACE',x['path'],x['scope'])
ev(fid,'computation or formal certificate','PASS_COMPLETE_CANONICAL_ERROR_SUMS',ep,'Exactly one'+str(charge)+' append; all overlapping errors retained, both entire sums below2^-230.')
ev(fid,'used and rechecked in this run','PASS_CANONICAL_PROOF_SCOPE_AND_HASH',dst,scope)
ev(fid,'computation or formal certificate','PASS_COMPLETE_ABSOLUTE_PLUS_SEPARATE_COMPLETION_BUDGET',s['updated_completion_budget'],'Full current ordered absolute array plus separate1266/3484/2473/14750 debits below2^-230; absolute floors27/11; unchanged P27/P28_rem/P29/Pmix and actual residual support-at-least'+str(s['signed_support_minimum'])+'.')
wr('checks/root_'+key+'_events.json',dict(events=events))
qp=B/'QUESTIONS.tsv'
with qp.open(newline='') as f:r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;rows=list(r)
(B/'research'/('questions_before_'+key+'.tsv')).write_bytes(qp.read_bytes())
for row in rows:
 if row['id'] in ['Q1','Q2']:
  v=row['finding_ids_or_current_gate'];i=v.index('CURRENT FINITE NONVANISHING GATE');j=v.index('J14 retains R042:',i);g=v[i:j];assert 'All'+str(len(a))+' chronological' in g and priorp in g
  if s.get('finite_gate_replacement'):
   g=s['finite_gate_replacement'].rstrip()+' '
   assert g.startswith('CURRENT FINITE NONVANISHING GATE') and 'All'+str(n)+' chronological' in g and ep in g
   assert 'complete absolute support floors remain27/11' in g and ('actual R_ge'+str(s['signed_support_minimum'])) in g and s['updated_completion_budget'] in g
  else:
   anchor=s.get('gate_anchor','The sufficient inequality J26.2,');assert g.count(anchor)==1
   g=g.replace('All'+str(len(a))+' chronological','All'+str(n)+' chronological').replace(priorp,ep).replace(anchor,s['gate_delta']+' '+anchor)
   for old,new in s.get('gate_replacements',[]):
    assert g.count(old)==1;g=g.replace(old,new)
  row['finding_ids_or_current_gate']=v[:i]+g+v[j:]+' '+scope
qid=s.get('question_id','Q1-POSTREVIEW32-'+fid)
existing=[r for r in rows if r['id']==qid]
if s.get('update_existing_question',False):
 assert len(existing)==1
 existing[0].update(dict(zip(fields,[qid,fid+'; '+dst,s['question'],'PROVED_IN_STATED_SCOPE',scope])))
else:
 assert not existing
 rows.append(dict(zip(fields,[qid,fid+'; '+dst,s['question'],'PROVED_IN_STATED_SCOPE',scope])))
with qp.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
bp=B/'scripts/build_paper.py';t=bp.read_text();ls=t.splitlines(keepends=True)
for nd in ast.parse(t).body:
 if isinstance(nd,ast.Assign) and isinstance(nd.targets[0],ast.Name) and nd.targets[0].id in ['checked','pending']:
  name=nd.targets[0].id;vs=ast.literal_eval(nd.value)
  if name=='checked':assert dst not in vs;vs.append(dst)
  else:vs=[v for v in vs if v not in [src]+s.get('pending_remove',[])]
  ls[nd.lineno-1]=name+' = '+repr(vs)+'\n'
  for k in range(nd.lineno,nd.end_lineno):ls[k]=''
bp.write_text(''.join(ls))
gd=B/'GROTHENDIECK_DICTIONARY.md';number=max(map(int,re.findall(r'^## (\d+)\.',gd.read_text(),re.M)))+1
with gd.open('a') as f:f.write('\n\n## '+str(number)+'. '+fid+'\n\n'+scope+'\n\n'+s['geometry']+'\n')
for p in ['LEDGER.md','IMPLICATIONS.md']:
 with(B/p).open('a') as f:f.write('\n## Checked '+fid+' — '+now+'\n\n'+scope+'\n')
assert sha(s['completion'])==completion_hash
out=dict(separate_completion_exponents=debit,one_sided_budget_file=s['updated_completion_budget'],time_utc=now,finding=fid,source_sha256=ph,canonical_sha256=sha(dst),root_review_sha256=sha(s['root']['report']),peer_review_sha256=sha(s['peer']['report']),events=len(events),questions=len(rows),new_charge=charge,error_file=ep,errors=[n,31],all_top_floor=new_floor,uniform_floor=11,spec_sha256=sha(args.spec));wr('research/'+key+'_integration_manifest.json',out)
state=rd('research/run_state.json')
(B/'research/current_research_status.md').write_text('# Current research status — after '+fid+'\n\nUpdated '+now+'.\n\n'+'\n\n'.join('## '+r['id']+' — '+r['state']+'\n\n'+r['finding_ids_or_current_gate'] for r in rows if r['id'] in ['Q1','Q2','Q3','Q4'])+'\n\nReview '+str(state['review_count'])+'; next review '+state['next_review_due_utc']+'. Latest durable checkpoint '+str(state.get('last_durable_checkpoint_count', state['checkpoint_count']))+'; next checkpoint due '+state['next_checkpoint_due_utc']+'. Current '+str(n)+'/31 exact errors, floors'+str(new_floor)+'/11.\n')
print(json.dumps(out))
