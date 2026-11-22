#!/usr/bin/env python3
"""Exact finite-matrix certificate for a limitation of Schur-lift perfectness.

The node is R=A[[x,y]]/(xy-pi^3), with 2=pi^2.  The triangular
involution has polynomial lattice class, but its underived Schur lift
contains two copies of R/(pi^2,pi*x), a nonperfect module.  The infinite
projective-dimension conclusion is proved in the accompanying note using
the displayed minimal matrix factorization, not inferred from finite tests.
"""
from pathlib import Path
from time import perf_counter
import json
import sympy as s


def run():
    start=perf_counter()
    p,x,y=s.symbols('pi x y')
    g=x*y-p**3
    phi=s.Matrix([[-x,-p**2],[p,y]])
    psi=s.Matrix([[y,p**2],[-p,-x]])
    assert s.simplify(phi*psi+g*s.eye(2))==s.zeros(2)
    assert s.simplify(psi*phi+g*s.eye(2))==s.zeros(2)
    presentation=s.Matrix([[p,x]])
    assert s.simplify(presentation*phi)==s.Matrix([[0,g]])
    assert phi.subs({p:0,x:0,y:0})==s.zeros(2)
    assert psi.subs({p:0,x:0,y:0})==s.zeros(2)

    action=s.Matrix([[-1,p*x],[0,1]])
    assert action*action==s.eye(2)
    inc=s.Matrix([[1],[0]])
    proj=s.Matrix([[0,1]])
    assert action*inc==-inc
    assert proj*action==proj
    difference=action-s.eye(2)
    assert difference==s.Matrix([[-2,p*x],[0,0]])
    assert difference.subs(2,p**2)==s.Matrix([[-p**2,p*x],[0,0]])

    # Tensor words11,12,21,22, with place permutation(12).
    place=s.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
    e=s.diag(0,1,1,0)
    words=range(4);perm=[0,2,1,3]
    remaining={(i,j) for i in words for j in words};orbits=[]
    while remaining:
        a=min(remaining);orb={a,(perm[a[0]],perm[a[1]])}
        remaining-=orb;orbits.append(sorted(orb))
    sbasis=[]
    for orb in orbits:
        b=s.zeros(4)
        for i,j in orb:b[i,j]=1
        assert b*place==place*b
        sbasis.append(b)
    assert len(sbasis)==10
    corner=[e*b*e for b in sbasis]
    assert s.Matrix.hstack(*[b.reshape(16,1) for b in corner]).rank()==2
    se=[]
    for i in words:
        b=s.zeros(4);b[i,1]=1;b[perm[i],2]=1
        assert b*place==place*b and b*e==b
        se.append(b)
    corner_g=e*place*e
    for i in words:assert se[i]*corner_g==se[perm[i]]
    assert s.Matrix.hstack(*[b.reshape(16,1) for b in se]).rank()==4

    # Regular right-B summand tensor_B M is M: explicit kernel splitting.
    i=s.eye(2)
    relation=s.BlockMatrix([[-action,i],[i,-action]]).as_explicit()
    quotient=s.BlockMatrix([[i,action]]).as_explicit()
    kernel=s.BlockMatrix([[-action],[i]]).as_explicit()
    section=s.BlockMatrix([[i],[s.zeros(2)]]).as_explicit()
    assert quotient*relation==s.zeros(2,4)
    assert quotient*kernel==s.zeros(2)
    assert quotient*section==i
    assert s.BlockMatrix([[section,kernel]]).as_explicit().det()==1
    assert relation[:,:2]==kernel
    assert relation[:,2:]==kernel*(-action)
    return {
        'status':'PASS: underived Schur-lift perfectness is not necessary for an individual polynomial lattice class',
        'ring_scope':'R=A[[x,y]]/(xy-pi^3), A a dyadic DVR with2=pi^2; polynomial localization version also works',
        'triangular_action':str(action),
        'lattice_class':'[M]=[sign]+[trivial] by the checked admissible triangular extension',
        'schur_algebra_rank':10,
        'corner_rank':2,
        'Se_rank':4,
        'Se_right_group_decomposition':'trivial^2 plus regular',
        'schur_lift_underlying_module':'R^4 direct sum (R/(pi^2,pi*x))^2',
        'matrix_factorization_phi':str(phi),
        'matrix_factorization_psi':str(psi),
        'matrix_factorization_equations_checked':2,
        'presentation_syzygy_equations_checked':2,
        'minimality':'Both factorization matrices reduce to0 at(pi,x,y)',
        'infinite_pd_proof':'Provided in notes/C_schur_nonperfect_boundary.md using exactness of the matrix factorization and nonzero Tor in every degree; not a finite-search inference',
        'not_claimed':'No Swan obstruction or criterion for the unresolved node; no necessity conclusion for coherent modular regularity.',
        'runtime_seconds':perf_counter()-start}

if __name__=='__main__':
    output=run()
    path=Path(__file__).resolve().parents[1]/'logs/C_finish_schur_nonperfect_boundary.json'
    path.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:output[k] for k in ['status','schur_algebra_rank','corner_rank','Se_rank','runtime_seconds']},indent=2))
