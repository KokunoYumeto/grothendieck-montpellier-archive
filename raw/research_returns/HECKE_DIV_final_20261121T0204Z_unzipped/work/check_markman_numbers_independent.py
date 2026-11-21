"""Independent rational-polynomial audit of M9/M10, without SymPy.

GRR coefficients are expanded by multinomial counting. Intersections are read
from the four nonzero monomials of (bc-e^2)^3, with all factorials explicit.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial, comb
import json

root=Path(__file__).parent
claimed=json.loads((root/'markman_output_numbers.json').read_text())

def clean(p):
    return {m:c for m,c in p.items() if c}
def add(*ps):
    out={}
    for p in ps:
        for m,c in p.items(): out[m]=out.get(m,F(0))+c
    return clean(out)
def scale(p,c): return clean({m:v*c for m,v in p.items()})
def mul(p,q):
    out={}
    for a,c in p.items():
        for b,d in q.items():
            m=tuple(x+y for x,y in zip(a,b))
            out[m]=out.get(m,F(0))+c*d
    return clean(out)
def power(p,n):
    out={(0,0,0):F(1)}
    for _ in range(n): out=mul(out,p)
    return out
def integral(p):
    out=F(0)
    for (i,j,k),c in p.items():
        assert i+j+k==6
        if k%2==0 and i==j==3-k//2 and 0<=k//2<=3:
            r=k//2
            out+=c*(-1)**r*comb(3,r)*factorial(i)*factorial(j)*factorial(k)
    return out

input_coefficients=[1,1,-6,-2]
ch=[]
for k in range(4):
    out={}
    for ix in range(k+1):
        for ip in range(k-ix+1):
            iy=k-ix-ip
            coefficient=F((-1)**(iy+k+1),factorial(ix)*factorial(ip)*factorial(iy))
            for j in range(4-k):
                upower=ix+j
                vpower=ix+ip+3-k-j
                if max(upower,vpower)>3: continue
                c=coefficient*comb(3-k,j)*input_coefficients[upower]*input_coefficients[vpower]
                c*=factorial(upower)*factorial(vpower)
                monomial=(ix,iy,ip)
                out[monomial]=out.get(monomial,F(0))+c
    ch.append(clean(out))

expected=[
    {(0,0,0):F(96)},
    {(1,0,0):F(264),(0,1,0):F(22),(0,0,1):F(-48)},
    {(0,0,2):F(12),(1,0,1):F(-132),(0,1,1):F(-11),(2,0,0):F(-144),(1,1,0):F(-24),(0,2,0):F(-1)},
    {(0,0,3):F(-2),(1,0,2):F(-6),(0,1,2):F(6),(2,0,1):F(72),(1,1,1):F(12),(0,2,1):F(1,2),(3,0,0):F(24),(2,1,0):F(-72),(1,2,0):F(1,2),(0,3,0):F(-1,6)},
]
assert ch==expected
r=96
kappa2=add(ch[2],scale(power(ch[1],2),F(-1,2*r)))
kappa3=add(ch[3],scale(mul(ch[1],ch[2]),F(-1,r)),scale(power(ch[1],3),F(1,3*r*r)))
h0={(1,0,0):F(12),(0,1,0):F(1)}
assert kappa2==scale(power(h0,2),F(-169,48))
expected_k3=scale({(1,0,2):F(-10368),(0,1,2):F(864),(3,0,0):F(288576),(2,1,0):F(51408),(1,2,0):F(6012),(0,3,0):F(119)},F(13,3456))
assert kappa3==expected_k3
h=scale(h0,3)
h6=integral(power(h,6))
c2=scale(kappa2,-r**4)
c3=scale(kappa3,2*r**6)
hc2=integral(mul(power(h,4),c2))
hc3=integral(mul(power(h,3),c3))
delta=h6/factorial(6)
R=112*r*r*2+r*12+6
Dminus=(r-2)*R*hc2+F(r*(r-1)*(r-2),2)*R**3*h6
Dplus=Dminus+hc3
assert all(z.denominator==1 for z in [h6,hc2,hc3,delta,Dminus,Dplus])
M=4*16**6*int(delta)
Dprincipal=16**3*M**6*int(Dplus)
delta3=1701760099946011389900
B3=6493952361560098735300
H3=max(1,delta3**2*Dprincipal**2//648)
numbers={
    'normalized_regularity':R,
    'h_six':int(h6),
    'polarization_delta':int(delta),
    'h_four_c2_normalized':int(hc2),
    'h_three_c3_normalized':int(hc3),
    'negative_cycle_degree':int(Dminus),
    'positive_cycle_degree':int(Dplus),
    'D6_source':int(Dplus),
    'principal_comparison_M':M,
    'D6_principal':Dprincipal,
    'n3_lattice_height_cap_H3':H3,
    'fourfold_multiplier_coefficient_of_q':1080*H3,
    'fourfold_degree_coefficient_of_abs_a_plus_abs_b':3240*H3*B3*Dprincipal,
}
for key,value in numbers.items(): assert claimed[key]==value,(key,claimed[key],value)
result={
    'method':'Independent Fraction polynomial dictionaries and multinomial GRR expansion; no symbolic algebra package',
    'character_and_kappa_polynomials_agree':True,
    'intersection_nonzero_exponents':'(i,j,k)=(3-r,3-r,2r), integral=(-1)^r binom(3,r)i!j!k!',
    'all_numbers_match':True,
    'numbers':numbers,
}
(root/'markman_numbers_independent_check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:numbers[k] for k in ['normalized_regularity','h_six','D6_source','principal_comparison_M']},indent=2))
print('All character coefficients, kappa coefficients, intersections, and transport numbers match.')
