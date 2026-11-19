"""Check the archive manifest, required members, CRCs and record counts."""
from pathlib import Path
import argparse,csv,hashlib,io,json,zipfile
p=argparse.ArgumentParser();p.add_argument('archive');p.add_argument('--output');a=p.parse_args()
archive=Path(a.archive);issues=[]
with zipfile.ZipFile(archive) as z:
 bad=z.testzip()
 if bad:issues.append('CRC failure: '+bad)
 manifest=json.loads(z.read('ARCHIVE_MANIFEST.json'))
 names=set(z.namelist())
 for f in manifest['files']:
  data=z.read(f['path'])
  if len(data)!=f['bytes'] or hashlib.sha256(data).hexdigest()!=f['sha256']:issues.append('Manifest mismatch: '+f['path'])
 if names!={f['path'] for f in manifest['files']}|{'ARCHIVE_MANIFEST.json'}:issues.append('Unmanifested member')
 required=['SA13_dossier.md','SA13_entries.tsv','SA13_items.json','SA13_claims.json','SA13_problems.json','SA13_readings.tsv','SA13_links.tsv','SA13_directions.md','SA13_references.bib','CHECK_EVENTS.tsv','progress.log']
 for n in required:
  if n not in names:issues.append('Missing required member: '+n)
 entries=list(csv.DictReader(io.StringIO(z.read('SA13_entries.tsv').decode()),delimiter='\t'))
 if len(entries)!=379 or len({e['entry_id'] for e in entries})!=379:issues.append('Invalid entry coverage')
 if any(n.endswith('.zip') for n in names):issues.append('Nested attachment or checkpoint ZIP')
 final=json.loads(z.read('outputs/final_validation.json'))
 if not final['passed']:issues.append('Final validation not passed')
 report={'archive':archive.name,'bytes':archive.stat().st_size,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'manifest_files_checked':len(manifest['files']),'required_files':len(required),'entries':len(entries),'record_counts':final['checks'],'passed':not issues,'issues':issues}
text=json.dumps(report,indent=2)+'\n'
if a.output:Path(a.output).write_text(text)
print(text)
if issues:raise SystemExit(1)
