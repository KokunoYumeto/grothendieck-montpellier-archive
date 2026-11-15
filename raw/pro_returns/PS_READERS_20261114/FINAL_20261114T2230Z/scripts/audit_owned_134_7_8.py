"""Non-mutating source-ID audit of the pages assigned to the 134-7/8 reviewer.

This checks the recorded completeness of actual reviews; it does not infer or
certify visual inspection from file existence alone.
"""
from pathlib import Path
import csv,json,collections,re,importlib.util
P=Path(__file__).resolve().parents[1];I=P.parent/'inputs/text';R=P/'records'
s=importlib.util.spec_from_file_location('review',Path(__file__).with_name('review_134_7_8.py'));review=importlib.util.module_from_spec(s);s.loader.exec_module(review)
def read(p):return list(csv.DictReader(p.open(),delimiter='\t'))
owned=[f'ps_134-{c}_{n:03d}' for c,end in [(6,60),(7,112),(8,39)] for n in range(1,end+1)]
rows=read(R/'CHECK_DECISIONS_134_7_8.tsv');ledger=read(R/'PAGE_REVIEW_134_7_8.tsv');ids=collections.Counter(x['source_id'] for x in rows);reviews={x['key']:x for x in ledger}
required={'wording','formula','addition','omission','other','handwritten note added on the page, absent from arXiv (or handwritten deletion not applied)','handwritten note rewritten in arXiv','struck text printed in arXiv (handwritten deletion not applied)','unparsed'}
expected=[];before=collections.Counter();after=collections.Counter();missing_files=[];bad_reviews=[];missing_review_notes=[]
for n,row in enumerate(read(I/'records/PS_ARXIV_DIFF.tsv'),1):
 if row['page_key'] in owned and row['kind'] in required:expected.append(f'DIFF:{n}')
notes={x['key']:x for x in read(I/'transcription/ps_NOTES.tsv')}
for key in owned:
 original=(I/'transcription/ps_pages'/(key+'.tex')).read_text()
 for name in ['unsure','illegible']:
  count=len(review.macros(original,name));before[name]+=count
  expected.extend(f'{name.upper()}:{key}:{n}' for n in range(1,count+1))
 ns=[x.strip() for x in notes[key]['notes'].split(' | ') if not x.startswith('LONG-HANDWRITING:')]
 expected.extend(f'NOTE:{key}:{n}' for n in range(1,len(ns)+1));expected.append('META:'+key)
 path=P/'checked_pages'/(key+'.tex')
 if not path.exists():missing_files.append(key)
 else:
  text=path.read_text()
  for name in ['unsure','illegible']:after[name]+=len(review.macros(text,name))
  if 'not yet checked by eye.' in text:bad_reviews.append(key+': stale status')
 if key not in reviews or reviews[key]['both_halves_viewed']!='yes':bad_reviews.append(key+': missing two-half review ledger')
 rp=P/'review_notes'/(key+'.json')
 if not rp.exists():missing_review_notes.append(key)
 elif json.loads(rp.read_text()).get('both_halves_viewed') is not True:bad_reviews.append(key+': review evidence flag absent')
variants=json.loads((R/'MASTER_VARIANTS_134_7_8.json').read_text())
variant_mismatches=[]
for v in variants:
 text=(P/'checked_pages'/(v['key']+'.tex')).read_text()
 if text.count(v['before'])!=1:variant_mismatches.append({'source_id':v['source_id'],'key':v['key'],'occurrences':text.count(v['before'])})
report={'owned_pages':len(owned),'decision_rows':len(rows),'review_rows':len(ledger),'required_source_ids_by_kind':dict(collections.Counter(x.split(':',1)[0] for x in expected)),'missing_required_source_ids':[x for x in expected if ids[x]!=1],'duplicate_source_ids':[x for x,n in ids.items() if n!=1],'missing_checked_files':missing_files,'invalid_review_status':bad_reviews,'missing_evidence_json':missing_review_notes,'original_doubt_macros':dict(before),'retained_or_new_doubt_macros':dict(after),'explicit_master_variants':len(variants),'variant_source_match_exceptions':variant_mismatches,'extra_owned_keys':sorted(set(reviews)-set(owned)),'notes':'The two-half flags and per-page evidence were recorded during actual image review. This audit verifies source-ID and file coverage only; root owns final normalization, builds and PDF inspection.'}
report['coverage_complete']=not any(report[x] for x in ['missing_required_source_ids','duplicate_source_ids','missing_checked_files','invalid_review_status','missing_evidence_json','extra_owned_keys'])
(R/'OWNERSHIP_AUDIT_134_7_8.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
