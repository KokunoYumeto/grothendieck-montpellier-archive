"""Preserve a reused run name and restore its earlier evidence from checkpoint06."""
from pathlib import Path
from zipfile import ZipFile
import json

root = Path(__file__).resolve().parents[1]
output = root / 'code/output'
old_stem = 'bibliography_pass8'
new_stem = 'bibliography_post06_lc'
archive = root.parent / 'RESEARCH_SA12_checkpoint_06.zip'
restored = []
with ZipFile(archive) as z:
    for suffix in ['.run.json', '.stdout.txt', '.stderr.txt']:
        old = output / (old_stem + suffix)
        new = output / (new_stem + suffix)
        if new.exists():
            raise SystemExit('Refusing to overwrite the preserved current run.')
        new.write_bytes(old.read_bytes())
        old.write_bytes(z.read('RESEARCH_SA12/code/output/' + old_stem + suffix))
        restored.append(str(old.relative_to(root)))
record = {'preserved_current_run': new_stem, 'restored_earlier_run': old_stem,
          'source_archive_read_only': archive.name, 'restored_files': restored,
          'note': 'The exact current command/output is preserved; its original printed log stem remains in that output. No checkpoint archive was changed.'}
(output / 'bibliography_run_name_repair.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
