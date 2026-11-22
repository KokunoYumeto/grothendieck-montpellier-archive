"""Preserve the successful preparation build before the final bibliography build."""
from pathlib import Path
import datetime, hashlib, json, shutil, time
root = Path(__file__).resolve().parents[1]
started = time.perf_counter()
copied = []
for relative in ['logs/build_01.txt', 'logs/build_02.txt', 'logs/build_03.txt',
                 'logs/build_04.txt', 'logs/build_diagnostics.json',
                 'RESEARCH_SA23_paper.log', 'RESEARCH_SA23_paper.bbl']:
    source = root / relative
    target = root / 'logs' / ('build_checkpoint04_preparation02_' + source.name)
    if target.exists():
        raise SystemExit('Refusing to overwrite retained preparation output: ' + str(target))
    shutil.copyfile(source, target)
    copied.append({'source': relative, 'saved': str(target.relative_to(root)),
                   'sha256': hashlib.sha256(target.read_bytes()).hexdigest()})
record = {'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'preserved_outputs': copied,
          'reason': 'Three newly added documentary bibliography entries and observed prose spacing are being incorporated. Mathematical statements are unchanged.',
          'elapsed_seconds': time.perf_counter() - started}
(root / 'logs/root_checkpoint04_final_prepare.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
