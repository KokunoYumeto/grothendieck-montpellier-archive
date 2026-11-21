#!/usr/bin/env python3
"""Exact E0 last-meridian constraints for the full cabled B3 action.

The fixed colored sixteen-kernel values are necessary, while the chosen
thirty-eight-kernel extension is kept separate as a compatibility witness.
"""
from pathlib import Path
import json,time
import numpy as np
HERE=Path(__file__).resolve().parent;PENT=HERE.parent/'pentagon';CHAR=HERE.parent/'characters'

def run():
    start=time.monotonic();invt=np.load(CHAR/'records/affine216_marked_pair_kernels.npz')
    meta=json.loads((CHAR/'records/affine216_marked_pair_kernels.json').read_text())
    mt,iv,pk,nielsen=[invt[k]for k in['multiplication','inverse','pair_kernel','nielsen']]
    elements=invt['elements'];one=6;assert tuple(elements[one])==(0,0,1,0,0,1)
    data=np.load(HERE/'hurwitz_cabling_three_action.npz');triples=data['triples'];V=data['V_1_0']
    last=triples[:,2];desired=last[np.argsort(V)]
    products=mt[mt[triples[:,0],triples[:,1]],last];assert len(set(products))==1
    a=int(iv[products[0]]);bs=np.unique(last);kids=sorted(set(map(int,pk[a,bs])))
    def members(x,y):
        todo=[one];seen={one}
        for g in todo:
            for h in[x,y]:
                q=int(mt[g,h])
                if q not in seen:seen.add(q);todo.append(q)
        return np.array(todo,dtype=int)
    def derived(x,y,mem):
        c=int(mt[mt[mt[x,y],iv[x]],iv[y]]);gens=np.unique(mt[mt[mem,c],iv[mem]])
        todo=[one];seen={one}
        for g in todo:
            for h in gens:
                q=int(mt[g,h])
                if q not in seen:seen.add(q);todo.append(q)
        return np.array(sorted(todo),dtype=int)
    mapcache={};dercache={}
    def mapping(x,y):
        key=int(x),int(y)
        if key not in mapcache:
            k=int(pk[key]);can=invt[f'kernel_{k}_members'];new=members(*key)
            assert len(can)==len(new)
            fwd=np.full(216,-1,dtype=int);back=fwd.copy();fwd[can]=new;back[new]=can
            mapcache[key]=(k,fwd,back)
        return mapcache[key]
    def der(k):
        if k not in dercache:
            x,y=meta['kernels'][k]['pair'];dercache[k]=derived(x,y,invt[f'kernel_{k}_members'])
        return dercache[k]
    target={}
    for b in bs:
        vals=np.unique(desired[last==b]);assert len(vals)==1
        target[int(b)]=int(vals[0])
    allowed={};saved={'last_inputs':np.array([a,*bs]),'required_kernels':np.array(kids)}
    for k in kids:
        these=[int(b)for b in bs if pk[a,b]==k];dd=der(k);pred=[]
        for b in these:
            _,fwd,_=mapping(a,b);f=fwd[dd];assert min(f)>=0
            pred.append(mt[mt[iv[f],b],f])
        want=np.array([target[b]for b in these]);pred=np.stack(pred,axis=1)
        allowed[k]=dd[np.all(pred==want[None,:],axis=1)]
        saved[f'fiber_{k}']=allowed[k]
    colored=np.load(PENT/'hurwitz_colored_last_gentle.npz')
    coloredkids=colored['kernel_ids'];anchor={}
    coloredmeta=json.loads((PENT/'hurwitz_colored_last_gentle.json').read_text())
    # The sixteen values become unique after the already imposed gentle
    # orbit relations; some individual conjugator fibers have two values.
    for cid in coloredmeta['cases'][0]['orbit_cache_ids']:
        kk=colored[f'orbit_{cid}_kernel_ids'];aa=colored[f'orbit_{cid}_assignments']
        for j,k in enumerate(kk):
            if k in coloredkids:
                vals=np.unique(aa[:,j]);assert len(vals)==1
                anchor[int(k)]=int(vals[0])
    assert len(anchor)==len(coloredkids)
    for k,v in anchor.items():
        allowed[k]=np.intersect1d(allowed[k],[v])if k in allowed else np.array([v])
    assert all(len(v)>0 for v in allowed.values())
    orbits=[];seen=set()
    for k in sorted(allowed):
        if k in seen:continue
        todo=[k]
        for q in todo:
            for kk in nielsen[q]:
                if int(kk)not in todo:todo.append(int(kk))
        todo.sort();seen.update(todo);orbits.append(todo)
    chosen=np.load(PENT/'hurwitz_colored_full_core.npz')
    chosen_values=dict(zip(map(int,chosen['kernel_ids']),map(int,chosen['values_0'])))
    rows=[];chosen_ext=[]
    for no,orbit in enumerate(orbits):
        base=min((k for k in orbit if k in allowed),key=lambda k:len(allowed[k]))
        x,y=meta['kernels'][base]['pair'];z=int(iv[mt[x,y]])
        directed=[(x,y),(y,z),(z,x),(y,x),(z,y),(x,z)]
        maps=[mapping(*q)for q in directed];assert set(k for k,_,_ in maps)==set(orbit)
        found=[]
        for g0 in allowed[base]:
            for g1 in der(base):
                g2=int(iv[mt[g1,g0]])
                vals=[g0,g1,g2,iv[g0],iv[g1],iv[g2]];assign={};valid=True
                for(k,_,back),v in zip(maps,vals):
                    q=int(back[v]);assert q>=0
                    if(k in assign and assign[k]!=q)or(k in allowed and q not in allowed[k]):
                        valid=False;break
                    assign[k]=q
                if not valid:continue
                def ev(xx,yy):
                    k,fwd,_=mapping(xx,yy);q=int(fwd[assign[k]]);assert q>=0;return q
                for k in orbit:
                    xx,yy=meta['kernels'][k]['pair'];zz=int(iv[mt[xx,yy]])
                    fxy=ev(xx,yy);fyx=ev(yy,xx);fyz=ev(yy,zz);fzx=ev(zz,xx)
                    if mt[fyx,fxy]!=one or mt[mt[fzx,fyz],fxy]!=one:valid=False;break
                    neg=one
                    for v in[fzx,iv[zz],fyz,iv[yy],fxy,iv[xx]]:neg=int(mt[neg,v])
                    if neg!=one:valid=False;break
                if valid:found.append(tuple(assign[k]for k in orbit))
        found=sorted(set(found));compatible=[q for q in found if all(q[j]==chosen_values[k]for j,k in enumerate(orbit)if k in chosen_values)]
        saved[f'orbit_{no}_kernel_ids']=np.array(orbit)
        saved[f'orbit_{no}_assignments']=np.array(found,dtype=int).reshape(-1,len(orbit))
        saved[f'orbit_{no}_chosen_compatible']=np.array(compatible,dtype=int).reshape(-1,len(orbit))
        rows.append({'orbit':orbit,'extension_count':len(found),'chosen_colored_extension_count':len(compatible)})
        print(rows[-1],flush=True)
    out={'statement':'D23.F43 cabled source-value probe','tuple_degree':len(triples),'last_entry_count':len(bs),
         'last_pair_kernels':kids,'unanchored_fiber_sizes':{str(k):len(saved[f'fiber_{k}'])for k in kids},
         'fixed_colored_anchor_count':len(anchor),'gentle_orbits':rows,
         'all_orbits_nonempty':all(r['extension_count']for r in rows),
         'chosen_colored_extension_compatible':all(r['chosen_colored_extension_count']for r in rows),
         'elapsed_seconds':time.monotonic()-start,
         'scope':'Exact same-kernel derived fibers and all two/three/m=-1 constraints. Cross-orbit common-word membership and actual profinite realization remain separate.'}
    np.savez_compressed(HERE/'hurwitz_cabling_last_gentle.npz',**saved)
    (HERE/'hurwitz_cabling_last_gentle.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':run()
