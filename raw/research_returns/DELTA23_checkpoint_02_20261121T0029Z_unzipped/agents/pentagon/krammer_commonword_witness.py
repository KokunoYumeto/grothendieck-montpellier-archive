#!/usr/bin/env python3
"""Find exact F' kernel separation for the two unitary mixed-pair maps."""
import json,pathlib
import numpy as np
from krammer_f9_probe import to3
from krammer_first_pair import inv,mul,key

HERE=pathlib.Path(__file__).parent
def wi(w):return [-j for j in w[::-1]]
def reduce(w):
    out=[]
    for j in w:
        if out and out[-1]==-j:out.pop()
        else:out.append(j)
    return out
def ev(gs,w):
    ims={1:gs[0],2:gs[1],-1:inv(gs[0]),-2:inv(gs[1])};v=np.eye(len(gs[0]),dtype=np.int16)
    for j in w:v=mul(v,ims[j])
    return v
def run():
    data=json.loads((HERE.parent/'characters/records/krammer_mixed_correlation.json').read_text())
    maps=[[to3(np.array(g)).astype(np.int16) for g in row['unitary_generators']] for row in data['pairs']]
    comm=[1,2,-1,-2];c=[ev(gs,comm) for gs in maps]
    seen={key(c[0]):0};orbit=[(c[0],c[1],comm)];cur=0;witness=None
    gis=[[inv(g) for g in gs] for gs in maps]
    while cur<len(orbit):
        a,b,w=orbit[cur];cur+=1
        for j in range(2):
            aa=mul(mul(maps[0][j],a),gis[0][j]);bb=mul(mul(maps[1][j],b),gis[1][j]);ww=reduce([j+1]+w+[-j-1]);k=key(aa)
            if k in seen:
                old=orbit[seen[k]]
                if not np.array_equal(old[1],bb):witness=reduce(ww+wi(old[2]));break
            else:seen[k]=len(orbit);orbit.append((aa,bb,ww))
        if witness is not None:break
    if witness is None:
        # A consistent conjugacy orbit can still fail on its generated subgroup.
        gens=[];gs0=[];gs1=[];group={key(np.eye(6,dtype=np.int16)):(np.eye(6,dtype=np.int16),[])}
        for a,b,w in orbit:
            if key(a) in group:continue
            gens.append(w);gs0.append(a);gs1.append(b)
            seen2={key(np.eye(6,dtype=np.int16)):0};queue=[(np.eye(6,dtype=np.int16),np.eye(6,dtype=np.int16),[])];cursor=0
            while cursor<len(queue):
                a0,b0,w0=queue[cursor];cursor+=1
                for ga,gb,gw in zip(gs0,gs1,gens):
                    aa=mul(a0,ga);bb=mul(b0,gb);ww=reduce(w0+gw);k=key(aa)
                    if k in seen2:
                        old=queue[seen2[k]]
                        if not np.array_equal(old[1],bb):witness=reduce(ww+wi(old[2]));break
                    else:seen2[k]=len(queue);queue.append((aa,bb,ww))
                if witness is not None:break
            if witness is not None:break
            group={key(aa):(bb,ww) for aa,bb,ww in queue}
    assert witness is not None
    vals=[ev(gs,witness) for gs in maps]
    assert np.array_equal(vals[0],np.eye(6,dtype=np.int16))
    assert not np.array_equal(vals[1],np.eye(6,dtype=np.int16))
    assert all(sum(1 if j==a else -1 if j==-a else 0 for j in witness)==0 for a in [1,2])
    out={'word_encoding':'1=x,2=y,negative=inverse; products left to right','word':witness,'word_length':len(witness),'exponent_sums':[0,0],'unitary34_value':vals[0].tolist(),'unitary45_value':vals[1].tolist(),'conjugacy_orbit_size_at_collision':len(orbit),'result':'PASS: F-prime kernels differ; with simplicity this proves derived joint image SU3(3)^2.'}
    (HERE/'krammer_commonword_witness.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':run()
