#!/usr/bin/env python3
"""Compare selected source modules with the author's split tar.gz, without full extraction.

This checks byte identity only. It does not run Lean or certify mathematics.
The 14 original parts are https://alpo.ge/lean.tar.gz.part01 through part14.
"""
from pathlib import Path
import argparse
import hashlib
import json
import tarfile
from datetime import datetime, timezone

class PartsReader:
    def __init__(self, paths):
        self.paths = iter(paths)
        self.current = None

    def read(self, size):
        blocks = []
        left = size
        while left:
            if self.current is None:
                try:
                    self.current = next(self.paths).open('rb')
                except StopIteration:
                    break
            data = self.current.read(left)
            if data:
                blocks.append(data)
                left -= len(data)
            else:
                self.current.close()
                self.current = None
        return b''.join(blocks)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--parts-dir', type=Path, required=True)
    parser.add_argument('--sources-dir', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    parts = [args.parts_dir / f'lean.tar.gz.part{i:02d}' for i in range(1, 15)]
    wanted = {p.relative_to(args.sources_dir).as_posix(): p for p in args.sources_dir.rglob('*.lean')}
    records = []
    count = 0
    started = datetime.now(timezone.utc).isoformat()
    with tarfile.open(fileobj=PartsReader(parts), mode='r|gz') as archive:
        for member in archive:
            count += 1
            if not member.isfile():
                continue
            pieces = member.name.removeprefix('./').split('/')
            target = next(('/'.join(pieces[i:]) for i in range(min(3, len(pieces)))
                           if '/'.join(pieces[i:]) in wanted), None)
            if target is None:
                continue
            data = archive.extractfile(member).read()
            actual = hashlib.sha256(data).hexdigest()
            recovered = hashlib.sha256(wanted[target].read_bytes()).hexdigest()
            records.append({'path': target, 'author_archive_member': member.name,
                            'bytes': len(data), 'author_sha256': actual,
                            'mirror_sha256': recovered, 'byte_equal': actual == recovered})
    missing = sorted(set(wanted) - {r['path'] for r in records})
    result = {'started_utc': started, 'completed_utc': datetime.now(timezone.utc).isoformat(),
              'archive_url_pattern': 'https://alpo.ge/lean.tar.gz.partNN',
              'parts': 14, 'compressed_bytes': sum(p.stat().st_size for p in parts),
              'archive_entries_streamed': count, 'targeted_files_at_start': len(wanted),
              'matched_files': records, 'unmatched_targets': missing}
    args.output.write_text(json.dumps(result, indent=2))
    print(f'{len(records)} matched modules; {sum(r["byte_equal"] for r in records)} byte-identical; '
          f'{len(missing)} unmatched; {count} archive entries streamed.')
    if missing or any(not r['byte_equal'] for r in records):
        raise SystemExit(1)

if __name__ == '__main__':
    main()
