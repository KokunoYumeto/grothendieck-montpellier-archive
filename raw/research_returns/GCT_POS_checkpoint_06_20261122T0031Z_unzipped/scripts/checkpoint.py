"""Scheduled, non-overwriting checkpoint packager. Call only at the due time."""
from pathlib import Path
import zipfile, hashlib, json, sys, tempfile, shutil
from datetime import datetime, timezone
root=Path(__file__).resolve().parents[1]
number=int(sys.argv[1]); stamp=sys.argv[2]
out=root.parent/'exports'/f'GCT_POS_checkpoint_{number:02d}.zip'
if out.exists(): raise SystemExit('Refusing to overwrite an existing checkpoint')
state={'checkpoint':number,'time_utc':stamp,'status':'ACTIVE RESEARCH','model':'GPT-6 Astra Pro','effort':'not exposed','first_formal_review_utc':'2026-11-21T23:01:00Z','next_checkpoint_utc':sys.argv[3],'main_gate':'Numerical PH3 refuted by actual poles at2^(n−1)·3^r; exact r=0 and strict index bounds remain open. Proposed sharp maximal-order bound refuted by K-018; n4/n5 fixed loci complete.','source_archive':'GCT_POS_the_positivity_hypotheses_of_geometric_complexity_th.zip'}
state['formal_review']=json.loads((root/'REVIEWS_STATE.json').read_text()) if (root/'REVIEWS_STATE.json').exists() else None
(root/'CHECKPOINT_STATE.json').write_text(json.dumps(state,indent=2)+'\n')
with (root/'LEDGER.md').open('a') as f:
 f.write(f'\n## Checkpoint {number:02d} — {stamp}\n\nScheduled 45-minute snapshot of all current deliverables and work documentation. No earlier checkpoint ZIP is nested. Active research continues. The compiled main PDF may lag the latest checked TeX additions; the source and event ledger determine current status. Next checkpoint: {sys.argv[3]}.\n')
files=sorted(p for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix not in {'.pyc','.aux','.log','.out','.toc','.synctex'} and not p.name.startswith('GCT_POS_checkpoint_'))
with tempfile.TemporaryDirectory(prefix='gct_pos_checkpoint_snapshot_',dir=root.parent) as temporary:
 snapshot=Path(temporary)
 for p in files:
  q=snapshot/p.relative_to(root);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
 with zipfile.ZipFile(out,'x',zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as z:
  for p in files:
   relative=p.relative_to(root);z.write(snapshot/relative,relative)
receipt={'file':str(out),'files':len(files),'size_bytes':out.stat().st_size,'sha256':hashlib.file_digest(out.open('rb'),'sha256').hexdigest(),'created_utc':stamp}
(root.parent/f'checkpoint_{number:02d}_local_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
