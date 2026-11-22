#!/usr/bin/env python3
"""Append reviewed requested-source access records without altering any theorem."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import time

root = Path(__file__).resolve().parents[1]
start = time.perf_counter()
target = root / 'ROOT_references.bib'
old = target.read_text()
sources = ['notes/A567_Birman_access_entry.bib', 'notes/ROOT_Knudsen_Raynaud_access_entries.bib']
added = []
for name in sources:
    content = (root / name).read_text()
    keys = re.findall(r'@\w+\{([^,]+),', content)
    assert keys and all(('{' + key + ',') not in old for key in keys)
    old += '\n' + content.strip() + '\n'
    added.extend(keys)
before = hashlib.sha256(target.read_bytes()).hexdigest()
target.write_text(old)
record = {'actual_utc': datetime.now(timezone.utc).isoformat(),
          'sources': sources, 'added_keys': added,
          'before_sha256': before,
          'after_sha256': hashlib.sha256(target.read_bytes()).hexdigest(),
          'seconds': time.perf_counter() - start,
          'scope': 'Actual access and limited reading only; no mathematical statement or gate status changed'}
(root / 'logs/ROOT_integrate_late_source_entries.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
