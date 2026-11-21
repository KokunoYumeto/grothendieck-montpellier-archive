"""Independent complete G026 fixed-constant reconstruction from cycle subsets."""
from pathlib import Path
from math import comb
import hashlib,json
import numpy as np
from verify_rectangular import partitions,character,z

HERE=Path(__file__).resolve().parent


def hvals(cyc,limit):
    a=[1]+[0]*limit
    for c in cyc:
        for n in range(c,limit+1):a[n]+=a[n-c]
    return np.array([a[n]-(a[n-1] if n else 0) for n in range(limit+1)],dtype=np.int64)


def traces(xs,bs):
    xs=np.array(xs,dtype=np.int64)[:,None];bs=np.array(bs,dtype=np.int64)[None,:]
    aa=xs+bs;limit=int(aa.max())+1;cache={}
    def schur(cyc):
        if cyc not in cache:cache[cyc]=hvals(cyc,limit)
        h=cache[cyc]
        hb=h[bs];prev=h[np.maximum(bs-1,0)]*(bs>0)
        bound=int(h.max())**2*2
        assert bound<2**63
        return h[aa]*hb-h[aa+1]*prev
    out=[]
    for cyc in partitions(5):
        val=schur(cyc)
        for mask in range(1,1<<len(cyc)):
            selected=[i for i in range(len(cyc)) if mask>>i&1]
            if sum(cyc[i] for i in selected)>3:continue
            rest=tuple(cyc[i] for i in range(len(cyc)) if not(mask>>i&1))
            val=val+(-1)**len(selected)*schur(rest)
        out.append(val)
    return out


def multiplicities(xs,bs):
    ts=traces(xs,bs);answer=[]
    for mu in partitions(5):
        weights=[(120//z(cyc))*character(mu,cyc) for cyc in partitions(5)]
        assert sum(abs(w)*int(np.max(np.abs(t))) for w,t in zip(weights,ts))<2**63
        num=sum(w*t for w,t in zip(weights,ts))
        assert np.all(num%120==0);val=num//120;assert val.min()>=0
        answer.append(val)
    return answer


def main():
    ref=json.loads((HERE.parent/'root/FIRST_POWER_ZERO_TWIST_CERTIFICATE.json').read_text())
    notes=[];count=0
    raw=multiplicities(range(240),range(3,303))
    assert max(int(v.max()) for v in raw)==ref['bulk_b3']['input_max']
    for mu,values in zip(partitions(5),raw):
        tab=np.empty((60,60,4,5),dtype=np.int64)
        assert int(values.max())*128<2**63
        for i in range(4):
            for j in range(5):
                val=sum((-1)**(i+j-u-v)*comb(i,u)*comb(j,v)*values[60*u:60*(u+1),60*v:60*(v+1)] for u in range(i+1) for v in range(j+1))
                assert val.min()>=0
                if i+j>5:assert not np.any(val)
                elif i+j:assert val.min()>0
                tab[:,:,i,j]=val;count+=val.size
        label=''.join(map(str,mu));row=ref['bulk_b3']['labels'][label]
        assert hashlib.sha256(tab.astype('<i8').tobytes()).hexdigest()==row['sha256']
        assert int(tab.min())==row['min'] and int(tab.max())==row['max']
        assert np.argwhere(tab[:,:,0,0]==0).tolist()==ref['bulk_b3']['zero_pairs'][label]
        notes.append(f'PASS bulk outer={label};72000 constants; all extrema, zeros and SHA256 match')
    for b,shift in [(0,5),(1,3),(2,1)]:
        raw=multiplicities(range(shift,shift+240),[b])
        for mu,values in zip(partitions(5),raw):
            values=values[:,0];tab=np.empty((60,4),dtype=np.int64)
            assert int(values.max())*8<2**63
            for i in range(4):
                val=sum((-1)**(i-u)*comb(i,u)*values[60*u:60*(u+1)] for u in range(i+1))
                assert val.min()>=0
                if i:assert val.min()>0
                tab[:,i]=val;count+=val.size
            label=''.join(map(str,mu));row=ref['boundaries'][str(b)]['labels'][label]
            assert hashlib.sha256(tab.astype('<i8').tobytes()).hexdigest()==row['sha256']
            assert int(tab.min())==row['min'] and int(tab.max())==row['max']
            assert np.flatnonzero(tab[:,0]==0).tolist()==ref['boundaries'][str(b)]['zero_residues'][label]
        notes.append(f'PASS b={b};1680 constants; all extrema, zeros and seven SHA256 streams match')
    assert count==509040
    notes.append(f'PASS all {count} constants; every active nonconstant order positive; exact integer and overflow checks passed')
    (HERE/'FIRST_POWER_ZERO_TWIST_CERTIFICATE_INDEPENDENT_CHECK.txt').write_text('\n'.join(notes)+'\n')
    print('\n'.join(notes))


if __name__=='__main__':main()
