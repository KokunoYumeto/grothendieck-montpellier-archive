#!/usr/bin/env python3
"""HD-G15: exact exterior Fourier calculation for the fourfold point-ideal square.
21 November 2026. GPT-6 Astra Pro, inherited effort, /root/g34.
No imports from other certificates. Symbolic identities are over Q(l).
"""
from pathlib import Path
import json
import sympy as S

l=S.Symbol('l')

def clean(p):
    out={}
    for m,c in p.items():
        c=S.cancel(c)
        if c!=0: out[m]=c
    return out

def add(*ps):
    out={}
    for p in ps:
        for m,c in p.items(): out[m]=out.get(m,0)+c
    return clean(out)

def scale(p,c): return clean({m:c*v for m,v in p.items()})
def one(i): return {1<<i:S.Integer(1)}

def mul(p,q):
    out={}
    for m,c in p.items():
        for n,d in q.items():
            if m&n: continue
            inv=sum((n&((1<<i)-1)).bit_count()
                    for i in range(max(m.bit_length(),n.bit_length()))
                    if (m>>i)&1)
            out[m|n]=out.get(m|n,0)+(-1)**inv*c*d
    return clean(out)

def wedge(i,j): return mul(one(i),one(j))
def exp(p,n):
    out={0:S.Integer(1)}
    term=out
    for k in range(1,n+1):
        term=scale(mul(term,p),S.Rational(1,k))
        out=add(out,term)
    return out

def same(p,q):
    diff=add(p,scale(q,-1))
    assert not diff,diff

def integrate_cd(p):
    out={}
    for m,c in p.items():
        if m&12!=12: continue
        new=(m&3)|((m>>2)&12)
        out[new]=out.get(new,0)+c
    return clean(out)

# Input real one-forms a,b,c,d,u,v; output a,b,u,v.
hxy=mul(add(one(0),one(2)),add(one(1),one(3)))
hy=wedge(2,3)
pin=add(wedge(2,5),scale(wedge(3,4),-1))
ab=wedge(0,1); uv=wedge(2,3)
pout=add(wedge(0,3),scale(wedge(1,2),-1))
normalizer=exp(scale(pout,S.Rational(-1,2)),2)
gaussian=integrate_cd(exp(add(scale(hxy,l),scale(hy,l),scale(pin,-1)),3))
point_first=integrate_cd(mul(hxy,exp(add(scale(hy,l),scale(pin,-1)),3)))
point_second=integrate_cd(mul(hy,exp(add(scale(hxy,l),scale(pin,-1)),3)))
both_points=integrate_cd(mul(hxy,hy))
raw_expected=scale(exp(add(scale(ab,l/2),scale(pout,S.Rational(1,2)),
                            scale(uv,-1/(2*l))),2),2*l)
same(gaussian,raw_expected)
same(point_first,exp(add(scale(ab,l),pout),2))
same(point_second,exp(scale(ab,l),2))
same(both_points,ab)
normalized=[mul(normalizer,z)
            for z in (gaussian,point_first,point_second,both_points)]
same(normalized[0],add({0:2*l},scale(ab,l*l),scale(uv,-1),
                          scale(mul(ab,uv),-l/2)))
same(normalized[1],exp(add(scale(ab,l),scale(pout,S.Rational(1,2))),2))
same(normalized[2],exp(add(scale(ab,l),scale(pout,S.Rational(-1,2))),2))
same(normalized[3],ab)

def lift(p,j): return {m<<(4*j):c for m,c in p.items()}

products=[]
for pair in normalized:
    out={0:S.Integer(1)}
    for j in range(4): out=mul(out,lift(pair,j))
    products.append(out)
v=add(products[0],scale(products[1],-1),scale(products[2],-1),products[3])
A=add(*(lift(ab,j) for j in range(4)))
B=add(*(lift(uv,j) for j in range(4)))
P=add(*(lift(pout,j) for j in range(4)))
pieces=[{m:c for m,c in v.items() if m.bit_count()==2*k} for k in range(3)]
r=16*l**4-2
ch1=add(scale(A,8*l**5-2*l),scale(B,-8*l**3))
ch2=add(scale(mul(A,A),2*l**6-l*l),
        scale(mul(A,B),-4*l**4),scale(mul(B,B),2*l*l),
        scale(mul(P,P),S.Rational(-1,4)))
same(pieces[0],{0:r});same(pieces[1],ch1);same(pieces[2],ch2)
C=add(ch2,scale(mul(ch1,ch1),-1/(2*r)))
alpha_mask=sum(12<<(4*j) for j in range(4))
inverted={m:(-1)**((m&alpha_mask).bit_count())*c for m,c in C.items()}
same(C,inverted)

# Whole character at l=0 is obtained from the polynomial per-pair forms.
vzero=clean({m:c.subs(l,0) for m,c in v.items()})
ptA={sum(3<<(4*j) for j in range(4)):S.Integer(1)}
ptB={sum(12<<(4*j) for j in range(4)):S.Integer(1)}
same(vzero,add(ptA,ptB,scale(exp(scale(P,S.Rational(1,2)),8),-1),
               scale(exp(scale(P,S.Rational(-1,2)),8),-1)))

# In holomorphic coordinates z,bar(z),w,bar(w), P=i/2(z bar(w)-bar(z) w).
pc=add(*(lift(scale(add(wedge(0,3),scale(wedge(1,2),-1)),S.I/2),j)
         for j in range(4)))
ac=add(*(lift(scale(wedge(0,1),S.I/2),j) for j in range(4)))
bc=add(*(lift(scale(wedge(2,3),S.I/2),j) for j in range(4)))
witness=(1<<0)|(1<<3)|(1<<4)|(1<<7)
assert mul(pc,pc)[witness]==S.Rational(-1,2)
assert all(p.get(witness,0)==0 for p in (mul(ac,ac),mul(ac,bc),mul(bc,bc)))
assert scale(mul(pc,pc),S.Rational(-1,4))[witness]==S.Rational(1,8)

out={
 'statement':'HD-G15','date':'2026-11-21',
 'who':'GPT-6 Astra Pro; inherited effort; /root/g34',
 'four_one_pair_Fourier_identities':'PASS',
 'whole_four_pair_character_terms':len(v),
 'rank':str(r),
 'ch1_coefficients_Hx_Halpha':['8*l**5-2*l','-8*l**3'],
 'ch2_coefficients_Hx2_HxHalpha_Halpha2_P2':
      ['2*l**6-l**2','-4*l**4','2*l**2','-1/4'],
 'centered_second_character_inversion_invariant':True,
 'l_zero_whole_character':'pt_x+pt_alpha-exp(P/2)-exp(-P/2)',
 'holomorphic_witness_mask':witness,
 'P2_witness_coefficient':'-1/2',
 'centered_second_witness_coefficient':'1/8',
 'whole_character':{str(m):str(c) for m,c in sorted(v.items())},
 'scope':'Exact exterior Fourier and character identities. Ext, trace, ample-square uniqueness and the geometric obstruction are proved separately in the TeX fragment.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('All four exact one-pair Fourier identities PASS.')
print('Whole four-pair character and centered second class PASS; terms:',len(v))
print('Inversion invariance, l=0 specialization and nonzero holomorphic witness1/8 PASS.')
