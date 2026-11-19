"""Attach executed exact searches and successfully opened source URLs to manual claims."""
from pathlib import Path
import json,csv,re
R=Path('/workspace/scratch/a77a578fa7d4/SA12_work/reviews/31')
Q=json.loads((R/'search_manifest.json').read_text())
C=json.loads((R/'claims.json').read_text())
B={x['key']:x for x in json.loads((R/'reference_verification.json').read_text())}
rows=[];byquery={}
for p in sorted((R/'outputs').glob('search_audit_*.json')):
 d=json.loads(p.read_text());result=d['result'];text='\n'.join(x.get('text','') for x in result.get('content',[]) if x.get('type')=='text')
 hits=re.findall(r'([^\n]+) \((https?://[^\n]+)\)\n【([^】]+)】',text)
 rr=[dict(title=a,url=b,ref=c) for a,b,c in hits]
 for q in d['request']['queries']:
  byquery[q['query_id']]=dict(response_file=str(p.relative_to(R)),results=rr,ok=not result.get('isError',False) and 'error' not in result)
for q in Q:
 a=byquery[q['query_id']];assert a['ok'],q['query_id']
 refs=[k for k in q['refs'] if k in B]
 opened=[B[k]['url'] for k in refs if B[k]['note']=='verified']
 row=dict(query_id=q['query_id'],date='2026-11-19',engine=q['engine'],exact_query=q['query'],claims=';'.join(q['claims']),purpose=q['scope'],response_file=a['response_file'],results_scope='Combined results for this four-or-fewer-query batch; not attributed to one query by the search API.',result_urls=';'.join(x['url'] for x in a['results']),primary_urls_opened=';'.join(opened),primary_locator=';'.join(k+': '+B[k]['locator'] for k in refs),assessment='Compare exact hypotheses in claims.json; retrieved summaries/AI translations were not treated as theorem evidence.')
 rows.append(row)
def tsv(path,rows,fields):
 with path.open('w',newline='') as f:
  w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
tsv(R/'literature_search_log.tsv',rows,list(rows[0]))
tsv(R/'claim_search_map.tsv',[dict(claim_id=c['id'],query_id=q['query_id'],scope=q['scope']) for c in C for q in Q if c['id'] in q['claims']],['claim_id','query_id','scope'])
old=[dict(claim_id=c['id'],exploratory_query_ids=';'.join(c.get('query_ids',[]))) for c in C]
tsv(R/'exploratory_query_map.tsv',old,['claim_id','exploratory_query_ids'])
for c in C:c['query_ids']=[q['query_id'] for q in Q if c['id'] in q['claims']]
(R/'claims.json').write_text(json.dumps(C,ensure_ascii=False,indent=2)+'\n')
# Log direct openings separately. An attempted URL is not a successful verification.
openrows=[]
for p in sorted((R/'outputs').glob('web_*.json')):
 d=json.loads(p.read_text());text='\n'.join(x.get('text','') for x in d.get('content',[]) if x.get('type')=='text')
 for block in text.split('\n--------------------------------------------------------------------------------\n'):
  src=re.search(r'Source: (open|find|click|screenshot)\((\{.*?\})\)',block)
  if not src:continue
  try:request=json.loads(src.group(2))
  except json.JSONDecodeError:continue
  ref=re.search(r'【([^】]+)】',block);heading=block.strip().split('\n')[0]
  url=re.search(r'\((https?://[^\n]+)\)',heading)
  openrows.append(dict(file=str(p.relative_to(R)),operation=src.group(1),request=json.dumps(request,ensure_ascii=False),source_ref=ref.group(1) if ref else '',url=url.group(1) if url else request.get('ref_id',''),status='failed' if re.search(r'Failed to fetch|Internal Error|403\)? Forbidden|502\)? Bad Gateway',block) else 'returned content',title=heading))
tsv(R/'opened_sources.tsv',openrows,['file','operation','request','source_ref','url','status','title'])
(R/'literature_search_log.md').write_text('''# Literature-search audit for cote31

All126 claim records are mapped in `claim_search_map.tsv` to51 exact queries whose requests and responses are retained in `outputs/search_audit_*.json`. These are the closing reproducibility searches. The earlier exploratory responses are retained in `outputs/web_search*.json`, and the earlier working query identifiers are preserved in `exploratory_query_map.tsv`; the closing manifest replaces those working identifiers for audit purposes.

The search service returns combined results for each batch. The TSV therefore labels the result URL list as combined batch results; it does not pretend that each hit came from a particular query. The `primary_urls_opened` column identifies sources actually opened elsewhere in this same run, and the adjacent locator records the theorem or passage read. `opened_sources.tsv`, raw web responses, the primary read log, and selected primary excerpts provide the access trail. A search hit is not recorded as an opened source merely because it appeared in the results.

The search used both available search engines, with stronger-engine follow-up for difficult unmatched formulations, and searches directed to zbMATH Open, arXiv, MathOverflow and Numdam. Exact EGA/SGA passages and author-hosted texts supplied the mathematical comparisons. Direct zbMATH attempts returned access errors in the exploratory trail; those are not called successful verification. MathOverflow served as discovery: the closed-restriction question found there concerns pullback of modules on a ringed scheme, so it was explicitly rejected as an exact match for the manuscript’s inverse image of abelian sheaves on the Zariski space.

Search results from AI-translated SGA sites, generated course sites, aggregators and search snippets were not used as mathematical evidence. The supplied Pro notes’ references were reopened in real editions. Named earlier project runs were not evidence for any claim’s fate.

Negative findings are bounded: an exact match was not located within the documented searches. They do not assert that no theorem exists. The nonproper Picard prompt was followed backward to Murre1964; its stated Picard application is proper. The nonabelian base-change prompt was followed forward to Haine–Holzschuh–Wolf2024 and backward to its Giraud reference, with the latter original book explicitly unverified. The flat-dimension prompt was followed to Shatz1966 through MilneADT; metadata is verified, full Shatz proof was not obtained. The relative-projectivity trail was followed to Broué2007 and the two distinct1954 Higman papers it cites.
''')
print(json.dumps({'exact_queries':len(rows),'claim_query_links':sum(len(c['query_ids']) for c in C),'claims':len(C),'opened_operations':len(openrows)}))
