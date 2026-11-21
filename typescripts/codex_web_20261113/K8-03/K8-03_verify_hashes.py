"""Reconstruct the pre-witness text using only marked spans and verify both hash lists."""
import csv
import hashlib
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def digest(data):
    return hashlib.sha256(data).hexdigest()

def run():
    log = (ROOT / 'progress.log').read_text(encoding='utf-8')
    stages = log.split('transcription frozen ', 1)
    assert len(stages) == 2 and 'witness check done ' in stages[1]
    expected = []
    for stage in (stages[0], stages[1].split('witness check done ', 1)[0]):
        pairs = re.findall(r'^SHA-256 ([0-9a-f]{64})  (.+)$', stage, re.MULTILINE)
        assert len(pairs) == 16
        expected.append({path: value for value,path in pairs})
    sites = defaultdict(list)
    with (ROOT / 'K8-03_witness.tsv').open(encoding='utf-8') as handle:
        for row in csv.DictReader(handle, delimiter='\t'):
            sites[int(row['scan'])].append(row)
    assert sum(map(len, sites.values())) == 130
    frozen_files, final_files = {}, {}
    for path in sorted((ROOT / 'pages').glob('*.tex')):
        scan = int(path.stem[-3:])
        data = path.read_bytes()
        final = data.decode('utf-8')
        restored = final
        next_at = len(final)
        for row in reversed(sites[scan]):
            a, b = int(row['final_start']), int(row['final_end'])
            assert 0 <= a <= b <= next_at and final[a:b] == row['final']
            assert row['frozen'].startswith((r'\unsure{', r'\illegible{'))
            restored = restored[:a] + row['frozen'] + restored[b:]
            next_at = a
        for row in sites[scan]:
            a, b = int(row['frozen_start']), int(row['frozen_end'])
            assert restored[a:b] == row['frozen']
        name = str(path.relative_to(ROOT))
        frozen_files[name] = restored.encode('utf-8')
        final_files[name] = data
    master = 'K8-03_transcription.tex'
    for files, checks in zip((frozen_files, final_files), expected):
        files[master] = b''.join(files.values())
        assert {n:digest(data) for n,data in files.items()} == checks
    assert (ROOT / master).read_bytes() == final_files[master]
    print('Verified 16 frozen hashes and 16 final hashes. All differences lie within previously marked spans.')

if __name__ == '__main__':
    run()
