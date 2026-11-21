#!/usr/bin/env python3
"""Forward-only merge through checked DP60; preserve the dated earlier ledger."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,hashlib,re
root=Path(__file__).resolve().parents[1]; now=datetime.now(timezone.utc).isoformat()
def read(p):
 with p.open(newline='') as f:
  r=csv.DictReader(f,delimiter='\t');return r.fieldnames,list(r)
def write(p,fields,rows):
 with p.open('w',newline='') as f:
  w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
ef,es=read(root/'CHECK_EVENTS.tsv')
def event(sid,who,kind,scope,outcome,evidence,when):
 if any(e['evidence']==evidence for e in es):return
 serial=max(int(e['event_id'].split('-')[1]) for e in es)+1
 es.append(dict(zip(ef,[f'DPC-{serial:03d}',sid,'2026-11-21 UTC',when,who,'GPT-6 Astra Pro','not exposed by runtime','DP_MULT_20261121',kind,scope,outcome,evidence])))
_,ars=read(root/'research/archive_binomial_check_events.tsv')
for e in ars:
 number=int(e['event_id'].removeprefix('ABA-CE'))
 if not 75<=number<=83:continue
 kind='computation or formal certificate' if number==82 else 'targeted proof check'
 event(e['statement_id'],e['checker'],kind,e['scope'],e['outcome']+' LIMIT: '+e['limitations'],'research/archive_binomial_check_events.tsv:'+e['event_id'],e['utc_time'])
for n in (57,58,59,60):
 for p in sorted((root/'research').glob(f'DP{n}_*review_metadata.json')):
  d=json.loads(p.read_text())
  if 'scope' not in d:continue
  when=next((d[k] for k in ['observed_completion_utc','observed_complete_read_utc','recorded_utc','observed_whole_read_utc'] if k in d),now)
  event(f'DP{n}',d.get('who',d.get('agent','/root')),'targeted proof check',d['scope'],d.get('outcome',d.get('result','PASS')),'research/'+p.name,when)
d=json.loads((root/'research/DP57_step2_checks.json').read_text())
for e in d['proof_events']:
 event('DP57','/root/step2_higher','targeted proof check',e['scope'],e['outcome'],'research/DP57_step2_checks.json:'+e['id'],e['observed_completion_utc'])
mf,ms=read(root/'AUTHOR_SOURCE_MANIFEST.tsv'); existing={x['path']:x for x in ms}; added=[]
for fn in ['DP57_added_sources_manifest.json','DP61_added_sources_manifest.json']:
 d=json.loads((root/'research'/fn).read_text())
 for r in d['records']:
  data=(root/'research/external_lean'/r['path']).read_bytes(); sha=hashlib.sha256(data).hexdigest()
  original=r.get('sha256',r.get('author_sha256'))
  assert len(data)==r['bytes'] and sha==original
  if r['path'] in existing:assert existing[r['path']]['sha256']==sha
  else:
   row={'path':r['path'],'author_archive_member':r['author_archive_member'],'bytes':str(r['bytes']),'sha256':sha,'byte_equal_to_author_archive':'True','recovery_method':'direct extraction from original 14-part author archive','pinned_recovery_url':''}
   existing[r['path']]=row;added.append(row)
  if fn.startswith('DP57'):
   scope='; '.join(r.get('reading_scope',[]))
   if scope and not scope.startswith('Recovered by symbol matching only'):
    event('ALPOGE-DP57-'+r['path'].split('/')[-1],'/root/step2_higher','used and rechecked in this run',scope,'PASS within actual stated source-reading scope; no whole-module audit beyond explicitly stated ranges.','research/DP57_added_sources_manifest.json:read:'+r['path'],d['recorded_utc'])
ms=sorted(existing.values(),key=lambda x:x['path']);write(root/'AUTHOR_SOURCE_MANIFEST.tsv',mf,ms)
review_path=root/'research/translate_endpoint_manifest_review.json'
review=json.loads(review_path.read_text()) if review_path.exists() else {'recorded_utc':now,'new_rows':len(added),'total_rows':len(ms),'scope':'Python verified local length and SHA256 against the original-archive extraction metadata for DP57 and DP61. This is a source-identity computation, not a source proof read or Lean execution.','new_paths':[x['path'] for x in added]}
review['last_rechecked_utc']=now
review_path.write_text(json.dumps(review,indent=2)+'\n')
event('SOURCE-IDENTITY-DP57-DP61','/root','computation or formal certificate',review['scope'],'PASS all recorded byte lengths and hashes; '+str(len(added))+' added inventory rows.','research/translate_endpoint_manifest_review.json',now)
d=json.loads((root/'research/DP57_step2_checks.json').read_text())
for s in d['source_events']:
 for r in s['additional_previously_recovered_source_reads']:
  event('ALPOGE-DP57-'+r['path'].split('/')[-1],'/root/step2_higher','used and rechecked in this run',r['reading_scope'],'PASS exact source scope; recorded after source pass, individual read times not separately captured.','research/DP57_step2_checks.json:'+s['id']+':'+r['path'],s['recorded_utc'])
 for r in s['primary_web_reads']:
  event('PRIMARY-DP57','/root/step2_higher','used and rechecked in this run',r['title']+'; '+r['locators']+'; '+r['scope'],'PASS cited hypotheses and precise statement locators.','research/DP57_step2_checks.json:'+s['id']+':'+r['url'],s['recorded_utc'])
write(root/'CHECK_EVENTS.tsv',ef,es)
qf,qs=read(root/'QUESTIONS.tsv')
gate=('DP54/56/58 close global finite-jet existence and quantitative interpolation. DP55/57 construct the exact mixed-type endpoint Fi period and its adelic realization over E(i), at a fresh split principal level, with actual value1. DP59 identifies the exact generic permitted theta-translate lattice and proves that individual allowed translates already attain the sharp ordinary/two-row harmonic valuations at polynomial levels. DP60 supplies global interpolants with constant p-adic precision, no new good-prime denominators and logarithmic section sup-size O(degree). Remaining: one compatible mixed-type Moduli/CMObj construction and its actual nonzero iterated theta image, the prescribed full row degrees/selected functional, all six lift identities, and a net integer-saving comparison including source normalization, row, rank, level and polarization costs. Neither a shorter chain nor general minimality is proved.')
for q in qs:
 if q['id']=='Q3e':q.update(finding_ids_or_counterexample='U2;DP25-DP60',current_gate_or_scope=gate)
newqs=[
 ('Q3as','DP57;StatementMass IsCMUnram;RecLevelStep20-51;TiedValFi239-255','Can the concrete mixed CM example satisfy the generic unramified host and actual adelic endpoint interfaces?','proved with stated remaining type boundary','DP57','E(i)=Q(zeta28), J² with integral rotation action and principal polarization, and a fresh split principal29-level satisfy the generic Host, genus, reduction, DecoPtSurj and IsLevOf inputs. The endpoint has an actual nonzero period. Old induced-quadratic CMObj/Datum and eight-divisibility wrapper remain inapplicable.'),
 ('Q3at','DP59;IsVtOver32-42;ThetaPt SymLift44-51;Mumford1966 §1','Do the actual generic permitted torsion translates realize the sharp higher-height ordinary and two-row harmonic jets?','proved','DP59','Their integral span is [alpha]*H0(L^M), rank M^g, with a basis indexed A[alpha²]/A[alpha]. It separates n-jets for M>=rn+b. Some individual permitted translate or pair has exact DP58 valuation, with M=29^e=O(n) and kappa=O(n²). Old CM-type and selected-theta-image membership are not inferred.'),
 ('Q3au','DP60;DP56;Stacks02KH','Can finite sharp global theta jets be realized with controlled section size and bounded integral precision?','proved','DP60','Modulo11 precision already preserves every explicit finite witness. Bounded algebraic residue representatives yield sections over OE[1/14] with log sup norm O(kappa+log n), kappa=O(n), and no new good-prime denominators. These are full-section-space norms in fixed metrics, not the source level-dependent gauge or a complete gain-minus-cost comparison.')]
ids={q['id'] for q in qs}
for q in newqs:
 if q[0] not in ids:qs.append(dict(zip(qf,q)))
write(root/'QUESTIONS.tsv',qf,qs)
total=len(ms);extra=total-526
readme=root/'README.md';s=readme.read_text().replace('Run DP_MULT_20261121;21November2026,Europe/Berlin.','Run DP_MULT_20261121; 21 November 2026, UTC. Early event records preserve their original date labels; exact later timestamps use UTC.')
s=re.sub(r'the\d+ targeted modules:526 checked in the recorded full sweep and\d+ directly extracted',f'the {total} targeted modules: 526 checked in the recorded full sweep and {extra} directly extracted',s)
readme.write_text(s)
p=root/'DP_MULT.tex';s=p.read_text()
s=re.sub(r'The expanded targeted inventory contains \d+ modules, recovered either.*?Exact declaration locators',lambda _:f'The expanded targeted inventory contains {total} modules, recovered either at mirror commit \\path{{7cbf7a0c32fca1badf05931879a37c3f8a2b03b4}} or directly from the author\'s archive. The recorded sweep compared 526 local copies byte for byte with the original archive, all matching; {extra} further modules were extracted directly from that archive with exact member and byte hashes, as recorded in the successive manifests. Exact declaration locators',s,flags=re.S)
p.write_text(s)
print(json.dumps({'recorded_utc':now,'events':len(es),'questions':len(qs),'source_modules':total,'added_source_rows':len(added)}))
