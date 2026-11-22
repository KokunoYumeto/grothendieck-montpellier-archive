#!/usr/bin/env python3
"""Package all current work, never another checkpoint ZIP.

The scheduled checkpoint creation guard enforces the requested45-minute
cadence. It does not wait, upload, or mark an active session complete.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import csv
import hashlib
import json
import zipfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('index', type=int)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[3]
    started = datetime(2026,11,21,23,12,tzinfo=timezone.utc)
    now = datetime.now(timezone.utc)
    elapsed = (now-started).total_seconds()
    assert args.index >= 1
    assert elapsed >= args.index*45*60, 'Scheduled time has not arrived'
    assert elapsed < args.index*45*60+5*60, 'Outside scheduled checkpoint window'
    target = root/f'GCT_OBS_checkpoint_{args.index:02d}.zip'
    assert not target.exists(), 'Never overwrite an earlier checkpoint'
    manifest = []
    entries = []
    for base, prefix in [(root/'deliverable',Path('')), (root/'work',Path('work'))]:
        for p in sorted(base.rglob('*')):
            if not p.is_file() or '__pycache__' in p.parts:
                continue
            if p.suffix in ('.zip','.fmt','.pyc','.pdf','.aux','.toc','.out'):
                continue
            arc = str(prefix/p.relative_to(base))
            entries.append((p,arc))
    entries.append((root/'upload/PROMPT(20261121-231313).md','instructions/PROMPT.md'))
    for p,arc in entries:
        b=p.read_bytes()
        manifest.append(dict(path=arc,size_bytes=len(b),sha256=hashlib.sha256(b).hexdigest()))
    metadata=dict(index=args.index,created_utc=now.isoformat(),elapsed_seconds=elapsed,
                  active_session=True,source_archive='GCT_OBS_explicit_multiplicity_obstructions_for_the_padded_pe.zip',files=manifest)
    with zipfile.ZipFile(target,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p,arc in entries:z.write(p,arc)
        z.writestr('CHECKPOINT_MANIFEST.json',json.dumps(metadata,indent=2)+'\n')
    with zipfile.ZipFile(target) as z:
        assert z.testzip() is None
        assert not any(name.lower().endswith('.zip') for name in z.namelist())
        for required in ('GCT_OBS.tex','QUESTIONS.tsv','LEDGER.md','CHECK_EVENTS.tsv','IMPLICATIONS.md'):
            assert required in z.namelist()
    print(json.dumps(dict(path=str(target),size_bytes=target.stat().st_size,
                          sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
                          files=len(entries),created_utc=now.isoformat())))


if __name__=='__main__':main()
