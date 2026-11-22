#!/usr/bin/env python3
"""Exact Q(i)/Q(sqrt(-3)) H6 projector and quadratic-division checks.
No numerical approximation; this is a finite arithmetic certificate, not a
verification of cycle existence or of the supplied comass estimate.
"""
import json
import sympy as S


def simp(z):
    return S.simplify(S.expand_complex(z))


def gaussian():
    a=2+S.I
    ab=2-S.I
    rows=[]
    for j in range(7):
        unit=simp(S.I**j*(-S.I)**(6-j))
        eig=simp(a**j*ab**(6-j))
        ebar=simp(ab**j*a**(6-j))
        p=simp((1-unit)*(150-eig-ebar))
        assert p==(768 if j in [0,6] else 0)
        rows.append({'j':j,'unit':str(unit),'A':str(eig),'Abar':str(ebar),'projector':str(p)})
    r=-117; q=125; det=q*q-r*r
    gram=S.Matrix([[1,r],[r,q*q]])
    v1=S.Matrix([q*q,-r]);v2=S.Matrix([-r,1])
    assert det==1936
    assert (v1.T*gram*v1)[0]==5500**2
    assert (v2.T*gram*v2)[0]==44**2
    R=768;kappa=400
    d_bound=(R//6)**2
    n_bound=det*d_bound
    degree_bound=2*kappa*q*44*(R//6)
    assert (d_bound,n_bound,degree_bound)==(16384,31719424,563200000)
    return {'character_rows':rows,'Gram_shape':str(gram),'determinant':det,'R':R,'kappa':kappa,
            'd_over_D2':d_bound,'N_over_delta_D2':n_bound,'degree_over_delta_sqrtT_D2':degree_bound}


def eisenstein():
    w=(-1+S.sqrt(3)*S.I)/2
    wb=S.conjugate(w)
    a=2+w;ab=2+wb
    rows=[]
    for j in range(7):
        unit=simp(w**j*wb**(6-j))
        eig=simp(a**j*ab**(6-j))
        p=simp((1+unit+unit**2)*(27-eig))
        assert p==(162 if j in [0,6] else 0)
        rows.append({'j':j,'unit':str(unit),'S':str(eig),'projector':str(p)})
    b=3+w
    lam=simp(b**6)
    assert simp(lam-(-143+180*S.sqrt(3)*S.I))==0
    r=-143;q=343;det=q*q-r*r
    gram=S.Matrix([[1,r],[r,q*q]])
    v1=S.Matrix([q*q,-r]);v2=S.Matrix([-r,1])
    assert det==97200
    assert (v1.T*gram*v1)[0]==3*61740**2
    assert (v2.T*gram*v2)[0]==3*180**2
    R=162;kappa=81
    d_bound=(R//6)**2
    n_bound=det*d_bound
    degree_bound=2*kappa*q*180*(R//6)
    assert (d_bound,n_bound,degree_bound)==(729,70858800,270050760)
    return {'character_rows':rows,'basis_operator_eigenvalue':str(lam),'Gram_shape':str(gram),
            'determinant':det,'R':R,'kappa':kappa,'d_over_D2':d_bound,
            'N_over_delta_D2':n_bound,'degree_over_delta_sqrt3T_D2':degree_bound}


if __name__=='__main__':
    result={'gaussian':gaussian(),'eisenstein':eisenstein(),
            'certificate_scope':'Exact cyclotomic eigenvalues, integral projector, Gram inverse constants and dual norms only.'}
    print(json.dumps(result,indent=2))
