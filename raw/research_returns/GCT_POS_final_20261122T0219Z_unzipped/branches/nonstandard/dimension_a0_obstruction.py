"""Finite exact identities for the all-degree N-024 a0-route obstruction.

The coefficient-weight inequalities for arbitrary F are in N165--167.
No bounded support scan is used.
"""
from pathlib import Path
import json,sympy as s
HERE=Path(__file__).resolve().parent
q,v=s.symbols('q v');D=q+2+1/q;a0=D*(D-3)

def coeff(p,k):return s.expand(p).coeff(q,k)

def main():
    assert [coeff(a0,k) for k in range(-2,3)]==[1,1,0,1,1]
    assert [coeff(a0*a0,k) for k in range(-4,5)]==[1,2,1,2,4,2,1,2,1]
    assert coeff(3*D*a0,0)==6
    assert coeff(6*D*a0*a0,0)==72
    rows={(r['b'],r['bp'],r['bpp']):s.expand(s.sympify(r['c']))
          for r in json.loads((HERE/'dependencies/e3_constants.json').read_text())}
    g2=rows['Sigma','g2_1','Sigma'];square=rows['Sigma','Sigma','Sigma']
    assert s.expand(g2-(D**2*(D-1)).subs(q,v**2))==0
    assert s.expand(square-(4*D**2*(D-1)**2).subs(q,v**2))==0
    assert g2.coeff(v,0)==14 and square.coeff(v,0)==144
    w,l,f,m=s.symbols('w l f m')
    groups=[32*w,176*w,120*w,72*w-76,50*w-40-10*l,s.Integer(216),104+56*l]
    assert s.expand(sum(groups))==450*w+46*l+204
    score=s.expand(((sum(groups)-4424)/2).subs(w,12+4*f))
    assert score==590+900*f+23*l and score.subs({f:4,l:4})==4282
    assert 40+32*3<144<=40+32*4
    common_groups=[2*m*m*w,44*m*w,120*w,72*w-76,50*w-40-10*l,54*m,26*m+14*m*l]
    assert s.expand(sum(common_groups))==s.expand(2*(m+11)**2*w+(14*m-10)*l+80*m-116)
    common_score=s.expand((sum(common_groups)-4424)/2)
    assert common_score==s.expand((m+11)**2*w+(7*m-5)*l+40*m-2270)
    lower=s.expand(common_score.subs({w:20,l:4}))
    assert lower==20*m*m+508*m+130
    assert lower.subs(m,6)==3898 and lower.subs(m,8)==5474
    assert common_score.subs({m:6,w:20,l:8})==4046
    assert s.expand(a0+2-(D-1)*(D-2))==0
    out={'status':'PASS_FINITE_INPUTS_FOR_ALL_DEGREE_OBSTRUCTION',
         'true_G2_central':14,'baseline_G2_central':6,'forced_nonzero_F_mass':2,
         'true_square_central':144,'baseline_square_central':72,
         'square_central_bound':'40+32*f','forced_F_mass':4,'forced_L_mass':4,
         'score_formula':'590+900*f+23*l','modified_family_lower_bound':4282,
         'attainment':'NOT_ASSERTED','general_dimension_ring_lower_bound':'NOT_ASSERTED',
         'arbitrary_common_scale_score':'(m+11)^2*w+(7*m-5)*l+40*m-2270',
         'common_scale_general_minimum':3898,'common_scale_bar_minimum':4046,
         'common_scale_mass8_lower_bound':5474}
    (HERE/'dimension_a0_obstruction_verified.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
