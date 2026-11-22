"""Read-only raw-DEFLATE size bound; never creates a ZIP or archive object."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys
import zipfile
import zlib

def estimate(root):
    root = Path(root)
    records = []
    for p in (root / 'code/output').glob('checkpoint*_archive_verification.json'):
        a = json.loads(p.read_text())
        if a.get('full_crc') == a.get('all_manifest_hashes') == 'PASS':
            records.append((a['checkpoint'], a))
    number, previous = max(records)
    with zipfile.ZipFile(previous['archive']) as z:
        old = json.loads(z.read(root.name + '/CHECKPOINT_MANIFEST.json'))
        old_hashes = {x['path']: x['sha256'] for x in old['files']}
        old_sizes = {i.filename.removeprefix(root.name + '/'): i.compress_size for i in z.infolist()}
    total = raw = unchanged = changed = 0
    pdf = (root / 'build/RESEARCH_SA12_paper.pdf').read_bytes()
    for p in sorted(root.rglob('*')):
        if not p.is_file() or p.suffix == '.zip' or '__pycache__' in p.parts or p.name == 'CHECKPOINT_MANIFEST.json':
            continue
        rel = str(p.relative_to(root))
        data = pdf if rel == 'RESEARCH_SA12_paper.pdf' else p.read_bytes()
        raw += len(data)
        if old_hashes.get(rel) == hashlib.sha256(data).hexdigest():
            total += old_sizes[rel]
            unchanged += 1
        else:
            total += len(zlib.compress(data, 6, wbits=-15))
            changed += 1
        total += 96 + 2 * len((root.name + '/' + rel).encode('utf-8'))
    assert unchanged + changed < 65_000
    total += 750_000
    return dict(utc=datetime.now(timezone.utc).isoformat(), archive_created=False,
                unchanged_size_reference_checkpoint=number, conservative_bound_bytes=total,
                remaining_below_cap_bytes=500_000_000 - total, raw_bytes=raw,
                unchanged_files=unchanged, changed_or_new_files=changed,
                method='Raw-DEFLATE at level6; exact unchanged compressed sizes; 76-byte local/central fixed headers plus20-byte/member reserve and UTF8 names twice;750k for manifest, end records and following small logs. All members and counts below ZIP64 limits. No ZIP created.')

if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    result = estimate(root)
    assert result['conservative_bound_bytes'] < 500_000_000, result
    if len(sys.argv) == 2:
        out = root / sys.argv[1]
        assert not out.exists()
        out.write_text(json.dumps(result, indent=2) + '\n')
    else:
        assert len(sys.argv) == 1
    print(json.dumps(result, indent=2))
