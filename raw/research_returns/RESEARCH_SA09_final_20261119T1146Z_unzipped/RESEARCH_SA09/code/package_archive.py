"""Build one research ZIP, preserving certificates and omitting source caches."""
from pathlib import Path
import argparse, csv, datetime, hashlib, json, time, zipfile
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--kind',choices=['final','checkpoint'],default='final')
parser.add_argument('--number',type=int,default=1)
args=parser.parse_args()
start=time.perf_counter()
now=datetime.datetime.now(datetime.timezone.utc)
name='RESEARCH_SA09_final.zip' if args.kind=='final' else f'RESEARCH_SA09_checkpoint_{args.number:02d}.zip'
dest=ROOT.parent/name
assert not dest.exists(), 'Archives are never overwritten'
required=['RESEARCH_SA09_paper.tex','RESEARCH_SA09_paper.pdf','RESEARCH_SA09_results.csv',
 'RESEARCH_SA09_references.bib','RESEARCH_SA09_report.md','PROGRESS_LEDGER.md','CHECK_EVENTS.tsv']
if args.kind=='final':
 assert all((ROOT/p).is_file() for p in required)
 report=(ROOT/'RESEARCH_SA09_report.md').read_text()
 assert not report.startswith('INCOMPLETE') and 'ROOT_FINAL_QA_PLACEHOLDER' not in report
 last=[r for r in json.loads((ROOT/'logs'/'integrated_build.json').read_text()) if r['command'][0]=='lualatex'][-1]
 assert last['exit_code']==0 and last['over_2pt_count']==0
 assert last['missing_characters']==0 and not last['undefined_references']
 assert len(PdfReader(ROOT/'RESEARCH_SA09_paper.pdf').pages)==41
 assert len(list(csv.DictReader((ROOT/'RESEARCH_SA09_results.csv').open())))==43
 event_rows=list(csv.reader((ROOT/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
 assert len(event_rows)==181 and all(len(r)==5 for r in event_rows)
def sha(data): return hashlib.sha256(data).hexdigest()
sources=[]
for p in sorted((ROOT/'sources').rglob('*')):
 if p.is_file(): sources.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())})
(ROOT/'logs'/'source_cache_hashes.json').write_text(json.dumps(sources,indent=2))
excluded={'dold_puppe_1961_locator_text.txt','happel_1988_lawful_preview.txt',
 'happel_1988_publisher_index.txt','lang_algebra_2002_publisher_frontmatter.txt','lang_algebra_2002_ch6_publisher_preview.txt'}
excerpt_json={'requested_sources_audit.json','requested_sources_audit.stdout.txt','a3_b4_inspect_sources.json'}
def trim(obj):
 if isinstance(obj,list): return [trim(x) for x in obj]
 if not isinstance(obj,dict): return obj
 out={k:trim(v) for k,v in obj.items() if k not in {'context','statement','last_page_first_lines'}}
 if set(obj)&{'context','statement','last_page_first_lines'}: out['verbatim_source_text_omitted_from_export']=True
 return out
files=[ROOT/p for p in required+['README.md','RESEARCH_SA09_paper.bbl'] if (ROOT/p).exists()]
for directory in ['sections','notes','code','logs']:
 for p in sorted((ROOT/directory).rglob('*')):
  if not p.is_file() or '__pycache__' in p.parts: continue
  if directory=='logs' and p.name in excluded: continue
  files.append(p)
for p in sorted((ROOT/'qa').iterdir()):
 if p.is_file() and (p.name.startswith(('page-','contact-')) or p.name in
   {'QA_REPORT.md','render_manifest.json','final_image_comparison.json'}): files.append(p)
payload={};transformed=[]
for p in files:
 relative=str(p.relative_to(ROOT));data=p.read_bytes()
 if p.parent.name=='logs' and p.name in excerpt_json:
  data=(json.dumps(trim(json.loads(data)),indent=2)+'\n').encode();transformed.append(relative)
 payload[relative]=data
assert [p for p in payload if p.endswith('.pdf')]==['RESEARCH_SA09_paper.pdf']
manifest={'kind':args.kind,'created_utc':now.isoformat(),
 'start_utc':'2026-11-19T11:03:18.760737+00:00',
 'first_checkpoint_due_utc':'2026-11-19T11:48:18.760737+00:00',
 'completed_before_first_checkpoint_due':now < datetime.datetime(2026,11,19,11,48,18,760737,tzinfo=datetime.timezone.utc),
 'excluded':['original attachments','third-party source text and images','runtime caches','temporary harness PDF','earlier ZIPs'],
 'source_text_metadata_exports':transformed,
 'files':[{'path':k,'bytes':len(v),'sha256':sha(v)} for k,v in sorted(payload.items())]}
payload['ARCHIVE_MANIFEST.json']=(json.dumps(manifest,indent=2)+'\n').encode()
with zipfile.ZipFile(dest,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=8) as z:
 for relative,data in sorted(payload.items()): z.writestr('RESEARCH_SA09/'+relative,data)
with zipfile.ZipFile(dest) as z:
 assert z.testzip() is None
 assert not any(p.endswith('.zip') for p in z.namelist())
assert dest.stat().st_size<500_000_000
validation={'archive_name':dest.name,'payload_files':len(payload),
 'initial_crc_test':'passed','no_nested_zip':True,'only_pdf':'RESEARCH_SA09_paper.pdf',
 'payload_build_and_validation_seconds':round(time.perf_counter()-start,6),
 'completed_before_first_checkpoint_due':manifest['completed_before_first_checkpoint_due']}
with zipfile.ZipFile(dest,'a',compression=zipfile.ZIP_DEFLATED,compresslevel=8) as z:
 z.writestr('RESEARCH_SA09/ARCHIVE_VALIDATION.json',json.dumps(validation,indent=2)+'\n')
with zipfile.ZipFile(dest) as z: assert z.testzip() is None
result={'archive':str(dest),'bytes':dest.stat().st_size,'sha256':sha(dest.read_bytes()),
 'file_count':len(payload)+1,'crc_test':'passed','runtime_seconds':round(time.perf_counter()-start,6),
 'completed_before_first_checkpoint_due':manifest['completed_before_first_checkpoint_due']}
(ROOT.parent/(dest.stem+'_archive_log.json')).write_text(json.dumps(result,indent=2))
print(json.dumps(result))
