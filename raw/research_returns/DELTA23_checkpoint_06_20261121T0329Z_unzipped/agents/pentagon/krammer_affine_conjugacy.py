#!/usr/bin/env python3
"""Exact Krammer--affine Frobenius-dual comparison; DELTA23."""
import contextlib,io,json,pathlib
import numpy as np
from krammer_f9_probe import matrices
with contextlib.redirect_stdout(io.StringIO()):
    import twisted_affine_extension as f

def inv(M):
    cols=[]
    for c in range(len(M)):
        sol=f.gauss(M,[int(j==c) for j in range(len(M))],len(M))
        assert sol['consistent']
        cols.append(sol['solution'])
    return list(map(list,zip(*cols)))
def tr(M):return list(map(list,zip(*M)))
def frob(M):return [[f.cub.add(x%3,3*(-(x//3)%3)) for x in row] for row in M]
def dual(M):return tr(inv(M))
def hom(g):return [[g[2],g[3],g[0]],[g[4],g[5],g[1]],[0,0,1]]
def from3(M):
    d=len(M)//2;out=[[0]*d for _ in range(d)]
    for i in range(d):
        for j in range(d):
            a,b=map(int,[M[2*i,2*j],M[2*i+1,2*j]])
            assert np.array_equal(M[2*i:2*i+2,2*j:2*j+2],[[a,-b%3],[b,a]])
            out[i][j]=a+3*b
    return out

P=[[7,7,2],[8,7,3],[2,8,1]];Pi=inv(P)
def recover(W):return frob(dual(f.mm(f.mm(Pi,from3(W)),P)))

def run():
    a=f.cub.ai(f.cub.am(f.cub.s,f.cub.r));b=f.cub.am(f.cub.am(f.cub.s,a),f.cub.s)
    targets=[dual(frob(hom(g))) for g in [a,b]]
    ks=[g.tolist() for g in matrices(3,3,6)]
    assert all(f.mm(K,P)==f.mm(P,T) for K,T in zip(ks,targets))
    out={'mode':'Frobenius contragredient','P':P,'P_inverse':Pi,'K1':ks[0],'K2':ks[1],'target_sigma1':targets[0],'target_sigma2':targets[1],'identities':'K_j P = P overline(eta(sigma_j))^(-T), j=1,2; P invertible','result':'PASS'}
    path=pathlib.Path(__file__)
    path.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    pp=path.with_name('krammer_first_pair.npz')
    if pp.exists():
        z=np.load(pp);cand=z['gentle_candidates'];wi=[0,1,2,3,6,7]
        data=json.loads(path.with_name('affine_cubic_detector.json').read_text())
        allowed={tuple(row['f']):(row['rho'],row['a3']) for row in data['gentle_f_images']}
        good=[];labels=[];counts={str(v):0 for v in allowed.values()}
        for c in cand:
            eta=recover(c[np.ix_(wi,wi)])
            assert eta[2]==[0,0,1]
            enc=tuple([eta[0][2],eta[1][2],eta[0][0],eta[0][1],eta[1][0],eta[1][1]])
            if enc in allowed:
                good.append(c);labels.append(allowed[enc]);counts[str(allowed[enc])]+=1
        out['necessary_first_pair_candidates_after_P3']=len(good);out['counts_by_rho_a3']=counts
        np.savez_compressed(path.with_name('krammer_filtered_first_pair.npz'),candidates=np.array(good),labels=np.array(labels))
        path.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':run()
