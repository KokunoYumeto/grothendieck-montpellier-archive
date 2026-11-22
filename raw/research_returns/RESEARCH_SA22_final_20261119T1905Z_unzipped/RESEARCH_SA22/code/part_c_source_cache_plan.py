"""Produce an exact, read-only normalization proposal after manual content review.

Only this utility's plan/output files are written. No input is normalized here.
"""
import datetime,hashlib,json,pathlib,re,time
ROOT=pathlib.Path(__file__).resolve().parents[1]
tick=time.perf_counter(); started=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(b):return hashlib.sha256(b).hexdigest()
def meta(rel):
 p=ROOT/rel;b=p.read_bytes();return {'path':rel,'bytes':len(b),'sha256':sha(b),'mtime_ns':p.stat().st_mtime_ns}
def at(o,ptr):
 for bit in ptr.strip('/').split('/'):
  bit=bit.replace('~1','/').replace('~0','~');o=o[int(bit)] if isinstance(o,list) else o[bit]
 return o
def field(o,ptr,reason,block=None):
 s=at(o,ptr);assert isinstance(s,str)
 d={'pointer':ptr,'reason':reason,'field_characters':len(s),'field_utf8_bytes':len(s.encode()),'field_sha256':sha(s.encode())}
 if block is not None:
  parts=re.split(r'\n-{8,}\n',s);b=parts[block]
  d.update(mode='one_source_block_in_string',separator_regex=r'\n-{8,}\n',zero_based_block=block,block_count=len(parts),block_characters=len(b),block_utf8_bytes=len(b.encode()),block_sha256=sha(b.encode()),reference_ids=re.findall(r'【([^】]+)】',b),urls=list(dict.fromkeys(re.findall(r'https?://[^\s)<>]+',b))))
 else:d['mode']='whole_string'
 return d

direct=[]
for rel,reason in [
 ('notes/a567_review_Solynin1999.txt','Complete raw Solynin article extraction; authored analysis is elsewhere.'),
 ('notes/part_c_archive_index.html','Raw public archive-index HTML; URLs/provenance are already in authored notes.'),
 *[(f'notes/original_scans_a567/hoshi_rims1558_pdf_{n}.png','Complete non-user Hoshi source-page image, not our paper QA or a user manuscript page.') for n in [56,61,65]]]:
 direct.append({**meta(rel),'action':'exclude_reproducible_cache','reason':reason})

embedded=[]
for ext in ['json','txt']:
 for stem,pointers in [
  ('part_c_a2b_audit_admissibility_page_output',['/embedded_text']),
  ('part_c_a2b_audit_source_pages_output',[f'/rendered_pages/{i}/embedded_text' for i in range(6)]),
  ('part_c_gabriel_locate_output',[f'/hits/{i}/page_head' for i in range(16)]),
 ]:
  rel='code/'+stem+'.'+ext;o=json.loads((ROOT/rel).read_text())
  reason='Raw extracted mathematical source-page text; preserve page number, source path, query/hit count and execution metadata.'
  embedded.append({**meta(rel),'action':'normalize_selected_fields_after_authorization','fields':[field(o,p,reason) for p in pointers]})

for name,ptr,block,reason in [
 ('part_a567_fujiwara1992_system1_queries.json','/result/content/0/text',5,'Cox1978 original mathematical first-page body, including introduction and start of definition; approximately520retrieved words.'),
 ('part_a567_fujiwara_ias_discovery_1634.json','/result/content/0/text',8,'Original IAS1991–92report body spanning source lines0–278/PDFpages6–19; over3000retrieved words, beyond factual catalogue metadata.'),
 ('part_a567_fujiwara_ias_provenance_1635.json','/content/0/text',2,'Original IAS1991–92report find response with416source lines and over3000retrieved words; retain specific Fujiwara locators in authored audit.'),
 ('part_b_lieberman_variants_web_output.json','/result/content/0/text',2,'Original standard-conjectures mathematical page body, including Hodge-type conjecture and remarks; approximately364retrieved words.'),
 ('part_c_pfluger_distinct_search1.json','/result/content/0/text',10,'Original Conformal Welding chapter body with equations and multiple paragraphs; approximately430retrieved words.')]:
 rel='code/'+name;o=json.loads((ROOT/rel).read_text())
 embedded.append({**meta(rel),'action':'normalize_selected_source_block_after_authorization','fields':[field(o,ptr,reason,block)]})

optional=[]
for ext in ['json','txt']:
 rel='code/part_c_lieberman_historical_landing_output.'+ext;o=json.loads((ROOT/rel).read_text())
 optional.append({**meta(rel),'action':'optional_catalogue_thumbnail_cache_only','fields':[field(o,'/images/1/src','Embedded13142-character data-image GIF from a catalogue landing page; image identity not reinterpreted as mathematical evidence. Preserve media type/hash/dimensions if normalization is chosen.')]})

plan={'snapshot_utc':started,'scope':'Bounded source-cache hygiene outside sources/. This proposal is not an authorization and does not mutate any reviewed input. Keep factual catalogue metadata, bounded snippets and all authored/mathematical execution outputs.','direct_exclusions':direct,'embedded_source_normalization':embedded,'optional_binary_catalogue_cache':optional,'preserve_notes':['All authored Markdown/TeX proofs and audit notes, including quotation-aware source derivations.','All mathematical finite certificates and program outputs, regardless of size.','All user-provided manuscript images in notes/original_scans_a567 other than the three named Hoshi pages.','Generated qa/paper*.png images; other qa literature images are already excluded by current filter.','Large factual catalogue/identifier inventories, library holdings, reference lists, abstracts and short bounded snippets are not marked for blanket exclusion.','A567s eight latest Lieberman records are already normalized; retain their metadata replacements and normalization manifest.'],'pre_normalization_requirements':['Verify original bytes/hash still match the plan.','Preserve exact original bytes outside the deliverable and record the raw-backup path/hash.','For selected strings or selected blocks preserve source URL/refID, page/line locator, character count and SHA256; retain untouched query/time/status/count metadata and unselected factual blocks.','Do not change prior checkpoints or claim a new mathematical/source gate closure.']}
dest=ROOT/'checks/part_c_source_cache_plan.json';dest.write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
out={'started_utc':started,'runtime_seconds':time.perf_counter()-tick,'network_requests':0,'mathematical_checks':0,'input_files_changed':0,'plan_path':str(dest.relative_to(ROOT)),'plan_sha256':sha(dest.read_bytes()),'direct_exclusion_files':len(direct),'direct_exclusion_bytes':sum(x['bytes'] for x in direct),'embedded_files':len(embedded),'embedded_whole_string_fields':sum(sum(f['mode']=='whole_string' for f in x['fields']) for x in embedded),'embedded_selected_source_blocks':sum(sum(f['mode']=='one_source_block_in_string' for f in x['fields']) for x in embedded),'embedded_total_file_bytes':sum(x['bytes'] for x in embedded),'optional_thumbnail_files':len(optional)}
outpath=ROOT/'code/part_c_source_cache_plan_output.json';outpath.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
