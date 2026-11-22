"""Verify the final CP29 manuscript and actual image record without creating any ZIP."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,re,sys,zipfile,zlib
root=Path(__file__).resolve().parents[1]
build=sys.argv[1];now=datetime.now(timezone.utc).isoformat()
freeze=json.loads((root/'code/output/checkpoint29_source_freeze.json').read_text())
for rel,digest in freeze['files'].items():
 assert hashlib.sha256((root/rel).read_bytes()).hexdigest()==digest,rel
run=json.loads((root/f'code/output/{build}.run.json').read_text())
log=(root/f'code/output/{build}.stdout.txt').read_text()
assert run['returncode']==0
assert not any(x in log for x in ['Warning','Missing character','undefined'])
over=lambda text:[float(x) for x in re.findall(r'Overfull \\hbox \(([0-9.]+)pt too wide\)',text)]
after=over(log);before=over((root/'code/output/build_pass187.stdout.txt').read_text())
assert max(after,default=0)<=2
pdf=root/'build/RESEARCH_SA12_paper.pdf';digest=hashlib.sha256(pdf.read_bytes()).hexdigest()
render=json.loads((root/'qa/checkpoint29_render.json').read_text())
inspection=json.loads((root/'qa/checkpoint29_actual_inspection.json').read_text())
assert inspection['build']==build and inspection['pdf_sha256']==digest
assert inspection['rendered_pages']==render['rendered_pages']
assert inspection['actual_image_output_observed'] is True
expected=[f'qa/checkpoint29_contact_{i}.webp' for i in range(1,(len(render['rendered_pages'])+8)//9+1)]
assert inspection['contact_sheets_viewed']==expected
assert all((root/p).is_file() for p in expected)
with (root/'RESEARCH_SA12_results.csv').open() as f:rows=sum(1 for _ in csv.DictReader(f))
with (root/'CHECK_EVENTS.tsv').open() as f:events=sum(1 for _ in csv.DictReader(f,delimiter='\t'))
assert rows==freeze['statement_count'] and events==freeze['check_event_count']
qa=dict(utc=now,build=build,pages=render['pdf_pages'],sha256=digest,
 overfull_before=len(before),maximum_overfull_before_pt=max(before,default=0),
 overfull_after=len(after),maximum_overfull_after_pt=max(after,default=0),
 warnings_after=0,undefined_references_after=0,undefined_citations_after=0,missing_characters_after=0,
 rendered_and_inspected_pages=render['rendered_pages'],individual_full_page_inspections=inspection['full_pages_viewed'],
 actual_inspection_record='qa/checkpoint29_actual_inspection.json',image_format='lossless WebP',
 lossless_pixel_roundtrip_checks=len(render['lossless_pixel_roundtrip_checks']),visual_outcome=inspection['visual_outcome'],
 source_freeze='code/output/checkpoint29_source_freeze.json',
 note='The local-recognition diagonal matrix was moved from inline math to a display; exact typography provenance is retained separately from the four original proof audits. The failed checkpoint28 slot remains absent; its genuine completed image inspection is retained as earlier evidence.')
for rel in ['qa/pdf_verified.json','qa/pdf_verified_checkpoint29.json']:
 (root/rel).write_text(json.dumps(qa,indent=2)+'\n')
review=json.loads((root/'code/output/formal_review19.json').read_text())
assert review['movement'] and review['consecutive_no_movement_reviews']==0 and not review['stopping_condition_met']
assert not (root.parent/'RESEARCH_SA12_checkpoint_28.zip').exists()
scope=f'''# Checkpoint29 scope

INCOMPLETE. Scheduled creation:20 November2026,21:55UTC. This preparation creates no archive. The scheduled archive will include all current deliverables and accumulated documentation, excluding supplied originals and previous ZIPs. Checkpoint28 was not created: its21:10 attempt rejected an uncertified final PDF, and actual verification finished ten seconds later. No off-cadence retry was performed. The full failed-slot record is included.

The source-frozen manuscript has {render['pdf_pages']}pages, {rows}statement rows, {events}actual central check events and57requested outcome rows. Final build:{build}; PDF SHA256:{digest}. Only general D.1, general D.2(ii), and residual dependent L8 remain open.

Review19 completed at21:10UTC and recorded one grouped strict reduction: bounded-geometric-period hereditary ordinary and prescribed-field projective-semilinear counts on arbitrary complete-local covers, their faithful projective crown consequences, and the finite-puncture normal-proper-surface transfer with degree-linear genus, normalized different, local jets and once-per-completed-source budgets. Full scalar coefficient orders and field-image orders remain unrestricted. Local geometric periods are measured after the actual local field kernels. All supporting effectivity, cohomology and curve results belong to this single group.

After that review, exact natural symplectic and orthogonal model recognition and its global finite-puncture crown closure were assembled. The model's full twisted scalar class is killed by two; all local restrictions retain that identity. The bound retains d(P), the exact family ranges, graph indices and actual coefficient fields. These are consequences of the existing group, not an additional movement. An explicit unitary shift/clock example has scalar obstruction of exact unbounded odd order. It disproves only a proposed uniform algebraic exponent shortcut; it constructs no representation of one fixed geometric fundamental group and does not refute the open hereditary count.

Unbounded-geometric-period hereditary counts, unrestricted natural alternating actions, uncovered cross-characteristic families, full generation, hereditary original-divisorial local pairs and the uncovered higher-dimensional boundary cases remain unresolved. New separate research retains its individual status and is not silently promoted into the manuscript. Formal review20 is due22:10UTC; two consecutive reviews without a requested-row status change or a strictly smaller strongest main gate require stopping. Source verification, bibliography notes, auxiliary examples, recognition closures, compilation, image inspection and archive handling do not reset that counter.

Actual image inspection:{len(expected)}contact sheets covering{len(render['rendered_pages'])}pages; full-page inspections:{', '.join(map(str,inspection['full_pages_viewed']))}. All new images use lossless WebP and exact decoded-RGB round-trip checks. Final warnings, missing characters and undefined citations/references:zero. Maximum final overflow:{max(after,default=0)}pt, within the2pt requirement. The separate typography correction reduced the new14.35371pt overflow without changing any matrix entry or proof.
'''
(root/'CHECKPOINT29_SCOPE.md').write_text(scope)
with (root/'PROGRESS_LEDGER.md').open('a') as f:
 f.write('\n\n## Checkpoint29 manuscript verification completed\n\nINCOMPLETE. '+now+'. '+str(rows)+'statements; '+str(events)+'check events; '+str(render['pdf_pages'])+'pages. Exact PDF:'+digest+'. Root actually viewed '+str(len(expected))+'contact sheets and '+str(len(inspection['full_pages_viewed']))+'individual pages. No warnings/undefined references/citations/missing characters; maximum overflow'+str(max(after,default=0))+'pt. This is QA, not movement. No ZIP created by this verification. Scheduled checkpoint29 is21:55UTC.\n')
# Read-only raw-DEFLATE size calculation: this builds no ZIP or archive object.
# Reuse exact compressed sizes only for unchanged members; compress changed bytes
# in memory with the same method as the later scheduled ZIP writer.
with zipfile.ZipFile(root.parent/'RESEARCH_SA12_checkpoint_27.zip') as z:
 old=json.loads(z.read('RESEARCH_SA12/CHECKPOINT_MANIFEST.json'))
 old_hash={v['path']:v['sha256'] for v in old['files']}
 old_sizes={i.filename.removeprefix('RESEARCH_SA12/'):i.compress_size for i in z.infolist()}
 upper=raw=unchanged=changed=0
 for p in sorted(root.rglob('*')):
  if not p.is_file() or p.suffix=='.zip' or '__pycache__' in p.parts or p.name=='CHECKPOINT_MANIFEST.json':continue
  rel=str(p.relative_to(root));data=pdf.read_bytes() if rel=='RESEARCH_SA12_paper.pdf' else p.read_bytes();raw+=len(data)
  if old_hash.get(rel)==hashlib.sha256(data).hexdigest():upper+=old_sizes[rel];unchanged+=1
  else:upper+=len(zlib.compress(data,6,wbits=-15));changed+=1
  upper+=256+2*len(('RESEARCH_SA12/'+rel).encode())
 upper+=3_000_000
assert upper<500_000_000,upper
prep=dict(utc=now,scheduled_archive_utc='2026-11-20T21:55:00+00:00',archive_created=False,
 size_method='Read-only per-file raw-DEFLATE calculation, unchanged member-size reuse, conservative header/manifest reserve; no ZIP created.',
 current_conservative_zip_bound_bytes=upper,current_raw_bytes=raw,unchanged_files=unchanged,changed_or_new_files=changed,
 remaining_below_cap_bytes=500_000_000-upper,verified_pdf=qa)
(root/'code/output/checkpoint29_preparation.json').write_text(json.dumps(prep,indent=2)+'\n')
print(json.dumps({k:v for k,v in prep.items() if k!='verified_pdf'},indent=2))
