"""Assemble explicitly promoted post19 units with four actual proof audits."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,re,sys
root=Path(__file__).resolve().parents[1]
name=sys.argv[1];paths=sys.argv[2:];assert paths
out=root/('code/output/integrate_post19_'+name+'.json');assert not out.exists()
now=datetime.now(timezone.utc).isoformat()
cols=['id','statement','status','where_proved','depends_on','manuscript_pages','notes']
with (root/'parts/D/results_D.csv').open() as f:rows=list(csv.DictReader(f))
known={x['id'] for x in rows};added=[];new_events=[];files=[]
pattern=re.compile(r'\\begin\{(proposition|corollary|lemma|theorem|example)\}\[([^\]]+)\]\s*\\label\{([^}]+)\}')
staged=[]
staged_labels=set(known)
staged_bib_keys=set(re.findall(r'@\w+\{([^,]+),',(root/'parts/D/references_D.bib').read_text()))
paper_before=(root/'parts/D/paper_D.tex').read_text()
def passed(value):
 return value=='PASS' or isinstance(value,str) and value.startswith('PASS: ')
for path in paths:
 m=json.loads((root/path).read_text())
 if isinstance(m.get('audit_scope'),dict) and all(isinstance(a,dict) for a in m['audit_scope'].values()):
  assert set(m['audit_scope'])=={'root','B','C','D'}
  checked_scopes={}
  for actor,a in m['audit_scope'].items():
   actual=json.loads((root/a['record']).read_text())
   assert passed(actual.get('verdict',actual.get('outcome')))
   if m.get('audited_candidate'):
    assert actual['sha256']==m['audited_candidate']['sha256']
   checked_scopes[actor]=a['scope']+' Source scope: '+a.get('source_scope','See actual record.')+' Record: '+a['record']
  m['audit_scope']=checked_scopes
  m.setdefault('scope_precision',m.get('scope_limits',''))
 if isinstance(m.get('audit_scope'),str):
  m.setdefault('scope_precision',m['audit_scope'])
  audits=m['audits']
  if isinstance(audits,dict):
   assert set(audits)=={'root','B','C','D'}
   assert all(passed(a.get('verdict',a.get('outcome'))) and (root/a['record']).exists() for a in audits.values())
   m['audit_scope']={actor:str(a.get('audit_scope',a.get('scope')))+' Record: '+a['record'] for actor,a in audits.items()}
  else:
   for a in audits:
    a.setdefault('record',a.get('path'))
    a.setdefault('scope',m['audit_scope'])
    if 'verdict' not in a and 'outcome' not in a:
     actual=json.loads((root/a['record']).read_text())
     a['verdict']=actual.get('verdict',actual.get('status',actual.get('outcome')))
   assert all(passed(a.get('verdict',a.get('outcome'))) and (root/a['record']).exists() for a in audits)
   m['audit_scope']={a.get('auditor',a.get('actor')):a['scope']+' Record: '+a['record'] for a in audits}
 m.setdefault('recorded_utc',m.get('promoted_at_utc',m.get('created_utc',m.get('timestamp_utc'))))
 assert m['recorded_utc'] and set(m['audit_scope'])=={'root','B','C','D'}
 p=root/m['path'];source=p.read_text();assert hashlib.sha256(p.read_bytes()).hexdigest()==m['sha256']
 units=list(pattern.finditer(source));assert {u[3] for u in units}==set(m['labels'])
 assert all(u[2].startswith(('Proved:','Proved under','Known:')) for u in units)
 assert not (set(m['labels']) & staged_labels)
 staged_labels.update(m['labels'])
 assert '\\input{'+m['path']+'}' not in paper_before
 if m.get('bibliography'):
  b=m['bibliography'];b=dict(path=b,sha256=m['bibliography_sha256'],keys=m.get('bibliography_keys',m.get('new_bibliography_keys'))) if isinstance(b,str) else b
  bp=root/b['path'];bs=bp.read_text();assert hashlib.sha256(bp.read_bytes()).hexdigest()==b['sha256'];assert 'Opened' in bs
  assert b['keys'] is not None and not(set(b['keys'])&staged_bib_keys)
  staged_bib_keys.update(b['keys']);m['bibliography']=b
 staged.append((m,source,units))
for m,source,units in staged:
 scope=m.get('scope_precision',m.get('scope',[]));scope=' '.join(scope) if isinstance(scope,list) else scope
 movement=m.get('movement_classification',m.get('movement',m.get('research_movement',m.get('movement_scope','Auxiliary; no main-gate movement.'))))
 for u in units:
  assert u[3] not in known,u[3]
  rows.append(dict(id=u[3],statement=u[2].split(':',1)[-1].strip(),status='Known' if u[2].startswith('Known:') else 'Proved under stated hypotheses',where_proved=m['path']+': label '+u[3],depends_on='; '.join(sorted(set(re.findall(r'\\ref\{([^}]+)\}',source)))),manuscript_pages='29/061,066',notes=scope+' Four full actual-file/source audits. '+str(movement)))
  known.add(u[3]);added.append(u[3])
  for actor,audit in m['audit_scope'].items():
   who='/root' if actor=='root' else '/root/part_'+actor.lower()
   new_events.append(dict(statement_id=u[3],date=m['recorded_utc'],who='GPT-6 Astra Pro; '+who+'; SA12 run1; effort setting not independently exposed',type='targeted proof check',outcome='PASS: '+str(audit)))
 p=root/'parts/D/paper_D.tex';s=p.read_text();line='\\input{'+m['path']+'}';assert line not in s;p.write_text(s+'\n'+line+'\n')
 if m.get('bibliography'):
  b=m['bibliography'];b=dict(path=b,sha256=m['bibliography_sha256'],keys=m.get('bibliography_keys',m.get('new_bibliography_keys'))) if isinstance(b,str) else b
  bp=root/b['path'];bs=bp.read_text();assert hashlib.sha256(bp.read_bytes()).hexdigest()==b['sha256'];assert 'Opened' in bs
  p=root/'parts/D/references_D.bib';s=p.read_text();old=set(re.findall(r'@\w+\{([^,]+),',s));assert not(set(b['keys'])&old);p.write_text(s+'\n'+bs)
 files.append({'path':m['path'],'sha256':m['sha256']})
with (root/'parts/D/results_D.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(rows)
p=root/'parts/D/CHECK_EVENTS_D.tsv'
with p.open() as f:events=list(csv.DictReader(f,delimiter='\t'))
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(events+new_events)
r=dict(utc=now,labels=added,added_rows=len(added),added_events=len(new_events),files=files,additional_independent_movement_events=0,requested_status_changes=[],archive_created=False)
out.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
