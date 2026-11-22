"""Retain the successful ordered Library result without rewriting its archive."""
from pathlib import Path
import datetime, json, time
root = Path(__file__).resolve().parents[1]
started = time.perf_counter()
receipt = {
    'local_path': '/workspace/scratch/a7ef7e55112c/RESEARCH_SA23_checkpoint_04.zip',
    'purpose': 'create_library_file', 'status': 'succeeded',
    'file_id': 'file_000000007be88210ae99402931c08a2b',
    'library_file_id': 'libfile_3bd07d87a42c8191a0c88d8071a70afe',
    'file_name': 'RESEARCH_SA23_checkpoint_04.zip',
    'local_metadata_applied': True, 'path': '/RESEARCH_SA23_checkpoint_04.zip',
    'current_version_number': 0,
}
history_path = root / 'checkpoint_history.json'
history = json.loads(history_path.read_text())
entry = next(item for item in history if item['checkpoint'] == 4)
assert entry['bytes'] == 204763895
assert entry['sha256'] == '82a4d5b70fbb6b4467588ca1b9736d34f87edd6a9a9c18c14237e665884516d4'
assert Path(receipt['local_path']).stat().st_size == entry['bytes']
entry.update({key: receipt[key] for key in ['file_id', 'library_file_id',
                                          'current_version_number', 'local_metadata_applied']})
history_path.write_text(json.dumps(history, indent=2) + '\n')
record = {'recorded_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'ordered_results': [receipt], 'archive_unchanged': True,
          'elapsed_seconds': time.perf_counter() - started}
(root / 'logs/root_checkpoint04_receipt.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
