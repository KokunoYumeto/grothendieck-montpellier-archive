"""Create one immutable research checkpoint. Invoke only at the scheduled interval."""
from pathlib import Path
import hashlib,json,sys,zipfile
ROOT=Path(__file__).resolve().parents[1]
final_mode=sys.argv[1]=='final'
if final_mode:
    review=json.loads((ROOT/'notes/progress_review_state.json').read_text())
    assert review['no_movement_streak']>=2, 'Final delivery is not yet authorized by the scheduled stopping rule.'
    target=ROOT.parent/'RESEARCH_SA22_final.zip'
    contents_name='FINAL_CONTENTS.txt'
else:
    number=int(sys.argv[1])
    target=ROOT.parent/f'RESEARCH_SA22_checkpoint_{number:02d}.zip'
    contents_name='CHECKPOINT_CONTENTS.txt'
if target.exists():raise RuntimeError('Never overwrite a checkpoint')
manifest=[]
for p in sorted((ROOT/'sources').rglob('*')):
    if p.is_file():
        manifest.append(dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,
                       sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
source_plan_path=ROOT/'checks'/'part_c_source_cache_plan.json'
extra_source_caches={}
if source_plan_path.exists():
    source_plan=json.loads(source_plan_path.read_text())
    for item in source_plan['direct_exclusions']:
        p=ROOT/item['path']
        assert p.is_file(), 'A named source cache is missing: '+item['path']
        digest=hashlib.sha256(p.read_bytes()).hexdigest()
        assert digest==item['sha256'], 'A named source cache changed after review: '+item['path']
        extra_source_caches[item['path']]=item
        manifest.append(dict(path=item['path'],bytes=p.stat().st_size,sha256=digest,
            cache_scope='Raw non-user literature/index cache outside sources/',reason=item['reason']))
(ROOT/'notes'/'public_source_cache_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
included=[]
for p in sorted(ROOT.rglob('*')):
    if not p.is_file():continue
    rel=p.relative_to(ROOT)
    if rel.as_posix()==contents_name:continue
    if rel.as_posix() in extra_source_caches:continue
    if '__pycache__' in rel.parts or 'tex-runtime' in rel.parts:continue
    # Preserve source-acquisition output/provenance as well as bibliography fragments.
    # Full literature/scans/OCR remain a reproducible cache, outside the deliverable.
    if rel.parts[0]=='sources' and p.suffix not in {'.bib','.json','.csv','.tsv','.out','.log','.ris'}:continue
    if rel.parts[0]=='qa' and not p.name.startswith('paper'):continue
    if p.suffix in {'.zip','.fmt'}:continue
    included.append(p)
(ROOT/contents_name).write_text(
    '\n'.join(str(p.relative_to(ROOT)) for p in included)+'\n'+contents_name+'\n')
included.append(ROOT/contents_name)
with zipfile.ZipFile(target,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in included:z.write(p,'RESEARCH_SA22/'+str(p.relative_to(ROOT)))
with zipfile.ZipFile(target) as z:
    assert z.testzip() is None, 'New archive failed its integrity check'
if target.stat().st_size>=500_000_000:raise RuntimeError('Archive exceeds user limit')
print(json.dumps(dict(path=str(target),files=len(included),bytes=target.stat().st_size,
                     sha256=hashlib.sha256(target.read_bytes()).hexdigest())))
