"""Verify ZIP integrity and every included file's manifest hash."""
from pathlib import Path
import datetime, hashlib, json, sys, zipfile
w=Path(__file__).resolve().parents[1]
n=int(sys.argv[1]); archive=w.parent/f'RESEARCH_SA15_checkpoint_{n:02d}.zip'
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    manifest=json.loads(z.read(f'notes/checkpoint_{n:02d}_manifest.json'))
    count=0
    for row in manifest['files']:
        if row['included']:
            data=z.read(row['path'])
            assert len(data)==row['size'],row['path']
            assert hashlib.sha256(data).hexdigest()==row['sha256'],row['path']
            count+=1
    assert len(z.namelist())==count+1
out=dict(checkpoint=n,checked_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
         archive=str(archive),included_manifest_hashes=count,zip_crc='PASS',
         bytes=archive.stat().st_size,sha256=hashlib.sha256(archive.read_bytes()).hexdigest())
(w/'outputs'/f'checkpoint_{n:02d}_archive_verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
