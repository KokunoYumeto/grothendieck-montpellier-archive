"""List complete deliverables only; omit binaries and reproducible batch intermediates."""
from pathlib import Path
import csv,hashlib
root=Path(__file__).resolve().parent
exclude={'POLARIZATION_R4_L4_B15.input','POLARIZATION_R4_L4_B15_CERTIFICATES.txt',
         'POLARIZATION_R4_L4_B15_RANKS.tsv','POLARIZATION_R6_L1_B5_SELECTED.compact'}
files=[]
for p in sorted(root.rglob('*')):
    if not p.is_file() or p.name in exclude or p.name=='FINAL_FILE_MANIFEST.tsv':continue
    if '__pycache__' in p.parts:continue
    if p.relative_to(root).parts[0] in {'polarization_r4_l4_parts','polarization_r6_parts'}:continue
    if p.suffix not in {'.py','.cpp','.md','.tsv','.txt','.json','.tex','.gz','.input','.compact'}:continue
    files.append(dict(path=str(p.relative_to(root.parent.parent)),bytes=p.stat().st_size,
                      SHA256=hashlib.sha256(p.read_bytes()).hexdigest()))
with (root/'FINAL_FILE_MANIFEST.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['path','bytes','SHA256'],delimiter='\t')
    w.writeheader();w.writerows(files)
print('complete_files',len(files),'bytes',sum(r['bytes'] for r in files))
