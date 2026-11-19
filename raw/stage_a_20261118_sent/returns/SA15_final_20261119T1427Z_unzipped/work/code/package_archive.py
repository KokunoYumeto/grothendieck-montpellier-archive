"""Package current work; omit supplied inputs and copyrighted reference copies.
Run with a new checkpoint name only at the prescribed45-minute boundary.
The final artifact uses the same documentation exclusion policy.
"""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,re,zipfile
BASE=Path(__file__).resolve().parents[2]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def excluded_reference(p):
 n=p.name.lower()
 if p.suffix.lower() in {'.pdf','.png','.jpg','.jpeg'}:return True
 # These four P894 files were deliberately reduced to request/result metadata;
 # they contain the exact search history, not third-party excerpts.
 if n.startswith('search_sessions_'):return False
 if p.suffix=='.json' and re.match(r'(web_|search_|open_|find_|screenshots_|p56_search_|p56_open_|sga_search)',n):return True
 if p.suffix in {'.json','.jsonl','.txt'}:
  try:
   if '[wordlim ' in p.read_text():return True
  except UnicodeError:pass
 if p.suffix=='.txt' and re.match(r'(hartshorne\d|katzmessing\d|lenstra_oort\d|breuil\d|fontaine\d|raynaud\d|sga[147]_)',n):return True
 return False
def main():
 ap=argparse.ArgumentParser();ap.add_argument('name');ap.add_argument('--final',action='store_true');a=ap.parse_args()
 target=BASE/a.name
 if target.exists():raise SystemExit('Refusing to overwrite an archive')
 records=[];paths=[]
 for root in [BASE/'work',BASE/'deliverables']:
  if not root.exists():continue
  for p in sorted(root.rglob('*')):
   if not p.is_file() or '__pycache__' in p.parts or p.suffix in {'.pyc','.zip'}:continue
   rel=p.relative_to(BASE)
   if 'archive_metadata' in p.parts:continue
   omit=excluded_reference(p)
   rec={'path':str(rel),'bytes':p.stat().st_size,'sha256':sha(p),'included':not omit}
   if omit:
    rec['reason']='Reference full text/tool excerpt or scan omitted from redistribution; URLs and our paraphrased findings are in the research/reference ledgers.'
    if p.suffix=='.json':
     try:
      text=p.read_text();rec['urls']=sorted(set(re.findall(r'https?://[^\s"<>\\]+',text)))[:150]
     except UnicodeError:pass
   else:paths.append(p)
   records.append(rec)
 meta=BASE/'work/archive_metadata';meta.mkdir(exist_ok=True)
 stamp=datetime.now(timezone.utc).isoformat()
 manifest={'archive':a.name,'created_utc':stamp,'previous_checkpoints':[p.name for p in sorted(BASE.glob('SA15_checkpoint_*.zip'))],'attachments_excluded':['upload/SA15_Cristaux.zip','upload/PROMPT(20261119-130151).md','sources/'],'files':records}
 mp=meta/(target.stem+'_manifest.json');mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
 with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for p in paths:
   rel=p.relative_to(BASE)
   # Final top-level documents are directly accessible. Work remains under work/.
   name=str(p.relative_to(BASE/'deliverables')) if rel.parts[0]=='deliverables' else str(rel)
   z.write(p,name)
  z.write(mp,'archive_manifest.json')
  z.writestr('packaging_result.json',json.dumps({'archive':a.name,
    'created_utc':stamp,'included_document_files':len(paths),
    'excluded_reference_copies':sum(not r['included'] for r in records),
    'attachments_included':False,'earlier_checkpoint_archives_included':False,
    'note':'The external archive byte count and SHA256 are necessarily computed after this ZIP is closed.'},ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'file':str(target),'bytes':target.stat().st_size,'sha256':sha(target),'included_files':len(paths)+2,'excluded_reference_copies':sum(not r['included'] for r in records),'created_utc':stamp}))
if __name__=='__main__':main()
