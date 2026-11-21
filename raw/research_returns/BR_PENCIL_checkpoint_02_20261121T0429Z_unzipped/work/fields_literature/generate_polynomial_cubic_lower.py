#!/usr/bin/env python3
"""Turn p=4 weight pivots into exact integer certificates."""
from itertools import combinations,permutations
from pathlib import Path
import json,time
import sympy as sp

HERE=Path(__file__).resolve().parent
IW=list(combinations(range(12),4));JW=list(combinations(range(12),5))
IM=[sum(1<<i for i in w) for w in IW]
JM=[sum(1<<i for i in w) for w in JW]

def parity(p):return (-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))

def tensor(sign):
    T={}
    for a,last in enumerate((2,3)):
        labels=(0,1,last)
        for r in permutations(range(3)):
            for c in permutations(range(3)):
                word=tuple(4*r[i]+labels[c[i]] for i in range(3))
                T[(a,)+word]=parity(r)*parity(c) if sign==-1 else 1
    return T

def matrix(T,rows,cols):
    result=[]
    for row in rows:
        j,l=divmod(row,12);J=JM[j];line=[]
        for col in cols:
            alpha,rest=divmod(col,len(IW)*12);i,k=divmod(rest,12);I=IM[i]
            if I&J!=I:line.append(0);continue
            b=(J^I).bit_length()-1
            s=(-1)**(1-alpha+(I&((1<<b)-1)).bit_count())
            line.append(s*T.get((1-alpha,b,k,l),0))
        result.append(line)
    return result

def main():
    data=json.loads((HERE/'polynomial_cubic_koszul_results.json').read_text())
    data.append(json.loads((HERE/'polynomial_cubic_p2_pivots.json').read_text()))
    result=[];start=time.time()
    for old in data:
        if old['p']!=4:continue
        if old['family']=='per' and old['prime']!=2:continue
        T=tensor(-1 if old['family']=='det' else 1);blocks=[];primes=set()
        for b in old['blocks']:
            rows,cols=b['minor_rows'],b['minor_cols']
            M=matrix(T,rows,cols)
            value=int(sp.Matrix(M).det(method='domain-ge'))
            assert value
            primes.update(int(x) for x in sp.factorint(abs(value)))
            blocks.append({'weight':b['weight'],'rows':rows,'cols':cols,'determinant_Z':value})
        rec={'family':old['family'],'p':4,'matrix_shape':old['shape'],'pure_cost':330,
             'certified_rank':sum(len(b['rows']) for b in blocks),
             'pivot_prime':old['prime'],
             'field_condition':('all_characteristics' if old['family']=='per' else 'characteristic_not2or3'),
             'excluded_primes':sorted(primes),'blocks':blocks}
        result.append(rec)
        print(rec['family'],rec['certified_rank'],'prime divisors',sorted(primes),'seconds',time.time()-start,flush=True)
    (HERE/'polynomial_cubic_lower_certificate.json').write_text(json.dumps(result,separators=(',',':'))+'\n')

if __name__=='__main__':main()
