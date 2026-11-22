"""Verify all bytes in an already-created immutable checkpoint."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,zipfile,json,hashlib
p=argparse.ArgumentParser();p.add_argument('number',type=int);a=p.parse_args()
r=Path(__file__).resolve().parents[1];zpath=r.parent/f'HODGE_DIVISION_checkpoint_{a.number:02d}.zip'
with zipfile.ZipFile(zpath) as z:
 assert z.testzip() is None
 names=z.namelist();assert not any(n.lower().endswith('.zip') for n in names)
 manifest=json.loads(z.read('HODGE_DIVISION/CHECKPOINT_MANIFEST.json'))
 assert manifest['checkpoint']==a.number
 expected={'HODGE_DIVISION/'+f['path'] for f in manifest['files']}|{'HODGE_DIVISION/CHECKPOINT_MANIFEST.json'}
 assert len(names)==len(set(names)) and set(names)==expected
 for row in manifest['files']:
  b=z.read('HODGE_DIVISION/'+row['path']);assert len(b)==row['bytes'];assert hashlib.sha256(b).hexdigest()==row['sha256'],row['path']
 for f in manifest['retained_external_mathematical_inputs']:assert 'HODGE_DIVISION/'+f in expected
out={'status':'PASS','verified_at_utc':datetime.now(timezone.utc).isoformat(),'snapshot_utc':manifest['snapshot_utc'],'checkpoint':a.number,'archive_entries':len(names),'manifest_files':len(manifest['files']),'retained_mathematical_inputs':len(manifest['retained_external_mathematical_inputs']),'bytes':zpath.stat().st_size,'sha256':hashlib.sha256(zpath.read_bytes()).hexdigest(),'scope':'All archived file bytes and SHA256 values match the manifest; no nested ZIP; every mathematical table input present.'}
(r/f'research/checkpoint{a.number:02d}_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
