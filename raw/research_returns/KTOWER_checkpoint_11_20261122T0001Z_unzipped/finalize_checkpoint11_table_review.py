from pathlib import Path
import json,hashlib,datetime,csv,shutil
B=Path(__file__).resolve().parent;now=datetime.datetime.now(datetime.timezone.utc).isoformat();h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old=json.loads((B/'pdf_review11_postnotes/render_manifest.json').read_text());new=json.loads((B/'pdf_review11_tablefix/render_manifest.json').read_text())
assert h(B/'KTOWER.tex')==new['tex_sha256'] and h(B/'KTOWER.pdf')==new['pdf_sha256']
assert new['changed_pages']==[5,*range(237,251)]
paths=['evidence/unitary_audit/checkpoint11_postnotes_visual_review.json','evidence/geometry_tower/checkpoint11_postnotes_layout_review.json','evidence/lean_chain/pdf_checkpoint11_postnotes_layout_review.json','evidence/root_pdf11_postnotes_review.json']
for p in paths:
 data=(B/p).read_text();assert old['pdf_sha256'] in data,(p,'wrong predecessor')
r={'checked_utc':now,'reviewer':'/root; GPT-6 Astra Pro; effort setting not exposed','scope':'Fresh actual visual inspection of all15changed pages5,237-250 using three sheets, plus enlarged237,240,244. All other235pages are exact pixel matches to the fully visually reviewed248-page predecessor.','pdf_sha256':new['pdf_sha256'],'tex_sha256':new['tex_sha256'],'pages_freshly_viewed':new['changed_pages'],'enlarged_pages':[237,240,244],'result':'PASS: split rows fit well above footer; TOC, table and end prose fit without overlap or clipping.','layout_only':True,'mathematical_scope':'Two table-row splits retain every assertion and add only repeated object-description cells; full mathematical proofs unchanged.','pixel_lineage_manifest':{'path':'pdf_review11_tablefix/render_manifest.json','sha256':h(B/'pdf_review11_tablefix/render_manifest.json')},'predecessor_reviews':[{'path':p,'sha256':h(B/p)} for p in paths]}
rp=B/'evidence/root_pdf11_tablefix_review.json';rp.write_text(json.dumps(r,indent=2)+'\n');paths.append(str(rp.relative_to(B)))
# Lossless deduplication of new contact-sheet caches; do not remove local originals.
dp=B/'REBUILDABLE_DUPLICATES.json';dup=json.loads(dp.read_text());omitted={x['omitted_cache_path'] for x in dup['files']};index={}
for p in sorted(B.glob('pdf_review*/*.png')):
 rel=str(p.relative_to(B))
 if rel in omitted or rel.startswith('pdf_review11_postnotes/') or rel.startswith('pdf_review11_tablefix/'):continue
 index.setdefault(h(p),rel)
added=[]
for p in sorted(list((B/'pdf_review11_postnotes').glob('*.png'))+list((B/'pdf_review11_tablefix').glob('*.png'))):
 rel=str(p.relative_to(B));hh=h(p)
 if rel in omitted:continue
 if hh in index:
  assert p.read_bytes()==(B/index[hh]).read_bytes()
  item={'omitted_cache_path':rel,'canonical_path':index[hh],'sha256':hh,'bytes':p.stat().st_size};dup['files'].append(item);added.append(item)
 else:index[hh]=rel
dup['date_utc']=now;dup['scope']='Only byte-identical rendered cache copies listed here are omitted from future ZIPs; canonical PNGs, whole-page pixel manifests, original reviews, source PDFs and restoration script retain all evidence. No older ZIP modified.'
dp.write_text(json.dumps(dup,indent=2)+'\n')
shutil.copy2(B/'PDF_REVIEW.json',B/'evidence/checkpoint11_table_fix/previous_PDF_REVIEW.json')
report={'tex_sha256':new['tex_sha256'],'pdf_sha256':new['pdf_sha256'],'pages':new['pages'],'pages_rendered':list(range(1,new['pages']+1)),'checked_utc':now,'reviewer':'/root and three named peers; GPT-6 Astra Pro; effort setting not exposed','complete_visual_review':True,'review_evidence':[{'path':p,'sha256':h(B/p)} for p in paths],'scope':'Predecessor248pages completely visually inspected by unitary1-60,geometry61-120,lean121-180,root181-248. Two oversized table rows split. All15changedpages5,237-250 freshly viewed by root, with237,240,244 enlarged. Exact whole-page pixel comparison proves remaining235pages identical to predecessor. Layout review is separate from mathematical whole-proof checks.','render_manifest':'pdf_review11_tablefix/render_manifest.json','render_manifest_sha256':h(B/'pdf_review11_tablefix/render_manifest.json'),'contact_sheets':[x['path'] for x in new['sheets']],'predecessor_render_manifest':'pdf_review11_postnotes/render_manifest.json','formatting_repairs':['Two oversized crosswalk rows split at semantic boundaries; no mathematical text deleted.'],'build':'checkpoint11_tablefix_pass3.log: no warnings, overfull boxes or undefined references. Only pdflatex invoked; no Lean build or run.','duplicate_cache_manifest':{'path':'REBUILDABLE_DUPLICATES.json','sha256':h(dp)}}
(B/'PDF_REVIEW.json').write_text(json.dumps(report,indent=2)+'\n')
with (B/'ROOT_CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['KT-PDF-CHECKPOINT11-POSTNOTES',now,'/root; run KTOWER','GPT-6 Astra Pro','not exposed','used and rechecked in this run','PASS actual pages181-248 visual inspection; two footer encroachments corrected,15changedpages freshly inspected; full250page visual coverage with pixel lineage','evidence/root_pdf11_postnotes_review.json; evidence/root_pdf11_tablefix_review.json; PDF_REVIEW.json'])
print(json.dumps({'pdf_review_sha256':h(B/'PDF_REVIEW.json'),'pages':new['pages'],'duplicates_added':len(added),'raw_bytes_saved':sum(x['bytes'] for x in added),'total_duplicates':len(dup['files'])}))
