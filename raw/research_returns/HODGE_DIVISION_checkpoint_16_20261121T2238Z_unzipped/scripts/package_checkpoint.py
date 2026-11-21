"""Create one scheduled, immutable research checkpoint; never nest ZIPs.

This packages authored proofs, registers, code and exact certificates.
Third-party full texts remain retrieval caches and are excluded; their
source records and hashes remain in the checkpoint.
"""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import argparse, hashlib, json, zipfile

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('number',type=int)
args=parser.parse_args()
state_path=ROOT/'RUN_STATE.json'
state=json.loads(state_path.read_text())
now=datetime.now(timezone.utc)
start=datetime.fromisoformat(state['start_utc'])
due=start+timedelta(minutes=45*args.number)
if now<due:
    raise SystemExit(f'Checkpoint is not due until {due.isoformat()}; no archive written.')
if args.number!=state['last_checkpoint']+1:
    raise SystemExit('Checkpoint number must be the next unused number.')
name=f'HODGE_DIVISION_checkpoint_{args.number:02d}.zip'
out=ROOT.parent/name
if out.exists():
    raise SystemExit('Refusing to overwrite an earlier checkpoint.')

state.update(last_checkpoint=args.number,last_checkpoint_utc=now.isoformat(),
             last_checkpoint_name=name,status='ACTIVE')
state_path.write_text(json.dumps(state,indent=2)+'\n')
with (ROOT/'LEDGER.md').open('a') as f:
    f.write(f'\n## Checkpoint{args.number:02d}\n\n{now.isoformat()} — '
            'Scheduled 45-minute checkpoint; research remains active. '
            'All current authored deliverables and work documentation are included, '
            'with no earlier ZIP nested. Third-party full texts are excluded; '
            'source locators and hashes are retained.\n')
(ROOT/'README_CHECKPOINT.md').write_text(
    f'# HODGE_DIVISION checkpoint {args.number:02d}\n\n'
    f'Snapshot: {now.isoformat()}. This is an active research checkpoint, '
    'not a final claim of completion. Read HODGE_DIVISION.tex, QUESTIONS.tsv, '
    'LEDGER.md, CHECK_EVENTS.tsv and IMPLICATIONS.md together. '
    'The agent directories include complete new proofs and work in progress '
    'whose integration or independent checking may still be pending.\n\n'
    'Reproduction uses the original attached input ZIP plus this checkpoint. '
    'The exact arithmetic scripts carry their numerical inputs directly. '
    'Primary full texts are retrieval caches, not redistributed artifacts; '
    'consult the accompanying SOURCES.md / SOURCE_LOG.md records and hashes. '
    'No TeX compilation is claimed: the installed engines lacked a usable '
    'format or accessible bundle; source integrity is checked separately.\n')

external_names={'DerauxKlein.txt','CahnF4.txt','LiSpitkovskyZobin.txt','equation13.png',
                'Carter1972.txt','weyle6.g','weyle7.g','weyle8.g',
                'Landherr1935.txt','CataneseDettweiler2014.txt',
                'BBT_author.txt','Tseng2010.txt','JarvisKimura2009.txt'}
excluded_suffixes={'.zip','.pdf','.aux','.out','.toc','.synctex','.pyc'}
# Exact mathematical table inputs are required by the retained source-to-input
# certificates. They are code/data, not cached article full texts. Preserve the
# original paths so a restored checkpoint can rerun these certificates directly.
table_dirs={
    'agents/g34_eightfolds/bireflection/csp6_odd/cache',
    'agents/imprimitive/lie_small_fields/cache',
    'research/a2_cores/cache',
}
table_inputs={str(p.relative_to(ROOT)) for d in table_dirs
              for p in (ROOT/d).glob('*.jl')}
table_inputs.update('research/sources/chevie/'+n
                    for n in ('weyle6.g','weyle7.g','weyle8.g','retrieval.json'))
def include(p):
    rel=p.relative_to(ROOT)
    if str(rel) in table_inputs:
        return p.is_file() and not p.is_symlink()
    return (p.is_file() and not p.is_symlink()
            and 'sources' not in rel.parts and 'references_cache' not in rel.parts
            and 'cache' not in rel.parts
            and '__pycache__' not in rel.parts
            and p.suffix.lower() not in excluded_suffixes
            and p.name not in external_names
            and p.name!='CHECKPOINT_MANIFEST.json')
files=sorted(p for p in ROOT.rglob('*') if include(p))
# Read each file once so concurrent research cannot make a manifest hash
# differ from the bytes actually stored in this checkpoint.
payloads=[(str(p.relative_to(ROOT)),p.read_bytes()) for p in files]
manifest={
    'checkpoint':args.number,'snapshot_utc':now.isoformat(),
    'due_utc':due.isoformat(),'status':'ACTIVE',
    'files':[{'path':name,'bytes':len(data),
              'sha256':hashlib.sha256(data).hexdigest()} for name,data in payloads],
    'exclusions':'No prior ZIP, third-party article full-text cache, or generated build cache. Exact mathematical table code/data needed by the retained certificates are included at original paths.',
    'retained_external_mathematical_inputs':sorted(table_inputs)}
mp=ROOT/'CHECKPOINT_MANIFEST.json'
mp.write_text(json.dumps(manifest,indent=2)+'\n')
payloads.append(('CHECKPOINT_MANIFEST.json',mp.read_bytes()))
with zipfile.ZipFile(out,'x',zipfile.ZIP_DEFLATED) as z:
    for name,data in payloads:z.writestr('HODGE_DIVISION/'+name,data)
with zipfile.ZipFile(out) as z:
    assert z.testzip() is None
    assert not any(n.lower().endswith('.zip') for n in z.namelist())
print(json.dumps({'path':str(out),'files':len(payloads),'bytes':out.stat().st_size,
                  'sha256':hashlib.sha256(out.read_bytes()).hexdigest()}))
