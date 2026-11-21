#!/usr/bin/env python3
"""Exact orthogonal spinor signs and two normalizer coset representatives."""
from pathlib import Path
import json,itertools,numpy as np,importlib.util,contextlib,io
HERE=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('orth112',HERE/'code/hurwitz_orthogonal112.py')
ort=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(ort)
Q=ort.Q;I=np.eye(6,dtype=int)
def norm(v):return int(v@Q@v%3)
def reflection(v):
    q=norm(v);assert q
    R=(I-2*q*np.outer(v,v@Q))%3
    assert np.array_equal(R.T@Q@R%3,Q)
    return R
# A fixed orthogonal basis, obtained by exact Gram--Schmidt.
basis=[]
for v0 in itertools.product(range(3),repeat=6):
    v=np.array(v0,dtype=int)
    for u in basis:v=(v-(v@Q@u%3)*norm(u)*u)%3
    if norm(v):basis.append(v)
    if len(basis)==6:break
B=np.array(basis).T;diag=B.T@Q@B%3
assert np.count_nonzero(diag)==6 and ort.rank(B)==6
def spinor(M,return_vectors=False):
    assert np.array_equal(M.T@Q@M%3,Q)
    cur=M.copy();ans=1;vectors=[]
    for v in basis:
        image=cur@v%3
        if np.array_equal(image,v):continue
        w=(image-v)%3
        if norm(w):
            cur=reflection(w)@cur%3;ans=ans*norm(w)%3;vectors.append(w.tolist())
        else:
            w=(image+v)%3;assert norm(w)
            cur=reflection(v)@reflection(w)@cur%3
            ans=ans*norm(v)*norm(w)%3;vectors.extend([w.tolist(),v.tolist()])
        assert np.array_equal(cur@v%3,v)
    assert np.array_equal(cur,I)
    assert ort.determinant(M)==pow(2,len(vectors),3)
    return (ans,vectors)if return_vectors else ans
signs=[spinor(M)for M in ort.matrices]
assert set(signs)=={1,2} and spinor(-I%3)==1
R=reflection(basis[0]);T=np.zeros((6,6),dtype=int)
for j in range(0,6,2):
    if diag[j,j]==diag[j+1,j+1]:T[j:j+2,j:j+2]=[[1,1],[1,2]]
    else:T[j:j+2,j:j+2]=[[0,1],[1,0]]
M=B@T@ort.inverse(B)%3
assert np.array_equal(M.T@Q@M%3,2*Q%3)
assert ort.determinant(M)==1 and ort.determinant(R)==2
# Conjugation by any similitude preserves spinor norm on SO.  Check the
# two explicit outer representatives on every stabilizer generator.
for C in [R,M]:
    Ci=ort.inverse(C)
    for A,e in zip(ort.matrices,signs):assert spinor(C@A@Ci%3)==e
comm=R@M@ort.inverse(R)@ort.inverse(M)%3
assert np.array_equal(comm.T@Q@comm%3,Q) and ort.determinant(comm)==1
out={'statement':'D23.C24','orthogonal_basis':B.tolist(),'diagonal_form':diag.tolist(),
     'stabilizer_spinor_norms':signs,'minus_identity_spinor_norm':1,
     'reflection_representative':R.tolist(),'reflection_determinant':2,'reflection_multiplier':1,
     'nonsquare_similitude_representative':M.tolist(),'similitude_determinant':1,'similitude_multiplier':2,
     'similitude_square_spinor':spinor(M@M%3),
     'outer_commutator_spinor':spinor(comm),
     'spinor_preserved_by_outer_conjugation_on_SO':True,
     'normalizer_over_PSO_quotient':'C2 x C2, detected by determinant and multiplier',
     'result':'PASS'}
coords=ort.coords;idx={tuple(v):j for j,v in enumerate(coords)}
perms=np.array([[idx[ort.proj(C@v)]for v in coords]for C in [R,M]])
np.savez_compressed(HERE/'records/hurwitz_orthogonal_signs.npz',reflection=R,similitude=M,
                    outer_permutations=perms,stabilizer_spinor_norms=np.array(signs))
(HERE/'records/hurwitz_orthogonal_signs.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
