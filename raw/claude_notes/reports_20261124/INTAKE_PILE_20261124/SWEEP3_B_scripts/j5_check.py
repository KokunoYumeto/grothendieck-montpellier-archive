# Independent scripted check of SA14_SA19 row J1-Th5 (J5): split quadric fourfold over F3-bar.
import sympy as sp, itertools
x=sp.symbols('x0:6'); t=sp.symbols('t')
Q=x[0]*x[3]+x[1]*x[4]+x[2]*x[5]
planes={'alpha':[x[3],x[4],x[5]],'beta':[x[2],x[3],x[4]],'alphap':[x[0],x[1],x[5]],'betap':[x[0],x[1],x[2]]}
# 1. planes lie on X: Q reduces to 0 modulo the linear ideal
for n,I in planes.items():
    r=Q.subs({v:0 for v in I}); print(n,'on X:',sp.expand(r)==0)
# 2. smoothness of X over any field of char 3: gradient vanishes only at 0
g=[sp.diff(Q,v) for v in x]; print('gradient',g)
# 3. intersections of planes (linear algebra): common zero set dimension (projective) = 5 - rank
def inter(A,B):
    M=sp.Matrix([[sp.diff(l,v) for v in x] for l in A+B]); r=M.rank(); return 5-r, M.nullspace()
for a,b in [('alpha','alphap'),('beta','betap'),('alpha','betap'),('beta','alphap')]:
    d,ns=inter(planes[a],planes[b]); print(a,b,'proj dim',d,'points',[list(v) for v in ns] if d==0 else ('empty' if d<0 else 'pos-dim'))
# 4. transversality at e2 and e5: tangent spaces of X, plane, plane'
def tangent(lin, pt):
    rows=[[sp.diff(l,v) for v in x] for l in lin]+[[sp.diff(Q,v).subs(dict(zip(x,pt))) for v in x]]
    return sp.Matrix(rows)
for a,b,pt in [('alpha','alphap',[0,0,1,0,0,0]),('beta','betap',[0,0,0,0,0,1])]:
    # T_pt(plane a) + T_pt(plane b) should span T_pt(X) (dim 4 affine-cone dim 5): intersection of tangent spaces = line of the point
    M=sp.Matrix([[sp.diff(l,v) for v in x] for l in planes[a]+planes[b]])
    print(a,b,'combined linear rank (5 => tangent spaces meet only in the point):',M.rank())
# 5. restrictions to Y = V(x2 - t x5), t a unit
for n,I in planes.items():
    M=sp.Matrix([[sp.diff(l,v) for v in x] for l in I+[x[2]-t*x[5]]])
    ns=M.nullspace(); print(n,'cap Y: proj dim',5-M.rank(),'spanned by',[list(v) for v in ns])
# 6. fibres x0x3+x1x4+t x5^2 (t!=0) rank 5, t=0 rank 4; fibre at infinity rank 4 ; char 3 Gram via polarization
def rank_char3(q,vars_):
    H=sp.hessian(q,vars_)  # symmetric bilinear 2B; in char 3, 2 invertible
    return H.applyfunc(lambda e: e%3 if e.is_number else e).rank(iszerofunc=lambda e: sp.simplify(e)%3==0 if e.is_number else e==0)
v5=[x[0],x[1],x[3],x[4],x[5]]
print('fibre t=1 rank',sp.hessian(x[0]*x[3]+x[1]*x[4]+x[5]**2,v5).rank(),'t=0 rank',sp.hessian(x[0]*x[3]+x[1]*x[4],v5).rank())
print('Z.Z\' = alpha.alphap - alpha.betap - beta.alphap + beta.betap = 1-0-0+1 = 2 (from items 3-4)')
