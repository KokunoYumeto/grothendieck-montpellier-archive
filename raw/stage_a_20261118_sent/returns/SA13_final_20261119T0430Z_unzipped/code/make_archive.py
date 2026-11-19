"""Create immutable timed checkpoints or the single final deliverable; omit external copyrighted source bodies."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,zipfile,json,hashlib
root=Path(__file__).resolve().parents[2]
p=argparse.ArgumentParser();p.add_argument('--kind',choices=['checkpoint','final'],required=True);p.add_argument('--number');p.add_argument('--utc',required=True);a=p.parse_args()
folder=root/'archives';folder.mkdir(exist_ok=True)
name=f'SA13_checkpoint_{a.number}.zip' if a.kind=='checkpoint' else 'SA13.zip'
dest=folder/name
if dest.exists():raise SystemExit('Refusing to overwrite an existing archive')
selected=[];excluded=[]
for f in sorted((root/'deliverable').rglob('*')):
 if not f.is_file():continue
 rel=f.relative_to(root/'deliverable')
 # External source documents/OCR and raw web responses stay in private research scratch.
 if f.name.startswith('web_') or f.suffix.lower() in ['.pdf','.png','.jpg'] or ('outputs' in rel.parts and ('sga7_' in f.name or 'ocr_' in f.name) and f.name not in ['ocr_codex_sources.txt','ocr_sga_run1.txt']) or '__pycache__' in rel.parts:
  excluded.append(str(rel));continue
 selected.append((f,str(rel)))
if a.kind=='checkpoint':
 for f in sorted((root/'work').rglob('*')):
  if f.is_file() and (f.name in ['pages.json','entries.json','REVIEW_PROTOCOL.md','ROOT_CODEX_REVIEW.md']):selected.append((f,'resume/'+str(f.relative_to(root/'work'))))
manifest={'kind':a.kind,'created_utc':a.utc,'archive':name,'prior_checkpoints':[f.name for f in sorted(folder.glob('SA13_checkpoint_*.zip'))], 'files':[{'path':n,'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f,n in selected], 'excluded_external_source_or_temporary_outputs':excluded,'attachments_included':False,'resume':'Restore this tree; re-extract original attached ZIPs as sources/notes and sources/texts. code/inventory.py and code/read_sources.py document indexing. Checkpoints do not certify completion.' if a.kind=='checkpoint' else 'Final consolidated dossier.'}
with zipfile.ZipFile(dest,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for f,n in selected:z.write(f,n)
 z.writestr('ARCHIVE_MANIFEST.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'path':str(dest),'bytes':dest.stat().st_size,'files':len(selected),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'created_utc':a.utc},indent=2))
