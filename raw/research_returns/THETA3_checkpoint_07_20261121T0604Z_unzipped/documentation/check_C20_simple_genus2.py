"""Exact exploratory certificate for a genus-two factor in the C16 tower."""
import sympy as s
x,T=s.symbols('x T'); A=-30; B=-25
c=x**3+A*x+B
phi=x**4-60*x*x-100*x-300
psi3=3*phi
f4=x**6+5*A*x**4+20*B*x**3-5*A*A*x*x-4*A*B*x-8*B*B-A**3
psi5=s.expand(32*c*c*f4-psi3**3)
psi7=s.expand(psi5*psi3**3-128*c*c*f4**3)
print('psi7=',psi7)
print('psi7 irreducible Q:',s.Poly(psi7,x).is_irreducible)
print('psi7 integer content:',s.Poly(psi7,x).content())

def pointcount(p,a,degree):
    if degree==1:
        return p+1+sum(0 if (v:=((z-a)*(z**4-60*z*z-100*z-300))%p)==0 else 1 if pow(v,(p-1)//2,p)==1 else -1 for z in range(p))
    d=next(k for k in range(2,p) if pow(k,(p-1)//2,p)==p-1)
    def add(u,v):return ((u[0]+v[0])%p,(u[1]+v[1])%p)
    def mul(u,v):return ((u[0]*v[0]+d*u[1]*v[1])%p,(u[0]*v[1]+u[1]*v[0])%p)
    coeffs=[1,-a,-60,60*a-100,100*a-300,300*a]
    total=0
    for v in range(p):
        for u in range(p):
            z=(u,v); val=(0,0)
            for co in coeffs: val=add(mul(val,z),(co,0))
            norm=(val[0]**2-d*val[1]**2)%p
            total += 0 if norm==0 else 1 if pow(norm,(p-1)//2,p)==1 else -1
    return p*p+1+total

for p in [37,47,107,113,149,157,197]:
    poly=s.Poly(psi7,x,modulus=p)
    roots=[a for a in range(p) if poly.eval(a)%p==0]
    print('prime',p,'roots',roots)
    for a in roots:
        if int(phi.subs(x,a))%p==0:continue
        n1=pointcount(p,a,1);n2=pointcount(p,a,2)
        a1=p+1-n1;a2=(n2-p*p-1+a1*a1)//2
        f=T**4-a1*T**3+a2*T*T-p*a1*T+p*p
        disc=s.discriminant(f,T)
        delta=a1*a1-4*(a2-2*p)
        conditions=[a1==0,a1*a1==p+a2,a1*a1==2*a2,a1*a1==3*a2-3*p]
        print({'p':p,'a':a,'N1':n1,'N2':n2,'a1':a1,'a2':a2,'Frob':str(f),'irreducible':s.Poly(f,T).is_irreducible,'ordinary':a2%p!=0,'HZ_exceptions':conditions,'disc':disc,'real_delta':delta,'real_disc_squarefree':s.ntheory.factor_.core(delta,2)})
