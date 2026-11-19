"""Write a numbered full-work checkpoint, excluding supplied/fetched sources."""
from pathlib import Path
import argparse,hashlib,zipfile,time
p=argparse.ArgumentParser();p.add_argument('number',type=int);args=p.parse_args()
start=time.perf_counter();root=Path(__file__).resolve().parents[1]
out=root.parent/f'RESEARCH_SA10_checkpoint_{args.number:02d}.zip'
if out.exists(): raise SystemExit('Refusing to overwrite a checkpoint')
excluded={'literature_A','literature_B','literature_C','references_B56','tex_cache','__pycache__'}
skip={'.fmt','.dvi','.synctex.gz'}
files=[]
for f in root.rglob('*'):
    if not f.is_file(): continue
    rel=f.relative_to(root)
    if any(part in excluded for part in rel.parts): continue
    if 'ink_B56' in rel.parts and f.suffix.lower() in {'.png','.jpg','.pdf'}: continue
    if f.suffix in skip or f.suffix=='.zip': continue
    if f.suffix=='.pdf' and not (root/'logs/PDF_QA_APPROVED.txt').exists(): continue
    files.append(f)
manifest=root/f'CHECKPOINT_{args.number:02d}_FILES.tsv'
manifest.write_text('path\tbytes\tsha256\n'+'\n'.join(f'{f.relative_to(root)}\t{f.stat().st_size}\t{hashlib.sha256(f.read_bytes()).hexdigest()}' for f in sorted(files))+'\n')
files.append(manifest)
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for f in sorted(files): z.write(f,f.relative_to(root))
    for f in (root.parent/'library_helpers').glob('*.py'):
        name=str(Path('support/library_helpers')/f.name)
        if name not in z.namelist(): z.write(f,name)
if out.stat().st_size>=500_000_000: raise SystemExit('Checkpoint exceeds 500 MB')
print(out)
print(f'{len(files)} working files; {out.stat().st_size} compressed bytes; runtime {time.perf_counter()-start:.6f} seconds')
