#!/usr/bin/env python3
"""Complete colored C+^3 D Hurwitz inventory, with exact first detector maps."""
from pathlib import Path
import itertools,json,sys,time
import numpy as np

HERE=Path(__file__).resolve().parent

def run(kind='inverse'):
    start=time.monotonic()
    sl=[a for a in itertools.product(range(3),repeat=4)if(a[0]*a[3]-a[1]*a[2])%3==1]
    els=[v+a for v in itertools.product(range(3),repeat=2)for a in sl]
    ix={a:i for i,a in enumerate(els)};one=ix[(0,0,1,0,0,1)]
    def multiply(a,b):
        u,v,A,B,C,D=a;x,y,E,F,G,H=b
        return((u+A*x+B*y)%3,(v+C*x+D*y)%3,(A*E+B*G)%3,(A*F+B*H)%3,(C*E+D*G)%3,(C*F+D*H)%3)
    mt=np.array([[ix[multiply(a,b)]for b in els]for a in els],dtype=np.int16)
    iv=np.array([next(j for j in range(216)if mt[i,j]==one)for i in range(216)],dtype=np.int16)
    seed=ix[(0,0,2,1,0,2)]
    def conjugacy(g):return sorted({int(mt[mt[h,g],iv[h]])for h in range(216)})
    first=conjugacy(seed)
    if kind=='inverse':second=conjugacy(int(iv[seed]))
    elif kind=='order4':second=conjugacy(ix[(0,0,0,1,2,0)])
    elif kind=='order3plus':second=conjugacy(ix[(0,0,1,1,0,1)])
    elif kind=='order3minus':second=conjugacy(ix[(0,0,1,2,0,1)])
    elif kind=='order3affineplus':second=conjugacy(ix[(0,1,1,1,0,1)])
    elif kind=='order3affineminus':second=conjugacy(ix[(0,1,1,2,0,1)])
    else:raise ValueError(kind)
    assert not set(first)&set(second)
    classes=[np.array(first),np.array(second)];indices=[{int(g):i for i,g in enumerate(c)}for c in classes]
    con=[];cen=[];transport=[]
    for c,ci in zip(classes,indices):
        action=np.array([[ci[int(mt[mt[g,a],iv[g]])]for a in c]for g in range(216)],dtype=np.int16)
        con.append(action);cen.append(np.where(action[:,0]==0)[0])
        transport.append(np.array([next(g for g in range(216)if action[g,a]==0)for a in range(len(c))]))
    patterns=[];all_ids=[];all_reps=[];offset=[0]
    for color in range(4):
        pattern=[int(j==color)for j in range(4)];patterns.append(pattern)
        dims=[len(classes[t])for t in pattern];size=int(np.prod(dims[1:]));ids=np.full(size,-1,dtype=int);reps=[]
        for code in range(size):
            if ids[code]>=0:continue
            js=np.array(np.unravel_index(code,tuple(dims[1:])))
            trans=np.column_stack([con[t][cen[pattern[0]],j]for t,j in zip(pattern[1:],js)])
            codes=np.ravel_multi_index(trans.T,tuple(dims[1:]));ids[codes]=len(reps)
            reps.append([0]+js.tolist())
        all_ids.append(ids);all_reps.append(np.array(reps,dtype=np.int16));offset.append(offset[-1]+len(reps))
    N=offset[-1];gs=[]
    for k in range(3):
        parts=[]
        for color,(pattern,reps)in enumerate(zip(patterns,all_reps)):
            newcolor=k+1 if color==k else k if color==k+1 else color
            target=patterns[newcolor];moved=reps.copy()
            u=classes[pattern[k]][reps[:,k]];v=classes[pattern[k+1]][reps[:,k+1]]
            newu=mt[mt[u,v],iv[u]]
            moved[:,k]=[indices[target[k]][int(g)]for g in newu];moved[:,k+1]=reps[:,k]
            h=transport[target[0]][moved[:,0]]
            normalized=np.column_stack([con[t][h,moved[:,j]]for j,t in enumerate(target)])
            assert np.all(normalized[:,0]==0)
            dims=[len(classes[t])for t in target]
            codes=np.ravel_multi_index(normalized[:,1:].T,tuple(dims[1:]))
            parts.append(offset[newcolor]+all_ids[newcolor][codes])
        g=np.concatenate(parts);assert len(set(g))==N;gs.append(g)
    a,b,c=gs;I=np.arange(N)
    assert np.array_equal(a[b[a]],b[a[b]]) and np.array_equal(b[c[b]],c[b[c]])
    assert np.array_equal(a[c],c[a])
    z=a[b[c]];assert np.array_equal(z[z[z[z]]],I)
    tuples=np.concatenate([np.column_stack([classes[t][reps[:,j]]for j,t in enumerate(pattern)])
                           for pattern,reps in zip(patterns,all_reps)])
    colors=np.concatenate([np.full(len(reps),j,dtype=int)for j,reps in enumerate(all_reps)])
    def canonical_plus_triple(t):
        js=np.array([indices[0][int(g)]for g in t]);h=transport[0][js[0]];v=con[0][h,js]
        return min(tuple(map(int,row))for row in con[0][cen[0][:,None],v[None,:]])
    old=np.load(HERE/'hurwitz_cubic216_four_13.npz');lookup={}
    for idx,label in zip(old['detector_subset'],old['detector_map']):
        t=[ix[tuple(map(int,g))]for g in old['tuple_elements'][idx,:3]]
        key=canonical_plus_triple(t)
        if key in lookup:assert lookup[key]==label
        lookup[key]=int(label)
    assert len(lookup)==36
    forget={}
    for j in range(offset[3],offset[4]):
        key=canonical_plus_triple(tuples[j,:3])
        if key in lookup:forget[j]=lookup[key]
    seen=set();orbits=[]
    for v in range(N):
        if v in seen:continue
        queue=[v];seen.add(v)
        for u in queue:
            for g in gs:
                w=int(g[u])
                if w not in seen:seen.add(w);queue.append(w)
        orbits.append(queue)
    orbits.sort(key=len);rows=[]
    def subgroup_order(t):
        seen={one};queue=[one]
        for g in queue:
            for h in t:
                v=int(mt[g,h])
                if v not in seen:seen.add(v);queue.append(v)
        return len(seen)
    for no,orb in enumerate(orbits):
        inv={v:j for j,v in enumerate(orb)};prod=one
        for g in tuples[orb[0]]:prod=int(mt[prod,g])
        pc=conjugacy(prod);subset=[j for j,v in enumerate(orb)if v in forget]
        entry={'orbit':no,'degree':len(orb),'product_conjugacy_representative':els[min(pc)],
               'product_class_size':len(pc),'generated_subgroup_order':subgroup_order(tuples[orb[0]]),
               'detector_subset_size':len(subset)}
        if subset:
            local=np.array([[inv[int(g[v])]for v in orb]for g in gs]);fm={j:forget[orb[j]]for j in subset}
            assert set(fm.values())==set(range(36))
            for k in range(2):
                assert all(int(local[k,j])in fm and fm[int(local[k,j])]==int(old['detector_generators'][k,fm[j]])for j in subset)
            entry['marked216_retained']=True
            np.savez_compressed(HERE/f'hurwitz_colored_{kind}_orbit_{no}.npz',generators=local,
                tuple_elements=np.array(els,dtype=np.int16)[tuples[orb]],colors=colors[orb],
                detector_subset=np.array(subset),detector_map=np.array([fm[j]for j in subset]),
                detector_generators=old['detector_generators'])
        rows.append(entry);print(entry,flush=True)
    out={'kind':kind,'class_sizes':list(map(len,classes)),'degree':N,'orbit_degrees':list(map(len,orbits)),
         'orbits':rows,'all_braid_full_twist_relations':True,'elapsed_seconds':time.monotonic()-start,
         'scope':'Complete colored class union and literal first-detector retention. Full GT stability additionally requires isolated orbit or invariant property.'}
    (HERE/f'hurwitz_colored_{kind}.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items()if k!='orbits'},indent=2),flush=True)

if __name__=='__main__':run(sys.argv[1]if len(sys.argv)>1 else'inverse')
