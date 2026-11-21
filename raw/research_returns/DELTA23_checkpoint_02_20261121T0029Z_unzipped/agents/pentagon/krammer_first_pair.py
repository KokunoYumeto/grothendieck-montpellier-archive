#!/usr/bin/env python3
"""Exact necessary actual-gentle first-pair tests in the new F9 Krammer quotient."""
import json,pathlib,time
from collections import deque
import numpy as np
from krammer_f9_probe import matrices,to3,mp

def key(a):return a.astype(np.int8).tobytes()
def unkey(a,d=12):return np.frombuffer(a,dtype=np.int8).reshape((d,d)).astype(np.int16)
def mul(a,b):return a@b%3
def inv(a):
    d=len(a);ar=np.concatenate([a.copy(),np.eye(d,dtype=np.int16)],axis=1)
    for j in range(d):
        p=next(k for k in range(j,d) if ar[k,j])
        ar[[j,p]]=ar[[p,j]];ar[j]=ar[j]*int(ar[j,j])%3
        for k in range(d):
            if k!=j and ar[k,j]:ar[k]=(ar[k]-ar[k,j]*ar[j])%3
    return ar[:,d:]
def gp(gs,limit=100000):
    eye=np.eye(len(gs[0]),dtype=np.int16);seen={key(eye):0};els=[eye];cursor=0
    while cursor<len(els):
        a=els[cursor];cursor+=1
        for g in gs:
            b=mul(a,g);kb=key(b)
            if kb not in seen:
                seen[kb]=len(els);els.append(b)
                if len(els)>limit:raise RuntimeError('group limit')
    return els,seen
def closure_commutator(x,y):
    xi,yi=inv(x),inv(y);c=mul(mul(mul(x,y),xi),yi)
    orbit={key(c)};todo=[c];cursor=0
    while cursor<len(todo):
        a=todo[cursor];cursor+=1
        for g,gi in [(x,xi),(y,yi)]:
            b=mul(mul(g,a),gi);kb=key(b)
            if kb not in orbit:orbit.add(kb);todo.append(b)
    # Greedy generator reduction keeps the final enumeration compact.
    gens=[];els=[np.eye(len(x),dtype=np.int16)];seen={key(els[0]):0}
    for c in todo:
        if key(c) not in seen:
            gens.append(c);els,seen=gp(gens)
    return els,seen,len(todo),len(gens)

def conjclass(x,y,z):
    gs=[(x,inv(x)),(y,inv(y))];seen={key(z)};todo=[z];cursor=0
    while cursor<len(todo):
        a=todo[cursor];cursor+=1
        for g,gi in gs:
            b=mul(mul(g,a),gi);kb=key(b)
            if kb not in seen:seen.add(kb);todo.append(b)
    return seen

def run():
    st=time.monotonic();a,b,c=[to3(g).astype(np.int16) for g in matrices(4,3,6)]
    x,y=mp(a,2),mp(b,2);p,pi=gp([x,y]);assert len(p)==46656
    der,di,oc,ng=closure_commutator(x,y);assert len(der)==3888
    s=mul(mul(a,b),a);r=mul(a,b);tau=a
    sr=conjclass(x,y,s);rr=conjclass(x,y,r)
    good=[];braid=0;center=0;projections={}
    wi=[0,1,2,3,6,7] # F12,F13,F23 over F3
    for f in der:
        fi=inv(f);bb=mul(mul(fi,b),f)
        if np.array_equal(mul(mul(a,bb),a),mul(mul(bb,a),bb)):braid+=1
        else:continue
        if np.array_equal(mp(mul(a,bb),3),mp(r,3)):center+=1
        else:continue
        ss=mul(mul(a,bb),a);r1=mul(a,bb)
        if key(ss) not in sr or key(r1) not in rr:continue
        good.append(f);w=key(f[np.ix_(wi,wi)])
        projections[w]=projections.get(w,0)+1
    np.savez_compressed(pathlib.Path(__file__).with_suffix('.npz'),generators=np.array([a,b,c]),pure=np.array(p,dtype=np.int8),derived=np.array(der,dtype=np.int8),gentle_candidates=np.array(good,dtype=np.int8))
    out={'pure_order':len(p),'derived_order':len(der),'commutator_conjugacy_orbit':oc,'derived_generator_count':ng,'braid_candidates':braid,'center_candidates':center,'both_pure_frame_candidates':len(good),'distinct_W_projections':len(projections),'W_projection_multiplicities':sorted(projections.values()),'pure_s_conjugacy_class':len(sr),'pure_r_conjugacy_class':len(rr),'elapsed_seconds':time.monotonic()-st,'scope':'Necessary finite braid, center and pure-frame constraints for actual gentle elements; no candidate lift asserted.'}
    print(json.dumps(out,indent=2),flush=True);pathlib.Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run()
