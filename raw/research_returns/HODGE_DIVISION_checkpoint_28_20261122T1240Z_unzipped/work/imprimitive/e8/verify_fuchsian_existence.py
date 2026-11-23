#!/usr/bin/env python3
"""Fresh M verification from the archived center, without the missing seed/fuchs.py.
21 November 2026, GPT-6 Astra Pro, inherited effort, /root/imprimitive.
Input candidate data: Severn unrefereed archive. No theorem in it is presumed.
The transport library is separately whole-code-read and endpoint-checked.
Only 23 residue columns use finite differences; 64 Q columns are exact derivatives.
"""
from pathlib import Path
import json,time,sys
import numpy as np
import sympy as sp
from fractions import Fraction
from cert_lib_audited import *

BASE=Path(__file__).resolve().parent
T0=time.time();setprec(256)
data=json.loads((BASE/'center_g.json').read_text())
targets=json.loads((BASE/'mtuple.json').read_text())
AT=np.array(targets['a'],dtype=int)
BT,CT,DT=[np.array(z,dtype=int) for z in targets['g'][0]]
I8=eye(8);mvals=[1,3,7,9,11,13,17,19]
U1=[acb(*z) for z in data['u1']]
U2FIX=acb(*data['u2j0']);j0=data['j0'];others=data['others']
X=[acb(arb(a).mid(),arb(b).mid()) for a,b in data['center']]
assert len(X)==87
ps=[acb(0),acb(1),acb(2,1)]
POLES=[0j,1+0j,2+1j];z0=.5-1j

def path(p):
    phi=np.angle(z0-p)
    circle=[p+.45*np.exp(1j*(phi+2*np.pi*k/12)) for k in range(13)]
    return [z0]+circle+[z0]
PATHS=[path(p) for p in POLES]

def npmat(M):
    return np.array([[complex(float(M[i,j].real.mid()),float(M[i,j].imag.mid()))
                      for j in range(M.ncols())] for i in range(M.nrows())])

def unpack(w):
    v1=w[:8];u2=[None]*8;u2[j0]=U2FIX
    for k,j in enumerate(others):u2[j]=w[8+k]
    v2=w[15:23]
    Q=acb_mat([[w[23+8*i+j] for j in range(8)] for i in range(8)])
    return v1,u2,v2,Q

def residues(w):
    v1,u2,v2,Q=unpack(w)
    return [acb_mat([[acb(mvals[i])/20 if i==j else 0 for j in range(8)] for i in range(8)]),
            acb_mat([[U1[i]*v1[j] for j in range(8)] for i in range(8)]),
            acb_mat([[u2[i]*v2[j] for j in range(8)] for i in range(8)])]

def monodromy(w):
    A=residues(w)
    return [transport(A,ps,P,frac=.35,N=100) for P in PATHS]

# Exact target spectral assertions, used to certify omitted eigenvector equations.
x=sp.Symbol('x');a,b,c,d=[sp.Matrix(z.tolist()) for z in (AT,BT,CT,DT)]
assert a*b*c*d==sp.eye(8)
assert a**20==sp.eye(8) and d**12==sp.eye(8)
assert a.charpoly(x).as_expr()==x**8-x**6+x**4-x**2+1
for t in (b,c):assert t*t==sp.eye(8) and (sp.eye(8)-t).rank()==1
cp=(x-1)**2*(x*x+x+1)*(x**4-x*x+1)
assert sp.expand(d.charpoly(x).as_expr()-cp)==0
LAM=[acb.exp_pi_i(acb(2*m)/20) for m in mvals]

def target_eigenvector(T,lam):
    M=acb_mat([[acb(int(T[i,j]))-(lam if i==j else 0) for j in range(8)] for i in range(8)])
    Mn=npmat(M)
    # These floats choose a minor only. The ball determinant must exclude zero.
    best=max((abs(np.linalg.det(np.delete(np.delete(Mn,r,0),k,1))),r,k)
             for r in range(8) for k in range(8))
    _,r,k=best;rows=[i for i in range(8) if i!=r];cols=[i for i in range(8) if i!=k]
    P=acb_mat([[M[i,j] for j in cols] for i in rows]);assert not P.det().contains(0)
    sol=P.solve(acb_mat([[-M[i,k]] for i in rows]))
    v=[acb(0)]*8;v[k]=acb(1)
    for j,q in enumerate(cols):v[q]=sol[j,0]
    return v
EV=[target_eigenvector(AT,z) for z in LAM]

def reflection(T):
    R=np.eye(8,dtype=int)-T
    j=int(np.argmax(np.abs(R).sum(axis=0)));xp=R[:,j]
    k=int(np.argmax(np.abs(xp)));yp=[Fraction(int(R[k,l]),int(xp[k])) for l in range(8)]
    assert all(Fraction(int(R[i,l]))==int(xp[i])*yp[l] for i in range(8) for l in range(8))
    assert sum(Fraction(int(xp[i]))*yp[i] for i in range(8))==2
    pivot=next(i for i in range(8) if yp[i])
    W=[]
    for i in range(8):
        if i==pivot:continue
        w=[acb(0)]*8;w[i]=acb(1);q=-yp[i]/yp[pivot]
        w[pivot]=acb(q.numerator)/q.denominator;W.append(w)
    return [acb(int(v)) for v in xp],W
RB,RC=reflection(BT),reflection(CT)

Ms0=monodromy(X)
DROP0=[];DROPR=[]
for M,lam in [(Ms0[0],z) for z in LAM]:
    values,vectors=np.linalg.eig((npmat(M)-complex(float(lam.real.mid()),float(lam.imag.mid()))*np.eye(8)).T)
    DROP0.append(int(np.argmax(np.abs(vectors[:,int(np.argmin(np.abs(values)))]))))
for M in Ms0[1:]:
    values,vectors=np.linalg.eig((npmat(M)+np.eye(8)).T)
    drop=int(np.argmax(np.abs(vectors[:,int(np.argmin(np.abs(values)))])))
    rp=int(np.argmax(np.abs(npmat(M)-np.eye(8)).sum(axis=1)))
    DROPR.append((drop,rp))
print('Fixed dropped rows',DROP0,DROPR,flush=True)

def equations(w,Ms=None):
    if Ms is None:Ms=monodromy(w)
    v1,u2,v2,Q=unpack(w)
    out=[sum((U1[i]*v1[i] for i in range(8)),acb(0))-acb(1)/2,
         sum((u2[i]*v2[i] for i in range(8)),acb(0))-acb(1)/2]
    for z,e,drop in zip(LAM,EV,DROP0):
        vec=(Ms[0]-I8*z)*Q*acb_mat([[v] for v in e])
        out.extend(vec[i,0] for i in range(8) if i!=drop)
    for M,(xp,W),(drop,rp) in zip(Ms[1:],(RB,RC),DROPR):
        vec=(M+I8)*Q*acb_mat([[v] for v in xp])
        out.extend(vec[i,0] for i in range(8) if i!=drop)
        for wv in W:out.append(((M-I8)*Q*acb_mat([[v] for v in wv]))[rp,0])
    out.append(Q.det()-1);assert len(out)==87
    return out,Ms

F0,_=equations(X,Ms0)
print('F(center) upper',max(upper_float(abs(v)) for v in F0),'elapsed',time.time()-T0,flush=True)
NVAR=87;h=2.**-80;R=2.**-40
D=[[acb(0) for _ in range(NVAR)] for _ in range(NVAR)]
for j in range(23):
    Xp=list(X);Xp[j]+=h;Fp,_=equations(Xp)
    for i in range(NVAR):D[i][j]=(Fp[i]-F0[i])/h
    print('Residue FD column',j,'elapsed',round(time.time()-T0,2),flush=True)

# Exact derivative with respect to Q_{uv}; no transport reevaluation is needed.
Q=unpack(X)[3];assert not Q.det().contains(0)
adj=Q.inv()*Q.det()
for u in range(8):
 for v in range(8):
    col=[acb(0),acb(0)]
    for z,e,drop in zip(LAM,EV,DROP0):
        M=Ms0[0]-I8*z
        col.extend(M[i,u]*e[v] for i in range(8) if i!=drop)
    for M,(xp,W),(drop,rp) in zip(Ms0[1:],(RB,RC),DROPR):
        Mp=M+I8;Mm=M-I8
        col.extend(Mp[i,u]*xp[v] for i in range(8) if i!=drop)
        col.extend(Mm[rp,u]*wv[v] for wv in W)
    col.append(adj[v,u]);assert len(col)==NVAR
    for i in range(NVAR):D[i][23+8*u+v]=col[i]
D=acb_mat(D)
Yn=np.linalg.inv(npmat(D));Y=acb_mat([[C(Yn[i,j]) for j in range(NVAR)] for i in range(NVAR)])
print('Approx inverse proposed; condition',np.linalg.cond(npmat(D)),flush=True)
XR=[acb(arb(t.real.mid(),R),arb(t.imag.mid(),R)) for t in X]
FR,_=equations(XR);K=[upper_float(abs(v)) for v in FR]
print('Cauchy bound max',max(K),'elapsed',time.time()-T0,flush=True)
YF=Y*acb_mat([[v] for v in F0]);eta=max(upper_float(abs(YF[i,0])) for i in range(NVAR))
n1=mat_norm_upper(eye(NVAR)-Y*D);nY=mat_norm_upper(Y)
# Only 23 columns have finite-difference error; all Q columns are exact derivatives.
Erow=max(upper_float(23*arb(k)*arb(h)/(arb(R)*(arb(R)-arb(h)))) for k in K)
rho=upper_float(10*arb(eta));assert 0<h<R and 0<rho<R
Crow=max(upper_float(2*NVAR*NVAR*arb(rho)*arb(k)/(arb(R)-arb(rho))**2) for k in K)
kappa=upper_float(arb(n1)+arb(nY)*arb(Erow)+arb(nY)*arb(Crow))
contraction=(kappa<1 and arb(eta)+arb(kappa)*arb(rho)<arb(rho))
assert contraction
root_displacement=upper_float(arb(eta)/(1-arb(kappa)))
archived_L_radius=1.0528417230446196e-34
assert arb(root_displacement)<arb(archived_L_radius)
for t,(a0,b0) in zip(X,data['center']):
    root_box=acb(arb(t.real.mid(),root_displacement),arb(t.imag.mid(),root_displacement))
    assert acb(arb(a0,archived_L_radius),arb(b0,archived_L_radius)).contains(root_box)
print('Contraction PASS',{'eta':eta,'rho':rho,'kappa':kappa,'n1':n1,'nY':nY},flush=True)

Xr=[acb(arb(t.real.mid(),rho),arb(t.imag.mid(),rho)) for t in X]
_,Ms=equations(Xr)
minors=[]
for M,z,drop in [(Ms[0],z,q) for z,q in zip(LAM,DROP0)]+[(Ms[j+1],-acb(1),DROPR[j][0]) for j in range(2)]:
    E=M-I8*z;rows=[i for i in range(8) if i!=drop]
    options=[]
    for omit in range(8):
        cols=[i for i in range(8) if i!=omit]
        det=acb_mat([[E[i,j] for j in cols] for i in rows]).det()
        if not det.contains(0):options.append((omit,str(det)))
    assert options;minors.append({'drop_row':drop,'minor':options[0]})
for M,(_,rp) in zip(Ms[1:],DROPR):assert any(not (M-I8)[rp,j].contains(0) for j in range(8))
print('All omitted-row and reflection-pivot conditions PASS',flush=True)

# Outward Arb Gershgorin bounds. The original archive's float radius printout
# was not used as a proof. The target monodromy gives exact eigenvalues modulo Z.
AA=residues(Xr);Binf=-(AA[0]+AA[1]+AA[2])
_,Vn=np.linalg.eig(npmat(Binf));V=acb_mat([[C(Vn[i,j]) for j in range(8)] for i in range(8)])
assert not V.det().contains(0)
T=V.inv()*Binf*V
labels=[];discs=[]
for i in range(8):
    q=Fraction(round(float(T[i,i].real.mid())*12),12)
    exact=acb(q.numerator)/q.denominator
    radius=abs(T[i,i]-exact)+sum((abs(T[i,j]) for j in range(8) if j!=i),arb(0))
    assert radius<arb(1)/10**10
    labels.append(str(q));discs.append(upper_float(radius))
assert sorted(Fraction(q) for q in labels)==sorted(map(Fraction,['-1','-1','-11/12','-2/3','-7/12','-5/12','-1/3','-1/12']))
print('Rigorous infinity discs PASS',labels,max(discs),flush=True)
report={'statement':'E8 Fuchsian M existence and exact conjugacy','date':'2026-11-21',
 'reviewer':'GPT-6 Astra Pro; inherited effort; /root/imprimitive',
 'input':'Candidate archived center and gauge data; JSON converted by restricted data-only loader',
 'nvariables':87,'finite_difference_columns':23,'exact_Q_derivative_columns':64,
 'eta':eta,'rho':rho,'kappa':kappa,'contraction':contraction,'n1':n1,'nY':nY,
 'root_displacement_upper':root_displacement,'archived_L_radius':archived_L_radius,
 'root_in_archived_L_box':True,'coordinatewise_box_containments':87,
 'FD_row_error_bound':Erow,'Cauchy_derivative_variation_bound':Crow,'Kmax':max(K),
 'side':True,'dropped_rows_0':DROP0,'reflection_rows':DROPR,'side_minors':minors,
 'Einf_num':labels,'disc_radius_max':max(discs),'infinity_disc_bounds':discs,
 'target_a_charpoly':'x8-x6+x4-x2+1','target_d_charpoly':'(x-1)^2*(x2+x+1)*(x4-x2+1)',
 'target_a_order20':True,'target_d_order12':True,
 'elapsed_seconds':time.time()-T0,
 'scope':'Fresh interval verification from the supplied center, using reviewed transport majorants; analytic root/conjugacy and based-loop arguments are proved separately.'}
(BASE/'existence_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
print('DONE fresh verification',round(time.time()-T0,2),flush=True)
