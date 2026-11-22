"""Record completed image inspection and checkpoint18 readiness; creates no ZIP."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, zipfile
root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
pdf = root / 'build/RESEARCH_SA12_paper.pdf'
log = (root/'code/output/build_pass113.stdout.txt').read_text()
run = json.loads((root/'code/output/build_pass113.run.json').read_text())
assert run['returncode'] == 0
assert not any(s in log for s in ['Warning','Overfull','Missing character','undefined'])
render = json.loads((root/'qa/checkpoint18_render.json').read_text())
assert render['pdf_pages'] == 345 and len(render['rendered_pages']) == 58
assert render['image_format'] == 'webp'
assert len(render['lossless_pixel_roundtrip_checks']) == 65
record = dict(utc=now,build='build_pass113',pages=345,
    sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),
    overfull_before=0,overfull_after=0,maximum_overfull_after_pt=0,
    warnings_after=0,undefined_citations_after=0,undefined_references_after=0,
    missing_characters_before=0,missing_characters_after=0,
    rendered_and_inspected_pages=render['rendered_pages'],
    individual_full_page_inspections=[311,316,318,320],
    image_format='lossless WebP',lossless_pixel_roundtrip_checks=65,
    intermediate_build_errors=('Build109 stopped before document processing because the task-local '
        'TEXMF runtime path was omitted. Build110 used the already installed support tree and '
        'succeeded. Bibliography27 and builds111,112,113 ran sequentially. Build112 still requested '
        'one label rerun; final build113 is entirely clean. The initial renderer stopped on an '
        'execution-metadata JSON mistaken for an integration manifest; filtering .run.json records '
        'fixed that input selection before any inspection images were produced.'),
    visual_outcome=('Root actually viewed all seven contact sheets at13:26–13:27UTC, covering58 '
        'pages: every new proof page308–320, preceding307, updated unresolved discussion and '
        'bibliography through345, and a19-page spread. Root also viewed full-page images311,316,318,320 '
        'for the sparse-DVR presentation, nonreduced automatic adjunction, determinant recurrence '
        'and single-curve residue proof. No clipping, overlap, missing glyph or text beyond the '
        'margins was observed. Every new WebP passed an exact RGB pixel round-trip comparison. '
        'All earlier inspection images are unchanged. Only this exact PDF hash is certified.'))
for name in ['qa/pdf_verified.json','qa/pdf_verified_checkpoint18.json']:
    (root/name).write_text(json.dumps(record,indent=2)+'\n')
with (root/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n## Checkpoint18 paper verification completed\n\nINCOMPLETE. '+now+
        '. Sequential build113 has345pages, SHA256'+record['sha256']+
        '. Root actually viewed seven contact sheets covering58pages and full pages311,316,318,320. '
        'Final counts are zero warnings, overfull boxes, missing characters and unresolved citations/references. '
        'All65 new inspection images use lossless WebP with exact RGB round-trip checks; old images remain unchanged. '
        'The intermediate runtime-path omission, label rerun and renderer manifest-filter correction are recorded in '
        'qa/pdf_verified_checkpoint18.json. There are339 assembled statements,1048central check events and57requested '
        'outcome rows. Nine post17 units are integrated. No additional main reduction occurred after review11; '
        'generation, determinant charts, sparse DVR charts and one-curve residues remain auxiliary or closure inputs. '
        'General D.1, D.2(ii) and residual L8 remain open. Review12 is due14:10UTC; checkpoint18 is due13:40UTC. '
        'No archive is created by this verification.\n')
scope='''# Checkpoint18 scope

INCOMPLETE. Scheduled creation:20 November2026,13:40UTC. This is a full current-work archive, excluding supplied input attachments and earlier ZIPs.

The verified assembled manuscript has345pages, build113,339statement records,1048central check events and57requested outcome rows. Nine post17 units are assembled: the all-dimensional local surface-detected Brauer-zero transfer; three sparse-DVR presentation results; two bounded-geometric-period closure results; uniform generation of reflexive pullbacks; the fixed-determinant finite-cycle chart; and the single-smooth-exceptional-curve Brauer residue/period-degree cover proposition.

The fixed-period result covers every fixed bound B on geometric Brauer period, with its constant allowed to depend on B and scalar order unrestricted. It is a closure of the ONE Brauer-zero main reduction recorded at formal review11, not another movement event. Uniform generation and actual O(nr²) fixed-determinant section charts do not yet prove effective finite-thickening unit-object realization or all-arrow determination. The single-curve residue cover has exactly the geometric period as its degree and is etale over the entire resolution, but no representation count uniform in that period is inferred. Sparse DVR charts retain the explicit uncontrolled global coefficient-pole and constrained-extension issues.

General D.1, general D.2(ii) and residual L8 remain open. Formal review11 occurred at13:10:00.050379UTC and recorded one strict reduction since review10, resetting the consecutive no-movement count to0. The next formal review is14:10UTC. No additional movement is inferred from these auxiliary statements, closure consequences, searches, proof audits or packaging. Current research notes preserve their own unproved/candidate status and exact remaining realization conditions.

The final PDF has zero warnings, overfull boxes, missing characters and undefined citations/references. Root actually viewed seven contact sheets covering58pages and full pages311,316,318,320. The QA record is qa/pdf_verified_checkpoint18.json. New inspection images use lossless WebP with65 exact RGB round-trip checks; every earlier image is preserved unchanged. Intermediate build109's omitted runtime path and the first renderer's metadata-selection error were corrected and are recorded. Bibliography27 and subsequent builds were sequential; only final113 is certified.

Checkpoint17 and every earlier checkpoint remain immutable. The next scheduled checkpoint is14:25UTC. No off-schedule archive is created.
'''
(root/'CHECKPOINT18_SCOPE.md').write_text(scope)
previous = root.parent/'RESEARCH_SA12_checkpoint_17.zip'
with zipfile.ZipFile(previous) as z:
    old = json.loads(z.read('RESEARCH_SA12/CHECKPOINT_MANIFEST.json'))
    old_hash = {x['path']:x['sha256'] for x in old['files']}
    sizes = {x.filename.removeprefix('RESEARCH_SA12/'):x.compress_size for x in z.infolist()}
    upper=0;raw=0;unchanged=0;changed=0
    for p in root.rglob('*'):
        if not p.is_file() or p.suffix=='.zip' or '__pycache__' in p.parts:continue
        rel=str(p.relative_to(root));b=p.read_bytes();raw+=len(b)
        if rel=='RESEARCH_SA12_paper.pdf':b=pdf.read_bytes()
        if old_hash.get(rel)==hashlib.sha256(b).hexdigest():
            upper+=sizes[rel];unchanged+=1
        else:
            upper+=len(b)+len(b)//1000+64;changed+=1
        upper+=256+2*len(('RESEARCH_SA12/'+rel).encode())
    upper+=3_000_000 # late notes, metadata, manifest and receipt reserve
assert upper<500_000_000,upper
prep=dict(utc=now,scheduled_archive_utc='2026-11-20T13:40:00+00:00',archive_created=False,
    current_conservative_zip_bound_bytes=upper,current_raw_bytes=raw,
    unchanged_files=unchanged,changed_or_new_files=changed,
    remaining_below_cap_bytes=500_000_000-upper,verified_pdf=record)
(root/'code/output/checkpoint18_preparation.json').write_text(json.dumps(prep,indent=2)+'\n')
print(json.dumps({k:v for k,v in prep.items() if k!='verified_pdf'},indent=2))
