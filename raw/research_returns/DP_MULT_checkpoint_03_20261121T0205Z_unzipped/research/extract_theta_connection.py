from pathlib import Path
import sys,tarfile,json,hashlib
from datetime import datetime,timezone
sys.path.insert(0,str(Path('DP_MULT_work/research').resolve()))
from verify_author_archive import PartsReader
root=Path('DP_MULT_work/research/external_lean'); parts=Path('author_archive')
prefix='ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/TaylorDiscriminants/'
exact={prefix+'WickVanishing/'+f+'.lean' for f in ('CanonA','ExpConjConnectionIntegral','FirstDerivativeShiftIntegral','HarmonicValueIntegral','GaugeBilinearTermEqNegDoubleSum','GaugeTrans')}
records=[];started=datetime.now(timezone.utc).isoformat();entries=0;scanned=0
with tarfile.open(fileobj=PartsReader([parts/f'lean.tar.gz.part{i:02d}' for i in range(1,15)]),mode='r|gz') as ar:
 for m in ar:
  entries+=1
  if not m.isfile() or not m.name.startswith('lean/src/'+prefix) or not m.name.endswith('.lean'):continue
  p=m.name[len('lean/src/'):]; data=ar.extractfile(m).read(); txt=data.decode('utf-8');scanned+=1
  matches=[s for s in ('ConnectionIntegrality','AdmissibilitySecond','CanonGaugeSt','const_hL') if s in txt]
  if p not in exact and not matches:continue
  dest=root/p;old=dest.read_bytes() if dest.exists() else None
  dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
  records.append({'path':p,'author_archive_member':m.name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'previously_present':old is not None,'previous_byte_equal':old==data if old is not None else None,'matches':matches,'reading_scope':'recovered for targeted tracing; not yet read'})
out={'started_utc':started,'completed_utc':datetime.now(timezone.utc).isoformat(),'archive_entries_streamed':entries,'archive_url_pattern':'https://alpo.ge/lean.tar.gz.partNN','matched_files':records,'scanned_count':scanned,'agent':'/root/step2_higher','model':'GPT-6 Astra Pro','effort':'not exposed'}
Path('DP_MULT_work/research/theta_normalization_added_sources_connection.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'matched':len(records),'scanned':scanned,'files':[{'path':r['path'],'matches':r['matches']} for r in records]},indent=2))
