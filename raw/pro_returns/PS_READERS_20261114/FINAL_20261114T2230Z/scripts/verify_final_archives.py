"""Verify the two delivery ZIPs against their complete logical-file manifest."""
from pathlib import Path
import argparse,csv,hashlib,io,json,subprocess,tempfile,zipfile

PUBLISHED_PDFS={
 'readers/PS_EN_diplomatic.pdf',
 'readers/PS_EN_corrected_apparatus.pdf',
 'readers/PS_EN_reading.pdf',
 'readers/PS_EN_master_annotated.pdf',
 'readers/PS_GUIDE.pdf',
}

def digest(data):
 return hashlib.sha256(data).hexdigest()

def verify(archives,restore=False,final_gate=False):
 restore=restore or final_gate
 members={};opened=[];receipts=[]
 try:
  for path in map(Path,archives):
   z=zipfile.ZipFile(path);opened.append(z)
   assert z.testzip() is None,path.name
   for info in z.infolist():
    name=info.filename;p=Path(name)
    assert not p.is_absolute() and '..' not in p.parts and not info.is_dir(),name
    assert name not in members,'Duplicate physical path: '+name
    assert p.suffix!='.zip','Nested archive: '+name
    members[name]=(z,info)
   receipts.append({'archive':path.name,'bytes':path.stat().st_size,'sha256':digest(path.read_bytes()),'physical_files':len(z.infolist()),'zip_crc_check':'passed'})
  def read(name):
   z,info=members[name];return z.read(info)
  manifest=list(csv.DictReader(io.StringIO(read('records/ARCHIVE_CONTENTS.tsv').decode()),delimiter='\t'))
  aliases=list(csv.DictReader(io.StringIO(read('records/FILE_ALIASES.tsv').decode()),delimiter='\t'))
  manifest_paths=[r['path'] for r in manifest]
  alias_paths=[r['path'] for r in aliases]
  assert len(manifest_paths)==len(set(manifest_paths)),'Duplicate logical manifest path'
  assert len(alias_paths)==len(set(alias_paths)),'Duplicate image alias path'
  assert 'records/ARCHIVE_CONTENTS.tsv' not in manifest_paths,'The logical manifest must not recursively include itself'
  logical_aliases={r['path']:r for r in manifest if r['storage']=='duplicate image alias'}
  assert set(alias_paths)==set(logical_aliases),{
   'aliases_absent_from_manifest':sorted(set(alias_paths)-set(logical_aliases)),
   'manifest_aliases_absent_from_table':sorted(set(logical_aliases)-set(alias_paths))}
  amap={r['path']:r for r in aliases};expected={'records/ARCHIVE_CONTENTS.tsv'};checked=0
  for name,row in logical_aliases.items():
   assert all(amap[name][field]==row[field] for field in ['bytes','sha256','replacement']),\
    'Alias table and logical manifest disagree: '+name
  for row in manifest:
   name=row['path'];target=row['replacement'];p=Path(name)
   assert not p.is_absolute() and '..' not in p.parts,name
   if row['storage']=='physical file':
    assert target==name and name not in amap,name;expected.add(name)
   else:
    assert row['storage']=='duplicate image alias' and name not in members,name
    assert name in amap and amap[name]['replacement']==target and amap[name]['sha256']==row['sha256'],name
   data=read(target)
   assert len(data)==int(row['bytes']) and digest(data)==row['sha256'],name
   checked+=1
  assert set(members)==expected,{'missing':sorted(expected-set(members)),'unexpected':sorted(set(members)-expected)}
  restoration=None
  if restore:
   with tempfile.TemporaryDirectory(prefix='ps_delivery_restore_') as directory:
    root=Path(directory)
    for z in opened:z.extractall(root)
    process=subprocess.run(['python3','scripts/restore_file_aliases.py'],cwd=root,capture_output=True,text=True,check=True)
    restoration=json.loads(process.stdout)
    for row in manifest:
     data=(root/row['path']).read_bytes()
     assert len(data)==int(row['bytes']) and digest(data)==row['sha256'],row['path']
    logical_paths=set(manifest_paths)|{'records/ARCHIVE_CONTENTS.tsv'}
    restored_paths={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
    assert restored_paths==logical_paths,{
     'missing_restored_paths':sorted(logical_paths-restored_paths),
     'unexpected_restored_paths':sorted(restored_paths-logical_paths)}
    restoration['all_restored_file_hashes_match']=True
    restoration['restored_file_set_matches_manifest']=True
    if final_gate:
     published=sorted(p.relative_to(root).as_posix() for p in root.rglob('*.pdf'))
     assert set(published)==PUBLISHED_PDFS,published
     process=subprocess.run(['python3','scripts/final_qa_gate.py','--allow-omitted-historical-pdfs','--check-only'],cwd=root,capture_output=True,text=True)
     assert process.returncode==0,'Extracted final QA failed: '+process.stdout+process.stderr
     restoration['final_qa_gate']=json.loads(process.stdout)
     restoration['published_pdf_files']=published
  scope=('final publication: logical-file integrity, exact-byte restoration, the exact five published PDFs, and the extracted final QA gate'
         if final_gate else 'logical-file integrity and exact-byte restoration; publication policy was not checked'
         if restore else 'logical-file and physical-archive integrity; restoration and publication policy were not checked')
  return {'complete':True,'verification_scope':scope,'final_publication_validated':bool(final_gate),'restoration_tested':bool(restore),'archives':receipts,'logical_files_including_manifest':checked+1,'physical_files':len(members),'duplicate_image_aliases':len(aliases),'manifest_self_hash':'The manifest is included as a physical ZIP member; its integrity is covered by ZIP CRC and the external archive SHA-256. It does not recursively hash itself.','restoration':restoration}
 finally:
  for z in opened:z.close()

def main():
 parser=argparse.ArgumentParser();parser.add_argument('archives',nargs='+');parser.add_argument('--restore',action='store_true');parser.add_argument('--final-gate',action='store_true');args=parser.parse_args()
 print(json.dumps(verify(args.archives,args.restore,args.final_gate),indent=2))

if __name__=='__main__':main()
