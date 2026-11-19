"""Exact finite certificate for A.207's noninjective annulus attachment.
The abstract complex models the mapping cylinder of C4 -> C3 with
b0,b1 -> c0; b2 -> c1; b3 -> c2. The quotient parametrization is
semialgebraic, not asserted PL on the collapsed prism.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations

T = [('b0','b1','c0'), ('b1','b2','c0'), ('b2','c1','c0'),
     ('b2','b3','c1'), ('b3','c2','c1'), ('b3','b0','c2'),
     ('b0','c0','c2')]
V = sorted({v for t in T for v in t})
E = sorted({tuple(sorted(e)) for t in T for e in combinations(t,2)})
counts = Counter(tuple(sorted(e)) for t in T for e in combinations(t,2))
checks = 0

def check(predicate, label):
    global checks
    assert predicate, label
    checks += 1
    print('PASS\t'+label)

def connected(vertices, edges):
    adj = {v:set() for v in vertices}
    for a,b in edges: adj[a].add(b); adj[b].add(a)
    if not vertices: return False
    seen={next(iter(vertices))}; todo=list(seen)
    while todo:
        for w in adj[todo.pop()]-seen: seen.add(w); todo.append(w)
    return seen==set(vertices)

check((len(V),len(E),len(T))==(7,14,7), 'f-vector (7,14,7)')
check(len(set(map(frozenset,T)))==7, 'all seven triangles distinct')
check(connected(V,E), 'complex connected')
check(set(counts.values())=={1,2}, 'each edge in one or two triangles')
check(len(V)-len(E)+len(T)==0, 'Euler characteristic zero')
for v in V:
    edges=[tuple(x for x in t if x!=v) for t in T if v in t]
    vs={x for e in edges for x in e}
    degrees=Counter(x for e in edges for x in e)
    check(connected(vs,edges) and len(edges)==len(vs)-1 and
          sorted(degrees.values())==[1,1]+[2]*(len(vs)-2),
          'vertex link is an interval: '+v)
B={e for e,n in counts.items() if n==1}
Btop={tuple(sorted(('b'+str(i),'b'+str((i+1)%4)))) for i in range(4)}
Bbottom={tuple(sorted(('c'+str(i),'c'+str((i+1)%3)))) for i in range(3)}
check(B==Btop|Bbottom and Btop.isdisjoint(Bbottom), 'boundary exactly disjoint C4 and C3')
orient=defaultdict(list)
for t in T:
    for a,b in ((t[0],t[1]),(t[1],t[2]),(t[2],t[0])):
        orient[tuple(sorted((a,b)))].append(1 if a<b else -1)
check(all(sum(orient[e])==0 for e,n in counts.items() if n==2), 'listed triangle orientations agree on shared edges')
check(all(sum(orient[e]) in {-1,1} for e in B), 'oriented boundary coefficients are units')

# Exact rational boundary matrices and chain-complex ranks.
def rank(A):
    A=[[Fraction(x) for x in row] for row in A]
    i=0
    for j in range(len(A[0]) if A else 0):
        p=next((k for k in range(i,len(A)) if A[k][j]),None)
        if p is None: continue
        A[i],A[p]=A[p],A[i]
        c=A[i][j]; A[i]=[x/c for x in A[i]]
        for k in range(len(A)):
            if k!=i and A[k][j]:
                c=A[k][j]; A[k]=[x-c*y for x,y in zip(A[k],A[i])]
        i+=1
    return i
D1=[[int(v==e[1])-int(v==e[0]) for e in E] for v in V]
D2=[]
for e in E:
    row=[]
    for a,b,c in T:
        terms=((a,b),(b,c),(c,a))
        row.append(sum((1 if x<y else -1) for x,y in terms if tuple(sorted((x,y)))==e))
    D2.append(row)
check(all(sum(D1[i][k]*D2[k][j] for k in range(len(E)))==0 for i in range(len(V)) for j in range(len(T))), 'boundary squared zero exactly')
check((rank(D1),rank(D2))==(6,7), 'exact boundary ranks (6,7), hence Betti numbers (1,1,0)')
print(f'{checks} assertions passed; connected orientable surface, two boundary circles, Euler characteristic 0: annulus.')
