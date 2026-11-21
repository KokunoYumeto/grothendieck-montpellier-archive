"""Independent reconstruction of all 403200 T048 b=0 Newton constants."""
from pathlib import Path
from math import comb
import hashlib,json
import numpy as np
from verify_rectangular import partitions,character,z
from verify_outer5_fivepoint_family import sym_standard
from verify_outer5_stable_defect import induced_correction

HERE=Path(__file__).resolve().parent


def main():
    classes=list(partitions(5));traces=[];bounds=[]
    for cyc in classes:
        hx=[sym_standard(cyc,x) for x in range(240)]
        hp=[sym_standard(cyc,x-1) for x in range(240)]
        c=[sym_standard(cyc,2*K+13)-cyc.count(1)*sym_standard(cyc,K+7) for K in range(240)]
        d=[sym_standard(cyc,2*K+12)-cyc.count(1)*sym_standard(cyc,K+7) for K in range(240)]
        corr=[induced_correction(cyc,x,0,3) for x in range(240)]
        bound=max(map(abs,hx))*max(map(abs,c))+max(map(abs,hp))*max(map(abs,d))+max(map(abs,corr))
        assert bound<2**63
        hx,hp,c,d,corr=map(lambda arr:np.array(arr,dtype=np.int64),(hx,hp,c,d,corr))
        traces.append(hx[:,None]*c[None,:]-hp[:,None]*d[None,:]+corr[:,None]);bounds.append(bound)
    source=json.loads((HERE.parent/'theta/outer5/SYMMETRIC_THREE_DEFECT_SUMMARY.json').read_text())
    notes=[];count=0;largest=0;minimum=None;overflow=0
    for mu in partitions(5):
        weights=[(120//z(cyc))*character(mu,cyc) for cyc in classes]
        bound=sum(abs(w)*b for w,b in zip(weights,bounds))*64
        assert bound<2**63;overflow=max(overflow,bound)
        numerator=sum(w*t for w,t in zip(weights,traces));assert np.all(numerator%120==0)
        values=numerator//120;assert np.all(values>=0)
        key=','.join(map(str,mu));ref=source['summary'][key];hasher=hashlib.sha256()
        for i in range(4):
            for j in range(4):
                val=sum((-1)**(i+j-u-v)*comb(i,u)*comb(j,v)*values[60*u:60*(u+1),60*v:60*(v+1)] for u in range(i+1) for v in range(j+1))
                lo=int(val.min());hi=int(val.max());assert lo>=0
                assert lo==ref['minima'][f'{i},{j}'] and hi==ref['maxima'][f'{i},{j}']
                if i==j==3:assert not np.any(val)
                elif i+j:
                    assert lo>0;minimum=lo if minimum is None else min(minimum,lo)
                else:assert np.argwhere(val==0).tolist()==ref['zero_pairs']
                largest=max(largest,hi);count+=val.size
                hasher.update(val.astype('<i8',copy=False).tobytes(order='C'))
        assert hasher.hexdigest()==ref['table_sha256']
        notes.append(f'PASS outer={key} all57600 constants and SHA256={hasher.hexdigest()}')
    assert count==403200 and largest==646806600 and minimum==1054
    notes.append(f'PASS total={count}; maximum={largest}; minimum nonconstant active={minimum}; signed64 bound={overflow}')
    (HERE/'SYMMETRIC_THREE_DEFECT_INDEPENDENT_CHECK.txt').write_text('\n'.join(notes)+'\n')
    print('\n'.join(notes))


if __name__=='__main__':main()
