"""Prescribed-character spectral refinement, including nonfaithful lifts.

Usage: python recursive_character.py n target max_modulus
The character target is reduced modulo each successive lift modulus.
All LP outputs are reconstructed and certified over Q before saving.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
import json
import subprocess
import sys
import time
import numpy as np
from scipy.optimize import linprog

root=Path(__file__).resolve().parent
n,target,max_modulus=map(int,sys.argv[1:4])
start=time.time()

def solve(weights,modulus):
    values=[sorted(set(x)) for x in weights]
    multiplicities=[Counter(x) for x in weights]
    edges=[e for e in product(*values) if sum(e)%modulus==0]
    rows=[(a,v) for a in range(3) for v in values[a]]
    matrix=[[int(e[a]==v) for e in edges] for a,v in rows]
    rhs=[multiplicities[a][v] for a,v in rows]
    a=np.array(matrix,dtype=float);b=np.array(rhs,dtype=float)
    def negative_certificate(candidate):
        y=[Fraction(float(v)).limit_denominator(10**6) for v in candidate]
        if all(sum(y[i]*matrix[i][j] for i in range(len(rows)))>=0 for j in range(len(edges))) and sum(y[i]*rhs[i] for i in range(len(rows)))<0:
            return {'W':weights,'y':[str(v) for v in y]}
        return None
    # Most high-modulus supports have independent columns.  Rationally
    # certify their linear solve first, retaining LP as an unconditional
    # fallback.  Floating-point ranks never decide feasibility by themselves.
    linear,_,rank,_=np.linalg.lstsq(a,b,rcond=None)
    residual=a@linear-b
    if max(abs(residual),default=0)>1e-8:
        certificate=negative_certificate(residual)
        if certificate is not None:return certificate
    elif rank==len(edges):
        x=[Fraction(float(v)).limit_denominator(10**6) for v in linear]
        if all(sum(x[j]*matrix[i][j] for j in range(len(edges)))==rhs[i] for i in range(len(rows))):
            if all(v>=0 for v in x):
                return {'W':weights,'E':edges,'x':[str(v) for v in x],'strict':all(v>0 for v in x)}
            bad=next(j for j,v in enumerate(x) if v<0)
            unit=np.zeros(len(edges));unit[bad]=1
            candidate=np.linalg.lstsq(a.T,unit,rcond=None)[0]
            certificate=negative_certificate(candidate)
            if certificate is not None:return certificate
    dual=linprog(b,A_ub=-a.T,b_ub=np.zeros(len(edges)),bounds=[(-1,1)]*len(rows),method='highs')
    assert dual.success
    if dual.fun < -1e-8:
        y=[Fraction(float(v)).limit_denominator(10**6) for v in dual.x]
        assert all(sum(y[i]*matrix[i][j] for i in range(len(rows)))>=0 for j in range(len(edges)))
        assert sum(y[i]*rhs[i] for i in range(len(rows)))<0
        return {'W':weights,'y':[str(v) for v in y]}
    objective=np.zeros(len(edges)+1);objective[-1]=-1
    primal=linprog(objective,A_ub=np.c_[-np.eye(len(edges)),np.ones(len(edges))],b_ub=np.zeros(len(edges)),A_eq=np.c_[a,np.zeros(len(rows))],b_eq=b,bounds=[(0,None)]*(len(edges)+1),method='highs')
    assert primal.success
    x=[Fraction(float(v)).limit_denominator(10**6) for v in primal.x[:-1]]
    assert all(v>=0 for v in x)
    assert all(sum(x[j]*matrix[i][j] for j in range(len(edges)))==rhs[i] for i in range(len(rows)))
    return {'W':weights,'E':edges,'x':[str(v) for v in x],'strict':all(v>0 for v in x)}

previous='BASE';modulus=2;levels=[]
while modulus<=max_modulus:
    stem=root/f'character_n{n}_t{target}_m{modulus}'
    result_path=stem.with_name(stem.name+'_result.json')
    if result_path.exists():
        result=json.loads(result_path.read_text())
        assert (result['n'],result['M'],result['target'])==(n,modulus,target)
        good=result['feasible']
        print('RESUME',n,target,modulus,result['counts'],flush=True)
    else:
        spectra=stem.with_name(stem.name+'_spectra.txt')
        stats=stem.with_name(stem.name+'_stats.json')
        subprocess.run([str(root/'refine_character'),str(n),str(modulus),str(target),str(previous),str(spectra),str(stats)],check=True)
        result=json.loads(stats.read_text());good=[];counts=Counter();completed=0
        certificates=stem.with_name(stem.name+'_certificates.jsonl')
        if certificates.exists():
            with certificates.open() as old:
                for line in old:
                    cert=json.loads(line);completed+=1
                    if 'x' in cert:good.append(cert);counts['feasible']+=1
                    else:counts['infeasible']+=1
            print('RESUME CERTIFICATES',n,target,modulus,completed,dict(counts),flush=True)
        with spectra.open() as source,certificates.open('a') as output:
            for i,line in enumerate(source):
                if i<completed:continue
                flat=list(map(int,line.split()));assert len(flat)==3*n
                weights=[flat[a*n:(a+1)*n] for a in range(3)]
                cert=solve(weights,modulus);output.write(json.dumps(cert,separators=(',',':'))+'\n')
                if 'x' in cert:good.append(cert);counts['feasible']+=1
                else:counts['infeasible']+=1
                if i%5000==0:print('FILTER',n,target,modulus,i,'/',result['orbits'],dict(counts),'time',round(time.time()-start,2),flush=True)
        result.update({'n':n,'M':modulus,'target':target,'normalized_target':target%modulus,'scope':'eigenvalues in mu_M and determinant exponent target, up to units preserving target','counts':dict(counts),'feasible':good})
        result_path.write_text(json.dumps(result,indent=2))
        print('DONE',n,target,modulus,dict(counts),'time',round(time.time()-start,2),flush=True)
    levels.append(result)
    previous=stem.with_name(stem.name+'_feasible.txt')
    with previous.open('w') as output:
        for record in good:output.write(' '.join(str(v) for factor in record['W'] for v in factor)+'\n')
    if not good:break
    modulus*=2
(root/f'character_n{n}_t{target}_summary.json').write_text(json.dumps(levels,indent=2))
