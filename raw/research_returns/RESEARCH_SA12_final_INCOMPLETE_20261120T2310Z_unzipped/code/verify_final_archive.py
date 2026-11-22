"""Verify every final ZIP member, checksum and the actual stopping record."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import time
import zipfile

root = Path(__file__).resolve().parents[1]
archive = root.parent / 'RESEARCH_SA12_final_INCOMPLETE.zip'
assert archive.stat().st_size < 500_000_000
start = time.perf_counter()
prefix = root.name + '/'
with zipfile.ZipFile(archive) as z:
    names = z.namelist()
    assert len(names) == len(set(names))
    assert not any(name.endswith('.zip') for name in names)
    manifest = json.loads(z.read(prefix + 'CHECKPOINT_MANIFEST.json'))
    assert manifest['kind'] == 'separate_final_after_stopping_rule'
    assert manifest['checkpoint'] == 'final'
    assert set(names) == {prefix + 'CHECKPOINT_MANIFEST.json'} | {prefix + x['path'] for x in manifest['files']}
    for entry in manifest['files']:
        data = z.read(prefix + entry['path'])
        assert len(data) == entry['bytes']
        assert hashlib.sha256(data).hexdigest() == entry['sha256'], entry['path']
    qa = json.loads(z.read(prefix + 'qa/pdf_verified.json'))
    digest = hashlib.sha256(z.read(prefix + 'RESEARCH_SA12_paper.pdf')).hexdigest()
    assert digest == qa['sha256']
    assert hashlib.sha256(z.read(prefix + 'build/RESEARCH_SA12_paper.pdf')).hexdigest() == digest
    review = json.loads(z.read(prefix + f'code/output/formal_review{manifest["stopping_review"]}.json'))
    assert review['stopping_condition_met'] and review['consecutive_no_movement_reviews'] >= 2
    assert not review['movement']
    assert json.loads(z.read(prefix + 'code/output/research_stopped.json'))['all_research_agents_stopped']
record = dict(recorded_utc=datetime.now(timezone.utc).isoformat(), kind='verified_final_archive',
              archive=str(archive), archive_created_utc=manifest['utc'], archive_bytes=archive.stat().st_size,
              archive_sha256=hashlib.sha256(archive.read_bytes()).hexdigest(), members=len(names),
              full_crc='PASS', manifest_membership='PASS', all_manifest_hashes='PASS',
              verified_pdf_sha256=digest, verified_pdf_build=qa['build'], pdf_pages=qa['pages'],
              stopping_review=manifest['stopping_review'], stopping_condition='PASS',
              prior_zip_members=0, seconds=time.perf_counter() - start)
out = root / 'code/output/final_archive_verification.json'
assert not out.exists()
out.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
