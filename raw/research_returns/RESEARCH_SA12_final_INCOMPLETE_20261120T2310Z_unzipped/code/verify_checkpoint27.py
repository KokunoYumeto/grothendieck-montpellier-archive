"""Certify completed actual image inspection for CP27; create no archive."""
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
assert not any(s in log for s in ['Warning', 'Missing character', 'undefined'])
overflow = lambda s: [float(x) for x in re.findall(r'Overfull \\hbox \(([0-9.]+)pt too wide\)', s)]
after = overflow(log)
before = overflow((root / 'code/output/build_pass175.stdout.txt').read_text())
assert max(after, default=0) <= 2.0
render = json.loads((root / 'qa/checkpoint27_render.json').read_text())
inspection = json.loads((root / 'qa/checkpoint27_actual_inspection.json').read_text())
sha = hashlib.sha256(pdf.read_bytes()).hexdigest()
assert inspection['pdf_sha256'] == sha
assert inspection['rendered_pages'] == render['rendered_pages']
assert len(inspection['contact_sheets_viewed']) == (len(render['rendered_pages']) + 8) // 9
assert inspection['actual_image_output_observed'] is True
record = dict(
    utc=now, build=build, pages=render['pdf_pages'], sha256=sha,
    overfull_before=len(before), maximum_overfull_before_pt=max(before, default=0),
    overfull_after=len(after), maximum_overfull_after_pt=max(after, default=0),
    warnings_after=0, undefined_citations_after=0, undefined_references_after=0,
    missing_characters_after=0,
    rendered_and_inspected_pages=sorted(set(render['rendered_pages']) | set(inspection['full_pages_viewed'])),
    individual_full_page_inspections=inspection['full_pages_viewed'],
    image_format='lossless WebP',
    lossless_pixel_roundtrip_checks=len(render['lossless_pixel_roundtrip_checks']),
    actual_inspection_record='qa/checkpoint27_actual_inspection.json',
    visual_outcome=inspection['visual_outcome'],
    intermediate_build_notes='Before is the actual first post26 build175, whose four-column split display stopped compilation. Its exact alignment-only correction is recorded. The first clean546-page build178 and all actual image inspections are retained under qa/checkpoint27_initial_verified before six later auxiliary units were integrated. Only the final exact PDF hash is certified here. All bibliography and LuaLaTeX passes are sequential; actual typography changes have separate exact records.'
)
for name in ['qa/pdf_verified.json', 'qa/pdf_verified_checkpoint27.json']:
    (root / name).write_text(json.dumps(record, indent=2) + '\n')
with (root / 'RESEARCH_SA12_results.csv').open() as f:
    rows = sum(1 for _ in csv.DictReader(f))
with (root / 'CHECK_EVENTS.tsv').open() as f:
    events = sum(1 for _ in csv.DictReader(f, delimiter='\t'))
review = json.loads((root / 'code/output/formal_review18.json').read_text())
assert review['consecutive_no_movement_reviews'] == 0 and not review['stopping_condition_met']
with (root / 'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n## Checkpoint27 paper verification completed\n\nINCOMPLETE. ' + now + '. Final ' + build + ' has ' + str(render['pdf_pages']) + 'pages, SHA256 ' + sha + '. Root actually viewed ' + str(len(inspection['contact_sheets_viewed'])) + ' contact sheets covering ' + str(len(render['rendered_pages'])) + ' pages and full pages ' + ', '.join(map(str, inspection['full_pages_viewed'])) + '. Final build has zero warnings and undefined citations/references; overfull boxes before/after:' + str(len(before)) + '/' + str(len(after)) + ', maximum final overflow:' + str(max(after, default=0)) + 'pt (required limit2pt). There are ' + str(rows) + ' statement rows and ' + str(events) + ' actual central check events. This verification is not research movement and creates no ZIP. Review18 recorded two grouped main-gate reductions, counter0; review19 is due21:10UTC. Checkpoint27 is scheduled20:25UTC.\n')
scope = f'''# Checkpoint27 scope

INCOMPLETE. Scheduled creation:20 November2026,20:25UTC. This full archive contains the current deliverables and accumulated documentation, excluding original supplied attachments and earlier ZIPs. It performs no unscheduled formal review.

The verified manuscript has {render['pdf_pages']}pages, final {build}, SHA256 {sha}, {rows}statement rows and {events}actual central check events. Newly assembled units and exact historical integration hashes are recorded in code/output/integrate_post19_post26*.json. Audited candidate snapshots and exact status-only promotions remain included. Research files not assembled retain their individual status.

The arbitrary-cover ordinary and prescribed-field-character semilinear counts prove q^(A_R t r^2) classes on every connected degree-t punctured cover of a fixed complete excellent normal local surface. The concrete faithful linear and semilinear crown consequences allow arbitrary permutation quotients and field characters, including field order divisible by p, subject to their explicit bounded residual outer index and quadratic simple-order comparison. The generator estimate retains d(P). They do not prove arbitrary-cover projective counting.

The finite-puncture alternating criterion now charges minimum weighted imprimitive-tower energy, sum(T_i m_i^2) over unrestricted levels, and allows arbitrary-height towers of the stated modelled primitive actions. The new recognition includes non-natural alternating-socle subset/product actions with squared matrix rank at most4N and the checked small-order branch. Unbounded natural A_N/S_N actions remain charged. The original-divisorial theorem retains its earlier whole-orbit scope; hereditary original-divisorial local-pair counting has not been proved.

The auxiliary controlled SNC refinement gives at most2delta+7G<=9G+2v-2c point blowups for a reduced proper curve, in every characteristic. On the actual degree-t cover model this yields O_R(t) centres, components, nodes and normalization genus. Pullback of the old actual Cartier cycles preserves full nonreduced-cycle cohomology, weak-cycle vanishings, intersections, generation, determinant markings and actual Frobenius inverse-pole bounds. The stipulated centres also preserve a uniform Jacobian ratio. This does not bound products of adjacent cycle multiplicities or itself construct a twisted anchor. The separately retained projective-cost note identifies the original component and node costs without claiming a hereditary projective theorem.

Six auxiliary units completed after review18 give the full-bundle degree bound, actual canonical orders and a fixed Morita-product conductor, actual scaled-separability tensors, explicit local Newton action lifting and exact averaging, and bounded-period geometric anchor comparisons. A bipartite refinement supplies an actual generating anchor of rank at mostM^4. Its coarse order and Hom modules satisfy the exact bounded Cartier sandwiches, but arbitrary intermediate-lattice cohomology/generation and relative reflexive-hull flatness are not inferred. The local action theorem does not itself prove simultaneous global Morita-unit or overlap effectivity. These six supporting statements are not an additional main-gate movement or a completed hereditary projective count.

Formal review18 at20:10UTC counted two grouped strict reductions since review17: the arbitrary-cover ordinary/semilinear counting and faithful crown consequence, and the enlarged finite-puncture tower-energy alternating criterion. Supporting geometry, object-family constructions, scalar estimates and recognition are not separately counted. No requested outcome changed. General D.1, general D.2(ii), and residual dependent L8 remain open. The consecutive no-movement counter is zero; review19 is due21:10UTC. The next scheduled checkpoint is21:10UTC if work continues. Only a requested-row status change or a strictly smaller strongest main gate can reset the stopping counter.

The final PDF has zero warnings, missing characters and undefined citations/references. Overfull boxes before/after:{len(before)}/{len(after)}; maximum final overflow:{max(after, default=0)}pt, within the2pt limit. Actual image inspection is recorded in qa/checkpoint27_actual_inspection.json and qa/pdf_verified_checkpoint27.json. New inspection images use lossless WebP with exact RGB round-trip checks. Earlier immutable archives retain their original bytes. Only the exact certified PDF hash is delivered.
'''
(root / 'CHECKPOINT27_SCOPE.md').write_text(scope)
with zipfile.ZipFile(root.parent / 'RESEARCH_SA12_checkpoint_26.zip') as z:
    old = json.loads(z.read('RESEARCH_SA12/CHECKPOINT_MANIFEST.json'))
    old_hash = {x['path']: x['sha256'] for x in old['files']}
    sizes = {x.filename.removeprefix('RESEARCH_SA12/'): x.compress_size for x in z.infolist()}
    upper = raw = unchanged = changed = 0
    for p in root.rglob('*'):
        if not p.is_file() or p.suffix == '.zip' or '__pycache__' in p.parts:
            continue
        rel = str(p.relative_to(root))
        b = pdf.read_bytes() if rel == 'RESEARCH_SA12_paper.pdf' else p.read_bytes()
        raw += len(b)
        if old_hash.get(rel) == hashlib.sha256(b).hexdigest():
            upper += sizes[rel]
            unchanged += 1
        else:
            upper += len(b) + len(b) // 1000 + 64
            changed += 1
        upper += 256 + 2 * len(('RESEARCH_SA12/' + rel).encode())
    upper += 3_000_000
assert upper < 500_000_000, upper
prep = dict(
    utc=now, scheduled_archive_utc='2026-11-20T20:25:00+00:00', archive_created=False,
    current_conservative_zip_bound_bytes=upper, current_raw_bytes=raw,
    unchanged_files=unchanged, changed_or_new_files=changed,
    remaining_below_cap_bytes=500_000_000 - upper, verified_pdf=record
)
(root / 'code/output/checkpoint27_preparation.json').write_text(json.dumps(prep, indent=2) + '\n')
print(json.dumps({k: v for k, v in prep.items() if k != 'verified_pdf'}, indent=2))
