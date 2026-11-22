"""Certify the exact CP30 PDF only after actual image inspection and review20."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re
import sys
import zipfile
import zlib

root = Path(__file__).resolve().parents[1]
build = sys.argv[1]
pdf_only = len(sys.argv) == 3 and sys.argv[2] == '--pdf-only'
assert len(sys.argv) == 2 or pdf_only
now = datetime.now(timezone.utc).isoformat()
freeze = json.loads((root / 'code/output/checkpoint30_source_freeze.json').read_text())
assert freeze['build'] == build
for rel, digest in freeze['files'].items():
    assert hashlib.sha256((root / rel).read_bytes()).hexdigest() == digest, rel
run = json.loads((root / f'code/output/{build}.run.json').read_text())
log = (root / f'code/output/{build}.stdout.txt').read_text()
assert run['returncode'] == 0
assert not any(x in log for x in ['Warning', 'Missing character', 'undefined'])
over = lambda text: [float(x) for x in re.findall(r'Overfull \\hbox \(([0-9.]+)pt too wide\)', text)]
after = over(log)
assert max(after, default=0) <= 2
pdf = root / 'build/RESEARCH_SA12_paper.pdf'
digest = hashlib.sha256(pdf.read_bytes()).hexdigest()
render = json.loads((root / 'qa/checkpoint30_render.json').read_text())
inspection = json.loads((root / 'qa/checkpoint30_actual_inspection.json').read_text())
assert inspection['build'] == build and inspection['pdf_sha256'] == digest
assert inspection['rendered_pages'] == render['rendered_pages']
assert inspection['actual_image_output_observed'] is True
prefix = render.get('artifact_prefix', 'checkpoint30')
expected = [f'qa/{prefix}_contact_{i}.webp'
            for i in range(1, (len(render['rendered_pages']) + 8) // 9 + 1)]
assert inspection['contact_sheets_viewed'] == expected
assert all((root / p).is_file() for p in expected)
with (root / 'RESEARCH_SA12_results.csv').open() as f:
    rows = sum(1 for _ in csv.DictReader(f))
with (root / 'CHECK_EVENTS.tsv').open() as f:
    events = sum(1 for _ in csv.DictReader(f, delimiter='\t'))
assert rows == freeze['statement_count'] and events == freeze['check_event_count']
qa = dict(utc=now, build=build, pages=render['pdf_pages'], sha256=digest,
          overfull_after=len(after), maximum_overfull_after_pt=max(after, default=0),
          warnings_after=0, undefined_references_after=0, undefined_citations_after=0,
          missing_characters_after=0, rendered_and_inspected_pages=render['rendered_pages'],
          individual_full_page_inspections=inspection['full_pages_viewed'],
          actual_inspection_record='qa/checkpoint30_actual_inspection.json',
          image_format='lossless WebP',
          lossless_pixel_roundtrip_checks=len(render['lossless_pixel_roundtrip_checks']),
          visual_outcome=inspection['visual_outcome'],
          source_freeze='code/output/checkpoint30_source_freeze.json',
          intermediate_build_note='Build190 stopped before manuscript compilation because the private TEXMF path was omitted. Build191 reused the installed support tree. Subsequent passes use the recorded runtime wrapper. All bibliography and LuaLaTeX passes were sequential.',
          typography_record='code/output/checkpoint30_toc_spacing_delta.json',
          mathematical_correction_record='code/output/integrate_A_chain_coordinate_correction.json',
          previous_pdf_QA='qa/pdf_verified_checkpoint30_pre_coordinate_correction.json',
          note='Every new proof page, the full corrected A-chain block and its Artinian companion, and the changed opening/scope/bibliography pages were rendered and actually inspected. The contents number column was widened in an earlier typography-only pass. A separately documented substantive correction defines intrinsic branch jets and proves adapted coordinates; its four exact audits, original erroneous source, exact reversal and all earlier images remain preserved. No mathematical correction is disguised as typography.')
for rel in ['qa/pdf_verified.json', 'qa/pdf_verified_checkpoint30.json']:
    (root / rel).write_text(json.dumps(qa, indent=2) + '\n')
if pdf_only:
    print(json.dumps({'build': build, 'pages': render['pdf_pages'], 'sha256': digest,
                      'actual_image_inspection_verified': True,
                      'formal_review_or_archive_created': False}))
    raise SystemExit(0)
review = json.loads((root / 'code/output/formal_review20.json').read_text())
assert not review['stopping_condition_met']
scope = f'''# Checkpoint30 scope

INCOMPLETE. Scheduled creation:20 November2026,22:40UTC. This verification creates no archive. Checkpoint29 was created on time, all6652members passed exact manifest/hash/CRC verification, and its save succeeded. Its487984132-byte archive is immutable. Checkpoint28 remains absent; its failed-slot and late-verification records are retained without a late retry.

The source-frozen manuscript has{render['pdf_pages']}pages,{rows}statement rows,{events}central check events and57requested outcome rows. Final build:{build}. PDF SHA256:{digest}. General D.1, general D.2(ii), and residual dependent L8 remain open.

Five newly assembled auxiliary units have four complete actual-file/source audits each. The prime-to-characteristic local period-index input and mixed-node subdivision give a generating anchor of rank M, equal to the geometric period; its coarse order has rank M² and twisted rank-r objects have local order-module rank r/M. Exceptional Picard rigidity keeps the divisor of every specified Artinian punctured line comparison equal to its closed-fibre divisor. The resulting class-openness theorem applies to already effective finite-type ordinary and fixed-order Morita unit families, without fixed determinant charts. A fixed elliptic cone has connected Heisenberg covers whose explicit projective unitary representations have exact unbounded geometric Brauer periods; the actual descended cyclic algebra is identified and the lower bound follows from the unramified norm criterion.

The rank-period and class-openness statements do not construct a uniform quantitative object atlas. The cone images are nilpotent, and no epimorphism onto the ambient simple unitary group or counterexample to the hereditary count is asserted. Separate incidence, balanced-residual and chain calculations retain their research-note status. No numerical experiment is substituted for a geometric proof.

The earlier A-chain framing proposition has a substantive correction. A preassigned w can vanish identically on a transverse endpoint branch; the finite jets are now defined intrinsically by maximal-ideal powers. The complete all-characteristic adapted-coordinate argument was checked independently by root,B,C,D. It preserves the original jet bounds and the actual Artinian companion. The original erroneous source, five-block reversal, exact audited candidate and all historical audit records remain available. Eight correction check events were appended for two existing labels; no new statement or movement was counted.

Formal review20 recorded movement:{review['movement']}; consecutive no-movement reviews:{review['consecutive_no_movement_reviews']}. Its exact strongest-gate comparison is in code/output/formal_review20.json. Review21 is due23:10UTC. Two consecutive formal reviews without a requested-row status change or strictly smaller strongest main gate require stopping and a separate final ZIP. Auxiliary statements, source audits, compilation, image inspection and archive handling do not reset the counter.

Actual image inspection:{len(expected)}contact sheets covering{len(render['rendered_pages'])}pages; individual full-page inspections:{', '.join(map(str, inspection['full_pages_viewed']))}. The contents number column was widened after page4 inspection showed three-digit subsection numbers touching titles; the exact typography delta and prior changed rasters are retained. All new inspection images use lossless WebP with exact decoded-RGB equality checks. Final warnings, missing characters and undefined references/citations:zero. Maximum overflow:{max(after, default=0)}pt, within the2pt requirement.
'''
(root / 'CHECKPOINT30_SCOPE.md').write_text(scope)
with (root / 'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n## Checkpoint30 manuscript verification completed\n\nINCOMPLETE. '
            + now + '. ' + str(rows) + 'statements; ' + str(events) + 'check events; '
            + str(render['pdf_pages']) + 'pages. Exact PDF:' + digest + '. Root actually viewed '
            + str(len(expected)) + 'contact sheets and ' + str(len(inspection['full_pages_viewed']))
            + 'individual pages. Final warnings/undefined citations/references/missing characters:zero; '
            + 'maximum overflow' + str(max(after, default=0)) + 'pt. This is QA, not movement. No ZIP created.\n')

# A read-only compression estimate creates no ZIP or archive object.
with zipfile.ZipFile(root.parent / 'RESEARCH_SA12_checkpoint_29.zip') as z:
    old = json.loads(z.read('RESEARCH_SA12/CHECKPOINT_MANIFEST.json'))
    old_hash = {v['path']: v['sha256'] for v in old['files']}
    old_sizes = {i.filename.removeprefix('RESEARCH_SA12/'): i.compress_size for i in z.infolist()}
    upper = raw = unchanged = changed = 0
    for p in sorted(root.rglob('*')):
        if not p.is_file() or p.suffix == '.zip' or '__pycache__' in p.parts or p.name == 'CHECKPOINT_MANIFEST.json':
            continue
        rel = str(p.relative_to(root))
        data = pdf.read_bytes() if rel == 'RESEARCH_SA12_paper.pdf' else p.read_bytes()
        raw += len(data)
        if old_hash.get(rel) == hashlib.sha256(data).hexdigest():
            upper += old_sizes[rel]
            unchanged += 1
        else:
            upper += len(zlib.compress(data, 6, wbits=-15))
            changed += 1
        # Seekable ZIP_DEFLATED writestr uses 30-byte local and 46-byte
        # central fixed headers. All members and totals are below ZIP64
        # limits. Reserve an additional20 bytes per member, then750k for
        # the compressed manifest, end records and subsequent small logs.
        upper += 96 + 2 * len(('RESEARCH_SA12/' + rel).encode())
    upper += 750_000
assert upper < 500_000_000, upper
prep = dict(utc=now, scheduled_archive_utc='2026-11-20T22:40:00+00:00', archive_created=False,
            current_conservative_zip_bound_bytes=upper, current_raw_bytes=raw,
            unchanged_files=unchanged, changed_or_new_files=changed,
            remaining_below_cap_bytes=500_000_000-upper, verified_pdf=qa,
            size_method='Read-only raw-DEFLATE calculation, exact unchanged-size reuse, actual76-byte ZIP fixed headers plus20-byte/member reserve, UTF8 names twice, and750k manifest/end/log reserve. No ZIP or archive object created.')
(root / 'code/output/checkpoint30_preparation.json').write_text(json.dumps(prep, indent=2) + '\n')
print(json.dumps({k: v for k, v in prep.items() if k != 'verified_pdf'}, indent=2))
