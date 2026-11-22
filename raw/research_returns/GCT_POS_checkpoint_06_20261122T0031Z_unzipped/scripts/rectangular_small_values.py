from symmetric_character import rectangular_triple, clear_cache
from pathlib import Path
from time import monotonic
import argparse,json
p=argparse.ArgumentParser()
p.add_argument('--n',type=int,default=4)
p.add_argument('--max-s',type=int,default=10)
p.add_argument('--out',required=True)
a=p.parse_args(); start=monotonic(); values=[]
for s in range(a.max_s+1):
    value=rectangular_triple(a.n,s)
    values.append(value)
    clear_cache()
    print(json.dumps({'n':a.n,'s':s,'value':value,'seconds':round(monotonic()-start,3)}),flush=True)
    Path(a.out).write_text(json.dumps({'n':a.n,'values':values,
        'method':'exact Murnaghan--Nakayama character inner product',
        'scope':'finite coefficients only, no rational-series reconstruction'},indent=2))
