"""Verify immutable CP29 membership, every member hash/CRC, and the certified PDF."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,zipfile,time
root=Path(__file__).resolve().parents[1]
archive=root.parent/'RESEARCH_SA12_checkpoint_29.zip'
start=time.perf_counter(); assert archive.stat().st_size<500_000_000
prefix='RESEARCH_SA12/'
with zipfile.ZipFile(archive) as z:
    names=z.namelist(); assert len(names)==len(set(names))
    assert not any(name.endswith('.zip') for name in names)
    manifest=json.loads(z.read(prefix+'CHECKPOINT_MANIFEST.json'))
    assert manifest['checkpoint']==29
    assert set(names)=={prefix+'CHECKPOINT_MANIFEST.json'}|{prefix+f['path'] for f in manifest['files']}
    for entry in manifest['files']:
        data=z.read(prefix+entry['path'])
        assert len(data)==entry['bytes']
        assert hashlib.sha256(data).hexdigest()==entry['sha256'],entry['path']
    qa=json.loads(z.read(prefix+'qa/pdf_verified.json'))
    digest=hashlib.sha256(z.read(prefix+'RESEARCH_SA12_paper.pdf')).hexdigest()
    assert digest==qa['sha256']
    assert hashlib.sha256(z.read(prefix+'build/RESEARCH_SA12_paper.pdf')).hexdigest()==digest
record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),checkpoint=29,archive=str(archive),
 archive_created_utc=manifest['utc'],archive_bytes=archive.stat().st_size,
 archive_sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),members=len(names),
 full_crc='PASS',manifest_membership='PASS',all_manifest_hashes='PASS',
 verified_pdf_sha256=digest,verified_pdf_build=qa['build'],pdf_pages=qa['pages'],
 prior_zip_members=0,seconds=time.perf_counter()-start)
out=root/'code/output/checkpoint29_archive_verification.json'; assert not out.exists()
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
