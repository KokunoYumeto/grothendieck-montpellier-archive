"""Record one confirmed save result; never uploads, retries, searches or guesses."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys

root = Path(__file__).resolve().parents[1]
token = sys.argv[1]
assert len(sys.argv) == 2
if token == 'final':
    prefix = 'final'
    archive = root.parent / 'RESEARCH_SA12_final_INCOMPLETE.zip'
else:
    number = int(token)
    assert number >= 30
    prefix = f'checkpoint{number}'
    archive = root.parent / f'RESEARCH_SA12_checkpoint_{number:02d}.zip'
result = json.loads((root / f'code/output/{prefix}_library_upload_result.json').read_text())
assert list(result) == ['results'] and len(result['results']) == 1
saved = result['results'][0]
assert saved['local_path'] == str(archive)
assert saved['purpose'] == 'create_library_file'
assert saved['status'] == 'succeeded', 'Save is not confirmed; do not retry or infer success.'
assert saved['library_file_id'] and saved['file_name'] == archive.name
verified = json.loads((root / f'code/output/{prefix}_archive_verification.json').read_text())
assert verified['full_crc'] == verified['all_manifest_hashes'] == 'PASS'
assert archive.stat().st_size == verified['archive_bytes']
assert hashlib.sha256(archive.read_bytes()).hexdigest() == verified['archive_sha256']
receipt = dict(recorded_utc=datetime.now(timezone.utc).isoformat(),
               checkpoint='final' if token == 'final' else number,
               archive_verification=verified, saved_result=saved,
               user_delivery='native Library ZIP link', original_archive_immutable=True)
out = root / f'code/output/{prefix}_saved_receipt.json'
assert not out.exists()
out.write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps({'status': saved['status'], 'file_name': saved['file_name'],
                  'library_file_id': saved['library_file_id'], 'archive_bytes': verified['archive_bytes'],
                  'archive_sha256': verified['archive_sha256']}))
