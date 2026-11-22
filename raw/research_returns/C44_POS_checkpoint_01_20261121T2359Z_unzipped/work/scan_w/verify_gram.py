"""Exact algebra checks for C44-W02/W03 and C44-S03; not a proof checker."""
from pathlib import Path
import json
import sympy as S

d, s, q, delta, b1, b2 = S.symbols('d s q delta b1 b2')
H = 4*q*q-s*s
G = d*S.Matrix([[1,s/2],[s/2,q*q]])
num = S.Matrix([4*q*q*b1-2*s*b2,4*b2-2*s*b1])
assert S.simplify(G.det()-d*d*H/4) == 0
assert (G*num-d*H*S.Matrix([b1,b2])).applyfunc(S.simplify) == S.zeros(2,1)
assert S.simplify(G.inv()[0,0]-4*q*q/(d*H)) == 0
assert S.simplify(G.inv()[1,1]-4/(d*H)) == 0

t=S.symbols('t')
examples=[]
for n in (1,2,3):
    a=2+S.I
    ab=2-S.I
    f=S.Poly(S.expand((t-a**(2*n))*(t-ab**(2*n))),t)
    g=S.Poly(S.expand(S.prod(t-a**j*ab**(2*n-j) for j in range(1,2*n))),t)
    result=int(S.resultant(f,g,t))
    R=abs(result)
    vv=S.Poly(S.invert(g,f)*R,t)
    pp=vv*g
    uu=S.div(S.Poly(R,t)-pp,f)[0]
    assert S.expand((uu*f+vv*g).as_expr()-R)==0
    assert all(c.q == 1 for c in pp.all_coeffs())
    kappa=sum(abs(int(coeff))*5**(power[0]*n) for power,coeff in pp.terms())
    ss=int(S.expand(a**(2*n)+ab**(2*n)))
    qq=5**n
    hh=4*qq*qq-ss*ss
    assert hh>0
    for j in range(2*n+1):
        lam=S.expand(a**j*ab**(2*n-j))
        value=S.simplify(pp.eval(lam))
        assert value == (R if j in (0,2*n) else 0)
    examples.append({'n':n,'K':'Q(i)','a':'2+i','R':R,'kappa':kappa,'q':qq,'s':ss,'H':hh,
                     'f':str(f.as_expr()),'g':str(g.as_expr()),'projector_numerator':str(pp.as_expr())})

# Truncated two-variable intersection ring: primitive vector has alternating
# coefficients and its middle square has d+1 surviving terms of sign (-1)^d.
square_examples=[]
for dim in (2,4,6,8,10):
    coeff=[(-1)**i for i in range(dim+1)]
    assert all(coeff[i]+coeff[i-1]==0 for i in range(1,dim+1))
    norm=sum(coeff[i]*coeff[dim-i] for i in range(dim+1))
    assert norm==dim+1
    square_examples.append({'dimension_X':dim,'primitive_w_square_over_N_squared':norm})

# Concrete bad-order example: E:y^2=x^3-x over F_5 has Frobenius trace -2,
# hence is ordinary; K=Q(i), norm(-1+2i)=5.
points=[(x,y) for x in range(5) for y in range(5) if (y*y-x*x*x+x)%5==0]
assert len(points)+1==8
bad_order={'field':5,'equation':'y^2=x^3-x','number_of_points':8,'frobenius_trace':-2,
           'ordinary':True,'CM_field':'Q(i)','order':'Z+5 Z[i]'}
out={'status':'all_exact_checks_passed','symbolic_checks':['Gram determinant','integer clearing identity','dual-basis norm factors'],
     'projector_examples':examples,'fermat_square_examples':square_examples,'bad_order_example':bad_order,
     'scope':'Exact arithmetic identities only; geometric and positivity proofs require mathematical reading.'}
Path(__file__).with_name('verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
