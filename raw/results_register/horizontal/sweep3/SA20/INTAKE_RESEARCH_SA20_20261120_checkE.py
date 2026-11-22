"""Independent checks of RESEARCH_SA20 Part E (E.003-E.006, E.012) for the intake of 20 Nov 2026.
Claude Opus 5.5 at effort max (acf08879a01b97ed4)."""
import itertools as it
from collections import Counter
def comp(p, q): return tuple(p[i] for i in q)
def sign(p):
    n=len(p); seen=[0]*n; c=0
    for i in range(n):
        if not seen[i]:
            c+=1; j=i
            while not seen[j]: seen[j]=1; j=p[j]
    return (-1)**(n-c)
S6=list(it.permutations(range(6)))
duads=[frozenset(d) for d in it.combinations(range(6),2)]
syn=set()
for a in duads:
    for b in duads:
        if a&b: continue
        syn.add(frozenset([a,b,frozenset(range(6))-a-b]))
syn=list(syn)
totals=[frozenset(f) for f in it.combinations(syn,5) if len({d for s in f for d in s})==15]
tot_sorted=sorted(totals,key=lambda t: sorted(sorted(sorted(d) for d in s) for s in t))
tix={t:i for i,t in enumerate(tot_sorted)}
def ad(s,d): return frozenset(s[x] for x in d)
def asy(s,y): return frozenset(ad(s,d) for d in y)
PH={s:tuple(tix[frozenset(asy(s,y) for y in t)] for t in tot_sorted) for s in S6}
# (1) hexagons and bihexagons
hexes=set()
for p in it.permutations(range(1,6)):
    cyc=(0,)+p
    edges=frozenset(frozenset((cyc[i],cyc[(i+1)%6])) for i in range(6))
    hexes.add(edges)
hexes=list(hexes)
bih=[(i,j) for i in range(len(hexes)) for j in range(i+1,len(hexes)) if not (hexes[i]&hexes[j])]
adj={i:set() for i in range(len(hexes))}
for i,j in bih: adj[i].add(j); adj[j].add(i)
comps=[]; seen=set()
for i in range(len(hexes)):
    if i in seen: continue
    st=[i]; c={i}
    while st:
        x=st.pop()
        for y in adj[x]:
            if y not in c: c.add(y); st.append(y)
    seen|=c; comps.append(c)
deg=Counter(len(adj[i]) for i in adj)
# Petersen check: 10 vertices, 3-regular, girth 5 (no triangles, no 4-cycles)
def girth_ok(c):
    for x in c:
        for y in adj[x]:
            if adj[x]&adj[y]: return False
    for x in c:
        for y in c:
            if x<y and y not in adj[x] and len(adj[x]&adj[y])>1: return False
    return True
# component -> total: the synthemes of a hexagon (its two alternating matchings)
def hex_synthemes(h):
    # recover cyclic order
    nb={v:[] for v in range(6)}
    for e in h:
        a,b=tuple(e); nb[a].append(b); nb[b].append(a)
    cyc=[0,nb[0][0]]
    while len(cyc)<6:
        nxt=[v for v in nb[cyc[-1]] if v!=cyc[-2]][0]; cyc.append(nxt)
    m1=frozenset(frozenset((cyc[i],cyc[i+1])) for i in (0,2,4))
    m2=frozenset(frozenset((cyc[i],cyc[(i+1)%6])) for i in (1,3,5))
    return {m1,m2}
comp_tot=[]
for c in comps:
    sy=set()
    for h in c: sy|=hex_synthemes(hexes[h])
    comp_tot.append(frozenset(sy) in totals)
print("(1) hexagons:",len(hexes),"bihexagons:",len(bih),"components:",len(comps),"sizes:",sorted(len(c) for c in comps),
      "degrees:",dict(deg),"Petersen (3-regular, girth 5):",all(girth_ok(c) for c in comps),
      "each component's synthemes form a total:",all(comp_tot))
# (2) the hemi-icosahedron model of E.004
F0=[frozenset(map(int,s)) for s in "012 015 023 034 045 124 134 135 235 245".split()]
edge_ct=Counter(frozenset(e) for f in F0 for e in it.combinations(sorted(f),2))
link_ok=True
for v in range(6):
    lk=[f-{v} for f in F0 if v in f]
    g={u:set() for u in range(6) if u!=v}
    for e in lk:
        a,b=tuple(e); g[a].add(b); g[b].add(a)
    if not all(len(x)==2 for x in g.values()): link_ok=False
compl_ok=all(((frozenset(range(6))-t) in F0)!=(t in F0) for t in map(frozenset,it.combinations(range(6),3)))
orbit=set()
for s in S6: orbit.add(frozenset(frozenset(s[x] for x in f) for f in F0))
stab=[s for s in S6 if frozenset(frozenset(s[x] for x in f) for f in F0)==frozenset(F0)]
print("(2) every edge in 2 faces:",set(edge_ct.values())=={2},"; 15 edges:",len(edge_ct),"; vertex links are 5-cycles:",link_ok,
      "; exactly one of each complementary pair is a face:",compl_ok,"; S6-orbit:",len(orbit),"; stabilizer order:",len(stab),
      "all even:",all(sign(s)==1 for s in stab),"transitive:",len({s[0] for s in stab})==6)
# biicosahedra: complement pairs; map to totals via stabilizer: stabilizer of the pair is a transitive S5 = point stabilizer of a total
bi=set()
for o in orbit:
    co=frozenset(frozenset(range(6))-f for f in o)
    bi.add(frozenset([o,co]))
print("    complementary pairs (biicosahedra):",len(bi))
# (3) the square twist of E.006
Q=(0,1,2,3); eps=(4,5)
diag=[frozenset([0,2]),frozenset([1,3])]
def pres(s): return frozenset(s[x] for x in Q)==frozenset(Q) and frozenset(frozenset(s[x] for x in d) for d in diag)==frozenset(diag)
H=[s for s in S6 if pres(s)]
img=[PH[s] for s in H]
orbs={}
for i in range(6): orbs.setdefault(frozenset(g[i] for g in img),None)
orbs=list(orbs)
Qs=[o for o in orbs if len(o)==4][0]
sides=[frozenset([0,1]),frozenset([1,2]),frozenset([2,3]),frozenset([0,3])]
def twist_classes(kind):
    # elements: (e, c) with e in eps, c a side (kind='side') or a vertex (kind='vertex'), modulo (e,c)~(e',opposite c)
    if kind=='side':
        objs=sides; opp=lambda c: sides[(sides.index(c)+2)%4]; act=lambda s,c: frozenset(s[x] for x in c)
    else:
        objs=list(Q); opp=lambda c: (c+2)%4; act=lambda s,c: s[c]
    cls={}
    for e in eps:
        for c in objs:
            key=frozenset([(e,c),(4 if e==5 else 5,opp(c))])
            cls[key]=None
    cls=list(cls)
    def actcls(s,k):
        (e,c)=sorted(k,key=str)[0]
        img_=(s[e],act(s,c))
        return [kk for kk in cls if img_ in kk][0]
    return cls, actcls
for kind in ('side','vertex'):
    cls,actcls=twist_classes(kind)
    Ql=sorted(Qs)
    n_eq=0
    for perm in it.permutations(Ql):
        f=dict(zip(cls,perm))
        if all(PH[s][f[k]]==f[actcls(s,k)] for s in H for k in cls): n_eq+=1
    print("(3) equivariant bijections Q* <-> eps ^ (%s square):"%kind, n_eq)
# (4) Harer-Zagier numbers for n=7 by direct enumeration of one-face gluings of a 14-gon
def pairings(lst):
    if not lst: yield []; return
    a=lst[0]
    for i in range(1,len(lst)):
        b=lst[i]; rest=lst[1:i]+lst[i+1:]
        for p in pairings(rest): yield [(a,b)]+p
n=7; cnt=Counter()
tau=tuple((i+1)%(2*n) for i in range(2*n))
for p in pairings(list(range(2*n))):
    al=[0]*(2*n)
    for a,b in p: al[a]=b; al[b]=a
    sig=tuple(tau[al[i]] for i in range(2*n))   # sigma = tau o alpha
    seen=[0]*(2*n); c=0
    for i in range(2*n):
        if not seen[i]:
            c+=1; j=i
            while not seen[j]: seen[j]=1; j=sig[j]
    cnt[(n+1-c)//2]+=1
print("(4) genus distribution of one-face gluings, m=7:",dict(sorted(cnt.items())),"total",sum(cnt.values()))
