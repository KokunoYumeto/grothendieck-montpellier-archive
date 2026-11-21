#!/usr/bin/env python3
"""Exact direct-cofactor certificate for M015; finite checks supplement its proof."""
from pathlib import Path
from itertools import combinations_with_replacement
from functools import lru_cache
import json, math, time
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]

def graph(R):
    pairs=list(combinations_with_replacement(range(R),2))
    vertices=[('root',)]+[('v',i) for i in range(R)]
    vertices += [('p',i,j) for i,j in pairs]+[('q',i,j) for i,j in pairs]
    idx={v:i for i,v in enumerate(vertices)}
    z=sp.symbols('z0:'+str(R))
    A=sp.eye(len(vertices))
    def edge(a,b,label):A[idx[a],idx[b]]-=label
    for i in range(R):
        edge(('v',i),('root',),z[i])
        edge(('root',),('v',i),z[(i+1)%R])
    for i,j in pairs:
        edge(('p',i,j),('v',i),z[j])
        edge(('v',(j-1)%R),('q',i,j),z[i])
    return A,z,idx,pairs

def candidates(R,idx,pairs):
    # Each record is a desired cofactor monomial and its actual matrix-entry direction.
    out={(): (idx[('root',)],idx[('root',)])}
    for k in range(R):
        out[((k+1)%R,)]=(idx[('v',k)],idx[('root',)])
    for i in range(R):
        for k in range(R):
            if i!=k:
                out[tuple(sorted((i,(k+1)%R)))]=(idx[('v',k)],idx[('v',i)])
    for i,j in pairs:
        for a,b in pairs:
            if i!=(b-1)%R:
                out[tuple(sorted((i,j,a,b)))]=(idx[('q',a,b)],idx[('p',i,j)])
    for degree in (0,1,2,4):
        assert all(t in out for t in combinations_with_replacement(range(R),degree))
    return out

def direct_case(R):
    A,z,idx,pairs=graph(R)
    target=candidates(R,idx,pairs)
    expected=1-sum(z[i]*z[(i+1)%R] for i in range(R))
    assert sp.expand(A.det(method='domain-ge')-expected)==0
    @lru_cache(None)
    def cofactor(row,col):
        return sp.expand((-1)**(row+col)*A.minor_submatrix(row,col).det(method='domain-ge'))
    for mon,(row,col) in target.items():
        actual=cofactor(row,col)
        wanted=sp.prod(z[i] for i in mon)
        assert sp.expand(actual-wanted)==0,(R,mon,actual)
    directions={}
    for degree in range(6):
        for mon in combinations_with_replacement(range(R),degree):
            if degree in (3,5):
                linear=mon[0]
                base=mon[1:]
            else:
                linear=None
                base=mon
            row,col=target[base]
            direction=(row,col,linear)
            assert direction not in directions
            directions[direction]=mon
            actual=cofactor(row,col)*(1 if linear is None else z[linear])
            assert sp.expand(actual-sp.prod(z[i] for i in mon))==0
    expected_rank=math.comb(R+5,5)
    assert len(directions)==expected_rank
    return {'R':R,'r':R+1,'matrix_size':A.rows,'target_dimension':expected_rank,
            'direct_cofactors_checked':len(target),'unit_jacobian_minor':True,
            'constant_and_quadratic_base_determinant_checked':True}

if __name__=='__main__':
    started=time.time()
    checks=[]
    for R in (3,4):
        result=direct_case(R)
        checks.append(result)
        print(json.dumps(result),flush=True)
    coverage=[]
    for R in range(3,21):
        pairs=list(combinations_with_replacement(range(R),2))
        # Only the vertex index set is needed for the larger combinatorial checks.
        vertices=[('root',)]+[('v',i) for i in range(R)]
        vertices += [('p',i,j) for i,j in pairs]+[('q',i,j) for i,j in pairs]
        target=candidates(R,{v:i for i,v in enumerate(vertices)},pairs)
        coverage.append({'R':R,'monomial_cofactors':len(target)})
    result={'finding':'M-015','method':'Exact symbolic minors of the full pencils, plus finite monomial-cover checks',
            'direct_cases':checks,'coverage_cases':coverage,'all_passed':True,
            'elapsed_seconds':time.time()-started,'scope':'Finite certificate; general proof is cyclic_star_jets.tex'}
    (ROOT/'checks/cyclic_star_jet_certificate.json').write_text(json.dumps(result,indent=2))
    print(json.dumps({'all_passed':True,'elapsed_seconds':result['elapsed_seconds']}),flush=True)
