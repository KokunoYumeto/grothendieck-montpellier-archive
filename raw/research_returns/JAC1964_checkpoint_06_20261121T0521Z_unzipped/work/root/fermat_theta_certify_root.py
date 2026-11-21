"""Arb inputs and explicitly enclosed finite theta computations.

The analytic grid/Jensen inequalities and truncation bounds are documented
in FERMAT_THETA_CERTIFICATE.md. No random quadrature is used here.
"""
import os
os.environ["OPENBLAS_NUM_THREADS"]="1"
import itertools, json, math
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from flint import arb,acb,acb_mat,ctx
TAU=np.array([[.5+1j,-.5,-.5-.5j],
              [-.5,.5+1j,.5+.5j],
              [-.5-.5j,.5+.5j,1+1j]])
X,Y=TAU.real,TAU.imag
T=np.array([[-1,(-1+1j)/2,(1+1j)/2],
            [-1,(1-1j)/2,-(1+1j)/2],
            [0,0,-1-1j]])
W=np.diag([0,-1+1j,1+1j])

ctx.prec=160
PI=arb.pi(); L2=arb(2).log(); base=(-PI/8).exp()
root=[acb(arb(j)/8).exp_pi_i() for j in range(16)]
powcache={}
def pw(n):
    n=int(n)
    if n not in powcache:powcache[n]=base**n
    return powcache[n]
def ballerr(r):return acb(arb(0,r),arb(0,r))
def aa(q):
    if isinstance(q,F):return arb(q.numerator)/q.denominator
    return arb(q)
def cint(z):
    c=complex(float(z.real.mid()),float(z.imag.mid()))
    r=abs(z.real-arb(c.real))+abs(z.imag-arb(c.imag))
    return c,np.nextafter(float(r.upper()),np.inf)
def conv(arr):
    c=np.zeros(arr.shape,complex);r=np.zeros(arr.shape,float)
    for ix in np.ndindex(arr.shape):c[ix],r[ix]=cint(arr[ix])
    return c,r
def put(msg):print(msg,flush=True)

grid=np.array(list(itertools.product(range(-21,22),repeat=3)),dtype=int)
q=np.rint(np.einsum('ni,ij,nj->n',grid,Y,grid)).astype(int)
xx=np.rint(2*np.einsum('ni,ij,nj->n',grid,X,grid)).astype(int)
sel=q<=100;kphi=grid[sel];qp=q[sel];xp=xx[sel]
pars=(kphi[:,0]%2)*4+(kphi[:,1]%2)*2+kphi[:,2]%2
ephi=[pw(4*qq)*root[(2*xx)%16] for qq,xx in zip(qp,xp)]
G=[[acb(0) for p in range(8)] for row in range(7)]
for k,p,z in zip(kphi,pars,ephi):
    weights=[1]+[int(k[i]*k[j]) for i in range(3) for j in range(i,3)]
    for row,wt in enumerate(weights):G[row][p]+=wt*z
for row in range(7):
    for p in range(8):G[row][p]+=ballerr("1e-45")
mat=acb_mat([[G[r][c] for c in range(7)] for r in range(7)])
rhs=acb_mat([[-G[r][7]] for r in range(7)])
sol=mat.solve(rhs);cp=[sol[j,0] for j in range(7)]+[acb(1)]
put("Certified Gamma00 kernel.")

thetanulls={}
ngrid=np.array(list(itertools.product(range(-12,13),repeat=3)),dtype=int)
for ch in itertools.product(range(2),repeat=6):
    if sum(ch[i]*ch[i+3] for i in range(3))%2:continue
    u=2*ngrid+np.array(ch[:3])
    qu=np.rint(np.einsum('ni,ij,nj->n',u,Y,u)).astype(int)
    xu=np.rint(2*np.einsum('ni,ij,nj->n',u,X,u)).astype(int)
    ph=xu+4*(u@np.array(ch[3:]))
    out=acb(0)
    for a,b in zip(qu[qu<=200],ph[qu<=200]):out+=pw(2*a)*root[int(b)%16]
    thetanulls[ch]=out+ballerr("1e-45")
logT=sum((abs(z).log() for z in thetanulls.values()),arb(0))
habs=arb(1)
for ch,z in thetanulls.items():
    if ch[0]==1:habs*=abs(z)
half=sum((cp[int(p)]*z*((-1)**int(k[0])) for k,p,z in zip(kphi,pars,ephi)),acb(0))
half+=ballerr(arb("1e-45")*sum((abs(c) for c in cp),arb(0)))
scale=habs/abs(half);cp=[c*scale for c in cp]
assert all(abs(c)<arb(1) for c in cp), "uniform Frobenius tail requires this bound"
put("Certified thetanulls and Frobenius scale.")

def coeffs(D):
    vals={}
    if D==2:
        sel=q<=50;ks=grid[sel];qs=q[sel];xs=xx[sel]
    for jj in itertools.product(range(D),repeat=3):
        u=np.array(jj,dtype=float)/D;z=T@u
        out=acb(0);su=jj[1]**2+jj[2]**2;di=-jj[1]**2+jj[2]**2
        if D==4:
            zr=np.rint(8*z.real).astype(int);zi=np.rint(8*z.imag).astype(int)
            es=4*qp+2*(kphi@zi)+su
            ph=2*xp+2*(kphi@zr)+di
            for p,e,b in zip(pars,es,ph):out+=cp[int(p)]*pw(e)*root[int(b)%16]
            out+=ballerr("1e-20")
        else:
            zr=np.rint(4*z.real).astype(int);zi=np.rint(4*z.imag).astype(int)
            es=8*qs+4*(ks@zi)+2*su
            ph=4*xs+4*(ks@zr)+2*di
            for e,b in zip(es,ph):out+=pw(e)*root[int(b)%16]
            out+=ballerr("1e-30")
        vals[jj]=out
    Sr=[]
    for r in range(D):
        val=sum(((-PI/D*(D*n+r)**2).exp() for n in range(-12,13)),arb(0))
        Sr.append(val+arb(0,"1e-100"))
    c=np.empty((D,D,D),object)
    for rr in itertools.product(range(D),repeat=3):
        z=sum((v*root[(-16//D*sum(r*j for r,j in zip(rr,jj)))%16] for jj,v in vals.items()),acb(0))/D**3
        c[rr]=z/(Sr[rr[0]]*Sr[rr[1]]*Sr[rr[2]])
    return c

C4=coeffs(4);C2=coeffs(2)
put("Certified product theta coefficients.")

def basis(D,n,off):
    out=np.empty((n*n,D),object)
    for ix in range(n):
        for iy in range(n):
            x=F(ix,n)+off[0];y=F(iy,n)+off[1]
            x-=math.floor(x+F(1,2));y-=math.floor(y+F(1,2))
            for r in range(D):
                z=acb(0)
                for kk in range(-D*9+r,D*9+1,D):
                    z+=acb(2*aa(kk*x),aa((F(kk)+D*y)**2/D)).exp_pi_i()
                out[ix*n+iy,r]=z+ballerr("1e-100")
    return out

def grams(n):
    kvals=range(-12,13);ds=range(-24,25)
    pf={d:(-PI*d*d/4).exp() for d in ds}
    fx={};fy={}
    for ix in range(n):
        x=F(2*ix+1,2*n)-F(1,2)
        for d in ds:
            sinc=arb(1) if d==0 else (PI*d/n).sin()/(PI*d/n)
            fx[ix,d]=acb(2*d*aa(x)).exp_pi_i()*sinc
    for iy in range(n):
        lo=F(iy,n)-F(1,2);hi=F(iy+1,n)-F(1,2)
        for s in ds:
            fy[iy,s]=arb(n)/4*((2*PI.sqrt()*aa(hi+F(s,4))).erf()-(2*PI.sqrt()*aa(lo+F(s,4))).erf())
    out=np.empty((n*n,4),object)
    for ix in range(n):
        for iy in range(n):
            row=[acb(0) for j in range(4)]
            for k in kvals:
                for l in kvals:row[(k%2)*2+l%2]+=pf[k-l]*fx[ix,k-l]*fy[iy,k+l]
            for j in range(4):out[ix*n+iy,j]=row[j]+ballerr("1e-80")
    return out

def contraction_error(c,cr,bs,brs):
    sc=sum((arb(abs(z.real))+arb(abs(z.imag)) for z in c.flat),arb(0))
    rc=sum((arb(float(r)) for r in cr.flat),arb(0))
    B=[arb(float(np.nextafter(np.max(abs(b.real)+abs(b.imag)),np.inf))) for b in bs]
    R=[arb(float(np.max(r))) for r in brs]
    P=B[0]*B[1]*B[2]
    PP=(B[0]+R[0])*(B[1]+R[1])*(B[2]+R[2])
    unit=arb(2)**-53;gamma=4096*unit/(1-4096*unit)
    bound=rc*PP+sc*(PP-P)+gamma*sc*P+arb(2)**-1000
    return np.nextafter(float(bound.upper()),np.inf)

def mean_log_contract(C,Bs,lower):
    c,cr=conv(C);br=[conv(b) for b in Bs];bs=[v[0] for v in br];rs=[v[1] for v in br]
    err=contraction_error(c,cr,bs,rs)
    a=np.einsum('abc,ia->ibc',c,bs[0],optimize=True)
    a=np.einsum('ibc,jb->ijc',a,bs[1],optimize=True)
    bins=12;hist=np.zeros(2**bins+1,dtype=np.int64);esum=0;total=0;small=float('inf')
    for i in range(len(bs[0])):
        z=np.einsum('jc,kc->jk',a[i],bs[2],optimize=True)
        if lower:
            rr=np.nextafter(z.real*z.real,-np.inf);ii=np.nextafter(z.imag*z.imag,-np.inf)
            ss=np.nextafter(rr+ii,-np.inf)
            mag=np.nextafter(np.sqrt(np.maximum(ss,0)),-np.inf)
            v=np.nextafter(mag-err,-np.inf)
        else:v=np.nextafter(z.real+err,np.inf)
        small=min(small,float(v.min()))
        if np.any(v<=0):raise ArithmeticError("nonpositive certified lower input")
        mant,ex=np.frexp(v)
        idx=(mant*(2**bins)).astype(np.int64)
        if not lower:idx+=1
        hist+=np.bincount(idx.ravel(),minlength=len(hist))
        esum+=int(ex.sum());total+=v.size
    out=arb(0)
    for j,count in enumerate(hist):
        if count:out+=int(count)*arb(j).log()
    out+=(esum-total*bins)*L2
    return out/total,{"uniform_complex_error":err,"smallest_enclosed_input":small,"points":total,"log_bin_bits":bins}

if __name__=="__main__":
    import argparse
    pa=argparse.ArgumentParser();pa.add_argument("--n",type=int,default=16);args=pa.parse_args()
    n=args.n
    offsets=[(F(1,37),F(1,41)),(F(2,43),F(3,47)),(F(3,53),F(5,59))]
    Bs=[basis(4,n,off) for off in offsets]
    put("Certified level-four grid bases.")
    kl,kmeta=mean_log_contract(C4,Bs,True)
    Klower=kl-4*L2-6*L2/n**2
    put("Completed finite grid lower logarithms.")
    Gs=grams(n)
    CD=np.empty((4,4,4),object)
    for r in itertools.product(range(2),repeat=3):
        for s in itertools.product(range(2),repeat=3):
            CD[tuple(2*a+b for a,b in zip(r,s))]=C2[r]*C2[s].conjugate()/arb(2).sqrt()
    hl,hmeta=mean_log_contract(CD,[Gs,Gs,Gs],False)
    Hupper=hl/2
    Ilower=Klower-2*Hupper+arb(7)/2*L2
    Alower=Ilower/7-logT/18-arb(10)/63*L2
    hE=-2*(arb(1)/4).gamma().log()+L2+PI.log()/2
    archchi=arb(37)/18*L2-3*(2*PI).log()-logT/18
    F18lower=3*hE+L2/4-archchi
    finite_b_lower=F18lower/7
    HeightLower=arb(7)/2*(finite_b_lower+Alower)
    vals={"log_abs_T":logT,"K_lower":Klower,"H_upper":Hupper,"I_lower":Ilower,"A_lower":Alower,
          "hE":hE,"finite_order_over18_lower":F18lower,"finite_b_lower":finite_b_lower,"height_lower":HeightLower}
    result={"status":"explicit one-sided analytic bounds with Arb inputs and enclosed floating tensor arithmetic",
            "n":n,"precision_bits":ctx.prec,"bounds":{k:str(v) for k,v in vals.items()},"grid":kmeta,"cells":hmeta,
            "height_lower_rational_test":bool(HeightLower>arb(1)/100)}
    path=Path(__file__).with_name("fermat_theta_certify.json");path.write_text(json.dumps(result,indent=2))
    put(json.dumps(result,indent=2))
