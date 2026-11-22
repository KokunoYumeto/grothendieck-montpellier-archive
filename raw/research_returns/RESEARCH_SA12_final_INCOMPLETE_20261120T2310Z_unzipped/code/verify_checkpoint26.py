"""Certify completed actual image inspection for CP26; create no archive."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,re,sys,zipfile
root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
build=sys.argv[1]
pdf=root/'build/RESEARCH_SA12_paper.pdf'
log=(root/f'code/output/{build}.stdout.txt').read_text()
run=json.loads((root/f'code/output/{build}.run.json').read_text())
assert run['returncode']==0
assert not any(s in log for s in ['Warning','Missing character','undefined'])
overflow=lambda s:[float(x) for x in re.findall(r'Overfull \\hbox \(([0-9.]+)pt too wide\)',s)]
after=overflow(log)
before=overflow((root/'code/output/build_pass165.stdout.txt').read_text())
assert max(after,default=0)<=2.0
render=json.loads((root/'qa/checkpoint26_render.json').read_text())
inspection=json.loads((root/'qa/checkpoint26_actual_inspection.json').read_text())
sha=hashlib.sha256(pdf.read_bytes()).hexdigest()
assert inspection['pdf_sha256']==sha
assert inspection['rendered_pages']==render['rendered_pages']
assert len(inspection['contact_sheets_viewed'])==(len(render['rendered_pages'])+8)//9
assert inspection['actual_image_output_observed'] is True
record=dict(utc=now,build=build,pages=render['pdf_pages'],sha256=sha,
 overfull_before=len(before),maximum_overfull_before_pt=max(before,default=0),
 overfull_after=len(after),maximum_overfull_after_pt=max(after,default=0),
 warnings_after=0,undefined_citations_after=0,undefined_references_after=0,
 missing_characters_after=0,
 rendered_and_inspected_pages=sorted(set(render['rendered_pages'])|set(inspection['full_pages_viewed'])),
 individual_full_page_inspections=inspection['full_pages_viewed'],
 image_format='lossless WebP',lossless_pixel_roundtrip_checks=len(render['lossless_pixel_roundtrip_checks']),
 actual_inspection_record='qa/checkpoint26_actual_inspection.json',
 visual_outcome=inspection['visual_outcome'],
 intermediate_build_notes='The before count is the actual first post25 build165. The shared quantifier in D.CR.6 was moved to its own gathered row with exact reversal recorded. Only the final exact PDF hash is certified. All bibliography and LuaLaTeX passes are sequential.')
for name in ['qa/pdf_verified.json','qa/pdf_verified_checkpoint26.json']:
 (root/name).write_text(json.dumps(record,indent=2)+'\n')
with (root/'RESEARCH_SA12_results.csv').open() as f:rows=sum(1 for _ in csv.DictReader(f))
with (root/'CHECK_EVENTS.tsv').open() as f:events=sum(1 for _ in csv.DictReader(f,delimiter='\t'))
review=json.loads((root/'code/output/formal_review17.json').read_text())
assert review['consecutive_no_movement_reviews']==0 and not review['stopping_condition_met']
with (root/'PROGRESS_LEDGER.md').open('a') as f:
 f.write('\n\n## Checkpoint26 paper verification completed\n\nINCOMPLETE. '+now+'. Final '+build+' has '+str(render['pdf_pages'])+'pages, SHA256 '+sha+'. Root actually viewed '+str(len(inspection['contact_sheets_viewed']))+' contact sheets covering '+str(len(render['rendered_pages']))+' pages and full pages '+', '.join(map(str,inspection['full_pages_viewed']))+'. Final build has zero warnings and undefined citations/references; overfull boxes before/after:'+str(len(before))+'/'+str(len(after))+', maximum final overflow:'+str(max(after,default=0))+'pt (required limit2pt). There are '+str(rows)+' statement rows and '+str(events)+' actual central check events. This verification is not research movement and creates no ZIP. Review17 recorded one strict enlarged alternating criterion, counted once; review18 is due20:10UTC. Checkpoint26 is scheduled19:40UTC.\n')
scope=f'''# Checkpoint26 scope

INCOMPLETE. Scheduled creation:20 November2026,19:40UTC. This full archive contains the current deliverables and accumulated documentation, excluding original supplied attachments and earlier ZIPs. It performs no unscheduled formal review.

The verified manuscript has {render['pdf_pages']}pages, final {build}, SHA256 {sha}, {rows}statement rows and {events}actual central check events. Newly assembled units and exact historical integration hashes are recorded in code/output/integrate_post19_post25*.json. Subsequent typography-only hashes and exact reversals are recorded in the relevant source manifests. Research files not assembled retain their explicit individual status.

The post25 additions include the strict separating parameter pencil and uniformly comparable strong reduction cycles C<=Z<=alpha C on the specified relative-minimal models, with degree-linear numerical budgets. The intrinsic integral unit-jet theorem gives exact finite equations and effectivity for actual bounded-pole families. The simultaneous finite Frobenius object construction retains a lower jet and its specified generating quotient; generated fixed-determinant comparison gives clopen unit classes even for the noncanonical constructed families.

The ordinary synthesis now proves q^(A_R t r^2) GL_r(F_q)-conjugacy classes on every connected degree-t punctured cover of a fixed complete excellent normal local surface, without a tameness condition. It uses O(f t r^2) coordinates and equations of uniformly bounded degree and one generating open locus per fixed determinant tuple. No coflat rank stratum or quantitative comparison-scheme bound is needed. Its faithful-linear crown consequence permits arbitrary permutation quotients, with the stated bounded residual outer index and quadratic order comparison; the generator bound retains d(P). The semilinear extension permits every prescribed field character, including wild field-cover order. Its direct graph/Jacobian scalar estimate and equivariant same-model cycles give the exact cancellation (f/d)(td)=ft. These results and their prerequisites form one concrete controlled-crown/counting enlargement for the next scheduled formal review. The supporting statements are not separate movements. Twisted projective determinant enumeration and arbitrary-cover projective counts remain outside this proved scope.

The second enlarged criterion replaces whole-local orbit squares by minimum weighted tower energy in the finite-puncture setting. Exact nonsimple Shapiro controls arbitrary-height towers of qualifying primitive matrix models, charging only unrestricted levels by sum(T_i m_i^2). The one-level unrestricted certificate recovers the previous square-sum condition. This is one restricted-alternating enlargement, with the stated dimensional and finite-normalization consequences; it does not establish hereditary original-divisorial local-pair counting or unrestricted alternating multiplicities.

The enlarged restricted-alternating criterion and the fixed-pair/global original-boundary projective counts retain their exact proved scopes. General D.1, general D.2(ii), unrestricted alternating multiplicities, general uncovered crowns and dependent residual L8 remain unresolved. Review17 at19:10UTC recorded one strict enlargement of the alternating criterion since review16 and no requested status change. Its consecutive no-movement counter is zero. Review18 is due20:10UTC; the next scheduled checkpoint is20:25UTC. Only a completed requested-row change or a strictly smaller strongest main gate can reset the stopping counter; prerequisites, closures, searches, audits and packaging are not counted independently.

The final PDF has zero warnings, missing characters and undefined citations/references. Overfull boxes before/after:{len(before)}/{len(after)}; maximum final overflow:{max(after,default=0)}pt, within the2pt limit. Actual image inspection is recorded in qa/checkpoint26_actual_inspection.json and qa/pdf_verified_checkpoint26.json. New inspection images use lossless WebP with exact RGB round-trip checks. Historical inspection records and lossless encoding maps remain included; earlier immutable archives retain their original bytes. Only the exact certified PDF hash is delivered.
'''
(root/'CHECKPOINT26_SCOPE.md').write_text(scope)
with zipfile.ZipFile(root.parent/'RESEARCH_SA12_checkpoint_25.zip') as z:
 old=json.loads(z.read('RESEARCH_SA12/CHECKPOINT_MANIFEST.json'))
 old_hash={x['path']:x['sha256'] for x in old['files']}
 sizes={x.filename.removeprefix('RESEARCH_SA12/'):x.compress_size for x in z.infolist()}
 upper=0;raw=0;unchanged=0;changed=0
 for p in root.rglob('*'):
  if not p.is_file() or p.suffix=='.zip' or '__pycache__' in p.parts:continue
  rel=str(p.relative_to(root))
  b=pdf.read_bytes() if rel=='RESEARCH_SA12_paper.pdf' else p.read_bytes()
  raw+=len(b)
  if old_hash.get(rel)==hashlib.sha256(b).hexdigest():
   upper+=sizes[rel];unchanged+=1
  else:
   upper+=len(b)+len(b)//1000+64;changed+=1
  upper+=256+2*len(('RESEARCH_SA12/'+rel).encode())
 upper+=3_000_000
assert upper<500_000_000,upper
prep=dict(utc=now,scheduled_archive_utc='2026-11-20T19:40:00+00:00',archive_created=False,
 current_conservative_zip_bound_bytes=upper,current_raw_bytes=raw,
 unchanged_files=unchanged,changed_or_new_files=changed,
 remaining_below_cap_bytes=500_000_000-upper,verified_pdf=record)
(root/'code/output/checkpoint26_preparation.json').write_text(json.dumps(prep,indent=2)+'\n')
print(json.dumps({k:v for k,v in prep.items() if k!='verified_pdf'},indent=2))
