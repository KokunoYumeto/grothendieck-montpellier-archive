"""Exact symbolic checks for AR-19; no p-adic evaluation is assumed."""
import sympy as s
x,y,F=s.symbols('x y F')
def D(g):
    return s.diff(g,F)*(-x)+s.diff(g,x)*2*y+s.diff(g,y)*(3*x*x+1)
expr=-F*(2*x*x+1)-y*(F*F+x)
assert s.expand(D(D((F**3-3*F*x-2*y)/6))-expr)==0
i=s.I;t=s.sqrt(2);vals=[]
pts=[]
for e in (1,-1):
    X=i*(1+e*t);Y=(1+e*t)*(1-i)
    assert s.simplify(Y**2-X**3-X)==0
    slope=(3*X**2+1)/(2*Y)
    XX=s.simplify(slope**2-2*X)
    YY=s.simplify(slope*(X-XX)-Y)
    assert XX==i and YY==0
    FF=-(3*X**2+1)/(4*Y)
    val=s.simplify(expr.subs({x:X,y:Y,F:FF}))
    assert s.simplify(val+(1+i)/4)==0
    vals.append(val);pts.append((X,Y))
X,Y=pts[0];sl=s.simplify(Y/(X+i))
XX=s.simplify(sl**2-X+i);YY=s.simplify(sl*(X-XX)-Y)
assert s.simplify(XX-pts[1][0])==0 and s.simplify(YY-pts[1][1])==0
print('E(P+) = E(P-) =', vals[0])
print('Sum =', s.simplify(sum(vals)))
print('Full moment / Omega_p^5 =',s.simplify(2*16**2*sum(vals)))
print('Residues of coefficient at i=2,3 mod5:', [(-256*(1+j))%5 for j in (2,3)])
print('All exact checks PASS')
