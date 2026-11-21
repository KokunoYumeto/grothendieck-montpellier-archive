#!/usr/bin/env python3
"""Literal braid identity linking the mixed45 pair to the mixed34 three-cycle."""
from pathlib import Path
import sys,json,numpy as np
HERE=Path(__file__).resolve().parents[1];ROOT=HERE.parents[1];PENT=HERE.parent/'pentagon'
sys.path.insert(0,str(HERE.parent/'five_level_six'))
from cyclic12_cover import braid,wi
from hurwitz_mixed_reflection_map import Reflection

def run():
    s=(1,2,1);X4=s*2;t=(3,2,3);X5=t*2;x=(3,3);a=(1,1);z4=(1,2,3)*4
    assert braid(wi(s)+X5+s)==braid(a+wi(x+X4)+z4)
    assert braid(a+x+wi(a)+wi(x))==braid(())
    assert braid(a+X4+wi(a)+wi(X4))==braid(())
    theta=Reflection();A,B,C=np.load(PENT/'hurwitz_cubic216_four_13.npz')['generators']
    S=A[B[A]];Si=np.argsort(S);T=C[B[C]];fifth=T[T];central=A[A]
    assert np.array_equal(Si[fifth[S]],central[theta.z])
    assert np.array_equal(central[theta.x],theta.x[central])
    assert np.array_equal(central[theta.y],theta.y[central])
    raw=np.load(PENT/'hurwitz_raw_pentagon45.npz')
    base=np.load(ROOT/'records/hurwitz_pentagon45_fibers.npz');rows=[];values=[]
    for k,(i,j)in enumerate(raw['labels']):
        if not np.array_equal(raw['pentagon_defects'][k],np.arange(8064)):continue
        R=base[f'R_{i}'][j];H=base[f'H_{i}'][j]
        expected=S[theta(R)[np.argsort(R)][Si]]
        assert np.array_equal(H,expected)
        rows.append({'base_index':int(i),'fiber_index':int(j),'joint_gentle_cycle_pass':True})
        values.append(expected)
    assert len(rows)==18
    out={'statement':'D23.C29','literal_B4_identity':'s^-1 X5 s=A^2 (X3 X4)^-1 z4; s=ABA',
         'central_input_invariance_scope':'All commutator words; central A^2 and z4 factors drop.',
         'cases':rows,'passes':18,'result':'PASS'}
    (HERE/'records/hurwitz_mixed45_cycle_link.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(HERE/'records/hurwitz_mixed45_cycle_link.npz',labels=np.array([(r['base_index'],r['fiber_index'])for r in rows]),H=np.array(values))
    print(json.dumps(out,indent=2))

if __name__=='__main__':run()
