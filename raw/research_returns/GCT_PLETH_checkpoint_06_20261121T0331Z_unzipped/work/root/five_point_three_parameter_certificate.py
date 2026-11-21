"""Exhaustive fixed Newton certificate for G-020: a,k,t >= 0.

No huge lookup table is needed: coefficients are specified by seven fixed
trace recurrences and finite differences.  This script checks their signs
over every residue and keeps compact exact minima, zero sets and hashes.
"""
from pathlib import Path
from math import comb
import hashlib, json, sys
import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'rectangular'))
from verify_rectangular import partitions,character,z

labels=list(partitions(5))
classes=((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))
weights=[[120//z(c)*character(mu,c) for c in classes] for mu in labels]
maxindex=900
traces=[]
for cyc in classes:
    f=[1]+[0]*maxindex
    for length in cyc:
        for d in range(length,maxindex+1):f[d]+=f[d-length]
    traces.append([f[0]]+[f[d]-f[d-1] for d in range(1,maxindex+1)])


def h(g,n):
    return traces[g][n] if n>=0 else 0


def diff(g,base,step,order):
    return sum((-1)**(order-j)*comb(order,j)*h(g,base+step*j)
               for j in range(order+1))


def mix(g,base,j,l):
    return sum((-1)**(j+l-u-v)*comb(j,u)*comb(l,v)*h(g,base+120*u+60*v)
               for u in range(j+1) for v in range(l+1))


# Trace residue polynomials have degree at most3.  The actual upper index
# needed below is177+3*120+3*60=717, below maxindex.
DA=np.array([[[diff(g,r,60,i) for r in range(60)] for i in range(4)] for g in range(7)],dtype=np.int64)
DAP=np.array([[[diff(g,r-1,60,i) for r in range(60)] for i in range(4)] for g in range(7)],dtype=np.int64)
JK=np.array([[[diff(g,r-1,60,j) for r in range(60)] for j in range(4)] for g in range(7)],dtype=np.int64)
indices=[(i,j,l) for i in range(4) for j in range(4) for l in range(4)]
RK=np.arange(60)[:,None]; RT=np.arange(60)[None,:]; C=2*RK+RT
minimum={','.join(map(str,mu)):{} for mu in labels}
maximum={','.join(map(str,mu)):{} for mu in labels}
zeros={','.join(map(str,mu)):[] for mu in labels}
hashes={','.join(map(str,mu)):hashlib.sha256() for mu in labels}
bad=[];count=0;zero_positions=[]

for i,j,l in indices:
    H=np.array([[mix(g,c,j,l) for c in range(178)] for g in range(7)],dtype=np.int64)
    HP=np.array([[mix(g,c-1,j,l) for c in range(178)] for g in range(7)],dtype=np.int64)
    # A conservative Python-integer bound proves all vectorized intermediates
    # fit signed64; exact integer division is checked separately.
    bound=sum(max(abs(int(v)) for v in DA[g,i])*max(abs(int(v)) for v in H[g])
              +max(abs(int(v)) for v in DAP[g,i])*max(abs(int(v)) for v in HP[g])
              +(0 if l else classes[g].count(1)*max(abs(int(v)) for v in DA[g,i]-DAP[g,i])*max(abs(int(v)) for v in JK[g,j]))
              for g in range(7))*180
    assert bound<2**63,(i,j,l,bound)
    classarrays=[]
    for g in range(7):
        value=DA[g,i,:,None,None]*H[g,C][None,:,:]-DAP[g,i,:,None,None]*HP[g,C][None,:,:]
        if l==0:
            value=value-classes[g].count(1)*(DA[g,i]-DAP[g,i])[:,None,None]*JK[g,j][None,:,None]
        classarrays.append(value)
    zero_for_all=True
    for mu,ww in zip(labels,weights):
        key=','.join(map(str,mu));value=sum(w*v for w,v in zip(ww,classarrays))
        assert np.all(value%120==0),(mu,i,j,l,'integrality')
        value=value//120
        low=int(value.min());high=int(value.max());slot=f'{i},{j},{l}'
        minimum[key][slot]=low;maximum[key][slot]=high
        count+=value.size
        hashes[key].update(value.astype('<i8',copy=False).tobytes(order='C'))
        if low<0:
            where=np.argwhere(value<0)
            bad.append({'label':mu,'orders':[i,j,l],'count':len(where),
                        'examples':[(tuple(map(int,p)),int(value[tuple(p)])) for p in where[:8]]})
        if high:zero_for_all=False
        if (i,j,l)==(0,0,0):
            zeros[key]=[list(map(int,p)) for p in np.argwhere(value==0)]
    if zero_for_all:zero_positions.append([i,j,l])
    if (j,l)==(0,0):print('a difference order',i,'count',count,'negative_blocks',len(bad),flush=True)

result={'statement':'G-020','period':60,'verified_entries':count,
        'negative_blocks':bad,'minima':minimum,'maxima':maximum,
        'identically_zero_difference_positions':zero_positions,
        'zero_triples_in_residue_cube':zeros,
        'table_sha256':{key:value.hexdigest() for key,value in hashes.items()}}
(HERE/'FIVE_POINT_THREE_PARAMETER_SUMMARY.json').write_text(json.dumps(result,indent=2)+'\n')
print('TOTAL',count,'negative blocks',len(bad),'zero difference positions',len(zero_positions),flush=True)
for key in zeros:print(key,'zero triples',len(zeros[key]),zeros[key][:25],flush=True)
assert not bad
