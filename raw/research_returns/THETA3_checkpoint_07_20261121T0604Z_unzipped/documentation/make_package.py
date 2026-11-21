"""Create a research package; never include earlier checkpoint archives.
Published external inputs are cited with URLs, pinned paths and byte hashes.
Generated research records, proofs and computation code are preserved in full.
"""
from pathlib import Path
import zipfile,json,datetime,hashlib,csv,sys
root=Path(__file__).resolve().parent.parent
state=json.loads((root/'work/run_state.json').read_text())
mode=sys.argv[1]
now=datetime.datetime.now(datetime.timezone.utc)
if mode=='checkpoint':
 due=datetime.datetime.fromisoformat(state['next_checkpoint_utc'].replace('Z','+00:00'))
 if now<due:
  print(json.dumps({'status':'not_due','now':now.isoformat(),'due':due.isoformat()}));sys.exit(0)
 number=state['checkpoint_number']+1
 name=f'THETA3_checkpoint_{number:02d}.zip'
else:name='THETA3_final.zip'
path=root/name
if path.exists():raise SystemExit('Refusing to overwrite existing package: '+name)
snapshot_state=dict(state)
if mode=='checkpoint':
 snapshot_state['checkpoint_number']=number
 snapshot_state['last_checkpoint_path']=str(path)
 snapshot_state['last_checkpoint_created_utc']=now.isoformat()
 snapshot_state['next_checkpoint_utc']=(due+datetime.timedelta(minutes=45)).isoformat().replace('+00:00','Z')
entries=[]
for p in sorted((root/'deliverables').rglob('*')):
 if p.is_file() and p.suffix not in {'.aux','.log','.out','.toc'}:entries.append((p,str(p.relative_to(root/'deliverables'))))
for p in sorted((root/'work').rglob('*')):
 if not p.is_file():continue
 rel=p.relative_to(root/'work')
 if rel.parts[0] in {'archive_images','library_helper','library_private','paper_build'}:continue
 if rel.parts[0]=='external' and p.suffix not in {'.json','.md','.tsv'}:continue
 if rel.parts[0]=='alpoge_mirror' and p.suffix=='.lean':continue
 if p.suffix in {'.md','.tsv','.py','.tex','.json'} or (p.suffix=='.txt' and rel.parts[0] not in {'texqa','texruntime','theta_A_qa'}):
  entries.append((p,'documentation/'+str(rel)))
for p in sorted((root/'sources').rglob('*')):
 if p.is_file():entries.append((p,'supplied_sources/'+str(p.relative_to(root/'sources'))))
manifest=[]
with zipfile.ZipFile(path,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p,name_in_zip in entries:
  data=(json.dumps(snapshot_state,indent=2)+'\n').encode() if p==root/'work/run_state.json' else p.read_bytes()
  z.writestr(name_in_zip,data)
  manifest.append((name_in_zip,len(data),hashlib.sha256(data).hexdigest()))
 z.writestr('PACKAGE_MANIFEST.tsv','path\tbytes\tsha256\n'+''.join(f'{a}\t{b}\t{c}\n' for a,b,c in manifest))
 z.writestr('PACKAGE_STATUS.md',f'# {mode.title()} package\n\nCreated {now.isoformat()}.\n\nThis package preserves all generated deliverables, proof records, check events and computation code available at this point, together with the supplied sources. Original external publications are identified by retrieval records and exact byte hashes rather than republished wholesale. The mirrored Lean module paths and hashes allow recovery from the pinned public commit. Earlier checkpoint ZIPs are never nested.\n')
with zipfile.ZipFile(path) as z:
 bad=z.testzip()
 if bad:raise SystemExit('ZIP verification failed: '+bad)
 if any('checkpoint_' in x and x.endswith('.zip') for x in z.namelist()):raise SystemExit('Nested checkpoint detected')
if mode=='checkpoint':
 (root/'work/run_state.json').write_text(json.dumps(snapshot_state,indent=2)+'\n')
print(json.dumps({'status':'created','path':str(path),'bytes':path.stat().st_size,'members':len(entries)+2,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}))
