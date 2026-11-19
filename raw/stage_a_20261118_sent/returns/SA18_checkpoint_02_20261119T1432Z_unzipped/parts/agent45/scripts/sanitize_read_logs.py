"""Replace duplicated attached passages with a range/hash audit manifest.

The tool reads were performed and their outputs inspected. The final deliverable
must not copy the attached sources. These log files are therefore represented by
their original filenames, byte counts and content hashes, not the source text.
"""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1]
out=root/'outputs'
manifest=out/'source_read_manifest.json'
records=json.loads(manifest.read_text()) if manifest.exists() else []
for p in sorted(out.glob('read_*.txt')):
    data=p.read_bytes()
    records.append({'original_read_log':p.name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'disposition':'Source-content duplicate removed; original attached source and range encoded by filename remain the authoritative endpoint.'})
    p.unlink()
manifest.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'recorded_read_outputs':len(records),'remaining_source_copy_logs':len(list(out.glob('read_*.txt')))}))
