"""Open the held-back attachment only after freezing the complete entry."""
from pathlib import Path
from datetime import datetime,timezone
import zipfile

root=Path(__file__).resolve().parents[2]
work=root/'OBJ_H035_work'
assert (work/'ENTRY.md').is_file() and (work/'research/ENTRY_BEFORE_RESULTS.md').is_file()
assert not (root/'sources/OBJ_H035_results').exists(), 'Results were already opened.'
stamp=datetime.now(timezone.utc).isoformat()
with (work/'progress.log').open('a') as stream:
    stream.write('results opened '+stamp+'\n')
print('results opened',stamp,flush=True)
dest=(root/'sources/OBJ_H035_results').resolve();dest.mkdir()
with zipfile.ZipFile(root/'upload/OBJ_H035_results.zip') as archive:
    for info in archive.infolist():
        target=(dest/info.filename).resolve()
        if not target.is_relative_to(dest):raise ValueError('unsafe ZIP path')
        print(info.filename,info.file_size)
        if info.is_dir():target.mkdir(parents=True,exist_ok=True)
        else:
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_bytes(archive.read(info))
