"""Create a scheduled immutable archive; do not invent proof or check records."""
from pathlib import Path
import argparse, csv, datetime, hashlib, json, zipfile
root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('number', type=int)
number = parser.parse_args().number
stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
dest = root.parent / f'RESEARCH_SA23_checkpoint_{number:02d}.zip'
if dest.exists(): raise SystemExit('Refusing to overwrite an earlier checkpoint')
history_path = root / 'checkpoint_history.json'
history = json.loads(history_path.read_text()) if history_path.exists() else []
if history and number != max(x['checkpoint'] for x in history) + 1:
    raise SystemExit('Checkpoint numbers must be consecutive')
included, omitted = [], []
for path in sorted(root.rglob('*')):
    rel = path.relative_to(root)
    if rel.parts[0] == 'runtime' or '__pycache__' in rel.parts: continue
    if not path.is_file() or rel.name == 'checkpoint_manifest.json': continue
    source_cache = (rel.parts[0] == 'sources'
        or (rel.parts[0] == 'notes' and path.suffix == '.pdf')
        or (rel.parts[0] == 'notes' and 'web_' in path.name and path.suffix == '.json')
        or (rel.parts[0] == 'verification' and 'scan' in path.name))
    if path.suffix == '.zip' or source_cache or path.suffix in {'.aux','.toc','.out'}:
        omitted.append({'path':str(rel),'bytes':path.stat().st_size,
                        'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    else: included.append(path)
manifest = {'created_utc':stamp,'checkpoint':number,
    'included':[str(x.relative_to(root)) for x in included]+['checkpoint_manifest.json'],
    'omitted_retrievable_caches':omitted,
    'omitted_runtime':'runtime/: recreate using code/setup_lualatex.py; package hashes and extraction logs retained',
    'earlier_checkpoints':history,
    'original_inputs':'Use the original attachment; extracted inputs are not copied into checkpoints'}
manifest_path = root/'checkpoint_manifest.json'
manifest_path.write_text(json.dumps(manifest,indent=2)+'\n')
included.append(manifest_path)
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as archive:
    for path in included: archive.write(path,Path('RESEARCH_SA23')/path.relative_to(root))
if dest.stat().st_size >= 500_000_000:
    raise SystemExit('Archive exceeds 500 MB; do not deliver')
with (root/'RESEARCH_SA23_results.csv').open() as f:
    statement_rows = sum(1 for _ in csv.DictReader(f))
result = {'checkpoint':number,'file':str(dest),'bytes':dest.stat().st_size,
    'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'files':len(included),
    'statement_rows':statement_rows,'created_utc':stamp}
history.append(result)
history_path.write_text(json.dumps(history,indent=2)+'\n')
print(json.dumps(result))
