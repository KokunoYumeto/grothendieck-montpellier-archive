#!/usr/bin/env python3
"""Archive all authored work; omit source copies and downloaded publications.

The wall-clock timestamp is supplied from clock.curr_time rather than the
executor's differently configured clock. This script never schedules itself.
"""
import argparse, hashlib, json, re, zipfile
from pathlib import Path

p=argparse.ArgumentParser();p.add_argument('--number',type=int,required=True);p.add_argument('--utc',required=True)
a=p.parse_args();base=Path(__file__).resolve().parents[1];dest=base.parent/f'SA06_checkpoint_{a.number:02d}.zip'
if dest.exists(): raise SystemExit('Checkpoint names are immutable: destination already exists')
included=[];excluded=[];web=[];reads=[]
for f in sorted(base.rglob('*')):
 if not f.is_file(): continue
 r=f.relative_to(base); s=str(r)
 if '__pycache__' in r.parts or 'cache_sources' in r.parts or f.suffix in {'.pdf','.png','.jpg','.pyc'}:
  excluded.append(s);continue
 if f.suffix=='.json' and re.search(r'(web|search)[^/]*\.json$',s,re.I):
  obj=json.loads(f.read_text()); raw=json.dumps(obj,ensure_ascii=False)
  web.append({'audit_file':s,'request':obj.get('request',obj.get('query',obj.get('queries'))),'urls':sorted(set(re.findall(r'https?://[^\s"<>\\]+',raw))),'source_refs':sorted(set(re.findall(r'turn\d+(?:search|view|fetch)\d+',raw))),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
  excluded.append(s);continue
 if f.suffix in {'.txt','.out'} and (('research' in r.parts and not f.name.endswith('.out')) or ('audit' in r.parts and any(z in f.name for z in ('transcription','_tex_','_notes_','_doubts_','note_headings'))) or f.name.startswith('read_')):
  reads.append({'path':s,'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'recreate':'Read the corresponding supplied attachment with the included read_sources/read_source program; no manuscript scan was used.'})
  excluded.append(s);continue
 included.append(f)
manifest={'checkpoint':a.number,'created_utc':a.utc,'included_files':[str(f.relative_to(base)) for f in included], 'excluded_source_caches_and_duplicate_readouts':excluded,'original_attachments_required':['SA06_Thorie_des_motifs_part2.zip','PROMPT(20261119-130252).md'],'previous_checkpoints':[f'SA06_checkpoint_{n:02d}.zip' for n in range(1,a.number)],'resume':'All authored part files and all computation/authoring programs are present. Unpack the original supplied source archive separately under source/. Continue from the progress log; do not treat a checkpoint as the final six-stage dossier.'}
with zipfile.ZipFile(dest,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for f in included:z.write(f,'SA06_work/'+str(f.relative_to(base)))
 z.writestr('SA06_work/audit/checkpoint_manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
 z.writestr('SA06_work/audit/source_readout_manifest.json',json.dumps(reads,ensure_ascii=False,indent=2)+'\n')
 z.writestr('SA06_work/audit/web_query_locator_audit.json',json.dumps(web,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'path':str(dest),'files':len(included)+3,'bytes':dest.stat().st_size,'utc':a.utc}))
