#!/usr/bin/env python3
"""Check immutable archive integrity and every non-self manifest hash."""
from pathlib import Path
import hashlib,json,sys,zipfile,time
root=Path(__file__).resolve().parents[1]
n=int(sys.argv[1]); p=root.parent/f'RESEARCH_SA20_checkpoint_{n:02d}.zip'
start=time.perf_counter()
with zipfile.ZipFile(p) as z:
    assert z.testzip() is None
    manifest=json.loads(z.read('RESEARCH_SA20/notes/checkpoint_file_manifest.json'))
    for row in manifest:
        b=z.read('RESEARCH_SA20/'+row['path'])
        assert len(b)==row['bytes'],row['path']
        assert hashlib.sha256(b).hexdigest()==row['sha256'],row['path']
    names=z.namelist()
    assert len(names)==len(manifest)+1
result={'archive':p.name,'status':'PASS','files':len(names),'manifest_hashes_checked':len(manifest),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'runtime_seconds':time.perf_counter()-start}
(root/f'logs/checkpoint{n:02d}_integrity.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
