#!/usr/bin/env python3
"""Finite ordinary-polynomial checks for C029; this does not execute E."""
import itertools, json, pathlib, random
import sympy as sp

BASE=pathlib.Path(__file__).resolve().parent
rng=random.Random(290627)
counts={'local_divisions':0,'ordinary_verifier_certificates':0,
        'ordinary_cnf_certificates':0,'boolean_assignments_examined':0}

def basis(xs,bits):
    return sp.prod(x if b else 1-x for x,b in zip(xs,bits))

def divide_boolean(p,xs):
    """Return q with p-ML(p)=sum_j q_j*(x_j^2-x_j), over ZZ."""
    q=[sp.Integer(0) for _ in xs]
    for alpha,coeff in sp.Poly(sp.expand(p),*xs,domain=sp.ZZ).terms():
        eps=tuple(min(a,1) for a in alpha)
        for j,a in enumerate(alpha):
            if a<2: continue
            outside=sp.prod(xs[l]**(eps[l] if l<j else alpha[l])
                            for l in range(len(xs)) if l!=j)
            q[j]+=coeff*outside*sum(xs[j]**r for r in range(a-1))
    return [sp.expand(t) for t in q]

def check_verifier(xs,fs):
    v=len(xs)
    ai=[sp.Integer(0) for _ in fs]
    for bits in itertools.product((0,1),repeat=v):
        counts['boolean_assignments_examined']+=1
        values=[int(f.subs(dict(zip(xs,bits)))) for f in fs]
        assert all(t in (-1,0,1) for t in values)
        bad=next((i for i,t in enumerate(values) if t),None)
        assert bad is not None
        ai[bad]+=values[bad]*basis(xs,bits)
    ai=list(map(sp.expand,ai))
    corrections=[sp.Integer(0) for _ in xs]
    for i,f in enumerate(fs):
        local=tuple(x for x in xs if x in f.free_symbols)
        assert len(local)<=3
        for sig in itertools.product((0,1),repeat=len(local)):
            fixed=dict(zip(local,sig))
            delta=sp.expand(basis(local,sig)*(f-f.subs(fixed)))
            qs=divide_boolean(delta,local) if local else []
            assert sp.expand(delta-sum(q*(x*x-x) for q,x in zip(qs,local)))==0
            assert all(q==0 or sp.Poly(q,*local).total_degree()<=len(local) for q in qs)
            counts['local_divisions']+=1
            A=sp.expand(ai[i].subs(fixed))
            for x,q in zip(local,qs):
                corrections[xs.index(x)]+=A*q
    final=list(ai)
    for j,x in enumerate(xs):
        index=next(i for i,f in enumerate(fs) if sp.expand(f-(x*x-x))==0)
        final[index]=sp.expand(final[index]-corrections[j])
    assert sp.expand(sum(a*f for a,f in zip(final,fs))-1)==0
    assert all(a==0 or sp.Poly(a,*xs).total_degree()<=v for a in final)
    assert all(sp.Poly(a,*xs,domain=sp.ZZ) is not None for a in final)
    counts['ordinary_verifier_certificates']+=1

for v in range(1,6):
    xs=sp.symbols('x0:'+str(v))
    for case in range(5):
        local=[]
        for _ in range(v+2):
            a,b,c=(rng.choice(xs) for _ in range(3))
            local.append(sp.expand(c-a*b if rng.randrange(2) else c+a-1))
        # Contradictory unary relations ensure unsatisfiability; the proof uses
        # only the explicitly asserted local/unit-valued polynomial properties.
        local += [xs[0],xs[0]-1]
        rng.shuffle(local)
        check_verifier(xs,[x*x-x for x in xs]+local)

# One literal AND/NOT verification circuit for x AND (NOT x), forced to accept.
xs=sp.symbols('x0:3')
check_verifier(xs,[x*x-x for x in xs]+[xs[1]+xs[0]-1,
                                     xs[2]-xs[0]*xs[1],xs[2]-1])

def check_cnf(xs,clauses):
    # A clause is stored by its distinct variable indices and falsifying bits.
    gs=[basis(tuple(xs[j] for j in I),sig) for I,sig in clauses]
    multipliers=[]
    for i,(I,sig) in enumerate(clauses):
        free=tuple(j for j in range(len(xs)) if j not in I)
        A=sp.Integer(0)
        for bits in itertools.product((0,1),repeat=len(free)):
            counts['boolean_assignments_examined']+=1
            assignment=dict(zip((xs[j] for j in I),sig))
            assignment.update(zip((xs[j] for j in free),bits))
            weight=sp.prod(1-g.subs(assignment) for g in gs[:i])
            A+=weight*basis(tuple(xs[j] for j in free),bits)
        A=sp.expand(A)
        assert A==0 or sp.Poly(A,*xs).total_degree()<=len(xs)-len(I)
        multipliers.append(A)
    assert sp.expand(sum(A*g for A,g in zip(multipliers,gs))-1)==0
    counts['ordinary_cnf_certificates']+=1

for n in range(1,6):
    xs=sp.symbols('x0:'+str(n))
    for case in range(5):
        clauses=[]
        for _ in range(2*n):
            I=tuple(sorted(rng.sample(range(n),rng.randrange(1,min(n,3)+1))))
            clauses.append((I,tuple(rng.randrange(2) for _ in I)))
        clauses.extend([((0,),(0,)),((0,),(1,))])
        rng.shuffle(clauses)
        check_cnf(xs,clauses)
    k=min(n,3)
    check_cnf(xs,[(tuple(range(k)),sig) for sig in itertools.product((0,1),repeat=k)])

result={'finding':'NN-C029','result':'all assertions passed','counts':counts,
        'method':'Exact expanded polynomial comparison over ZZ, after local monomial division and first-violation construction',
        'limitations':'Finite examples only; does not run E, bound its circuit cost, prove IPS verification efficient, or establish a positive-characteristic circuit transfer.'}
(BASE/'FINITE_CHECK_IPS_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
