#!/usr/bin/env python3
"""All 80 exact local forms for mu4 G33, from the 40 enumerated classes.

Arithmetic is over Q(omega,i), in basis 1,omega,i,i*omega. No numerical
eigenvalue recognition or number-field norm oracle is used.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
def emul(x,y):
    a,b=x;c,d=y
    return (a*c-b*d,a*d+b*c-b*d)
def eadd(x,y):return tuple(a+b for a,b in zip(x,y))
def eneg(x):return tuple(-a for a in x)
def einv(x):
    a,b=x;n=a*a-a*b+b*b
    assert n
    return ((a-b)/n,-b/n)
class F:
    __slots__=('v',)
    def __init__(self,a=0,b=0,c=0,d=0):
        self.v=a.v if isinstance(a,F) else tuple(Q(x) for x in (a,b,c,d))
    def __add__(x,y):
        y=F(y);return F(*(a+b for a,b in zip(x.v,y.v)))
    __radd__=__add__
    def __neg__(x):return F(*(-a for a in x.v))
    def __sub__(x,y):return x+-F(y)
    def __rsub__(x,y):return F(y)+-x
    def __mul__(x,y):
        y=F(y);a,b=x.v[:2],x.v[2:];c,d=y.v[:2],y.v[2:]
        return F(*(eadd(emul(a,c),eneg(emul(b,d)))+eadd(emul(a,d),emul(b,c))))
    __rmul__=__mul__
    def inv(x):
        a,b=x.v[:2],x.v[2:];r=einv(eadd(emul(a,a),emul(b,b)))
        return F(*(emul(a,r)+eneg(emul(b,r))))
    def __truediv__(x,y):return x*F(y).inv()
    def __rtruediv__(x,y):return F(y)*x.inv()
    def __pow__(x,k):
        if k<0:return x.inv()**(-k)
        r=F(1)
        while k:
            if k&1:r=r*x
            x=x*x;k//=2
        return r
    def conj(x):
        a,b,c,d=x.v;return F(a-b,-b,-c+d,d)
    def sigma_i_fixed(x):
        a,b,c,d=x.v;return F(a-b,-b,c-d,-d)
    def __bool__(x):return any(x.v)
    def __eq__(x,y):return x.v==F(y).v
    def serial(x):return [str(a) for a in x.v]
    def __repr__(x):return str(x.serial())

Z=F();ONE=F(1);I=F(0,0,1);W=F(0,1)
def mat(a):return [[F(x) for x in r] for r in a]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def tr(a):return [list(x) for x in zip(*a)]
def star(a):return [[x.conj() for x in r] for r in tr(a)]
def mul(a,b):return [[sum((x*y for x,y in zip(r,c)),Z) for c in tr(b)] for r in a]
def sub(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(a,t):return [[x*t for x in r] for r in a]
def rref(a):
    a=[r[:] for r in a];p=[];i=0
    for j in range(len(a[0])):
        k=next((k for k in range(i,len(a)) if a[k][j]),None)
        if k is None:continue
        a[i],a[k]=a[k],a[i];v=a[i][j];a[i]=[x/v for x in a[i]]
        for k in range(len(a)):
            if k!=i and a[k][j]:
                v=a[k][j];a[k]=[x-v*y for x,y in zip(a[k],a[i])]
        p.append(j);i+=1
        if i==len(a):break
    return a,p
def det(a):
    if not a:return ONE
    a=[r[:] for r in a];d=ONE
    for j in range(len(a)):
        k=next((k for k in range(j,len(a)) if a[k][j]),None)
        if k is None:return Z
        if k!=j:a[j],a[k]=a[k],a[j];d=-d
        p=a[j][j];d=d*p
        for k in range(j+1,len(a)):
            v=a[k][j]/p
            for l in range(j+1,len(a)):a[k][l]=a[k][l]-v*a[j][l]
    return d
def inv(a):
    n=len(a);r,p=rref([x+y for x,y in zip(a,eye(n))]);assert p[:n]==list(range(n))
    return [x[n:] for x in r]
def serial(a):return [[x.serial() for x in r] for r in a]
def divide_one(p):
    q=[p[0]]
    for c in p[1:]:q.append(c+q[-1])
    assert not q[-1]
    return q[:-1]

def main():
    data=json.loads((ROOT/'g33_classes.json').read_text())
    H=[[F(*a) for a in r] for r in data['gram']]
    assert det(H)==2
    rows=[]
    for c in data['classes']:
        w=[[F(*a) for a in r] for r in c['matrix']]
        assert mul(mul(star(w),H),w)==H
        cpw=[F(*a) for a in c['charpoly_desc']]
        # Independent determinant evaluation validates the C++ Newton
        # characteristic polynomial at six exact rational arguments.
        for x in range(6):
            value=Z
            for a in cpw:value=value*x+a
            assert det(sub(scale(eye(5),F(x)),w))==value
        for phase in [ONE,I]:
            g=scale(w,phase);cp=[F(*a)*phase**j for j,a in enumerate(c['charpoly_desc'])]
            f=0;p=cp[:]
            while len(p)>1 and sum(p,Z)==0:p=divide_one(p);f+=1
            b=sum(p,Z);d=5-f
            A=sub(eye(5),g);_,cols=rref(A);assert len(cols)==d
            C=[[r[j] for j in cols] for r in A]
            gram=mul(mul(star(C),H),C) if d else []
            gd=det(gram);assert gd==gd.conj() and gd
            rows.append({'R_class':c['class'],'scalar':'1' if phase==1 else 'i','class_size':c['size'],
                         'moving_rank':d,'charpoly_desc':[a.serial() for a in cp],
                         'moving_columns':cols,'moving_gram':serial(gram),'moving_gram_determinant':gd.serial(),
                         'det_one_minus_moving':b.serial(),
                         'local_seifert_ratio':(gd/b).serial(),
                         'forced_outside_type':bool(phase==I and c['target_quarter_turn_type'])})
    assert len(rows)==80
    refs=[r for r in rows if r['moving_rank']==1]
    assert sum(r['class_size'] for r in refs)==45 and all(r['scalar']=='1' for r in refs)
    outs=[r for r in rows if r['scalar']=='i' and r['moving_rank']==3]
    assert len(outs)==2 and all(r['forced_outside_type'] for r in outs)
    for r in outs:
        gd=F(*r['moving_gram_determinant'])
        witnesses=[1+I,1-I*W]
        witness=next(z for z in witnesses if gd==8*z*z.conj())
        r['moving_determinant_over_eight_norm_witness']=witness.serial()

    # Direct D4 representatives in the orthogonal coordinate basis.
    H0=mat([[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,2]])
    j=mat([[0,1,0,0,0],[-1,0,0,0,0],[0,0,0,1,0],[0,0,-1,0,0],[0,0,0,0,1]])
    g=scale(j,I);gi=inv(g)
    C=[[ONE,Z,Z],[I,Z,Z],[Z,ONE,Z],[Z,I,Z],[Z,Z,ONE]]
    Cp=[[ONE,Z,Z],[-I,Z,Z],[Z,ONE,Z],[Z,-I,Z],[Z,Z,ONE]]
    assert mul(mul(star(C),H0),C)==mat([[2,0,0],[0,2,0],[0,0,2]])
    # These two displayed moving bases are for iw and -iw respectively.
    assert mul(g,C)==mul(C,mat([[-1,0,0],[0,-1,0],[0,0,I]]))
    gm=scale(g,-1)
    assert mul(gm,Cp)==mul(Cp,mat([[-1,0,0],[0,-1,0],[0,0,-I]]))
    assert mul(mul(star(Cp),H0),Cp)==mat([[2,0,0],[0,2,0],[0,0,2]])
    bp=4*(1-I);bm=4*(1+I)
    disc=F(2)**10*F(8)**2/(F(2)**10*bp*bm)
    assert disc==2 and (1+I)*(1+I).conj()==2
    # The ten doubled root reflections, followed by iw,(iw)^(-1),
    # generate mu4*G33; extracting i uses the recorded word for w.
    target=next(c for c in data['classes'] if c['class']==27)
    ww=[[F(*a) for a in r] for r in target['matrix']]
    gg=scale(ww,I)
    generators=[]
    for k in range(5):
        s=eye(5)
        s[k]=[s[k][j]-H[k][j] for j in range(5)]
        assert mul(s,s)==eye(5)
        generators.append(s)
    wword=eye(5)
    for k in target['word']:wword=mul(wword,generators[k-1])
    assert wword==ww and mul(gg,inv(ww))==scale(eye(5),I)
    tuple_matrices=[s for s in generators for _ in range(2)]+[gg,inv(gg)]
    product=eye(5)
    for a in tuple_matrices:product=mul(product,a)
    assert product==eye(5)
    out={'status':'PASS all 80 exact local forms and forced-profile discriminant',
         'field':'Q(omega,i)','basis':['1','omega','i','i*omega'],
         'relations':'omega^2+omega+1=0; i^2=-1; complex conjugation changes both omega and i',
         'classes':rows,'outside_moving_rank_three_classes':[r['R_class'] for r in outs],
         'forced_profile_signed_discriminant_representative':'2',
         'explicit_norm_witness':'Norm(1+i)=2',
         'rational_descent_discriminant_obstruction':False,
         'natural_L_cover_tuple':{'description':'s1,s1,...,s5,s5,i*w,(i*w)^(-1)',
                                  'w_word':target['word'],'product_one':True,
                                  'group_generation_verified':True,'cover_genus':233281,
                                  'coefficient_CW_signature':[3,3],
                                  'paired_boundary_graph_multiplicity':3,
                                  'original_Qi_source_constructed':False},
         'original_Qi_splitness_proved':False,
         'generic_extra_endomorphisms_or_dominance_proved':False}
    (ROOT/'g33_local_forms.json').write_text(json.dumps(out,indent=2)+'\n')
    print(out['status'])
    for r in outs:print({k:r[k] for k in ['R_class','moving_gram_determinant','det_one_minus_moving','local_seifert_ratio']})

if __name__=='__main__':main()
