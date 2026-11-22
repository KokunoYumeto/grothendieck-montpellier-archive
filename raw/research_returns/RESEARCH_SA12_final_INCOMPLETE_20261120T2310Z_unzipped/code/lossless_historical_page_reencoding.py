"""Preserve historical rendered-page pixels using lossless WebP.

Only checkpoint01--17 generated individual PNG pages are converted. Their
original bytes remain in immutable checkpoint23. No source or archive changes.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from PIL import Image
import hashlib, json, re, time, zipfile

root = Path(__file__).resolve().parents[1]
qa = root / 'qa'
record_path = qa / 'historical_page_encoding_map.json'
started = time.perf_counter()
with zipfile.ZipFile(root.parent / 'RESEARCH_SA12_checkpoint_23.zip') as archive:
    old = json.loads(archive.read('RESEARCH_SA12/CHECKPOINT_MANIFEST.json'))
old_hash = {x['path']: x['sha256'] for x in old['files']}
record = json.loads(record_path.read_text()) if record_path.exists() else {
    'started_utc': datetime.now(timezone.utc).isoformat(),
    'purpose': 'Retain every historical inspected pixel while respecting the full-archive500MB cap.',
    'format': 'lossless WebP; exact decoded RGB equality',
    'original_byte_source': 'Immutable RESEARCH_SA12_checkpoint_23.zip',
    'files': []
}
seen = {x['original_path']: x for x in record['files']}

def save_record():
    tmp = record_path.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(record, indent=2) + '\n')
    tmp.replace(record_path)

def convert(path):
    original = path.read_bytes()
    rel = str(path.relative_to(root))
    digest = hashlib.sha256(original).hexdigest()
    assert old_hash.get(rel) == digest, rel
    dest = path.with_suffix('.webp')
    with Image.open(path) as im:
        im.load()
        assert im.mode == 'RGB', (path, im.mode)
        rgb, size = im.tobytes(), im.size
        metadata = {key: im.info[key] for key in ('icc_profile', 'exif', 'xmp') if key in im.info}
        if not dest.exists():
            tmp = dest.with_suffix('.webp.tmp')
            im.save(tmp, format='WEBP', lossless=True, quality=100, method=4, exact=True, **metadata)
            with Image.open(tmp) as check:
                assert check.size == size and check.convert('RGB').tobytes() == rgb
            tmp.replace(dest)
        with Image.open(dest) as check:
            assert check.size == size and check.convert('RGB').tobytes() == rgb
    encoded = dest.read_bytes()
    assert len(encoded) < len(original), rel
    return path, {
        'utc': datetime.now(timezone.utc).isoformat(),
        'original_path': rel, 'current_path': str(dest.relative_to(root)),
        'original_bytes': len(original), 'current_bytes': len(encoded),
        'original_sha256': digest, 'current_sha256': hashlib.sha256(encoded).hexdigest(),
        'rgb_sha256': hashlib.sha256(rgb).hexdigest(),
        'width': size[0], 'height': size[1], 'mode': 'RGB',
        'exact_decoded_pixel_equality': True, 'color_metadata_preserved': sorted(metadata)
    }

paths = [p for p in sorted(qa.glob('checkpoint??_page_*.png'))
         if 1 <= int(re.match(r'checkpoint(\d+)_', p.name)[1]) <= 17]
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
        save_record()
        path.unlink()

record.update(completed_utc=datetime.now(timezone.utc).isoformat(),
              count=len(record['files']),
              original_bytes=sum(x['original_bytes'] for x in record['files']),
              current_bytes=sum(x['current_bytes'] for x in record['files']),
              seconds=time.perf_counter() - started)
record['bytes_saved'] = record['original_bytes'] - record['current_bytes']
save_record()
with (qa / 'HISTORICAL_IMAGE_PATHS.md').open('a') as f:
    f.write('\n\n## Individual checkpoint pages\n\n'
            'The checkpoint01--17 individual page PNGs have also been losslessly '
            're-encoded as WebP, with every decoded RGB pixel and all dimensions '
            'verified equal. Resolve original page-image paths through '
            'historical_page_encoding_map.json, which retains original/current '
            'paths, hashes and sizes. Their original bytes remain in immutable '
            'checkpoint23. Earlier inspection records retain the actual filenames '
            'and timestamps observed at that time. No new image-inspection claim '
            'or mathematical progress is made by re-encoding.\n')
print(json.dumps({k: record[k] for k in ['completed_utc', 'count', 'original_bytes', 'current_bytes', 'bytes_saved', 'seconds']}, indent=2))
