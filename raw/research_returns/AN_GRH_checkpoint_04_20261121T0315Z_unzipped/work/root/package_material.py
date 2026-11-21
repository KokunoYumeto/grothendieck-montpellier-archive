from pathlib import Path
import csv, shutil, json
base=Path('/workspace/scratch/63b175cc138c')
out=base/'final'
def copy(src,dst):
 src=base/src if not Path(src).is_absolute() else Path(src)
 dst=out/dst
 dst.parent.mkdir(parents=True,exist_ok=True)
 shutil.copy2(src,dst)
# Exact requested/source-audit tables, plus concise working documentation.
for p in (base/'work/row_audit').glob('*.tsv'):copy(p,p.name)
for n in ['ROW_AUDIT_NOTES.md','inventory.json','LIBRARY_RECOVERY_FINAL_SEARCHES.json','LIBRARY_RECOVERY_RESULTS.json']:
 p=base/'work/row_audit'/n
 if p.exists():copy(p,Path('evidence')/n)
for n in ['GT_LEVEL_SCOPE.tsv','GT_UNIT_CERTIFICATES.tsv','GT_UNIT_WORDS.tsv']:
 copy(Path('work/gt_certificates')/n,n)
for n in ['verify_gt_units.py','check_unit_certificates.py']:
 copy(Path('work/gt_certificates')/n,Path('certificates/gt')/n)
# Scripts use their own folder for data.
for n in ['GT_UNIT_CERTIFICATES.tsv','GT_UNIT_WORDS.tsv']:
 copy(Path('work/gt_certificates')/n,Path('certificates/gt')/n)
copy('work/gt_certificates/GT_NOTES.md','evidence/GT_NOTES.md')
for n in ['check_theta_obstruction.py','check_theta_obstruction.out','check_b23_geometry.py','check_b23_geometry.out']:
 copy(Path('work/root')/n,Path('certificates/A06')/n)
copy('work/effective_galois/check_a06_prime_orbit.py','certificates/A06/check_a06_prime_orbit_independent.py')
copy('work/effective_galois/A06_prime_orbit_result.json','certificates/A06/A06_prime_orbit_result.json')
copy('work/row_audit/verify_theta_small_independent.py','certificates/A06/verify_theta_small_independent.py')
copy('work/row_audit/theta_small_independent.out','certificates/A06/theta_small_independent.out')
for n in ['primitive_conductors.py','primitive_conductors.json','primitive_conductors.out','primitive_verify.py','primitive_verify.json','primitive_verify.out','primitive_191_229.py','conductor_recheck.out','bezout_recheck.out']:
 p=base/'work/row_audit/B23_recheck'/n
 if p.exists():copy(p,Path('certificates/B23')/n)
for p in (base/'work/row_audit/B23_recheck/primitive_certificates').iterdir():
 if p.is_file():copy(p,Path('certificates/B23/primitive_certificates')/p.name)
for p in (base/'work/effective_galois').glob('*.md'):copy(p,Path('evidence/proof_checks')/p.name)
for n in ['A1_reductions_notes.md','source_manifest.tsv']:
 copy(Path('work/root')/n,Path('evidence')/n)
# Event fragments are retained exactly; the combined required TSV normalizes headers.
copy('final/CHECK_EVENTS.tsv','evidence/check_events/root_initial.tsv')
for p in (base/'work/gt_certificates').glob('CHECK_EVENTS*.tsv'):copy(p,Path('evidence/check_events')/p.name)
copy('work/effective_galois/CHECK_EVENTS.tsv','evidence/check_events/CHECK_EVENTS_GALOIS.tsv')
copy('work/row_audit/ROW_CHECK_EVENTS.tsv','evidence/check_events/ROW_CHECK_EVENTS.tsv')
# Retain only the exact relevant textual provenance, never giant source archives.
manifest=list(csv.DictReader(open(base/'work/row_audit/SOURCE_RECOVERY_MANIFEST.tsv'),delimiter='\t'))
for r in manifest:
 key=next((k for k in r if 'local' in k and 'path' in k),None)
 if not key:key=next((k for k in r if 'path' in k),None)
 if not key:continue
 rel=Path(r[key])
 p=base/rel
 if p.exists() and p.is_file() and p.suffix!='.zip':copy(p,rel)
for p in (base/'source').iterdir():
 if p.is_file() and p.suffix.lower() in {'.tex','.md','.tsv','.lean'}:copy(p,Path('source')/p.name)
for n in ['pbc_level4.py','pbc_resolvents.py','pbc_cm_frames_24_60.py']:
 p=base/'recovered/LM8_PUSH_cp17_text/code'/n
 if p.exists():copy(p,p.relative_to(base))
# The root file inventory is useful if this package is resumed in another workspace.
print('Copied',len([p for p in out.rglob('*') if p.is_file()]),'files; bytes',sum(p.stat().st_size for p in out.rglob('*') if p.is_file()))
