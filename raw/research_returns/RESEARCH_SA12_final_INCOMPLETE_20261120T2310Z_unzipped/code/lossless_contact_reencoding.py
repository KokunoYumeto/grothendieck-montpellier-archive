"""Retain historical contact-sheet pixels in lossless WebP to respect the ZIP cap.

Only generated QA contact sheets are re-encoded. No source PDF, manuscript,
individual rendered page, supplied attachment, or earlier ZIP is changed.
Each historical PNG path remains resolvable through the full provenance map.
The source PNG is removed only after exact RGB verification and a durable
per-file record; its original bytes also remain in checkpoint20.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from PIL import Image
import hashlib, json, time

root = Path(__file__).resolve().parents[1]
qa = root / 'qa'
record_path = qa / 'historical_contact_encoding_map.json'
started = time.perf_counter()
record = json.loads(record_path.read_text()) if record_path.exists() else {
    'started_utc': datetime.now(timezone.utc).isoformat(),
    'purpose': 'Preserve all historical inspection pixels while keeping full archives under500MB.',
    'format': 'lossless WebP; exact decoded RGB equality required',
    'original_byte_source': 'Immutable RESEARCH_SA12_checkpoint_20.zip',
    'files': [],
}
seen = {entry['original_path']: entry for entry in record['files']}

def convert(path):
    original = path.read_bytes()
    dest = path.with_suffix('.webp')
    with Image.open(path) as im:
        im.load()
        assert im.mode == 'RGB', (path, im.mode)
        rgb = im.tobytes()
        size = im.size
        kwargs = {key: im.info[key] for key in ('icc_profile', 'exif', 'xmp') if key in im.info}
        if dest.exists():
            with Image.open(dest) as check:
                assert check.convert('RGB').tobytes() == rgb and check.size == size
        else:
            temp = dest.with_suffix('.webp.tmp')
            im.save(temp, format='WEBP', lossless=True, quality=100, method=4, exact=True, **kwargs)
            with Image.open(temp) as check:
                assert check.convert('RGB').tobytes() == rgb and check.size == size
            temp.replace(dest)
    encoded = dest.read_bytes()
    assert len(encoded) < len(original), path
    return path, {
        'utc': datetime.now(timezone.utc).isoformat(),
        'original_path': str(path.relative_to(root)),
        'current_path': str(dest.relative_to(root)),
        'original_bytes': len(original),
        'current_bytes': len(encoded),
        'original_sha256': hashlib.sha256(original).hexdigest(),
        'current_sha256': hashlib.sha256(encoded).hexdigest(),
        'rgb_sha256': hashlib.sha256(rgb).hexdigest(),
        'width': size[0], 'height': size[1], 'mode': 'RGB',
        'exact_decoded_pixel_equality': True,
        'color_metadata_preserved': sorted(kwargs),
    }

paths = sorted(qa.glob('*contact*.png'))
pending = []
for path in paths:
    rel = str(path.relative_to(root))
    if rel in seen:
        entry = seen[rel]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == entry['original_sha256']
        assert hashlib.sha256((root / entry['current_path']).read_bytes()).hexdigest() == entry['current_sha256']
        path.unlink()
    else:
        pending.append(path)

with ThreadPoolExecutor(max_workers=4) as pool:
    for future in as_completed([pool.submit(convert, path) for path in pending]):
        path, entry = future.result()
        record['files'].append(entry)
        record_path.write_text(json.dumps(record, indent=2) + '\n')
        path.unlink()

record['completed_utc'] = datetime.now(timezone.utc).isoformat()
record['count'] = len(record['files'])
record['original_bytes'] = sum(x['original_bytes'] for x in record['files'])
record['current_bytes'] = sum(x['current_bytes'] for x in record['files'])
record['bytes_saved'] = record['original_bytes'] - record['current_bytes']
record['seconds'] = time.perf_counter() - started
record_path.write_text(json.dumps(record, indent=2) + '\n')
(qa / 'HISTORICAL_IMAGE_PATHS.md').write_text(
    '# Historical inspection images\n\n'
    'INCOMPLETE. Every historical contact sheet remains available with identical '
    'decoded RGB pixels in lossless WebP. The complete old-to-current path map, '
    'original and current hashes, dimensions, pixel hashes and exact equality '
    'checks are in historical_contact_encoding_map.json. Existing inspection '
    'records preserve their original observed filenames and timestamps; resolve '
    'those paths through this map. Earlier immutable checkpoint ZIPs retain the '
    'original PNG bytes. No earlier ZIP, source document or individual rendered '
    'page was modified. This lossless encoding change adds no new image-inspection '
    'claim and no research movement.\n'
)
print(json.dumps({key: record[key] for key in ('completed_utc', 'count', 'original_bytes', 'current_bytes', 'bytes_saved', 'seconds')}, indent=2))
