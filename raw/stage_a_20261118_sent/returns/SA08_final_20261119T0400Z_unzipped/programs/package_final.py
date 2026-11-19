"""Build the one final deliverable, with authored work and reproducibility audit.
The original attachments, earlier archives and copyrighted source caches are not
redistributed. The final ZIP is created exclusively and is never overwritten.
"""
from pathlib import Path
import datetime,hashlib,json,re,zipfile
R=Path(__file__).resolve().parents[1];O=R/'outputs';DEST=R.parent/'SA08.zip'
validation=json.loads((O/'SA08_validation.json').read_text())
if validation['verdict']!='PASS':raise SystemExit('Final validation is not PASS')
if DEST.exists():raise SystemExit('Refusing to overwrite final SA08.zip')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def excluded(p):
 s=p.relative_to(R).as_posix()
 return (s.startswith(('sources/','work/numbered/','work/reference_pdfs/','research/','checkpoint_metadata/'))
  or '__pycache__' in s or '/references/' in s
  or p.suffix.lower() in ('.pdf','.png','.dvi','.zip','.pyc')
  or ('/logs/' in '/'+s and ('search' in p.name or 'web_' in p.name))
  or s.endswith(('_entries_source.json','_scan_index.json','embedded_source.json','embedded_read.txt','sga4_excerpt.txt','Garvin1998.txt','package_final_output.json')))
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (O/'progress.log').open('a') as f:
 f.write(now+'\tFINAL_ARCHIVE\tSA08.zip; all required records pass final structural/editorial validation.\n')
 f.write(now+'\tEND\tSix-stage dossier complete; final archive being assembled for persistent delivery.\n')
files={};skipped=[]
for p in sorted(R.rglob('*')):
 if not p.is_file():continue
 s=p.relative_to(R).as_posix()
 if excluded(p):
  skipped.append({'path':s,'bytes':p.stat().st_size,'sha256':sha(p)});continue
 name=p.relative_to(O).as_posix() if p.is_relative_to(O) else s
 if name in files:raise ValueError('Duplicate archive name '+name)
 files[name]=p
setup=R.parent/'SA08_setup_output.txt'
if setup.exists():files['logs/setup_original_output.txt']=setup
retrieval={}
for p in sorted(list((R/'research').rglob('*.json'))+list((R/'logs').glob('*search*.json'))):
 try:d=json.loads(p.read_text())
 except Exception:continue
 raw=json.dumps(d,ensure_ascii=False)
 request=d.get('request',d.get('args',d.get('query',d.get('queries')))) if isinstance(d,dict) else None
 retrieval[p.relative_to(R).as_posix()]={'request':request,'urls':sorted(set(re.findall(r'https?://[^\s<>"\\)]+',raw))),
  'source_refs':sorted(set(re.findall(r'turn\d+(?:search|view|fetch)\d+',raw))),
  'raw_sha256':sha(p),'note':'External source text bodies are not redistributed; authored search assessments and source locators are retained.'}
inputs=[]
for p in sorted((R.parent/'upload').glob('*')):
 if p.is_file():inputs.append({'filename':p.name,'bytes':p.stat().st_size,'sha256':sha(p)})
manifest={'created_utc':now,'archive':'SA08.zip','validation':validation,
 'members':[{'path':name,'bytes':p.stat().st_size,'sha256':sha(p)} for name,p in files.items()],
 'input_attachments_not_embedded':inputs,
 'earlier_checkpoints_not_embedded':[{'filename':p.name,'sha256':sha(p)} for p in sorted(R.parent.glob('SA08_checkpoint_*.zip'))],
 'excluded_source_cache_and_input_inventory':skipped,
 'restoration':'Extract this archive into a directory named SA08_work. Put original SA08_notes.zip and SA08_texts.zip in the adjacent upload directory. programs/setup.py restores inputs and numbered reading copies; final judgments are already retained under work/. The outputs folder will be recreated by the builders.'}
with zipfile.ZipFile(DEST,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for name,p in files.items():z.write(p,name)
 z.writestr('research/retrieval_audit.json',json.dumps(retrieval,ensure_ascii=False,indent=2)+'\n')
 z.writestr('FINAL_MANIFEST.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
with zipfile.ZipFile(DEST) as z:
 bad=z.testzip()
 if bad:raise SystemExit('ZIP CRC failure: '+bad)
 required=['SA08_dossier.md','SA08_entries.tsv','SA08_items.json','SA08_claims.json','SA08_problems.json','SA08_readings.tsv','SA08_links.tsv','SA08_directions.md','SA08_references.bib','CHECK_EVENTS.tsv','progress.log']
 missing=set(required)-set(z.namelist())
 if missing:raise SystemExit('Missing required archive files: '+str(missing))
 result={'archive':'SA08.zip','member_count':len(z.namelist())+1,'required_files':required,'crc':'PASS','created_utc':now,
         'note':'The packaging program output is included verbatim. A hash of the entire archive cannot be embedded in itself; FINAL_MANIFEST.json hashes the authored input members.'}
report=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
(R/'logs/package_final_output.json').write_text(report)
with zipfile.ZipFile(DEST,'a',zipfile.ZIP_DEFLATED,compresslevel=9) as z:z.writestr('logs/package_final_output.json',report)
with zipfile.ZipFile(DEST) as z:
 if z.testzip():raise SystemExit('Final ZIP CRC failure')
print(report,end='')
