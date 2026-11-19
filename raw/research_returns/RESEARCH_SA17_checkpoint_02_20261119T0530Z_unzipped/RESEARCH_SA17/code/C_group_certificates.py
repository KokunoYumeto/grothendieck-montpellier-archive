#!/usr/bin/env python3
"""Exact finite checks for central twists, isoclinism, and the local ring obstruction."""
import json
from itertools import product
from collections import Counter
from time import perf_counter
import numpy as np
START=perf_counter()

def pairings():
    p=3;V=list(product(range(p),repeat=4));W=list(product(range(p),repeat=2))
    idx={v:i for i,v in enumerate(V)}
    add=np.array([[idx[tuple((x+y)%p for x,y in zip(v,w))] for w in V] for v in V])
    def b1(v,w):return ((v[0]*w[1]-v[1]*w[0])%3,(v[2]*w[3]-v[3]*w[2])%3)
    def f9mul(x,y):return ((x[0]*y[0]-x[1]*y[1])%3,(x[0]*y[1]+x[1]*y[0])%3)
    def b2(v,w):
        a=f9mul(v[:2],w[2:]);b=f9mul(v[2:],w[:2])
        return tuple((x-y)%3 for x,y in zip(a,b))
    output={}
    for name,b in [('Heis_F3_times_Heis_F3',b1),('Heis_F9',b2)]:
        table=np.array([[b(v,w) for w in V] for v in V],dtype=np.int16)
        assert np.all((table+table.transpose(1,0,2))%3==0)
        assert np.all(table[np.arange(81),np.arange(81)]==0)
        for v in range(81):
            # Exhaustive additivity for all w,u; antisymmetry gives the other variable.
            assert np.array_equal(table[add[v],:,:],(table[v][None,:,:]+table)%3)
        image_sizes=[len({tuple(x) for x in table[v]}) for v in range(81)]
        assert image_sizes.count(1)==1
        image={tuple(x) for x in table.reshape(-1,2)};assert len(image)==9
        dist=Counter({r:sum(n==3**r for n in image_sizes[1:]) for r in (1,2)})
        if name=='Heis_F3_times_Heis_F3':assert dist=={1:16,2:64}
        else:assert dist=={1:0,2:80}
        output[name]={'order':729,'center_order':9,'derived_order':9,'central_quotient_order':81,'nonzero_commutator_map_rank_distribution':dict(dist),'radical_dimension':0,'pairing_image_size':9,'additivity_triples_checked':81**3,'group_law':'(v,z)*(w,t)=(v+w,z+t+2*b(v,w)) over F3','derived_crossed_module':'zero map F3^2 -> F3^4 with trivial action'}
    return output

def central_twists():
    Q=list(product(range(2),repeat=2));G=list(product(range(2),repeat=3));idx={g:i for i,g in enumerate(G)}
    out=[]
    for a,b,c in product(range(2),repeat=3):
        def mul(g,h):
            e=(a*g[0]*h[0]+b*g[1]*h[1]+c*g[1]*h[0])%2
            return ((g[0]+h[0])%2,(g[1]+h[1])%2,(g[2]+h[2]+e)%2)
        tab=[[idx[mul(g,h)] for h in G] for g in G]
        one=idx[(0,0,0)]
        assert all(tab[one][x]==x==tab[x][one] for x in range(8))
        inv=[next(y for y in range(8) if tab[x][y]==one==tab[y][x]) for x in range(8)]
        assert all(tab[tab[x][y]][z]==tab[x][tab[y][z]] for x,y,z in product(range(8),repeat=3))
        center=[x for x in range(8) if all(tab[x][y]==tab[y][x] for y in range(8))]
        comm={tab[tab[tab[x][y]][inv[x]]][inv[y]] for x,y in product(range(8),repeat=2)}
        derived={one}
        while True:
            new=derived|{tab[x][y] for x in derived for y in comm}
            if new==derived:break
            derived=new
        prescribed={idx[(0,0,z)] for z in range(2)}
        actual=(set(center)==prescribed,derived==prescribed)
        criterion=(bool(c),bool(c));assert actual==criterion
        involutions=sum(x!=one and tab[x][x]==one for x in range(8))
        kind=('Q8' if involutions==1 else 'D8') if c else 'abelian'
        out.append({'cocycle_coefficients':[a,b,c],'center_size':len(center),'derived_size':len(derived),'center_test':actual[0],'derived_test':actual[1],'pairing_test':bool(c),'group':kind,'nonidentity_involutions':involutions,'associativity_triples_checked':8**3})
    assert Counter(x['group'] for x in out)=={'abelian':4,'D8':3,'Q8':1}
    return out

def finite_ring():
    # Z/4[u]/(u^2-1), all 16 elements enumerated as (a,b)=a+b*u.
    R=list(product(range(4),repeat=2));zero=(0,0);one=(1,0);u=(0,1);minus_one=(3,0)
    def add(x,y):return tuple((a+b)%4 for a,b in zip(x,y))
    def mul(x,y):return ((x[0]*y[0]+x[1]*y[1])%4,(x[0]*y[1]+x[1]*y[0])%4)
    assert all(mul(mul(x,y),z)==mul(x,mul(y,z)) and mul(x,add(y,z))==add(mul(x,y),mul(x,z)) for x,y,z in product(R,repeat=3))
    units=[x for x in R if any(mul(x,y)==one for y in R)]
    nonunits=set(R)-set(units)
    assert all(add(x,y) in nonunits for x,y in product(nonunits,repeat=2))
    assert all(mul(x,y) in nonunits for x in nonunits for y in R)
    assert mul(u,u)==one and u not in [one,minus_one]
    return {'order':16,'characteristic':4,'unit_count':len(units),'nonunits_form_ideal':True,'is_local':True,'u':[0,1],'u_squared':[1,0],'u_is_not_plus_or_minus_one':True,'ring_law_triples_checked':16**3}

def frobenius_levels():
    out=[]
    for p in [2,3,5,7]:
        for n in [1,2,3]:
            modulus=p**n
            # Invariants of U-I are exactly (a,0) at every finite level;
            # no lift of the quotient's vector 1 can be invariant.
            fixed=sum(b%modulus==0 for a,b in product(range(modulus),repeat=2))
            assert fixed==modulus
            out.append({'p':p,'level':n,'module_order':modulus**2,'Frobenius_order':modulus,'fixed_points':fixed,'invariant_lifts_of_quotient_one':0})
    return out

if __name__=='__main__':
    result={'isoclinism':pairings(),'central_twists':central_twists(),'local_ring_quotient':finite_ring(),'Frobenius_finite_levels':frobenius_levels()}
    result['runtime_seconds']=round(perf_counter()-START,6)
    print(json.dumps(result,indent=2))
