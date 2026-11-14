"""Remove runtime location strings from retained build diagnostics.

Only diagnostic logs and standard output are changed. Text, mathematics, line
numbers, warning measurements, and compilation outcomes are preserved.
"""
from pathlib import Path
import re,hashlib,csv
P=Path(__file__).resolve().parents[1]
root=P.parent
replacements=[(str(P),'PROJECT'),(str(root),'WORKSPACE'),(str(Path.home()),'AGENT'),('/'.join(['','usr','share']),'TEXSYSTEM'),('/'.join(['','tmp']),'TEMP')]
rows=[]
for p in sorted((P/'logs').iterdir()):
 if p.suffix not in {'.log','.stdout'}:continue
 before=p.read_text(errors='replace');s=before
 s=re.sub(r'<\s*(/[^>]+)>',lambda m:'<FONT:'+Path(m[1].replace('\n','')).name+'>',s,flags=re.S)
 for a,b in replacements:
  if a:s=re.sub(r'\s*'.join(re.escape(c) for c in a),b,s)
 s=re.sub(r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}','[address omitted]',s,flags=re.I)
 if s!=before:
  p.write_text(s)
  rows.append({'file':str(p.relative_to(P)),'before_sha256':hashlib.sha256(before.encode()).hexdigest(),'after_sha256':hashlib.sha256(s.encode()).hexdigest(),'reason':'Runtime absolute paths replaced by diagnostic root labels; embedded font paths reduced to font basenames; address strings redacted if present. Earlier immutable checkpoint archives are unchanged; this sanitized diagnostic supersedes their version.'})
f=P/'records/PRIVACY_REDACTIONS.tsv'
old=list(csv.DictReader(f.open(),delimiter='\t')) if f.exists() else []
if rows:
 with f.open('w',newline='') as out:
  w=csv.DictWriter(out,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(old+rows)
print({'sanitized_log_files':len(rows)})
