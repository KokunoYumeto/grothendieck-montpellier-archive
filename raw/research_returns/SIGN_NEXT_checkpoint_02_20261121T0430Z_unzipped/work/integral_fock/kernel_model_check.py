#!/usr/bin/env python3
"""Exact checks of actual m=2 column weights and finite exterior theta jets.
This executes Python/SymPy, not Lean. Large actual coefficient modules are
handled by the proved functorial construction; small complete matrices are
independently expanded to test Cauchy--Binet, scalar normalization and indices.
"""
from pathlib import Path
from itertools import combinations, product
from fractions import Fraction as Q
from math import factorial, comb
import json
import sympy as S
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
from sympy.polys.domains import ZZ
ROOT=Path(__file__).resolve().parent

def vf(n,p):
    out=0
    while n:
        n//=p;out+=n
    return out

def actual_column(last):
    u=[Q(113,2),Q(47,2),Q(39,2),Q(31,2),Q(23,2),Q(15,2),Q(7,2),Q(last,2)]
    base=[int(x-Q(7-2*i,2)) for i,x in enumerate(u)]
    lamN=[base,base+[-88]*16,base+[-88]*16+[-90]*16]
    lamTrue=[[x-8*j for x in row] for j,row in enumerate(lamN)]
    shifts=[row[-1] for row in lamTrue]
    alpha=[[x-row[-1] for x in row] for row in lamTrue]
    sharp=[88,98];div=[96,106]
    ins=[shifts[j]+sharp[j] for j in range(2)]
    nu=[[x+ins[j] for x in alpha[j]] for j in range(2)]
    assert shifts[1:]==[-x for x in div]
    assert [nu[j]+[0]*16 for j in range(2)]==alpha[1:]
    # Independent HC source-parameter formula from Numbers.nu.
    e=[100,118]
    nu2=[]
    for j in [1,2]:
        vals=[]
        for i in range(8+16*(j-1)):
            if i<8:sp=u[i]
            else:
                block=(i-8)//16;r=(i-8)%16
                sp=-e[block]+Q(17-2*(r+1),2)
            vals.append(sp+e[j-1]-Q((8+16*(j-1))+(8+16*j)-1-2*i,2))
        assert all(x.denominator==1 for x in vals)
        nu2.append(list(map(int,vals)))
    assert nu==nu2
    tests=[]
    for j,row in enumerate(alpha):
        for i in range(len(row)-1):
            d=row[i]-row[i+1]
            if d<2:continue
            tests.append({'stage':j,'root_one_based':i+1,'gap':d,'F2_Weyl':2,'F2_dual':d*(d-1),'divided2_Weyl':1,'divided2_dual':comb(d,2)})
    jets=[]
    for j,row in enumerate(nu):
        fac=1
        for x in row:fac*=factorial(x)
        coefficient=Q(1,fac)
        assert fac*coefficient==1
        jets.append({'step':j+1,'source_rank':len(row),'target_rank':len(row)+16,
            'degree':sum(row),'determinant_inserted_degree':len(row)*ins[j],
            'diagonal_jet':1,'highest_period':1,
            'diagonal_factorial_valuations':{str(p):sum(vf(x,p) for x in row) for p in [2,3,5,7,11,13,29,31,89]}})
    return {'unshifted':lamN,'true_weights':lamTrue,'det_shifts':shifts,'polynomial_parts':alpha,'kernel_shapes':nu,'det_insertions':ins,'root_tests':tests,'highest_kernel_tests':jets}

actual=actual_column(-1);big_special=actual_column(-7)
assert actual['det_insertions']==[91,2]
assert big_special['det_insertions']==[88,2]
assert actual['polynomial_parts'][0]==[50,18,15,12,9,6,3,0]
assert actual['kernel_shapes'][0]==[141,109,106,103,100,97,94,91]
assert actual['kernel_shapes'][1]==[143,111,108,105,102,99,96,93]+[2]*16

def snf_vals(B):
    D=smith_normal_form(B,domain=ZZ)
    return [abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]

def coords(T,U):
    C,params=T.gauss_jordan_solve(U)
    assert params.rows==0
    assert T*C==U
    return C

def tensor_model(lam,r):
    heights=[sum(x>=c for x in lam) for c in range(1,max(lam)+1)]
    colsets=[list(combinations(range(r),h)) for h in heights]
    inds=list(product(*colsets));loc={v:i for i,v in enumerate(inds)}
    dim=len(inds);generators=[]
    for a in range(r):
        for b in range(r):
            if a==b:continue
            E=S.zeros(dim)
            for k,ind in enumerate(inds):
                for c,I in enumerate(ind):
                    if b in I and a not in I:
                        J=list(I);pos=J.index(b);J[pos]=a
                        inversions=sum(J[x]>J[y] for x in range(len(J)) for y in range(x+1,len(J)))
                        J=tuple(sorted(J));out=list(ind);out[c]=J
                        E[loc[tuple(out)],k]+=(-1)**inversions
            Er=S.eye(dim)
            for h in range(1,sum(lam)+1):
                Er=Er*E/h
                if not any(Er):break
                assert all(v.q==1 for v in Er)
                generators.append(S.Matrix(Er.rows,Er.cols,[int(x) for x in Er]))
    t=S.zeros(dim,1);t[loc[tuple(tuple(range(h)) for h in heights)],0]=1
    T=t
    while True:
        M=S.Matrix.hstack(T,*[g*T for g in generators])
        M=S.Matrix(M.rows,M.cols,[int(x) for x in M])
        Tnext=hermite_normal_form(M)
        if Tnext==T:break
        T=Tnext
    assert snf_vals(T)==[1]*T.cols
    ell=len(lam)
    xx=S.symbols(f'x0:{r*ell}')
    X=S.Matrix(r,ell,xx)
    polys=[]
    for ind in inds:
        val=S.Integer(1)
        for I,h in zip(ind,heights):val*=X.extract(list(I),list(range(h))).det()
        polys.append(S.Poly(S.expand(val),xx))
    mons=sorted(set().union(*(set(p.monoms()) for p in polys)))
    Pi=S.Matrix([[p.coeff_monomial(m) for p in polys] for m in mons])
    F=S.diag(*[S.prod(factorial(x) for x in m) for m in mons])
    G=Pi.T*F*Pi
    c=(t.T*G*t)[0]
    P=T*(T.T*T).inv()*T.T
    assert G==c*P
    assert T.T*G*T==c*(T.T*T)
    return {'lam':lam,'r':r,'h':heights,'inds':inds,'T':T,'xx':xx,'X':X,'polys':polys,'c':c,'dim':dim}

small=[]
for lam in [[2,1],[3,1],[2,2],[3]]:
    A=tensor_model(lam,2);B=tensor_model(lam,3)
    assert A['c']==B['c']
    zz=S.symbols('z0:6');Z=S.Matrix(3,2,zz)
    mat=S.Matrix([[S.prod(Z.extract(list(I),list(J)).det() for I,J in zip(ib,ia)) for ia in A['inds']] for ib in B['inds']])
    for col,p in enumerate(A['polys']):
        sub={A['X'][i,s]:sum(Z[u,i]*B['X'][u,s] for u in range(3)) for i in range(2) for s in range(len(lam))}
        left=S.expand(p.as_expr().subs(sub,simultaneous=True))
        right=S.expand(sum(B['polys'][row].as_expr()*mat[row,col] for row in range(B['dim'])))
        assert S.expand(left-right)==0
    coeffs={}
    for row in range(mat.rows):
        for col in range(mat.cols):
            for beta,v in S.Poly(S.expand(mat[row,col]),zz).terms():
                if v==0:continue
                coeffs.setdefault(beta,S.zeros(mat.rows,mat.cols))[row,col]=v
    for C in coeffs.values():
        M=coords(B['T'],C*A['T'])
        assert all(v.q==1 for v in M)
    J=lambda beta:S.prod(x+1 for x in beta)*(-1)**beta[0]
    BJ=sum((J(beta)*C for beta,C in coeffs.items()),S.zeros(mat.rows,mat.cols))
    MBJ=coords(B['T'],BJ*A['T'])
    assert all(v.q==1 for v in MBJ)
    Ain=S.Matrix([[1,0],[0,1],[0,0]])
    inc=mat.subs(dict(zip(zz,list(Ain))))
    Min=coords(B['T'],inc*A['T'])
    assert snf_vals(Min)==[1]*A['T'].cols
    small.append({'partition':lam,'ambient_dimensions':[A['dim'],B['dim']],
      'cyclic_ranks':[A['T'].cols,B['T'].cols], 'fock_scalar':str(A['c']),
      'coefficient_matrices_checked':len(coeffs),'inclusion_smith':snf_vals(Min),
      'integer_moment_kernel_smith':snf_vals(MBJ),
      'source_cyclic_basis':A['T'].tolist(),'target_cyclic_basis':B['T'].tolist()})
    print('checked',lam,'ambient',A['dim'],B['dim'],'cyclic',A['T'].cols,B['T'].cols,'c',A['c'],flush=True)

record={'kind':'exact Python/SymPy check; no Lean kernel execution',
 'actual_numEx_w0':actual,'numBig_distinguished_real_place_w0':big_special,
 'numBig_other_real_places':'same weights as numEx; numBig scale differs',
 'small_complete_matrix_tests':small,
 'large_module_scope':'Actual large weight and diagonal-highest-jet arithmetic checked; all-module primitive-chain result uses IF08 proof, not expansion of astronomical matrices.'}
(ROOT/'kernel_model_check.json').write_text(json.dumps(record,indent=2,default=lambda x:int(x)))
print('all checks passed',flush=True)
