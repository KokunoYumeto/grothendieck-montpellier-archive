"""Finite spectral diagnostics for the K018 iterated family, not a global pole proof."""
from sympy import Matrix
from fractions import Fraction as F
from itertools import product
from collections import Counter
from pathlib import Path
import json,argparse

parser=argparse.ArgumentParser()
parser.add_argument('--output-index',type=int,default=2)
args=parser.parse_args()

root=Path(__file__).resolve().parent
g=json.loads((root/'amplifying_gadget_q8.json').read_text())
E=g['support'];bd=g['boundary'];p=g['intercept_numerators'];u=g['slope_numerators']
support=[(0,0,0),(0,1,1),(1,0,1),(1,1,0)]
masses=[F(1,2)]*4;n=2;selected=(0,0,0);out=[]
for k in range(5):
    modulus=2*256**k
    if k:
        A=Matrix([[int(e[a]==i) for e in support] for a in range(3) for i in range(n)])
        rows=[i for i in range(3*n) if i not in (2*n-1,3*n-1)]
        inverse=A[rows,:].inv()*modulus
        for row,mass in zip(inverse.tolist(),masses):
            if (mass*modulus).numerator%2:
                flat=[0]*(3*n)
                for i,v in zip(rows,row):flat[i]=int(v)%modulus
                break
        weights=[flat[j*n:(j+1)*n] for j in range(3)]
        chi=sum(flat)%modulus
        pairs=[[(i,j) for i in range(n) for j in range(i+1,n)
                if (weights[a][i]-weights[a][j])%modulus==modulus//2] for a in range(3)]
        counts=[]
        for mod in [modulus,2**(n-1)]:
            fixed_v=sum(sum(e)%mod==0 for e in product(*weights))
            fixed_sl=sum(sum(v*v for v in Counter(a%mod for a in factor).values())
                         for factor in weights)-3
            counts.append([mod,fixed_v,fixed_sl,fixed_v-fixed_sl])
        record={'k':k,'n':n,'M':modulus,'support':support.copy(),
                'masses':[str(x) for x in masses],'W':weights,'chi':chi,'pairs':pairs,
                'distinct_spectra':all(len(set(factor))==n for factor in weights),
                'fixed_counts':counts}
        out.append(record)
        print(n,'pairs',pairs,'distinct',record['distinct_spectra'],'fixed counts',counts,flush=True)
    if k==4:break
    index=support.index(selected);r=masses.pop(index);support.pop(index)
    maps=[]
    for a in range(3):
        others=[i for i in range(8) if i!=bd[a]]
        maps.append({bd[a]:selected[a],**{v:n+j for j,v in enumerate(others)}})
    added=[tuple(maps[a][edge[a]] for a in range(3)) for edge in E]
    support.extend(added);masses.extend(F(x+y*r,256) for x,y in zip(p,u))
    selected=added[args.output_index];n+=7
suffix='' if args.output_index==2 else '_output'+str(args.output_index)
(root/('amplifier_spectral_diagnostics'+suffix+'.json')).write_text(json.dumps(out,indent=2))
