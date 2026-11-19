"""Create a scheduled checkpoint without sources, caches, or earlier ZIPs."""
import argparse
import hashlib
import json
import zipfile
from datetime import datetime,timezone
from pathlib import Path

parser=argparse.ArgumentParser();parser.add_argument('--number',type=int,required=True)
parser.add_argument('--due',required=True);args=parser.parse_args()
due=datetime.fromisoformat(args.due).astimezone(timezone.utc)
now=datetime.now(timezone.utc)
assert now>=due, 'Do not create a checkpoint before its scheduled time.'
root=Path(__file__).resolve().parents[1]
dest=root.parent/f'RESEARCH_SA21_checkpoint_{args.number:02d}.zip'
assert not dest.exists(),'Earlier checkpoints must never be overwritten.'
def include(p):
 rel=p.relative_to(root)
 if any(x in {'__pycache__','build','scans'} for x in rel.parts):return False
 if p.suffix in {'.zip','.pyc','.fmt','.aux','.toc','.out','.bbl','.blg'}:
  # Agent .out files are actual computation logs, not LaTeX auxiliaries.
  return p.suffix=='.out' and 'logs' not in rel.parts
 if p.suffix=='.pdf' and rel.as_posix()!='RESEARCH_SA21_paper.pdf':return False
 if 'sources' in rel.parts and p.suffix in {'.pdf','.png','.jpg'}:return False
 return True
files=sorted(p for p in root.rglob('*') if p.is_file() and include(p))
manifest=root/f'CHECKPOINT_{args.number:02d}_MANIFEST.tsv'
lines=['path\tbytes\tsha256']
for p in files:
 lines.append(f'{p.relative_to(root)}\t{p.stat().st_size}\t{hashlib.sha256(p.read_bytes()).hexdigest()}')
manifest.write_text('\n'.join(lines)+'\n')
meta=root/f'CHECKPOINT_{args.number:02d}_NOTE.md'
previous=[f'RESEARCH_SA21_checkpoint_{i:02d}.zip' for i in range(1,args.number)]
meta.write_text(f'# Checkpoint {args.number:02d}\n\nScheduled: {due.isoformat()}\n\nCreated: {now.isoformat()}\n\nPrevious checkpoints: '+(', '.join(previous) or 'none')+'\n\nThis is a working checkpoint. See the report and ledger for unfinished audits. Earlier ZIPs, attached input files, source facsimiles, runtime dependencies, and transient typesetting products are excluded. All mathematical scripts, outputs, proofs, notes, and source-access records written so far are included.\n')
files=sorted(set(files+[manifest,meta]))
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in files:z.write(p,Path('RESEARCH_SA21')/p.relative_to(root))
assert dest.stat().st_size<500_000_000
print(json.dumps({'file':str(dest),'bytes':dest.stat().st_size,'files':len(files),'created':now.isoformat()}))
