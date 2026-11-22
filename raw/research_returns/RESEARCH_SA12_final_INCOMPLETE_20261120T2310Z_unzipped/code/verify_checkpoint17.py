"""Record actual final visual inspection and readiness; does not create a ZIP."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,zipfile,csv
root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
pdf=root/'build/RESEARCH_SA12_paper.pdf'
log=(root/'code/output/build_pass105.stdout.txt').read_text()
run=json.loads((root/'code/output/build_pass105.run.json').read_text())
assert run['returncode']==0
assert not any(s in log for s in ['Warning','Overfull','Missing character','undefined'])
render=json.loads((root/'qa/checkpoint17_render.json').read_text())
assert render['pdf_pages']==331 and len(render['rendered_pages'])==63
record={'utc':now,'build':'build_pass105','pages':331,'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
 'overfull_before':0,'overfull_after':0,'maximum_overfull_after_pt':0,'warnings_after':0,
 'undefined_citations_after':0,'undefined_references_after':0,'missing_characters_before':0,'missing_characters_after':0,
 'intermediate_build_errors':'Build101 stopped because tag D.IC.2 was inside split; the tag was moved without changing the mathematics. Build102 completed with zero overfull boxes. Bibliography25 succeeded. Builds103 and104 inadvertently overlapped for part of their execution; neither is used as the final verification. Both were confirmed finished before the isolated build105, which is clean and stable.',
 'rendered_and_inspected_pages':render['rendered_pages'],'individual_full_page_inspections':[288,300,307],
 'visual_outcome':'Root actually viewed all seven contact sheets at12:47--12:48UTC, covering63 pages: every new proof page288--308, preceding page287, updated unresolved discussion and bibliography through331, and an18-page spread. Root also viewed full-page images288,300,307 for the repaired cycle display, finite-jet equations and complete-local Brauer-zero theorem. No clipping, overlap, missing glyph or text outside margins was observed. The final isolated build105 log has zero warnings, overfull boxes, missing characters and undefined references/citations. Only this exact PDF hash is certified.'}
for name in ['qa/pdf_verified.json','qa/pdf_verified_checkpoint17.json']:
 (root/name).write_text(json.dumps(record,indent=2)+'\n')
with (root/'PROGRESS_LEDGER.md').open('a') as f:
 f.write('\n\n## Checkpoint17 paper verification completed\n\nINCOMPLETE. '+now+'. Isolated build105 has331pages, SHA256'+record['sha256']+'. Root actually viewed seven contact sheets covering63pages and full pages288,300,307. Final counts are zero warnings, overfull boxes, missing characters and unresolved citations/references. The intermediate tag error and accidental overlap of passes103/104 are explicitly recorded; only the subsequent isolated build105 is certified. There are330 assembled statements,1012central check events and57requested outcome rows. The17post16 units include one strict Brauer-zero main-gate reduction, with local/geometric/descent/selected-product closures; the cycle and framing estimates remain auxiliary. Separate post17 higher-dimensional local transfer and three sparse-DVR units are proved source outside the frozen manuscript. Review10 remains its actual historical no-movement review with counter1; review11 is due13:10UTC. Checkpoint17 is scheduled12:55UTC; no archive has yet been created.\n')
scope='''# Checkpoint17 scope

INCOMPLETE. Scheduled creation:20 November2026,12:55UTC. This checkpoint is a full current-work archive, excluding supplied input attachments and prior ZIPs.

The verified assembled manuscript is331pages, build105. It contains330statement records,1012central actual check events,57requested outcome rows and31finite-certificate programs in the inventory. All17new post16 statements are assembled. The one main reduction removes the scalar-order bound for geometric Brauer-zero projective representations on normal proper surfaces and complete normal local surfaces. Detecting-surface, finite-normalization and selected-simple-product results are closures of that same reduction. Integral cycles, RDP Hom/framing and finite jets are auxiliary and do not prove a hereditary object atlas.

The separate post17 local surface-transfer corollary and three sparse-DVR statements have complete four-actor audits and remain outside the frozen compiled manuscript and assembled statement table. Their source, audit records and exact scope are included. Sparse DVR charts do not control global coefficient poles or the constrained surface-extension locus. Further research notes retain their own candidate status.

General D.1, general D.2(ii) and residual L8 remain unresolved. The actual review10 at12:10UTC found no movement and recorded one consecutive no-movement review. The completed later Brauer-zero reduction will be compared at review11, scheduled13:10UTC; the older review has not been rewritten. Only a requested-row change or strict reduction of the strongest main gate counts as movement. Auxiliaries, closure consequences, recognition, repeated audits and packaging do not count.

The PDF log and visual inspection record are qa/pdf_verified_checkpoint17.json. Root actually viewed all seven63-page contact sheets and full pages288,300,307. Zero overfull boxes before and after the successful full builds; final zero warnings, missing characters and undefined references/citations. Build101's equation-tag error was repaired; accidental overlap of builds103/104 was superseded by the final isolated build105.

All previous checkpoints are immutable. The next scheduled checkpoint is13:40UTC. No checkpoint is created outside its scheduled slot.
'''
(root/'CHECKPOINT17_SCOPE.md').write_text(scope)
# Conservative size bound, without making an off-schedule trial archive.
previous=root.parent/'RESEARCH_SA12_checkpoint_16.zip'
with zipfile.ZipFile(previous) as z:
 old=json.loads(z.read('RESEARCH_SA12/CHECKPOINT_MANIFEST.json'))
 old_hash={x['path']:x['sha256'] for x in old['files']}
 sizes={x.filename.removeprefix('RESEARCH_SA12/'):x.compress_size for x in z.infolist()}
 upper=0;raw=0;unchanged=0;changed=0
 for p in root.rglob('*'):
  if not p.is_file() or p.suffix=='.zip' or '__pycache__' in p.parts:continue
  rel=str(p.relative_to(root));b=p.read_bytes();raw+=len(b)
  if old_hash.get(rel)==hashlib.sha256(b).hexdigest():upper+=sizes[rel];unchanged+=1
  else:upper+=len(b)+len(b)//1000+64;changed+=1
  upper+=256+2*len(('RESEARCH_SA12/'+rel).encode())
 upper+=2_000_000 # late audit files, updated manifest and receipt reserve
assert upper<500_000_000,upper
prep={'utc':now,'scheduled_archive_utc':'2026-11-20T12:55:00+00:00','archive_created':False,'current_conservative_zip_bound_bytes':upper,'current_raw_bytes':raw,'unchanged_files':unchanged,'changed_or_new_files':changed,'remaining_below_cap_bytes':500_000_000-upper,'verified_pdf':record}
(root/'code/output/checkpoint17_preparation.json').write_text(json.dumps(prep,indent=2)+'\n')
print(json.dumps({k:v for k,v in prep.items() if k!='verified_pdf'}))
