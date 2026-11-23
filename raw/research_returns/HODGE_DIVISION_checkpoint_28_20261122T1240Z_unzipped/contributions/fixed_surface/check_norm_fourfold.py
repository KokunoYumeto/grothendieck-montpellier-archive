"""Exact intersections for the actual genus-five triple-cover norm source.
This is rational arithmetic, not a proof-assistant certification.
"""
import sympy as s
import json
from pathlib import Path
eta, th, nu, t=s.symbols('eta th nu t')
fact=s.factorial
T=81*eta**4-27*eta**3*nu+s.Rational(9,2)*eta**2*nu**2-s.Rational(1,2)*eta*nu**3+nu**4/24

def integral_X(poly):
    out=0
    for (e,a,b),c in s.Poly(s.expand(poly),eta,th,nu).terms():
        assert e+a+b==8
        out+=c*fact(a)*fact(b)*s.binomial(13-b,a)*s.binomial(5,b)*3**b
    return s.simplify(out)

def integral_T(poly):
    return s.simplify(integral_X(poly*T)/3)

ct=s.series((1+3*eta*t)*(1+eta*t)**(-4)*s.exp(-th*t/(1+eta*t)),t,0,5).removeO().expand()
c=[s.Integer(1)]+[s.expand(ct.coeff(t,j)) for j in range(1,5)]
c1,c2,c3,c4=c[1:]
K=-c1
nums={
 'eta4':integral_T(eta**4),'eta3theta':integral_T(eta**3*th),
 'eta2theta2':integral_T(eta**2*th**2),'etatheta3':integral_T(eta*th**3),
 'theta4':integral_T(th**4),'c1_4':integral_T(c1**4),
 'c1_2_c2':integral_T(c1**2*c2),'c2_2':integral_T(c2**2),
 'c1_c3':integral_T(c1*c3),'c4':integral_T(c4),
 'virtual_normal_top':integral_T(c1**4-3*c1**2*c2+c2**2+2*c1*c3-c4)}
expected={'eta4':27,'eta3theta':216,'eta2theta2':1512,'etatheta3':9072,'theta4':45360,
 'c1_4':91611,'c1_2_c2':53190,'c2_2':30888,'c1_c3':22518,'c4':7371,'virtual_normal_top':594}
td=[1,c1/2,(c1**2+c2)/12,c1*c2/24,(-c1**4+4*c1**2*c2+3*c2**2+c1*c3-c4)/720]
beta8=fact(8)*3**4
grr=[s.simplify(integral_T(th**(4-j)*td[j])) for j in range(5)]
coeff=[s.simplify(v/beta8) for v in grr]
expected_grr=[45360,-27216,8568,-1872,318]
expected_coeff=[s.Rational(1,72),-s.Rational(1,120),s.Rational(17,6480),-s.Rational(13,22680),s.Rational(53,544320)]
D=3**7*fact(8)
degf=fact(8)*3**12
pushfactor=fact(8)*3**8
w2=s.simplify(degf*3*D/(pushfactor**2*s.Rational(9,2)))
checks={**{k:bool(nums[k]==v) for k,v in expected.items()},
 'chern1':s.expand(c1+eta+th)==0,
 'chern2':s.expand(c2+2*eta**2-2*eta*th-th**2/2)==0,
 'chern3':s.expand(c3-10*eta**3+s.Rational(3,2)*eta*th**2+th**3/6)==0,
 'chern4':s.expand(c4+25*eta**4+10*eta**3*th-s.Rational(3,2)*eta**2*th**2-s.Rational(2,3)*eta*th**3-th**4/24)==0,
 'grr_pairings':grr==expected_grr,'grr_coefficients':coeff==expected_coeff,
 'weil_norm18':w2==18,'cycle_square648':s.Rational(1,72)**2*beta8+w2==648,
 'embedding_contradiction':nums['virtual_normal_top']<s.Rational(1,72)**2*beta8,
 'rho_g13_r2_d8':13-3*(13-8+2)==-8}
checks={k:bool(v) for k,v in checks.items()}
assert all(checks.values()),checks
out={'date_utc':'2026-11-22','model':'GPT-6 Astra Pro','effort':'not exposed','run':'/root/fixed_surface',
 'statement_ids':['HD-F1-S13','HD-F1-S14','HD-F1-S15'],
 'all_pass':True,'checks':checks,'chern_classes':[str(v) for v in c],
 'numbers':{k:str(v) for k,v in nums.items()},'grr_pairings':[str(v) for v in grr],
 'full_character_coefficients':[str(v) for v in coeff],
 'weil_norm':str(w2),'cycle_square':'648',
 'scope':'Exact arithmetic from the proved mixed-intersection and normal-bundle identities; geometric assertions are in norm_fourfold_followup.tex.'}
path=Path(__file__).with_name('norm_fourfold_certificate.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'all_pass':True,'checks':len(checks),'certificate':str(path)}))
