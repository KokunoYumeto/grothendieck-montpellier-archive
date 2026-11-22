"""Record the completed scheduled checkpoint; this does not create an archive."""
from pathlib import Path
from datetime import datetime, timezone
import json, time

R=Path(__file__).resolve().parents[1]
started=time.perf_counter()
p=R/'notes/checkpoint_saved_records.json'
d=json.loads(p.read_text())
name='RESEARCH_SA22_checkpoint_06.zip'
assert not any(x['name']==name for x in d['checkpoints'])
item=dict(name=name,saved_utc='2026-11-19T15:44:42+00:00',bytes=50079984,
    sha256='bed18f666f9214af18be8828d887a274917a295ce1d238c8130f979d4e201c0e',
    library_file_id='libfile_fde3_f-beb9db9fd2208191a31595200c6bafb3_3de54532f60c8191850458563edee173')
d['checkpoints'].append(item)
p.write_text(json.dumps(d,indent=2)+'\n')
entry='''

### Checkpoint06 saved 2026-11-19T15:44:42+00:00

The scheduled checkpoint due15:42:29UTC was created after the final current-build image review and saved as a new immutable ZIP:50,079,984bytes,1132files,SHA256 `bed18f666f9214af18be8828d887a274917a295ce1d238c8130f979d4e201c0e`. It contains the123-page build21,148 numbered statements,460check events,125 bibliography entries, and176 program files. Zero overfull boxes, undefined references/citations or missing characters remain. Eleven current-build pages were displayed directly; twenty current rendered images are byte-identical to previously displayed build20 pages, covering23distinct pages in total. The original-source metadata output files are now preserved as well as their hashes. Next checkpoint is due16:29:42UTC /17:29:42Europe/Berlin.

### Definition-scope issue identified immediately after checkpoint06

The independent A1 audit found that toric compatibility of two canonical cap circles alone does not force their hyperbolic boundary lengths to agree. The equal-length graph theorems explicitly impose the needed equality, but the definition-options sentence in `sections/part_a1_cut_choice.tex` is too broad. This is recorded as a live mathematical scope gap: prove the full independent-halfedge toric-seam map and its fibers, or narrow the stated interpretation with a complete explanation. An unequal-length two-pants example is being completed. It is not a refutation of the already stated equal-length graph-range theorem. The three original-source requirements remain open separately. No claim of global completion is made.
'''
with (R/'PROGRESS_LEDGER.md').open('a') as f:f.write(entry)
gap=dict(id='A1-toric-independent-lengths',opened_utc=datetime.now(timezone.utc).isoformat(),
    status='under proof audit',file='sections/part_a1_cut_choice.tex',
    claim='Toric cap compatibility alone licenses the equal-length geodesic range theorem.',
    issue='Unequal paired hyperbolic lengths are possible with toric boundary gluing.',
    gate='Prove the exact independent-halfedge radius-projection image and fibers, and qualify the geodesic interpretation.',
    affects=['A.1 definition choices','A1-nontoric-cut scope sentence'])
(R/'notes/live_mathematical_scope_gaps.json').write_text(json.dumps([gap],indent=2)+'\n')
out=dict(**item,recorded_utc=datetime.now(timezone.utc).isoformat(),seconds=time.perf_counter()-started)
(R/'code/root_checkpoint06_receipt_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
