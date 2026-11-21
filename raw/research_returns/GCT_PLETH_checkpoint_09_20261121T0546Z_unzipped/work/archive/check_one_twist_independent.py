"""Independent full T055/T056 reconstruction from rank-three normal Weyl traces.

Only prior archive audit helpers are imported.  All interpolation, differences,
and multiplicity arithmetic use Python unbounded integers/Fractions.  Third
normal degree is truncated at one because the exact Weyl coefficient has that
bound; no Schur decomposition or proposed pair formula is used for the samples.
"""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import permutations,product
from math import comb,lcm
from pathlib import Path
import hashlib,json,time
import numpy as np
from check_variable_wall_independent import (
    h,selected_types,simplex,binomial_basis,decode,encode,difference,
    CLASSES,CHARS,SIZES,PARTITIONS,
)

HERE=Path(__file__).resolve().parent
THETA=HERE.parent/'theta'/'outer5'/'variable_wall'
SAFE_DEGREES=(5,4,3,2,0,2,0)
DELTA=(2,1,0)
WEYL=tuple((p,(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3)))
           for p in permutations(range(3)))

@lru_cache(None)
def normal(selected,k):
    out={(0,0,0):1}
    for ell in selected:
        new=defaultdict(int)
        for old,value in out.items():
            for z in range((1-old[2])//ell+1):
                for p in range(k-z):
                    for q in range(k-z-p):
                        new[old[0]+ell*p,old[1]+ell*q,old[2]+ell*z]+=value
        out=dict(new)
    return tuple(out.items())

@lru_cache(None)
def literal_trace(g,a,b,k):
    alpha=(a+1,b+1,1)
    total=0
    for selected,rest,orientation in selected_types(CLASSES[g]):
        for exponents,multiplicity in normal(selected,k):
            for permutation,sgn in WEYL:
                indices=tuple(alpha[i]+DELTA[i]-DELTA[permutation[i]]-exponents[i]
                              for i in range(3))
                if min(indices)<0:continue
                value=orientation*multiplicity*sgn
                for index in indices:
                    value*=h(rest,index)
                    if not value:break
                total+=value
    return total

def reconstruct(g,phase):
    period=lcm(*CLASSES[g]);ar,br,kr=phase
    rK=(kr-3)%period;rB=(br-3*rK-6)%period;rX=(ar-br)%period
    residue=(rX,rB,rK);points=simplex(SAFE_DEGREES[g]);values={}
    for q in points:
        X,B,K=(residue[i]+period*q[i] for i in range(3))
        k=K+3;b=3*k-3+B
        values[q]=literal_trace(g,b+X,b,k)
    polynomial=defaultdict(Fraction)
    for order in points:
        constant=0
        for q in product(*(range(j+1) for j in order)):
            factor=(-1)**(sum(order)-sum(q))
            for d,u in zip(order,q):factor*=comb(d,u)
            constant+=factor*values[q]
        if not constant:continue
        bases=[binomial_basis(residue[i],period,order[i]) for i in range(3)]
        for powers in product(*(range(len(base)) for base in bases)):
            c=Fraction(constant)
            for i,p in enumerate(powers):c*=bases[i][p]
            polynomial[powers]+=c
    return {p:c for p,c in polynomial.items() if c},len(points)

def strip_change(poly):
    # Explicit substitution (X,B,K_old)=(X,-1,K+2).
    out=defaultdict(Fraction)
    for (i,j,k),c in poly.items():
        for t in range(k+1):out[i,0,t]+=c*(-1)**j*comb(k,t)*2**(k-t)
    return {p:c for p,c in out.items() if c}

def margins(data,expected,strip=False):
    identity=data[0][(0,0,0)]
    assert all(c>=0 for c in identity.values())
    records=[];active=[]
    orders=(product(range(4),[0],range(5)) if strip
            else product(range(4),range(5),range(6)))
    for order in orders:
        if not any(order):continue
        ident=difference(identity,order);bounds=defaultdict(Fraction)
        for size,phases in zip(SIZES[1:],data[1:]):
            worst={}
            for poly in phases.values():
                for power,c in difference(poly,order).items():
                    worst[power]=max(worst.get(power,Fraction(0)),abs(c))
            for power,c in worst.items():bounds[power]+=size*c
        if not ident and not bounds:continue
        margin={p:ident.get(p,Fraction(0))-bounds.get(p,Fraction(0)) for p in set(ident)|set(bounds)}
        assert all(c>=0 for c in margin.values()),(order,margin)
        assert margin.get((0,0,0),0)>0
        active.append(order);records.append((order,margin))
    assert [list(o) for o in active]==expected['active_orders']
    table={tuple(row['order']):row for row in expected['margins']}
    for order,margin in records:
        assert {p:c for p,c in margin.items() if c}==decode(table[order]['margin'])
        assert margin[(0,0,0)]==Fraction(table[order]['constant'])
        assert min(margin.values())==Fraction(table[order]['minimum'])
    return {'orders':len(active),'minimum_constant_margin':str(min(m[(0,0,0)] for _,m in records)),
            'coefficientwise_margins':{','.join(map(str,o)):encode(m) for o,m in records}}

def residue_cube(data,expected,strip=False):
    if strip:
        X,K=np.indices((60,60),dtype=np.int64).reshape(2,-1)
        B=np.zeros(X.size,dtype=np.int64);coordinates=np.array([X,B,K])
        a=3*K+11+X;b=3*K+11;k=K+5
    else:
        coordinates=np.indices((60,60,60),dtype=np.int64).reshape(3,-1)
        X,B,K=coordinates;a=3*K+6+B+X;b=3*K+6+B;k=K+3
    powers=[[axis.astype(object)**i for i in range(6)] for axis in coordinates]
    traces=[]
    for g,phases in enumerate(data):
        period=lcm(*CLASSES[g])
        denominator=lcm(*(c.denominator for poly in phases.values() for c in poly.values()))
        phase_id=((a%period)*period+b%period)*period+k%period
        result=np.zeros(X.size,dtype=object)
        for phase,poly in phases.items():
            ids=np.flatnonzero(phase_id==(phase[0]*period+phase[1])*period+phase[2])
            value=np.zeros(len(ids),dtype=object)
            for exponents,c in poly.items():
                term=np.full(len(ids),c.numerator*(denominator//c.denominator),dtype=object)
                for axis,p in enumerate(exponents):term*=powers[axis][p][ids]
                value+=term
            assert not np.any(value%denominator)
            result[ids]=value//denominator
        if not strip:assert int(np.max(np.abs(result)))==expected['class_bounds'][g]['maximum_absolute_trace']
        traces.append(result)
    records=[];all_values=[];strip_digest=hashlib.sha256()
    for mu,chi,reference in zip(PARTITIONS,CHARS,expected['labels']):
        numerator=np.zeros(X.size,dtype=object)
        for size,c,trace in zip(SIZES,chi,traces):numerator+=size*c*trace
        assert not np.any(numerator%120)
        values=numerator//120
        assert int(values.min())==reference['minimum']
        assert int(values.max())==reference['maximum']
        assert int(values[0])==reference['origin_value']
        zeros=[list(map(int,coordinates[:,i] if not strip else coordinates[[0,2],i]))
               for i in np.flatnonzero(values==0)]
        assert zeros==reference['zeros']
        assert int(values.min())>=0
        digest=hashlib.sha256(np.ascontiguousarray(values,dtype='<i8').tobytes()).hexdigest()
        if not strip:assert digest==reference['sha256_le_int64']
        records.append({'label':mu,'minimum':int(values.min()),'maximum':int(values.max()),
                        'origin_value':int(values[0]),'zeros':zeros,'sha256_le_int64':digest})
        all_values.append(values)
        if strip:strip_digest.update((repr((tuple(mu),[int(v) for v in values]))+'\n').encode())
    if strip:assert strip_digest.hexdigest()==expected['residue_sha256']
    return {'constants':len(records)*X.size,'labels':records,
            'origin_traces':[int(t[0]) for t in traces],
            'zero_count':sum(len(r['zeros']) for r in records),
            'combined_strip_sha256':strip_digest.hexdigest() if strip else None}

def main():
    start=time.monotonic();source=THETA/'ONE_TWIST_POLYNOMIALS.json'
    expected=json.loads(source.read_text());data=[];samples=0
    for g,cycles in enumerate(CLASSES):
        period=lcm(*cycles);phases={}
        for phase in product(range(period),repeat=3):
            polynomial,count=reconstruct(g,phase)
            assert polynomial==decode(expected['phase_polynomials'][g][','.join(map(str,phase))]),(g,phase)
            phases[phase]=polynomial;samples+=count
        data.append(phases)
        print('PASS class',cycles,len(phases),'exact phase polynomials',flush=True)
    saved=[{','.join(map(str,p)):encode(v) for p,v in row.items()} for row in data]
    (HERE/'ONE_TWIST_POLYNOMIALS_INDEPENDENT.json').write_text(json.dumps(saved,indent=2)+'\n')
    main_margins=margins(data,expected)
    print('PASS T055',main_margins['orders'],'margins',flush=True)
    main_cube=residue_cube(data,json.loads((THETA/'ONE_TWIST_RESIDUE_RECEIPT.json').read_text()))
    print('PASS T055',main_cube['constants'],'base constants',flush=True)
    stripdata=[{p:strip_change(v) for p,v in row.items()} for row in data]
    stripsource=THETA/'ONE_TWIST_STRIP_POLYNOMIALS.json'
    stripexpected=json.loads(stripsource.read_text())
    for row,ref in zip(stripdata,stripexpected['phase_polynomials']):
        assert {','.join(map(str,p)):encode(v) for p,v in row.items()}==ref
    strip_margins=margins(stripdata,stripexpected,True)
    strip_cube=residue_cube(stripdata,json.loads((THETA/'ONE_TWIST_STRIP_RECEIPT.json').read_text()),True)
    # Further literal normal trace checks on the actual B=-1 strip, rather than
    # relying solely on an algebraic substitution into chamber polynomials.
    strip_traces=0
    for X,K in product((0,1,2,5,8),(0,1,3,6)):
        k=K+5;b=3*k-4;a=b+X
        for g,cycles in enumerate(CLASSES):
            L=lcm(*cycles);poly=stripdata[g][(a%L,b%L,k%L)]
            value=sum(c*X**p[0]*K**p[2] for p,c in poly.items())
            assert value==literal_trace(g,a,b,k),(X,K,g)
            strip_traces+=1
    receipt={'statement':'T055/T056 independent complete phase and base reconstruction','status':'PASS',
             'method':'unexpanded rank-three normal-subset Weyl traces with exact third-degree truncation; rational unisolvent interpolation under proved safe bounds; literal step60 polynomial translations; Python-object unbounded residue arithmetic',
             'safe_phase_degrees':SAFE_DEGREES,'phase_polynomials':449,'unisolvent_trace_values':samples,
             'chamber_margins':main_margins,'chamber_cube':main_cube,
             'strip_margins':strip_margins,'strip_cube':strip_cube,'additional_strip_literal_traces':strip_traces,
             'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
             'strip_source_sha256':hashlib.sha256(stripsource.read_bytes()).hexdigest(),
             'elapsed_seconds':time.monotonic()-start}
    (HERE/'ONE_TWIST_INDEPENDENT_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print('PASS',samples,'unisolvent traces;',main_cube['constants']+strip_cube['constants'],
          'base constants;',strip_traces,'literal strip traces',flush=True)

if __name__=='__main__':main()
