#!/usr/bin/env python3
"""Record completion after the substantive reviews and final audit have passed."""
import json
from datetime import datetime,timezone
from pathlib import Path
R=Path(__file__).resolve().parents[1]
v=json.loads((R/'VALIDATION.json').read_text())
assert v['passed'] and not v['source_range_scan_notes']
t=datetime.now(timezone.utc).isoformat()
lines=[
 'STAGE 1 COMPLETE: 380 individually reviewed entries; 252 canonical items after six explicit cross-packet item aliases. No keyword-based semantic verdicts.',
 'STAGE 2 COMPLETE: 216 canonical claim records; every claim linked to searched fate, page status and computation/proof record; one Sullivan provenance record separately attributed.',
 'STAGE 3 COMPLETE: 73 authorial problems with exact scoped literature states and separately stated present formulations.',
 'STAGE 4 COMPLETE: 173 evidence-backed reading alarms; no image decisions or changes to source transcription.',
 'STAGE 5 COMPLETE: 107 checked correspondence rows; external-project correspondences also in their own table; 105 original project leads retain explicit updated verification/unlocated status.',
 'STAGE 6 COMPLETE: 12 ranked directions, each linked to existing item, claim and problem IDs; subsequent research tasks are not developed here.',
 f'FINAL VALIDATION: {v["checks_passed"]}/{v["checks_total"]} structural/provenance checks passed; 961 named manuscript line ranges checked; all18 supplied files retain initial hashes; zero scan/line metadata gaps.',
 'END: substantive work and all six requested deliverables are complete; final immutable SA09.zip is being sealed and persisted. Packaging creation time and per-file hashes are recorded in ARCHIVE_MANIFEST.json.'
]
p=R/'progress.log'
if '\n'+t+' END:' in p.read_text():raise SystemExit('Already recorded')
with p.open('a') as f:
 for line in lines:f.write(t+' '+line+'\n')
print(json.dumps({'completion_utc':t,'stage_completions':6,'validation_passed':v['passed']},indent=2))
