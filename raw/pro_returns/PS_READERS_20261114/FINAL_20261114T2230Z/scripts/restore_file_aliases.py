"""Restore duplicate image paths from verified byte-identical ZIP members."""
from pathlib import Path
import argparse,csv,hashlib,json,shutil
P=Path(__file__).resolve().parents[1]
def safe(relative):
 p=Path(relative)
 if p.is_absolute() or '..' in p.parts:raise ValueError('Unsafe relative alias path')
 result=(P/p).resolve();result.relative_to(P.resolve());return result
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
 a=argparse.ArgumentParser();a.add_argument('--verify-only',action='store_true');args=a.parse_args()
 table=P/'records/FILE_ALIASES.tsv';rows=list(csv.DictReader(table.open(),delimiter='\t'));restored=0
 for row in rows:
  target=safe(row['replacement']);destination=safe(row['path']);expected=row['sha256']
  assert target.is_file() and target.stat().st_size==int(row['bytes']) and sha(target)==expected,row['replacement']
  if destination.exists():assert destination.is_file() and sha(destination)==expected,row['path']
  elif not args.verify_only:
   destination.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(target,destination);assert sha(destination)==expected;restored+=1
 print(json.dumps({'verified_aliases':len(rows),'restored_paths':restored,'verify_only':args.verify_only}))
if __name__=='__main__':main()
