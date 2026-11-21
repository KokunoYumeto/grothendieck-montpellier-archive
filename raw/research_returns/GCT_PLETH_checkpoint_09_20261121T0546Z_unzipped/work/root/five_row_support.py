#!/usr/bin/env python3
"""G031: complete outer-five nonvanishing, with fixed arithmetic and lookup."""
from pathlib import Path
import argparse,json

LABELS=('5','41','32','311','221','2111','11111')
HERE=Path(__file__).resolve().parent
INDEX={tuple(n['gaps']):tuple(n['multiplicities'])
       for n in json.loads((HERE/'FIVE_ROW_SUPPORT_INDEX.json').read_text())['nodes']}

def normalize(g):
    a,b,c,d=g
    if a and a>=3*b+2*c+d:
        lower=max(1,3*b+2*c+d)
        return (lower+(a-lower)%10,b,c,d)
    if d and d>=a+2*b+3*c:
        lower=max(1,a+2*b+3*c)
        return (a,b,c,lower+(d-lower)%10)
    return tuple(g)

def classify(partition):
    lam=tuple(partition)
    if any(type(v) is not int or v<0 for v in lam):
        raise ValueError('partition entries must be nonnegative integers')
    if any(a<b for a,b in zip(lam,lam[1:])):
        raise ValueError('partition entries must be weakly decreasing')
    if sum(lam)%5:raise ValueError('partition size must be divisible by five')
    while lam and lam[-1]==0:lam=lam[:-1]
    inner=sum(lam)//5
    if len(lam)>5:
        return {'inner':inner,'case':'length exceeds five','support':[False]*7,
                'exact_multiplicities':[0]*7}
    lam=lam+(0,)*(5-len(lam));d=lam[-1]
    g=tuple(lam[i]-lam[i+1] for i in range(4))
    vector=None
    if not any(g):
        vector=(1,0,0,0,0,0,0);case='determinant'
    elif all(g):
        case='strict full support'
        ray=(g[1:]==(1,1,1) and g[0]%5==1) or (g[:3]==(1,1,1) and g[3]%5==1)
        if ray:
            vector=(0,1,1,1,1,1,0) if g==(1,1,1,1) else (0,2,3,3,3,2,0)
            case='strict exceptional ray'
        elif g==(1,2,2,1):
            vector=(0,2,3,4,4,3,1);case='strict exceptional point'
        elif g==(2,1,1,2):
            vector=(0,2,3,3,3,2,1);case='strict exceptional point'
    else:
        normal=normalize(g);vector=INDEX.get(normal)
        case='wall exceptional point or ray' if vector is not None else 'wall full support'
    if vector is not None and d%2:vector=vector[::-1]
    result={'inner':inner,'partition':lam,'determinant_shift':d,
            'gaps':g,'case':case,
            'support':[True]*7 if vector is None else [v>0 for v in vector]}
    if vector is not None:result['exact_multiplicities']=vector
    if any(g) and not all(g):result['normalized_gaps']=normalize(g)
    return result

def nonzero(partition,outer='5'):
    if isinstance(outer,(list,tuple)):outer=''.join(map(str,outer))
    if outer not in LABELS:raise ValueError('outer label must be a partition of five')
    return classify(partition)['support'][LABELS.index(outer)]

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('partition',help='comma-separated weakly decreasing entries')
    parser.add_argument('--outer',default=None)
    args=parser.parse_args()
    lam=tuple(int(v) for v in args.partition.split(',') if v)
    result=classify(lam)
    result['labels']=LABELS
    if args.outer is not None:result['requested_nonzero']=nonzero(lam,args.outer)
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
