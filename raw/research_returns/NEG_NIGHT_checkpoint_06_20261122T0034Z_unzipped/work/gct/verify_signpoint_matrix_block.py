"""Exact check of the split M_2 block at q=-1.
The input is the supplied integral structure-constant table.  Matrix products,
the correction by Sigma/4, and trace Gram matrix are independently constructed.
"""
from fractions import Fraction as F
from pathlib import Path
import itertools, json
import sympy as sp

v=sp.Symbol('v')
rows=json.loads(Path('sources/OURS_E4_scripts/e3_constants.json').read_text())
tab={}
for r in rows:
    c=sp.cancel(sp.sympify(r['c'],locals={'v':v}).subs(v,sp.I))
    tab[r['b'],r['bp'],r['bpp']]=F(int(c.p),int(c.q))
names=sorted({b for key in tab for b in key})
def add(a,b):
    out=dict(a)
    for z,c in b.items():out[z]=out.get(z,F(0))+c
    return {z:c for z,c in out.items() if c}
def scale(a,c):return {z:x*c for z,x in a.items() if x*c}
def mul(a,b):
    out={}
    for x,c in a.items():
        for y,d in b.items():
            for z in names:
                if (x,y,z) in tab:out[z]=out.get(z,F(0))+c*d*tab[x,y,z]
    return {z:c for z,c in out.items() if c}
words=['1','12','21','2']
beta={x:{'g2_'+x:F(1),**({'Sigma':F(1,4)} if len(x)==1 else {})} for x in words}
mat={'1':sp.Matrix([[0,8],[0,0]]),'12':sp.Matrix([[16,0],[0,0]]),
     '21':sp.Matrix([[0,0],[0,16]]),'2':sp.Matrix([[0,0],[8,0]])}
result=[]
for x,y in itertools.product(words,repeat=2):
    p=mul(beta[x],beta[y])
    out={z:p.get('g2_'+z,F(0)) for z in words}
    back={}
    for z,c in out.items():back=add(back,scale(beta[z],c))
    assert back==p,(x,y,p,back)
    matrix=sum((sp.Rational(c.numerator,c.denominator)*mat[z] for z,c in out.items()),sp.zeros(2))
    assert matrix==mat[x]*mat[y],(x,y)
    result.append({'x':x,'y':y,'coefficients':{z:str(c) for z,c in out.items() if c}})
sigma={'Sigma':F(1)}
assert not mul(sigma,sigma)
for b in beta.values():assert not mul(sigma,b) and not mul(b,sigma)
gram=[[int(sp.trace(mat[x]*mat[y])) for y in words] for x in words]
cert={'specialization':'q=-1; D=0','basis_words':words,
      'correction':'beta_1=gamma_1+Sigma/4; beta_2=gamma_2+Sigma/4; beta_12=gamma_12; beta_21=gamma_21',
      'products_checked':16,'Sigma_annihilates_block':True,'Sigma_square_zero':True,
      'matrix_images':{x:[list(mat[x].row(i)) for i in range(2)] for x in words},
      'Gram_for_matrix_trace':gram,'products':result}
Path('work/gct/signpoint_matrix_certificate.json').write_text(json.dumps(cert,indent=2,default=int))
print(json.dumps({k:v for k,v in cert.items() if k not in ['products','matrix_images']},indent=2))
