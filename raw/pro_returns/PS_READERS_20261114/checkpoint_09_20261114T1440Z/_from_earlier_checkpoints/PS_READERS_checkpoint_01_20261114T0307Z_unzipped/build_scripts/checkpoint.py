#!/usr/bin/env python3
"""Create a new, non-overwriting checkpoint; inputs remain in supplied ZIPs."""
import argparse, hashlib, json, zipfile
from pathlib import Path
from review import ROOT
from assemble_records import main as assemble

def main(note):
    stats=assemble();directory=ROOT/'checkpoints';directory.mkdir(exist_ok=True)
    numbers=[int(p.stem.rsplit('_',1)[1]) for p in directory.glob('PS_READERS_checkpoint_*.zip')]
    n=max(numbers,default=0)+1;name=f'PS_READERS_checkpoint_{n:02d}.zip';target=directory/name
    assert not target.exists()
    status=f'''# Pursuing Stacks: working checkpoint {n:02d}

This checkpoint records work in progress. It is not a completed edition.

{note}

- Pages visually reviewed and committed: {stats['reviewed_pages']} / 706.
- Original comparison rows: 12,140; all are present in ARXIV_CONCORDANCE.tsv.
- Rows awaiting image review retain the explicit pending outcome.
- Source edits recorded: {stats['source_changes']}.
- Decision records: {stats['decision_rows']}.
- No reader has passed the complete publication gates at this checkpoint.

## Contents and continuation

checked_pages/ contains only pages with a complete, explicit visual review.
review/ holds the item-level findings and exact source edits. A page's original
metadata header is historical; its current status is in its review record.
guide_parts/ holds section paragraphs completed during review.
build_scripts/ contains the reproducible record and edition tooling written so far.
PAGE_REVIEW_COVERAGE.tsv and REVIEW_STATUS.json provide exact coverage.

The supplied archives PS_TEXT.zip, PS_SCANS_1.zip and PS_SCANS_2.zip remain the
sources for transcription/, records/, arxiv/, standard/ and scans/. Extract them
beside build_scripts/, preserving their internal paths, then restore this
checkpoint over the extracted tree. The arXiv witness and scans are not republished
inside this checkpoint. No previous checkpoint ZIP is embedded.

Run `python build_scripts/assemble_records.py` to rebuild the audit tables.
Run it with `--require-complete` to enforce the visual-review completion gate.
Run `python build_scripts/review.py status` to report coverage by cote.
The scripts themselves do not make or infer image decisions.
'''
    (ROOT/'README.md').write_text(status)
    roots=['checked_pages','review','guide_parts','build_scripts']
    files=[p for d in roots for p in (ROOT/d).rglob('*') if p.is_file() and '__pycache__' not in p.parts]
    files += [ROOT/n for n in ['README.md','CHECK_DECISIONS.tsv','ARXIV_CONCORDANCE.tsv','PAGE_REVIEW_COVERAGE.tsv','REVIEW_STATUS.json']]
    for n in ['CHANGES_EN.tsv','APPARATUS_COUNTS.md','TYPESETTING_FIXES.tsv','TYPESETTING_REPORT.md','BUILD_STATUS.json']:
        if (ROOT/n).exists():files.append(ROOT/n)
    if (ROOT/'output').exists():
        files += [p for p in (ROOT/'output').rglob('*') if p.is_file() and p.suffix in ('.tex','.pdf','.json','.tsv','.md')]
    entries=[]
    with zipfile.ZipFile(target,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=7) as z:
        for p in sorted(set(files)):
            relative=str(p.relative_to(ROOT));data=p.read_bytes();z.writestr(relative,data)
            entries.append({'path':relative,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
        z.writestr('CHECKPOINT_MANIFEST.json',json.dumps(entries,indent=2)+'\n')
    print(json.dumps({'checkpoint':name,'files':len(entries),'bytes':target.stat().st_size,'reviewed_pages':stats['reviewed_pages']}))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--note',default='Page review and edition preparation are ongoing.');a=p.parse_args();main(a.note)
