"""Certify completed actual image inspection for CP28; never create an archive."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, re, sys, zipfile

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
build = sys.argv[1]
pdf = root / 'build/RESEARCH_SA12_paper.pdf'
log = (root / f'code/output/{build}.stdout.txt').read_text()
run = json.loads((root / f'code/output/{build}.run.json').read_text())
assert run['returncode'] == 0
assert not any(value in log for value in ['Warning', 'Missing character', 'undefined'])
overflow = lambda value: [float(x) for x in re.findall(r'Overfull \\hbox \(([0-9.]+)pt too wide\)', value)]
after = overflow(log)
before = overflow((root / 'code/output/build_pass183.stdout.txt').read_text())
assert max(after, default=0) <= 2.0
render = json.loads((root / 'qa/checkpoint28_render.json').read_text())
inspection = json.loads((root / 'qa/checkpoint28_actual_inspection.json').read_text())
sha = hashlib.sha256(pdf.read_bytes()).hexdigest()
assert inspection['pdf_sha256'] == sha and inspection['build'] == build
assert inspection['rendered_pages'] == render['rendered_pages']
assert len(inspection['contact_sheets_viewed']) == (len(render['rendered_pages']) + 8) // 9
assert inspection['actual_image_output_observed'] is True
record = dict(
    utc=now, build=build, pages=render['pdf_pages'], sha256=sha,
    overfull_before=len(before), maximum_overfull_before_pt=max(before, default=0),
    overfull_after=len(after), maximum_overfull_after_pt=max(after, default=0),
    warnings_after=0, undefined_citations_after=0, undefined_references_after=0, missing_characters_after=0,
    rendered_and_inspected_pages=sorted(set(render['rendered_pages']) | set(inspection['full_pages_viewed'])),
    individual_full_page_inspections=inspection['full_pages_viewed'], image_format='lossless WebP',
    lossless_pixel_roundtrip_checks=len(render['lossless_pixel_roundtrip_checks']),
    actual_inspection_record='qa/checkpoint28_actual_inspection.json', visual_outcome=inspection['visual_outcome'],
    intermediate_build_notes='Build182 stopped before manuscript compilation because the existing private TEXMF path was omitted; build183 reused the installed support tree. Its first full compilation had a7.19272pt prose overflow and first-pass new-label warnings. The exact slash-to-and typography correction is recorded separately from the mathematical audits. All bibliography and LuaLaTeX passes remain sequential. Only the final exact PDF hash is certified here.'
)
for name in ['qa/pdf_verified.json', 'qa/pdf_verified_checkpoint28.json']:
    (root / name).write_text(json.dumps(record, indent=2) + '\n')
with (root / 'RESEARCH_SA12_results.csv').open() as f:
    rows = sum(1 for _ in csv.DictReader(f))
with (root / 'CHECK_EVENTS.tsv').open() as f:
    events = sum(1 for _ in csv.DictReader(f, delimiter='\t'))
prior = json.loads((root / 'code/output/formal_review18.json').read_text())
assert prior['consecutive_no_movement_reviews'] == 0 and not prior['stopping_condition_met']
assessment = json.loads((root / 'code/output/review19_main_assessment.json').read_text())
assert assessment['assembled_statement_count'] == rows
assert assessment['central_actual_check_event_count'] == events
with (root / 'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n## Checkpoint28 paper verification completed\n\nINCOMPLETE. ' + now + '. Final ' + build + ' has ' + str(render['pdf_pages']) + 'pages, SHA256 ' + sha + '. Root actually viewed ' + str(len(inspection['contact_sheets_viewed'])) + ' contact sheets covering ' + str(len(render['rendered_pages'])) + ' pages and full pages ' + ', '.join(map(str, inspection['full_pages_viewed'])) + '. Zero final warnings and undefined citations/references; overfull boxes before/after:' + str(len(before)) + '/' + str(len(after)) + ', maximum final overflow:' + str(max(after, default=0)) + 'pt (required limit2pt). There are ' + str(rows) + ' statement rows and ' + str(events) + ' actual central check events. This is verification, not research movement, and creates no ZIP. Formal review19 and checkpoint28 are due21:10UTC; the staged assessment records one grouped bounded-period main-gate reduction.\n')
scope = f'''# Checkpoint28 scope

INCOMPLETE. Scheduled creation:20 November2026,21:10UTC. This full archive contains the current deliverables and accumulated documentation, excluding original supplied attachments and earlier ZIPs. Formal review19 is performed at that scheduled time, before archive creation.

The verified manuscript has {render['pdf_pages']}pages, final {build}, SHA256 {sha}, {rows}statement rows and {events}actual central check events. Newly assembled units and their exact historical integration hashes are recorded in code/output/integrate_post19_post27*.json. Audited candidate snapshots, dependency-discharge deltas, status-only promotions and separate typography changes remain included. Unassembled research files retain their individual status.

{assessment['report_summary']}

The projective count retains the full scalar coefficient obstruction, even when its order is unbounded. Only geometric Brauer period is bounded. For nonconstant field bands this period is measured after restriction to the field kernel. The genuine twisted H2 calculation includes the middle Cartan-Leray descent term; the exceptional-lattice quotient requires the squared permutation-kernel bound. The short Frobenius cycle has f/a phases on the degree-ta field cover, giving O_R,B(ftr²) coordinates and bounded-degree equations without an expanded deck word.

Simultaneous Morita construction retains the actual canonical full orders, balanced arrows, inverse equations and overlap cocycles with the specified lower marking. All coefficient-ring formal effectivity is distinct from Noetherian completed-base algebraization. Generated fixed determinants and global finite Hom equations give the required etale unit-Isom comparison even for noncanonical objects in the finite atlas. Morita reconstruction is used on the puncture. No arbitrary intermediate-lattice generation, relative root-stack hull flatness, or bounded-degree etale neutralizing cover is inferred.

The earlier finite-puncture alternating criterion continues to charge minimum weighted imprimitive-tower energy, with the previously checked non-natural alternating recognition. Unbounded natural A_N/S_N actions remain charged. Hereditary original-divisorial local-pair counting has not been proved. General nonabelian crowns still require their explicit faithful model, bounded residual outer index and quadratic simple-order comparison; generator estimates retain d(P).

No requested outcome changes. General D.1, general D.2(ii), and residual dependent L8 remain open. The formal review record contains the exact comparison with review18. All prerequisites and corollaries of the new bounded-period count are grouped as one reduction. Source checking, builds, image QA and archive delivery do not reset the no-movement counter. The next checkpoint is21:55UTC and review20 is22:10UTC if research continues.

The final PDF has zero warnings, missing characters and undefined citations/references. Overfull boxes before/after:{len(before)}/{len(after)}; maximum final overflow:{max(after, default=0)}pt, within the2pt limit. Actual image inspection is recorded in qa/checkpoint28_actual_inspection.json and qa/pdf_verified_checkpoint28.json. New inspection images use lossless WebP with exact RGB round-trip checks. Previous immutable archives retain their original bytes.
'''
(root / 'CHECKPOINT28_SCOPE.md').write_text(scope)
with zipfile.ZipFile(root.parent / 'RESEARCH_SA12_checkpoint_27.zip') as z:
    old = json.loads(z.read('RESEARCH_SA12/CHECKPOINT_MANIFEST.json'))
    old_hash = {entry['path']: entry['sha256'] for entry in old['files']}
    sizes = {entry.filename.removeprefix('RESEARCH_SA12/'): entry.compress_size for entry in z.infolist()}
    upper = raw = unchanged = changed = 0
    for p in root.rglob('*'):
        if not p.is_file() or p.suffix == '.zip' or '__pycache__' in p.parts:
            continue
        rel = str(p.relative_to(root))
        data = pdf.read_bytes() if rel == 'RESEARCH_SA12_paper.pdf' else p.read_bytes()
        raw += len(data)
        if old_hash.get(rel) == hashlib.sha256(data).hexdigest():
            upper += sizes[rel]
            unchanged += 1
        else:
            upper += len(data) + len(data) // 1000 + 64
            changed += 1
        upper += 256 + 2 * len(('RESEARCH_SA12/' + rel).encode())
    upper += 3_000_000
assert upper < 500_000_000, upper
prep = dict(utc=now, scheduled_archive_utc='2026-11-20T21:10:00+00:00', archive_created=False,
            current_conservative_zip_bound_bytes=upper, current_raw_bytes=raw,
            unchanged_files=unchanged, changed_or_new_files=changed,
            remaining_below_cap_bytes=500_000_000 - upper, verified_pdf=record)
(root / 'code/output/checkpoint28_preparation.json').write_text(json.dumps(prep, indent=2) + '\n')
print(json.dumps({key: value for key, value in prep.items() if key != 'verified_pdf'}, indent=2))
