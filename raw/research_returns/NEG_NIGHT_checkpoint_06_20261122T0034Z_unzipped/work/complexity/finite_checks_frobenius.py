#!/usr/bin/env python3
"""Finite certificate for C023's exact coefficient and projective parity identities.

This does not execute E, compute a sheaf resolution, or substitute for the
general Cech proof. It exhausts all two-variable clause subsets and additional
seeded small formulas, using integer coefficient extraction before reduction.
"""
import itertools, json, random
from pathlib import Path

def factors_for(n, clauses):
    relations=[]
    used=set()
    for clause in clauses:
        scope=tuple(i for i,sign in clause)
        used.update(scope)
        allowed=[a for a in itertools.product((0,1),repeat=len(scope))
                 if any(a[j]==sign for j,(i,sign) in enumerate(clause))]
        relations.append((scope,allowed))
    for i in range(n):
        if i not in used:relations.append(((i,),[(0,),(1,)]))
    occurrences=[[] for _ in range(n)]
    factors=[]
    e=0
    for scope,allowed in relations:
        labels=list(range(e,e+len(scope)));e+=len(scope)
        for i,label in zip(scope,labels):occurrences[i].append(label)
        factors.append([sum(1<<(2*label+bit) for label,bit in zip(labels,a))
                        for a in allowed])
    for incident in occurrences:
        assert incident
        factors.append([sum(1<<(2*label+bit) for label in incident)
                        for bit in (0,1)])
    return factors,2*e

def coefficient(factors,rail_count):
    dp={0:1}
    for terms in factors:
        nxt={}
        for mask,c in dp.items():
            for term in terms:
                if mask&term:continue
                z=mask|term;nxt[z]=nxt.get(z,0)+c
        dp=nxt
    return dp.get((1<<rail_count)-1,0)

def satcount(n,clauses):
    return sum(all(any(x[i]==sign for i,sign in clause) for clause in clauses)
               for x in itertools.product((0,1),repeat=n))

def run():
    cases=point_cases=0
    dimensions=set()
    universe=[]
    for codes in itertools.product((-1,0,1),repeat=2):
        if all(c==-1 for c in codes):continue
        universe.append(tuple((i,c) for i,c in enumerate(codes) if c!=-1))
    formulas=[]
    for selected in range(1<<len(universe)):
        formulas.append((2,[c for j,c in enumerate(universe) if selected>>j&1]))
    rng=random.Random(20261121)
    for n in (3,4,5):
        for _ in range(24):
            clauses=[]
            for _ in range(rng.randrange(1,5)):
                scope=sorted(rng.sample(range(n),rng.randrange(1,min(n,3)+1)))
                clauses.append(tuple((i,rng.randrange(2)) for i in scope))
            formulas.append((n,clauses))
    for n,clauses in formulas:
        fs,d=factors_for(n,clauses)
        c=coefficient(fs,d);expected=satcount(n,clauses)
        assert c==expected,(n,clauses,c,expected)
        cases+=1;dimensions.add(d+1)
        if d<=8:
            p_nonzero=0
            for assignment in range(1<<d):
                value=1
                for terms in fs:
                    value&=sum((assignment&t)==t for t in terms)%2
                p_nonzero+=value
            projective_count=(1<<(d+1))-1-p_nonzero
            assert projective_count%2==(1+c)%2
            point_cases+=1
    # Empty-clause and zero-variable replacements: nonzero cubics in P^2.
    for monomial_mask,expected in [(1,0),(7,1)]:
        count=sum(not((x&monomial_mask)==monomial_mask) for x in range(1,8))
        assert count%2==(1+expected)%2
        point_cases+=1
    result={'result':'pass','integer_coefficient_cases':cases,
            'projective_point_parity_cases':point_cases,
            'ambient_variable_counts':sorted(dimensions),
            'scope':'C023 finite coefficient and F2-point identities only; no E execution or formal cohomology verification'}
    Path(__file__).with_name('FINITE_CHECK_FROBENIUS_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__':run()
