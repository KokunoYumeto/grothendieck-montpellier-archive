"""Join existing evidence and manually curated census labels to final records.

This program makes no mathematical verdicts. It transports the reviewer
decisions, exact search ledgers, and declared provenance into final IDs.
"""
from pathlib import Path
from collections import Counter, defaultdict
import csv, json, re
B=Path(__file__).resolve().parents[2]; W=B/'work'; D=B/'deliverables'
def read(p):return json.loads(p.read_text())
def save(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def rows(p):return list(csv.DictReader(p.open(),delimiter='\t'))
def tsv(n,x,fields):
 with (D/n).open('w') as f:
  q=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore');q.writeheader()
  for z in x:q.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in z.items()})
ids=read(D/'SA15_id_map.json'); claims=read(D/'SA15_claims.json')
refs={x['key']:x for x in read(D/'SA15_reference_evidence.json')}
statuses={x['legacy_claim_id']:x for x in rows(W/'global_audit/status_index.tsv')}

def remap(s):
 return re.sub(r'P(?:56|67|78|894)-[ICP]\d{3}',lambda m:ids.get(m.group(),m.group()),s)
status_rows=[]
for c in claims:
 ss=[statuses[x] for x in c['legacy_ids']]
 buckets=list(dict.fromkeys(s['census_bucket'] for s in ss))
 bucket=buckets[0] if len(buckets)==1 else 'mixed or conditional page status'
 c['status_census']=bucket
 c['status_census_basis']={'source':'work/global_audit/status_index.tsv',
   'component_buckets':buckets,
   'reason':'Transported individually read documentary labels; different component statuses remain mixed after a continuous-calculation merge.' if len(buckets)>1 else 'Transported individually read census label; original status_on_pages remains authoritative.'}
 refinement=any(s['is_present_run_refinement']=='True' for s in ss)
 o=str(c.get('origin','manuscript'))
 if refinement: origin='present-run refinement'
 elif o=='foreign inserted text':origin='foreign inserted text'
 elif o=='later comparison identified by the earlier run':origin='later comparison identified by earlier run'
 elif o=='idea of the earlier run, rechecked here':origin='earlier-run assertion rechecked here'
 else:origin='manuscript or transcribed reused text'
 c['origin_census']=origin
 # These six records explicitly state the counterstatement/qualified result
 # in their statement field, alongside a separate report of the manuscript.
 # Their refutation event therefore points to that same compound record.
 same_record_refinements={'P894-C006','P894-C023','P894-C025','P894-C071','P894-C072','P894-C077'}
 if set(c['legacy_ids']) & same_record_refinements:
  c['refined_statement_id']=c['id']
  c['refined_statement']=('For d≥2 the reduction GL_d(Z/p²)→GL_d(F_p) has the recorded exceptional splitting cases (d,p)=(2,2),(2,3),(3,2); the d=2,p=2 section is independently certified here. The full list is read through Singla’s exact backward reference, not an independently audited original classification proof.'
    if 'P894-C006' in c['legacy_ids'] else c['statement'])
  c['refutation_target_convention']='This record contains the literal manuscript report and the explicit corrected statement; the check event identifies this corrected field under the same record ID.'
 for s in ss:status_rows.append({'claim_id':c['id'],**s})
 # A generic date note is supplemented, never converted into a fabricated
 # first-circulation date. Source dates are not priority claims.
 old=c['fate_date'];chron=[]
 for key in c['refs']:
  e=refs[key];dates=[]
  for inspection in e['inspections']:
   for k in ['date_evidence','dates','date_history','first_circulation','publication_date','version_date']:
    if inspection.get(k):dates.append(str(inspection[k]))
  chron.append({'key':key,'bibliographic_year':e['fields'].get('year'),
    'circulation_or_version_evidence':list(dict.fromkeys(dates)),
    'qualification':'An unspecified first circulation date is unknown; bibliographic year alone is not a first-circulation claim.'})
 c['fate_date']={'as_of':'2026-11-19','reviewer_date_record':old,'reference_chronology':chron}
save('SA15_claims.json',claims)
tsv('SA15_status_census.tsv',status_rows,['claim_id','legacy_claim_id','package','census_bucket','documentary_component','modern_validity_component','status_mixture','is_present_run_refinement','status_on_pages_original','origin_original','origin_provenance_note','normalization_reason'])

# Exact query transport. The source-family grouping was curated by the readers.
search={};families=[]
p56f={x['id']:x for x in read(W/'cotes5_6/search_families.json')}
for c in read(W/'cotes5_6/claims.json'):
 fam=c['literature_search_history']['family_id'];f=p56f[fam]
 search[c['id']]={'family':'P56:'+fam,'ledger':'work/cotes5_6/search_families.json',
   'queries':f.get('queries',[]),'source_investigation':f.get('checked_hits',[]),
   'limits':f.get('limitations_and_unsuccessful_searches',[])}
for f in p56f.values():families.append({'package':'P56',**f})
q67={x['query_id']:x for x in rows(W/'cotes6_7/query_log.tsv')}
for x in rows(W/'cotes6_7/search_by_claim.tsv'):
 search[x['claim_id']]={'family':x['families'],'ledger':'work/cotes6_7/search_by_claim.tsv',
  'queries':[q67[k] for k in x['query_ids'].split(';') if k],
  'source_investigation':x['opened_reference_keys'],'limits':x['exact_match_or_limit']}
for x in rows(W/'root_review/literature_search.tsv'):
 search[x['claim_id']]={'family':'P78:'+x['search_family'],'ledger':'work/root_review/literature_search.tsv',
  'queries':x['queries'],'source_investigation':x['opened_reference_keys'],
  'limits':x['scope_result'],'search_mode':x['search_mode']}
for f in read(W/'root_review/search_families.json'):families.append({'package':'P78',**f})
qsg={x['query_id']:x for x in rows(W/'cotes6_7/sga7_query_log.tsv')}
for x in rows(W/'cotes6_7/supplementary_root_search_by_claim.tsv'):
 search[x['claim_id']]={'family':'VGR:exact-follow-up','ledger':'work/cotes6_7/sga7_query_log.tsv',
  'queries':[qsg[k] for k in x['query_ids'].split(';') if k],
  'source_investigation':x['opened_reference_keys'],'limits':x['exact_match_or_limit']}
search['P78-C035']['supplementary_exact_search']=search['P78-C071']

p894sessions={}
for p in sorted((W/'cotes8_9_4/outputs').glob('search_sessions_*.json')):
 for x in read(p):p894sessions[x['search_id']]=x
family894={}
for line in (W/'cotes8_9_4/research_log.md').read_text().splitlines():
 if not re.match(r'\| F\d\d \|',line):continue
 _,fam,issue,sessions,boundary,_=line.split('|')
 nums=[]
 for a,b in re.findall(r'S(\d{3})(?:[–-]S(\d{3}))?',sessions):
  nums.extend(range(int(a),int(b or a)+1))
 fam=fam.strip();requests=[p894sessions[f'P894-S{n:03}']['request'] for n in dict.fromkeys(nums)]
 family894[fam]={'family':'P894:'+fam,'ledger':'work/cotes8_9_4/research_log.md; work/cotes8_9_4/outputs/search_sessions_*.json',
   'queries':requests,'source_investigation':issue.strip(),'limits':boundary.strip()}
for cid,fam in read(W/'cotes8_9_4/claim_search_families.json').items():search[cid]=family894[fam]

searchrows=[]
for c in claims:
 parts=[]
 for old in c['legacy_ids']:
  assert old in search,('unsearched claim',old)
  parts.append({'legacy_id':old,**search[old]})
 searchrows.append({'claim_id':c['id'],'as_of':'2026-11-19',
  'search_families':list(dict.fromkeys(x['family'] for x in parts)),
  'search_evidence':parts,'exact_fate_assessment':c['fate'],'reference_keys':c['refs']})
tsv('SA15_claim_search.tsv',searchrows,['claim_id','as_of','search_families','search_evidence','exact_fate_assessment','reference_keys'])
save('SA15_search_families.json',families+list(family894.values()))

# One accessible citation key/URL guide, with inspection limits kept in JSON.
guide=['# Reference keys and opened sources','',
 'The bibliography note records access, not an independent proof certificate. '
 'Detailed locators, version dates and inspection limits are in `SA15_reference_evidence.json`.','',
 '| Key | Work | Year | Access | Link |','|---|---|---|---|---|']
for key,e in sorted(refs.items()):
 f=e['fields'];title=f.get('title','').replace('|','\\|');url=f.get('url','')
 guide.append('| '+key+' | '+title+' | '+f.get('year','')+' | '+f['note']+' | '+('[source]('+url+')' if url else 'No verified URL')+' |')
(D/'SA15_reference_guide.md').write_text('\n'.join(guide)+'\n')

stats=read(D/'SA15_core_counts.json');stats.update(read(D/'SA15_aux_counts.json'))
stats['claim_status_census']=dict(Counter(c['status_census'] for c in claims))
stats['claim_origin_census']=dict(Counter(c['origin_census'] for c in claims))
stats['claims_with_search_evidence']=len(searchrows)
stats['directions']=12
save('SA15_counts.json',stats)
print(json.dumps({'claims':len(claims),'searched_claims':len(searchrows),
 'raw_status_rows':len(status_rows),'status_counts':stats['claim_status_census'],
 'origin_counts':stats['claim_origin_census']},ensure_ascii=False))
