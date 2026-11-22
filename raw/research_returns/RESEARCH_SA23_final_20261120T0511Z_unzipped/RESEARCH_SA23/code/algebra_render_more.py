"""Render selected original pages for exact source comparison."""
from pathlib import Path
import subprocess
import time

root=Path(__file__).resolve().parents[1]
start=time.perf_counter()
jobs={
 'algebra_SGA6.pdf':[2,3,4,5,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432],
 'EGAIV4.pdf':[188,226,227,228,255,256,260,270,346,347],
 'EGA0IV.pdf':[18,123,124,125,126],
 'EGAIII1.pdf':[129,130,132],
}
for name,pages in jobs.items():
    source=root/'sources'/name
    for page in pages:
        prefix=source.stem if source.stem.startswith('algebra_') else 'algebra_'+source.stem
        dest=root/'sources'/f'{prefix}_p{page:03d}'
        if dest.with_suffix('.png').exists():
            print('EXISTS',dest.with_suffix('.png'),flush=True)
            continue
        command=['pdftoppm','-f',str(page),'-l',str(page),'-scale-to','1900',
                 '-singlefile','-png',str(source),str(dest)]
        result=subprocess.run(command,capture_output=True,text=True)
        print('command',repr(command),'exit',result.returncode,flush=True)
        if result.stderr:
            print(result.stderr,flush=True)
        result.check_returncode()
print('Elapsed seconds',time.perf_counter()-start,flush=True)
