"""Create one immutable checkpoint at its prescribed 45-minute boundary.

Call only with a fresh clock__curr_time value. This script neither uploads
nor overwrites an archive. The upload and xattr receipt are handled by the
parent in the same tool invocation after creation.
"""
import argparse
import datetime as dt
import hashlib
import json
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
parser=argparse.ArgumentParser()
parser.add_argument('--number',type=int,required=True)
parser.add_argument('--utc',required=True)
args=parser.parse_args()
now=dt.datetime.strptime(args.utc,'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=dt.timezone.utc)
start=dt.datetime(2026,11,21,20,4,37,tzinfo=dt.timezone.utc)
due=start+dt.timedelta(minutes=45*args.number)
if now<due:
    raise SystemExit(f'Checkpoint not due until {due.isoformat()}; no archive created.')
if args.number<1:
    raise SystemExit('Positive checkpoint number required.')
path=ROOT/f'NEG_NIGHT_checkpoint_{args.number:02d}.zip'
if path.exists():
    raise SystemExit('Immutable checkpoint already exists; will not overwrite.')
items=[]
reference_copies=[]
def external_reference_copy(source):
    rel=source.relative_to(ROOT).as_posix()
    if rel.startswith(('work/root/references/','work/analytic/references/')):
        return True
    if rel.startswith('work/complexity/'):
        if source.name in {'c052_ramified_precision_one_outline.txt',
                           'c029_E_interface_excerpt.txt',
                           'c033_E_interface_excerpt.txt'}:
            return False  # Authored work notes or excerpts from the supplied E input.
        if source.name.startswith('goldreich_izsak12'):
            return False  # The primary paper explicitly grants CC-BY reuse.
        return source.suffix in {'.pdf','.png','.ps'} or (source.suffix=='.txt' and source.name!='hoza.txt')
    return rel in {'work/analytic/Martinet1971.pdf','work/analytic/martinet_p407.png','work/analytic/Csordas_Smith_Varga_1994.pdf','work/analytic/Csordas_Smith_Varga_1994.txt'} or (rel.startswith('work/analytic/') and source.name.lower().startswith(('csv_page-','csv1994_page','csordas_smith_varga_1994_page','critical_length_','gonek_landau','rudnick_sarnak')))
for source in sorted((ROOT/'deliverables').rglob('*')):
    if source.is_file():items.append((source,source.relative_to(ROOT/'deliverables').as_posix()))
for prefix in ['work','sources']:
    for source in sorted((ROOT/prefix).rglob('*')):
        if not source.is_file() or '__pycache__' in source.parts:continue
        if source.suffix in {'.pyc','.zip'}:continue
        if external_reference_copy(source):
            reference_copies.append({'local_research_path':source.relative_to(ROOT).as_posix(),'size_bytes':source.stat().st_size,'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'locator':'Exact work, statement, URL and audit are retained in the corresponding chapter and source-locator/check-event registers.','scope':'Third-party reference copy acquired during this run; full original not redistributed. Supplied source files are included unchanged.'})
            continue
        items.append((source,source.relative_to(ROOT).as_posix()))
prompt=ROOT/'upload/PROMPT(20261121-200413).md'
items.append((prompt,'TASK_PROMPT.md'))
manifest=[{'path':name,'size':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p,name in items]
with zipfile.ZipFile(path,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p,name in items:z.write(p,name)
    z.writestr('CHECKPOINT_MANIFEST.json',json.dumps({'number':args.number,'due_utc':due.isoformat(),'created_clock_utc':args.utc,'files':manifest},indent=2)+'\n')
    z.writestr('EXTERNAL_REFERENCE_COPIES.json',json.dumps(reference_copies,indent=2)+'\n')
with zipfile.ZipFile(path) as z:
    bad=z.testzip()
    if bad:raise SystemExit('ZIP integrity failure at '+bad)
result={'path':str(path),'size_bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'entries':len(items)+2,'created_clock_utc':args.utc}
print(json.dumps(result))
