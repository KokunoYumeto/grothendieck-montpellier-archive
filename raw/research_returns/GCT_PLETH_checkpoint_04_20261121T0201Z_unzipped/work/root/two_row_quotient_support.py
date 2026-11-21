"""G-021: exact residue support, streamed without a large lookup table."""
from pathlib import Path
from hashlib import sha256
from math import comb
import json
import numpy as np

HERE = Path(__file__).resolve().parent
LABELS = ('5','41','32','311','221','2111','11111')
SIZES = (1,10,15,20,20,30,24)
CHARS = ((1,1,1,1,1,1,1),(4,2,0,1,-1,0,-1),
         (5,1,1,-1,1,-1,0),(6,0,-2,0,0,0,1),
         (5,-1,1,-1,-1,1,0),(4,-2,0,1,1,0,-1),
         (1,-1,1,1,-1,-1,1))
FIXED = (5,3,1,2,0,1,0)

def h(g,n):
    if n<0:return 0
    if g==0:return comb(n+3,3)
    if g==1:return (n//2+1)*((n+1)//2+1)
    if g==2:return n//2+1 if n%2==0 else 0
    if g==3:return n//3+1
    if g==4:return (1,-1,1,0,0,0)[n%6]
    if g==5:return int(n%4==0)
    return (1,-1,0,0,0)[n%5]

def schur(g,a,b):
    return h(g,a)*h(g,b)-h(g,a+1)*h(g,b-1)

# Build the finite factors with arbitrary-precision Python integers, then
# bound every class summand and character partial sum before using int64.
RST=np.zeros((7,3,60,60),dtype=object)
HD=np.zeros((7,3,60,60),dtype=object)
for g in range(7):
    for x in range(60):
        for b in range(60):
            a=x+b
            s0=schur(g,a,b)
            s1=schur(g,a-1,b)+schur(g,a,b-1)
            z=schur(g,a-1,b-1)
            RST[g,:,x,b]=(s0-s1+z,s1-2*z,z)
    for k in range(60):
        for t in range(60):
            c=2*k+t
            hc,h1,h2=h(g,c),h(g,c-1),h(g,c-2)
            HD[g,:,k,t]=(hc-FIXED[g]*h(g,k-1),hc-h1,hc-2*h1+h2)

class_bounds=[sum(int(np.max(np.abs(RST[g,j])))*int(np.max(np.abs(HD[g,j])))
                  for j in range(3)) for g in range(7)]
NUMERATOR_BOUND=max(sum(abs(SIZES[g]*CHARS[ell][g])*class_bounds[g]
                        for g in range(7)) for ell in range(7))
assert NUMERATOR_BOUND < 2**63
RST=RST.astype(np.int64);HD=HD.astype(np.int64)

hashes=[sha256() for _ in LABELS]
zeros=[[] for _ in LABELS]
minimum=[None]*7;maximum=[None]*7
observed_numerator=0
for x in range(60):
    classes=np.zeros((7,60,60,60),dtype=np.int64)
    for g in range(7):
        for j in range(3):
            classes[g]+=RST[g,j,x,:,None,None]*HD[g,j,None,:,:]
    for ell,label in enumerate(LABELS):
        numerator=np.zeros((60,60,60),dtype=np.int64)
        for g in range(7):numerator+=SIZES[g]*CHARS[ell][g]*classes[g]
        assert np.all(numerator%120==0)
        values=numerator//120
        assert np.all(values>=0)
        observed_numerator=max(observed_numerator,int(np.max(np.abs(numerator))))
        hashes[ell].update(values.astype('<i8').tobytes(order='C'))
        lo,hi=int(values.min()),int(values.max())
        minimum[ell]=lo if minimum[ell] is None else min(minimum[ell],lo)
        maximum[ell]=hi if maximum[ell] is None else max(maximum[ell],hi)
        zeros[ell].extend((x,int(b),int(k),int(t)) for b,k,t in np.argwhere(values==0))
    if x%10==0:print('x',x,'zeros',sum(map(len,zeros)),flush=True)

result={'statement':'G-021','checked_entries':7*60**4,
        'integer_bound':NUMERATOR_BOUND,'class_bounds':class_bounds,
        'observed_max_abs_numerator':observed_numerator,
        'hash_order':'x,b,k,t lexicographic, signed little-endian int64',
        'labels':{label:{'min':minimum[i],'max':maximum[i],
                         'sha256':hashes[i].hexdigest(),'zeros':zeros[i]}
                  for i,label in enumerate(LABELS)},
        'total_zeros':sum(map(len,zeros))}
(HERE/'TWO_ROW_QUOTIENT_SUPPORT.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS',result['checked_entries'],'entries;',result['total_zeros'],'zeros',flush=True)
print('bound',NUMERATOR_BOUND,'zeros by label',list(map(len,zeros)),flush=True)
