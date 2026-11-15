"""Create complete, losslessly deduplicated ZIPs with explicit image-path aliases."""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
import collections,csv,hashlib,json,shutil,tempfile
from contextlib import contextmanager
IMAGE_SUFFIXES={'.png','.jpg','.jpeg'}
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def files(root):return sorted(p for p in root.rglob('*') if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts)
def preference(relative):
 parts=relative.parts
 current={'final_PS_EN_diplomatic','final_PS_EN_corrected_apparatus','final_PS_EN_reading','final_PS_EN_master_annotated','final_PS_GUIDE'}
 return (0 if any(x in current for x in parts) else 1,len(parts),relative.as_posix())
def prepare(root):
 root=Path(root);groups=collections.defaultdict(list)
 for p in files(root):
  if p.suffix.lower() in IMAGE_SUFFIXES:groups[digest(p)].append(p)
 aliases=[]
 for sha,paths in groups.items():
  if len(paths)<2:continue
  paths.sort(key=lambda p:preference(p.relative_to(root)));retained=paths[0]
  for p in paths[1:]:aliases.append({'path':p.relative_to(root).as_posix(),'replacement':retained.relative_to(root).as_posix(),'bytes':p.stat().st_size,'sha256':sha,'reason':'Identical rendered-image bytes are stored once. The named replacement is the complete byte-identical file; restore_file_aliases.py recreates this path without inference or image modification.'})
 aliases.sort(key=lambda x:x['path']);aliaspath=root/'records/FILE_ALIASES.tsv'
 with aliaspath.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=['path','replacement','bytes','sha256','reason'],delimiter='\t');w.writeheader();w.writerows(aliases)
 amap={r['path']:r for r in aliases};manifest=root/'records/ARCHIVE_CONTENTS.tsv';rows=[]
 for p in files(root):
  if p==manifest:continue
  rel=p.relative_to(root).as_posix();alias=amap.get(rel)
  rows.append({'path':rel,'bytes':p.stat().st_size,'sha256':digest(p),'storage':'duplicate image alias' if alias else 'physical file','replacement':alias['replacement'] if alias else rel})
 with manifest.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=['path','bytes','sha256','storage','replacement'],delimiter='\t');w.writeheader();w.writerows(rows)
 return amap,rows
@contextmanager
def capture(root,excluded=None):
 """Capture stable bytes before constructing manifests or compressed members."""
 root=Path(root);excluded=set(excluded or [])
 with tempfile.TemporaryDirectory(prefix='ps_archive_snapshot_',dir=root.parent) as directory:
  snapshot=Path(directory)
  for p in files(root):
   relative=p.relative_to(root)
   if relative.as_posix() in excluded:continue
   if relative.as_posix() in {'records/FILE_ALIASES.tsv','records/ARCHIVE_CONTENTS.tsv'}:continue
   for attempt in range(20):
    before=p.stat();data=p.read_bytes();after=p.stat()
    if (before.st_size,before.st_mtime_ns)==(after.st_size,after.st_mtime_ns) and len(data)==after.st_size:break
   else:raise RuntimeError('File did not stabilize for archive capture: '+relative.as_posix())
   target=snapshot/relative;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
  yield snapshot
def write_captured_zip(root,destination,selected=None,prepared=None):
 root=Path(root);destination=Path(destination);amap,rows=prepared if prepared else prepare(root)
 chosen=files(root) if selected is None else sorted(selected)
 with ZipFile(destination,'x',ZIP_DEFLATED,compresslevel=6) as z:
  z.comment=b'Complete unique artifacts. Duplicate images are mapped in records/FILE_ALIASES.tsv; run scripts/restore_file_aliases.py after extraction.'
  for p in chosen:
   rel=p.relative_to(root).as_posix()
   if rel not in amap:z.write(p,rel)
 return {'logical_files':len(chosen),'physical_files':sum(p.relative_to(root).as_posix() not in amap for p in chosen),'duplicate_image_aliases':sum(p.relative_to(root).as_posix() in amap for p in chosen),'bytes':destination.stat().st_size,'sha256':digest(destination)}
def write_zip(root,destination,selected=None,prepared=None):
 if prepared is not None:raise ValueError('Use write_captured_zip only with a prepared immutable snapshot')
 root=Path(root);relative_selection=None if selected is None else [p.relative_to(root) for p in selected]
 with capture(root) as snapshot:
  prepared=prepare(snapshot)
  chosen=None if relative_selection is None else [snapshot/p for p in relative_selection]
  result=write_captured_zip(snapshot,destination,selected=chosen,prepared=prepared)
  for name in ['FILE_ALIASES.tsv','ARCHIVE_CONTENTS.tsv']:shutil.copyfile(snapshot/'records'/name,root/'records'/name)
  result['manifest_basis']='immutable captured file bytes'
  return result
