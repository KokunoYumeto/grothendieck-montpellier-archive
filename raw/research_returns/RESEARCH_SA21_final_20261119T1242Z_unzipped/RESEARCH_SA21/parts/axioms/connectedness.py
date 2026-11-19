"""Exhaustive finite checks of the component theorem, standard-library Python.
GPT-6 Astra (OpenAI), /root/axioms, 2026-11-19. No priority claim.
The proof for arbitrary sets is in axioms.tex; these checks are independent.
"""
from itertools import combinations
from time import perf_counter

def admissible(f):
    supp=0
    for a in f:supp|=a
    for a in f:
        lower=0
        for b in f:
            if b!=a and b&a==b:lower|=b
        if a&~lower==0:return False
    for i in range(supp.bit_length()):
        if supp>>i&1:
            members=[a for a in f if a>>i&1]
            if not any(all(a&b==a for b in members) for a in members):return False
    return True

def run(n):
    L=(1<<n)-1;sets=list(range(1,L+1))
    elements=[]
    for mask in range(1<<len(sets)):
        f=frozenset(sets[i] for i in range(len(sets)) if mask>>i&1)
        if f and admissible(f) and any(all(b&a==b for b in f) for a in f):elements.append(f)
    index={f:i for i,f in enumerate(elements)};parent=list(range(len(elements)))
    def find(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    def union(i,j):parent[find(i)]=find(j)
    for i,f in enumerate(elements):
        for a in f:
            g=frozenset(b for b in f if b&a==b)
            assert g in index
            union(i,index[g])
    comps={}
    for i,f in enumerate(elements):comps.setdefault(find(i),set()).add(f)
    got={frozenset(c) for c in comps.values()}
    expected=set()
    if n:
        expected.add(frozenset({frozenset({L})}))
    exceptions=set().union(*expected) if expected else set()
    if n>=2:
        for i in range(n):
            A=L^(1<<i);c=frozenset({frozenset({A}),frozenset({A,L})})
            expected.add(c);exceptions.update(c)
    rest=frozenset(set(elements)-exceptions)
    if rest:expected.add(rest)
    assert got==expected,(n,got,expected)
    print('n=',n,'elementary figures=',len(elements),'components=',len(got),'component sizes=',sorted(map(len,got)))
    if n>=2:
        isolated=frozenset({L});point=frozenset({1})
        assert find(index[isolated])!=find(index[point])
        # These elementary families have overlapping support but common
        # closed-subfamily intersection empty; hence are incompatible.
        assert isolated.isdisjoint(point)
        assert L&1

if __name__=='__main__':
    t=perf_counter()
    for n in range(5):run(n)
    print('complete component classification and C4 witnesses PASS')
    print('seconds',perf_counter()-t)
