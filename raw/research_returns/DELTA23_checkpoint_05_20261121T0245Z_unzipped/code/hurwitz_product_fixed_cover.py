#!/usr/bin/env python3
"""Raw product-fixed degree8064 Hurwitz cover and exact deck-lift tests."""
from pathlib import Path
import itertools,json,time,numpy as np
ROOT=Path(__file__).resolve().parents[1];PENT=ROOT/'agents/pentagon'
def run():
    started=time.monotonic()
    sl=[a for a in itertools.product(range(3),repeat=4)if(a[0]*a[3]-a[1]*a[2])%3==1]
    els=[v+a for v in itertools.product(range(3),repeat=2)for a in sl]
    ix={a:i for i,a in enumerate(els)};one=ix[(0,0,1,0,0,1)]
    def multiply(a,b):
        u,v,A,B,C,D=a;x,y,E,F,G,H=b
        return((u+A*x+B*y)%3,(v+C*x+D*y)%3,(A*E+B*G)%3,(A*F+B*H)%3,(C*E+D*G)%3,(C*F+D*H)%3)
    mt=np.array([[ix[multiply(a,b)]for b in els]for a in els],dtype=np.int16)
    iv=np.array([next(j for j in range(216)if mt[i,j]==one)for i in range(216)],dtype=np.int16)
    d=np.load(PENT/'hurwitz_cubic216_four_13.npz'); basegens=d['generators']
    tuples=np.array([[ix[tuple(map(int,a))]for a in row]for row in d['tuple_elements']],dtype=np.int16)
    def product(t):
        ans=one
        for x in t:ans=int(mt[ans,x])
        return ans
    p=product(tuples[0]);powers=[one]
    for k in range(1,6):powers.append(int(mt[powers[-1],p]))
    assert len(set(powers))==6 and mt[powers[-1],p]==one
    centralizer=[g for g in range(216)if mt[g,p]==mt[p,g]]
    assert set(centralizer)==set(powers)
    raw=[];transport=[]
    for t in tuples:
        pi=product(t)
        g=next(g for g in range(216)if mt[mt[g,pi],iv[g]]==p)
        transport.append(g);t0=mt[mt[g,t],iv[g]]
        for h in powers:raw.append(mt[mt[h,t0],iv[h]])
    raw=np.array(raw);index={tuple(map(int,t)):j for j,t in enumerate(raw)}
    assert len(index)==len(raw)==8064 and all(product(t)==p for t in raw)
    gs=[]
    for j in range(3):
        moved=raw.copy();u=raw[:,j];v=raw[:,j+1]
        moved[:,j]=mt[mt[u,v],iv[u]];moved[:,j+1]=u
        g=np.array([index[tuple(map(int,t))]for t in moved],dtype=np.int32)
        assert len(set(map(int,g)))==8064
        assert np.array_equal(g//6,basegens[j][np.arange(8064)//6])
        gs.append(g)
    A,B,C=gs;I=np.arange(8064);deck=6*(I//6)+(I%6+1)%6
    assert np.array_equal(A[B[A]],B[A[B]]) and np.array_equal(B[C[B]],C[B[C]])
    assert np.array_equal(A[C],C[A])
    z=A[B[C]];z=z[z[z[z]]]
    assert np.array_equal(z,deck)
    assert all(np.array_equal(g[deck],deck[g])for g in gs)
    phases=np.array([g[::6]%6 for g in gs]);s=A[B[A]];z3=s[s]
    qA=basegens[0];a,b,c=basegens;s0=a[b[a]];qZ=s0[s0]
    ez=z3[::6]%6
    # Exhaustive cyclic-deck-equivariant lift of each projective V commuting
    # with A and z3: solve the exact Z/6 potential equations on their orbits.
    cand=np.load(PENT/'hurwitz_global_conjugators.npz');checks=[];saved={}
    for bit in [0,1]:
        passing=[];potentials=[]
        for k,V in enumerate(cand[f'mixed72_V_{bit}']):
            potential=np.full(1344,-1,dtype=np.int16);valid=True;components=0
            for start in range(1344):
                if potential[start]>=0:continue
                potential[start]=0;queue=[start];components+=1
                for i in queue:
                    for q,e in [(qA,phases[0]),(qZ,ez)]:
                        j=int(q[i]);value=(int(potential[i])+int(e[V[i]])-int(e[i]))%6
                        if potential[j]<0:potential[j]=value;queue.append(j)
                        elif int(potential[j])!=value:valid=False;break
                    if not valid:break
                if not valid:break
            if valid:
                rawV=6*V[I//6]+(I%6+potential[I//6])%6
                assert np.array_equal(rawV[A],A[rawV]) and np.array_equal(rawV[z3],z3[rawV])
                assert np.array_equal(rawV[deck],deck[rawV])
                passing.append(k);potentials.append(potential)
        checks.append({'a3':bit,'input_candidates':len(cand[f'mixed72_V_{bit}']),
                       'A_z3_deck_lift_candidates':len(passing),'passing_indices':passing})
        saved[f'passing_{bit}']=np.array(passing);saved[f'potentials_{bit}']=np.array(potentials)
        print(checks[-1],flush=True)
    np.savez_compressed(ROOT/'records/hurwitz_product_fixed_cover.npz',generators=np.array(gs),
                        tuples=raw,group_elements=np.array(els),product=np.array(els[p]),
                        product_transporters=np.array(transport),deck=deck,generator_phases=phases,**saved)
    out={'statement':'D23.H6 probe','raw_degree':8064,'base_degree':1344,'deck_order':6,
         'fixed_product':els[p],'full_preimage_verified':True,'Artin_relations':'PASS',
         'full_twist_is_deck_generator':True,'centralizer_of_product_is_cyclic6':True,
         'connectedness':'Base action transitive and central full twist transitive on every fiber.',
         'checks':checks,'elapsed_seconds':time.monotonic()-started,
         'scope':'Raw actualGT stability uses exact product preservation, proved separately. Lift tests here impose only A,z3 and deck commutation.'}
    (ROOT/'records/hurwitz_product_fixed_cover.json').write_text(json.dumps(out,indent=2)+'\n')
    print('Built8064-point cover; elapsed',out['elapsed_seconds'])
if __name__=='__main__':run()
