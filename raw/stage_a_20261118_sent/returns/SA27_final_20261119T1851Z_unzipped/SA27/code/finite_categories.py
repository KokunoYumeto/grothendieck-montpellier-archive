"""Exact finite-nerve certificates for the SA27 root audit.

Only rational Betti numbers are claimed by this program. Nonzero rational
homology is enough for the stated counterexamples. Mathematical arguments
identifying the sphere types appear in root_mathematical_checks.md.
"""
from collections import defaultdict
from itertools import product, combinations
import json
import sympy as sp

class Category:
    def __init__(self, objects, edges, relations=()):
        self.objects=tuple(objects); self.edges=edges
        self.paths=[]
        def visit(s,t,p):
            self.paths.append((s,p))
            for a,(u,v) in edges.items():
                if u==t: visit(s,v,p+(a,))
        for o in self.objects: visit(o,o,())
        self.parent={p:p for p in self.paths}
        def find(p):
            if self.parent[p]!=p: self.parent[p]=find(self.parent[p])
            return self.parent[p]
        self.find=find
        def union(p,q):
            p,q=find(p),find(q)
            if p==q:return False
            assert p[0]==q[0] and self.target(p)==self.target(q)
            self.parent[q]=p;return True
        for s,p,q in relations:union((s,tuple(p)),(s,tuple(q)))
        changed=True
        while changed:
            changed=False
            groups=defaultdict(list)
            for p in self.paths:groups[find(p)].append(p)
            for members in groups.values():
                for p,q in combinations(members,2):
                    for r in self.paths:
                        if self.target(r)==p[0]:
                            changed |= union((r[0],r[1]+p[1]),(r[0],r[1]+q[1]))
                        if self.target(p)==r[0]:
                            changed |= union((p[0],p[1]+r[1]),(q[0],q[1]+r[1]))
        self.morphisms=tuple(dict.fromkeys(find(p) for p in self.paths))
        self.nonid=tuple(p for p in self.morphisms if p[1])
        self.verify()
    def target(self,p):return self.edges[p[1][-1]][1] if p[1] else p[0]
    def compose(self,g,f):
        assert self.target(f)==g[0]
        return self.find((f[0],f[1]+g[1]))
    def verify(self):
        for f in self.morphisms:
            assert self.compose((self.target(f),()),f)==f
            assert self.compose(f,(f[0],()))==f
        for f,g,h in product(self.morphisms,repeat=3):
            if self.target(f)==g[0] and self.target(g)==h[0]:
                assert self.compose(h,self.compose(g,f))==self.compose(self.compose(h,g),f)
    def homology(self):
        bases=[list(self.objects),[(f,) for f in self.nonid]]
        while bases[-1]:
            bases.append([p+(f,) for p in bases[-1] for f in self.nonid if self.target(p[-1])==f[0]])
        ds=[sp.zeros(0,len(bases[0]))]
        for n in range(1,len(bases)):
            index={p:i for i,p in enumerate(bases[n-1])}
            d=sp.zeros(len(bases[n-1]),len(bases[n]))
            for col,p in enumerate(bases[n]):
                if n==1:
                    d[index[self.target(p[0])],col]+=1;d[index[p[0][0]],col]-=1
                else:
                    for i in range(n+1):
                        if i==0:q=p[1:]
                        elif i==n:q=p[:-1]
                        else:q=p[:i-1]+(self.compose(p[i],p[i-1]),)+p[i+1:]
                        d[index[q],col]+=(-1)**i
            ds.append(d)
        for n in range(2,len(ds)):assert ds[n-1]*ds[n]==sp.zeros(ds[n-1].rows,ds[n].cols)
        ranks=[m.rank() for m in ds]
        return {'objects':len(self.objects),'nonidentity_morphisms':len(self.nonid),
                'nondegenerate_simplices':[len(b) for b in bases[:-1]],
                'boundary_ranks':ranks,
                'betti_Q':[len(bases[n])-ranks[n]-ranks[n+1] for n in range(len(bases)-1)]}

def poset_category(objects,lt):
    edges={f'{x}>{y}':(x,y) for x in objects for y in objects if lt(x,y)}
    rel=[(x,(f'{x}>{y}',f'{y}>{z}'),(f'{x}>{z}',)) for x,y,z in product(objects,repeat=3) if lt(x,y) and lt(y,z)]
    return Category(objects,edges,rel)

def literal_appendix_example(terminals=0):
    objects=['o_prime','o','a','b']+[f't{i}' for i in range(terminals)]
    edges={'lambda':('o_prime','o'),'mu':('o_prime','o'),'alpha':('o','a'),'beta':('o','b')}
    relations=[('o_prime',('lambda','alpha'),('mu','alpha')),('o_prime',('lambda','beta'),('mu','beta'))]
    for i in range(terminals):
        edges[f'rho{i}']=('a',f't{i}');edges[f'sigma{i}']=('b',f't{i}')
        relations.append(('o',('alpha',f'rho{i}'),('beta',f'sigma{i}')))
    return Category(objects,edges,relations)

def main():
    results={}
    vertices=['v00','v01','v10','v11']
    edge_faces={'h0':{'v00','v10'},'h1':{'v01','v11'},'v0':{'v00','v01'},'v1':{'v10','v11'},'diag':{'v00','v11'}}
    cube_cells=vertices+list(edge_faces)+['q0','q1']
    def cube_lt(x,y):
        return x in edge_faces.get(y,set()) or (y in ['q0','q1'] and (x in vertices or x in ['h0','h1','v0','v1']))
    results['114_004_ordinary_cube_product_faces']=poset_category(cube_cells,cube_lt).homology()
    z=['v0','v1','v2','e01','e12','e20']
    face={'e01':{'v0','v1'},'e12':{'v1','v2'},'e20':{'v2','v0'}}
    def lt(x,y):return x in face.get(y,set())
    results['118_023_Z_circle']=poset_category(z,lt).homology()
    results['118_023_Y_one_cone']=poset_category(['p']+z,lambda x,y:(x=='p' and y in z) or lt(x,y)).homology()
    results['118_023_X_double_cone']=poset_category(['p','q']+z,lambda x,y:(x in ['p','q'] and y in z) or lt(x,y)).homology()
    results['118_023_pushout_arrow']=poset_category(['q','star'],lambda x,y:x=='q' and y=='star').homology()
    # In the pushout Y -> *, crossing arrows q -> z are identified along every
    # relation z -> z'. Their equivalence classes are exactly components of Z.
    classes={x:{x} for x in z}
    for x,y in product(z,repeat=2):
        if lt(x,y):
            u=classes[x]|classes[y]
            for k in u:classes[k]=u
    results['118_023_pushout_crossing_classes']=len(set(tuple(sorted(v)) for v in classes.values()))
    for n,label in [(0,'V00'),(1,'Vprime_contractible'),(2,'pushout')]:
        results['DerXIIApp_'+label]=literal_appendix_example(n).homology()
    # A nonstrict filtration-preserving map with every level map a weak equivalence.
    results['118_039_040_lax_example']={
        'I':[0,1],'X':'0<1','Y':'point','X_0':[0],'X_1':[0,1],
        'Y_0':['point'],'Y_1':['point'],'phi':[0,1],'psi_f':[0,0],
        'all_level_maps_between_contractible_categories':True,'strict_triangle':False}
    # Empty indexing category: binary preservation is vacuous, unit is not.
    results['118_035_empty_unit']={'A_objects':0,'presheaf_objects':1,'binary_comparison':'empty -> empty, isomorphism','unit_comparison':'empty -> point, not W_infinity'}
    # W_ne: f is a weak equivalence iff domain/codomain have same emptiness.
    X=(1,0);Y=(1,1);Z=(0,1)
    results['118_036_W_nonempty']={'X':X,'Y':Y,'Z':Z,'f_in_W':any(X)==any(Y),'product_f_in_W':any(a*b for a,b in zip(X,Z))==any(a*b for a,b in zip(Y,Z))}
    assert results['118_023_X_double_cone']['betti_Q']==[1,0,1]
    assert results['118_023_pushout_arrow']['betti_Q']==[1,0]
    assert results['DerXIIApp_V00']['betti_Q']==[1,0,1]
    assert results['DerXIIApp_pushout']['betti_Q']==[1,0,0,1]
    assert results['114_004_ordinary_cube_product_faces']['betti_Q']==[1,1,1]
    assert not results['118_036_W_nonempty']['product_f_in_W']
    print(json.dumps(results,indent=2))

if __name__=='__main__':main()
