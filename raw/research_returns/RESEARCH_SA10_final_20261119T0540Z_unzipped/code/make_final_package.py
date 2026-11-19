"""Prepare or build the final archive; retain checkpoint paths and all authored records."""
from pathlib import Path
import argparse,csv,hashlib,json,shutil,time,zipfile
parser=argparse.ArgumentParser();parser.add_argument('--build',action='store_true');args=parser.parse_args()
start=time.perf_counter();root=Path(__file__).resolve().parents[1]
excluded_dirs={'literature_A','literature_B','literature_C','references_B56','tex_cache','__pycache__'}
excluded_suffixes={'.fmt','.dvi','.zip'}
def exclusion(path):
    rel=path.relative_to(root)
    if any(s in excluded_dirs for s in rel.parts): return 'Research input or runtime cache'
    if path.suffix.lower() in excluded_suffixes: return 'Runtime binary or earlier archive'
    if 'ink_B56' in rel.parts and path.suffix.lower() in {'.png','.jpg','.pdf'}: return 'Primary manuscript scan rendering'
    return None
pdf=root/'RESEARCH_SA10_paper.pdf'
qa=json.loads((root/'qa/final_qa.json').read_text())
assert qa['approval']=='PASS'
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==qa['pdf_sha256']
assert (root/'RESEARCH_SA10_report.md').read_text().startswith('| Item | Outcome |')
assert not (root/'RESEARCH_SA10_report.md').read_text().startswith('INCOMPLETE')
with (root/'RESEARCH_SA10_results.csv').open() as f:
    rows=list(csv.DictReader(f))
assert len(rows)==74 and len({r['id'] for r in rows})==74
for dirname in ['code_B','code_B56','code_C']:
    dest=root/'code/programs'/dirname
    dest.mkdir(parents=True,exist_ok=True)
    for p in (root/dirname).rglob('*'):
        if p.is_file() and '__pycache__' not in p.parts:
            target=dest/p.relative_to(root/dirname);target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(p,target)
shutil.copy2(root/'logs/fetch_primary_A.out',root/'code/fetch_primary_A.out')
support=root/'support/library_helpers';support.mkdir(parents=True,exist_ok=True)
for p in (root.parent/'library_helpers').glob('*.py'): shutil.copy2(p,support/p.name)
all_paths=[p for p in root.rglob('*') if p.is_file()]
files=sorted(p for p in all_paths if not exclusion(p))
omissions=[]
for p in all_paths:
    why=exclusion(p)
    if why: omissions.append((str(p.relative_to(root)),why))
with (root/'DELIVERY_EXCLUSIONS.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['path','reason']);w.writerows(sorted(omissions))
missing=[]
for manifest in root.glob('CHECKPOINT_*_FILES.tsv'):
    with manifest.open() as f:
        for row in csv.DictReader(f,delimiter='\t'):
            path=root/row['path']
            if not path.exists(): missing.append((manifest.name,row['path']))
assert not missing,missing
print(f'Preflight PASS: {len(files)} selected current files; {len(rows)} results; QA digest matches; no missing checkpoint-manifest path.')
print(f'Excluded {len(omissions)} research-input/runtime files. No supplied attachment or previous ZIP is selected.')
print(f'Preparation runtime {time.perf_counter()-start:.9f} seconds.')
if not args.build:
    raise SystemExit(0)
out=root.parent/'RESEARCH_SA10_final.zip'
if out.exists(): raise SystemExit('Refusing to overwrite an existing final archive')
# This manifest intentionally excludes itself; it hashes every other selected
# file. The final ZIP is verified externally after writing, avoiding a self-hash.
manifest=root/'DELIVERY_MANIFEST.tsv'
files=sorted(p for p in root.rglob('*') if p.is_file() and not exclusion(p) and p!=manifest)
snapshot={str(p.relative_to(root)):p.read_bytes() for p in files}
with manifest.open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['path','bytes','sha256'])
    for name,data in snapshot.items():
        w.writerow([name,len(data),hashlib.sha256(data).hexdigest()])
snapshot[manifest.name]=manifest.read_bytes()
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for name,data in snapshot.items(): z.writestr(name,data)
assert out.stat().st_size<500_000_000
with zipfile.ZipFile(out) as z:
    assert z.testzip() is None
print(f'Final archive PASS: {len(snapshot)} entries; {out.stat().st_size} bytes; CRC verified; no nested ZIP.')
print(f'Total runtime {time.perf_counter()-start:.9f} seconds.')
