"""Exact marked free basis of Gamma_0(6)/+- and its Atkin--Lehner w_3.

No external algebra packages are used.  The Bass--Serre coset graph is
constructed from the two projective-line actions mod 2 and mod 3.
"""
from collections import deque
from fractions import Fraction
import json
from pathlib import Path

OUT = Path(__file__).parent
S = (0,1,-1,0)
R = (0,-1,1,-1)
I = (1,0,0,1)

def mul(a,b):
    return (a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3])

def inv(a):
    d=a[0]*a[3]-a[1]*a[2]
    return tuple(Fraction(x,d) for x in (a[3],-a[1],-a[2],a[0]))

def pm(a):
    for v in a:
        if v:
            return tuple(x if v>0 else -x for x in a)

def wmat(w):
    m=I
    for x in w:
        m=mul(m, S if x==1 else R if x==2 else mul(R,R))
    return pm(m)

def winv(w):
    return tuple(1 if x==1 else -x for x in w[::-1])

def red(w):
    st=[]
    for x in w:
        if st and st[-1]==1 and x==1:
            st.pop()
        elif st and abs(st[-1])==2 and abs(x)==2:
            v=st.pop()//2+x//2
            v%=3
            if v: st.append(2 if v==1 else -2)
        else: st.append(x)
    return tuple(st)

def rownorm(v,p):
    v=tuple(a%p for a in v)
    q=next(a for a in v if a)
    return tuple(a*pow(q,-1,p)%p for a in v)

def state(m):
    return (rownorm(m[2:],2),rownorm(m[2:],3))

def act(q,g):
    return tuple(rownorm((u*g[0]+v*g[2],u*g[1]+v*g[3]),p)
                 for (u,v),p in zip(q,(2,3)))

q0=state(I)
states=[q0]
seen={q0}
for q in states:
    for g in (S,R):
        v=act(q,g)
        if v not in seen: seen.add(v);states.append(v)
assert len(states)==12
ss={q:act(q,S) for q in states}
rr={q:act(q,R) for q in states}
assert all(ss[ss[q]]==q and ss[q]!=q for q in states)
assert all(rr[rr[rr[q]]]==q and rr[q]!=q for q in states)

orbits=[]; oi={}
for q in states:
    if q in oi:continue
    ob=(q,rr[q],rr[rr[q]])
    for t in ob:oi[t]=len(orbits)
    orbits.append(ob)
assert len(orbits)==4

# A maximal tree: two r-edges in each r-orbit, plus three s-edges
# connecting the four r-orbits.
treeadj={q:[] for q in states}
for q,a,b in orbits:
    for u,v,g in ((q,a,2),(a,b,2)):
        treeadj[u].append((v,g));treeadj[v].append((u,-g))
se=[]
for q in states:
    if states.index(q)<states.index(ss[q]):se.append((q,ss[q]))
parent=list(range(4))
def find(x):
    while parent[x]!=x:x=parent[x]
    return x
non=[]
for q,t in se:
    a,b=find(oi[q]),find(oi[t])
    if a!=b:
        parent[a]=b
        treeadj[q].append((t,1));treeadj[t].append((q,1))
    else:non.append((q,t))
assert len(non)==3
paths={q0:()}
todo=deque([q0])
while todo:
    q=todo.popleft()
    for t,g in treeadj[q]:
        if t not in paths:paths[t]=paths[q]+(g,);todo.append(t)
assert len(paths)==12

letters={}
for i,(q,t) in enumerate(non,1):letters[q]=i;letters[t]=-i
basis=[red(paths[q]+(1,)+winv(paths[t])) for q,t in non]

def freered(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return tuple(out)

def rewrite(w):
    q=q0;out=[]
    for x in w:
        if x==1:
            if q in letters:out.append(letters[q])
            q=ss[q]
        else:
            for _ in range(1 if x==2 else 2):q=rr[q]
    assert q==q0,(w,q)
    return freered(out)

def expand(w):
    out=()
    for x in w:out+=basis[x-1] if x>0 else winv(basis[-x-1])
    return red(out)

assert [rewrite(w) for w in basis]==[(1,),(2,),(3,)]
for q in states:
    assert rewrite(paths[q]+(1,1)+winv(paths[q]))==()
    assert rewrite(paths[q]+(2,2,2)+winv(paths[q]))==()

# Euclidean reduction in PSL2(Z). U = [[1,1],[0,1]] = r^-1 s.
U=(1,1,0,1)
Uword=(-2,1)
assert wmat(Uword)==U
def powword(w,n):return w*n if n>=0 else winv(w)*(-n)
def frommatrix(a):
    a=tuple(int(x) for x in a);original=pm(a);left=()
    assert a[0]*a[3]-a[1]*a[2]==1
    while a[2]:
        q=a[0]//a[2]
        a=mul((1,-q,0,1),a);left=powword(Uword,-q)+left
        a=mul(S,a);left=(1,)+left
    if a[0]<0:a=tuple(-x for x in a)
    assert a[0]==a[3]==1
    w=red(winv(left)+powword(Uword,a[1]))
    assert wmat(w)==original,(w,wmat(w),original)
    return w

W=(3,-2,6,-3)
images=[]
for w in basis:
    m=mul(mul(W,wmat(w)),inv(W))
    assert all(v.denominator==1 for v in m)
    im=rewrite(frommatrix(m));images.append(im)
    assert wmat(expand(im))==pm(m)

def subst(w,ims):
    out=()
    for x in w:
        im=ims[abs(x)-1]
        if x<0:im=tuple(-t for t in im[::-1])
        out+=im
    return freered(out)

W2=tuple(int(x/3) for x in mul(W,W))
c=rewrite(frommatrix(W2))
for i,im in enumerate(images,1):
    assert subst(im,images)==freered(c+(i,)+tuple(-t for t in c[::-1]))

data={
    's':S,'r':R,'u':U,'w3':W,
    'cosets':states,'s_permutation':[states.index(ss[q]) for q in states],
    'r_permutation':[states.index(rr[q]) for q in states],
    'tree_transversals':[paths[q] for q in states],
    'non_tree_s_edges':[(states.index(q),states.index(t)) for q,t in non],
    'basis_sr_words':basis,'basis_matrices':[wmat(w) for w in basis],
    'w3_images_free_words':images,'w3_square_inner_word':c,
    'w3_square_matrix':W2,
    'homology_w3':[[sum(1 if x==j else -1 if x==-j else 0 for x in images[i])
                     for i in range(3)] for j in range(1,4)],
    'checks':['12 cosets','four 3-cycles and six 2-cycles',
              'three generator Bass--Serre free basis',
              'exact matrix conjugations','w3 squared is stated inner automorphism']
}
(OUT/'level6_words.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
