"""Exact central partial-transpose cone for a pair of Specht types.

Group counts, character table, Gram kernel, and final witness are exact.
SciPy is used only to discover a nonnegative kernel vector; the resulting
rational vector is checked exactly before any finite-block certificate is saved.
No finite result in this program establishes a regularized lower bound.
"""
from pathlib import Path
from functools import lru_cache
from fractions import Fraction
from collections import Counter
import argparse, json, math, subprocess, time
import numpy as np
import sympy as sp
from scipy.optimize import linprog

ROOT=Path(__file__).resolve().parents[1]


def partitions(n, top=None):
    if n==0:
        yield (); return
    for a in range(min(n, top or n), 0, -1):
        for b in partitions(n-a, a):
            yield (a,)+b


@lru_cache(None)
def character(shape, cycles):
    if not cycles:
        return int(not shape)
    length=cycles[0]
    cells={(i,j) for i,a in enumerate(shape) for j in range(a)}
    answer=0
    for smaller in partitions(sum(shape)-length):
        if len(smaller)>len(shape) or any(a>shape[i] for i,a in enumerate(smaller)):
            continue
        removed=cells-{(i,j) for i,a in enumerate(smaller) for j in range(a)}
        if len(removed)!=length:
            continue
        if any((i+1,j) in removed and (i,j+1) in removed and (i+1,j+1) in removed for i,j in removed):
            continue
        seen=set(); pending=[next(iter(removed))]
        while pending:
            cell=pending.pop()
            if cell in seen:
                continue
            seen.add(cell);i,j=cell
            pending.extend(x for x in ((i+1,j),(i-1,j),(i,j+1),(i,j-1))
                           if x in removed and x not in seen)
        if len(seen)==length:
            answer+=(-1)**(len({i for i,j in removed})-1)*character(smaller, cycles[1:])
    return answer


def main(lam,mu,tag):
    started=time.time();n=sum(lam);assert n==sum(mu)
    shapes=list(partitions(n));size=math.factorial(n)
    table=[[character(a,c) for c in shapes] for a in shapes]
    class_sizes=[]
    for c in shapes:
        z=math.prod(k**m*math.factorial(m) for k,m in Counter(c).items())
        class_sizes.append(size//z)
    dims=[character(a,(1,)*n) for a in shapes]
    for i in range(len(shapes)):
        for j in range(len(shapes)):
            assert sum(s*a*b for s,a,b in zip(class_sizes,table[i],table[j]))==size*(i==j)
    la=shapes.index(lam);mb=shapes.index(mu)
    rows=[f'{n} {len(shapes)}']
    rows += [' '.join(map(str,(len(c),*c,table[la][i],table[mb][i]))) for i,c in enumerate(shapes)]
    cpp=ROOT/'programs/pg_op_pair_counts.cpp';exe=Path('/tmp/pg_op_pair_counts')
    if not exe.exists() or exe.stat().st_mtime<cpp.stat().st_mtime:
        subprocess.run(['c++','-O3','-std=c++17',str(cpp),'-o',str(exe)],check=True)
    raw=subprocess.run([str(exe)],input='\n'.join(rows)+'\n',text=True,capture_output=True,check=True).stdout.splitlines()
    assert int(raw[0])==size
    counts=[list(map(int,row.split())) for row in raw[1:]]
    assert len(counts)==len(shapes) and all(len(row)==len(shapes) for row in counts)
    identity=shapes.index((1,)*n)
    for c in range(len(shapes)):
        assert counts[identity][c]==class_sizes[c]*table[la][c]*table[mb][c]
        assert counts[c][identity]==table[la][c]*table[mb][c]
        for h in range(len(shapes)):
            assert class_sizes[c]*counts[c][h]==class_sizes[h]*counts[h][c]
    multiplicities=[]
    for nu in range(len(shapes)):
        value=Fraction(sum(s*a*b*c for s,a,b,c in zip(class_sizes,table[la],table[mb],table[nu])),size)
        assert value.denominator==1 and value>=0
        multiplicities.append(int(value))
    active=[i for i,m in enumerate(multiplicities) if m]
    assert sum(d*m for d,m in zip(dims,multiplicities))==dims[la]*dims[mb]
    T=sp.Matrix([table[i] for i in active])
    M=sp.diag(*class_sizes)*sp.Matrix(counts)
    K=sp.diag(*[dims[i] for i in active])*(T*M*T.T)*sp.diag(*[dims[i] for i in active])/size**2
    ranks=[dims[i]*multiplicities[i] for i in active]
    assert K==K.T and K*sp.ones(len(active),1)==sp.Matrix(ranks)
    D=2*(sp.diag(*ranks)-K)
    entropies=[-sum(a/n*math.log2(a/n) for a in shapes[i]) for i in active]
    candidates=sorted(set(entropies),reverse=True)
    constraints=D*sp.diag(*[sp.Rational(1,r) for r in ranks])
    Aeq=np.vstack((np.array(constraints,dtype=float),np.ones((1,len(active)))))
    beq=np.r_[np.zeros(len(active)),1.0]
    witness=None;attempts=[]
    for threshold in candidates:
        allowed=[i for i,h in enumerate(entropies) if h>=threshold-1e-11]
        bounds=[(0,None) if i in allowed else (0,0) for i in range(len(active))]
        lp=linprog(np.zeros(len(active)),A_eq=Aeq,b_eq=beq,bounds=bounds,method='highs')
        attempts.append({'threshold':threshold,'numerical_success':bool(lp.success)})
        if not lp.success:
            continue
        support=[i for i,y in enumerate(lp.x) if y>1e-9]
        E=constraints[:,support].col_join(sp.ones(1,len(support)))
        solution=next(iter(sp.linsolve((E,sp.Matrix([0]*len(active)+[1])))))
        variables=set().union(*(x.free_symbols for x in solution))
        solution=[x.subs({v:0 for v in variables}) for x in solution]
        if not all(x>=0 for x in solution):
            continue
        y=sp.zeros(len(active),1)
        for i,z in zip(support,solution):y[i]=z
        x=sp.diag(*[sp.Rational(1,r) for r in ranks])*y
        assert D*x==sp.zeros(len(active),1) and sum(r*z for r,z in zip(ranks,x))==1
        assert all(x[i]==0 for i in range(len(active)) if i not in allowed)
        witness={'threshold_bits':min(entropies[i] for i,z in enumerate(x) if z>0),
                 'coefficients':[str(z) for z in x],
                 'trace':1,
                 'support':[list(shapes[active[i]]) for i,z in enumerate(x) if z>0]}
        break
    assert witness is not None
    encode=lambda A:[[str(a) for a in row] for row in A.tolist()]
    output={'status':'PASS exact rational finite-block central-PT witness; no optimality or regularization claim',
            'n':n,'q_min':max(len(lam),len(mu)),'lambda':list(lam),'mu':list(mu),
            'permutation_pairs_evaluated':len(shapes)*size,
            'all_partitions':[list(a) for a in shapes],'character_table':table,'class_sizes':class_sizes,
            'word_counts':counts,'active_partitions':[list(shapes[i]) for i in active],
            'multiplicities':[multiplicities[i] for i in active],'ranks':ranks,
            'K':encode(K),'D':encode(D),'kernel_dimension':len(D.nullspace()),
            'witness':witness,'numerical_threshold_attempts':attempts,'elapsed_seconds':time.time()-started}
    p=ROOT/'outputs'/f'{tag}.json';t=p.with_suffix('.json.tmp');t.write_text(json.dumps(output,indent=2)+'\n');t.replace(p)
    print(json.dumps({k:v for k,v in output.items() if k in ('status','n','q_min','lambda','mu','kernel_dimension','witness','elapsed_seconds')},indent=2),flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--lam',nargs='+',type=int,required=True)
    parser.add_argument('--mu',nargs='+',type=int,required=True);parser.add_argument('--tag',required=True)
    args=parser.parse_args();main(tuple(args.lam),tuple(args.mu),args.tag)
