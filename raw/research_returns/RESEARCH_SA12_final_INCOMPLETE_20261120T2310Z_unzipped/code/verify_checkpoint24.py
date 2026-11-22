"""Record completed actual image inspection and CP24 readiness; creates no ZIP."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,sys,zipfile,re
root=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
build=sys.argv[1];pdf=root/'build/RESEARCH_SA12_paper.pdf'
log=(root/f'code/output/{build}.stdout.txt').read_text();run=json.loads((root/f'code/output/{build}.run.json').read_text())
assert run['returncode']==0
assert not any(s in log for s in ['Warning','Missing character','undefined'])
overfull=[float(x) for x in re.findall(r'Overfull \\hbox \(([0-9.]+)pt too wide\)',log)]
assert max(overfull,default=0)<=2.0
initial_log=(root/'code/output/build_pass155.stdout.txt').read_text()
initial_overfull=[float(x) for x in re.findall(r'Overfull \\hbox \(([0-9.]+)pt too wide\)',initial_log)]
render=json.loads((root/'qa/checkpoint24_render.json').read_text())
inspection=json.loads((root/'qa/checkpoint24_actual_inspection.json').read_text())
sha=hashlib.sha256(pdf.read_bytes()).hexdigest();assert inspection['pdf_sha256']==sha
assert inspection['rendered_pages']==render['rendered_pages']
assert len(inspection['contact_sheets_viewed'])==(len(render['rendered_pages'])+8)//9
assert inspection['actual_image_output_observed'] is True
record=dict(utc=now,build=build,pages=render['pdf_pages'],sha256=sha,
 overfull_before=len(initial_overfull),maximum_overfull_before_pt=max(initial_overfull,default=0),
 overfull_after=len(overfull),maximum_overfull_after_pt=max(overfull,default=0),warnings_after=0,
 undefined_citations_after=0,undefined_references_after=0,missing_characters_after=0,
 rendered_and_inspected_pages=render['rendered_pages'],individual_full_page_inspections=inspection['full_pages_viewed'],
 image_format='lossless WebP',lossless_pixel_roundtrip_checks=len(render['lossless_pixel_roundtrip_checks']),
 actual_inspection_record='qa/checkpoint24_actual_inspection.json',visual_outcome=inspection['visual_outcome'],
 intermediate_build_notes='Only the final exact hash certified here is delivered. All bibliography and LuaLaTeX passes are sequential; intermediate warnings and their resolutions remain in the logs.')
for name in ['qa/pdf_verified.json','qa/pdf_verified_checkpoint24.json']:(root/name).write_text(json.dumps(record,indent=2)+'\n')
with (root/'RESEARCH_SA12_results.csv').open() as f:nrows=sum(1 for _ in csv.DictReader(f))
with (root/'CHECK_EVENTS.tsv').open() as f:nevents=sum(1 for _ in csv.DictReader(f,delimiter='\t'))
with (root/'PROGRESS_LEDGER.md').open('a') as f:
 f.write('\n\n## Checkpoint24 paper verification completed\n\nINCOMPLETE. '+now+'. Final '+build+' has '+str(render['pdf_pages'])+'pages, SHA256 '+sha+'. Root actually viewed '+str(len(inspection['contact_sheets_viewed']))+' contact sheets covering '+str(len(render['rendered_pages']))+' pages and full pages '+', '.join(map(str,inspection['full_pages_viewed']))+'. Final build has zero warnings and undefined citations/references; overfull boxes before/after:'+str(len(initial_overfull))+'/'+str(len(overfull))+', maximum final overflow:'+str(max(overfull,default=0))+'pt (required limit2pt). There are '+str(nrows)+' statement rows and '+str(nevents)+' actual central check events. This verification is not research movement and creates no ZIP. Review15 recorded two strict main-gate reductions, each counted once; review16 is due18:10UTC. Checkpoint24 is scheduled18:10UTC.\n')
scope='''# Checkpoint24 scope

INCOMPLETE. Scheduled creation:20 November2026,18:10UTC, after formal review16 at the same scheduled time. This full archive contains all current deliverables and accumulated documentation, excluding original supplied attachments and earlier ZIPs.

The verified manuscript has {pages}pages, final {build}, SHA256 {sha}, {rows}statement rows and {events}actual central check events. Newly assembled units and exact hashes are recorded in code/output/integrate_post19_post23*.json. Research files not assembled retain their explicit individual status.

The global finite-puncture unrestricted-PGL theorem and its fixed-curve, dimensional, normalization and defining-characteristic simple-product consequences are proved. A separate restricted alternating factorial bound, with fixed finitely generated local quotient control, is proved in its exact stated scope. Further developments are described in the report and the exact formal-review assessment. General D.1, general D.2(ii), and residual L8 remain open. Only a completed requested-row change or a strictly smaller strongest main gate can reset the stopping counter; prerequisites, closures, searches, audits and packaging are not counted independently.

Formal review16 is executed before this checkpoint is created. Its completed record, comparison with review15 and stopping counter are in code/output/formal_review16.json; review15 was the latest completed review when this PDF verification was staged. The next scheduled checkpoint after this one is18:55UTC.

The final PDF has zero warnings, missing characters and undefined citations/references. Overfull boxes before/after:{before}/{after}; maximum final overflow:{overflow}pt, within the2pt limit. Actual image inspection is recorded in qa/checkpoint24_actual_inspection.json and qa/pdf_verified_checkpoint24.json. New inspection images use lossless WebP with exact RGB round-trip checks. Historical contact sheets and individual pages retain every decoded pixel; old/current paths and hashes are in qa/historical_contact_encoding_map.json and qa/historical_page_encoding_map.json. Earlier immutable archives retain their original bytes. Only the exact certified PDF hash is delivered.
'''.format(pages=render['pdf_pages'],build=build,sha=sha,rows=nrows,events=nevents,before=len(initial_overfull),after=len(overfull),overflow=max(overfull,default=0))
(root/'CHECKPOINT24_SCOPE.md').write_text(scope)
previous=root.parent/'RESEARCH_SA12_checkpoint_23.zip'
with zipfile.ZipFile(previous) as z:
 old=json.loads(z.read('RESEARCH_SA12/CHECKPOINT_MANIFEST.json'));old_hash={x['path']:x['sha256'] for x in old['files']};sizes={x.filename.removeprefix('RESEARCH_SA12/'):x.compress_size for x in z.infolist()}
 upper=0;raw=0;unchanged=0;changed=0
 for p in root.rglob('*'):
  if not p.is_file() or p.suffix=='.zip' or '__pycache__' in p.parts:continue
  rel=str(p.relative_to(root));b=pdf.read_bytes() if rel=='RESEARCH_SA12_paper.pdf' else p.read_bytes();raw+=len(b)
  if old_hash.get(rel)==hashlib.sha256(b).hexdigest():upper+=sizes[rel];unchanged+=1
  else:upper+=len(b)+len(b)//1000+64;changed+=1
  upper+=256+2*len(('RESEARCH_SA12/'+rel).encode())
 upper+=3_000_000
assert upper<500_000_000,upper
prep=dict(utc=now,scheduled_archive_utc='2026-11-20T18:10:00+00:00',archive_created=False,current_conservative_zip_bound_bytes=upper,current_raw_bytes=raw,unchanged_files=unchanged,changed_or_new_files=changed,remaining_below_cap_bytes=500_000_000-upper,verified_pdf=record)
(root/'code/output/checkpoint24_preparation.json').write_text(json.dumps(prep,indent=2)+'\n')
print(json.dumps({k:v for k,v in prep.items() if k!='verified_pdf'},indent=2))
