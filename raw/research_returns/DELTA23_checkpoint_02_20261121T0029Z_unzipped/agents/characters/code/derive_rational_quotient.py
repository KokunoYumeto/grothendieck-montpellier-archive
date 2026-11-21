from pathlib import Path
import sympy as s
X,Y=s.symbols('X Y');d=s.sqrt(-3);w=(-1+d)/2
simp=lambda a:s.simplify(s.expand_complex(a)) if False else s.simplify(s.expand(a))
def add(p,q):
 if p is None:return q
 if q is None:return p
 x,y=p;u,v=q
 if simp(x-u)==0:
  if simp(y+v)==0:return None
  m=3*x*x/(2*y)
 else:m=(v-y)/(u-x)
 xx=simp(m*m-x-u); yy=simp(m*(x-xx)-y)
 return xx,yy
P=(s.Integer(2),s.Integer(2)); T=(1-d,2*d)
def alpha(p):
 if p is None:return T
 return add((simp(w*w*p[0]),p[1]),T)
pts=[P]
for j in range(7):pts.append(add(pts[-1],P))
a,b,c,e=s.symbols('a b c e'); L=Y+2*X-2;g=a*X**2+b*X+c+e*Y
rows=[]
rows.append(g.subs({X:2,Y:-2}))
for p in pts[1:4]:
 q=alpha(p)
 row=simp(L.subs({X:q[0],Y:q[1]})*g.subs({X:p[0],Y:p[1]})-L.subs({X:p[0],Y:p[1]})*g.subs({X:q[0],Y:q[1]}))
 row=s.Poly(row,d).as_expr() if False else row
 rows.append(row)
A=s.linear_eq_to_matrix(rows,[a,b,c,e])[0]
print('alpha O,P,T',T,alpha(P),alpha(T))
print('nullspace',A.nullspace())
# Quotient value at -P is tangent derivative ratio.
yprime=s.Rational(3)*2**2/(-4)
Lm=2+yprime;gm=(s.diff(g,X)+s.diff(g,Y)*yprime).subs({X:2,Y:-2})
# Set z=L/g, z(-P)=1; z(2P)=1/4.
rows.append(gm-Lm)
rows.append((g-4*L).subs({X:5,Y:-11}))
sol=s.solve(rows,[a,b,c,e]);print('solution',sol)
g=s.factor(g.subs(sol));print('quotient z=',L/g)
Path('work/agents/characters/records/belyi_quotient_coordinate.txt').write_text('alpha(P)=zeta3^2*P+(1-sqrt(-3),2sqrt(-3))\n'+str(L/g)+'\n')
