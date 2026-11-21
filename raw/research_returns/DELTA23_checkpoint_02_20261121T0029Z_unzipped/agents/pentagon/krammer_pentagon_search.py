#!/usr/bin/env python3
"""Exact reduced Krammer pentagon search using D23.P6,F13,C9; DELTA23.

This tests necessary finite equations, not liftability to profinite GT.
"""
import json,pathlib,time
import numpy as np
from krammer_f9_probe import to3
from krammer_first_pair import mul,inv,closure_commutator

HERE=pathlib.Path(__file__).parent
def run():
    st=time.monotonic();z=json.loads((HERE.parent/'characters/records/krammer_mixed_correlation.json').read_text())
    raw=lambda a:to3(np.array(a)).astype(np.int16)
    xs=[raw(a) for a in z['X_matrices']]
    C,Q,central=[raw(z[j]) for j in ['C_full','Q_full','D_central_full']]
    Ci,Qi=inv(C),inv(Q);z45=inv(mul(xs[3],xs[4]))
    assert np.array_equal(mul(xs[2],C),mul(mul(C,central),z45))
    assert np.array_equal(mul(xs[3],C),mul(C,xs[3]))
    assert np.array_equal(mul(z45,Q),mul(Q,z45))
    assert np.array_equal(mul(xs[3],Q),mul(Q,xs[4]))
    assert all(np.array_equal(mul(central,x),mul(x,central)) for x in xs[3:])
    row=z['pairs'][0];B=raw(row['splitting_basis']);Bi=inv(B)
    hg=[raw(a) for a in row['solvable_generators']];ug=[raw(a) for a in row['unitary_generators']]
    H,_,_,_=closure_commutator(*hg);U,_,_,_=closure_commutator(*ug)
    assert len(H)==27 and len(U)==6048
    for j,x in enumerate(xs[2:4]):
        diag=np.zeros((12,12),dtype=np.int16);diag[:6,:6]=hg[j];diag[6:,6:]=ug[j]
        assert np.array_equal(mul(mul(B,diag),Bi),x)
    Ui=np.array([inv(u) for u in U],dtype=np.int16);U=np.array(U,dtype=np.int16)
    gs=np.load(HERE/'krammer_first_pair.npz')['generators'].astype(np.int16);a,b,c=gs
    D=mul(mul(mul(mul(mul(a,b),c),a),b),a);Di=inv(D)
    assert np.array_equal(mul(D,D),2*np.eye(12,dtype=np.int16)%3)
    assert np.array_equal(mul(mul(D,xs[0]),Di),xs[2])
    assert np.array_equal(mul(mul(D,xs[3]),Di),xs[4])
    fs=np.load(HERE.parent/'five_level_six/krammer_six_first_pair.npz')
    F=fs['candidates'].astype(np.int16);labels=fs['labels'];counts=np.zeros(6,dtype=np.int64);negative=np.zeros(6,dtype=np.int64)
    solutions=[];sol_labels=[];sol_index=[]
    for hi,h in enumerate(H):
        block=np.zeros((len(U),12,12),dtype=np.int16);block[:,:6,:6]=h;block[:,6:,6:]=U
        blocki=np.zeros_like(block);blocki[:,:6,:6]=inv(h);blocki[:,6:,6:]=Ui
        R=(B@block%3)@Bi%3;Ri=(B@blocki%3)@Bi%3
        r=(Ci@R%3)@C%3;ri=(Ci@Ri%3)@C%3
        # P=R D R^-1 F^-1 D^-1 H F.  P=I iff F A_R=B_R F.
        # H=Q^-1 r Q r^-1, so B_R=H^-1 D=r Q^-1 r^-1 Q D.
        AR=(R@D%3)@Ri%3
        BR=(((r@Qi%3)@ri%3)@Q%3)@D%3
        for fi,f in enumerate(F):
            left=f@AR%3;right=BR@f%3
            good=np.flatnonzero(np.all(left==right,axis=(1,2)))
            badscalar=np.flatnonzero(np.all(left==(-right)%3,axis=(1,2)))
            counts[fi]+=len(good);negative[fi]+=len(badscalar)
            for ui in good:
                solutions.append(R[ui]);sol_labels.append(labels[fi]);sol_index.append([hi,int(ui)])
        print(json.dumps({'H_index':hi,'counts':counts.tolist(),'minus_identity_counts':negative.tolist(),'elapsed':time.monotonic()-st}),flush=True)
    out={'statement':'D23.P7 finite computation only','R_candidates':27*6048,'F_candidates':6,'labels':labels.tolist(),'identity_counts':counts.tolist(),'minus_identity_counts':negative.tolist(),'solution_count':len(solutions),'elapsed_seconds':time.monotonic()-st,'scope':'Every actual gentle element satisfying the pentagon maps to this list. Converse/liftability and S4 nu4 correlation not asserted.'}
    (HERE/'krammer_pentagon_search.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(HERE/'krammer_pentagon_solutions.npz',R=np.array(solutions,dtype=np.int8),labels=np.array(sol_labels,dtype=np.int8),indices=np.array(sol_index,dtype=np.int16))
    print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':run()
