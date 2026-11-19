"""Structural audit and serialization of the manually assigned source/search map."""
from pathlib import Path
from collections import Counter
import json,csv
B=Path(__file__).resolve().parents[1];O=B/'parts/root'
claims=json.loads((O/'claims.json').read_text());items=json.loads((O/'items.json').read_text());problems=json.loads((O/'problems.json').read_text())
refs={x['key']:x for x in json.loads((O/'references.json').read_text())}
searches={x['id']:x for x in json.loads((B/'research/root_research_log.json').read_text())}
entries=list(csv.DictReader((O/'entries.tsv').open(),delimiter='\t'))
ids={x['id'] for x in items}
assert len(entries)==107 and len({r['entry_id'] for r in entries})==107
assert all(e['item_id'] in ids for e in entries)
assert all(c['items'] and all(i in ids for i in c['items']) for c in claims)
assert all(c['refs'] and all(r in refs for r in c['refs']) for c in claims)
assert all(c['research_searches'] and all(s in searches for s in c['research_searches']) for c in claims)
assert all(p['refs'] and all(r in refs for r in p['refs']) for p in problems)
for c in claims:
 co=c['computation']
 if 'code' in co:
  assert (B/co['code']).exists(),(c['id'],co['code'])
  out=json.loads((B/co['output']).read_text())
  assert all(k in out for k in co['certificate_keys']),(c['id'],co['certificate_keys'],list(out))
rows=[]
for c in claims:
 for sid in c['research_searches']:
  s=searches[sid]
  rows.append(dict(statement_id=c['id'],search_id=sid,date=s['date'],queries=' | '.join(s['queries']),opened_references='; '.join(c['refs']),exact_match_or_limit=c['fate']))
# Explicit, manually assigned problem-search families; no thematic auto-matching.
groups={1:'RS-CORRESP',2:'RS-CORRESP',3:'RS-CORRESP',4:'RS-DIAGONAL',5:'RS-DIAGONAL',6:'RS-DIAGONAL',7:'RS-DIAGONAL',8:'RS-DIAGONAL',9:'RS-DIAGONAL',10:'RS-DIAGONAL',11:'RS-QUADRIC',12:'RS-QUADRIC',13:'RS-QUADRIC',14:'RS-QUADRIC',15:'RS-QUADRIC',16:'RS-QUADRIC',17:'RS-QUADRIC',18:'RS-QUADRIC',19:'RS-QUADRIC',20:'RS-QUADRIC',21:'RS-QUADRIC',22:'RS-TORI',23:'RS-TORI',24:'RS-TORI',25:'RS-TORI',26:'RS-TORI',27:'RS-TORI',28:'RS-TORI',29:'RS-TORI',30:'RS-TORI',31:'RS-DELZANT',32:'RS-DELZANT',33:'RS-STEIN',34:'RS-COHERENCE',35:'RS-STEIN',36:'RS-STEIN',37:'RS-DIMENSION',38:'RS-DIMENSION',39:'RS-TORUS'}
for p in problems:
 sid=groups[int(p['id'].split('-')[-1])-11000];s=searches[sid]
 rows.append(dict(statement_id=p['id'],search_id=sid,date=s['date'],queries=' | '.join(s['queries']),opened_references='; '.join(p['refs']),exact_match_or_limit=p['state_of_art']))
with (O/'literature_search.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=['statement_id','search_id','date','queries','opened_references','exact_match_or_limit'],delimiter='\t');w.writeheader();w.writerows(rows)

coverage={'owner':'root','method':'Complete direct sequential source reading, followed by targeted rereading; saved source outputs document the read passages. No verdict was inferred from a keyword or heading.',
 'files':[
  {'file':'SA18_texts/pro/MPL_11_043-058+56_transcription.tex','lines':[1,1958],'status':'fully read'},
  {'file':'SA18_texts/codex/K55-01_transcription.tex','lines':[1,574],'status':'fully read'},
  {'file':'SA18_texts/codex/K56-01_transcription.tex','status':'fully read'},
  {'file':'SA18_texts/codex/K56-02_transcription.tex','status':'fully read'},
  {'file':'SA18_texts/codex/K56-03_transcription.tex','status':'fully read'},
  {'file':'SA18_notes/pro/MPL_11_043-058+56_notes.md','entries':[1,107],'status':'fully read, including appendices'},
  {'file':'SA18_notes/pro/MPL_11_043-058+56_doubts.md','status':'fully read'},
  {'file':'SA18_notes/codex/K55-01_notes.md','status':'fully read'},
  {'file':'SA18_notes/codex/K56-01_notes.md','status':'fully read'},
  {'file':'SA18_notes/codex/K56-02_notes.md','status':'fully read'},
  {'file':'SA18_notes/codex/K56-03_notes.md','status':'fully read'}],
 'documentary_outputs':[str(p.relative_to(B)) for p in sorted((B/'outputs').glob('root_*'))],
 'public_sources':'Original EGA IV.1/IV.2, SGA3 XII/XIV, SGA7 II and other PDFs were read outside the deliverable tree. Exact locators and verification scope are in references.json, not copies of the copyrighted source bodies.'}
(O/'read_coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2))
audit={'entries':len(entries),'items':len(items),'claims':len(claims),'problems':len(problems),'references':len(refs),'claim_classes':dict(Counter(c['class'] for c in claims)),'claim_statuses':dict(Counter(c['status_on_pages'] for c in claims)),'literature_rows':len(rows),'all_claims_searched':True,'all_problems_have_opened_comparators':True,'all_named_certificates_exist':True,'verification_note':'Search assignments and exact-match decisions were authored manually; this program checks their completeness and file/reference integrity.'}
(O/'audit.json').write_text(json.dumps(audit,indent=2));print(json.dumps(audit,indent=2))
