"""Independent G030 complete certificate using Python unbounded integers.

The normal characters are rebuilt as products of literal cycle factors.
No root character engine, table generator, or positive evaluator is called.
Only the final JSON hashes and extrema are read for comparison.
"""
from pathlib import Path
from math import comb
from collections import defaultdict
from functools import lru_cache
import hashlib,json
import numpy as np
from verify_rectangular import partitions,character,z

HERE=Path(__file__).resolve().parent


@lru_cache(None)
def normal(cycles):
    poly={(0,0):1}
    for c in cycles:
        nxt=defaultdict(int)
        for (p,q),v in poly.items():
            for dp,dq in ((0,0),(c,0),(0,c)):
                nxt[p+dp,q+dq]+=v
        poly=dict(nxt)
    result=[]
    for degree in range(sum(cycles)+1):
        for q in range(degree//2+1):
            p=degree-q
            value=poly.get((p,q),0)-poly.get((p+1,q-1),0)
            if value:result.append((p,q,value))
    return tuple(result)


@lru_cache(None)
def complete(cycles,limit):
    a=[1]+[0]*limit
    for c in cycles:
        for n in range(c,limit+1):a[n]+=a[n-c]
    return tuple(a[n]-(a[n-1] if n else 0) for n in range(limit+1))


def traces(xs,bs):
    xs=np.array(tuple(xs),dtype=int)[:,None]
    bs=np.array(tuple(bs),dtype=int)[None,:]
    aa=xs+bs
    limit=int(aa.max())+1
    result=[]
    for cyc in partitions(5):
        val=np.zeros((len(xs),bs.shape[1]),dtype=object)
        for mask in range(1<<len(cyc)):
            selected=tuple(cyc[i] for i in range(len(cyc)) if mask>>i&1)
            if sum(selected)>3:continue
            rest=tuple(cyc[i] for i in range(len(cyc)) if not(mask>>i&1))
            hv=np.array(complete(rest,limit),dtype=object)
            def h(index):
                return hv[np.maximum(index,0)]*(index>=0)
            sign=(-1)**len(selected)
            for p,q,c in normal(selected):
                value=h(aa-p)*h(bs-q)-h(aa-q+1)*h(bs-p-1)
                # The zero convention also enforces rho containment.
                val+=sign*c*value*(aa>=p)*(bs>=q)
        result.append(val)
    return result


def multiplicities(xs,bs):
    ts=traces(xs,bs)
    result=[]
    for mu in partitions(5):
        numerator=sum((120//z(cyc))*character(mu,cyc)*value
                      for cyc,value in zip(partitions(5),ts))
        assert all(v%120==0 for v in numerator.flat)
        values=numerator//120
        assert min(values.flat)>=0
        result.append(values)
    return result


def compare(values,row,label,shape):
    assert all(isinstance(x,int) for x in values.flat)
    lo,hi=min(values.flat),max(values.flat)
    assert (lo,hi)==(row['min'],row['max']),(label,lo,hi,row)
    assert -2**63<=lo<=hi<2**63
    data=np.array(values,dtype='<i8').reshape(shape)
    assert hashlib.sha256(data.tobytes()).hexdigest()==row['sha256'],label


def main():
    ref=json.loads((HERE.parent/'root/SECOND_POWER_ZERO_TWIST_CERTIFICATE.json').read_text())
    notes=[];count=0
    raw=multiplicities(range(240),range(5,305))
    assert max(max(v.flat) for v in raw)==ref['bulk_b5']['input_max']
    for mu,values in zip(partitions(5),raw):
        tab=np.empty((60,60,4,5),dtype=object)
        for i in range(4):
            for j in range(5):
                value=sum((-1)**(i+j-u-v)*comb(i,u)*comb(j,v)*
                          values[60*u:60*(u+1),60*v:60*(v+1)]
                          for u in range(i+1) for v in range(j+1))
                assert min(value.flat)>=0
                if i+j>5:assert not any(value.flat)
                elif i+j:assert min(value.flat)>0
                tab[:,:,i,j]=value;count+=value.size
        label=''.join(map(str,mu))
        compare(tab,ref['bulk_b5']['labels'][label],label,(60,60,4,5))
        assert np.argwhere(tab[:,:,0,0]==0).tolist()==ref['bulk_b5']['zero_pairs'][label]
        notes.append(f'PASS bulk outer={label};72000 constants; all extrema, zeros and SHA256 match')
        print(notes[-1],flush=True)
    for b in range(5):
        shift=10-2*b
        raw=multiplicities(range(shift,shift+240),[b])
        assert max(max(v.flat) for v in raw)==ref['boundaries'][str(b)]['input_max']
        for mu,values in zip(partitions(5),raw):
            values=values[:,0];tab=np.empty((60,4),dtype=object)
            for i in range(4):
                value=sum((-1)**(i-u)*comb(i,u)*values[60*u:60*(u+1)]
                          for u in range(i+1))
                assert min(value.flat)>=0
                if i:assert min(value.flat)>0
                tab[:,i]=value;count+=value.size
            label=''.join(map(str,mu))
            compare(tab,ref['boundaries'][str(b)]['labels'][label],label,(60,4))
            assert np.flatnonzero(tab[:,0]==0).tolist()==ref['boundaries'][str(b)]['zero_residues'][label]
        notes.append(f'PASS b={b};1680 constants; all extrema, zeros and seven SHA256 streams match')
        print(notes[-1],flush=True)
    assert count==512400
    notes.append(f'PASS all {count} constants; Python unbounded integer traces and differences; every active nonconstant order positive and all inactive orders zero')
    (HERE/'SECOND_POWER_ZERO_TWIST_CERTIFICATE_INDEPENDENT_CHECK.txt').write_text('\n'.join(notes)+'\n')
    print(notes[-1],flush=True)


if __name__=='__main__':main()
