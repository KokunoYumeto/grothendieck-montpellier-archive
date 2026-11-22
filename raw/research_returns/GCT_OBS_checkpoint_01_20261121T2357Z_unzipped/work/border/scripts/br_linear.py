"""Small exact linear algebra and tensor construction; Python standard library.
Coordinates are sparse dictionaries. p=0 means Q; p prime means F_p.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations

PAIRS = tuple(combinations(range(4), 2))
RECTS = tuple((I, J) for I in PAIRS for J in PAIRS)
NONUNIT_PIVOTS = set()


def add(u, v): return tuple(x+y for x,y in zip(u,v))
def neg(u): return tuple(-x for x in u)
def varwt(v): return tuple(int(i==v//4) for i in range(4))+tuple(int(i==v%4) for i in range(4))
def quadwt(q): return tuple(int(i in RECTS[q][0]) for i in range(4))+tuple(int(i in RECTS[q][1]) for i in range(4))


class Space:
    def __init__(self, p=0): self.p, self.rows = p, {}
    def reduce(self, v):
        p=self.p
        v={i:x%p for i,x in v.items() if x%p} if p else {i:Fraction(x) for i,x in v.items() if x}
        for pivot, row in sorted(self.rows.items()):
            x=v.get(pivot,0)
            if not x: continue
            for j,y in row.items():
                z=v.get(j,0)-x*y
                if p: z%=p
                if z: v[j]=z
                else: v.pop(j,None)
        return v
    def append(self,v):
        v=self.reduce(v)
        if not v:return False
        i=min(v);x=v[i]
        if not self.p:
            NONUNIT_PIVOTS.update(n for n in (abs(x.numerator),x.denominator) if n>1)
        inv=pow(x,-1,self.p) if self.p else 1/x
        v={j:(y*inv%self.p if self.p else y*inv) for j,y in v.items()}
        self.rows[i]=v
        return True
    def rank(self):return len(self.rows)
    def canonical(self):
        reduced={}
        for i,row in sorted(self.rows.items(),reverse=True):
            v=dict(row)
            for j,other in sorted(reduced.items()):
                x=v.get(j,0)
                if not x:continue
                for k,y in other.items():
                    z=v.get(k,0)-x*y
                    if self.p:z%=self.p
                    if z:v[k]=z
                    else:v.pop(k,None)
            reduced[i]=v
        return tuple(tuple(sorted(v.items())) for i,v in sorted(reduced.items()))


def rank(vectors,p=0):
    s=Space(p)
    for v in vectors:s.append(v)
    return s.rank()


def rowspace(rows,p=0):
    s=Space(p)
    for v in rows:s.append(dict(v))
    return s.canonical()


def nullspace(rows,dim,p=0):
    r=rowspace(rows,p);pivots={v[0][0] for v in r};out=[]
    for f in range(dim):
        if f in pivots:continue
        v={f:1}
        for row in r:
            row=dict(row);lead=min(row);x=-row.get(f,0)
            if p:x%=p
            if x:v[lead]=x
        out.append(v)
    return out


def tensor(subset,sign):
    support=sorted({4*r+c for q in subset for r in RECTS[q][0] for c in RECTS[q][1]})
    pos={v:i for i,v in enumerate(support)};j=len(subset);m=len(support)
    U=[{} for _ in support]
    for a,q in enumerate(subset):
        (r,s),(c,d)=RECTS[q]
        u,v,x,y=[pos[k] for k in (4*r+c,4*r+d,4*s+c,4*s+d)]
        for b,z,k in ((u,y,1),(y,u,1),(v,x,sign),(x,v,sign)):U[z][(a,b)]=k
    aw=[neg(quadwt(q)) for q in subset];bw=[varwt(v) for v in support]
    weights=defaultdict(list)
    for a in range(j):
        for b in range(m):weights[add(aw[a],bw[b])].append((a,b))
    image={neg(w):i for i,w in enumerate(bw)}
    blocks=[]
    for w,coords in weights.items():
        params=coords[:-1] if w in image else coords
        if params:
            if w in image:assert U[image[w]][coords[-1]] in (-1,1)
            blocks.append((w,tuple(params)))
    assert sum(len(c) for w,c in blocks)==j*m-m
    return support,U,aw,bw,blocks


def wedge(vector,orientation,index):
    out={}
    for (a,b),v in vector.items():
        f,other=(a,b) if orientation=='A' else (b,a)
        if f==index:continue
        key=(other,min(f,index),max(f,index))
        out[key]=out.get(key,0)+(v if f<index else -v)
    return {i:x for i,x in out.items() if x}


def setup(subset,sign,p=0,extra=()):
    """Reconstruct quotient maps for every torus weight, with no certificate data."""
    support,U,aw,bw,blocks=tensor(subset,sign)
    U=U+[{tuple(ab):1} for ab in extra]
    maps={};base_ranks={};nf={};bases={}
    for orientation,fw in (('A',aw),('B',bw)):
        nf[orientation]=len(fw);spaces=defaultdict(lambda:Space(p))
        for vec in U:
            a,b=next(iter(vec));w=add(aw[a],bw[b])
            for i,x in enumerate(fw):spaces[add(w,x)].append(wedge(vec,orientation,i))
        base_ranks[orientation]=sum(s.rank() for s in spaces.values())
        lm=[]
        for w,coords in blocks:
            cols=[]
            for i,x in enumerate(fw):
                t=add(w,x)
                residues=[spaces[t].reduce(wedge({ab:1},orientation,i)) for ab in coords]
                rows=defaultdict(dict)
                for q,v in enumerate(residues):
                    for k,z in v.items():rows[k][q]=z
                conditions=rowspace([tuple(r.items()) for r in rows.values()],p)
                cols.append((t,residues,conditions))
            lm.append(cols)
        maps[orientation]=lm;bases[orientation]=spaces
    return {'subset':subset,'sign':sign,'prime':p,'support':support,'U':U,'blocks':blocks,
            'maps':maps,'base_ranks':base_ranks,'factor_dims':nf,'bases':bases}


def saturation_rank(data,chosen,orientation):
    groups=defaultdict(list)
    for b in chosen:
        for w,cols,cond in data['maps'][orientation][b]:groups[w].extend(cols)
    return data['base_ranks'][orientation]+sum(rank(v,data['prime']) for v in groups.values())


def line_minimum(data,index,orientation):
    cols=data['maps'][orientation][index];d=len(data['blocks'][index][1]);p=data['prime']
    for zeros in range(len(cols),-1,-1):
        for S in combinations(range(len(cols)),zeros):
            eq=[row for i in S for row in cols[i][2]]
            if len(rowspace(eq,p))<d:return len(cols)-zeros
    raise AssertionError('no projective line')
