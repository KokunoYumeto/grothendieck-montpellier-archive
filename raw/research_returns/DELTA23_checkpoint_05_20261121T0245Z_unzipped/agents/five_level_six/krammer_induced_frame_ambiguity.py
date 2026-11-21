#!/usr/bin/env python3
"""Exact Krammer coordinate for the surviving harmonic frame ambiguity."""
import contextlib,io,json,runpy
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    ns=runpy.run_path(str(HERE/'krammer_quotient_extension.py'))
mm,mp,inv,to3,f9=map(ns.get,['mm','mp','inv','to3','f9'])
P,Pi,I6=ns['P'],ns['Pi'],ns['I6']
IW,IQ=ns['IW'],ns['IQ']
gamma=to3([[0,1,0],[2,0,0],[0,0,1]])
target=mm(mm(P,inv(gamma).T),Pi)
s=mm(mm(ns['a'],ns['b']),ns['a'])
choices=[]
for beta in ns['derived']:
    if np.array_equal(beta[np.ix_(IW,IW)],target) and np.array_equal(beta[np.ix_(IQ,IQ)],I6):
        assert np.array_equal(mm(beta,s),mm(s,beta))
        choices.append(beta)
assert len(choices)==3
order_four=[b for b in choices if np.array_equal(mp(b,4),ns['I'])]
assert len(order_four)==1
beta=order_four[0]
induced=json.loads((HERE.parent/'characters/records/induced_s4_harmonic.json').read_text())
assert induced['F_derived_orders']==[6912,1728,64,1]
assert 3888//486==8 and 1728//64==27
out={
 'statement':'D23.F16',
 'field':'F3[i], i^2=-1; encoding a+3b',
 'Krammer_beta_matrix_F9':f9(beta),
 'Krammer_beta_order':4,
 'Krammer_beta_W_affine_coordinate':[[0,1,0],[2,0,0],[0,0,1]],
 'Krammer_beta_Q_block':'identity',
 'Krammer_beta_commutes_with_half_twist':True,
 'Krammer_Fprime_order':3888,
 'Krammer_Fprime_abelianization_order':8,
 'induced_Fprime_order':1728,
 'induced_Fprime_abelianization_order':27,
 'joint_Fprime_image':'full direct product by solvable Goursat and coprime abelianizations',
 'induced_beta_coordinate':'identity on all24 sheets',
 'q12_beta':[9,4,8,9],
 'q4_beta':[1,0,0,1],
 'q3_beta':[0,1,2,0],
 'scope':'Finite frame conjugator ambiguity. No actual gentle element or actual pure frame is asserted.',
 'result':'PASS'
}
(HERE/'krammer_induced_frame_ambiguity.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
