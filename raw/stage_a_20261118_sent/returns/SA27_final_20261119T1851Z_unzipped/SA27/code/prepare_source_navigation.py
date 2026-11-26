"""Regenerate a scratch navigation input from the original supplied notes.

This parses entry boundaries only; it makes no textual or mathematical verdict.
The full extracted-source navigation is deliberately omitted from the ZIP.
"""
import argparse
import hashlib
import json
from pathlib import Path

R = Path(__file__).resolve().parents[1]
SOURCE = R.parent / 'source/SA27_notes/pro/MPL_118_notes.md'
TARGET = R / 'work/p118/entry_navigation.json'

parser = argparse.ArgumentParser()
parser.add_argument('--check', action='store_true', help='Compare without writing.')
args = parser.parse_args()
lines = SOURCE.read_text().splitlines(keepends=True)
starts = [n for n, line in enumerate(lines) if line.startswith('### ')]
records = []
for n, start in enumerate(starts):
    end = starts[n + 1] if n + 1 < len(starts) else len(lines)
    records.append({'n': n + 1, 'heading': lines[start][4:].strip(),
                    'text': ''.join(lines[start:end]), 'line': start + 1})
assert len(records) == 318
if args.check:
    assert records == json.loads(TARGET.read_text()), 'Navigation parser must preserve exact entry content.'
else:
    TARGET.write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'entries': len(records), 'mode': 'check only' if args.check else 'regenerated',
                  'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                  'verdicts_generated': 0, 'result': 'PASS'}, indent=2))
